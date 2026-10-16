# Publication release verification - 16 October 2026

The current combined PDF has 136 pages, 269 numbered display equations and 12 figures. The combined Word edition contains the same articles, mathematical appendices, numbered equations and figures, constructed from the same TeX mathematical source; its native Word pagination is 149 pages. The five individual Word articles retain Unicode mathematics for LinkedIn copying. DOI references and article-local citation sequences are updated.

The appendix revision preserves the main article bodies apart from the declared DOI and citation additions. Complete derivations have canonical locations, later applications retain their distinct calculations, and the coefficient Student-t and positive group-scale half-t priors are separated. All 37 current mathematical checks passed. The final TeX log has no missing-glyph, unresolved-reference or overfull-box diagnostics.

See [current checks](build/publication_release_checks_2026-10-16.json), [body-fidelity comparison](build/article_fidelity_checks_2026-10-16.json), [equation/link checks](build/pdf_numbering_validation.json) and [posting pack](00_POSTING_PACK.md). The Word contents page and equation-register pagination were finalized and visually verified. The PNG download contains all twelve figures.

## Historical verification record

The following 10 October record describes its earlier build. Current counts and formats are above.

# Publication release verification — 10 October 2026

The five individual Word files and combined Word edition were rendered through Microsoft Word and visually inspected. All six use ordinary Unicode mathematics, contain no Word equation objects, and embed the seven named diagrams across the series. The combined Word edition is 67 pages; the TeX PDF is 136 pages. The final TeX log contains no missing-character, overfull-box or undefined-command errors.

The final PDF and Word page renders were checked for clipping, overlap and incomplete diagrams. Article 2 retains its extended discussion and adds Student-t scale priors, computational updates, Bayesian limit boundaries and uncertainty for human review.

The PDF contains five mathematical appendices, one after each article. The logistic and survival hierarchies include group distributions and hyperpriors. Citation numbering follows first appearance within each article and its appendix, with 19, 25, 20, 13 and 10 references respectively. Numerical checks include 50 worked-example checks and 37 mathematical identity checks.

Displayed equations are numbered by article and appendix: 309 blocks, with an equation register and 760 validated internal PDF links. Every equation number is present in the PDF and all equation TeX is preserved from the numbered source. Final page-content comparison found only page 48 changed after the preceding full review; that page was freshly rendered and reviewed. The Word editions retain Unicode text and embedded diagrams.

The general financing proposition is ring-fenced receivables; SPV identifies the vehicle chosen in particular worked examples. Article headers no longer say Draft for review. The requirements post includes CRISP-DM, data-engineering pipelines, Power BI and Tableau.

## LinkedIn post character counts

Counts include LF line breaks and exclude a trailing newline where none is present. Replacing the Zenodo placeholder changes the count.

- `ARTICLE_1_LINKEDIN_POST.md`: 1,487
- `ARTICLE_2_LINKEDIN_POST.md`: 1,726
- `ARTICLE_3_LINKEDIN_POST.md`: 1,554
- `ARTICLE_4_LINKEDIN_POST.md`: 1,909
- `ARTICLE_5_LINKEDIN_POST.md`: 1,764
- `UNDERWRITE_FOR_COLLECTION_LINKEDIN_POST_2026-10-08.md`: 2,000
- `UNDERWRITE_FOR_COLLECTION_MASTER_WHITEPAPER_LINKEDIN_POST_2000_CHARACTERS.md`: 2,000
- `REQUIREMENTS_AND_SPECIFICATIONS_LINKEDIN_POST_2000_CHARACTERS.md`: 2,000

`SHA256SUMS.json` records the exact released files.
