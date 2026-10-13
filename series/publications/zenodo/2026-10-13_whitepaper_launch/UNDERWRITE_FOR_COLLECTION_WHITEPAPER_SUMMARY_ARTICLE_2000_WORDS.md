# Underwrite for Collection and the design of sustainable MSME credit

Nevil Maloba

Whitepaper DOI: [10.5281/zenodo.23343888](https://doi.org/10.5281/zenodo.23343888)

## The practical question that started the research

How can lenders support sustainable MSME repayment across the life of a facility? That question began this work. A business can have customers, profitable orders and a credible growth opportunity while receiving cash after its loan instalment falls due. Understanding that sequence brings underwriting into the enterprise’s operations: purchasing stock, paying suppliers, meeting payroll, completing an order and collecting the customer’s payment.

What began as LinkedIn articles has developed into Underwrite for Collection, a completed research whitepaper comprising six manuscripts across five parts and two reproducible worked cases. Its organising idea is to design credit around the conditions that produce sustainable repayment. Product terms, evidence, risk models, servicing decisions, recovery arrangements and funding become connected parts of the same economic process.

Exploring the IFoA introduction to banking module supplied an academic motivation and an actuarial lens for these practical questions. It encouraged me to examine how uncertainty, cash timing, customer outcomes and institutional responsibilities can be considered together. The resulting paper gives practitioners a connected framework for examining the full credit journey, with explicit calculations and a programme of empirical questions.

## Start with the business and its cash calendar

The first part places the enterprise’s operating cycle alongside the lender’s contractual calendar. Loan purpose matters because it helps establish how financed activity is expected to generate repayment. Stock purchases, productive assets and working capital each create different cash requirements and receipt patterns. Facility size, draw conditions, tenor, repayment frequency and grace periods can then be assessed against the activity they support.

The first worked case makes this tangible. A hypothetical business begins with KES 250,000 cash, receives a KES 200,000 customer advance and borrows KES 500,000. Its order produces KES 180,000 before financing costs. When the final customer payment arrives on day 60, the business finishes with KES 405,000 cash. The same order exposes a funding problem when that receipt moves to day 90 while debt remains due on day 60.

Maintaining the assumed KES 100,000 operating floor then requires KES 495,000 of additional cash. That amount defines a practical decision: secure financing, bring forward receipts or agree a revised payment schedule. The operating ledger gives the credit officer and borrower a shared basis for comparing those options.

## Establish whose cash the lender is measuring

Part 2a examines the evidence behind financial features. An MSME may operate through several bank accounts, payment channels and related entities. A statement credit can represent customer revenue, borrowing, owner capital, an internal transfer or a reversed transaction. Establishing account control and transaction purpose determines how those movements enter an assessment of recurring operating capacity.

The second worked case reconstructs opening cash from two controlled accounts. Gross statement credits of KES 390,000 reconcile to KES 120,000 in confirmed operating receipts at the first decision cutoff. Invoice verification supports KES 170,000. Consolidated settled cash remains KES 250,000 throughout. The new evidence changes the interpretation of the receipt while preserving the cash reconciliation.

The paper also records when an event happened, when it became known and when it was verified. Those dates allow a historical decision to be reconstructed using the information available at that time. A later invoice, collateral update or payment confirmation receives its own place in the evidence history. This makes both model evaluation and human review more faithful to operational reality.

## Give uncertainty a practical role in underwriting

Part 2b develops a hierarchical Bayesian approach to credit risk. Product, sector, geography, institution, origination cohort and calendar effects provide a structured way to represent differences across portfolios. Partial pooling allows groups with limited observations to learn from the wider population while better evidenced groups support more specific estimates. The hierarchy connects individual facilities with the environments in which they operate.

The model’s outputs include posterior risk estimates, credible intervals and probabilities of crossing defined thresholds. These quantities help a reviewer judge the strength of the evidence behind a recommendation. A wide interval can prompt a targeted information request or closer examination of alternative terms. The decision also draws on affordability, expected cash, customer circumstances and the institution’s approved policy.

Computation is part of that design. The paper develops structured inference, regularisation and offline estimation, with versioned model outputs available for governed use. Nonlinear features and AI representations have defined roles alongside economically interpretable variables. Each model component is assessed through calibration, time based validation, stability and its contribution to the decision the lender needs to make.

## Follow the pathways between arrears and recovery

A facility can move from current payments into arrears, return to current status, prepay, restructure or enter a recovery process. Survival and multi-state approaches allow the research to examine when these transitions occur and how they affect collectible cash. Following the path also clarifies the observation period needed to distinguish an early improvement from sustained performance.

The worked account fixture contains 20 facilities that have reached 90 days past due. Five remain at that status, while the others occupy several different states. Six are currently paying on time, and three have the follow-up needed to satisfy the example’s sustained-current definition. Reporting these paths alongside their populations gives managers a more informative picture of cure, recurrence and recovery.

Part 1 applies the same discipline to industry statistics. Dates, populations and denominators remain attached to each reported figure. Aggregate NPL measures establish portfolio context, while cohort histories, realised cash and workout costs connect that context to the paper’s research question about sustainable collection.

## Turn evidence into an accountable intervention

Part 3 connects analytical evidence to customer treatment through a Credit Policy and Compliance Gate. The gate identifies the proposed action, supporting evidence, eligibility, responsible officer, required agreement, implementation route and follow-up measure. A repayment reminder, evidence request, revised schedule or specialist recovery review therefore has an explicit purpose and an accountable owner.

In the operating case, an approved extension to day 90 produces minimum cash of KES 120,000 and terminal cash of KES 397,500. The borrower’s finance cost and the lender’s economics change with the revised schedule. The governance case then follows the decision through evidence review, delegated authority, borrower agreement, contract booking and an observed synthetic payment. Each stage has a distinct record.

Kenya’s Data Protection Act 2019 and Data Protection General Regulations 2021 inform the paper’s treatment of purpose, data use, transparency, review and accountability. Customer explanations and meaningful human assessment sit within the operational design. The lender can show what information supported an action, who authorised it and how the customer can seek review.

## Learn which actions improve outcomes

The paper distinguishes a risk forecast from the effect of taking an action. A forecast describes expected outcomes under a specified information and policy setting. An intervention evaluation asks how outcomes change when an eligible action is taken. Defining that comparison helps practitioners design research that can answer a management question.

Randomised pilots and suitable quasi-experimental designs can examine repayment timing, durable cure, re-default, net recovery, business continuity and customer experience. The research specifies eligibility, assignment, the comparison treatment, observation windows and outcome definitions. These records also make later analysis of adaptive policies more credible. Contextual bandits, sequential collection decisions and reject inference receive further development in the follow-on article series.

## Make bank controlled research reproducible

Part 4 describes how research can operate within a participating institution’s environment. Authorised access, purpose-bound datasets, versioned features and controlled analytical outputs support work with sensitive credit information. The bank retains responsibility for its customer records, operational systems and decisions. Researchers bring documented methods into that environment and produce evidence that institutional owners can review.

The proposed architecture connects source records, model versions, approvals and execution events. Correlation identifiers link the workflow; distinct event identifiers and settlement references establish individual actions. The worked replay exercises approval, execution, settlement failure, retry and confirmed receipt. This provides a concrete starting point for integration with servicing systems, payment records and financial reconciliation.

## Connect collection to pricing and funding

Part 5 follows the cash consequences into pricing, expected credit loss, capital, liquidity, asset and liability management, and funds transfer pricing. Each function uses a stated horizon, exposure measure and valuation convention. The connection is the underlying facility and its cash history. Reconciliation explains how that shared history supports different institutional decisions.

For the illustrative loan, a contractual margin budget produces a hurdle coupon of 20.04%. A scenario-weighted cash-earnings calculation produces 22.655%, reflecting foregone interest and additional funding and capital time. The KES 2,024 earnings reconciliation shows precisely why the two views differ. The coupon results are conditional on the example’s assumptions and provide inputs for a wider pricing assessment.

The protection example gives guarantees their own payment calendar. Acceptance, claim determination and receipt occur at different dates. Treasury can therefore assess the liquidity needed while recovery is pending, while credit and finance evaluate the protection’s effect on their respective measures. This connects recovery readiness with funding decisions throughout the facility’s life.

## Connect business finance with ring fenced receivables

Financing the operating business examines the enterprise’s cash generation, working capital, obligations and continuing activities. Financing ring-fenced receivables follows identified claims and the collections dedicated to repayment. In this paper, the optional worked example uses a special purpose vehicle to hold loan repayment receivables. Customer receipts support the borrower’s operations; the borrower’s debt payments then supply the vehicle’s collections.

That connection requires explicit ownership and cash records. The example follows purchase funding, a funded reserve, servicing expenses, investor claims and a dated payment waterfall. Eligibility and coverage triggers change how cash is allocated. A timing delay reduces the equity investor’s residual cash even when ultimate asset receipts remain unchanged, because the notes require funding for longer.

These linked views help readers ask practical questions about the same economic chain: can the enterprise produce repayment, can the lender collect and fund the facility, and how do transferred collections meet the financing structure’s obligations?

## Three questions for the next institutional study

Which product structures best align repayment with the cash cycles of defined MSME populations? A participating lender can begin with a specific product and compare receipt patterns, repayment schedules, operating liquidity and subsequent arrears. This question links origination choices to the outcomes observed after disbursement, giving product teams evidence for improving facility design and supporting viable business activity.

Which evidence and interventions improve sustainable collection at an acceptable cost and customer impact? The research can compare eligible responses, measure the additional cash attributable to each response and follow recurrence over a defined period. Costs, complaints, review requests and business continuity belong beside repayment measures, allowing the institution to assess the whole decision and explain its trade-offs.

How should those outcomes change pricing, expected loss, funding and management action? The institution can reconcile the same facility histories across credit, collections, finance and Treasury, with each function retaining its definitions and authority. This creates a practical route from research findings into approved operating requirements. The follow-on five-article series develops credit experiments, sequential collection, reject inference, Treasury control and bank-controlled agentic workflows. Together, these questions organise the next stage around decisions that a participating institution can test and implement.

## Read the paper and reproduce the cases

The two cases connect the manuscript’s ideas to inputs, calculations and recorded decisions. Their hypothetical assumptions are stated explicitly, and the accompanying Python research lab provides editable inputs, cash ledgers, event fixtures, automated tests and reproduction instructions. Readers can trace the figures, inspect the rules and develop further scenarios around a defined business question.

I am grateful to Judy Chege, whose writing strongly influenced the credit-lifecycle framing, and Sukrit Ghildiyal, whose comment on Geofrey Osiemo’s SVM and IFRS 9 post prompted the cash-provenance article. CPA James K. and Felix Sifuna helped sharpen the NPL discussion. Beata Lubinska’s Treasury writing and Mariusz Podsiadlo’s ALM work also informed the questions developed here.

The completed whitepaper provides a foundation for practitioners, researchers and institutional teams to examine credit design together. Its central invitation is practical: follow the business activity, preserve the evidence, make the decision accountable and measure the cash and customer outcomes that follow.

---

**Read the whitepaper:** [10.5281/zenodo.23343888](https://doi.org/10.5281/zenodo.23343888)

**Reproduce the cases:** [Underwrite for Collection research lab](https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab)

**Licence:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/).
