"""Independent arithmetic examples and failure cases for the teaching case."""
import copy
from decimal import Decimal as D
import unittest
import cases


class WorkedCaseTests(unittest.TestCase):
    def setUp(self): self.c=cases.load_inputs()
    def near(self,a,b,tol="0.000001"): self.assertLessEqual(abs(a-D(str(b))),D(tol))

    def test_operating_sources_uses_and_finance(self):
        r=cases.borrower(self.c)
        self.assertEqual([x["closing"] for x in r["rows"]],[D(340000),D(220000),D(405000)])
        self.assertEqual(r["closing"]-D(250000),D(1000000)-D(820000)-D(25000))
        for row in r["rows"]:
            self.assertEqual(row["closing"],row["opening"]+row["receipts"]+row["draw"]-row["operating"]-row["debt"]-row["fee"])

    def test_delayed_receipt_is_an_unfinanced_gap_not_a_loan(self):
        r=cases.borrower(self.c,"delay_unfinanced")
        self.assertEqual(r["minimum"],D(-395000))
        self.assertEqual(r["peak_financing_needed"],D(495000))
        self.assertFalse(r["executable_without_new_finance"])

    def test_extension_changes_cash_schedule(self):
        r=cases.borrower(self.c,"approved_extension")
        self.assertEqual(r["closing"],D(397500))
        self.assertEqual(r["minimum"],D(120000))
        self.assertEqual(r["peak_financing_needed"],0)

    def test_term_hurdle_independent_calculation(self):
        r=cases.pricing(self.c)
        self.assertEqual(r["expected_loss"],D(12800))
        self.assertEqual(r["economic_profit"],D(-1700))
        self.assertEqual(r["hurdle_coupon"],D("0.2004"))
        c=copy.deepcopy(self.c);c["loan"]["coupon"]=D("0.2004")
        self.near(cases.pricing(c)["economic_profit"],0)

    def test_extension_risk_fixed_sensitivity(self):
        r=cases.pricing(self.c,"extension")
        self.assertEqual(r["economic_profit"],D(-3650))
        self.assertEqual(r["expected_loss"],cases.pricing(self.c)["expected_loss"])

    def test_revolver_distinct_income_and_exposure_bases(self):
        r=cases.pricing(self.c,"revolver")
        self.assertEqual(r["average_drawn"],D(550000))
        self.assertEqual(r["ead"],D(630000))
        self.assertEqual(r["coupon"],D(16500))
        self.near(r["economic_profit"],"-4558.666666666667")
        self.near(cases.borrower(self.c,"revolver")["closing"],"403333.333333333333")

    def test_eir_reprices_contract_and_probabilities_sum(self):
        r=cases.cash_shortfall(self.c)
        self.near(cases.pv(D(515000),r["eir"],60),490000)
        self.assertEqual(sum(x["weight"] for x in r["rows"]),1)
        self.assertGreater(r["late_only_time_loss"],0)
        self.assertNotEqual(r["receipt_shortfall"],cases.pricing(self.c)["expected_loss"])

    def test_cash_shortfall_zero_when_all_pay_as_contracted(self):
        c=copy.deepcopy(self.c);c["credit"]["default_probability"]=D(0);c["credit"]["late_nondefault_probability"]=D(0)
        self.near(cases.cash_shortfall(c)["receipt_shortfall"],0)

    def test_full_cash_earnings_reconciles_to_margin_budget(self):
        r=cases.scenario_profit(self.c)
        self.assertEqual(r["expected_contribution"],D(-2100))
        self.assertEqual(r["expected_capital_charge"],D(1624))
        self.assertEqual(r["expected_economic_profit"],D(-3724))
        self.assertEqual(r["required_coupon"],D(".22655"))
        # Foregone coupon 600, extra funding 1200 and extra capital time 224.
        self.assertEqual(r["bridge_from_margin_budget"],D(-600)-D(1200)-D(224))
        c=copy.deepcopy(self.c);c["loan"]["coupon"]=r["required_coupon"]
        self.near(cases.scenario_profit(c)["expected_economic_profit"],0)

    def test_protection_no_double_recovery_and_payment_delay(self):
        r=cases.protection(self.c)
        self.assertEqual(r["guarantee_payment"],D(150000))
        self.assertEqual(r["claim_net"],D(147000))
        self.assertLess(r["gross_recovery"]+r["guarantee_payment"],D(500000))
        self.assertLess(r["incremental_nrv_at_default"],r["claim_net"])
        self.assertEqual(r["weaker_expected_loss"],D(16800))
        self.assertLess(r["expected_net_benefit_at_day_0"],D(880))

    def test_guarantee_cap_binds(self):
        c=copy.deepcopy(self.c);c["protection"]["cap"]=D(50000)
        self.assertEqual(cases.protection(c)["guarantee_payment"],D(50000))

    def test_no_future_evidence_or_outage_refresh(self):
        for t in (35,42):
            r=cases.evidence_state(self.c,t)
            self.assertEqual(r["last_verified"],0)
            self.assertEqual(r["recovery_fraction"],D(".4"))
        self.assertFalse(cases.evidence_state(self.c,35)["pending_verification"])
        self.assertTrue(cases.evidence_state(self.c,42)["pending_verification"])
        self.assertEqual(cases.evidence_state(self.c,45)["recovery_fraction"],D(".2"))

    def test_workflow_cash_waits_for_settlement(self):
        e=cases.workflow_fixture()
        for t in range(50,56): self.assertFalse(cases.replay(e,t)["available_cash"])
        self.assertTrue(cases.replay(e,56)["available_cash"])

    def test_exact_duplicate_is_idempotent_but_collision_fails(self):
        e=cases.workflow_fixture()
        self.assertEqual(cases.replay(e,60),cases.replay(e+[copy.deepcopy(e[-1])],60))
        bad=copy.deepcopy(e[-1]);bad["bank_reference"]="DIFFERENT"
        with self.assertRaises(ValueError): cases.replay(e+[bad],60)

    def test_unapproved_execution_or_unreferenced_settlement_fails(self):
        with self.assertRaises(ValueError): cases.replay([dict(id="x",sequence=0,known_day=0,state="executed")],1)
        e=cases.workflow_fixture();del e[-1]["bank_reference"]
        with self.assertRaises(ValueError): cases.replay(e,60)

    def test_vintage_subtraction_is_not_cure(self):
        r=cases.vintage()
        self.assertEqual(r["original"],100);self.assertEqual(r["active"],95)
        self.assertEqual(r["difference_same_denominator"],15)
        self.assertEqual(r["currently_current_after90"],6)
        self.assertEqual(r["confirmed_three_month_current"],3)

    def test_pool_opening_capital_and_base_independent_totals(self):
        r=cases.pool(self.c)
        self.assertEqual(r["opening_sources"],D(5250000))
        self.assertEqual(r["total_receipts"],D(5150000))
        # Principal collected=5m; coupon=150k; fees=20k; note interest=50k.
        self.near(r["equity_profit"],80000)
        self.near(r["total_equity_cash"],830000)
        self.near(r["total_note_interest"],50000)

    def test_pool_period_and_principal_conservation_all_cases(self):
        for mode in ("base","delay","default"):
            r=cases.pool(self.c,mode)
            for row in r["rows"]:
                self.near(row["conservation_residual"],0)
                self.assertGreaterEqual(row["closing_cash"],0)
                self.assertGreaterEqual(row["closing_reserve"],0)
                for k in ("a","b"):
                    self.assertGreaterEqual(row["closing_notes"][k],0)
                    self.near(row["opening_notes"][k]-row["payments"][f"{k}_principal"],row["closing_notes"][k])
            self.near(sum(sum(row["payments"].values())+row["equity"] for row in r["rows"]),
                      r["total_receipts"]+self.c["pool"]["reserve"])

    def test_pool_delay_keeps_ultimate_receipts_but_reduces_equity(self):
        base,late=cases.pool(self.c),cases.pool(self.c,"delay")
        self.assertEqual(base["total_receipts"],late["total_receipts"])
        self.assertLess(late["total_equity_cash"],base["total_equity_cash"])
        self.assertEqual(late["rows"][0]["receipts"],0)
        self.assertTrue(late["rows"][0]["early_amortisation"])
        self.assertEqual(late["rows"][0]["equity"],0)

    def test_pool_default_excludes_asset_before_distribution(self):
        r=cases.pool(self.c,"default")
        self.assertEqual(r["rows"][0]["oc_before_collections"],1)
        self.assertTrue(r["rows"][0]["early_amortisation"])
        self.assertEqual(r["rows"][0]["equity"],0)
        self.assertEqual(r["rows"][1]["equity"],0)
        self.assertLess(r["total_equity_cash"],r["equity_invested"])

    def test_zero_default_recovery_still_reconciles(self):
        c=copy.deepcopy(self.c);c["credit"]["gross_recovery_fraction"]=D(0)
        r=cases.pool(c,"default")
        for row in r["rows"]: self.near(row["conservation_residual"],0)
        self.assertLess(r["total_equity_cash"],cases.pool(self.c,"default")["total_equity_cash"])

    def test_oc_threshold_is_strict(self):
        c=copy.deepcopy(self.c);c["pool"]["oc_trigger"]=D(10)/9
        self.assertFalse(cases.pool(c)["rows"][0]["early_amortisation"])
        c["pool"]["oc_trigger"]+=D('.000001')
        self.assertTrue(cases.pool(c)["rows"][0]["early_amortisation"])

    def test_early_reserve_priority_is_explicit(self):
        row=cases.pool(self.c,"default")["rows"][0]
        self.near(row["closing_notes"]["a"],"1473333.333333333333")
        self.assertEqual(row["closing_reserve"],D(240000))
        self.assertEqual(row["payments"]["b_interest"],D(10000))

    def test_fee_exhaustion_retains_arrears_without_negative_cash(self):
        c=copy.deepcopy(self.c);c["pool"]["fee_per_30_days"]=D(6000000)
        r=cases.pool(c)
        for row in r["rows"]:
            self.assertEqual(row["equity"],0)
            self.assertGreater(row["fees_due"],0)
            self.near(row["conservation_residual"],0)
            self.assertEqual(sum(v for k,v in row["payments"].items() if k!='fees'),0)

    def test_all_default_has_no_finite_coupon_hurdle(self):
        c=copy.deepcopy(self.c);c["credit"]["default_probability"]=D(1);c["credit"]["late_nondefault_probability"]=D(0)
        self.assertIsNone(cases.scenario_profit(c)["required_coupon"])

    def test_invalid_assumptions_fail_before_producing_results(self):
        for section,key,value in [("credit","default_probability",D("1.1")),("pool","equity",D(1)),
                                  ("revolver","limit",D(1)),("loan","term_days",61)]:
            c=copy.deepcopy(self.c);c[section][key]=value
            with self.assertRaises(ValueError): cases.run(c)

    def test_repeated_run_is_identical(self): self.assertEqual(cases.run(self.c),cases.run(self.c))


if __name__=="__main__": unittest.main(verbosity=2)
