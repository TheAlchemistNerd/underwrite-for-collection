---
title: "Underwrite for Collection"
subtitle: "Part 4: Bank-Controlled Research Sandboxes and Enterprise Credit Architecture"
author: "Nevil Maloba"
email: "nevillemaloba@gmail.com"
date: "6 September 2026"
lang: "en-GB"
---

# Abstract

Lifecycle underwriting becomes institutional when a bank can reproduce the evidence, model, policy and human authority behind a decision without releasing an unrestricted customer dataset or turning a research prototype into an ungoverned production service. Part 4 designs that institutional boundary. It establishes a bank-controlled research sandbox, a canonical event and identity fabric, purpose-bound model-to-data access, progressive evidence stages from synthetic development to shadow scoring, and an approved artefact lifecycle with deterministic serving, fallback and rollback. Privacy-enhancing methods are matched to explicit threats rather than treated as substitutes for governance. Experiment assignment, treatment receipt and matured outcomes enter the same lineage as payments, modifications, cures and recoveries. Explicit integration contracts then carry authorised results into origination, core banking, servicing, collections, finance, expected-credit-loss, capital and treasury processes while preserving their separate ownership. The resulting architecture makes rigorous research compatible with bank accountability, customer rights, independent validation, operational resilience and controlled publication.

## 1. Bring the method to the bank

A relationship manager visits a small food processor whose instalment has just failed. The enterprise is still producing, its retail orders remain visible and two invoices should settle within ten days. Its bank systems hold a more fragmented story. The core loan account records the missed amount. Payments hold incoming and outgoing cash. The relationship platform holds a call note. A collections application has opened a case. The credit bureau file may reflect a different reporting date. The model service has an earlier risk estimate, and the research team that designed a proposed lifecycle challenger has none of the identifiable records.

The conventional response is to ask for an anonymised extract and analyse it elsewhere. That request often compresses a difficult institutional problem into a file-transfer problem. Removing names does not necessarily remove the possibility of re-identification. An MSME's sector, location, facility size, transaction rhythm and uncommon sequence of events can together become identifying. A static extract also loses corrections, decision-time availability, policy versions and the operational actions that changed the later outcome. The file may be safer than a production database, yet less capable of answering the research question and harder to reconcile to the bank's books.

The stronger design brings approved research code to governed data. Customer records remain within a bank-controlled boundary. A purpose-specific analytical view exposes only the fields and history required for the registered study. Stable pseudonymous keys connect facilities, payments, interventions and outcomes, while the identity map remains in a separately controlled service. The researcher can test the pipeline, inspect approved summaries and submit reproducible jobs without acquiring a portable copy of the loan book. Independent validators can replay the same versioned job against the same point-in-time snapshot. Disclosure reviewers decide which aggregate tables, coefficients, diagnostics or model artefacts may leave the environment.

This arrangement is both an evidential and a rights architecture. Kenya's Data Protection Act requires lawful, fair and transparent processing, explicit and legitimate purposes, data minimisation, accuracy, storage limitation and appropriate safeguards. It also requires a data-protection impact assessment where processing is likely to create high risk, addresses significant solely automated decisions, embeds protection by design and permits research processing only with the applicable conditions and safeguards [1]. The Data Protection (General) Regulations make these duties operational through retention schedules, pseudonymisation, automated-decision controls, accuracy measures and DPIA triggers that include large-scale linkage, significant profiling and innovative processing in the specified circumstances [2].

The ODPC's 2025 research guidance is especially relevant to this programme. It treats research processing as a risk-based activity rather than a blanket exemption, calls for purpose and lawful-basis analysis, data minimisation, secure handling, data-sharing agreements where required and non-identifiable publication, and expressly identifies trusted research environments among available privacy-enhancing measures [3]. The practical question is therefore not whether a dataset has been called anonymous. It is whether the participating institutions can demonstrate why each item is processed, who can act on it, how access is controlled, how outputs are checked, when records are removed and how a customer's rights remain exercisable.

The bank-controlled research sandbox is the place where those controls, the Part 2a evidence contract, the Part 2b model artefact and the Part 3 intervention contract meet. It is an internal research and validation environment. It does not itself confer regulatory permission to launch a new product or customer treatment. A live pilot follows only after the licensed institution has completed the relevant legal, risk, conduct, model, technology and supervisory pathway.

## 2. The control boundary is an operating model

The word *sandbox* can suggest a disposable technical playground. Here it means a governed collection of environments with named owners, permitted data movements and release gates. The bank remains the data controller or otherwise records the applicable controller and processor roles. It owns the customer relationship, product decision, Credit Policy and Compliance Gate, production credentials and systems of record. A research institution, technology supplier or model developer may supply code, methods and analysis under an approved mandate. It does not acquire the bank's authority merely because its model produces a probability.

That retained authority has a concrete Kenyan banking implication. The CBK Guidance Note on Cybersecurity places responsibility for the institution's cyber strategy, policy and standards with its board and senior management and recognises risks arising through privileged access, interconnected systems and service providers [4]. The CBK Guideline on Outsourcing requires institutions to manage the risks of outsourced activities and identifies information-system management, loan-application processing, research and bad-debt collection among activities that may be material. It also reserves core management and lending decisions to the institution, including the decision to grant loans and determine compliance with applicable requirements [5]. A model-to-data arrangement must therefore preserve bank control over decision rights as carefully as it preserves custody of records.

The architecture contains six connected planes:

1. **Systems of record** hold legally and operationally authoritative customer, facility, payment, servicing, collection and accounting events.
2. **The evidence plane** reconstructs point-in-time features, outcomes and data-quality states from versioned source events.
3. **The research plane** provides synthetic, pseudonymised or approved aggregate views according to the study and user role.
4. **The model plane** trains and validates challengers offline, then registers an approved, signed and reproducible scoring artefact.
5. **The decision plane** combines model output with the versioned Credit Policy and Compliance Gate, human authority and customer communication.
6. **The record and learning plane** sends executed terms, realised cash, complaints, cures, re-defaults and recoveries to operational systems and future validation.

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
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 34, "rankSpacing": 48}
}}%%
flowchart LR
    S[SOURCE SYSTEMS AND EVIDENCE<br/>authoritative events, pseudonymous keys,<br/>point-in-time state and reconciliation] --> R[RESEARCH AND VALIDATION<br/>purpose-bound views, approved code,<br/>independent challenge and secure analysis]
    R --> M[MODEL ARTEFACT AND POLICY GATE<br/>transforms, posterior summaries, calibration,<br/>law, contract, affordability and human route]
    M --> X[CUSTOMER ACTION AND DOWNSTREAM RECORDS<br/>decision, communication, terms, cash, ECL inputs,<br/>capital, treasury and experiment outcomes]
    X -->|Matured outcomes| S

    classDef source fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.8px;
    classDef research fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.8px;
    classDef decision fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.9px;
    class S source;
    class R research;
    class M,X decision;
```

**Figure 1: The bank-controlled lifecycle-credit architecture.** The research team works through an approved analytical boundary. The licensed institution retains the source records, model release, policy gate, customer action and downstream financial record. Matured outcomes return to the evidence plane without rewriting the information available at the original decision.

The planes are logical boundaries, not a demand for six technology products. A smaller institution may implement several planes on one private-cloud platform with separate identities, storage policies and deployment accounts. A larger bank may use different systems and teams. The control requirement remains the same: every material data movement, transformation, approval and decision must have one accountable owner and a reproducible contract.

## 3. One event fabric, several accountable records

Part 2a defined why a payment is not one timestamp. Part 4 assigns that temporal truth to operating systems. A transaction has an economic time, an ingestion time, a time when the bank could first use it, and sometimes a correction time. A customer decision has a cutoff, a policy effective time and an execution time. If those clocks are compressed into one database update timestamp, a later correction can leak into a historical training row and an old score can appear more informed than it was.

Each accepted event therefore enters the evidence plane through a canonical envelope:

\[
\mathcal E_k=
\left(
e_k,\;s_k,\;t_k^{\mathrm{event}},\;t_k^{\mathrm{known}},
t_k^{\mathrm{effective}},\;v_k^{\mathrm{schema}},\;v_k^{\mathrm{definition}},
q_k,\;r_k,\;h_k
\right),
\]

where \(e_k\) is a unique event identifier, \(s_k\) the source system, the three times record occurrence, institutional availability and business effectiveness, \(v^{\mathrm{schema}}\) and \(v^{\mathrm{definition}}\) identify the technical and business meaning, \(q_k\) carries quality and correction status, \(r_k\) identifies the superseded or related event, and \(h_k\) is a content digest used to detect unintended alteration. A reversal or correction creates a related event. It does not silently replace the historical record used by a prior decision.

Canonical identifiers connect customer, enterprise, facility, account, collateral or guarantee, payment, servicing case, intervention and outcome. Direct identifiers remain in the system that needs them. The evidence plane uses stable pseudonymous keys. This gives the research programme longitudinal continuity without making names, telephone numbers, national identifiers or free-text case notes ubiquitous analytical fields. The mapping service is separately permissioned, and its use is itself logged.

The mapping service also maintains the temporal economic-entity graph defined in Part 2a. Deterministic links begin with verified legal ownership, authorised account control, facility liability, settlement identifiers and explicit contractual relationships. Probabilistic matching can propose links from approved attributes and relational context, but its candidates retain confidence and review status. Every relationship carries valid and knowledge intervals so a later change in ownership, signatory or account use does not rewrite an earlier decision.

Cash provenance is implemented as a separate governed service downstream of canonicalisation. It pairs internal transfers, decomposes aggregator settlements where authorised evidence exists, links refunds and reversals to their economic event, identifies candidate cycles and assigns an economic cash class with a versioned reason. The service publishes operating, liquidity, financing, capital, internal and unresolved views. It does not alter the account ledger or infer customer motive. Material uncertainty travels into the feature, model and policy packets.

System ownership follows the event's meaning. The core lending or product subledger owns contractual principal, interest, charges and status. The payments system owns settlement events. The customer and relationship systems own verified communication and authorised profile changes. Collections owns case actions and promises, while the contract system owns executed modifications. Finance owns journals and reporting classifications. The research evidence plane does not become a competing book of record. It preserves source identifiers, derives registered analytical states and reconciles those states to their owners.

| Record family | Authoritative owner | Analytical representation | Required control |
|---|---|---|---|
| Facility and contractual schedule | Product subledger or core lending system | Versioned cash-flow schedule and product state | Executed terms, effective date and amendment lineage |
| Payment and settlement | Payments and account ledger | Eligible cash event with availability time | Duplicate, reversal, value-date and settlement reconciliation |
| Entity and economic cash provenance | Identity owners, account-control records, payments, settlement and approved enterprise evidence | Temporal graph, economic-event path, cash class, confidence and unresolved value | False-merge and false-split tests, transfer pairing, monetary reconciliation, purpose and access control |
| Delinquency and collection | Servicing and collections systems | State transition, case and contact event | Approved DPD definition, channel, outcome and complaint link |
| Modification and restructure | Contract and credit workflow | New schedule and modification classification | Authority, affordability, customer acceptance and accounting flag |
| Model and policy decision | Scoring service and decision engine | Immutable decision packet | Evidence cutoff, artefact, policy, reasons, override and execution |
| Recovery and closure | Recovery subledger and finance | Gross cash, direct cost, net recovery and closure | Cash receipt, cost allocation, write-off and control-total reconciliation |

**Table 1: Proposed source-of-record and analytical-ownership matrix.** A derived lifecycle state remains traceable to the authoritative events that support it. Ownership is assigned by economic and legal meaning, not by whichever platform happens to display the result.

Risk data must also be fit for aggregation. The Basel Committee's risk-data principles emphasise governance, common identifiers, metadata, accuracy, completeness, timeliness, reconciliation, authoritative sources and independent validation. The principles were initially directed at systemically important banks, but their architecture provides a useful proportionate benchmark for any institution attempting to connect model evidence to material risk decisions [6]. A small bank may implement fewer platforms; it does not need weaker definitions.

Before a model is trained, the evidence plane tests temporal validity and balance identities. For facility \(i\) over period \(t\), a simplified control is:

\[
B_{i,t}^{\mathrm{close}}
=B_{i,t}^{\mathrm{open}}
+D_{i,t}+I_{i,t}+F_{i,t}
-P_{i,t}-C_{i,t}-W_{i,t}+A_{i,t},
\]

where \(D\) is disbursement or draw, \(I\) accrued interest, \(F\) charges, \(P\) eligible payment, \(C\) credits or reversals in the customer's favour, \(W\) write-off and \(A\) other approved adjustments. Each term has a source, sign convention and availability time. Aggregate balances reconcile to portfolio and general-ledger control totals within approved tolerances. An unreconciled population can remain available for data-quality diagnosis, but it cannot quietly become the champion's training population.

The economic-cash views add a second reconciliation. The sum of external operating, financing, capital, internal, refund or reversal, exceptional and unresolved classes must reproduce accepted source credits after currency, fee, duplication and consolidation adjustments. Paired internal transfers reconcile across sender and receiver accounts and contribute once to consolidated economic flow. Aggregator decompositions reconcile to the net bank settlement and retained fees, reserves, refunds or chargebacks. Exceptions remain visible by event count and monetary value until corrected, approved or expired under policy.

At decision time, the scoring service writes a compact decision packet containing the evidence snapshot, feature and model versions, posterior summaries, support and quality states, policy version, available actions, selected route, human authority, customer communication and downstream keys. The packet's identity can be expressed as:

\[
d_{i,t}=H\!\left(
x_{i,t}^{\mathrm{PIT}},
v_{\mathrm{graph}},v_{\mathrm{provenance}},
v_{\mathrm{feature}},v_{\mathrm{model}},v_{\mathrm{cal}},
v_{\mathrm{policy}},a_{i,t},o_{i,t}
\right),
\]

where \(H\) is a governed digest, \(v_{\mathrm{graph}}\) and \(v_{\mathrm{provenance}}\) identify the relationship and economic-cash interpretations used, \(a_{i,t}\) the executed action and \(o_{i,t}\) the authorised override record where one exists. The digest is an integrity control and lookup key. The underlying evidence, approvals and records remain the substantive proof of what happened.

## 4. Model-to-data access and the trusted research environment

The research workspace begins with a registered purpose, not a broad entitlement to explore. Its protocol names the question, population, variables, outcome horizon, legal basis, retention period, users, processors, publication plan and prohibited uses. The DPIA links that protocol to foreseeable harms, data-subject rights, automated-decision effects, re-identification risk, security, mitigations and residual-risk ownership. A material change in features, linkage, population, partner, infrastructure or customer effect reopens the assessment.

Access is the intersection of several permissions:

\[
\mathcal D_{u,t}^{\mathrm{allow}}
=\mathcal D^{\mathrm{role}}_u
\cap\mathcal D^{\mathrm{purpose}}_p
\cap\mathcal D^{\mathrm{environment}}_z
\cap\mathcal D^{\mathrm{approval}}_a
\cap\mathcal D^{\mathrm{time}}_t.
\]

The user must have the right role, the dataset must serve the registered purpose, the environment must be approved for its sensitivity, the required authorisation must be active, and the credential must remain within its time window. Row and column policies can further constrain products, institutions, regions or outcome maturity. Service identities receive the same discipline as people. Production-scoring credentials cannot be reused in a notebook, and a research job cannot write into a customer decision table.

The architecture separates five zones. The production zone retains direct identity and transactional authority. The linkage zone creates and controls pseudonymous keys. The research zone contains approved variables and tools, normally without unrestricted internet access or removable storage. The validation zone can reproduce the work but remains organisationally independent of development. The release zone checks proposed outputs for small cells, unusual combinations, sensitive text, model leakage and contractual restrictions. Re-identification is available only to an authorised operational function for a defined customer or data-quality purpose, never as a routine research convenience.

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
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 36, "rankSpacing": 50}
}}%%
flowchart TB
    subgraph CUSTODY[DATA CUSTODY AND PURPOSE]
        direction LR
        P[PRODUCTION AND IDENTITY<br/>contracts, transactions,<br/>customer action] --> K[CONTROLLED LINKAGE AND PROVENANCE<br/>pseudonymous keys, temporal entity graph,<br/>cash paths, classes and confidence]
        K --> R[TRUSTED RESEARCH<br/>purpose-limited views,<br/>versioned jobs and no raw export]
    end
    subgraph ASSURANCE[ASSURANCE AND RELEASE]
        direction LR
        V[INDEPENDENT VALIDATION<br/>replay, benchmarking,<br/>fairness and failure tests] --> O[CONTROLLED OUTPUT<br/>disclosure review,<br/>publication and artefact approval]
        O --> S[PRODUCTION SCORING<br/>deterministic interface,<br/>least privilege and monitoring]
    end
    CUSTODY -->|Validated research package| ASSURANCE
    ASSURANCE -->|Approved artefact and decision record| CUSTODY

    classDef production fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.9px;
    classDef controlled fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.9px;
    classDef assurance fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.9px;
    class P,S production;
    class K,R controlled;
    class V,O assurance;
```

**Figure 2: The model-to-data research boundary.** Direct identity remains in production, longitudinal research uses controlled pseudonymous linkage, validation is independent, and only disclosure-checked results or approved artefacts leave the research path. Re-identification follows a named operational purpose and authority.

The controls are more than authentication. Workspace images and dependencies are versioned. Data imports are approved and scanned. Queries, jobs and output requests are logged. Secrets come from a managed service and are not written into notebooks. Privileged access is time-limited and reviewed. Backups follow the same sensitivity classification as primary storage. Retention covers source snapshots, derived tables, logs, model artefacts and temporary files rather than deleting only the convenient copy.

The research environment also preserves intellectual honesty. A public or synthetic dataset may be copied into development. A pseudonymised institution dataset remains controlled personal data where attribution remains possible. A table may leave the workspace only after disclosure review. A model artefact can itself reveal sensitive information and is therefore classified, tested and released deliberately. NIST's AI Risk Management Framework provides a useful voluntary lifecycle vocabulary for governing, mapping, measuring and managing these socio-technical risks [7]. The NIST Privacy Framework complements it by linking data processing to privacy risk and organisational outcomes [8]. Kenyan law and the bank's approved controls remain the governing authority.

## 5. Progress through evidence stages, not data shortcuts

The absence of a portable bank dataset does not stop development. It changes the order of proof. Public KBA, CBK, KNBS and other authoritative series can establish sector context and exercise acquisition controls. A synthetic portfolio can reproduce product schedules, selection, censoring, delayed outcomes, modifications, interventions, macroeconomic regimes and deliberate data faults. These materials are appropriate for testing schemas, code, estimands, power, recovery logic and failure handling. They do not establish the accuracy, fairness or commercial value of a model for Kenyan MSMEs.

Institutional evidence begins with a secure retrospective reconstruction. The bank maps definitions, rebuilds point-in-time snapshots, measures missingness, reconciles balances and tests the transparent benchmark before exposing an advanced challenger. Shadow scoring then runs the approved candidate prospectively without changing a customer's price, limit, treatment or collection path. It reveals latency, coverage, support excursions, calibration as outcomes mature, operational failure and disagreement with the existing process. A live pilot follows as a separate decision, with lawful treatments, eligibility, assignment, customer safeguards, stop rules and accountable owners. This progression prevents a technically successful notebook from being mistaken for a validated credit service.

Privacy-enhancing technology enters only where its protection matches the threat. A single-bank study will usually obtain more control and less complexity from a well-administered private workspace or secure enclave than from federated learning. Federated learning becomes relevant when several institutions seek a shared model while retaining local records. For institution \(j\), a simplified objective is:

\[
\min_{\theta}\;\sum_{j=1}^{J}\pi_j L_j(\theta),
\qquad \pi_j\ge 0,\quad \sum_j\pi_j=1,
\]

with local losses \(L_j\), agreed weights \(\pi_j\) and a shared parameter vector \(\theta\). The founding method shows how local updates can train a common model without centralising the underlying observations [9]. That does not make the updates harmless. Institutions can have materially different sectors, products, definitions and policies; an update can leak information, be poisoned or conceal weak performance in a small participant.

Secure aggregation can prevent the coordinator from seeing each institution's update in the clear while still recovering an authorised aggregate [10]. Differential privacy can bound how much a released statistic or trained artefact changes when one protected unit is added or removed, but only after the privacy unit, adjacency relation, clipping, mechanism and cumulative budget are defined. NIST's guidance also emphasises implementation hazards and the need to evaluate the complete guarantee, not merely the presence of noise [11]. A trusted execution environment can protect code and data during computation from parts of the surrounding infrastructure, while attestation, side-channel analysis, key management, patching and operator responsibilities remain necessary. These mechanisms complement purpose limitation, access control, validation and disclosure review. They do not replace them.

## 6. Promote a complete artefact and preserve a safe return path

The approved production object is more than a coefficient file. It contains the data contract, feature definitions, point-in-time transforms, spline bases, hierarchy maps, residualiser and encoder versions where used, calibration, posterior scoring quantities, uncertainty rules, support ranges, reason mappings, policy interface, dependencies, test evidence, effective date, expiry, fallback and rollback identifier. Its registry entry links the development dataset, code revision, environment lock, validation report, approvals and known limitations.

Registry states are explicit: development, validation, approved for shadow use, approved for bounded production, restricted, superseded and retired. Promotion requires independent evidence and named authority. A model may pass numerical tests and remain unsuitable because its population is too narrow, its explanations cannot support the action, its latency is unstable or its operational fallback has not been exercised.

Before release, the production implementation is compared with the independently validated reference. For a registered test set \(\mathcal T\), the equivalence condition may be written:

\[
\max_{i\in\mathcal T}
\left|\widehat p_i^{\mathrm{prod}}-\widehat p_i^{\mathrm{ref}}\right|
\le \varepsilon_p,
\qquad
\max_{i\in\mathcal T}
\left|\widehat u_i^{\mathrm{prod}}-\widehat u_i^{\mathrm{ref}}\right|
\le \varepsilon_u,
\]

where \(\widehat p\) is the calibrated risk quantity, \(\widehat u\) an approved uncertainty output and the tolerances are justified before testing. Schema, missing-value, new-group, boundary, concurrency and degraded-dependency fixtures accompany the numerical comparison.

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
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 34, "rankSpacing": 48}
}}%%
flowchart TB
    subgraph RELEASE[CONTROLLED RELEASE PATH]
        direction LR
        D[DEVELOP AND VALIDATE<br/>versioned evidence, code,<br/>fairness and failure tests] --> S[SHADOW AND RELEASE GATE<br/>prospective scores, no customer effect,<br/>equivalence and policy approval]
        S --> P[BOUNDED PRODUCTION<br/>signed artefact, deterministic scoring,<br/>expiry and least privilege]
        P --> M{JOINT MONITORING<br/>calibration, drift, cash,<br/>conduct and operations}
    end
    subgraph RETURN[SAFE RETURN PATH]
        direction LR
        F[SAFE FALLBACK<br/>explicit-only or policy route,<br/>owner and recovery condition] --> V[INDEPENDENT REVALIDATION<br/>repair, replay and<br/>controlled re-release]
        R[ROLLBACK<br/>previous approved artefact,<br/>incident review and notification] --> V
    end
    RELEASE -->|Data degradation or material failure| RETURN
    RETURN -->|Approved re-release| RELEASE

    classDef build fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.8px;
    classDef assure fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.8px;
    classDef decide fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.9px;
    class D,S,P build;
    class V,M assure;
    class F,R decide;
```

**Figure 3: Model promotion, bounded production and safe return.** Shadow use generates prospective operating evidence before customer effect. Production retains tested fallback and rollback paths, while material failures return the artefact to independent review rather than triggering an unrecorded repair.

Fallback is designed before failure. If the AI representation is unavailable, the approved explicit-only model may serve where validated. If point-in-time features are stale or incomplete, the policy gate can defer, restrict the available action or route the case to a person. If calibration or conduct monitoring breaches a release threshold, the previous approved artefact can be restored. Every route records affected accounts, start and end time, decision consequences, owner and cure evidence.

## 7. Experiment and enterprise records must join at the decision

A causal study cannot be reconstructed from a later list of customers who received a message. The enterprise record stores eligibility time, eligibility-rule version, assignment unit, arm, randomisation or propensity, treatment availability, delivery, receipt, adherence, crossover, contamination, human override and withdrawal. Outcomes retain their definitions and maturity windows. Payments, arrears, cure, re-default, modification, complaint, gross recovery, direct workout cost and net recovery then join through the decision-time keys established earlier.

This design supports intention-to-treat analysis from assignment and per-protocol or treatment-received analysis from execution, with their different assumptions stated. It also prevents a servicing action from becoming an accidental predictor of an outcome it helped create. A reminder sent after emerging arrears belongs to treatment history; the later payment is an outcome. Both may become valid time-varying history at a future decision cutoff, but neither may be moved backwards into the earlier evidence set.

Enterprise integration follows a fit-gap rule. For each calculation, the bank determines whether the existing platform can perform it natively and transparently, whether it belongs in a governed product or analytical service, or whether the platform should receive only the approved result and lineage. The HLR and its uncertainty remain in the model service. Policy permissions remain in the decision service. Contractual balances remain in the product subledger. The general ledger receives balanced accounting events. Part 5's ECL, capital and treasury processes consume approved data and results under their own methodologies rather than inheriting a credit score as an accounting conclusion.

An integration contract specifies event identity, producer, consumer, schema, units, currency, timestamp semantics, idempotency, correction method, service objective, authentication, failure behaviour and reconciliation owner. A successful API response is not proof that the economic event posted correctly. The executed action must reconcile from customer communication to product terms, cash settlement, subledger and control total. Manual adjustments remain possible under maker-checker authority, a reason code and subsequent reconciliation.

## 8. Validation, resilience and ecosystem accountability

Independent validation covers the whole decision service. It challenges the conceptual model, data lineage, point-in-time reconstruction, software implementation, policy interface, customer explanations, group outcomes, operational capacity and failure modes. The output-release process separately checks whether a proposed research table, narrative or artefact is authorised, statistically supportable and sufficiently protected. This permits rigorous publication without turning a public paper into a map of customer records or security controls.

Third-party participation follows the same lifecycle. The bank assesses criticality, data access, subcontractors, concentration, security, service levels, audit rights, incident notification, business continuity, exit and portability. The FSB's third-party risk toolkit provides a useful international structure for identifying critical services and managing them throughout the relationship [12]. The Basel operational-resilience principles add governance, critical-operation mapping, tolerance for disruption, testing, dependency management and incident recovery [13]. These complement the CBK requirements already governing the participating bank.

The RACI is economical but explicit. The bank's business and credit functions own the product and decision. Data owners certify sources and quality. The model owner develops or sponsors the artefact. Independent model risk validates it. Compliance, legal, conduct and the data-protection function approve their respective controls. Technology owns the production service and resilience. Collections and servicing own executed interventions. Finance, impairment, capital and treasury own downstream recognition. Internal audit tests the control framework. Researchers own the registered analysis and reproducibility package, while publication requires bank and disclosure approval under the agreed protocol.

Service levels describe customer and risk consequences, not only uptime. They include event freshness, evidence completeness, scoring latency, fallback activation, human-review response, correction propagation, experiment-log completeness, reconciliation breaks, recovery objectives and incident escalation. A degraded service should fail into a known customer-safe and risk-approved state. Its recovery test must demonstrate that delayed events, duplicate actions and conflicting versions cannot silently enter the lifecycle record.

The phrase *regulatory sandbox* remains reserved for a regulator-operated testing regime with its own admission and safeguards. Kenya's Capital Markets Authority, for example, publishes a Regulatory Sandbox Policy Guidance Note for innovative capital-markets products [14]. That framework does not establish a CBK banking pathway for this programme. The proposed environment is therefore a bank-controlled research sandbox followed, where required, by a regulator-engaged controlled pilot under a pathway agreed in writing with the relevant authority.

<!-- U4C-CASE-4-START -->

### Worked replay case: settlement is an observable state

The companion local fixture replays draft, review, approval, execution, a failed settlement attempt, retry and referenced settlement. Execution requires approval, duplicate IDs must agree, and settlement requires a bank reference; exact repeated events are idempotent. Cash becomes available only in the settled state. The verified transitions provide a basis for institution integration: connect the bank interface, authenticate external references, configure production permissions and reconcile the general ledger.

See the worked case appendix, U4C-MSME-001, and the [GitHub research lab](https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab) for the declared hypothetical assumptions, full schedules, calculation code, tests and instructions for reproducing both worked cases.

<!-- U4C-CASE-4-END -->

## 9. Conclusion

Part 4 turns lifecycle underwriting from a compelling method into an accountable banking capability. The source records remain authoritative, research moves to governed data, the champion becomes a complete approved artefact, policy and human authority remain visible, and every intervention returns as a reproducible cash and customer outcome. Synthetic development, retrospective reconstruction, shadow scoring and bounded live use form successive standards of evidence. Privacy, cybersecurity, model risk and operational resilience are designed into those stages rather than added after deployment.

This architecture gives Part 5 a dependable financial interface. Contractual and behavioural cash flows, modifications, cures, defaults, recoveries, treatment costs and uncertainty can enter pricing, ECL, capital, liquidity and funding analysis with their definitions, timestamps and owners intact. The bank can then ask not only whether the model predicted well, but whether the complete system produced more sustainable and collectible credit relationships.

## References

[1] Republic of Kenya, “Data Protection Act, 2019,” *Kenya Law*, 2019. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2022-12-31. [Accessed: Sep. 6, 2026].

[2] Republic of Kenya, “The Data Protection (General) Regulations, 2021,” Legal Notice No. 263 of 2021, *Kenya Law*, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng@2022-01-14. [Accessed: Sep. 6, 2026].

[3] Office of the Data Protection Commissioner, “Guidance Notes: Processing for Research Purposes,” Nairobi, Kenya, 2025. [Online]. Available: https://www.odpc.go.ke/wp-content/uploads/2025/11/ODPC-%E2%80%93-GUIDANCE-NOTES-Processing-for-Research-Purpose.pdf. [Accessed: Sep. 6, 2026].

[4] Central Bank of Kenya, “Guidance Note on Cybersecurity for the Banking Sector,” Nairobi, Kenya, 2017. [Online]. Available: https://www.centralbank.go.ke/uploads/banking_circulars/634077191_GUIDANCE%20NOTE%20ON%20CYBERSECURITY%20FOR%20THE%20BANKING%20SECTOR.pdf. [Accessed: Sep. 6, 2026].

[5] Central Bank of Kenya, “Guideline on Outsourcing, CBK/PG/16,” in *Prudential Guidelines*, Nairobi, Kenya, pp. 393-409. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2016/08/PRUDENTIAL-GUIDELINES.pdf. [Accessed: Sep. 6, 2026].

[6] Basel Committee on Banking Supervision, “Principles for effective risk data aggregation and risk reporting,” Bank for International Settlements, Basel, Switzerland, Jan. 2013, with implementation observations updated Jan. 2026. [Online]. Available: https://www.bis.org/publ/bcbs239.htm. [Accessed: Sep. 6, 2026].

[7] E. Tabassi, “Artificial Intelligence Risk Management Framework (AI RMF 1.0),” National Institute of Standards and Technology, Gaithersburg, MD, NIST AI 100-1, Jan. 2023, doi: 10.6028/NIST.AI.100-1.

[8] National Institute of Standards and Technology, “NIST Privacy Framework: A Tool for Improving Privacy through Enterprise Risk Management, Version 1.0,” Gaithersburg, MD, Jan. 2020. [Online]. Available: https://www.nist.gov/privacy-framework/privacy-framework. [Accessed: Sep. 6, 2026].

[9] H. B. McMahan, E. Moore, D. Ramage, S. Hampson and B. Agüera y Arcas, “Communication-efficient learning of deep networks from decentralized data,” in *Proc. 20th Int. Conf. Artificial Intelligence and Statistics*, vol. 54, 2017, pp. 1273-1282.

[10] K. Bonawitz *et al.*, “Practical secure aggregation for privacy-preserving machine learning,” in *Proc. 2017 ACM SIGSAC Conf. Computer and Communications Security*, 2017, pp. 1175-1191, doi: 10.1145/3133956.3133982.

[11] J. Near, D. Darais and N. Lefkovitz, “Guidelines for Evaluating Differential Privacy Guarantees,” National Institute of Standards and Technology, Gaithersburg, MD, NIST SP 800-226, Mar. 2025, doi: 10.6028/NIST.SP.800-226.

[12] Financial Stability Board, “Enhancing Third-Party Risk Management and Oversight: A Toolkit for Financial Institutions and Financial Authorities,” Basel, Switzerland, Dec. 2023. [Online]. Available: https://www.fsb.org/2023/12/final-report-on-enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities-2/. [Accessed: Sep. 6, 2026].

[13] Basel Committee on Banking Supervision, “Principles for Operational Resilience,” Bank for International Settlements, Basel, Switzerland, Mar. 2021. [Online]. Available: https://www.bis.org/bcbs/publ/d516.htm. [Accessed: Sep. 6, 2026].

[14] Capital Markets Authority, “Regulatory Sandbox Policy Guidance Note,” Nairobi, Kenya, Mar. 2019. [Online]. Available: https://cma.or.ke/wp-content/uploads/2023/03/Regulatory-Sandbox-Policy-Guidance-Note-March-2019-Final.pdf. [Accessed: Sep. 6, 2026].
