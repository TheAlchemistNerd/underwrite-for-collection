# AI, bandits and reinforcement learning across the credit and Treasury lifecycle

**4 October 2026. Source review and proposed development; current manuscript and code status distinguished throughout.**

## Direct answer

The whitepaper gives AI a developed **predictive** role, gives contextual bandits an explicit **later experimental challenger** role, and routes validated behavioural evidence into Treasury and ALCO governance. It does not yet develop or implement a complete sequential reinforcement-learning controller for either collections or the balance sheet.

**Follow-up package added 4 October 2026:** the two proposed 4,000-word article outlines and the Kenyan legal map now sit beside this review:

- [Sequential collection control article outline](SEQUENTIAL_COLLECTION_RL_LINKEDIN_OUTLINE_4000_WORDS_2026-10-04.md)
- [Treasury/ALM/POMDP control article outline](TREASURY_ALM_POMDP_CONTROL_LINKEDIN_OUTLINE_4000_WORDS_2026-10-04.md)
- [Kenya automated-decision and data-governance legal map](KENYA_AUTOMATED_DECISION_DATA_GOVERNANCE_REVIEW_2026-10-04.md)
- [Screenshot synthesis: Treasury ALM, portfolio loss and workbench boundaries](<../../../regtech-kesonia-treasury/docs/methods/SCREENSHOT_ENRICHMENT_ALM_CREDIT_LOSS_AND_WORKBENCH_2026-10-04.md>)

The first extends Part 3's one-step contextual-bandit proposal into a constrained sequential research design. The second extends Part 5 without confusing borrower-level causal evidence with bank-wide funding or hedging effects. Both are outlines, not completed articles, legal clearance or deployed algorithms.

The existing case code implements reconciled hypothetical cash and governed decisions. There is no fitted neural credit model, bandit learning loop or sequential RL policy in that laboratory. A deterministic policy gate is an important control but is not a learned policy. Part 6 exists as a [brief](../briefs/Part_6_BRIEF.md); the current manuscript directory contains Parts 1, 2a, 2b, 3, 4 and 5.

## Where each role is already documented

| Current source | What it develops | Current limit |
|---|---|---|
| [Part 2a §6](../parts/Part_2a_Temporal_Evidence_and_Feature_Engineering.md#6-what-artificial-intelligence-adds-after-behavioural-scoring-is-established) | Candidate GRU/Transformer encoders, time/entity-aware representations and controls for duplication of explicit financial information | Method architecture; no fitted encoder in the worked-case laboratory |
| [Part 2b §§3–7 and §12](../parts/Part_2b_Hierarchical_Bayesian_Underwriting_Causal_Identification_and_Lifecycle_Dependence.md) | Hierarchical Bayesian prediction, nonlinearities, shrinkage, causal identification and held-out validation | A risk estimate under an observed policy does not estimate the effect of changing that policy |
| [Part 3 §7](../parts/Part_3_Regulatory_Orchestration_Fair_Intervention_and_Collection_Governance.md#7-learning-which-interventions-work) | Stable randomised pilot first; contextual bandit later; logged propensities and a one-step doubly robust policy-value formula | No executable assignment/learning/evaluation experiment yet |
| [Part 4, experiment record](../parts/Part_4_Bank_Controlled_Research_Sandboxes_and_Enterprise_Credit_Architecture.md) | Eligibility, assignment, delivery, receipt, crossover, override, withdrawal and mature outcomes | Institutional logging and interfaces still require implementation evidence |
| [Part 5 §§6.2–6.3](../parts/Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md) | Treasury recognition of available cash; acceleration, ultimate recovery and durable performance; shadow, live evidence and approval stages | Improved repayment prediction alone does not establish a usable funding benefit |
| Part 5 §§7.1–7.7 | Funding curves, two-sided FTP, attribution, IRRBB, ALCO and a Treasury scorecard | No RL-based hedge/funding optimiser is specified or demonstrated |
| Part 5 §8 and §11.3 | Causal net economic value and intended-use approval | Economic scenario comparisons remain separate from identified treatment effects |
| [Part 6 brief](../briefs/Part_6_BRIEF.md) | Population, assignment, power, delayed outcomes, safeguards and staged scale-up | Detailed manuscript and experimental implementation remain open |

The [worked laboratory](../../research_lab/README.md) is explicit about hypothetical inputs and the absence of fitted PD/LGD/CCF, causal estimates and live execution. Read the older Treasury gap review as historical review evidence; current Part 5 now contains the detailed FTP and ALCO sections listed above.

## 1. Prediction, experiment and sequential control answer different questions

**Predictive AI:** given information available today, what repayment, drawdown, prepayment or recovery path is plausible? Parts 2a–2b propose testing whether learned event sequences add useful information beyond explicit business cash variables. Forecast quality needs future-period calibration and uncertainty; a neural representation does not itself supply causal identification.

**Multi-armed bandit:** choose among permitted alternatives, observe the chosen action's outcome and adapt allocation as evidence accumulates. A contextual bandit conditions that choice on the customer's information. A plain bandit learns pooled action values; a contextual bandit can distinguish which action is useful for which eligible customer. One decision may have a delayed 90-day outcome and still be formulated as a bandit if later treatment is fixed and the episode is defined appropriately.

**Sequential reinforcement learning:** choose a sequence whose earlier actions change later states and feasible decisions. For example, payment alignment may change inventory, next month's income, re-default risk and the usefulness of a later workout action. This requires trajectory-level modelling/evaluation. The Part 3 one-step formula cannot simply be relabelled as a sequential policy evaluator. [Jiang and Li, 2016](https://proceedings.mlr.press/v48/jiang16.html).

Repeated monthly recalculation of a supervised risk score is not sufficient to establish RL. Nor does the existence of a partially observed borrower state automatically require a particular point-process or intensity model. Choose a model because it represents the decision and can be evaluated with the available data.

## 2. A practical contextual-bandit experiment

**Proposed design, not a completed experiment.** Start with one bounded decision episode: a permitted reminder channel/timing or an offered cash-planning discussion. Compare with an eligible standard-service option. Keep required hardship support and contractual rights outside randomised withholding. Separate experiments for material contractual amendments from low-impact servicing choices because their eligibility, costs and outcomes differ.

The recorded context contains decision-time business cash, product, arrears, affordability, existing obligations, prior contacts and evidence quality. The policy gate first determines the permitted action set. The assignment mechanism then chooses among those actions. Log the probability of the action **after all gating, capacity constraints and policy mixing**, together with policy version and past information used by the adaptive mechanism.

Use a stable randomised pilot to establish operational adherence and outcome measurement. An adaptive challenger can subsequently compare, for example, a hierarchical Thompson-sampling rule with the fixed allocation and a simple policy rule. The algorithm choice, prior, update schedule and exploration floor would need to be specified; none is selected in the current manuscript.

### Outcome and inference requirements

- Define primary outcomes such as sustainable cure or net recovery over a registered horizon; record re-default, business continuity, cost and customer burden alongside them.
- Pending outcomes stay pending. An account without 90 days of follow-up is not automatically a failed treatment.
- Distinguish assignment from offer, acceptance, delivery and override. Primary assignment-effect analysis and treatment-received analysis answer different questions.
- Freeze a candidate policy before a separate evaluation period. Keep borrower/group and time boundaries in nuisance-model fitting.
- Allow for adaptive assignment in uncertainty estimates; ordinary independent-sample confidence intervals and unrestricted repeated significance checks need not be valid. [Cook, Mishler and Ramdas, 2024](https://proceedings.mlr.press/v236/cook24a.html).
- Examine overlap, rare actions and effective sample size. Clipping large weights trades variance against bias; it is not a substitute for support or identification.
- If evaluating policy value and learning a treatment effect are both objectives, state both. Allocation that favours a currently promising arm can reduce precision for comparisons involving other arms.

For a stochastic one-step target policy, the Part 3 estimator can be extended as:

\[
\widehat V_{DR}(\pi)=\frac1n\sum_{i=1}^{n}
\left[\sum_{a\in\mathcal A_i}\pi(a\mid X_i)\widehat\mu(X_i,a)
+\frac{\pi(A_i\mid X_i)}{e_i(A_i\mid X_i,\mathcal H_{i-1})}
\{Y_i-\widehat\mu(X_i,A_i)\}\right].
\]

Here **n** is the number of evaluation episodes; **i** identifies an episode; **Xᵢ** is its decision-time context; **𝒜ᵢ** is its permitted action set; **Aᵢ** is the assigned action; **Yᵢ** is its defined outcome; **π** is the target assignment policy; **eᵢ** is the actual logging probability conditional on context and prior experiment history **ℋᵢ₋₁**; and **μ̂** is an appropriately fitted outcome model. The sum supplies predicted value under the target policy and the weighted residual corrects it using observed outcomes. For a deterministic target, this reduces to the manuscript's form. [Dudík, Langford and Li, 2011](https://icml.cc/2011/papers/554_icmlpaper.pdf).

This formula assumes the relevant outcome is observed or that missingness/censoring is separately addressed. Doubly robust estimation does not repair unmeasured confounding, unsupported actions or incorrect treatment definitions. Adaptive-history dependence, nuisance fitting and outcome timing must be part of the estimator and its inference.

## 3. A sequential collection-policy extension

**Proposed extension.** Define decision stages and histories including available cash, arrears, previous support, business activity, protection status, pending receipts and evidence uncertainty. Choose feasible actions such as follow-up, maintaining terms, a permitted alignment offer or specialist review. A partially observed formulation is appropriate only if its latent state, observation process and updating assumptions can be justified.

Define a finite episode and terminal treatment of unpaid debt so a policy cannot improve its measured reward by pushing losses beyond the reporting window. Compare a fixed policy, a simple decision rule, the one-step bandit where appropriate, and a sequential method using the same scenarios and data support.

The objective can be discounted net cash value with explicit treatment, servicing and incremental funding costs. If capital is charged, multiply the annual charge rate by the capital exposure and the elapsed year fraction; distinguish that charge from a separately imposed solvency constraint. State whether a funding-inclusive discount rate or explicit funding cost is used so financing cost is not deducted twice. Customer affordability, required protections, contact limits and authority remain constraints rather than penalties a larger expected profit can buy away.

**Completion evidence:** reproducible trajectories, logged conditional action probabilities, supported policy evaluation with uncertainty, stress/model-misspecification tests, independent challenge and a prospective comparison. Success in a simulator establishes results under its assumptions. It does not establish effects on actual borrowers.

## 4. How the evidence reaches Treasury, ALM, FTP and ALCO

| Function | Useful AI contribution | Role of adaptive control | Required financial evidence |
|---|---|---|---|
| **Treasury cash planning** | Forecast dated settled and unrestricted collections, utilisation and recovery; quantify uncertainty | A collections experiment may change those cash paths | Separate accelerated from incremental receipts; test reversals, concentration, outages, persistent performance and customer working capital |
| **ALM — asset–liability management** | Estimate behavioural lives, prepayment, deposit pass-through/withdrawal and scenario dependence | Sequential funding/hedging research is a candidate where decisions alter later balance-sheet choices | Match assets and liabilities through time; compare NII (net interest income), EVE (economic value of equity), cash shortfall and collateral need under constraints |
| **FTP — funds transfer pricing** | Supply approved behavioural cash timing and optionality assumptions to the transfer-pricing methodology | A bandit does not directly determine a justified internal funding price | Freeze curve and policy versions, reconcile asset charge/deposit credit/Treasury residual, and attribute changes to volume, rate, basis, behaviour and cost |
| **ALCO — asset–liability committee** | Present alternative actions, sensitivities, uncertainty and exceptions in a common decision pack | A simulator or optimiser can recommend candidate actions | Named authority approves assumptions, limits and material actions; outcomes are compared with the original recommendation |

Part 5 already specifies the Treasury recognition and approval sequence. It is therefore stronger to connect the experimental output explicitly to that sequence than to add generic claims that AI optimises Treasury.

### A simple Treasury timing illustration

Suppose an experiment eventually supports an estimate that **KES 100,000 arrives 10 days earlier**, with the same ultimate collection, no additional re-default and usable settlement. At an assumed simple **12% annual marginal funding rate on ACT/365**, the undiscounted funding-cost saving is:

\[
100{,}000\times0.12\times\frac{10}{365}=\text{KES }328.77.
\]

If extra treatment/processing cost is KES 500, this channel alone contributes **KES −171.23**. Both numbers are hypothetical arithmetic. Other benefits or costs require their own estimates. The KES 100,000 receipt is not KES 100,000 of incremental value, and a single timing result does not automatically change FTP, recognised liquidity or customer terms.

### Treasury RL needs its own design

A possible ALM research state includes the dated balance sheet, maturities, curves, deposit behaviour, collateral, available facilities and capital/liquidity headroom. Feasible actions could include funding tenor, approved hedge quantity and liquidity-buffer allocation. A scenario engine supplies transitions; costs include execution, funding and margin liquidity. Stress constraints and concentration limits restrict actions.

Compare such a controller against a rule policy, constrained optimisation and model-predictive control before adding RL complexity. A bank has limited independent strategic histories, shared market shocks and actions that can change its own future funding conditions. Historical off-policy value can therefore have weak support. A borrower-level bandit experiment does not identify the counterfactual effect of a bank-wide funding strategy. This research belongs primarily in RegTech; Underwrite supplies credit and collection cash behaviour.

The newly supplied Treasury and credit-loss screenshots also sharpen the financial interpretation. ALM should assess both NII over a stated earnings horizon and EVE under stated discounting and behavioural assumptions; non-maturing-deposit pass-through, repricing lags, runoff and migration drive the result. A “free-funds” benefit in a rising-rate scenario is conditional on deposit retention, repricing, asset reinvestment and expenses. FTP is the approved internal allocation of funding, tenor and liquidity economics; it is not the external customer rate or a reward to be optimized in isolation. ALCO-approved risk appetite, prudential constraints and model-risk controls must define the feasible policy before any reward comparison. RegTech's [screenshot synthesis](<../../../regtech-kesonia-treasury/docs/methods/SCREENSHOT_ENRICHMENT_ALM_CREDIT_LOSS_AND_WORKBENCH_2026-10-04.md>) gives the definitions and banking-side examples.

For credit, a one-period \(PD\times LGD\times EAD\) calculation is an expected-loss approximation, while IFRS 9 ECL is a discounted, probability-weighted cash-shortfall measure and portfolio tail loss depends on dependence across borrowers. Do not present an intervention's expected collections or a local cure effect as unexpected loss, economic capital or regulatory capital. The two-loan common-shock illustration and the distinctions between accounting ECL, economic capital and regulatory capital are documented in the linked RegTech note; Underwrite remains the owner of borrower-level outcome definitions and collection evidence.

## 5. Concrete additions to the development programme

| ID | Proposed addition | Home and evidence needed |
|---|---|---|
| AI1 | Algorithm and experiment contract for one contextual bandit | Parts 3 and 6; eligibility, actual assignment probabilities, delayed rewards, adaptive inference, stopping and fallback |
| AI2 | Reproducible policy-learning comparison | Underwrite laboratory; fixed randomisation, simple rule and adaptive challenger; independent policy evaluation and explicit synthetic status |
| AI3 | Sequential treatment protocol where carry-over matters | Part 6 with Part 2b methods; trajectories, state/action/reward definitions, censoring and sequential evaluation |
| AI4 | Experimental outcome → cash ladder → FTP sensitivity | Part 5 and RegTech interface; amounts, dates, uncertainty, cost reconciliation and intended-use approval |
| AI5 | ALCO scenario decision and optional control-method comparison | RegTech canonical case; baseline optimisation first, supported RL research where justified, committee decision record and monitoring |

These extend U2/U4 in the [IFoA practical-application review](IFOA_PRACTICAL_APPLICATION_REVIEW_2026-10-03.md). AI1–AI5 are **proposed**, and no chapter, trained policy or production interface is made complete by this note. The immediate public explanation should state: predictive AI supports forecasts; experimental methods estimate action effects; adaptive policies require their own evaluation; Treasury and ALCO approve the financial use of the evidence.
