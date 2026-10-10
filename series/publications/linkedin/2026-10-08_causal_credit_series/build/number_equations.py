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
    path = Path(sys.argv[1]).resolve()
    protected = list(path.parent.parent.glob('ARTICLE_*.md')) + list((path.parent / 'appendices').glob('*.md'))
    source_hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
    text = path.read_text(encoding='utf-8')
    equations, headings, counts = collect(text)

    def pick(scope, section, step=1):
        matches = [e for e in equations if e['scope'] == scope and
                   e['section'].startswith(section) and e['step'] == step]
        if len(matches) != 1:
            raise ValueError(f'Ambiguous or absent equation selector: {scope}/{section}/{step}')
        return matches[0]

    def ref(e):
        return r'\eqref{' + e['label'] + '}'

    def refs(scope, section, *steps):
        return ', '.join(ref(pick(scope, section, s)) for s in steps)

    # Short named anchors are used for the principal cross-article concepts.
    named = {
        'a1-discounted-cash-value': ('1', 'Four elements', 2),
        'a1-ips-policy-value': ('1', 'Off-policy evaluation', 1),
        'a1-dr-policy-value': ('1', 'Off-policy evaluation', 2),
        'a1-competing-risk-incidence-derivation': ('A1', 'A1.8', 4),
        'a2-bellman-value': ('2', 'Sequential control', 1),
        'a2-belief-state': ('2', 'Sequential control', 2),
        'a2-logistic-hierarchy': ('A2', 'A2.5', 1),
        'a2-group-distributions-hyperpriors': ('A2', 'A2.5', 2),
        'a2-hazard-likelihood': ('A2', 'A2.6', 3),
        'a2-pg-gaussian-posterior': ('A2', 'A2.10', 3),
        'a2-bayesian-limit-threshold': ('2', 'Bayesian decision boundaries', 4),
        'a3-selection-transport': ('A3', 'A3.3', 3),
        'a3-selection-sensitivity': ('A3', 'A3.5', 3),
        'a4-ftp-cash-charge': ('A4', 'A4.4', 5),
        'a4-feasible-bellman-recursion': ('A4', 'A4.9', 4),
        'a5-risk-cap-probability': ('5', 'Show the reviewer', 1),
        'a5-benefit-probability': ('5', 'Show the reviewer', 2),
        'a5-cash-shortfall-probability': ('5', 'Show the reviewer', 3),
    }
    for name, selector in named.items():
        item = pick(*selector)
        item['label'] = 'eq:' + name
        item['description'] = name.split('-', 1)[1].replace('-', ' ').capitalize()
    pick('A2', 'A2.10', 3)['description'] = 'Pólya–Gamma Gaussian conditional posterior'

    # Prose appears in this PDF edition only, next to the relevant section.
    notes = {
      ('1', 'Four elements of a contextual bandit'):
        f"Equation {refs('1', 'Four elements', 2)} uses the discounted cash convention derived in equations {refs('A1', 'A1.2', 1, 3, 4)}. The institution's internal funding charge is developed in equation {refs('A4', 'A4.4', 5)}.",
      ('1', 'Delayed outcomes need careful handling'):
        f"The competing-risk probability below connects to the incidence derivation in equation {refs('A1', 'A1.8', 4)} and the shared hazard likelihood in equation {refs('A2', 'A2.6', 3)}.",
      ('2', 'Put the risk models inside the decision problem'):
        f"Equations {refs('A2', 'A2.5', 1, 2)} specify the full logistic hierarchy and hyperpriors; equation {refs('A2', 'A2.6', 3)} specifies the separate survival likelihood. The selection analysis in Article 3 applies the same named levels in equations {refs('A3', 'A3.6', 1, 2)}.",
      ('2', 'Pólya–Gamma computation supports posterior estimation'):
        f"The Gaussian conditional posterior is derived in equation {refs('A2', 'A2.10', 3)} and expanded for selective labels in equation {refs('A3', 'A3.8', 6)}. Its service-facing numerical form appears in equations {refs('A5', 'A5.6', 8, 9)}.",
      ('2', 'Bayesian decision boundaries turn predictions into limit-review evidence'):
        f"The expected-value boundary in equation {refs('2', 'Bayesian decision boundaries', 4)} is derived in Appendix A2.12. The distinct risk-cap, incremental-benefit and predictive-cash probabilities used by a reviewer appear in equations {refs('5', 'Show the reviewer', 1, 2, 3)}.",
      ('3', 'Model the selection process, then test its assumptions'):
        f"Appendix A3.3 derives selection transport beginning with equation {refs('A3', 'A3.3', 1)}. Equation {refs('A3', 'A3.5', 3)} supplies the explicit sensitivity model when unobserved selection remains relevant; Article 1's policy estimators appear in equations {refs('1', 'Off-policy evaluation', 1, 2)}.",
      ('4', 'Constrained stochastic control rather than reward-only optimization'):
        f"The Treasury recursion in equation {refs('A4', 'A4.9', 4)} extends the control form introduced in equation {refs('2', 'Sequential control', 1)} with Treasury-specific actions, cash flows and feasible sets. Its belief update is equation {refs('A4', 'A4.10', 1)}; Appendix A2.3 derives the borrower-level belief construction.",
      ('5', 'Show the reviewer three kinds of uncertainty'):
        f"Equations {refs('5', 'Show the reviewer', 1, 2, 3)} have separate derivations and worked calculations in Appendices A5.1–A5.4. The expected-value limit boundary they complement is equation {refs('2', 'Bayesian decision boundaries', 4)}.",
    }
    insertions = {}
    for end, scope, title in headings:
        if (scope, title) in notes:
            insertions[end] = '\n\n' + notes[scope, title]

    # Fenced raw-LaTeX blocks preserve valid single-token arguments such as
    # \frac{numerator}n verbatim through Pandoc's Markdown reader.
    replacements = [(e['start'], e['end'],
                     '```{=latex}\n\\begin{equation}\n\\tag{' + e['number'] + '}\\label{' + e['label'] +
                     '}\n' + e['latex'] + '\n\\end{equation}\n```') for e in equations]
    replacements += [(pos, pos, value) for pos, value in insertions.items()]
    for start, end, value in sorted(replacements, reverse=True):
        text = text[:start] + value + text[end:]
    text = re.sub(r'<!-- equation-scope: A?[1-5] -->\s*', '', text)

    topics = [
        ('Cash and value', [('1', 'Four elements', 2), ('A1', 'A1.2', 3), ('A4', 'A4.4', 5)]),
        ('Policy evaluation', [('1', 'Off-policy evaluation', 1), ('1', 'Off-policy evaluation', 2), ('A1', 'A1.6', 3)]),
        ('Survival and competing risks', [('A1', 'A1.8', 4), ('A2', 'A2.6', 3), ('A3', 'A3.9', 6)]),
        ('Hierarchies and hyperpriors', [('A2', 'A2.5', 1), ('A2', 'A2.5', 2), ('A3', 'A3.6', 2)]),
        ('Pólya–Gamma computation', [('A2', 'A2.10', 3), ('A3', 'A3.8', 6), ('A5', 'A5.6', 8)]),
        ('Credit-limit decisions', [('2', 'Bayesian decision boundaries', 4), ('2', 'Bayesian decision boundaries', 7), ('A5', 'A5.5', 2)]),
        ('Selection and sensitivity', [('A3', 'A3.3', 1), ('A3', 'A3.5', 3)]),
        ('Bellman and POMDP control', [('2', 'Sequential control', 1), ('A2', 'A2.3', 3), ('A4', 'A4.9', 4), ('A4', 'A4.10', 2)]),
        ('Reviewer uncertainty', [('5', 'Show the reviewer', 1), ('5', 'Show the reviewer', 2), ('5', 'Show the reviewer', 3)]),
    ]
    guide = ['\\clearpage', '# Navigating the equations', '',
             'Displayed equations are numbered by article: (2.1) belongs to Article 2. Appendix numbers carry an A: (A2.1) belongs to its mathematical appendix. An aligned derivation has one number for the complete displayed block. Inline mathematical symbols remain unnumbered.', '',
             'Equation references and page numbers are clickable. The register at the end of this edition lists every displayed block by topic and derivation step. Section labels such as A2.5 identify appendix sections; equation labels appear in parentheses.', '',
             '| Follow this idea | Connected equations |', '| --- | --- |']
    for title, selectors in topics:
        guide.append('| ' + title + ' | ' + ', '.join(ref(pick(*s)) for s in selectors) + ' |')
    first_break = text.index('\\newpage')
    text = text[:first_break] + '\n'.join(guide) + '\n\n' + text[first_break:]

    register = ['\\clearpage', '# Equation register', '',
                'Each linked number identifies one displayed block. Step numbers count the successive blocks within the named topic; aligned derivations share a single equation number.', '']
    md = ['# Equation register', '', 'Generated for the combined TeX PDF. The article and Unicode Word sources are unchanged.', '',
          'Use article numbers (1.1)–(5.n) and appendix numbers (A1.1)–(A5.n). The PDF contains clickable equation/page references. Semantic labels remain stable when unrelated equations are inserted.', '']
    for scope in ['1', 'A1', '2', 'A2', '3', 'A3', '4', 'A4', '5', 'A5']:
        title = 'Appendix ' + scope if scope.startswith('A') else 'Article ' + scope
        register += ['## ' + title, '', '| Equation | Topic and derivation step | Page |', '| --- | --- | --- |']
        md += ['## ' + title, '', '| Equation | Topic and derivation step | Stable label |', '| --- | --- | --- |']
        for e in equations:
            if e['scope'] != scope:
                continue
            register.append('| ' + ref(e) + ' | ' + e['description'] + ' | \\pageref{' + e['label'] + '} |')
            md.append('| (' + e['number'] + ') | ' + e['description'] + ' | `' + e['label'] + '` |')
        register.append('')
        md.append('')
    text += '\n\n' + '\n'.join(register) + '\n'
    destination = path.with_name(path.name.replace('_TYPESET.md', '_NUMBERED.md'))
    destination.write_text(text, encoding='utf-8')
    (path.parent.parent / 'EQUATION_REGISTER.md').write_text('\n'.join(md).rstrip() + '\n', encoding='utf-8')
    requested = re.findall(r'\\(?:eqref|pageref)\{([^}]+)\}', text)
    labels = {e['label'] for e in equations}
    assert set(requested) <= labels
    assert len(labels) == len(equations)
    report = dict(display_equations=len(equations), counts_by_scope=dict(counts),
                  cross_reference_occurrences=len(requested), contextual_cross_reference_paragraphs=len(insertions),
                  undefined_references=sorted(set(requested) - labels),
                  entries=equations,
                  article_sources_unchanged=True, inline_math_unnumbered=True)
    assert all(hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest for name, digest in source_hashes.items())
    report['unchanged_source_hashes'] = source_hashes
    (path.parent / 'equation_numbering_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in {'entries', 'unchanged_source_hashes'}}, indent=2))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
