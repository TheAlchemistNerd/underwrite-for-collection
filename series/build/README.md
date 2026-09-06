# Draft PDF compilation cycle

This folder contains the repeatable PDF build for the *Underwrite for Collection* MSME series. The current reading edition compiles Parts 1 through 5 without changing the substantive text of accepted earlier manuscripts.

## Build

From the project folder, run:

```powershell
& .\series\build\build_draft_pdf.ps1
```

The default output is written to:

```text
series\dist\Underwrite_for_Collection_MSME_Lifecycle_Draft_Parts_1_to_5_2026-09-06.pdf
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
- Ordinary pages retain the part label, series title, page number and draft date.
- Mermaid flowcharts use `curve: "stepAfter"` so connectors follow straight, orthogonal grid paths rather than curved splines.
- Dense Mermaid diagrams receive full-page scaling while retaining aspect ratio.
- The build cache is stored in the repository-level ignored `scratchpad` area.

This is a draft reading cycle. Later parts can be added to the `$parts` array in `build_draft_pdf.ps1` once their manuscript files are ready.
