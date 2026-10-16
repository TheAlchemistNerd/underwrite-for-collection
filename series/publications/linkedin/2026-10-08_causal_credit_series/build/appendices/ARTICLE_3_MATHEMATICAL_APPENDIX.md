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

## A3.6 Article 3 action term within the shared hierarchy

The complete sector, region and origination-vintage hierarchy, its Gaussian coefficient baseline, and its positive half-Student-t group-scale priors are specified in A2.5 and A2.11. This section retains the Article 3 extension for a contract-specific risk target and selective outcomes. For a declared contract $a$ and horizon $\tau$, write

$$
\begin{aligned}
D_i^a(\tau)\mid X_i&\sim\operatorname{Bernoulli}(p_{i,a,\tau}^L),\\
\operatorname{logit}(p_{i,a,\tau}^L)
&=\alpha^L+X_i^\mathsf T\beta^L
+u^L_{s(i)}+v^L_{r(i)}+w^L_{c(i)}+g^L(a,X_i).
\end{aligned}
$$

Here $s(i)$, $r(i)$ and $c(i)$ identify sector, region and origination vintage; $g^L(a,X_i)$ represents the declared action basis and any supported interactions. If the data and design do not identify an action effect, the model remains prognostic and this term is omitted or restricted accordingly. The hazard model uses its own $H$ parameters and action term $g^H(a,X_i)$, as set out in A2.6. The shared level names do not imply that logistic and hazard coefficients are equal or that the two likelihoods are jointly fitted.

The current baseline in A2.5 assigns Gaussian priors to regression coefficients and half-Student-t priors to positive group standard deviations; A2.11 contains the scale-mixture derivation and updates. The observed funded-loan likelihood alone describes outcomes in its observed population. A3.1–A3.5 specify the selection assumptions, support and sensitivity analysis needed to interpret or transport those estimates to an applicant target.

For a local Gaussian pooling illustration, take a group estimate $\widehat u=0.7$, sampling variance $1/n$ and prior variance $\sigma^2=0.04$. Using the normal-normal expression derived in A2.5, $n=10$ gives shrinkage weight $0.04/(0.04+1/10)=2/7$ and posterior mean $0.2$; $n=100$ gives weight $0.8$ and posterior mean $0.56$. This illustrates how greater group information reduces shrinkage. It is an exact calculation for the Gaussian approximation, not a closed-form posterior for the logistic model.

*Source connection:* The hierarchical modelling and partial-pooling sources are [4] and [5]; the complete common hierarchy is in A2.5.

The local action-effect symbol $g^L$ represents the fixed-horizon response denoted $h^L$ in the article body; $g^H$ represents its hazard response $q^H$. These model-specific labels preserve separate logistic and survival estimands.

## A3.7 Distinguish coefficient priors from group-scale priors

The prior roles are distinct; the normal–Gamma identity and half-Student-t scale derivations are in A2.11. In the current baseline specified in A2.5, fixed-effect coefficients have Gaussian priors, for example $\beta^m\sim N(0,B^m)$, while each $\sigma_k^m>0$ is a half-Student-t(3) prior on a sector, region or vintage group standard deviation. The half-t controls pooling through the scale of conditionally Gaussian group effects. Its degrees of freedom do not turn a regression coefficient into a Student-t variable.

A Student-t coefficient prior is a separately declared alternative or sensitivity model. For example, a coefficient-specific mixture for $\beta_j\sim\operatorname{Student\text{-}t}_3(0,s_j)$ uses $\lambda_j\sim\operatorname{Gamma}(3/2,3/2)$ and $\beta_j\mid\lambda_j\sim N(0,s_j^2/\lambda_j)$. Here $\lambda_j$ is a coefficient-specific precision. The auxiliary variables used for a half-t group scale in A2.11 instead belong to the positive scale parameter and its scale-mixture representation. These variables and updates are not interchangeable.

Accordingly, a reproducible Article 3 fit records the coefficient-prior family and scales separately from each group-scale prior, parameterisation and update. Under the registered Gaussian-coefficient baseline, the Pólya–Gamma block in A2.10 is conditionally Gaussian with fixed prior precision. Under a Student-t coefficient alternative, the same block is conditionally Gaussian only after conditioning on the coefficient-specific mixture precisions and updating them as part of the sampler. The half-t group-scale updates remain separate. A degrees-of-freedom value of three for the group-scale prior is not evidence that the alternative coefficient prior has been fitted.

*Source connection:* The prior-scale sources are discussed in A2.11, which supplies the complete mixture and auxiliary-update derivations.

## A3.8 Article 3 conditional-update check

The Pólya–Gamma identity and full Gaussian conditional derivation are given in A2.10. The following intercept-only calculation retains the Article 3 numerical check. With nine binary outcomes and one event, $\sum_i\kappa_i=1-9/2=-3.5$. Suppose the current Pólya–Gamma draws sum to $2$ and the intercept prior is $N(0,4)$, giving prior precision $1/4$. The conditional update is

$$
V_*=(2+1/4)^{-1}=4/9,
\qquad
m_*=(4/9)(-3.5)=-14/9,
\qquad
\alpha\mid\omega,y\sim N(-14/9,4/9).
$$

Thus this sampler step has conditional mean approximately $-1.5556$ and variance $0.4444$. It is one conditional draw, not the marginal fitted posterior. Posterior reporting requires validated updates of the latent variables, coefficients, hierarchy scales and any other parameters in the registered model, with convergence and effective-sample-size checks. In computation, solve using a factorisation of the positive-definite precision matrix rather than explicitly forming its inverse when feasible.

For the optional Student-t coefficient model described in A3.7, a Gaussian coefficient update is conditional on its coefficient-specific mixture precisions. The group-scale updates remain distinct and follow A2.11. This example therefore demonstrates a computational block without conflating the two prior families.

*Source connection:* Polson, Scott and Windle [9] provide the augmentation identity and conditional calculation derived in full at A2.10.

## A3.9 Align logistic and hazard outcomes for reject inference

The Article 3 logistic and event-time models can be compared only when their target event, contract, population and horizon match. The general event, competing-cause and cumulative-incidence definitions are in A1.8; the complete hazard likelihood, Cox partial likelihood and piecewise-baseline update are in A2.6. Those sections contain the derivations retained as the canonical treatments.

For a specified contract $a$, covariates $X=x$ and horizon $\tau$, define the logistic target as

$$
p_{L,a}(\tau\mid x)=\Pr\{D^a(\tau)=1\mid X=x\}.
$$

The corresponding hazard target is the default cumulative incidence $F_{H,a,D}(\tau\mid x)$ when competing terminal causes are present. In that setting, compare the logistic probability with default incidence, not with $1-S(\tau)$, which is the probability of any terminal event. A logistic endpoint described as “default by twelve months” must therefore use the same default definition and competing-exit rule as the hazard-derived twelve-month incidence. Cure or restructuring followed by possible re-default requires matching transition and terminal-event definitions as well.

The comparison also requires the same contract or action, outcome population, follow-up maturity and censoring treatment. An endpoint among originated borrowers is not the same estimand as an offer-policy outcome over all applicants. The terms $g^L(a,X)$ and $g^H(a,X)$ describe model-specific action effects; sharing an action label does not establish equal effects or a causal interpretation. Experimental or adjustment assumptions must support the relevant contrast.

This alignment does not resolve selective labels. A risk estimate fitted to funded, observed loans remains conditional on that evidence unless the selection assumptions and support in A3.2–A3.5 justify transport to the target applicant population. Matching a logistic and hazard horizon cannot supply outcomes for rejected applicants or remove sensitivity to unobserved selection.

*Source connection:* The event-time model source cited in [6] supports the hazard formulation. A1.8 defines the event and competing-risk targets, and A2.6 gives the complete hazard derivations.

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

Appendix A2.7 defines the probability-weighted discounted cash-shortfall calculation. Here the additional task is to carry selection-sensitive default estimates into the same contract, scenario and recovery definitions.

The contractual cash flows, scenarios, discount rate, horizon, modifications and recoveries follow the applicable IFRS 9 measurement requirements. Twelve-month ECL concerns lifetime cash shortfalls associated with default events possible during the next twelve months; it is not simply twelve months of missing instalments. A default-time expression illustrating that distinction is

$$
\mathrm{ECL}_{12}
=\int_0^{12\,\mathrm{months}}
E[\text{discounted lifetime shortfall}\mid T_D=u]\,dF_D(u),
$$

with the credit model and accounting definition aligned to the relevant default and shortfall conventions. Receipts occurring after twelve months can enter the conditional lifetime shortfall for a default within the next twelve months.

The quantile-based economic-capital convention is defined in Appendix A2.7. Applying it to the selected-label example gives a direct numerical comparison between mean and tail loss.

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

### Further methodological reading

Additional sources retained from the article bibliography: [21].
