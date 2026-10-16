"""Add PDF-only equation labels, numbered displays and navigable derivation links.

Input is the fresh TYPESET Markdown emitted by typeset_math.py. No article or
appendix source is rewritten. Scope markers are set by build_combined_pdf.ps1.
One displayed mathematical block gets one number; aligned derivations remain
one block. Inline mathematics stays unnumbered. Semantic topic + content digest
labels stay stable when unrelated equations are inserted or reordered.
"""
from collections import Counter, OrderedDict
from pathlib import Path
import hashlib
import json
import re
import sys
import unicodedata

# Restrict headings to one line despite DOTALL in the display-math branch.
TOKEN = re.compile(r'<!-- equation-scope: (A?[1-5]) -->|^(#{1,6}) ([^\n]+)$|^\$\$[ \t]*\n(.*?)\n\$\$[ \t]*$', re.M | re.S)


def slug(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    text = re.sub(r'^A\d+\.\d+\s*', '', text)
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:70].rstrip('-')


def collect(text):
    scope = None
    section = ''
    counts = Counter()
    section_counts = Counter()
    equations = []
    headings = []
    for match in TOKEN.finditer(text):
        if match[1]:
            scope = match[1]
            section = ''
        elif match[2]:
            section = match[3].strip()
            headings.append((match.end(), scope, section))
        else:
            if scope is None:
                raise ValueError('Display equation encountered before its article/appendix scope')
            latex = match[4].strip()
            assert latex and not re.search(r'\\(?:tag|label|begin\{equation)', latex)
            counts[scope] += 1
            section_counts[scope, section] += 1
            digest = hashlib.sha256(re.sub(r'\s+', '', latex).encode()).hexdigest()[:10]
            label = f'eq:{scope.lower()}-{slug(section)}-{digest}'
            equations.append(dict(scope=scope, number=f'{scope}.{counts[scope]}', label=label,
                                  section=section, step=section_counts[scope, section],
                                  latex=latex, start=match.start(), end=match.end(),
                                  description=f'{section}: step {section_counts[scope, section]}'))
    assert set(counts) == {'1', '2', '3', '4', '5', 'A1', 'A2', 'A3', 'A4', 'A5'}
    assert len({e['label'] for e in equations}) == len(equations)
    return equations, headings, counts


def main():
    path=Path(sys.argv[1]).resolve()
    sources=list(path.parent.parent.glob('ARTICLE_*.md'))+list((path.parent/'appendices').glob('*.md'))
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    text=path.read_text(encoding='utf-8')
    equations,headings,counts=collect(text)
    def section_eq(section):
        return [e for e in equations if re.match(re.escape(section)+r'(?:\s|$)',e['section'])]
    def ref(e): return r'\eqref{'+e['label']+'}'
    sections={re.match(r'(A[1-5]\.\d+)',h).group(1):h for _,_,h in headings if re.match(r'A[1-5]\.\d+',h)}
    anchor=lambda sec:'appendix-'+sec.lower().replace('.','-')
    notes={
      '1': 'Full derivations for offer experiments, policy evaluation and competing risks are collected in A1.3–A1.9; the hierarchical hazard likelihood is in A2.6.',
      '2': 'The complete hierarchy is specified in A2.5–A2.6. A2.10 derives the Pólya–Gamma update; A2.11 distinguishes Student-t coefficient priors from half-t group-scale priors. A2.12 derives the economic decision boundary.',
      '3': 'A3.6–A3.9 apply the hierarchy and inference derivations from A2.5, A2.6, A2.10 and A2.11 to selective labels. Their local calculations and target-alignment conditions remain alongside the application.',
      '4': 'A4.9–A4.10 apply the Bellman and belief-state derivations in A2.2–A2.3 to Treasury constraints, cash flows and policy comparisons. A4.1–A4.8 derive the financial quantities used by those controls.',
      '5': 'A5.1–A5.5 derive the reviewer quantities and worked decision gates. A5.6 connects their approved model artifacts to A2.5, A2.6, A2.10 and A2.11; A5.7–A5.8 specify numerical and workflow checks.'}
    replacements=[]
    for e in equations:
        replacements.append((e['start'],e['end'],'```{=latex}\n\\begin{equation}\n\\tag{'+e['number']+'}\\label{'+e['label']+'}\n'+e['latex']+'\n\\end{equation}\n```'))
    for pos,scope,title in headings:
        if re.match(r'A[1-5]\.\d+',title):
            sec=re.match(r'A[1-5]\.\d+',title).group(0)
            replacements.append((pos,pos,' {#'+anchor(sec)+'}'))
    for a,b,value in sorted(replacements,reverse=True): text=text[:a]+value+text[b:]
    # Navigation is added to the combined edition; reading-article sources stay untouched.
    text=re.sub(r'<!-- equation-scope: ([1-5]) -->',lambda m:notes[m[1]]+'\n',text)
    text=re.sub(r'<!-- equation-scope: A[1-5] -->\s*','',text)
    # Clickable subsection references are applied only outside fenced code, headings and math.
    chunks=re.split(r'(```[\s\S]*?```|^#{1,6} [^\n]+$|\$[^\n$]+\$)',text,flags=re.M)
    pattern=re.compile(r'(?<![\w#/-])(A[1-5]\.\d+)(?!\d)')
    for i in range(0,len(chunks),2):
        chunks[i]=pattern.sub(lambda m:'['+m[1]+'](#'+anchor(m[1])+')' if m[1] in sections else m[0],chunks[i])
    text=''.join(chunks)
    topics=[('Survival and competing risks',['A1.8','A2.6','A3.9']),('Hierarchies',['A2.5','A3.6']),('Pólya–Gamma computation',['A2.10','A3.8']),('Coefficient and group-scale priors',['A2.11']),('Credit-limit decisions',['A2.12','A5.5']),('Policy evaluation',['A1.5','A1.6','A2.15']),('Selection and sensitivity',['A3.3','A3.5']),('Bellman and POMDP control',['A2.2','A2.3','A4.10']),('Reviewer uncertainty',['A3.13','A5.1','A5.7'])]
    guide=['\\clearpage','# Navigating the equations','','Equations are numbered by article, such as (2.1), and by appendix, such as (A2.1). Each aligned displayed block has one number. Inline mathematical expressions remain unnumbered. Appendix subsection labels, such as A2.5, identify the complete derivation; the equation register identifies each displayed step.','','| Topic | Complete derivation and applications | Selected equations |','| --- | --- | --- |']
    for title,secs in topics:
        chosen=[]
        for sec in secs:
            found=section_eq(sec)
            if found: chosen.append(found[0])
        guide.append('| '+title+' | '+', '.join('['+sec+'](#'+anchor(sec)+')' for sec in secs)+' | '+', '.join(ref(e) for e in chosen)+' |')
    first=text.index('\\newpage');text=text[:first]+'\n'.join(guide)+'\n\n'+text[first:]
    register=['\\clearpage','# Equation register','','Each number links to one displayed block. Page references refer to the PDF edition.','','']
    md=['# Equation register','','Generated from the shared numbered source for the combined PDF and Word editions.','']
    for scope in ['1','A1','2','A2','3','A3','4','A4','5','A5']:
        title=('Appendix ' if scope.startswith('A') else 'Article ')+scope
        register+=['\\Needspace{7\\baselineskip}','## '+title,'','| Equation | Topic and derivation step | PDF page |','| --- | --- | --- |']
        md+=['## '+title,'','| Equation | Topic and derivation step | Stable label |','| --- | --- | --- |']
        for e in equations:
            if e['scope']!=scope:continue
            register.append('| '+ref(e)+' | '+e['description']+' | \\pageref{'+e['label']+'} |')
            md.append('| ('+e['number']+') | '+e['description']+' | `'+e['label']+'` |')
        register.append('');md.append('')
    text+='\n\n'+'\n'.join(register)+'\n'
    requested=re.findall(r'\\(?:eqref|pageref)\{([^}]+)\}',text)
    labels={e['label'] for e in equations};assert set(requested)<=labels
    destination=path.with_name(path.name.replace('_TYPESET.md','_NUMBERED.md'))
    destination.write_text(text,encoding='utf-8')
    (path.parent.parent/'EQUATION_REGISTER.md').write_text('\n'.join(md),encoding='utf-8')
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in hashes.items())
    report=dict(display_equations=len(equations),counts_by_scope=dict(counts),cross_reference_occurrences=len(requested),contextual_cross_reference_paragraphs=5,undefined_references=[],entries=equations,article_sources_unchanged=True,inline_math_unnumbered=True,unchanged_source_hashes=hashes)
    (path.parent/'equation_numbering_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in {'entries','unchanged_source_hashes'}},indent=2))

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8'); main()
