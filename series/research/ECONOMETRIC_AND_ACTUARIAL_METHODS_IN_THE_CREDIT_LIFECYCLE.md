These methods form a connected lifecycle rather than eleven independent modelling exercises:
Underwriting estimates whether deterioration will occur; survival models estimate when; causal methods test what changes it; cash-flow models translate the resulting states into collections and losses; validation determines whether the estimates remain dependable; stress and capital models determine how much risk the institution can retain.

1. Hierarchical logistic and survival models
The hierarchical Bayesian logistic regression is the primary underwriting model. For a defined outcome horizon, such as default or serious delinquency within 90 days, it estimates:
\[
P(Y_{i,h}=1\mid X_i)
\]Its linear predictor combines explicit liquidity features, residual AI embeddings, nonlinear effects, selected interactions and hierarchical effects for products, platforms, geographies and cohorts.
The hierarchy provides partial pooling. A small geographic segment does not receive a completely independent risk estimate based on a few observations. Its estimate is drawn toward the portfolio mean, while a large, information-rich segment can differentiate itself more strongly.
The survival model answers a different question:
\[
\lambda_i(t)=\lambda_0(t)\exp(X_i^\top\beta)
\]Instead of only predicting whether an event occurs within a fixed horizon, it estimates the timing of delinquency, cure, prepayment, restructuring or default. It naturally handles loans that have not yet matured or experienced an event.
The intended division is:
- Hierarchical logistic model: champion for operational PD and credit-policy decisions.
- Survival or hazard model: challenger for event timing, censoring and sequential-credit analysis.
- Multi-state survival extension: source of contractual and behavioural cash-flow timing.
2. Panel, cohort, platform, geographic and time effects
Credit data contain repeated and clustered observations. Loans originated in the same month may experience the same economic conditions. Borrowers on the same platform may share payment rails, income cycles and operational shocks. Enterprises in the same geography may share weather, infrastructure and market conditions.
The model therefore separates:
- Borrower or enterprise effects.
- Product effects.
- Origination-cohort or vintage effects.
- Platform effects.
- Geographic effects.
- Calendar-time effects.
A simplified specification is:
\[
\eta_i=\alpha+X_i^\top\beta
+u_{\mathrm{product}(i)}
+v_{\mathrm{platform}(i)}
+g_{\mathrm{geo}(i)}
+c_{\mathrm{cohort}(i)}
+\delta_{t(i)}
\]This prevents the model from treating correlated accounts as independent evidence. It also distinguishes borrower risk from environmental conditions.
For example, deteriorating collections across one platform may reflect a settlement outage rather than simultaneous deterioration in every borrower. A cohort effect can identify loans originated during an unusually loose underwriting period. A time effect can capture a broad economic shock without permanently labelling the affected borrowers as intrinsically risky.
3. AR(1) and RW1 temporal structures
Calendar effects should usually evolve smoothly rather than jump independently each month.
An AR(1) structure is:
\[
\delta_t=\rho\delta_{t-1}+\varepsilon_t,
\qquad |\rho|<1
\]It assumes shocks persist but gradually revert toward a long-run level. This is suitable when credit conditions exhibit cyclical persistence.
A first-order random walk, or RW1, is:
\[
\delta_t=\delta_{t-1}+\varepsilon_t
\]It allows the underlying risk level to drift without forcing mean reversion. It is more flexible but can absorb too much trend if weakly governed.
In the architecture, these structures can govern:
- Portfolio-wide credit conditions.
- Cohort deterioration.
- Platform-specific operational stress.
- Default and cure intensities.
- Recovery timing.
- Macroeconomic regime effects.
AR(1) and RW1 should be treated as alternative temporal specifications and tested through predictive validation. They should not both be added merely because they are mathematically available.
4. Nonlinear P-splines and regularisation
Financial distress rarely changes linearly with liquidity variables. Moving from a DLR of 20% to 30% may have little effect, while moving from 90% to 100% may materially increase risk. Earnings velocity may become important only after crossing a deterioration threshold.
P-splines represent a nonlinear relationship using B-spline basis functions:
\[
f(x)=\sum_{k=1}^{K}B_k(x)\theta_k
\]A difference penalty controls unnecessary curvature:
\[
\Delta^m\theta_k\sim N(0,\tau^{-1})
\]This lets the data identify smooth thresholds without producing an unstable curve that follows every fluctuation.
P-splines are applied to interpretable variables such as:
- Dynamic debt-to-liquidity ratio.
- Earnings velocity.
- Repayment velocity.
- Cash-flow asymmetry.
- Wallet volatility.
- Utilisation.
- Time since depletion.
Regularisation has two related roles:
- Spline penalties control nonlinear complexity.
- Regularised horseshoe priors shrink redundant residual neural-embedding coefficients.
The neural representations are first cross-fitted and residualised against the explicit variables. Regularisation then controls whatever incremental information remains. This reduces duplicated signal and multicollinearity while preserving useful AI evidence.
5. Treatment-effect estimation for collection interventions
A payment after a reminder does not prove that the reminder caused the payment. The borrower may have paid anyway.
Treatment-effect estimation asks:
\[
E[Y(1)-Y(0)]
\]where \(Y(1)\) is the outcome under an intervention and \(Y(0)\) is the counterfactual outcome without it.
Candidate interventions include:
- Payment reminders.
- Alternative payment dates.
- Temporary instalment reductions.
- Restructuring offers.
- Limit reductions.
- Collection-channel changes.
- Financial-counselling support.
- Early human-servicing contact.
The evaluation should measure more than immediate payment. Relevant outcomes include:
- Cash collected.
- Time to cure.
- Re-default within a defined period.
- Modification success.
- Complaints and customer harm.
- Cost of intervention.
- Net present value of collections.
- Longer-term credit access.
Conditional treatment effects can identify which borrowers benefit from an intervention. However, treatment models should govern interventions, not quietly replace the underwriting PD.
6. Randomised-pilot design
Randomised pilots provide the cleanest evidence about whether an intervention works.
Eligible accounts can be randomly assigned to:
- Existing servicing practice.
- New intervention.
- Alternative intervention intensity.
- Alternative timing or communication channel.
Randomisation may occur at account, borrower, branch, platform or geographic-cluster level. Cluster randomisation may be necessary when treatment could spill over between borrowers or servicing teams.
A credible pilot requires:
- Predefined eligibility criteria.
- A primary outcome and horizon.
- Power and sample-size calculations.
- Stratification by important risk segments.
- Intention-to-treat analysis.
- Monitoring of treatment delivery.
- Customer-protection guardrails.
- Predefined stopping rules.
- Analysis of cure durability and re-default.
- Documentation of exclusions and attrition.
The bank-controlled sandbox provides the environment for designing and validating these experiments before any model or intervention affects production customers.
7. Difference-in-differences, event studies and quasi-experiments
Randomisation is sometimes impossible because a policy has already been rolled out, a platform makes a system-wide change, or regulation affects a defined group.
Difference-in-differences compares the change in an affected group with the contemporaneous change in a comparison group:
\[
\widehat{\tau}_{DiD}
=
(\bar Y_{T,\mathrm{post}}-\bar Y_{T,\mathrm{pre}})
-
(\bar Y_{C,\mathrm{post}}-\bar Y_{C,\mathrm{pre}})
\]It could evaluate:
- A new collection workflow introduced at selected branches.
- A platform settlement-policy change.
- A KESONIA-linked repricing transition.
- A restructuring programme introduced for one product.
- A guarantee becoming available to an eligible borrower class.
Event studies extend this by estimating effects before and after the event. Pre-event coefficients help test whether the treated and comparison groups were already following different trends.
Other quasi-experimental methods may include regression discontinuity around eligibility thresholds, instrumental variables where a defensible instrument exists, and matched comparison designs.
These methods require explicit assumptions, especially parallel trends, absence of anticipatory behaviour and appropriate treatment of staggered adoption.
8. Competing risks, cure, re-default and recovery models
A loan has more possible outcomes than performing or defaulted. From a delinquent state it may:
- Cure.
- Restructure.
- Prepay.
- Remain delinquent.
- Default.
- Be written off.
- Enter recovery.
- Produce a partial or full recovery.
Competing-risk models estimate cause-specific or subdistribution hazards for these mutually competing transitions. Multi-state models then connect them:
\[
\text{Current}
\rightarrow
\text{Delinquent}
\rightarrow
\{\text{Cure, Modification, Default}\}
\rightarrow
\{\text{Re-default, Recovery, Closure}\}
\]Cure models distinguish temporary arrears from persistent deterioration. Re-default models test whether a cure or modification remains sustainable. Recovery modelling separates:
- Probability of recovery.
- Recovery amount.
- Recovery timing.
- Workout and legal costs.
- Guarantee or insurance proceeds.
- Counterparty settlement delays.
These outputs are essential because two portfolios with the same ultimate default rate can generate very different liquidity needs and economic losses if their collection and recovery timing differs.
9. Out-of-time validation, calibration and covariate-shift testing
Random training-test splits can leak future information and overstate performance. The model is therefore validated on later periods, future vintages and, where possible, previously unseen platforms or geographies.
Out-of-time validation tests whether the model survives changing conditions.
Discrimination measures whether higher-risk accounts are ranked above lower-risk accounts. Calibration tests whether predicted probabilities correspond to realised frequencies. Relevant measures include:
- Observed-to-expected ratios.
- Calibration intercept and slope.
- Reliability plots.
- Brier score.
- Log loss.
- Horizon-specific default rates.
- Calibration by product, platform, geography and borrower group.
Covariate-shift monitoring tests whether the production population differs from the development population. PSI can contribute, but it should be combined with:
- Changes in feature distributions.
- Missingness and data-quality changes.
- New platform or product populations.
- Outcome-prevalence changes.
- Residual and calibration drift.
- Changes in intervention policy.
- Delayed outcome maturity.
A model may continue ranking accounts correctly while materially misestimating absolute PD. That distinction matters for limits, ECL, pricing and capital.
10. Macroeconomic scenario and stress transmission
Macroeconomic conditions affect several lifecycle mechanisms simultaneously.
A stress scenario may change:
- Default probability.
- Drawdown and utilisation.
- Cure probability.
- Modification demand.
- Prepayment.
- Recovery rates and delays.
- Platform revenue.
- Funding costs.
- Deposit behaviour.
- Guarantee claims.
- Collateral or receivable values.
The model therefore transmits a coherent scenario through underwriting, collections, ECL, capital, liquidity and funding rather than applying unrelated shocks to each department.
For example, a KESONIA increase may raise funding costs and customer repayments. Reduced MSME cash flow may increase utilisation and delinquency. Collections may slow, behavioural maturity may extend, and Treasury may require more liquidity. ECL and economic capital will respond through different horizons and recognition rules, but should reflect the same economic scenario.
Care is needed to avoid double counting. A common macroeconomic shock should not be added independently through the time effect, explicit macro variables and a manual overlay without reconciliation.
11. Marginal economic-capital allocation
Expected loss represents the central or average loss absorbed through pricing and provisions. Economic capital addresses unexpected adverse loss in the tail of the portfolio distribution.
A simplified definition is:
\[
EC=\rho(L)-E[L]
\]where \(\rho(L)\) may be a high-quantile VaR, expected shortfall or another approved tail-risk measure.
Marginal allocation asks how much each product, cohort, platform or concentration contributes to portfolio capital. Under an Euler allocation:
\[
EC_j=w_j\frac{\partial EC}{\partial w_j}
\]The allocated contributions should reconcile to total capital when the chosen risk measure and portfolio model satisfy the required conditions.
This supports decisions about:
- Risk-adjusted product pricing.
- Platform and sector limits.
- Origination capacity.
- Capital-intensive concentrations.
- Guarantee and insurance purchases.
- Receivables eligible for ring-fenced funding.
- Risk-adjusted performance measurement.
- Portfolio diversification.
A segment can have a modest standalone expected loss but a large marginal-capital contribution if it becomes most impaired during the same scenarios as the rest of the portfolio. Conversely, a segment with a higher standalone PD may provide diversification if its losses are weakly dependent on the dominant portfolio risks.
Together, these eleven components convert the project from a credit-scoring exercise into a complete econometric and actuarial credit-risk architecture.