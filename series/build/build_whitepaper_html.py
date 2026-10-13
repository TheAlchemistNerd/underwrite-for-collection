"""Build self-contained HTML from the same active chapters and worked appendix."""
from pathlib import Path
import argparse
import os
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]
SERIES=ROOT/'series'
CSS='''<style>
html{background:#edf2f6;color:#162a3a}body{max-width:1120px;margin:2rem auto;padding:3rem;background:white;font:17px/1.65 Georgia,serif}
h1,h2,h3,h4,nav{font-family:Arial,sans-serif}h1{color:#123e56}h2{margin-top:3rem;border-top:2px solid #b58c3b;padding-top:1rem;color:#123e56}
h3{color:#246477}a{color:#006b8a}table{border-collapse:collapse;width:100%;font:14px/1.5 Arial,sans-serif;margin:1.5rem 0;display:block;overflow:auto}
th,td{padding:.65rem;border-bottom:1px solid #ccd6df;vertical-align:top}th{background:#e5eff4;text-align:left}tr:nth-child(even){background:#f8fafc}
pre{overflow:auto;background:#f2f5f7;padding:1rem;font-size:13px}code{font-size:.87em}img{max-width:100%;height:auto}math{font-size:1.02em}
@media(max-width:800px){body{padding:1.2rem;margin:0}table{font-size:12px}}@media print{body{margin:0;padding:0;max-width:none}nav{display:none}h2{break-before:page}}
</style>'''


def body(path):
    return re.sub(r'\A---\n.*?\n---\n','',path.read_text(encoding='utf-8'),count=1,flags=re.S).strip()


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--case-only',action='store_true');args=parser.parse_args()
    scratch=ROOT/'scratchpad/build/underwrite-for-collection-series';scratch.mkdir(parents=True,exist_ok=True)
    out=SERIES/'dist';out.mkdir(exist_ok=True)
    style=scratch/'worked-case-style.html';style.write_text(CSS,encoding='utf-8')
    appendix=SERIES/'appendices/WORKED_OPERATING_AND_FINANCE_CASE.md'
    governed=SERIES/'appendices/GOVERNED_EVIDENCE_AND_INTERVENTION_CASE.md'
    acknowledgements=SERIES/'appendices/ACKNOWLEDGEMENTS_AND_LINKEDIN_INPUTS_2026-10-04.md'
    sources=[(SERIES/'parts').glob('Part_'+label+'_*') for label in ('1','2a','2b','3','4','5')]
    chapters=[next(x) for x in sources]
    combined=['# Underwrite for Collection\n\n## Integrated research edition: 4 October 2026\n\nNevil Maloba. Includes the reproducible operating, finance and governed evidence cases, and acknowledgements to practitioners whose LinkedIn writing and discussions helped shape the research. The worked cases use stated hypothetical inputs and reproducible calculations.\n\nOriginal text: CC BY-NC-SA 4.0.']
    for path in chapters:
        title=path.stem.replace('_',' ')
        combined.append('# '+title+'\n\n'+body(path))
    combined.append('# Worked case appendix\n\n'+body(appendix))
    combined.append('# Governed evidence appendix\n\n'+body(governed))
    combined.append(body(acknowledgements))
    assembly=scratch/'Underwrite_for_Collection_White_Paper_HTML.md'
    assembly.write_text('\n\n'.join(combined)+'\n',encoding='utf-8')
    targets=[(appendix,'Underwrite_for_Collection_Worked_Case_2026-10-01.html','One order, several cash clocks'),
             (governed,'Underwrite_for_Collection_Governed_Evidence_Case_2026-10-01.html','Governing evidence and intervention')]
    if not args.case_only: targets.append((assembly,'Underwrite_for_Collection_Master_2026-10-04.html','Underwrite for Collection: integrated research edition'))
    env=os.environ.copy()
    chrome=Path(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    if chrome.exists(): env.setdefault('PUPPETEER_EXECUTABLE_PATH',str(chrome))
    for src,name,title in targets:
        command=['pandoc',str(src),'-s','--toc','--toc-depth=3','--mathml','--embed-resources',
                 '--from=markdown+tex_math_dollars+tex_math_single_backslash','--include-in-header='+str(style),
                 '--metadata=pagetitle:'+title,'--resource-path='+os.pathsep.join(map(str,[SERIES/'parts',SERIES,ROOT])),
                 '--lua-filter='+str(SERIES/'build/mermaid.lua'),'-o',str(out/name)]
        subprocess.run(command,cwd=scratch,env=env,check=True)
        print(out/name)


if __name__=='__main__':main()
