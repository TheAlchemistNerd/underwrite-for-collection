"""Reproducible evidence-to-decision teaching case. Standard library only.

Every policy threshold, action record and financial scenario is hypothetical.
Point-in-time replay uses both effective and knowledge time. Monetary amounts
retain Decimal precision; source classification never changes booked cash.
"""
from copy import deepcopy
from decimal import Decimal as D
import json
from pathlib import Path

ZERO = D(0)


def load_fixture(path=None):
    return json.loads(Path(path or Path(__file__).with_name('decision_case_inputs.json')).read_text(encoding='utf-8'))


def visible(record, cutoff, event_field='effective_at'):
    return record['known_at'] <= cutoff and record[event_field] <= cutoff


def transaction_view(fixture, cutoff):
    """Return immutable account cash and an as-of economic classification bridge."""
    accounts = {a['id']: a for a in fixture['accounts']
                if a['known_at'] <= cutoff and a['effective_from'] <= cutoff}
    if not accounts or any(a['owner'] != fixture['economic_unit'] for a in accounts.values()):
        raise ValueError('Approved account ownership is incomplete for this economic unit')
    rows, seen = [], set()
    for original in fixture['transactions']:
        if original['id'] in seen:
            raise ValueError('Duplicate source transaction identifier')
        seen.add(original['id'])
        if not visible(original, cutoff, 'settled_at'):
            continue
        if original['account'] not in accounts:
            raise ValueError('Cash event requires point-in-time verified account ownership')
        row = deepcopy(original)
        row['amount'] = D(row['amount'])
        versions = [v for v in fixture['classification_versions'] if v['transaction_id'] == row['id']
                    and visible(v, cutoff) and v['verified_at'] <= cutoff]
        if versions:
            chosen = max(versions, key=lambda v: (v['known_at'], v['version']))
            row.update({'class': chosen['class'], 'classification_version': chosen['version'],
                        'classification_evidence': chosen['evidence']})
        else:
            row['classification_version'] = 'source-v1'
        rows.append(row)
    by_id = {r['id']: r for r in rows}
    reversed_ids = set()
    for row in rows:
        if 'reverses' in row:
            origin = by_id.get(row['reverses'])
            if not origin or origin['amount'] != -row['amount'] or origin['account'] != row['account']:
                raise ValueError('Reversal must reconcile to the original observed account credit')
            if origin['id'] in reversed_ids:
                raise ValueError('A credit cannot be reversed twice')
            reversed_ids.update([origin['id'], row['id']])
    pairs = {}
    for row in rows:
        if row['class'] == 'internal_transfer':
            pairs.setdefault(row['pair'], []).append(row)
    for pair in pairs.values():
        if len(pair) != 2 or sum((r['amount'] for r in pair), ZERO) != ZERO or pair[0]['account'] == pair[1]['account']:
            raise ValueError('Internal transfer needs two matched, opposite account movements')
    balances = {k: D(v['opening']) for k, v in accounts.items()}
    bridge = {k: ZERO for k in ('operating_receipts', 'operating_costs', 'financing_net', 'capital_net', 'unresolved_net')}
    raw_credits = transfer_credits = reversed_credits = external_positive = ZERO
    for row in rows:
        amount, kind = row['amount'], row['class']
        balances[row['account']] += amount
        raw_credits += max(ZERO, amount)
        if kind == 'internal_transfer':
            transfer_credits += max(ZERO, amount)
        elif row['id'] in reversed_ids:
            reversed_credits += max(ZERO, amount)
        else:
            external_positive += max(ZERO, amount)
            if kind in ('operating_receipt', 'related_operating_receipt'):
                if amount < 0: raise ValueError('Operating receipt must be a credit')
                bridge['operating_receipts'] += amount
            elif kind == 'operating_cost':
                if amount > 0: raise ValueError('Operating cost must be a debit')
                bridge['operating_costs'] += amount
            elif kind == 'financing': bridge['financing_net'] += amount
            elif kind == 'capital': bridge['capital_net'] += amount
            elif kind == 'unresolved': bridge['unresolved_net'] += amount
            else: raise ValueError('Unmapped economic class')
    opening = sum((D(a['opening']) for a in accounts.values()), ZERO)
    closing = sum(balances.values(), ZERO)
    operating_net = bridge['operating_receipts'] + bridge['operating_costs']
    residual = closing - opening - sum(bridge.values())
    if residual != 0: raise AssertionError('Cash classification bridge failed')
    return dict(cutoff=cutoff, rows=rows, account_balances=balances, opening=opening, closing=closing,
                raw_credits=raw_credits, transfer_credits=transfer_credits, reversed_credits=reversed_credits,
                external_positive=external_positive, **bridge, operating_net=operating_net,
                unresolved_share=max(ZERO, bridge['unresolved_net']) / external_positive if external_positive else ZERO,
                cash_reconciliation=residual)


def evidence_route(view, policy, permission=True, coverage_complete=True):
    """Illustrative internal policy; no likelihood or motive is inferred."""
    if not permission:
        return dict(view='unavailable', steps=['defer'], reason='Required authority to obtain/use source is absent', executable=False)
    if not coverage_complete:
        return dict(view='reduced_features', steps=['reduced_features', 'request_evidence', 'human_review'],
                    reason='Use observed cash; withhold complete-enterprise recurring-income features', executable=False)
    if view['unresolved_share'] > D(policy['material_unresolved_share']):
        return dict(view='conservative_scenario', steps=['conservative_scenario', 'request_evidence', 'human_review', 'defer'],
                    reason='Verify the invoice and cash purpose of T08 before a material recurring-income decision', executable=False)
    return dict(view='accepted', steps=['accept'], reason='Cash bridge and classification support the stated decision', executable=True)


def amendment_options(finance_inputs):
    from cases import borrower, pricing
    result = {}
    for name, bmode, pmode in [('original_on_time', 'on_time', 'term'),
                              ('delay_keep_contract', 'delay_unfinanced', 'term'),
                              ('approved_90_day_extension', 'approved_extension', 'extension')]:
        b = borrower(finance_inputs, bmode)
        p = pricing(finance_inputs, pmode)
        result[name] = dict(minimum_cash=b['minimum'], financing_needed=b['peak_financing_needed'],
                            finance_cost=b['finance_cost'], terminal_cash=b['closing'],
                            margin_budget_economic_profit=p['economic_profit'],
                            affordability_pass=b['minimum'] >= finance_inputs['operating']['cash_floor'])
    # The unmodified late path is an uncovered scheduled-payment forecast.
    result['delay_keep_contract']['margin_budget_economic_profit'] = None
    result['delay_keep_contract']['pricing_status'] = 'requires a dated delinquency/workout path; scheduled term budget alone is insufficient'
    return result


def amendment_gate(options, policy, receipt_verified, authority, borrower_agreement):
    selected = options['approved_90_day_extension']
    if not receipt_verified:
        return dict(state='deferred', executable=False, steps=['request_evidence', 'human_review', 'defer'], reason='Customer receipt date needs verification')
    if selected['minimum_cash'] < D(policy['cash_floor']):
        return dict(state='review_required', executable=False, steps=['human_review'], reason='Revised cash path breaches the adopted operating floor')
    if selected['margin_budget_economic_profit'] < -D(policy['maximum_approved_concession_loss']):
        return dict(state='review_required', executable=False, steps=['human_review'], reason='Analytical concession exceeds the sample delegated loss budget')
    if not authority:
        return dict(state='awaiting_authority', executable=False, steps=['human_review'], reason='A delegated credit officer must authorise this amendment')
    if not borrower_agreement:
        return dict(state='awaiting_borrower_agreement', executable=False, steps=['human_review'], reason='Borrower agreement to the revised schedule remains outstanding')
    return dict(state='approved', executable=True, steps=['accept', 'approved'], reason='Verified receipt, affordable schedule, authorised concession and borrower agreement recorded')


def append_event(log, event):
    for prior in log:
        if prior['id'] == event['id']:
            if prior == event: return log
            raise ValueError('Event identifier collision')
    if event['effective_at'] > event['known_at']:
        raise ValueError('This execution fixture records completed events, not future instructions')
    if log and event['known_at'] < log[-1]['known_at']:
        raise ValueError('Append log in knowledge-time order')
    if event['kind'] == 'approved':
        if not event.get('authority') or not event.get('borrower_agreement'):
            raise ValueError('Approval requires authority and borrower agreement')
        if not any(e['kind'] == 'reviewed' and e['evidence_version'] == event['evidence_version'] for e in log):
            raise ValueError('Approval requires the reviewed evidence version')
    elif event['kind'] == 'booked':
        if not any(e['id'] == event['approval_id'] and e['kind'] == 'approved' and
                   e['evidence_version'] == event['evidence_version'] and e['known_at'] <= event['effective_at'] for e in log):
            raise ValueError('Booking requires prior matching approval')
    elif event['kind'] == 'settled':
        if D(event['amount']) <= 0: raise ValueError('Settlement must be positive')
        if not isinstance(event.get('rail_reference'), str) or not event['rail_reference'].strip():
            raise ValueError('Settlement requires a nonempty rail reference')
        if any(e.get('rail_reference') == event['rail_reference'] for e in log):
            raise ValueError('Duplicate settlement rail reference')
        if not any(e['id'] == event['booking_id'] and e['kind'] == 'booked' and e['known_at'] <= event['effective_at'] for e in log):
            raise ValueError('Settlement requires the executed revised contract')
    elif event['kind'] == 'reviewed':
        if event['recommended_due_day'] != 90:
            raise ValueError('This bounded amendment fixture supports the reviewed 90-day option')
    else:
        raise ValueError('Unsupported event kind')
    log.append(deepcopy(event))
    return log


def action_snapshot(fixture, cutoff, finance_inputs):
    log=[]
    for event in fixture['action_events']:
        if visible(event, cutoff): append_event(log, event)
    kinds=[e['kind'] for e in log]
    booked='booked' in kinds
    l=finance_inputs['loan']
    due_day=90 if booked else 60
    due=l['principal']*(D(1)+l['coupon']*D(due_day)/D(360))
    received=sum((D(e['amount']) for e in log if e['kind']=='settled'),ZERO)
    return dict(cutoff=cutoff,state=kinds[-1] if kinds else 'unreviewed',effective_due_day=due_day,
                expected_contract_payment=due,settled_cash=received,
                delivered_action='90-day schedule booked' if booked else 'original schedule remains effective',
                outcome='payment observed in synthetic follow-up' if received else 'awaiting observed payment',
                payment_shortfall=max(ZERO,due-received) if received else None,
                durable_outcome='follow-up incomplete',event_ids=[e['id'] for e in log])


def protection_snapshot(fixture, cutoff, finance_inputs):
    known=[e for e in fixture['protection_evidence'] if visible(e,cutoff)]
    verified=[e for e in known if e.get('verified_at','9999') <= cutoff and 'gross_recovery' in e]
    if not verified: raise ValueError('No verified protection baseline at cutoff')
    current=max(verified,key=lambda e:e['verified_at'])
    latest=max(known,key=lambda e:e['known_at'])
    principal=finance_inputs['loan']['principal']
    cost=principal*finance_inputs['credit']['workout_cost_fraction']
    recovery=D(current['gross_recovery'])
    pd=finance_inputs['credit']['default_probability']
    changed=current['result']=='confirmed_change'
    decision=current.get('customer_decision', {})
    approved_no_action=(changed and decision.get('authority') is True and
                        decision.get('action')=='retain_contract' and
                        isinstance(decision.get('actor'),str) and bool(decision['actor'].strip()) and
                        isinstance(decision.get('rationale'),str) and bool(decision['rationale'].strip()) and
                        bool(decision.get('id')) and decision.get('known_at','9999') <= cutoff and
                        bool(decision.get('next_review_at')))
    return dict(cutoff=cutoff,last_verified_at=current['verified_at'],latest_evidence=latest['result'],
                verified_gross_recovery=recovery,nominal_lgd=(principal-recovery+cost)/principal,
                pd=pd,expected_nominal_loss=pd*(principal-recovery+cost),
                steps=['human_review','authorised_no_action'] if approved_no_action else ['human_review'] if changed else ['request_evidence','human_review'] if latest['result']!='confirmed' else ['accept'],
                contract_action='authorised no borrower-contract action; refresh recovery assumption and follow recorded review date' if approved_no_action else 'customer decision awaits authority and rationale' if changed else 'retain current contract',
                review_owner=current['owner'],
                customer_decision=deepcopy(decision) if approved_no_action else None,
                closure_evidence=f"{current['id']} specialist review; {decision['id']} authorised customer decision and rationale" if approved_no_action else None)


def build_results(fixture, finance_inputs):
    prior=transaction_view(fixture,'2026-09-30')
    after=transaction_view(fixture,'2026-10-03')
    if prior['closing'] != finance_inputs['operating']['opening_cash']:
        raise ValueError('Prior-window cash must reconcile to primary order opening cash')
    options=amendment_options(finance_inputs)
    return dict(case_id=fixture['case_id'],before=prior,after=after,options=options,
                routes={'unresolved':evidence_route(prior,fixture['policy']),
                        'resolved':evidence_route(after,fixture['policy']),
                        'partial_coverage':evidence_route(prior,fixture['policy'],coverage_complete=False),
                        'no_permission':evidence_route(prior,fixture['policy'],permission=False)},
                amendment={'unverified':amendment_gate(options,fixture['policy'],False,False,False),
                           'missing_authority':amendment_gate(options,fixture['policy'],True,False,True),
                           'missing_agreement':amendment_gate(options,fixture['policy'],True,True,False),
                           'approved':amendment_gate(options,fixture['policy'],True,True,True)},
                action_snapshots=[action_snapshot(fixture,d,finance_inputs) for d in ['2026-11-18','2026-11-19','2026-12-30','2026-12-31']],
                protection=[protection_snapshot(fixture,d,finance_inputs) for d in ['2026-10-01','2026-11-08','2026-11-10','2026-11-15']])


def json_default(value):
    if isinstance(value,D): return str(value)
    raise TypeError(type(value).__name__)
