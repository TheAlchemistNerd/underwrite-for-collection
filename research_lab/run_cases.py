"""Reproduce results, appendix and delimited chapter exhibits; never replace chapters."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from cases import load_inputs, run

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent


def money(x): return f"{Decimal(x).quantize(Decimal('.01'),rounding=ROUND_HALF_UP):,.2f}"
def pct(x): return f"{Decimal(x)*100:,.3f}%"
def table(head, rows):
    return '\n'.join(['| '+' | '.join(head)+' |','| '+' | '.join('---' for _ in head)+' |']+
                     ['| '+' | '.join(str(c) for c in row)+' |' for row in rows])


def sections(c,r):
    s={}
    b=r['borrower'];p=r['pricing'];cs=r['cash_shortfall'];sp=r['scenario_profit'];g=r['protection']
    s['borrower_base']=table(['Day','Customer cash','Loan draw','Operating paid','Debt paid','Closing cash'],
        [[x['day'],money(x['receipts']),money(x['draw']),money(x['operating']),money(x['debt']),money(x['closing'])] for x in b['on_time']['rows']])
    s['borrower_summary']=table(['Schedule','Minimum cash','Additional cash to floor','Terminal cash','Finance cost'],
        [[k.replace('_',' '),money(v['minimum']),money(v['peak_financing_needed']),money(v['closing']),money(v['finance_cost'])] for k,v in b.items()])
    metrics=[('Income','income'),('Funding cost','funding'),('Operating cost','operating_cost'),('Undrawn liquidity cost','liquidity_cost'),
             ('Default EAD','ead'),('Nominal loss allowance','expected_loss'),('Allocated capital','capital'),('Capital charge','capital_charge'),
             ('Contribution before capital','contribution'),('Economic profit','economic_profit')]
    s['pricing']=table(['KES','60-day term','90-day extension','60-day revolver'],[[label]+[money(p[k][key]) for k in ('term','extension','revolver')] for label,key in metrics])
    s['scenario_profit']=table(['State','Weight','Resolution day','Funding cost','Contribution','Economic profit'],
        [[x['name'].replace('_',' '),pct(x['weight']),x['resolution_day'],money(x['funding']),money(x['contribution']),money(x['economic_profit'])] for x in sp['rows']])
    s['scenario_bridge']=table(['Reconciliation, KES','Amount'],[
        ['Margin-budget economic profit',money(p['term']['economic_profit'])],
        ['Scenario-weighted contribution',money(sp['expected_contribution'])],
        ['Scenario-weighted capital charge',money(sp['expected_capital_charge'])],
        ['Scenario-weighted economic profit',money(sp['expected_economic_profit'])],
        ['Difference from margin budget',money(sp['bridge_from_margin_budget'])]])
    s['scenario_bridge']+='\n\nThe KES 2,024 difference comprises KES 600 expected foregone interest, KES 1,200 additional funding time and KES 224 additional capital time. Contribution is measured before capital; RAROC divides that contribution by allocated capital, and economic profit deducts the capital charge once.'
    s['eir']=f"The solved annual effective rate is **{pct(cs['eir'])}**. It reprices the contractual receipt to KES {money(cs['net_proceeds'])}; the simple annual coupon uses its separately stated ACT/360 convention."
    s['cash_shortfall']=table(['State','Weight','Receipt day','Receipt','Receipt PV','Weighted PV'],
        [[x['name'].replace('_',' '),pct(x['weight']),x['day'],money(x['amount']),money(x['pv']),money(x['weighted_pv'])] for x in cs['rows']])
    s['cash_shortfall_summary']=table(['Measure','KES'],[[label,money(cs[key])] for label,key in [
        ('Contractual net proceeds','net_proceeds'),('Expected gross receipt PV','expected_receipts_pv'),('Receipt shortfall','receipt_shortfall'),
        ('Separate expected workout-cost PV','separate_workout_cost_pv'),('Management comparison including cost','management_shortfall_with_cost'),
        ('PV loss if all cash is 30 days late','late_only_time_loss')]])
    s['protection']=table(['Measure','KES'],[[label,money(g[key])] for label,key in [
        ('Gross recovery at day 180','gross_recovery'),('Workout cost at day 180','workout_cost'),('Guarantee receipt at day 240','guarantee_payment'),
        ('Guarantee net of claim cost','claim_net'),('Unprotected recovery PV at default','unprotected_nrv_at_default'),
        ('Protected recovery PV at default','protected_nrv_at_default'),('Expected incremental value at origination, after premium','expected_net_benefit_at_day_0')]])
    s['evidence']=table(['Cutoff day','Last verified day','Evidence age','Recovery parameter','Outage','Review pending'],
        [[x['cutoff'],x['last_verified'],x['age_days'],pct(x['recovery_fraction']),'Yes' if x['source_outage'] else 'No','Yes' if x['pending_verification'] else 'No'] for x in r['evidence']])
    s['workflow']=table(['Cutoff day','State','Unique events','Receipt available'],
        [[x['cutoff'],x['state'],x['unique_events'],'Yes' if x['available_cash'] else 'No'] for x in r['workflow']])
    v=r['vintage']
    s['vintage']=table(['Population or measure','Count / rate'],[
        ['Original accounts',v['original']],['Active accounts',v['active']],['Ever 90+',v['ever90']],['Currently 90+',v['current90']],
        ['Ever minus current, original denominator',v['difference_same_denominator']],['Currently current after 90+',v['currently_current_after90']],
        ['Confirmed three consecutive current months',v['confirmed_three_month_current']],['Incomplete current follow-up',v['followup_incomplete']],
        ['Ever 90+ / original',pct(v['ever_rate'])],['Current 90+ / active',pct(v['current_rate_active'])]])
    pool=c['pool']
    s['pool_opening']=table(['Opening sources, KES','Amount','Opening uses, KES','Amount'],[
        ['Class A',money(pool['class_a']),'Receivable purchase',money(r['pool']['base']['purchase'])],
        ['Class B',money(pool['class_b']),'Funded reserve',money(pool['reserve'])],
        ['Equity',money(pool['equity']),'Total uses',money(r['pool']['base']['purchase']+pool['reserve'])],
        ['Total sources',money(r['pool']['base']['opening_sources']),'','']])
    s['pool_results']=table(['Pool scenario','Asset receipts','Note interest','Expenses','Equity cash','Equity gain / loss'],
        [[k]+[money(x[key]) for key in ('total_receipts','total_note_interest','total_fees','total_equity_cash','equity_profit')] for k,x in r['pool'].items()])
    parts=[]
    for k,x in r['pool'].items():
        parts.append(f"#### Vehicle {k}: distributions, KES\n\n"+table(['Day','Fees','A interest','A principal','B interest','B principal'],
            [[z['day']]+[money(z['payments'][key]) for key in ('fees','a_interest','a_principal','b_interest','b_principal')] for z in x['rows']]))
        parts.append(table(['Day','Cash held','Reserve held','Equity paid','Early amortisation','Cash residual'],
            [[z['day'],money(z['closing_cash']),money(z['closing_reserve']),money(z['equity']),'Yes' if z['early_amortisation'] else 'No',money(z['conservation_residual'])] for z in x['rows']]))
    s['pool_ledgers']='\n\n'.join(parts)
    return s


def chapter_blocks(r):
    b=r['borrower'];p=r['pricing'];sp=r['scenario_profit']
    suffix='\n\nSee the worked case appendix, U4C-MSME-001, and the [GitHub research lab](https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab) for the declared hypothetical assumptions, full schedules, calculation code, tests and instructions for reproducing both worked cases.'
    texts={
        '1':f"""### Worked operating case: a profitable order can still miss its payment date

The connected example starts with KES 250,000 cash, a KES 200,000 customer advance and KES 500,000 borrowing. The order earns KES 180,000 before finance costs and ends with KES {money(b['on_time']['closing'])} cash when the customer pays on day 60. If the same customer receipt arrives on day 90 but the loan remains due on day 60, the unfinanced forecast reaches KES {money(b['delay_unfinanced']['minimum'])}. Maintaining the KES 100,000 operating floor would require KES {money(b['delay_unfinanced']['peak_financing_needed'])} of additional cash. That amount identifies the additional funding to secure or the payment schedule to renegotiate. Enterprise cash and the specific loan's repayment clock must therefore be tested together. Cash above the operating floor is analytical owner headroom to assess against the enterprise's other obligations and distribution rules.""",
        '2a':"""### Worked evidence case: availability precedes model use

In the connected case, a rights change effective on day 20 first becomes known on day 40 and is verified on day 45. The day-35 forecast uses the evidence known by day 35. A feed outage on day 30 preserves the day-0 verification timestamp and prompts a freshness review. At day 42 the change is known but pending review; the record retains that uncertainty and the last verified parameter. This separation of effective, known and verified dates is exercised by the reproducible fixture. Feed freshness and borrower performance are reviewed as separate evidence dimensions.""",
        '2b':"""### Worked outcome case: distinguish current status, cure and loss

The account-path fixture contains 20 loans that have ever been 90+ days past due: five remain 90+, four are in lesser arrears, six are current, three prepaid and two exited through foreclosure. Only three have enough follow-up to satisfy the illustrative three-consecutive-current-month rule. The 15 accounts that left 90+ comprise several outcomes; the sustained-current count is three under the stated rule. The associated finance case also keeps nominal principal loss, dated recovery cash and discounted contractual shortfall as separate targets. These definitions establish the outcome labels for subsequent hierarchical estimation and intervention evaluation using observed account histories.""",
        '3':f"""### Worked intervention case: change the contract through an accountable decision

Moving the example loan's due date from day 60 to day 90, with 90 days of simple interest, produces minimum borrower cash of KES {money(b['approved_extension']['minimum'])} instead of an unfinanced deficit. The change requires a documented revised schedule, borrower acceptance, authority and execution evidence. This contractual scenario comparison defines the financial outcomes to measure in a subsequent causal evaluation of the policy. Holding PD and recovery fixed solely to isolate timing, the lender's margin-budget economic profit changes from KES {money(p['term']['economic_profit'])} to KES {money(p['extension']['economic_profit'])}. Borrower feasibility and lender value are both part of the decision.""",
        '4':"""### Worked replay case: settlement is an observable state

The companion local fixture replays draft, review, approval, execution, a failed settlement attempt, retry and referenced settlement. Execution requires approval, duplicate IDs must agree, and settlement requires a bank reference; exact repeated events are idempotent. Cash becomes available only in the settled state. The verified transitions provide a basis for institution integration: connect the bank interface, authenticate external references, configure production permissions and reconcile the general ledger.""",
        '5':f"""### Worked finance case: reconcile the budget to the cash paths

For the illustrative KES 500,000 fixed-rate loan, the contractual margin budget produces KES {money(p['term']['economic_profit'])} economic profit at an 18% ACT/360 coupon. Its budget hurdle is 20.04%. A separate scenario-weighted cash-earnings calculation includes foregone interest, late funding and capital time; its economic profit is KES {money(sp['expected_economic_profit'])} and its conditional hurdle coupon is 22.655%. The explicit KES 2,024 reconciliation connects the budget and cash-earnings conventions. Each hurdle is conditional on the stated assumptions; an actual quote adds market evidence, affordability and the applicable benchmark and contract terms.

The revolving alternative earns coupon on KES 550,000 average funded balance while using KES 630,000 conditional default EAD. The cash-shortfall exhibit derives its own EIR and separates receipt timing from workout cost. Protection is valued at its actual assumed payment date. The optional ten-loan pool then allocates the same type of loan receivable through a KES 5.25 million sources-and-uses statement, a funded reserve and a dated waterfall. Its base equity cash is KES {money(r['pool']['base']['total_equity_cash'])}; a timing delay reduces it to KES {money(r['pool']['delay']['total_equity_cash'])} despite unchanged ultimate asset receipts. The vehicle clock, transfer price and contractual priority are stated separately from the bank case."""
    }
    return {k:v+suffix for k,v in texts.items()}


def content():
    c=load_inputs();r=run(c)
    baseline=(HERE/'publication_baseline.sha256').read_text().strip()
    actual=hashlib.sha256((HERE/'case_inputs.json').read_bytes()).hexdigest()
    if baseline!=actual:
        raise SystemExit('Inputs differ from the published prose baseline. Use --results-only for sensitivity runs; revise prose and baseline fingerprint before publishing a changed calibration.')
    appendix=(HERE/'appendix_template.md').read_text(encoding='utf-8')
    for k,v in sections(c,r).items(): appendix=appendix.replace('{{'+k+'}}',v)
    if re.search(r'{{\w+}}',appendix): raise ValueError('Unfilled appendix template token.')
    products={ROOT/'research_lab/results/case_results.json':json.dumps(r,default=str,indent=2,ensure_ascii=False)+'\n',
              ROOT/'series/appendices/WORKED_OPERATING_AND_FINANCE_CASE.md':appendix}
    for label,text in chapter_blocks(r).items():
        matches=list((ROOT/'series/parts').glob('Part_'+label+'_*'))
        if not matches: continue
        if len(matches)!=1: raise ValueError(f'Ambiguous chapter {label}')
        path=matches[0];old=path.read_text(encoding='utf-8')
        start=f'<!-- U4C-CASE-{label}-START -->';end=f'<!-- U4C-CASE-{label}-END -->'
        if start not in old: raise ValueError(f'Missing insertion marker in {path.name}')
        pattern=re.escape(start)+r'.*?'+re.escape(end)
        new,n=re.subn(pattern,lambda _:start+'\n\n'+text+'\n\n'+end,old,flags=re.S)
        if n!=1: raise ValueError(f'Nonunique marker in {path.name}')
        products[path]=new
    source_names=['case_inputs.json','cases.py','test_cases.py','run_cases.py','appendix_template.md','publication_baseline.sha256']
    manifest={'case_id':c['case_id'],'edition':'2026-10-01','numeric_precision':40,'source_sha256':{
        name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in source_names},
        'generated_sha256':{path.relative_to(ROOT).as_posix():hashlib.sha256(text.encode('utf-8')).hexdigest() for path,text in products.items()}}
    products[HERE/'results/reproduction_manifest.json']=json.dumps(manifest,indent=2)+'\n'
    return products


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');parser.add_argument('--results-only',action='store_true')
    args=parser.parse_args()
    if args.results_only:
        path=HERE/'results/scenario_results.json';path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(run(load_inputs()),default=str,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(path);return
    failed=[]
    for path,text in content().items():
        encoded=text.encode('utf-8')
        if args.check:
            if not path.exists() or path.read_bytes()!=encoded: failed.append(str(path))
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(encoded)
    if failed: raise SystemExit('Stale generated outputs:\n'+'\n'.join(failed))
    print('Exact regeneration check passed.' if args.check else 'Results, appendix, chapter exhibits and manifest generated.')


if __name__=='__main__': main()
