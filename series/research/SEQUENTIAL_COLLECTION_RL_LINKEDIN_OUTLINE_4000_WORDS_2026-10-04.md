# From one-step bandits to sequential collection control

## LinkedIn article outline — planned length: 4,000 words

**Working title:** *From a One-Step Bandit to Sequential Control: Can We Learn Which Collection Action Helps This Borrower Next?*

**Status:** Detailed editorial and research outline. This is not a completed article, a deployed controller, or legal advice. It extends the one-step contextual-bandit discussion proposed in Part 3 of *Underwrite for Collection*.

**Audience:** Credit-risk, collections, data-science, compliance, product and model-risk teams working with individual and small-business lending.

**Thesis:** A contextual bandit chooses one action for a defined decision episode. Sequential reinforcement learning (RL) becomes relevant only when actions alter later borrower states and future options. In collections, any learned policy must operate inside a human-approved, legally reviewed action set; rights, affordability protections and required service cannot be converted into costs that a higher expected recovery may outweigh.

**Anchor example:** A fictional borrower with irregular business receipts misses a scheduled payment. The lender can select among permitted, proportionate actions over several review dates: a respectful reminder, a cash-flow conversation, a permitted payment-alignment offer, or specialist review. The case follows the account through accepted contact, actual receipt, cure, re-default and customer burden. All numbers are labelled illustrative unless they are later replaced by a documented, validated case.

## Word plan

| Section | Words |
|---|---:|
| 1. Opening: a reminder is not the whole policy | 150 |
| 2. What the one-step bandit can and cannot answer | 350 |
| 3. When the problem becomes a sequential control problem | 450 |
| 4. State, action, observation and reward design | 350 |
| 5. Method ladder: control first, RL only when justified | 500 |
| 6. Kenyan legal and rights architecture | 600 |
| 7. Reproducible worked example | 500 |
| 8. Experiment design and sequential policy evaluation | 450 |
| 9. Operational governance, monitoring and failure modes | 350 |
| 10. A staged implementation blueprint | 180 |
| 11. Conclusion | 120 |
| **Total** | **4,000** |

## Detailed outline

### 1. Opening: a reminder is not the whole policy — 150 words

- Start with the missed-payment event and the familiar choice to send a reminder.
- Ask what should happen after the borrower replies that a customer has paid late and the business expects cash next week.
- Contrast a single action's average effect with a sequence whose earlier action changes the next state: a call may surface a remittance date; an agreed payment plan may affect next month's cash and willingness to engage.
- State the boundary: the objective is sustainable, lawful resolution and accurate learning, not maximum short-term cash at any cost.

### 2. What the one-step bandit can and cannot answer — 350 words

- Recap the Part 3 contextual bandit: at one decision point, use context \(X_t\), choose an eligible action \(A_t\), and evaluate a defined outcome \(Y_t\).
- Define the logging propensity \(e_t(a\mid X_t,H_{t-1})\): the probability that the actual assignment process selected that action after eligibility, capacity and randomization gates.
- Explain why this helps when comparing one permitted reminder or contact timing with the standard service.
- Distinguish a bandit from an ordinary predictive risk score. The score predicts an outcome under a data-generating policy; the bandit estimates or learns action value under an assignment process.
- Give the transition test: if the chosen action changes later state or later feasible actions, a one-step value is incomplete. If actions do not affect later states within the chosen episode, a contextual bandit may remain the simpler right model.
- Avoid implying that any repeated monthly score is RL or that one delayed outcome alone makes an episode sequential.
- Tie back to the existing review: Part 3 proposes a stable randomized pilot before an adaptive challenger; the current project has not implemented either.

### 3. When the problem becomes a sequential control problem — 450 words

- Introduce the Markov decision process (MDP) as a mathematical model of repeated decisions under stochastic transitions; connect it to stochastic/optimal control through the same basic question: choose controls over time to optimize expected future value.
- Define a finite horizon \(t=0,\ldots,T\), state \(S_t\), action \(A_t\), transition law \(P(S_{t+1}\mid S_t,A_t)\), per-period utility \(r_t\), and a policy \(\pi(A_t\mid S_t)\).
- Give a Bellman recursion:
  \[
  V_t(s)=\max_{a\in\mathcal A_{\mathrm{allowed}}(s,t)}
  \mathbb E\!\left[r_t(s,a,S_{t+1})+V_{t+1}(S_{t+1})\mid s,a\right].
  \]
- Explain that the allowed set is a policy and rights gate, not something learned by maximizing outcomes.
- Introduce a partially observable MDP (POMDP) only where a relevant state is genuinely hidden or noisy: the lender sees posted transactions and customer reports, not all cash, obligations, or intent. The POMDP's information state is a belief distribution over possible states, updated from a specified observation model.
- Distinguish incomplete data from a proven latent state. Do not use a POMDP to turn missing evidence into confident claims about a borrower's private finances.
- Explain irregular review timing and long outcome horizons; a semi-Markov formulation may fit better when actions and follow-up intervals have different durations.
- State assumptions the writer must make explicit: Markov sufficiency, action consistency, stationarity or drift, interference across related accounts, episode end, and terminal unpaid exposure.

### 4. State, action, observation and reward design — 350 words

- Build state candidates from variables available at decision time: product and contractual schedule, validated arrears history, recent observed receipts, prior contacts and delivery, commitments, disputes, hardship flags where lawfully and appropriately used, data freshness, and uncertainty.
- Keep the borrower-entered information and derived features distinguishable; timestamp provenance and label uncertain/missing information as such.
- Define a narrow action set: standard service; respectful reminder through a permitted channel; request for a cash-flow discussion; a contractually and operationally authorized alignment option; specialist or human review.
- Exclude coercive contact, unauthorized third-party disclosure, random withholding of required support, and actions that would change terms without proper authority and process.
- Keep lender value, borrower outcomes and rights as separate dimensions. Potential reward elements may include sustainable repayment, net realized cash, re-default, servicing cost, customer burden and business continuity. Never collapse legal or contractual duties into a soft penalty.
- Keep expected loss, accounting ECL, portfolio tail loss and capital measures distinct. A one-period \(PD\times LGD\times EAD\) illustration is not automatically the booked IFRS 9 ECL, economic capital or regulatory capital; a borrower-level collection policy should not be rewarded against a portfolio capital formula it does not estimate.
- Define a hard feasibility filter \(\mathcal A_{\mathrm{allowed}}\) before policy scoring. Legal rights, consent/notice conditions, contact rules, affordability and authority are not for the reward function to trade away.
- Describe a POMDP observation as a noisy signal with a calibrated observation model, not a guessed “true borrower state.”

### 5. Method ladder: control first, RL only when justified — 500 words

- Set out a decision hierarchy:
  1. descriptive monitoring and a fixed lawful policy;
  2. a pre-specified randomized comparison for one decision;
  3. a transparent rule or contextual bandit for one-step adaptation;
  4. constrained dynamic programming or model-predictive control for repeated decisions with an explicit transition model;
  5. offline or model-based RL only if it adds material value and has sufficient support, robust policy evaluation and a credible simulator.
- Explain model-predictive control: repeatedly optimize over a short forecast horizon, execute only the next approved action, then update on new observations. It may be easier to inspect and constrain than an end-to-end learned policy.
- Present constrained MDP/POMDP optimization:
  \[
  \max_\pi \mathbb E_\pi\!\left[\sum_{t=0}^{T}\gamma^t r_t\right]
  \quad\text{subject to}\quad
  \mathbb E_\pi\!\left[\sum_{t=0}^{T}\gamma^t c_{j,t}\right]\le d_j,
  \]
  while clarifying that statutory rights and prohibited actions need hard per-decision gates in addition to cumulative operational constraints.
- Describe offline policy evaluation (OPE): replay logged trajectories only when state/action support and propensities are adequate; compare importance sampling, sequential doubly robust methods and fitted models; report overlap, effective sample size, uncertainty and sensitivity to unmeasured confounding.
- Explain why long reward delays, censoring, settlement reversals, rare actions, changing policies and partial observation make OPE fragile.
- Say what RL does not fix: unobserved confounding, poor data quality, illegal action sets, no overlap, a bad simulator, distribution shift or lack of a human owner.
- Technical sources to use: Kaelbling, Littman & Cassandra on POMDPs; Jiang & Li on sequential doubly robust OPE; Wachi & Sui on constrained safe RL; MIT OpenCourseWare dynamic programming and stochastic control notes.

### 6. Kenyan legal and rights architecture — 600 words

- Start by distinguishing **Article 31 of the Constitution** (privacy) from **section 31 of the Data Protection Act, 2019** (a prior DPIA for likely high-risk processing). The article must not call the Act's section “Article 31.”
- Explain scope: the Data Protection Act protects personal data about identified/identifiable natural persons. A limited company is not itself a data subject, but an owner, sole proprietor, guarantor, director or contact may be. Entity-level cash flows can still identify a natural person in small portfolios.
- Map the general rules:
  - DPA s25: fair, lawful, transparent processing; specified purposes; minimization; valid explanation for private-affairs data; accuracy; retention limits.
  - ss26–29: rights and collection/notice duties, including informing people of purpose, recipients, controller/processor contacts, security, whether provision is mandatory, and consequences of not providing data.
  - s30: lawful bases include specified consent and necessity grounds such as contract, legal obligation and carefully balanced legitimate interests; not a universal “consent-only” rule. Purpose-compatible further processing still matters.
  - s31 plus General Regs rr49–53: high-risk processing assessment before processing; automated decisions/profiling with legal or similar significant effects, large-scale processing, linking datasets for different purposes, innovative technology and other listed cases trigger close DPIA analysis; consult ODPC before processing when the statutory high-risk condition remains.
  - s32 and General Reg r4: when relying on consent, make it specific, informed and clear, including relevant automated use, third-party sharing, transfers, withdrawal and consequences.
  - s35 and General Reg r22: rights around solely automated decisions with legal/significant effects; notice, meaningful information about logic, significance/consequences, fairness, error prevention, suitable statistical procedures, correction of inaccuracies, bias controls and human intervention/voice. A nominal rubber-stamp reviewer is not a safe design assumption.
  - s36 objection; s37 commercial use; ss40–43 rectification/erasure, design/default and security/breach. Treat s37 carefully: obtain counsel's view on its interaction with s30 for model development or commercial reuse; do not assume one provision automatically disposes of the other.
  - ss44–47 add conditions for sensitive personal data, with a specific rule for health data in s46. Identify whether any hardship or vulnerability feature contains sensitive data or permits sensitive inferences; do not label ordinary financial information sensitive by default.
  - ss48–50 govern transfers outside Kenya and related safeguards. Map cloud hosting, subprocessors and research access against the actual transfer route.
- Add credit-specific rules:
  - Banking (Credit Reference Bureau) Regulations 2020 rr26, 37 and 39–40: notice before negative-information furnishing, dispute correction, and a bureau score not being the sole basis for credit denial. Rule 63(1)(c)–(2) separately requires an adverse-action notice when bureau information contributed to an adverse decision; distinguish these obligations when the model consumes bureau scores.
  - CBK Digital Credit Providers Regulations 2022 r2 expressly excludes licensed banks, microfinance institutions and SACCOs, among others. Apply the instrument only after classifying the provider. For an in-scope DCP, r20 constrains collection conduct; rr13–15 govern confidentiality and bureau data (including pre-listing notice under r14(5)–(6)); r18 requires reasonable ability-to-repay appraisal; rr22–26 cover complaints, systems, consumer information and permitted information access.
- Bound other constitutional principles accurately: Article 27 equality is a discrimination lens; Article 46 consumer rights may apply to consumer relationships; Article 47 is fair administrative action, especially for public bodies or public administrative functions, not a blanket rule that every private lender decision is an administrative act.
- End with a workflow: classify the decision and people affected; identify purpose, data, role and lawful basis; complete DPIA and consultation if required; publish understandable notice; constrain actions; provide a reachable challenge path and meaningful review; document updates and outcomes.

### 7. Reproducible worked example — 500 words

- Use a synthetic four-stage trajectory with transparent assumptions: day 0 missed payment; day 7 observation of delayed remittance; day 14 response/commitment; day 30 cash receipt or no receipt; later outcome window includes re-default.
- Give two strategies: a fixed standard reminder policy and an illustrative state-contingent policy. Do not claim the latter is better merely because it was designed with a simulator.
- Define the state table and uncertainty, action set, transition assumptions and outcome definitions before showing calculations.
- Calculate a simple present-value or net-recovery example and report borrower outcomes beside lender outcomes. A payment shifted earlier is a timing benefit, not automatically an incremental collection; count only proven incremental value after costs and reversals.
- Demonstrate a penalty trap: if the reward sees only 30-day collections, aggressive actions might move a payment into the window while increasing re-default or customer burden later. Fix with longer follow-up and terminal values, not by pretending the immediate reward captures all welfare.
- Include sample Bellman backup for one state/action, and a small policy table of estimated value, uncertainty and eligibility.
- Add a clear label: synthetic demonstration, not borrower advice, causal evidence, model output or a live policy.

### 8. Experiment design and sequential policy evaluation — 450 words

- Stage 0: define the estimand, horizon, eligible population, baseline, permitted actions and customer safeguards.
- Stage 1: validate data capture, decision timestamps, delivery, assignment, acceptance, overrides and mature outcomes.
- Stage 2: conduct a pre-registered randomized pilot for a limited one-step action where equipoise and service safeguards permit; do not randomize away legal rights, essential assistance, contractual remedies or ordinary complaint handling.
- Stage 3: only if treatment carry-over matters and evidence supports sequential modeling, design a sequential experiment with approved exploration limits, customer-level trajectory IDs and logging of conditional assignment probability at every decision.
- Stage 4: freeze the candidate policy, evaluate on a later or otherwise properly separated cohort, and compare with the best current policy.
- Distinguish intention-to-treat, treatment-received and per-protocol questions. Track non-delivery, withdrawal, censoring, re-default and competing exits.
- Require inference that accounts for adaptive assignment, repeated observations, customer-level clustering, delayed outcomes and stopping rules.

### 9. Operational governance, monitoring and failure modes — 350 words

- Require a versioned action policy, guardrails, fallback, named accountable owner, independent challenge and override reason codes.
- Monitor calibration and policy value separately; also audit contact burden, complaints, affordability, fairness across appropriate groups, data freshness, adverse outcomes, legal basis and action eligibility.
- Treat drift, channel failure, new data sources, changed collection practices, model revisions or changes in who acts as triggers for review and possible DPIA refresh.
- Route data correction and disputes into current decisions and downstream learning records; distinguish correcting live features from legally required retention of historical decision evidence.
- Do not infer that de-identification has succeeded merely because names were removed; check re-identification and small-cell risk.
- Keep the action record: decision-time information, source/freshness, policy/model version, permitted set, actual assignment probability, action offered/delivered, reviewer, explanation, override, outcome and correction.
- State kill conditions: rights failure, unsafe behavior, invalid propensity logging, major overlap loss, unresolved distribution shift or evidence of unequal harm.

### 10. A staged implementation blueprint — 180 words

- Deliverable A: Part 3 experiment contract and action dictionary.
- Deliverable B: Part 6 empirical protocol, with explicit observation, action, outcome, missingness and legal gates.
- Deliverable C: synthetic state-transition laboratory with fixed-policy, bandit, rule-based and constrained-control comparisons.
- Deliverable D: prospective, human-authorized test only after data governance, DPIA, legal review and independent validation are satisfied.
- Place code and case details in the research laboratory; keep public article claims narrower than the evidence.
- Separate “research simulation,” “shadow recommendation,” “human decision support” and “live automated decision” as different intended uses.

### 11. Conclusion — 120 words

- Return to the opening question: the best next contact may depend on what the last contact changed, but that does not make the algorithm the decision owner.
- Summarize the progression: prediction → one-step experiment → sequential control only when action carry-over, data and evaluation justify it.
- Close with the practical test: Can the lender show what was known, what action was permitted, why it was selected, how the borrower can correct or contest information, and whether the policy improved sustainable outcomes over a strong baseline?

## Claims and editorial checks

- Do not say “AI understands the borrower”; describe recorded evidence and uncertainty.
- Do not present human intervention as a cure-all or claim section 35 applies to every model score; analyze the decision, material effect and actual human role.
- Do not use “POMDP” merely because a file is incomplete; justify the latent state and observation model.
- Do not claim that a simulated sequential policy establishes causal benefit or legal compliance.
- State that this is a research proposal for Underwrite for Collection, not an implementation already present in the whitepaper or laboratory.

## Core source list

- Kenya Constitution, 2010, Articles 27, 31, 46 and 47: https://www.mod.go.ke/the-constitution-of-kenya-2010-online/
- Data Protection Act, 2019 (Kenya Law): https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402022-12-31/source
- Data Protection (General) Regulations, 2021, L.N. 263/2021 (Kenya Law): https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng%402022-12-31/source
- ODPC DPIA Guidance Note: https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Note-on-Data-Protection-Impact-Assessment-1.pdf
- Banking (Credit Reference Bureau) Regulations, 2020, L.N. 55/2020: https://www.centralbank.go.ke/wp-content/uploads/2026/03/The-Banking-Credit-Reference-Bureau-Regulations.pdf
- CBK Digital Credit Providers Regulations, 2022, L.N. 46/2022: https://www.centralbank.go.ke/wp-content/uploads/2022/03/L-.N.-No.-46-Central-Bank-of-Kenya-Digital-Credit-Providers-Regulations-2022.pdf
- Kaelbling, Littman & Cassandra (1998), *Planning and Acting in Partially Observable Stochastic Domains*: https://www.cassandra.org/arc/papers/aij98.pdf
- Jiang & Li (2016), *Doubly Robust Off-policy Value Evaluation for Reinforcement Learning*: https://proceedings.mlr.press/v48/jiang16.html
- Wachi & Sui (2020), *Safe Reinforcement Learning in Constrained Markov Decision Processes*: https://proceedings.mlr.press/v119/wachi20a.html
- MIT OCW, *Dynamic Programming and Stochastic Control*: https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/pages/lecture-notes/

## Relationship to the whitepaper

This outline extends the Part 3 contextual-bandit proposal and the Part 6 research brief. It does not replace the planned causal protocol, and it does not say sequential RL is already implemented. Add it to the master whitepaper only after the action/rights gate, worked case, legal review and sequential evaluation method are resolved. For the EL/ECL/tail-risk terminology used in the financial bridge, see the [cross-project screenshot synthesis](<../../../regtech-kesonia-treasury/docs/methods/SCREENSHOT_ENRICHMENT_ALM_CREDIT_LOSS_AND_WORKBENCH_2026-10-04.md>).
