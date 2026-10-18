# Moniepoint cash flow case

This reproducible synthetic case implements transaction provenance, point-in-time cash capacity, Bayesian cash uncertainty, dated facility terms, simulated maker–checker approvals, receipts, repeat lending and workout. Currency is KES. The scenario assumptions are original teaching inputs, with Moniepoint used as an industry application.

Run from the repository root:

```powershell
python -B research_lab/moniepoint_cashflow_case/run_case.py
python -B -m unittest discover -s research_lab/moniepoint_cashflow_case -p test_model.py -v
python -B research_lab/moniepoint_cashflow_case/build_charts.py
```

The numerical engine uses Python standard-library functions. Charts additionally use Pillow and Windows Arial. `--inputs path.json --output path` supports an alternative assumption set. The default parameters are exported as `output/moniepoint_cashflow_case_2026-10-18/inputs.json`.

Read the full case and derivation at [the narrative](../../docs/research/MONIEPOINT_REPRODUCIBLE_CASHFLOW_CASE_2026-10-18.md). Its source map identifies exact mature sections of Underwrite for Collection and the five-article research series.

## Key conventions

- Gross historical credits and verified operating cash are separate measures; transfers, financing, owner capital and reversals retain their source classes.
- Observed history ends at decision day 90. Later transactions and later-known classifications are excluded from that snapshot.
- The conjugate Normal model supplies a credible interval for mean cash and a wider predictive interval for next-month cash, with declared prior and noise assumptions.
- A KES30,000 facility requires three KES11,000 instalments. The policy cap, cash reserve and predictive shortfall threshold are author-selected inputs.
- Human roles are simulated decision fixtures. The event stream demonstrates proposals, independent checker approvals, execution receipts, monitoring and amended schedules.
- Repayments clear the oldest due instalment first; principal precedes fee within that instalment. Funding continues on unrecovered principal after default.
- Trading obligations continue to accrue as a contracted cash-calendar stress assumption. Unpaid trading bills, existing debt and household shortfalls are reported. This is a cash-calendar and decision model; inventory quantities and production constraints require their own extension.
- Repeat requests are prescribed fixtures. A live product assessment would additionally establish a renewed business purpose, financing gap and customer value.
- The rescheduled case preserves the household shortfall caused by delayed receipts. Lower contractual arrears and higher terminal cash must be read with that shortfall.
- Source-coverage deferrals have no observed loan outcome. They are retained separately from funded non-default observations.

## Output and validation

Ten scenario folders contain raw records, separate truth, classified transactions, coverage, account maps, decision snapshots, daily merchant cash, loan and instalment records, monitoring and versioned audit events. Scenario summaries, inputs and a source-hash verification manifest sit at the output root. Thirty-six tests check monetary reconciliation, temporal validity, source defects, cash uncertainty, review order, FIFO allocations and workout funding.

Whitepaper: https://doi.org/10.5281/zenodo.23343888.
