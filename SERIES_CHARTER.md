# Series Charter: Underwrite for Collection

## 1. Purpose

The series advances a lifecycle view of MSME credit in Kenya. It begins with a simple proposition: origination is only the opening event in a credit relationship. A sound credit architecture anticipates the cash flows, information, interventions, servicing capacity, restructurings and recovery paths that will determine whether a facility remains affordable and collectible after disbursement.

The series will combine a human account of MSME cash-flow uncertainty with mathematical modelling, bank implementation, regulatory analysis and experimental evidence. It will not treat behavioural scoring as a substitute for conventional credit analysis. Behavioural information is one evidence layer within a wider system that includes legal capacity, affordability, business economics, product structure, collateral and guarantees where relevant, macroeconomic conditions, servicing quality, collection conduct, accounting, capital and funding.

## 2. Intended audiences

The manuscripts must remain intelligible and useful to several audiences at once:

- MSME owners and representative bodies.
- Commercial banks, microfinance banks and other licensed credit providers.
- Credit, collections, restructuring and recoveries teams.
- Risk, finance, treasury, ALM, capital and IFRS 9 teams.
- Data scientists, actuaries, economists and model validators.
- Enterprise architects, privacy engineers and information-security teams.
- The Central Bank of Kenya, the Office of the Data Protection Commissioner and other relevant public authorities.
- Kenya Bankers Association research and policy audiences.
- Development-finance institutions, guarantee providers, credit insurers, investors and risk-transfer counterparties.
- Academic and professional readers interested in causal inference, Bayesian methods and responsible AI.

Technical depth must not erase the business story. Narrative clarity must not dilute definitions, assumptions, equations, evidence or limitations.

## 3. Series identity

The working series title is:

> **Underwrite for Collection: An MSME Lifecycle Credit Architecture for Kenya**

The recurring lifecycle is:

```text
MSME activity and financing need
              ↓
Product design and responsible origination
              ↓
Point-in-time operational and financial evidence
              ↓
Prognostic risk and uncertainty estimation
              ↓
Credit Policy and Compliance Gate
              ↓
Randomised or quasi-experimental intervention evidence
              ↓
Servicing, collection, cure, restructuring and recovery
              ↓
ECL, capital, pricing, liquidity and funding consequences
              ↓
Governed learning and product redesign
```

## 4. Canonical conceptual separations

Every part must maintain the following distinctions.

### 4.1 Prediction, causation and policy

A prognostic model estimates outcomes under observed policy and data. A randomised or credible quasi-experimental design estimates the effect of an intervention under a defined estimand. A policy layer applies legal, contractual, conduct, risk-appetite and operational constraints. These are connected but not interchangeable.

The hierarchical Bayesian logistic regression is the principal prognostic architecture. Randomisation, regression discontinuity, difference-in-differences, interrupted time series, instrumental variables, synthetic controls and target-trial emulation provide causal evidence where their identification assumptions are satisfied. The Credit Policy and Compliance Gate remains downstream of model inference.

### 4.2 Behavioural evidence and borrower intent

Observed cash-flow, repayment and engagement patterns may indicate rising repayment difficulty, volatility, operational disruption or the need for review. They do not establish motive. The manuscripts will use observable and auditable states rather than labels such as “strategic defaulter” unless intent is established through a separate lawful process.

### 4.3 Explicit variables and AI representations

Explicit variables retain defined economic meanings. Examples include earnings velocity, repayment velocity, cash-flow asymmetry, debt-to-liquidity measures, transaction volatility, utilisation, arrears transitions and time since cash depletion. AI neural sequence representations may capture residual temporal structure.

Where both blocks enter a downstream model, neural representations will be cross-fitted and residualised against the explicit design matrix. Optional whitening may address within-embedding geometry. Residualisation reduces representational duplication; it does not establish causality or remove confounding. Regularised-horseshoe priors shrink weak residual contributions but do not mechanically produce exact zeros.

### 4.4 Hierarchical pooling and inference

Product, sector, geography, institution, vintage, cohort and relevant time effects may be partially pooled where their definitions and sample sizes support identification. Driver-specific effects from the prior platform-focused work will not be carried over mechanically. MSME-level effects require repeated matured credit episodes or a justified longitudinal structure.

Pólya–Gamma augmentation is an offline inference strategy for the full hierarchical logistic model. It makes Gaussian parameter blocks conditionally conjugate while preserving partial pooling. It is not an online scoring operation and does not alter the economic meaning of the HLR. P-spline difference penalties, Gaussian hierarchical effects, and AR(1) or RW1 time processes can be updated efficiently within a blocked sampler. Hyperparameters, shrinkage scales, persistence and correlation structures retain their own updates.

Production decisions use an approved posterior artifact, calibrated summaries and versioned uncertainty outputs. No MCMC sampling runs inside a credit request.

### 4.5 Default occurrence, timing and lifecycle state

Binary default models, hazard models and multi-state models answer different questions. The HLR estimates a defined-horizon outcome probability. A survival challenger estimates timing subject to censoring and competing events. A multi-state model represents movement among current, early arrears, modification, cure, re-default, default, recovery and closure states.

A Cox model does not automatically provide a transition matrix. Transition estimates require a compatible multi-state or competing-risks specification. Gamma-frailty conjugacy is a separate survival extension, not the foundation of the primary HLR. Hawkes processes, POMDPs and contextual bandits are optional challengers whose assumptions must be demonstrated before operational use.

### 4.6 Collection, cure and recovery

Collections are not defined only as cash received or accounts contacting a threshold. Outcomes will distinguish:

- contractual payment;
- arrears prevention;
- cure;
- durable cure;
- re-default;
- modification and restructuring;
- prepayment;
- charge-off;
- gross recovery;
- workout and contact cost;
- net present value of recovery;
- complaints and customer harm;
- business continuity and survival;
- time spent in each lifecycle state.

An intervention is successful only relative to its estimand, horizon, cost and conduct constraints.

### 4.7 Pricing and probability measures

Real-world default probabilities support underwriting, monitoring, stress testing and IFRS 9 inputs. Market-consistent or risk-neutral transformations serve valuation purposes when a tradable instrument, calibration basis and valuation objective justify them. Adding a risk premium to KESONIA does not turn a physical default probability into a risk-neutral probability.

For regulated customer pricing, the canonical CBK structure will be stated with its effective-date context:

```text
Customer lending rate = KESONIA + K_RBCP
Total cost of credit = KESONIA + K_RBCP + fees and charges
```

`K_RBCP` must not be equated with a treatment effect, regulatory capital, expected loss, note margin or investor hurdle. Those quantities receive distinct notation and reconciliation.

### 4.8 Accounting, capital and liquidity

IFRS 9 expected credit loss, regulatory capital, economic capital, pricing margin, provisions, cash reserves, liquidity buffers and risk-transfer protection are separate constructs. A lower model PD does not automatically produce an accounting release, capital reduction or lower funds-transfer price. Each outcome follows its own governance, calibration, approval and legal framework.

Frequent borrower collections do not automatically shorten behavioural maturity, create high-quality liquid assets or remove funding mismatch. ALM and FTP must model settlement availability, prepayment, delinquency, cure, default, recovery, benchmark repricing, operational lags and stress behaviour.

### 4.9 Regulation, contract, policy and convention

Each material control will be labelled as one of:

- applicable law or regulation;
- supervisory guidance;
- contractual term or covenant;
- internal credit policy or risk appetite;
- statistical convention;
- proposed experimental safeguard;
- implementation recommendation.

Kenya’s Data Protection Act requires a lawful basis and relevant safeguards; it does not make consent the universal basis for all processing. Significant solely automated decisions require specific analysis, transparency, contestability and human-review arrangements. Fairness heuristics such as an 80 percent selection-rate comparison may be diagnostic, but they are neither a complete fairness standard nor a statement of Kenyan law.

The series will not assert an official CBK regulatory sandbox route or fixed duration unless a primary current source establishes it. The default formulation is a bank-controlled research sandbox followed by a regulator-engaged controlled pilot under a pathway agreed in writing with the relevant supervisor.

## 5. Experimental doctrine

The programme will use experimentation to learn which product and servicing choices improve sustainable repayment, not to maximise short-run extraction.

Separate experimental families will evaluate:

1. Additional evidence or score use.
2. Product and repayment structure.
3. Supportive servicing and collection interventions.
4. Restructuring and recovery pathways.

Randomisation occurs only where equipoise, lawful authority, operational capacity and customer protection permit it. No participant may be assigned an unlawful, misleading, unaffordable or knowingly harmful treatment. Materially adverse action, hardship, vulnerability and complaint pathways remain governed by policy and human review.

Where randomisation is not feasible, a quasi-experimental design must state its assignment mechanism, estimand, identifying assumptions, diagnostics and falsification tests. Adaptive experimentation may follow stable conventional trials, but only with logged propensities, positivity floors, delayed-outcome handling, off-policy evaluation, monitoring and pre-agreed stop rules.

## 6. Data-access doctrine

The preferred research architecture is model-to-data rather than unrestricted data extraction. Bank data remains within a bank-controlled environment such as an on-premises platform, private cloud, secure enclave, clean room or equivalent governed boundary. Researchers receive approved features, de-identified analytical views, synthetic development data or disclosure-controlled outputs according to role.

Federated learning, secure aggregation, differential privacy, multiparty computation and trusted execution environments are tools, not automatic guarantees. The chosen design must address privacy leakage, update poisoning, membership inference, output disclosure, auditability and operational ownership.

Public KBA, CBK, KNBS, World Bank and IMF evidence can establish context and support aggregate analyses. It cannot replace institution-level lifecycle data for estimating borrower-level treatment effects or model performance. A synthetic portfolio can demonstrate feasibility, power and software behaviour; it must not be presented as empirical evidence about Kenyan MSMEs.

## 7. Evidence and citation standard

Primary Kenyan sources take precedence for Kenyan legal, regulatory, benchmark and industry claims. International standards and original academic research support methods and comparators. Professional commentary may provide context but cannot override primary authority.

Each manuscript will use IEEE numerical citations ordered by first appearance. References begin on a new page in publication outputs, and each entry begins as a separate paragraph. Claims that are time-sensitive will include an as-of date. Source retrieval, canonical URL, access status, jurisdiction, relevance and limitations will be tracked in the master source index.

## 8. Narrative and language standard

The prose will advance the argument constructively. It will explain what the architecture accomplishes, how it operates and under which conditions its claims hold. Necessary qualifications will be integrated into the reasoning rather than written as defensive disclaimers.

Each part will begin with a recognisable MSME situation and gradually move from economic intuition to architecture, equations, evidence and implementation. Dense diagrams, worked examples and tables will carry relationships that would be cumbersome in prose. Mathematical notation will be defined on first use and remain stable across the series.

## 9. Independence and preservation

The source library is read-only. The Mwendo Pamoja copies are comparators for scale, technical density, mathematical treatment and document architecture. The new manuscripts will not rebrand or lightly paraphrase Mwendo Pamoja. They will derive a distinct MSME research programme from the collectability thesis and relevant retained methods.

## 10. Definition of success

The completed series should allow a bank, researcher or public institution to understand:

- why collectability should shape product design before disbursement;
- what information is needed at each lifecycle stage;
- how prediction, uncertainty and causal effects differ;
- how to test product and intervention choices responsibly;
- how results enter servicing, ECL, capital, pricing, ALM and funding;
- how the architecture can operate inside a bank’s control boundary;
- what evidence is required before deployment or scale;
- and how an ecosystem pilot could become a reproducible Kenyan research contribution.

