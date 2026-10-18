# 4G Capital x Underwrite for Collection

The article, Word document, companion LinkedIn post, 22-slide pitch deck, six charts and merchant-finance case are maintained in the Underwrite for Collection repository.

Repository: https://github.com/TheAlchemistNerd/underwrite-for-collection

Unzip the package and run from its root:

```powershell
python -B research_lab/four_g_merchant_finance_case/run_case.py
python -B -m unittest discover -s research_lab/four_g_merchant_finance_case -p test_model.py -v
python -B research_lab/partner_case_visuals/build_four_g_case_charts.py
```

The model uses Python standard-library functions. Chart generation additionally uses Pillow and Arial. The case follows twelve synthetic merchants through seven scenarios, with protected and unprotected lender ledgers. All 24 tests passed after repository relocation.

The article and deck retain their approved 18 October economic results and visual layout. Earlier release links to the Mwendo research-lab folder lead to a location note for this owning repository.

The article source used by the reproducible Word builder is stored in research_lab/partner_case_visuals/inputs/FOUR_G_ARTICLE_SOURCE.md. The model's own assumptions.json controls its numerical inputs.

Licence: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International. https://creativecommons.org/licenses/by-nc-sa/4.0/
