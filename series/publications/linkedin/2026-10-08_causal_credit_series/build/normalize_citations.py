"""Normalize article-local IEEE citations; appendices share the article bibliography.

Run once to apply, then use --check to validate without editing. Mathematical
indices, fenced diagrams, inline TeX and displayed TeX are excluded.
"""
from pathlib import Path
import re, json, hashlib, sys

ROOT = Path(__file__).resolve().parent.parent
REFHEAD = re.compile(r'^### References\s*$', re.M)
ENTRY = re.compile(r'^\[(\d+)\] (.+)$', re.M)
CITE = re.compile(r'(?<![\w/])\[(\d+)\](?:\s*[–−-]\s*\[(\d+)\])?(?!\()')
PROTECTED = re.compile(r'```[\s\S]*?```|\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^\n$]*\$|`[^`\n]+`')
BDA = 'A. Gelman, J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, and D. B. Rubin, *Bayesian Data Analysis*, 3rd ed. Boca Raton, FL, USA: CRC Press, 2013, chs. 2, 5 and 9. Author resources: https://sites.stat.columbia.edu/gelman/book/.'
HALFT = 'A. Gelman, “Prior distributions for variance parameters in hierarchical models,” *Bayesian Analysis*, vol. 1, no. 3, pp. 515–534, 2006, doi: 10.1214/06-BA117A. Available: https://www.stat.columbia.edu/~gelman/research/published/taumain.pdf.'
WAND = 'M. P. Wand, J. T. Ormerod, S. A. Padoan, and R. Frühwirth, “Mean field variational Bayes for elaborate distributions,” *Bayesian Analysis*, vol. 6, no. 4, pp. 847–900, 2011, doi: 10.1214/11-BA631, Result 5. Author copy: https://matt-p-wand.net/publicns/Wand11.pdf.'
COX = 'D. R. Cox, “Regression models and life-tables,” *Journal of the Royal Statistical Society: Series B*, vol. 34, no. 2, pp. 187–220, 1972. Available: https://web.stanford.edu/~lutian/coursepdf/cox1972paper.pdf.'
POMDP = 'L. P. Kaelbling, M. L. Littman, and A. R. Cassandra, “Planning and acting in partially observable stochastic domains,” *Artificial Intelligence*, vol. 101, nos. 1–2, pp. 99–134, 1998, doi: 10.1016/S0004-3702(98)00023-X. Author copy: https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf.'
WILSON = 'E. B. Wilson, “Probable inference, the law of succession, and statistical inference,” *Journal of the American Statistical Association*, vol. 22, no. 158, pp. 209–212, 1927, doi: 10.1080/01621459.1927.10502953.'
EHRHARDT = 'A. Ehrhardt, C. Biernacki, V. Vandewalle, P. Heinrich, and S. Beben, “Reject inference methods in credit scoring,” *Journal of Applied Statistics*, vol. 48, nos. 13–15, pp. 2734–2754, 2021, doi: 10.1080/02664763.2021.1929090. Available: https://pmc.ncbi.nlm.nih.gov/articles/PMC9041715/.'
LAKKARAJU = 'H. Lakkaraju, J. Kleinberg, J. Leskovec, J. Ludwig, and S. Mullainathan, “The selective labels problem: Evaluating algorithmic predictions in the presence of unobservables,” in *Proc. 23rd ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining*, 2017, pp. 275–284, doi: 10.1145/3097983.3098066. Author copy: https://www.cs.cornell.edu/home/kleinber/kdd17-selective.pdf.'

def split_article(text):
    h = REFHEAD.search(text)
    assert h, 'No References heading'
    matches = list(ENTRY.finditer(text[h.end():]))
    assert matches
    refs = {int(m[1]):m[2] for m in matches}
    assert len(refs) == len(matches), 'Duplicate reference IDs'
    end = h.end() + matches[-1].end()
    return text[:h.start()], refs, text[end:]

def plain_chunks(text):
    last = 0
    for m in PROTECTED.finditer(text):
        yield False,text[last:m.start()]
        yield True,m[0]
        last = m.end()
    yield False,text[last:]

def ids(text):
    result=[]
    for protected,chunk in plain_chunks(text):
        if protected: continue
        for m in CITE.finditer(chunk):
            a=int(m[1]); b=int(m[2]) if m[2] else a
            assert b>=a, ('Descending old citation range',m[0])
            result.extend(range(a,b+1))
    return result

def remap(text,mapping):
    def sub(m):
        a=int(m[1]);b=int(m[2]) if m[2] else a
        return ', '.join(f'[{mapping[k]}]' for k in sorted(range(a,b+1),key=lambda k:mapping[k]))
    def cluster(m):
        return ', '.join(f'[{k}]' for k in sorted(set(map(int,re.findall(r'\d+',m[0])))))
    return ''.join(chunk if protected else re.sub(r'\[\d+\](?:,\s*\[\d+\])+',cluster,CITE.sub(sub,chunk)) for protected,chunk in plain_chunks(text))

def add_ref(refs,value):
    for n,v in refs.items():
        if v==value:return n
    n=max(refs)+1; refs[n]=value;return n

def append_cite_to_paragraph(body,start,numbers):
    # Exact paragraph prefix makes additions independent of concurrent math edits.
    pat=re.compile(re.escape(start)+r'[^\n]*(?:\n(?!\s*\n)[^\n]+)*')
    m=pat.search(body)
    assert m, ('Missing paragraph',start)
    p=m[0].rstrip(); suffix=' '+', '.join(f'[{n}]' for n in numbers)+'.'
    if p.endswith('.'):p=p[:-1]
    return body[:m.start()]+p+suffix+body[m.end():]

def support(appendix,section,text):
    pat=re.compile(r'(^## '+re.escape(section)+r'[^\n]*\n)',re.M)
    assert pat.search(appendix),section
    return pat.sub(lambda m:m[0]+'\n'+text+'\n',appendix,count=1)

def prepare(n,body,refs,appendix):
    for k,v in list(refs.items()):
        if 'PMC9041715' in v:refs[k]=EHRHARDT
        if 'Lakkaraju' in v:refs[k]=LAKKARAJU
        if 'A. C. Clayton' in v:refs[k]=v.replace('A. C. Clayton','D. G. Clayton')+' doi: 10.1093/biomet/65.1.141.'
        if 'Y. Jiang and L. Li' in v:refs[k]=v.replace('Y. Jiang','N. Jiang')
    if n==1:
        cox=add_ref(refs,COX)
        body=append_cite_to_paragraph(body,'Survival analysis helps represent',[cox])
        body=append_cite_to_paragraph(body,'The Kenyan legal framework',[16]) if 'The Kenyan legal framework' in body else body
        appendix=support(appendix,'A1.3','The credit experiment separates assigned offers and subsequent behaviour using the experimental-design logic in [4].')
        appendix=support(appendix,'A1.4','The linear confidence-bound construction follows [5]; inference under adaptive assignment follows [6].')
        appendix=support(appendix,'A1.5','The evaluation setting and overlap requirements follow [1], [9].')
        appendix=support(appendix,'A1.6','The augmented estimator follows the doubly robust policy-evaluation construction in [1].')
        appendix=support(appendix,'A1.8',f'The hazard specification follows [{cox}], with competing-risk and transition distinctions supported by [17], [18].')
        appendix=support(appendix,'A1.9','The conditional fairness rates follow [10].')
    if n==2:
        bda=add_ref(refs,BDA);wand=add_ref(refs,WAND);cox=add_ref(refs,COX);pomdp=add_ref(refs,POMDP)
        body=append_cite_to_paragraph(body,'A credit-limit adjustment is a decision',[bda])
        body=append_cite_to_paragraph(body,'These scale variables and the Pólya',[wand])
        # In the appendix, early citations support each derivation directly.
        for sec,txt in [('A2.2',f'The finite-horizon value recursion is the fully observed special case of the control formulation in [{pomdp}].'),('A2.3',f'The belief-state construction and observation update follow [{pomdp}].'),('A2.5',f'The hierarchical posterior and partial-pooling construction follow [{bda}, ch. 5].'),('A2.6',f'The proportional-hazards and partial-likelihood construction follows [{cox}].'),('A2.7','The cash-shortfall interpretation follows [12], and the regulatory/internal capital distinction follows [15].'),('A2.8','The conditional fairness rates follow [9].'),('A2.9','The dependence construction follows [14].'),('A2.10','The augmentation identity and conditional Gaussian calculation follow [16].'),('A2.11',f'The scale prior follows [20], the normal–Gamma representation [21], and the inverse-Gamma auxiliary representation [{wand}, Result 5].'),('A2.12',f'The expected-utility comparison follows [{bda}, ch. 9]. The declared payoff matrix determines the economic threshold.' )]:
            # Keep all citation brackets numeric-only for automatic export matching.
            txt=re.sub(r'\[(\d+), ([^\]]+)\]',r'[\1] (\2)',txt)
            appendix=support(appendix,sec,txt)
    if n==3:
        bda=add_ref(refs,BDA);half=add_ref(refs,HALFT);cox=add_ref(refs,COX);wilson=add_ref(refs,WILSON);wand=add_ref(refs,WAND)
        body=append_cite_to_paragraph(body,'A hierarchical Bayesian logistic model',[bda,half])
        body=append_cite_to_paragraph(body,'A hierarchical Cox model',[cox])
        # Cite Wilson where the original score interval is explained.
        p=next((p for p in body.split('\n\n') if 'Wilson' in p),'')
        if p:body=body.replace(p,p.rstrip().rstrip('.')+f' [{wilson}].',1)
        for sec,txt in [('A3.2','The selective-label and reject-inference problem follows [1]–[3].'),('A3.4','The augmented estimator adapts the doubly robust construction in [4], [5] to the stated selection assumptions.'),('A3.6',f'The multilevel prior and pooling structure follow [{bda}], [{half}].'),('A3.7',f'The auxiliary scale representation follows [{wand}], Result 5.'),('A3.8','The augmentation identity follows [6].'),('A3.9',f'The hazard and partial-likelihood framework follows [{cox}].'),('A3.10',f'The score-inversion interval follows [{wilson}].'),('A3.11','The adaptive-allocation setting follows [7].'),('A3.12','The accounting cash-shortfall interpretation follows [15].')]:appendix=support(appendix,sec,txt)
    if n==4:
        pomdp=add_ref(refs,POMDP)
        for sec,txt in [('A4.2','The value and earnings risk perspectives follow [1], [2].'),('A4.4','The customer benchmark and pricing conventions follow [3]–[5].'),('A4.7','The illustrative ratio definitions follow [6], [7].'),('A4.9',f'The recursion follows the dynamic-programming framework in [{pomdp}], connected to bank balance-sheet control in [9].'),('A4.10',f'The belief-state update follows [{pomdp}].')]:appendix=support(appendix,sec,txt)
        appendix=appendix.replace('Basel Committee, *Interest Rate Risk in the Banking Book* (2016); Basel Framework LCR and NSFR standards; CBK, *Revised Risk-Based Credit Pricing Model* (2025); and H. Englisch et al., “Deep treasury management for banks” (2023).','the IRRBB standard [1], LCR and NSFR definitions [6], [7], revised customer-pricing framework [4], and bank Treasury control study [9].')
    if n==5:
        bda=add_ref(refs,BDA);wand=add_ref(refs,WAND)
        # Explicit decision-analysis and inference authority in the main text.
        p=next((p for p in body.split('\n\n') if 'Beta(4,96)' in p),'')
        if p:body=body.replace(p,p.rstrip().rstrip('.')+f' [{bda}].',1)
        for sec,txt in [('A5.2',f'The conjugate beta–binomial calculation follows [{bda}], ch. 2.'),('A5.5',f'The expected-payoff and uncertainty-review distinction follows the decision-analysis framework in [{bda}], ch. 9.'),('A5.6',f'The logistic augmentation follows [3]; the auxiliary half-t representation follows [{wand}], Result 5.')]:appendix=support(appendix,sec,txt)
        start=appendix.index('Pólya–Gamma inference follows N. G. Polson')
        appendix=appendix[:start]+f'Pólya–Gamma inference follows [3], and the half-t auxiliary-variable representation follows [{wand}], Result 5. Numerical summaries are derived from the specified illustrative distributions using the inference and decision framework in [{bda}]. The workflow applies the bank-controlled architecture [1] and the legal sources [4], [5].\n'
    return body,refs,appendix

def unique(seq):return list(dict.fromkeys(seq))

report={'date':'2026-10-09','numbering':'Restart at [1] per article; appendices reuse that article bibliography.','articles':[],'source_corrections':['Lakkaraju initials and unrelated arXiv link corrected to original author-hosted paper and DOI.','Ehrhardt et al. title, journal, year, authors and DOI corrected.','Clayton initials corrected to D. G.','Jiang initials corrected to N.','Original Mwendo decision-limit reference: Gelman et al., Bayesian Data Analysis, 3rd ed., 2013, ch. 9.']}
apply='--check' not in sys.argv
for n in range(1,6):
    path=next(p for p in ROOT.glob(f'ARTICLE_{n}_*.md') if 'LINKEDIN_POST' not in p.name)
    ap=ROOT/'build'/'appendices'/f'ARTICLE_{n}_MATHEMATICAL_APPENDIX.md'
    original=path.read_text(encoding='utf-8'); appendix=ap.read_text(encoding='utf-8')
    body,refs,tail=split_article(original)
    old_mapping={}
    if apply:
        body,refs,appendix=prepare(n,body,refs,appendix)
        # Every retained source receives a relevant citation. Unused sources are
        # retained as explicitly labelled further reading, never silently dropped.
        order=unique(ids(body)+ids(tail)+ids(appendix))
        missing=sorted(set(order)-set(refs)); assert not missing,(n,missing)
        unused=sorted(set(refs)-set(order))
        if unused:
            appendix+='\n### Further methodological reading\n\nAdditional sources retained from the article bibliography: '+', '.join(f'[{k}]' for k in unused)+'.\n'
            order+=unused
        mapping={old:new for new,old in enumerate(order,1)}
        body=remap(body,mapping);tail=remap(tail,mapping);appendix=remap(appendix,mapping)
        refs={mapping[k]:v for k,v in refs.items()}
        new=body+'### References\n\n'+'\n\n'.join(f'[{k}] {refs[k]}' for k in sorted(refs))+tail
        # Atomic final writes follow all calculations, minimizing conflict risk.
        path.write_text(new,encoding='utf-8');ap.write_text(appendix,encoding='utf-8')
        old_mapping={str(k):v for k,v in mapping.items()}
    body,refs,tail=split_article(path.read_text(encoding='utf-8'))
    appendix=ap.read_text(encoding='utf-8')
    first=unique(ids(body)+ids(tail)+ids(appendix))
    inbody=unique(ids(body)+ids(tail)); inappendix=unique(ids(appendix))
    missing=sorted(set(first)-set(refs)); unused=sorted(set(refs)-set(first))
    duplicate_values=[v for v in set(refs.values()) if list(refs.values()).count(v)>1]
    good=first==list(range(1,len(refs)+1)) and not missing and not unused and not duplicate_values
    report['articles'].append({'article':n,'source':path.name,'appendix':str(ap.relative_to(ROOT)),'reference_count':len(refs),'first_appearance_sequence':first,'body_citations':inbody,'appendix_only_references':sorted(set(inappendix)-set(inbody)),'unresolved':missing,'uncited':unused,'duplicate_bibliography_entries':duplicate_values,'old_to_new':old_mapping,'sequential':good,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'appendix_sha256':hashlib.sha256(ap.read_bytes()).hexdigest()})
    assert good,(n,report['articles'][-1])
report['pass']=all(a['sequential'] for a in report['articles'])
(ROOT/'build'/'citation_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'pass':report['pass'],'articles':[{'article':a['article'],'references':a['reference_count'],'appendix_only':a['appendix_only_references']} for a in report['articles']]},indent=2))
