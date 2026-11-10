from pathlib import Path
import hashlib,json,re
root=Path(r'C:\Users\Nevo\Downloads\behavioural credit scoring - underwrite to collect rct\series\publications\linkedin\2026-10-08_causal_credit_series')
snapshot=root/'build'/'revision_2026-10-16'; snapshot.mkdir(exist_ok=True)
for i in range(1,6):
    p=next(p for p in root.glob(f'ARTICLE_{i}_*.md') if 'LINKEDIN_POST' not in p.name)
    dest=snapshot/p.name
    if not dest.exists(): dest.write_bytes(p.read_bytes())
outline='''# Appendix revision outline and article-fidelity checks

16 October 2026

## 1. Preserve the reading articles

The five main articles retain their prose, displayed equations, examples, research questions and figures. The publication update adds the foundational whitepaper DOI and adjusts citation numbers where necessary. A saved pre-revision copy of every article supports a comparison that excludes only those declared bibliographic changes. Article-body mathematical expressions and Mermaid source blocks are compared exactly.

## 2. Give each derivation a complete home

| Shared material | Complete derivation retained | Later appendix revision | Unique material preserved |
| --- | --- | --- | --- |
| Survival, competing risks and cumulative incidence | A1.7–A1.8; hierarchical hazard likelihood in A2.6 | A2.6 points to the event definitions; A3.9 points to both locations | Cox likelihood, baseline-hazard update, reject-inference event/population/contract/horizon alignment |
| Logistic and hazard hierarchies | A2.5–A2.6 | A3.6 and A5.6 refer to the complete hierarchy | Contract-specific action predictor, numerical pooling example, approved-model output contract |
| Pólya–Gamma augmentation | A2.10 | A3.8 and A5.6 refer to the derivation | A3.8 intercept-only conditional-update check; A5.6 operational artifacts |
| Student-t coefficients and half-t group scales | A2.11 | A3.7 and A5.6 apply the prior-role distinction | Signed coefficient mixture, positive scale mixtures, centered/non-centered updates, separately versioned choices |
| Linear UCB | A1.4 | A2.13 refers to A1.4 | Logistic Thompson sampling and its posterior action choice |
| One-step IPS and doubly robust evaluation | A1.5–A1.6 | A2.15 refers to those proofs | Sequential trajectory estimator, support assumptions and pilot arithmetic |
| Fairness-rate definitions | A1.9 | A2.8 refers to the definitions | Constrained policy, selection-rate ratio, selected-label and weighted diagnostics in A3.14 |
| Expected loss, accounting ECL and capital conventions | A2.7 | A3.12 refers to the common definitions | Conditional EAD/LGD covariance, reject-sensitivity example, twelve-month default/lifetime-shortfall distinction, numerical tail check |
| Bellman recursion and POMDP belief update | A2.2–A2.3 | A4.9–A4.10 refer to the common control derivations | Treasury state/action units, feasible funding and hedge controls, portfolio dependence and paired policy comparison |
| Posterior cap summaries and decision gates | A3.13; distinct risk/effect/cash targets in A5.1 | A5.5 refers to A5.2 and A2.12; A5.7 refers to the earlier summary definitions | Beta calculation, expected-payoff interpretation, Monte Carlo error and release tolerances |

A short formula that defines a new local application can remain. Repeated algebra is replaced by a reference to its complete derivation. Each later subsection states what changes in its own setting.

## 3. Clarify the priors

The baseline has Gaussian fixed-effect coefficients and half-Student-t(3) priors on positive sector, region and vintage standard deviations. A Student-t(3) prior on a signed coefficient is an explicitly chosen alternative. Its latent precision and the group-scale auxiliary variables are recorded separately. Three is the degrees of freedom; the normal–Gamma representation uses Gamma shape and rate 3/2. Conditional Gaussian updates depend on the stated likelihood augmentation and prior choice. The overall posterior retains its latent-variable mixture.

The appendix maps local action-effect symbols to the corresponding main-article symbols without rewriting the article equations. Logistic risk and event hazards retain separate coefficients, group effects and baseline-hazard definitions.

## 4. Rebuild from the same sources

1. Add the Zenodo DOI to each article's whitepaper reference and normalize IEEE references within each article and its appendix.
2. Generate the combined numbered TeX source from the current articles and revised appendices, preserving all named diagrams and chart images.
3. Build the PDF through the existing Pandoc/XeLaTeX workflow.
4. Build the combined Word edition from that same numbered mathematical source, using Word equations derived from TeX, the same content, figures and appendix order.
5. Build the five individual Word articles with Unicode symbols for LinkedIn copying and embedded images.

## 5. Release checks

- Compare the source articles with their pre-revision copies; confirm unchanged prose and mathematics after the declared citation/DOI adjustment.
- Check every cross-reference, equation number, citation and canonical derivation pointer.
- Run the existing numerical checks, including posterior gates, prior mixtures and cash reconciliations.
- Count and verify figure assets in the sources, individual Word files, combined Word and PDF.
- Inspect rendered pages for equation overflow, missing glyphs, chart legibility and page flow.
- Record outputs and verification results; commit only the affected series files after review.

## 6. Separate posting packages

4G Capital and Moniepoint have separate artifact audits. Their article text, Word files, short posts, covers, charts and any existing decks are listed separately so they can be posted without mixing them with the five-article appendix revision.
'''
(root/'APPENDIX_REVISION_OUTLINE_2026-10-16.md').write_text(outline,encoding='utf-8')
# The citation normalizer now performs only the declared DOI update and renumbering.
p=root/'build'/'normalize_citations.py'; s=p.read_text(encoding='utf-8')
a=s.index('def prepare('); b=s.index('\ndef unique(',a)
safe='''def prepare(n,body,refs,appendix):
    doi='https://doi.org/10.5281/zenodo.23343888'
    found=next((k for k,v in refs.items() if doi in v or ('Maloba' in v and 'Underwrite for Collection' in v)),None)
    if found is None:
        found=add_ref(refs,'N. Maloba, *Underwrite for Collection*, integrated research whitepaper, 2026. Zenodo. '+doi+'.')
    elif doi not in refs[found]:
        refs[found]=refs[found].rstrip().rstrip('.')+'. Zenodo: '+doi+'.'
    if found not in ids(body):
        body=body.rstrip()+f'\\n\\nThe foundational whitepaper, *Underwrite for Collection*, is available on Zenodo [{found}].\\n\\n'
    return body,refs,appendix
'''
s=s[:a]+safe+s[b:]
s=s.replace("'date':'2026-10-09'","'date':'2026-10-16'")
p.write_text(s,encoding='utf-8')
# Individual Unicode exports have dynamic figure counts and a separate combined build.
p=root/'build'/'build_word_articles.py';s=p.read_text(encoding='utf-8')
s=s[:s.index('# One uploadable reading document')]
s=s.replace("assert item['diagrams']==[1,2,1,2,1][i-1]","assert item['diagrams']==len(re.findall(r'!\\[',body)), (i,item['diagrams'])")
p.write_text(s,encoding='utf-8')
# Keep A3's sensitivity-specific loss treatment; use the complete A2 definitions.
p=root/'build'/'appendices'/'ARTICLE_3_MATHEMATICAL_APPENDIX.md';s=p.read_text(encoding='utf-8')
a=s.index('For an accounting cash-shortfall calculation,'); b=s.index('The contractual cash flows',a)
s=s[:a]+'Appendix A2.7 defines the probability-weighted discounted cash-shortfall calculation. Here the additional task is to carry selection-sensitive default estimates into the same contract, scenario and recovery definitions.\n\n'+s[b:]
a=s.index('An economic-capital convention may instead use');b=s.index('For a single stylised loan',a)
s=s[:a]+'The quantile-based economic-capital convention is defined in Appendix A2.7. Applying it to the selected-label example gives a direct numerical comparison between mean and tail loss.\n\n'+s[b:]
s=s.replace('P\ufffdlya','Pólya')
s=s.replace('## A3.7','The local action-effect symbol $g^L$ represents the fixed-horizon response denoted $h^L$ in the article body; $g^H$ represents its hazard response $q^H$. These model-specific labels preserve separate logistic and survival estimands.\n\n## A3.7',1)
p.write_text(s,encoding='utf-8')
print('Saved article baseline, structured outline, safe DOI normalizer, Unicode builder update and scoped A3 revision.')
