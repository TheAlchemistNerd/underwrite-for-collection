# Part 2b Brief

## Working title

**Hierarchical Bayesian Underwriting, Causal Identification and Lifecycle Dependence**

## Scale

- Full-source target: 10,166 words.
- Editorial-prose target: 9,681 words.

## Purpose

Part 2b provides the statistical centre of the series. It must explain what is forecast, how uncertainty and heterogeneity are represented, when an intervention effect can be inferred, and how lifecycle timing and correlated shocks extend the primary model.

## Primary prognostic model

The main model is a hierarchical Bayesian logistic regression with:

- global and product intercepts;
- explicit lifecycle variables represented linearly or through governed P-splines;
- cross-fitted residual AI representations;
- regularised-horseshoe shrinkage on the residual block;
- selected pre-specified interactions;
- partially pooled sector, institution, geography and cohort effects;
- an identifiable exchangeable, RW1 or AR(1) time structure where supported.

Pólya–Gamma augmentation will be presented as an offline inference strategy for the complete HLR. Conditional Gaussian updates preserve partial pooling and work naturally with Gaussian spline penalties and time processes. Remaining scale, persistence, correlation and calibration parameters retain separate updates. Production uses approved posterior artifacts rather than live MCMC.

## Causal programme

The manuscript will define potential outcomes and distinguish:

- score performance under observed policy;
- the incremental value of an evidence source;
- the effect of product design;
- the effect of a servicing or collection intervention;
- heterogeneous treatment effects;
- policy value under operational and conduct constraints.

Randomised studies are preferred where feasible. Regression discontinuity, difference-in-differences, interrupted time series, synthetic controls, instrumental variables and target-trial emulation will be presented with their specific assumptions and diagnostics.

## Lifecycle and dependence challengers

- Multi-state or competing-risks models for current, arrears, modification, cure, re-default, default and recovery.
- Hierarchical Cox or parametric survival models where proportionality and baseline-hazard treatment are appropriate.
- Gamma frailty as a survival extension rather than the basis of the HLR.
- Copula, factor or portfolio models for correlated sector and macroeconomic stress.
- POMDP, bandit, Hawkes and structural/intensity models located in appendices or challenger sections according to their purpose.

## Required validation

- posterior predictive checks;
- discrimination and calibration by time and subgroup;
- observed-to-expected and decision-curve analysis;
- prior and smoothing sensitivity;
- covariate and concept-shift monitoring;
- selective-label and missing-outcome diagnostics;
- out-of-time and institution-held-out tests;
- causal balance, overlap, placebo and falsification checks;
- decision-focused utility and harm analysis.

## Acceptance tests

- The hierarchy is not sacrificed for computational convenience.
- Prediction, causal effect and policy action are never represented by the same quantity.
- Every outcome has horizon and censoring treatment.
- The neural block adds residual information rather than duplicating explicit features.
- Complex challengers appear only where they answer an identified question.

