# Sequential Credit and Treasury LinkedIn Articles

Prepared 7 October 2026 from the two supplied pasted texts, the Underwrite for Collection and Mwendo Pamoja manuscripts, the accumulated review notes, the Kenya data-protection review, and the Fannie Mae/Freddie Mac research protocols.

## Drafts

1. [From Rejected Applications to Sequential Support](ARTICLE_1_REJECT_INFERENCE_AND_SEQUENTIAL_CREDIT_CONTROL.md) — **about 3,500 words** before its references. It develops reject inference, selective labels, controlled offer evidence, contextual-bandit evaluation and sequential collection control.
2. [From Balance-Sheet Scenarios to Stochastic Control](ARTICLE_2_TREASURY_POMDP_AND_STOCHASTIC_CONTROL.md) — **about 3,500 words** before its references. It develops the method ladder from scenarios and optimization to MPC, POMDPs and carefully governed RL, with a reproducible Treasury illustration.

The counts use whitespace-separated text before each References section and include headings, tables and figure captions. Equations use Unicode notation. Each article has an independent numbered reference list in IEEE style.

## Companion diagrams

- [Reject-inference and collection-control flow](ARTICLE_1_REJECT_INFERENCE_FLOW.svg)
- [Treasury method ladder and evidence flow](ARTICLE_2_TREASURY_CONTROL_METHOD_LADDER.svg)

The Markdown articles embed the companion images by relative filename. The SVG files are independent assets for inserting in a LinkedIn article or exporting to another image format.

## Line-by-line source integration

Both pasted files were read through to their final lines: the reject-inference material has **287 lines** and the two-article brief has **304 lines**. The supplied notes contribute the following, now carried into the drafts:

- Define a default label against a specified hypothetical offer and horizon. Keep historical repayment under originated contracts separate from counterfactual outcomes for declined applicants.
- Separate funding propensity from probability of default, and state the overlap, conditional-selection and unobserved-selection assumptions. A hierarchical Bayesian model and Pólya–Gamma computation organize or sample a specified model; they do not identify missing outcomes.
- Separate rejected-applicant outcomes from immature follow-up on originated loans. Use survival and competing-risk methods for observed loan histories; keep future outcomes pending until mature.
- Use a fixed randomized pilot inside a separately approved eligibility and affordability region. Record the eligible action set, assigned and delivered offers, propensity, take-up, booked contract, overrides, outcomes and maturity.
- Separate intention-to-treat offer effects, take-up, risk among originated takers, offer economics and collection-policy value. Doubly robust estimators still require support, correct propensities and a credible design.
- Extend from one-step contextual bandits to sequential control only after state, transitions, delayed outcomes, legal action authority and operational constraints are specified. Treat a POMDP as appropriate only when a latent state and observation process are described.
- Keep fairness/access observations distinct from repayment-conditioned metrics for which rejected applicants have no observed labels. Keep IFRS 9 ECL, expected loss in pricing, economic capital and regulatory capital separately defined.
- Carry Treasury and ALM concepts through an auditable numerical case, while preserving NII, EVE, liquidity, FTP, customer rate and capital as distinct measures and decision owners.

## Project and dataset boundaries reflected in the articles

- The Underwrite for Collection crosswalk covers Part 1 portfolio metrics and lifecycle context; Part 2 risk and selective labels; Part 3 experiments and interventions; Part 4 operating data and decision records; and Part 5 recovery and financial consequences.
- The Mwendo Pamoja crosswalk covers Parts 1–2 product, cash-flow and evidence structure; Part 3 regulatory orchestration and interventions; Part 4 systems and telemetry; Part 5 KESONIA pricing, capital and funding; and Part 6 implementation and evidence controls.
- Business finance and ring-fenced receivables finance are treated as separate cash-flow propositions, requiring separate states, eligibility tests, evidence and monitoring.
- Fannie Mae and Freddie Mac are used as methodological examples of selected acquired-loan performance histories, including servicing paths, censoring, modification, cure and loss resolution. Their application-to-acquisition selection chain does not provide rejected-applicant counterfactuals or Kenyan MSME outcomes. The local GSE protocols are proposed research; raw GSE data have not been acquired and audited for those protocols, so the articles do not claim completed GSE analyses.
- The legal treatment distinguishes Constitution Article 31 (privacy) from Data Protection Act section 31 (DPIA), scopes solely automated decisions and Regulation 22 safeguards, and distinguishes the CRB and Digital Credit Provider rules by their legal scope. The articles describe governance and research design, not a completed legal opinion or a deployed system.
- Treasury examples are explicitly illustrative. They demonstrate reproducible calculations and data boundaries; they are not a fitted bank policy, an approved FTP curve or a claim of production RL.
