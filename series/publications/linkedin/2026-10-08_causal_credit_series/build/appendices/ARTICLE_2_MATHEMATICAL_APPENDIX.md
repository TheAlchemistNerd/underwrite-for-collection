# Mathematical appendix to Article 2

## A2.1 Indices and model meanings

This appendix derives the mathematical specifications used in Article 2. Let $i$ index a facility, $t$ a decision time, $\tau$ an outcome horizon, $s(i)$ sector, $r(i)$ region and $c(i)$ origination vintage. $D$ is the registered evidence. A policy $\pi$ selects from the permitted action set $\mathcal A_t$. Model label $L$ identifies fixed-horizon logistic parameters; $H$ identifies separate hazard parameters. Normal distributions use mean and variance, Gamma distributions shape and rate. All posterior statements condition on the declared model, data and scenario. A credible interval describes uncertainty about a parameter or expected contrast; a predictive interval also includes future outcome variation.

## A2.2 Bellman recursion

The finite-horizon value recursion is the fully observed special case of the control formulation in [24].

For terminal value $g_T$, stage reward $r_t$, horizon $T$ and per-step discount $\gamma$, policy value is:

$$
V_t^\pi(s)=\mathbb E^\pi\left[
\sum_{j=t}^{T-1}\gamma^{j-t}r_j+\gamma^{T-t}g_T(S_T)
\mid S_t=s\right].
$$

Separate the first reward and apply iterated expectation. Under the Markov assumption, conditioning the continuation on the next state is sufficient:

$$
V_t^\pi(s)=\sum_{a\in\mathcal A_t(s)}\pi_t(a\mid s)
\int\left[r_t(s,a,s')+\gamma V_{t+1}^\pi(s')\right]P_t(ds'\mid s,a).
$$

Maximising at each permitted state gives:

$$
\begin{aligned}
V_t(s)&=\max_{a\in\mathcal A_t(s)}
\int[r_t(s,a,s')+\gamma V_{t+1}(s')]P_t(ds'\mid s,a),\\
V_T(s)&=g_T(s).
\end{aligned}
$$

The action set encodes eligibility and authority. The reward, transition and terminal condition describe one common decision problem. Discounting must match the time unit; irregular intervals require the adjustment below.

## A2.3 POMDP prediction and observation update

The belief-state construction and observation update follow [24].

Let $Z_t$ be latent state, $O_t$ observation, $T_a(z'\mid z)$ the transition law, and $L_a(o\mid z')$ the observation likelihood. The belief conditions on observations and previous actions:

$$
b_t(z)=\Pr(Z_t=z\mid O_{1:t},A_{1:t-1}).
$$

The law of total probability gives a predicted belief; Bayes' rule incorporates the new observation:

$$
\begin{aligned}
\bar b_{t+1}(z')&=\sum_z T_{a_t}(z'\mid z)b_t(z),\\
p(o\mid b_t,a_t)&=\sum_{z'}L_{a_t}(o\mid z')\bar b_{t+1}(z'),\\
b_{t+1}(z')&=
\frac{L_{a_t}(o_{t+1}\mid z')\bar b_{t+1}(z')}
{\sum_{\tilde z}L_{a_t}(o_{t+1}\mid\tilde z)\bar b_{t+1}(\tilde z)}.
\end{aligned}
$$

Replace sums by integrals for continuous state. The denominator must be positive under the model. If $\mathcal B(b,a,o)$ denotes the update and $\bar r(b,a)$ expected stage reward, the belief-space Bellman equation is:

$$
V_t(b)=\max_{a\in\mathcal A_t(b)}
\left\{\bar r(b,a)+\gamma\sum_o p(o\mid b,a)
V_{t+1}(\mathcal B(b,a,o))\right\}.
$$

Information-gathering actions can improve continuation value through a changed belief. Their observation model, cost and permitted data collection are specified. The transition law requires credible action-response evidence.

## A2.4 Semi-Markov timing

Let $U>0$ be time to the next transition, $K(ds',du\mid s,a)$ its joint destination-duration distribution, and $\rho$ a continuous discount rate. If $r(s,a,s',u)$ is the present value of rewards earned before and at that transition, conditioning gives:

$$
V(s)=\max_{a\in\mathcal A(s)}
\int\left[r(s,a,s',u)+e^{-\rho u}V(s')\right]K(ds',du\mid s,a).
$$

Cash received continuously enters $r$ through its discounted integral over $[0,U]$. A finite horizon truncates durations at remaining time and uses a terminal value. Setting $U=1$ and $\gamma=e^{-\rho}$ recovers the discrete recursion. This distinguishes otherwise equal receipts arriving at different dates.

## A2.5 Complete logistic hierarchy

The hierarchical posterior and partial-pooling construction follow [9] (ch. 5).

For a mature default indicator at horizon $\tau$:

$$
\begin{aligned}
D_i(\tau)&\sim\operatorname{Bernoulli}(p_{i,\tau}),\\
p_{i,\tau}&=\frac{e^{\eta_i^L}}{1+e^{\eta_i^L}},\\
\eta_i^L&=\alpha^L+X_i^\mathsf T\beta^L
+u_{s(i)}^L+v_{r(i)}^L+w_{c(i)}^L,\\
\mathcal L_L&=\prod_i p_{i,\tau}^{D_i(\tau)}
(1-p_{i,\tau})^{1-D_i(\tau)}.
\end{aligned}
$$

The same named levels apply separately for $m\in\{L,H\}$:

$$
\begin{aligned}
u_s^m&=\sigma_u^m z_{us}^m,&z_{us}^m&\sim N(0,1),\\
v_r^m&=\sigma_v^m z_{vr}^m,&z_{vr}^m&\sim N(0,1),\\
w_c^m&=\sigma_w^m z_{wc}^m,&z_{wc}^m&\sim N(0,1),\\
\sigma_k^m&\sim\operatorname{HalfStudentT}(3,s_{0,k}^m),
&&k\in\{u,v,w\},\\
\alpha^L&\sim N(0,s_\alpha^2),&\beta^m&\sim N(0,B^m).
\end{aligned}
$$

This baseline assigns Gaussian priors to the signed fixed-effect coefficients $\beta^m$ and half-Student-t priors only to the positive group standard deviations $\sigma_k^m$. A Student-t coefficient prior is a separately declared alternative, defined in A2.11; it is not implied by the half-t group-scale prior. Raw effects are independent in this baseline specification. A dependence prior or identifying constraint is recorded when used. $B^m$ is positive definite. Hyperprior scales are calibrated on the link scale through prior-predictive simulation. Additional institution, product or calendar levels each require their own index and prior. An immature or selectively observed binary label requires a model for observation and selection.

Multiplying likelihood and priors gives the posterior. Sharing a scale distribution allows partial pooling. A Gaussian local approximation illustrates it: if a group estimate $\hat u_s$ has variance $v_s$ and prior $N(0,\sigma_u^2)$, completing the square yields:

$$
\mathbb E[u_s\mid\hat u_s,\sigma_u]
=\frac{\sigma_u^2}{\sigma_u^2+v_s}\hat u_s,\qquad
\operatorname{Var}(u_s\mid\hat u_s,\sigma_u)
=(v_s^{-1}+\sigma_u^{-2})^{-1}.
$$

Large sampling variance produces stronger pooling. The logistic posterior itself uses the Bernoulli likelihood rather than this explanatory approximation.

## A2.6 Hierarchical hazards and their likelihood

The proportional-hazards and partial-likelihood construction follows [25].

The hazard model uses separate coefficients and group effects:

$$
\eta_i^H(t)=X_i(t)^\mathsf T\beta^H
+u_{s(i)}^H+v_{r(i)}^H+w_{c(i)}^H,\qquad
\lambda_i(t)=\lambda_0(t)e^{\eta_i^H(t)}.
$$

Time-varying predictors use information available just before the relevant time. The baseline hazard supplies the intercept role. A Bayesian piecewise-constant baseline can use $\lambda_{0\ell}\sim\operatorname{Gamma}(a_\ell,b_\ell)$ in interval $\ell$. A Cox partial-likelihood fit instead estimates relative effects while leaving baseline estimation to a subsequent step.

A1.8 derives the hazard-to-survival identity, and A1.7 gives the right-censored event contribution. Substituting the hierarchical hazard above gives the likelihood used here.

For $y_i=\min(T_i,C_i)$ and event indicator $\delta_i=1\{T_i\le C_i\}$, conditionally independent censoring allows its likelihood factor to be separated:

$$
\mathcal L_H=\prod_i\lambda_i(y_i)^{\delta_i}
\exp\left[-\int_0^{y_i}\lambda_i(u)du\right].
$$

At an untied event time, condition on one event occurring in risk set $\mathcal R(t_i)$. The common baseline cancels, giving:

$$
\mathcal L_{\rm partial}=
\prod_{i:\delta_i=1}
\frac{e^{\eta_i^H(t_i)}}{\sum_{j\in\mathcal R(t_i)}e^{\eta_j^H(t_i)}}.
$$

Ties require a declared method, and absolute risk needs a baseline estimate. For a piecewise baseline with $d_\ell$ events and adjusted exposure $E_\ell=\sum_i\int_{I_\ell}Y_i(t)e^{\eta_i^H(t)}dt$, its conditional likelihood is proportional to $\lambda_{0\ell}^{d_\ell}e^{-\lambda_{0\ell}E_\ell}$. Consequently:

$$
\lambda_{0\ell}\mid\cdots\sim
\operatorname{Gamma}(a_\ell+d_\ell,b_\ell+E_\ell).
$$

This baseline-rate conjugacy is separate from logistic Pólya–Gamma inference.

These survival and hazard identities hold conditional on the fitted coefficients, frailties and baseline. A posterior survival prediction averages the conditional survival for each draw. For posterior parameter vector $\vartheta$, the calculation is

$$
\overline S_i(t\mid D)=\int\exp[-\Lambda_i(t;\vartheta)]p(\vartheta\mid D)\,d\vartheta
\approx\frac1B\sum_{b=1}^B\exp[-\Lambda_i(t;\vartheta^{(b)})].
$$

In general this differs from $\exp\{-\mathbb E[\Lambda_i(t;\vartheta)\mid D]\}$. By convexity, the former is at least the latter. For a new group, draws also integrate its new group effect; for an observed group they use its conditional posterior. A logistic model fitted independently at several horizons needs a joint horizon specification or an explicitly checked monotonicity restriction to ensure that cumulative default probabilities increase with the horizon. Its group labels alone do not impose that restriction.

For competing terminal causes, each cause retains its own baseline, coefficients and sector, region and vintage effects. A1.8 derives event-free survival, cumulative incidence and probability conservation. For every joint posterior draw, compute those quantities from the complete set of cause-specific hazards before averaging across draws. Default risk is the default cumulative incidence when other terminal exits compete; a single-event model uses one minus survival. Cure followed by re-default uses the intermediate-state transition construction in A1.8. These calculations retain the dependencies represented by the joint posterior.

## A2.7 Expected loss, cash shortfall and capital

The cash-shortfall interpretation follows [1], and the regulatory/internal capital distinction follows [4].

For scenario weight $w_j$, contractual cash $C_t^{\rm contract}$, expected receipt $C_{tj}^{\rm received}$ and accounting discount $d_t$, probability weighting and present-value linearity give:

$$
\operatorname{ECL}=\sum_j w_j\sum_t d_t
(C_t^{\rm contract}-C_{tj}^{\rm received}),\qquad \sum_j w_j=1.
$$

The recognition purpose determines the horizon and scenario set. Twelve-month ECL includes lifetime shortfalls from defaults possible during the next twelve months. For $Z=1\{\text{default}\}\operatorname{EAD}\operatorname{LGD}$, conditioning gives:

$$
\mathbb E[Z]=\operatorname{PD}\,
\mathbb E[\operatorname{EAD}\operatorname{LGD}\mid\text{default}].
$$

Replacing the conditional product expectation by fixed EAD and LGD produces the familiar product approximation. When both vary, conditional covariance matters. Recovery timing and discounting belong in the full cash-loss specification.

For portfolio loss $L$, define $\operatorname{VaR}_\alpha(L)=\inf\{l:\Pr(L\le l)\ge\alpha\}$. Expected shortfall can be defined for general distributions by:

$$
\operatorname{ES}_\alpha(L)=
\frac1{1-\alpha}\int_\alpha^1\operatorname{VaR}_u(L)\,du.
$$

Internal capital may subtract $\mathbb E[L]$ from either declared tail measure. RAROC divides a consistently defined risk-adjusted income numerator by allocated economic capital. Each cost appears once. The article's illustration gives $1100-250=850$ and $850/5000=17\%$; a complete RAROC still specifies funding, expected loss, tax and capital allocation.

## A2.8 Constraints and fairness

The conditional fairness rates follow [2].

Let $J(\pi)=\mathbb E^\pi[\sum_t\gamma^tr_t]$ and $C_k(\pi)=\mathbb E^\pi[\sum_t c_{kt}]$. Maximisation is subject to $C_k(\pi)\le B_k$ and permitted actions. Nonnegative multipliers give:

$$
\mathcal L(\pi,\lambda)=J(\pi)
-\sum_k\lambda_k\{C_k(\pi)-B_k\},\qquad\lambda_k\ge0.
$$

This assists optimisation of expectation constraints; feasibility is checked against the original problem. Hard eligibility remains in the action set. Strong duality requires further conditions.

A1.9 defines the group true-positive and false-positive rates and their outcome conventions. Those definitions apply here at the registered decision time, population and horizon. The policy may add a selection-rate ratio:

$$
s_g=\Pr(\widehat Y=1\mid G=g),\qquad
\operatorname{SelectionRatio}_{g,g_0}=s_g/s_{g_0},\quad s_{g_0}>0.
$$

The positive decision and comparison group are declared with the rule. A zero denominator requires a defined review route. Each fairness constraint states whether it applies to a single decision, a cohort or a trajectory; sequential action histories and selective observation determine its estimation and uncertainty. The legal and model-validation process approves the evaluation population, lawful data basis and thresholds.

## A2.9 Clayton copula

The dependence construction follows [3].

For uniform marginals and $\theta>0$:

$$
C_\theta(u,v)=(u^{-\theta}+v^{-\theta}-1)^{-1/\theta}.
$$

Setting $u=v=q$ yields the lower-tail coefficient:

$$
\lambda_L=\lim_{q\downarrow0}\frac{C(q,q)}q
=\lim_{q\downarrow0}(2-q^\theta)^{-1/\theta}
=2^{-1/\theta}.
$$

Near one, $C(q,q)=1-2(1-q)+o(1-q)$, so $\lambda_U=\lim_{q\uparrow1}\{1-2q+C(q,q)\}/(1-q)=0$. The Archimedean generator $\varphi(u)=(u^{-\theta}-1)/\theta$ gives Kendall's tau:

$$
\begin{aligned}
\tau&=1+4\int_0^1\frac{\varphi(u)}{\varphi'(u)}du\\
&=1-\frac4\theta\left(\frac12-\frac1{\theta+2}\right)
=\frac\theta{\theta+2}.
\end{aligned}
$$

Variable orientation determines the economic meaning of the lower tail. The copula parameter is estimated separately from a hierarchy-scale prior's degrees of freedom.

## A2.10 Pólya–Gamma derivation

The augmentation identity and conditional Gaussian calculation follow [5].

For binomial trials $b_i$, successes $y_i$, logit $\eta_i$ and $\kappa_i=y_i-b_i/2$, the augmentation identity is:

$$
\frac{e^{y_i\eta_i}}{(1+e^{\eta_i})^{b_i}}
=2^{-b_i}e^{\kappa_i\eta_i}
\int_0^\infty e^{-\omega_i\eta_i^2/2}
p_{\operatorname{PG}(b_i,0)}(\omega_i)d\omega_i.
$$

Exponential tilting gives $\omega_i\mid\eta_i\sim\operatorname{PG}(b_i,\eta_i)$; Bernoulli data use $b_i=1$. Let $Z$ be the expanded logistic design, including all sector, region and vintage indicators, and $\theta$ its stacked coefficients. Given scales, use $\theta\sim N(m_0,V_0)$ and $\Omega=\operatorname{diag}(\omega_i)$. Multiplying likelihood kernel and prior gives:

$$
\log p(\theta\mid\cdots)=
-\tfrac12\theta^\mathsf T(Z^\mathsf T\Omega Z+V_0^{-1})\theta
+\theta^\mathsf T(Z^\mathsf T\kappa+V_0^{-1}m_0)+\text{constant}.
$$

Complete the square:

$$
\begin{aligned}
V_*&=(Z^\mathsf T\Omega Z+V_0^{-1})^{-1},\\
m_*&=V_*(Z^\mathsf T\kappa+V_0^{-1}m_0),\\
\theta\mid\omega,\text{scales},D&\sim N(m_*,V_*).
\end{aligned}
$$

Scales, correlations, smoothing parameters and latent variables receive their own validated updates. Sharing the same named hierarchy does not change the hazard likelihood into this logistic likelihood.

When updating one coefficient block, retain the other predictor components as an offset $c$: $\eta=Z\theta+c$. The Gaussian precision stays $Z^{\mathsf T}\Omega Z+V_0^{-1}$, while its information vector becomes $Z^{\mathsf T}(\kappa-\Omega c)+V_0^{-1}m_0$. A sum-to-zero constraint can be implemented through a full-column-rank basis for the constrained effects; the design and Gaussian covariance are then expressed in that basis. For computation, factor the precision and solve linear systems instead of explicitly calculating its inverse. This retains the same distribution while making the numerical operations and residual checks explicit. The prior block is Gaussian in the baseline hierarchy of A2.5. If independent Student-t coefficient priors are registered instead, condition on their coefficient-specific mixing precisions from A2.11 and replace only those coefficients' prior-precision entries; the half-t group-scale updates remain separate.

## A2.11 Student-t coefficient priors and half-t group-scale updates

The half-t scale prior follows [6], its normal–Gamma representation follows [7], and the inverse-Gamma auxiliary representation follows [8] (Result 5). This subsection keeps two distinct prior roles explicit. The baseline in A2.5 uses Gaussian fixed-effect coefficients and half-Student-t priors on positive group standard deviations. A Student-t prior on a signed coefficient is an optional, separately registered sensitivity model.

**Student-t prior for a signed regression coefficient.** For coefficient $\beta_j$ and scale $s_{\beta j}>0$:

$$
\begin{aligned}
\lambda_{\beta j}&\sim\operatorname{Gamma}(\nu/2,\nu/2),\qquad
\beta_j\mid\lambda_{\beta j}\sim N(0,s_{\beta j}^2/\lambda_{\beta j}),\\
p(\beta_j)&=\frac{\Gamma((\nu+1)/2)}{\Gamma(\nu/2)\sqrt{\nu\pi}\,s_{\beta j}}
\left(1+\frac{\beta_j^2}{\nu s_{\beta j}^2}\right)^{-(\nu+1)/2},\\
\lambda_{\beta j}\mid\beta_j&\sim\operatorname{Gamma}\left(
\frac{\nu+1}{2},\frac{\nu+\beta_j^2/s_{\beta j}^2}{2}\right).
\end{aligned}
$$

Here Gamma is parameterised by shape and rate. Each $\lambda_{\beta j}$ belongs to its own coefficient. Conditional on these latent precisions, the Pólya–Gamma coefficient block remains Gaussian: in A2.10, the corresponding coefficient-prior precision entries become $\lambda_{\beta j}/s_{\beta j}^2$. This alternative changes the fixed-effect prior and must be named and validated as such. It does not follow from assigning a half-t prior to $\sigma_k$.

**Half-Student-t prior for a positive group standard deviation.** For one hierarchy level with standard deviation $\sigma_k>0$ and prior scale $s_{0,k}>0$, let a signed auxiliary variable have the normal–Gamma mixture and set its absolute value to the group scale:

$$
\lambda_{\sigma k}\sim\operatorname{Gamma}(\nu/2,\nu/2),\qquad
\widetilde{\sigma}_k\mid\lambda_{\sigma k}\sim N(0,s_{0,k}^2/\lambda_{\sigma k}),\qquad
\sigma_k=|\widetilde{\sigma}_k|.
$$

Integrating out $\lambda_{\sigma k}$ gives the half-Student-t density

$$
p(\sigma_k)=\frac{2\Gamma((\nu+1)/2)}{\Gamma(\nu/2)\sqrt{\nu\pi}\,s_{0,k}}
\left(1+\frac{\sigma_k^2}{\nu s_{0,k}^2}\right)^{-(\nu+1)/2},\qquad\sigma_k>0.
$$

For $\nu=3$, this reduces to

$$
p(\sigma_k)=\frac{4}{\pi\sqrt{3}\,s_{0,k}}
\left(1+\frac{\sigma_k^2}{3s_{0,k}^2}\right)^{-2},\qquad\sigma_k>0.
$$

The Gamma shape and rate are both $3/2$ when $\nu=3$. The scale $\sigma_k$ controls pooling of the distinct, conditionally Gaussian group effects, for example $u_{ks}\mid\sigma_k\sim N(0,\sigma_k^2)$. It is positive and is not a signed regression coefficient. The mixing precision $\lambda_{\sigma k}$ is specific to this group-scale representation; it is not any of the coefficient-specific $\lambda_{\beta j}$ values.

Conditioning on the positive scale gives the mixture update

$$
\lambda_{\sigma k}\mid\sigma_k\sim\operatorname{Gamma}\left(
\frac{\nu+1}{2},\frac{\nu+\sigma_k^2/s_{0,k}^2}{2}\right).
$$

For a direct update of $\sigma_k$ given centred effects $u_{ks}$ and $\lambda_{\sigma k}$, the log kernel includes both the Gaussian effects' normalising factor and the scale mixture:

$$
\log p(\sigma_k\mid u,\lambda_{\sigma k})
=-J_k\log\sigma_k-\frac{\sum_s u_{ks}^2}{2\sigma_k^2}
-\frac{\lambda_{\sigma k}\sigma_k^2}{2s_{0,k}^2}+\text{constant},\qquad\sigma_k>0.
$$

This is not the same update as $\lambda_{\sigma k}\mid\sigma_k$, and the normal–Gamma representation alone does not give a Gaussian full conditional for the group standard deviation.

**Centered inverse-Gamma auxiliary update for the half-t scale.** Define $\operatorname{IG}(a,b)$ by density proportional to $x^{-a-1}\exp(-b/x)$, with shape $a$ and scale parameter $b$. An alternative representation of the same half-Student-t prior is

$$
\sigma_k^2\mid a_k\sim\operatorname{IG}(\nu/2,\nu/a_k),\qquad
a_k\sim\operatorname{IG}(1/2,1/s_{0,k}^2).
$$

Integrating over $a_k$ gives $p(\sigma_k^2)\propto(\sigma_k^2)^{-1/2}(\sigma_k^2+\nu s_{0,k}^2)^{-(\nu+1)/2}$. Applying the Jacobian $2\sigma_k$ recovers the half-t density above. For $J_k$ independent centred effects $u_{ks}\mid\sigma_k\sim N(0,\sigma_k^2)$, the Gibbs conditionals are

$$
\begin{aligned}
\sigma_k^2\mid a_k,u&\sim\operatorname{IG}\left(
\frac{\nu+J_k}{2},\frac{\nu}{a_k}+\frac12\sum_s u_{ks}^2\right),\\
a_k\mid\sigma_k^2&\sim\operatorname{IG}\left(
\frac{\nu+1}{2},\frac{\nu}{\sigma_k^2}+\frac1{s_{0,k}^2}\right).
\end{aligned}
$$

These inverse-Gamma updates apply to centred effects. With non-centred effects $u=\sigma_k z$, holding $z$ fixed changes the conditional. For a group contribution $\sigma_k v$, where $v=Z_gz$ and $\eta=c+\sigma_kv$, the augmented logistic likelihood contributes

$$
p(\sigma_k\mid z,\omega,\ldots)\propto
\mathbf1\{\sigma_k>0\}
\exp\left[-\frac{\sigma_k^2}{2}v^{\mathsf T}\Omega v
+\sigma_kv^{\mathsf T}(\kappa-\Omega c)\right]p(\sigma_k).
$$

Conditioning on the normal–Gamma scale auxiliary variable gives an explicit non-centred block. Define

$$
q_{\sigma k}=v^{\mathsf T}\Omega v+\lambda_{\sigma k}/s_{0,k}^2,
\qquad m_{\sigma k}=q_{\sigma k}^{-1}v^{\mathsf T}(\kappa-\Omega c).
$$

Completing the square yields

$$
\sigma_k\mid z,\omega,\lambda_{\sigma k},D
\sim N(m_{\sigma k},q_{\sigma k}^{-1})\ \text{truncated to }(0,\infty).
$$

This block holds raw non-centred effects $z$ fixed. The centred inverse-Gamma block holds realised effects $u$ fixed. The two auxiliary constructions are alternative implementations of the declared prior; each sampler follows its own consistent conditioning scheme. Integrating Gaussian group effects over a shared half-t standard deviation gives a different mixture from independent Student-t priors on signed fixed coefficients.

Here $p(\sigma_k)$ is the declared half-t scale prior (or its correctly conditioned auxiliary form). A centred inverse-Gamma update cannot be reused while holding $z$ fixed. Use validated centred Gibbs blocks, a correctly derived non-centred method, or an explicitly derived interweaving scheme. Compare convergence, effective sample size and effective sample size per elapsed second under the registered workload. Across all representations, coefficient-prior and group-scale-prior families, scales and parameterisations are recorded independently; conditional conjugacy applies to the stated blocks while the marginal posterior remains a mixture.

## A2.12 Limit boundary and human-review uncertainty

The expected-utility comparison follows [9] (ch. 9). The declared payoff matrix determines the economic threshold.

Let $\bar p=\mathbb E[p\mid D]$, repayment gain $G\ge0$, default loss $L>0$ and separately defined denial cost $O\ge0$. Linearity of expectation for fixed payoffs gives:

$$
\begin{aligned}
\mathbb E[V_1\mid D]&=(1-\bar p)G-\bar pL,\\
\mathbb E[V_0\mid D]&=-(1-\bar p)O,\\
\mathbb E[V_1-V_0\mid D]&=(G+O)-\bar p(G+O+L).
\end{aligned}
$$

Set the final expression to zero:

$$
p^*=\frac{G+O}{G+O+L}.
$$

For $G=1200$, $O=0$, $L=18800$, the threshold is $6\%$. At $\bar p=4\%$, expected extension value is $0.96(1200)-0.04(18800)=400$ KES.

This boundary compares one specified extension with its stated alternative, under linear monetary utility and fixed payoffs. The repayment probability concerns that extension's outcome; the denial cost is incurred in the counterfactual repayment state of the same extension. For a limit increase on an existing facility, measure changes in value relative to keeping the current limit, preserving the existing balance and expected recoveries in both alternatives. If the action changes utilisation, default risk, repayment timing, servicing cost or recovery, calculate the full action-specific posterior value rather than substituting its risk into a fixed-payoff threshold:

$$
a^*=\arg\max_{a\in\mathcal A^{\rm permitted}}
\int\!\int U(v,a)\,p(v\mid\vartheta,D,a)
p(\vartheta\mid D)\,dv\,d\vartheta.
$$

For linear $U(v,a)=v$ the comparison uses expected value; nonlinear utility requires the value distribution. The cap-exceedance gate below is a separately approved constraint, so it can route a case to review even when its mean-based financial comparison is favourable.

Posterior draws give the cap-exceedance estimate:

$$
\hat q_{\rm cap}=\frac1B\sum_{b=1}^B
1\{p^{(b)}>p_{\rm cap}\}.
$$

Compare it with the approved $\epsilon$ to select a review route. Monte Carlo precision depends on effective sample size. If utilisation, gain or recovery is uncertain, preserve dependence through joint draws and compute $\Delta^{(b)}=V_1^{(b)}-V_0^{(b)}$. Quantiles supply its credible interval and $B^{-1}\sum_b1\{\Delta^{(b)}>\delta\}$ estimates probability of worthwhile benefit. A causal $\Delta$ is a declared conditional or population-average potential-outcome contrast under an identified design. Separate action intervals do not determine uncertainty in their difference:

$$
\operatorname{Var}(V_1-V_0)=
\operatorname{Var}(V_1)+\operatorname{Var}(V_0)
-2\operatorname{Cov}(V_1,V_0).
$$

For posterior uncertainty about two expected action values, paired draws from the same fitted model preserve their shared parameter uncertainty in this calculation. A variance for the realised individual treatment effect $Y(1)-Y(0)$ is a different target: a standard parallel-arm trial identifies the marginal outcome distributions but does not observe both outcomes for the same person. Its cross-potential-outcome covariance requires additional assumptions or bounds. The reported credible interval should therefore name its mean-effect or policy-value estimand.

Future cash prediction integrates both parameter and outcome variation:

$$
p(C\mid D,a)=\int p(C\mid\theta,a)p(\theta\mid D)d\theta.
$$

The law of total variance decomposes predictive variance into $\mathbb E[\operatorname{Var}(C\mid\theta,a)\mid D]+\operatorname{Var}(\mathbb E[C\mid\theta,a]\mid D)$. This distinguishes the PD parameter interval, causal-contrast interval and predictive cash interval on the reviewer screen.

## A2.13 Linear UCB and logistic Thompson sampling

A1.4 derives the ridge estimate, confidence ellipsoid and Linear UCB action score. That construction supplies the linear benchmark here. For hierarchical logistic Thompson sampling, draw the full expanded coefficient vector:

$$
\tilde\theta_t\sim p(\theta\mid D_t),\qquad
\tilde p_t(a)=\{1+e^{-z_t(a)^\mathsf T\tilde\theta_t}\}^{-1},
\qquad a_t=\arg\max_{a\in\mathcal A_{{\rm safe},t}}\tilde Q_t(a).
$$

The design includes the named group levels; $z_t(a)$ here denotes that expanded row, separately from non-centred raw effects. The sampled binary probability enters a defined cash-and-cost value. The appropriate objective depends on whether the event means repayment, default or another outcome.

## A2.14 MCTS and graph explanations

Given a first action, a declared subsequent rollout policy and simulator:

$$
Q_H(s,a)=\mathbb E\left[\sum_{k=0}^H\gamma^kr_{t+k}
\mid S_t=s,a_t=a,\text{rollout policy and model}\right].
$$

A sample mean of simulated returns estimates this expectation. UCT allocates additional search visits through:

$$
U(s,a)=\hat Q(s,a)+c\sqrt{\frac{\log N(s)}{N(s,a)}}.
$$

Unvisited permitted actions are initialised before division by their visit count. Search allocation is computational; model error is assessed independently against observed outcomes.

Here $H$ is the last reward offset, so the displayed sum includes $H+1$ rewards. A specified terminal value adds $\gamma^{H+1}g(S_{t+H+1})$. If the application defines a horizon as $H$ decisions instead, use offsets $0,\ldots,H-1$ and terminal factor $\gamma^H$. Under partial observation, the search node is a belief or a retained history, and simulated observations update it through A2.3. The UCT constant $c$ is scaled to the return units; scaling a cash reward without updating $c$ changes the exploration trade-off.

For an explanation with $M$ players and coalition value $v(S)$, the Shapley attribution is:

$$
\phi_j=\sum_{S\subseteq\{1,\ldots,M\}\setminus\{j\}}
\frac{|S|!(M-|S|-1)!}{M!}
[v(S\cup\{j\})-v(S)].
$$

The weight counts permutations whose predecessors of $j$ are exactly $S$, divided by all $M!$ permutations. Averaging marginal contributions gives this formula. GraphSVX approximates attribution under its feature/graph and perturbation convention. It explains the selected prediction target; MCTS evaluates a defined action path.

For each ordering, the sum of players' successive contributions telescopes to $v(\{1,\ldots,M\})-v(\varnothing)$. Averaging proves the efficiency identity $\sum_j\phi_j=v(\{1,\ldots,M\})-v(\varnothing)$. A graph-explanation method can also use tree search to identify explanatory subgraphs, but that search space and coalition value differ from the controller's permitted action trajectories and economic return. Neither attribution construction supplies a causal intervention effect without the separate identification assumptions.

## A2.15 Off-policy evaluation and pilot arithmetic

A1.5–A1.6 derive the one-step importance-weight identity and doubly robust estimator. Their consistency, exchangeability and support conditions apply at each sequential decision. This subsection extends that evaluation to full action histories.

For trajectories, define $\rho_t=\prod_{j=0}^t\pi(A_j\mid H_j)/e(A_j\mid H_j)$ and $\hat V_t(H_t)=\sum_a\pi(a\mid H_t)\hat Q_t(H_t,a)$. A sequential doubly robust score is:

$$
\hat V_0(H_0)+\sum_{t=0}^{T-1}\gamma^t\rho_t
[R_t+\gamma\hat V_{t+1}(H_{t+1})-\hat Q_t(H_t,A_t)],
\qquad\hat V_T=0.
$$

Correct sequential weights convert each term to the target-policy distribution; the fitted continuation terms telescope under iterated expectation. Exchangeability and overlap are required at each decision. Weight truncation alters the estimator and its bias–variance trade-off.

In the illustrative 100-case pilot, each arm contains 50 cases. Day-60 rates are $38/50=0.76$ and $46/50=0.92$, a difference of 16 percentage points. Day-90 sustained rates are $34/50=0.68$ and $41/50=0.82$, a difference of 14 percentage points. Count differences of eight and seven are distinct from those rate differences. The net-cash calculation is $1100-250=850$ KES per assigned case. These are arithmetic checks on hypothetical inputs; empirical conclusions require observed data and the registered analysis.

## A2.16 Sources and implementation status

Each subsection identifies its methodological sources in Article 2's reference list. The auxiliary half-t representation above is checked by direct integration under the stated inverse-Gamma convention. The appendix expands the article's mathematical specification; fitted diagnostics, local treatment effects and deployed-system evidence are separate validation deliverables.

### Further methodological reading

Additional sources retained from the article bibliography: [26].
