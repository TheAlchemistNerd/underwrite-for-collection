# Part 5 Source and Claim Ledger

## Status key

- **Fact:** direct statement from a cited primary source.
- **Definition:** controlled meaning used by this series.
- **Method:** proposed quantitative or operating method.
- **Recommendation:** implementation choice requiring institutional approval.
- **Diligence:** contractual, legal, accounting or regulatory conclusion requiring responsible professional review.

## Claim ledger

| ID | Planned claim | Status | Principal authority | Drafting control |
|---|---|---|---|---|
| P5-C01 | KESONIA is a transaction-based, volume-weighted overnight unsecured KES interbank benchmark administered and published by CBK. | Fact | CBK KESONIA page and FAQ | Preserve publication and value-date distinction. |
| P5-C02 | The revised RBCPM expresses the total lending rate as KESONIA plus premium `K`, with fees and charges added for total cost of credit. | Fact | CBK Revised RBCPM; CBK Apr. 2026 MPC Report | Use `K_RBCP` in the paper to avoid collision with capital notation. |
| P5-C03 | `K_RBCP` includes lending-related costs, shareholder return and borrower risk. | Fact | CBK Revised RBCPM | Do not reduce it to PD or expected loss. |
| P5-C04 | A compounded-in-arrears contract requires an explicit calendar, observation, day-count, fallback and correction convention. | Method | CBK KESONIA FAQ; local KESONIA engineering corpus | Present formula as implementation specification, not universal contract wording. |
| P5-C05 | HLR outputs are physical-measure prognostic evidence that can feed approved pricing, impairment and capital processes. | Definition and method | Parts 2b and 4; IFRS 9; BCBS ECL guidance | Preserve separate transformation, calibration and approval. |
| P5-C06 | IFRS 9 ECL is a probability-weighted discounted cash-shortfall measure using reasonable and supportable information. | Fact | IFRS 9 paras. 5.5 and B5.5 | Keep 12-month ECL meaning precise. |
| P5-C07 | A model score or observed intervention does not itself determine stage, accounting modification or write-off. | Method and governance | IFRS 9; Part 4 enterprise contract | Assign decisions to approved accounting policy and owner. |
| P5-C08 | Credit enhancements enter ECL only according to the applicable contractual and accounting conditions. | Fact and diligence | IFRS 9 impairment material | Separate economic recovery from accounting recognition. |
| P5-C09 | Regulatory capital, accounting allowance and internal economic capital answer different questions. | Definition | CBK Prudential Guidelines; Basel Framework | Avoid claims of automatic capital relief. |
| P5-C10 | Internal economic capital should capture portfolio tail loss, concentration and model uncertainty at a stated horizon and confidence standard. | Method | BCBS credit-risk and concentration principles | Describe VaR and expected shortfall as governed alternatives. |
| P5-C11 | Collection timing, settlement, cure and recovery lag affect liquidity even when expected ultimate loss is unchanged. | Method | BCBS liquidity principles; local collection corpus | Distinguish asset value from cash availability. |
| P5-C12 | Bank ALM and FTP use contractual and behavioural cash flows, repricing and liquidity attributes. | Fact and method | BCBS IRRBB and liquidity guidance | Keep treasury ownership visible. |
| P5-C13 | OFSAA ALM and FTP can operationalise instrument cash flows and matched-maturity attribution. | Fact | Oracle official documentation | Present as optional implementation. |
| P5-C14 | Intervention value includes incremental durable collection, treatment cost, funding, conduct effects and capital usage. | Method | Parts 3 and 4; experimental standard | Use causal estimates only where assignment supports them. |
| P5-C15 | Kenya's Credit Guarantee Scheme shares part of qualifying MSME credit risk through participating financial intermediaries. | Fact | PFM CGS Regulations; National Treasury CGS | Avoid importing historic coverage percentages into every facility. |
| P5-C16 | Guarantee economics require coverage, attachment, exclusions, waiting period, claims timing, recoveries and counterparty performance. | Method | CGS terms; Basel CRM principles | Model gross and net cash separately. |
| P5-C17 | Prudential recognition of guarantees requires applicable legal and operational conditions. | Fact and diligence | Basel CRE22; CBK framework | State that the participating bank and supervisor determine recognition. |
| P5-C18 | An optional securitisation can transfer eligible cash-flow assets to a ring-fenced vehicle under Kenyan capital-markets law. | Fact and diligence | Kenya Capital Markets Act; ABS Regulations | Present as optional funding extension and preserve true-sale diligence. |
| P5-C19 | SPV asset yield, note margin, investor hurdle and bank FTP are separate quantities. | Definition | Canonical notation register; local structural-finance corpus | Use `m_fund` for a note or funding margin. |
| P5-C20 | Part 5 hands Part 6 testable financial outcomes rather than assumed balance-sheet benefits. | Method | Series charter and Part 6 brief | Require empirical or controlled synthetic validation. |

## Primary online authorities reviewed on 6 September 2026

1. Central Bank of Kenya, KESONIA portal and FAQ.
2. Central Bank of Kenya, Revised Risk-Based Credit Pricing Model, Aug. 2025.
3. Central Bank of Kenya, Monetary Policy Committee Report, Apr. 2026.
4. IFRS Foundation, IFRS 9 Financial Instruments and impairment supporting material.
5. Basel Committee on Banking Supervision, Expected credit losses.
6. Central Bank of Kenya, Prudential Guidelines, including capital adequacy and asset classification/provisioning.
7. Basel Committee on Banking Supervision, Principles for the Management of Credit Risk, Apr. 2025.
8. Basel Framework, IRRBB, liquidity-risk and credit-risk-mitigation modules.
9. National Treasury and Kenya Law, Credit Guarantee Scheme materials.
10. Kenya Law, Capital Markets Act and Asset-Backed Securities Regulations.
11. Oracle, official ALM, cash-flow-engine and FTP documentation.

## Local material incorporated

- `UNDERWRITE_FOR_COLLECTION.md` and its side-by-side semantic analysis.
- `IN_THE_SPIRIT_OF_UNDERWRITING_TO_COLLECT_ROUGH_RESEARCH.md`.
- KBA canonical research specification, data dictionary and source-extraction ledger.
- KESONIA reform, compounding, ERP, IFRS 9, ALM and FTP research notes.
- Mwendo Pamoja Part 5 as a structural comparator.
- Parts 1 to 4 of the current MSME series and the canonical definitions register.

## Evidence boundaries

- Public KESONIA and product-rate data can measure pricing transmission. They cannot establish account-level collectability without matured facility histories.
- IFRS 9 permits methods that satisfy its principles; the paper proposes an architecture and leaves accounting approval with the reporting entity.
- Basel materials provide international standards and methods. Kenyan regulatory recognition follows the applicable CBK framework and supervisory decision.
- A guarantee, insurance contract or SPV changes net economics only through enforceable coverage, cash settlement and allocated rights.
- Improvements in discrimination or calibration become financial benefits only after implementation, causal, accounting, treasury and capital controls accept the relevant evidence.

