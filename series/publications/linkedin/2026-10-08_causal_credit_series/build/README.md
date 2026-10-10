# Rebuild the publication editions

Run from the release folder on Windows. Dependencies: Python with python-docx, lxml, Pillow and pypdf; Pandoc; MiKTeX/XeLaTeX; Mermaid CLI (`mmdc`); and the Calibri, Segoe UI and Cambria Math fonts. Configure `puppeteer.json` for the installed browser if regenerating diagrams.

```powershell
python build/build_word_articles.py
powershell -NoProfile -File build/build_combined_pdf.ps1 -PythonExecutable python
python build/check_publication.py
python build/normalize_citations.py --check
python build/mathematical_audit_checks.py
```

The Word builder preserves mathematical expressions as ordinary Unicode text. The PDF builder creates a separate TeX-ready intermediate through `typeset_math.py`, leaving the article sources unchanged. `mermaid.lua` renders named PNG/SVG files when their Mermaid definitions change; unchanged supplied assets are reused.

Final editions are in `publications/`; editable diagrams are in `linkedin_diagrams/`. Inspect the rebuilt files visually before publication. Generated intermediates in this build directory can be reproduced from the committed sources.

The five editable mathematical appendices are in `appendices/`. The PDF builder inserts each appendix after its corresponding article and uses `publication-header.tex` for layout. Appendix citations share the article's numbered bibliography. The Word editions retain the article bodies and Unicode formulations.

`number_equations.py` numbers displayed blocks by article and appendix, adds linked cross-references and produces `EQUATION_REGISTER.md`. The PDF build runs three TeX passes to resolve the linked page references. Short inline expressions remain unnumbered; an aligned derivation receives one number for the whole block. The Word editions preserve ordinary Unicode mathematics for LinkedIn.
