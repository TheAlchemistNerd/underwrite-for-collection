# Article 3 mathematical appendix: selective labels, posterior inference and evidence boundaries

This appendix derives the statistical relationships used in Article 3. A repayment outcome is indexed by contract, population and horizon. The calculations distinguish an observed loan outcome, an estimate for a supported population and a sensitivity calculation for unobserved outcomes. The examples are hypothetical and use KES for currency. The common hierarchical structure retains sector, region and origination-vintage effects so that its uncertainty can be carried into the later decision and operating workflows.

## A3.1 Define the offer, funding and outcome separately

Let $X_i$ be the information available before applicant $i$ is considered for a complete contract $a$. Let $U_i(a)$ indicate whether that applicant would accept and draw the offer. Let $D_i^a(\tau)$ indicate default by horizon $\tau$ under origination of that specified contract and servicing regime. The latter is a potential outcome under a funding intervention. If the target is an offer policy rather than a funding intervention, also define an applicant-level outcome $Y_i^{\mathrm{offer}}(a)$, whose meaning includes non-take-up. These definitions avoid assigning a factual loan-default label to somebody who never took a loan.

The principal targets are

$$
\begin{aligned}
p_a(x)&=\Pr\{D_i^a(\tau)=1\mid X_i=x\},\\
t_a(x)&=\Pr\{U_i(a)=1\mid X_i=x\},\\
p_a^{\mathrm{takers}}(x)
&=\Pr\{D_i^a(\tau)=1\mid X_i=x,U_i(a)=1\},\\
v_a(x)&=E[Y_i^{\mathrm{offer}}(a)\mid X_i=x].
\end{aligned}
$$

These are respectively funding-intervention risk, offer take-up, risk among that offer's takers, and value per applicant receiving the offer policy. Equal numerical values are possible but are not assumed. The contract $a$ includes limit or advance, price and fees, term, repayment dates, guarantees, security and servicing. Historical outcomes under different contracts require explicit action adjustment or contract-specific strata.

For the derivations below, let $S_i=1$ denote financing under the specified contract $a$ with the target outcome observed. Selection can be decomposed further into approval, delivery, acceptance, disbursement and outcome observation. If the historical data contain several offers, replace $S$ by $S_a=1\{S=1,A=a\}$ and use the joint selection probability for that contract. A propensity for generic approval alone does not adjust changes in contract or take-up.

## A3.2 Why observed labels do not identify missing outcomes by themselves

The selective-label and reject-inference problem follows [1], [2], [3].

Write

$$
e(x)=\Pr(S=1\mid X=x),\qquad
m_s(x)=\Pr\{D^a(\tau)=1\mid X=x,S=s\}.
$$

The law of total probability gives

$$
p_a(x)=e(x)m_1(x)+\{1-e(x)\}m_0(x).
$$

Historical financed loans estimate $m_1(x)$ where supported; the full application file can estimate $e(x)$. The unobserved $m_0(x)$ remains needed for the all-applicant target. With only the fact that a binary probability lies between zero and one,

$$
e(x)m_1(x)\le p_a(x)\le e(x)m_1(x)+1-e(x).
$$

At $e=0.60$ and $m_1=0.05$, these identification bounds are 3% to 43%. They are logical bounds under the defined outcome, not a 95% uncertainty interval. Additional justified restrictions can narrow them; a narrow fitted-model interval alone does not alter their identification basis.

An observed-data likelihood makes the information gap explicit. Under a selection-ignorable outcome model with parameter $\theta$, an unobserved binary outcome contributes

$$
\sum_{d=0}^{1}p_\theta(x)^d\{1-p_\theta(x)\}^{1-d}
=p_\theta(x)+1-p_\theta(x)=1.
$$

Thus its missing label contributes no direct repayment-likelihood factor. In a correctly specified data-augmentation algorithm, drawing that missing label is a computational device whose integration returns this same likelihood; it does not enlarge the observed sample. Treating one imputed draw as an additional fixed observation during refitting can instead add artificial information.

For non-ignorable selection, let $e_d(x)=\Pr(S=1\mid D^a=d,X=x)$. At a given $x$, the observed categories have probabilities

$$
\begin{aligned}
\Pr(S=1,D=1\mid x)&=e_1(x)p_a(x),\\
\Pr(S=1,D=0\mid x)&=e_0(x)\{1-p_a(x)\},\\
\Pr(S=0\mid x)&=1-e_1(x)p_a(x)-e_0(x)\{1-p_a(x)\}.
\end{aligned}
$$

Only two category probabilities are independent, while $p_a,e_1,e_0$ supply three unknown quantities at that $x$. Without extra restrictions or information, different combinations produce the same observed distribution. A joint selection-outcome model makes those restrictions explicit through a functional form, measured predictors, a defensible exclusion variable, prior information or prospective observations.

*Source connection:* Lakkaraju and colleagues, “The Selective Labels Problem,” motivates the observation boundary; Crook and Banasik, “Does Reject Inference Really Improve the Performance of Application Scoring Models?”, motivates testing how reject-inference assumptions affect results.

## A3.3 Transport from financed applicants to a defined target

Assume consistency for the declared contract, conditional selection exchangeability

$$
D^a(\tau)\mathrel{\perp\!\!\!\perp}S\mid X,
$$

and positive selection probability $e(X)>0$ wherever the target applicant distribution has mass. Then $m_0(x)=m_1(x)=m(x)$ and the target mean default probability is $\mu_a=E_X[m(X)]$. The usual stronger overlap statement $0<e(X)<1$ permits comparison of selected and non-selected applicants; estimating the all-applicant mean from outcomes fundamentally requires a positive chance of a selected analogue in each target region.

For a complete applicant sample, the inverse-selection identity follows by conditioning:

$$
\begin{aligned}
E\left[\frac{SD}{e(X)}\middle|X\right]
&=\frac{\Pr(S=1\mid X)}{e(X)}E[D\mid X,S=1]\\
&=m(X).
\end{aligned}
$$

Consequently,

$$
\widehat\mu_{\mathrm{IPW}}
=\frac1N\sum_{i=1}^N\frac{S_iD_i}{\widehat e(X_i)}
$$

targets all $N$ applicants, under the stated conditions and a consistent selection model. Multiplication by $S_i$ means the summand is zero when the outcome is absent; no default value is imputed into the underlying record.

If the target is specifically the historically unfinanced population, use its covariate distribution:

$$
\begin{aligned}
E[D^a\mid S=0]
&=\frac{E[\{1-e(X)\}m(X)]}{\Pr(S=0)}\\
&=\frac{E\left[S\frac{1-e(X)}{e(X)}D\right]}{\Pr(S=0)}.
\end{aligned}
$$

The selected observations receive odds weights $(1-e)/e$, rather than the all-applicant weights $1/e$. If only a financed file exists and the applicant distribution or selection probabilities are unknown, neither target is automatically recovered. An independently sampled target population can instead be handled with a properly estimated density ratio; that ratio needs information about both populations.

**Numerical example.** Suppose the target has 100 applicants in each of two strata. Financing probabilities are 0.5 and 0.25, giving 50 and 25 financed observations. Observed default counts are 5 and 5. The raw financed-loan estimate is $10/75=13.333\%$. The IPW numerator is $5/0.5+5/0.25=30$, giving $30/200=15\%$. This equals the equally weighted stratum calculation $(0.10+0.20)/2$. The first calculation describes the selected portfolio; the second describes the target under exchangeability. Neither calculation corrects an unrecorded selection variable that also affects default.

At $e(x)=0$, the reciprocal weight is undefined, expressing the absence of outcome support. Near-zero probabilities generate concentrated weights. Report the weight distribution and the diagnostic $(\sum_iw_i)^2/\sum_iw_i^2$ alongside uncertainty. Truncating weights changes the calculation and requires an explicit sensitivity or revised target interpretation.

## A3.4 Doubly robust selection adjustment

The augmented estimator adapts the doubly robust construction in [7], [8] to the stated selection assumptions.

For working outcome model $\widehat m(X)$ and working selection model $\widehat e(X)$, define

$$
\widehat\mu_{\mathrm{DR}}
=\frac1N\sum_i\left[
\widehat m(X_i)+\frac{S_i}{\widehat e(X_i)}
\{D_i-\widehat m(X_i)\}\right].
$$

Conditioning on $X$ under exchangeable selection gives

$$
\begin{aligned}
E\left[\widehat m(X)+\frac{S}{\widehat e(X)}
(D-\widehat m(X))\middle|X\right]
&=\widehat m(X)+\frac{e(X)}{\widehat e(X)}\{m(X)-\widehat m(X)\},\\
\operatorname{Bias}(X)
&=\left(\frac{e(X)}{\widehat e(X)}-1\right)
\{m(X)-\widehat m(X)\}.
\end{aligned}
$$

The conditional bias is zero if either working model is correct. It need not be zero when selection exchangeability fails, since then $E[D\mid S=1,X]$ differs from the target conditional mean. Cross-fitting fits nuisance functions away from the evaluated observation; its purpose is to control overfitting effects, with inference requiring suitable regularity and convergence rates. Observed model accuracy in the financed subset cannot establish the exchangeability condition.

For unequal contract assignments, a more complete residual term uses the probability of selection and action jointly. With $I_i(a)=1\{S_i=1,A_i=a\}$ and $e_a(x)=\Pr\{I_i(a)=1\mid X_i=x\}$,

$$
\widehat\mu_a=\frac{1}{N}\sum_i\left[
\widehat m_a(X_i)+\frac{I_i(a)}{\widehat e_a(X_i)}
\{D_i-\widehat m_a(X_i)\}\right].
$$

Further right-censoring or missing follow-up requires its own outcome-observation treatment. The Article 1 appendix derives the corresponding action-policy estimator and observation weights. Those weights adjust separate mechanisms and must correspond to the decision and data actually delivered.

*Source connection:* Dudík, Langford and Li, “Doubly Robust Policy Evaluation and Learning,” gives the policy version of this augmentation logic; Wang, Agarwal and Dudík, “Optimal and Adaptive Off-Policy Evaluation in Contextual Bandits,” discusses its evaluation setting and overlap challenges.

## A3.5 Derive log-odds sensitivity for unobserved selection

Let $\delta_g$ be a declared sensitivity parameter for segment $g$. Write

$$
\operatorname{logit}m_0(x)
=\operatorname{logit}m_1(x)+\delta_g.
$$

Since $\operatorname{logit}p=\log\{p/(1-p)\}$, exponentiating yields

$$
\frac{m_0(x)}{1-m_0(x)}
=e^{\delta_g}\frac{m_1(x)}{1-m_1(x)}.
$$

Solving for the unobserved-group risk gives

$$
m_0(x;\delta_g)
=\frac{e^{\delta_g}m_1(x)}{1-m_1(x)+e^{\delta_g}m_1(x)}.
$$

Thus $e^{\delta_g}$ is the assumed rejected-to-financed odds ratio within that segment and context. It is not a parameter identified merely by observing financed-loan defaults. At $m_1=0.05$, choices $\delta=\log(1/2),0,\log2$ give 2.5641%,5%,9.5238% for the unfinanced-group risk. If $e=0.60$, corresponding all-applicant risks are

$$
0.6(0.05)+0.4m_0
=4.0256\%,\quad5.0000\%,\quad6.8095\%.
$$

For posterior draws $m_1^{(b)}(x)$ and $e^{(b)}(x)$, transform each draw at each fixed sensitivity value $\delta$ and aggregate over the target covariates:

$$
\mu_a^{(b)}(\delta)
=\frac1N\sum_i\left[
e^{(b)}(X_i)m_1^{(b)}(X_i)
+\{1-e^{(b)}(X_i)\}m_0^{(b)}(X_i;\delta)
\right].
$$

The quantiles across $b$ quantify posterior uncertainty conditional on a chosen $\delta$. Variation across $\delta$ shows sensitivity to the identification assumption. These two sources of uncertainty should remain visible to the reviewer. A prior for $\delta$ can be used if its external basis and influence are stated; its posterior concentration does not become observed reject performance.

## A3.6 The common sector, region and vintage hierarchy

The multilevel prior and pooling structure follow [4], [5].

For a fixed horizon and contract, let the linear predictor be

$$
\begin{aligned}
D_i^a(\tau)\mid p_i&\sim\operatorname{Bernoulli}(p_i),\\
p_i&=\operatorname{logit}^{-1}(\eta_i),\\
\eta_i&=\alpha^L+u^L_{s(i)}+v^L_{r(i)}+w^L_{c(i)}
+f^L(X_i)+h^L(a,X_i).
\end{aligned}
$$

Here $s(i),r(i),c(i)$ index sector, region and origination vintage. Superscript $L$ identifies logistic parameters; superscript $H$ identifies hazard parameters. $f^L$ contains declared borrower transformations, while $h^L$ contains offer effects and interactions. A design row $z_i^\top$ can collect these terms so that $\eta_i=z_i^\top\theta$. Group effects require identifiability constraints or proper centred priors together with a declared intercept convention. Reference levels or sum-to-zero constraints must be implemented consistently in scoring and estimation.

One non-centred scale specification is

$$
\begin{aligned}
u^m_s&=\sigma^m_u\widetilde u^m_s,&\widetilde u^m_s&\sim N(0,1),\\
v^m_r&=\sigma^m_v\widetilde v^m_r,&\widetilde v^m_r&\sim N(0,1),\\
w^m_c&=\sigma^m_w\widetilde w^m_c,&\widetilde w^m_c&\sim N(0,1),\\
\sigma^m_k&\sim\operatorname{HalfStudentT}(\nu=3,s^m_{0,k}),
&&k\in\{u,v,w\},\quad m\in\{L,H\},\\
\alpha^L&\sim N(0,s_\alpha^2),&\beta^m&\sim N(0,B^m),\\
\lambda_{0,\ell}&\sim\operatorname{Gamma}(a_\ell,b_\ell).
\end{aligned}
$$

Each $\sigma^m_k$ is a family scale shared across that effect's levels within model $m$. Normal's second argument is variance or covariance; Gamma uses shape and rate. The declared positive $s^m_{0,k},s_\alpha,a_\ell,b_\ell$ and positive-definite $B^m$ complete the prior specification. $\beta^m$ includes the coefficients of the declared feature and action-interaction bases. Prior-predictive checks assess implications on the appropriate log-odds or log-hazard scale. A vintage random walk or autoregression is an optional extension with its own innovation-scale prior and explicit temporal structure; exchangeable vintage effects do not imply that time-series dependence automatically exists.

**Why pooling depends on information.** In a Gaussian analogue, suppose a noisy group statistic obeys $\overline y_j\mid u_j\sim N(u_j,s^2/n_j)$ with $u_j\sim N(0,\tau^2)$. Multiplying the two normal kernels gives posterior precision $n_j/s^2+1/\tau^2$ and mean

$$
E[u_j\mid\overline y_j]
=\frac{\tau^2}{\tau^2+s^2/n_j}\overline y_j.
$$

The shrinkage weight approaches one as the group's data become precise and approaches zero as the prior group scale becomes small. For $\tau^2=0.04$, $s^2=1$, $\overline y_j=0.7$, a group of 10 gives posterior mean 0.2; a group of 100 gives 0.56. This is an exact Gaussian demonstration of pooling, not an exact closed-form logistic posterior. The augmented logistic model obtains analogous conditional Gaussian calculations within its full sampler.

Posterior draws preserve uncertainty about group scales and correlations where those are modelled. A sector–region–vintage subgroup with little information may depend strongly on pooling and prior choices. Human review should therefore display its support and sensitivity alongside its credible interval. To estimate a causal offer effect through $h(a,X)$, the model still needs the experiment or adjustment assumptions that identify the offer comparison.

## A3.7 Half-Student-t scale mixtures and their computational role

The auxiliary scale representation follows [20], Result 5.

Use a Gamma distribution with shape and rate. For $\nu>0$ and scale $s_0>0$, let

$$
\lambda\sim\operatorname{Gamma}(\nu/2,\nu/2),
\qquad q\mid\lambda\sim N(0,s_0^2/\lambda).
$$

Multiply the normal and Gamma densities, retaining terms depending on $q$ and $\lambda$:

$$
p(q,\lambda)\propto
\lambda^{(\nu+1)/2-1}
\exp\left[-\frac{\lambda}{2}
\left(\nu+\frac{q^2}{s_0^2}\right)\right].
$$

The Gamma integral $\int_0^\infty\lambda^{a-1}e^{-b\lambda}d\lambda=\Gamma(a)/b^a$ gives

$$
p(q)=\frac{\Gamma((\nu+1)/2)}
{\Gamma(\nu/2)\sqrt{\nu\pi}\,s_0}
\left(1+\frac{q^2}{\nu s_0^2}\right)^{-(\nu+1)/2}.
$$

This is a centred Student-t density. Setting $\sigma=|q|$ yields density $2p(\sigma)$ for $\sigma>0$, the half-t prior. For $\nu=3$, the Gamma shape and rate are both 3/2; the Student-t degrees of freedom are 3. The normal variance is $s_0^2/\lambda$, so its standard deviation is $s_0/\sqrt\lambda$.

In the hierarchy, a group effect is $u_j=\sigma z_j$ with $z_j\sim N(0,1)$. Conditional on $\sigma$, the effect is normal; assigning a half-t to $\sigma$ defines a scale mixture for $u_j$, but its marginal law is not automatically the same Student-t density just derived for $q$. The scale-mixture identity therefore needs its variable labels. It supplies a flexible positive scale prior and useful parameterisations, while coefficient conjugacy in the binary likelihood comes from the separate Pólya–Gamma augmentation below.

*Source connection:* Gelman, “Prior Distributions for Variance Parameters in Hierarchical Models,” motivates calibrated half-t scale priors and sensitivity analysis. The Stan User's Guide, “Reparameterizing a Student-t Distribution,” documents the normal–Gamma representation and its computational use.

## A3.8 Derive the Pólya–Gamma Gaussian conditional posterior

The augmentation identity follows [9].

For observed binary $y_i$ and log-odds $\eta_i$, the Bernoulli likelihood is

$$
p(y_i\mid\eta_i)=\frac{e^{y_i\eta_i}}{1+e^{\eta_i}}.
$$

Use $1+e^{\eta}=2e^{\eta/2}\cosh(\eta/2)$ and define $\kappa_i=y_i-1/2$. Then

$$
p(y_i\mid\eta_i)=\frac12e^{\kappa_i\eta_i}\cosh^{-1}(\eta_i/2).
$$

The Pólya–Gamma Laplace-transform identity for $\omega\sim\operatorname{PG}(1,0)$ is

$$
E[e^{-\omega\eta^2/2}]=\cosh^{-1}(\eta/2).
$$

Substitution rewrites the likelihood as

$$
p(y_i\mid\eta_i)
=\frac12e^{\kappa_i\eta_i}
\int_0^\infty e^{-\omega_i\eta_i^2/2}
p_{\mathrm{PG}(1,0)}(\omega_i)\,d\omega_i.
$$

The tilted conditional distribution is $\omega_i\mid\eta_i,y_i\sim\operatorname{PG}(1,\eta_i)$. Conditional on the latent $\omega_i$, its contribution to the log-likelihood is quadratic: $\kappa_i\eta_i-\omega_i\eta_i^2/2$.

Let $Z$ be the full design matrix for the common hierarchy, $\Omega=\operatorname{diag}(\omega_i)$, and $\kappa=(\kappa_i)$. Conditional on hierarchy scales, choose a proper Gaussian coefficient prior $\theta\sim N(m_0,Q_0^{-1})$, where $Q_0$ is its precision matrix. Combine likelihood and prior:

$$
\log p(\theta\mid\omega,y,\text{scales})
=-\frac12\theta^\top(Z^\top\Omega Z+Q_0)\theta
+\theta^\top(Z^\top\kappa+Q_0m_0)+\text{constant}.
$$

Completing the square gives

$$
\begin{aligned}
V_*&=(Z^\top\Omega Z+Q_0)^{-1},\\
m_*&=V_*(Z^\top\kappa+Q_0m_0),\\
\theta\mid\omega,y,\text{scales}&\sim N(m_*,V_*).
\end{aligned}
$$

For the article's compact notation, substitute the expanded $Z=X$, stacked $\theta=\beta$ and $Q_0=\Sigma_0^{-1}$, obtaining its displayed covariance. The expansion includes sector, region and vintage indicators, with covariance conditional on their current scales. If fixed offsets $c$ are retained outside the updated block, use $Z^\top(\kappa-\Omega c)+Q_0m_0$ in the conditional mean. This accounts for other predictor components while updating a subset of coefficients.

**One conditional-update check.** In an intercept-only model with nine outcomes and one event, $\sum_i\kappa_i=1-9/2=-3.5$. Suppose the current latent draws sum to 2 and the intercept prior is $N(0,4)$. Then

$$
V_*=(2+1/4)^{-1}=4/9,
\qquad m_*=(4/9)(-3.5)=-14/9.
$$

The next coefficient draw is therefore $N(-1.5556,0.4444)$ conditional on those latent variables. This single update is not the marginal fitted posterior. Repeated validated updates of latent variables, coefficients, scales and any correlation parameters generate the marginal posterior draws used for reporting. In software, factor and solve the positive-definite precision matrix rather than explicitly forming its inverse whenever feasible; compare numerical residuals and Monte Carlo diagnostics against the declared tolerances.

The hierarchy-scale updates are separate from this Gaussian block. Conditional conjugacy improves a defined computational step; elapsed time, effective sample size, convergence, calibration and decision stability still need measurement. The approved scoring artefact can store posterior draws or validated summaries so that a reviewer receives uncertainty without refitting the full model during every decision.

*Source connection:* Polson, Scott and Windle, “Bayesian Inference for Logistic Models Using Pólya–Gamma Latent Variables,” supplies the augmentation identity and Gaussian conditional calculation.

## A3.9 Survival likelihood, hierarchy and default incidence

The hazard and partial-likelihood framework follows [6].

For event time $T_i$, censoring time $C_i$, observed time $t_i=\min(T_i,C_i)$ and event indicator $\delta_i$, specify

$$
\lambda_i(t\mid a)=\lambda_0(t)
\exp\{X_i^\top\beta^H+q^H(a,X_i)+u^H_{s(i)}+v^H_{r(i)}+w^H_{c(i)}\}.
$$

Using the same sector, region and vintage indexing does not require the logistic and survival coefficients to be numerically identical; they describe different likelihoods and time targets. Any joint sharing needs an explicit joint model. For a time-constant predictor $\eta_i$, cumulative hazard is $\Lambda_i(t)=e^{\eta_i}\Lambda_0(t)$ and survival is $S_i(t)=\exp[-\Lambda_i(t)]$.

Under conditionally independent censoring, the event component of the likelihood is

$$
L=\prod_i\lambda_i(t_i)^{\delta_i}S_i(t_i)
=\prod_i\lambda_0(t_i)^{\delta_i}
\exp\{\delta_i\eta_i-e^{\eta_i}\Lambda_0(t_i)\}.
$$

At distinct event times and conditional on one event in the risk set $\mathcal R(t_i)$, the baseline hazard cancels from the probability that unit $i$ is that event:

$$
\Pr(i\text{ fails}\mid\mathcal R(t_i),\text{one event})
=\frac{e^{\eta_i}}{\sum_{j\in\mathcal R(t_i)}e^{\eta_j}}.
$$

Multiplying these probabilities gives the Cox partial likelihood. Ties need a declared approximation or exact treatment. Absolute default probabilities additionally require an estimated or modelled baseline hazard. The fully Bayesian implementation here uses the $H$ hierarchy and the piecewise baseline Gamma priors in A3.6. Let $d_\ell$ be the number of events in interval $\ell$, and let $e_{i\ell}$ be subject $i$'s observed time at risk in that interval. Conditional on hazard predictors, the likelihood kernel for the interval rate is $\lambda_{0,\ell}^{d_\ell}\exp[-\lambda_{0,\ell}\sum_i e_{i\ell}e^{\eta_i}]$. Multiplying by its Gamma prior gives

$$
\lambda_{0,\ell}\mid\text{event data},\eta
\sim\operatorname{Gamma}\left(a_\ell+d_\ell,
b_\ell+\sum_i e_{i\ell}e^{\eta_i}\right).
$$

This is a conditional baseline update within the joint posterior; the hazard coefficient and scale updates follow their own likelihood blocks. A partial-likelihood coefficient fit alone does not provide all components of a Bayesian cash-flow forecast.

For competing terminal causes, $\lambda_{ik}$ is cause-specific and

$$
L_i=\left\{\prod_k\lambda_{ik}(t_i)^{1\{\delta_i=1,J_i=k\}}\right\}
\exp\left[-\int_0^{t_i}\sum_k\lambda_{ik}(u)\,du\right].
$$

The contract-specific default incidence is

$$
F_{iD}(\tau)=\int_0^\tau
\exp\left[-\int_0^u\sum_k\lambda_{ik}(v)\,dv\right]
\lambda_{iD}(u)\,du.
$$

A twelve-month logistic target for default before competing termination should be calibrated to this same event definition if compared with a survival-derived probability. Cure and restructuring often need intermediate states because a loan can later default. Article 1's appendix derives the corresponding Aalen–Johansen transition estimator and distinguishes cause-specific from subdistribution hazards.

## A3.10 The guarded pilot and the Wilson interval

The score-inversion interval follows [11].

In the article's example,1,000 applicants pass the study eligibility screen,100 receive a random offer,80 accept and draw, and four of those 80 default by the declared horizon. The three directly observed proportions have distinct meanings:

$$
\widehat{\Pr}(\text{offered})=100/1{,}000=10\%,
\quad
\widehat{\Pr}(\text{draw}\mid\text{offered})=80/100=80\%,
\quad
\widehat p=4/80=5\%.
$$

There are 900 applicants not offered the contract,20 offered but not funded, and 920 without an observed funded-loan repayment path. This distinction keeps assignment and take-up visible. An ITT effect additionally needs the specified comparator and an applicant-level outcome measured under both assignments.

For the funded-loan descriptive rate, suppose $K\sim\operatorname{Binomial}(n,p)$ with independent, exchangeable outcomes and complete follow-up. Under the score test, retain candidate values of $p$ satisfying

$$
\frac{(\widehat p-p)^2}{p(1-p)/n}\le z^2,
\qquad z=z_{1-\alpha/2}.
$$

Multiplying through and collecting powers of $p$ gives

$$
(n+z^2)p^2-(2n\widehat p+z^2)p+n\widehat p^{\,2}\le0.
$$

The interval between the two quadratic roots can be written

$$
\frac{\widehat p+z^2/(2n)}{1+z^2/n}
\ \pm\ 
\frac{z}{1+z^2/n}
\sqrt{\frac{\widehat p(1-\widehat p)}n+\frac{z^2}{4n^2}}.
$$

Substituting $n=80$, $\widehat p=0.05$ and $z=1.96$ produces centre 0.07061888 and half-width 0.05100564, hence

$$
[0.01961324,\;0.12162453],
$$

or approximately 1.96% to 12.16%. This reproduces the article's rounded 2.0%–12.2%. It is a frequentist score confidence interval for the defined funded sample, not a posterior credible interval or a whole-reject-population guarantee. Correlated group loans, unequal risk, incomplete follow-up or adaptive recruitment require an uncertainty method matched to those features.

For comparison, an explicitly chosen beta prior gives a Bayesian binomial calculation. If $p\sim\operatorname{Beta}(a_0,b_0)$, multiplication by the likelihood yields

$$
p\mid K=k,n\sim\operatorname{Beta}(a_0+k,b_0+n-k).
$$

An equal-tail credible interval is given by the 0.025 and 0.975 quantiles of that posterior. Under the illustrative Jeffreys prior $a_0=b_0=1/2$, the posterior is $\operatorname{Beta}(4.5,76.5)$ and its mean is $4.5/81=5.5556\%$. The prior, posterior mean and interval should be labelled; they describe funded pilot risk under the binomial model. A hierarchy extends this calculation to sector, region and vintage variation and carries the added parameter uncertainty into its draws.

*Source connection:* Wilson, “Probable Inference, the Law of Succession, and Statistical Inference,” derives the score-interval approach; DOI: https://doi.org/10.1080/01621459.1927.10502953. Its confidence-interval interpretation is retained separately from the Bayesian illustration.

## A3.11 Adaptive offers preserve an explicit observation process

The adaptive-allocation setting follows [10].

After a suitable fixed-design pilot, a registered mixture allocation can use

$$
\pi_t(a\mid x)
=(1-\epsilon_t)\widehat\pi_t(a\mid x)+\epsilon_tq(a\mid x).
$$

Because both component policies sum to one, so does the mixture. If $q(a\mid x)>0$ and $\epsilon_t$ has a positive floor, the mixture preserves a calculable probability for that eligible action. With two eligible offers, uniform $q$ and $\epsilon_t=0.2$, a deterministic current favourite receives 0.9 and the alternative 0.1. Outcomes still arrive only for delivered actions and, for funded-loan repayment, for acceptors who originate. Logged assignment probabilities support offer-policy evaluation; they do not by themselves eliminate acceptance selection or disclose repayment under an unissued loan. The Article 1 appendix supplies the expectation proofs and delayed-outcome conditions.

Under group guarantees, let $Y_i(\mathbf A_g)$ depend on the vector of assignments within group $g$. The ordinary notation $Y_i(A_i)$ is then incomplete unless an interference restriction is justified. Cluster randomisation can compare group-level assignment policies. An exposure-mapping design can instead define quantities such as the proportion of other members assigned a support treatment and identify effects under explicit network assumptions. The randomisation unit, analysis unit and customer-rights process must therefore agree with the guarantee structure.

## A3.12 Expected loss, cash shortfall and tail capital

The accounting cash-shortfall interpretation follows [19].

Let $D$ indicate default over a specified horizon, $E$ exposure at default and $G$ loss given default as a fraction of exposure. The random credit loss is $L=DEG$, so

$$
\begin{aligned}
E[L]
&=\Pr(D=1)E[EG\mid D=1]\\
&=\mathrm{PD}\left[
E[E\mid D=1]E[G\mid D=1]
+\operatorname{Cov}(E,G\mid D=1)\right].
\end{aligned}
$$

The familiar product $\mathrm{PD}\times\mathrm{EAD}\times\mathrm{LGD}$ follows when the exposure and severity definitions already absorb their joint expectation, or when fixed values or appropriate conditional-independence approximations justify dropping the covariance. Wrong-way dependence between drawdown and recovery makes that approximation material. For fixed EAD KES 100,000, LGD 40% and PD 5%, the simplified expected loss is KES 2,000. Applying the sensitivity risks 2.5641% and 9.5238% changes that calculation to KES 1,025.64 and KES 3,809.52; these are assumption-based scenarios rather than booked provisions.

For an accounting cash-shortfall calculation, let $C_t$ denote contractual amounts due, $R_t^{(s)}$ expected receipts including eligible recoveries in scenario $s$, $w_s$ scenario probabilities summing to one, and $d_t^{\mathrm{EIR}}$ the applicable effective-interest discount factors. A schematic probability-weighted amount is

$$
\mathrm{ECL}=\sum_s w_s\sum_t d_t^{\mathrm{EIR}}
\{C_t-R_t^{(s)}\}.
$$

The contractual cash flows, scenarios, discount rate, horizon, modifications and recoveries follow the applicable IFRS 9 measurement requirements. Twelve-month ECL concerns lifetime cash shortfalls associated with default events possible during the next twelve months; it is not simply twelve months of missing instalments. A default-time expression illustrating that distinction is

$$
\mathrm{ECL}_{12}
=\int_0^{12\,\mathrm{months}}
E[\text{discounted lifetime shortfall}\mid T_D=u]\,dF_D(u),
$$

with the credit model and accounting definition aligned to the relevant default and shortfall conventions. Receipts occurring after twelve months can enter the conditional lifetime shortfall for a default within the next twelve months.

An economic-capital convention may instead use the loss tail:

$$
\operatorname{VaR}_\alpha(L)
=\inf\{\ell:\Pr(L\le\ell)\ge\alpha\},
\qquad
\mathrm{EC}_\alpha=\operatorname{VaR}_\alpha(L)-E[L].
$$

For a single stylised loan with loss KES 40,000 with probability 5% and zero otherwise, expected loss is KES 2,000 and $\operatorname{VaR}_{0.99}=40{,}000$, giving KES 38,000 under this convention. A portfolio calculation requires dependence, concentration, exposure and recovery modelling; applicable regulatory capital is determined by its own rules. The example isolates the mathematical difference between the mean and the tail, while the research keeps simulated reject outcomes separate from actual ledger events.

*Source connection:* IFRS Foundation, “IFRS 9 Financial Instruments,” supplies the accounting objective and applicable horizon. The expectation and quantile equations above expose the assumptions behind the article's simplified product and tail-risk distinctions.

## A3.13 Evidence delivered to the human reviewer

For a candidate offer or limit, retain the posterior draws $p_a^{(b)}(x)$, the population-support label, the declared sensitivity grid and any identified action-effect draws. A 95% equal-tail risk interval is $[q_{0.025}(p_a\mid D),q_{0.975}(p_a\mid D)]$. A policy-cap probability can be calculated as

$$
\widehat{\Pr}(p_a>p_{\mathrm{cap}}\mid D)
=\frac1B\sum_{b=1}^B1\{p_a^{(b)}>p_{\mathrm{cap}}\}.
$$

The Monte Carlo uncertainty in this estimated probability depends on the effective sample size of the correlated posterior indicator draws, not simply the raw number of stored draws. A credible interval for a causal effect additionally depends on its identified treatment design. Predictive intervals include future outcome variation as well as parameter uncertainty. The interface should retain these labels, the contract and horizon, data cutoff, hierarchy and prior version, sensitivity assumptions, permitted actions and approval history. This supplies uncertainty that is useful for an actual review decision and a computational record that can be reproduced.

## A3.14 Classification diagnostics in a selectively observed portfolio

Let $r_i$ be a default-risk score, with larger values indicating greater predicted default risk. The area under the receiver operating characteristic curve (AUC) for the financed, observed population has the pairwise interpretation

$$
\begin{aligned}
\mathrm{AUC}_{S=1}
={}&\Pr(r_i>r_j\mid D_i=1,D_j=0,S_i=S_j=1)\\
&+\tfrac12\Pr(r_i=r_j\mid D_i=1,D_j=0,S_i=S_j=1).
\end{aligned}
$$

Its sample estimate averages the ranking indicator over every observed default–non-default pair. It measures ranking in the selected sample, rather than calibration or performance among unfinanced applicants. A target-population weighted ranking estimate needs the same selection-exchangeability and support conditions as the earlier transport calculation, and remains sensitive to unsupported regions.

For a declared threshold $c$, write $\widehat D=1\{r\ge c\}$ and let $G$ denote an evaluation group. The observed-population rates are

$$
\mathrm{TPR}_{g,S=1}=\Pr(\widehat D=1\mid D=1,G=g,S=1),
\qquad
\mathrm{FPR}_{g,S=1}=\Pr(\widehat D=1\mid D=0,G=g,S=1).
$$

Equal opportunity compares the first rate; equalized odds compares both. A positive default flag is different from a positive approval decision, so the recorded label convention belongs in every report. If target rates are estimated with selection weights, derive each as a ratio of weighted joint and conditioning-event probabilities. For example,

$$
\widehat{\mathrm{TPR}}_g
=\frac{\sum_i S_i\widehat e(X_i)^{-1}
  1\{G_i=g,D_i=1,\widehat D_i=1\}}
 {\sum_i S_i\widehat e(X_i)^{-1}1\{G_i=g,D_i=1\}}.
$$

This ratio requires a positive supported denominator and suitable uncertainty analysis. Zero observed defaults in a small group do not establish a perfect default-detection rate. Report group sizes, the observed or transported population, label maturity, posterior or sampling uncertainty and the sensitivity assumptions. The selection derivations explain why an apparently strong aggregate AUC or fairness statistic can coexist with uncertainty about rejected applicants.

*Source connection:* Hardt, Price and Srebro, “Equality of Opportunity in Supervised Learning,” defines the group-error criteria. The pairwise AUC identity and the weighted ratios follow from the definitions of the relevant conditional probabilities.
