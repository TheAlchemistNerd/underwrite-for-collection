---
title: "Underwrite for Collection"
subtitle: "Part 2b: Hierarchical Bayesian Underwriting, Causal Identification and Lifecycle Dependence"
author: "Neville Maloba"
email: "nevillemaloba@gmail.com"
date: "6 September 2026"
lang: "en-GB"
---

# Abstract

Part 2a ended at an evidence boundary. It produced explicit lifecycle variables, residual artificial-intelligence representations, contractual context, data-quality indicators and the exact information cutoff for an MSME credit decision. Part 2b develops the statistical architecture that receives those objects. Its champion is a hierarchical Bayesian logistic regression that estimates a defined-horizon outcome under observed policy, pools information across related but heterogeneous portfolios, retains nonlinear economic effects through governed P-splines, and controls the residual AI block through cross-fitting and regularised-horseshoe shrinkage.

The model is embedded in a wider research design. A prognostic probability describes what is likely under a stated information set and policy. A causal estimand asks what would change under a permissible alternative product or intervention. A policy rule selects an action within legal, conduct, affordability, operational and portfolio constraints. Randomised pilots provide the primary causal route where they are justified; regression discontinuity, difference-in-differences, instrumental variables, synthetic control and target-trial emulation supply narrower alternatives when their identification conditions are credible.

Fixed-horizon default is only one collection outcome. Hierarchical piecewise-exponential, competing-risk and multi-state challengers add default timing, modification, cure, durable cure, re-default, prepayment and recovery. Marginal models for exposure at default, loss severity and recovery timing then convert probability into collectible cash. Shared factors are represented before any residual copula so that economic shocks are not counted twice. Offline Pólya-Gamma or reference NUTS inference produces a signed posterior artefact for low-latency scoring. The result is a disciplined handoff from temporal evidence to intervention governance, expected loss, capital, pricing and funding.

## 1. When a probability becomes a collection question

Return to the wholesaler whose customer payment cleared on Tuesday morning but reached the lending ledger after the scheduled monitoring run. By the next week, the operational mismatch has been repaired. The facility is current, the large customer continues buying, and the business remains profitable. A statistical system looking back from month end can now see the corrected allocation. The system that advised the lender at 09:10 on Tuesday could see only the information permitted at that earlier cutoff.

Suppose that system produced a 7.4 percent probability of entering 30-day arrears within the next 60 days. The number sounds precise, yet four separate questions immediately follow. What event counts as entry into 30-day arrears? Is the forecast conditional on the existing repayment calendar and servicing policy? Does the posterior remain wide because the enterprise belongs to a thinly observed sector or because two current signals conflict? Would changing the payment date reduce the risk, or would it merely move the same shortage into another week? Which action remains suitable after affordability, customer communication, operational capacity and portfolio limits are considered?

These questions establish the statistical centre of underwriting for collection. A forecast is useful when its outcome, horizon, population, information cutoff and policy context are explicit. Its uncertainty must travel with it. An observed association becomes evidence for intervention only through a design that supports the relevant counterfactual comparison. The final action remains a governed decision, not a synonym for either prediction or causation.

Hierarchical Bayesian modelling is well suited to this architecture because it represents the uncertainty around portfolio, group and borrower-level quantities in one probability system and allows related groups to share information [1]. Hierarchical credit-risk research also demonstrates why outcome maturity and censoring require more care than labelling every account that has not yet defaulted as performing [2]. The value is not a general claim that Bayesian machinery always predicts better. It is the ability to state what has been pooled, what remains uncertain, how prior information enters, and how a posterior predictive distribution changes as evidence matures.

Part 2b therefore separates three objects:

1. **Prognostic distribution.** The champion estimates a distribution for a defined future outcome under the observed or specified operating policy. It may estimate fixed-horizon default, arrears entry, or another approved event.
2. **Causal contrast.** A trial or credible quasi-experiment estimates how an eligible product, servicing or collection intervention changes a stated outcome for a stated population.
3. **Decision policy.** The Credit Policy and Compliance Gate selects from feasible actions using model outputs, causal evidence, law, contract, affordability, conduct, capacity and portfolio constraints.

The architecture also separates a champion from challengers. The hierarchical logistic champion supplies a calibrated fixed-horizon probability. A timing challenger uses censored exposure to estimate when an event may occur. A multi-state challenger estimates transitions through arrears, modification, cure and recovery. Marginal exposure and severity models estimate the cash amount at risk and the value that may be recovered. A dependence layer asks how losses co-move after observed shared drivers have been modelled. Each component earns a role by answering a different question.

```{.mermaid layout=fullpage}
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial",
    "primaryColor": "#EAF2F8",
    "primaryTextColor": "#17324D",
    "primaryBorderColor": "#2E5E7E",
    "lineColor": "#4F6B7A",
    "secondaryColor": "#E8F5F2",
    "tertiaryColor": "#FFF4D6"
  },
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 30, "rankSpacing": 44}
}}%%
flowchart TB
    E[Part 2a evidence contract<br/>point-in-time explicit features,<br/>residual AI evidence and quality] --> O[Outcome and horizon contract<br/>episode, cutoff, maturity and policy]

    O --> C[Champion HLR<br/>calibrated fixed-horizon<br/>posterior probability]
    O --> T[Timing and multi-state challengers<br/>default, cure, re-default,<br/>prepayment and recovery]
    O --> X[Causal evidence programme<br/>randomised or identified<br/>quasi-experimental contrasts]

    C --> M[Marginal cash-risk interfaces<br/>PD, exposure, cure,<br/>LGD and recovery timing]
    T --> M
    M --> D[Shared-factor and<br/>residual-dependence layer]

    C --> G[Credit Policy and<br/>Compliance Gate]
    X --> G
    D --> P[Portfolio loss paths<br/>ECL, capital, pricing,<br/>funding and risk transfer]
    G --> A[Approved action<br/>originate, limit, support,<br/>restructure or recover]
    A --> L[Observed lifecycle outcome<br/>cash, cure, cost, harm<br/>and business continuity]
    L --> E

    classDef evidence fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.6px;
    classDef model fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.6px;
    classDef decision fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.8px;
    class E,O,L evidence;
    class C,T,X,M,D,P model;
    class G,A decision;
```

**Figure 1: Statistical architecture for underwriting toward collectible outcomes.** The champion, timing and state challengers, causal evidence programme, dependence model and policy gate perform distinct jobs. Realised cash and customer outcomes return through the point-in-time evidence process rather than entering earlier decisions retrospectively.

The figure is also a safeguard against modelling escalation. Artificial intelligence enters through the residual evidence contract defined in Part 2a when it improves future-period calibration or decision value beyond the explicit model. A copula is built on calibrated marginal probabilities. A causal forest follows an identified intervention design. A posterior distribution informs a separate decision rule. The chain remains useful because each interface states what the next component can legitimately consume.

The human purpose remains visible. A lender wants to distinguish an enterprise whose current signal reflects a repairable timing mismatch from one whose cash-generating capacity has deteriorated, and to do so early enough for a proportionate response. The borrower benefits when uncertainty is treated as uncertainty rather than silently converted into an adverse label. The collections team benefits when the model forecasts specific states and cash consequences instead of producing a rank with no operational meaning. Finance and risk teams benefit when the same episode definitions can later reconcile default, exposure, cure and recovery with expected loss and capital.

## 2. Observation units, horizons and selective outcomes

The model does not score an abstract enterprise detached from a facility. Its principal record is a borrower-product-episode-decision tuple:

\[
\mathcal O_i=(b_i,p_i,e_i,t_{0i},H_i,\pi_i,\mathcal I_i),
\]

where \(b_i\) identifies the enterprise or connected borrower unit, \(p_i\) the product, \(e_i\) the legally and operationally defined credit episode, \(t_{0i}\) the decision cutoff, \(H_i\) the forecast horizon, \(\pi_i\) the policy under which future outcomes will be observed, and \(\mathcal I_i\) the information set available at the cutoff. Product and episode definitions matter. An invoice-finance draw against a verified debtor, an overdraft review, an asset-finance instalment and a working-capital term loan do not share the same exposure path merely because the borrower is the same.

For product \(p\) and horizon \(H_p\), the champion outcome is:

\[
Y_i^{(H_p)}=
\mathbf 1\!\left\{\tau_i^{D}-t_{0i}\leq H_p\right\},
\]

where \(\tau_i^{D}\) is the first time the episode satisfies the approved default definition. The definition must specify the event, materiality threshold, cure treatment, product scope and relationship to modification or forbearance. It must also state whether the intended prediction is first default, any default, entry into a defined arrears state, or another outcome. A probability without that contract cannot be compared across models or passed reliably into accounting and portfolio analysis.

The label is mature only when follow-up reaches the end of the horizon or the event occurs earlier. If the training cutoff is \(T\), an episode with no observed default contributes a known negative champion label only when:

\[
t_{0i}+H_p\leq T.
\]

An open episode whose horizon extends beyond \(T\) is right-censored. It is available to a compatible timing model with its observed at-risk interval; it is not converted into a successful repayment. This distinction is especially important when products have different maturities or when a recently originated vintage has had less time to deteriorate. Credit research has long noted that censoring can make future defaulters appear as non-defaulters when classification datasets are constructed too early [2].

One enterprise may contribute repeated decisions, facilities and matured episodes. Those records are statistically dependent through common management, cash flows, ownership, sector and prior lender actions. Randomly distributing them across training and validation folds would let the model learn from another version of the same enterprise. The default validation unit is therefore the connected borrower or economic group. Time-forward validation then holds out later decisions as well as later outcomes. Institution-held-out validation is added when the intended claim concerns transport to another lender.

The binary champion does not collapse the lifecycle into one permanent label. A separate outcome vector records:

\[
\mathbf Y_i^{\mathrm{life}}=
\left(
T_i^{A},
T_i^{M},
T_i^{C},
I_i^{DC},
T_i^{RD},
T_i^{D},
R_i(\cdot),
C_i^{\mathrm{work}},
H_i^{\mathrm{cust}}
\right),
\]

where \(T^A\) is time to arrears, \(T^M\) time to modification, \(T^C\) time to cure, \(I^{DC}\) indicates durable cure over a pre-specified window, \(T^{RD}\) time to re-default, \(T^D\) time to default, \(R(\cdot)\) the recovery cash-flow path, \(C^{\mathrm{work}}\) workout and contact cost, and \(H^{\mathrm{cust}}\) defined customer-harm or complaint outcomes. These quantities feed different models and decisions. They share the episode spine, which makes reconciliation possible.

Historical approval policy creates another missing-outcome problem. Repayment performance is observed principally for applicants whom the lender approved and who accepted and drew the product. The earlier decision therefore influences which labels exist. This is the selective-label problem: observed outcomes are not a random sample of all applicants, because the decision process determines who becomes observable [3]. Declined applications should not be relabelled as defaults or non-defaults. Likewise, bureau performance on another lender's product may add permitted evidence but does not recreate the exact contract, exposure and intervention path that the declined facility would have produced.

Let \(S_i=1\) denote that the target outcome becomes observable under the historical process. Model development learns directly from:

\[
P\!\left(Y_i=1\mid X_i,S_i=1,\pi_{\mathrm{hist}}\right),
\]

while a new policy may seek a quantity for a wider population. Transport from the first to the second requires support and assumptions that the approved-only sample cannot manufacture. The programme therefore combines four disciplined routes: retain the champion within its validated population; use shadow scoring to observe score distributions without changing approvals; use external or later outcomes where their definitions are compatible and lawful; and create prospective evidence through carefully bounded randomised or quasi-experimental designs where genuine uncertainty and customer protection permit them.

Selection also continues after disbursement. A limit reduction changes future exposure. A restructuring changes payment opportunities. Intensive contact may change both repayment and complaints. A borrower who prepays leaves the default risk set. A sold or refinanced facility may become unobservable to one institution. Every action is therefore recorded with its assignment mechanism, timing and eligibility. Part 2b models outcomes conditional on that history; Part 6 will design the prospective programme that can learn which actions caused better outcomes.

The observation contract now gives the champion a clear task. It receives only information available at \(t_0\), forecasts a matured product-specific event over \(H_p\) under policy \(\pi\), pools evidence across registered hierarchies, and reports uncertainty. It does not need to answer the timing, intervention and portfolio-dependence questions alone. Those questions receive their own likelihoods and validation tests in the sections that follow.

## 3. The champion hierarchical Bayesian logistic model

The champion begins with a probability statement rather than a score transformation. For matured episode \(i\), let:

\[
Y_i\sim\operatorname{Bernoulli}(p_i),
\qquad
\operatorname{logit}(p_i)=\eta_i.
\]

The linear predictor is block structured:

\[
\begin{aligned}
\eta_i={}&\alpha_{p[i]}
+\mathbf q_i^{\mathsf T}\boldsymbol\beta_z
+\widetilde{\mathbf h}_i^{\mathsf T}\boldsymbol\beta_h
+\mathbf r_i^{\mathsf T}\boldsymbol\gamma\\
&+u_{s[i]}+v_{g[i]}+w_{j[i]}+c_{k[i]}+\delta_{t[i]}
+\mathbf m_i^{\mathsf T}\boldsymbol\xi .
\end{aligned}
\]

Each block has one declared job:

- \(\alpha_{p[i]}\) is the intercept for product \(p\), stated at the registered reference levels and centred feature values.
- \(\mathbf q_i=Q(\mathbf z_i)\) contains centred linear terms and P-spline bases for explicit lifecycle features.
- \(\widetilde{\mathbf h}_i\) is the cross-fitted residual AI representation delivered under the Part 2a contract.
- \(\mathbf r_i\) is a small, pre-specified interaction design.
- \(u_s,v_g,w_j,c_k\) are partially pooled sector, geography, institution and origination-cohort effects.
- \(\delta_t\) is an approved calendar-time or regime effect.
- \(\mathbf m_i\) contains contractual and data-quality metadata that should affect interpretation but are neither behavioural features nor neural evidence.

The explicit block gives the model its economic spine. Candidate quantities include net settled cash generation over registered windows, repayment velocity, cash-flow asymmetry, debt-to-liquidity measures, account volatility, utilisation, days since liquidity depletion, arrears transitions, customer-receipt concentration, operating-obligation coverage and time since the most recent verified business activity. Every transformation retains its unit, window, permitted population and missingness rule from Part 2a. A ratio whose numerator covers seven days and denominator covers ninety days does not silently change windows during model development. A facility-balance variable does not become an enterprise cash-flow variable because both are denominated in shillings.

The hierarchy reflects repeated structures in the lending problem rather than a search for arbitrary clusters. Sector pools enterprises exposed to related demand and input conditions. Geography may capture lawful and sufficiently aggregated local conditions after proxy and fairness review. Institution effects support research across participating lenders without pretending that their products, populations and definitions are identical. Cohort effects represent origination vintages that share underwriting policy and macroeconomic conditions. Product intercepts keep a short working-capital facility from inheriting the baseline rate of a longer asset-finance contract.

For a generic sector effect \(u_s\), a non-centred representation is:

\[
u_s=\sigma_u z_s,
\qquad
z_s\sim\mathcal N(0,1),
\qquad
\sigma_u\sim\operatorname{HalfStudent}\text{-}t(\nu_u,0,a_u).
\]

Equivalent structures apply to geography, institution and cohort effects. The group effects are centred, for example through a sum-to-zero constraint after transformation, so that the intercept retains its meaning. Hyperprior scales are calibrated through prior-predictive simulation on the log-odds and probability scales. A Half-Student-\(t\) prior with finite degrees of freedom can retain substantial mass for genuine heterogeneity while controlling the extreme tail more tightly than a Half-Cauchy. A Half-Normal may be a useful sensitivity specification where large group deviations are implausible. The choice is documented and tested because scale-prior behaviour can materially affect weakly identified hierarchical models.

Partial pooling is easiest to understand through the posterior precision. In a Gaussian approximation for an identified group effect, the posterior location has the form:

\[
\widehat u_s
\approx
\frac{I_s}{I_s+\sigma_u^{-2}}\widehat u_s^{\mathrm{local}}
+
\frac{\sigma_u^{-2}}{I_s+\sigma_u^{-2}}\,0,
\]

where \(I_s\) represents the group's likelihood information. A group with little matured evidence remains close to the collective mean and carries a wider posterior. A well-observed group can move away when its data support differentiation. In the actual logistic hierarchy the update is joint rather than this scalar approximation, but the economic interpretation remains: differentiation is earned through information rather than assigned because a segment name sounds distinctive.

Random slopes are reserved for relationships with a prior economic reason and adequate cross-group support. If short-term debt-to-liquidity pressure is expected to operate differently across products, the model may use:

\[
\beta_{z,p}=\bar\beta_z+L_{\Omega}\operatorname{diag}(\boldsymbol\sigma_\beta)\mathbf z_p,
\qquad
\mathbf z_p\sim\mathcal N(\mathbf 0,\mathbf I),
\]

where \(L_{\Omega}\) is the Cholesky factor of a correlation matrix. Marginal scales and correlations receive separate priors. This separates magnitude from correlation, while the non-centred form improves computation when group information is weak. Random slopes over the residual AI embedding advance only through a dedicated challenger with adequate group evidence and dimensional control.

Interactions also follow economic ownership. A pre-specified term may represent high revolving utilisation combined with declining settled receipts, or concentration in one customer combined with a longer settlement delay. Strong heredity requires the associated main effects to remain in the model when an interaction is active. Interaction coefficients receive their own shrinkage scale. This prevents the neural block, spline basis and a broad interaction search from competing to express the same local curvature.

The model produces a posterior distribution, not only a fitted coefficient vector:

\[
p_i^{(m)}=\operatorname{logit}^{-1}(\eta_i^{(m)}),
\qquad m=1,\ldots,M.
\]

For a known group, the draw includes its posterior effect. For a genuinely new group, prediction integrates over the registered population distribution or a governed higher-level mapping rather than assigning the most favourable observed group. The output contract can therefore report posterior mean and median PD, credible intervals, tail probabilities above policy thresholds, and uncertainty decomposed by data, group and parameter sources where the approximation supports it.

Calibration is estimated on future or cross-fitted predictions, separately by product when evidence permits:

\[
\operatorname{logit}\left(p_{i,\mathrm{cal}}^{(m)}\right)
=a_p+b_p\operatorname{logit}\left(p_i^{(m)}\right),
\qquad b_p>0.
\]

The calibration intercept \(a_p\) corrects systematic level error and slope \(b_p\) corrects over- or under-dispersion. They are stored with their estimation window and uncertainty. Calibration is fitted on future or cross-fitted outcomes and reported alongside ranking, subgroup stability and time-split integrity.

```{.mermaid layout=fullpage}
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial",
    "primaryColor": "#EAF2F8",
    "primaryTextColor": "#17324D",
    "primaryBorderColor": "#2E5E7E",
    "lineColor": "#4F6B7A",
    "secondaryColor": "#E8F5F2",
    "tertiaryColor": "#FFF4D6"
  },
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 32, "rankSpacing": 44}
}}%%
flowchart TB
    E[Point-in-time evidence contract<br/><br/>Explicit lifecycle features and P-splines<br/>Residual cross-fitted AI representation<br/>Registered strong-heredity interactions<br/>Contract and data-quality metadata]
    H[Cross-classified hierarchy<br/><br/>Product and sector<br/>Geography and institution<br/>Origination vintage and calendar time]
    E --> ETA[HLR linear predictor<br/>identified block structure]
    H --> ETA
    ETA --> POST[Posterior fixed-horizon PD<br/>mean, interval and tail probability]
    POST --> CAL[Out-of-time product calibration]
    CAL --> ART[Signed scoring output<br/>versions, support, quality and reasons]
    ART --> GATE[Credit Policy and<br/>Compliance Gate]

    classDef evidence fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.5px;
    classDef hierarchy fill:#F1EAF8,stroke:#6B4C8A,color:#30203F,stroke-width:1.5px;
    classDef model fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.7px;
    classDef decision fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.8px;
    class E evidence;
    class H hierarchy;
    class ETA,POST,CAL,ART model;
    class GATE decision;
```

**Figure 2: Champion HLR with assigned evidence, hierarchy and calibration interfaces.** Explicit lifecycle variables, residual AI evidence, interactions, metadata and group effects enter through separate blocks. The posterior remains an inferential output until calibration, artefact controls and the policy gate are applied.

This champion can be benchmarked against a conventional scorecard, penalised logistic regression and tree-based model using the same point-in-time sample. The comparison is empirical. The champion earns acceptance through calibrated future-period probabilities, stable subgroup behaviour, decision value, reconstructibility and operational fit. Hierarchical structure contributes a principled way to share information; it does not excuse weak labels, incomplete outcomes or a model whose cash implications cannot be reconciled.

## 4. Governed nonlinearities, hierarchy and time

Many collection relationships are nonlinear. A modest fall in settled receipts may be absorbed by cash reserves, while a similar fall near the repayment boundary may sharply increase arrears risk. Revolving utilisation may carry limited information at low levels and become more consequential when headroom disappears. Repayment velocity can distinguish a business returning toward schedule from one moving away, yet the effect may flatten once the account is comfortably current. A single linear coefficient imposes one slope across all these regimes.

The champion uses a P-spline where nonlinearity is supported. P-splines combine a B-spline basis with an explicit discrete penalty on adjacent coefficients [4]. For continuous feature \(x\), a cubic basis gives:

\[
f(x)=\sum_{k=1}^{K}B_{k,3}(x)\zeta_k=\mathbf B(x)^{\mathsf T}\boldsymbol\zeta.
\]

A second-order difference penalty controls curvature:

\[
\Delta^2\zeta_k=\zeta_k-2\zeta_{k-1}+\zeta_{k-2},
\qquad
\Delta^2\boldsymbol\zeta\mid\tau_f
\sim\mathcal N(\mathbf 0,\tau_f^2\mathbf I).
\]

Equivalently, if \(D_2\) is the second-difference matrix, the prior contribution is proportional to:

\[
\exp\!\left[-\frac{1}{2\tau_f^2}
\boldsymbol\zeta^{\mathsf T}D_2^{\mathsf T}D_2\boldsymbol\zeta\right].
\]

The B-spline basis controls representation and the penalty controls roughness. A reasonably rich, fixed basis therefore need not select one fragile set of a few knots. The smoothing scale determines how much curvature the data may support. The penalty has a null space, so the implementation explicitly separates or constrains the unpenalised constant and linear components. The fitted smooth is centred over the development population:

\[
\sum_{i\in\mathcal D_{\mathrm{train}}}f(x_i)=0,
\]

which prevents the smooth from redefining the product intercept. If a QR, eigen or Demmler-Reinsch transformation improves numerical conditioning, the penalty matrix and back-transformation move with the basis. Orthogonalising a basis while leaving its prior penalty behind would silently create a different model.

Every accepted smooth has a versioned specification: feature definition, unit, transformations, spline degree, interior and boundary knots, validated support, penalty order, smoothing-scale prior, centring rule, missingness path, clipping policy and reason-code representation. Boundary handling is especially important. A smooth curve inside observed support is not evidence that extrapolation beyond the largest witnessed debt-to-liquidity value is benign. The service flags out-of-support values and applies a governed conservative or referral rule rather than extending an attractive tail mechanically.

Product variation is added through pooled deviations:

\[
f_p(x)=f_0(x)+g_p(x),
\qquad
D_2\boldsymbol\zeta_{g,p}
\sim\mathcal N(\mathbf 0,\tau_g^2\mathbf I).
\]

Sparse products remain near the common shape, while sufficiently observed products may differ. Monotonicity is imposed only when the economic definition, contractual mechanism and empirical evidence justify it. For example, increasing obligations relative to verified liquidity may reasonably be expected to increase risk over a defined range, but data errors, numerator changes and product restructuring can complicate an absolute global constraint.

Calendar and vintage variation require a similarly explicit choice. An exchangeable time effect is suitable when periods share a distribution without an ordered dependence. A first-order random walk represents local drift:

\[
\delta_t\mid\delta_{t-1},\sigma_\delta
\sim\mathcal N(\delta_{t-1},\sigma_\delta^2).
\]

An AR(1) effect represents movement around a long-run level:

\[
\delta_t-\mu_\delta
=\rho(\delta_{t-1}-\mu_\delta)+\epsilon_t,
\qquad
\epsilon_t\sim\mathcal N(0,\sigma_\delta^2),
\quad |\rho|<1.
\]

Under a stationary initial distribution, the marginal variance is \(\sigma_\delta^2/(1-\rho^2)\). A RW1 has no mean-reverting level; an AR(1) does. Neither is selected because a narrative labels the economy as drifting or mean reverting. Prior-predictive trajectories, available time depth, held-out calibration and posterior identifiability determine whether an ordered effect adds value beyond observable macroeconomic variables and cohort intercepts. Appendix A preserves the related B-spline plus RW1 and B-spline plus AR(1) coefficient-prior alternatives for direct comparison.

Binning remains useful for diagnostic plots and operational summaries. It can reveal sparse tails, non-monotonic empirical rates and support gaps when uncertainty and sample counts are shown. It is not the default likelihood transformation. Bernoulli observations may be collapsed exactly to a Binomial count only when the design row, hierarchy assignments, exposure definition and event probability are identical:

\[
Y_g=\sum_{i\in g}Y_i
\sim\operatorname{Binomial}(n_g,p_g).
\]

Grouping continuous features into approximate cells changes the model because members no longer share an identical \(p_g\). Any such quantisation is benchmarked against individual records and labelled an approximation. The champion retains the continuous P-spline representation at scoring time.

The nonlinear and time structures now remain rich but bounded. Each has an economic owner, an identification constraint, a prior-predictive interpretation, a validated support range and a future-period test. That discipline allows curvature and drift to improve collection forecasts without turning flexibility into an untraceable search across every possible shape.

## 5. Residual AI evidence and regularised horseshoe shrinkage

Part 2a assigned named financial quantities to the explicit path and reserved the AI branch for residual sequence information. This distinction matters because a neural encoder can reconstruct familiar ratios from the same underlying account events even when the ratios are not supplied as named columns. If both representations enter the HLR without control, a declining cash pattern may appear in earnings velocity, a spline over debt-to-liquidity, several transaction-window features and multiple embedding dimensions. Coefficients then compete to explain one economic movement, which weakens stability and reason attribution.

The AI representation is therefore built and tested as an incremental evidence block. Let \(\mathbf h_i\in\mathbb R^d\) be a low-dimensional bottleneck produced from the authorised sequence history. For validation fold \(k(i)\), the encoder, bottleneck selection and residualiser are trained without the fold's borrowers and without future periods. The residual representation is:

\[
\widetilde{\mathbf h}_i
=
\mathbf h_i-\widehat{\mathbb E}_{-k(i)}
\left[\mathbf h_i\mid\mathbf q_i,\mathbf m_i\right].
\]

The projection design includes the explicit P-spline basis and metadata that the AI block could reproduce. A linear ridge projection is often easier to audit; a nonlinear residualiser may be benchmarked when the linear projection leaves material predictable structure. In either case, the mapping is fitted only on training data and replayed unchanged on the held-out fold. Borrower grouping and time-forward splitting remain active. The method borrows the discipline of cross-fitting, which separates nuisance-model fitting from held-out evaluation [5], while its role here is representational control within a prognostic architecture.

Residualisation is tested rather than assumed. The development report measures canonical correlations and out-of-fold predictability between \(\widetilde{\mathbf h}\) and the explicit design, examines condition numbers and posterior correlations, and checks whether explicit effect shapes change materially when the AI block is added. A small remaining correlation can be acceptable because finite samples and changing populations prevent perfect geometric orthogonality. The objective is stable incremental information, not a ceremonial zero in one development matrix.

Optional whitening addresses a different problem. If \(S_h\) is the training-fold covariance of residual embeddings, a regularised transform may define:

\[
\mathbf h_i^{\star}
=
\left(S_h+\epsilon I\right)^{-1/2}
\widetilde{\mathbf h}_i.
\]

Whitening reduces scale and correlation within the residual AI block. It does not project the block away from explicit variables and does not remove confounding. The transform, regularisation \(\epsilon\), retained dimensions and sign convention are stored in the artefact. Because embedding axes may rotate when an encoder is retrained, monitoring includes representation-alignment and ablation tests rather than interpreting one latent coordinate as a permanent business concept.

A regularised horseshoe prior controls the residual coefficient vector. The original horseshoe combines a global shrinkage scale with local scales, concentrating weak signals near zero while retaining heavy tails for stronger effects [6]. The regularised form adds a finite slab and a principled way to encode expected sparsity, which is useful for logistic models under separation or weak identification [7]. One parameterisation is:

\[
\begin{aligned}
\beta_{h,j}\mid\tau,\widetilde\lambda_j
&\sim\mathcal N(0,\tau^2\widetilde\lambda_j^2),\\
\widetilde\lambda_j^2
&=\frac{c^2\lambda_j^2}{c^2+\tau^2\lambda_j^2},\\
\lambda_j&\sim\operatorname{C^+}(0,1),
\end{aligned}
\]

where \(\tau\) controls global sparsity, \(\lambda_j\) allows local escape from shrinkage and \(c\) limits the variance of the largest coefficients through a finite slab. The prior expectation for the effective number of non-negligible dimensions informs \(\tau\); it is set with reference to sample size, event prevalence and bottleneck dimension. The slab scale is examined on the log-odds and probability scales so that a weakly informative value corresponds to plausible risk movements.

Continuous shrinkage rarely makes a coefficient exactly zero. Importance is therefore assessed through posterior contribution, ablation and stability, not through a claim that the prior has performed automatic discrete selection. The explicit coefficients, residual AI coefficients, interactions and group deviations receive separate prior families or scales. This prevents a wide AI block from determining how strongly an economically necessary contractual variable is regularised.

Four nested models form the minimum comparison:

1. Explicit linear and contractual baseline.
2. Explicit baseline plus governed P-splines and hierarchy.
3. Hierarchical model plus unadjusted AI bottleneck, used to diagnose duplication.
4. Hierarchical model plus cross-fitted residual AI and regularised horseshoe.

The residual model advances only if it improves out-of-time log score or Brier score, calibration, tail outcomes or defined decision value without unacceptable subgroup instability. If its incremental contribution decays, the explicit model remains a fully operational champion or fallback. This creates an architecture in which artificial intelligence can add temporal evidence while the lender retains a coherent model when that contribution is unavailable or no longer stable.

## 6. Pólya-Gamma offline inference and the production artefact

The HLR posterior is computationally demanding because the logistic likelihood is not Gaussian in its coefficient vector. Pólya-Gamma augmentation supplies a useful offline inference strategy for the complete hierarchy [8]. It introduces one latent variable per Bernoulli or Binomial likelihood contribution and converts the coefficient block into a Gaussian conditional while preserving the logistic model and its partial pooling.

For a likelihood contribution with linear predictor \(\psi_i=\mathbf x_i^{\mathsf T}\boldsymbol\theta\), outcome \(y_i\in\{0,1\}\), and \(\kappa_i=y_i-\tfrac12\), the Pólya-Gamma identity gives:

\[
\frac{\exp(y_i\psi_i)}{1+\exp(\psi_i)}
=
\frac{1}{2}\exp(\kappa_i\psi_i)
\int_0^\infty
\exp\!\left(-\frac{\omega_i\psi_i^2}{2}\right)
p(\omega_i)\,d\omega_i,
\]

with:

\[
\omega_i\mid\psi_i\sim\operatorname{PG}(1,\psi_i).
\]

Conditional on \(\boldsymbol\omega\), the likelihood kernel is Gaussian in \(\boldsymbol\theta\). Stack the design rows in \(X\), define \(\Omega=\operatorname{diag}(\omega_1,\ldots,\omega_n)\), and use a Gaussian prior \(\boldsymbol\theta\sim\mathcal N(\mathbf m_0,V_0)\). The coefficient conditional is:

\[
V_n=\left(X^{\mathsf T}\Omega X+V_0^{-1}\right)^{-1},
\qquad
\mathbf m_n
=V_n\left(X^{\mathsf T}\boldsymbol\kappa+V_0^{-1}\mathbf m_0\right),
\]

\[
\boldsymbol\theta\mid\boldsymbol\omega,\cdots
\sim\mathcal N(\mathbf m_n,V_n).
\]

In the full HLR, \(\boldsymbol\theta\) can contain product intercepts, explicit linear terms, P-spline coefficients, residual AI coefficients, registered interactions and Gaussian hierarchical or time effects. Sparse P-spline penalties and Gaussian Markov structures can therefore enter the precision matrix directly. A singular difference penalty is combined with proper priors or constraints for its null-space components so that the joint update remains identified.

The model is conditionally conjugate rather than fully closed form. Pólya-Gamma variables must be updated. Hierarchy scales, spline smoothing scales, regularised-horseshoe global and local scales, covariance correlations, AR persistence and calibration parameters retain their own conditional, slice, Metropolis, Hamiltonian or other validated updates. A blocked sampler may update strongly coupled coefficients jointly while using sparse Cholesky factorisation, conjugate-gradient methods or other tested linear algebra. Prior choices for group scales follow the sensitivity discipline developed for hierarchical variance parameters [9].

NUTS remains the reference comparator. On a representative development sample, the team compares posterior means, intervals, tail probabilities, group shrinkage, calibration and predictive quantities from Pólya-Gamma blocked Gibbs with a well-diagnosed NUTS fit. It also records wall-clock time, memory, effective sample size per second, numerical precision and sensitivity under sparse defaults or separation. Agreement is assessed on decisions and posterior functionals, not only on individual coefficients whose parameterisations may differ.

The production scoring path does not run either sampler. It consumes an approved posterior artefact. Three cadences remain distinct:

- **Event-time evidence refresh** updates the point-in-time state when authorised source events arrive.
- **Online score refresh** evaluates the accepted feature and hierarchy mappings against a signed posterior summary or representative draws.
- **Offline model refresh** re-estimates parameters after a scheduled review or a governed trigger, completes validation, and publishes a new artefact only after approval.

```{.mermaid layout=fullpage}
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial",
    "primaryColor": "#EAF2F8",
    "primaryTextColor": "#17324D",
    "primaryBorderColor": "#2E5E7E",
    "lineColor": "#4F6B7A",
    "secondaryColor": "#E8F5F2",
    "tertiaryColor": "#FFF4D6"
  },
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 32, "rankSpacing": 43}
}}%%
flowchart TB
    subgraph OFFLINE[Governed offline estimation]
        direction TB
        D[Point-in-time development data<br/>mature labels and grouped folds] --> F[Fit explicit, spline,<br/>hierarchy and AI transforms]
        F --> I[Posterior inference<br/>Pólya-Gamma Gibbs and<br/>reference NUTS benchmark]
        I --> V[Technical, temporal,<br/>fairness and decision validation]
        V --> A{Approval gate}
        A -->|Accepted| S[Signed posterior artefact]
        A -->|Revise| F
    end

    subgraph ARTIFACT[Versioned artefact contents]
        direction TB
        S --> SC[Schema and support ranges]
        S --> TR[Splines, residualiser,<br/>whitening and hierarchy maps]
        S --> PO[Posterior summaries or draws,<br/>calibration and uncertainty rules]
        S --> GO[Reason mappings, fallback,<br/>expiry and rollback]
    end

    subgraph ONLINE[Low-latency production path]
        direction TB
        E[Current eligible evidence] --> R[Replay approved transformations]
        SC --> R
        TR --> R
        PO --> Q[Compute calibrated PD,<br/>interval and tail quantities]
        R --> Q
        GO --> Q
        Q --> G[Credit Policy and<br/>Compliance Gate]
        G --> L[Decision and outcome ledger]
    end

    L -. matured evidence for<br/>the next governed refresh .-> D

    classDef evidence fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.5px;
    classDef model fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.6px;
    classDef decision fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.8px;
    class D,E,L,SC,TR,PO,GO evidence;
    class F,I,V,S,R,Q model;
    class A,G decision;
```

**Figure 3: Offline posterior estimation and low-latency scoring remain separate.** The signed artefact carries every transformation required to reproduce the accepted model. Current evidence may refresh a score without retraining, while matured outcomes return through a governed development cycle.

The artefact contains model and data-schema versions, feature definitions, spline basis and penalty metadata, encoder and residualiser versions, whitening transform if used, hierarchy mappings, priors, posterior draws or approved analytic summaries, calibration parameters, support limits, uncertainty rules, reason mappings, validation status, effective and review dates, and fallback and rollback identifiers. A new group is scored through the approved population hierarchy. A missing AI representation routes to the tested explicit-only fallback. An out-of-support explicit variable is recorded and handled according to policy rather than silently clipped without trace.

This arrangement makes computational sophistication compatible with operational control. The sampler can use CPUs, GPUs or specialised sparse linear algebra according to the validated implementation. The underwriting request receives a deterministic, replayable interface whose result can be reconstructed from the same artefact and point-in-time evidence. Computation therefore strengthens the model without placing an adaptive, unaudited posterior fit inside a customer interaction.

## 7. Prognosis, intervention effects and policy value

The champion model forecasts what tends to happen under the lending and servicing policy represented in its development data. That forecast can identify an MSME whose cash conversion is weakening, whose repayment velocity has slowed, or whose exposure is becoming difficult to service. It cannot, by itself, establish whether a payment holiday, a due-date change, a smaller revolving limit, a collections message, or a restructuring offer will improve the outcome. The intervention changes the path being predicted. This is why the collection architecture carries prognosis and causal learning on separate, connected rails.

For an eligible episode \(i\), let \(A_i\in\mathcal A\) denote an intervention assigned at the decision time and let \(Y_i(a)\) be the potential outcome that would be observed under action \(a\). A binary average treatment effect at horizon \(H\) is

\[
\tau(H)=\mathbb E\left[Y_i(1)-Y_i(0)\right].
\]

The outcome can instead be a durable cure indicator, days in arrears, net recovery value, or a customer-harm measure. The protocol must state the population, treatment, comparator, assignment unit, decision time, outcome, horizon, estimand and analysis set. For example, an operational question may be: among otherwise eligible Kenyan micro and small enterprises entering 1 to 7 days past due, what is the intention-to-treat effect of a one-cycle flexible repayment offer, compared with standard servicing, on durable cure by day 60 and re-default by day 120? The predictive PD is useful for stratification and precision. The random assignment identifies the effect.

Randomised pilots are the preferred route where uncertainty is genuine, the intervention is lawful and ethically supportable, and no borrower is denied a required protection. Cluster assignment can reduce contamination when relationship managers or branches cannot reliably deliver different scripts to adjacent customers. Individual assignment is more efficient when the treatment is digitally delivered and interference is limited. Randomisation is recorded before exposure, allocation is auditable, and primary outcomes and subgroup analyses are pre-specified. Intention-to-treat preserves the value of assignment; treatment-on-the-treated analysis additionally requires a defensible instrument or compliance model.

Existing experiments show why contract design deserves this discipline. A Kenyan field experiment with micro-distributors compared a standard fixed-repayment loan with performance-contingent microequity and mutuality designs, illustrating that finance can share business-state risk rather than place the entire adjustment burden on a fixed instalment [10]. Evidence from Bangladesh similarly studies repayment flexibility and enterprise risk taking under a specific microcredit setting [11]. These studies do not prescribe one universal Kenyan bank product. They demonstrate a more important proposition for the present architecture: repayment structure is an intervention that can be assigned, measured and learned from, rather than treated as an invisible constant behind a default label.

When randomisation is not available, a quasi-experiment begins with an explicit source of identifying variation. A regression-discontinuity design estimates a local effect around a threshold only if potential outcomes vary continuously at the cutoff, the running variable is not precisely manipulated, and the policy on each side is stable. Bandwidth, functional form, density, covariate continuity and alternative-cutoff tests accompany the estimate [12]. It is particularly relevant when a registered score threshold changes a limit or support offer, although the result applies locally to cases near that threshold.

A difference-in-differences design can study a staggered servicing or product rollout when untreated potential-outcome trends are credible. Group-time effects, anticipation windows and appropriate comparison cohorts are required because a single two-way fixed-effects coefficient can blend different treatment timings. Pre-trend and event-study evidence, composition stability and sensitivity to concurrent changes form part of the design [13]. Synthetic control can construct a weighted comparison for a branch, region or platform rollout when one aggregate unit is treated and a sufficiently long pre-period and donor pool exist [14]. Target-trial emulation provides a broader protocol for observational comparisons: specify eligibility, treatment strategies, assignment, start of follow-up, outcome, causal contrast and analysis before aligning the observational records [15].

An instrumental-variable route may be considered when an operational mechanism shifts treatment receipt without directly shifting the outcome except through that treatment. Queue rotation, randomised encouragement or a capacity rule can sometimes supply such variation. Relevance, exclusion, independence and monotonicity are substantive claims, not labels inferred from a strong first stage. The resulting local effect belongs to the population whose treatment changes because of the instrument.

Heterogeneous treatment effects follow identification. A causal forest or hierarchical interaction model can estimate how a validated effect varies across pre-treatment characteristics [16]. Policy learning can then search for a constrained allocation rule that maximises an explicitly defined value function [17]. Both stages use held-out or cross-fitted predictions, overlap diagnostics and uncertainty. A subgroup with a high predicted default probability is not automatically the subgroup with the largest benefit from support. Conversely, a lower-risk enterprise may yield a large, low-cost improvement from a small timing adjustment.

The policy value must include both sides of the ledger. Let \(a\in\mathcal A_i\) be a feasible action and let \(L_i(a)\), \(C_i(a)\), \(H_i(a)\) and \(O_i(a)\) denote expected credit loss, intervention cost, customer-harm cost and operational burden under that action. A simple research objective is

\[
a_i^{\star}
=\arg\min_{a\in\mathcal A_i}
\mathbb E\!\left[
L_i(a)+C_i(a)+\lambda_H H_i(a)+\lambda_O O_i(a)
\mid \mathcal I_i
\right].
\]

The weights and feasible set are governed policy choices. The exercise reports value by borrower segment, product, institution and economic state, together with distributional and conduct outcomes. It also monitors interference, non-compliance, attrition, delayed maturity, repeat assignment, contact fatigue and multiplicity. A pilot stops or adapts under pre-specified safety and operational rules, while its statistical analysis preserves the original estimand.

```{.mermaid layout=fullpage}
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial",
    "primaryColor": "#EAF2F8",
    "primaryTextColor": "#17324D",
    "primaryBorderColor": "#2E5E7E",
    "lineColor": "#4F6B7A",
    "secondaryColor": "#E8F5F2",
    "tertiaryColor": "#FFF4D6"
  },
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 34, "rankSpacing": 46}
}}%%
flowchart TB
    Q[Collection question<br/>population, action, comparator,<br/>outcome and horizon] --> B[Pre-treatment evidence<br/>and eligibility]

    B --> P[Prognostic rail<br/><br/>Champion HLR risk and uncertainty<br/>under the observed policy<br/>Stratification and precision adjustment]
    B --> D{Causal design route}
    D -->|Genuine equipoise| R[Randomised pilot<br/>individual or cluster assignment]
    D -->|Identified natural variation| QX[Quasi-experimental programme<br/><br/>Regression discontinuity<br/>Difference in differences<br/>Synthetic control<br/>Target trial emulation]
    R --> E[Treatment effect<br/>uncertainty and design diagnostics]
    QX --> E

    P --> H[Heterogeneity analysis<br/>after identification]
    E --> H
    H --> V[Constrained policy value<br/>cash, conduct and capacity]
    V --> G[Credit Policy and<br/>Compliance Gate]
    G --> O[Action, delivery and<br/>outcome ledger]
    O --> M[Mature evidence for<br/>prediction and causal refresh]

    classDef evidence fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.5px;
    classDef model fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.6px;
    classDef decision fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.8px;
    class Q,B,O,M evidence;
    class P,R,QX,E,H model;
    class D,V,G decision;
```

**Figure 4: Prediction, causal identification and policy execution answer different questions.** The champion score describes risk under an observed policy. Trials and credible quasi-experiments estimate intervention effects. A governed value rule combines the evidence only after its assumptions and operational constraints are visible.

## 8. The lifecycle timing and multi-state challengers

The fixed-horizon HLR gives a stable champion decision interface, but collections also asks when risk may materialise and how an account moves among recoverable states. A hierarchical piecewise-exponential model is the first timing challenger. Divide follow-up into intervals \(j=1,\ldots,J\). For episode \(i\), let \(d_{ij}\) indicate an event in interval \(j\), \(r_{ij}\) be at-risk exposure time, and

\[
\log \lambda_{ij}
=\alpha_j+\mathbf x_i^{\mathsf T}\boldsymbol\beta
+u_{s(i)}+v_{g(i)}+w_{j(i)}.
\]

The interval likelihood can be written as

\[
d_{ij}\mid r_{ij},\lambda_{ij}
\sim\operatorname{Poisson}(r_{ij}\lambda_{ij}),
\]

which supplies a computationally convenient representation of a piecewise-constant hazard [18], [19]. Right-censored episodes contribute their observed at-risk time without being labelled non-default. The survival probability through time \(t\) is

\[
S_i(t)=\exp\!\left[-\Lambda_i(t)\right],
\qquad
P(T_i\le t)=1-S_i(t),
\]

where \(\Lambda_i(t)\) is cumulative hazard. At the champion horizon \(H_p\), the timing model's \(1-S_i(H_p)\) is compared with the HLR probability on the same outcome definition, eligible population and cutoff. Material disagreement is investigated through censoring, time-varying effects, specification and calibration rather than averaged away.

The reconciliation uses posterior draws. For each eligible episode and draw, the challenger produces a horizon event probability and the champion produces its calibrated counterpart. The review examines their average difference, dispersion, calibration by predicted-risk band, and divergence by product, vintage and remaining tenor. A timing model that agrees at 60 days but separates at 180 days may be revealing genuine duration structure. A model that diverges only in the newest, least mature cohort may be exposing unstable baseline hazards or incomplete follow-up. This comparison gives the challenger a defined route to improvement: it must explain timing, censoring or state occupancy better while preserving or improving common-horizon calibration.

Collections contains more than a first-default clock. A multi-state model represents transitions among current, early arrears, modification, cure, durable cure, re-default, default, recovery and closure states [20]. Its transition intensity

\[
\lambda_{rs,i}(t)
=\lim_{\Delta t\downarrow0}
\frac{P\{X_i(t+\Delta t)=s\mid X_i(t)=r,\mathcal H_i(t)\}}
{\Delta t}
\]

answers a state-specific question: for an account presently in state \(r\), how quickly does it enter state \(s\), conditional on its history and current evidence? A semi-Markov extension includes time already spent in the present state where memorylessness is implausible. Transition probabilities then support expected days in arrears, durable-cure probability, re-default risk, collection workload and discounted cash recovery.

Competing events require the estimand to remain explicit. A cause-specific hazard asks about the instantaneous occurrence of one transition among accounts still event-free. A subdistribution approach targets cumulative incidence while retaining competing events in a modified risk set [21]. Neither is a universal replacement for the other. Prepayment, closure, write-off and cure can change both the interpretation and the population remaining under observation.

Transition construction also respects the observation process. A daily state engine can record exact digital payments, while external recovery and legal events may arrive in intervals. The likelihood distinguishes an actual event time from an interval-censored or administratively recorded date. The Markov assumption is checked by adding duration in state and selected history summaries. When duration materially changes the next transition after current state and covariates are known, the semi-Markov version becomes the more credible operational representation.

Persistent borrower frailty is optional. A shared Gamma frailty may be useful when repeated, matured episodes identify stable unobserved heterogeneity, but borrower identity alone is not enough. Product, enterprise, connected exposure and time effects are evaluated first, and frailty sensitivity is compared with alternative dependence and robust-variance treatments. The survival challenger is therefore adopted because timing and censoring matter, while any convenient conjugacy remains secondary to an identified economic question.

```{.mermaid layout=fullpage}
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Arial",
    "primaryColor": "#EAF2F8",
    "primaryTextColor": "#17324D",
    "primaryBorderColor": "#2E5E7E",
    "lineColor": "#4F6B7A",
    "secondaryColor": "#E8F5F2",
    "tertiaryColor": "#FFF4D6"
  },
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 32, "rankSpacing": 44}
}}%%
flowchart TB
    C[Current] --> EA[Early arrears]
    C --> PP[Prepayment or contractual closure]
    EA --> CU[Cure]
    EA --> MO[Modification]
    EA --> DF[Default]
    CU --> DC[Durable cure]
    CU --> RD[Re-default]
    MO --> CU
    MO --> RD
    RD --> MO
    RD --> DF
    DF --> RC[Recovery process]
    RC --> RO[Recovery outcome<br/><br/>Partial recovery and continued work<br/>Full recovery and closure<br/>Write-off and closure]
    RO --> O[Collection quantities<br/><br/>Transition timing and state occupancy<br/>Recovery amount and delay<br/>Workload, cost and net cash value]

    classDef current fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.5px;
    classDef improve fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.6px;
    classDef stress fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.8px;
    classDef terminal fill:#F5ECEC,stroke:#9B4C4C,color:#5A2525,stroke-width:1.6px;
    class C,PP current;
    class CU,DC improve;
    class EA,MO,RD stress;
    class DF,RC,RO terminal;
    class O current;
```

**Figure 5: The lifecycle challenger follows timing, cure, re-default and recovery.** States are operational definitions with entry, exit and maturity rules. The diagram becomes a transition register, not a decorative funnel, and each permitted movement maps to data, likelihood and cash-flow tests.

## 9. From default probability to collectible cash

A probability becomes financially useful when it joins a cash-flow model without absorbing quantities that have different meanings. For product \(p\) at horizon \(H\), the architecture therefore passes separate posterior distributions for probability of default, exposure at default, cure, prepayment, loss severity, recovery amount, recovery delay and workout cost. A convenient expected-loss identity is

\[
\operatorname{EL}_{i,H}
=\mathbb E\!\left[
\operatorname{PD}_{i,H}
\times \operatorname{EAD}_{i,T_D}
\times \operatorname{LGD}_{i,H}
\mid \mathcal I_i
\right],
\]

where dependence inside the expectation is retained. Multiplying three separately averaged point estimates is permitted only as a disclosed approximation. It can miss the fact that adverse business conditions raise both drawdown and severity, or that an early restructuring reduces future EAD while changing the timing of receipts.

Exposure follows the contract. For an amortising facility it evolves through scheduled principal, verified prepayments, capitalised charges and modification terms. For revolving credit it also includes future utilisation before default. If \(B_i(t)\) is drawn balance, \(L_i(t)\) limit and \(\operatorname{CCF}_i\) the conditional conversion of undrawn capacity, a scenario-specific exposure can be written

\[
\operatorname{EAD}_i(t)
=B_i(t)+\operatorname{CCF}_i(t)\,[L_i(t)-B_i(t)].
\]

The conversion factor is estimated by product, utilisation state and horizon with time-forward evidence. It is not borrowed unexamined from a different portfolio. A limit reduction, draw freeze or performance-contingent schedule changes this path, so policy evaluation simulates exposure under each feasible action rather than inserting an intervention effect into an unchanged EAD.

For invoice finance, exposure and collection are also tied to the financed invoice, verified debtor, dilution, dispute and settlement route. One enterprise can remain solvent while a concentrated customer delays payment, so debtor-level concentration and recourse terms affect both EAD and recovery. For asset finance, collateral value, repossession time and business interruption enter the recovery path. The common episode spine permits product-specific mechanics without forcing them into one generic balance multiplier.

Recovery is a dated sequence of gross receipts and costs. For default at \(T_D\), let \(R_{ik}\) be cash received at delay \(\tau_{ik}\), \(C_{ik}^{\mathrm{work}}\) the attributable workout cost, and \(d_i(\tau)\) the approved discount factor. Net recovery value is

\[
\operatorname{NRV}_i
=\sum_{k=1}^{K_i}
d_i(\tau_{ik})
\left(R_{ik}-C_{ik}^{\mathrm{work}}\right),
\qquad
\operatorname{LGD}_i
=1-\frac{\operatorname{NRV}_i}{\operatorname{EAD}_i(T_D)}.
\]

Collateral realisation, guarantor payment, insurer refund, cash sweep and borrower repayment remain separately coded because their legal rights, delays and costs differ. Cures are not automatically recoveries: an account can return to current status and later re-default. A durable-cure window and re-default observation period therefore precede final performance classification.

Portfolio aggregation retains scenario coherence. Posterior draws are propagated through contractual schedules so that one draw contains aligned default, utilisation, cure, recovery and timing assumptions. This produces a distribution of monthly and cumulative net cash rather than a collection of unrelated percentiles. Finance can reconcile the mean path, risk can examine tail loss and collections can see workload and timing. The same draw identifiers allow Part 5 to compare gross asset cash, operating costs, funding obligations and protection layers under one state of the world.

The handoff to pricing, accounting and structured finance is a versioned distributional output, not one undifferentiated score. It includes horizon PD, transition probabilities, EAD paths, discounted recovery paths, expected loss, tail loss, calibration segment, posterior uncertainty, scenario and model version. Part 5 can then translate the same cash logic into KESONIA-linked pricing, expected credit loss, capital, reserve and ring-fenced funding decisions without redefining the underlying credit event.

## 10. Common shocks and residual dependence

MSME defaults cluster because firms share customers, suppliers, platforms, neighbourhoods, transport corridors, weather, policy changes, interest rates and demand conditions. The first response is to model these observed channels directly. Macroeconomic regimes enter the contextual evidence set; sector, geography, institution and origination cohort receive hierarchical effects; connected enterprises are grouped; and validation holds out entire common-risk units. Residual dependence is considered only after the marginal models are calibrated under those shared factors.

Let \(F_1,\ldots,F_m\) be calibrated marginal distributions for portfolio loss or default quantities. Sklar's representation writes the joint distribution as

\[
F(y_1,\ldots,y_m)
=C_{\boldsymbol\theta}
\left(F_1(y_1),\ldots,F_m(y_m)\right),
\]

where \(C_{\boldsymbol\theta}\) is a copula [22]. The decomposition allows marginal underwriting evidence and residual co-movement to be tested separately. For discrete default indicators, the likelihood uses probability rectangles or an appropriate latent-variable construction because the copula is not uniquely identified between the jumps of discrete marginals.

The Clayton family is a purposeful challenger when lower-tail liquidity states are expected to coincide. In two dimensions,

\[
C_{\theta}(u,v)
=\left(u^{-\theta}+v^{-\theta}-1\right)^{-1/\theta},
\qquad \theta>0,
\]

with lower-tail dependence coefficient

\[
\lambda_L=2^{-1/\theta}.
\]

Clayton's construction has a long association with dependent event times [23], but narrative plausibility does not select it. Gaussian, Student \(t\), Gumbel, rotated Archimedean and factor-copula alternatives are compared according to the portfolio question. A \(t\)-copula may represent symmetric tail association; a rotated family may match an adverse orientation defined on survival rather than default scales. Variable definitions and rotations are recorded so that “lower tail” always refers to the same economic direction.

The main control is a shock-allocation register. Fuel-price stress, policy tightening or platform disruption cannot be loaded simultaneously as an explicit scenario shift, a time effect, a latent hierarchy effect and a copula shock without reconciliation. Each systematic driver has a primary owner. The residual layer receives the dependence left after those owners have acted, and stress scenarios state whether they condition the marginals, the copula, or both.

Dependence may also change through time. A static parameter is the baseline because short datasets can mistake one crisis window for a permanent law. A dynamic challenger links \(\theta_t\) to a small number of registered macro states or a regularised latent process, then tests whether the added movement predicts later co-defaults. The fit preserves the same marginal forecasts used in the independent baseline, which allows the incremental value of time-varying dependence to be measured directly. Scenario analysis can then widen dependence under a named common shock without refitting every borrower probability to the same adverse observation.

Validation compares empirical and posterior-predictive co-default counts, sector and geography concentrations, rank dependence, joint tail exceedances, portfolio loss quantiles and tranche or covenant quantities. Parametric-bootstrap goodness-of-fit tests help evaluate candidate copulas [24], while temporal and cluster resampling test whether apparent tail dependence is stable. A more elaborate dependence model advances only when it improves held-out joint outcomes and materially informs concentration, capital, reserve or risk-transfer decisions. This keeps correlation from becoming an ornamental coefficient detached from collectible cash.

## 11. Decision quantities and the policy boundary

The underwriting service publishes quantities that a decision can consume: calibrated event probabilities, posterior intervals, tail exceedance probabilities, lifecycle transitions, expected collectible cash, expected loss and data-quality status. It does not collapse policy, regulation and commercial judgement into the fitted coefficient vector. For feasible action set \(\mathcal A_i^{\mathrm{feasible}}\), the economic layer may calculate

\[
a_i^{\star}
=\arg\max_{a\in\mathcal A_i^{\mathrm{feasible}}}
\mathbb E\left[U_i(a,L_i,C_i,H_i)\mid\mathcal I_i\right],
\]

and can add a tail constraint such as

\[
\operatorname{CVaR}_{q}\!\left(L_i(a)\mid\mathcal I_i\right)
\le K_i(a).
\]

Here \(U_i\) states the approved value function, \(L_i\) loss, \(C_i\) delivery cost, \(H_i\) customer outcome and \(K_i\) allocated risk capacity. Decision-focused evaluation can show whether a forecast improves choices at relevant thresholds [25], but the utility units and constraints belong to credit governance. They are calibrated for the lender's and customer's consequences rather than inherited from another decision setting.

The Credit Policy and Compliance Gate receives model version, evidence timestamp, posterior quantities, uncertainty, support and quality flags, causal-evidence status, aggregate exposure and concentration. It then applies the registered legal, contractual, risk-appetite, affordability, fair-treatment, product and operational rules. The output may approve, decline, change a limit, alter price within authorised bounds, offer support, restructure, intensify contact, route to specialist recovery, or defer for missing evidence. Approval and collections are therefore joined by the same lifecycle record without giving one model unrestricted authority over every action.

Uncertainty changes the route, not merely the wording of a report. A wide interval caused by a new sector may support a smaller initial exposure, a shorter review period or additional verified evidence. A wide interval caused by a stale ledger may trigger data repair and temporary reliance on contractual features. A high probability with strong causal evidence for a low-cost support action may route to an offer before arrears deepen. These mappings are registered separately from model parameters and tested for customer and portfolio consequences.

Reason communication follows the same ownership structure. Explicit features and registered interactions supply human-readable economic drivers. A residual AI contribution is described through its governed feature family, direction, stability and supporting explicit context rather than assigning a fictional name to a latent coordinate. The decision record distinguishes the model's influential evidence from the policy rule that determined the action and from any authorised human override.

This boundary also supports supervision. The Central Bank of Kenya's risk-based approach emphasises the identification, measurement, monitoring and control of material risks [26]. The architecture makes those verbs observable: the champion estimates and monitors, the causal programme tests interventions, the cash layer measures consequences, and the policy gate controls action. Exceptions and overrides carry reason, authority, duration and outcome. Aggregate limits remain enforceable even when an individual expected-value calculation appears attractive.

## 12. Validation as a collection discipline

Validation asks whether the architecture remains truthful at the moments that matter: before disbursement, during deterioration, after intervention, at recovery, and under common stress. It begins before fitting. Prior predictive simulation tests whether intercepts, spline shapes, hierarchy scales, horseshoe sparsity and time effects imply plausible event rates and group variation. Simulation-based calibration on recoverable synthetic settings tests whether the inference implementation can reproduce known generative quantities. Unit tests compare Pólya-Gamma and reference NUTS likelihoods, transforms and predictions.

Posterior computation is assessed with multiple chains, rank-normalised split \(\widehat R\), folded diagnostics, bulk and tail effective sample sizes, Monte Carlo standard errors and trace behaviour [27]. NUTS runs additionally report divergences, tree-depth saturation and energy diagnostics. Pólya-Gamma runs report latent-variable stability, sparse-solve accuracy and block autocorrelation. Thresholds are defined in the validation protocol, and exceptions require resolution or a documented restriction before an artefact can be approved.

Predictive validation is time-forward and borrower-grouped. Every connected enterprise remains in one fold. Successive windows reproduce information availability, label maturity, macro vintages and the policy that generated outcomes. Sector-held-out, geography-held-out, institution-held-out and emerging-product tests measure transfer rather than hiding sparse groups inside random splits. Performance is reported overall and by decision-relevant segment using calibration intercept and slope, observed-to-expected ratios, Brier and log scores, ranking, interval coverage and tail-event capture. Proper scoring rules reward honest distributions rather than confident point forecasts alone [28].

Model comparison follows the architecture's ownership rules. The explicit-only champion candidate is compared with explicit plus unadjusted AI, explicit plus cross-fitted residual AI, and residual AI with regularised horseshoe shrinkage. The review examines out-of-time value, calibration, coefficient and reason stability, subgroup reliability, compute cost and incremental decisions. Residual correlations, variance-inflation summaries and projection diagnostics reveal duplicated evidence. Removing the AI block, perturbing it, or replacing it with noise should change results only in ways supported by genuine held-out signal.

The timing challenger is validated on survival calibration, time-dependent discrimination, integrated scoring, cumulative incidence, state occupancy, transition counts and recovery timing. The cash layer reconciles predicted principal, interest, prepayment, cure, default, recovery, cost and write-off to ledger totals. The copula layer is judged on joint events and portfolio loss, not marginal AUC. PSIS-LOO can support within-development comparison when its Pareto diagnostics are acceptable [29], but it does not replace the forward and clustered tests that mirror deployment.

Causal validation follows the design. Randomised pilots report allocation integrity, baseline balance, treatment receipt, attrition, missingness, spillovers, primary estimates and multiplicity control. Regression discontinuity reports density and continuity tests, bandwidth sensitivity and placebo cutoffs. Difference-in-differences reports pre-trends, timing and comparison cohorts. Target-trial analyses inspect eligibility alignment, time zero, overlap, censoring and negative controls. Heterogeneous effects are replicated out of sample before entering a policy rule.

Monitoring continues after approval. Calibration, evidence freshness, missingness, support excursions, population and concept drift, transition rates, overrides, contact outcomes, customer complaints, restructures, cures, re-defaults and net recoveries are reviewed together. A change in data or business process opens a diagnosis: source defect, economic shift, product change, servicing change or model deterioration. The response may repair data, recalibrate, restrict a segment, revert to the explicit-only artefact, initiate a controlled experiment or refresh the model. Independent model risk, credit, collections, legal, compliance, data and business reviewers receive enough lineage to reproduce the finding.

Transfer validation is staged rather than declared once. A new participating institution begins with schema reconciliation, outcome-definition mapping and shadow scoring. Its posterior group effect remains strongly pooled until matured local evidence accumulates. Approval for live use specifies products, limits, monitoring frequency and expiry. Expansion requires stable calibration and collection outcomes in the new setting. This sequence turns external validity into a measurable programme and prevents an encouraging pooled result from becoming an unsupported claim of universal transportability.

The final acceptance question is economic and human. Does the model support sustainable collection while improving risk selection, timing, product structure and intervention quality across the full lifecycle? A technically converged model that creates unstable limits, avoidable customer harm or uncollectible balances has not passed. A simpler specification that remains calibrated, actionable and auditable may be the stronger production model.

## Conclusion

The MSME introduced at the beginning is not a static application row. It is a business whose invoices, costs, withdrawals, repayments and operating shocks unfold under a product and servicing policy. Part 2a established the point-in-time evidence contract. This part turns that evidence into a disciplined inferential architecture.

The champion is a calibrated hierarchical Bayesian logistic regression with governed P-splines, partially pooled group effects, residual artificial-intelligence representations and regularised-horseshoe shrinkage. Pólya-Gamma augmentation makes its Gaussian blocks computationally tractable offline while the production request uses a signed, replayable posterior artefact. Timing and multi-state challengers add censoring, cure, re-default and recovery dynamics. A residual dependence layer addresses joint stress only after observable common causes and calibrated marginals are represented.

Prediction remains connected to, but distinct from, causal evidence. Randomised pilots and credible quasi-experiments test whether product and servicing actions improve durable collection and customer outcomes. The cash layer carries PD, EAD, cure, prepayment, LGD, recovery timing and cost into a common distributional handoff. The policy gate then makes authorised decisions within conduct, capacity and concentration constraints.

Part 3 develops the intervention and governance operating model. Part 4 carries the artefacts, event lineage and controls into enterprise systems. Part 5 converts the forecast distribution into pricing, expected credit loss, capital, liquidity and risk-transfer decisions. Together, the sequence underwrites for collection by treating repayment as a designed lifecycle outcome rather than an after-the-fact statistic.

\newpage

## Appendix A: Preserved spline and time-prior alternatives

The champion uses P-splines: a B-spline basis with a second-difference penalty and separately identified null-space terms. Two alternatives remain available for sensitivity and challenger work.

For ordered coefficient vector \(\boldsymbol\beta=(\beta_1,\ldots,\beta_K)^{\mathsf T}\), a B-spline plus first-order random-walk prior is

\[
\beta_k-\beta_{k-1}\sim\mathcal N(0,\tau_{\mathrm{RW}}^2),
\qquad k=2,\ldots,K.
\]

This favours locally smooth coefficient evolution while permitting broad level and slope components. Identification uses an explicit intercept and centring or sum constraints. A B-spline plus stationary AR(1) prior is

\[
\beta_k-\mu
=\rho(\beta_{k-1}-\mu)+\epsilon_k,
\qquad
\epsilon_k\sim\mathcal N(0,\sigma_{\epsilon}^2),
\qquad |\rho|<1.
\]

It favours reversion toward \(\mu\) across the ordered coefficient index. Because a coefficient index is not automatically economic time, its interpretation is stated carefully. For calendar effects, the same RW1 or AR(1) structures can apply directly to \(\delta_t\), where order has an explicit temporal meaning.

All variants use the same knots, degree, boundary policy, feature scaling and out-of-support rules during comparison. The validation set tests calibration, smooth shape, boundary stability, effective degrees of freedom, extrapolation, posterior uncertainty and decisions. The alternatives are preserved because different portfolios may support different local smoothness or persistence structures. Promotion depends on evidence and interpretability rather than on prior family alone.

The comparison report plots the function and first derivative on the observed support, with a rug or weighted density showing where evidence exists. It also reports prior and posterior roughness, sensitivity to knot density, and the contribution of null-space terms. Product-specific deviations are overlaid with their uncertainty and effective sample sizes. This makes the distinction between basis choice, penalty choice and economic shape visible to reviewers, while retaining B-spline plus RW1 and B-spline plus AR(1) specifications as fully reproducible challengers.

## Appendix B: Blocked Pólya-Gamma computation

For each offline iteration:

1. Compute every linear predictor from the current explicit, spline, residual-AI, interaction, hierarchy and time blocks.
2. Draw \(\omega_i\sim\operatorname{PG}(1,\eta_i)\) for each observation or exact aggregated design row.
3. Update strongly coupled Gaussian coefficient blocks jointly using their likelihood and prior precision matrices.
4. Update hierarchy scales, covariance parameters, spline smoothing scales, horseshoe scales and time-process parameters using their validated conditional or numerical kernels.
5. Apply identification constraints or the equivalent parameterisation and calculate calibration and posterior-predictive quantities.
6. Record diagnostics and retain draws according to the approved warm-up, thinning if any, storage and convergence protocol.

Fixed seeds, environment lockfiles, source hashes, fold assignments, transforms and sampler settings form the reproducibility record. The exported artefact contains only approved scoring quantities and transformations. It does not contain an active training loop.

The implementation stores the sparse precision blocks and their ordering, checks positive definiteness after constraints, and verifies selected Gaussian updates against direct dense calculations on small fixtures. Parallel chains use independent random streams. Posterior storage retains enough draws for tail decisions and challenger reconciliation, while a compressed scoring representation is accepted only after its probabilities, intervals and threshold exceedances match the retained draws within approved tolerances. Restart, rollback and numerical-failure tests form part of release validation.

## Appendix C: Causal estimand and design register

| Treatment family | Assignment unit | Primary estimand | Example horizon | Identification route | Required diagnostics | Conduct constraint |
|---|---|---|---|---|---|---|
| Repayment timing | Enterprise episode | Intention-to-treat effect on durable cure | 60 and 120 days | Randomised pilot | Balance, receipt, attrition, spillover | Preserve required protections |
| Threshold support | Score-threshold episode | Local average effect near cutoff | Product-specific | Regression discontinuity | Density, continuity, bandwidth, placebo cutoffs | Registered threshold and override log |
| Servicing rollout | Branch, platform or cohort | Group-time treatment effect | Multiple periods | Difference-in-differences | Pre-trends, anticipation, composition | Stable comparison practice |
| Regional product design | Region or platform | Aggregate treated-unit effect | Pilot period | Synthetic control | Pre-fit, donor sensitivity, placebo units | No hidden concurrent intervention |
| Observational restructuring | Eligible distressed episode | Per-protocol or treatment-strategy contrast | Cure and re-default windows | Target-trial emulation | Time-zero alignment, overlap, censoring, negative controls | Explicit eligibility and treatment versions |
| Targeted intervention | Eligible episode or cluster | Constrained policy value | Operational horizon | Validated heterogeneous effects and policy learning | Honest splitting, subgroup stability, capacity simulation | Fair treatment, budget and contact limits |

\newpage

## References

[1] A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari and D. B. Rubin, *Bayesian Data Analysis*, 3rd ed. Boca Raton, FL, USA: CRC Press, 2013.

[2] F. Liu, Z. Hua and A. Lim, “Identifying future defaulters: A hierarchical Bayesian method,” *European Journal of Operational Research*, vol. 241, no. 1, pp. 202-211, 2015, doi: [10.1016/j.ejor.2014.08.008](https://doi.org/10.1016/j.ejor.2014.08.008).

[3] H. Lakkaraju, J. Kleinberg, J. Leskovec, J. Ludwig and S. Mullainathan, “The selective labels problem: Evaluating algorithmic predictions in the presence of unobservables,” in *Proc. 23rd ACM SIGKDD Int. Conf. Knowledge Discovery and Data Mining*, 2017, pp. 275-284, doi: [10.1145/3097983.3098066](https://doi.org/10.1145/3097983.3098066).

[4] P. H. C. Eilers and B. D. Marx, “Flexible smoothing with B-splines and penalties,” *Statistical Science*, vol. 11, no. 2, pp. 89-121, 1996, doi: [10.1214/ss/1038425655](https://doi.org/10.1214/ss/1038425655).

[5] V. Chernozhukov et al., “Double/debiased machine learning for treatment and structural parameters,” *The Econometrics Journal*, vol. 21, no. 1, pp. C1-C68, 2018, doi: [10.1111/ectj.12097](https://doi.org/10.1111/ectj.12097).

[6] C. M. Carvalho, N. G. Polson and J. G. Scott, “The horseshoe estimator for sparse signals,” *Biometrika*, vol. 97, no. 2, pp. 465-480, 2010, doi: [10.1093/biomet/asq017](https://doi.org/10.1093/biomet/asq017).

[7] J. Piironen and A. Vehtari, “Sparsity information and regularization in the horseshoe and other shrinkage priors,” *Electronic Journal of Statistics*, vol. 11, no. 2, pp. 5018-5051, 2017, doi: [10.1214/17-EJS1337SI](https://doi.org/10.1214/17-EJS1337SI).

[8] N. G. Polson, J. G. Scott and J. Windle, “Bayesian inference for logistic models using Pólya-Gamma latent variables,” *Journal of the American Statistical Association*, vol. 108, no. 504, pp. 1339-1349, 2013, doi: [10.1080/01621459.2013.829001](https://doi.org/10.1080/01621459.2013.829001).

[9] A. Gelman, “Prior distributions for variance parameters in hierarchical models,” *Bayesian Analysis*, vol. 1, no. 3, pp. 515-534, 2006, doi: [10.1214/06-BA117A](https://doi.org/10.1214/06-BA117A).

[10] F. Cordaro, M. Fafchamps, C. Mayer, M. Meki, S. Quinn and K. Roll, “Microequity and mutuality: Experimental evidence on credit with performance-contingent repayment,” National Bureau of Economic Research, Cambridge, MA, USA, Working Paper 30411, Sep. 2022, doi: [10.3386/w30411](https://doi.org/10.3386/w30411).

[11] M. Battaglia, S. Gulesci and A. Madestam, “Repayment flexibility and risk taking: Experimental evidence from credit contracts,” *The Review of Economic Studies*, vol. 91, no. 5, pp. 2635-2675, 2024, doi: [10.1093/restud/rdad107](https://doi.org/10.1093/restud/rdad107).

[12] G. W. Imbens and T. Lemieux, “Regression discontinuity designs: A guide to practice,” *Journal of Econometrics*, vol. 142, no. 2, pp. 615-635, 2008, doi: [10.1016/j.jeconom.2007.05.001](https://doi.org/10.1016/j.jeconom.2007.05.001).

[13] B. Callaway and P. H. C. Sant'Anna, “Difference-in-differences with multiple time periods,” *Journal of Econometrics*, vol. 225, no. 2, pp. 200-230, 2021, doi: [10.1016/j.jeconom.2020.12.001](https://doi.org/10.1016/j.jeconom.2020.12.001).

[14] A. Abadie and J. Gardeazabal, “The economic costs of conflict: A case study of the Basque Country,” *American Economic Review*, vol. 93, no. 1, pp. 113-132, 2003, doi: [10.1257/000282803321455188](https://doi.org/10.1257/000282803321455188).

[15] M. A. Hernán and J. M. Robins, “Using big data to emulate a target trial when a randomized trial is not available,” *American Journal of Epidemiology*, vol. 183, no. 8, pp. 758-764, 2016, doi: [10.1093/aje/kwv254](https://doi.org/10.1093/aje/kwv254).

[16] S. Wager and S. Athey, “Estimation and inference of heterogeneous treatment effects using random forests,” *Journal of the American Statistical Association*, vol. 113, no. 523, pp. 1228-1242, 2018, doi: [10.1080/01621459.2017.1319839](https://doi.org/10.1080/01621459.2017.1319839).

[17] S. Athey and S. Wager, “Policy learning with observational data,” *Econometrica*, vol. 89, no. 1, pp. 133-161, 2021, doi: [10.3982/ECTA15732](https://doi.org/10.3982/ECTA15732).

[18] D. R. Cox, “Regression models and life-tables,” *Journal of the Royal Statistical Society: Series B (Methodological)*, vol. 34, no. 2, pp. 187-220, 1972, doi: [10.1111/j.2517-6161.1972.tb00899.x](https://doi.org/10.1111/j.2517-6161.1972.tb00899.x).

[19] N. Laird and D. Olivier, “Covariance analysis of censored survival data using log-linear analysis techniques,” *Journal of the American Statistical Association*, vol. 76, no. 374, pp. 231-240, 1981, doi: [10.1080/01621459.1981.10477634](https://doi.org/10.1080/01621459.1981.10477634).

[20] P. K. Andersen and N. Keiding, “Multi-state models for event history analysis,” *Statistical Methods in Medical Research*, vol. 11, no. 2, pp. 91-115, 2002, doi: [10.1191/0962280202SM276ra](https://doi.org/10.1191/0962280202SM276ra).

[21] J. P. Fine and R. J. Gray, “A proportional hazards model for the subdistribution of a competing risk,” *Journal of the American Statistical Association*, vol. 94, no. 446, pp. 496-509, 1999, doi: [10.1080/01621459.1999.10474144](https://doi.org/10.1080/01621459.1999.10474144).

[22] R. B. Nelsen, *An Introduction to Copulas*, 2nd ed. New York, NY, USA: Springer, 2006, doi: [10.1007/0-387-28678-0](https://doi.org/10.1007/0-387-28678-0).

[23] D. G. Clayton, “A model for association in bivariate life tables and its application in epidemiological studies of familial tendency in chronic disease incidence,” *Biometrika*, vol. 65, no. 1, pp. 141-151, 1978, doi: [10.1093/biomet/65.1.141](https://doi.org/10.1093/biomet/65.1.141).

[24] C. Genest, B. Rémillard and D. Beaudoin, “Goodness-of-fit tests for copulas: A review and a power study,” *Insurance: Mathematics and Economics*, vol. 44, no. 2, pp. 199-213, 2009, doi: [10.1016/j.insmatheco.2007.10.005](https://doi.org/10.1016/j.insmatheco.2007.10.005).

[25] A. J. Vickers and E. B. Elkin, “Decision curve analysis: A novel method for evaluating prediction models,” *Medical Decision Making*, vol. 26, no. 6, pp. 565-574, 2006, doi: [10.1177/0272989X06295361](https://doi.org/10.1177/0272989X06295361).

[26] Central Bank of Kenya, *Risk Based Supervision Framework*. Nairobi, Kenya: CBK, May 2013. [Online]. Available: [CBK framework](https://www.centralbank.go.ke/wp-content/uploads/2016/08/CBKs-Risk-Based-Supervision-Framework-May-2013-1.pdf). [Accessed: Sep. 6, 2026].

[27] A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P. C. Bürkner, “Rank-normalization, folding, and localization: An improved R-hat for assessing convergence of MCMC,” *Bayesian Analysis*, vol. 16, no. 2, pp. 667-718, 2021, doi: [10.1214/20-BA1221](https://doi.org/10.1214/20-BA1221).

[28] T. Gneiting and A. E. Raftery, “Strictly proper scoring rules, prediction, and estimation,” *Journal of the American Statistical Association*, vol. 102, no. 477, pp. 359-378, 2007, doi: [10.1198/016214506000001437](https://doi.org/10.1198/016214506000001437).

[29] A. Vehtari, A. Gelman and J. Gabry, “Practical Bayesian model evaluation using leave-one-out cross-validation and WAIC,” *Statistics and Computing*, vol. 27, no. 5, pp. 1413-1432, 2017, doi: [10.1007/s11222-016-9696-4](https://doi.org/10.1007/s11222-016-9696-4).
