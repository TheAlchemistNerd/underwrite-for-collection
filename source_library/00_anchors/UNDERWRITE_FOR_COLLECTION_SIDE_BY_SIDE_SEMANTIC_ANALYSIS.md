I completed a side-by-side semantic reading of all 3,473 lines of the rough document and all 248 lines of Underwrite for Collection. No files were modified.
The two documents are complementary, but they perform different jobs:
- Underwrite for Collection is the disciplined industry thesis.
- In the Spirit of Underwriting to Collect is a large research notebook exploring how that thesis could be tested through prospective experimentation, behavioural modelling and institution-contained data infrastructure.
The rough document should not replace or be merged wholesale into the article. It should become the source reservoir for a separate methodological paper and controlled pilot protocol.
1. Corpus assessment
Document	Approximate size	Function	Current condition
[Underwrite for Collection](C:/Users/Nevo/Downloads/insuretech & embedded finance/publications/linkedin/UNDERWRITE_FOR_COLLECTION.md)	3,905 words	Practitioner thesis	Coherent, sourced and publication-ready
[In the Spirit of Underwriting to Collect](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/In the spirit of underwriting to collect.md)	19,403 words	Exploratory research notebook	Conceptually rich but structurally and evidentially rough


The rough document contains:
- 3,473 lines.
- Approximately 150 URL occurrences.
- 64 distinct URLs.
- No dependable Markdown heading hierarchy.
- Fifteen major conversational turns after the opening question.
- Repeated source previews, AI disclaimers, image remnants and duplicated prompts.
- A mixture of valid hypotheses, implementation ideas, provisional examples and unsupported legal or regulatory claims.
Its source base is not yet academically balanced. Among the 64 distinct URLs are:
- Six Facebook links.
- Five LinkedIn posts or articles.
- Five PEMiG pages.
- Two Medium articles.
- Only a small number of direct CBK and Kenya Law sources.
- Several foreign sandbox rules incorrectly used to support claims about Kenya.
That does not make the notebook worthless. It means it should be treated as hypothesis-generating material, not as verified evidence.
2. The central relationship between the documents
The anchor article advances this proposition:
A loan is successfully underwritten only when its structure, monitoring and intervention design support sustainable collection after disbursement.

The rough document asks the natural next question:
How can a lender establish, through prospective and ethically controlled evidence, which product structures, monitoring signals and interventions actually improve sustainable collection?

That is the main complement.
The article already says lenders should use randomised pilots or credible quasi-experimental designs, but it stops at the principle. The rough document begins constructing the missing experimental programme:
- Which decisions should be tested?
- Which borrowers should enter the experiment?
- What is the control?
- What can be randomised lawfully?
- How should treatment effects be estimated?
- How can trials adapt without exposing customers to a deteriorating arm?
- How should customer welfare constrain optimisation?
- How can the model operate when bank data cannot leave the institution?
- How do cure, re-default, recovery, ECL, capital and funding enter the outcome definition?
- How should a challenger graduate into production?
The rough document therefore does not merely add more modelling. It proposes an evidence-production mechanism for the philosophy articulated in the article.
3. Line-by-line semantic map
Rough-document lines	Principal idea	Contribution	Required treatment
1–72	RCTs and supervised testing	Introduces prospective experimentation	Retain the question; verify the regulatory route
73–229	Cash-flow and psychometric trial arms	Identifies alternative evidence and repayment design	Separate scoring, product and intervention treatments
230–377	Causal credit scoring	Introduces counterfactual reasoning, ATE and CATE	Retain causality; remove claims that a predictive model is inherently causal
378–511	PEMiG and retrospective assessment	Provides a market-comparison case	Reframe cautiously; vendor pages cannot prove regulatory status
512–845	Critique of retrospective data and KESONIA	Identifies reject inference, structural change and policy dependence	Strong material after correcting the meaning of KESONIA and K_RBCP
846–1077	HLR, Cox, P-splines, horseshoe and neural residualisation	Supplies candidate statistical architecture	Separate model purposes and correct several statistical descriptions
1078–1218	Contextual bandits and POMDPs	Adds adaptive intervention learning	Retain as later-stage challengers, not initial production architecture
1219–1320	Intensity and Hawkes models	Explores high-frequency event timing	Optional challenger; a POMDP does not inherently require a point process
1321–1480	Anatomy of the pricing premium	Connects risk evidence with Kenyan pricing	Correct to the official RBCPM definition and prevent double counting
1481–1830	ALM, FTP and high-frequency collections	Connects realised cash timing with funding economics	Retain, but remove unsupported claims about duration, HQLA and regulatory acceptance
1831–2177	Redlining, shared value and borrower states	Adds conduct risk and supportive intervention	One of the strongest narrative extensions
2178–2452	Forbearance, fairness and section 35	Creates operational guardrails	Retain principles; remove invented mandatory thresholds and legal absolutes
2453–2775	Champion-challenger, maker-checker and validation	Adds production governance	Strong extension after converting examples into governed policy choices
2776–3078	Active versus shadow trials, duration and data sandbox	Addresses evidence maturity and exposure limits	Retain the staged design; verify all timelines and allocation rules
3079–3245	Model-to-data deployment	Solves the institutional-data problem	Highly valuable; replace absolute privacy claims with a layered secure architecture
3246–3473	Cure, social research and epidemiological analogies	Adds multidisciplinary lifecycle language	Retain carefully; analogies should illuminate rather than stigmatise


4. What the rough document contributes to the anchor article
4.1 A prospective evidence strategy
The anchor correctly observes that treatment selection contaminates observational collection outcomes. The rough document advances this by proposing actual experimentation.
This is supported by credible precedent. Randomised credit experiments have tested repayment flexibility, payment timing and performance-contingent contracts. A Kenyan experiment examined performance-contingent repayment for micro-distributors, measuring business outcomes, welfare and repayment—not default alone. Similar research in Bangladesh found that repayment flexibility could improve business outcomes while reducing default for some borrowers. J-PAL Kenya study, J-PAL repayment-flexibility study.
The strongest addition is therefore not “use a complex causal AI engine.” It is:
Treat product structure, servicing and supportive collection interventions as testable causes of sustainable repayment.

4.2 Rejected applicants and missing counterfactuals
The rough document correctly identifies a limitation in retrospective loan-book analysis: rejected applicants usually have no performance outcome in the lender’s portfolio.
A model trained only on approved borrowers learns within the historical approval policy. This creates:
- Selective labels.
- Limited support.
- Reject-inference uncertainty.
- Historical policy dependence.
- Weak evidence for underserved segments.
The anchor discusses point-in-time correctness but does not yet address selection created by the earlier underwriting policy. The new paper should distinguish:
- Data leakage: using future information.
- Selection bias: observing outcomes only for approved borrowers.
- Confounding: treatment assignment related to risk.
- Policy feedback: decisions change the future data-generating process.
- Concept drift: economic or behavioural relationships change over time.
- Interference: one borrower’s intervention affects another borrower.
This is a material theoretical extension.
4.3 The difference between prediction and intervention
The anchor separates evidence, inference, policy and action. The rough document adds a further separation that will be essential:
1. Prognostic model: estimates what is likely to happen without a specified new intervention.
2. Causal treatment model: estimates how a permissible intervention changes an outcome.
3. Decision policy: selects an eligible intervention subject to constraints.
4. Operational workflow: executes, records and reviews the action.
The HLR is principally prognostic. Randomisation can support causal estimation. A contextual bandit or POMDP may later optimise a policy. None of these is interchangeable with the others.
4.4 Durable cure as an experimental endpoint
The anchor defines durable cure but does not develop it as the centre of an intervention experiment. The rough paper does.
A strong trial would measure:
- Entry into arrears.
- Time to first cure.
- Durability of cure.
- Re-default after cure.
- Modification and post-modification performance.
- Business survival or continued productive activity.
- Net present value of recovery.
- Customer hardship and complaints.
- Working-capital retention.
- Contact burden.
- Treatment cost.
- Eventual write-off.
- ECL and capital consequences.
This is stronger than using a short-term promise-to-pay or immediate cash receipt as the reward.
4.5 Model-to-data architecture
The rough document’s most practically valuable discovery is that the methodology should move to the institution’s data rather than assuming that a bank will export customer-level records.
The statement that obtaining anonymised data is “impossible” is too absolute. Lawful research access can be possible under appropriate governance. Operationally, however, planning on the assumption that a bank will hand a founder an account-level dataset is unrealistic.
A more viable evidence pathway is:
Public and synthetic research
             ↓
Bank-controlled secure data environment
             ↓
Retrospective point-in-time validation
             ↓
Prospective shadow deployment
             ↓
Restricted live intervention trial
             ↓
Independent validation and controlled scaling
The bank-controlled environment could be:
- An on-premises research enclave.
- A bank-controlled private-cloud workspace.
- A confidential data clean room.
- A locked virtual desktop with no raw-data export.
- A trusted execution environment.
- A federated analytical arrangement where multiple institutions participate.
- A secure container deployed into each participating institution.
Permitted outputs would be restricted to:
- Aggregated statistics.
- Validated model artefacts.
- Disclosure-controlled tables.
- Approved coefficients or posterior summaries.
- Reproducibility manifests.
- Independent-validation reports.
- Privacy-reviewed synthetic extracts.
Federated learning alone does not eliminate privacy risk. Model updates can leak information. Secure aggregation, clipping, minimum cohort sizes, output controls and possibly differential privacy would still be required. NIST’s federated-learning guidance makes this distinction clearly.
For a single-bank pilot, ordinary federated learning may add unnecessary complexity. A bank-controlled secure research enclave is the simpler starting point. Federated infrastructure becomes relevant when multiple institutions need to learn jointly without pooling raw data.
5. What the anchor article corrects in the rough document
The anchor provides discipline that the exploratory paper frequently loses.
5.1 KESONIA is not the experimental control
The rough document repeatedly describes KESONIA as a “fixed” or “static” control baseline. That is inaccurate.
KESONIA is a transaction-based overnight benchmark published every business day. Under the revised RBCPM:
Total lending rate = KESONIA + K
and:
Total cost of credit = KESONIA + K + fees and charges
The premium includes lending-related costs, shareholder return and the borrower’s risk profile. CBK’s KESONIA overview, CBK April 2026 MPC report.
KESONIA is therefore:
- A common market reference component.
- Time-varying rather than static.
- Not a treatment arm.
- Not itself the control group.
- Not the entirety of the lending price.
- Not the causal effect being estimated.
A trial can hold the contractual benchmark convention consistent across contemporaneous arms while stratifying or blocking by calendar time. The control is the bank’s current approved policy, not KESONIA itself.
5.2 The RCT should not try to “discover K” directly
The rough document frequently equates treatment effects with the customer premium.
An RCT might estimate whether:
- Payment-date alignment improves durable cure.
- Flexible repayments reduce default.
- A particular reminder improves settlement.
- A temporary draw freeze prevents overextension.
- A hardship offer improves net recovery.
- A human contact is more effective than a digital notification.
Those estimates may influence expected loss, operating cost, product design and eventually an approved pricing methodology. They are not themselves K_RBCP.
The pricing layer must preserve:
- Benchmark rate.
- Funding and liquidity cost.
- Expected loss.
- Unexpected-loss or capital allocation.
- Operating and servicing cost.
- Customer-specific risk.
- Shareholder return.
- Fees and taxes.
- Contractual and regulatory constraints.
5.3 Neural residualisation is not a confounder-removal machine
The rough file says neural residualisation “strips out confounders,” macroeconomic shocks and even observation effects. That is too strong.
Our established treatment is more defensible:
- Create explicit variables with clear definitions and ownership.
- Learn neural representations from permitted sequences.
- Generate those representations out of fold.
- Regress or project them against the explicit feature block.
- Pass residual representations into the HLR.
- Apply regularised-horseshoe shrinkage.
- Test whether the residual neural block adds stable out-of-time value.
This reduces duplication between explicit and learned features. It does not establish causal identification or remove unobserved confounding.
5.4 Horseshoe priors do not set coefficients exactly to zero
The rough paper repeatedly states that the horseshoe “instantly” or “absolutely” zeroes irrelevant variables. Continuous horseshoe priors strongly shrink weak coefficients but generally do not produce exact zeros.
The correct role is:
- Global-local regularisation.
- Strong concentration near zero.
- Heavy tails for signals supported by evidence.
- Control of a potentially wide residual-embedding or interaction block.
- Posterior inclusion interpretation only with an explicit decision rule.
5.5 Pólya–Gamma augmentation is an inference strategy
Pólya–Gamma augmentation does not make the model causal and does not perform online learning by itself. It makes Gaussian parameter blocks of a Bayesian logistic model conditionally conjugate.
It belongs in the offline inference architecture:
Hierarchical logistic model
        ↓
Pólya–Gamma augmentation
        ↓
Blocked posterior computation
        ↓
Validated and versioned posterior artefact
        ↓
Low-latency production scoring
Production requests should not run full MCMC.
5.6 Cox models do not automatically supply a POMDP transition matrix
A Cox model estimates a hazard under its assumptions. A POMDP needs state-transition and observation models. They can be connected, but one is not automatically the other.
For the proposed lifecycle, a better sequence is:
- Fixed-horizon HLR for governed PD.
- Competing-risk or multi-state survival model for delinquency, cure, prepayment, modification and default.
- Observation model for irregular transaction and repayment evidence.
- Decision policy operating over the estimated state distribution.
- POMDP only after simpler rule-based and multi-state policies have been benchmarked.
A Hawkes process may be tested for clustered payment events, but it should remain a challenger. Transaction clustering alone does not prove repayment intent or impending default.
5.7 Intent should not be inferred from behavioural traces
The rough document divides borrowers into “stressed” and “strategic defaulters.” That is operationally dangerous.
High till activity combined with missed repayments does not prove bad faith. There may be:
- Disputed debits.
- Working-capital commitments.
- Another lender’s sweep.
- Settlement delays.
- Fraud or account compromise.
- Restricted funds.
- Household emergencies.
- Incorrect identity resolution.
- Platform outages.
- Contract misunderstandings.
The states should be renamed around observable operational conditions:
- Current and stable.
- Emerging liquidity stress.
- Payment friction or engagement unavailable.
- Restructuring assessment.
- Delinquent with unresolved cause.
- Intensive review.
- Insolvency or recovery.
- Cured.
- Closed.
Intentional avoidance can be investigated by authorised humans; it should not be asserted by a latent-state model.
6. Experimental design that emerges from both documents
The best design is not one three-arm experiment in which scoring method, interest rate, repayment frequency and collection action all change together. That would make the causal mechanism impossible to identify.
The research programme should separate four experiments.
Experiment A: Evidence and prediction
Compare:
1. Existing approved scorecard.
2. Cash-flow variables added.
3. Psychometric variables added.
4. Explicit behavioural variables plus HLR.
5. Explicit variables plus residualised neural representation.
This phase is primarily predictive and can begin in shadow mode.
Psychometrics should be a challenger, not an assumed measure of integrity or character. Validation should examine reliability, gaming, language, cultural transportability, accessibility and disparate impact.
Experiment B: Product and repayment structure
Randomise permissible product structures within pre-approved equivalence boundaries, such as:
- Payment dates aligned to cash receipts.
- Weekly versus monthly schedules.
- A limited payment-deferral option.
- Fixed instalment versus bounded performance-contingent repayment.
- Different grace-period designs.
- Voluntary rather than automatic revenue-linked repayment.
The Kenyan J-PAL experiment on performance-contingent repayment provides a directly relevant precedent.
Experiment C: Supportive interventions
Among eligible customers, test:
- Reminder timing.
- Communication channel.
- Human versus digital contact.
- Payment-date adjustment offers.
- Hardship assessment invitations.
- Temporary draw restriction.
- Restructuring review.
- Inventory-cycle-aligned repayment.
- Contact suspension during documented vulnerability.
A micro-randomised trial may be suitable for low-risk, repeatable interventions. Material adverse actions should not be experimentally automated.
Experiment D: Adaptive policy
Only after the first experiments establish safety and initial treatment effects should a contextual bandit allocate among permissible supportive actions.
The trial must retain:
- Minimum exploration probabilities.
- Logged assignment propensities.
- Predefined safety constraints.
- Off-policy evaluation.
- Time-uniform or sequential inference.
- Treatment-effect estimation robust to adaptive allocation.
- Independent monitoring.
- Rollback and stop rules.
Adaptive bandit allocation changes the data distribution and complicates conventional inference; it does not automatically improve causal validity. Appropriate methods can provide inference under adaptive experimentation, but the design and propensity history must be preserved. Anytime-valid off-policy inference.
7. Regulatory and legal corrections
7.1 Do not assume a formal CBK sandbox rulebook
The rough document repeatedly asserts:
- A standard CBK sandbox application.
- A strict twelve-month CBK limit.
- An automatic route to a second twelve months.
- Required filing thirty days before expiry.
- Specific portfolio and account caps.
- Required monthly reports.
- Mandatory joint applications.
The cited support comes substantially from the UAE, Malaysia, Uganda and Kenyan legal commentary—not a published CBK sandbox policy.
I found an official and operational Kenyan capital-markets sandbox administered by the Capital Markets Authority. CMA sandbox. CBK innovation surveys discuss institution-level innovation sandboxes and refer to prospective sandbox activity under CBK guidance, but this does not establish the detailed public application regime asserted in the rough document. CBK Banking Sector Innovation Survey 2024.
The safe terminology is therefore:
A bank-controlled research sandbox followed by a regulator-engaged controlled pilot under a pathway agreed in writing with the relevant supervisor.

The architecture may ultimately involve:
- CBK for banking, credit or payment activity.
- CMA where capital-market products or securitisation experiments are involved.
- IRA where embedded insurance is tested.
- ODPC for high-risk personal-data processing and DPIA questions.
- Competition or consumer-protection authorities where relevant.
The exact pathway must be confirmed rather than assumed.
7.2 Section 35 does not make consent universally mandatory
Section 35 protects people from decisions based solely on automated processing that produce legal or similarly significant effects. It contains exceptions for contractual necessity, legal authorisation and consent, with safeguards and reconsideration rights. Kenya Data Protection Act.
The General Regulations require transparency, meaningful information, error controls, appropriate statistical procedures, measures against discriminatory effects and access to human intervention. High-risk profiling, dataset linkage and innovative technology may also require a DPIA. Data Protection (General) Regulations.
The correct approach is:
- Determine the lawful basis for each processing purpose.
- Do not default automatically to consent.
- Use consent only where it can genuinely be freely given and withdrawn.
- Distinguish research, underwriting, servicing and marketing purposes.
- Establish whether a decision is solely automated.
- Provide meaningful human review.
- Conduct a DPIA.
- Minimise data and retention.
- Provide notice, challenge and correction routes.
A credit applicant may not have a genuinely free choice if refusing consent automatically prevents access to an otherwise available product. That requires particular care.
7.3 The 80-percent rule is not Kenyan law
The rough file repeatedly presents the US-style four-fifths rule as mandatory Kenyan compliance. It is not a universal Kenyan legal threshold and is not sufficient as a fairness framework.
Fairness review should combine:
- Approval and pricing distributions.
- False-positive and false-negative rates.
- Calibration within relevant groups.
- Equal opportunity where appropriate.
- Affordability and over-indebtedness outcomes.
- Contact burden.
- Cure and re-default.
- Customer complaints.
- Product benefit and harm.
- Intersectional subgroup analysis.
- Stability across time and geography.
- Review of proxy variables.
No single fairness metric will be appropriate for every decision.
8. The correct sandbox and data-access strategy
Your example is directionally right: if external customer-level data cannot be obtained, the programme should not wait indefinitely for a conventional research extract.
The preferred architecture is:
Phase 0: Public and synthetic foundation
- Use CBK, KBA, KNBS and other official aggregate data.
- Build a synthetic portfolio with realistic censoring, selection, interventions and macroeconomic regimes.
- Validate software, estimands, power calculations and reporting.
- Do not claim synthetic results represent Kenyan borrowers.
Phase 1: Bank-controlled retrospective enclave
- Deploy code into the bank’s environment.
- Reconstruct point-in-time data.
- Perform label, leakage and selective-approval audits.
- Benchmark simple models.
- Export only approved aggregate outputs.
- Use robustly informative rather than artificially “tight” priors.
- Test prior-data conflict before borrowing historical information.
Phase 2: Prospective shadow mode
- Score current cases without changing decisions.
- Validate latency, lineage and calibration.
- Observe policy disagreement.
- Test reason codes and human workflows.
- Measure how often data are missing, late or corrected.
- Do not describe shadow predictions as causal evidence.
Phase 3: Restricted low-risk field experiment
- Randomise only approved, ethically acceptable interventions.
- Apply eligibility and exclusion criteria.
- Keep adverse decisions under human authority.
- Use exposure, customer and financial stop rules.
- Pre-register the protocol and statistical analysis plan.
- Measure borrower welfare and conduct outcomes beside cash.
Phase 4: Adaptive trial
- Introduce bandit allocation only among interventions already shown to be safe.
- Preserve minimum exploration and assignment probabilities.
- Use independent monitoring.
- Prevent protected or proxy variables from determining harmful treatment intensity.
- Retain a stable benchmark cohort.
Phase 5: Scale and lifecycle validation
- Require mature outcomes.
- Examine durable cure and re-default.
- Reconcile realised cash to ECL, capital and funding.
- Validate across new vintages, sectors and economic conditions.
- Scale through formal model and policy governance.
9. ALM, FTP and accounting treatment
The rough document makes an important connection between collection timing and funding economics, but overstates its consequences.
Daily repayments may shorten realised weighted-average life only if:
- They settle reliably.
- Reversals are controlled.
- They remain available to the bank.
- The behaviour persists under stress.
- Operational costs do not offset the benefit.
- Prepayment and delinquency models are validated.
- The effect is recognised under approved FTP policy.
Daily collections do not automatically become HQLA, eliminate liquidity risk or justify a lower transfer price.
The trial may generate evidence for:
- Behavioural cash-flow curves.
- Collection and settlement lags.
- Prepayment.
- Drawdown behaviour.
- Cure and recovery timing.
- Liquidity-gap modelling.
- Matched-maturity FTP.
- IRRBB stress.
- Product profitability.
These should be secondary financial outcomes, not manipulated trial targets.
Similarly, a lower modelled PD does not automatically release accounting provisions or regulatory capital. IFRS 9 ECL depends on approved staging, forward-looking scenarios, cash shortfalls and governance. Regulatory capital follows its own framework. Only validated changes in expected and realised performance should reach finance and capital processes.
10. Recommended new publication architecture
The material now supports four related but distinct outputs.
A. Existing practitioner article
Underwrite for Collection: Rebuilding Credit Architecture Around Sustainable Cash Recovery
Keep largely unchanged. It is the public, accessible thesis.
B. Methodological paper
From Underwriting to Evidence: Prospective Lifecycle Credit Experiments for MSME Lending
Its contribution would be:
- Separating prediction, causal estimation and intervention policy.
- Using hierarchical models for sparse MSME segments.
- Estimating durable cure and net recovery.
- Addressing selective labels and reject inference.
- Comparing fixed and adaptive experiments.
- Protecting borrowers through constrained actions.
- Integrating product, conduct and financial outcomes.
C. Institutional implementation protocol
Bank-Controlled Research Sandbox Protocol for Lifecycle Credit
This would specify:
- Model-to-data architecture.
- Data enclave controls.
- Point-in-time reconstruction.
- Shadow deployment.
- Trial governance.
- DPIA and human review.
- Champion-challenger.
- Maker-checker.
- Safety and rollback.
- Disclosure-controlled research outputs.
D. KBA empirical research stream
From KESONIA to Sustainable Collection
This remains the Kenya-specific pricing and policy paper. It can use public macroeconomic and sector data initially, then incorporate institution-contained experimental results if a partner becomes available.
Final judgement
The rough document is not a competing version of Underwrite for Collection. It is the beginning of its research and experimentation programme.
Its strongest discoveries are:
- Retrospective loan books cannot answer every causal question.
- Rejected applicants create a selective-label problem.
- Product and collection design can be experimentally evaluated.
- Cure and re-default are better endpoints than immediate payment alone.
- Models should move to protected bank data.
- Shadow testing and active experimentation serve different purposes.
- Adaptive learning requires stronger, not weaker, governance.
- Customer welfare belongs inside the objective function.
- Collection timing has consequences for ECL, capital, ALM and FTP.
- Lifecycle outcomes should determine whether a model graduates.
Its main weaknesses are:
- Treating a predictive stack as inherently causal.
- Conflating KESONIA, K_RBCP, expected loss and treatment effects.
- Assuming a documented CBK sandbox process that has not been established.
- Importing foreign sandbox timelines into Kenya.
- Presenting illustrative limits as regulations.
- Treating consent as the only lawful basis.
- Treating the 80-percent rule as Kenyan law.
- Treating SHAP as causal explanation.
- Treating neural residualisation as removal of confounding.
- Treating federated parameter updates as automatically anonymous.
- Inferring borrower intent from transaction traces.
- Introducing the full HLR–Cox–Hawkes–bandit–POMDP stack before simpler models have earned replacement.
The clean synthesis is:
Underwrite for Collection defines the institutional objective. The new methodological work should define how a lender can learn, under controlled and ethically governed conditions, which products and interventions produce sustainable repayment, durable cure, fair customer outcomes and better realised cash.

The rough file should be preserved unchanged as the discovery record. A new manuscript should be built from its validated concepts rather than attempting to edit the 19,000-word conversation into publication form.
