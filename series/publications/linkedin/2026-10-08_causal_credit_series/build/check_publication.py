from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
import json, re

root = Path(__file__).resolve().parent.parent
diagrams = root / 'linkedin_diagrams'
names = [
('01_offer_experiment_and_governed_learning', '1. Credit-offer experiments'),
('02_temporal_graph_bandits_mcts_graphsvx', '2. Graphs, bandits, MCTS and GraphSVX'),
('02_evidence_to_sequential_collection_control', '3. Sequential collection control'),
('03_reject_inference_evidence_path', '4. Reject-inference evidence'),
('04_treasury_data_to_alco_approval', '5. Treasury data and ALCO approval'),
('04_treasury_constrained_control_loop', '6. Constrained Treasury control'),
('05_bank_controlled_agentic_ai_workflow', '7. Bank-controlled agentic AI'),
]
canvas = Image.new('RGB', (1800, 2800), 'white')
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 25)
index = ['# Named diagrams for LinkedIn', '', 'Each diagram is saved as a PNG for uploading, an SVG for scaling, and a Mermaid source file for editing.', '']
for i, (name, title) in enumerate(names):
    for extension in ('png', 'svg', 'mmd'):
        assert (diagrams / (name + '.' + extension)).exists(), name + '.' + extension
    pic = Image.open(diagrams / (name + '.png')).convert('RGB')
    pic.thumbnail((860, 630))
    x, y = (i % 2) * 900, (i // 2) * 700
    draw.text((x + 20, y + 12), title, font=font, fill='#14394d')
    canvas.paste(pic, (x + (900 - pic.width)//2, y + 55))
    index.append(f'- **{title}**: [PNG]({name}.png) | [SVG]({name}.svg) | [Mermaid]({name}.mmd)')
canvas.save(diagrams / '00_linkedin_diagrams_contact_sheet.png')
(diagrams / '00_LINKEDIN_DIAGRAMS_INDEX.md').write_text('\n'.join(index)+'\n', encoding='utf-8')
old = diagrams / '02_sequential_collection_control_path.png'
if old.exists():
    old.unlink()
pdf = root / 'publications/UNDERWRITE_FOR_COLLECTION_FIVE_ARTICLE_RESEARCH_EDITION_2026-10-08.pdf'
reader = PdfReader(pdf)
texts = [p.extract_text() or '' for p in reader.pages]
post = (root / 'publications/UNDERWRITE_FOR_COLLECTION_LINKEDIN_POST_2026-10-08.md').read_text(encoding='utf-8')
assert len(post) == 2000, len(post)
master_post=(root/'publications/UNDERWRITE_FOR_COLLECTION_MASTER_WHITEPAPER_LINKEDIN_POST_2000_CHARACTERS.md').read_text(encoding='utf-8')
assert len(master_post)==2000, len(master_post)
spec_post=(root/'publications/REQUIREMENTS_AND_SPECIFICATIONS_LINKEDIN_POST_2000_CHARACTERS.md').read_text(encoding='utf-8')
assert len(spec_post)==2000, len(spec_post)
report = {'pdf_pages':len(reader.pages), 'pdf_bytes':pdf.stat().st_size, 'post_characters':len(post), 'named_diagrams':len(names), 'pages_with_images':[i+1 for i,p in enumerate(reader.pages) if len(p.images)], 'source_word_counts':{p.name:len(p.read_text(encoding='utf-8').split()) for p in root.glob('ARTICLE_*.md')}}
assert all(len(t.strip()) > 20 for t in texts), 'Unexpected empty page'
assert '\ufffd' not in ''.join(texts), 'PDF contains replacement characters'
(root / 'build/publication_checks.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
(root / 'build/pdf_text.txt').write_text('\n\f\n'.join(texts), encoding='utf-8')
print(json.dumps(report, indent=2))
