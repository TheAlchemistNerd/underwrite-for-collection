# Canonical Definitions and Notation Register

This register will be expanded as each part is accepted. A term or symbol defined here must not acquire a different meaning in another part without a recorded decision.

## Lifecycle definitions

**Origination:** The governed process through which a product is designed, an application is assessed, terms are offered and a facility is created.

**Collection:** The lawful receipt and allocation of amounts due, together with the product, servicing and intervention arrangements that support sustainable repayment.

**Cure:** A transition from a defined delinquent state to a defined current or restructured-performing state.

**Durable cure:** A cure that remains effective for a pre-specified performance window without re-default or repeated material delinquency.

**Recovery:** Cash or economic value realised after default or charge-off, stated gross or net of workout cost and discounted where the analysis requires it.

**Collectability:** The conditional capacity of a legally enforceable and operationally serviceable facility to generate sustainable contractual or restructured cash flows across its lifecycle.

**Lifecycle outcome:** A defined event or state such as current, arrears, modification, cure, durable cure, re-default, default, recovery, closure or complaint.

## Modelling definitions

**Prognostic model:** A model estimating the distribution of a future outcome under observed or specified policy, without claiming that a feature or score causes that outcome.

**Causal estimand:** A precisely defined contrast between potential outcomes for a population, treatment, comparator, horizon and outcome.

**Credit Policy and Compliance Gate:** The downstream rule layer applying law, regulation, contract, conduct, risk appetite, operational capacity and portfolio constraints to model and account information.

**Explicit lifecycle features:** Interpretable financial, repayment and servicing variables with defined calculations and ownership.

**Residual neural representation:** A cross-fitted AI sequence representation projected away from the explicit design matrix before optional whitening and Bayesian shrinkage.

**Partial pooling:** Hierarchical estimation in which sparse groups borrow information from a wider population while data-rich groups may differentiate.

**Pólya–Gamma augmentation:** A latent-variable method that makes Gaussian coefficient blocks of a Bayesian logistic model conditionally conjugate for offline inference.

**P-spline:** A spline basis with a discrete-difference penalty on adjacent coefficients, normally expressed through a Gaussian prior conditional on a smoothing scale.

## Principal HLR notation

For outcome `Y_i` and linear predictor `eta_i`:

```text
Y_i ~ Bernoulli(logit⁻¹(eta_i))

eta_i = alpha
      + Q_i beta_z
      + H_tilde_i beta_h
      + R_i gamma
      + u_sector(i)
      + v_institution(i)
      + w_geography(i)
      + delta_t(i)
```

Where:

- `Q_i` is the governed explicit design matrix, including spline bases.
- `H_tilde_i` is the cross-fitted residual AI representation.
- `R_i` contains pre-specified interactions or treatment-independent contextual terms.
- `u`, `v` and `w` are identifiable hierarchical effects.
- `delta_t` is a cohort or time effect with a stated exchangeable, RW1 or AR(1) prior.

For Pólya–Gamma inference:

```text
omega_i | eta_i ~ PG(1, eta_i)
```

This augmentation changes computation, not the model’s lifecycle interpretation.

## Causal notation

- `A_i`: assigned or observed intervention.
- `Y_i(a)`: potential outcome under intervention `a`.
- `tau`: causal estimand, defined with population, treatment, comparator, outcome and horizon.
- `e(X_i)`: propensity or assignment probability where relevant.
- `Z_i`: instrument or assignment variable only when the exclusion and relevance assumptions are stated.

## Pricing and balance-sheet notation

- `r_KESONIA(t)`: applicable KESONIA benchmark over time.
- `K_RBCP`: customer risk-based credit-pricing premium under the applicable CBK framework.
- `EL`: expected loss, with horizon and measurement basis stated.
- `ECL`: IFRS 9 expected credit loss under the approved accounting methodology.
- `K_reg`: regulatory capital requirement.
- `EC`: internal economic-capital measure.
- `FTP`: governed funds-transfer price or charge.
- `OpEx`: allocated operating and servicing cost.
- `m_fund`: funding or note margin where relevant.
- `CoC`: cost of capital.
- `NPV_rec`: net present value of recoveries after workout cost.

These terms must not share the generic symbol `K`.

## Status labels

Every material proposition in a working ledger will be classified as:

- source-backed fact;
- observed data;
- derived quantity;
- model output;
- contractual term;
- regulatory requirement;
- internal policy;
- statistical convention;
- testable hypothesis;
- implementation recommendation;
- unresolved diligence item.

