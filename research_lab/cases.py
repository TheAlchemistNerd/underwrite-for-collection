"""A deliberately bounded, deterministic credit operating case. Standard library only.

Cash computations use Decimal. Interest uses ACT/360; discounted scenario values
use effective ACT/365. No amounts are rounded before the reporting boundary.
This is neither a fitted credit model nor a production accounting/servicing engine.
"""
from __future__ import annotations
from copy import deepcopy
from datetime import date, timedelta
from decimal import Decimal, getcontext
import json
from pathlib import Path

getcontext().prec = 40
D = Decimal
ZERO = D(0)
ONE = D(1)


def load_inputs(path=None):
    raw = json.loads(Path(path or Path(__file__).with_name("case_inputs.json")).read_text(encoding="utf-8"))
    def convert(v):
        if isinstance(v, dict):
            return {k: convert(x) for k, x in v.items()}
        if isinstance(v, str):
            try:
                return D(v)
            except Exception:
                pass
        return v
    result = convert(raw)
    validate(result)
    return result


def validate(c):
    l, cr, r, p = c["loan"], c["credit"], c["revolver"], c["pool"]
    if l["term_days"] != 60 or l["delayed_receipt_day"] != 90 or l["day_basis"] != 360:
        raise ValueError("The teaching event graph fixes term=60, delay=90 and ACT/360.")
    if cr["recovery_day"] != 180 or c["protection"]["payment_day"] != 240:
        raise ValueError("The case event graph fixes recovery=180 and protection payment=240.")
    def nonnegative(v):
        if isinstance(v, dict):
            for x in v.values(): nonnegative(x)
        elif isinstance(v, (D, int)) and v < 0:
            raise ValueError("Negative case assumptions are not supported.")
    nonnegative(c)
    for v in [cr["default_probability"], cr["late_nondefault_probability"], cr["gross_recovery_fraction"],
              cr["workout_cost_fraction"], cr["weakened_gross_recovery_fraction"], r["stress_ccf"],
              c["protection"]["share_of_unrecovered_principal"]]:
        if not ZERO <= v <= ONE: raise ValueError("Probability/fraction outside [0,1].")
    if cr["default_probability"] + cr["late_nondefault_probability"] > ONE:
        raise ValueError("Scenario probabilities exceed one.")
    if min(l["principal"], l["capital_ratio"]) <= 0: raise ValueError("Positive principal and capital required.")
    if r["limit"] < l["principal"] + r["second_draw_day_30"]: raise ValueError("Draw exceeds commitment.")
    if not 0 < p["first_batch_count"] < p["loan_count"]: raise ValueError("Two nonempty pool batches required.")
    if p["class_a"] + p["class_b"] + p["equity"] != p["loan_count"] * l["principal"] + p["reserve"]:
        raise ValueError("SPV opening sources do not equal purchase plus reserve.")
    if c["protection"]["acceptance_day"] > c["protection"]["payment_day"]:
        raise ValueError("Protection cannot pay before acceptance.")


def interest(balance, rate, days):
    return balance * rate * D(days) / D(360)


def pv(amount, rate, days):
    return amount / (ONE + rate) ** (D(days) / D(365))


def borrower(c, mode="on_time"):
    if mode not in ("on_time", "delay_unfinanced", "approved_extension", "revolver"):
        raise ValueError(mode)
    o, l, r = c["operating"], c["loan"], c["revolver"]
    revolving = mode == "revolver"
    due_day = 90 if mode == "approved_extension" else 60
    receipt_day = 90 if mode in ("delay_unfinanced", "approved_extension") else 60
    principal = l["principal"] + (r["second_draw_day_30"] if revolving else ZERO)
    coupon = interest(l["principal"], l["coupon"], due_day)
    if revolving: coupon += interest(r["second_draw_day_30"], l["coupon"], 30)
    average_undrawn = r["limit"] - l["principal"] - r["second_draw_day_30"] / 2
    unused_fee = interest(average_undrawn, r["undrawn_fee_rate"], 60) if revolving else ZERO
    cash, rows = o["opening_cash"], []
    for day in sorted({0, 30, 60, receipt_day, due_day}):
        receipts = o["customer_advance"] if day == 0 else (o["customer_balance"] if day == receipt_day else ZERO)
        draw = l["principal"] if day == 0 else (r["second_draw_day_30"] if revolving and day == 30 else ZERO)
        operating = {0: o["supplier_day_0"], 30: o["payroll_day_30"], 60: o["completion_day_60"]}.get(day, ZERO)
        debt = principal + coupon + unused_fee if day == due_day else ZERO
        fee = l["fee"] if day == 0 else ZERO
        opening = cash
        cash += receipts + draw - operating - debt - fee
        rows.append(dict(day=day, date=(date.fromisoformat(c["valuation_date"]) + timedelta(days=day)).isoformat(),
                         opening=opening, receipts=receipts, draw=draw, operating=operating, debt=debt, fee=fee,
                         closing=cash, financing_needed=max(ZERO, o["cash_floor"] - cash)))
    return dict(rows=rows, closing=cash, minimum=min(x["closing"] for x in rows),
                peak_financing_needed=max(x["financing_needed"] for x in rows),
                finance_cost=coupon + unused_fee + l["fee"],
                terminal_headroom=max(ZERO, cash - o["cash_floor"]),
                operating_surplus=o["customer_advance"] + o["customer_balance"] - sum(o[k] for k in
                    ["supplier_day_0", "payroll_day_30", "completion_day_60"]),
                executable_without_new_finance=all(x["closing"] >= 0 for x in rows))


def pricing(c, mode="term"):
    l, cr, r = c["loan"], c["credit"], c["revolver"]
    days = 90 if mode == "extension" else 60
    avg_drawn, avg_undrawn, ead = l["principal"], ZERO, l["principal"]
    if mode == "revolver":
        avg_drawn += r["second_draw_day_30"] / 2
        avg_undrawn = r["limit"] - avg_drawn
        drawn_at_stress = l["principal"] + r["second_draw_day_30"]
        ead = drawn_at_stress + r["stress_ccf"] * (r["limit"] - drawn_at_stress)
    elif mode not in ("term", "extension"):
        raise ValueError(mode)
    coupon = interest(avg_drawn, l["coupon"], days)
    commitment_fee = interest(avg_undrawn, r["undrawn_fee_rate"], days)
    liquidity_cost = interest(avg_undrawn, r["undrawn_liquidity_cost_rate"], days)
    funding = interest(avg_drawn, l["funding_rate"], days)
    cost = l["operating_cost"] + (l["extension_admin_cost"] if mode == "extension" else ZERO)
    lgd = ONE - cr["gross_recovery_fraction"] + cr["workout_cost_fraction"]
    expected_loss = ead * cr["default_probability"] * lgd
    capital = ead * l["capital_ratio"]
    capital_charge = interest(capital, l["capital_hurdle"], days)
    income = coupon + l["fee"] + commitment_fee
    contribution = income - funding - cost - expected_loss - liquidity_cost
    required_coupon = (funding + cost + expected_loss + liquidity_cost + capital_charge - l["fee"] - commitment_fee) / (avg_drawn * D(days) / 360)
    return dict(days=days, average_drawn=avg_drawn, average_undrawn=avg_undrawn, ead=ead, lgd=lgd,
                coupon=coupon, upfront_fee=l["fee"], commitment_fee=commitment_fee, income=income,
                funding=funding, operating_cost=cost, liquidity_cost=liquidity_cost, expected_loss=expected_loss,
                capital=capital, capital_charge=capital_charge, contribution=contribution,
                economic_profit=contribution-capital_charge, period_raroc=contribution/capital,
                annualised_simple_raroc=contribution/capital*D(360)/days, hurdle_coupon=required_coupon)


def cash_shortfall(c):
    l, cr = c["loan"], c["credit"]
    proceeds = l["principal"] - l["fee"]
    due = l["principal"] + interest(l["principal"], l["coupon"], 60)
    if proceeds <= 0: raise ValueError("Positive net proceeds required for the case EIR.")
    eir = (due / proceeds) ** (D(365)/60) - ONE
    pd, late = cr["default_probability"], cr["late_nondefault_probability"]
    rows = []
    for name, weight, day, amount in [
        ("on_time", ONE-pd-late, 60, due), ("late_same_cash", late, 90, due),
        ("default_gross_receipt", pd, 180, l["principal"] * cr["gross_recovery_fraction"])]:
        discounted = pv(amount, eir, day)
        rows.append(dict(name=name, weight=weight, day=day, amount=amount, pv=discounted, weighted_pv=weight*discounted))
    expected_pv = sum(x["weighted_pv"] for x in rows)
    expected_cost_pv = pd * pv(l["principal"] * cr["workout_cost_fraction"], eir, 180)
    return dict(net_proceeds=proceeds, due=due, eir=eir, rows=rows, expected_receipts_pv=expected_pv,
                receipt_shortfall=proceeds-expected_pv, separate_workout_cost_pv=expected_cost_pv,
                management_shortfall_with_cost=proceeds-expected_pv+expected_cost_pv,
                late_only_time_loss=proceeds-pv(due,eir,90))


def scenario_profit(c):
    """Undiscounted lifetime cash earnings bridge; distinct from the margin budget.

    Facility is fully funded until final resolution; capital is held until then.
    Default ends in write-off of unrecovered principal at day 180. No further
    interest is collected in default. Upfront fee is retained in all states.
    """
    l,cr=c["loan"],c["credit"]
    pd,late=cr["default_probability"],cr["late_nondefault_probability"]
    coupon=interest(l["principal"],l["coupon"],60)
    rows=[]
    for name,w,day,default in [("on_time",ONE-pd-late,60,False),("late_same_cash",late,90,False),("default",pd,180,True)]:
        recovered=l["principal"]*cr["gross_recovery_fraction"] if default else l["principal"]+coupon
        workout=l["principal"]*cr["workout_cost_fraction"] if default else ZERO
        funding=interest(l["principal"],l["funding_rate"],day)
        contribution=l["fee"]+recovered-l["principal"]-funding-l["operating_cost"]-workout
        charge=interest(l["principal"]*l["capital_ratio"],l["capital_hurdle"],day)
        rows.append(dict(name=name,weight=w,resolution_day=day,receipt=recovered,funding=funding,
                         workout=workout,contribution=contribution,capital_charge=charge,economic_profit=contribution-charge))
    expected=sum(x["weight"]*x["economic_profit"] for x in rows)
    slope=(ONE-pd)*l["principal"]*D(60)/360
    return dict(rows=rows,expected_contribution=sum(x["weight"]*x["contribution"] for x in rows),
                expected_capital_charge=sum(x["weight"]*x["capital_charge"] for x in rows),
                expected_economic_profit=expected,required_coupon=l["coupon"]-expected/slope if slope else None,
                bridge_from_margin_budget=expected-pricing(c)["economic_profit"])


def protection(c):
    l, cr, g = c["loan"], c["credit"], c["protection"]
    principal = l["principal"]
    gross, cost = principal*cr["gross_recovery_fraction"], principal*cr["workout_cost_fraction"]
    guaranteed = min(g["cap"], g["share_of_unrecovered_principal"] * max(ZERO, principal-gross))
    claim_net = guaranteed-g["claim_cost"] if guaranteed else ZERO
    unprotected = pv(gross-cost, cr["recovery_discount_rate"], 120)
    benefit = pv(claim_net, cr["recovery_discount_rate"], 180)
    return dict(gross_recovery=gross, workout_cost=cost, guarantee_payment=guaranteed, claim_net=claim_net,
                unprotected_nrv_at_default=unprotected, protected_nrv_at_default=unprotected+benefit,
                incremental_nrv_at_default=benefit,
                expected_net_benefit_at_day_0=cr["default_probability"]*pv(claim_net,cr["recovery_discount_rate"],240)-g["premium_day_0"],
                weaker_lgd=ONE-cr["weakened_gross_recovery_fraction"]+cr["workout_cost_fraction"],
                weaker_expected_loss=principal*cr["default_probability"]*(ONE-cr["weakened_gross_recovery_fraction"]+cr["workout_cost_fraction"]))


def evidence_state(c, cutoff):
    """Knowledge-time filtration: effective dates never backdate availability."""
    facts = [dict(id="initial", effective=0, known=0, verified=0, fraction=c["credit"]["gross_recovery_fraction"]),
             dict(id="rights_change", effective=20, known=40, verified=45, fraction=c["credit"]["weakened_gross_recovery_fraction"])]
    known = [f for f in facts if f["known"] <= cutoff]
    usable = [f for f in known if f["verified"] <= cutoff]
    selected = max(usable, key=lambda x:x["verified"])
    return dict(cutoff=cutoff, last_verified=selected["verified"], age_days=cutoff-selected["verified"],
                recovery_fraction=selected["fraction"], source_outage=cutoff>=30 and cutoff<45,
                pending_verification=any(f["verified"]>cutoff for f in known))


def replay(events, cutoff):
    """Local workflow demonstration, not an interface to a bank or payment rail."""
    permitted = {"new":{"drafted"}, "drafted":{"reviewed"}, "reviewed":{"approved","rejected"},
                 "approved":{"executed"}, "executed":{"settled","failed"}, "failed":{"executed"},
                 "settled":set(), "rejected":set()}
    state, seen = "new", {}
    for e in sorted((x for x in events if x["known_day"]<=cutoff), key=lambda x:(x["known_day"],x["sequence"])):
        if e["id"] in seen:
            if e != seen[e["id"]]: raise ValueError("Conflicting payload under the same event ID.")
            continue
        if e["state"] not in permitted[state]: raise ValueError("Unapproved or out-of-order state transition.")
        if e["state"] == "settled" and not e.get("bank_reference"):
            raise ValueError("Settlement requires a bank reference in this demonstration.")
        seen[e["id"]] = deepcopy(e)
        state = e["state"]
    return dict(state=state, unique_events=len(seen), available_cash=state=="settled")


def workflow_fixture():
    states = ["drafted","reviewed","approved","executed","failed","executed","settled"]
    return [dict(id=f"remittance-{i}", sequence=i, known_day=50+i, state=s,
                 **({"bank_reference":"SYNTHETIC-SETTLEMENT-1"} if s=="settled" else {})) for i,s in enumerate(states)]


def vintage():
    # 100 original accounts, of which 20 have ever been 90+ DPD.
    rows = []
    groups = [(80,"current",False,False),(5,"90_plus",True,False),(4,"1_to_89",True,False),
              (3,"current",True,True),(3,"current",True,False),(3,"prepaid",True,False),(2,"foreclosed",True,False)]
    for n,state,ever,sustained in groups:
        rows += [dict(state=state,ever90=ever,three_month_current_confirmed=sustained) for _ in range(n)]
    ever=sum(x["ever90"] for x in rows)
    current90=sum(x["state"]=="90_plus" for x in rows)
    active=sum(x["state"] not in ("prepaid","foreclosed") for x in rows)
    return dict(original=len(rows), ever90=ever, current90=current90, active=active,
                difference_same_denominator=ever-current90, currently_current_after90=6,
                confirmed_three_month_current=sum(x["three_month_current_confirmed"] for x in rows),
                followup_incomplete=3, ever_rate=D(ever)/len(rows), current_rate_active=D(current90)/active,
                mixed_denominator_difference=D(ever)/len(rows)-D(current90)/active)


def pool(c, mode="base"):
    """Static two-batch runoff. Transfers at par; no revolving purchases or fair-value claim.

    Normal priority: fees, A interest/principal, B interest/principal, reserve refill,
    equity. Early amortisation pays all principal available in that same seniority;
    reserve then supports fees/interest only; equity is trapped until final runoff.
    """
    if mode not in ("base","delay","default"): raise ValueError(mode)
    p,l,cr=c["pool"],c["loan"],c["credit"]
    principal=l["principal"]
    due=principal+interest(principal,l["coupon"],60)
    n1,n2=p["first_batch_count"],p["loan_count"]-p["first_batch_count"]
    n_default=1 if mode=="default" else 0
    final=180 if n_default else 60
    batches={30: n1-n_default if mode!="delay" else 0,60:n2+(n1 if mode=="delay" else 0)}
    notes={"a":p["class_a"],"b":p["class_b"]}
    note_start=notes.copy()
    interest_due={"a":ZERO,"b":ZERO}
    fees_due=ZERO
    principal_paid={"a":ZERO,"b":ZERO}
    cash,reserve,eligible=ZERO,p["reserve"],principal*p["loan_count"]
    early=False
    rows=[]
    previous=0
    for day in ([30,60,180] if n_default else [30,60]):
        opening_cash, opening_reserve = cash,reserve
        opening_notes=notes.copy()
        # Default information arrives before this period's distribution.
        if day==30 and n_default: eligible-=principal*n_default
        outstanding=notes["a"]+notes["b"]
        oc=eligible/outstanding if outstanding else None
        if oc is not None and oc<p["oc_trigger"]: early=True
        early_at_start=early
        accrual_days=day-previous
        new_fee=p["fee_per_30_days"]*D(accrual_days)/30
        if day==180: new_fee+=principal*cr["workout_cost_fraction"]*n_default
        fees_due+=new_fee
        for k in notes: interest_due[k]+=interest(notes[k],p[f"{k}_coupon"],accrual_days)
        scheduled_count=batches.get(day,0)
        receipts=due*scheduled_count
        if day==180: receipts+=principal*cr["gross_recovery_fraction"]*n_default
        cash+=receipts
        eligible-=principal*scheduled_count
        reserve_draw=ZERO
        payments={}
        def pay(amount, allow_reserve):
            nonlocal cash,reserve,reserve_draw
            if allow_reserve and cash<amount:
                draw=min(reserve,amount-cash)
                cash+=draw; reserve-=draw; reserve_draw+=draw
            payment=min(cash,amount)
            cash-=payment
            return payment
        payments["fees"]=pay(fees_due,True)
        fees_due-=payments["fees"]
        cumulative_schedule=D(n1)/p["loan_count"] if day==30 else ONE
        principal_shortfall=ZERO
        for k in ("a","b"):
            payments[f"{k}_interest"]=pay(interest_due[k],True)
            interest_due[k]-=payments[f"{k}_interest"]
            scheduled=max(ZERO,note_start[k]*cumulative_schedule-principal_paid[k])
            target=notes[k] if early_at_start else min(notes[k],scheduled)
            payments[f"{k}_principal"]=pay(target,not early_at_start)
            notes[k]-=payments[f"{k}_principal"]
            principal_paid[k]+=payments[f"{k}_principal"]
            principal_shortfall+=max(ZERO,scheduled-payments[f"{k}_principal"])
        if principal_shortfall>0 or fees_due>0 or sum(interest_due.values())>0: early=True
        topup=ZERO
        if not early and day!=final:
            topup=min(cash,max(ZERO,p["reserve"]-reserve)); cash-=topup; reserve+=topup
        release=ZERO
        if day==final:
            # Any final reserve first services remaining senior obligations.
            release=reserve; cash+=release; reserve=ZERO
            extra=pay(fees_due,False); payments["fees"]+=extra; fees_due-=extra
            for k in ("a","b"):
                extra=pay(interest_due[k],False); payments[f"{k}_interest"]+=extra; interest_due[k]-=extra
                extra=pay(notes[k],False); payments[f"{k}_principal"]+=extra; notes[k]-=extra; principal_paid[k]+=extra
        equity=ZERO
        if (not early or day==final) and sum(notes.values())+sum(interest_due.values())+fees_due==0:
            equity=cash;cash=ZERO
        elif not early and day!=final:
            equity=cash;cash=ZERO
        residual=cash+reserve-(opening_cash+opening_reserve+receipts-sum(payments.values())-equity)
        rows.append(dict(day=day, opening_cash=opening_cash, opening_reserve=opening_reserve,
                         opening_notes=opening_notes, receipts=receipts, eligible_principal=eligible,
                         oc_before_collections=oc, early_amortisation=early, payments=payments,
                         reserve_draw=reserve_draw, reserve_topup=topup, reserve_release=release,
                         closing_cash=cash, closing_reserve=reserve, closing_notes=notes.copy(),
                         unpaid_interest=interest_due.copy(), fees_due=fees_due, equity=equity,
                         conservation_residual=residual))
        previous=day
    return dict(rows=rows, purchase=principal*p["loan_count"], opening_sources=sum(note_start.values())+p["equity"],
                equity_invested=p["equity"], total_equity_cash=sum(x["equity"] for x in rows),
                equity_profit=sum(x["equity"] for x in rows)-p["equity"], terminal_note_loss=sum(notes.values()),
                total_receipts=sum(x["receipts"] for x in rows), total_fees=sum(x["payments"]["fees"] for x in rows),
                total_note_interest=sum(x["payments"][f"{k}_interest"] for x in rows for k in ("a","b")))


def run(c):
    validate(c)
    return dict(borrower={m:borrower(c,m) for m in ("on_time","delay_unfinanced","approved_extension","revolver")},
                pricing={m:pricing(c,m) for m in ("term","extension","revolver")}, cash_shortfall=cash_shortfall(c),
                scenario_profit=scenario_profit(c), protection=protection(c), evidence=[evidence_state(c,t) for t in (0,35,42,45)],
                workflow=[dict(cutoff=t,**replay(workflow_fixture(),t)) for t in (52,53,54,55,56)],
                vintage=vintage(), pool={m:pool(c,m) for m in ("base","delay","default")})
