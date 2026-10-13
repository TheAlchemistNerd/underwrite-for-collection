# One order, several cash clocks

Reproducible companion to the **Underwrite for Collection master whitepaper, 1 October 2026 edition**. All data are hypothetical; the active bank lending case and the optional receivables vehicle have separate clocks and conventions.

[Open this research lab on GitHub](https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab). The two whitepaper appendices link directly to this directory.

## Run

Python 3.10+; standard library only. From the repository root:

```powershell
python -m unittest discover -s research_lab -p 'test_*.py' -v
python research_lab/run_cases.py
python research_lab/run_cases.py --check
```

The generator writes JSON results, the worked appendix, delimited case exhibits in the six active manuscripts and a SHA-256 reproduction manifest. Chapter updates are confined to labelled case blocks. Dates and source hashes are deterministic; all calculations run locally using the supplied files.

## Files

- `case_inputs.json`: dated operating, loan, credit, revolver, protection and pool assumptions.
- `cases.py`: Decimal cash ledgers, pricing, discounted receipts, workflow/evidence fixtures and static pool waterfall.
- `test_cases.py`: independent expected values, reconciliations, rejection and boundary cases.
- `appendix_template.md`: narrative and generated-table insertion points.
- `publication_baseline.sha256`: the exact input version reviewed with the published prose.
- `results/case_results.json`: unrounded canonical results, Decimal quantities serialised as strings.
- `results/reproduction_manifest.json`: source and output fingerprints, including the integrated chapter versions.
- `../series/appendices/WORKED_OPERATING_AND_FINANCE_CASE.md`: generated reading appendix.

To explore changed assumptions, edit a copy or temporarily change `case_inputs.json` and run `python research_lab/run_cases.py --results-only`. This writes a separately labelled local `results/scenario_results.json`. Restore the published inputs afterwards. To publish a revised case, review the narrative and fixed-value tests, update the baseline fingerprint, regenerate and review the full output. Extending the event clock also requires the dependent schedules and validation rules to be updated together.

## Financial conventions

All money is KES, loan coupon/funding/capital simple ACT/360, and recovery discounting effective ACT/365. The contractual EIR is solved separately. The margin budget recognises promised interest and scheduled funding; the lifetime cash-earnings exhibit reconciles coupon loss, extended funding and capital time. Each loss enters once. Institution application adds calibrated PD/LGD/CCF, an identified intervention evaluation, approved accounting and legal/capital treatment, and operational settlement interfaces.

The pool has ten loan receivables, two maturity batches, par purchase including all transferred interest, a funded reserve and sticky early amortisation. Reserve support in early amortisation covers expenses and interest, including junior interest; collection cash funds accelerated principal. The declared waterfall permits readers to evaluate alternative priorities. Extensions can add revolving purchases, foreign-currency flows, hedges and guarantee payments with their own cash and ownership records.

See appendix sections A1-A10 for full amounts, assumptions, application steps and accumulated-review provenance. All inputs needed to reproduce the published baseline are included in this repository.

## Governed evidence case U4C-GOV-001

`decision_case.py` and `decision_case_inputs.json` add a reconciled September cash history, a versioned operating-receipt classification, a governed 90-day amendment and protection review. `run_decision_case.py` reuses the primary borrower and pricing functions and produces the [governed appendix](../series/appendices/GOVERNED_EVIDENCE_AND_INTERVENTION_CASE.md). Its policies, actors and observed follow-up are synthetic.

```powershell
python research_lab/run_decision_case.py --write-appendix
python research_lab/run_cases.py
python research_lab/run_cases.py --check
python -m unittest discover -s research_lab -p 'test_*.py' -v
```

The local evidence outputs are under `output/governed_evidence_case_2026-10-01`. Input/code hashes, financial results and tests accompany the narrative. The original and governed cases share a single KES 250,000 opening balance: the prior-window transaction reconciliation supplies that balance without adding it a second time.

## Development provenance

The [internal review lineage](REVIEW_PROVENANCE.md) preserves the research-note references used to develop the cases. Public appendix explanations and references are self-contained.
