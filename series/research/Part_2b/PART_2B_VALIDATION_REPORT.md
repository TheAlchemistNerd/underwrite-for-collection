# Part 2b Validation Report

## Scope

This report validates:

- The Part 2b hierarchical Bayesian underwriting manuscript.
- The Parts 1, 2a and 2b PDF reading edition.
- The Part 2b source and claim ledger.
- The CC BY 4.0 publication and reuse page in the PDF build chain.

Validation date: 6 September 2026.

## Length and structure

| Test | Result | Status |
|---|---:|---|
| Full source words excluding References | 10,333 | Pass |
| Full-source benchmark | 10,166 | Within 1.7 percent |
| Editorial words excluding References, YAML and Mermaid source | 9,559 | Pass |
| Editorial benchmark | 9,681 | Within 1.3 percent |
| Numbered main sections | 12 | Pass |
| Conclusion | Present | Pass |
| Appendices | 3 | Pass |
| Full-page Mermaid figures | 5 | Pass |
| Figure captions | 5 | Pass |
| Display-math opening and closing delimiters | 43 and 43 | Pass |

The main sections progress from the decision question and observation contract through the champion HLR, governed nonlinearities, residual AI evidence, offline inference, causal identification, timing challengers, collectible cash, dependence, policy and validation. The appendices retain B-spline with RW1 and AR(1) alternatives, the blocked Pólya-Gamma computation, and the causal design register.

## Statistical acceptance checks

- The champion remains a hierarchical Bayesian logistic regression.
- Product, sector, geography, institution, vintage and calendar effects retain partial pooling.
- P-splines are the primary nonlinear specification.
- B-spline plus RW1 and B-spline plus AR(1) alternatives remain reproducible challengers in Appendix A.
- Neural sequence representations are identified as artificial-intelligence evidence and are cross-fitted, residualised against the explicit design, optionally whitened within their own block, and regularised with a finite-slab horseshoe.
- Pólya-Gamma augmentation applies to the complete HLR as an offline conditional-conjugacy strategy.
- The production path consumes a signed posterior artefact and does not perform MCMC during an underwriting request.
- The timing challenger handles right censoring through a hierarchical piecewise-exponential formulation.
- The multi-state challenger distinguishes arrears, modification, cure, durable cure, re-default, default, recovery and closure.
- Prediction, causal intervention effects and policy value are separately defined.
- RCT, regression discontinuity, difference-in-differences, synthetic-control, target-trial, heterogeneous-effect and policy-learning routes state their principal identification conditions.
- PD, EAD, cure, prepayment, LGD, recovery amount, recovery delay and workout cost remain separate.
- Residual copula dependence is introduced only after calibrated marginals and observed common factors.

## Citation and language checks

| Test | Result | Status |
|---|---:|---|
| Distinct in-text IEEE numbers | 29 | Pass |
| Reference entries | 29 | Pass |
| First-appearance order | 1 through 29 without reversal | Pass |
| Orphan references | 0 | Pass |
| Missing reference numbers | 0 | Pass |
| Reference page break | Present | Pass |
| Long dashes | 0 | Pass |
| Unicode replacement characters | 0 | Pass |

Sources were selected through the part-specific source and claim ledger. The body uses primary methodological publications, Kenyan field evidence, an international repayment-flexibility comparator and official Central Bank of Kenya supervision material. Claims are limited to the use approved in the ledger.

## Parse and compilation checks

- Pandoc parsed the manuscript to a JSON abstract syntax tree successfully.
- XeLaTeX compiled the complete edition successfully after correcting the inline copula delimiter identified by the first render.
- All five Part 2b Mermaid figures rendered at scale 3 through the established filter.
- Figures use top-to-bottom flow and orthogonal step routing.
- Figure 2 was converted from a compressed horizontal fan into a tall champion-model flow.
- Figure 4 was converted into a legible prediction, causal-design and policy sequence.
- Figure 5 was converted into a vertical lifecycle and recovery path with larger boxes.
- The causal estimand table fits within the text area.
- References begin on a separate page and each entry begins a separate paragraph.

## PDF and visual QA

Final PDF:

series/dist/Underwrite_for_Collection_MSME_Lifecycle_Draft_Parts_1_2a_and_2b_2026-09-06.pdf

| Property | Result |
|---|---|
| Pages | 81 |
| File size | 4,004,648 bytes |
| PDF SHA-256 | 026FEC0B3B10234FD8CB78FE3FB33E4680857B15E59277D0C30A9301E346D399 |
| Part 2b source SHA-256 | 8FDA42A8D067E69E106B15408616F7AC31B10C67928D42BE28F6763E7649C5D7 |
| Cover metadata | Neville Maloba and nevillemaloba@gmail.com |
| Licence leaf | CC BY 4.0, including commercial reuse with attribution |

All 81 pages were rendered with Poppler. The full contact sheets were inspected, followed by full-size inspection of the licence page, the Part 2b part-title page, Figures 1 through 5, the conclusion, appendices, causal-design table and every reference page. No clipping, footer collision, unresolved mathematical glyph, broken link text or diagram-caption separation was observed.

## File-operation check

The root all_md_files_combined.md file is absent, as requested. No additional source file was deleted during this work.

## Result

Part 2b passes the first-draft word-count, mathematical, computational, causal, citation, diagram and PDF-rendering gates. The edition is suitable for sequential review before Part 3 drafting begins.
