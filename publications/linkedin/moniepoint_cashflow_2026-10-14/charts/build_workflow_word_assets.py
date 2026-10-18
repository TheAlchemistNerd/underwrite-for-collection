from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageChops
import json, html, math
P=Path(__file__).resolve().parent
font_path=Path('C:/Windows/Fonts/arial.ttf')
bold_path=Path('C:/Windows/Fonts/arialbd.ttf')
def font(n,b=False): return ImageFont.truetype(str(bold_path if b else font_path),n)
specs=[
('MONIEPOINT_WORKFLOW_01_EVIDENCE_AND_CALCULATIONS',[(0,1150),(1125,2190),(2165,3030),(3025,3623)],['Source permissions and the dated case record','Usable evidence and transaction cash provenance','Cash calculations, uncertainty and challenge','Correction loop and selection-support assessment']),
('MONIEPOINT_WORKFLOW_02_APPROVAL_AND_EXECUTION',[(0,935),(915,1995),(1975,2860),(2840,3610),(3590,4328)],['Versioned policy and registered risk extensions','Eligible experimental allocation and reviewer packet','Human review and independent checker','Expiring instruction and current-conditions gate','Execution receipt and reconciled loan ledger']),
('MONIEPOINT_WORKFLOW_03_MONITORING_AND_LEARNING',[(0,1020),(935,1790),(1770,2392)],['Cash-calendar monitoring and signal classification','Evidence correction, servicing and mature outcomes','Portfolio authority and controlled model release'])]
items=[]
for panel,(stem,ranges,titles) in enumerate(specs,1):
 im=Image.open(P/(stem+'.png')).convert('RGB')
 for j,((top,bottom),title) in enumerate(zip(ranges,titles),1):
  bottom=min(bottom,im.height)
  crop=im.crop((0,top,im.width,bottom))
  diff=ImageChops.difference(crop,Image.new('RGB',crop.size,'white')).convert('L')
  bbox=diff.point(lambda p:255 if p>12 else 0).getbbox()
  left=max(0,bbox[0]-14);right=min(im.width,bbox[2]+14)
  crop=crop.crop((left,0,right,crop.height))
  w=max(crop.width,730); out=Image.new('RGB',(w,crop.height+125),'white'); d=ImageDraw.Draw(out)
  d.text((18,10),f'Workflow {panel} - segment {j} of {len(ranges)}',font=font(26,True),fill='#142C3E')
  d.text((18,45),title,font=font(21),fill='#142C3E')
  out.paste(crop,((w-crop.width)//2,85))
  d.text((18,out.height-30),'Read with the adjoining segment; connector bands overlap.',font=font(18),fill='#4B5D6B')
  name=f'MONIEPOINT_WORD_WORKFLOW_{panel:02d}_{j:02d}.png';out.save(P/name,dpi=(150,150))
  orientation='landscape' if w>1000 else 'portrait'
  width=9.6 if orientation=='landscape' else 6.3
  # Keep the diagram inside the usable page height as well as width.
  max_height=6.55 if orientation=='landscape' else 8.25
  width=min(width,max_height*w/out.height)
  items.append({'image':name,'panel':panel,'segment':j,'title':title,'caption':f'Workflow {panel}, segment {j} of {len(ranges)}. {title}. Adjoining connector bands overlap; complete nodes are retained.','orientation':orientation,'recommended_width_inches':round(width,2),'pixel_width':w,'pixel_height':out.height,'source':stem+'.png','source_crop':[left,top,right,bottom]})
# Compact body overview using the same workflow roles as the full Mermaid source.
W,H=1500,1210
im=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(im)
sv=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" fill="white"/>']
def text(x,y,s,size=30,b=False,color='#142C3E'):
 d.text((x,y),s,font=font(size,b),fill=color)
 sv.append(f'<text x="{x}" y="{y+size}" font-family="Arial" font-size="{size}" font-weight="{"bold" if b else "normal"}" fill="{color}">{html.escape(s)}</text>')
def rect(box,fill,stroke):
 d.rectangle(box,fill=fill,outline=stroke,width=2)
 x1,y1,x2,y2=box;sv.append(f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
def arrow(points,color='#36566D',dashed=False):
 d.line(points,fill=color,width=3)
 a,b=points[-2],points[-1];ang=math.atan2(b[1]-a[1],b[0]-a[0]);tri=[b,(b[0]-14*math.cos(ang-.45),b[1]-14*math.sin(ang-.45)),(b[0]-14*math.cos(ang+.45),b[1]-14*math.sin(ang+.45))];d.polygon(tri,fill=color)
 sv.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="3"/>')
 sv.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in tri)+f'" fill="{color}"/>')
text(35,20,'Governed cash-flow credit workflow',42,True)
text(35,78,'Moniepoint application of the five-article causal credit series',27)
xs=[35,530,1025];ys=[150,470,790];bw,bh=440,230
nodes=[
('1  Evidence and identity',['Case and correlation ID','Permissions and coverage','Provenance and cutoff','Article 5'],0,0,'#F0F4F7'),
('2  Reproducible analysis',['Cash, rules and rolling measures','Dated repayment paths','Credible and predictive','uncertainty - Articles 2, 5'],1,0,'#EAF2F8'),
('3  Policy and support',['Eligible actions and limits','Evidence support - Article 3','Approved experiments','and logged probabilities - A1'],2,0,'#F3EEFA'),
('4  Meaningful review',['Inspect evidence and options','Amend, defer or approve','Independent checker','where required - Article 5'],0,1,'#FFF4D6'),
('5  Authorised execution',['Expiring instruction','Separate execution service','Receipt and loan ledger','Reconciled cash - Article 5'],1,1,'#EAF2F8'),
('6  Monitor and support',['Check coverage first','Review verified changes','Customer conversation','Sequential service - Article 2'],2,1,'#FFF4D6'),
('7  Observed outcomes',['Assignment versus delivery','Cash, arrears and recovery','Customer outcomes','Evaluation - Articles 1-3'],0,2,'#EAF2F8'),
('8  Portfolio interface',['Aggregate cash and drawings','Funding and risk scenarios','Treasury and ALCO authority','Article 4'],1,2,'#F3EEFA'),
('9  Controlled learning',['Replay and validation','Shadow and bounded pilot','Version, expiry and rollback','Article 5'],2,2,'#F3EEFA')]
for title,lines,col,row,fill in nodes:
 x,y=xs[col],ys[row];rect((x,y,x+bw,y+bh),fill,'#6B8190');text(x+16,y+15,title,30,True)
 for k,line in enumerate(lines):text(x+16,y+65+35*k,line,27)
arrow([(475,265),(530,265)]);arrow([(970,265),(1025,265)])
arrow([(1245,380),(1245,425),(255,425),(255,470)])
arrow([(475,585),(530,585)]);arrow([(970,585),(1025,585)])
arrow([(1245,700),(1245,745),(255,745),(255,790)])
arrow([(475,905),(530,905)]);arrow([(255,1020),(255,1055),(1245,1055),(1245,1020)])
text(35,1090,'Feedback: correct evidence, reconsider terms, review servicing and approve each new release.',25)
text(35,1134,'Research interfaces: offer allocation, sequential control, selection analysis and Treasury models.',25)
text(35,1170,'The full diagrams show the decision branches, approval gates and return paths.',25)
sv.append('</svg>');im.save(P/'MONIEPOINT_GOVERNED_WORKFLOW_OVERVIEW.png',dpi=(180,180));(P/'MONIEPOINT_GOVERNED_WORKFLOW_OVERVIEW.svg').write_text('\n'.join(sv),encoding='utf-8')
manifest={'overview':{'image':'MONIEPOINT_GOVERNED_WORKFLOW_OVERVIEW.png','recommended_width_inches':6.3,'caption':'Governed cash-flow credit workflow. The overview connects the five articles; detailed panels distinguish current synthetic case components from research interfaces.'},'segments':items,'notes':['All original full PNG/SVG/Mermaid files remain unchanged.','Segments use overlapping connector bands and retain complete nodes.','Use the supplied orientation and width to preserve readable text within the page.','The compact overview belongs in the article body; detailed segments form a workflow supplement.']}
(P/'MONIEPOINT_WORKFLOW_WORD_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
for x in items:print(x['image'],x['pixel_width'],x['pixel_height'],x['orientation'],x['recommended_width_inches'])
print('Overview saved; segment count',len(items))


