# Article 1 mathematical appendix: offers, cash outcomes and experimental learning

This appendix derives the mathematical relationships used in Article 1. All monetary examples are hypothetical. Each derivation states the population and information conditions needed for its interpretation. Probabilities are dimensionless; currency amounts are in Kenyan shillings (KES); the time unit is stated for each example. Equations concern an approved eligible population and a defined contract and servicing regime. A statistical comparison becomes a causal offer comparison when consistency, the stated assignment conditions and the relevant interference assumptions hold.

## A1.1 Notation and the unit of analysis

| Symbol | Definition |
|---|---|
| $i=1,\ldots,n$ | Eligible applicant or prespecified randomisation unit |
| $X_i$ | Information available before that unit's assignment |
| $H_{i-1}$ | Information available to the allocation rule before assignment $i$, including outcomes already received |
| $A_i\in\mathcal A(X_i)$ | Assigned approved offer; $\mathcal A(X_i)$ is the eligible action set |
| $e_i(a\mid X_i,H_{i-1})$ | Actual conditional assignment probability after eligibility gates |
| $\pi(a\mid x)$ | Target policy whose expected outcome is evaluated |
| $U_i(a)$ | Indicator that applicant $i$ would accept and draw offer $a$ |
| $Y_i(a)$ | Prespecified applicant-level outcome under offer $a$ |
| $R_i$ | Observed scalar reward, with declared accounting and observation conventions |
| $t$ and $\tau$ | Time since origination and the endpoint horizon |
| $d_t$ | Discount factor from time $t$ to the valuation date |
| $T_i,J_i,C_i$ | Event time, event cause, and right-censoring time |
| $\mu(x,a)$ | Conditional expected reward for action $a$ |
| $\theta$, $\beta$ | Regression coefficient vectors, defined in the relevant model |

The same letter is not used for take-up and survival time here: $U$ denotes take-up and $T$ denotes event time. The article's $T$ as a cash-flow horizon is written $\tau$ below. All probabilities and expectations are conditional on membership in the eligible study population unless another population is explicitly specified.

## A1.2 Construct the reward from a dated cash ledger

Let $P_0$ be the advance at origination, $Q_t$ actual borrower and recovery receipts, $O_t$ attributable operating and servicing payments, and $B_t$ external funding cash flow when it is explicitly included in the chosen financing convention. A realised asset-level discounted contribution, valued using a declared discount curve and with funding handled through that curve, is

$$
W=-P_0+\sum_{t=1}^{\tau}d_t(Q_t-O_t).
$$

The advance and subsequent principal receipts are both represented. A missed principal payment reduces $Q_t$; subtracting that same principal again as a realised loss would count the shortfall twice. If the analysis instead uses an accounting margin, its revenue and loss components must be defined so they reconcile to this cash ledger. For example, interest and fee income less funding expense, servicing expense and net credit charge is an accounting presentation with a separate principal roll-forward. The article's compact reward expression is meaningful only after making that choice explicit.

To derive a cash-shortfall presentation, let $Q_t^{\mathrm{ctr}}$ be the contractual receipts and define the present value of their shortfall by

$$
L_{\mathrm{PV}}=\sum_{t=1}^{\tau}d_t
  \left(Q_t^{\mathrm{ctr}}-Q_t\right).
$$

Substitution gives the identity

$$
\begin{aligned}
W
&=-P_0+\sum_t d_t(Q_t^{\mathrm{ctr}}-O_t)-L_{\mathrm{PV}}\\
&=-P_0+\sum_t d_t(Q_t-O_t).
\end{aligned}
$$

Consequently, the article's expected-value form can be implemented consistently as

$$
V(a,x)=E\!\left[
-P_0(a)+\sum_t d_t\{Q_t^{\mathrm{ctr}}(a)-O_t(a)\}
-L_{\mathrm{PV}}(a)\mid X=x\right].
$$

If $CF_t$ already denotes actual net cash including the initial advance and recovery shortfalls, a further deduction of $L_{\mathrm{PV}}$ is unnecessary. If funding cash flows $B_t$ are modelled explicitly, include their signs and dates and use a valuation convention consistent with that financing perspective. An FTP charge and an external funding cost require an explicit reconciliation; they cannot both be deducted for the same economic funding requirement without explanation. The IFRS 9 effective-interest-rate discount convention for an impairment allowance has its own purpose and is retained separately from the pricing discount curve.

**Numerical example.** Advance KES 100,000 today. Suppose twelve end-of-month receipts are KES 9,500, monthly servicing cost is KES 100, and the monthly discount rate is 1%. With full payment,

$$
\begin{aligned}
d_t&=(1.01)^{-t},\\
W&=-100{,}000+9{,}400\sum_{t=1}^{12}(1.01)^{-t}\\
&=-100{,}000+9{,}400\frac{1-(1.01)^{-12}}{0.01}\\
&=5{,}797.73\ \mathrm{KES}.
\end{aligned}
$$

If the final KES 9,500 receipt is missing and no later recovery is expected within the valuation model, its present-value shortfall is $9{,}500/(1.01)^{12}$. Reduce $W$ by that amount once. An eventual recovery is entered at its expected or realised recovery date, with its collection costs, rather than treated as immediate cash at default.

The value per eligible applicant also includes take-up. If $C_a^{\mathrm{offer}}$ is the cost of delivering the offer and $W_a$ is contribution conditional on origination,

$$
E[Y(a)\mid X=x]
=-C_a^{\mathrm{offer}}(x)
+\Pr\{U(a)=1\mid x\}\,
 E[W_a\mid U(a)=1,x].
$$

This is the law of total expectation, with a zero originated-loan contribution for non-takers and separately recorded offer costs. Other applicant outcomes, such as complaints or business distress, need their own definitions for non-takers. The separation explains why profit per originated loan and contribution per applicant can rank offers differently.

## A1.3 Random assignment, intention to treat and take-up

The credit experiment separates assigned offers and subsequent behaviour using the experimental-design logic in [4].

For two offers $a$ and $b$, define the eligible-population intention-to-treat estimand

$$
\Delta_{\mathrm{ITT}}=E[Y(a)-Y(b)].
$$

Assume consistency, no relevant interference between randomisation units, and assignment independent of potential outcomes within the randomisation strata. Then

$$
\begin{aligned}
E[Y\mid A=a]&=E[Y(a)\mid A=a]=E[Y(a)],\\
E[Y\mid A=b]&=E[Y(b)\mid A=b]=E[Y(b)].
\end{aligned}
$$

The difference of the two assigned-group means therefore estimates $\Delta_{\mathrm{ITT}}$. With stratification, calculate stratum-specific comparisons and aggregate using the target stratum proportions; an unweighted average across differently sized strata generally targets a different population.

Conditioning on acceptance changes the comparison:

$$
E[Y\mid A=a,U=1]
=E[Y(a)\mid U(a)=1].
$$

The corresponding mean under $b$ conditions on $U(b)=1$. The two accepting groups can have different risk and business characteristics. Randomisation of $A$ does not make these two post-assignment subgroups identical. Record acceptance as an outcome of the offer and retain every assigned applicant in the ITT denominator.

**Reproduce the article's counts.** In each arm 100 applicants are assigned. Take-up is 72% and 75%; current-or-repaid status among the funded loans is

$$
\frac{58}{72}=80.5556\%,\qquad
\frac{64}{75}=85.3333\%,
$$

giving a funded-subgroup difference of 4.7778 percentage points. Define a distinct applicant-level endpoint $J(a)=1$ if an applicant both originates and is current or fully repaid at twelve months. Its assigned-group estimates are 58% and 64%, giving an ITT difference of 6 percentage points for that combined endpoint. This endpoint is fully defined for non-takers, whose $J=0$ denotes no origination; it does not label them as defaulters. A simple independent-binomial standard error for the difference is

$$
\widehat{\mathrm{SE}}
=\sqrt{\frac{0.64(0.36)}{100}+\frac{0.58(0.42)}{100}}
=0.06885.
$$

The normal-approximation 95% interval is approximately $0.06\pm1.96(0.06885)$, or −7.49 to 19.49 percentage points. It is a rough fixed-design illustration; the realised cash endpoint requires its actual cash observations and its own uncertainty analysis.

For a finite population of $N=n_a+n_b$ randomly assigned units, the randomisation variance of the difference in means is

$$
\operatorname{Var}(\widehat\Delta)
=\frac{S_a^2}{n_a}+\frac{S_b^2}{n_b}
-\frac{S_{a-b}^2}{N},
$$

where $S_a^2,S_b^2$ are finite-population potential-outcome variances and $S_{a-b}^2$ is the variance of individual effects. The last quantity is unobserved because only one potential outcome is seen for each unit. Dropping its non-negative term yields the usual conservative variance estimator. Cluster assignment requires cluster-level inference; treating members of a common guarantee group as independent can understate uncertainty.

A first planning approximation for equal-sized arms comparing binary endpoints with common planning rate $p_0$ and detectable difference $\delta$ is

$$
n_{\mathrm{per\ arm}}\approx
\frac{2(z_{1-\alpha/2}+z_{1-\beta})^2p_0(1-p_0)}{\delta^2}.
$$

Here $\alpha$ is the two-sided TypeI error target and $1-\beta$ is power. At 5% significance,80% power, $p_0=0.5$ and $\delta=0.10$, using unrounded normal quantiles, the approximation is 392.44, rounded up to 393 per arm. This is a planning calculation under independent complete follow-up. Unequal allocation, censoring, multiplicity, cluster correlation and sequential stopping require the corresponding design calculation. For equal clusters of size $m$ and exchangeable intracluster correlation $\rho$, the variance inflation $1+(m-1)\rho$ follows by summing the $m$ variances and $m(m-1)$ covariances of the cluster total.

**When an offer is an instrument.** Let $Z$ be a random encouragement to take a fixed contract, $U(z)$ take-up, and $Y(u)$ an outcome defined under receipt and non-receipt. Under random encouragement, exclusion of a direct $Z$ effect, monotonicity $U(1)\ge U(0)$, a non-zero first stage and the relevant consistency/interference conditions,

$$
\frac{E[Y\mid Z=1]-E[Y\mid Z=0]}
{E[U\mid Z=1]-E[U\mid Z=0]}
=E[Y(1)-Y(0)\mid U(1)>U(0)].
$$

To see why, partition applicants into never-takers, always-takers and compliers. Exclusion makes the first two groups' contribution to the assignment effect zero. The numerator is the complier proportion times their average receipt effect; the denominator is the complier proportion. Price and repayment-schedule changes can directly change outcomes even among people who take up both offers, so they require a different causal model unless this exclusion condition is defensible.

*Source connection:* Karlan and Zinman, “Observing Unobservables,” motivates separating randomised contract information, take-up and repayment. The algebra above states the additional conditions for each estimand explicitly.

## A1.4 Adaptive probabilities and the linear-UCB calculation

The linear confidence-bound construction follows [5]; inference under adaptive assignment follows [6].

Let $\widehat\pi_i$ and $q_i$ each be probability distributions on the approved set $\mathcal A(X_i)$. For a registered exploration weight $0\le\epsilon_i\le1$,

$$
\pi_i(a\mid X_i,H_{i-1})
=(1-\epsilon_i)\widehat\pi_i(a\mid X_i,H_{i-1})
+\epsilon_iq_i(a\mid X_i,H_{i-1}).
$$

Non-negativity follows from the component distributions; summing over $a$ gives $(1-\epsilon_i)+\epsilon_i=1$. If $q_i(a)\ge q_{\min}>0$ and $\epsilon_i\ge\epsilon_{\min}>0$ for an eligible action, then $\pi_i(a)\ge\epsilon_{\min}q_{\min}$. With two actions, uniform $q$, $\epsilon=0.2$ and a current best-action point mass, the probabilities become 0.9 and 0.1. The floor applies only after hard eligibility restrictions. The realised final assignment probability must also account for any actual allocation-stage override mechanism; a deterministic human change cannot simply retain the pre-override randomisation probability.

For a linear reward model, use an action-context feature vector $\phi_i(a)\in\mathbb R^d$ and assume

$$
R_i=\phi_i(A_i)^\top\theta+\varepsilon_i,
\qquad E[\varepsilon_i\mid X_i,A_i,H_{i-1}]=0.
$$

For ridge parameter $\lambda>0$, minimise the accumulated squared errors plus $\lambda\|\theta\|^2$. Differentiating and equating to zero gives

$$
\begin{aligned}
B_i&=\lambda I+\sum_{j<i}\phi_j(A_j)\phi_j(A_j)^\top,\\
b_i&=\sum_{j<i}\phi_j(A_j)R_j,\\
\widehat\theta_i&=B_i^{-1}b_i.
\end{aligned}
$$

If a confidence ellipsoid is $\|\theta-\widehat\theta_i\|_{B_i}\le c_i$, the Cauchy–Schwarz inequality gives

$$
\phi^\top\theta
\le\phi^\top\widehat\theta_i
+c_i\sqrt{\phi^\top B_i^{-1}\phi}.
$$

The LinUCB choice maximises that upper bound over permitted actions. Its claimed confidence coverage requires an appropriate $c_i$ and assumptions such as bounded features and conditionally sub-Gaussian reward noise. A generic tuning constant has an exploration interpretation but no automatic safety or coverage guarantee. For an orthogonal two-dimensional example, $B=\operatorname{diag}(4,1)$, $b=(8,1)^\top$, and $c=1$ give $\widehat\theta=(2,1)^\top$. The scores for unit-vector actions are 2.5 and 2.0. Greater uncertainty raises the second action's bonus from 0.5 to 1, while the policy constraints still determine whether either action is available.

**Logistic Thompson sampling.** For a binary event, set $p_\theta(x,a)=\{1+\exp[-\phi(x,a)^\top\theta]\}^{-1}$ and update the specified posterior. Draw $\widetilde\theta_i$ from that posterior and choose

$$
A_i\in\arg\max_{a\in\mathcal A(X_i)}
\widetilde Q_i(X_i,a).
$$

Here $\widetilde Q_i$ combines the sampled event probability with the documented take-up, exposure, severity, timing and cost model. If the event is default, maximising $p_{\widetilde\theta}$ itself would maximise default probability. The allocation probability of Thompson sampling is the posterior probability that an action wins this value comparison, subject to tie rules and eligibility; it is different from the sampled default probability. The shared hierarchy is specified in A2.5; Pólya–Gamma computation and the distinct coefficient and group-scale priors are derived in A2.10–A2.11. A3.6–A3.8 apply those results to selective labels and provide a numerical check. Their sector, region and vintage effects use the same evidence and time-window definitions.

*Source connection:* Li and colleagues, “A Contextual-Bandit Approach to Personalized News Article Recommendation,” develops the linear-UCB approach. Durand and colleagues, “Contextual Bandits for Adaptive Treatment Allocation,” discusses controlled adaptive allocation. Hadad and colleagues, “Confidence Intervals for Policy Evaluation in Adaptive Experiments,” addresses uncertainty under adaptive sampling.

## A1.5 Derive inverse-propensity policy evaluation

The evaluation setting and overlap requirements follow [1], [12].

For a fixed target policy $\pi$ evaluated on the study's context distribution, define

$$
V(\pi)=E_X\left[\sum_a\pi(a\mid X)\mu(X,a)\right].
$$

Assume the observed reward agrees with its assigned potential reward, the action assignment is conditionally exchangeable given recorded context and history, observed outcomes satisfy the declared measurement rule, and $e_i(a)>0$ whenever $\pi(a)>0$. Conditional on $X_i,H_{i-1}$,

$$
\begin{aligned}
E\!\left[\frac{\pi(A_i\mid X_i)}{e_i(A_i\mid X_i,H_{i-1})}R_i
\,\middle|\,X_i,H_{i-1}\right]
&=\sum_a e_i(a)\frac{\pi(a\mid X_i)}{e_i(a)}\mu(X_i,a)\\
&=\sum_a\pi(a\mid X_i)\mu(X_i,a).
\end{aligned}
$$

Averaging and applying iterated expectation proves the IPS identity

$$
\widehat V_{\mathrm{IPS}}(\pi)
=\frac1n\sum_i
\frac{\pi(A_i\mid X_i)}{e_i(A_i\mid X_i,H_{i-1})}R_i.
$$

The proof permits predictable adaptive logging probabilities, but precision calculations must account for that adaptive process. A target policy selected using the same evaluated rewards also needs sample splitting or an analysis that addresses policy selection. When context or reward distributions change with calendar time, the estimator targets the declared mixture of those contexts and times; transport to a different period needs additional assumptions.

For weights $w_i$, the common concentration diagnostic is

$$
n_{\mathrm{eff}}=\frac{(\sum_iw_i)^2}{\sum_iw_i^2}.
$$

It measures weight concentration, not a universal replacement for the actual sampling variance. Clipping $w_i$ to $\min(w_i,c)$ changes the conditional expectation in the proof and generally introduces bias. The self-normalised estimator $\sum_iw_iR_i/\sum_iw_i$ is a ratio estimator; it can be consistent under appropriate conditions but does not inherit exact finite-sample unbiasedness from the IPS sum.

## A1.6 Derive the doubly robust estimator and its remainder

The augmented estimator follows the doubly robust policy-evaluation construction in [1].

Let $\widehat m(x,a)$ be an outcome regression and $\widehat e_i(a)$ a working logging-probability model, fitted without using the evaluated observation's outcome. Define

$$
\psi_i=
\sum_a\pi(a\mid X_i)\widehat m(X_i,a)
+\frac{\pi(A_i\mid X_i)}{\widehat e_i(A_i)}
\{R_i-\widehat m(X_i,A_i)\}.
$$

Taking conditional expectation under the true $e_i$ yields

$$
E[\psi_i\mid X_i,H_{i-1}]
=\sum_a\pi(a)\left[
\widehat m_a+\frac{e_i(a)}{\widehat e_i(a)}(\mu_a-\widehat m_a)
\right].
$$

Subtract the desired conditional value to obtain

$$
E[\psi_i\mid X_i,H_{i-1}]-\sum_a\pi(a)\mu_a
=\sum_a\pi(a)
\left(\frac{e_i(a)}{\widehat e_i(a)}-1\right)
(\mu_a-\widehat m_a).
$$

The remainder vanishes if the logging model is correct or if the outcome regression is correct. This is the double-robustness property. Estimation error, same-sample overfitting, weak overlap and adaptive dependence still affect consistency and uncertainty; cross-fitting and appropriate sequential inference address specific parts of those problems.

**Reproducible four-record example.** Observe actions $(a,b,a,b)$ and rewards $(8,4,6,2)$ under equal 0.5 logging probabilities. Evaluate a policy with probabilities $(0.75,0.25)$. The weights are $(1.5,0.5,1.5,0.5)$, giving

$$
\widehat V_{\mathrm{IPS}}=(12+2+9+1)/4=6,
\qquad n_{\mathrm{eff}}=4^2/5=3.2.
$$

With working regressions $\widehat m_a=6$ and $\widehat m_b=4$, the direct-policy prediction is 5.5 for every record. Weighted residuals are $(3,0,0,-1)$, so

$$
\widehat V_{\mathrm{DR}}=5.5+(3+0+0-1)/4=6.
$$

This small calculation checks arithmetic; it supplies no meaningful empirical precision estimate or policy-performance evidence.

*Source connection:* Dudík, Langford and Li, “Doubly Robust Policy Evaluation and Learning,” and Wang, Agarwal and Dudík, “Optimal and Adaptive Off-Policy Evaluation in Contextual Bandits,” establish the policy-evaluation framework. The expectation proof here shows exactly which assumptions the article invokes.

## A1.7 Delayed outcomes and censoring

Let $M_i=1$ indicate that the complete target-horizon reward is observed by the analysis date, and let $g_i=\Pr(M_i=1\mid X_i,A_i,H_{i-1})$. If outcome observation is conditionally independent of the completed reward given these variables and $g_i>0$, then

$$
E\!\left[\frac{M_iR_i}{g_i}\middle|X_i,A_i,H_{i-1}\right]
=E[R_i\mid X_i,A_i,H_{i-1}].
$$

Combining this observation weight with the action weight gives

$$
\widehat V=\frac{1}{n}\sum_i
\frac{\pi(A_i\mid X_i)}{e_i(A_i\mid X_i,H_{i-1})}
\frac{M_iR_i}{g_i}.
$$

A 0.8 observation probability produces a 1.25 observation weight. If recent loans have zero probability of reaching the twelve-month endpoint by the analysis date, this identity cannot recover their realised twelve-month rewards; use mature cohorts or a clearly labelled forecasting model. If observation depends on unmeasured financial distress, the conditional observation assumption also fails. Early delinquency and final loss belong in a joint, prespecified model if both are used; treating them as independent repeated evidence about the same loan overstates information.

For event data, observe $\widetilde T_i=\min(T_i,C_i)$ and $\delta_i=1\{T_i\le C_i\}$. Under independent right censoring conditional on the model covariates, the event-time likelihood contribution, omitting a separate censoring factor, is

$$
L_i=\lambda_i(\widetilde T_i)^{\delta_i}
\exp\{-\Lambda_i(\widetilde T_i)\},
\qquad
\Lambda_i(t)=\int_0^t\lambda_i(u)\,du.
$$

An observed event contributes its density $\lambda_iS_i$; a censored record contributes survival $S_i$. Censoring does not mean a zero eventual loss. Administrative censoring, informative missingness and competing termination are different mechanisms and receive different treatment.

## A1.8 Hazard, survival and competing-risk incidence

The hazard specification follows [7], with competing-risk and transition distinctions supported by [8], [9].

The event hazard satisfies $\lambda(t)=f(t)/S(t)$, where $S(t)=\Pr(T>t)$ and $f(t)=-S'(t)$. Rearranging gives

$$
\frac{d\log S(t)}{dt}=-\lambda(t),
\qquad
S(t)=\exp\left\{-\int_0^t\lambda(u)\,du\right\}.
$$

For a Cox specification $\lambda(t\mid x,a)=\lambda_0(t)\exp\{x^\top\beta+g(a,x)\}$ with time-constant predictor,

$$
S(t\mid x,a)=\exp\{-\Lambda_0(t)\exp[x^\top\beta+g(a,x)]\}.
$$

The hazard ratio compares instantaneous rates among those still at risk. It is not generally a probability ratio or a causal effect. Time-varying coefficients or proportional-hazards failures require an appropriately extended model.

With mutually exclusive terminal causes $k=1,\ldots,K$, define cause-specific hazard $\lambda_k(t)$ among loans still free of every terminal event. Their sum determines overall survival:

$$
S(t)=\exp\left\{-\int_0^t\sum_k\lambda_k(u)\,du\right\}.
$$

The probability of surviving to just before $u$ and then exiting by cause $k$ in $du$ is $S(u-)\lambda_k(u)du$. Integration derives the cumulative-incidence function:

$$
F_k(\tau)=\Pr(T\le\tau,J=k)
=\int_0^\tau S(u-)\lambda_k(u)\,du,
\qquad
S(\tau)+\sum_kF_k(\tau)=1.
$$

For constant annual hazards $\lambda_D=0.04$ for default and $\lambda_P=0.16$ for prepayment, the one-year default incidence is

$$
F_D(1)=\frac{0.04}{0.20}(1-e^{-0.20})=3.6254\%.
$$

The single-event expression $1-e^{-0.04}=3.9211\%$ describes a different calculation that removes the prepayment hazard. Treating prepayment as a risk-set exit is appropriate when estimating a cause-specific default hazard, but converting that hazard to absolute default incidence requires all competing hazards. This distinction explains the article's warning about treating prepayment as ordinary independent censoring in an absolute-risk calculation.

At event times $t_j$, let $n_j$ be the at-risk count, $d_{kj}$ cause-$k$ events and $d_j=\sum_kd_{kj}$. The competing-risk product-limit construction is

$$
\widehat S(t)=\prod_{t_j\le t}(1-d_j/n_j),
\qquad
\widehat F_k(t)=\sum_{t_j\le t}
\widehat S(t_j-)\frac{d_{kj}}{n_j}.
$$

Independent censoring conditional on the relevant strata and appropriately measured event causes are required. Cure and restructuring may instead be intermediate states. If $Q(t)$ contains transition intensities $q_{rs}(t)$, with $q_{rr}=-\sum_{s\ne r}q_{rs}$, the transition matrix solves

$$
\frac{\partial P(s,t)}{\partial t}=P(s,t)Q(t),
\qquad P(s,s)=I.
$$

The Aalen–Johansen estimator replaces intensity increments by observed transitions per risk set and forms the ordered matrix product

$$
\widehat P(s,t)=\prod_{s<u\le t}(I+d\widehat A(u)).
$$

For transition interpretation under the stated model, the state description must carry enough history for the assumed Markov structure, or the analysis must explicitly extend it. The Fine–Gray subdistribution hazard instead satisfies

$$
\widetilde\lambda_D(t)
=\frac{F_D'(t)}{1-F_D(t)},
\qquad
F_D(t)=1-\exp\left\{-\int_0^t\widetilde\lambda_D(u)\,du\right\}.
$$

Its denominator differs from all-cause event-free survival. Cause-specific Cox and Fine–Gray regression therefore attach coefficients to different quantities. Randomised or otherwise identified offer comparisons remain necessary for causal interpretation of differences between offers.

*Source connection:* Cox, “Regression Models and Life-Tables”; Aalen and Johansen, “An Empirical Transition Matrix for Non-Homogeneous Markov Chains Based on Censored Observations”; and Fine and Gray, “A Proportional Hazards Model for the Subdistribution of a Competing Risk.”

## A1.9 Fairness measures and uncertainty shown to reviewers

The conditional fairness rates follow [13].

Let $G$ denote an evaluation group, $Y=1$ the declared positive outcome and $\widehat Y=1$ the declared positive decision. Then

$$
\operatorname{TPR}_g=\Pr(\widehat Y=1\mid Y=1,G=g),
\qquad
\operatorname{FPR}_g=\Pr(\widehat Y=1\mid Y=0,G=g).
$$

Equal opportunity equates the TPR across groups; equalized odds equates both TPR and FPR. Accuracy also depends on the group's outcome prevalence $p_g$:

$$
\operatorname{Accuracy}_g
=p_g\operatorname{TPR}_g+(1-p_g)(1-\operatorname{FPR}_g).
$$

Therefore equalized odds does not generally imply equal accuracy. The positive label must be explicit: default detection and approval of sustainable repayment use different label conventions. With selective labels, these empirical rates initially describe the observed-outcome population. Weighted or model-based population rates require the corresponding selection assumptions and support.

A posterior credible interval for an identified conditional mean effect and a predictive interval for a future realised outcome answer different questions. For model parameters $\vartheta$, future outcome $Y_{\mathrm{new}}$ and data $D$, the law of total variance gives

$$
\operatorname{Var}(Y_{\mathrm{new}}\mid D)
=E[\operatorname{Var}(Y_{\mathrm{new}}\mid\vartheta,D)\mid D]
+\operatorname{Var}(E[Y_{\mathrm{new}}\mid\vartheta,D]\mid D).
$$

The first term is future outcome variability conditional on the model; the second is posterior parameter uncertainty. For human review, retain expected contribution, the effect or risk credible interval, the predictive cash range and any approved threshold-exceedance probability, each labelled with its horizon and assumptions. These quantities become causal evidence when the underlying comparison is causally identified and the evaluation addresses adaptive assignment, take-up, missingness and support.

*Source connection:* Hardt, Price and Srebro, “Equality of Opportunity in Supervised Learning,” defines the group-rate distinctions. The uncertainty decomposition is an application of iterated conditional expectation and variance.

### Further methodological reading

Additional sources retained from the article bibliography: [20].
