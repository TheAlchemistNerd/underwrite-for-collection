# Kenya legal map for sequential credit and Treasury decision systems

**Prepared:** 4 October 2026  
**Purpose:** Research and editorial map for the two proposed articles on sequential collections decisions and Treasury stochastic control.  
**Scope note:** This is a structured research aid, not a Kenyan legal opinion. Counsel and the institution's data-protection, compliance and prudential owners must confirm applicability, current text, contractual context and sector rules before a public claim or deployment.

## 1. Correct the section/article reference first

- **Article 31 of the Constitution of Kenya, 2010** protects the right to privacy, including protection from unnecessary requirement or revelation of family/private-affairs information and infringement of communications.
- **Section 31 of the Data Protection Act, 2019 (DPA)** is the data protection impact assessment (DPIA) provision.
- The Act says it gives effect to Article 31(c) and (d). The article outlines should use the accurate label each time.

## 2. Applicability: whose data and which decisions?

The DPA's data subject is an identified or identifiable natural person. A company borrower is not itself a natural-person data subject. Its sole proprietor, owner, director, guarantor, employee or contact may be. Business-account flows can also reveal an individual when the enterprise is small or the person's transactions are identifiable.

Separate two questions:

1. Is personal data processed at any stage? If yes, the general DPA duties may apply even if the final model sees aggregates.
2. Is an individual subject to a decision based solely on automated processing that has legal effects or significantly affects them? That narrower decision pattern engages DPA s35 and the automated-decision rules; it is not the same question as whether AI was used somewhere in a bank workflow.

An aggregate bank balance-sheet optimizer will often present a different personal-data profile from account-level depositor behavior or a borrower-level collection policy. Aggregation must be evaluated for re-identification risk and does not dispose of confidentiality, prudential, security or other obligations.

## 3. Core statutory and constitutional map

| Source | Relevant provisions | Design implication for this work |
|---|---|---|
| Constitution of Kenya, 2010 | Arts. 27, 31, 46, 47 | Privacy and equality are central. Consumer rights matter for individuals acting as consumers. Fair administrative action applies in its proper public/administrative context; do not assert it automatically governs each internal private-bank decision. |
| Data Protection Act, 2019 | s25 | Lawful, fair, transparent, purpose-limited, necessary, accurate and time-bounded processing; a valid explanation is needed where private-affairs data are required. |
| DPA | ss26–29 | Data subject rights; direct collection as the default with statutory exceptions; use only for lawful, specific, explicit purposes; advance collection notices about rights, purpose, recipients, contacts, safeguards, mandatory/voluntary status and consequences. |
| DPA | s30 | Identify and document an applicable lawful basis. Consent is one basis, not the only one. Contract necessity, legal obligation, public task and legitimate interests each have their own conditions. Further processing must remain purpose-compatible. |
| DPA | s31 | Before processing likely to create high risk, assess operations/purpose, necessity/proportionality, risks and mitigations. If the assessment indicates high residual risk, consult the Data Commissioner before processing. |
| DPA | s32; General Regulations r4 | If relying on consent, explain identity, purpose by operation, data types, relevant automated use, transfers, sharing, withdrawal and consequences; retain evidence of valid consent. |
| DPA | s35; General Regulations r22 | Right not to be subject to a solely automated decision, including profiling, with legal or significant effect, subject to the listed exceptions. The General Regulations define automated individual decision-making as a decision made without human involvement and require notice, meaningful information about logic, significance/consequences, fairness, error prevention, appropriate statistical procedures, inaccuracy correction, bias controls and a route to human intervention and expression of the person's view. |
| DPA | s36 | A data subject may object to processing, subject to the statutory exception for overriding compelling legitimate interests or legal claims. An experiment and adaptive update process need an objection-handling route. |
| DPA | s37 | Commercial use of personal data has a specific rule referring to express consent or authorization under written law with notice, and anonymisation where possible. Its relationship to s30 and a particular lender's model-development or reuse purpose needs Kenyan counsel's analysis; do not treat the ordinary s30 lawful-basis assessment as automatically resolving s37. |
| DPA | ss40–43 | Rectification/erasure; privacy by design/default; security measures; breach notification/communication duties. Keep correction workflows effective in both operational features and relevant records, while retaining evidence only for justified purposes and periods. |
| DPA | ss44–47 | Additional conditions for sensitive personal data, including specific requirements for health data. Classify each feature and derived variable; ordinary financial data are not automatically sensitive, but hardship, health or family-related information and inferences need a documented assessment. Do not infer or use such variables just because they improve prediction. |
| DPA | ss48–50 | Conditions and safeguards for transfers outside Kenya, including safeguards for sensitive data and the provision that may require certain processing to use a Kenyan server or data centre. Map hosting, subprocessors, analytics and research access. |
| DPA | ss18–19; Registration Regulations, 2021 | Determine controller/processor roles and whether each entity must be registered. ODPC guidance identifies provision of financial services as a mandatory-registration category even where the ordinary size thresholds would otherwise matter; confirm the precise entity/activity. |
| General Regulations, 2021 | rr19–23, 49–53 | Data-sharing agreements/process; automated decision governance; data-protection policy; listed DPIA triggers; DPIA conduct, prior consultation and report consideration/audit. |
| Complaints Handling and Enforcement Regulations, 2021 | Whole instrument | Complaints, investigation and enforcement are part of operational risk: retain records, assign complaint owners, respond through the statutory process and remediate errors. |

### Section 35 exceptions require careful application

Section 35's restriction has exceptions where the decision is necessary to enter into or perform a contract, authorized by law with suitable safeguards, or based on the data subject's consent. Do not assume that a generic contract clause makes every model or policy necessary, or that bundled consent is freely chosen, sufficiently specific or informed. Even where an exception applies, the wider DPA principles, General Regulations, notice, security and rights remain relevant. The actual role of a human must be real enough to consider relevant information; a rubber stamp should not be described as meaningful review.

## 4. DPIA and innovation-specific requirements

General Regulations r49 expressly lists as high-risk processing, among other cases:

- automated decision-making with legal or similar significant effect, including profiling or algorithmic means, or sensitive data used to determine service access;
- large-scale processing for an incompatible new purpose;
- biometric/genetic data; data concerning children or vulnerable groups;
- linking separate datasets from different sources and different purposes;
- large-scale personal-data processing;
- innovative technological or organizational solutions; and
- processing that prevents a data subject exercising a right.

This makes a proposed sequential collection policy a strong candidate for a DPIA analysis before any pilot or production processing. Do not reduce the assessment to an algorithm card. Map purposes, features, sources, roles, decisions, recipients, observation/action logs, retention, rights, risks, mitigations and residual risk. Section 31's prior consultation applies when the assessment indicates high risk; confirm the required process and timing against the statute, General Regulations and current ODPC guidance.

The ODPC DPIA Guidance Note treats automated decision-making with legal/similar significant effects and profiling/economic-situation predictions as high-risk indicators. Guidance informs the assessment; it is not a substitute for the Act or Regulations.

## 5. Credit-specific rules that materially affect the examples

### Banking (Credit Reference Bureau) Regulations, 2020

- Rule 26 requires advance notice before furnishing negative credit information (the rule provides a default 30 days and allows a shorter period in the customer contract), and controls accuracy/correction of disputed information.
- Rules 37 and related dispute provisions establish report access, dispute investigation and correction routes.
- Rule 39 provides for credit scores; rule 40 says a score shall not be used solely to deny a loan, facility or financial service. The institution considers it as one factor, gives written appraisal/reasons, and a score-only denial can attract a penalty.
- Rule 63(1)(c)–(2) requires an adverse-action notice when a decision is adverse in whole or part because of bureau information, at the time the decision is communicated, including the bureau's identity and the customer's rights to obtain and dispute the report. Keep this distinct from r26's notice before negative information is furnished;
- For a model using bureau data, ensure the customer can challenge wrong source data and that a corrected bureau item does not continue silently to drive the policy. Do not treat a bureau score explanation as a complete explanation of the lender's own model.

### CBK Digital Credit Providers Regulations, 2022

Regulation 2 expressly excludes institutions licensed under the Banking Act, Microfinance Act and SACCO Societies Act, among other cases. Classify the lender and its activity before applying this instrument; its collection provisions do not automatically govern every bank or other regulated lender. For an in-scope DCP:

- r20 prohibits specified abusive collection conduct, including threats, shaming, harvesting contacts for collection, unauthorized contact with third parties and harassment;
- r13 requires confidentiality policies and limits sharing of customer information except with consent or as required/permitted by written law;
- rr14–15 govern credit-information exchange/use/security; r14(5) requires at least 30 days' pre-submission notice before negative bureau reporting, or a shorter contractual period no shorter than seven days, and r14(6) requires notice within 30 days after submission;
- r18 requires reasonable steps to assess ability to repay before advancing credit;
- rr22–26 cover complaint redress, secure/reliable information systems, fair/clear information, and limiting access/collection to information reasonably required for credit appraisal, approval, disbursement and collection.

The examples should identify the institution class first. Do not apply a DCP-only rule to all banks or a CRB rule to a bank-wide ALM decision.

### Consumer protection and administrative fairness

The Consumer Protection Act, 2012 is relevant to consumer transactions within its scope; it should not be casually applied to every business/MSME facility as though a company borrower were always an individual consumer. Article 47 and the Fair Administrative Action Act are important where a public authority or administrative function makes the decision. Their direct application to a private lender's internal credit decision requires context-specific analysis.

## 6. Operational data-governance requirements for sequential learning

Each decision episode should be reconstructible from a governed event record:

1. controller/processor and any joint-controller roles, including the lender, platform, collection vendor, bureau and hosting provider;
2. purpose, lawful basis, data categories, sources, notice and consent evidence where relevant;
3. point-in-time data snapshot, provenance, freshness, quality flags and corrections known at that moment;
4. eligibility/action-set gate and the policy/model version;
5. actual assigned action and its conditional probability after the operational and legal gates;
6. offer, delivery, acceptance, human review, override and reason;
7. outcome window, settlement/cure/re-default/recovery, costs, censoring and customer complaint/impact;
8. retention, correction/deletion restrictions, cross-border access and downstream model-update status.

Adaptive policies should not infer sensitive or intimate variables just because they improve prediction. Every new source, changed purpose, large-scale data linkage, new model or new automated effect should trigger a documented change assessment and DPIA refresh decision. An opt-out or objection cannot be coded as a negative reward. Statutory rights and prohibited actions must be enforced before action selection, not represented only as penalties in the objective.

For RL evaluation, propensity logging and policy evaluation are methodological requirements, not themselves legal authority. A complete mathematical estimator cannot cure an invalid purpose, unfair experiment, unsupported action or uninformative notice.

## 7. Treasury / ALM / FTP perimeter

Map Treasury data by granularity:

- **Potentially non-personal:** market curves, institution-wide funding totals, aggregate product cash flows or bank-level risk metrics that do not identify people.
- **Potentially personal:** named/identifiable deposit account behavior, borrower repayment histories, sole-proprietor cash flows or individually inferred rate sensitivity.
- **Separate confidential information:** customer/account-level bank information may be restricted by banking confidentiality and institutional controls even where a processing table has been aggregated or pseudonymized.

The ordinary bank-level recommendation to choose funding tenor or a hedge is not automatically an individual decision under s35. If the same system sets an identifiable customer's rate, deposit offer or credit access, assess that customer-level decision separately. Treasury needs an institution-specific inventory of CBK prudential requirements, internal ALCO policy, model-risk obligations, outsourced-service controls and authority limits. The article should keep those applicable rules as hard external constraints and send the actual rule map to the relevant institution's legal/risk team.

The supplied ALM course and Treasury/RL screenshots are technical prompts, not legal authorities. Their proposed action/reward setup is mapped in the [Treasury and credit-loss screenshot review](<../../../regtech-kesonia-treasury/docs/methods/SCREENSHOT_ENRICHMENT_ALM_CREDIT_LOSS_AND_WORKBENCH_2026-10-04.md>); Article 2 should apply the data-granularity distinction above to each input and keep law, approved prudential limits and delegated authority outside the learned reward.

## 8. AI-specific law and policy status

Kenya's AI Strategy 2025–2030 is a government policy strategy, not itself an AI statute. The Artificial Intelligence Bill, 2026 (Senate Bills No. 4 of 2026) is a legislative watch item. The parliamentary record verified for this review lists the Bill in Senate business; it is not to be described as enacted or as an operative AI Act. Recheck its status, amendments and any assent/gazettement immediately before publication. Until then, the binding baseline for personal-data uses remains the Constitution, DPA and applicable subsidiary/sector legislation.

Do not import EU AI Act duties as Kenyan law. They may be discussed as a clearly labelled comparison only.

## 9. Recommended legal gate sequence for the two articles

1. **Classify:** natural-person data, entity data, bank-confidential data; decision audience and material effects.
2. **Map:** controller, processor, joint participation, vendors, transfers and access.
3. **Specify purpose and basis:** test compatibility, minimization and the potential operation of s37 commercial use.
4. **Assess risk:** s31 / r49 DPIA before high-risk processing; consultation if statutory residual-high-risk condition is met.
5. **Design notice and rights:** accurate collection notice, automated-decision disclosure, meaningful reasons, correction, objection, complaint and human intervention.
6. **Constrain policy:** allowed-action list and independent limits; do not optimize legal rights as a soft objective.
7. **Prove operations:** security, processor terms, registration, retention, breach handling, versioned audit and corrective feedback.
8. **Authorize use:** legal, DPO, compliance, risk, model validation, product and accountable business-owner review; no inference that this outline is approval.

## 10. Primary source register

- Constitution of Kenya, 2010 (official government page): https://www.mod.go.ke/the-constitution-of-kenya-2010-online/
- Data Protection Act, 2019 (Kenya Law, consolidated source): https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402022-12-31/source
- Data Protection (General) Regulations, 2021, L.N. 263/2021 (Kenya Law): https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng%402022-12-31/source
- Data Protection (Registration of Data Controllers and Data Processors) Regulations, 2021: https://new.kenyalaw.org/akn/ke/act/ln/2021/265/eng%402022-01-14/source
- ODPC legal framework page listing the Act and 2021 Regulations: https://www.odpc.go.ke/data-protection-laws-kenya/
- ODPC DPIA Guidance Note: https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Note-on-Data-Protection-Impact-Assessment-1.pdf
- ODPC digital credit provider guidance: https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Note-for-Digital-Credit-Providers.pdf
- CBK (Digital Credit Providers) Regulations, 2022, L.N. 46/2022: https://www.centralbank.go.ke/wp-content/uploads/2022/03/L-.N.-No.-46-Central-Bank-of-Kenya-Digital-Credit-Providers-Regulations-2022.pdf
- Banking (Credit Reference Bureau) Regulations, 2020, L.N. 55/2020: https://www.centralbank.go.ke/wp-content/uploads/2026/03/The-Banking-Credit-Reference-Bureau-Regulations.pdf
- Consumer Protection Act, 2012: https://new.kenyalaw.org/akn/ke/act/2012/46/eng%402022-12-31/publication
- Senate AI Bill record: https://www.parliament.go.ke/node/25555
- Kenya AI Strategy: https://www.ict.go.ke/node/641

## Editorial application

- Put a short legal-perimeter box in Article 1 and refer readers to this fuller research map.
- Article 1 should foreground DPA s35/r22, s31/r49, s25–30, s36–37, credit bureau accuracy/score rules and DCP-specific limitations.
- Article 2 should foreground Article 31/DPA distinctions, granular personal-data boundary, purpose/minimization, DPIA where account-level behavioral processing is high-risk, and institution-specific prudential gates.
- In both, say clearly that applicable-law conclusions must be refreshed and reviewed by Kenyan counsel before operational deployment.
