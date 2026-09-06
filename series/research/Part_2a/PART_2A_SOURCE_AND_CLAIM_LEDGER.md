# Part 2a Source and Claim Ledger

Research cut-off: 6 September 2026.

## Purpose of this ledger

Part 2a explains how MSME operating events become time-correct, governed and reproducible credit evidence. It specifies the evidence interface consumed by Part 2b. It does not estimate the HLR, determine a regulatory decision, or claim that behavioural variables cause repayment.

## Verified source sequence

| Ref. | Source | Authority and role | Claims assigned to Part 2a |
|---|---|---|---|
| [1] | Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk* | Current international supervisory guidance | Credit administration, current borrower information, monitoring, controls and early identification require evidence after origination |
| [2] | Central Bank of Kenya, *2024 Survey Report on MSME Access to Bank Credit* | Primary Kenyan sector survey | Kenyan MSME product and information context; cash-flow fit; information capital and credit-scoring relevance |
| [3] | D. Caire and M. Fernandez Vidal, *Leveraging Transactional Data for Micro and Small Enterprise Lending* | Applied cross-market research | Transaction data may complement credit history; sales, expenses, orders and invoices can contain predictive repayment evidence; findings remain population-specific |
| [4] | Republic of Kenya, *Data Protection Act*, No. 24 of 2019 | Primary Kenyan legislation | Lawfulness, transparency, purpose limitation, minimisation, accuracy, retention and data protection by design |
| [5] | Republic of Kenya, *Data Protection (General) Regulations*, 2021 | Primary Kenyan regulations | Automated-decision transparency, meaningful logic, error prevention, human intervention, purpose limitation, minimisation and accuracy controls |
| [6] | Debezium, *Debezium Connector for SQL Server* | Official technology documentation | Committed row-level change capture; snapshots; duplicate-event possibility after failure; schema and source metadata |
| [7] | Apache Software Foundation, *Apache Kafka Documentation* | Official technology documentation | Event streams, keys and topic partitions; ordering is a partition-level property |
| [8] | Apache Software Foundation, *Streaming Analytics: Apache Flink* | Official technology documentation | Event time, processing time, watermarks, out-of-order events and reproducible event-time computation |
| [9] | Apache Software Foundation, *Flink SQL Joins* | Official technology documentation | Event-time temporal joins require versioned state, time attributes and tested late-record behaviour |
| [10] | Delta Lake Project, *Delta Lake Documentation* | Official technology documentation | ACID tables, schema enforcement, batch and streaming integration, and historical table versions |
| [11] | Delta Lake Project, *Change Data Feed* | Official technology documentation | Insert, update and delete change records, commit versions and timestamps, and retention constraints |
| [12] | OpenLineage, *Object Model* | Official open-standard documentation | Jobs, runs, datasets and facets provide a practical lineage vocabulary |
| [13] | Feast, *Point-in-Time Joins* | Official technology documentation | Historical feature retrieval scans backward from each entity timestamp within a defined TTL; point-in-time retrieval supports training-serving consistency |
| [14] | K. Cho et al., “Learning Phrase Representations Using RNN Encoder-Decoder for Statistical Machine Translation” | Original peer-reviewed method | GRU architecture as a possible recurrent encoder for ordered event histories |
| [15] | A. Vaswani et al., “Attention Is All You Need” | Original peer-reviewed method | Self-attention and Transformer architecture as a possible representation mechanism for longer sequences |
| [16] | V. Chernozhukov et al., “Double/debiased machine learning for treatment and structural parameters” | Original peer-reviewed method | Cross-fitting as sample splitting that prevents an observation from training the nuisance model used to generate its own representation; causal orthogonality requires additional score construction |
| [17] | Central Bank of Kenya, *Monthly Economic Indicators* | Primary Kenyan macroeconomic source | Monthly Kenyan monetary, banking and economic context is publication-driven rather than a high-frequency borrower stream |
| [18] | Central Bank of Kenya, *KESONIA Interest Rate Benchmark* | Primary benchmark source | KESONIA is published each business day for the preceding business day, demonstrating publication-time and effective-time separation |
| [19] | World Bank, *Indicators API Documentation* | Official multilateral data documentation | Versioned programmatic access to international indicator series and their metadata |
| [20] | International Monetary Fund, *IMF Data APIs* | Official multilateral data documentation | SDMX 2.1 and 3.0 interfaces for macroeconomic datasets |

## Claims approved for the manuscript

| Claim ID | Proposed claim | Classification | Source | Qualification |
|---|---|---|---|---|
| P2A-C01 | Credit monitoring needs current borrower and facility information after disbursement. | Supervisory principle | [1] | Does not prescribe one technology stack or data source. |
| P2A-C02 | Transaction histories can complement bureau and application evidence for defined MSE populations. | Applied empirical proposition | [2], [3] | Foreign case studies do not establish Kenyan effect sizes or universal transferability. |
| P2A-C03 | A behavioural feature is usable only when its purpose, provenance, calculation, availability time and missingness rule are defined. | Canonical implementation requirement | [4], [5], [12], [13] | The exact lawful basis and purpose remain institution-specific. |
| P2A-C04 | Event time, source commit time, ingestion time, decision time and outcome maturity answer different questions. | Canonical temporal definition | [6], [8], [13] | Additional effective, publication, correction and posting times may be required by source. |
| P2A-C05 | A record may be economically effective before it is available to the lender, or corrected after the decision. | Temporal proposition | [6], [8], [11], [15] | Historical reconstruction must use what was available, not the latest corrected value. |
| P2A-C06 | CDC can capture committed database changes, but replay may produce duplicates. | Official implementation fact | [6] | Idempotency and reconciliation remain application responsibilities. |
| P2A-C07 | Kafka ordering is scoped to a topic partition. | Official implementation fact | [7] | Stable entity keys, producer configuration and downstream sequencing are still required. |
| P2A-C08 | Watermarks express progress in event time and govern treatment of out-of-order records. | Official implementation fact | [8] | Watermark policy is a design choice with timeliness and completeness trade-offs. |
| P2A-C09 | Temporal joins need versioned reference state and explicit late-data tests. | Official implementation fact | [9] | Syntax and supported semantics depend on the connector and Flink release. |
| P2A-C10 | Historical table versions aid reconstruction but do not prove upstream accuracy or lawful usability. | Qualified implementation synthesis | [4], [10], [11] | Transactional storage is not a substitute for source reconciliation or a statutory ledger. |
| P2A-C11 | Explicit lifecycle features should have one engineered owner and one definition. | Canonical model-governance requirement | [3], [12], [13] | Raw events may feed more than one branch, but a named engineered metric should not be duplicated silently. |
| P2A-C12 | AI sequence representations may capture residual ordering and interaction information after explicit variables are assigned. | Testable modelling proposition | [14], [15] | Value must be established out of time against simpler baselines. |
| P2A-C13 | Cross-fitted residualisation reduces self-fitting and linear redundancy with explicit variables. | Statistical implementation proposition | [16] | It is not automatically Neyman-orthogonal, causal, independent or free of nonlinear redundancy. |
| P2A-C14 | Low-frequency context must preserve observation, publication, revision and decision availability dates. | Data-governance requirement | [17]-[20] | Release cadence varies across sources and series. |
| P2A-C15 | Missingness may be operationally informative but must not be assigned an economic meaning without testing. | Testable modelling proposition | [4], [5] | A data outage, borrower inactivity and lender non-participation are distinct states. |
| P2A-C16 | The online scoring view and offline training view must be validated for semantic equivalence. | Model-risk control | [10]-[13] | Equality is evaluated on approved sample events, tolerances and versions, not assumed from shared feature names. |

## Canonical clock register

| Clock | Symbol | Meaning | Example |
|---|---|---|---|
| Economic event time | `T_event` | When the underlying business or payment event occurred | Customer paid an invoice at 10:14 |
| Effective time | `T_effective` | When a state or rule applies economically or contractually | A new repayment schedule becomes effective on Monday |
| Source commit or posting time | `T_commit` | When the source system committed or posted the record | The core ledger allocated the receipt at 10:18 |
| Ingestion time | `T_ingest` | When the analytical platform received the event | CDC record reached the controlled stream at 10:19 |
| Publication time | `T_publish` | When an external observation became public | CBK published the preceding day's benchmark at 09:00 |
| Decision time | `T_decision` | The cutoff for a specific model or policy decision | A limit review ran at 10:20 |
| Correction time | `T_correct` | When a source revision or error correction became available | A reversed payment was corrected next day |
| Outcome-maturity time | `T_mature` | When enough follow-up exists to assign the outcome | A 90-day durable-cure label matures after 90 days |
| Cash-realisation time | `T_cash` | When collection or recovery cash is actually received and cleared | Recovery proceeds cleared on settlement date |

## Feature ownership rules

1. Every feature has a business definition, unit, numerator, denominator, window, zero-denominator rule, owner, source, clock, availability timestamp, missingness rule, version and permitted purpose.
2. The explicit lifecycle path owns named financial and servicing metrics such as repayment velocity, cash-flow asymmetry, debt-service coverage, debt-to-liquidity, utilisation pressure, buffer days, arrears transitions and fulfilled promises.
3. The AI path receives authorised raw or minimally transformed sequences and produces cross-fitted representations. It does not receive duplicate copies of the named explicit metrics unless a pre-registered challenger experiment tests that design.
4. Residual AI representations are projected against the explicit design matrix on training folds. Optional whitening may improve numerical conditioning within the residual block.
5. The production feature service serves an approved versioned artefact. Training, backfilling, correction and online scoring preserve separate operational states.

## Claims held for later parts

- HLR likelihood, Pólya-Gamma inference, P-spline priors, regularised horseshoe and hierarchical effects: Part 2b.
- Automated decision rights, adverse-action explanation, customer safeguards and Kenyan regulatory orchestration: Part 3.
- Bank-controlled sandbox, privacy-enhancing computation and system integration: Part 4.
- KESONIA customer pricing, ECL, economic capital, ALM, FTP, reserves and risk transfer: Part 5.
- Randomised pilots, quasi-experimental estimands, power and scale-up: Part 6.

## Excluded claims

- More data necessarily produce better or fairer credit decisions.
- Transaction data are equivalent to audited financial statements.
- A point-in-time feature-store call guarantees freedom from leakage.
- Delta time travel reconstructs information that was not retained or proves source truth.
- Watermarks recover every late event without a stated policy.
- Kafka provides global ordering across a topic.
- Neural representations are inherently superior to explicit features.
- Residualisation makes an embedding causal, statistically independent or fully orthogonal in every nonlinear sense.
- Public aggregate data can substitute for account-level lifecycle data.
- A specific latency target is a property of the architecture before measurement under load.
