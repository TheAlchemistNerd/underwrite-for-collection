# From Transactions to Accountable Credit Decisions
## A financial-domain specification for governed AI, sustainable cash-flow lending and the five-article research programme

### Abstract

Cash-flow lending becomes operational when each recommendation can be traced from an economic event through a dated evidence snapshot, financial calculation, approved policy and realised outcome. This article builds that domain model from *Underwrite for Collection*, its five-article research series and the reproducible Moniepoint merchant case. It defines what the system must understand about transactions, business cash, obligations, facility terms, interventions, selection, recoveries, funding and customer outcomes. A synthetic example traces KES500,000 of gross credits to KES25,000 of monthly residual cash, then to an illustrative facility and scenario-level lender contribution. The five articles supply different methods for controlled credit-offer experiments, sequential collections, reject inference, Treasury control and bank-governed agents. Together they form a connected research and implementation programme while retaining separate estimands, services and decision authority. The objective is a practical bank system whose financial outputs are reproducible, whose uncertainty is visible, and whose actions can be reviewed and linked to actual cash outcomes.

### Research questions

1. How should heterogeneous transaction records become a dated, reproducible measure of business repayment capacity with source provenance and uncertainty?
2. How should experiments, sequential intervention learning and reject-inference research work together while answering distinct causal and predictive questions?
3. What financial contracts connect borrower decisions to portfolio and Treasury views while preserving review authority, customer outcomes and auditability?

## 1. Start with the question the five articles develop

The practical question behind *Underwrite for Collection* is whether a facility’s structure and continuing management support sustainable repayment from cash a borrower can generate. A lender therefore needs more than a static score or high account turnover. It needs an evidence chain from enterprise activity to the amount and date of available cash, from that cash to contractual payments, and from the payments to servicing, recovery and borrower outcomes. That chain is the financial backbone around which an AI workflow can coordinate. The system’s first job is to represent the business and facility accurately; its next job is to help authorized people use that representation consistently. [1]

The five articles extend the problem in sequence: experiments and contextual offers (Article 1), sequential collection (Article 2), selected repayment labels (Article 3), Treasury and ALM (Article 4), and bank-controlled orchestration (Article 5). The Moniepoint case supplies a transaction-to-decision example. These methods can share identifiers and governed aggregates, while retaining separate estimands, assumptions and decision authority. [2], [3]

## 2. Represent the business before calculating capacity

The first object is an economic entity. A merchant may trade through bank, wallet, POS, marketplace and cash channels. Records identify the merchant, owner, controlled accounts, counterparties and data providers, with evidence and review status for each link. A proposed match carries confidence and source references for confirmation or correction. Keeping unresolved relationships visible preserves the distinction between trading receipts, owner funding, related-party transfers and financing.

Each event needs economic, settlement, system-receipt and classification-known times. A sale may occur Monday, settle Tuesday, arrive Wednesday and be recognized as a transfer on day 96. A day-90 decision uses only its then-available classification; a later correction creates a new snapshot. This supports replay and evaluation against evidence genuinely available at decision time.

The event taxonomy separates receipts, refunds, reversals, owner capital, loan proceeds, transfers, supplier and operating payments, household needs, taxes, existing debt and facility cash. It supports three views: movements in the cash ledger, recurring business income and costs, and repayment capacity after obligations and liquidity buffer. Loan proceeds create a liability; controlled-account transfers consolidate to zero; a reversal corrects its original event. Encode these identities in versioned calculations.

Financing a going concern uses ongoing cash generation, working capital, obligations, owners and operations. A ring-fenced receivables stream adds receivable eligibility, obligor concentration, dilution, legal transfer and enforceability, account control, servicing continuity, reserves and waterfall. The Moniepoint case models business cash flow; the whitepaper also develops receivables mechanics. [1], [3]

For each receivable, record the originator, obligor, servicer, account controller, transfer evidence and reconciliation owner. These fields support enforceability and waterfall testing.

## 3. Reproduce the Moniepoint cash bridge

The case uses three completed months for one synthetic merchant. In the last month, gross credits total KES500,000: KES410,000 is verified trade receipt, KES45,000 is owner capital, KES30,000 is borrowing, and KES15,000 is correction credit matched to a reversal debit. A further KES50,000 transfer between controlled accounts nets to zero in the consolidated view. A duplicate event ID is counted once. A missing wallet month fails the coverage gate. A receipt classification learned on day 96 enters a later snapshot. The model-visible records and synthetic truth file are separate, allowing the test harness to verify classification while reproducing the information set available on day 90. [3]

The latest monthly residual is calculated as:

**C = KES410,000 − KES270,000 − KES70,000 − KES20,000 − KES25,000 = KES25,000.**

Here C is operating cash after supplier commitments, operating expenses, household needs and existing debt, before the proposed facility. The prior three monthly residuals are KES20,000, KES30,000 and KES25,000. This measure is distinct from gross account credits, accounting profit and next month’s certain cash. It becomes useful when a lender can identify its source window, coverage, class rules and date cutoff, and can place prospective dues against the actual receipt calendar.

Static checks reconcile account totals, duplicates and paired transfers. A rolling average summarizes a declared window, while a cash-floor rule protects a stated reserve. Define each measure’s currency, cutoff, coverage, missing-day and seasonal treatment, and version. A rolling average describes activity; a threshold is policy; a posterior interval quantifies uncertainty; a causal estimate measures an intervention effect. Keep the types distinct.

## 4. Make uncertainty useful to the reviewer

The teaching case fits a simple Bayesian model to three residual observations Cₘ. It assumes conditionally independent Normal observations with fixed σ = KES8,000 and prior μ ∼ Normal(m₀, s₀²), where m₀ = KES25,000 and s₀ = KES15,000. The posterior update is:

**vₙ = (1/s₀² + n/σ²)⁻¹**

**mₙ = vₙ(m₀/s₀² + Σₘ Cₘ/σ²)**

**μ | C ∼ Normal(mₙ, vₙ),   Cₙ₊₁ | C ∼ Normal(mₙ, σ² + vₙ).**

The posterior mean is KES25,000. Its 95% credible interval is KES16,348–33,652; the 95% predictive interval for next-month cash is KES7,091–42,909. The predictive interval is wider because it includes future monthly variation as well as uncertainty about the mean. Under these assumptions, the probability that next-month residual cash falls below KES11,000 is 6.27%; the probability it falls below KES35,000 is 86.31%. Interpret each as conditional on the stated observation window, model assumptions and source quality. [3]

The example’s declared decision rule caps the proposed payment at 50% of posterior mean cash, KES12,500, requires a complete source window and dated cash-calendar pass, and sets a 10% maximum predictive-shortfall probability. These synthetic policy parameters make the decision boundary testable. In a bank system, policy owners approve the thresholds, independent validation assesses the model, and the interface shows how the recommendation changes with assumptions and observations. A reviewer can request evidence, adjust the amount or schedule, or route an exception, with rationale recorded.

For a candidate action a, the decision service can report the posterior distribution of next-period cash, P(Cₜ₊₁ < due(a) | evidence), the expected lender contribution under the declared cost convention, and the customer cash-floor probability. The policy layer first removes actions that breach approved eligibility or affordability constraints; among the remaining actions it presents the relevant quantities and boundary status. If posterior uncertainty straddles a limit or affordability threshold, the case can route to a reviewer for more evidence or a documented judgement. This makes the credible interval operational: it signals how stable a recommendation is to uncertainty instead of pretending a point estimate settles the decision.

Article 2 also develops hierarchical logistic and survival models, Pólya–Gamma computation, Student-t coefficient priors and half-Student-t group-scale priors. The first governs a coefficient; the second governs a positive group standard deviation, with separate parameters, supports, scales and diagnostics. The series distinguishes PD, predictive-cash, causal-effect and action-difference intervals. Label each with its target and decision meaning so reviewers can interpret the uncertainty directly. [2]

## 5. Put facility terms on a dated cash calendar

The case’s illustrative facility advances KES30,000 on day 1 and sets three KES11,000 payments on days 30, 60 and 90. Each payment comprises KES10,000 principal and KES1,000 fee, for total fees of KES3,000. These are declared synthetic terms. The merchant begins with KES50,000 cash. Five normal receipts of KES82,000 arrive on days 6, 12, 18, 24 and 30, while five supplier payments of KES54,000 are due on days 1, 7, 13, 19 and 25. Operating bills, household needs and existing debt have their own dates. The daily cash engine tests the KES20,000 reserve. [3]

The facility contract should define principal, fees, effective dates, due dates, grace rules, allocation order, accrual convention, arrears, rescheduling authority, default, recovery and closure. Original dues remain recorded when an authorized reschedule creates a new schedule. Each receipt is allocated to a due amount with principal, fee and date visible. The ledger separates amount due, amount settled, reversal, days past due, cure, restructure, write-off and recovery. These distinctions let Collections evaluate service actions, Finance reconcile cash and Risk measure portfolio outcomes from the same factual record.

The stress convention retains unpaid supplier and operating obligations as liabilities. An operating extension could model stock, supplier credit, curtailed purchases, lost sales and recovery when inventory and sales data support those assumptions. Repeat lending in the fixture requires full settlement, a seven-day cooling period, 30 observed days with residual cash at least KES22,000, settled bills and a renewed purpose-and-capacity review. [3]

## 6. Trace contribution from receipts to risk-sharing

The lender-contribution identity is:

**Π = collected fees − funding cost − origination and servicing costs − workout cost − principal written off + cash recoveries.**

The case assumes 12% annual funding on a 365-day basis, KES500 origination cost per loan, KES2 servicing cost per performing loan-day and KES400 workout cost per default. It reports contribution before central overhead, tax and a capital hurdle. Funding cost continues on unrecovered principal through day 300. Two checks reconcile originations to principal repaid, written-off principal and terminal performing principal; and reconcile contribution to lender net cash plus terminal principal. These identities make the profit calculation auditable and expose missing timing assumptions.

The ten scenarios yield useful distinctions. Baseline funding gives three loans, no defaults and KES5,184.66 contribution. Duplicate-feed and internal-transfer scenarios preserve that result after reconciliation. A missing channel or day-96 classification results in no loan and no repayment label. Delayed settlement results in three loans, eight maximum days past due, KES5,155.07 contribution and KES20,000 household shortfall. Margin stress results in two loans and KES3,456.44; sustained stress produces one default and KES−22,151.23 contribution, with KES180,000 household shortfall. A reviewed reschedule yields KES5,056.03 contribution alongside KES20,000 household shortfall. The cash result is therefore presented with arrears, obligations and household effects. [3]

An IFC or other guarantee enters as a separate claim and recovery ledger: eligible exposure, attachment, coverage, cap, exclusions, submission, acceptance, settlement delay, currency, recovery sharing and reporting. Record an accepted claim as a receivable under its contractual terms; recognize the cash flow at settlement. The case’s funding cost and contribution can then compare 30-day and 90-day settlement and model coverage against the underlying eligible loss. This gives the 4G Capital case a reproducible extension while preserving the Moniepoint case’s business-cash-flow focus.

Keep realized contribution separate from expected credit loss and capital measures. Expected credit loss estimates the probability-weighted present value of contractual cash shortfalls; realized contribution follows observed receipts, funding, service, workout and recovery. Economic capital describes a tail-loss buffer under a selected horizon and confidence standard, while RAROC relates risk-adjusted return to its chosen capital measure. Each output needs its population, horizon, scenario and model version. The five-article series discusses these connections, while the case supplies the receipt-level ledger from which the realized result can be reproduced [2], [3], [7], [8].

## 7. Articles 1–3: offers, sequential collection and observed outcomes

Article 1 records an eligible offer set, assignment probabilities, offer shown, take-up, facility schedule and mature outcome. This separates assignment, acceptance and repayment so the experiment estimates the effect defined by its design. Contextual bandits can follow once eligibility and outcome measurement are stable. Linear UCB, logistic Thompson sampling and Boltzmann/softmax are candidate allocators; policy sets eligible actions and the service logs its selection probability. That probability describes allocation, while a posterior interval describes uncertainty. Outcomes include dated receipts, delinquency, cure, customer conditions and lender contribution at a stated horizon. [2]

Article 2 treats collection as a sequence under an evolving, partly observed borrower state. The snapshot can include cash forecast, source coverage, due amount, arrears age, dispute, prior contact, customer preference and uncertainty. A state or belief update informs a bounded choice such as reminder, source check, support referral, date adjustment or no additional contact. Deterministic rules block duplicate contact and route disputes; models estimate outcomes; policy defines eligibility; reviewers authorize consequential changes. Survival or competing-risk models describe event timing, while an identified experiment estimates intervention effects. The event record retains state, available actions, chosen action, approval, delivery and subsequent cash. [2]

Article 3 tracks selection from application through evidence coverage, eligibility, offer, acceptance, disbursement and outcome maturity. A declined or unfunded case carries an unobserved repayment outcome with a reason code where available. Guarded experiments can create evidence in an approved segment. Propensity and overlap records support policy evaluation; fairness analysis locates differences at coverage, selection, treatment or outcome stages. Mwendo Pamoja Part 3 contributes fair-servicing and borrower-context principles, linked here to specific experiments and decisions. [1], [2], [6]

## 8. Article 4: connect borrower cash to Treasury decisions

Article 4 aggregates dated facility cash flows into portfolio earnings, liquidity, expected-loss and capital views. Contractual dues remain distinct from settled receipts; delayed collections change cash timing, while cure, default and repricing affect risk and income. Approved aggregates retain product, vintage, currency, scenario, as-of date and transformation version while limiting direct identity. KESONIA affects floating-rate loan payments and asset income. Market rates separately affect deposit prices, migration, withdrawals and replacement funding; deposit beta describes liability repricing. These paths meet in NIM, collections, liquidity, expected credit loss and capital. Credit and Treasury can use a common approved scenario through separate models, then combine results for ALCO. FTP and constrained stochastic control operate at the institution level, separately from borrower collection policy. [2]

The Dynare MCP material is a macro-scenario tooling example: Dygnosis handles source navigation and static diagnostics; official Dynare through MATLAB or Octave performs numerical solution, simulation and estimation. An approved scenario enters Treasury through a versioned data contract [9], [10].

## 11. Article 5: agentic workflow around financial services

The bank-controlled workflow in Article 5 coordinates registered services. An intake task checks source, coverage and permission. A provenance task proposes classifications with source references. The reconciliation engine verifies totals and account links. The cash engine computes residuals and the dated calendar. Statistical services return posterior or predictive quantities. The policy service checks which actions are eligible. An agent can assemble those outputs into a review packet. An authorized officer accepts, amends, requests evidence or declines the proposal. Maker-checker approval is applied where required, and a separate execution service acts only on an approved, non-expired request. A receipt records the execution result and joins it to later realized outcomes. [2], [3]

~~~mermaid
flowchart TD
    S[Bank and permitted payment sources] --> G[Purpose, permission and source gateway]
    G --> E[Immutable event ledger with event and availability times]
    E --> P[Entity resolution, provenance and coverage]
    P --> R[Deterministic reconciliation and cash bridge]
    R --> C[Cash calendar and facility ledger]
    C --> M[Versioned statistical services: posterior, prediction, causal effect]
    M --> Q[Approved policy and eligible action set]
    Q --> O[Agent orchestrator: gather, check, summarize and route]
    O --> H[Human review and maker-checker approval]
    H --> X[Separate authorized execution service]
    X --> L[Execution receipt, servicing events and realized cash]
    L --> V[Monitoring, experiment evaluation and model oversight]
    V --> E
    T[Approved macro and market scenarios] --> A[Portfolio, Treasury and ALCO services]
    L --> A
    A --> H
~~~

The diagram’s authority boundary is deliberate: the agent routes work and presents evidence; deterministic and statistical services calculate; policy restricts; a person approves; a separate service executes. Every step is linked by case and correlation IDs, event IDs, timestamps, source references, model and policy versions, approver, idempotency key and execution receipt. A hash can detect record changes; cryptographic identity and signing require their own key and trust controls. The financial result remains reproducible even when the model that drafted the summary is later replaced.

## 12. Data protection and meaningful review are domain requirements

Kenya’s Data Protection Act covers processing principles and data-subject rights. Section 35 addresses decisions based solely on automated processing that produce legal effects or significantly affect a person, including notice, reconsideration and a new non-automated decision route. Regulation 22 defines automated individual decision-making as a decision without human involvement and specifies information about logic, transparency and fairness, significance and consequences, error prevention, appropriate mathematical or statistical procedures, correction of inaccuracies, bias controls and human intervention. The workflow therefore records what the reviewer can inspect, change and decide, supporting accurate classification of the decision process. Regulation 49 identifies high-risk processing categories for a prior DPIA, including significant automated decisions, large-scale processing, linking datasets from different sources or purposes and innovative technology. [4], [5]

The Central Bank of Kenya’s banking-sector AI survey records credit-risk assessment among leading reported applications and highlights data quality, governance, cybersecurity, third-party and skills considerations. The staged design addresses those local operating conditions [11].

Implement these obligations through purpose and permission registries, notice and retention versions, access roles, DPIA status, review routes and correction history. Persistent agent state carries a case token and minimum task data; approved services retrieve only the required fields. Customer-facing records explain the information and decision process. Institutions map legal basis, controller/processor roles and sector rules to each product and purpose.

The reviewer can inspect source transactions, uncertainty, dated cash and the proposed schedule; request evidence, record the borrower’s explanation or change the action. Mark values as observed, inferred, simulated or policy-assumed. Separate proposal, approval and execution. Record override rationale, approver, time, expiry and outcome so review quality can be evaluated.

## 13. Evaluate each component against its financial purpose

Evaluate deterministic controls first: reconciled totals, transfers, duplicates, reversals, cutoffs, coverage and facility balances. Validate models for calibration, interval coverage, diagnostics, segments, drift and outcome maturity. Test policy eligibility and affordability, and workflow extraction, classification, routing, correction and abstention. Assess the full product on realised cash, operating capacity, arrears, cure, restructuring, recovery and contribution. [3]

Move from historical replay to read-only shadow mode, then human-reviewed proposals. Replay reconstructs the original information cutoff; shadow mode compares outputs alongside current practice. Prospective experiments or sequential learning follow with defined eligibility, assignments, outcomes, follow-up, safeguards and ownership. Scenario comparisons quantify stipulated assumptions; prospective designs estimate causal impact. Model artifacts become policy inputs through a versioned approval process. [2]

Institution-owned acceptance thresholds should include reconciled values, lineage for displayed numbers, reproducible snapshots, authorization checks, minimum coverage, validated interval performance, service latency and drift escalation. Set and version the values for the portfolio and systems, with an accountable response for each failed gate.

## 14. A staged implementation path

Build the baseline before adding multiple agents: event schema, as-of snapshot, cash bridge, calendar, facility ledger, scenario runner and reproducible outputs from the Moniepoint case. Provide a reviewer screen for coverage, classes, unresolved events, intervals and due dates. Keep synthetic truth outside model-visible data and preserve source and parameter hashes. Then add scoped intake, classification and summarization agents with schema, lineage and arithmetic checks.

Integrate account, wallet and POS adapters; CRM/Dynamics for cases; ERP and accounting for obligations; core banking for approved, idempotent instructions; and Oracle Treasury through published aggregate data products. Power BI or Tableau presents governed measures. Excel-DNA, Office.js, VSTO, C++ kernels, C# services and React interfaces are candidates selected against bank standards, licensing, controls and workload benchmarks.

Attach the research services by article: assignments and propensities (1), states and actions (2), selection and labels (3), funding scenarios (4), and governance and approvals (5). CRISP-DM organizes business and data understanding, preparation, modeling, evaluation and deployment; add purpose review, independent validation, change approval, monitoring and incident response. Give each stage an owner, entry criteria, artifacts and rollback. [2]

## Conclusion

The five-article series and Moniepoint case give a bank a concrete starting point: model financial events and decisions, then use agents to coordinate evidence and review. Common identifiers and tested contracts connect experiments, collections, selective outcomes, Treasury control and governance. Bayesian and causal methods provide uncertainty and intervention evidence; reconciliation, policy ownership and human judgement make them actionable. Begin with a reproducible baseline, then add read-only assistance, reviewed proposals and prospective learning. Evaluate each stage against realized receipts, customer conditions and institution economics.

## References

[1] N. Maloba, *Underwrite for Collection: An Integrated Research Whitepaper on Sustainable MSME Credit*, 2026. Zenodo DOI: https://doi.org/10.5281/zenodo.23343888. Bank-controlled architecture: Part 4, https://github.com/TheAlchemistNerd/underwrite-for-collection/blob/main/series/parts/Part_4_Bank_Controlled_Research_Sandboxes_and_Enterprise_Credit_Architecture.md. Capital and Treasury treatment: Part 5 §§5–6, https://github.com/TheAlchemistNerd/underwrite-for-collection/blob/main/series/parts/Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md.

[2] N. Maloba, *Causal Credit and Treasury Decision-Making*, five-article research series, 2026, Articles 1–5 and mathematical appendices. https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/series/publications/linkedin/2026-10-08_causal_credit_series.

[3] N. Maloba, “Moniepoint and Underwrite for Collection reproducible cash flow case,” 2026, narrative, Python model and outputs. Narrative: https://github.com/TheAlchemistNerd/underwrite-for-collection/blob/main/docs/research/MONIEPOINT_REPRODUCIBLE_CASHFLOW_CASE_2026-10-18.md; model: https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab/moniepoint_cashflow_case.

[4] Republic of Kenya, *Data Protection Act*, No. 24 of 2019, secs. 25, 31, 35–36. https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15/source.

[5] Republic of Kenya, *Data Protection (General) Regulations*, Legal Notice 263 of 2021, regs. 4, 19–22, 27–36 and 49–53. https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng%402022-12-31/source.

[6] M. Dudík, J. Langford and L. Li, “Doubly robust policy evaluation and learning,” in *Proc. 28th International Conference on Machine Learning*, 2011. https://icml.cc/2011/papers/554_icmlpaper.pdf.

[7] IFRS Foundation, *IFRS 9 Financial Instruments*, B5.5.28–B5.5.33. https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ifrs-9-financial-instruments.pdf.

[8] Basel Committee on Banking Supervision, *Guidance on credit risk and accounting for expected credit losses*, 2015. https://www.bis.org/publications/201512-guidelines-guidance-credit-risk-and-accounting-expected-credit-losses.

[9] Dygnosis project, “A language server and MCP for Dynare,” source and documentation, accessed 3 Nov. 2026. https://github.com/naivej/dygnosis.

[10] Dynare Team, *The Dynare Reference Manual, Version 7.2*, 2026. https://www.dynare.org/manual/.

[11] Central Bank of Kenya, *Survey on Artificial Intelligence in the Banking Sector*, survey issued March 2025, reporting sector information as at 31 Dec. 2024. https://www.centralbank.go.ke/uploads/banking_sector_reports/595566510_Survey%20on%20Artificial%20Intelligence%20in%20the%20Banking%20Sector.pdf.

### Source note

Moniepoint case values are synthetic, reproducible assumptions for illustrating the financial calculations. The cited laws and regulations inform the control design; institutions map them to the applicable entity, product, data roles and processing purpose.
