import unittest
from copy import deepcopy
from model import *

class CashflowCaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.results={s:run_scenario(s) for s in SCENARIOS}
    def test_hand_check(self):
        m=self.results['baseline']['snapshot']['monthly'][-1]
        self.assertEqual(m['gross_credits'],500000);self.assertEqual(m['operating_receipts'],410000)
        self.assertEqual(m['owner_capital'],45000);self.assertEqual(m['other_loan_drawdowns'],30000);self.assertEqual(m['reversal_credits'],15000)
        self.assertEqual(m['obligations'],385000);self.assertEqual(m['verified_residual'],25000)
    def test_duplicate_does_not_change_economic_cash(self):
        a=self.results['baseline']['snapshot'];b=self.results['duplicate_feed']['snapshot']
        self.assertEqual(a['monthly'],b['monthly']);self.assertEqual(len(b['duplicate_records']),1)
    def test_internal_transfers_cancel(self):
        a=self.results['baseline']['snapshot'];b=self.results['internal_transfers']['snapshot']
        self.assertEqual(a['posterior_mean'],b['posterior_mean']);self.assertEqual(b['monthly'][-1]['internal_net'],0)
    def test_missing_channel_routes_to_evidence(self):
        self.assertEqual(self.results['missing_channel']['snapshot']['route'],'request_evidence')
        self.assertEqual(self.results['missing_channel']['summary']['loans'],0)
    def test_late_classification_changes_current_not_historical(self):
        rows,truth,cov,_=synthetic_history('late_classification')
        old,_=snapshot(rows,cov,90);new,_=snapshot(rows,cov,96)
        self.assertGreater(old['unresolved'],0);self.assertEqual(new['unresolved'],0)
        self.assertEqual(old['route'],'request_evidence');self.assertEqual(new['route'],'offer_for_human_review')
    def test_future_knowledge_cannot_change_old_snapshot(self):
        rows,_,cov,_=synthetic_history('late_classification');before,_=snapshot(rows,cov,90)
        for row in rows:
            if row['classification_known_day']>90: row['cash_class']='exceptional'
        after,_=snapshot(rows,cov,90);self.assertEqual(before,after)
    def test_future_transactions_are_excluded(self):
        rows,_,cov,_=synthetic_history();before,_=snapshot(rows,cov,90)
        row=deepcopy(rows[0]);row.update(record_id='FUTURE',economic_id='FUTURE',event_day=91,known_day=91,settlement_day=91,amount=999999)
        rows.append(row);after,_=snapshot(rows,cov,90);self.assertEqual(before,after)
    def test_conflicting_duplicates_fail(self):
        rows,_,cov,_=synthetic_history('duplicate_feed');rows[-1]['amount']+=1
        with self.assertRaises(ValueError): snapshot(rows,cov,90)
    def test_predictive_interval_wider_than_mean_interval(self):
        s=self.results['baseline']['snapshot'];self.assertLess(s['predictive_low'],s['mean_credible_low']);self.assertGreater(s['predictive_high'],s['mean_credible_high'])
    def test_request_exceeds_cap(self):
        s=self.results['baseline']['snapshot'];self.assertGreater(s['requested_instalment'],s['maximum_monthly_payment']);self.assertLess(s['shortfall_probability'],.1)
    def test_calendar_gate(self):
        r=run_scenario('baseline',{'cash_open':0});self.assertEqual(r['snapshot']['route'],'cash_calendar_review');self.assertEqual(r['summary']['loans'],0)
    def test_noise_uncertainty_changes_route(self):
        r=run_scenario('baseline',{'monthly_noise_sd':30000});self.assertEqual(r['snapshot']['route'],'affordability_review')
    def test_baseline_three_cycles(self):
        r=self.results['baseline'];self.assertEqual(r['summary']['paid_loans'],3);self.assertEqual(r['summary']['defaults'],0)
    def test_every_cash_row_reconciles(self):
        for r in self.results.values():
            for row in r['merchant_daily']: self.assertAlmostEqual(row['cash_reconciliation_error'],0,places=6)
    def test_lender_contribution_reconciles(self):
        for r in self.results.values(): self.assertAlmostEqual(r['summary']['lender_contribution_reconciliation_error'],0,places=6)
    def test_principal_reconciles(self):
        for r in self.results.values():
            s=r['summary'];self.assertAlmostEqual(s['originations'],s['principal_collected']+s['gross_principal_writeoff']+s['terminal_performing_principal'])
    def test_loan_fees_and_principal_bounded(self):
        for r in self.results.values():
            for loan in r['loans']:
                self.assertLessEqual(loan['principal_paid'],loan['principal']);self.assertLessEqual(loan['fee_paid'],3000)
    def test_operating_payables_reconcile(self):
        for r in self.results.values():
            flows=future_events(r['summary']['scenario'],300)
            accrued=-sum(v for es in flows.values() for k,v in es if k in ('supplier','operating_cost'))
            self.assertAlmostEqual(accrued,sum(x['operating_paid'] for x in r['merchant_daily'])+r['summary']['terminal_operating_payables'])
    def test_existing_debt_reconciles(self):
        for r in self.results.values(): self.assertAlmostEqual(250000,sum(x['existing_debt_paid'] for x in r['merchant_daily'])+r['summary']['terminal_existing_debt_arrears'])
    def test_household_needs_reconcile(self):
        for r in self.results.values(): self.assertAlmostEqual(200000,sum(x['household_paid'] for x in r['merchant_daily'])+r['summary']['household_shortfall'])
    def test_approval_precedes_execution_and_checker_differs(self):
        for r in self.results.values():
            events=r['audit_events']
            for ix,e in enumerate(events):
                if e['stage']=='execution_receipt':
                    approvals=[x for x in events[:ix] if x['stage'] in ('approval','repeat_approval')]
                    self.assertTrue(approvals);self.assertEqual(approvals[-1]['actor'],'credit_checker')
    def test_event_identifiers_unique(self):
        for r in self.results.values():
            ids=[x['event_id'] for x in r['audit_events']];self.assertEqual(len(ids),len(set(ids)))
    def test_event_hash_chain(self):
        for r in self.results.values():
            for a,b in zip(r['audit_events'],r['audit_events'][1:]): self.assertEqual(b['previous_event_hash'],digest(a))
    def test_repeat_has_observed_history_only(self):
        for r in self.results.values():
            for loan in r['loans']:
                self.assertLess(loan['decision_evidence_through'],loan['origination_day'])
                if loan['origination_day']>1: self.assertGreaterEqual(loan['repeat_trailing_residual'],22000)
    def test_future_stress_does_not_change_initial_offer(self):
        for name in ('delayed_settlement','margin_stress','sustained_stress','reviewed_reschedule'):
            self.assertEqual(self.results[name]['snapshot'],self.results['baseline']['snapshot'])
    def test_feed_gap_routes_before_credit_action(self):
        a=self.results['post_disbursement_feed_gap'];b=self.results['baseline']
        self.assertEqual(a['summary']['lender_contribution'],b['summary']['lender_contribution'])
        self.assertEqual(next(x for x in a['monitoring'] if x['day']==60)['route'],'repair_source')
    def test_reschedule_is_prospective(self):
        r=self.results['reviewed_reschedule'];first=[x for x in r['instalments'] if x['loan_id']=='L01']
        self.assertEqual(first[0]['approved_due'],30);self.assertEqual(first[1]['approved_due'],75);self.assertEqual(first[2]['approved_due'],105)
        self.assertEqual(r['summary']['max_new_loan_dpd'],0)
    def test_late_payment_raises_funding(self):
        self.assertGreater(self.results['delayed_settlement']['summary']['funding_cost'],self.results['baseline']['summary']['funding_cost'])
    def test_default_stops_repeats_and_records_bills(self):
        r=self.results['sustained_stress']['summary'];self.assertEqual(r['loans'],1);self.assertEqual(r['defaults'],1);self.assertGreater(r['terminal_operating_payables'],0)
    def test_nonnegative_cash_and_payables(self):
        for r in self.results.values():
            for x in r['merchant_daily']:
                self.assertGreaterEqual(x['closing_cash'],0);self.assertGreaterEqual(x['closing_operating_payables'],0)
    def test_workout_principal_continues_to_cost_funding(self):
        r=self.results['sustained_stress'];default_day=r['loans'][0]['default_day']
        later=[x for x in r['merchant_daily'] if x['day']>default_day]
        self.assertTrue(all(x['funding_cost']>0 for x in later))
    def test_fifo_clears_earlier_fee_before_later_principal(self):
        schedule=[dict(number=1,approved_due=30,principal_due=10000,fee_due=1000,principal_paid=10000,fee_paid=0),dict(number=2,approved_due=60,principal_due=10000,fee_due=1000,principal_paid=0,fee_paid=0)]
        principal,fee=allocate_payment(schedule,60,1500)
        self.assertEqual(fee,1000);self.assertEqual(principal,500)
        self.assertEqual(schedule[0]['fee_paid'],1000);self.assertEqual(schedule[1]['principal_paid'],500)
    def test_fifo_never_prepays_future_instalment(self):
        schedule=[dict(number=1,approved_due=30,principal_due=10000,fee_due=1000,principal_paid=0,fee_paid=0)]
        self.assertEqual(allocate_payment(schedule,29,50000),(0,0))
    def test_instalment_allocations_match_loan_totals(self):
        for r in self.results.values():
            for loan in r['loans']:
                inst=[x for x in r['instalments'] if x['loan_id']==loan['loan_id']]
                self.assertAlmostEqual(loan['principal_paid'],sum(x['principal_paid'] for x in inst))
                self.assertAlmostEqual(loan['fee_paid'],sum(x['fee_paid'] for x in inst))
    def test_deterministic(self): self.assertEqual(run_scenario('baseline'),run_scenario('baseline'))
    def test_unfunded_has_no_default_label(self):
        r=self.results['missing_channel'];self.assertEqual(r['loans'],[])
        # Zero rows is a missing lending outcome, rather than an observed non-default.

if __name__=='__main__': unittest.main()
