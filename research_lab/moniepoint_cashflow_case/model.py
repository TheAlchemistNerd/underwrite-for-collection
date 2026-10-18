"""Synthetic, auditable transaction-to-decision credit case. All currency is KES."""
from __future__ import annotations
from collections import defaultdict
from copy import deepcopy
from math import sqrt
from statistics import NormalDist
import hashlib, json

MODEL_VERSION = 'moniepoint-cashflow-1.0'
POLICY_VERSION = 'cash-calendar-human-review-1.0'
SCENARIOS = ('baseline', 'duplicate_feed', 'internal_transfers', 'missing_channel', 'late_classification', 'delayed_settlement', 'margin_stress', 'sustained_stress', 'reviewed_reschedule', 'post_disbursement_feed_gap')
DEFAULTS = dict(history_months=3, decision_day=90, future_days=300, cash_open=50000.0, cash_floor=20000.0,
    principal=30000.0, requested_monthly_payment=35000.0, instalment=11000.0, tenor=90,
    annual_funding_rate=0.12, origination_cost=500.0, daily_servicing_cost=2.0, workout_cost=400.0,
    default_dpd=30, recovery_lag=30, prior_mean=25000.0, prior_sd=15000.0, monthly_noise_sd=8000.0,
    maximum_shortfall_probability=0.10, maximum_payment_share=0.50, min_coverage=1.0,
    max_cycles=3, graph_version='entity-graph-1', classification_version='cash-taxonomy-1')


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def synthetic_history(scenario='baseline'):
    """Observed records and separate ground truth; event_day and known_day are distinct."""
    records, truth, n = [], [], 0
    def add(day, amount, cash_class, source='bank', economic_id=None, owner='enterprise', known=None, classification_known=None, note=''):
        nonlocal n
        n += 1
        eid = economic_id or f'E{n:04d}'
        row = dict(record_id=f'R{n:04d}', economic_id=eid, event_day=day, settlement_day=day,
            known_day=day if known is None else known, classification_known_day=day if classification_known is None else classification_known,
            amount=round(float(amount),2), source=source, account=f'{owner}-{source}', entity='M001' if owner=='enterprise' else 'OWNER',
            cash_class=cash_class, permitted_purpose='credit-assessment', note=note,
            graph_version='entity-graph-1', classification_version='cash-taxonomy-1')
        records.append(row); truth.append(dict(record_id=row['record_id'], true_economic_id=eid, true_class=cash_class))
    for month, receipts in enumerate((405000.0, 415000.0, 410000.0)):
        start=month*30
        for d in (6,12,18,24,30):
            for src, share in [('bank',.7), ('wallet',.3)]:
                amount=receipts/5*share
                delayed = 96 if scenario=='late_classification' and month==2 and d==30 and src=='bank' else None
                add(start+d, amount, 'operating_receipt', src, classification_known=delayed)
        add(start+15,45000,'owner_capital',note='Owner is a separate economic entity; external support is separately visible.')
        add(start+5,30000,'loan_drawdown',note='Other lender financing; liability recorded in obligations evidence.')
        add(start+18,15000,'reversal',note='Correction pair credits and debits net to zero.')
        add(start+18,-15000,'reversal',note='Correction pair debit.')
        for d in (1,7,13,19,25): add(start+d,-54000,'supplier')
        for d,v in ((10,25000),(20,25000),(30,20000)): add(start+d,-v,'operating_cost')
        add(start+28,-20000,'household')
        add(start+30,-25000,'existing_debt')
    if scenario=='duplicate_feed':
        original=next(x for x in records if x['event_day']==90 and x['source']=='bank' and x['amount']>0)
        dupe=deepcopy(original); dupe['record_id']='R-DUP'; dupe['note']='Second feed copy of the same authoritative economic event.'
        records.append(dupe); truth.append(dict(record_id='R-DUP',true_economic_id=original['economic_id'],true_class=original['cash_class']))
    if scenario=='internal_transfers':
        add(85,50000,'internal',source='bank',note='Credit into controlled bank account.')
        add(85,-50000,'internal',source='wallet',note='Matching debit from controlled wallet.')
    if scenario=='missing_channel':
        records=[x for x in records if not(x['source']=='wallet' and x['event_day']>60)]
    coverage=[dict(source=s, month=m, start_day=m*30+1, end_day=(m+1)*30, complete=not(scenario=='missing_channel' and s=='wallet' and m==2), known_day=90) for m in range(3) for s in ('bank','wallet')]
    accounts=[dict(account='enterprise-bank',entity='M001',relation='verified_control',known_day=1),dict(account='enterprise-wallet',entity='M001',relation='verified_control',known_day=1),dict(account='owner-bank',entity='OWNER',relation='owner_capital_provider',known_day=1)]
    return records,truth,coverage,accounts


def snapshot(records, coverage, cutoff, p=None):
    p=p or DEFAULTS
    eligible=[deepcopy(x) for x in records if x['known_day']<=cutoff and x['settlement_day']<=cutoff and x['permitted_purpose']=='credit-assessment']
    eligible.sort(key=lambda x:(x['known_day'],x['record_id']))
    unique={}; duplicates=[]
    for row in eligible:
        key=(row['economic_id'],row['account'])
        if key in unique:
            if row['amount'] != unique[key]['amount']: raise ValueError('Conflicting duplicate amounts require review')
            duplicates.append(row['record_id']); continue
        if row['classification_known_day']>cutoff: row['cash_class']='unresolved'
        unique[key]=row
    classified=list(unique.values()); monthly=[]
    for m in range(3):
        rows=[x for x in classified if m*30<x['event_day']<=(m+1)*30]
        totals=defaultdict(float)
        for x in rows: totals[x['cash_class']]+=x['amount']
        operating=totals['operating_receipt']
        costs=-sum(totals[k] for k in ('supplier','operating_cost','household','existing_debt'))
        monthly.append(dict(month=m+1, gross_credits=sum(max(0,x['amount']) for x in rows), operating_receipts=operating,
            owner_capital=totals['owner_capital'], other_loan_drawdowns=totals['loan_drawdown'], reversal_credits=sum(x['amount'] for x in rows if x['cash_class']=='reversal' and x['amount']>0),
            internal_net=totals['internal'], obligations=costs, verified_residual=operating-costs, unresolved_credits=sum(max(0,x['amount']) for x in rows if x['cash_class']=='unresolved')))
    known_cov=[x for x in coverage if x['known_day']<=cutoff]
    cov=sum(x['complete'] for x in known_cov)/6
    obs=[x['verified_residual'] for x in monthly]
    variance=1/(1/p['prior_sd']**2+len(obs)/p['monthly_noise_sd']**2)
    mean=variance*(p['prior_mean']/p['prior_sd']**2+sum(obs)/p['monthly_noise_sd']**2)
    sd=sqrt(variance); pred_sd=sqrt(variance+p['monthly_noise_sd']**2)
    unresolved=sum(x['unresolved_credits'] for x in monthly)
    shortfall=NormalDist(mean,pred_sd).cdf(p['instalment'])
    expected_cash=p['cash_open']+p['principal']; calendar_min=expected_cash
    for d, evs in sorted(future_events('baseline',90).items()):
        expected_cash+=sum(v for _,v in evs)
        if d in (30,60,90): expected_cash-=p['instalment']
        calendar_min=min(calendar_min,expected_cash)
    route='offer_for_human_review'
    if cov<p['min_coverage'] or unresolved>0: route='request_evidence'
    elif calendar_min<p['cash_floor']: route='cash_calendar_review'
    elif p['instalment']>p['maximum_payment_share']*mean or shortfall>p['maximum_shortfall_probability']: route='affordability_review'
    result=dict(cutoff=cutoff,coverage=cov,unresolved=unresolved,duplicate_records=duplicates,monthly=monthly,
        expected_calendar_minimum_cash=calendar_min,posterior_mean=mean,posterior_sd=sd,mean_credible_low=mean-1.96*sd,mean_credible_high=mean+1.96*sd,
        predictive_low=mean-1.96*pred_sd,predictive_high=mean+1.96*pred_sd,shortfall_probability=shortfall,
        maximum_monthly_payment=p['maximum_payment_share']*mean,requested_instalment=p['requested_monthly_payment'],
        requested_shortfall_probability=NormalDist(mean,pred_sd).cdf(p['requested_monthly_payment']),route=route,
        model_version=MODEL_VERSION,policy_version=POLICY_VERSION,evidence_hash=digest(classified))
    return result,classified


def future_events(scenario, horizon):
    events=defaultdict(list)
    for month in range((horizon+29)//30):
        start=30*month
        revenue=410000.; supplier=270000.; delay=0
        if scenario in ('delayed_settlement','reviewed_reschedule') and month==1: delay=15
        if scenario=='margin_stress' and month in (1,2): supplier=310000.
        if scenario=='sustained_stress' and month>=1: revenue=270000.
        for d in (6,12,18,24,30): events[start+d+delay].append(('customer_receipt',revenue/5))
        for d in (1,7,13,19,25): events[start+d].append(('supplier',-supplier/5))
        for d,v in ((10,25000),(20,25000),(30,20000)): events[start+d].append(('operating_cost',-v))
        events[start+28].append(('household',-20000.))
        events[start+30].append(('existing_debt',-25000.))
    return events


def allocate_payment(schedule, day, available):
    """Contracted FIFO: clear the oldest due instalment, principal then fee within it."""
    principal_paid=fee_paid=0.0
    for item in sorted(schedule,key=lambda x:(x['approved_due'],x['number'])):
        if item['approved_due']>day: continue
        p=min(available,item['principal_due']-item['principal_paid'])
        available-=p;item['principal_paid']+=p;principal_paid+=p
        f=min(available,item['fee_due']-item['fee_paid'])
        available-=f;item['fee_paid']+=f;fee_paid+=f
    return principal_paid,fee_paid


def run_scenario(name, parameters=None):
    p=deepcopy(DEFAULTS); p.update(parameters or {})
    records,truth,coverage,accounts=synthetic_history(name)
    snap,classified=snapshot(records,coverage,p['decision_day'],p)
    cid='MONIEPOINT-'+name.upper(); audit=[]
    def log(day,stage,actor,details):
        event=dict(case_id=cid,event_id=f'{cid}-E{len(audit)+1:04d}',day=day,stage=stage,actor=actor,model_version=MODEL_VERSION,policy_version=POLICY_VERSION,evidence_hash=snap['evidence_hash'],details=details)
        event['previous_event_hash']=digest(audit[-1]) if audit else ''
        audit.append(event)
    log(0,'evidence_snapshot','evidence_service',{'route':snap['route'],'cutoff':90})
    log(0,'requested_terms_review','credit_maker',{'requested_monthly':p['requested_monthly_payment'],'capacity_cap':snap['maximum_monthly_payment'],'decision':'revise_terms'})
    approved=snap['route']=='offer_for_human_review'
    if approved:
        log(0,'proposal','credit_maker',{'principal':p['principal'],'instalment':p['instalment'],'reason':'Cash calendar, capacity cap and predictive shortfall gate passed.'})
        log(0,'approval','credit_checker',{'decision':'approve','scope':'First synthetic facility only; repeat loans receive fresh review.'})
    else:
        log(0,'evidence_request','credit_maker',{'decision':snap['route'],'reason':'Source coverage or classification needs resolution.'})
    flows=future_events(name,p['future_days']); daily=[]; loans=[]; instalments=[]; monitoring=[]; cash=p['cash_open']; payables=0.; debt=0.; fees_collected=0.; funding=0.; costs=0.; default_loss=0.; recoveries=0.; lender_cash=0.; last_cycle=0
    operations_shortfall=0.; household_shortfall=0.; debt_shortfall=0.
    active=None
    for day in range(1,p['future_days']+1):
        cash_open=cash; payables_open=payables; loan_draw=0.; payment=0.; principal_paid=0.; fee_paid=0.; recovery=0.; workout_cost=0.; orig_cost=0
        if approved and (day==1 or (active is None and day-last_cycle>=7 and len(loans)<p['max_cycles'] and day<=p['future_days']-p['tenor']+1)):
            previous=[x for x in daily if day-30<=x['day']<day]
            trailing=sum(x['operating_receipts']-x['operating_obligations_accrued'] for x in previous)
            gate=day==1 or (len(previous)==30 and trailing>=2*p['instalment'] and payables<.01 and cash>=p['cash_floor'])
            if gate:
                active=dict(loan_id=f'L{len(loans)+1:02d}',origination_day=day,principal=p['principal'],principal_paid=0.,fee_paid=0.,status='performing',default_day=None,writeoff=0.,recovery=0.,close_day=None,decision_evidence_through=day-1,repeat_trailing_residual=trailing if day>1 else None)
                loans.append(active); loan_draw=p['principal'];cash+=loan_draw;lender_cash-=loan_draw;orig_cost=p['origination_cost'];costs+=orig_cost;lender_cash-=orig_cost
                for k in (1,2,3): instalments.append(dict(loan_id=active['loan_id'],number=k,original_due=day+30*k-1,approved_due=day+30*k-1,principal_due=p['principal']/3,fee_due=p['instalment']-p['principal']/3,principal_paid=0.,fee_paid=0.))
                if day>1:
                    log(day,'repeat_proposal','credit_maker',{'loan_id':active['loan_id'],'evidence_through':day-1,'trailing_residual':trailing})
                    log(day,'repeat_approval','credit_checker',{'loan_id':active['loan_id'],'decision':'approve'})
                log(day,'execution_receipt','payment_adapter',{'loan_id':active['loan_id'],'principal':loan_draw,'receipt_id':cid+'-'+active['loan_id']+'-DRAW'})
        opening_principal=sum(max(0,x['principal']-x['principal_paid']-x['recovery']) for x in loans)
        daily_funding=opening_principal*p['annual_funding_rate']/365;funding+=daily_funding;lender_cash-=daily_funding
        servicing=p['daily_servicing_cost'] if active and active['status']=='performing' else 0;costs+=servicing;lender_cash-=servicing
        events=flows.get(day,[]); receipts=sum(v for k,v in events if k=='customer_receipt'); accrued=-sum(v for k,v in events if v<0);cash+=receipts
        operating_due=-sum(v for k,v in events if k in ('supplier','operating_cost'));household_due=-sum(v for k,v in events if k=='household');existing_due=-sum(v for k,v in events if k=='existing_debt')
        # Accrued trading obligations are paid before household drawings and new-loan repayments.
        payables+=operating_due; paid_operations=min(cash,payables);cash-=paid_operations;payables-=paid_operations
        paid_household=min(cash,household_due);cash-=paid_household;household_shortfall+=household_due-paid_household
        debt+=existing_due;paid_existing=min(cash,debt);cash-=paid_existing;debt-=paid_existing
        operations_shortfall+=max(0,operating_due-paid_operations)
        # Monitoring uses only the received data at this day. A feed gap is checked first.
        if day%30==0:
            start=max(1,day-29);window=[x for x in daily if start<=x['day']<day]
            current_receipts=sum(x['operating_receipts'] for x in window)+receipts
            coverage_ok=not(name=='post_disbursement_feed_gap' and day==60)
            reported_receipts=current_receipts if coverage_ok else current_receipts*.70
            route='repair_source' if not coverage_ok else ('customer_cash_review' if current_receipts<410000*.9 else 'routine')
            monitoring.append(dict(day=day,window_receipts=reported_receipts,coverage_complete=coverage_ok,route=route,evidence_through=day))
            log(day,'monitoring_route','monitoring_service',{'coverage_complete':coverage_ok,'observed_receipts':reported_receipts,'route':route})
        # The extension is proposed after observed late receipts, then approved prospectively.
        if name=='reviewed_reschedule' and day==45 and active and active['status']=='performing':
            observed=sum(x['operating_receipts'] for x in daily if 31<=x['day']<=44)+receipts
            log(day,'schedule_change_proposal','servicing_maker',{'observed_receipts_since_day31':observed,'reason':'Customer review confirms fifteen-day settlement delay.'})
            for inst in instalments:
                if inst['loan_id']==active['loan_id'] and inst['approved_due']>=day: inst['approved_due']+=15
            log(day,'schedule_change_approval','credit_checker',{'extension_days':15,'effective_day':45})
            log(day,'schedule_change_receipt','contract_adapter',{'schedule_version':'2','effective_day':45})
        overdue=0.;dpd=0
        if active and active['status']=='performing':
            schedule=[x for x in instalments if x['loan_id']==active['loan_id']]
            due_principal=sum(x['principal_due'] for x in schedule if x['approved_due']<=day)
            due_fee=sum(x['fee_due'] for x in schedule if x['approved_due']<=day)
            remaining_principal=max(0,due_principal-active['principal_paid']);remaining_fee=max(0,due_fee-active['fee_paid'])
            available=max(0,cash-p['cash_floor']) if payables<.01 and debt<.01 else 0
            principal_paid,fee_paid=allocate_payment(schedule,day,available)
            payment=principal_paid+fee_paid;cash-=payment;lender_cash+=payment;fees_collected+=fee_paid;active['principal_paid']+=principal_paid;active['fee_paid']+=fee_paid
            for inst in sorted(schedule,key=lambda x:x['approved_due']):
                if inst['approved_due']<=day and inst['principal_paid']+inst['fee_paid']<inst['principal_due']+inst['fee_due']-.01:
                    dpd=day-inst['approved_due'];break
            overdue=max(0,due_principal+due_fee-active['principal_paid']-active['fee_paid'])
            if active['principal_paid']>=active['principal']-.01 and active['fee_paid']>=3*(p['instalment']-p['principal']/3)-.01:
                active['status']='paid';active['close_day']=day;last_cycle=day;log(day,'facility_closed','loan_ledger',{'loan_id':active['loan_id'],'principal_paid':active['principal_paid'],'fees_paid':active['fee_paid']});active=None
            elif dpd>=p['default_dpd']:
                active['status']='default';active['default_day']=day;active['writeoff']=active['principal']-active['principal_paid'];default_loss+=active['writeoff'];approved=False
                workout_cost=p['workout_cost'];costs+=workout_cost;lender_cash-=workout_cost
                log(day,'workout_review','credit_checker',{'loan_id':active['loan_id'],'dpd':dpd,'gross_principal_writeoff':active['writeoff']})
        if active and active['status']=='default' and day==active['default_day']+p['recovery_lag']:
            recovery=min(active['writeoff'],max(0,cash-p['cash_floor'])) if payables<.01 and debt<.01 else 0
            cash-=recovery;lender_cash+=recovery;recoveries+=recovery;active['recovery']=recovery
            log(day,'workout_recovery','payment_adapter',{'loan_id':active['loan_id'],'recovery':recovery,'receipt_id':cid+'-REC'})
        daily.append(dict(day=day,opening_cash=cash_open,operating_receipts=receipts,operating_obligations_accrued=accrued,operating_paid=paid_operations,household_paid=paid_household,existing_debt_paid=paid_existing,
            loan_draw=loan_draw,new_loan_principal_paid=principal_paid,new_loan_fee_paid=fee_paid,recovery_paid=recovery,closing_cash=cash,closing_operating_payables=payables,closing_existing_debt_arrears=debt,
            new_loan_arrears=overdue,days_past_due=dpd,funding_cost=daily_funding,servicing_cost=servicing,origination_cost=orig_cost,workout_cost=workout_cost,lender_cash=lender_cash,
            cash_reconciliation_error=cash-(cash_open+receipts+loan_draw-paid_operations-paid_household-paid_existing-payment-recovery)))
    performing=sum(x['principal']-x['principal_paid'] for x in loans if x['status']=='performing')
    unresolved=sum(x['writeoff']-x['recovery'] for x in loans if x['status']=='default')
    summary=dict(scenario=name,decision_route=snap['route'],loans=len(loans),paid_loans=sum(x['status']=='paid' for x in loans),defaults=sum(x['status']=='default' for x in loans),
        originations=sum(x['principal'] for x in loans),principal_collected=sum(x['principal_paid'] for x in loans),fee_collected=fees_collected,funding_cost=funding,operating_cost=costs,
        gross_principal_writeoff=default_loss,recovery=recoveries,net_realized_credit_loss=default_loss-recoveries,lender_contribution=fees_collected-funding-costs-default_loss+recoveries,
        terminal_performing_principal=performing,terminal_default_principal=unresolved,terminal_merchant_cash=cash,minimum_merchant_cash=min(x['closing_cash'] for x in daily),
        terminal_operating_payables=payables,terminal_existing_debt_arrears=debt,household_shortfall=household_shortfall,max_new_loan_dpd=max(x['days_past_due'] for x in daily),
        terminal_accrued_unpaid_fees=sum(x['fee_due']-x['fee_paid'] for x in instalments if x['approved_due']<=p['future_days']),
        lender_cash=lender_cash,lender_contribution_reconciliation_error=fees_collected-funding-costs-default_loss+recoveries-(lender_cash+performing),
        max_cash_reconciliation_error=max(abs(x['cash_reconciliation_error']) for x in daily))
    return dict(parameters=p,summary=summary,snapshot=snap,raw_transactions=records,transaction_truth=truth,classified_transactions=classified,source_coverage=coverage,accounts=accounts,merchant_daily=daily,loans=loans,instalments=instalments,audit_events=audit,monitoring=monitoring)


