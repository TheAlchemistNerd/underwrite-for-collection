# White paper compilation cycle

This folder contains the repeatable PDF build for the *Underwrite for Collection* MSME research white paper. The 4 October 2026 acknowledgement edition compiles the six active manuscripts, the operating/finance and governed-evidence appendices, and a final acknowledgements page. The 1 October 2026 PDF remains preserved as the earlier edition. Labelled case exhibits are part of the current manuscripts.

## Build

From the project folder, run:

```powershell
& .\series\build\build_whitepaper_pdf.ps1
```

The default output is written to:

```text
series\dist\Underwrite_for_Collection_MSME_Credit_Lifecycle_Whitepaper.pdf
```

An alternative file name can be supplied with `-OutputName`; directory components are rejected so every build remains inside `series\dist`.

## Inputs and build components

- `series\parts\Part_1_MSME_Credit_Lifecycle_and_Collection_Cascades.md`
- `series\parts\Part_2a_Temporal_Evidence_and_Feature_Engineering.md`
- `series\parts\Part_2b_Hierarchical_Bayesian_Underwriting_Causal_Identification_and_Lifecycle_Dependence.md`
- `series\parts\Part_3_Regulatory_Orchestration_Fair_Intervention_and_Collection_Governance.md`
- `series\parts\Part_4_Bank_Controlled_Research_Sandboxes_and_Enterprise_Credit_Architecture.md`
- `series\parts\Part_5_KESONIA_Pricing_Expected_Credit_Loss_Capital_and_Funding.md`
- `series\build\corporate.yaml`
- `series\build\whitepaper-header.tex`
- `series\build\mermaid.lua`

The cycle uses Pandoc and XeLaTeX for document composition. Mermaid diagrams are rendered through Mermaid CLI and Chromium using the same general corporate compilation approach as the Mwendo Pamoja white paper.

The Part 1 matched-population chart panel is reproducible from its cited values. Regenerate it before compilation when the source data or design changes:

```powershell
python .\series\scripts\generate_part1_population_charts.py
```

## Layout contract

- The cover has no running header or footer.
- Each part begins on a dedicated title leaf.
- The contents use Roman page numbers; the manuscripts use Arabic page numbers.
- References begin on a new page for each part.
- Ordinary pages retain the part label, series title, page number and research-edition date.
- Mermaid flowcharts use `curve: "stepAfter"` so connectors follow straight, orthogonal grid paths rather than curved splines.
- Dense Mermaid diagrams receive full-page scaling while retaining aspect ratio.
- The build cache is stored in the repository-level ignored `scratchpad` area.

This is the canonical integrated build of the current five-part research programme. Any future manuscript extensions can be added to the `$parts` array in `build_whitepaper_pdf.ps1` through a separately reviewed edition.


## Worked case and HTML edition

Before publication, run:

```powershell
python -m unittest discover -s research_lab -p 'test_*.py' -v
python research_lab/run_decision_case.py --write-appendix
python research_lab/run_cases.py
python research_lab/run_cases.py --check
python series/build/build_whitepaper_html.py
$env:PUPPETEER_EXECUTABLE_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
& .\series\build\build_whitepaper_pdf.ps1
```

The appendix inputs are `series/appendices/WORKED_OPERATING_AND_FINANCE_CASE.md` and `series/appendices/GOVERNED_EVIDENCE_AND_INTERVENTION_CASE.md`; the current integrated build also includes `series/appendices/ACKNOWLEDGEMENTS_AND_LINKEDIN_INPUTS_2026-10-04.md`. `-AssembleOnly` writes the assembled Markdown without invoking the PDF compiler. HTML builds use the same six chapters, both worked-case appendices and the acknowledgements, embed diagrams and render equations as MathML, and write a dated 4 October master HTML plus two standalone case HTML files in `series/dist`. The PDF uses the established corporate layout. Historical dated editions remain separate. The case generator is guarded by a published-input fingerprint so changed assumptions cannot silently accompany unchanged baseline prose.

The default PDF output is `series/dist/Underwrite_for_Collection_MSME_Credit_Lifecycle_Whitepaper.pdf`; rebuilding replaces that same filename. Both case appendices and all six manuscript exhibits link to the public GitHub `research_lab`. Edit the narrative templates in the lab and regenerate to keep every published case record aligned.
