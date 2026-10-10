from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from pypdf import PdfReader
import hashlib, json, subprocess

root=Path(__file__).resolve().parent.parent
out=root/'build/word_final_revision_qa'
out.mkdir(exist_ok=True)
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
docs=sorted((root/'publications/word').glob('ARTICLE_*.docx'))+[root/'publications/UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION_2026-10-08.docx']
poppler=Path('C:/Users/Nevo/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
reports=[]
for n,p in enumerate(docs,1):
    with ZipFile(p) as z:
        xml=etree.fromstring(z.read('word/document.xml'))
        text=''.join(xml.xpath('//w:t/text()',namespaces=ns))
        drawings=len(xml.findall('.//w:drawing',ns))
        assert not xml.findall('.//m:oMath',ns),p
        assert '\\frac' not in text and '\\begin' not in text,p
        assert 'Draft for review' not in text and 'This draft' not in text,p
        assert 'CC BY-NC-SA 4.0' in text,p
        symbols=sorted(set(c for c in text if ord(c)>127))
        assert len(symbols)>10,p
        if n in (2,6):
            for expected in ['σ ∼ Half-Student-t(ν=3, scale=s₀)','p* = (G+O)/(G+O+L)','credible interval']:
                assert expected in text,expected
        if n in (1,6): assert 'Financing ring-fenced receivables is the general proposition' in text
        if n in (3,6): assert 'Where the worked structure uses a special-purpose vehicle (SPV)' in text
    pdf=root/'build/word/qa'/p.stem/(p.stem+'.pdf')
    old=root/'build/word_before_final_revision'/(p.stem+'.pdf')
    reader=PdfReader(pdf)
    texts=[page.extract_text() or '' for page in reader.pages]
    before=[page.extract_text() or '' for page in PdfReader(old).pages]
    changed=[i+1 for i,t in enumerate(texts) if i>=len(before) or t!=before[i]]
    key_pages={1,len(texts)}
    search=['Financing ring-fenced receivables is the general proposition','Where the worked structure uses a special-purpose vehicle','This article','Article 2','Article 4']
    for i,t in enumerate(texts):
        t=' '.join(t.split())
        if any(s in t for s in search): key_pages.add(i+1)
    key_pages.update(changed)
    dest=out/f'document_{n}';dest.mkdir(exist_ok=True)
    for page in sorted(key_pages):
        if (dest/f'page-{page:03}.png').exists() and page not in changed:
            continue
        subprocess.run([str(poppler),'-f',str(page),'-l',str(page),'-r','115','-png','-singlefile',str(pdf),str(dest/f'page-{page:03}')],check=True,capture_output=True)
    reports.append({'document':n,'docx':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'render_pdf':str(pdf),'render_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(texts),'unicode_text':True,'unicode_symbol_count':len(symbols),'native_math_or_latex':False,'embedded_diagrams':drawings,'changed_pages_since_previous_render':changed,'pages_rendered_for_final_revision_review':sorted(key_pages)})
report={'date':'2026-10-10','status':'pending_visual_review','scope':'Final Word revisions, all six package integrity checks and targeted rendered-page review after earlier full visual QA','prior_full_review':['build/word_1_3_visual_qa.json','build/word_4_5_combined_visual_qa.json'],'documents':reports,'issues':[]}
(root/'build/word_final_revision_validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
