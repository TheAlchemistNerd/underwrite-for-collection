---
title: "Underwrite for Collection"
subtitle: "Part 5: KESONIA Pricing, Expected Credit Loss, Capital and Funding"
author: "Neville Maloba"
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

For an accrual period from (a) to (b), let (r_i) be a published KESONIA observation expressed as a decimal, let (n_i) be the calendar days for which that observation applies under the contract, and let (d=\sum_i n_i). A transparent compounded factor and annualised rate are:

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

The borrower-risk component can use expected loss, transition risk, recovery cost and concentration evidence. Its units must remain consistent. A one-year PD cannot be multiplied by a lifetime LGD and a point-in-time balance and then compared directly with an annual interest margin. For a facility \(i\), product horizon \(h\) and physical probability measure \(\mathbb P\), a simple expected-loss rate is:

\[
EL_i(h)
=\frac{
\mathbb E_{\mathbb P}\!\left[L_i(h)\mid\mathcal I_{i,t}\right]
}{E_i(h)},
\]

where \(L_i(h)\) is the defined cash loss over the horizon, \(\mathcal I_{i,t}\) is the evidence available at pricing time and \(E_i(h)\) is a compatible exposure or average-balance denominator. A richer calculation follows monthly default, cure, drawdown, recovery and expense cash flows. Either approach produces a pricing input after calibration and governance. It does not determine the whole \(K_{\mathrm{RBCP}}\).

Lifecycle underwriting improves that input by distinguishing customers whose origination profile looks similar but whose later cash conversion and repayment evidence diverge. The explicit features, residual AI representation and hierarchical effects described in Part 2b can update the distribution of future cash loss. Part 3 then chooses from authorised actions. A rising posterior risk estimate may prompt a review, an affordable payment-date alignment, a limit change or a collections intervention. The existing facility's customer premium changes only when the contract and approved policy permit repricing or when new terms are lawfully agreed.

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

IFRS 9 measures expected credit losses as probability-weighted credit losses that incorporate the time value of money and reasonable and supportable information available without undue cost or effort about past events, current conditions and forecasts of future economic conditions. The framework is principles-based and permits methods that satisfy those requirements [4]. The lifecycle architecture contributes event history, calibrated transitions and cash-flow timing. The reporting entity's accounting policy determines how those inputs become an allowance.

Let \(CS_{i,m}^{(s)}\) be the cash shortfall in month \(m\) under forward-looking scenario \(s\), measured as the contractual cash due to the reporting entity less the cash it expects to receive, including cash flows from eligible collateral and contractual credit enhancements where the accounting requirements include them. With scenario weight \(\pi_s\), original effective interest rate \(EIR_i\) and time fraction \(\tau_m\), a cash-shortfall expression is:

\[
ECL_i
=\sum_{s=1}^{S}\pi_s
\sum_{m\in\mathcal H_i}
\frac{CS_{i,m}^{(s)}}{(1+EIR_i)^{\tau_m}},
\qquad
\sum_{s=1}^{S}\pi_s=1.
\]

The horizon \(\mathcal H_i\) depends on the applicable impairment stage and instrument requirements. Twelve-month ECL is the portion of lifetime cash shortfalls associated with defaults possible within the next twelve months. It is not limited to cash that happens to be missed during the next twelve months. Lifetime ECL reflects default risk across the expected life. The distinction is important for short MSME facilities, revolving lines and facilities whose behavioural use extends beyond one contractual billing interval [4].

The model-to-ECL bridge therefore contains more than a PD field. For each reporting date it stores the instrument population, stage, default definition, scenario-conditioned marginal or conditional PD term structure, EAD path, LGD or expected cash-shortfall path, prepayment, cure, recovery timing, directly attributable recovery assumptions, contractual credit enhancements, original EIR, currency, source versions and overlay. The bank reconciles opening allowance, new originations, repayments, transfers between stages, changes in risk, modifications, write-offs, recoveries and closing allowance.

Significant increase in credit risk, or SICR, is an accounting assessment of the change in lifetime default risk since initial recognition. A lifecycle score may provide relevant evidence through payment status, cash-flow deterioration, utilisation, adverse restructuring, sector stress or a material increase in calibrated lifetime risk. The approved policy combines those signals with qualitative indicators, backstops and reasonable forward-looking information. It also distinguishes a temporary data outage from economic deterioration.

Operational cure and accounting improvement are related but separately governed. A customer can clear an arrear and become operationally current today. The bank may require a sustained performance period, supporting evidence and reconsideration of forward-looking risk before concluding that credit risk has improved enough for an accounting stage transfer. The durable-cure definition from Part 1 provides evidence for that assessment without becoming a universal accounting rule. The same separation applies to re-default: a renewed delinquency after cure updates the observed transition history and tests whether the cure policy was economically durable.

Modification is another cash-flow event rather than a label for failure. An affordable term extension may improve collection and reduce ultimate loss while changing the present value of the asset. Where a modification of a financial asset does not result in derecognition, IFRS 9 requires the gross carrying amount to be recalculated as the present value of modified contractual cash flows discounted at the original EIR, with the applicable modification gain or loss recognised [4]. The contract workflow records the authorised new schedule, customer acceptance, purpose, effective date and accounting classification. The ECL engine then measures the remaining credit risk under the approved policy.

Write-off records the reduction of gross carrying amount when there is no reasonable expectation of recovery for all or part of the asset under the applicable requirements. It does not end the need to record later recovery cash, legal status or customer treatment. Recovery after write-off remains a distinct event with receipt date, gross amount, direct cost and accounting destination. This is why Part 4 required collection and finance records to remain joined after the credit decision.

The BCBS guidance on credit-risk practices for expected credit losses emphasises robust methodologies, experienced credit judgement, common processes, data and validation, while recognising that accounting frameworks determine the allowance [5]. The bank should therefore validate ECL components at their proper levels: discrimination and calibration for risk estimates, transition and cure accuracy, recovery amount and timing, scenario sensitivity, stage allocation, overlay governance and total allowance back-testing. A good account-level score can coexist with a poor ECL if timing, exposure, recovery or scenario assumptions are weak.

The accounting owner also controls the relationship between model output and journals. A production HLR artefact can send approved PD term structures, uncertainty, evidence quality and lineage into the impairment platform. It does not post its own allowance. Finance and credit-risk functions approve the scenario weights, stage logic, LGD, EAD, recovery assumptions and overlays, and the general ledger receives a balanced journal with reconciliation keys. This preserves the value of continuous evidence while keeping financial reporting reproducible.

## 5. Economic capital carries the adverse portfolio story

Expected loss describes the centre of a defined loss distribution. The accounting allowance applies IFRS 9 recognition and measurement to expected cash shortfalls. Regulatory capital follows the rules in the applicable CBK prudential framework. Internal economic capital is the institution's assessment of capital needed to absorb adverse loss at a stated horizon, confidence standard and solvency objective. The four quantities can use related data, but they have different mandates and cannot be substituted for one another.

The CBK Prudential Guidelines set the local capital-adequacy and asset-classification framework for regulated institutions [6]. The bank maps each exposure, mitigant and calculation to the currently applicable requirements and supervisory treatment. A better behavioural model may improve risk management before it changes any regulatory parameter. Recognition follows validation, governance and the method permitted for that institution.

For internal analysis, let \(L_{1y}\) be the one-year portfolio loss after ordinary contractual collections and recoveries but before capital absorbs the outcome. Let \(\rho_q\) be the board-approved risk functional at confidence level \(q\). Economic capital can be represented as:

\[
EC_q=\rho_q(L_{1y})-\mathbb E[L_{1y}],
\]

with \(\rho_q=VaR_q\) under a quantile standard or \(\rho_q=ES_q\) where the institution uses expected shortfall. The horizon, confidence level, treatment of expected loss, tax, diversification, pension or operational risks and capital definition must be stated. A number without those choices is not a capital measure.

The simulation or analytical engine draws coherent outcomes. Borrower transitions respond to common macroeconomic and sector factors, facility-level evidence and hierarchical effects. EAD reflects scheduled amortisation, further draw, cancellation and conversion. LGD reflects cure, collateral or guarantee cash, workout cost and recovery delay. Parameter draws propagate posterior uncertainty. Dependence challengers test residual clustering after observable common drivers have been represented. Model-form scenarios compare the champion with credible alternatives.

This matters for MSME portfolios because diversification can be overstated by counting borrowers rather than economic drivers. Restaurants in different neighbourhoods may depend on the same delivery platform. Retailers may share an importer, currency exposure or landlord. Farmers and processors may share rainfall and commodity shocks. Transport businesses may share fuel-price sensitivity. The current Basel supervisory principles identify sector, geography, product, collateral, currency, funding source and economic interdependence as relevant forms of concentration and require forward-looking stress testing across material risks [7], [8].

The internal capital pack should therefore report expected one-year loss, selected quantiles, expected shortfall where used, scenario loss, concentration add-ons, marginal and allocated capital, and the contribution of parameter and model uncertainty. Reverse stress identifies the combination of default timing, utilisation, recovery delay and common shock that first breaches a capital or risk-appetite boundary. Management can then change limits, sector mix, collateral, guarantee use, collection capacity or pricing through approved policy.

Allocated economic capital also supports product economics. For product or segment \(g\), a risk-adjusted contribution may be expressed as:

\[
RA_g
=Y_g-FTP_g-EL_g-OpEx_g-CoC\times EC_g,
\]

where each term uses the same period and exposure basis. This is a management view, not the customer-rate formula. It can show that a product with high nominal yield consumes disproportionate collection capacity, liquidity or tail capital. It can also show that an intervention which lowers durable loss and tail dependence creates value even when immediate interest income falls.

## 6. Collection timing becomes a treasury variable

An instalment can be economically valuable and still arrive too late to fund today's obligation. A promise to pay, a pending mobile-money instruction, an uncleared cheque, an accepted guarantee claim and cash in the settlement account are different liquidity states. The lifecycle ledger therefore records initiation, acceptance, settlement, reversal and final allocation separately. Treasury receives cash only when the account-control and settlement rules say it is available.

For time bucket \(b\), a simple cumulative liquidity position is:

\[
LG_b=C_0+\sum_{m\le b}
\left(CF_m^{\mathrm{settled}}+F_m^{\mathrm{available}}
-D_m^{\mathrm{contractual}}-O_m^{\mathrm{operating}}
-U_m^{\mathrm{contingent}}\right),
\]

where \(C_0\) is usable opening cash, \(F^{\mathrm{available}}\) is committed or reliably available funding, \(D\) is debt and depositor cash due, \(O\) is operating cash outflow and \(U\) is a scenario allowance for undrawn commitments, payment reversals, claim delay or other contingent use. The ladder is run by currency and legal entity. A positive expected ultimate recovery does not cure a negative near-term bucket until its timing and availability are credible.

Behavioural maturity links Part 2b to this ladder. A nominal 30-day facility may remain outstanding after a payment-date alignment, modification or partial cure. A revolving limit can draw when the enterprise's operating cash is already under pressure. Recovery may have a high ultimate percentage and a long legal delay. Treasury stresses those timing channels together with failed-payment recycling, concentration, guarantee settlement and new-funding availability.

The Basel liquidity principles call for prospective cash-flow forecasts across assets, liabilities and off-balance-sheet items, realistic behavioural assumptions, explicit allocation of liquidity costs and stress testing over multiple horizons [9]. CBK's 2025 guidelines add the applicable Kenyan LCR, NSFR and leverage-ratio framework for regulated banks [10]. Lifecycle evidence improves the behavioural inputs to those processes. Treasury and finance retain the approved regulatory calculations.

## 7. ALM and matched-maturity FTP translate cash timing into product economics

Asset-liability management asks how contractual and behavioural asset cash flows interact with funding, repricing, embedded options and liquidity. Funds-transfer pricing attributes the relevant cost or benefit to a product or relationship so that commercial performance is not confused with an unpriced treasury position. Neither function is a synonym for KESONIA or \(K_{\mathrm{RBCP}}\).

A KESONIA-linked MSME asset may reprice at the end of a monthly observation period while the deposit or wholesale funding that supports it reprices on another date. Fixed-rate assets, floors, caps, prepayments and undrawn revolving commitments add optionality. Stress can extend behavioural maturity at the same time that funding becomes more expensive. ALM therefore models both the scheduled contract and the customer's plausible response under each scenario.

IRRBB, or interest rate risk in the banking book, captures the effect of adverse rate movements on the bank's earnings and economic value. The Basel framework treats earnings and economic-value measures as complementary and requires assumptions about repricing, options and customer behaviour to be governed and stressed [11]. For a defined horizon, the bank can report:

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

The operating sequence begins with reconciled account schedules from Part 4. Treasury maps contractual cash flows, applies approved prepayment, drawdown, cure, modification and recovery behaviours, generates repricing and liquidity ladders, and runs benchmark, basis and behavioural shocks. Finance and product teams receive the transfer rate and matched spread. ALCO receives aggregate NII, EVE, liquidity and concentration views. The customer price remains governed through the RBCPM and product process.

Oracle Financial Services Funds Transfer Pricing is one possible enterprise implementation. Oracle describes matched-maturity transfer pricing and instrument-level allocation of asset, funding and interest-rate spreads, while its cash-flow engine supports contractual schedules, repricing and ALM scenarios [12]. A bank may use that platform, another treasury system or a validated internal engine. The authoritative product terms and settlement events remain in their source systems, and the treasury engine reconciles its output rather than becoming a second loan ledger.

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

Kenya's Credit Guarantee Scheme provides a concrete public example. The Public Finance Management (Credit Guarantee Scheme) Regulations establish a scheme intended to encourage additional MSME lending through partial guarantees and define participating financial intermediaries, eligible credit and reporting responsibilities [13]. The National Treasury describes the current programme as risk sharing between the Scheme and participating financial institutions, with qualifying facilities originated and monitored by those institutions [14]. Scheme participation therefore complements underwriting and collection. It does not replace lender due diligence, servicing or recovery.

Economic protection, IFRS 9 recognition and regulatory-capital recognition are tested separately. IFRS 9 includes cash flows from collateral and other credit enhancements in ECL when the relevant requirements are met and the enhancement is part of the contractual terms and not recognised separately [4]. Prudential recognition follows the applicable framework. The Basel credit-risk-mitigation standard requires legal enforceability and operational conditions for eligible guarantees and identifies residual risks such as claim delay, documentation weakness, maturity mismatch and counterparty dependence [15]. The participating bank maps those conditions to the current CBK treatment before recognising capital benefit.

Monitoring continues after cover is purchased. The dashboard follows covered and uncovered EAD, premium or fee, attachment utilisation, claim frequency, acceptance and rejection, settlement lag, recoveries, subrogation, expiry, counterparty credit, sector concentration and basis between the portfolio loss definition and the covered event. Gross and net calibration are both retained. A falling net loss can reflect a strong portfolio, generous protection or delayed recognition of an uncovered deterioration, so management reads the movement with exposure and claim status.

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

A bank can apply the lifecycle architecture while retaining loans on its balance sheet. Where scale, legal feasibility and investor demand justify another funding channel, eligible receivables may support a ring-fenced securitisation or private funding vehicle. The Capital Markets Act permits cash-flow-generating assets that are legally capable of sale, transfer or assignment to enter a securitisation trust and addresses true sale under Kenyan law [16]. The Asset-Backed Securities Regulations define the originator, issuer, trustee, servicer, eligible assets, credit enhancement and investor cash-flow structure for covered offers [17]. Transaction counsel, accountants, tax advisers, the relevant regulators and investors determine the structure in practice.

The optional vehicle purchases only receivables and associated rights that the originator owns and can transfer. An eligibility schedule tests documentation, balance, arrears, currency, sector, geography, prior encumbrance, data quality, concentration and enforceability. The servicer collects through controlled accounts. A waterfall pays permitted expenses, senior interest and principal, subordinate obligations, reserve cures and residual amounts in the contractual order. Overcollateralisation, cash reserves, subordination and early-amortisation triggers are modelled as finite protections.

The vehicle's analysis starts with the same monthly cash-flow distribution but retains separate funding quantities. Asset yield is the return collected on purchased receivables. A note margin \(m_{\mathrm{fund}}\) is an investor funding term. Bank FTP is the originating institution's internal funding attribution. The investor hurdle is a required return or valuation input. Excess spread is the cash remaining after realised asset collections, losses, expenses and note costs under the waterfall. These quantities are reconciled without renaming one another.

For tranche \(k\), attachment \(A_k\) and exhaustion \(E_k\), scenario loss can be represented as:

\[
TL_{k,s}=\min\!\left\{\max\!\left(L_s-A_k,0\right),E_k-A_k\right\}.
\]

The lender pack reports one-year and ultimate loss, payment timing, reserve use, covenant breaches and principal shortfall by scenario. Legal transfer, investor protection and capital relief remain consequences of the executed transaction and applicable approvals. The model supplies reproducible evidence for those decisions.

## 11. One control plane, several accountable owners

Part 5 completes the journey from a quoted benchmark to realised and transferred loss. Credit owns risk appetite and customer selection. Product and legal own terms. Finance owns ECL and journals. Capital owns internal and regulatory assessment. Treasury owns ALM, liquidity and FTP. Collections owns executed recovery strategy. The protection owner manages guarantees and claims. An optional vehicle's trustee, servicer and calculation agent own its contractual cash waterfall.

The joined evidence plane lets those owners reconcile without collapsing their mandates. A customer payment has one economic amount and timestamp, while pricing, ECL, capital and liquidity interpret it for different decisions. Part 6 will test whether the proposed lifecycle system improves durable collection, net recovery, customer outcomes and risk-adjusted economics under a bank-controlled experimental programme.

## References

[1] Central Bank of Kenya, “KESONIA Interest Rate Benchmark,” Nairobi, Kenya, 2026. [Online]. Available: https://www.centralbank.go.ke/kesonia/. [Accessed: Sep. 6, 2026].

[2] Central Bank of Kenya, *Revised Risk-Based Credit Pricing Model*, Nairobi, Kenya, Aug. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf. [Accessed: Sep. 6, 2026].

[3] Central Bank of Kenya, *36th Monetary Policy Committee Report*, Nairobi, Kenya, Apr. 2026, p. 20. [Online]. Available: https://www.centralbank.go.ke/uploads/monetary_policy_reports/131378250_36th%20Monetary%20Policy%20Committee%20Report%2C%20April%202026.pdf. [Accessed: Sep. 6, 2026].

[4] IFRS Foundation, *IFRS 9 Financial Instruments*, London, U.K., 2024. [Online]. Available: https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2024/issued/part-a/ifrs-9-financial-instruments.pdf?bypass=on. [Accessed: Sep. 6, 2026].

[5] Basel Committee on Banking Supervision, “Expected credit losses,” in *Basel Committee Consolidated Guidelines*, Bank for International Settlements, Basel, Switzerland, 2026. [Online]. Available: https://www.bis.org/committees/bcbs/basel-consolidated-guidelines/module/pap/20. [Accessed: Sep. 6, 2026].

[6] Central Bank of Kenya, *Prudential Guidelines for Institutions Licensed under the Banking Act*, CBK/PG/03 and CBK/PG/04, Nairobi, Kenya, Jan. 2013. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2016/08/PRUDENTIAL-GUIDELINES.pdf. [Accessed: Sep. 6, 2026].

[7] Basel Committee on Banking Supervision, *Principles for the Management of Credit Risk*, Bank for International Settlements, Basel, Switzerland, Apr. 2025. [Online]. Available: https://www.bis.org/publications/202504-guidelines-principles-management-credit-risk. [Accessed: Sep. 6, 2026].

[8] Basel Committee on Banking Supervision, “The Core Principles and assessment criteria,” Principle 19, *Basel Framework*, Apr. 2024. [Online]. Available: https://www.bis.org/committees/bcbs/basel-framework/standard/bcp/40/inforce/2024-04-25/published/2024-04-25. [Accessed: Sep. 6, 2026].

[9] Basel Committee on Banking Supervision, “Liquidity risk management and supervision,” *Basel Committee Consolidated Guidelines*, Jan. 2026. [Online]. Available: https://www.bis.org/committees/bcbs/basel-consolidated-guidelines/module/lqy/10. [Accessed: Sep. 6, 2026].

[10] Central Bank of Kenya, *Guidelines on the Liquidity Coverage Ratio, Net Stable Funding Ratio and Leverage Ratio*, Nairobi, Kenya, Apr. 2025. [Online]. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/04/GUIDELINES-ON-BASEL-III-LIQUIDITY-STANDARDS-AND-LEVERAGE-RATIO.pdf. [Accessed: Sep. 6, 2026].

[11] Basel Committee on Banking Supervision, “Interest rate risk in the banking book,” SRP31, *Basel Framework*, effective Jan. 1, 2026. [Online]. Available: https://www.bis.org/committees/bcbs/basel-framework/standard/srp/31/inforce/2026-01-01/published/2024-07-16. [Accessed: Sep. 6, 2026].

[12] Oracle, *Oracle Financial Services Funds Transfer Pricing User Guide*, Release 8.1.2.5.0, Sep. 2025. [Online]. Available: https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/funds-transfer-pricing/81250/ftpug/funds-transfer-pricing-user-guide.pdf. [Accessed: Sep. 6, 2026].

[13] Republic of Kenya, *The Public Finance Management (Credit Guarantee Scheme) Regulations, 2020*, Legal Notice No. 197 of 2020. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2020/197/eng%402022-12-31. [Accessed: Sep. 6, 2026].

[14] National Treasury and Economic Planning, “Credit Guarantee Scheme,” Nairobi, Kenya, 2026. [Online]. Available: https://cgs.treasury.go.ke/. [Accessed: Sep. 6, 2026].

[15] Basel Committee on Banking Supervision, “Standardised approach: credit risk mitigation,” CRE22, *Basel Framework*, Nov. 2020. [Online]. Available: https://www.bis.org/basel_framework/chapter/CRE/22.htm. [Accessed: Sep. 6, 2026].

[16] Republic of Kenya, *Capital Markets Act*, Cap. 485A, secs. 30I-30L. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/1989/17/eng%402023-12-11. [Accessed: Sep. 6, 2026].

[17] Republic of Kenya, *The Capital Markets (Asset-Backed Securities) Regulations*, Legal Notice No. 184 of 2007, rev. Dec. 31, 2022. [Online]. Available: https://new.kenyalaw.org/akn/ke/act/ln/2007/184/eng%402022-12-31. [Accessed: Sep. 6, 2026].
