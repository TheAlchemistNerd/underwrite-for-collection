---
title: "Underwrite for Collection"
subtitle: "Part 3: Regulatory Orchestration, Fair Intervention and Collection Governance"
author: "Nevil Maloba"
email: "nevillemaloba@gmail.com"
date: "6 September 2026"
lang: "en-GB"
---

# Abstract

Continuous underwriting creates value when an earlier warning leads to a better decision, a more sustainable payment path and a more collectible cash outcome. Part 3 defines the governance architecture between statistical evidence and customer treatment. It separates the prognostic distribution, causal evidence, policy eligibility and authorised action; introduces a graduated intervention library; and formalises a Credit Policy and Compliance Gate that carries legal, contractual, affordability, conduct, operational and portfolio constraints into every decision. Kenyan data-protection, banking, digital-credit, credit-information and consumer-protection duties are mapped according to the institution and activity in scope. Fairness is measured across access, error, intervention, contact, complaint, cure, re-default and net-recovery outcomes, with uncertainty made visible. Randomised and quasi-experimental designs are then positioned as governed methods for learning which permissible treatments create durable value. The result is an accountable route from a posterior risk estimate to proportionate human and institutional action.

## 1. From warning to permission

A small distributor supplies twelve neighbourhood shops. Her largest customer normally pays on the twenty-fifth day of each month, while the lender collects a working-capital instalment on the twenty-third. A two-day misalignment creates a familiar sequence: the account balance falls, the scheduled deduction fails, a reminder is sent and the arrears clock begins. Part 2b may correctly detect that this pattern raises the probability of 30-day arrears. Yet the warning alone cannot decide whether the lender should move the collection date, offer a short grace period, reduce the facility, begin a restructure review or continue the existing schedule.

The decision depends on more than risk rank. The lender must know whether the customer's receipts remain economically viable, whether the product contract permits a change, whether the action is affordable, who bears its cost, whether similar customers receive comparable treatment, whether the communication is clear, and what happens if the customer disagrees. A model may estimate a future state. Permission to act comes from the licensed institution's mandate, the contract, applicable law, approved policy and a named human or committee authority.

That separation brings the paper's governing idea into practice. A loan is underwritten for collection when product structure, monitoring and intervention are designed around sustainable cash performance after disbursement. Collection therefore begins as a design discipline, not as a department that appears after default. Kenya's Central Bank prudential guideline on consumer protection places fairness, reliability, transparency, equity and responsiveness across the institution's relationship with the customer, and assigns the board responsibility for the consumer-protection framework [1]. For digital credit providers within scope, the 2022 regulations add specific requirements for fair and transparent information, complaints handling, transaction records and collection conduct [2]. Data use and automated decision-making also sit within the rights and duties created by Kenya's Data Protection Act [3].

Part 3 operationalises these obligations through four linked objects:

1. **Model inference** estimates a defined future outcome from the information available at the decision cutoff. It includes the posterior mean, interval, tail probability, support-range status, entity-resolution coverage, cash-provenance status and data-quality state.
2. **Causal evidence** estimates how a specified permissible treatment changes an outcome for an eligible population relative to a defined alternative.
3. **Policy eligibility** determines which actions are available under law, contract, conduct standards, affordability rules, operational capacity and portfolio constraints.
4. **Customer treatment** is the actual communication, offer, modification, restriction, support or recovery action executed by its authorised owner.

The same record connects the four objects without collapsing them. A high probability of arrears may prompt an affordability conversation. Evidence from a prior pilot may show that payment-date alignment improves durable cure for enterprises with verified recurring receipts. The contract may permit that alignment without repricing. The policy gate may still route the case to a person because the receipts are unusually concentrated or the model is outside its support. The final action can then be explained in terms of payment timing, contractual conditions and the customer's available choices.

```{.mermaid layout=fullpage}
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial",
    "primaryColor": "#EAF2F8",
    "primaryTextColor": "#17324D",
    "primaryBorderColor": "#2E5E7E",
    "lineColor": "#4F6B7A",
    "secondaryColor": "#E8F5F2",
    "tertiaryColor": "#FFF4D6"
  },
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 36, "rankSpacing": 48}
}}%%
flowchart TB
    E[Point-in-time evidence<br/>posterior risk, uncertainty,<br/>data quality and account state] --> I[Model inference<br/>what may happen under<br/>the stated current policy]
    I --> C[Causal evidence<br/>what a specified permissible<br/>treatment may change]
    C --> P[Policy eligibility<br/>law, contract, affordability,<br/>conduct, capacity and portfolio]
    P --> H{Decision route}
    H -->|Standard supported case| A[Authorised action<br/>communicate, offer,<br/>modify, restrict or recover]
    H -->|Material uncertainty or exception| R[Human review<br/>reason, evidence,<br/>authority and expiry]
    R --> A
    A --> O[Lifecycle outcomes<br/>cash, durable cure, re-default,<br/>cost, complaint and continuity]
    O --> L[Treatment and outcome ledger<br/>matured evidence for validation,<br/>policy review and future trials]
    L --> E

    classDef evidence fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.7px;
    classDef analysis fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.7px;
    classDef decision fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.9px;
    class E,O,L evidence;
    class I,C analysis;
    class P,H,R,A decision;
```

**Figure 1: From lifecycle evidence to authorised customer treatment.** Prediction, causal learning, policy eligibility and execution remain separate decision objects. Outcomes return through a point-in-time ledger so later evidence can improve the system without rewriting what was known at the earlier decision.

## 2. The intervention contract

An intervention needs the same discipline as a financial product. It has a target population, a mechanism, an owner, a cost, an expiry and a measurable outcome. Calling an action "supportive" does not establish that it helped. A reminder may reduce accidental lateness for one enterprise and create an excessive contact burden for another. A grace period may protect productive investment, or postpone recognition of a cash-flow problem. A limit freeze may contain exposure while removing the liquidity needed to complete profitable orders. The decision record must make these possibilities testable.

For action (a) considered at decision time (t), define the intervention contract:

\[
\mathcal C_{a,t}=
\left(
\mathcal E_{a,t},\mathcal X_{a,t},m_a,o_a,c_a,d_a,
\tau_a,\mathbf Y_a,\rho_a,\chi_a
\right),
\]

where \(\mathcal E\) is the eligible population, \(\mathcal X\) the mandatory exclusions, \(m\) the hypothesised mechanism, \(o\) the authorised owner, \(c\) the cost bearer, \(d\) the customer communication and delivery channel, \(\tau\) the treatment and outcome horizon, \(\mathbf Y\) the outcome vector, \(\rho\) the monitoring and stop rule, and \(\chi\) the reconsideration, complaint and escalation route. A policy version links these fields to the exact rules effective at the time.

The outcome vector is deliberately wider than payment received:

\[
\mathbf Y_a=
\left(
\mathrm{Cash}_{0:H},
I^{\mathrm{DC}}_H,
I^{\mathrm{RD}}_H,
\mathrm{Cost}_{0:H},
\mathrm{Complaint}_{0:H},
\mathrm{ContactBurden}_{0:H},
\mathrm{Continuity}_{H}
\right).
\]

It records discounted cash, durable cure, re-default, direct intervention and recovery cost, complaint outcomes, contact burden and a product-appropriate indicator of business continuity. The last measure might be continued trading, verified turnover, fulfilment of customer orders or retention of a productive asset. It is defined before the experiment and collected only where a lawful, proportionate data route exists.

Every executed action enters a treatment ledger with the pre-action score and uncertainty, policy and model versions, eligibility, assignment mechanism, communication, customer response, executed terms, cash-flow change, human participation and downstream outcomes. This record addresses three sources of bias. First, the action changes what happens next. Second, the lender observes repayment only for customers who received credit and remained observable. Third, teams may select easier cases for supportive treatment and harder cases for recovery, making a successful treatment appear more effective than it was.

The ledger also preserves customer meaning. A business that pays after one reminder is not automatically "unwilling." A night-time transaction pattern is not intent. A decline in earnings is evidence about cash generation, not a diagnosis of the owner. The system uses observed states and stated uncertainty, while staff establish context through appropriate engagement.

## 3. A graduated intervention library

The intervention library follows the lifecycle rather than dividing work into disconnected origination and collections systems. A current account can receive information or payment alignment. Early stress may justify a voluntary budgeting conversation or a temporary support offer. Arrears may require a documented cure or modification pathway. Persistent distress may require restructuring, collateral action or recovery. Each step preserves the customer's payment history and contractual state so that assistance and recognition develop together.

| Lifecycle state | Illustrative intervention | Primary mechanism | Required evidence and control | Outcome emphasis |
|---|---|---|---|---|
| Current, stable | Clear schedule and self-service information | Reduce avoidable error and information cost | Accurate balance, due date and channel; customer choice | On-time cash, low contact burden |
| Current, timing mismatch | Payment-date alignment or split instalment | Match debt service to verified receipt rhythm | Contractual authority, affordability, no hidden fee | Durable performance and business continuity |
| Early stress | Reminder choice, budgeting prompt or hardship triage | Create time for diagnosis and action | Contact preferences, vulnerability screen, staff route | Avoided arrears, complaints and opt-out |
| Short arrears | Funded grace period or cure arrangement | Bridge temporary liquidity without obscuring account state | Eligibility, cost bearer, accounting review and expiry | Cure, re-default and net cash |
| Viable but impaired | Modification or restructure assessment | Restore a payment path supported by cash capacity | Full affordability review, approval, new cash flows and disclosures | Sustainable payment, ECL and continuity |
| Non-viable or persistent default | Proportionate recovery and security enforcement | Maximise lawful net recovery while limiting harm | Authority, accurate debt, conduct rules, complaint route | Discounted net recovery, time and cost |

This taxonomy separates communication from contract change. A message that explains the amount due is not a restructure. A payment-date change is recorded even when it has no fee or principal concession. A temporary grace arrangement remains visible to impairment and portfolio processes. A restructure creates a new contractual cash-flow schedule and passes through the accounting assessment owned by the reporting institution. Recovery uses an accurate balance, an authorised channel, humane conduct and the appropriate notice process.

```{.mermaid layout=fullpage}
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial",
    "primaryColor": "#EAF2F8",
    "primaryTextColor": "#17324D",
    "primaryBorderColor": "#2E5E7E",
    "lineColor": "#4F6B7A",
    "secondaryColor": "#E8F5F2",
    "tertiaryColor": "#FFF4D6"
  },
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 34, "rankSpacing": 46}
}}%%
flowchart TB
    S1[CURRENT AND STABLE<br/>clear schedule, receipt and<br/>self-service information] --> S2[CURRENT WITH TIMING MISMATCH<br/>payment alignment or<br/>split-instalment offer]
    S2 --> S3[EARLY STRESS<br/>preferred-channel reminder,<br/>hardship triage and review]
    S3 --> S4[SHORT ARREARS<br/>funded grace or<br/>documented cure arrangement]
    S4 --> S5[VIABLE BUT IMPAIRED<br/>affordability assessment,<br/>modification or restructure]
    S5 --> S6[PERSISTENT DEFAULT<br/>proportionate recovery,<br/>security and legal process]

    S2 -->|Receipts normalise| S1
    S3 -->|Verified recovery| S2
    S4 -->|Durable cure| S2
    S5 -->|Sustained new schedule| S2
    S6 -->|Resolved balance| X[Closure, write-off or<br/>completed recovery]

    classDef normal fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.8px;
    classDef watch fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.8px;
    classDef assist fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.9px;
    classDef resolve fill:#F8EAEA,stroke:#A94B4B,color:#5A2020,stroke-width:1.9px;
    class S1,S2 normal;
    class S3 watch;
    class S4,S5 assist;
    class S6,X resolve;
```

**Figure 2: The governed MSME intervention ladder.** Accounts can move forward or return to a healthier state. Every transition preserves the contract, account status, intervention, customer communication and outcome history required for accounting, validation and fair-treatment review.

The ladder is neither a universal sequence nor an automated escalation timer. An enterprise can move directly to a restructure review after a verified shock, remain on its original schedule with no intervention, or proceed to recovery when viability and contractual facts warrant it. Mandatory protections and legal processes take priority over an experimental treatment. The action library makes these routes explicit before a model or agent begins recommending them.

## 4. The Credit Policy and Compliance Gate

The Credit Policy and Compliance Gate is the runtime boundary between evidence and permission. It receives the Part 2b posterior artefact, explicit lifecycle state, product terms, affordability evidence, entity-resolution and cash-provenance status, data-quality status, customer treatment history and portfolio context. It returns an authorised action, a review route or a reasoned deferral. The gate is versioned independently from the statistical model, allowing a lender to change a product limit, contact rule or approval authority without retraining the HLR.

For customer-account state \(s_{i,t}\), let \(\mathcal A\) be the intervention library. The feasible action set is:

\[
\mathcal A^{\mathrm{feas}}(s_{i,t})=
\mathcal A^{\mathrm{law}}
\cap\mathcal A^{\mathrm{contract}}
\cap\mathcal A^{\mathrm{conduct}}
\cap\mathcal A^{\mathrm{afford}}
\cap\mathcal A^{\mathrm{ops}}
\cap\mathcal A^{\mathrm{portfolio}}.
\]

The terms are implemented as traceable decision tables. The legal table identifies the entity and applicable rule. The contractual table verifies product terms and authority. The conduct table applies contact, disclosure, fair-treatment and vulnerability controls. The affordability table tests the proposed cash path. The operations table verifies channel, staff and servicing capacity. The portfolio table applies exposure, concentration and funding constraints. An empty intersection produces a deferral or human route rather than an improvised action.

Within the feasible set, a policy may rank actions by expected lifecycle value:

\[
a^*(s)=\arg\max_{a\in\mathcal A^{\mathrm{feas}}(s)}
\mathbb E\!\left[
\mathrm{DCF}_{a}
-C_{a}
-\lambda_h H_{a}
-\lambda_b B_{a}
\mid s,\mathcal D
\right],
\]

where \(\mathrm{DCF}_a\) is discounted net cash, \(C_a\) direct intervention and servicing cost, \(H_a\) a registered customer-harm vector, and \(B_a\) business-continuity loss. The weights \(\lambda_h\) and \(\lambda_b\) express approved governance priorities; they cannot monetise away a hard legal or policy prohibition. The expectation integrates predictive and, where identified, treatment-effect uncertainty.

The value calculation is reported as a vector before any approved scalar ranking is applied. Credit risk sees expected arrears, default and recovery. Finance sees cash timing and direct cost. Conduct sees communication, complaint and hardship outcomes. The relationship team sees continuity of the enterprise and its trading cycle. Presenting these components separately prevents a small estimated collection gain from concealing a material increase in re-default, customer distress or operating burden. Policy owners approve the horizon and weights through a recorded change process, and sensitivity analysis shows when a recommended action depends on a narrow valuation choice.

Uncertainty creates an operational choice. The gate can route a case to review when the probability of harmful performance exceeds an approved tolerance or when the model is outside support:

\[
\mathrm{Review}_{i,t}=
\mathbf 1\!\left\{
P\!\left(g_h(H_{a})>h_{\max}\mid s_{i,t},\mathcal D\right)>\alpha
\;\lor\;
q_{i,t}^{\mathrm{support}}=0
\;\lor\;
q_{i,t}^{\mathrm{data}}<q_{\min}
\;\lor\;
q_{i,t}^{\mathrm{prov}}<q_{\min}^{\mathrm{prov}}
\right\}.
\]

Here, \(g_h\) maps the registered harm vector to the governed escalation measure and \(q^{\mathrm{prov}}\) records whether entity and economic-cash evidence meets the decision's approved provenance threshold. This rule gives uncertainty a destination. A reviewer receives the proposed entity links, transaction paths, cash classes, confidence, decision sensitivity, available actions, contractual and policy constraints, and a time-limited authority. The reviewer may confirm, reject or defer a classification using controlled reason codes and proportionate supporting evidence. An unresolved or related-party flow is not treated as evidence of intent; it is an evidential state whose materiality determines the route.

```{.mermaid layout=fullpage}
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial",
    "primaryColor": "#EAF2F8",
    "primaryTextColor": "#17324D",
    "primaryBorderColor": "#2E5E7E",
    "lineColor": "#4F6B7A",
    "secondaryColor": "#E8F5F2",
    "tertiaryColor": "#FFF4D6"
  },
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 32, "rankSpacing": 44}
}}%%
flowchart TB
    IN[Versioned input packet<br/>risk distribution, account state,<br/>cash provenance, quality,<br/>affordability and history] --> L[Legal and entity scope]
    L --> C[Contract and product authority]
    C --> F[Fair-treatment, contact<br/>and vulnerability controls]
    F --> O[Operational capacity and<br/>portfolio constraints]
    O --> Q{Supported, complete<br/>and within authority?}
    Q -->|Yes| D[Approved decision table<br/>action, owner, expiry,<br/>notice and accounting flags]
    Q -->|Exception or uncertainty| H[Human review queue<br/>evidence pack, permitted choices,<br/>authority and response time]
    H --> D
    D --> R[Decision record<br/>model, policy, reason, communication,<br/>override, complaint and outcome keys]

    classDef input fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.7px;
    classDef gate fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.9px;
    classDef action fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.8px;
    class IN,R input;
    class L,C,F,O,Q gate;
    class H,D action;
```

**Figure 3: Credit Policy and Compliance Gate with a substantive human-review route.** The gate tests entity scope, authority, conduct, affordability, capacity and portfolio constraints before an action is executed. The final record preserves the evidence, owner, reason, communication and future outcome key.

## 5. A Kenya-first control architecture

Regulatory orchestration begins by identifying the institution, activity, customer and decision in scope. A bank, a licensed digital credit provider, a credit reference bureau, a data controller and a contracted technology provider may participate in the same lifecycle while carrying different duties. The canonical control register therefore records five fields before translating a source into a system rule: the instrument and provision, regulated entity, covered activity, effective date, and operational control owner. Contractual covenants, internal credit policy and statistical monitoring thresholds sit in adjacent registers and retain their own labels.

For a bank licensed under the Banking Act, CBK/PG/22 supplies a direct supervisory foundation. It expects customers to be treated equitably, honestly and fairly throughout their relationship with the institution, calls for humane treatment in face-to-face and remote contact, and addresses prudent lending, understandable product information and complaints [1]. The board owns the framework; credit, servicing and collections teams express it in their controls. This supports an intervention architecture in which suitability, total cost, communication and recourse are checked when an action is designed and again when it is delivered.

The Digital Credit Providers Regulations apply to licensed DCPs while expressly excluding institutions licensed under the Banking Act and other listed categories from their application. Within their scope, they provide particularly concrete lifecycle requirements. Regulation 20 prohibits threats, shaming, unauthorised contact with a customer's contacts and other oppressive or abusive collection conduct. Regulations 21 and 22 address transaction records and complaints. Regulations 25 to 27 address fair and transparent information, reasonably required customer information, terms, charges and complaint channels [2]. A multi-party programme maps these controls to the DCP when one participates and uses them as a documented conduct benchmark only where another institution voluntarily adopts them.

Personal-data governance begins with the Data Protection Act. Its principles include lawful, fair and transparent processing, purpose limitation, minimisation, accuracy, retention discipline and appropriate safeguards. The architecture registers a lawful basis for each purpose rather than treating one consent screen as permanent permission for every later use. Collection servicing, credit assessment, model development, fairness audit and research publication are separate purposes with potentially different data fields, recipients, retention periods and legal analyses [3].

Automated decision-making receives a specific control path. Section 35 concerns a decision based solely on automated processing, including profiling, that produces legal effects or similarly significantly affects the data subject. Where an applicable exception supports such processing, the Act provides notification and a route to reconsideration or a new decision that is not based solely on automation. The General Regulations add operational safeguards, including meaningful information about the logic, significance and envisaged consequences, appropriate statistical procedures, error controls, measures addressing discriminatory effects and bias, and an ability to obtain human intervention and express a point of view [4].

The practical unit of analysis is the decision, not the presence of a model somewhere in the process. A daily portfolio-risk dashboard may inform a manager without deciding a customer's rights. A fully automated decline, material limit reduction or restructure decision can have a very different effect. The decision inventory records whether processing is solely automated, the effect on the customer, the legal basis, the logic summary, notification, reconsideration path and human authority. A human reviewer must be able to examine the evidence, consider relevant customer information and change the result. Merely clicking an automatically selected outcome would not provide the substantive reconsideration contemplated by the control design.

High-risk processing is assessed before deployment. Under the General Regulations, DPIA triggers include automated decisions with legal or similarly significant effects, large-scale processing, sensitive data, combining datasets from different sources, systematic monitoring and innovative technologies in the stated circumstances [4]. The ODPC's guidance for digital credit providers translates these principles into sector-specific practices around purpose, transparency, data-subject rights, profiling, data sharing, retention, security and DPIAs [5]. For this architecture, the DPIA is a living design artefact linked to the feature register, decision inventory, processors, cross-border transfers, incidents and material changes.

Credit-information controls form another distinct route. The Banking (Credit Reference Bureau) Regulations provide customer rights to obtain and dispute credit information and to understand how a bureau score was arrived at. They also require an institution to issue an adverse-action notice when bureau information contributed to an adverse decision, identifying the bureau and the customer's access and dispute rights [6]. The notice rule is attached to the bureau-data condition in the decision log. A separate, institution-designed explanation standard covers material actions based on its own lifecycle model, ensuring that useful reasons remain available even when CRB information played no part.

The Consumer Protection Act supplies wider rules on consumer agreements, unfair practices and credit agreements where the transaction and borrower fall within its scope [7]. Because MSMEs range from sole traders to incorporated enterprises, the applicability field cannot be inferred from the label "MSME." Product counsel determines the covered relationship. The customer experience can still adopt a consistent higher standard: accurate balances, understandable terms, visible fees, freely chosen channels, documented modifications and meaningful recourse.

Complaints close the control loop. CBK's banking-sector mechanism describes documented channels, prompt acknowledgement, fair investigation, a reasoned outcome and escalation to the Central Bank where appropriate [8]. The architecture therefore treats a complaint as both an individual case requiring resolution and a portfolio signal. Repeated complaints about a reason code, contact channel, branch, model version or intervention reveal a possible design defect. Root-cause analysis feeds the policy owner, model-risk team, data-protection function and product committee while the individual remedy proceeds on its own timetable.

## 6. Explanation, fairness and vulnerability

An explanation should tell the customer what happened and give an authorised reviewer enough evidence to act. The architecture uses two linked layers. The **decision reason** names the material explicit facts and policy rule, such as a recent scheduled-to-actual payment gap, current facility utilisation and the affordability rule governing a proposed limit. The **model evidence record** gives validators the feature values, nonlinear contributions, posterior uncertainty, residual AI-block contribution, support status and sensitivity checks. The customer receives plain language and available choices; the reviewer receives the governed evidence package.

Residual AI evidence requires special care. Part 2a strips from the neural representation the linear and nonlinear variation already represented by explicit features, while Part 2b shrinks the residual block through regularised horseshoe priors. An explanation can therefore state that an approved behavioural pattern contributed incremental evidence after the named explicit variables, then show whether the same decision survives without that block. The architecture does not invent a human motive for a latent coordinate. When the residual block becomes decisive and no stable customer-facing reason exists, the gate can route the case to review or restrict the block to monitoring until explanation and outcome evidence mature.

Fairness is evaluated as a system property. The NIST AI Risk Management Framework provides a useful voluntary comparator by placing validity, reliability, transparency, explainability, privacy and harmful-bias management within a continuous govern, map, measure and manage cycle [9]. For MSME credit, the measurement unit must also respect the enterprise form, product, sector, geography, channel and data availability. Audit attributes are processed under an approved lawful basis, separated from production decisioning where appropriate and never inferred from a location proxy merely to complete a metric.

For group \(g\) and score bin \(B_k\), group-conditional calibration can be monitored through:

\[
\Delta^{\mathrm{cal}}_{g,k}
=
\mathbb E[Y\mid \widehat p\in B_k,G=g]
-
\mathbb E[\widehat p\mid \widehat p\in B_k,G=g].
\]

Conditional error gaps can complement calibration. Equal opportunity, for example, compares true-positive rates across groups for a carefully defined favourable outcome, while equalized odds also compares false-positive rates [10]. In collections, the outcome label must match the decision. Approval error, unnecessary limit restriction, failure to offer an eligible support action and escalation to intensive recovery are different events. A metric defined around default prediction cannot alone assess whether contact burden or restructure access was fair.

Calibration and error-rate parity can conflict when outcome prevalence differs across groups, even for informative risk scores [11]. The governance response is a declared measurement portfolio rather than selection of the most convenient statistic. The monthly fairness pack reports sample size and intervals for approval, price, limit, support eligibility, intervention receipt, contact frequency, complaints, durable cure, re-default, write-off and discounted net recovery. Intersectional slices are reviewed where data support them. Small groups receive uncertainty intervals and pooled monitoring rather than unstable league tables.

Vulnerability is handled through service design. A temporary illness, bereavement, business interruption, disability, low literacy or language need may alter the suitable channel and human support route. The system records only the minimum information required for an authorised purpose, places sensitive details behind restricted access and expires temporary accommodations according to policy. A vulnerability flag cannot become an unreviewed risk penalty. Contact policies specify permitted times, frequency, channel preference, identity verification and escalation, while collectors see the accurate balance, prior promises, disputes and accommodations before engagement.

Fairness review also follows benefits. If a payment-alignment tool is effective, the institution asks who was eligible, who was offered it, who accepted it and who achieved durable cure. Unequal access to a beneficial treatment can matter as much as unequal exposure to an adverse decision. Complaint text and call-quality review provide qualitative evidence alongside rates. Customer interviews can reveal whether the intervention was understood, whether it preserved supplier or employee payments, and whether the revised schedule remained workable after the first successful instalment.

## 7. Learning which interventions work

Part 2b established the difference between prognosis and causal identification. Part 3 turns that distinction into an intervention protocol. Randomisation occurs only after the gate has removed actions that are unlawful, contractually unavailable, unaffordable, operationally unsupported or required as mandatory protection. The experiment compares two or more permissible alternatives about which the institution has genuine uncertainty. Customers retain the disclosures, service standards, reconsideration and complaint routes applicable to every arm.

Evidence from credit experiments explains why this discipline matters. A Kenyan randomised evaluation of performance-contingent finance for micro-distributors compared fixed debt with equity-like, hybrid and indexed structures, finding that contract design changed business and repayment outcomes [12]. In India, a two-month microfinance grace period increased business investment and long-run profits while also increasing default [13]. The results point in the same methodological direction: product flexibility can redistribute benefit and risk, so a lender should measure enterprise outcomes, repayment, cost and selection together.

The primary estimand for intervention \(a\) against comparator \(a_0\) is defined in the eligible population:

\[
\tau^{\mathrm{DC}}_{a,a_0}(H)
=
\mathbb E\!\left[
I^{\mathrm{DC}}_H(a)-I^{\mathrm{DC}}_H(a_0)
\mid S\in\mathcal E_{a,a_0}
\right],
\]

with companion estimands for re-default, discounted net recovery, business continuity, complaints and contact burden. Durable cure requires a defined arrears exit followed by sustained performance over the registered window. A payment made immediately after intensive contact is an intermediate response, not the complete outcome. The analysis includes take-up, non-compliance, censoring and interference where businesses share customers, suppliers, guarantors or local shocks.

The first controlled pilot uses a stable randomised policy with recorded assignment probabilities. Mandatory hardship or protection routes remain outside randomisation. Allocation can be stratified by product, baseline risk band, enterprise size and relevant cohort variables, with clusters used when treatment may spill across branches or relationship managers. Pre-specified stopping rules cover customer harm, complaints, arrears, model failure, operational incidents and imbalance. A data-monitoring group reviews blinded or appropriately partitioned results under a charter.

Adaptive policies belong to a later challenger stage. A contextual bandit can learn which available action performs best for a state, but only after actions, propensities, costs and delayed outcomes are logged reliably. For a deterministic evaluation policy \(\pi\), a doubly robust estimate of value is:

\[
\widehat V_{\mathrm{DR}}(\pi)
=\frac{1}{n}\sum_{i=1}^{n}
\left[
\widehat\mu(X_i,\pi(X_i))
+\frac{\mathbf 1\{A_i=\pi(X_i)\}}{\widehat e(A_i\mid X_i)}
\left\{Y_i-\widehat\mu(X_i,A_i)\right\}
\right],
\]

where \(\widehat e\) is the logged or estimated treatment propensity and \(\widehat\mu\) the outcome model [14]. The estimator gains robustness when at least one nuisance component is adequately specified, while credible use still requires overlap, correct timing, consistent treatment definitions and stable logging. Propensity floors, bounded importance weights, time-forward evaluation and subgroup diagnostics protect against a policy whose apparent value depends on rare assignments.

When randomisation is unavailable, the design follows the assignment mechanism. A policy threshold may support regression discontinuity near the cutoff. Staggered branch adoption may support difference-in-differences if pre-trends and concurrent changes are credible. A capacity lottery can serve as an instrument when it affects the outcome through treatment and satisfies the other identifying conditions. Target-trial emulation can structure an observational comparison using explicit eligibility, time zero, strategies, follow-up and censoring. Each route identifies a narrower claim than an RCT, and the evidence label travels with the resulting treatment estimate into the gate.

## 8. Portfolio triggers and accountable management information

Individual actions accumulate into portfolio consequences. The management pack connects model, policy, treatment, cash and customer outcomes by product, vintage, sector, geography, institution and intervention cohort. It reports calibration, missingness, support-range exceptions, approval and limit movements, arrears entry, modification, cure, re-default, gross and net recovery, contact cost, complaints, human-review volume and override outcomes. Finance can reconcile these states to balances and cash; risk can reconcile them to exposure and loss; conduct teams can examine treatment and recourse.

A portfolio threshold is most useful when uncertainty accompanies it. For metric \(M_t\) and approved threshold \(c\), the monitoring engine can report:

\[
q_t=P(M_t>c\mid\mathcal D_t),
\]

alongside the point estimate, interval, denominator and data maturity. Escalation may progress from analyst investigation to policy-owner review, temporary restriction, committee action and documented release. The action depends on cause and consequence. A data-quality failure can suspend a feature path while contractual servicing continues. Calibration deterioration can return uncertain cases to human review. A concentration breach can restrict new exposure. A statistically stable increase in durable re-default can prompt a product or intervention redesign.

Population Stability Index, feature drift and embedding drift remain screening measures. They trigger diagnosis of changes in population, data generation, product rules, economic conditions and outcomes. Release decisions use performance, calibration, economic value and customer impact rather than a standalone heuristic. Each trigger records the owner, evidence window, action, expiry, cure test and committee authority.

## 9. Conclusion

Continuous underwriting becomes an institutional capability when it connects early evidence to a lawful and accountable choice. The architecture in Part 3 gives that connection a formal shape. Prognostic distributions describe future states. Causal designs estimate the effects of permissible alternatives. The Credit Policy and Compliance Gate defines feasible actions. Named owners communicate and execute those actions. A treatment ledger then measures cash, durable cure, re-default, cost, complaints and business continuity.

This is how underwriting for collection moves from a slogan to a governed operating system. The lender can intervene earlier without converting every signal into restriction, learn from real outcomes without confusing treatment selection with model performance, and preserve a reviewable record from data cutoff to customer resolution. Part 4 will carry this decision contract into the enterprise technology, identity, event and audit architecture. Part 5 will translate its outcomes into pricing, expected loss, capital, liquidity and funding. Part 6 will turn the controls and estimands into a staged research and implementation programme with banks and ecosystem partners.

```{=latex}
\clearpage
```

## References

[1] Central Bank of Kenya, *Prudential Guidelines for Institutions Licensed under the Banking Act*, Guideline on Consumer Protection, CBK/PG/22, Jan. 2013. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2016/08/PRUDENTIAL-GUIDELINES.pdf. Accessed: Sep. 6, 2026.

[2] Republic of Kenya, *The Central Bank of Kenya (Digital Credit Providers) Regulations, 2022*, Legal Notice No. 46 of 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2022/46/eng%402022-04-22. Accessed: Sep. 6, 2026.

[3] Republic of Kenya, *Data Protection Act, 2019*, No. 24 of 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15. Accessed: Sep. 6, 2026.

[4] Republic of Kenya, *The Data Protection (General) Regulations, 2021*, Legal Notice No. 263 of 2021. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng%402022-12-31. Accessed: Sep. 6, 2026.

[5] Office of the Data Protection Commissioner, *Guidance Note for Digital Credit Providers*, Nairobi, Kenya, Dec. 2023. [Online]. Available: https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Note-for-Digital-Credit-Providers.pdf. Accessed: Sep. 6, 2026.

[6] Republic of Kenya, *The Banking (Credit Reference Bureau) Regulations, 2020*, Legal Notice No. 55 of 2020, rev. Dec. 31, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2020/55/eng%402022-12-31. Accessed: Sep. 6, 2026.

[7] Republic of Kenya, *Consumer Protection Act, 2012*, No. 46 of 2012, rev. Dec. 31, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2012/46/eng%402022-12-31. Accessed: Sep. 6, 2026.

[8] Central Bank of Kenya, *Resolution of Customer Complaints in the Banking Sector*, Dec. 2023. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2023/12/Customer-Complaints-Handling-Mechanism.pdf. Accessed: Sep. 6, 2026.

[9] E. Tabassi, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1. Gaithersburg, MD, USA: National Institute of Standards and Technology, Jan. 2023, doi: 10.6028/NIST.AI.100-1.

[10] M. Hardt, E. Price and N. Srebro, “Equality of Opportunity in Supervised Learning,” in *Advances in Neural Information Processing Systems 29*, 2016. [Online]. Available: https://proceedings.neurips.cc/paper_files/paper/2016/hash/6a9659feb1216f14f7384ba499518b38-Abstract.html. Accessed: Sep. 6, 2026.

[11] A. Chouldechova, “Fair prediction with disparate impact: A study of bias in recidivism prediction instruments,” *Big Data*, vol. 5, no. 2, pp. 153-163, 2017, doi: 10.1089/big.2016.0047.

[12] F. Cordaro, M. Fafchamps, C. Mayer, M. Meki, S. Quinn and K. Roll, “Microequity and mutuality: Experimental evidence on credit with performance-contingent repayment,” National Bureau of Economic Research, Cambridge, MA, USA, Working Paper 30411, Sep. 2022, doi: 10.3386/w30411.

[13] E. Field, R. Pande, J. Papp and N. Rigol, “Does the classic microfinance model discourage entrepreneurship among the poor? Experimental evidence from India,” *American Economic Review*, vol. 103, no. 6, pp. 2196-2226, 2013, doi: 10.1257/aer.103.6.2196.

[14] M. Dudik, J. Langford and L. Li, “Doubly robust policy evaluation and learning,” in *Proc. 28th Int. Conf. Machine Learning*, Bellevue, WA, USA, 2011, pp. 1097-1104. [Online]. Available: https://icml.cc/2011/papers/554_icmlpaper.pdf. Accessed: Sep. 6, 2026.
