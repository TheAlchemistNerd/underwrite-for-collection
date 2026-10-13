from copy import deepcopy
from decimal import Decimal as D
import unittest
import decision_case as g
from cases import load_inputs


class GovernedCaseTests(unittest.TestCase):
    def setUp(self):
        self.f=g.load_fixture(); self.c=load_inputs()

    def test_prior_window_reconciles_to_order_opening(self):
        v=g.transaction_view(self.f,'2026-09-30')
        self.assertEqual(v['opening'],D(200000)); self.assertEqual(v['closing'],D(250000))
        self.assertEqual(v['account_balances'],{'BANK-A':D(130000),'BANK-B':D(120000)})
        self.assertEqual(v['closing'],self.c['operating']['opening_cash'])
        self.assertEqual(v['cash_reconciliation'],0)

    def test_gross_credits_have_separate_economic_components(self):
        v=g.transaction_view(self.f,'2026-09-30')
        self.assertEqual(v['raw_credits'],D(390000)); self.assertEqual(v['operating_receipts'],D(120000))
        self.assertEqual(v['transfer_credits'],D(70000)); self.assertEqual(v['reversed_credits'],D(20000))
        self.assertEqual(v['financing_net'],0); self.assertEqual(v['capital_net'],D(30000))
        self.assertEqual(v['unresolved_net'],D(50000)); self.assertEqual(v['operating_net'],D(-30000))

    def test_later_classification_changes_income_not_cash(self):
        before=g.transaction_view(self.f,'2026-09-30'); after=g.transaction_view(self.f,'2026-10-03')
        self.assertEqual(after['operating_receipts'],D(170000)); self.assertEqual(after['unresolved_net'],0)
        self.assertEqual(after['operating_net'],D(20000)); self.assertEqual(before['account_balances'],after['account_balances'])
        self.assertEqual(g.transaction_view(self.f,'2026-10-02')['operating_receipts'],D(120000))

    def test_effective_date_does_not_leak_later_knowledge(self):
        self.f['classification_versions'][0]['known_at']='2026-10-10'
        self.assertEqual(g.transaction_view(self.f,'2026-10-03')['unresolved_net'],D(50000))

    def test_reversal_is_visible_only_when_known(self):
        self.assertEqual(g.transaction_view(self.f,'2026-09-15')['operating_receipts'],D(140000))
        self.assertEqual(g.transaction_view(self.f,'2026-09-16')['operating_receipts'],D(120000))

    def test_transfer_must_match_before_consolidation(self):
        self.f['transactions'][3]['amount']='69000'
        with self.assertRaisesRegex(ValueError,'matched'): g.transaction_view(self.f,'2026-09-30')

    def test_unverified_account_cannot_enter_consolidation(self):
        self.f['accounts'][1]['known_at']='2026-10-03'
        with self.assertRaisesRegex(ValueError,'ownership'): g.transaction_view(self.f,'2026-09-30')

    def test_duplicate_source_transaction_rejected(self):
        self.f['transactions'].append(deepcopy(self.f['transactions'][0]))
        with self.assertRaisesRegex(ValueError,'Duplicate'): g.transaction_view(self.f,'2026-09-30')

    def test_unresolved_and_partial_coverage_have_specific_routes(self):
        v=g.transaction_view(self.f,'2026-09-30')
        self.assertEqual(v['unresolved_share'],D(50000)/D(300000))
        self.assertIn('defer',g.evidence_route(v,self.f['policy'])['steps'])
        self.assertEqual(g.evidence_route(v,self.f['policy'],coverage_complete=False)['view'],'reduced_features')
        self.assertFalse(g.evidence_route(v,self.f['policy'],permission=False)['executable'])

    def test_resolved_evidence_can_be_accepted(self):
        self.assertEqual(g.evidence_route(g.transaction_view(self.f,'2026-10-03'),self.f['policy'])['steps'],['accept'])

    def test_option_math_reuses_primary_case(self):
        o=g.amendment_options(self.c)
        self.assertEqual(o['delay_keep_contract']['financing_needed'],D(495000))
        self.assertEqual(o['approved_90_day_extension']['minimum_cash'],D(120000))
        self.assertEqual(o['approved_90_day_extension']['finance_cost'],D(32500))
        self.assertEqual(o['approved_90_day_extension']['margin_budget_economic_profit'],D(-3650))
        self.assertIsNone(o['delay_keep_contract']['margin_budget_economic_profit'])

    def test_permission_and_consent_are_separate_prerequisites(self):
        o=g.amendment_options(self.c)
        self.assertEqual(g.amendment_gate(o,self.f['policy'],True,False,True)['state'],'awaiting_authority')
        self.assertEqual(g.amendment_gate(o,self.f['policy'],True,True,False)['state'],'awaiting_borrower_agreement')
        self.assertEqual(g.amendment_gate(o,self.f['policy'],True,True,True)['state'],'approved')

    def test_affordability_and_concession_limits_apply(self):
        o=g.amendment_options(self.c); o['approved_90_day_extension']['minimum_cash']=D(99999)
        self.assertFalse(g.amendment_gate(o,self.f['policy'],True,True,True)['executable'])
        o=g.amendment_options(self.c); self.f['policy']['maximum_approved_concession_loss']='3000'
        self.assertFalse(g.amendment_gate(o,self.f['policy'],True,True,True)['executable'])

    def test_approval_does_not_change_contract_or_create_cash(self):
        v=g.action_snapshot(self.f,'2026-11-18',self.c)
        self.assertEqual(v['state'],'approved'); self.assertEqual(v['effective_due_day'],60)
        self.assertEqual(v['settled_cash'],0)
        booked=g.action_snapshot(self.f,'2026-11-19',self.c)
        self.assertEqual(booked['effective_due_day'],90); self.assertEqual(booked['expected_contract_payment'],D(522500))

    def test_settlement_requires_observation_at_cutoff(self):
        self.assertEqual(g.action_snapshot(self.f,'2026-12-30',self.c)['settled_cash'],0)
        v=g.action_snapshot(self.f,'2026-12-31',self.c)
        self.assertEqual(v['settled_cash'],D(522500)); self.assertEqual(v['payment_shortfall'],0)
        self.assertEqual(v['durable_outcome'],'follow-up incomplete')

    def test_illegal_execution_and_approval_are_rejected(self):
        with self.assertRaisesRegex(ValueError,'approval'): g.append_event([],self.f['action_events'][2])
        with self.assertRaisesRegex(ValueError,'executed'): g.append_event([],self.f['action_events'][3])
        bad=deepcopy(self.f['action_events'][1]); bad['authority']=False
        with self.assertRaisesRegex(ValueError,'authority'): g.append_event([],bad)

    def test_retry_idempotence_and_collision(self):
        log=[]; event=self.f['action_events'][0]
        g.append_event(log,event); g.append_event(log,event); self.assertEqual(len(log),1)
        collision=deepcopy(event); collision['recommended_due_day']=120
        with self.assertRaisesRegex(ValueError,'collision'): g.append_event(log,collision)

    def test_partial_settlement_preserves_shortfall(self):
        self.f['action_events'][3]['amount']='510000'
        self.assertEqual(g.action_snapshot(self.f,'2026-12-31',self.c)['payment_shortfall'],D(12500))

    def test_duplicate_settlement_reference_rejected(self):
        log=[]
        for e in self.f['action_events']: g.append_event(log,e)
        duplicate=deepcopy(log[-1]); duplicate['id']='A05'
        with self.assertRaisesRegex(ValueError,'rail reference'): g.append_event(log,duplicate)

    def test_settlement_requires_nonempty_reference(self):
        for value in [None, '', '   ', 123]:
            log=[]
            for e in self.f['action_events'][:3]: g.append_event(log,e)
            event=deepcopy(self.f['action_events'][3]); event['rail_reference']=value
            with self.assertRaisesRegex(ValueError,'nonempty'): g.append_event(log,event)

    def test_source_outage_preserves_last_verification_and_loss(self):
        v=g.protection_snapshot(self.f,'2026-11-08',self.c)
        self.assertEqual(v['last_verified_at'],'2026-10-01')
        self.assertEqual(v['expected_nominal_loss'],D(12800))

    def test_verified_change_updates_recovery_and_records_no_action(self):
        before=g.protection_snapshot(self.f,'2026-11-10',self.c)
        after=g.protection_snapshot(self.f,'2026-11-15',self.c)
        self.assertEqual(before['expected_nominal_loss'],D(12800)); self.assertEqual(after['expected_nominal_loss'],D(16800))
        self.assertEqual(before['pd'],after['pd']); self.assertIn('authorised_no_action',after['steps'])
        self.assertEqual(after['closure_evidence'],'P04 specialist review; CD01 authorised customer decision and rationale')

    def test_recovery_update_does_not_authorise_customer_decision(self):
        self.f['protection_evidence'][3]['customer_decision']['authority']=False
        after=g.protection_snapshot(self.f,'2026-11-15',self.c)
        self.assertEqual(after['expected_nominal_loss'],D(16800))
        self.assertNotIn('authorised_no_action',after['steps']); self.assertIsNone(after['closure_evidence'])

    def test_customer_no_action_requires_rationale_and_known_decision(self):
        for update in [{'rationale':'   '},{'known_at':'2026-11-16'}]:
            f=deepcopy(self.f); f['protection_evidence'][3]['customer_decision'].update(update)
            after=g.protection_snapshot(f,'2026-11-15',self.c)
            self.assertEqual(after['expected_nominal_loss'],D(16800)); self.assertIsNone(after['customer_decision'])

    def test_repeated_run_is_identical(self):
        self.assertEqual(g.build_results(self.f,self.c),g.build_results(self.f,self.c))

    def test_publication_fingerprint_checks_governance_input(self):
        import run_decision_case as p
        import cases, json
        from pathlib import Path
        finance=json.loads(Path(cases.__file__).with_name('case_inputs.json').read_text(encoding='utf8'))
        self.assertTrue(p.publication_is_current(self.f,finance))
        self.f['policy']['cash_floor']='90000'
        self.assertFalse(p.publication_is_current(self.f,finance))

    def test_publication_fingerprint_checks_primary_finance_input(self):
        import run_decision_case as p
        import cases, json
        from pathlib import Path
        finance=json.loads(Path(cases.__file__).with_name('case_inputs.json').read_text(encoding='utf8'))
        finance['loan']['coupon']='0.19'
        self.assertFalse(p.publication_is_current(self.f,finance))


if __name__=='__main__': unittest.main()
