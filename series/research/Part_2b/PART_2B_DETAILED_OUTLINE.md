# Part 2b Detailed Outline

## Working title and governing question

**Hierarchical Bayesian Underwriting, Causal Identification and Lifecycle Dependence**

Part 2b asks how a lender can convert the point-in-time evidence contract from Part 2a into calibrated forecasts, separate those forecasts from causal intervention evidence, and extend the resulting marginal risks into timing, recovery and dependent portfolio outcomes. Its governing economic test is collectability: every statistical object must state what future cash or lifecycle event it forecasts, at what horizon, under which observed policy, and how uncertainty affects the next decision.

## Scale and drafting method

- Full-source target: 10,166 words, with a first-draft tolerance of plus or minus 5 percent.
- Editorial-prose target: 9,681 words.
- References are excluded from both targets.
- Mermaid labels count toward the full-source total but not editorial prose.
- Drafting proceeds section by section. A section is accepted only after its equations, citations, terminology and handoffs reconcile with the preceding accepted section.
- The main body carries the economic narrative and production architecture. Specialised derivations and alternative priors remain in appendices so mathematical depth is preserved without interrupting the argument.

## Planned structure and word budget

### Abstract, 230 to 280 words

- State the champion HLR, the causal programme and the timing/dependence challengers.
- Explain that the model forecasts outcomes under observed policy, while trials or credible quasi-experiments estimate intervention effects.
- Name the collection endpoints: default, cure, durable cure, re-default, recovery amount, recovery timing and net recovery value.
- State the production pattern: offline posterior estimation, signed posterior artefact, low-latency scoring and downstream policy gate.

### 1. When a probability becomes a collection question, 650 to 750 words

- Begin with an MSME whose payment outcome depends on both business state and the lender's earlier product and servicing choices.
- Connect Part 2a's feature contract to Part 2b's inferential contract.
- Define the statistical centre as three linked but separate tasks: prognosis, causal identification and decision policy.
- Introduce Figure 1, the champion/challenger and causal evidence architecture.
- Establish that a default probability is useful only with an outcome definition, horizon, data cutoff and action context.

### 2. Observation units, horizons and selective outcomes, 750 to 850 words

- Define the borrower-product-episode-decision record \((i,p,e,t_0)\).
- Define product horizon \(H_p\), outcome maturity and right censoring.
- Keep all records for one enterprise or connected exposure in the same validation fold.
- Distinguish application, facility, instalment, account-state and recovery observations.
- Explain selective labels created when approval decisions determine which repayment outcomes become observable.
- State the champion binary outcome and the separate lifecycle outcome vector.

### 3. The champion hierarchical Bayesian logistic model, 1,150 to 1,300 words

- Specify the Bernoulli likelihood and block-structured linear predictor.
- Define explicit P-spline design, residual AI representation, controlled interaction block and data-quality metadata.
- Use partially pooled product, sector, geography, institution and vintage effects.
- Define identification through centring or sum-to-zero constraints.
- Explain partial pooling as a continuous response to information volume, not a manual segment override.
- Provide group-level priors and non-centred parameterisation.
- Describe calibration as an out-of-time model component.
- Use Figure 2 to show feature ownership and model flow.

### 4. Governed nonlinearities, hierarchy and time, 850 to 950 words

- Define a cubic B-spline basis with second-difference P-spline penalty.
- State how knots, degree, boundary support, clipping, centring and smoothing-scale priors are versioned.
- Allow product-varying deviations only through partial pooling.
- Present exchangeable, RW1 and stationary AR(1) time structures as testable specifications.
- Preserve B-spline plus RW1 and B-spline plus AR(1) alternatives in Appendix A.
- Explain why binning is diagnostic unless design rows are exactly identical.

### 5. Residual AI evidence and regularised horseshoe shrinkage, 750 to 850 words

- Explain neural representations as AI-derived summaries of permitted event sequences.
- Require out-of-fold, borrower-grouped and time-aware generation.
- Residualise the AI bottleneck against the explicit design and metadata using training folds only.
- Treat optional whitening as a within-embedding geometry operation.
- Specify the regularised horseshoe with global, local and finite-slab scales.
- Require explicit-only, unadjusted-AI and residual-AI ablations.

### 6. Pólya-Gamma offline inference and the production artefact, 900 to 1,000 words

- Derive the Pólya-Gamma likelihood identity and Gaussian coefficient conditional.
- Apply conditional updates to the complete HLR while retaining hierarchical pooling.
- Identify blocks that retain their own updates.
- Compare blocked Gibbs with NUTS as a reference implementation.
- Explain exact Bernoulli-to-binomial aggregation only for identical design rows.
- Separate event-time feature refresh, online score refresh and offline model refresh.
- Use Figure 3 to show the offline-to-online artefact pathway.

### 7. Prognosis, intervention effects and policy value, 1,250 to 1,400 words

- Define potential outcomes and population, treatment, comparator, outcome and horizon.
- Separate predictive risk, incremental evidence value, product-design effects and servicing effects.
- Discuss randomised trials, including Kenyan and international repayment-flexibility evidence.
- Specify regression discontinuity, difference-in-differences, instrumental variables, synthetic control and target-trial emulation with their assumptions.
- Explain heterogeneous treatment effects and policy learning as later stages after identification.
- Address interference, non-compliance, attrition, delayed outcomes, contamination and multiplicity.
- Use Figure 4 to separate prediction, causal evidence and policy execution.

### 8. The lifecycle timing and multi-state challengers, 850 to 950 words

- Define a hierarchical piecewise-exponential model with at-risk exposure.
- Derive survival and horizon PD from cumulative hazard.
- Reconcile fixed-horizon HLR and survival probabilities at common horizons.
- Define current, early arrears, modification, cure, durable cure, re-default, default, recovery and closure states.
- Distinguish cause-specific and subdistribution hazard questions.
- Retain Gamma frailty only where repeated matured episodes identify persistent borrower heterogeneity.
- Use Figure 5 for the state architecture.

### 9. From default probability to collectible cash, 800 to 900 words

- Keep PD, EAD, cure, prepayment, LGD, recovery amount, recovery timing and workout cost separate.
- Define net present value of recovery.
- Explain revolving drawdown, amortising balances and performance-contingent schedules.
- Show how intervention changes future exposure and therefore future observed labels.
- State the posterior output contract passed to Part 5.

### 10. Common shocks and residual dependence, 750 to 850 words

- Model observed macro factors and hierarchical common effects before residual dependence.
- Use Sklar's theorem to motivate a copula over calibrated marginal outcomes.
- Define the Clayton lower-tail orientation for joint default and compare Gaussian or t alternatives.
- Prevent duplicate shock loading across marginals, hierarchy, copula and stress scenarios.
- Validate co-defaults, tail concentration and portfolio-loss quantities.

### 11. Decision quantities and the policy boundary, 600 to 700 words

- Define posterior expected utility and tail-risk quantities.
- Show that the economically preferred action remains subject to the feasible policy set.
- Separate approval, limit, price, support, restructuring and recovery actions.
- Pass model outputs, uncertainty, quality and causal evidence to the Credit Policy and Compliance Gate.

### 12. Validation as a collection discipline, 900 to 1,050 words

- Prior predictive, posterior predictive and simulation-based checks.
- Rank-normalised split \(\widehat R\), bulk and tail ESS, MCSE, divergences and sensitivity.
- Time-forward, borrower-grouped, sector-held-out and institution-held-out validation.
- Calibration intercept and slope, Brier and log scores, observed-to-expected ratios and decision-focused value.
- Model redundancy diagnostics and neural ablations.
- Causal balance, overlap, placebo, pre-trend and falsification tests.
- Multi-state, recovery and dependence validation.
- Constructive monitoring and independent review.

### Conclusion, 280 to 350 words

- Return to the MSME story.
- Summarise the champion, causal evidence and challenger roles.
- Hand intervention governance to Part 3 and cash-flow/accounting consequences to Part 5.

### Appendix A: Preserved spline and time-prior alternatives, 450 to 550 words

- B-spline with RW1 coefficient prior.
- B-spline with stationary AR(1) coefficient prior.
- Centring, boundary handling and comparative tests.

### Appendix B: Blocked Pólya-Gamma computation, 350 to 450 words

- Matrix conditional update.
- Sampler pseudocode.
- Artefact outputs and reproducibility record.

### Appendix C: Causal estimand and design register, 300 to 400 words

- Table of treatment family, unit, estimand, horizon, identification route, diagnostics and conduct constraint.

## Diagram standard

All Mermaid diagrams use top-to-bottom flow, orthogonal `stepAfter` routing, limited node density, explicit subgraphs and `layout=fullpage`. The build filter renders each at scale 3. Captions remain separate Markdown paragraphs and figures receive dedicated portrait pages unless a later visual test demonstrates a genuine need for landscape orientation.

## Acceptance gates

- The champion remains a hierarchical Bayesian logistic regression.
- Pólya-Gamma augmentation changes the offline computation, not the hierarchy or economic meaning.
- P-splines are primary; B-spline with RW1 and AR(1) alternatives are preserved in the appendix.
- Neural representations add residual information and remain distinct from explicit lifecycle features.
- Prediction, causation and policy are represented by different quantities and workflows.
- Every binary outcome has a horizon and maturity rule.
- Censoring and selective labels are handled explicitly.
- Timing, lifecycle, recovery and dependence challengers answer identified questions.
- Every source is cited at the claim it supports, in first-appearance IEEE order.
- Language remains constructive, technically confident and oriented toward capability.
- The final full-source and editorial counts pass the first-draft band before PDF inclusion.

