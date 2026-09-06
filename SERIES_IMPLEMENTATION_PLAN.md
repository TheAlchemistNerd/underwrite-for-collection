# Implementation Plan for the MSME Underwrite-for-Collection Series

## 1. Intended outcome

The project will produce a coherent six-part research series represented by seven labelled manuscripts. It will match the scale and depth of the Mwendo Pamoja Parts 1–6 while changing the unit of analysis from platform drivers and embedded-finance receivables to Kenyan MSMEs, their credit relationships, and the full banking ecosystem.

The work will not expand the existing LinkedIn article by simple accretion. The article supplies the governing intuition. The rough notebook supplies hypotheses, analogies, links, experimental ideas and unresolved questions. The KBA package supplies Kenyan policy relevance, public evidence and a nascent empirical specification. The modelling notes supply technical alternatives. The KESONIA material supplies pricing, accounting and treasury structure. The Mwendo manuscripts supply a comparator for depth, pacing, diagrams, equations and part-level scale.

Every manuscript will be independently readable and will also contribute to one cumulative argument: sustainable collection is an outcome of product design, evidence quality, model uncertainty, intervention choice, conduct, servicing, accounting and funding, not an isolated recovery function activated after arrears emerge.

## 2. Locked manuscript map and word counts

References and a shared glossary are excluded from the counts. Appendices, equations, tables, captions and diagram labels are included in the full-source count. Fenced code and Mermaid source are excluded from the editorial-prose count.

| Label | Working title | Full-source target | Editorial-prose target |
|---|---|---:|---:|
| Part 1 | Underwrite for Collection: The MSME Credit Lifecycle and Collection Cascades | 4,883 | 4,434 |
| Part 2a | Temporal Evidence, Behavioural Signals and Point-in-Time Feature Engineering | 7,191 | 6,348 |
| Part 2b | Hierarchical Bayesian Underwriting, Causal Identification and Lifecycle Dependence | 10,166 | 9,681 |
| Part 3 | Regulatory Orchestration, Fair Intervention and Collection Governance | 4,872 | 4,781 |
| Part 4 | Bank-Controlled Research Sandboxes and Enterprise Credit Architecture | 4,500 | 3,745 |
| Part 5 | KESONIA Pricing, Expected Credit Loss, Capital and Funding | 6,186 | 5,214 |
| Part 6 | Randomised Pilots, Quasi-Experiments and Ecosystem Execution | 5,155 | 4,592 |
| **Total** |  | **42,953** | **38,795** |

Drafting may temporarily range five percent above or below the targets. The technical-review draft must be within two percent. The publication candidate must be within one percent of the corresponding full-source target and must meet or exceed the editorial-prose target without padding.

## 3. Phase 0: corpus control and research design

The source corpus has been copied into the workspace and divided into four evidence layers. Before Part 1 drafting, the following registers will be active:

- a canonical definition and notation register;
- a source and citation index;
- a claim ledger distinguishing evidence, assumptions, proposals and calculations;
- a decision register for cross-part choices;
- an experimental-design register containing estimands, units, outcomes and safeguards;
- a word-count and quality ledger;
- a cross-part dependency map.

The rough notebook will be semantically decomposed rather than cited as authority. Each usable idea will be classified as a narrative insight, research hypothesis, candidate mechanism, methodological option, regulatory question, implementation proposition or source lead. Contradictory versions will be resolved in the registers before publication prose is drafted.

## 4. Part 1 phase: establish the economic and institutional problem

Part 1 will translate “underwrite for collection” into an MSME lifecycle thesis. It will begin with the operating reality of a small business whose sales, inventory, payroll, receivables, supplier terms, taxes and household withdrawals move on different clocks. A credit decision made from a static application snapshot can therefore be technically correct at origination yet structurally fragile during repayment.

The manuscript will distinguish willingness, capacity, timing, liquidity, solvency and recoverability. It will show how product tenor, instalment frequency, grace periods, covenants, security, guarantees, information cadence and servicing capacity shape future collectability. It will describe the ecosystem around the borrower: banks, credit-reference bureaus, payment providers, accountants, digital platforms, guarantors, DFIs, credit insurers, restructuring specialists, courts, regulators and representative bodies.

The central cascade diagrams will connect economic shocks to cash-flow compression, arrears, supplier disruption, tax or payroll stress, restructuring, default and recovery. A second diagram will show the constructive loop from observation to early support, durable cure and product redesign.

Part 1 will use aggregate KBA and CBK data carefully. Flow measures of new MSME lending will not be treated as denominators for sector-wide NPL stocks. The paper will use them to show that credit expansion and asset-quality pressure can coexist and require a lifecycle response.

The phase closes only when the research question, audience, definitions of collection and durable cure, ecosystem roles, and cross-references to Parts 2a–6 are stable.

## 5. Part 2a phase: build the evidence architecture

Part 2a will define the event-time and point-in-time data architecture required to observe an MSME credit lifecycle without leakage. Potential inputs include account transactions, loan ledgers, repayment allocations, invoices, merchant payments, payroll, tax records where lawfully available, inventory proxies, digital-platform activity, bureau events, servicing contacts, hardship indicators and macroeconomic releases.

The paper will separate exposure, stock, flow, state and outcome variables. It will document observation time, effective time, posting time, correction time and model-availability time. This is essential for reproducible training, fair back-testing and causal studies.

The feature architecture will contain two governed branches:

- explicit financial and lifecycle variables with interpretable definitions;
- cross-fitted AI neural sequence representations capturing residual temporal information.

Explicit variables will include cash inflow and outflow velocity, cash-flow asymmetry, debt-service coverage, debt-to-liquidity, utilisation, transaction volatility, reserve or buffer days, arrears transitions, repayment velocity, time since depletion, seasonality and sector-sensitive interactions. Neural embeddings will be residualised against the explicit design matrix before inclusion in the HLR. Alternative embedding geometry, B-spline–AR(1), B-spline–RW1 and neural architectures can be retained in appendices or challenger registers where they do not serve the central exposition.

The manuscript will also define bank-boundary data access, synthetic-data uses, missingness, revision lineage, feature ownership, data-quality fallbacks and the limitations of public aggregate data.

## 6. Part 2b phase: connect prediction, time and causal evidence

Part 2b will supply the deepest statistical treatment. Its primary prognostic model is a hierarchical Bayesian logistic regression with product, sector, institution, geography, cohort and time structure where justified. Governed P-splines represent nonlinear explicit effects. Cross-fitted residual AI representations enter through a regularised-horseshoe block. Pólya–Gamma augmentation supports offline conditionally conjugate inference while preserving hierarchical pooling.

The manuscript will define outcomes and horizons precisely. It will distinguish application default, missed-payment risk, transition to material arrears, cure, durable cure, re-default and net recovery. Posterior predictive checks, calibration, temporal validation, subgroup stability, sensitivity to prior scale and covariate-shift analysis will receive more weight than isolated coefficient intervals.

A multi-state or competing-risks challenger will model timing and state transitions. Copulas or other dependence structures may represent correlated sector, geographic, supply-chain or macroeconomic shocks where data supports them. Structural, intensity, frailty, POMDP, bandit and Hawkes approaches will be located according to the question they answer rather than assembled into one undifferentiated model.

The causal half of the manuscript will define potential outcomes, estimands, treatment assignment, interference, noncompliance, attrition and selective labels. It will explain why approved-only performance data create selection problems and how controlled exploration, reject inference diagnostics, regression discontinuity, instrumental variables or other designs may help under explicit assumptions.

The phase ends with a clean interface: prognostic posterior plus uncertainty enters the policy gate; experimentally estimated treatment effects inform intervention choice; neither object silently substitutes for the other.

## 7. Part 3 phase: make intervention lawful, fair and operational

Part 3 will organise actions across origination, monitoring, servicing, hardship, restructuring, collection and recovery. It will distinguish information interventions, reminders, repayment-date alignment, temporary payment relief, tenor extension, limit reduction, restructuring, referral and legal recovery.

Each action will have eligibility, authority, expected mechanism, contraindications, customer communication, human-review rights, outcome metrics, monitoring and stop rules. The analysis will cover the Data Protection Act, digital-credit and banking requirements, consumer protection, adverse-action explanation, contact conduct, complaint handling, vulnerability, fairness and model governance using current primary Kenyan sources.

Randomised pilots will test only lawful options under genuine uncertainty. Conventional controlled designs will precede adaptive optimisation. Quasi-experimental studies will be used when the assignment rule and identification conditions make them credible. The paper will treat contact burden, complaint incidence, business continuity and re-default as first-class outcomes alongside repayment.

## 8. Part 4 phase: locate the programme inside bank controls

Part 4 will specify a bank-controlled research sandbox and production pathway. It will define environments for synthetic development, de-identified exploration, secure institution-level analysis, shadow scoring, restricted pilots, model validation and controlled deployment.

The enterprise design will identify systems of record for customer, facility, limit, schedule, payment, delinquency, collection action, restructuring, complaint, ECL and accounting events. It will show event ingestion, point-in-time feature generation, model registry, posterior artifact approval, policy execution, case management, experiment logging, disclosure control, maker-checker approval and audit lineage.

Model-to-data is the default collaboration pattern. Federated learning, clean rooms, enclaves, trusted execution, secure aggregation and differential privacy will be evaluated against the actual partnership and threat model rather than offered as decorative technologies.

The manuscript will provide an ecosystem responsibility matrix covering the bank, technology or research partner, KBA, relevant regulators, independent validator, ethics or conduct oversight, DFI or guarantee partner, data providers and MSME representatives.

## 9. Part 5 phase: reconcile risk with pricing, accounting and funding

Part 5 will connect the lifecycle evidence to customer pricing, IFRS 9, economic capital, liquidity, ALM, FTP and risk transfer. It will use current CBK and KBA material and preserve the distinction among:

- KESONIA as a time-varying reference benchmark;
- the regulated risk-based customer premium;
- expected loss;
- operating and servicing costs;
- regulatory and economic capital;
- liquidity and maturity cost;
- bank FTP;
- guarantee, insurance or securitisation costs;
- investor or shareholder return.

The ECL section will map lifecycle states and forward-looking scenarios into PD, LGD, EAD, staging, modifications, recoveries and overlays. It will explain why a causal intervention result may change projected cash flows without automatically changing governance-approved accounting models.

The capital section will distinguish regulatory requirements from an internal economic-capital distribution. The funding section will use repricing ladders, behavioural tenor, collection lags, prepayment, default and recovery to quantify mismatch. Frequent collections will be treated as an empirical cash-flow feature rather than assumed liquidity.

Risk-transfer alternatives may include guarantees, credit insurance, first-loss protection, synthetic or funded structures and a ring-fenced receivables vehicle where legally and commercially appropriate. Their pricing and monitoring will depend on gross and net loss distributions, attachment, exhaustion, counterparty risk, basis risk, claims or call procedures, recoveries and moral-hazard controls.

## 10. Part 6 phase: convert the architecture into a credible programme

Part 6 will define a staged route from research question to bank adoption:

1. Ecosystem scoping and governance.
2. Public-data baseline and synthetic prototype.
3. Institutional data partnership and secure environment.
4. Retrospective point-in-time validation.
5. Prospective shadow operation.
6. Restricted randomised or quasi-experimental pilot.
7. Independent validation and conduct review.
8. Controlled scale-up.
9. Ongoing monitoring, publication and policy feedback.

The experimental protocol will specify cluster or individual randomisation, stratification, power, minimum detectable effect, delayed outcomes, contamination, spillovers, noncompliance, attrition, multiplicity, interim review and stop rules. Quasi-experimental alternatives will be pre-specified for interventions that cannot be randomised.

The manuscript will propose engagement with relevant banks and the wider ecosystem without implying commitments that do not exist. It will separate an internal bank research environment from any regulatory approval or sandbox pathway. Publication plans will distinguish synthetic feasibility results, aggregate public evidence and institution-derived results subject to disclosure and partner approval.

## 11. Cross-part diagrams and quantitative continuity

The series will use a consistent visual language. At minimum, it will maintain:

- one end-to-end lifecycle diagram;
- one MSME cash-flow and collection cascade;
- one point-in-time data and feature architecture;
- one prediction–causation–policy separation diagram;
- one multi-state credit-lifecycle diagram;
- one regulatory and intervention control stack;
- one bank-controlled research and deployment architecture;
- one KESONIA–pricing–ECL–capital–funding reconciliation;
- one phased ecosystem pilot roadmap.

Quantities and symbols will be registered once. If a symbol must change, all accepted parts will be reviewed through the decision register.

## 12. Review gates

Each part passes through six gates:

1. **Scope gate:** its question, audience, narrative and dependencies are fixed.
2. **Evidence gate:** material claims have authoritative sources or are labelled proposals.
3. **Technical gate:** definitions, equations, estimands and computations are dimensionally and statistically coherent.
4. **Regulatory gate:** law, guidance, contract, policy and recommendation are distinguished.
5. **Narrative gate:** the manuscript remains human, constructive and readable.
6. **Production gate:** citations, figures, tables, word counts and rendering pass automated and visual checks.

Acceptance of a part creates a baseline. Later improvements are applied through controlled amendments, not untracked rewrites.

## 13. Immediate next action

Parts 1 through 5 now have first complete drafts supported by part-specific outlines, claim ledgers and validation reports. The next authoring phase is Part 6. It will convert the architecture into a staged research and implementation programme covering synthetic rehearsal, bank-controlled retrospective validation, shadow scoring, randomised and quasi-experimental pilots, ecosystem governance, scale-up gates and final publication evidence.
