# Student-t priors and Bayesian limit decisions: corpus and integration map

Date: 8 October 2026. Internal research and editorial record.

## What was located and added

The review corpus explicitly proposes half-Student-t priors with ν=3 or ν=4 for hierarchy and spline scales. Mwendo Pamoja Part 2b fixes ν=3 in its displayed hierarchy. Underwrite for Collection Part 2b retains general finite degrees of freedom and prior sensitivity. Article 2 now develops that prior, its Gaussian scale-mixture representation, the Pólya–Gamma connection, the Bayesian limit boundary and a numerical limit-review example in two new subsections immediately after the existing Pólya–Gamma section. Existing article paragraphs were retained.

The current evidence supports a documented model specification and article explanation. A scoped search of Python and notebook files in the two repositories found no executable Student-t/half-t implementation using the searched StudentT, half-t, ν=3 or df=3 spellings. The review's NumPyro example is a code block in Markdown. No fitted hierarchical posterior or new limit-policy performance result is claimed by this insertion.

Two further paragraphs connect the model to computation and human review. The computation paragraph describes offline conditional-Gaussian updates, separate latent and scale updates, validated posterior artefacts and governed refresh. The human-review paragraph distinguishes the PD credible interval, posterior cap-exceedance probability, an identified causal-effect credible interval, the predictive cash interval and the posterior difference between actions. It explains sparse-group pooling and reviewer choices; overlap between separate action intervals is evaluated through the action comparison and decision costs.

## Exact source locations

| Source | Existing contribution | How Article 2 uses it |
| --- | --- | --- |
| [Transformer, spline and scale-prior review](<C:/Users/Nevo/Downloads/insuretech & embedded finance/docs/research/modelling-notes/transformer-ffn-SiLU-b-spline-funnel-ar-rw-nig-niw.md:1325>) | Non-centred scale parameterisation and scale/correlation separation. | Explains a scale prior's place within a hierarchy. |
| [Half-t recommendation and NumPyro illustration](<C:/Users/Nevo/Downloads/insuretech & embedded finance/docs/research/modelling-notes/transformer-ffn-SiLU-b-spline-funnel-ar-rw-nig-niw.md:1645>) | ν=3 or 4; a folded StudentT code example at line 1661; sensitivity at line 1703. | States ν=3 explicitly and retains prior-predictive and sampler checks. |
| [Low-level Bayesian hardware note](<C:/Users/Nevo/Downloads/insuretech & embedded finance/docs/research/modelling-notes/low_level_bayesian_hardware_optimization.md:13>) | Half-t density, ν=3 tail discussion and hardware illustration. | Confirms the provenance of the ν=3 discussion; hardware claims are not required for the article. |
| [Mwendo Part 2b, hierarchy](<C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_2b_Bayesian_Underwriting_and_Asymmetric_Copulas.md:54>) | Gaussian raw group effects and half-Student-t(3,1) hierarchy SDs at line 66. | Assigns the half-t to the group SD, then defines the conditional Gaussian group effect. |
| [UFC Part 2b, hierarchy](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/series/parts/Part_2b_Hierarchical_Bayesian_Underwriting_Causal_Identification_and_Lifecycle_Dependence.md:183>) | General half-t hyperprior; prior-predictive calibration and alternative-scale sensitivity. | Extends the explanation to sector, region, institution and cohort effects. |
| [UFC Part 2b, inference](<C:/Users/Nevo/Downloads/behavioural credit scoring - underwrite to collect rct/series/parts/Part_2b_Hierarchical_Bayesian_Underwriting_Causal_Identification_and_Lifecycle_Dependence.md:406>) | Pólya–Gamma Gaussian coefficient blocks; separate hyperparameter updates; NUTS comparison. | Explains conditional conjugacy and the approved posterior artefact. |
| [Mwendo Part 2b, decision boundaries](<C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_2b_Bayesian_Underwriting_and_Asymmetric_Copulas.md:465>) | Posterior expected payoff, break-even PD at line 497, uncertainty gate at line 520. | Derives the threshold, specifies its assumptions and adds a KES example. |
| [Mwendo Part 1, aggregate cap](<C:/Users/Nevo/Downloads/insuretech & embedded finance/whitepapers/mwendo-pamoja/parts/Part_1_Product_Architecture_and_Cascades.md:292>) | Aggregate exposure, earnings velocity, liquidity, utilisation, reserves, PD, uncertainty and stress. | Connects individual limit review to aggregate obligations and affordability. |

## Mathematical meanings retained

- **ν=3:** Student-t degrees of freedom. In the Gaussian/Gamma mixture, Gamma shape and rate are both 3/2.
- **Half-t:** Prior on a positive hierarchy standard deviation. Gaussian group effects conditional on that SD are the model's pooling structure.
- **Pólya–Gamma:** Logistic-likelihood augmentation yielding normal coefficient conditionals when combined with Gaussian conditional priors.
- **Conditional conjugacy:** Applies to specified blocks given the other variables. Hierarchy scales and covariance parameters retain separate updates. The marginal posterior is a mixture and requires posterior computation.
- **t-copula:** A separate choice for dependence between outcomes. Its parameter calibration and validation are independent of choosing a half-t hierarchy prior.
- **Limit threshold:** p*=(G+O)/(G+O+L) follows from fixed two-outcome linear payoffs over a common horizon. Under this model, expected payoff uses posterior mean PD; the uncertainty gate uses the posterior distribution.
- **Opportunity cost:** O is included only when separately defined in the action comparison. Setting O=0 keeps the example's foregone benefit from being counted twice.
- **Worked example:** G=KES 1,200; L=KES 18,800; O=0; p*=6%; posterior mean PD=4% gives expected value KES 400. The example is hypothetical and supplies no fabricated posterior-tail probability.
- **Prospective action:** Changing a limit can change utilisation and repayment. The causal effect requires experimental or otherwise identified action-response evidence.
- **Human review:** The PD parameter interval, cap-exceedance probability, conditional average causal-effect interval, action-difference distribution and predictive realised-cash interval answer different questions and are labelled accordingly.
- **Computational purpose:** The chosen prior and parameterisation support plausible partial pooling and feasible posterior calculation. Offline fitting, approved serving artefacts, calibration and sampler diagnostics remain part of the documented operating design.

## Propagation across the manuscripts

The following identifies existing destinations and the next integration work. Only Article 2 and this internal map were edited in this task.

| Manuscript location | Existing role | Practical next integration |
| --- | --- | --- |
| Mwendo Part 1 | Product cascades and aggregate exposure cap. | Make the limit-review example an input to the aggregate cap and product-specific cash test. |
| Mwendo Part 2a | Point-in-time financial and temporal evidence. | Freeze the exact exposure, utilisation and cash features available when posterior risk is calculated. |
| Mwendo Part 2b | ν=3 hierarchy, posterior computation, decision boundary and uncertainty rule. | Implement the specified prior; compare sensitivity, sampler diagnostics and decision reversals on declared data. |
| Mwendo Part 3 | Credit Policy and Compliance Gate, intervention ownership and decision records. | Carry expected payoff, cap exceedance, available actions, approval and review reasons into one typed record. |
| Mwendo Part 4 | Product and accounting events, approved integrations and retained versions. | Record approved limit changes separately from recommendations, then reconcile subsequent drawdowns and cash. |
| Mwendo Part 5 | PD/EAD/recovery inputs, pricing, funding and waterfall calculations. | Recompute exposure and cash paths after an approved limit change, preserving pricing, loss and waterfall conventions. |
| Mwendo Part 6 | Implementation sequence, tests and deployment ownership. | Add model and action-policy validation milestones before consequential deployment. |
| UFC Part 1 | Borrower operating cycles and facility design. | Explain which limit changes support an operating cycle and which increase future repayment burden. |
| UFC Part 2a | Verified lifecycle evidence and features. | Preserve entity resolution, cash provenance, permissible use and time cutoffs for limit-review inputs. |
| UFC Part 2b | General half-t hierarchy, PG inference and causal identification. | Compare ν=3 with the existing sensitivity specifications, and separate action-conditioned risk from treatment effects. |
| UFC Part 3 | Permitted intervention library and policy gate. | Add a declared limit-review action with eligibility, uncertainty review, affordability and customer redress. |
| UFC Part 4 | Bank-controlled research and enterprise deployment. | Serve versioned posterior summaries through controlled interfaces and retain human approval for governed actions. |
| UFC Part 5 | Pricing, ECL, capital, liquidity and funding. | Follow approved changes through utilisation, recovery timing, expected shortfall and funding effects. |

## Article sequence

Article 1 supplies the experimental comparison and approved action set. Article 2 now connects hierarchy uncertainty to limit review and sequential decisions. Article 3 addresses outcome selection and the evidence available around approval boundaries. Article 4 uses approved aggregate cash and exposure outcomes in institution-level control. A bank-controlled agent workflow may coordinate evidence retrieval, model calls, reviews and logging around those analyses, with authority allocated by the institution.

## Subsequent hierarchy and mathematical-appendix integration

On the subsequent consistency pass, all five article sources were updated so that the borrower models retain explicit sector, region and origination-vintage levels. Logistic and hazard functions use distinct model labels L and H. Article 2 supplies their complete non-centred group-scale construction, fixed-coefficient/intercept priors and a Bayesian piecewise-baseline-hazard option; compact PG and Thompson notation refers to the expanded design. Articles 4 and 5 preserve that model metadata in Treasury and controlled deployment handoffs. The new [Article 2 mathematical appendix](build/appendices/ARTICLE_2_MATHEMATICAL_APPENDIX.md) derives the models and decision formulas for the combined PDF. Source whitepapers and sibling repositories remain unchanged by this pass.

## Primary references added to Article 2

[20] A. Gelman, “Prior distributions for variance parameters in hierarchical models,” *Bayesian Analysis*, vol. 1, no. 3, pp. 515–534, 2006. [Author's paper](https://www.stat.columbia.edu/~gelman/research/published/taumain.pdf).

[21] Stan Development Team, “Reparameterizing a Student-t distribution,” *Stan User’s Guide*, sec. 23.7, ver. 2.27, 2021. [Official documentation](https://mc-stan.org/docs/2_27/stan-users-guide/reparameterization-section.html).
