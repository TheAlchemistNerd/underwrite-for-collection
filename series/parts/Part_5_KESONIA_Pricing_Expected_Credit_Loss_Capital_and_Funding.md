---
title: "Underwrite for Collection"
subtitle: "Part 5: KESONIA Pricing, Expected Credit Loss, Capital and Funding"
author: "Nevil Maloba"
email: "nevillemaloba@gmail.com"
date: "6 September 2026"
lang: "en-GB"
---

# Abstract

A credit facility enters an MSME as working capital and returns to a lender as a sequence of uncertain cash flows. Between those moments, the applicable benchmark may change, invoices may arrive late, a repayment may fail and cure, an intervention may alter behaviour, a guarantee claim may settle, or a recovery may take longer than its ultimate value suggests. Part 5 develops a financial architecture for that uncertainty. It begins with compounded KESONIA and the governed customer premium, then carries contractual and behavioural cash flows into IFRS 9 expected credit loss, internal economic capital, liquidity, asset-liability management, funds-transfer pricing, intervention economics and credit-risk transfer. The same lifecycle evidence supports each use, while horizon, probability measure, discount rule, recognition criteria and accountable owner remain distinct. Guarantees and optional ring-fenced receivables funding enter through contractually defined cash rather than assumed protection. The result is a joined control plane in which transparent pricing and sustainable collection reinforce each other: customer terms can be traced to approved components, accounting loss to probability-weighted cash shortfalls, capital to adverse portfolio outcomes, treasury to the timing of liquidity, and risk transfer to enforceable coverage and settled claims.

## 1. A benchmark reaches the enterprise through a contract

A wholesale distributor receives a variable-rate working-capital facility shortly before its busiest trading season. The enterprise does not experience the benchmark as an abstract monetary-policy signal. It experiences a quoted rate, a repayment amount, a reset date and the amount of cash that remains after suppliers, wages, tax and debt service. If the facility is repaid from daily sales, a small change in interest may be absorbed. If most cash arrives through two invoices near month-end, the same economic rate can produce a more difficult payment path. The benchmark starts the price; the contract and the enterprise's cash conversion cycle determine how that price is lived.

The Kenya Shilling Overnight Interbank Average, or KESONIA, is administered and published by the Central Bank of Kenya. It reflects the volume-weighted average rate on unsecured overnight Kenya shilling interbank transactions. CBK began publishing KESONIA and a KESONIA Compounded Index on 1 September 2025 and publishes the overnight observation for the previous business day. On weekends and bank holidays, the last working-day observation is held constant for the relevant calendar interval [1].

That daily rate is a reference observation. A loan accrual still requires a complete convention. The facility agreement or incorporated product terms must identify the authoritative source, value date, publication time, accrual start and end dates, day-count basis, observation shift or lookback where used, payment delay, rounding, floor, cap, reset frequency, fallback, correction policy and treatment of non-business days. Two facilities can both refer to compounded KESONIA while producing different payment timing because their observation windows or payment conventions differ. Those differences belong in the product record introduced in Part 4.

For an accrual period from \(a\) to \(b\), let \(r_i\) be a published KESONIA observation expressed as a decimal, let \(n_i\) be the calendar days for which that observation applies under the contract, and let \(d=\sum_i n_i\). A transparent compounded factor and annualised rate are:

\[
F_{a,b}=\prod_{i=1}^{d_b}\left(1+\frac{r_i n_i}{365}\right),
\qquad
R_{a,b}^{\mathrm{KESONIA}}
=\left(F_{a,b}-1\right)\frac{365}{d}.
\]

The amount of benchmark interest on principal (B) is (B(F_{a,b}-1)) before the contractual premium and other permitted components. A production engine should calculate from the official published observations or the official compounded index where the chosen convention permits it. An independently reconstructed factor is a control calculation. It is reconciled to the authorised source, calendar and contract before posting.

This calculation carries several operational controls. A received observation has publication date, value date, source digest and validation status. A later source correction creates a versioned event and follows the contractual correction window. Missing publication does not invite an invented rate. CBK's KESONIA materials identify CBR as the alternative reference where KESONIA is impractical and as a fallback when KESONIA data are unavailable, while contracts are expected to address the contingency [1]. The product owner, legal function and treasury function therefore agree the fallback before a customer is charged.

The revised Risk-Based Credit Pricing Model expresses the total lending rate for the relevant variable-rate facility as:

\[
r_{i,t}^{\mathrm{lend}}
=R_{a,b,t}^{\mathrm{KESONIA}}+K_{\mathrm{RBCP},i,t},
\]

and the total cost of credit includes the applicable disclosed fees and charges in addition to that lending rate [2]. CBK's implementation material records the revised model as fully operational from March 2026 and identifies KESONIA compounded in arrears as the common reference for covered variable-rate lending, with CBR available as the alternative reference rate in the stated circumstances [3]. Fixed-rate loans and foreign-currency loans require their own pricing basis.

The formula creates transparency by separating a common market reference from the bank's premium. It does not make every customer's instalment change daily. The contractual accrual and reset rules decide when accumulated benchmark observations affect an amount due. A daily ingestion service may update accrued interest each business day, while customer communication and collection follow the agreed billing cycle. This distinction lets the bank reconcile monetary transmission, contractual entitlement, accounting accrual and customer affordability without forcing them into one timestamp.

## 2. The premium is governed across the credit lifecycle

CBK describes the premium \(K\) as containing lending-related costs, the return to shareholders and the borrower's risk profile, together with other relevant lending costs under the framework [2], [3]. This paper writes it as \(K_{\mathrm{RBCP}}\) so that it cannot be confused with regulatory capital \(K_{\mathrm{reg}}\). It is a published bank-specific or product-specific commercial premium under an approved methodology. The posterior default probability from Part 2b is one possible input to its borrower-risk analysis. It is not the premium by itself.

A bank can govern the premium through a component bridge such as:

\[
K_{\mathrm{RBCP},g,t}
=c_{\mathrm{operate},g,t}
+c_{\mathrm{service},g,t}
+k_{\mathrm{borrower},g,t}
+c_{\mathrm{capital},g,t}
+\pi_{g,t}
+\varepsilon_{g,t},
\]

where \(g\) is an approved product or customer segment, the cost terms use documented allocation rules, \(k_{\mathrm{borrower}}\) is the governed borrower-risk contribution, \(c_{\mathrm{capital}}\) is the institution's pricing charge for allocated capital, \(\pi\) is the approved shareholder-return component and \(\varepsilon\) reconciles other permitted components. This is an internal management decomposition, not a replacement for CBK's definition or the bank's published methodology. Every component needs one owner, an as-of date, an allocation basis and a reconciliation to the approved premium.

### 2.1 Reconcile the customer premium to the Treasury transfer price

The customer rate and the internal transfer price answer related but different questions. The customer rate records the price agreed under the product, contract and approved RBCPM methodology. The transfer price attributes the economic value and cost of funding to the business that originates or holds the asset. A joined pricing architecture therefore preserves both quantities and reconciles them through a visible bridge.

Suppose the contractual benchmark for product group \(g\) during period \(t\) is \(R_{a,b,t}^{\mathrm{KESONIA}}\), and Treasury assigns the group an approved matched transfer rate \(FTP_{g,t}\). Define the Treasury increment over the customer benchmark as:

\[
\Delta FTP_{g,t}
=FTP_{g,t}-R_{a,b,t}^{\mathrm{KESONIA}}.
\]

The increment can be positive or negative. It reflects the relationship between the contractual benchmark and the institution's approved transfer-pricing curve for the asset's behavioural maturity, repricing frequency, liquidity use and embedded options. Its interpretation depends on the FTP policy. A transfer curve based on marginal funding cost answers a different management question from one based on average funding cost, and a matched-maturity method produces a different attribution from a single pooled rate. The selected method should remain consistent across comparable products and should be accompanied by a reconciliation showing how the curve was constructed and applied.

For internal product analysis, the premium can then be viewed through a more granular reconciliation:

\[
\widehat K_{\mathrm{bridge},g,t}
=\Delta FTP_{g,t}
+EL_{g,t}^{\mathrm{price}}
+c_{\mathrm{operate},g,t}
+c_{\mathrm{service},g,t}
+c_{\mathrm{capital},g,t}
+\pi_{g,t}
+\varepsilon_{g,t}^{\mathrm{other}},
\]

subject to:

\[
\widehat K_{\mathrm{bridge},g,t}
=K_{\mathrm{RBCP},g,t}
\quad\text{after approved reconciliation adjustments.}
\]

This bridge is an analytical control beneath the formal CBK expression, not an alternative customer-pricing rule. The external rate continues to follow KESONIA plus the approved premium [2], [3]. Internally, the bridge shows which part of the increment over KESONIA is associated with matched funding and liquidity, which part reflects expected credit loss, which part meets operating and servicing cost, which part remunerates allocated capital, and which part represents the approved commercial return.

The expected-loss term in the granular bridge is the explicit allocation of the borrower-risk contribution already represented by \(k_{\mathrm{borrower}}\) in the higher-level decomposition. A bank may retain the broader borrower-risk term where its approved methodology combines expected loss with other calibrated risk adjustments. It may instead display expected loss and each additional risk adjustment separately. Whichever presentation is selected, the bridge should count each economic component once. IFRS 9 allowance, regulatory capital and internal economic-capital charge retain their separate meanings even when related information contributes to product economics.

The corresponding risk-adjusted contribution before tax can be displayed as:

\[
M_{g,t}^{\mathrm{risk\text{-}adjusted}}
=r_{g,t}^{\mathrm{lend}}
-FTP_{g,t}
-EL_{g,t}^{\mathrm{price}}
-c_{\mathrm{operate},g,t}
-c_{\mathrm{service},g,t}
-c_{\mathrm{capital},g,t},
\]

with fee income and fee-related cost presented in separate lines where the product includes them. Substituting \(r_{g,t}^{\mathrm{lend}}=R_{a,b,t}^{\mathrm{KESONIA}}+K_{\mathrm{RBCP},g,t}\) makes the control relationship visible:

\[
M_{g,t}^{\mathrm{risk\text{-}adjusted}}
=K_{\mathrm{RBCP},g,t}
-\Delta FTP_{g,t}
-EL_{g,t}^{\mathrm{price}}
-c_{\mathrm{operate},g,t}
-c_{\mathrm{service},g,t}
-c_{\mathrm{capital},g,t}.
\]

The formula gives Product, Finance, Credit Risk and Treasury a shared reconciliation without merging their mandates. Treasury owns the transfer curve, liquidity and optionality attribution. Credit Risk owns the calibrated loss input and its limitations. Finance owns accounting recognition and the relationship between management economics and reported results. Capital Management owns the approved allocation and cost-of-capital method. Product owns the customer proposition, while Legal and Compliance confirm that the terms, disclosures and repricing permissions match the approved methodology and contract.

| Pricing or funding element | Primary question | Accountable owner | Required control |
|---|---|---|---|
| Compounded KESONIA | What benchmark applies under the contract? | Product, Legal and Treasury | Authoritative source, observation window, calendar, fallback and correction history |
| Treasury transfer rate | What funding and balance-sheet value is attributed to this asset? | Treasury | Approved curve, behavioural maturity, repricing convention and effective date |
| Treasury increment over KESONIA | How does internal matched funding differ from the customer benchmark? | Treasury and Product Finance | Reconciliation of curve, liquidity, basis and option effects |
| Expected-loss pricing input | What central credit loss is attributed to the product horizon? | Credit Risk | Compatible PD, EAD, LGD, recovery timing, scenario and exposure basis |
| Operating and servicing cost | What resources are consumed from origination through collection? | Finance and Operations | Activity-based allocation, volume basis, treatment cost and periodic back-testing |
| Capital charge | What return is required for the capital allocated to adverse loss? | Capital Management | Capital measure, allocation method, horizon, confidence standard and cost of capital |
| Commercial return | What approved residual return remains after the recognised costs? | Product and Finance | Hurdle, portfolio strategy, competition, affordability and governance approval |
| Fees and charges | What separately disclosed amounts apply to the customer? | Product, Legal and Finance | Contractual entitlement, disclosure, tax treatment and total-cost reconciliation |

The bridge is established at a governed pricing date. A new offer uses the benchmark convention, transfer curve, risk estimates, cost allocation and capital charge approved for that date. Contractual benchmark resets then follow the facility terms. Treasury may update its internal view of funding cost and behavioural maturity for management reporting without silently changing the customer's contractual premium. Where the contract permits repricing, the customer-facing change follows the documented product process, disclosures, notice period and approval route.

Price also changes behaviour. A wider premium can reduce take-up, change utilisation, encourage early repayment by stronger borrowers, increase payment pressure on marginal borrowers, or alter refinancing demand. Those responses affect the size, composition and timing of the asset book that Treasury must fund. Product planning should therefore connect price bands to acceptance, utilisation, prepayment, first-payment default, cure and early closure. Part 6 can estimate those relationships prospectively, while Part 5 carries the resulting cash-flow distributions into margin and liquidity analysis.

Randomised evidence from a South African consumer lender found downward-sloping credit demand and a stronger loan-size response to maturity than to price, consistent with binding liquidity constraints [4]. Its contribution here is experimental design, while Kenyan elasticity remains a quantity to be estimated from the relevant population. A pricing experiment should vary and measure rate, tenor and repayment burden together, then follow acceptance, utilisation, arrears and realised contribution. Treasury can therefore distinguish a rate that improves unit margin from a rate or maturity combination that changes the funded portfolio, customer selection and cash-flow timing.

The monthly pricing and transfer-pricing control pack should reconcile at least five views: the customer contract, the product subledger, the Treasury transfer record, the profitability ledger and the general ledger. Differences are classified by benchmark timing, curve version, behavioural assumption, modification, fee treatment, accounting basis or operational error. Material unexplained differences move through an assigned investigation and approval workflow. This turns the pricing bridge into an operating control rather than a formula displayed only at product approval.

The borrower-risk component can use expected loss, transition risk, recovery cost and concentration evidence. Its units must remain consistent. A one-year PD cannot be multiplied by a lifetime LGD and a point-in-time balance and then compared directly with an annual interest margin. For a facility \(i\), product horizon \(h\) and physical probability measure \(\mathbb P\), a simple expected-loss rate is:

\[
EL_i(h)
=\frac{
\mathbb E_{\mathbb P}\!\left[L_i(h)\mid\mathcal I_{i,t}\right]
}{E_i(h)},
\]

where \(L_i(h)\) is the defined cash loss over the horizon, \(\mathcal I_{i,t}\) is the evidence available at pricing time and \(E_i(h)\) is a compatible exposure or average-balance denominator. A richer calculation follows monthly default, cure, drawdown, recovery and expense cash flows. Either approach produces a pricing input after calibration and governance. It does not determine the whole \(K_{\mathrm{RBCP}}\).

Lifecycle underwriting improves that input by distinguishing customers whose origination profile looks similar but whose later cash conversion and repayment evidence diverge. The explicit features, residual AI representation and hierarchical effects described in Part 2b can update the distribution of future cash loss. Part 3 then chooses from authorised actions. A rising posterior risk estimate may prompt a review, an affordable payment-date alignment, a limit change or a collections intervention. The existing facility's customer premium changes only when the contract and approved policy permit repricing or when new terms are lawfully agreed.

Peer-reviewed transaction-level evidence from a Chinese fintech found that machine-learning models using non-traditional information improved loss and default prediction relative to traditional comparators, particularly under the studied aggregate credit shock, while the comparative advantage narrowed as customer credit history lengthened [5]. The institutional setting and data differ from Kenya. The study therefore strengthens the manuscript's regime-aware challenger design: measure the residual contribution of AI by relationship depth, portfolio segment and stress period, and retain it where local out-of-time cash-loss forecasts improve after calibration, stability and governance tests.

This creates four different commercial moments:

1. **New-offer pricing** applies the current benchmark, published premium methodology, product economics and customer assessment to a proposed facility.
2. **Contractual repricing** follows the benchmark and reset mechanics already agreed for an existing variable-rate facility.
3. **Limit or eligibility management** governs additional exposure, renewals and new draws without retrospectively rewriting accrued terms.
4. **Modification** changes contractual cash flows through an authorised process with affordability, conduct and accounting consequences.

The Credit Policy and Compliance Gate owns the permissible route. It receives posterior risk, uncertainty, evidence quality, affordability, product exposure and portfolio constraints, then combines them with law, contract and institutional policy. This keeps the role of AI economically useful and operationally bounded. The model improves the estimate of future outcomes; the institution decides which terms and actions are permitted.

Pricing governance also asks whether the premium remains sustainable for the enterprise. A higher charge may cover a greater expected loss on paper while increasing payment stress, adverse selection or early exit. The bank should therefore test acceptance, utilisation, first-payment default, cure, net recovery, complaints and repeat borrowing by price band. Part 6 will treat those outcomes as evidence to be measured rather than assuming that a wider margin always improves risk-adjusted return.

## 3. One lifecycle distribution, several financial measures

Once a facility has been disbursed, its financial meaning is carried by cash and time. A scheduled instalment is a contractual claim. A settled payment is liquidity. A missed payment is a state transition whose eventual loss depends on cure, modification, recovery and cost. A guarantee is a contingent cash flow whose value depends on coverage, documentation, claim acceptance and settlement timing. A model that stops at default probability leaves most of that economic path unrepresented.

For facility \(i\), month \(m\) and scenario \(s\), define net lender cash as:

\[
CF_{i,m}^{(s)}
=C_{i,m}^{P,(s)}+C_{i,m}^{I,(s)}+C_{i,m}^{F,(s)}
+R_{i,m}^{(s)}+G_{i,m}^{(s)}
-O_{i,m}^{\mathrm{serv},(s)}-O_{i,m}^{\mathrm{work},(s)}
-T_{i,m}^{(s)},
\]

where the three \(C\) terms are collected principal, interest and fee cash; \(R\) is recovery net of amounts already represented elsewhere; \(G\) is an eligible guarantee or insurance settlement; \(O^{\mathrm{serv}}\) is servicing cost; \(O^{\mathrm{work}}\) is direct workout cost; and \(T\) is the cost of the intervention assigned to that account. Refunds, collateral proceeds and recoveries are separate event families until their legal owner, gross amount, cost and allocation have been reconciled.

The HLR supplies conditional transition probabilities and uncertainty under the physical measure \(\mathbb P\). A timing challenger may refine when default, cure or recovery occurs. The product subledger supplies contractual schedules, outstanding balances and draw availability. The causal layer supplies an estimated intervention effect where the assignment design supports one. A cash-flow engine combines these objects without changing their provenance. It can then produce a distribution of principal, interest, expense, shortfall and recovery by month, product, sector, geography and institution.

That distribution has several destinations. Customer pricing asks which approved terms are sustainable at origination or renewal. IFRS 9 asks for probability-weighted discounted cash shortfalls at the reporting date. Economic capital asks how much adverse loss the institution chooses to withstand over a defined horizon and confidence standard. Treasury asks when cash arrives, when funding reprices and which gaps remain under stress. Risk transfer asks which losses are contractually covered and when a claim becomes cash. An investor valuation may ask for market-consistent discounting or a required return. Each use starts from common events but applies a different lens.

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
flowchart LR
    A[LIFECYCLE EVIDENCE<br/>contract, balance, payment, exposure,<br/>state, intervention and macro context] --> B[PHYSICAL CASH-FLOW DISTRIBUTION<br/>collection, cure, modification, default,<br/>recovery, cost, timing and uncertainty]
    B --> C[CUSTOMER PRICE<br/>benchmark, approved premium,<br/>fees and affordability]
    B --> D[IFRS 9 ECL<br/>stage, scenarios, cash shortfall,<br/>discount and accounting controls]
    B --> E[ECONOMIC CAPITAL<br/>one-year loss, dependence,<br/>concentration and tail standard]
    B --> F[LIQUIDITY AND FTP<br/>settlement, behavioural maturity,<br/>repricing and matched funding]
    B --> G[RISK TRANSFER<br/>coverage, claims, counterparty,<br/>basis and net retained loss]
    B --> H[OPTIONAL INVESTOR VIEW<br/>asset yield, structural protection,<br/>required return and valuation]

    classDef evidence fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.8px;
    classDef engine fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.9px;
    classDef destination fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.7px;
    class A evidence;
    class B engine;
    class C,D,E,F,G,H destination;
```

**Figure 1: From lifecycle evidence to distinct financial measures.** One physical cash-flow distribution preserves the relationships among prediction, collection and loss. Each destination then applies its own horizon, recognition rule, discounting, governance and accountable owner.

The probability measure matters most where valuation departs from forecasting. Under \(\mathbb P\), default and recovery estimates describe outcomes expected in the operating world represented by observed data and approved scenarios. A market-consistent measure \(\mathbb Q\) is useful where an institution values a tradable or contingent claim against sufficiently informative market prices and a documented calibration method. Adding a spread to KESONIA does not perform that transformation. In a market with limited comparable MSME credit instruments, the investor hurdle may be a transparent required return with sensitivity ranges rather than an asserted risk-neutral intensity.

Keeping the measures distinct supports innovation. The bank may use the full posterior distribution to stress future cash, a simpler approved quantity for a customer offer, a probability-weighted shortfall for impairment and a separately calibrated tail distribution for internal capital. Consistency means that the same borrower cannot be assumed current in one engine and defaulted at an earlier date in another without a documented reason. It does not require every function to use one number.

## 4. IFRS 9 follows probability-weighted cash shortfalls

IFRS 9 measures expected credit losses as probability-weighted credit losses that incorporate the time value of money and reasonable and supportable information available without undue cost or effort about past events, current conditions and forecasts of future economic conditions. The framework is principles-based and permits methods that satisfy those requirements [6]. The lifecycle architecture contributes event history, calibrated transitions and cash-flow timing. The reporting entity's accounting policy determines how those inputs become an allowance.

Let \(CS_{i,m}^{(s)}\) be the cash shortfall in month \(m\) under forward-looking scenario \(s\), measured as the contractual cash due to the reporting entity less the cash it expects to receive, including cash flows from eligible collateral and contractual credit enhancements where the accounting requirements include them. With scenario weight \(\pi_s\), original effective interest rate \(EIR_i\) and time fraction \(\tau_m\), a cash-shortfall expression is:

\[
ECL_i
=\sum_{s=1}^{S}\pi_s
\sum_{m\in\mathcal H_i}
\frac{CS_{i,m}^{(s)}}{(1+EIR_i)^{\tau_m}},
\qquad
\sum_{s=1}^{S}\pi_s=1.
\]

The horizon \(\mathcal H_i\) depends on the applicable impairment stage and instrument requirements. Twelve-month ECL is the portion of lifetime cash shortfalls associated with defaults possible within the next twelve months. It is not limited to cash that happens to be missed during the next twelve months. Lifetime ECL reflects default risk across the expected life. The distinction is important for short MSME facilities, revolving lines and facilities whose behavioural use extends beyond one contractual billing interval [6].

The model-to-ECL bridge therefore contains more than a PD field. For each reporting date it stores the instrument population, stage, default definition, scenario-conditioned marginal or conditional PD term structure, EAD path, LGD or expected cash-shortfall path, prepayment, cure, recovery timing, directly attributable recovery assumptions, contractual credit enhancements, original EIR, currency, source versions and overlay. The bank reconciles opening allowance, new originations, repayments, transfers between stages, changes in risk, modifications, write-offs, recoveries and closing allowance.

Significant increase in credit risk, or SICR, is an accounting assessment of the change in lifetime default risk since initial recognition. A lifecycle score may provide relevant evidence through payment status, cash-flow deterioration, utilisation, adverse restructuring, sector stress or a material increase in calibrated lifetime risk. The approved policy combines those signals with qualitative indicators, backstops and reasonable forward-looking information. It also distinguishes a temporary data outage from economic deterioration.

Operational cure and accounting improvement are related but separately governed. A customer can clear an arrear and become operationally current today. The bank may require a sustained performance period, supporting evidence and reconsideration of forward-looking risk before concluding that credit risk has improved enough for an accounting stage transfer. The durable-cure definition from Part 1 provides evidence for that assessment without becoming a universal accounting rule. The same separation applies to re-default: a renewed delinquency after cure updates the observed transition history and tests whether the cure policy was economically durable.

Modification is another cash-flow event rather than a label for failure. An affordable term extension may improve collection and reduce ultimate loss while changing the present value of the asset. Where a modification of a financial asset does not result in derecognition, IFRS 9 requires the gross carrying amount to be recalculated as the present value of modified contractual cash flows discounted at the original EIR, with the applicable modification gain or loss recognised [6]. The contract workflow records the authorised new schedule, customer acceptance, purpose, effective date and accounting classification. The ECL engine then measures the remaining credit risk under the approved policy.

Write-off records the reduction of gross carrying amount when there is no reasonable expectation of recovery for all or part of the asset under the applicable requirements. It does not end the need to record later recovery cash, legal status or customer treatment. Recovery after write-off remains a distinct event with receipt date, gross amount, direct cost and accounting destination. This is why Part 4 required collection and finance records to remain joined after the credit decision.

The financial-stability consequence of forward-looking impairment belongs in the same control pack without changing the accounting measure. The European Systemic Risk Board found that expected-loss recognition can concentrate effects on profit and regulatory capital near the beginning of a deteriorating phase, depending on migration and scenario dynamics [7]. Used as comparative financial-stability evidence, the finding supports coherent but separately reported ECL, capital and liquidity stresses. An earlier allowance signal can then inform funding and capital planning while retaining its accounting identity rather than being relabelled as a cash outflow or regulatory-capital requirement.

The BCBS guidance on credit-risk practices for expected credit losses emphasises robust methodologies, experienced credit judgement, common processes, data and validation, while recognising that accounting frameworks determine the allowance [8]. The bank should therefore validate ECL components at their proper levels: discrimination and calibration for risk estimates, transition and cure accuracy, recovery amount and timing, scenario sensitivity, stage allocation, overlay governance and total allowance back-testing. A good account-level score can coexist with a poor ECL if timing, exposure, recovery or scenario assumptions are weak.

The accounting owner also controls the relationship between model output and journals. A production HLR artefact can send approved PD term structures, uncertainty, evidence quality and lineage into the impairment platform. It does not post its own allowance. Finance and credit-risk functions approve the scenario weights, stage logic, LGD, EAD, recovery assumptions and overlays, and the general ledger receives a balanced journal with reconciliation keys. This preserves the value of continuous evidence while keeping financial reporting reproducible.

## 5. Economic capital carries the adverse portfolio story

Expected loss describes the centre of a defined loss distribution. The accounting allowance applies IFRS 9 recognition and measurement to expected cash shortfalls. Regulatory capital follows the rules in the applicable CBK prudential framework. Internal economic capital is the institution's assessment of capital needed to absorb adverse loss at a stated horizon, confidence standard and solvency objective. The four quantities can use related data, but they have different mandates and cannot be substituted for one another.

The CBK Prudential Guidelines set the local capital-adequacy and asset-classification framework for regulated institutions [9]. The bank maps each exposure, mitigant and calculation to the currently applicable requirements and supervisory treatment. A better behavioural model may improve risk management before it changes any regulatory parameter. Recognition follows validation, governance and the method permitted for that institution.

For internal analysis, let \(L_{1y}\) be the one-year portfolio loss after ordinary contractual collections and recoveries but before capital absorbs the outcome. Let \(\rho_q\) be the board-approved risk functional at confidence level \(q\). Economic capital can be represented as:

\[
EC_q=\rho_q(L_{1y})-\mathbb E[L_{1y}],
\]

with \(\rho_q=VaR_q\) under a quantile standard or \(\rho_q=ES_q\) where the institution uses expected shortfall. The horizon, confidence level, treatment of expected loss, tax, diversification, pension or operational risks and capital definition must be stated. A number without those choices is not a capital measure.

The simulation or analytical engine draws coherent outcomes. Borrower transitions respond to common macroeconomic and sector factors, facility-level evidence and hierarchical effects. EAD reflects scheduled amortisation, further draw, cancellation and conversion. LGD reflects cure, collateral or guarantee cash, workout cost and recovery delay. Parameter draws propagate posterior uncertainty. Dependence challengers test residual clustering after observable common drivers have been represented. Model-form scenarios compare the champion with credible alternatives.

The relationship between systematic factors and apparent diversification is structural, not merely a reporting preference. Gordy's risk-factor foundation for ratings-based capital shows the special conditions under which an exposure-level capital charge can be independent of the rest of the portfolio, including a single systematic factor and an asymptotically fine-grained portfolio [10]. An MSME book with platform, sector, supply-chain or geographic clusters can violate the economic spirit of those conditions even when it contains many accounts. Part 5 therefore preserves portfolio simulation, concentration diagnostics and factor-specific reverse stress rather than treating borrower count as diversification.

Where the approved risk measure is positively homogeneous and sufficiently differentiable, marginal or Euler allocation can decompose portfolio capital into contributions that reconcile back to the portfolio total. Tasche's credit-portfolio work develops estimators for such contributions [11]. The implementation should state the risk measure and test allocation additivity, numerical stability and tail-sample error. A convenient segment allocation is not accepted merely because it sums: it must also represent how that segment changes portfolio risk at the margin.

This matters for MSME portfolios because diversification can be overstated by counting borrowers rather than economic drivers. Restaurants in different neighbourhoods may depend on the same delivery platform. Retailers may share an importer, currency exposure or landlord. Farmers and processors may share rainfall and commodity shocks. Transport businesses may share fuel-price sensitivity. The current Basel supervisory principles identify sector, geography, product, collateral, currency, funding source and economic interdependence as relevant forms of concentration and require forward-looking stress testing across material risks [12], [13].

The internal capital pack should therefore report expected one-year loss, selected quantiles, expected shortfall where used, scenario loss, concentration add-ons, marginal and allocated capital, and the contribution of parameter and model uncertainty. Reverse stress identifies the combination of default timing, utilisation, recovery delay and common shock that first breaches a capital or risk-appetite boundary. Management can then change limits, sector mix, collateral, guarantee use, collection capacity or pricing through approved policy.

Allocated economic capital also supports product economics. For product or segment \(g\), a risk-adjusted contribution may be expressed as:

\[
RA_g
=Y_g-FTP_g-EL_g-OpEx_g-CoC\times EC_g,
\]

where each term uses the same period and exposure basis. This is a management view, not the customer-rate formula. It can show that a product with high nominal yield consumes disproportionate collection capacity, liquidity or tail capital. It can also show that an intervention which lowers durable loss and tail dependence creates value even when immediate interest income falls.

## 6. Collection timing becomes a treasury variable

An instalment can be economically valuable and still arrive too late to fund today's obligation. A promise to pay, a pending mobile-money instruction, an uncleared cheque, an accepted guarantee claim and cash in the settlement account are different liquidity states. The lifecycle ledger therefore records initiation, acceptance, settlement, reversal and final allocation separately. Treasury receives cash only when the account-control and settlement rules say it is available.

Kenyan payment law gives this event chain a precise legal anchor. The National Payment System Act distinguishes payment instructions, clearing, settlement obligations and settlement, and provides that settlement effected through the relevant system is final and irrevocable [14]. The National Payment System Regulations separately define an electronic retail transfer and real-time settlement, including completion of the debit and credit and simultaneous notification [15]. These definitions establish the settlement boundary. Treasury's further tests for legal-entity ownership, account restriction, availability and correct loan allocation remain internal and contractual controls after that boundary.

For time bucket \(b\), a simple cumulative liquidity position is:

\[
LG_b=C_0+\sum_{m\le b}
\left(CF_m^{\mathrm{settled}}+F_m^{\mathrm{available}}
-D_m^{\mathrm{contractual}}-O_m^{\mathrm{operating}}
-U_m^{\mathrm{contingent}}\right),
\]

where \(C_0\) is usable opening cash, \(F^{\mathrm{available}}\) is committed or reliably available funding, \(D\) is debt and depositor cash due, \(O\) is operating cash outflow and \(U\) is a scenario allowance for undrawn commitments, payment reversals, claim delay or other contingent use. The ladder is run by currency and legal entity. A positive expected ultimate recovery does not cure a negative near-term bucket until its timing and availability are credible.

Behavioural maturity links Part 2b to this ladder. A nominal 30-day facility may remain outstanding after a payment-date alignment, modification or partial cure. A revolving limit can draw when the enterprise's operating cash is already under pressure. Recovery may have a high ultimate percentage and a long legal delay. Treasury stresses those timing channels together with failed-payment recycling, concentration, guarantee settlement and new-funding availability.

CBK's KEPSS disclosure report illustrates the distinction in Kenya's high-value payment infrastructure: payment orders settle in real time when funding and technical conditions are met, and the resulting settlement finality is protected under the National Payment System Act [16]. Retail, mobile-money and platform rails can have different processing and account arrangements. The architecture therefore records the governing rail and its rules instead of applying the KEPSS timing convention to every collection.

The Basel liquidity principles call for prospective cash-flow forecasts across assets, liabilities and off-balance-sheet items, realistic behavioural assumptions, explicit allocation of liquidity costs and stress testing over multiple horizons [17]. CBK's 2025 guidelines add the applicable Kenyan LCR, NSFR and leverage-ratio framework for regulated banks [18]. Lifecycle evidence improves the behavioural inputs to those processes. Treasury and finance retain the approved regulatory calculations.

### 6.1 Recognise cash through settlement finality, availability and allocation

High-frequency activity becomes a Treasury input through an explicit sequence of states. The merchant records a sale; a payment instruction is initiated; the payment service accepts or rejects it; the relevant rail processes it; settlement becomes final under the applicable arrangement; the collection account receives value; account-control rules determine whether the value is available; and the loan subledger allocates the receipt to the correct obligation. A reversal, chargeback, disputed payment or reconciliation break can interrupt that sequence. Each timestamp answers a different operational question.

For realised cash event \(e\), define \(I_e^{\mathrm{final}}\) as the indicator that settlement is final and \(I_e^{\mathrm{available}}\) as the indicator that the funds are available to the relevant legal entity under its account and control arrangements. The amount recognised in Treasury's realised cash position is:

\[
CF_{e}^{\mathrm{Treasury}}
=CF_e^{\mathrm{gross}}
I_e^{\mathrm{final}}
I_e^{\mathrm{available}}
-C_e^{\mathrm{rail}}
-C_e^{\mathrm{reversal}}
-C_e^{\mathrm{restricted}},
\]

where the cost and restriction terms represent amounts that are separately identified and supported by the ledger. In implementation, multiplication by the indicators applies to the gross receipt, while each deduction follows its own recognition rule. The expression emphasises the governing principle: an observed transaction signal can support forecasting before it qualifies as realised, usable cash.

The lifecycle ledger should therefore expose at least the customer transaction time, payment-instruction time, channel acknowledgement, settlement date, value date, collection-account receipt, availability date, allocation date, reversal status and reconciliation status. Treasury can aggregate the final events into intraday and daily cash positions. Credit Risk can use earlier permitted signals for monitoring, while preserving their status as evidence rather than cash. Finance can reconcile the final allocation to the product subledger and general ledger. This shared event chain prevents a fast behavioural signal from being credited twice, first as expected collection and again as settled liquidity.

Mobile-money and platform-linked repayment require particular attention to cut-off times, weekends, bank holidays, prefunding, trust or settlement-account structure, service outages, failed instructions and concentration in a payment provider. The contractual due date can differ from the date on which the borrower initiates payment and from the date on which the institution can redeploy the value. The cash-flow engine retains all three. Treasury forecasts the actual availability date, Operations manages failed and unmatched items, and customer treatment follows the contractual and conduct framework.

### 6.2 A Treasury recognition gate converts behaviour into an approved assumption

A behavioural model may predict that daily or weekly collections shorten a portfolio's realised weighted-average life. Treasury recognises that benefit only after the relevant evidence passes a controlled validation gate. The gate is applied to each product, channel, cohort and material customer segment because aggregate stability can conceal a fragile subgroup or a concentrated payment route.

The recognition test addresses:

- settlement success and finality;
- reversal, return and dispute rates;
- time from instruction to available cash;
- weekend, holiday and cut-off effects;
- payment-rail and servicing outages;
- concentration by platform, aggregator, bank account and customer;
- persistence across vintages and economic conditions;
- prepayment, modification, cure and re-default behaviour;
- direct processing and servicing cost;
- customer affordability and working-capital retention;
- forecast error at each liquidity horizon;
- and performance under the approved stress scenarios.

Let \(\widehat{CF}_{g,b}^{\mathrm{settled}}\) be the forecast settled cash for group \(g\) and bucket \(b\). Treasury can express the available planning amount as:

\[
\widehat{CF}_{g,b}^{\mathrm{available}}
=\widehat{CF}_{g,b}^{\mathrm{settled}}
-H_{g,b}^{\mathrm{operations}}
-H_{g,b}^{\mathrm{behaviour}}
-H_{g,b}^{\mathrm{concentration}}
-H_{g,b}^{\mathrm{model}},
\]

where each \(H\) is a scenario-dependent deduction supported by evidence and governance. The terms are internal planning adjustments rather than regulatory haircuts. They can be represented through direct cash-flow stresses, conservative percentiles or another approved method. The method should preserve dependence between lower collections, longer settlement, greater drawdown and weaker recovery during the same adverse state.

The approved behavioural maturity follows the distribution of available principal cash rather than the number of payment messages. Thirty daily instructions do not create thirty independent sources of liquidity when they depend on one platform, one settlement account or the same underlying sales cycle. Similarly, a frequent deduction programme can produce an apparently short asset life by removing cash required for inventory and causing later re-default. The recognition test therefore examines durable cure, subsequent utilisation, working-capital sufficiency and total net recovery beside early cash velocity.

Model approval occurs in stages. Shadow operation first measures forecast accuracy and operational readiness without using the new assumption in live Treasury decisions. A controlled live phase then produces realised settlement and customer-outcome evidence. Independent validation assesses calibration, stability, sensitivity and limitations. Treasury proposes a behavioural assumption, Model Risk reviews the supporting method, Finance checks reconciliation, and ALCO approves the use, limit and review date. A material deterioration in settlement, forecast error, concentration or customer outcome can return the assumption to a more conservative state.

### 6.3 Separate accelerated cash from incremental cash and durable recovery

An intervention can change cash timing without changing the total amount eventually collected. It can also increase ultimate collection, reduce it, or create an early receipt followed by re-default. Treasury and Collections should decompose the observed effect rather than treating every post-intervention payment as new value.

For intervention \(a\) and comparator \(0\), the difference in expected collections can be separated conceptually as:

\[
\Delta CF_{a,0}
=\Delta CF_{a,0}^{\mathrm{timing}}
+\Delta CF_{a,0}^{\mathrm{ultimate}}
+\Delta CF_{a,0}^{\mathrm{durable\ cure}}
-\Delta CF_{a,0}^{\mathrm{redefault}}
-\Delta C_{a,0}^{\mathrm{operations}}.
\]

The timing term measures cash moved between buckets while holding ultimate collection constant. The ultimate term measures a change in the total collected amount over the governed horizon. The durable-cure term represents sustained restoration of payment performance. The re-default term captures early improvement that later reverses, and the operating-cost term captures the additional resources and payment-rail costs required to obtain the result. The components can overlap in raw observations, so the empirical design defines mutually consistent estimands and reconciliation rules.

This decomposition supports three distinct decisions. Treasury can value earlier cash even where ultimate recovery is unchanged. Credit Risk can evaluate whether the intervention changes default, cure and loss. Product and Conduct can evaluate whether the payment path remains affordable and sustainable. Part 6 should estimate the causal quantities where randomisation or a credible quasi-experimental design supports them. Until then, Part 5 can run transparent sensitivities rather than assigning causal meaning to association.

Randomised credit studies show why this decomposition must remain multidimensional. A field experiment with distressed credit-card borrowers in Indonesia found that a specific message treatment reduced delinquency, while experimental microfinance evidence from India found that a repayment grace period increased business investment and profits but also increased default [19], [20]. The studies concern different markets and treatments, yet together they demonstrate the relevant design principle: an intervention can change repayment, enterprise outcomes and credit loss in different directions. The Part 5 value equation therefore follows timing, durable cure, re-default, operating cost and customer outcomes rather than converting an early payment into assumed economic success.

### 6.4 Connect the operational ladder to LCR, NSFR and ordinary liquidity management

The internal cash ladder, the regulatory liquidity ratios and the stock of high-quality liquid assets are related control views with different definitions. A settled loan repayment increases cash available to the institution under its account arrangements. Its treatment in the Liquidity Coverage Ratio follows the applicable inflow definitions, caps and scenario rules. The repayment itself does not become a high-quality liquid asset merely because it arrived frequently. Once received, the institution may hold the resulting value in an asset that qualifies under the applicable framework, subject to that asset's own criteria and haircut [18].

The LCR view focuses on the prescribed short-term stress horizon. Treasury maps eligible outflows, recognised inflows and the qualifying liquid-asset stock under the current CBK rules. The internal ladder can be more granular, extending from intraday and daily buckets through weekly, monthly and longer horizons. Differences between internal and regulatory treatment are retained as named adjustments. This allows high-frequency collection evidence to improve operational forecasting while the formal ratio remains reproducible under its governing definitions.

The NSFR view addresses the relationship between available stable funding and required stable funding over the applicable structural horizon [18]. A short contractual MSME facility may still require a longer behavioural funding assumption if revolving use, modification or re-default extends its life. Conversely, reliable amortisation can reduce the outstanding balance over time. Treasury maps the exposure according to the regulatory framework and separately maintains the richer behavioural profile used for internal ALM. Neither view is inferred solely from payment frequency.

Ordinary liquidity management also covers risks that sit outside a single ratio. Treasury monitors concentrations of deposits and wholesale funding, unencumbered collateral, committed and uncommitted facilities, currency mismatches, settlement-account exposures, payment-provider dependencies, contingent drawdowns, guarantee-claim delays and the timing of recovery. These factors feed the cash ladder and the institution's risk appetite even where they have limited effect on a reported ratio in the current period.

### 6.5 Contingency funding begins before a ratio is breached

The contingency funding plan translates adverse cash projections into pre-authorised actions. Its triggers can include persistent forecast error, settlement disruption, unusual deposit outflow, drawdown acceleration, reduced market access, collateral calls, concentration events, guarantee-claim delay, covenant pressure or deterioration in the available liquidity buffer. The escalation process identifies the decision owner, communication route, available actions, execution time and recovery condition.

The scenario set should combine credit and liquidity channels. An MSME revenue shock can reduce repayments, increase revolving draws, lengthen cure, delay recoveries and raise demand for modifications. A payment-platform outage can defer otherwise performing cash. A KESONIA increase can raise wholesale funding cost and customer debt service on different reset dates. A loss of confidence can cause deposit outflow while the asset book extends. Treasury tests these combinations across intraday, short-term and structural horizons rather than moving each variable independently.

Available responses can include using the approved liquidity buffer, drawing a committed facility, adjusting new origination, changing eligible product mix, increasing term funding, pledging eligible collateral, executing an approved hedge, limiting undrawn commitments, accelerating a ring-fenced funding transaction or invoking contractual cash controls. Customer-facing measures remain within the Credit Policy and Compliance Gate and applicable conduct requirements. The contingency plan identifies actions that preserve liquidity without transferring distress to customers through unsuitable collection.

The plan is tested through simulations and operational exercises. Treasury records the time needed to obtain data, convene decision makers, mobilise collateral, access a facility, reconcile settlement accounts and communicate with relevant parties. Lessons update the liquidity model, operational playbook and limits. This closes the gap between a mathematically positive liquidity position and cash that the institution can actually mobilise during stress.

## 7. ALM and matched-maturity FTP translate cash timing into product economics

Asset-liability management asks how contractual and behavioural asset cash flows interact with funding, repricing, embedded options and liquidity. Funds-transfer pricing attributes the relevant cost or benefit to a product or relationship so that commercial performance is not confused with an unpriced treasury position. Neither function is a synonym for KESONIA or \(K_{\mathrm{RBCP}}\).

An international survey of 38 large banks conducted for the BIS Financial Stability Institute found that weak liquidity-transfer-pricing practice often used average rates, failed to charge assets and credit liabilities consistently, and did not transmit current marginal funding costs. Its better-practice conclusion was a centrally governed, marginal and matched-maturity approach, including blended rates for amortising or non-maturing products and charges for contingent liquidity use [21]. That evidence supports the architecture below while leaving the institution to construct a Kenya shilling curve from its own funding capacity, balance sheet and approved policy.

A KESONIA-linked MSME asset may reprice at the end of a monthly observation period while the deposit or wholesale funding that supports it reprices on another date. Fixed-rate assets, floors, caps, prepayments and undrawn revolving commitments add optionality. Stress can extend behavioural maturity at the same time that funding becomes more expensive. ALM therefore models both the scheduled contract and the customer's plausible response under each scenario.

IRRBB, or interest rate risk in the banking book, captures the effect of adverse rate movements on the bank's earnings and economic value. The Basel framework treats earnings and economic-value measures as complementary and requires assumptions about repricing, options and customer behaviour to be governed and stressed [22]. For a defined horizon, the bank can report:

\[
\Delta NII_h=NII_h^{\mathrm{shock}}-NII_h^{\mathrm{base}},
\]

\[
\Delta EVE=
\left[PV(A^{\mathrm{shock}})-PV(L^{\mathrm{shock}})\right]
-\left[PV(A^{\mathrm{base}})-PV(L^{\mathrm{base}})\right].
\]

Consider a lender funding short MSME receivables with a mixture of deposits and KESONIA-linked wholesale funding. A rapid increase in KESONIA raises the cost of the floating funding immediately. Customer assets may reset later, may be fixed, or may reach an affordability limit. At the same time, revolving borrowers may draw further and term borrowers may extend through approved modifications. The NII view measures the effect on near-term earnings; the EVE view discounts changed asset and liability cash flows over their lives. The intervention and collection models improve the behavioural assumptions without deciding the bank's IRRBB position.

For facility or cohort \(g\), a transparent matched transfer rate can be written:

\[
FTP_{g,t}=r_{\mathrm{curve}}(d_g,q_g,t)
+\lambda_{\mathrm{liq},g,t}
+\lambda_{\mathrm{option},g,t}
+\lambda_{\mathrm{basis},g,t},
\]

where \(d_g\) is behavioural duration, \(q_g\) is repricing frequency, the curve term reflects the approved funding curve, and the remaining terms attribute liquidity, option and basis effects. The bank documents whether credit spread, operating expense and capital are included elsewhere so that the same cost is not charged twice. A 14-day invoice bridge and a revolving line can share a benchmark and receive different FTP because their cash-flow and option profiles differ.

### 7.1 Construct the funding curve before attributing product performance

The approved funding curve is the central Treasury input to matched-maturity FTP. It represents the institution's internal value of funds by currency, term, repricing structure and liquidity behaviour. It is therefore richer than a copy of the overnight KESONIA observation. KESONIA anchors the relevant customer benchmark and can contribute to an internal floating-rate curve, while Treasury still has to represent the term and funding characteristics of the balance sheet that supports the loan.

A practical curve architecture begins with a governed set of observable market and internal funding points. Treasury can combine the applicable benchmark observations with the institution's marginal secured or unsecured funding evidence, term issuance, committed facilities and stable deposit behaviour. The policy states which points are admissible, how sparse maturities are interpolated, how exceptional transactions are excluded, how stale observations are handled and how the resulting curve is validated. The institution can use a marginal curve for new-business decisions, an average-cost view for complementary planning, or both with clearly separated purposes. A single reported rate should never alternate between those concepts without an identified methodology change.

The FSI evidence gives this choice an economic direction rather than a mechanical template. Matched-maturity marginal pricing makes a long or contingent use of liquidity visible when the product is originated, while a pooled average can transfer that cost to shorter or more stable business [21]. The curve should still be built from institution-specific executable or supportable funding evidence. The external study validates the control principle; local observations, governance and model performance determine the actual Kenya shilling term points and adjustments.

For analytical exposition, write the curve used for behavioural maturity \(d\), repricing frequency \(q\), currency \(c\) and valuation date \(t\) as:

\[
r_{\mathrm{curve}}(d,q,c,t)
=R_{\mathrm{ref}}(q,c,t)
+s_{\mathrm{source}}(d,c,t)
+\ell_{\mathrm{term}}(d,c,t)
+c_{\mathrm{balance\text{-}sheet}}(d,c,t),
\]

where \(R_{\mathrm{ref}}\) is the approved reference component, \(s_{\mathrm{source}}\) represents the institution's relevant funding-source spread, \(\ell_{\mathrm{term}}\) represents the value of committing liquidity for the behavioural term and \(c_{\mathrm{balance\text{-}sheet}}\) captures other approved funding effects allocated through the curve. The labels are management categories. Their exact construction follows the bank's FTP policy, accounting design and current regulatory framework.

The more detailed facility FTP equation then adds effects that belong to the asset rather than the general curve. A prepayable term loan contains an option that can shorten cash flows when rates move. An undrawn revolving commitment contains a draw option that can increase cash use during stress. A product whose customer benchmark resets monthly while its supporting funding reprices daily or at a longer interval creates basis and reset risk. Floors and caps can transfer economic value between customer and bank as the curve moves. Those effects belong in explicit \(\lambda_{\mathrm{option}}\) and \(\lambda_{\mathrm{basis}}\) terms, or in an equivalently documented implementation, so that the business unit can see why its transfer price differs from the simple benchmark.

Behavioural maturity determines the curve point only after the contractual schedule and plausible customer behaviour have been combined. For an amortising loan, Treasury begins with each expected principal and interest cash flow rather than assigning the legal final maturity to the whole balance. For a revolving line, expected draw, repayment and cancellation behaviour produce a distribution of cash use. For modified or restructured exposures, the approved schedule and re-default assumptions alter the projected profile. For recoveries, the receipt date and availability of cash matter more than the ultimate recovery percentage. Section 7.3 establishes the additional evidence required before high-frequency collection behaviour changes this maturity.

Curve construction also has a currency dimension. A Kenya shilling customer asset funded in Kenya shillings avoids a direct contractual currency mismatch, while its borrower may still carry economic foreign-exchange sensitivity through imported stock or fuel. That borrower sensitivity belongs in credit and stress analysis. If the bank or an optional funding vehicle finances Kenya shilling receivables with foreign-currency liabilities, the contractual currency mismatch enters Treasury directly. The transfer price then reflects the approved hedge, hedge tenor, rollover exposure, collateral or margin requirement, basis and residual open position. Customer credit risk and Treasury currency risk remain separate components even when the same exchange-rate shock affects both.

Restricted balances and other balance-sheet requirements affect how much gross funding is economically available for lending. For internal analysis, Treasury can express usable funding as:

\[
F_t^{\mathrm{usable}}
=F_t^{\mathrm{gross}}
-F_t^{\mathrm{restricted}}
-F_t^{\mathrm{collateral}}
-F_t^{\mathrm{operational}},
\]

where the deductions follow their actual legal, regulatory, contractual or operational treatment. The framework can include applicable reserve balances, pledged or encumbered cash, derivative margin, settlement prefunding and operational buffers. The current requirement and allocation basis are verified for the institution and date. The resulting cost enters the funding curve or a separately disclosed balance-sheet component according to FTP policy, once only. This treatment is more precise than describing restricted balances as idle or dead capital because the amounts can serve distinct monetary, prudential, settlement or risk-management purposes.

### 7.2 FTP is two-sided: assets receive charges and funding receives credits

A matched-maturity FTP system creates an internal transaction between Treasury and the business units. An asset-originating unit receives a funding charge that reflects the funds and balance-sheet capacity used by the asset. A deposit-gathering or funding unit receives a credit for the stable funding value it contributes. Treasury receives the residual interest-rate, liquidity and basis position that it is mandated to manage. This two-sided structure allows management to distinguish customer franchise value from a favourable or adverse Treasury position.

For an asset \(i\), let \(y_i\) be its customer yield on a compatible annualised basis and \(FTP_i^{A}\) its matched asset charge. The asset spread before credit, operating and capital costs is:

\[
S_i^{A}=y_i-FTP_i^{A}.
\]

For a deposit or funding relationship \(j\), let \(FTP_j^{L}\) be the internal credit assigned for its behavioural funding value and \(c_j^{\mathrm{customer}}\) the customer interest and directly attributed funding cost on the same basis. Its funding contribution is:

\[
S_j^{L}=FTP_j^{L}-c_j^{\mathrm{customer}}.
\]

The asset and liability contributions are management quantities. They support performance attribution while the bank's external income remains governed by customer contracts and financial-reporting policy. Treasury's residual reflects the consequences of the institution's aggregate funding, repricing and hedge decisions. A transfer-pricing process that charges lending units without crediting stable funding units gives an incomplete view of where balance-sheet value is created.

Non-maturity deposits require behavioural modelling because the customer can often withdraw contractually on demand while aggregate balances may display a more persistent economic life. Treasury can segment the observed balance into operationally stable and more volatile components, then estimate decay, retention, repricing sensitivity and stress outflow by product and customer population. The analysis should distinguish granular transactional balances from concentrated deposits, and should identify balances whose stability depends on promotional rates, a small number of customers, payment-platform relationships or correlated commercial activity.

Peer-reviewed evidence on the U.S. deposits channel shows why administered deposit rates and balances cannot be assumed to move one-for-one with the policy rate: banks widened deposit spreads as the policy rate increased, and deposit outflows varied with local market concentration [23]. The mechanism informs the design of beta, migration and outflow tests. A Kenyan institution estimates its own response by product, channel, customer type and rate regime, then stresses the possibility that digital competition or a loss of confidence shortens the historical deposit life.

Let \(D_{j,t}\) be the observed balance of deposit segment \(j\). A transparent analytical decomposition is:

\[
D_{j,t}=D_{j,t}^{\mathrm{core}}+D_{j,t}^{\mathrm{volatile}},
\]

where the core label represents the amount supported by the bank's approved behavioural evidence rather than a permanent guarantee of funding. The behavioural study examines survival or decay across horizons, migration between segments, rate sensitivity, concentration, seasonality and performance during institution-specific and market-wide stress. The model also estimates the deposit beta, meaning the proportion of a reference-rate movement that passes into the administered customer rate, together with the timing of that pass-through. Floors, non-linear customer response and competitive actions can make the beta vary across rate regimes.

These assumptions affect both IRRBB and liquidity. A longer modelled deposit life can support a longer FTP credit, while a higher stress outflow reduces its liquidity value. A slow repricing beta can initially support earnings when market rates rise, yet customer migration or delayed repricing can reverse that benefit. The bank therefore maintains a base behavioural profile, approved alternatives and stress assumptions rather than relying on one estimated average. The Basel IRRBB framework requires material behavioural and modelling assumptions to be governed and stressed [22]. The liquidity framework separately determines the regulatory treatment under the applicable CBK rules [18].

Deposit FTP should also preserve the distinction between economic value and operating cost. Branch, channel and relationship expenses remain in the operating-cost allocation. Deposit insurance, statutory balances, collateral requirements or other institution-specific effects enter the transfer framework only through the approved policy and applicable treatment. Treasury should be able to reconcile the gross funding credit, each adjustment and the net amount delivered to the business unit.

### 7.3 Select the FTP method according to the decision

Different management decisions can require different funding views. A marginal matched-maturity curve is generally informative for pricing a new facility because it asks what the next unit of funding and balance-sheet use is worth at the relevant maturity. An average-cost view helps explain reported portfolio performance and the historic cost of the existing funding stock. A liquidity planning view asks whether cash is available under stress. An IRRBB view asks how repricing and option behaviour change earnings and economic value. These views can share data and still produce different figures because they answer different questions.

The FTP policy should specify at least:

- the purpose of every curve and transfer rate;
- the currencies and legal entities covered;
- the products and portfolios assigned to each method;
- the benchmark and funding instruments used to build the curve;
- interpolation and extrapolation rules;
- the treatment of behavioural maturity and repricing;
- liquidity, basis and embedded-option adjustments;
- origination-date locking and subsequent reset conventions;
- the treatment of modifications, prepayments and early closures;
- deposit credits and asset charges;
- exception and override authority;
- and reconciliation to management accounts and the general ledger.

An origination-date transfer rate allows the bank to preserve the commercial performance of the original decision and to attribute later market movements to Treasury. A variable-rate asset may instead contain reset components whose transfer treatment follows the repricing structure. A modification can require a new management view while the accounting EIR continues to follow IFRS 9. These records are stored separately so that a product report does not reconstruct historical profitability using today's curve.

The Part 4 ledger should therefore pass a defined FTP event set into the Treasury environment. The minimum fields include legal entity, product, currency, origination date, contractual maturity, payment schedule, benchmark, reset dates, floor, cap, undrawn amount, prepayment rights, modification history, settlement status and approved behavioural segment. Treasury adds the curve identifier, curve date, method, behavioural maturity, adjustments, transfer rate, approval and later restatement reason. Oracle's FTP and cash-flow architecture provides one possible implementation of instrument-level matched-maturity allocation [24], while the control model remains applicable to other systems.

### 7.4 Attribute performance without moving risk between departments

The objective of FTP is disciplined attribution. The credit function remains accountable for borrower selection, limits, expected loss and concentration within its mandate. Operations remains accountable for servicing and collection cost. Product remains accountable for customer design and commercial performance. Treasury owns the funding, liquidity, interest-rate and hedge position transferred to it under policy. Capital Management owns the capital measure and allocation. Finance reconciles the combined result.

For product group \(g\), the management bridge can be expressed as:

\[
\begin{aligned}
\text{Customer yield}
&-\text{FTP charge}\\
&=\text{matched asset spread},\\
\text{matched asset spread}
&-\text{expected loss}\\
&-\text{operating and servicing cost}\\
&-\text{capital charge}\\
&=\text{risk-adjusted product contribution}.
\end{aligned}
\]

The bridge is produced by vintage, sector, product, channel and behavioural segment. It can reveal that a high headline yield is compensating for expensive funding, collection intensity or capital consumption. It can also show that a lower-yielding facility generates attractive contribution because its cash-flow timing, loss performance and operating burden are stable. These findings inform future product and funding decisions through governance rather than retrospectively redefining the customer's contractual rate.

Back-testing completes the cycle. Treasury compares the contractual and modelled cash-flow profile with actual settlement, prepayment, drawdown, modification, cure and recovery. It measures the effect of forecast error on liquidity gaps, NII, EVE and product margin. Material differences are allocated to data, model, behaviour, operations, market movement or policy. The relevant owner then corrects the source, assumption or method. This prevents favourable behavioural assumptions from remaining embedded in FTP after the portfolio has ceased to exhibit them.

### 7.5 IRRBB connects repricing gaps, behavioural options and basis risk

The NII and EVE measures introduced above become useful when their underlying repricing and behavioural channels are visible. Treasury first maps each asset, liability and material off-balance-sheet position to the date on which its economic rate can next change, while retaining contractual maturity as a separate field. A monthly KESONIA-linked asset with a floor can reprice at the next contractual reset, yet the floor can keep its effective rate unchanged. A deposit may be withdrawable on demand while its administered rate changes only after a management decision. A revolving commitment can create cash use before it creates interest income. These differences form the repricing profile.

For time bucket \(b\), a simple repricing gap is:

\[
RG_b=A_b^{\mathrm{reprice}}-L_b^{\mathrm{reprice}},
\]

where \(A_b^{\mathrm{reprice}}\) and \(L_b^{\mathrm{reprice}}\) are the rate-sensitive asset and liability amounts whose rates can change in that bucket under the approved assumptions. The gap is a diagnostic rather than a complete risk measure. It does not capture the size of the rate change, yield-curve shape, discounting, embedded options, basis relationships or future business. NII and EVE scenarios extend the analysis by repricing and valuing the full cash-flow set.

The MSME portfolio creates several material IRRBB channels:

- **Reset mismatch:** customer assets and supporting funding observe or reset against rates on different dates.
- **Basis risk:** KESONIA-linked assets can be supported by administered deposits, fixed-rate funding or another market instrument whose price moves differently.
- **Floor and cap risk:** contractual boundaries change the sensitivity of customer income as rates move.
- **Prepayment risk:** stronger borrowers may repay or refinance when rates and competition change, removing higher-yielding assets earlier than projected.
- **Extension risk:** modification, partial cure or stressed repayment can lengthen the asset profile when funding is expensive.
- **Drawdown risk:** revolving customers may use undrawn limits when liquidity weakens, increasing the balance and funding need.
- **Deposit optionality:** customers can withdraw balances or seek higher rates even where the bank's base model assigns behavioural stability.
- **Pipeline risk:** approved but undrawn offers can enter the balance sheet after the market curve has moved.

The scenario design should include changes in the level, slope and shape of the relevant rate curves, together with basis and behavioural variants that are plausible for the institution [22]. A parallel increase illustrates immediate funding pressure but cannot represent every MSME outcome. A short-end increase may affect overnight and short wholesale funding before longer customer assets reset. A flatter or inverted curve can change the economics of maturity transformation. A lower-rate scenario can activate asset floors, increase prepayment and reduce the value of deposit-rate lag. Each market scenario is paired with coherent assumptions for deposit beta, drawdown, prepayment, modification and new business.

Treasury should also report sensitivities by product, currency and legal entity. A key-rate or bucket sensitivity shows where economic value is concentrated along the curve. A basis sensitivity shows the effect of imperfect movement between the customer benchmark and the funding or hedge index. An option sensitivity shows the consequence of alternative prepayment, withdrawal and drawdown behaviour. Aggregation follows the bank's approved method and recognises diversification only where the risk relationships support it.

Hedging begins with the identified exposure. Treasury may reduce a reset gap, basis position, currency mismatch or option exposure through changes in funding mix, asset terms, balance-sheet limits or an approved financial instrument. The decision evaluates hedge cost, liquidity, collateral or margin requirements, rollover risk, counterparty credit and residual basis. Management-risk reduction and hedge-accounting qualification are separately assessed. Finance owns the accounting treatment, while Treasury owns the economic hedge and its ongoing effectiveness within the mandate.

The intervention architecture contributes to IRRBB by improving the distribution of behavioural cash flows. It can reveal that a payment-date alignment lengthens one bucket while improving ultimate repayment, or that a draw restriction reduces contingent funding use. Those effects enter Treasury after the recognition and validation process in section 6.2. The credit model supplies evidence about customer behaviour; the bank's IRRBB framework determines how that behaviour changes NII, EVE and limits.

### 7.6 ALCO governs assumptions, limits and management action

ALCO receives a joined view of liquidity, funding, IRRBB and product economics. Its role extends beyond reviewing a finished report. It approves the material methodologies and assumptions through which contractual positions become behavioural cash flows, transfer prices and stress results. The committee's mandate, delegated authorities and escalation routes determine which decisions are made by Treasury management, which require ALCO approval and which move to a board committee.

The governance cycle begins with an assumption register. Each material assumption records:

- definition and economic purpose;
- products, segments and legal entities covered;
- source data and observation window;
- estimation method and model owner;
- base, alternative and stress values;
- sensitivity and limitation;
- independent-review status;
- approval date and expiry or review date;
- performance threshold;
- and fallback value when evidence becomes unreliable.

The register covers deposit decay and beta, prepayment, drawdown, cure, modification, recovery timing, payment-rail settlement, behavioural maturity, new-business volume, wholesale-funding availability, guarantee settlement and optional SPV cash-flow assumptions. A model can supply several of those quantities, while accountable Treasury and risk functions decide whether they are fit for each intended use.

Limit design turns the analysis into operating discipline. The bank can set limits for cumulative liquidity gaps, survival horizon, funding concentration, unencumbered buffer, wholesale maturity concentration, currency mismatch, NII sensitivity, EVE sensitivity, basis exposure, behavioural-assumption reliance and model exceptions. Product and sector limits can also respond to concentration, drawdown and collection volatility. Every limit identifies its measurement frequency, warning level, breach level, authority, cure period and available actions.

ALCO actions may include changing the funding tenor, diversifying counterparties, increasing available liquidity, adjusting hedge positions, limiting a product's new originations, changing undrawn commitment policy, revising the approved behavioural assumption, altering the FTP curve or referring customer-term changes through Product and Credit governance. The action log records the evidence, decision, owner, implementation date and expected effect. Subsequent reporting compares the realised outcome with that expectation.

### 7.7 The Treasury scorecard makes forecast quality visible

A lifecycle Treasury scorecard should show the connection between customer cash, funding and balance-sheet risk. Its purpose is to make assumptions testable and to reveal whether an apparent product margin depends on unrecognised liquidity or interest-rate exposure.

The core scorecard includes:

- contractual, forecast and settled principal and interest cash by horizon;
- instruction-to-settlement and settlement-to-availability time;
- reversal, failed-payment and reconciliation-break rates;
- contractual and behavioural weighted-average life;
- prepayment, drawdown, modification, cure and re-default variance;
- cumulative liquidity gaps by currency and legal entity;
- liquidity-buffer availability and encumbrance;
- LCR and NSFR movements under the applicable calculations;
- deposit concentration, decay and repricing beta;
- wholesale-funding maturity and counterparty concentration;
- NII and EVE sensitivity by scenario;
- basis, floor, cap and option exposure;
- asset FTP charge, deposit FTP credit and Treasury residual;
- customer yield, matched spread and risk-adjusted contribution;
- guarantee-claim receivables and settlement delays;
- and forecast error, override, breach and remediation status.

Vintage reporting gives the scorecard an evidential spine. Each origination cohort retains its original product terms, curve, transfer price, risk estimate and expected cash profile. Actual settlement, prepayment, modification, default, cure and recovery are then compared with that baseline. The bank can distinguish a weak original assumption from a later market shock or operational failure. Reconstructing historical performance with the latest behavioural curve would obscure that distinction.

The scorecard also separates management and regulatory views. Internal expected cash, regulatory inflow recognition, accounting cash shortfalls and investor cash can differ because their rules and purposes differ. The report reconciles the populations and adjustments rather than forcing one number across all uses. That approach allows Treasury, Finance, Credit Risk, Capital Management and the optional SPV team to begin with the same underlying events while retaining their accountable calculations.

The operating sequence begins with reconciled account schedules from Part 4. Treasury maps contractual cash flows, applies approved prepayment, drawdown, cure, modification and recovery behaviours, generates repricing and liquidity ladders, and runs benchmark, basis and behavioural shocks. Finance and product teams receive the transfer rate and matched spread. ALCO receives aggregate NII, EVE, liquidity and concentration views. The customer price remains governed through the RBCPM and product process.

Oracle Financial Services Funds Transfer Pricing is one possible enterprise implementation. Oracle describes matched-maturity transfer pricing and instrument-level allocation of asset, funding and interest-rate spreads, while its cash-flow engine supports contractual schedules, repricing and ALM scenarios [24]. A bank may use that platform, another treasury system or a validated internal engine. The authoritative product terms and settlement events remain in their source systems, and the treasury engine reconciles its output rather than becoming a second loan ledger.

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
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 30, "rankSpacing": 46}
}}%%
flowchart TB
    A[CONTRACTUAL ASSET SCHEDULES<br/>principal, interest, fees,<br/>reset, floor, cap and maturity] --> C[BEHAVIOURAL CASH-FLOW LAYER<br/>draw, prepay, cure, modify,<br/>default, recovery and settlement]
    B[FUNDING AND LIQUIDITY SOURCES<br/>deposits, wholesale funding,<br/>capital and committed facilities] --> D[BANK ALM AND FTP<br/>cash ladder, repricing, NII, EVE,<br/>liquidity stress and matched rate]
    C --> D
    D --> E[PRODUCT ECONOMICS<br/>yield, FTP, expected loss,<br/>operating cost and capital charge]
    D --> F[ALCO AND RISK ACTION<br/>limits, funding mix, hedge,<br/>liquidity buffer and appetite]
    C --> G[OPTIONAL RING-FENCED ROUTE<br/>eligible receivables, controlled cash,<br/>waterfall and investor reporting]

    classDef input fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.8px;
    classDef engine fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.9px;
    classDef output fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.7px;
    class A,B input;
    class C,D engine;
    class E,F,G output;
```

**Figure 2: Contractual cash flows, behavioural maturity and matched funding.** The bank's ALM and FTP functions own the prudential funding view. The same reconciled asset cash flows can support an optional ring-fenced route without making that route the default architecture for every MSME portfolio.

## 8. Price the intervention as an economic decision

Part 3 treated an intervention as a governed action with a defined purpose, population, outcome and human route. Part 5 measures its economic consequence. A message that produces an immediate payment can still be poor policy if it merely moves cash by one day, increases complaints or is followed by re-default. A payment-date alignment may reduce near-term contractual receipts while improving durable cure and net recovery.

For intervention \(a\) against comparator \(0\), define causal net economic value over horizon \(h\) as:

\[
NEV_h(a,0)=
\Delta PV(C_h^{\mathrm{net}})
-\Delta Cost_h^{\mathrm{treat}}
-\Delta Cost_h^{\mathrm{fund}}
-CoC\times\Delta EC_h,
\]

where \(\Delta PV(C^{\mathrm{net}})\) is the identified change in discounted collections after direct workout cost, and the other terms measure incremental treatment, funding and allocated capital effects. Conduct, fairness, vulnerability and customer-sustainability limits are tested alongside the financial quantity. They are not converted into a price that permits harmful treatment.

The estimate requires the randomised or quasi-experimental design established in Part 3 and recorded in Part 4. Predictive model scores can target the eligible population, but observed payments after treatment do not identify the untreated counterfactual by themselves. Promotion requires durable-cure, re-default, net-recovery, cost, complaint and group-outcome evidence. The result informs servicing strategy and product design. It enters customer pricing only through the approved prospective methodology and never as an undisclosed surcharge for receiving assistance.

## 9. Risk transfer is a monitored cash-flow contract

MSME credit risk can be shared through a public or private guarantee, credit insurance, funded participation, first-loss facility or synthetic protection. Each form changes the lender's loss only through its executed terms. The model therefore represents protection as a contingent claim with an eligible population, coverage percentage, attachment, limit, exclusions, waiting period, reporting duties, claim event, settlement rule, recovery sharing, expiry and counterparty.

For scenario \(s\), define gross covered-pool loss \(L_s^{\mathrm{gross}}\), attachment \(A\), exhaustion \(E\), coverage fraction \(c\), and eligibility indicator \(I_s^{\mathrm{elig}}\). A stylised claim is:

\[
Claim_s=I_s^{\mathrm{elig}}\,c
\min\!\left\{\max\!\left(L_s^{\mathrm{gross}}-A,0\right),E-A\right\},
\]

and retained loss after settled protection is:

\[
L_s^{\mathrm{net}}=L_s^{\mathrm{gross}}-Claim_s
+P^{\mathrm{prot}}+C_s^{\mathrm{claim}}+C_s^{\mathrm{delay}},
\]

where \(P^{\mathrm{prot}}\) is protection premium or fee, \(C^{\mathrm{claim}}\) is the cost of reporting and pursuing a claim, and \(C^{\mathrm{delay}}\) measures the funding effect of settlement delay. The executed agreement may instead apply facility-level cover, pari-passu sharing, first-loss cover, deductibles or claim caps. The formula is configured to the contract rather than forcing every programme into one layer.

Kenya's Credit Guarantee Scheme provides a concrete public example. The Public Finance Management (Credit Guarantee Scheme) Regulations establish a scheme intended to encourage additional MSME lending through partial guarantees and define participating financial intermediaries, eligible credit and reporting responsibilities [25]. The National Treasury describes the current programme as risk sharing between the Scheme and participating financial institutions, with qualifying facilities originated and monitored by those institutions [26]. Scheme participation therefore complements underwriting and collection. It does not replace lender due diligence, servicing or recovery.

International principles add two tests to nominal coverage: additionality and sustainability. The World Bank and FIRST Initiative principles call for a clear mandate, sound governance and risk management, defined eligibility, partial coverage consistent with prudential treatment, transparent risk-based pricing, efficient claims management and systematic evaluation [27]. The scheme should therefore report whether it expanded viable credit or improved terms beyond the counterfactual, while also measuring claims, recoveries, concentration, operating cost and capital adequacy. A low observed claim rate is not sufficient evidence of success if the guarantee reached borrowers who would have received the same facility without it.

Cross-country peer-reviewed evidence on 76 partial credit guarantee schemes found wide variation in governance and risk-reduction tools, limited use of risk-based pricing, and a substantial government role in funding and management but less involvement in risk assessment and recovery [28]. The finding supports a deliberate allocation of responsibilities: the guarantor sets coverage, eligibility, pricing and claims discipline; the lender retains appraisal, monitoring, servicing and recovery duties defined by the programme; and the evaluation separates credit additionality, economic additionality and financial sustainability. Kenyan programme results remain an empirical question measured under the Kenyan scheme.

Economic protection, IFRS 9 recognition and regulatory-capital recognition are tested separately. IFRS 9 includes cash flows from collateral and other credit enhancements in ECL when the relevant requirements are met and the enhancement is part of the contractual terms and not recognised separately [6]. Prudential recognition follows the applicable framework. The Basel credit-risk-mitigation standard requires legal enforceability and operational conditions for eligible guarantees and identifies residual risks such as claim delay, documentation weakness, maturity mismatch and counterparty dependence [29]. The participating bank maps those conditions to the current CBK treatment before recognising capital benefit.

Monitoring continues after cover is purchased. The dashboard follows covered and uncovered EAD, premium or fee, attachment utilisation, claim frequency, acceptance and rejection, settlement lag, recoveries, subrogation, expiry, counterparty credit, sector concentration and basis between the portfolio loss definition and the covered event. Gross and net calibration are both retained. A falling net loss can reflect a strong portfolio, generous protection or delayed recognition of an uncovered deterioration, so management reads the movement with exposure and claim status.

### 9.1 Treasury distinguishes loss protection from available liquidity

Credit protection can reduce an institution's ultimate loss while leaving a near-term cash requirement. A guarantee claim may require delinquency, notice, documentation, a waiting period, verification and approval before settlement. Credit insurance can contain exclusions or contestable evidence. A funded participation transfers cash and economic exposure differently from an unfunded guarantee. A synthetic arrangement can transfer defined credit loss while leaving the underlying asset and its funding on the bank's balance sheet. Treasury therefore maps the executed form of protection into cash timing rather than inferring liquidity from the coverage percentage.

The liquidity ladder records at least four states: potential covered loss, notified claim, accepted claim receivable and settled claim cash. Only the last state enters realised available liquidity. A highly probable claim can support a scenario forecast while retaining its settlement uncertainty. The forecast records claim eligibility, expected amount, settlement distribution, currency, account destination, recovery-sharing rule and counterparty. A disputed or incomplete claim follows a separate path and receives no automatic cash credit.

For protection programme \(p\), let \(\Delta L_p\) be the scenario reduction in retained credit loss, \(P_p\) the protection premium or fee, \(C_p^{\mathrm{operation}}\) the administration and claim cost, \(C_p^{\mathrm{funding}}\) the value of funding the claim delay, and \(C_p^{\mathrm{basis}}\) and \(C_p^{\mathrm{counterparty}}\) the modelled cost of uncovered basis and counterparty deterioration. A management-value expression is:

\[
V_p^{\mathrm{protection}}
=PV(\Delta L_p)
-PV(P_p)
-PV(C_p^{\mathrm{operation}})
-PV(C_p^{\mathrm{funding}})
-PV(C_p^{\mathrm{basis}})
-PV(C_p^{\mathrm{counterparty}}).
\]

The calculation is performed across the scenario distribution. It reveals the difference between nominal coverage and economic value. A low-fee guarantee can have limited liquidity value when settlement is slow. A protection contract with fast settlement can still provide weak coverage if exclusions create significant basis. A strong counterparty can become correlated with the covered portfolio through sovereign, sector or macroeconomic stress. The institution therefore considers amount, timing, basis, concentration and counterparty capacity together.

Funded and unfunded structures also affect balance-sheet management differently. Upfront funded protection or a funded participation can provide liquidity at inception or transfer part of the asset funding, subject to the executed structure. An unfunded guarantee generally provides contingent loss reimbursement. Collateralised protection introduces collateral eligibility, valuation, margining, custody and liquidity requirements. Treasury, Credit Risk, Capital Management, Finance and Legal each record the treatment appropriate to their mandate.

### 9.2 Protection pricing and renewal use gross and net portfolio views

The protection decision begins with the gross loss distribution. Management then applies the exact contract to every scenario to calculate covered claim, retained loss, claim timing, premium and operational cost. The result is a net distribution that supports pricing, capital and liquidity analysis. Retaining the gross distribution prevents apparent improvement caused by broader protection from being mistaken for stronger underlying underwriting.

Pricing should examine:

- expected and tail claim value;
- attachment and exhaustion utilisation;
- timing of premium and claim cash;
- claim documentation and servicing cost;
- historical acceptance, rejection and dispute patterns;
- recovery and subrogation allocation;
- counterparty credit and concentration;
- currency and basis mismatch;
- collateral or margin requirements;
- maturity and renewal risk;
- and the effect on product and portfolio limits.

Renewal is a forward-looking decision. Protection that expires before the underlying asset matures leaves a residual period. A guarantee programme can change eligibility or capacity as market conditions deteriorate. Premium can rise precisely when the institution wishes to renew. Treasury includes those paths in funding and liquidity stress; Capital Management measures the effect on retained tail risk; Credit Risk evaluates the protected and unprotected portfolio; and Product assesses whether the resulting economics remain sustainable.

The reporting pack therefore reconciles gross loss, contractual claim, accepted claim, settled claim and net retained loss. It shows the portion of any capital or accounting benefit that has met the applicable recognition criteria, while separately showing economic protection and liquidity. This allows a decision maker to see, for example, that a programme provides meaningful ultimate loss protection but limited 30-day cash support.

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
    A[GROSS PORTFOLIO DISTRIBUTION<br/>default, draw, cure, recovery,<br/>cost, dependence and timing] --> B[EXPECTED LOSS AND ECL<br/>central cash loss and<br/>accounting recognition]
    A --> C[ECONOMIC-CAPITAL TAIL<br/>adverse loss, concentration,<br/>uncertainty and reverse stress]
    A --> D[PROTECTION CONTRACT<br/>eligibility, attachment, cover,<br/>exclusions and expiry]
    D --> E[CLAIM AND RECOVERY PROCESS<br/>notice, evidence, acceptance,<br/>settlement and subrogation]
    E --> F[NET RETAINED DISTRIBUTION<br/>settled claim, premium, delay,<br/>basis and counterparty risk]
    C --> G[CAPITAL AND RISK ACTION<br/>limits, allocation, renewal,<br/>protection and portfolio mix]
    F --> G

    classDef gross fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.8px;
    classDef process fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.9px;
    classDef action fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.7px;
    class A gross;
    class B,C,D,E,F process;
    class G action;
```

**Figure 3: Expected, tail and transferred loss.** Pricing, ECL and economic capital begin with the gross portfolio. Risk transfer changes the retained distribution only after coverage, claims, settlement delay, recoveries, basis and counterparty performance have been represented.

## 10. Ring-fenced receivables funding is an optional extension

A bank can apply the lifecycle architecture while retaining loans on its balance sheet. Where scale, legal feasibility and investor demand justify another funding channel, eligible receivables may support a ring-fenced securitisation or private funding vehicle. The Capital Markets Act permits cash-flow-generating assets that are legally capable of sale, transfer or assignment to enter a securitisation trust and addresses true sale under Kenyan law [30]. The Asset-Backed Securities Regulations define the originator, issuer, trustee, servicer, eligible assets, credit enhancement and investor cash-flow structure for covered offers [31]. Transaction counsel, accountants, tax advisers, the relevant regulators and investors determine the structure in practice.

The optional vehicle purchases only receivables and associated rights that the originator owns and can transfer. An eligibility schedule tests documentation, balance, arrears, currency, sector, geography, prior encumbrance, data quality, concentration and enforceability. The servicer collects through controlled accounts. A waterfall pays permitted expenses, senior interest and principal, subordinate obligations, reserve cures and residual amounts in the contractual order. Overcollateralisation, cash reserves, subordination and early-amortisation triggers are modelled as finite protections.

Ring-fencing changes legal rights and cash priorities, but its economic analysis must still include the sponsor and servicer. Gorton and Souleles show, in credit-card securitisation evidence, that investors can price sponsor risk and implicit support alongside the formal SPV structure [32]. The Kenyan transaction remains governed by its own law and documents. The research strengthens the scenario design: model originator distress, servicer interruption, commingling, asset-representation breach, replacement cost and voluntary support separately from the legal true-sale conclusion, making operational dependence visible while preserving the vehicle's legal distinction.

### 10.1 The vehicle has its own cash architecture

The ring-fenced vehicle converts eligible receivable cash flows into a contractually ordered funding structure. Its Treasury task begins with the legal entity and transaction documents. The vehicle receives only the assets and associated rights validly transferred to it, funds purchases through the agreed notes, equity or facilities, holds cash in controlled accounts and applies available funds through the priority of payments. The originator's bank-level ALM and FTP continue separately.

A practical account structure can include:

- a receivable purchase or funding account;
- a collection account receiving borrower and recovery cash;
- a principal account and an interest or revenue ledger where the documents distinguish them;
- a cash reserve or liquidity reserve account;
- permitted expense and tax accounts;
- a hedge or collateral account where applicable;
- and a distribution account for amounts released after the required tests.

The legal documents determine ownership, control, permitted withdrawals, account-bank standards and replacement triggers. The model mirrors those terms. It avoids treating an operational subledger as a bank account or using cash that is trapped, restricted or allocated to another priority.

Collections enter the vehicle through a defined servicing route. Where the servicer temporarily receives cash before remitting it to the controlled account, the structure measures commingling exposure, remittance frequency and replacement or sweep mechanics. A backup-servicing plan identifies the data, authority, payment instructions, customer communication and operational capacity needed to continue collection if the primary servicer fails. Servicing continuity is a liquidity protection because an otherwise performing receivable produces no usable cash when the collection mechanism is interrupted.

### 10.2 The borrowing base governs how much funding the assets support

The eligible receivable balance and the amount lenders are willing to advance are related but distinct. Let \(ER_{j,t}\) be the eligible balance of asset group \(j\), \(a_j\) its contractual advance rate, \(R_t\) required reserves or retained amounts, and \(DD_t\) other documented borrowing-base deductions. A stylised borrowing-base capacity is:

\[
BBC_t=\sum_j a_j ER_{j,t}-R_t-DD_t.
\]

Outstanding funded debt is tested against that capacity under the executed facility. The borrowing base can recognise different advance rates for product, seasoning, delinquency, concentration or other eligible classifications. Ineligible assets remain visible in the portfolio but contribute no borrowing-base value. A breach can require a cure, additional eligible assets, repayment, cash trapping or another contractual action.

Overcollateralisation provides a complementary view. For eligible receivables \(ER_t\) and the notes or debt included in the transaction definition \(N_t\):

\[
OC_t=\frac{ER_t}{N_t}.
\]

The denominator must follow the transaction documents. A test based on senior notes answers a different question from one based on senior plus subordinate debt or total capitalisation. The report displays the contractual threshold, actual ratio, headroom and cure requirement. Advance rate and overcollateralisation remain separate controls even where their numerical effects appear similar.

Eligibility is recalculated from point-in-time asset data. The calculation records receivable ownership, balance, product, currency, seasoning, arrears, modification, platform or channel, geography, obligor concentration, documentation, policy or guarantee status where relevant, and any prior encumbrance. Reversals and corrections produce a versioned borrowing-base result. The trustee or calculation agent can reproduce the result from the agreed data tape and rules.

### 10.3 SPV ALM matches receivable cash to note and reserve obligations

The vehicle's asset-liability management is narrower than the originating bank's prudential ALM but still economically important. It maps monthly and, where necessary, daily asset collections against note interest, note principal, fees, taxes, reserve requirements, hedge payments and other waterfall obligations. It monitors timing, basis, currency, optionality and concentration within the transaction boundary.

For bucket \(b\), the vehicle's projected cumulative cash position can be written:

\[
LG_b^{\mathrm{SPV}}
=C_0^{\mathrm{SPV}}
+\sum_{m\le b}\left(
CF_m^{\mathrm{asset}}
+F_m^{\mathrm{committed}}
-DS_m^{\mathrm{notes}}
-E_m^{\mathrm{senior}}
-H_m^{\mathrm{hedge}}
-R_m^{\mathrm{required}}
\right),
\]

where asset cash includes settled principal, interest, recoveries and eligible credit-enhancement proceeds; committed funding is recognised according to its availability conditions; note debt service follows the transaction documents; senior expenses follow their priority; hedge cash follows the executed agreement; and reserve requirements reflect the current test. The ladder is run under base and stressed asset scenarios.

The cash profile can contain several mismatches. Receivables may collect daily while notes pay monthly or quarterly. Assets may amortise while notes remain outstanding until a payment date. Customer assets and notes can observe compounded KESONIA over different windows or include different floors, lags and day-count conventions. Recoveries and guarantee claims can arrive after note obligations. A revolving purchase period can consume cash for new receivables while debt service continues. The model identifies each mismatch and the contractual mechanism that absorbs it.

### 10.4 Note pricing and the waterfall remain distinct from bank FTP

For floating-rate note class \(k\), a simplified coupon can be expressed as:

\[
r_{k,t}^{\mathrm{note}}
=R_{a_k,b_k,t}^{\mathrm{KESONIA}}
+m_{k,t},
\]

where the note's observation period, payment date, day count, fallback, floor and margin follow its own documents. The asset contract can use another observation window even where both sides reference KESONIA. The resulting basis and timing difference belong in the SPV cash model.

The note margin is an investor funding term. It is separate from the originating bank's internal FTP rate, the customer premium, expected loss, excess spread and investor hurdle. The vehicle can maintain a matched-funding attribution showing how asset yield covers note cost, expenses, expected loss, reserve drag and residual return. Calling that analysis SPV matched-funding attribution preserves the distinction from a bank-wide FTP system that prices business units and deposits.

On each payment date, the waterfall applies available funds in the contractual order. A representative sequence can include taxes and statutory amounts, trustee and account-bank costs, servicing fees, hedge payments, senior interest, senior principal, subordinate interest and principal, reserve replenishment and residual distribution. The actual order, caps, deferrals and pro rata or sequential rules come from the executed transaction. The calculation engine records cash entering each step, amount paid, shortfall, carried amount and ending balance.

### 10.5 Reserves, prefunding and permitted investments create real economics

A cash reserve provides time for asset collections to meet senior obligations during disruption. Its target can be a fixed amount, a percentage of notes, a defined number of months of senior expenses and debt service, or a formula that changes with the portfolio. The model reproduces the contractual definition and tests opening balance, required amount, deposits, releases, permitted investment income, draws, shortfall and cure.

Prefunding can reduce execution risk by providing cash before receivables are purchased, while unused cash creates negative carry when its permitted investment return is below the note cost and transaction expenses. A revolving structure adds reinvestment risk because available principal may purchase new assets whose yield, term or credit quality differs from the original pool. Eligibility, concentration and minimum-yield tests can govern purchases. The model measures the value of liquidity protection beside its cost.

Permitted investments are treated as assets with their own maturity, credit quality, liquidity and counterparty exposure. Reserve or collection cash is not assumed to earn the customer asset yield. Account-bank concentration, set-off, replacement conditions and access during operational disruption form part of the cash-risk analysis.

### 10.6 Triggers convert deterioration into contractual cash action

Performance triggers can include delinquency or default ratios, cumulative net loss, collection performance, excess spread, reserve shortfall, borrowing-base deficiency, overcollateralisation, concentration, servicer failure, account-bank downgrade or other documented events. A trigger is calculated from defined data, numerator, denominator, observation date and cure rule. It then activates the exact contractual response.

Early amortisation commonly changes the vehicle from purchasing or revolving into paying down debt. Cash that might otherwise acquire new receivables or reach the residual position is redirected through the protective waterfall. A senior sequential-pay rule can accelerate Class A principal. Reserve releases can become restricted. Equity or residual distributions can stop. The model shows both the trigger date and the resulting change in every later cash flow.

Trigger design requires balance. A late trigger can permit asset deterioration to consume structural protection. An excessively volatile trigger can force unnecessary amortisation after a temporary data or settlement event. The documents can include averaging, persistence, cure periods and data-quality fallbacks where appropriate. The calculation remains transparent so that investors can distinguish economic deterioration from an operational reporting break.

### 10.7 Currency, hedging and liquidity facilities follow executed capacity

A vehicle that acquires Kenya shilling receivables and issues Kenya shilling notes has limited direct contractual currency mismatch, although borrower cash can remain sensitive to exchange-rate shocks. If liabilities, expenses or investor commitments are denominated in another currency, the vehicle models principal, interest, collateral, margin and rollover cash under exchange-rate scenarios. A hedge can reduce the mismatch while introducing counterparty, basis, collateral and termination exposure.

A liquidity facility can bridge timing disruption under specified drawing conditions. It is not a substitute for absorbing credit loss unless the agreement expressly provides that protection. The model records commitment fee, available amount, draw conditions, interest, maturity, repayment priority, provider credit and termination events. An uncommitted facility enters stress as a contingent possibility rather than assured funding.

### 10.8 The SPV reporting pack reconciles assets, cash and investor claims

The monthly or payment-date pack should include:

- opening, purchased, collected, defaulted, recovered and closing receivables;
- eligible and ineligible asset balances with reason codes;
- borrowing-base capacity, debt and headroom;
- advance rates and overcollateralisation;
- principal, interest, recovery and expense collections;
- collection-account, reserve-account and distribution-account movements;
- asset yield, note coupon, basis and excess spread;
- note opening balance, interest, principal and closing balance by class;
- waterfall allocation and unpaid amounts;
- reserve target, balance, draw and cure;
- covenant, trigger and early-amortisation status;
- servicing remittance, reconciliation and backup-servicer readiness;
- guarantee or protection claim status;
- hedge, currency and counterparty exposure where applicable;
- and one-year and ultimate loss, principal shortfall and payment timing by scenario.

Each total reconciles to the asset tape, controlled bank accounts, note register and transaction ledger. The pack distinguishes expected, due, received, available and distributed cash. Investors, trustee, servicer, originator and calculation agent can therefore examine the same economic events through their contractual roles.

The vehicle's analysis starts with the same monthly cash-flow distribution but retains separate funding quantities. Asset yield is the return collected on purchased receivables. A note margin \(m_{\mathrm{fund}}\) is an investor funding term. Bank FTP is the originating institution's internal funding attribution. The investor hurdle is a required return or valuation input. Excess spread is the cash remaining after realised asset collections, losses, expenses and note costs under the waterfall. These quantities are reconciled without renaming one another.

For tranche \(k\), attachment \(A_k\) and exhaustion \(E_k\), scenario loss can be represented as:

\[
TL_{k,s}=\min\!\left\{\max\!\left(L_s-A_k,0\right),E_k-A_k\right\}.
\]

The lender pack reports one-year and ultimate loss, payment timing, reserve use, covenant breaches and principal shortfall by scenario. Legal transfer, investor protection and capital relief remain consequences of the executed transaction and applicable approvals. The model supplies reproducible evidence for those decisions.

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
  "flowchart": {"curve": "stepAfter", "nodeSpacing": 28, "rankSpacing": 42}
}}%%
flowchart TB
    A[ELIGIBLE RECEIVABLES<br/>contract, balance, performance,<br/>ownership and concentration] --> B[PURCHASE AND BORROWING BASE<br/>advance rate, deductions,<br/>cash contribution and headroom]
    B --> C[CONTROLLED CASH ARCHITECTURE<br/>collection, principal, reserve,<br/>expense, hedge and distribution accounts]
    C --> D[PRIORITY OF PAYMENTS<br/>senior expenses, hedge, servicing,<br/>note interest, principal and reserve cure]
    D --> E[CLASS A AND OTHER NOTES<br/>benchmark, margin, payment date,<br/>principal balance and shortfall]
    D --> F[RESERVE AND LIQUIDITY SUPPORT<br/>target, draw, replenishment,<br/>facility use and permitted investment]
    D --> G[RESIDUAL DISTRIBUTION<br/>available only after contractual<br/>tests and restricted-payment conditions]
    H[ASSET PERFORMANCE<br/>collection, default, cure,<br/>recovery, prepayment and modification] --> C
    H --> I[TRIGGERS AND COVENANTS<br/>borrowing base, OC, reserve,<br/>loss, concentration and servicing]
    I --> D
    I --> J[PROTECTIVE ACTION<br/>cash trap, purchase stop,<br/>sequential pay or early amortisation]
    J --> D
    K[TRUSTEE, SERVICER, ACCOUNT BANK,<br/>CALCULATION AGENT AND HEDGE PROVIDER] --> C
    K --> I

    classDef asset fill:#EAF2F8,stroke:#2E5E7E,color:#17324D,stroke-width:1.8px;
    classDef cash fill:#E8F5F2,stroke:#16857B,color:#17324D,stroke-width:1.9px;
    classDef action fill:#FFF4D6,stroke:#C58A00,color:#5A4100,stroke-width:1.7px;
    class A,H asset;
    class B,C,D,E,F,G,K cash;
    class I,J action;
```

**Figure 4: Ring-fenced receivables cash, note and control architecture.** Eligible assets support a governed borrowing base, while settled collections move through controlled accounts and the priority of payments. Reserves, covenants, service continuity and protective triggers determine when cash reaches noteholders or the residual position.

## 11. One control plane, several accountable owners

Part 5 completes the journey from a quoted benchmark to realised and transferred loss. Credit owns risk appetite and customer selection. Product and legal own terms. Finance owns ECL and journals. Capital owns internal and regulatory assessment. Treasury owns ALM, liquidity and FTP. Collections owns executed recovery strategy. The protection owner manages guarantees and claims. An optional vehicle's trustee, servicer and calculation agent own its contractual cash waterfall.

The joined evidence plane lets those owners reconcile without collapsing their mandates. A customer payment has one economic amount and timestamp, while pricing, ECL, capital and liquidity interpret it for different decisions. Part 6 will test whether the proposed lifecycle system improves durable collection, net recovery, customer outcomes and risk-adjusted economics under a bank-controlled experimental programme.

### 11.1 Each function owns a defined financial interpretation

The control plane begins with common event identity rather than one universal financial number. An account, contract, payment, modification, default, recovery or guarantee claim has an authoritative event history. Each accountable function applies the horizon, probability measure, recognition rule and policy required for its decision.

| Function | Principal Part 5 decision | Inputs received from the lifecycle | Controlled output |
|---|---|---|---|
| Product and Pricing | Which terms create a sustainable customer and portfolio proposition? | Benchmark, customer cash cycle, expected loss, FTP, operating cost and capital charge | Approved price, limit, tenor, repayment design and disclosure |
| Credit Risk | What loss and transition distribution is supported by the evidence? | PD, EAD, LGD, cure, recovery, concentration and uncertainty | Risk estimates, limits, stress results and portfolio action |
| Collections and Workout | Which authorised action improves durable cash and customer outcomes? | State, affordability, treatment eligibility, causal evidence and account history | Treatment, restructuring, recovery plan and outcome record |
| Finance | What amount is recognised and reported? | Contractual cash, original EIR, stage, scenarios, shortfall, modification and write-off | ECL, income, modification result, journals and disclosures |
| Capital Management | How much adverse loss should the institution withstand or allocate? | Gross and net loss distributions, dependence, concentration and mitigants | Regulatory assessment, economic capital, allocation and risk-adjusted return |
| Treasury and ALCO | When is cash available and how is funding, rate and liquidity risk managed? | Contractual and behavioural cash, deposits, funding, options, settlement and stress | Curves, FTP, liquidity position, NII, EVE, limits, hedge and funding action |
| Protection Management | What contractual loss transfer is available and performing? | Covered exposure, eligibility, attachment, claim, settlement and counterparty | Protection value, claim action, renewal decision and net retained loss |
| Structured Finance Parties | What cash belongs to the vehicle and how is it distributed? | Eligible assets, controlled accounts, borrowing base, notes, reserves and triggers | Waterfall, covenant result, investor report and protective action |
| Model Risk and Validation | Is a model or behavioural assumption fit for its intended financial use? | Development evidence, validation, stability, limitations and change request | Approval, restriction, monitoring threshold or remediation |
| Data and Technology | Can every result be reproduced from governed events and versions? | Source events, mappings, corrections, model artefacts and access controls | Reconciled data products, lineage, availability and operational evidence |
| Legal and Compliance | Are the terms, transfer, processing and actions authorised and enforceable? | Contract, regulation, policy, consent or lawful basis, and proposed action | Legal interpretation, control requirement, approval condition and exception |

The matrix prevents a model improvement from silently changing every downstream process. A new cure model can improve credit monitoring while Finance retains the approved ECL method, Treasury retains the approved behavioural maturity and Product retains the contractual pricing process. Each function can adopt the model after completing its intended-use assessment.

### 11.2 The monthly financial cycle reconciles before it explains

The reporting cycle starts by freezing the governed event population for the period, including late events, corrections and reversals according to the close policy. Operations and Finance reconcile due, paid, allocated, modified, defaulted, written-off and recovered amounts to controlled accounts, the product subledger and the general ledger. Differences remain visible with owners and resolution status.

Credit Risk then produces the approved risk and cash-flow distributions, including scenarios, concentration and model uncertainty. Finance calculates ECL and other accounting consequences under its policy. Capital Management updates internal and regulatory views. Treasury produces liquidity, funding, FTP, NII, EVE and hedge reporting. Protection Management reconciles covered exposure, claims and settled proceeds. Where a ring-fenced vehicle exists, its calculation agent applies the asset eligibility, borrowing base, accounts, waterfall and covenant rules.

The joined management bridge then explains movement from the prior period. It separates new originations, contractual amortisation, benchmark movement, premium and fee changes, model changes, stage migration, drawdown, modification, prepayment, cure, default, recovery, settlement delay, funding-curve movement, protection and capital allocation. Management can therefore see whether a change in risk-adjusted contribution came from customer performance, market rates, funding, accounting recognition, operational cost, model revision or structural protection.

### 11.3 Model and assumption changes have intended-use approval

Every material model or behavioural assumption has an inventory entry that identifies its purpose. The HLR and timing challengers may support underwriting, ECL inputs, collection targeting, liquidity forecasting, economic capital or SPV scenarios, but approval for one use does not automatically establish approval for another. Each use has its own materiality, validation evidence, fallback and accountable owner.

The intended-use discipline is also reflected in current comparative supervisory practice. The 2026 U.S. interagency Revised Guidance on Model Risk Management begins model development with a clear purpose, aligns validation rigor with model use and materiality, and requires users to understand limitations when a model is extended to another application [33]. Used as an external benchmark alongside the applicable Kenyan framework, it reinforces the Part 5 control: a model validated for underwriting enters ECL, capital, Treasury or vehicle reporting after the receiving function has assessed that specific use, data, performance range and fallback.

A material change package should contain:

- the economic question and intended use;
- the affected products, portfolios, legal entities and customers;
- source-data and point-in-time controls;
- development sample and observation horizon;
- comparative performance against the current method;
- calibration, discrimination and cash-flow forecast accuracy;
- sensitivity, stress and stability analysis;
- fairness, conduct and customer-outcome assessment where relevant;
- impact on ECL, capital, liquidity, FTP, pricing and SPV cash where applicable;
- operational readiness, parallel-run evidence and reconciliation;
- limitations, use restrictions and human-review requirements;
- rollback criteria and fallback method;
- independent-validation findings;
- and approvals from each affected function.

For Treasury use, the package includes settlement accuracy, forecast cash error, weighted-average-life error, prepayment and drawdown stability, liquidity-gap impact, NII and EVE sensitivity, funding-curve interaction and performance under operational and market stress. For Finance use, it includes stage, cash-shortfall and allowance consequences. For Capital use, it includes tail, dependence and concentration effects. For a vehicle, it includes borrowing-base, reserve, waterfall, trigger and note-payment effects.

### 11.4 The integrated scorecard preserves reconciliation across uses

The final Part 5 scorecard brings the departmental views together without ranking one as the master of the others. It reports customer price and total cost, expected and realised cash, ECL and stage movement, economic and regulatory capital, liquidity and funding, IRRBB, FTP and margin, treatment economics, protection, and optional vehicle performance. Every metric declares population, date, horizon, currency, numerator, denominator, scenario and version.

The scorecard includes reconciliations between:

- customer benchmark and charged rate;
- customer rate and internal FTP;
- expected contractual cash and settled available cash;
- physical expected loss and IFRS 9 ECL;
- expected loss and economic-capital tail;
- gross loss, covered claim and net retained loss;
- bank-held assets and assets sold or assigned to a vehicle;
- vehicle asset cash, waterfall cash and note balances;
- and expected intervention benefit and realised durable outcome.

Exceptions are part of the report. A missing settlement, failed reconciliation, model override, expired assumption, limit breach, disputed claim or unavailable funding source carries an owner, age, financial effect and remediation date. This gives executives a view of the architecture's reliability alongside its reported economics.

Part 6 then tests the mechanisms that can be learned prospectively: price response, repayment design, treatment uplift, durable cure, re-default, collection timing, customer outcomes and forecast accuracy. Part 5 retains ownership of how validated evidence enters pricing, accounting, capital, Treasury and funding after the relevant function has approved it.

## References

[1] Central Bank of Kenya, “KESONIA Interest Rate Benchmark,” Nairobi, Kenya, 2026. [Online]. Available: https://www.centralbank.go.ke/kesonia/. [Accessed: Sep. 6, 2026].

[2] Central Bank of Kenya, *Revised Risk-Based Credit Pricing Model*, Nairobi, Kenya, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf. [Accessed: Sep. 6, 2026].

[3] Central Bank of Kenya, *36th Monetary Policy Committee Report*, Nairobi, Kenya, Apr. 2026, p. 20. [Online]. Available: https://www.centralbank.go.ke/uploads/monetary_policy_reports/131378250_36th%20Monetary%20Policy%20Committee%20Report%2C%20April%202026.pdf. [Accessed: Sep. 6, 2026].

[4] D. S. Karlan and J. Zinman, “Credit elasticities in less-developed economies: Implications for microfinance,” *American Economic Review*, vol. 98, no. 3, pp. 1040–1068, Jun. 2008, doi: 10.1257/aer.98.3.1040.

[5] L. Gambacorta, Y. Huang, H. Qiu, and J. Wang, “How do machine learning and non-traditional data affect credit scoring? New evidence from a Chinese fintech firm,” *Journal of Financial Stability*, vol. 73, Art. no. 101284, Aug. 2024, doi: 10.1016/j.jfs.2024.101284.

[6] IFRS Foundation, *IFRS 9 Financial Instruments*, London, U.K., 2024. [Online]. Available: https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2024/issued/part-a/ifrs-9-financial-instruments.pdf?bypass=on. [Accessed: Sep. 6, 2026].

[7] European Systemic Risk Board, *Financial Stability Implications of IFRS 9*, Frankfurt am Main, Germany, Jul. 2017. [Online]. Available: https://www.esrb.europa.eu/pub/pdf/reports/20170717_fin_stab_imp_IFRS_9.en.pdf. [Accessed: Sep. 6, 2026].

[8] Basel Committee on Banking Supervision, “Expected credit losses,” in *Basel Committee Consolidated Guidelines*, Bank for International Settlements, Basel, Switzerland, 2026. [Online]. Available: https://www.bis.org/committees/bcbs/basel-consolidated-guidelines/module/pap/20. [Accessed: Sep. 6, 2026].

[9] Central Bank of Kenya, *Prudential Guidelines for Institutions Licensed under the Banking Act*, CBK/PG/03 and CBK/PG/04, Nairobi, Kenya, Jan. 2013. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2016/08/PRUDENTIAL-GUIDELINES.pdf. [Accessed: Sep. 6, 2026].

[10] M. B. Gordy, “A risk-factor model foundation for ratings-based bank capital rules,” *Journal of Financial Intermediation*, vol. 12, no. 3, pp. 199–232, Jul. 2003, doi: 10.1016/S1042-9573(03)00040-8.

[11] D. Tasche, “Capital allocation for credit portfolios with kernel estimators,” *Quantitative Finance*, vol. 9, no. 5, pp. 581–595, 2009, doi: 10.1080/14697680802620599.

[12] Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk*, Bank for International Settlements, Basel, Switzerland, Apr. 2025. [Online]. Available: https://www.bis.org/publications/202504-guidelines-principles-management-credit-risk. [Accessed: Sep. 6, 2026].

[13] Basel Committee on Banking Supervision, “The Core Principles and assessment criteria,” Principle 19, *Basel Framework*, Apr. 2024. [Online]. Available: https://www.bis.org/committees/bcbs/basel-framework/standard/bcp/40/inforce/2024-04-25/published/2024-04-25. [Accessed: Sep. 6, 2026].

[14] Republic of Kenya, *National Payment System Act*, No. 39 of 2011, sec. 9. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/2011/39/eng%402017-07-03. [Accessed: Sep. 6, 2026].

[15] Republic of Kenya, *The National Payment System Regulations*, Legal Notice No. 109 of 2014, rev. Dec. 31, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2014/109/eng%402022-12-31. [Accessed: Sep. 6, 2026].

[16] Central Bank of Kenya, *The Kenya Electronic Payment and Settlement System Report: December 2024*, Nairobi, Kenya, Dec. 2024. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/01/The-Kenya-Electronic-Payment-and-Settlement-System-Report-December-2024.pdf. [Accessed: Sep. 6, 2026].

[17] Basel Committee on Banking Supervision, “Liquidity risk management and supervision,” *Basel Committee Consolidated Guidelines*, Jan. 2026. [Online]. Available: https://www.bis.org/committees/bcbs/basel-consolidated-guidelines/module/lqy/10. [Accessed: Sep. 6, 2026].

[18] Central Bank of Kenya, *Guidelines on the Liquidity Coverage Ratio, Net Stable Funding Ratio and Leverage Ratio*, Nairobi, Kenya, Apr. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/04/GUIDELINES-ON-BASEL-III-LIQUIDITY-STANDARDS-AND-LEVERAGE-RATIO.pdf. [Accessed: Sep. 6, 2026].

[19] L. Bursztyn, S. Fiorin, D. Gottlieb, and M. Kanz, “Moral incentives in credit card debt repayment: Evidence from a field experiment,” *Journal of Political Economy*, vol. 127, no. 4, pp. 1641–1683, Aug. 2019, doi: 10.1086/701605.

[20] E. Field, R. Pande, J. Papp, and N. Rigol, “Does the classic microfinance model discourage entrepreneurship among the poor? Experimental evidence from India,” *American Economic Review*, vol. 103, no. 6, pp. 2196–2226, Oct. 2013, doi: 10.1257/aer.103.6.2196.

[21] J. Grant, *Liquidity Transfer Pricing: A Guide to Better Practice*, FSI Occasional Paper No. 10, Financial Stability Institute, Bank for International Settlements, Basel, Switzerland, Dec. 2011. [Online]. Available: https://www.bis.org/fsi/fsipapers10.pdf. [Accessed: Sep. 6, 2026].

[22] Basel Committee on Banking Supervision, “Interest rate risk in the banking book,” SRP31, *Basel Framework*, effective Jan. 1, 2026. [Online]. Available: https://www.bis.org/committees/bcbs/basel-framework/standard/srp/31/inforce/2026-01-01/published/2024-07-16. [Accessed: Sep. 6, 2026].

[23] I. Drechsler, A. Savov, and P. Schnabl, “The deposits channel of monetary policy,” *Quarterly Journal of Economics*, vol. 132, no. 4, pp. 1819–1876, Nov. 2017, doi: 10.1093/qje/qjx019.

[24] Oracle, *Oracle Financial Services Funds Transfer Pricing User Guide*, Release 8.1.2.5.0, Sep. 2025. [Online]. Available: https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/funds-transfer-pricing/81250/ftpug/funds-transfer-pricing-user-guide.pdf. [Accessed: Sep. 6, 2026].

[25] Republic of Kenya, *The Public Finance Management (Credit Guarantee Scheme) Regulations, 2020*, Legal Notice No. 197 of 2020. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2020/197/eng%402022-12-31. [Accessed: Sep. 6, 2026].

[26] National Treasury and Economic Planning, “Credit Guarantee Scheme,” Nairobi, Kenya, 2026. [Online]. Available: https://cgs.treasury.go.ke/. [Accessed: Sep. 6, 2026].

[27] World Bank Group and FIRST Initiative, *Principles for Public Credit Guarantee Schemes for SMEs*, Washington, DC, USA, 2015. [Online]. Available: https://www.worldbank.org/en/topic/financialsector/publication/principles-for-public-credit-guarantee-schemes-cgss-for-smes. [Accessed: Sep. 6, 2026].

[28] T. Beck, L. F. Klapper, and J. C. Mendoza, “The typology of partial credit guarantee funds around the world,” *Journal of Financial Stability*, vol. 6, no. 1, pp. 10–25, Apr. 2010, doi: 10.1016/j.jfs.2008.12.003.

[29] Basel Committee on Banking Supervision, “Standardised approach: credit risk mitigation,” CRE22, *Basel Framework*, Nov. 2020. [Online]. Available: https://www.bis.org/basel_framework/chapter/CRE/22.htm. [Accessed: Sep. 6, 2026].

[30] Republic of Kenya, *Capital Markets Act*, Cap. 485A, secs. 30I–30L. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/1989/17/eng%402023-12-11. [Accessed: Sep. 6, 2026].

[31] Republic of Kenya, *The Capital Markets (Asset-Backed Securities) Regulations*, Legal Notice No. 184 of 2007, rev. Dec. 31, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2007/184/eng%402022-12-31. [Accessed: Sep. 6, 2026].

[32] G. B. Gorton and N. S. Souleles, “Special purpose vehicles and securitization,” in *The Risks of Financial Institutions*, M. Carey and R. M. Stulz, Eds. Chicago, IL, USA: University of Chicago Press, 2007, pp. 549–602, doi: 10.7208/chicago/9780226092980.003.0013.

[33] Board of Governors of the Federal Reserve System, Federal Deposit Insurance Corporation, and Office of the Comptroller of the Currency, *Revised Guidance on Model Risk Management*, SR 26-2, Washington, DC, USA, Apr. 17, 2026. [Online]. Available: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm. [Accessed: Sep. 6, 2026].
