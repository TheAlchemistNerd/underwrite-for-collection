"""Check equation destinations, final TeX diagnostics and render every PDF page."""
from pathlib import Path
import json,re,subprocess,hashlib
from collections import Counter
from PIL import Image,ImageDraw,ImageFont
from pypdf import PdfReader

base=Path(__file__).resolve().parent
pdf=base.parent/'publications/UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION_2026-10-08.pdf'
stem='UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION_2026-10-08'
numbering=json.loads((base/'equation_numbering_report.json').read_text(encoding='utf-8'))
log=(base/(stem+'.log')).read_text(encoding='utf-8',errors='replace')
diagnostics=[line for line in log.splitlines() if re.search(r'Overfull|Missing character|undefined references|multiply defined|^!',line,re.I)]
assert not diagnostics,diagnostics
aux=(base/(stem+'.aux')).read_text(encoding='utf-8')
tex=(base/(stem+'.tex')).read_text(encoding='utf-8')
tex_equations=dict(re.findall(r'\\begin\{equation\}\s*\\tag\{[^}]+\}\\label\{([^}]+)\}\s*(.*?)\s*\\end\{equation\}',tex,re.S))
assert len(tex_equations)==numbering['display_equations'],len(tex_equations)
for entry in numbering['entries']:
    assert tex_equations[entry['label']].strip()==entry['latex'].strip(),entry['number']
labels=dict(re.findall(r'\\newlabel\{(eq:[^}]+)\}\{\{\{?([^}]+)\}',aux))
assert len(labels)==numbering['display_equations'],(len(labels),numbering['display_equations'])
for entry in numbering['entries']:
    assert labels[entry['label']]==entry['number'],entry
reader=PdfReader(pdf)
pdftotext=Path('C:/Users/Nevo/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe')
extracted=subprocess.run([str(pdftotext),'-layout',str(pdf),'-'],capture_output=True)
assert extracted.returncode==0,extracted.stderr.decode(errors='replace')
text=extracted.stdout.decode('utf-8')
texts=[t for t in text.split('\f') if t.strip()]
assert 'Draft for review' not in text
assert '\ufffd' not in text
assert all(len(t.strip())>10 for t in texts)
assert 'Navigating the equations' in text and 'Equation register' in text
searchable=re.sub(r'\s+','',text).translate(str.maketrans({'\ufd3e':'(','\ufd3f':')'}))
missing_numbers=[e['number'] for e in numbering['entries'] if '('+e['number']+')' not in searchable]
assert not missing_numbers,missing_numbers
destinations=reader.named_destinations
equation_destinations={k:v for k,v in destinations.items() if k.startswith(('equation.','AMS.'))}
assert len(equation_destinations)>=numbering['display_equations'],len(equation_destinations)
invalid_links=[]; link_count=0
for i,page in enumerate(reader.pages):
    for ref in page.get('/Annots',[]):
        link=ref.get_object()
        action=link.get('/A',{})
        destination=link.get('/Dest') or (action.get('/D') if action.get('/S')=='/GoTo' else None)
        if isinstance(destination,str):
            link_count+=1
            if destination not in destinations: invalid_links.append((i+1,destination))
assert not invalid_links,invalid_links
qa=base/'numbered_pdf_qa_2026-10-16';qa.mkdir(exist_ok=True)
poppler=Path('C:/Users/Nevo/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
render_hash=qa/'rendered_pdf_sha256.txt'
current_hash=hashlib.sha256(pdf.read_bytes()).hexdigest()
if len(list(qa.glob('page-*.png')))!=len(reader.pages) or not render_hash.exists() or render_hash.read_text().strip()!=current_hash:
    proc=subprocess.run([str(poppler),'-r','80','-png',str(pdf),str(qa/'page')],capture_output=True)
    assert proc.returncode==0,proc.stderr.decode(errors='replace')
    render_hash.write_text(current_hash,encoding='ascii')
pages=sorted(p for p in qa.glob('page-*.png') if int(p.stem.split('-')[-1]) <= len(reader.pages))
assert len(pages)==len(reader.pages),(len(pages),len(reader.pages))
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',20)
contacts=[]
for start in range(0,len(pages),4):
    sheet=Image.new('RGB',(1400,1900),'#dddddd');draw=ImageDraw.Draw(sheet)
    for n,path in enumerate(pages[start:start+4]):
        im=Image.open(path).convert('RGB');im.thumbnail((680,900))
        x=(n%2)*700;y=(n//2)*950
        draw.text((x+8,y+3),f'Page {start+n+1}',font=font,fill='black')
        sheet.paste(im,(x+(700-im.width)//2,y+30))
    c=qa/f'contact_{start+1:03d}_{min(start+4,len(pages)):03d}.png';sheet.save(c);contacts.append(str(c))
report={'date':'2026-10-16','file':str(pdf),'pages':len(reader.pages),'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'display_equations':len(labels),'counts_by_scope':numbering['counts_by_scope'],
        'equation_labels_correct':True,'all_equation_numbers_found_in_pdf':True,
        'all_equation_tex_preserved_verbatim':True,
        'number_text_check':'Poppler; font-mapped ornate parentheses normalised for comparison',
        'contextual_link_paragraphs':numbering['contextual_cross_reference_paragraphs'],
        'cross_reference_occurrences':numbering['cross_reference_occurrences'],
        'internal_pdf_links':link_count,'invalid_links':invalid_links,'final_tex_diagnostics':diagnostics,
        'draft_for_review_removed':True,'rendered_pages':len(pages),'visual_review_complete':False,
        'contacts':contacts}
(base/'pdf_numbering_validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='contacts'},indent=2))
