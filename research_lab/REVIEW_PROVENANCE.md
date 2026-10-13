# Internal development provenance for the worked cases

The public appendices explain the cases through their own assumptions, equations, records and main-whitepaper section references. This file preserves internal research lineage and technical reproduction details.

## Operating and finance case

- `series/research/ADDITIONAL_PRICING_REVIEW_AND_CONTENT_PLAN_2026-09-25.md`: money-based pricing, funding time, borrower affordability and the optional receivables extension.
- `series/research/COLLECTABILITY_FEEDBACK_AND_CONTINUOUS_REVERIFICATION_2026-09-25.md`: evidence freshness, borrower and collateral re-verification, accountable action.
- `series/research/PART_5_TREASURY_SEMANTIC_GAP_ANALYSIS.md`: settlement cash, expected-loss/profitability distinctions, FTP and reserve recognition.
- `series/research/ADDITIONAL_REVIEW_PRICING_AND_TREASURY_2026-09-23.md`: earlier review context; existing local review retained separately.
- Prior cross-project worked-case and owner-earnings reviews supplied the order ledger. The chosen values are preserved in the input file so reproduction does not depend on those external files.

Part 1 receives the operating-order exhibit; Part 2a the knowledge-time exhibit; Part 2b the cure and cash-outcome distinction; Part 3 the controlled-extension example; Part 4 the replay boundary; Part 5 the price-to-cash-earnings bridge and optional-pool results. This appendix is an additional input to the **master whitepaper build**.

## Original technical reproduction notes

The companion directory is `research_lab`. It uses Python 3.10 or later and the standard library. From the repository root:

```powershell
python -m unittest discover -s research_lab -p 'test_*.py' -v
python research_lab/run_cases.py
python research_lab/run_cases.py --check
```

`case_inputs.json` contains editable financial assumptions. The current event graph intentionally fixes 60-day maturity, a 90-day late receipt, day-180 recovery and day-240 guarantee payment. Unsupported timing changes fail validation instead of silently leaving parts of the case on the old clock. Changing the event graph requires changes to its schedules and tests. The prose describes the published baseline; a fingerprint prevents changed inputs from being silently published beside that prose. For sensitivity runs use `python research_lab/run_cases.py --results-only`, which writes numeric results separately. For a new published calibration, revise any affected prose, tests and the baseline fingerprint as well as the inputs.

`cases.py` computes the ledgers. `test_cases.py` verifies independent cash totals, a solved pricing hurdle, EIR repricing, timing sensitivity, evidence availability, workflow failures, vintage denominators and pool conservation. `run_cases.py` writes deterministic JSON, this appendix and source hashes; `--check` compares regenerated outputs byte for byte. The generator also refreshes only its labelled case blocks in the six active manuscripts when they are present. Historical source-library editions are not modified.


## Governed evidence case

The design draws on `series/research/ECONOMIC_CASH_PROVENANCE_AND_ENTITY_RESOLUTION_IMPLEMENTATION_PLAN.md`, sections 3, 6, 8 and 10, and `series/research/COLLECTABILITY_FEEDBACK_AND_CONTINUOUS_REVERIFICATION_2026-09-25.md`, section 5. These are development records; the public appendix states the resulting principles and evidence directly.

From the repository root:

```powershell
python research_lab/run_decision_case.py
python -m unittest discover -s research_lab -p test_decision_case.py -v
```

The generator reads `decision_case_inputs.json` and the primary `case_inputs.json`, calls the existing borrower/pricing functions, writes exact Decimal JSON results and this narrative, and records test evidence and input/code hashes. The fixture covers two controlled accounts, exact-value transfer/reversal pairing and one 90-day amendment. Further entity graphs, partial/multi-hop transfers and product amendments can extend these rules with their own tested contracts.

Baseline files are `decision_case.py`, `decision_case_inputs.json`, `test_decision_case.py`, `run_decision_case.py` and `decision_case_publication_baseline.json`. Outputs are written under `output/governed_evidence_case_2026-10-01/`. `--write-appendix` refreshes this canonical appendix after successful validation. `--check` compares exact regenerated results, narrative, frozen fixture and validation hashes with the existing output files.

The publication fingerprint covers both input documents. If either changes, normal prose generation stops so fixed explanatory examples cannot become stale. `--results-only --output output/my_governance_scenario` recalculates a changed fixture into a separate directory without publishing baseline narrative. Custom results retain the engine's reconciliation and event controls; baseline numerical regression tests are reported only when both inputs match the publication baseline.


## Public-reader revision

1 October 2026: remove internal Markdown filenames and project-planning references from the two new appendices. Retain complete financial assumptions, equations, ledgers, decision records, validation logic and within-whitepaper reading guides. Numerical inputs and financial algorithms are unchanged. The lab README remains the technical entry point.

## Reader-facing update, 13 October 2026

Both appendices and all six generated chapter exhibits now link to the [public research lab](https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab). The narrative states assumptions, calculation scope and institution-application steps constructively. Input values, financial algorithms and expected numerical results are preserved. Canonical sources generate the Markdown, HTML and same-name master PDF.
