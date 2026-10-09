# Underwrite for Collection: five connected LinkedIn articles

This sequence moves from borrower-level evidence to institution-level balance-sheet decisions. Each article has a distinct decision unit and adds a new layer to the previous one.

| Order | Article | Decision unit and contribution | Carries forward |
|---|---|---|---|
| 1 | [Testing Credit Offers for Collectability](ARTICLE_1_RCTS_CONTEXTUAL_BANDITS_CREDIT_OFFERS.md) | An eligible applicant and a complete offer. Establishes fixed randomized comparisons, response-adaptive allocation, delayed outcomes and policy-value estimation. | Creates the experimental and logging foundation used by article 2. |
| 2 | [From a One-Step Bandit to Sequential Credit Control](ARTICLE_2_CONTEXTUAL_BANDITS_AND_SEQUENTIAL_COLLECTION.md) | A borrower, facility or ring-fenced receivables stream across repeated servicing decisions. Develops temporal relationship graphs, one-step LinUCB/logistic Thompson policies, and MCTS only for constrained multi-step search over a validated simulator; treats GraphSVX as post-hoc model explanation, alongside state transitions, MDP/POMDP framing, credit cash outcomes and IFRS 9 boundaries. | Shows where historical funded cases stop supporting claims about never-funded applicants. |
| 3 | [Who Gets a Repayment Label?](ARTICLE_3_REJECT_INFERENCE_AND_SELECTIVE_LABELS.md) | Applicants selected by historical approval and lending policies. Treats reject inference as a counterfactual-evidence problem, with support maps, sensitivity analysis and safe prospective design. | Uses the evidence discipline from articles 1–2; does not re-teach bandits or sequential control. |
| 4 | [Can Reinforcement Learning Help Run a Bank’s Balance Sheet?](ARTICLE_4_TREASURY_ALM_STOCHASTIC_CONTROL.md) | The bank’s balance sheet and Treasury policy. Applies constrained stochastic control to ALM, FTP, IRRBB, liquidity and ALCO while keeping human decision authority. | Transfers the control vocabulary to a different scale; it does not treat borrower-level models as Treasury policy. |

| 5 | [Bringing the Methods into the Bank](ARTICLE_5_BANK_CONTROLLED_AGENTIC_AI_CREDIT_AND_TREASURY.md) | The bank-controlled operating workflow. Connects registered analytical tools, Bayesian uncertainty, human review, authorised execution, customer rights and outcome reconciliation. | Turns the first four decision methods into a coherent deployment and evaluation design. |

## Shared boundaries

The articles use the same evidence disciplines—timestamped data, defined populations, explicit assumptions, reproducible outcomes and governed decisions—but they do not collapse their targets. A borrower’s repayment action, an applicant’s unobserved potential outcome and a bank’s funding or hedge action are different interventions. The fourth article therefore builds on the control methods in the second while using bank-level states, constraints, objective measures and approval routes.

Data-protection discussion is limited to the Data Protection Act, 2019 and the Data Protection (General) Regulations, 2021. The recurring provisions are Act sections 25, 26, 31 and 35, and General Regulations 22 and 49–53, applied according to the data and decision in scope.

The named Mermaid diagrams are supplied as PNG images for LinkedIn upload and embedded in the Unicode Word documents. The combined PDF uses TeX mathematics. The posting guide pairs each article with its short post and Word document.
