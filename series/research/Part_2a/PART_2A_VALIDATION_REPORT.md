# Part 2a Validation Report

Validation date: 6 September 2026.

## Artifact

Canonical manuscript:

`series/parts/Part_2a_Temporal_Evidence_and_Feature_Engineering.md`

Supporting records:

- `PART_2A_SOURCE_AND_CLAIM_LEDGER.md`
- `PART_2A_DETAILED_OUTLINE.md`

## Scope and size

| Test | Result |
|---|---|
| Full-source body count, excluding References | 7,191 words |
| Planned full-source benchmark | 7,191 words |
| Editorial body count, excluding fenced code and Mermaid source | 6,604 words |
| Abstract | Present |
| Numbered substantive sections | 9 |
| Conclusion | Present |
| Mermaid diagrams | 3 |
| Pandoc table nodes | 3 |
| Fenced code blocks, including Mermaid | 4 |

The full-source body count matches the locked Part 2a benchmark exactly. Editorial prose runs 256 words above the reference editorial count because the new version adds the canonical clock register, privacy boundary, bitemporal reconstruction logic and feature-serving contract.

## Citation tests

| Test | Result |
|---|---|
| Body first appearances | `[1]` through `[20]` in ascending order |
| Reference entries | Exactly `[1]` through `[20]` |
| Body citations without entries | None |
| Reference entries without body citations | None |
| Duplicate reference numbers | None |
| Reference page break | Present |
| Reference paragraph separation | Every entry begins a separate paragraph |

Sources follow the project authority order. Kenyan law, CBK material and international supervisory guidance support legal, sector and monitoring claims. Original research supports GRU, Transformer and cross-fitting propositions. Official product documentation supports implementation capabilities and their limitations.

## Semantic and architecture tests

- Part 2a defines evidence and feature engineering; it does not estimate the HLR or issue customer actions.
- Event, effective, commit, ingestion, publication, decision, correction, outcome-maturity and cash-realisation clocks are distinct.
- Point-in-time eligibility requires availability as well as an event timestamp.
- Source corrections preserve the historical version known by the earlier decision.
- Public aggregate context is not substituted for account-level lifecycle data.
- Product subledgers, payment ledgers and originating external authorities retain their assigned evidential authority.
- The feature store is not described as the statutory or contractual system of record.
- CDC is limited to suitable database sources and duplicate replay is controlled explicitly.
- Kafka ordering is stated at topic-partition level.
- Watermarks are described as lateness policy rather than a completeness guarantee.
- Historical table versions and row-level point-in-time joins are distinguished.
- Named explicit lifecycle metrics have one engineered owner.
- Artificial intelligence is introduced after behavioural-scoring purpose and is treated as a challenger.
- Cross-fitting is entity and time aware.
- Residualisation is described as linear redundancy control, not causal orthogonalisation or statistical independence.
- KESONIA is used only as a publication-clock example; pricing remains in Part 5.
- Missingness cannot silently become an adverse borrower value.
- Training, shadow, production and backfill modes are separate.
- Part 2b receives a versioned evidence object containing explicit features, residual AI representation, masks, clocks, versions and lineage.

## Format and parser tests

| Test | Result |
|---|---|
| Pandoc Markdown plus dollar-delimited TeX parsing | Passed |
| Table recognition in Pandoc AST | Three tables recognised |
| Balanced fenced blocks | Passed |
| Em dashes | Zero |
| Figure numbering | Figures 1, 2 and 3 in order |
| Heading numbering | Sections 1 through 9 in order |

The installed Mermaid CLI could not complete visual rendering because its bundled Puppeteer session closed with a protocol error. The same failure occurred for a two-node smoke-test diagram, so it is an environment-level renderer fault rather than evidence of manuscript-specific syntax failure. Visual Mermaid and PDF QA remain a build-stage check when the renderer environment is repaired or the series compilation pipeline is invoked.

## Acceptance status

**Accepted as the first complete Part 2a manuscript draft.**

The next writing phase may begin with Part 2b after the user confirms progression. Later changes should be limited to cross-part reconciliation, source updates or evidence-backed editorial improvements recorded in the decision register.
