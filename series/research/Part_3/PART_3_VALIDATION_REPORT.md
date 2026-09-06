# Part 3 Validation Report

## Scope

This report validates:

- The Part 3 regulatory orchestration, fair intervention and collection-governance manuscript.
- The Parts 1, 2a, 2b and 3 PDF reading edition.
- The Part 3 detailed outline and source-and-claim ledger.
- The corrected series title, licence attribution and PDF metadata.

Validation date: 6 September 2026.

## Length and structure

| Test | Result | Status |
|---|---:|---|
| Full source words excluding References | 4,981 | Pass |
| Full-source benchmark | 4,872 | Within 2.2 percent |
| Editorial words excluding References, YAML and Mermaid source | 4,585 | Pass |
| Editorial benchmark | 4,781 | Within 4.1 percent |
| Numbered main sections | 9 | Pass |
| Full-page Mermaid figures | 3 | Pass |
| Figure captions | 3 | Pass |
| Pandoc table nodes | 1 | Pass |
| Display-math opening and closing delimiters | 9 and 9 | Pass |

The manuscript progresses from a relatable payment-timing mismatch through the four decision objects, intervention contract, graduated treatment library, Credit Policy and Compliance Gate, Kenya-first regulatory controls, explanation and fairness, experimental governance, portfolio escalation and conclusion.

## Governance and mathematical acceptance checks

- Model inference, causal evidence, policy eligibility and customer treatment remain separate.
- The intervention contract specifies population, exclusions, mechanism, owner, cost bearer, channel, horizon, outcomes, stop rule and review path.
- Collection effectiveness includes discounted cash, durable cure, re-default, intervention and recovery cost, complaints, contact burden and business continuity.
- The action set is the intersection of legal, contractual, conduct, affordability, operational and portfolio constraints.
- The constrained value function reports cash, cost, customer-harm and continuity components before scalar ranking.
- Posterior uncertainty, support-range failure and data-quality failure route to a substantive human-review process.
- Significant solely automated decisions are analysed at decision level under section 35 of the Data Protection Act and the General Regulations.
- Consent is presented as one possible lawful basis, not a universal basis for lifecycle processing.
- Credit-bureau adverse-action requirements remain tied to bureau information.
- The four-fifths rule and equalized odds are not presented as Kenyan legal standards.
- Fairness monitoring covers calibration, errors, access, intervention receipt, contact, complaints, cure, re-default and recovery.
- Randomisation occurs only among permissible alternatives after mandatory protections and exclusions.
- The doubly robust policy-value estimator is accompanied by overlap, timing, treatment-definition and logging conditions.
- Quasi-experimental claims are limited by their assignment mechanisms and identification assumptions.
- Behavioural patterns are not translated into borrower intent or character labels.
- Statistical drift metrics trigger diagnosis rather than automatic declarations of regulatory breach.

## Research and citation checks

| Test | Result | Status |
|---|---:|---|
| Distinct in-text IEEE numbers | 14 | Pass |
| Reference entries | 14 | Pass |
| First-appearance order | 1 through 14 without reversal | Pass |
| Orphan references | 0 | Pass |
| Missing reference numbers | 0 | Pass |
| Reference page break | Present | Pass |
| Long dashes | 0 | Pass |
| Unicode replacement characters | 0 | Pass |

The Kenyan control architecture uses primary Kenya Law, Central Bank of Kenya and Office of the Data Protection Commissioner materials. The experimental and computational sections use the primary NBER paper on the Kenyan performance-contingent finance experiment, the American Economic Review grace-period experiment, the original ICML doubly robust policy-evaluation paper and peer-reviewed fairness research. NIST AI RMF 1.0 is labelled as a voluntary international comparator.

## Diagram and compilation checks

- All three Part 3 Mermaid figures use top-to-bottom flow and orthogonal `stepAfter` routing.
- All figures use the same scale-3 Mermaid rendering chain and full-page portrait layout as the accepted Parts 2a and 2b figures.
- The source PNGs are high resolution. The three new render sizes are 1,398 by 4,839 pixels, 1,695 by 3,378 pixels and 1,083 by 4,302 pixels.
- Figure 1 preserves the inference, causal, policy, action and learning cycle.
- Figure 2 shows forward escalation and return-to-health paths without curved connectors.
- Figure 3 shows the gate, exception route, human review and decision record.
- The intervention table is a native Pandoc table and fits within the text area.
- All nine display equations render without clipping or unresolved glyphs.
- References begin on a new page and every reference entry begins a new paragraph.

## PDF and visual QA

Final PDF:

`series/dist/Underwrite_for_Collection_MSME_Lifecycle_Draft_Parts_1_to_3_2026-09-06.pdf`

| Property | Result |
|---|---|
| Pages | 99 |
| File size | 4,952,556 bytes |
| PDF SHA-256 | `EDC9783BBA6B7A70E9C9B5587D6CE53054A27B6F5DDB617A7370934D14B9A0DC` |
| Part 3 source SHA-256 | `171A656DB7645209A46C5C90BB235AC2C2C1E48328F2B9D76AAC13BE3E8FCCDA` |
| PDF title metadata | Underwrite for Collection: A Proposed Architecture for an MSME Credit LifeCycle System |
| PDF author metadata | Neville Maloba |
| Cover contact | nevillemaloba@gmail.com |
| Licence leaf | CC BY 4.0, including commercial reuse with attribution |

All 99 pages were rendered through Poppler. The cover, licence leaf, contents and all Part 3 pages were inspected through contact sheets. Full-size review covered the Part 3 title leaf, Figures 1 through 3, the intervention table, gate and review equations, conclusion, and both reference pages. No clipping, footer collision, missing glyph, diagram-caption separation, malformed table, local filesystem link or unrendered Mermaid source was observed.

## Title correction

The cover, PDF metadata and suggested licence attribution now use:

> **A Proposed Architecture for an MSME Credit LifeCycle System**

The earlier phrase “Architecture of MSME” is absent from the compiled PDF.

## Result

Part 3 passes the first-draft narrative, regulatory, mathematical, causal, citation, diagram and PDF-rendering gates. It is suitable for sequential review before Part 4 drafting begins.
