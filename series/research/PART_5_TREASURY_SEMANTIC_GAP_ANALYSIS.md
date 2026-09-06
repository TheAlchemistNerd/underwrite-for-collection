Yes. Your instinct is correct: Part 5 contains a sound treasury foundation, but it currently reads more like an integrated financial-risk chapter than a complete treasury architecture.
I compared all 4,617 lines across the three source documents and the current Part 5. The most important missing bridge is between:
high-frequency collection evidence → behavioural cash-flow recognition → treasury validation → FTP attribution → ALCO decisions.

No files were edited.
Overall assessment
Part 5 already handles these areas well:
- KESONIA compounding and contractual conventions.
- Separation of KESONIA from \(K_{\mathrm{RBCP}}\).
- IFRS 9 cash-shortfall modelling.
- Economic capital and concentration.
- Collection timing as a liquidity variable.
- IRRBB through NII and EVE.
- Matched-maturity FTP.
- Intervention economics.
- Guarantees and other credit-risk transfer.
- Optional ring-fenced receivables funding.
Its principal weakness is that treasury appears as a destination for modelled cash flows, but not yet as a fully developed operating function with its own:
- funding curves;
- behavioural assumptions;
- liquidity buffers;
- transfer-pricing governance;
- deposit modelling;
- balance-sheet limits;
- stress scenarios;
- hedge decisions;
- intraday settlement controls;
- ALCO reporting;
- and model-approval process.
The current Part 5 is technically responsible. It deliberately avoided several exaggerated claims in the rough research. But in doing so, it retained less of the genuinely valuable treasury reasoning than it could have.
1. What UNDERWRITE_FOR_COLLECTION.md contributes
The anchor article contains the thesis from which Part 5 grows, but it does not attempt a full treasury treatment.
Sustainable collectability as a financial objective
The central proposition is that lending should be designed around sustainable post-disbursement cash collection. It explicitly joins product design, monitoring, servicing, restructuring, recovery, expected loss, capital and funding. That framing appears at [lines 8–14 (line 8)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION.md:8).
Part 5 carries this forward effectively by beginning with an MSME facility entering the business as working capital and returning as uncertain cash flows.
Cash-flow timing and affordability
The article observes that a borrower may generate enough monthly revenue but still fail because receipts and repayments occur at incompatible times. It identifies:
- income timing and volatility;
- essential operating expenditure;
- other repayment obligations;
- seasonality;
- residual liquidity;
- and alignment between repayment and the activity being financed.
This appears at [lines 39–50 (line 39)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION.md:39).
Part 5 translates that idea into contractual and behavioural cash-flow ladders, but it could go further by connecting borrower cash conversion cycles to treasury’s product-level behavioural maturity assumptions.
Settlement-state distinctions
The article requires payment initiation, settlement, allocation and reversal to remain separate events. That is one of its most treasury-relevant observations because an initiated payment is not necessarily usable liquidity. See [lines 56–74 (line 56)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION.md:56).
Part 5 adopts this principle clearly in section 6. It distinguishes:
- a promise to pay;
- a pending mobile-money instruction;
- an uncleared cheque;
- an accepted guarantee claim;
- and settled cash.
That is an important strength.
Recovery, ECL, capital and funding
The article connects collection timing, cures, modifications, prepayments, collateral proceeds and workout costs to IFRS 9 cash shortfalls. It also distinguishes accounting stage, economic capital, liquidity and receivables-finance eligibility at [lines 148–163 (line 148)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION.md:148).
Part 5 expands all these areas substantially.
SPV and investor cash
The article says that investors in a ring-fenced SPV receive cash only after:
- collection lags;
- servicing costs;
- workout costs;
- recoveries;
- reserve requirements;
- and the priority of payments.
It calls for cohort-level cash flows, stress tests, covenants and early-amortisation triggers at [line 161 (line 161)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION.md:161).
Current Part 5 contains the optional SPV concept, eligibility, controlled accounts and waterfall, but this treatment is brief. It does not yet carry all those operational treasury mechanics into the SPV section.
2. What the rough research contributes to Part 5
The rough document contains the most extensive treasury thinking. Its claims vary in reliability, but its questions are valuable.
Lines 512–845: KESONIA and experimental pricing
This block asks how prospective evidence might affect risk-based pricing. It distinguishes the common KESONIA reference from borrower-specific pricing, but then sometimes describes KESONIA as a static experimental control and treats an RCT as directly discovering \(K\).
The useful propositions are:
- contemporaneous experimental groups should share the same benchmark convention;
- borrower-risk evidence should influence a governed pricing methodology;
- price elasticity can itself affect repayment and selection;
- retrospective portfolios may reflect earlier benchmark and underwriting regimes;
- pricing comparisons must control for calendar time and macroeconomic conditions.
Part 5 correctly rejects the idea that KESONIA is a static experimental control. It describes KESONIA as a daily overnight benchmark whose economic effect depends on the contract.
What remains underdeveloped is price elasticity. Part 5 acknowledges that a wider premium can increase payment stress, adverse selection or early exit, but it does not connect this to treasury’s volume, margin and funding projections.
Lines 846–1077: modelling architecture as a pricing input
This block develops the HLR, survival challenger, P-splines, residual neural representations and horseshoe priors.
Its Part 5 relevance is indirect but important:
- the HLR estimates the probability distribution of loss;
- the survival model contributes payment, cure and default timing;
- revolving utilisation contributes EAD;
- recovery models contribute amount and delay;
- hierarchical effects support sector and cohort differentiation;
- uncertainty should propagate into ECL, economic capital and liquidity stress.
Part 5 handles this well. It uses one physical cash-flow distribution as the common input to pricing, ECL, capital, treasury and risk transfer.
Lines 1078–1320: intervention timing and event intensity
This material explores contextual bandits, POMDPs, Cox models and point processes. Several mathematical relationships are overstated, particularly the claim that introducing a POMDP inherently introduces an intensity model.
The treasury-relevant ideas are nevertheless valuable:
- payment events can be irregular and clustered;
- collection actions can change the timing of cash;
- a payment reminder may move cash without changing ultimate loss;
- a restructuring can reduce near-term cash but improve ultimate recovery;
- expected collection timing should be conditional on treatment;
- state transitions should affect liquidity forecasts.
Part 5 partially captures this through its causal net economic value formula. It includes the change in discounted collections, treatment cost, funding cost and capital.
What remains missing is an explicit separation among:
1. cash accelerated from a later period;
2. genuinely incremental cash;
3. collections that would have occurred without treatment;
4. cash followed by rapid re-default;
5. and cash whose operational cost exceeds its liquidity benefit.
That distinction is crucial to Treasury. An intervention that advances a payment by three days may help a short liquidity bucket without improving lifetime economic value.
Lines 1321–1480: anatomy of the pricing premium
The rough document proposes a decomposition of \(K\) into risk, operating cost and shareholder margin. It mixes expected loss, unexpected loss, accounting provisions and capital in places, but identifies the right economic question: how does the customer premium reconcile to the bank’s actual cost structure?
The side-by-side analysis corrected the required component list to include:
- benchmark;
- funding and liquidity cost;
- expected loss;
- unexpected-loss or capital allocation;
- operating and servicing cost;
- customer-specific risk;
- shareholder return;
- fees and taxes;
- contractual and regulatory constraints.
Current Part 5 contains a premium bridge at [lines 46–73 (line 46)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/series/parts/Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md:46), but this is one place where treasury is materially underrepresented.
The formula includes:
- operating cost;
- servicing cost;
- borrower risk;
- capital;
- shareholder return;
- and a residual reconciliation term.
It does not explicitly show the part of FTP above or below KESONIA, such as:
- term liquidity premium;
- basis cost;
- embedded-option cost;
- statutory or reserve drag;
- and funding-source spread.
Those costs should not disappear into \(\varepsilon\). Part 5 later defines FTP, but it never algebraically reconnects FTP to \(K_{\mathrm{RBCP}}\).
That is probably the single most important missing treasury bridge.
Lines 1481–1670: ALM and FTP
This is the core treasury block in the rough document. It discusses:
- Treasury as the bank’s internal funding allocator.
- The MSME business unit receiving an internal transfer charge.
- KESONIA as an overnight reference for assets with longer behavioural lives.
- Term liquidity premiums.
- Cash reserve and statutory effects.
- Liquidity, interest-rate and maturity mismatch.
- ALCO governance.
- Behavioural prepayments and defaults.
- Separation of the Treasury transfer rate from credit and operating spreads.
- Matched-maturity FTP for KESONIA-linked facilities.
Current Part 5 successfully retains:
- the distinction between KESONIA and FTP;
- behavioural cash flows;
- the funding curve;
- liquidity, option and basis components;
- ALCO reporting;
- NII and EVE;
- and an optional Oracle implementation.
However, it compresses the actual treasury operating mechanism into a few paragraphs. Missing or lightly treated elements include:
- how the internal funding curve is constructed;
- whether marginal or average funding cost is used;
- how deposit products receive an FTP credit;
- how lending products receive an FTP charge;
- how variable-rate assets are transfer-priced between reset dates;
- how transfer rates are locked, reset or recalculated;
- how floors and caps are charged;
- how prepayment and drawdown options are priced;
- how liquidity premiums change across maturity buckets;
- and how the resulting transfer rate reconciles to business-unit margin.
Lines 1672–1830: high-frequency collections and Treasury validation
This is the most valuable underused section.
The rough document initially claims that frequent repayments collapse asset duration and justify a lower term liquidity premium. The user then challenges that conclusion. The resulting discussion introduces necessary prudential conditions:
- settlement lags;
- weekend effects;
- reversals;
- mobile-money clearing;
- operational failures;
- cash hoarding or diversion;
- behavioural instability;
- transaction costs;
- contractual versus behavioural maturity;
- and stress-dependent collection reliability.
The rough document then proposes a behavioural haircut before Treasury recognises collection velocity. Its specific formula and percentages are provisional, but the concept is strong.
Current Part 5 recognises that initiated cash is not settled cash and that behavioural maturity must be stressed. What it lacks is an explicit Treasury recognition gate.
A defensible gate would require evidence that high-frequency collections:
- settle reliably;
- remain available to the bank;
- survive reversals;
- persist across weekends and operational outages;
- remain stable under adverse economic conditions;
- are not produced by harmful depletion of working capital;
- exceed their processing and servicing costs;
- and have been accepted under the institution’s FTP policy.
Without such a gate, the chapter moves too quickly from lifecycle data to behavioural maturity.
Lines 1831–2452: fairness and forbearance as financial constraints
Much of this block belongs primarily to Parts 3 and 4. Its Part 5 implications include:
- aggressive collection can destroy the working capital that supports future repayment;
- forbearance changes contractual and behavioural cash flows;
- conduct restrictions can alter collection timing;
- customer harm and complaint costs affect economic value;
- repricing cannot be used indiscriminately as an intervention;
- and an apparently successful short-term collection can reduce long-term recovery.
Part 5’s intervention-value formula captures treatment, funding and capital costs. It could further recognise:
- modification gain or loss;
- forbearance-related liquidity displacement;
- re-default probability;
- complaint and remediation cost;
- and the value of preserving the borrower’s future productive capacity.
Lines 2453–2775: model governance and Treasury approval
This block introduces champion-challenger testing, maker-checker controls and model graduation. Some numerical thresholds are arbitrary, but the governance concept is relevant to Treasury.
Treasury should not change:
- behavioural maturity;
- liquidity premiums;
- collection assumptions;
- prepayment curves;
- or FTP charges
merely because a credit challenger has better predictive discrimination.
The Treasury use of a new behavioural model requires its own approval criteria:
- cash-flow forecast error;
- settlement accuracy;
- stability under stress;
- weighted-average-life error;
- liquidity-gap impact;
- NII and EVE sensitivity;
- FTP stability;
- operational cost;
- and observed versus predicted cash availability.
Current Part 5 says that Treasury applies approved behavioural assumptions, but it does not describe how those assumptions become approved.
Lines 2776–3078: shadow trials, exposure and data maturity
This block separates passive shadow testing from active interventions. Its Part 5 relevance is substantial.
A shadow model can estimate:
- differences in predicted payment timing;
- forecast accuracy;
- hypothetical liquidity gaps;
- expected FTP changes;
- and portfolio profitability effects.
But it cannot establish the causal cash-flow effect of an intervention unless the assignment design supports that inference.
Current Part 5 makes this distinction in the intervention section, but it does not explicitly divide Treasury evidence into:
- predictive shadow evidence;
- realised operational evidence;
- experimentally identified treatment effects;
- and assumptions approved for financial use.
Lines 3079–3245: model-to-data deployment
This block proposes deployment inside a bank-controlled environment. Most of it belongs in Part 4, but Treasury also needs:
- authoritative contractual schedules;
- payment-settlement feeds;
- deposit and funding data;
- rate-curve data;
- general-ledger reconciliation;
- approved model artefacts;
- and disclosure-controlled outputs.
Current Part 5 depends on Part 4’s account schedules but gives little attention to the Treasury data mart or reconciliation architecture.
Lines 3246–3473: cure, recovery and portfolio dependence
This material connects:
- cure;
- re-default;
- vintage analysis;
- EAD;
- LGD;
- contagion;
- and sector clustering.
Part 5 uses most of these concepts in ECL and economic capital. The remaining opportunity is Treasury-specific vintage reporting:
- contractual versus realised cash by vintage;
- settlement delay by vintage;
- behavioural maturity drift;
- FTP margin by vintage;
- recovery timing;
- guarantee settlement timing;
- and liquidity forecast error.
3. What the side-by-side semantic analysis contributes
The side-by-side analysis is the strongest guide for deciding what should enter Part 5 because it already separates useful concepts from unsupported claims.
Its direct treasury section is [lines 389–411 (line 389)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION_SIDE_BY_SIDE_SEMANTIC_ANALYSIS.md:389).
It establishes that frequent repayments shorten realised weighted-average life only when:
- settlement is reliable;
- reversals are controlled;
- cash remains available;
- performance persists during stress;
- operating costs do not consume the benefit;
- prepayment and delinquency models are validated;
- and the effect is accepted under approved FTP policy.
It also identifies the proper outputs:
- behavioural cash-flow curves;
- collection and settlement lags;
- prepayments;
- drawdown behaviour;
- cure and recovery timing;
- liquidity-gap modelling;
- matched-maturity FTP;
- IRRBB stress;
- and product profitability.
Current Part 5 incorporates every item at least conceptually, but not all at operating depth.
The semantic analysis also supplies three corrections that Part 5 has handled properly:
1. KESONIA is not an experimental control. It is a changing benchmark component. See [lines 150–164 (line 150)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION_SIDE_BY_SIDE_SEMANTIC_ANALYSIS.md:150).
2. An RCT does not directly discover \(K_{\mathrm{RBCP}}\). Treatment effects can inform expected loss, operating cost and product design, but the premium retains a wider economic and governance structure. See [lines 165–184 (line 165)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION_SIDE_BY_SIDE_SEMANTIC_ANALYSIS.md:165).
3. Liquidity and capital effects are secondary financial outcomes. They should be measured, not manipulated as trial targets. See [lines 389–411 (line 389)](C:/Users/Nevo/Downloads/insuretech & embedded finance/behavioural credit scoring - underwrite to collect rct/source_library/00_anchors/UNDERWRITE_FOR_COLLECTION_SIDE_BY_SIDE_SEMANTIC_ANALYSIS.md:389).
These corrections explain why Part 5 is cautious. The caution is justified, but a fuller treasury treatment can preserve it while adding operational detail.
4. Semantic comparison matrix
Treasury theme	Source treatment	Current Part 5	Assessment
KESONIA definition	Rough sometimes calls it static; semantic analysis corrects this	Accurate daily benchmark and compounding convention	Strong
Contractual benchmark mechanics	Limited in source documents	Source, dates, lookback, day count, floor, cap, fallback and correction	Strong
\(K_{\mathrm{RBCP}}\) decomposition	Rough identifies risk, cost and return but conflates items	Governed component bridge	Good, but funding/FTP spread is not explicit
Expected loss	Anchor and semantic analysis require consistent horizons	Physical-measure loss and IFRS 9 are separated	Strong
Settlement versus payment instruction	Anchor requires distinct states	Explicitly implemented	Strong
Behavioural maturity	Rough develops it extensively	Present in liquidity and FTP sections	Sound but compressed
High-frequency cash recognition	Rough proposes duration compression; semantic analysis adds conditions	General caution is present	Missing a formal validation gate
Liquidity ladder	Implied in anchor and rough	Explicit cumulative liquidity equation	Strong
LCR and NSFR	Rough overstates effects; semantic analysis corrects this	Mentioned with CBK citation	Too brief for a treasury chapter
HQLA	Rough incorrectly suggests collections create HQLA	Not repeated	Correct omission
IRRBB	Rough introduces Treasury ownership	NII and EVE formulas plus MSME use case	Present, but could be deeper
FTP	Rough provides the business-unit/Treasury bridge	Generic matched-maturity formula	Correct but under-specified
Deposit behaviour	Rough briefly mentions deposits and ALCO	Only visible in the figure	Material gap
CRR/statutory drag	Rough raises it, though simplistically	Not explicitly treated	Potential gap requiring careful sourcing
Intraday liquidity	Rough discusses settlement and clearing lags	Only indirectly represented	Underdeveloped
ALCO governance	Rough discusses ALCO approval	ALCO receives reports	Governance process is underdeveloped
Intervention economics	Anchor and rough connect treatment to cash	Formal causal net-economic-value equation	Strong
Risk transfer	Limited in rough	Detailed guarantees and retained-loss modelling	Stronger than the sources
SPV treasury	Anchor calls for reserves, waterfall and triggers	Optional section is concise	Materially underdeveloped
Treasury scorecard	Anchor supplies lifecycle metrics	No consolidated Treasury/ALCO scorecard	Gap
Data and model approval	Semantic analysis proposes evidence stages	Treasury uses approved assumptions	Approval pathway is not described


5. The treasury aspects Part 5 has most clearly missed
1. The algebraic bridge from KESONIA to FTP to customer margin
Part 5 defines \(K_{\mathrm{RBCP}}\) and FTP separately, but it does not reconcile them.
A future treatment should show that the customer-facing increment over KESONIA may need to absorb, subject to the approved methodology:
- the difference between the approved FTP rate and KESONIA;
- liquidity-premium attribution;
- basis and option charges;
- expected loss;
- operating and servicing cost;
- capital allocation;
- and required commercial return.
This would prevent Treasury cost from being hidden in a residual term and would make double counting visible.
2. Funding-curve construction
The current \(r_{\mathrm{curve}}(d_g,q_g,t)\) is mathematically clean but economically abstract.
The chapter does not explain:
- which observable or internal curve anchors are used;
- how an overnight benchmark is translated to term funding;
- how secured, unsecured, retail-deposit and wholesale sources differ;
- whether marginal or average funding cost is used;
- how liquidity premiums vary by term;
- or who approves curve changes.
3. Non-maturity deposits and deposit FTP
The figure mentions deposits, but Part 5 does not model them.
A complete bank treasury treatment needs at least conceptual coverage of:
- stable and volatile deposit components;
- deposit decay;
- repricing beta;
- lagged pass-through;
- administered rates;
- concentration;
- withdrawal behaviour under stress;
- and the FTP credit assigned to deposit-gathering units.
FTP should be two-sided. Lending units receive charges, while funding-generating units may receive credits.
4. Treasury recognition of high-frequency cash
The semantic analysis provides the missing principle: predicted frequent cash should not automatically change behavioural maturity or FTP.
Treasury needs a controlled graduation process from:
1. observed event frequency;
2. to settled cash behaviour;
3. to stress-tested behavioural maturity;
4. to approved liquidity assumptions;
5. to FTP recognition.
The evidence should include forecast error, reversal rates, settlement delays, weekend effects, operational outages, concentration and persistence through stress.
5. LCR, NSFR and contingency liquidity
Part 5 cites LCR and NSFR but does not show their practical relevance.
It could distinguish:
- contractual inflow from eligible regulatory inflow;
- settled cash from HQLA;
- expected inflow from inflow recognised under the applicable calculation;
- behavioural maturity from required stable funding;
- and ordinary liquidity management from regulatory ratios.
A broader treasury architecture would also include:
- liquidity buffers;
- encumbered versus unencumbered assets;
- committed backup funding;
- concentration of funding;
- early-warning indicators;
- survival horizons;
- and the contingency funding plan.
6. More complete IRRBB mechanics
IRRBB is present, not absent. But it currently stops at NII, EVE and one useful scenario.
Further depth could cover:
- repricing-gap ladders;
- basis risk between KESONIA-linked assets and deposit or wholesale funding;
- deposit beta;
- yield-curve shape shocks;
- floors and caps;
- prepayment and extension risk;
- undrawn revolving commitments;
- key-rate sensitivities;
- and assumption governance.
7. Intraday and payment-rail liquidity
The rough document raises a valid distinction between merchant payment activity and cash available to Treasury.
Part 5 should eventually distinguish:
- customer transaction time;
- payment instruction time;
- wallet deduction;
- switch confirmation;
- settlement finality;
- collection-account receipt;
- internal availability;
- reversal window;
- and allocation to principal, interest or fees.
This is particularly important where mobile-money or platform collections are treated as high-frequency liquidity evidence.
8. ALCO and FTP governance
The current draft says ALCO receives NII, EVE, liquidity and concentration views. It does not describe the governance cycle.
A complete treatment would identify:
- curve owner;
- assumption owner;
- model validator;
- business-unit challenge;
- ALCO approval;
- exception handling;
- model-change thresholds;
- transfer-price effective dates;
- back-testing;
- P&L attribution;
- and escalation when realised cash differs from the FTP assumption.
9. Treasury treatment of risk transfer
The risk-transfer section is strong from a credit and claims perspective, but it could say more about Treasury.
Treasury needs to distinguish:
- expected claim from settled claim;
- funded versus unfunded protection;
- claim-receivable liquidity;
- counterparty and wrong-way risk;
- premium-payment timing;
- basis risk;
- maturity mismatch;
- renewal risk;
- collateralisation;
- and the difference between capital relief and liquidity support.
A guarantee can reduce loss while doing little for a near-term liquidity gap if settlement is slow.
10. SPV treasury and note mechanics
Part 5’s ring-fenced route is currently only a structural introduction.
If the SPV remains in Part 5, its treasury treatment could include:
- collection, principal, interest and reserve accounts;
- payment dates and calculation periods;
- note benchmark and margin;
- asset and liability reset mismatch;
- prefunding and negative carry;
- borrowing-base and advance-rate tests;
- overcollateralisation;
- reserve targets;
- revolving and amortisation periods;
- early-amortisation triggers;
- commingling and servicer-disruption risk;
- liquidity facilities;
- hedge and FX treatment;
- permitted investments;
- and trustee or calculation-agent reporting.
The anchor article expressly anticipated reserves, waterfalls, covenants and early amortisation. Current Part 5 mentions these but does not develop their cash mechanics.
6. Material from the rough document that should remain excluded
The treasury gaps should not be filled by copying the rough document directly. Several statements were correctly omitted or corrected:
- KESONIA should not be described as static.
- KESONIA is not the RCT control group.
- An RCT does not directly calculate the whole \(K_{\mathrm{RBCP}}\).
- Frequent collection does not automatically make the loan short-duration.
- Daily repayments do not become HQLA.
- Collection inflows do not automatically improve LCR or NSFR treatment.
- A lower PD does not automatically release IFRS 9 provisions or regulatory capital.
- High-frequency cash does not make a portfolio self-funding.
- Hawkes intensity is not automatically a Treasury liquidity measure.
- A behavioural model does not determine the bank’s official IRRBB position.
- Illustrative behavioural haircuts should not be presented as regulatory parameters.
- Improved prediction does not automatically justify a lower FTP rate.
The side-by-side analysis already provides the correct principle: behavioural evidence can improve Treasury assumptions only after settlement, persistence, stress, operational cost and governance have been established.
Final judgement
Part 5 has captured the financial architecture of Treasury, but not yet the operating architecture of Treasury.
Its foundation is strong and technically more reliable than the rough document. The missing depth is concentrated in six areas:
1. Reconciliation of \(K_{\mathrm{RBCP}}\), KESONIA and FTP.
2. Construction and governance of the funding curve.
3. Deposit behaviour and two-sided FTP.
4. Validation of high-frequency collections before Treasury recognition.
5. Practical LCR, NSFR, intraday-liquidity and contingency-funding treatment.
6. ALCO governance, SPV treasury and detailed balance-sheet reporting.
So the answer is not that Part 5 omitted Treasury. It included the right treasury concepts, including IRRBB, but compressed them just where the last two source documents contained their most useful questions. The next refinement should deepen those mechanics while retaining the semantic analysis’s corrections and avoiding the rough research’s unsupported prudential conclusions.