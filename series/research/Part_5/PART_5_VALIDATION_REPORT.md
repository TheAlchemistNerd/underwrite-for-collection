# Part 5 Validation Report

## Manuscript

- File: `series/parts/Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md`
- Title: *KESONIA Pricing, Expected Credit Loss, Capital and Funding*
- Status: First complete draft
- Validation date: 6 September 2026

## Scale

| Measure | Target | Actual | Result |
|---|---:|---:|---|
| Full-source words excluding References | 6,186 | 6,186 | Pass, exact target |
| Editorial prose excluding Mermaid and References | At least 5,214 | 5,640 | Pass |
| Mermaid diagrams | 3 large portrait diagrams | 3 | Pass |
| IEEE references | Complete first-use sequence | 17 | Pass |

The word counts follow `WORD_COUNT_AND_QUALITY_GATES.md`. Full-source count includes headings, mathematical exposition, captions and Mermaid labels. Editorial count removes Mermaid source and References.

## Structural checks

- Pandoc Markdown AST parse: pass.
- YAML front matter: complete.
- Numbered body sections: 1 through 11 in order.
- References: begin under one independent References heading.
- Reference entries: each begins as a separate Markdown paragraph.
- First citation appearances: `[1]` through `[17]` in exact ascending order.
- Missing cited entries: none.
- Orphaned reference entries: none.
- Absolute filesystem links: none.
- Control characters: none.
- Em dashes and en dashes: none.

## Quantitative checks

The manuscript contains and defines:

1. A KESONIA compounded factor and annualised rate.
2. The CBK customer lending-rate and total-cost-of-credit identities.
3. An internal `K_RBCP` component bridge that remains subordinate to the approved CBK framework.
4. A physical-measure expected-loss rate with compatible horizon and exposure.
5. Scenario-level net lender cash flow.
6. Probability-weighted discounted IFRS 9 cash-shortfall ECL.
7. Internal economic capital under an explicitly selected risk functional.
8. Product risk-adjusted contribution.
9. A cumulative liquidity-gap ladder.
10. NII and EVE views of IRRBB.
11. A matched-maturity FTP charge.
12. Causal net economic value for an intervention.
13. Gross-to-net loss after a stylised protection layer.
14. Optional tranche-loss allocation for ring-fenced receivables funding.

Each equation was inspected in the final PDF. No equation crosses the text boundary or footer.

## Semantic reconciliations

- KESONIA remains a benchmark rather than a customer-risk estimate.
- `K_RBCP` remains broader than PD, expected loss, capital or FTP.
- New-offer pricing, contractual repricing, limit management and modification are separate events.
- Physical-measure forecasting and market-consistent valuation have separate purposes.
- Pricing expected loss, IFRS 9 ECL, accounting allowance, regulatory capital and internal economic capital are distinct.
- Accounting cure, operational cure, durable cure and re-default remain separately governed.
- A receivable, a payment instruction and settled cash have different liquidity states.
- Bank ALM and FTP remain treasury functions.
- OFSAA is one optional implementation rather than a source of contractual truth.
- Intervention value uses identified incremental outcomes rather than post-treatment association.
- Guarantee, insurance and other protection are modelled through eligibility, coverage, claims, settlement, recoveries and counterparty performance.
- Economic protection, accounting recognition and regulatory-capital recognition remain separate approvals.
- Ring-fenced receivables funding is optional and does not displace the primary bank-balance-sheet architecture.

## Source verification

Primary sources were checked online on 6 September 2026. The final sequence uses:

- Central Bank of Kenya for KESONIA, the Revised RBCPM, prudential guidance and liquidity standards.
- IFRS Foundation for IFRS 9 measurement, modification and write-off requirements.
- Basel Committee on Banking Supervision for expected-loss practice, credit risk, concentration, liquidity, IRRBB and credit-risk mitigation.
- National Treasury and Kenya Law for the Credit Guarantee Scheme.
- Kenya Law for the optional asset-backed-securitisation framework.
- Oracle documentation for the optional OFSAA implementation example.

No live KESONIA observation is hard-coded into the manuscript. This prevents a dated market value from becoming a permanent contractual assumption.

## PDF validation

- Output: `series/dist/Underwrite_for_Collection_MSME_Lifecycle_Draft_Parts_1_to_5_2026-09-06.pdf`
- Pages: 138.
- Page size: US Letter, portrait.
- Part 5 title leaf: physical page 118.
- Part 5 Figure 1: physical page 124.
- Part 5 Figure 2: physical page 131.
- Part 5 Figure 3: physical page 134.
- Part 5 References: physical pages 137 to 138.

All Part 5 pages were rendered to PNG and inspected through a contact sheet. The title leaf, body pages, equations, three full-page diagrams and both reference pages were also checked at normal reading scale. Figure 1 was changed from a shallow horizontal rank to a left-to-right trunk with vertically stacked destinations, which increased label size while preserving every relationship. Figures 2 and 3 retained the large portrait treatment. Connectors are straight and orthogonal. No clipping, overlap, missing glyph, orphaned caption or footer collision was observed.

## Acceptance result

Part 5 satisfies the first-complete-draft gate and the publication-candidate word-count gate. Series-level citation deduplication, Part 6 cross-references and final copy-editing remain future whole-series tasks.

