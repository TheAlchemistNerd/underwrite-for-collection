# 4G Capital: public evidence, guarantee mechanics and contact routes

**Checked:** 13 October 2026.  
**Lead research:** Underwrite for Collection. **Supporting methods:** Mwendo Pamoja's Bayesian decisions, interventions and operating-to-financing cash analysis.  
**Scope:** public evidence and a proposed research application. Product terms, portfolio results and pilot parameters enter through a documented engagement.

## 1. Product evidence and the application

| ID | Primary source | Verified public description | Proposed research use |
|---|---|---|---|
| E1 | [UPIA](https://www.4g-capital.com/upia) | Unsecured 30-day working-capital loans; branch support and training; loyalty-based pricing. Published range KES 5,000–149,999. | Follow stock purchase, sales, operating cash, repayment and remaining working capital across repeated cycles. Set price from the actual offer. |
| E2 | [KUZA](https://www.4g-capital.com/kuza) | 21-day stock credit through distributor partners; payment directly to distributor through mobile money; margin-based pricing; published range KES 5,000–360,000. | Link order, delivery, inventory, sales, settled receipts and repayment. Build distributor and merchant identifiers into the evidence model. |
| E3 | [4G Capital homepage](https://www.4g-capital.com/) | Describes a touch-tech combination of digital access, mobile-money payments, personal support and customised training. | Define how field observations become timely evidence; compare approved support methods and timing against business and lending outcomes. |
| E4 | [2026 privacy notice](https://8bc8d3dc-a6c3-4fec-aea0-b6aa1421a51a.filesusr.com/ugd/ca9a63_6bc5c61af4374a86b415a6440d18840c.pdf), linked from company product pages | Company notice covering personal-data processing. | Inventory existing purposes, recipients, rights and access controls before agreeing a specific research dataset. |

For an initial engagement, choose one product and a bounded merchant/distributor or branch cohort. Compare the current approved support process with a defined addition. Measure merchant cash after operating and household requirements, gross margin, inventory turnover, durable cure, customer experience and net lender collections. The central decision is whether a lending cycle supports the next viable trading cycle.

## 2. IFC: preserve the level and date of each figure

### Programme announcement

**[E5] [IFC announcement, 4 August 2026](https://www.ifc.org/en/pressroom/2026/ifc-supports-expansion-of-financing-for-kenya-s-small-businesses-through-the-first).** This announces three Kenyan CFLG transactions: 4G Capital, Equity Bank Kenya and KCB Bank Kenya. Aggregate figures are USD 24.2 million committed, USD 11 million IDA PSW backing, approximately USD 144.4 million equivalent local-currency lending and USD 120.2 million additional lending. IFC reports an 11:1 target leverage ratio. The programme serves microenterprises, women-owned businesses and climate-focused enterprises under IFC's USD 4 billion MSME Platform.

The announcement establishes commitment and the programme context. These aggregate figures belong to all three transactions. An article should state their scope directly when using them.

**[E6] [4G Capital announcement, 5 August 2026](https://www.4g-capital.com/post/4g-capital-partners-with-ifc-to-expand-financing-for-kenya-s-micro-and-small-businesses).** Confirms the partnership and describes expansion of working-capital access, including women-owned businesses, with continued support for institutional capability.

### 4G-specific project disclosure

**[E7] [IFC SII project 53511, MFP-CFLG-4G CAP](https://disclosures.ifc.org/project-detail/SII/53511/mfp-cflg-4g-cap).** Disclosed 24 May 2026; updated 4 July; approval 29 June; signing 30 June; displayed status pending disbursement.

| Narrative item | USD equivalent |
|---|---:|
| Kenyan-shilling portfolio | 44.4m |
| First-loss layer | 2.2m |
| IFC first-loss maximum | 2.0m |
| Second-loss layer | 42.2m |
| IFC second-loss maximum | 4.2m |
| IFC total narrative maximum | 6.2m |
| Separate approved-investment table | 8.20m |

The narrative describes an **unfunded financial guarantee**, retained 4G risk, pari-passu second-loss sharing and microenterprise/women-owned microenterprise beneficiaries in Kenya. Advisory work includes guarantee onboarding, underwriting and distributor finance. The public narrative and approval table give different totals; the executed agreement is the reference for implementation. The disclosure also identifies **Austen Titford, CFO, Austen.titford@4g-capital.com**, for project enquiries.

### Public facts to carry into the pitch

The published partnership creates a concrete reason to connect customer-level evidence to a portfolio protection ledger. The scoping deliverable should reconcile the signed terms to the loan tape and guarantee reporting requirements. The deck can illustrate the architecture with independently specified hypothetical parameters, then show where confirmed contract values replace those parameters.

## 3. Agreement terms needed to reproduce the facility

The following is an implementation request list developed for this research. Each term changes either eligibility, allocation, timing or the interpretation of results.

| Contract field | Reason for capture |
|---|---|
| Contracting entities and beneficiary | Identify the party entitled to submit claims and receive cash. |
| Executed maximum liability and currency | Reconcile the public figures, operational cap and currency conversion convention. |
| Portfolio definition | Establish whether the cap concerns cumulative originations, peak outstanding principal, an amortising pool or a replenishing portfolio. |
| Availability, inclusion and maturity dates | Admit only exposures within the agreed period and follow them to the contractual end. |
| Borrower/product/geographic eligibility | Map eligibility to verified source fields; establish whether each selected product qualifies. |
| Loss definition | Determine whether covered loss is principal, specified interest, net loss after recoveries, or another agreed quantity. |
| Attachment, layer size, sharing percentages and caps | Implement allocation precisely rather than inferring percentages from rounded disclosure amounts. |
| Deductibles, exclusions and limits | Apply per-loan, borrower, sector, vintage and portfolio provisions. |
| Claim trigger and waiting period | Distinguish arrears, default recognition, claim eligibility and submission. |
| Evidence package and acceptance process | Reconstruct the supported amount and its decision history. |
| Payment currency, lag and settlement instructions | Translate accepted claims into dated bank cash. |
| Recovery ownership and expenses | Allocate post-claim receipts and reasonable recovery costs according to the agreement. |
| Reinstatement, recycling and clawback | Recalculate available protection only when the relevant contractual rule allows it. |
| Fees and other costs | Evaluate financing economics after guarantee, servicing, reporting and operational expenditure. |
| Amendments and restructuring permissions | Preserve coverage when approved changes alter the borrower obligation. |
| Reporting, E&S and audit requirements | Maintain the records needed to demonstrate programme eligibility and performance. |

## 4. A computational structure for the worked example

This section specifies a generic model for a portfolio guarantee. Its variables are chosen for a transparent example and populated from the applicable agreement in a live engagement.

Let L be eligible cumulative loss under the defined calculation, A the first-layer size, α₁ and α₂ the guarantor's contractual sharing proportions, and K₁ and K₂ the respective guarantee caps. If the contract allocates losses proportionately within successive layers, the example can use:

G₁(L) = min(K₁, α₁ × min(L, A))

G₂(L) = min(K₂, α₂ × max(L − A, 0))

G(L) = G₁(L) + G₂(L)

R(L) = L − G(L)

Here G is allocated guarantee support and R is retained eligible loss before other contractual adjustments. Use a different allocation function when the agreement defines sequential first-loss absorption, aggregate deductibles, revolving cover or another structure. The rounded public layer amounts provide context; contractual sharing proportions are distinct input fields.

Maintain a separate **event ledger**. An exposure can produce an eligible loss on one date, a submitted claim later, acceptance after review and cash settlement later still. A claim receivable has an accounting status and an expected cash date. The liquidity model uses the actual scheduled or stressed settlement date. In this way a guarantee can improve retained-loss economics while the lender still needs cash to fund the intervening period.

For a dated cash model, write:

Cₜ = Cₜ₋₁ + Bₜ + Gₜ,cash + Fₜ − Dₜ − Oₜ − Sₜ − Qₜ

where C is lender cash, B borrower cash receipts, Gcash guarantee settlement, F external funding received, D new disbursements, O operating expenditure, S funding service and Q contractual guarantee fees or recovery remittances. Define each source once and reconcile it to the bank ledger. A subsequent recovery affects B and any sharing remittance Q, while an accounting receivable movement remains in its own reconciliation.

Evaluate commercial outcomes under equal borrower scenarios with and without protection. Keep borrower repayment probabilities linked to trading outcomes, obligations and interventions. Apply the guarantee to the lender's resulting loss and liquidity exposure. This separation makes the benefit measurable and preserves a clear explanation of what changes for the business, lender and risk-sharing partner.

## 5. Authoritative operational and evaluation anchors

**[E8] [IFC CFLG facility page](https://www.ifc.org/en/what-we-do/sector-expertise/financial-institutions/msme-finance/catalytic-first-loss-guarantee-facility)** describes portfolio coverage intended to expand finance to underserved MSMEs and demonstrate commercial viability. It lists eligible financial-service-provider types and qualification dimensions. The Kenya project is read through its own disclosure and executed terms.

**[E9] World Bank Group and FIRST Initiative, [Principles for Public Credit Guarantee Schemes for SMEs](https://www.worldbank.org/en/topic/financialsector/publication/principles-for-public-credit-guarantee-schemes-cgss-for-smes), 2015.** [Full report](https://documents1.worldbank.org/curated/en/576961468197998372/pdf/101769-REVISED-ENGLISH-Principles-CGS-for-SMEs.pdf). Principles 9–13 address eligibility, delivery, risk sharing, pricing and claims; principles 14–16 address reporting and evaluation. These are an operational comparison framework. For this engagement, translate them into eligibility checks, documented claim decisions, recovery allocation and a measured access-to-finance objective.

**[E10] F. Campos et al., “Teaching personal initiative beats traditional training in boosting small business in West Africa,” Science, vol. 357, no. 6357, pp. 1287–1290, 2017, doi: [10.1126/science.aan5329](https://doi.org/10.1126/science.aan5329).** [Full paper hosted by research partner IPA](https://poverty-action.org/sites/default/files/2023-10/science.aan5329.pdf). Its Togo randomised study compares training approaches and follows business outcomes. It motivates testing the content and delivery of support locally. A 4G study would estimate its own effects and connect them to repayment, borrower welfare and support cost.

## 6. Data protection and regulatory sources

- **[E11] [Kenya Data Protection Act 2019](https://new.kenyalaw.org/akn/ke/act/2019/24/eng%402019-11-15/source)**: sections 25–26, 29–31, 35, 41–43 and 48–49 are useful anchors for principles, rights, notice, legal basis, DPIA, automated decisions, security and transfers.
- **[E12] [Data Protection (General) Regulations 2021](https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf)**: regulation 22 addresses automated individual decisions; regulations 49–51 address high-risk assessment and consultation.
- **[E13] [ODPC Guidance Note for Digital Credit Providers](https://www.odpc.go.ke/wp-content/uploads/2024/02/ODPC-Guidance-Note-for-Digital-Credit-Providers.pdf)**, December 2023: sector implementation guidance read alongside the Act and regulations.
- **[E14] [CBK directory updated 29 September 2026](https://www.centralbank.go.ke/wp-content/uploads/2026/09/Directory-of-Digital-Credit-Providers-September-2026.pdf)**, entry 87: lists Fourth Generation Capital Limited, with licence date 27 March 2023. Establish the entity and applicable authorisation in the pilot charter.
- **[E15] [Central Bank of Kenya (Non-Deposit Taking Credit Providers) Regulations 2026, Legal Notice 191](https://new.kenyalaw.org/akn/ke/act/ln/2026/191/eng@2026-09-29/source.pdf)**: official gazette retrieved directly from Kenya Law. A source-specific reading note accompanies this register.

The pilot's data contract should identify purpose, lawful basis, source, sensitivity, retention, access, recipients and cross-border arrangements for each data group. A pseudonymous merchant identifier connects research events; authorised servicing staff retain the appropriate means to assist the customer. A review workflow records the recommendation, uncertainty, reasons, human decision and eventual outcome. Customer feedback and correction routes are part of the evidence design.

## 7. Verified public outreach routes

| Route | Published role | Suggested use |
|---|---|---|
| **contact@4g-capital.com**; [company contact form](https://www.4g-capital.com/) | General enquiries | Primary company introduction: request Strategy/Product, Credit/Risk and KUZA or UPIA sponsor. |
| [KUZA team form](https://www.4g-capital.com/kuza) | Product and distributor enquiries | A bounded distributor-finance pilot discussion. |
| **Austen.titford@4g-capital.com** | Project-specific CFO enquiry contact, E7 | A focused discussion of the public guarantee project, its reporting needs and research proposal. |
| **ifcfigcatalyticfirstloss@ifc.org** | IFC CFLG programme team, E8 | Programme-level methodological questions or an appropriate introduction; company engagement remains directed to 4G. |

No contact has been made. The addresses above are published on the cited official pages. Use one suitable route with a brief purpose and deck link; ask for the responsible internal team.

## 8. Suggested scoping deliverables

1. Product-to-cash map covering merchant, distributor, field officer, payment provider, lender and guarantor.
2. Reproducible trading-cycle case with settlement timing, owner withdrawals, repayment, residual stock and next-cycle capacity.
3. Bayesian limit/review card with credible intervals, posterior decision probabilities and data-quality flags.
4. Support-intervention protocol with a clear comparator, assignment, outcomes, repeat-cycle horizon and shared-officer/distributor effects.
5. Guarantee eligibility, claim, settlement and recovery ledger reconciled to funding cash.
6. A commercial evaluation of borrower outcomes, additional lending, retained risk, operating costs and sustainable scale.
