# From Treasury scenarios to partially observed stochastic control

## LinkedIn article outline — planned length: 4,000 words

**Working title:** *Treasury as a Control Problem: When Would a POMDP or Reinforcement Learning Add Value to ALM, FTP and ALCO?*

**Status:** Detailed editorial and research outline. It proposes a research extension to Part 5; it does not claim that a Treasury controller or RL implementation exists.

**Audience:** Bank Treasury, ALM, FTP, market/liquidity risk, finance, model risk, data science and ALCO members.

**Thesis:** Treasury decisions are sequential controls over an uncertain balance sheet. Stochastic optimization and model-predictive control should be the first comparators. A POMDP or RL method is useful only where material state uncertainty, repeated actions and learned dynamics justify its additional model and governance burden. A lender's collection experiment can inform cash-flow forecasts; it does not identify a bank-wide counterfactual funding or hedging strategy.

**Anchor example:** A hypothetical bank chooses a funding/hedge mix over monthly decision dates as deposits reprice and roll off, loans prepay or draw, and market curves move. The example carries uncertain collections from the Underwrite case into dated expected cash flows, then through funding and ALCO measures without claiming that a borrower-level model sets FTP or determines the bank's risk appetite.

## Word plan

| Section | Words |
|---|---:|
| 1. Opening: the balance sheet changes after each decision | 150 |
| 2. Translate treasury language into a control problem | 300 |
| 3. MDP, POMDP and the belief state | 450 |
| 4. Define objectives, actions and non-negotiable limits | 450 |
| 5. Choose the simplest method that can answer the question | 450 |
| 6. Reproducible Treasury case | 550 |
| 7. Kenyan legal and regulatory perimeter | 600 |
| 8. Evaluation, integration and ALCO governance | 500 |
| 9. Research and implementation sequence | 350 |
| 10. What this does not mean | 100 |
| 11. Conclusion | 100 |
| **Total** | **4,000** |

## Detailed outline

### 1. Opening: the balance sheet changes after each decision — 150 words

- Open with a Treasury action that changes the next state: fixing funding tenor, hedging an exposure or changing liquidity-buffer composition.
- Later deposits reprice, customers prepay, undrawn facilities are used, curves move and collateral is posted. The next best decision therefore depends partly on the previous action.
- Contrast a one-period forecast or one-step bandit with multi-period control.
- Frame the question as a model-selection problem: can a transparent scenario engine, deterministic rule, stochastic program or model-predictive controller already answer it? Use RL only if a sequential learner adds material, testable value.
- Connect to the whitepaper's Part 5: credit evidence contributes dated, uncertain borrower cash behavior to Treasury; it is not itself an FTP curve, hedge instruction or ALCO decision.

### 2. Translate treasury language into a control problem — 300 words

- Define ALM as managing cash-flow, repricing and value mismatch between assets and liabilities over time.
- Frame ALM as proactive balance-sheet management for sustainable profitability within liquidity, capital, customer, operational and risk-appetite constraints. Describe the ALCO, Treasury, independent risk, Finance and model-validation roles as a governance pattern whose actual delegations must be institution-specific.
- Define FTP as internal attribution/pricing of funding, liquidity, tenor and optionality under an approved methodology; it is an input/accounting signal for product and balance-sheet economics, not a free policy reward to manipulate.
- Distinguish the banking book from the trading book and identify credit spread risk in the banking book (CSRBB) separately from IRRBB where it is in scope; do not borrow a trading-book measure as a generic banking-book result.
- Define ALCO as the governance forum that sets or approves limits, assumptions and actions rather than a model substitute.
- Give a monthly finite-horizon setting, and differentiate state variables from forecasts, accounting allocations and control actions.
- Explain where Underwrite fits: estimate observed/causal collection timing and uncertainty; Treasury separately tests whether those cash flows are settled, available, diversified, persistent and appropriate for the liquidity/funding measure.
- Include four value pathways: timing benefit; genuinely incremental collection; changed funding or hedging cost; and liquidity/capital consequence. Do not double count a repayment as both extra cash and an equivalent FTP benefit.
- State that assumptions, repricing, curve versions and transfer prices need dated lineage.

### 3. MDP, POMDP and the belief state — 450 words

- Introduce a stochastic control model with state \(S_t\), action \(A_t\), stochastic market/customer transition \(P\), operating cost \(c_t\) and risk/return outcomes.
- Distinguish:
  - MDP: state summary is adequate for the transition model;
  - POMDP: the operational state is only partly observed, so the controller maintains a belief distribution \(b_t(s)\);
  - stochastic control: broad control-theoretic formulation, including continuous-time dynamics and constraints;
  - RL: methods for learning a policy or value function when parts of the transition/reward model are unknown.
- Avoid saying POMDP is the natural label for any forecast uncertainty. A POMDP requires an explicit hidden state and observation process. If parameter uncertainty is the issue, Bayesian model uncertainty or robust optimization may be clearer.
- Illustrate unobserved deposit pass-through and withdrawal response: known account cash balances and posted rates are observations; latent customer rate sensitivity is a modelled state/parameter, not a fact.
- Show belief update at a high level: prior belief × likelihood of observed deposit/repayment behavior, normalized. Require calibration and model checks before policy use.
- Explain partial observability costs: beliefs can be wrong, estimation errors compound through time, and a complex state does not create evidence.
- Note shared macro shocks create dependence across the whole bank; many account records are not thousands of independent bank-level policy histories.

### 4. Define objectives, actions and non-negotiable limits — 450 words

- Specify a separable objective that may include expected net interest income (NII), economic value of equity (EVE), funding cost, liquidity carry, hedge/transaction costs, collateral/margin cash, concentration and operational costs.
- Define NII and EVE horizons, balance-sheet assumptions and discounting separately. Model non-maturing deposit pass-through/beta, repricing lag, decay, withdrawal and migration with uncertainty. Treat “free funds” in rising rates as a conditional spread outcome, not a free-profit identity; state the balance-sheet comparator and asset-reinvestment, deposit-retention and expense assumptions.
- Define NIM and ROE denominators and capital allocation before comparing products or business units. An internal profitability measure does not itself establish economic profit, distributable cash or shareholder return.
- Do not combine them into an unexplained single reward. ALCO first sets tolerances and the model reports a frontier or constrained solution.
- Illustrate a constrained objective:
  \[
  \max_{\pi}\;\mathbb E_{\pi}\!\left[\sum_{t=0}^{T}\gamma^t R_t\right]
  \quad\text{subject to}\quad
  g_k(S_t,A_t)\le 0,\qquad
  \Pr_\pi(\text{limit breach})\le \epsilon_k.
  \]
- Describe candidate controls: approved funding mix/tenor, hedge tenor or notional within authority, liquidity-buffer composition, and review triggers. State explicitly which are decisions, forecasts or policy inputs.
- Hard constraints include the institution's applicable prudential limits, internal ALCO limits, contractual terms, approved counterparties/instruments, collateral availability and authorization. Do not teach the optimizer that breaching them is acceptable if the reward is high.
- Distinguish a penalty approximation from an enforceable feasibility filter; use robust/chance constraints only where the probability model and risk appetite are approved.
- Discuss uncertainty and stress regimes. Mean NII alone hides tail liquidity calls and collateral need.

### 5. Choose the simplest method that can answer the question — 450 words

- Present a ladder:
  1. repricing ladders, cash-flow schedules, deterministic shocks and scenario analysis;
  2. robust/stochastic programming and approved policy rules;
  3. rolling-horizon model-predictive control with explicit forecast updates;
  4. dynamic programming for a tractable state/action space;
  5. constrained RL/POMDP if repeated actions and unknown dynamics make a learned policy valuable.
- Explain why short-horizon MPC is often a good challenger: it can re-optimize as forecasts change, expose constraints and execute only a committee-approved next action.
- Explain RL's potential: discover interactions among action timing, uncertain deposit behavior, prepayment and evolving funding need. Explain costs: low number of bank-wide decisions, nonstationary markets, action-dependent data, simulator risk and poor off-policy support.
- Compare each method on out-of-sample decision value, limit breaches, tail liquidity, interpretability, operational resilience and maintenance cost—not only a fitted reward or backtest.
- Require a matched simulator and a benchmark policy before claiming improvement; stress state transitions and model misspecification.
- Include a safe-improvement gate: preserve a validated baseline, set maximum allowed policy deviation, require offline evaluation and independent sign-off, start in shadow mode, and retain human approval for execution.

### 6. Reproducible Treasury case — 550 words

- Define a simplified, fictional balance sheet with two decision dates, three funding choices and one permitted hedge choice. Specify unit, day count, curve date, cash-flow timing and all assumed parameters.
- Include a small uncertain state for deposit repricing/runoff and borrower cash receipts:
  - observed: scheduled loan balances, realized collections, available cash, current deposit rates, published curves and collateral posted;
  - latent/uncertain: next-period deposit response and future prepayment;
  - action: approved funding tenor/hedge exposure within limits;
  - transition: market scenario plus behavior response;
  - outcome: NII, EVE, liquidity buffer and margin cash through the same horizon.
- Carry an illustrative payment-timing estimate through a dated cash ladder. State why earlier identical repayment can reduce short-term funding need but not change lifetime expected collections; only additional receipts after costs count as incremental.
- Demonstrate an MPC comparison with a simple baseline and the uncertain scenario model. Report the chosen actions across base, runoff, rate-shock and collateral-stress cases.
- Include one rising-rate sensitivity that varies deposit pass-through and runoff, and report the distinct NII and EVE effects plus the change in liquidity, collateral and product/unit NIM. Identify assumptions behind each result; do not treat FTP transfer entries as consolidated income.
- Show a belief update for one observed deposit movement and the posterior distribution, but label all numbers synthetic and avoid an implied calibrated Kenyan bank model.
- Include reconciliation checks: balance sheet identities; opening/closing cash; interest accrual; hedge cash flows; FTP charge/credit and Treasury residual; collateral/margin; source/curve/policy version.
- Produce results as a reproducible script and CSV/Parquet outputs rather than a prose-only worked case.
- State what must be added before a real example: validated local instruments/curves, institution's prudential rules, behavioral histories, limit definitions, transaction cost, settlement and margin conventions.

### 7. Kenyan legal and regulatory perimeter — 600 words

- Explain that this Treasury article has two data cases:
  1. aggregate balance-sheet, market and institution-level data may not be personal data;
  2. account-level personal deposits, borrower-level repayments, sole-proprietor receipts or identifiable customer behavior is personal data and triggers the relevant DPA duties.
- Reuse the separate legal map; do not recite every statute in full.
- Apply Constitution Art 31 and DPA s25 purpose, minimization, accuracy, retention and fairness principles to any personal-data inputs. Articles 27/46 are relevant where individuals and consumer relationships are affected; Art47 should be applied carefully to public/administrative decisions rather than assumed to govern internal private-bank Treasury choices.
- Identify DPA s30 lawful basis, s29 notices, rights in s26, s31/General Regulations r49 DPIA, s35/r22 solely automated decisions and meaningful intervention, s36 objections, s37 commercial-use issue, ss41–43 design/default, security and breach provisions, ss44–47 sensitive-data conditions, and ss48–50 transfer provisions. Treat any sensitive-data question as a feature-level legal assessment, not an assumption that ordinary financial records are sensitive.
- The ordinary ALCO control recommendation does not automatically amount to a significant decision about an individual. If the same system changes an identifiable depositor's rate, product access or another individually significant outcome, analyze that decision separately.
- Keep customer data outside the policy state where aggregated sufficient statistics answer the Treasury question. Document aggregation method, re-identification risk and access roles; “pseudonymous” is not synonymous with anonymous.
- Add bank-specific prudential duties as a regulatory perimeter check: identify whether the institution is a bank, microfinance provider, DCP, SACCO or other regulated entity; map current CBK/sector rules, approved ALM policy, liquidity/capital limits, outsourcing and model-risk controls with counsel and the responsible risk officer.
- State that the Banking (Credit Reference Bureau) Regulations govern credit-information operations, not bank-wide ALM; cite them only where a case uses bureau data or scores.
- As of this research date, treat Kenya's Artificial Intelligence Bill, 2026 and AI Strategy as policy/legislative watch items, not as operative statutory duties. Recheck parliamentary status before publication.

### 8. Evaluation, integration and ALCO governance — 500 words

- Use realistic chronological backtests with curve vintages and information available at each decision date; do not leak future curves or realized cash outcomes into the state.
- Separate model fitting, parameter estimation, policy selection and independent evaluation in time.
- Use scenario robustness, stress tests, sensitivity to observation error, policy-regret bounds and action support. Show where a learned action is extrapolating beyond recorded policy.
- Backtest is not causal identification: the actions historically taken may respond to hidden information unavailable in the dataset. State where randomized or natural-experiment evidence would be required.
- Reconcile forecast cash to realized cash; separate collections timing, incremental receipts, recoveries, concentration and reversals.
- Present ALCO pack outputs: recommended next action, feasible alternatives, binding limits, exposure changes, uncertainty ranges, stress losses, assumptions, exceptions and a clear approval/decline record.
- Maintain versioned market data, curve construction, behavior assumptions, model code, decisions, overrides and outcomes.
- Establish model-change triggers and named owners in Treasury, market/liquidity risk, finance, compliance, data protection, model validation and technology.
- Require an approved fallback policy and a stop mechanism. Execution systems should check limits and authority independently of the learned model.

### 9. Research and implementation sequence — 350 words

- Step 1: define whether the question is customer-level collection, funding cash forecasting, ALM, FTP attribution or ALCO action. Do not mix their estimands.
- Step 2: document state/action/outcome dictionaries and legal data map.
- Step 3: create a reproducible static scenario case and reconcile every cash flow.
- Step 4: establish transparent rule-based, stochastic-programming and MPC baselines.
- Step 5: test POMDP/RL only where the uncertain state and action-dependent transition are evidenced; compare policy performance and constraints on identical scenarios.
- Step 6: run shadow recommendations and independent challenge; produce no autonomous execution in this research plan.
- Step 7: require institution-specific legal, compliance, Treasury, model-risk and committee approval before any live use.
- Include deliverables: scenario inputs, financial-quantity dictionary, model card, action authority matrix, policy evaluation report, ALCO output mock-up and reproducibility record.
- Link back to Part 5 sections on FTP, funding curve attribution, IRRBB and ALCO. Place institution-wide Treasury controller research primarily in RegTech KESONIA; Underwrite supplies the validated credit cash behavior and explicit boundary.

### 10. What this does not mean — 100 words

- RL is not automatically more accurate, more compliant or more profitable than optimization.
- A high-performing simulator policy can be wrong in production if transition assumptions are wrong.
- A bank's millions of accounts do not create millions of independent histories for a bank-wide policy.
- A borrower-level collection experiment does not identify the impact of changing wholesale funding or hedging.
- FTP must not be reverse-engineered as a reward to produce a preferred business answer.
- Aggregate data reduces personal-data exposure but does not settle confidentiality, banking secrecy, security or other sector duties.
- POMDP beliefs are disciplined uncertainty representations, not permission to infer intimate information without necessity and lawful authority.

### 11. Conclusion — 100 words

- Summarize the distinction: Treasury operates a sequential stochastic system; POMDP describes partial observability; stochastic control defines the optimization problem; RL is one possible way to learn a policy.
- State the evidence threshold for complexity: action carry-over matters, model transitions are credible, a simpler baseline is insufficient, and policy value can be evaluated under hard limits.
- Reconnect the workbench boundary: Underwrite for Collection generates carefully validated dated borrower cash evidence; RegTech KESONIA develops bank-wide curve, FTP, ALM and ALCO workflow research.
- Close with a practical committee question: “What changes in the next decision, under which stress, within which approved limit, and who authorizes it?”

## Claims and editorial checks

- Do not describe FTP as a control action unless a specific methodological decision is being optimized; keep internal funding attribution distinct from external balance-sheet execution.
- Do not imply that personal-data law applies identically to a wholly aggregate Treasury model and an account-level behavioral model.
- Do not claim that borrower-level experimental evidence makes a bank-wide Treasury policy causal.
- Do not imply that an RL policy can relax regulatory or ALCO limits.
- Do not call a synthetic demonstration a bank calibration, forecast, recommendation or regulatory compliance test.

## Core source list

- Kenya Constitution, 2010: https://www.mod.go.ke/the-constitution-of-kenya-2010-online/
- Data Protection Act, 2019 (Kenya Law): https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402022-12-31/source
- Data Protection (General) Regulations, 2021: https://new.kenyalaw.org/akn/ke/act/ln/2021/263/eng%402022-12-31/source
- ODPC DPIA Guidance Note: https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Note-on-Data-Protection-Impact-Assessment-1.pdf
- Kenya AI Bill record and text: https://www.parliament.go.ke/node/25555
- Kenya AI Strategy: https://www.ict.go.ke/node/641
- Kaelbling, Littman & Cassandra (1998), POMDPs: https://www.cassandra.org/arc/papers/aij98.pdf
- Jiang & Li (2016), sequential doubly robust OPE: https://proceedings.mlr.press/v48/jiang16.html
- Wachi & Sui (2020), constrained safe RL: https://proceedings.mlr.press/v119/wachi20a.html
- *Deep Treasury Management for Banks* (research paper; conceptual comparator, not Kenyan deployment evidence): https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2023.1120297/full
- MIT OCW, *Dynamic Programming and Stochastic Control*: https://ocw.mit.edu/courses/6-231-dynamic-programming-and-stochastic-control-fall-2015/pages/lecture-notes/

## Relationship to the whitepaper and project boundaries

The article is a proposed Part 5/Part 6 bridge. Underwrite for Collection can provide validated borrower-level collection timing and treatment-effect evidence. Institution-level curve construction, FTP, ALM, IRRBB, bank liquidity/capital limits and ALCO workflow belong primarily in RegTech KESONIA. SokoIntel may later present approved analytics; it is not the source of the policy authority or legal determination. None of those downstream artifacts is implied complete by this outline.

The supplied Treasury course and model-risk screenshots have been synthesized in the [ALM, credit-loss and workbench review](<../../../regtech-kesonia-treasury/docs/methods/SCREENSHOT_ENRICHMENT_ALM_CREDIT_LOSS_AND_WORKBENCH_2026-10-04.md>). Use it as the accounting and capital terminology check while drafting; the screenshot itself is not institution-specific evidence.
