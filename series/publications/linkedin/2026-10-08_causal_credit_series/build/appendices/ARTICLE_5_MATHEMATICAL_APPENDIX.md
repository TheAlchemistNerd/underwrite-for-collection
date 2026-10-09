# Mathematical appendix to Article 5

## A5.1 Three probability statements with separate meanings

Let $D$ denote the registered evidence; $a$ a candidate action; and $a_0$ a comparison action. The article uses

$$
q_p=\Pr\{p_{12}(a)>p_{\max}\mid D\},
$$

$$
q_\Delta=\Pr\{\Delta(a,a_0)>\delta\mid D,\mathcal I\},
$$

$$
q_C=\Pr\{C_{30}(a)<B_{30}\mid D,a\}.
$$

Here $p_{12}(a)$ is a modelled twelve-month default probability, $p_{\max}$ its approved threshold, $\Delta(a,a_0)$ an identified incremental outcome for a defined population, $\delta$ the minimum worthwhile benefit, and $\mathcal I$ the identification assumptions. $C_{30}(a)$ is future available cash over thirty days and $B_{30}$ the required amount on the same basis. Probabilities and $p_{\max}$ are dimensionless; cash, $B_{30}$ and a cash-valued $\Delta$ are in KES.

The first probability integrates over uncertainty about a default-risk parameter; the second over uncertainty about a causal estimand under its identification assumptions; the third over a predictive distribution of future cash. Their respective acceptance thresholds have separate purposes and approval routes.

Action notation records the decision being evaluated. A fitted conditional risk $\Pr(D_{12}=1\mid X,A=a)$ becomes an intervention risk $\Pr(D_{12}(a)=1\mid X)$ only when its data and design justify that interpretation. The same distinction applies to a cash forecast under a changed action. The reviewer receives the prediction target, population and identification assumptions beside the numerical summaries, so an observed association is not silently promoted to an action effect.

## A5.2 Derive the Beta posterior illustration

The conjugate beta–binomial calculation follows [7], ch. 2.

For a deliberately simple Bernoulli model, suppose $n$ conditionally independent observations contain $d$ defaults under one specified outcome definition, with default probability $p$. A Beta prior and binomial likelihood have kernels

$$
\pi(p)\propto p^{\alpha_0-1}(1-p)^{\beta_0-1},
\qquad
L(p;D)\propto p^d(1-p)^{n-d}.
$$

Multiplying and collecting powers gives

$$
p\mid D\sim\operatorname{Beta}(\alpha_0+d,\beta_0+n-d).
$$

For example, $\alpha_0=\beta_0=1$, $n=98$ and $d=3$ produce Beta$(4,96)$. This is an algebraic construction of the article’s illustrative posterior, not a claim that its hypothetical borrower was estimated from those observations. A fitted hierarchical, action-dependent borrower model would generate its own posterior risk distribution.

With $\alpha=4$, $\beta=96$,

$$
\mathbb E[p\mid D]=\frac{\alpha}{\alpha+\beta}=0.04,
$$

$$
\operatorname{Var}(p\mid D)
=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}
=\frac{384}{1{,}010{,}000}\approx0.000380198.
$$

Let $F(x)=I_x(4,96)$ be the regularised incomplete-beta cumulative distribution,

$$
I_x(\alpha,\beta)
=\frac{\int_0^x u^{\alpha-1}(1-u)^{\beta-1}\,du}
{\operatorname B(\alpha,\beta)},\qquad
\operatorname B(\alpha,\beta)
=\int_0^1u^{\alpha-1}(1-u)^{\beta-1}\,du.
$$

The central 95% credible interval uses the 2.5% and 97.5% quantiles:

$$
[F^{-1}(0.025),F^{-1}(0.975)]
=[0.0111167488,0.0860112643].
$$

Thus the displayed interval is approximately 1.11%–8.60%. The exceedance probability at 6% is

$$
q_p=1-I_{0.06}(4,96)=0.1483731733\approx14.84\%.
$$

For integer $\alpha,\beta$, the result can be reproduced without a special-function library using

$$
1-I_x(\alpha,\beta)
=\sum_{k=0}^{\alpha-1}
\binom{\alpha+\beta-1}{k}
x^k(1-x)^{\alpha+\beta-1-k}.
$$

Substituting $(\alpha,\beta)=(4,96)$ gives a four-term sum with binomial size 99. Quantiles can be computed by bisection on $F(x)$ over $[0,1]$. The credible interval is a posterior probability statement conditional on the model and evidence; predictive calibration and sensitivity remain separate validation tasks.

## A5.3 Derive the incremental-benefit illustration

Define a population-average cash effect

$$
\Delta(a,a_0)
=\mathbb E\left[Y(a)-Y(a_0)\mid\mathcal P\right],
$$

where $Y(a)$ is the stated ninety-day net-cash outcome under action $a$ and $\mathcal P$ the eligible population. Treatment costs are included consistently. Randomisation or a justified observational design, consistency, appropriate interference treatment, overlap and valid outcome measurement support its causal interpretation. Hierarchical priors can stabilise estimation within that design.

The article specifies a constructed posterior

$$
\Delta\mid D,\mathcal I\sim
\mathcal N(\mu_\Delta,\sigma_\Delta^2),
\qquad \mu_\Delta=8{,}000,\quad\sigma_\Delta=4{,}000\ \mathrm{KES}.
$$

If $Z=(\Delta-\mu_\Delta)/\sigma_\Delta$, then $Z\sim\mathcal N(0,1)$. Writing $\Phi$ for its cumulative distribution and using $\Phi^{-1}(0.95)=1.6448536269$, the central 90% interval is

$$
\begin{aligned}
\mu_\Delta\pm1.6448536269\sigma_\Delta
&=8{,}000\pm6{,}579.4145\\
&=[1{,}420.5855,14{,}579.4145]\ \mathrm{KES}.
\end{aligned}
$$

For minimum benefit $\delta$,

$$
q_\Delta=1-\Phi\left(\frac{\delta-8{,}000}{4{,}000}\right).
$$

At $\delta=0$, $q_\Delta=\Phi(2)=0.9772498681$, or approximately 97.72%. This is uncertainty about the defined average effect. An individual customer’s realised gain additionally depends on outcome variation and effect heterogeneity, so the same interval is not an individual-outcome forecast.

## A5.4 Derive the available-cash mixture

Article 5 constructs the predictive mass function

$$
\Pr(C=20{,}000)=0.30,\quad
\Pr(C=100{,}000)=0.50,\quad
\Pr(C=180{,}000)=0.20,
$$

where $C=C_{30}(a)$ is available cash in KES under the specified action. The probabilities sum to one. The predictive mean is

$$
\mathbb E[C]
=0.30(20{,}000)+0.50(100{,}000)+0.20(180{,}000)
=92{,}000\ \mathrm{KES}.
$$

The second moment and variance are

$$
\mathbb E[C^2]=11{,}600{,}000{,}000\ \mathrm{KES}^2,
$$

$$
\operatorname{Var}(C)
=\mathbb E[C^2]-\mathbb E[C]^2
=3{,}136{,}000{,}000\ \mathrm{KES}^2,
$$

giving standard deviation KES 56,000. For obligations $B_{30}=70{,}000$ KES, only the low-cash outcome is below the requirement, hence

$$
q_C=\Pr(C<70{,}000)=0.30.
$$

The expected shortfall amount relative to these obligations is

$$
\mathbb E[(70{,}000-C)_+]
=0.30(50{,}000)=15{,}000\ \mathrm{KES},
$$

where $(x)_+=\max(x,0)$. This obligation-shortfall measure has a different definition from a tail-risk measure also called expected shortfall in market-risk applications.

For a full fitted model with uncertain parameters $\theta$, future-shock distribution $p(C\mid\theta,D,a)$ and posterior $p(\theta\mid D)$,

$$
p(C\mid D,a)
=\int p(C\mid\theta,D,a)p(\theta\mid D)\,d\theta.
$$

The law of total variance separates process variation from parameter uncertainty:

$$
\operatorname{Var}(C\mid D,a)
=\mathbb E_{\theta\mid D}[\operatorname{Var}(C\mid\theta,D,a)]
+\operatorname{Var}_{\theta\mid D}[\mathbb E(C\mid\theta,D,a)].
$$

Thus a credible interval about a risk parameter and a predictive cash interval describe different distributions even when they are generated from the same posterior fit.

## A5.5 Limit-review logic and units

The expected-payoff and uncertainty-review distinction follows the decision-analysis framework in [7], ch. 9.

The example starts with limit $L=500{,}000$ KES and drawn principal $U=300{,}000$ KES. Existing undrawn headroom is $L-U=200{,}000$ KES. Increasing the limit by KES 100,000 would make $L'=600{,}000$ and undrawn headroom KES 300,000, before any new drawing. Cash disbursement changes only when a drawing is executed.

For an illustrative review tolerance $\epsilon_p=0.10$, the model criterion is

$$
\Pr\{p_{12}(a)>0.06\mid D\}\le0.10.
$$

The computed value $0.148373>0.10$ does not meet this route’s criterion, so the case follows the specified additional-evidence or higher-authority path. This is a rule for handling posterior uncertainty, not a realised-default guarantee. A separate support action can still be considered through its own eligibility and benefit review.

For a continuous strictly increasing posterior cumulative distribution $F_p$, the gate is equivalent to $F_p(p_{\max})\ge1-\epsilon_p$, or $F_p^{-1}(1-\epsilon_p)\le p_{\max}$. It therefore compares an upper posterior quantile with the approved cap. By contrast, the fixed-payoff financial comparison in Article 2 uses $\mathbb E[p\mid D]$: with repayment gain KES 1,200 and default loss KES 18,800, its threshold is $1200/(1200+18800)=6\%$ and the expected value at posterior mean 4% is KES 400. A favourable expected value and a failed uncertainty gate can coexist because they answer separate decision questions. Limit changes use incremental action values relative to the existing facility, with uncertain utilisation and recovery retained in joint posterior draws.

A schematic permissible-action set is

$$
\mathcal A^{\mathrm{review}}(D)
=\left\{a:\ G_k(D,a)=1\ \forall k,
\quad q_p(D,a)\le\epsilon_p\right\},
$$

where $G_k$ are the applicable contractual, affordability, conduct, mandate and data-quality gates for that action. Additional benefit or cash-risk criteria can be specified separately. Their thresholds are approved policy inputs. Where evidence is insufficient, the permitted response can be information gathering, deferral or another authorised action.

## A5.6 Conditional Gaussian computation and Student-t hierarchy

The logistic augmentation follows [3]; the auxiliary half-t representation follows [10], Result 5.

A registered fixed-horizon model can carry the explicit sector, region and vintage hierarchy

$$
\operatorname{logit}(p_{i,\tau})=\alpha^L+\boldsymbol x_i^{\mathsf T}\boldsymbol\beta^L
+u^L_{s(i)}+v^L_{r(i)}+w^L_{c(i)},
$$

where $s(i),r(i),c(i)$ map observation $i$ to sector, region and origination vintage, $\tau$ is the default horizon, and $L$ labels the logistic model. A proportional-hazard model has separate parameters labelled $H$:

$$
\eta_i^H(t)=\boldsymbol x_i(t)^\mathsf T\boldsymbol\beta^H
+u^H_{s(i)}+v^H_{r(i)}+w^H_{c(i)},\qquad
\lambda_i(t)=\lambda_0(t)e^{\eta_i^H(t)}.
$$

The baseline $\lambda_0(t)$ has inverse-time units and supplies the hazard intercept. For each model $m\in\{L,H\}$, the common hierarchy representation is

$$
\begin{aligned}
u_s^m&=\sigma_u^m z_{us}^m,&z_{us}^m&\sim N(0,1),\\
v_r^m&=\sigma_v^m z_{vr}^m,&z_{vr}^m&\sim N(0,1),\\
w_c^m&=\sigma_w^m z_{wc}^m,&z_{wc}^m&\sim N(0,1),\\
\sigma_k^m&\sim\operatorname{HalfStudentT}(3,s_{0,k}^m),
&&k\in\{u,v,w\},\\
\alpha^L&\sim N(0,s_\alpha^2),&
\boldsymbol\beta^m&\sim N(\boldsymbol0,B^m).
\end{aligned}
$$

The $z$ variables are independent standard-normal raw effects under this specification; each positive $\sigma$ is a group-variation scale. The constants $s_{0,k}^m$ and $s_\alpha$ are calibrated prior scales, and $B^m$ is a positive-definite fixed-coefficient covariance. A Bayesian piecewise baseline can use $\lambda_{0\ell}\sim\operatorname{Gamma}(a_\ell,b_\ell)$ for interval $\ell$, with positive declared shape and rate. The fixed-horizon outcome and hazard retain their own likelihood and parameter values.

For a mature binary label $y_i=D_i(\tau)$, the logistic likelihood is $\prod_i p_{i,\tau}^{y_i}(1-p_{i,\tau})^{1-y_i}$. For event time $t_i$ and censoring indicator $d_i$, the corresponding single-event survival likelihood under conditionally independent censoring is

$$
\mathcal L_H=\prod_i\lambda_i(t_i)^{d_i}
\exp\left[-\int_0^{t_i}\lambda_i(u)\,du\right].
$$

The hazard definition gives $d\log S_i(t)/dt=-\lambda_i(t)$, hence conditional survival

$$
S_i(t)=\exp\left[-\int_0^t\lambda_i(u)\,du\right].
$$

Prediction averages this expression over posterior draws. For competing terminal exits, replace the cumulative hazard by the sum over causes and calculate default incidence by integrating $S_i(t-)\lambda_{iD}(t)$ over the stated horizon. This connects the same named hierarchy to the appropriate probability target while retaining each outcome's likelihood.

For binary observations $y_i$, logistic predictor $\eta_i=\boldsymbol x_i^{\mathsf T}\boldsymbol\theta$ and $\kappa_i=y_i-1/2$, the likelihood has the Pólya–Gamma mixture representation

$$
\frac{e^{y_i\eta_i}}{1+e^{\eta_i}}
=\frac12e^{\kappa_i\eta_i}
\int_0^\infty e^{-\omega_i\eta_i^2/2}
p_{\mathrm{PG}(1,0)}(\omega_i)\,d\omega_i.
$$

Conditional on $\omega_i\sim\operatorname{PG}(1,\eta_i)$ and a Gaussian prior $\boldsymbol\theta\sim\mathcal N(\boldsymbol m_0,Q_0^{-1})$, the quadratic terms give

$$
\log p(\boldsymbol\theta\mid\boldsymbol\omega,\mathcal H,D)
=-\frac12\boldsymbol\theta^{\mathsf T}
(X^{\mathsf T}\Omega X+Q_0)\boldsymbol\theta
+\boldsymbol\theta^{\mathsf T}(X^{\mathsf T}\boldsymbol\kappa+Q_0\boldsymbol m_0)
+\mathrm{constant}.
$$

Completing the square yields

$$
\Sigma_*=(X^{\mathsf T}\Omega X+Q_0)^{-1},\qquad
\boldsymbol m_*=\Sigma_*(X^{\mathsf T}\boldsymbol\kappa+Q_0\boldsymbol m_0),
$$

$$
\boldsymbol\theta\mid\boldsymbol\omega,\mathcal H,D
\sim\mathcal N(\boldsymbol m_*,\Sigma_*).
$$

$X$ is the expanded design matrix, including intercept, fixed features and sector, region and vintage indicators. Its vector $\boldsymbol\theta$ stacks their coefficients and centred group effects. The set $\mathcal H$ contains the scale and other hyperparameters currently held fixed; $Q_0$ is the resulting conditional prior precision, $\boldsymbol m_0$ its mean, and $\Omega=\operatorname{diag}(\omega_i)$. In non-centred coordinates the relevant group columns are multiplied by their fixed scales and the raw effects receive standard-normal prior blocks. The same square-completion argument then applies to that transformed design. A separately specified hazard likelihood uses its corresponding inference method; Pólya–Gamma updates apply when its likelihood has the required form.

For the article’s Gaussian group effects $u_j\mid\sigma\sim\mathcal N(0,\sigma^2)$ with a half-Student-t prior on $\sigma$, one useful auxiliary representation is

$$
\sigma^2\mid\xi\sim\operatorname{IG}\left(\frac\nu2,\frac\nu\xi\right),
\qquad
\xi\sim\operatorname{IG}\left(\frac12,\frac1{A^2}\right).
$$

Here $A>0$ is the half-t scale, $\nu=3$ its degrees of freedom where selected, and IG$(a,b)$ has density proportional to $v^{-a-1}e^{-b/v}$ for $v>0$. Integrating $\xi$ gives

$$
p(\sigma)\propto
\left(1+\frac{\sigma^2}{\nu A^2}\right)^{-(\nu+1)/2},
\qquad \sigma>0.
$$

For $m$ independent centred group effects, the associated conditional scale updates are

$$
\sigma^2\mid\boldsymbol u,\xi
\sim\operatorname{IG}\left(
\frac{\nu+m}{2},\frac\nu\xi+\frac12\sum_{j=1}^{m}u_j^2\right),
$$

$$
\xi\mid\sigma^2
\sim\operatorname{IG}\left(
\frac{\nu+1}{2},\frac\nu{\sigma^2}+\frac1{A^2}\right).
$$

These expressions concern the centred scalar-variance hierarchy. Correlation structures or a non-centred parameterisation require their corresponding conditionals. The non-centred identity $u_j=\sigma z_j$, $z_j\sim\mathcal N(0,1)$ expresses the same hierarchy but changes sampling geometry.

To make that distinction computationally explicit, write a non-centred group contribution as $\sigma v$, where $v=Z_gz$ and the remaining predictor is the fixed offset $c$. With $\eta=c+\sigma v$, its conditional scale kernel is

$$
p(\sigma\mid z,\omega,\ldots)\propto\mathbf1\{\sigma>0\}
\exp\left[-\tfrac12\sigma^2v^{\mathsf T}\Omega v
+\sigma v^{\mathsf T}(\kappa-\Omega c)\right]p(\sigma).
$$

The centred inverse-Gamma update conditions on $u$ rather than $z$, so it is used only in the coordinates for which it was derived. Gaussian coefficient blocks, latent-variable updates and scale updates are assessed together through convergence, effective sample size and computation time; the deployed service can then use validated posterior artefacts for the approved refresh period.

An ordinary Student-t coefficient prior has another familiar representation: $\lambda\sim\operatorname{Gamma}(\nu/2,\nu/2)$ in shape–rate convention and $u\mid\lambda\sim\mathcal N(0,s^2/\lambda)$. At $\nu=3$, both Gamma parameters are $3/2$. This coefficient mixture and a half-t prior on a group standard deviation play different roles; the registered model states which is used.

## A5.7 Posterior summaries, numerical error and release checks

For retained posterior draws $\theta^{(1)},\ldots,\theta^{(M)}$, calculate each decision-specific risk $p^{(m)}=p_{12}(a;\theta^{(m)})$. The exceedance estimate is

$$
\widehat q_p=\frac1M\sum_{m=1}^{M}
\mathbf1\{p^{(m)}>p_{\max}\}.
$$

Empirical quantiles of the same draws estimate credible bounds. Causal-effect draws produce $\widehat q_\Delta$ analogously. Predictive cash additionally samples future outcomes conditional on each parameter draw. For independent draws, the standard error of a probability estimate is approximately $\sqrt{\widehat q(1-\widehat q)/M}$; correlated MCMC output requires a variance estimate or effective sample size appropriate to that indicator. A probability near the review threshold merits enough computation that simulation error is visible and acceptably small.

An approved approximation can be compared against reference summaries on a registered test set $\mathcal T$:

$$
\max_{i\in\mathcal T}|\widehat q_i^{\mathrm{service}}-\widehat q_i^{\mathrm{reference}}|
\le\varepsilon_q.
$$

Analogous tolerances cover credible bounds, predictive cash and resulting review routes. Passing these fixtures verifies the tested implementation agreement; it does not establish the model’s empirical accuracy outside the tested population.

## A5.8 Workflow invariants and what a replay test verifies

Let an action record contain identifier $e$, case identifier, approved payload digest $h$, permission scope, expiry $t^{\mathrm{exp}}$ and execution state. Proposed engineering invariants include

$$
\begin{aligned}
\operatorname{Execute}(e,t)\Rightarrow{}&
\operatorname{Approved}(e)\land\operatorname{Authorised}(e,t)\\
&{}\land(t\le t^{\mathrm{exp}})\\
&{}\land\bigl(\operatorname{Digest}(\operatorname{payload})=h\bigr).
\end{aligned}
$$

A repeated identifier with the same payload returns the existing result; a conflicting payload is rejected for review. Cash availability requires a reconciled settlement record with the required references and availability date. The accounting identity from Article 4 then updates the relevant ledger once for the economic event.

These are design specifications tested through replay, access-control and reconciliation fixtures. They are not statistical theorems about actual bank permissions, source authenticity or external settlement. Deployment evidence must show that the running services enforce them, that reviewers can exercise their authority, and that operational owners resolve exceptions. The resulting audit record connects the mathematical summary to the approved action and realised outcome.

### Sources supporting this appendix

Pólya–Gamma inference follows [3], and the half-t auxiliary-variable representation follows [10], Result 5. Numerical summaries are derived from the specified illustrative distributions using the inference and decision framework in [7]. The workflow applies the bank-controlled architecture [1] and the legal sources [4], [5].
