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

The expected-payoff and uncertainty-review distinction follows the decision-analysis framework in [7], ch. 9. A2.12 derives the fixed-payoff decision boundary; A5.2 supplies the Beta$(4,96)$ posterior calculation used in this workflow example.

The example starts with limit $L=500{,}000$ KES and drawn principal $U=300{,}000$ KES. Existing undrawn headroom is $L-U=200{,}000$ KES. Increasing the limit by KES 100,000 would make $L'=600{,}000$ and undrawn headroom KES 300,000, before any new drawing. Cash disbursement changes when a drawing is executed.

The review route allows a posterior cap-exceedance probability of at most $\epsilon_p=0.10$ at the approved risk cap $p_{\max}=0.06$. A5.2 computes that exceedance probability as approximately 14.84%. It therefore routes this case to additional evidence or higher-authority review. The criterion governs uncertainty about the risk parameter; realised defaults are subsequently assessed through outcome monitoring. A separate support action follows its own eligibility and benefit review.

For a continuous strictly increasing posterior cumulative distribution $F_p$, the probability gate in A5.1 is equivalent to $F_p(p_{\max})\ge1-\epsilon_p$, or $F_p^{-1}(1-\epsilon_p)\le p_{\max}$. It therefore compares an upper posterior quantile with the approved cap. The fixed-payoff illustration derived in A2.12 gives a 6% expected-payoff boundary and KES 400 expected value at the 4% posterior mean. That favourable expected value and the additional-review route above answer complementary decision questions: expected incremental value and the institution's tolerance for uncertainty. Limit changes use incremental action values relative to the existing facility, with uncertain utilisation and recovery retained in joint posterior draws.

A schematic permissible-action set is

$$
\mathcal A^{\mathrm{review}}(D)
=\left\{a:\ G_k(D,a)=1\ \forall k,
\quad q_p(D,a)\le\epsilon_p\right\},
$$

where $G_k$ are the applicable contractual, affordability, conduct, mandate and data-quality gates for that action. Additional benefit or cash-risk criteria can be specified separately. Their thresholds are approved policy inputs. Where more evidence is needed, the permitted response can be information gathering, deferral or another authorised action.

## A5.6 Model specification, computation and approved artifact

The derivations are collected once across the series. A2.5 defines the fixed-horizon logistic hierarchy and the sector, region and origination-vintage pooling structure. A1.8 gives the general survival and competing-risk quantities, and A2.6 derives the hierarchical hazard likelihood and baseline-hazard treatment. A3.6–A3.9 add the offer-selection and reject-inference estimands and align their logistic and survival targets. A2.10 contains the Pólya–Gamma identity and conditional Gaussian update; A2.11 contains the separate Student-t coefficient and half-Student-t group-scale mixture representations and updates. Article-body equations remain in place; these appendix references identify where their full mathematical derivations are maintained.

For the registered baseline, fixed regression coefficients have a Gaussian prior, for example $\boldsymbol\beta\sim\mathcal N(\boldsymbol 0,B)$, while each positive group standard deviation has its own half-Student-t prior, $\sigma_k>0$ and $\sigma_k\sim\operatorname{HalfStudentT}(3,A_k)$. The first prior regularises signed fixed coefficients; the second controls the dispersion of conditionally Gaussian group effects. A Student-t coefficient prior, such as $\beta_j\sim t_3(0,s_j)$ with a coefficient-specific Gamma precision mixture, is a separately registered sensitivity or alternative model. It is not implied by the half-t prior on $\sigma_k$. A fitted artifact records the active coefficient-prior family and its scales independently from the group-scale prior and parameterisation. The corresponding full mixture derivations remain at A2.11.

Pólya–Gamma augmentation provides a conditionally Gaussian update for the logistic likelihood in A2.10. The hazard and competing-risk likelihoods use the inference method registered for their likelihood; the logistic augmentation is used for them only if the specified likelihood admits that representation. A3.8 retains its local numerical conditional-update check, and A3.7 retains its model-specific prior-role explanation.

Each validated model artifact carries a versioned, reviewable contract:

| Artifact field | Required content |
| --- | --- |
| Model identity | Model and code version; registered specification; training-data cut or governed snapshot identifier. |
| Prediction target | Population, outcome/event definition, horizon, action and comparator, plus units and estimand type (risk, causal effect or predictive cash). |
| Model and prior configuration | Logistic or hazard model; feature and hierarchy schema; active coefficient-prior family and scales; group-scale priors; centred or non-centred parameterisation. |
| Computation provenance | Inference implementation, software version, sampler configuration, random seed or reproducibility key, run time and posterior-draw or summary-set identifier. |
| Validation evidence | Convergence and effective-sample diagnostics, Monte Carlo error, calibration and registered fixture results, approximation tolerances, reviewer disposition and unresolved exceptions. |
| Release authority | Independent validation and approval records, maker/checker identities and timestamps, permitted use, effective date, refresh/review date and superseding artifact identifier. |

The case-level output binds its summaries to that artifact and to the governed evidence snapshot: posterior risk and its credible bounds, posterior cap-exceedance probability, any identified action-effect interval and comparison, predictive cash distribution, and the decision threshold applied. Each quantity retains its own target, population, horizon, action and units. The artifact stores the summary method and draw reference needed to reproduce it, along with the case correlation identifier and approval state. Source personal data remain in their governed systems; the artifact carries controlled references and derived outputs required for review.

A release is eligible for a decision workflow only after the registered diagnostics, validation tolerances and approval checks pass. The release record identifies the approved refresh period and routes stale, failed or out-of-scope results for review. A5.7 specifies numerical error and release fixtures; A5.8 specifies replay, authorisation and reconciliation invariants. Together they connect the canonical model computations to a reproducible, governed decision artifact without repeating the derivations.

## A5.7 Numerical error, approximation tolerances and release checks

A3.13 defines the model-specific posterior review summaries and their draw-based calculation. A5.1 distinguishes the risk-parameter, identified causal-effect and predictive-cash probabilities used by this workflow. This section specifies how accurately the service must reproduce those summaries before release. The registered calculation fixes the target, action, horizon, interval convention and draw identifier, so the reference and service outputs describe the same quantity.

For a probability summary $q$, let $\widehat q$ be its estimated value from $M$ independent retained draws. The Monte Carlo standard error is approximately

$$
\operatorname{MCSE}(\widehat q)
\approx\sqrt{\frac{\widehat q(1-\widehat q)}{M}}.
$$

Correlated MCMC output requires a variance estimate or effective sample size appropriate to the indicator defining that probability. Credible-bound accuracy requires quantile-specific error assessment, and predictive cash accuracy also reflects the finite number of future-outcome simulations. Each output is therefore accompanied by its relevant numerical diagnostic. A probability close to a routing threshold receives sufficient computation and a documented review treatment when numerical error could change its route.

An approved approximation is compared against reference summaries on a registered test set $\mathcal T$:

$$
\max_{i\in\mathcal T}|\widehat q_i^{\mathrm{service}}-\widehat q_i^{\mathrm{reference}}|
\le\varepsilon_q.
$$

Reference simulations are run to an accuracy appropriate to this tolerance, and their numerical error is recorded alongside the service discrepancy. Analogous tolerances cover credible bounds, predictive cash and resulting review routes, including fixtures near policy thresholds. The exact Beta result in A5.2 provides one algebraic check for a compatible test fixture. Passing these fixtures establishes implementation agreement on the registered cases; calibration, population coverage and drift checks provide the corresponding empirical validation evidence.

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

The Pólya–Gamma and auxiliary half-t derivations are maintained at A2.10 and A2.11, respectively, with supporting sources [3] and [10], Result 5. Numerical summaries are derived from the specified illustrative distributions using the inference and decision framework in [7]. The workflow applies the bank-controlled architecture [1] and the legal sources [4], [5].
