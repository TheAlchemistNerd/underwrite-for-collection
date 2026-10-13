---
title: "Underwrite for Collection: one order, several cash clocks"
subtitle: "Reproducible operating and finance case U4C-MSME-001"
author: "Nevil Maloba"
date: "1 October 2026"
lang: en-GB
---

## A1. What this case establishes

**A profitable order, an affordable payment schedule, an acceptable lending return and an investable receivables pool are four separate tests.** This appendix carries a hypothetical MSME order through those tests with an explicit operating ledger, lender earnings, dated recoveries, evidence updates and an optional funding vehicle. The participating bank's balance sheet remains the primary architecture.

The examples connect dated cash, explicit denominators, lifecycle pricing, protection payment delays, verification freshness, settlement evidence and cash-limited distributions. They use declared hypothetical inputs to demonstrate reproducible arithmetic and workflow controls. Institutional application builds on these schedules with observed customer data, calibrated risk estimates, intervention evidence and documented transfer rights.

All money is KES. Day 0 is 1 October 2026. The fixed-rate example assumes an 18% simple ACT/360 coupon. Variable-rate applications can use the applicable KESONIA benchmark and contractual pricing method. Discounted recoveries use an assumed 9% effective ACT/365; the cash-shortfall exhibit separately derives an effective interest rate from its own contractual cash flows. Calculations retain full precision, with rounding applied for display. Individually rounded table cells may sum to a one-cent difference.

### Reading the evidence

| Result | Evidence level | Practical use |
|---|---|---|
| Borrower and lender cash schedules | Deterministic scenario | Arithmetic consequences of the stated contract and receipt dates |
| PD, recovery fraction, capital allocation and CCF | Assumptions | Declared inputs for sensitivity analysis and subsequent calibration |
| Approved extension | Alternative contractual scenario | Compare contractual schedules; estimate intervention effects through a defined evaluation design |
| Workflow replay | Tested local event fixture | Exercise states and approval checks; connect the verified workflow to bank interfaces |
| Pool waterfall | Static runoff demonstration | Trace contractual cash allocation; document legal transfer, tax and regulatory treatment for the transaction |

## A2. Start with the enterprise's operating cash

The borrower has KES 250,000 opening cash and wishes to retain a KES 100,000 operating floor. A customer pays KES 200,000 in advance and KES 800,000 on completion. The borrower pays KES 600,000 to a supplier at day 0, KES 120,000 payroll at day 30 and KES 100,000 completion costs at day 60. The KES 500,000 loan pays out on day 0; a KES 10,000 fee is paid immediately. Principal and KES 15,000 interest fall due on day 60.

For each event date:

$$
C_t=C_{t-1}+\text{customer receipts}_t+\text{loan draws}_t
-\text{operating payments}_t-\text{debt payments}_t-\text{fees}_t.
$$

Receipts are assumed available before the same-day payments. An intraday liquidity test can represent settlement delays. This ledger follows the order and stated opening cash; an enterprise-wide assessment adds other orders, taxes, capital expenditure, creditor commitments and distribution requirements.

| Day | Customer cash | Loan draw | Operating paid | Debt paid | Closing cash |
| --- | --- | --- | --- | --- | --- |
| 0 | 200,000.00 | 500,000.00 | 600,000.00 | 0.00 | 340,000.00 |
| 30 | 0.00 | 0.00 | 120,000.00 | 0.00 | 220,000.00 |
| 60 | 800,000.00 | 0.00 | 100,000.00 | 515,000.00 | 405,000.00 |

The order's KES 180,000 operating cash surplus becomes KES 155,000 after this facility's KES 25,000 finance cost. Closing cash is KES 405,000. The KES 305,000 above the operating floor is **analytical headroom** available for assessment against other orders, taxes, capital expenditure, creditor commitments, covenants and the firm's distribution rules. Opening cash is a liquidity resource; earnings arise from the order's revenue and costs.

### Receipt delay and a deliberate contract change

| Schedule | Minimum cash | Additional cash to floor | Terminal cash | Finance cost |
| --- | --- | --- | --- | --- |
| on time | 220,000.00 | 0.00 | 405,000.00 | 25,000.00 |
| delay unfinanced | -395,000.00 | 495,000.00 | 405,000.00 | 25,000.00 |
| approved extension | 120,000.00 | 0.00 | 397,500.00 | 32,500.00 |
| revolver | 320,000.00 | 0.00 | 403,333.33 | 26,666.67 |

If the KES 800,000 customer balance arrives on day 90 but the loan remains due on day 60, the unfinanced forecast reaches **minus KES 395,000**. Preserving the operating floor requires KES 495,000 of additional cash. That amount defines the funding task: secure an authorised facility, bring forward customer receipts or agree a revised payment schedule. The eventual closing balance is conditional on funding the intervening payments; the executable plan records the chosen funding source and its cost.

With an extension approved before the due date, principal becomes due on day 90 and the illustrative contract charges 90 days of simple interest: KES 22,500. Cash at day 60 is KES 120,000 and terminal cash KES 397,500. The extension maintains positive cash under the assumed receipts. Evaluate it alongside other eligible options using affordability, lender value and observed customer outcomes. The decision record contains the revised schedule, reason, borrower acceptance, authorised officer and execution evidence. The lender bears an extra KES 5,000 administration cost in the pricing sensitivity.

## A3. Keep price, exposure and capital denominators separate

The first pricing exhibit is a **contractual margin budget**. It uses promised coupon and fees, full scheduled funding time and a nominal principal-loss allowance including workout costs. Default probability is assumed to be 4% from origination through contractual day 60; recovery may occur after that default horizon. Gross principal recovery is 40%; workout cost is 4% of EAD. Nominal LGD is therefore 64%. These stated assumptions support a management-pricing calculation. An institution can supply its calibrated risk inputs and approved accounting and capital methods for the corresponding reporting views.

$$
\begin{aligned}
EL_{\mathrm{budget}}&=PD\times EAD\times(1-g+c),\\
M&=I+F-FTP-O-EL_{\mathrm{budget}}-L,\\
EP_{\mathrm{budget}}&=M-h\,EC\,T/360.
\end{aligned}
$$

Here $g$ is the gross-recovery fraction, $c$ the workout-cost fraction, $L$ the undrawn liquidity cost and $M$ the contribution before capital charge. The assumed funding rate is 9%, operating cost KES 5,000, allocated economic capital 12% of EAD and annual capital hurdle 14%. Funding is charged on the full drawn balance and capital is priced separately as an internal management convention. Another funding convention would require a reconciliation.

| KES | 60-day term | 90-day extension | 60-day revolver |
| --- | --- | --- | --- |
| Income | 25,000.00 | 32,500.00 | 26,666.67 |
| Funding cost | 7,500.00 | 11,250.00 | 8,250.00 |
| Operating cost | 5,000.00 | 10,000.00 | 5,000.00 |
| Undrawn liquidity cost | 0.00 | 0.00 | 83.33 |
| Default EAD | 500,000.00 | 500,000.00 | 630,000.00 |
| Nominal loss allowance | 12,800.00 | 12,800.00 | 16,128.00 |
| Allocated capital | 60,000.00 | 60,000.00 | 75,600.00 |
| Capital charge | 1,400.00 | 2,100.00 | 1,764.00 |
| Contribution before capital | -300.00 | -1,550.00 | -2,794.67 |
| Economic profit | -1,700.00 | -3,650.00 | -4,558.67 |

For the term loan, KES 25,000 income minus KES 7,500 funding, KES 5,000 operations and KES 12,800 loss allowance leaves minus KES 300 before capital. The KES 1,400 capital charge produces **minus KES 1,700 economic profit**. Period RAROC is minus 0.5%; its simple annualised equivalent is minus 3%. Under this budget convention, a **20.04%** coupon clears the hurdle. This conditional pricing result provides a starting point for assessing affordability, market conditions and customer response.

The 90-day extension column holds PD and LGD fixed to isolate timing and administration. For an actual extension, re-estimate exposure, default timing, recovery and funding over the revised horizon. This connects the contract change to its full credit and funding consequences.

### A revolving alternative

The facility limit is KES 650,000: KES 500,000 is drawn at day 0 and KES 100,000 at day 30. Average drawn balance is KES 550,000; average unused commitment is KES 100,000. Coupon is charged only on drawn balances. An assumed 1% annual undrawn fee generates KES 166.67, while a distinct 0.5% annual liquidity cost generates KES 83.33. At the stress date, KES 600,000 is drawn and 60% of the remaining KES 50,000 is assumed to convert, giving **KES 630,000 EAD**. That EAD measures conditional stress exposure; the average drawn balance determines contractual interest. The resulting borrower schedule ends at KES 403,333.33; lender value is assessed using the corresponding loss, funding and capital charges.

## A4. Reconcile the margin budget to lifetime cash earnings

A budget using all promised interest can overstate expected earnings if default eliminates that interest. A scheduled 60-day funding assumption also misses the cost of late settlement. Use the same loan in three mutually exclusive states: 80% pays KES 515,000 on day 60, 16% pays the same amount on day 90, and 4% defaults and yields KES 200,000 gross recovery on day 180 with KES 20,000 workout cost. The original fee is retained in every state. The delay state retains the original KES 15,000 contractual interest. This is a sensitivity with unchanged contractual entitlement, distinct from the approved extension in A2.

For this cash-earnings view, the lender funds the entire principal and holds the same allocated capital until resolution. At default resolution it writes off the unrecovered principal. The undiscounted contribution in state $s$ is:

$$
M_s=F+\text{receipts}_s-P-\text{funding}_s-O-\text{workout}_s.
$$

| State | Weight | Resolution day | Funding cost | Contribution | Economic profit |
| --- | --- | --- | --- | --- | --- |
| on time | 80.000% | 60 | 7,500.00 | 12,500.00 | 11,100.00 |
| late same cash | 16.000% | 90 | 11,250.00 | 8,750.00 | 6,650.00 |
| default | 4.000% | 180 | 22,500.00 | -337,500.00 | -341,700.00 |

| Reconciliation, KES | Amount |
| --- | --- |
| Margin-budget economic profit | -1,700.00 |
| Scenario-weighted contribution | -2,100.00 |
| Scenario-weighted capital charge | 1,624.00 |
| Scenario-weighted economic profit | -3,724.00 |
| Difference from margin budget | -2,024.00 |

The KES 2,024 difference comprises KES 600 expected foregone interest, KES 1,200 additional funding time and KES 224 additional capital time. Contribution is measured before capital; RAROC divides that contribution by allocated capital, and economic profit deducts the capital charge once.

The bridge explains how contractual income, payment outcomes and funding duration produce the two earnings measures. The expected cash-earnings coupon that clears this particular hurdle is **22.655%**, holding scenario probabilities and behaviour fixed. To evaluate a price change, estimate the corresponding selection, affordability, prepayment and default responses. Unrecovered principal is already included in the scenario cash flows, so each loss enters the earnings calculation once.

## A5. Same cash flows, different measurement question

For an illustrative amortised-cost cash-shortfall calculation, assume the KES 10,000 fee is integral to the effective interest rate, with other transaction costs set to zero. Initial net proceeds are KES 490,000; contractual collection is KES 515,000 at day 60. Solve:

$$
490{,}000=\frac{515{,}000}{(1+r_{\mathrm{EIR}})^{60/365}}.
$$

The solved annual effective rate is **35.353%**. It reprices the contractual receipt to KES 490,000.00; the simple annual coupon uses its separately stated ACT/360 convention.

| State | Weight | Receipt day | Receipt | Receipt PV | Weighted PV |
| --- | --- | --- | --- | --- | --- |
| on time | 80.000% | 60 | 515,000.00 | 490,000.00 | 392,000.00 |
| late same cash | 16.000% | 90 | 515,000.00 | 477,958.85 | 76,473.42 |
| default gross receipt | 4.000% | 180 | 200,000.00 | 172,264.80 | 6,890.59 |

The contractual present value is compared with probability-weighted gross receipt present values at that same EIR. Workout costs are displayed separately and included in the management comparison. The institution-specific accounting method specifies their eligibility and treatment when constructing the IFRS 9 allowance.

| Measure | KES |
| --- | --- |
| Contractual net proceeds | 490,000.00 |
| Expected gross receipt PV | 475,364.01 |
| Receipt shortfall | 14,635.99 |
| Separate expected workout-cost PV | 689.06 |
| Management comparison including cost | 15,325.05 |
| PV loss if all cash is 30 days late | 12,041.15 |

Each number answers a defined measurement question. The KES 12,800 pricing allowance is nominal principal loss plus workout cost; the receipt shortfall also captures foregone contractual interest and delayed payment at the original EIR. The KES 15,325.05 management comparison additionally discounts workout cost. Present these measures alongside their horizon, cash-flow scope and discount convention. The scenario cash earnings in A4 already include the corresponding losses.

IFRS 9's cash-shortfall concept considers amount and timing; the IASB's impairment review explains this context. To extend the exhibit into an accounting measurement, specify staging, significant increase in credit risk, the 12-month or lifetime default window, modification treatment, eligible collateral cash flows and guarantee recognition in an approved institution-specific method. The assumed 4% here applies from origination through contractual day 60; a 12-month PD requires its own horizon calibration. [IASB, IFRS 9 impairment review](https://www.ifrs.org/content/dam/ifrs/project/pir-9-impairment/rfi-iasb-2023-1-ifrs9-impairment.pdf).

## A6. Recovery readiness and protection have their own clocks

Default occurs on day 60. Gross recovery of KES 200,000 and KES 20,000 workout cost occur on day 180. A hypothetical guarantee pays 50% of principal remaining unrecovered after that gross receipt, capped at KES 250,000. Eligibility is accepted on day 90, the amount crystallises after the day-180 recovery, and payment occurs on day 240; claim cost is KES 3,000. The premium is KES 5,000 at origination. The lender bears interest shortfalls and workout costs. The contractual settlement here is net of the stated collateral recovery, preventing duplicate reimbursement. If payment preceded collateral realisation, subrogation and subsequent recovery sharing would need another explicit waterfall.

| Measure | KES |
| --- | --- |
| Gross recovery at day 180 | 200,000.00 |
| Workout cost at day 180 | 20,000.00 |
| Guarantee receipt at day 240 | 150,000.00 |
| Guarantee net of claim cost | 147,000.00 |
| Unprotected recovery PV at default | 174,971.74 |
| Protected recovery PV at default | 315,855.33 |
| Expected incremental value at origination, after premium | 556.08 |

The case assumes acceptance and payment with certainty conditional on default and eligibility. Guarantor default and dispute scenarios can extend that assumption. Acceptance is recorded on day 90; usable guarantee cash arrives on day 240. Funding the intervening period is therefore a separate liquidity decision. The discounted expected incremental benefit after premium is KES 556.08 under these assumptions. Add the chosen funding facility, capital treatment and behavioural response to evaluate the complete protection arrangement.

With PD unchanged at 4%, a verified decline in gross recoverability from 40% to 20% raises nominal LGD from 64% to 84% and the budget loss allowance from KES 12,800 to KES 16,800. This illustrates recovery readiness: payment performance and recovery prospects can evolve differently as rights, priority or collateral realisability change. The responsible owners assess PD, IFRS 9 staging and capital recognition using the evidence and criteria relevant to each decision.

## A7. Prove what was known and what actually settled

A day-0 review verifies 40% gross recoverability. A feed outage begins on day 30. A rights change has an effective date of day 20, first becomes known on day 40 and is verified on day 45 at 20% gross recoverability. Historical forecasts use the information known at their own cutoff, preserving the sequence of discovery and verification.

| Cutoff day | Last verified day | Evidence age | Recovery parameter | Outage | Review pending |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 40.000% | No | No |
| 35 | 0 | 35 | 40.000% | Yes | No |
| 42 | 0 | 42 | 40.000% | Yes | Yes |
| 45 | 45 | 0 | 20.000% | No | No |

The outage marks evidence as stale and preserves its verification date. At day 42 the rights change is known and awaiting resolution: route it for review, record the uncertainty and run a controlled sensitivity. The fixture retains the last verified recovery parameter until day 45 and keeps the pending evidence visible. A decision owner can apply an interim measure under the institution's documented evidence-review policy.

An independent remittance workflow moves through draft, review, approval, execution, settlement failure, retry and confirmed settlement. It illustrates payment control alongside the approved loan amendment. Contract effectiveness and receipt of cash have separate records. Exact duplicate event IDs are idempotent; conflicting payloads enter reconciliation. Execution requires recorded approval, and settlement requires a bank reference.

| Cutoff day | State | Unique events | Receipt available |
| --- | --- | --- | --- |
| 52 | approved | 3 | No |
| 53 | executed | 4 | No |
| 54 | failed | 5 | No |
| 55 | executed | 6 | No |
| 56 | settled | 7 | Yes |

The dated event fixture demonstrates the local state machine. Institution integration adds external-reference validation, segregation of duties, APIs, entitlements, general-ledger posting, bank reconciliation and an operational STP connection. A model forecast, an approval and a settled receipt each retain a distinct record linked through the workflow.

## A8. Vintage and cure use identifiable account paths

In a separate 100-account teaching fixture, 20 accounts have ever been 90+ days past due. Today, five remain 90+, four are 1-89 days late, six are current, three have prepaid and two have exited through foreclosure. Of the six currently current, three have three observed consecutive current months; three lack sufficient follow-up. The three-month rule is the operational definition adopted for this fixture; institution use specifies the applicable accounting and regulatory criteria.

| Population or measure | Count / rate |
| --- | --- |
| Original accounts | 100 |
| Active accounts | 95 |
| Ever 90+ | 20 |
| Currently 90+ | 5 |
| Ever minus current, original denominator | 15 |
| Currently current after 90+ | 6 |
| Confirmed three consecutive current months | 3 |
| Incomplete current follow-up | 3 |
| Ever 90+ / original | 20.000% |
| Current 90+ / active | 5.263% |

The 15 accounts that have left 90+ status comprise six currently current accounts, four in lesser arrears, three prepayments and two foreclosures. Three satisfy the stated sustained-current observation rule; the other three current accounts remain in follow-up. Report ever-90+ against the original 100 accounts and current-90+ against the 95 active accounts. A cure study then follows a defined entry population through recurrence, competing exits and censoring using dated account histories.

## A9. Optional transfer of the receivable rights

Financing the business evaluates the enterprise's total ability to repay. Financing **ring-fenced receivables** additionally assesses identified claims, enforceable transfer rights, eligibility, collection-account control, servicing continuity, expenses and distribution priority. This worked example uses a special purpose vehicle (SPV) to purchase **loan repayment receivables**. The customer's KES 800,000 payment enters the borrower's operating ledger; the borrower's scheduled debt service supplies the vehicle's collections. The two ledgers follow the same economic chain with explicit ownership and payment boundaries.

The optional vehicle purchases ten loans of the A2 size at KES 500,000 each. Its day 0 is the purchase date: five loans are already 30 days old and mature on vehicle day 30; five are newly originated and mature on vehicle day 60. Each transfers a KES 515,000 scheduled claim. The illustrative par purchase includes all that interest, including the seasoned loans' accrued portion; the seller retains origination fees. This stated transfer-price assumption makes the allocation reproducible. A transaction assessment adds market valuation, the seller's gain or loss and pre-transfer funding costs. Loan age and vehicle age are tracked separately. Collections after sale belong to the vehicle; the bank hold-to-resolution case represents the alternative ownership choice.

| Opening sources, KES | Amount | Opening uses, KES | Amount |
| --- | --- | --- | --- |
| Class A | 3,500,000.00 | Receivable purchase | 5,000,000.00 |
| Class B | 1,000,000.00 | Funded reserve | 250,000.00 |
| Equity | 750,000.00 | Total uses | 5,250,000.00 |
| Total sources | 5,250,000.00 |  |  |

Class A pays 8% and class B 12%, simple ACT/360, on outstanding principal. Principal amortises with the two asset batches. Servicing and vehicle expenses are KES 10,000 per 30 days of existence, payable at the displayed distribution dates. The static runoff assumes zero interest on deferred note interest, zero reserve investment income and zero tax; it follows the initial ten-loan pool through final resolution. Replenishment and guarantee arrangements can be added as separately funded flows. The fully funded reserve is part of opening sources and uses, with every draw and release tracked through the cash ledger.

### Contractual priority used in the computation

1. Pay outstanding vehicle expenses, then class A interest, scheduled class A principal, class B interest and scheduled class B principal.
2. In normal amortisation, reserve cash may meet each scheduled obligation. Refill the reserve before interim equity distributions.
3. Overcollateralisation is eligible principal divided by outstanding note principal, tested before that date's asset collections and distributions. A ratio below 1.05 triggers early amortisation immediately. A scheduled payment shortfall also triggers early amortisation, governing subsequent allocations; the trigger is sticky.
4. In early amortisation, apply available collection cash to all outstanding principal in the same A-before-B priority. Reserve draws support expenses and note interest, including B interest, while accelerated principal uses collection cash. This restricted-use reserve rule is explicit: it can support B interest while A principal remains outstanding. Alternative note terms would produce different results.
5. Trap equity cash while early amortisation persists. At final runoff, apply all remaining reserve first to unpaid expenses and notes, then release any residual. The default path retains cash until its recovery is resolved, even if all notes have already been repaid.

The code records opening and closing cash, reserves, note principal, unpaid interest, receipts, each distribution and a conservation residual for every date. Cash plus reserve follows:

$$
C_t+R_t=C_{t-1}+R_{t-1}+\text{asset receipts}_t
-\text{expenses paid}_t-\text{note payments}_t-\text{equity distributions}_t.
$$

| Pool scenario | Asset receipts | Note interest | Expenses | Equity cash | Equity gain / loss |
| --- | --- | --- | --- | --- | --- |
| base | 5,150,000.00 | 50,000.00 | 20,000.00 | 830,000.00 | 80,000.00 |
| delay | 5,150,000.00 | 65,222.22 | 20,000.00 | 814,777.78 | 64,777.78 |
| default | 4,835,000.00 | 53,155.56 | 80,000.00 | 451,844.44 | -298,155.56 |

#### Vehicle base: distributions, KES

| Day | Fees | A interest | A principal | B interest | B principal |
| --- | --- | --- | --- | --- | --- |
| 30 | 10,000.00 | 23,333.33 | 1,750,000.00 | 10,000.00 | 500,000.00 |
| 60 | 10,000.00 | 11,666.67 | 1,750,000.00 | 5,000.00 | 500,000.00 |

| Day | Cash held | Reserve held | Equity paid | Early amortisation | Cash residual |
| --- | --- | --- | --- | --- | --- |
| 30 | 0.00 | 250,000.00 | 281,666.67 | No | 0.00 |
| 60 | 0.00 | 0.00 | 548,333.33 | No | 0.00 |

#### Vehicle delay: distributions, KES

| Day | Fees | A interest | A principal | B interest | B principal |
| --- | --- | --- | --- | --- | --- |
| 30 | 10,000.00 | 23,333.33 | 216,666.67 | 0.00 | 0.00 |
| 60 | 10,000.00 | 21,888.89 | 3,283,333.33 | 20,000.00 | 1,000,000.00 |

| Day | Cash held | Reserve held | Equity paid | Early amortisation | Cash residual |
| --- | --- | --- | --- | --- | --- |
| 30 | 0.00 | 0.00 | 0.00 | Yes | 0.00 |
| 60 | 0.00 | 0.00 | 814,777.78 | Yes | 0.00 |

#### Vehicle default: distributions, KES

| Day | Fees | A interest | A principal | B interest | B principal |
| --- | --- | --- | --- | --- | --- |
| 30 | 10,000.00 | 23,333.33 | 2,026,666.67 | 10,000.00 | 0.00 |
| 60 | 10,000.00 | 9,822.22 | 1,473,333.33 | 10,000.00 | 1,000,000.00 |
| 180 | 60,000.00 | 0.00 | 0.00 | 0.00 | 0.00 |

| Day | Cash held | Reserve held | Equity paid | Early amortisation | Cash residual |
| --- | --- | --- | --- | --- | --- |
| 30 | 0.00 | 240,000.00 | 0.00 | Yes | 0.00 |
| 60 | 71,844.44 | 240,000.00 | 0.00 | Yes | 0.00 |
| 180 | 0.00 | 0.00 | 451,844.44 | Yes | 0.00 |

The timing stress delays the first five collections from vehicle day 30 to day 60 while preserving ultimate receipts. The first scheduled distribution exceeds available collections and reserve support, triggering early amortisation; longer note funding reduces residual cash. The credit stress defaults one first-batch loan before the vehicle day-30 distribution, removes its KES 500,000 principal from eligibility and recovers KES 200,000 on vehicle day 180, with KES 20,000 workout cost. This deterministic one-in-ten stress tests the pool's contractual response. The bank case separately uses a 4% default assumption. Vehicle day 180 is measured from purchase; each underlying loan retains its own origination date.

The default stress produces zero note principal loss under the stated inputs and priority. Extend the analysis with correlated defaults, changing eligibility and alternative transfer prices to assess capital, investor risk and valuation. Reported investor returns are total cash gain or loss over each scenario. Annualised equity IRRs can be derived from the dated equity cash flows. Vehicle-investor distributions and the operating borrower's owner earnings retain separate ledgers and denominators.

## A10. Reproduce, change and validate

The assumptions, cash schedules and calculation rules needed to follow the results are stated in sections A1-A9. The [GitHub research lab](https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab) contains the companion software for **U4C-MSME-001**, edition **1 October 2026**: editable inputs, calculation routines, automated checks and version fingerprints. Open its [reproduction guide](https://github.com/TheAlchemistNerd/underwrite-for-collection/blob/main/research_lab/README.md) for the execution commands and file inventory. The governed evidence case U4C-GOV-001 uses the same financial functions.

The implementation retains 40-digit decimal precision and rounds monetary values only for presentation. It verifies the following independently:

- Opening cash plus receipts and borrowing equals operating payments, debt payments, fees and closing cash on each date.
- Loan and note principal reconcile from opening balance through repayment or resolution to closing balance.
- The solved effective interest rate discounts the contractual receipt back to net proceeds.
- The pricing hurdle and the bridge from the margin budget to scenario-weighted earnings reproduce their stated amounts.
- Decision cutoffs preserve information available at the time; approval and settlement retain separate states.
- Every vehicle distribution is limited by available cash, with reserve use and unpaid obligations carried forward explicitly.

The published example uses day-60 maturity, a day-90 late customer receipt, day-180 recovery and day-240 guarantee payment. To extend the event clock, update the dependent schedules, validation rules and tests together. Input fingerprints bind each published explanation to its reviewed assumptions. Baseline runs reproduce the same financial results; sensitivity runs produce separately labelled results for review before publication.

### From the worked case to institution use

| Delivered in this edition | Institution application |
|---|---|
| One order, four borrower schedules, three margin budgets and lifetime cash-earnings bridge | Bank-specific product terms, taxes, fees, underwriting criteria and actual funding costs |
| Discounted receipt and workout-cost comparison | Approved accounting method, stage policy, calibrated scenarios and audit review |
| Recovery/protection timing and verification examples | Legal rights, guarantor terms, data feeds, counterparty risk and empirical recoveries |
| Tested local execution/settlement replay | Real interfaces, access controls, maker-checker permissions, reconciliation and operational testing |
| Static optional pool with timing and credit stresses | Legal transfer, servicing contracts, larger stress surface, market valuation and investor/regulatory treatment |
| Exact regeneration and arithmetic tests | Independent model validation, out-of-time performance, causal identification and production assurance |

The reconciled cash schedules provide inputs for institution-level pricing, funding, liquidity and capital analysis. Each receiving model specifies the quantity, horizon, ownership, accounting convention and approval record it consumes. This supports further curve, ALM, liquidity-ratio and decision-support work through explicit interfaces. For variable-rate Kenyan bank pricing, apply the relevant CBK model and the facility's benchmark and contractual terms. [CBK, Revised Risk-Based Credit Pricing Model](https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf).

### Reading this appendix alongside the whitepaper

The appendix follows the whitepaper's central argument: repayment depends on the economic activity, the evidence available at a decision date, the permitted response and the timing of usable cash. Each connection can be followed within this document:

| Main discussion | Worked evidence in this appendix |
|---|---|
| Part 1: the MSME credit lifecycle and collection cascades | A2: the order's operating surplus, repayment date and liquidity shortfall |
| Part 2a: temporal evidence and feature engineering | A7: effective, known and verified dates; source outages and settlement evidence |
| Part 2b: underwriting, causal identification and lifecycle dependence | A4-A5: assumed outcome paths and cash measures; A8: current status, sustained cure and incomplete follow-up |
| Part 3: fair intervention and collection governance | A2: an expressly approved extension; A7: the distinction between a decision and received cash |
| Part 4: research environments and enterprise credit architecture | A7: event replay, duplicate handling, approval and settlement controls |
| Part 5: pricing, expected credit loss, capital and funding | A3-A6: pricing and recovery; A9: purchase funding, reserve use and investor distributions |

The companion appendix, *Governing evidence and intervention: a reproducible operating case* (U4C-GOV-001), develops the Part 3 connection further. It reconstructs the same opening cash from account transactions, resolves uncertain receipt classifications, and follows an amendment through review, authority, booking and observed payment.
