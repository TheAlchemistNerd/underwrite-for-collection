# Underwrite for Collection: MSME Lifecycle Credit Research Series

[IFoA practical-application review](series/research/IFOA_PRACTICAL_APPLICATION_REVIEW_2026-10-03.md) · [AI, bandits, reinforcement learning and Treasury review](series/research/AI_BANDITS_RL_AND_TREASURY_REVIEW_2026-10-04.md). These notes identify existing evidence and proposed development requirements.

This workspace develops **Underwrite for Collection** from a practitioner article into a six-part Kenyan MSME credit-research series issued as seven manuscripts: Part 1, Part 2a, Part 2b, Part 3, Part 4, Part 5, and Part 6.

The series asks a practical question:

> How should banks and their ecosystem partners design MSME credit backward from sustainable collection, while using behavioural evidence, causal experimentation, Bayesian uncertainty, responsible AI, KESONIA-linked pricing, accounting, capital, and funding controls coherently across the credit lifecycle?

The work is independent of the Mwendo Pamoja white paper. Copies of the Mwendo manuscripts are retained only as structural and quality comparators. Their source files are not edited from this workspace.

## Directory map

```text
behavioural credit scoring - underwrite to collect rct/
├── In the spirit of underwriting to collect.md
├── UNDERWRITE_FOR_COLLECTION_SIDE_BY_SIDE_SEMANTIC_ANALYSIS.md
├── README.md
├── SERIES_CHARTER.md
├── SERIES_IMPLEMENTATION_PLAN.md
├── SOURCE_MANIFEST.md
├── source_library/
│   ├── 00_anchors/
│   ├── 01_kba_research_package/
│   ├── 02_credit_risk_research/
│   ├── 03_kesonia_enterprise_and_funding/
│   └── 04_structural_comparators/
└── series/
    ├── briefs/
    ├── governance/
    ├── parts/
    ├── references/
    └── research/
```

## Working sequence

The manuscripts will be developed sequentially. Work on a later part may identify a dependency, but it will not silently rewrite an accepted earlier part. Material changes will be recorded in the decision register and reconciled deliberately.

1. Part 1: the MSME economic setting, collectability thesis, lifecycle and ecosystem.
2. Part 2a: temporal data, exposure, point-in-time evidence and feature architecture.
3. Part 2b: hierarchical Bayesian prediction, survival, dependence and causal identification.
4. Part 3: interventions, regulation, consumer protection and collection governance.
5. Part 4: bank-controlled research environments, enterprise integration and model operations.
6. Part 5: KESONIA pricing, ECL, capital, liquidity, ALM and funding economics.
7. Part 6: randomised pilots, quasi-experiments, partnerships, scale-up and publication.

The brief for each manuscript is in `series/briefs`. Draft manuscripts will be created in `series/parts` only when their phase begins.

## Preservation rule

Files under `source_library` are frozen research copies. They must not be edited. Corrections, reconciliations, new claims and manuscript prose belong in `series`. The original rough notebook remains a research reservoir rather than a publication draft.

## Repository reconciliation

The standalone repository is now the authoritative working location. See [the migration record](MIGRATION_2026-09-26.md) for the restored series layout and transferred reviews.

## Reproducible worked case: 1 October 2026

The active series now includes one connected MSME operating and finance case, with chapter exhibits and a full [worked appendix](series/appendices/WORKED_OPERATING_AND_FINANCE_CASE.md). The [standard-library case lab on GitHub](https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab) reproduces the borrower ledger, margin-to-cash-earnings bridge, discounted receipts, protection, verification/workflow examples and optional receivables waterfall. All inputs are hypothetical.

Run the tests and exact-regeneration check described in the lab before rebuilding the [master whitepaper](series/build/README.md). Generated PDF/HTML exports remain local; source, tests and canonical numerical outputs are versionable.

## Governed evidence and intervention case

The [Part 3 companion appendix](series/appendices/GOVERNED_EVIDENCE_AND_INTERVENTION_CASE.md) connects bank-cash provenance, evidence review, affordability, permission, contract booking and observed settlement. It uses the same opening cash and loan as the finance case. Parts 3 and 5 contain linked exhibits; both appendices enter the master HTML/PDF build.

Run `python research_lab/run_decision_case.py --write-appendix`, then `python research_lab/run_cases.py` and the checks in the lab README before publication. The first command regenerates the governed example; the second refreshes the primary case's whole-chapter fingerprints after integration.

**Worked-case reader update, 13 October 2026:** the two appendices, six operating-case exhibits and two governance summaries now link to the public research lab. Their descriptions state the assumptions, results and practical institution-application steps. The master PDF rebuilds as `Underwrite_for_Collection_MSME_Credit_Lifecycle_Whitepaper.pdf`.
