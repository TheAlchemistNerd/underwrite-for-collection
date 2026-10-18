from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'output/moniepoint_cashflow_case_2026-10-18'; CHARTS=ROOT/'publications/linkedin/moniepoint_cashflow_2026-10-14/charts'
CHARTS.mkdir(parents=True,exist_ok=True)
W,H=1800,1100
C={'ink':'#142D45','blue':'#006DB0','orange':'#C56516','teal':'#008577','red':'#A82B37','grid':'#D9E1E7','muted':'#4E5F6F'}
FONT=Path('C:/Windows/Fonts/arial.ttf');BOLD=Path('C:/Windows/Fonts/arialbd.ttf')
def ft(s,b=False):return ImageFont.truetype(str(BOLD if b else FONT),s)
def canvas(title,subtitle):
    im=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(im)
    d.text((70,42),title,font=ft(48,True),fill=C['ink']);d.text((70,113),subtitle,font=ft(28),fill=C['muted'])
    d.text((70,1050),'Synthetic teaching case | KES | Reproduce from the exported transaction and loan ledgers',font=ft(24),fill=C['muted'])
    return im,d

def save(im,name):im.save(CHARTS/name)
def rows(name):
    with (OUT/name/'merchant_daily.csv').open(encoding='utf8') as f:return [{k:float(v) for k,v in row.items()} for row in csv.DictReader(f)]
def axes(d,xmin,xmax,ymin,ymax,yticks,xlabel,ylabel):
    L,T,R,B=170,260,1710,910
    fx=lambda x:L+(x-xmin)/(xmax-xmin)*(R-L);fy=lambda y:B-(y-ymin)/(ymax-ymin)*(B-T)
    for y in yticks:
        yy=fy(y);d.line((L,yy,R,yy),fill=C['grid'],width=2);d.text((L-30,yy),f'{y:,.0f}',font=ft(25),fill=C['muted'],anchor='rm')
    for x in range(int(xmin),int(xmax)+1,30):
        xx=fx(x);d.text((xx,B+22),str(x),font=ft(25),fill=C['muted'],anchor='mt')
    d.line((L,T,L,B,R,B),fill=C['ink'],width=3)
    d.text((L,T-40),ylabel,font=ft(25,True),fill=C['ink']);d.text(((L+R)/2,B+75),xlabel,font=ft(28),fill=C['ink'],anchor='mt')
    return fx,fy

def legend(d,items,y=185):
    x=170
    for name,color in items:
        d.line((x,y+15,x+50,y+15),fill=color,width=6);d.text((x+65,y),name,font=ft(28),fill=C['ink']);x+=65+d.textlength(name,font=ft(28))+60

snaps=json.loads((OUT/'decision_snapshots.json').read_text());s=snaps['baseline']
im,d=canvas('Uncertainty changes the proposed repayment','Three observed monthly residuals: KES20,000, KES30,000 and KES25,000')
L,R=400,1700; fx=lambda x:L+x/50000*(R-L)
for v in range(0,50001,10000):
    x=fx(v);d.line((x,260,x,850),fill=C['grid'],width=2);d.text((x,880),f'{v:,.0f}',font=ft(26),fill=C['muted'],anchor='mt')
for y,label,lo,hi,col in [(400,'Mean cash residual',s['mean_credible_low'],s['mean_credible_high'],C['blue']),(650,'Next month cash',s['predictive_low'],s['predictive_high'],C['teal'])]:
    d.text((70,y),label,font=ft(29,True),fill=C['ink'],anchor='lm');d.line((fx(lo),y,fx(hi),y),fill=col,width=14)
    d.ellipse((fx(25000)-10,y-10,fx(25000)+10,y+10),fill=col)
    d.text((fx(lo),y+35),f'{lo:,.0f}',font=ft(27),fill=col,anchor='mt');d.text((fx(hi),y+35),f'{hi:,.0f}',font=ft(27),fill=col,anchor='mt')
for val,lab,col,yy in [(11000,'Revised payment 11,000',C['orange'],220),(35000,'Requested payment 35,000',C['red'],175)]:
    x=fx(val)
    for y in range(260,850,24):d.line((x,y,x,y+13),fill=col,width=3)
    d.text((x,yy),lab,font=ft(27,True),fill=col,anchor='mt')
d.text((70,962),'95% mean credible interval and 95% predictive interval answer different questions.',font=ft(29,True),fill=C['ink'])
d.text((70,1003),'Normal likelihood; assumed monthly standard deviation KES8,000; prior mean KES25,000, SD KES15,000.',font=ft(24),fill=C['muted'])
save(im,'MONIEPOINT_CASE_01_CASH_UNCERTAINTY.png')

im,d=canvas('Settlement timing changes the merchant cash path','The same planned trading receipts arrive fifteen days later in the second month')
series=[('baseline','Baseline',C['blue']),('delayed_settlement','Delay',C['orange']),('reviewed_reschedule','Reviewed schedule',C['teal'])]
legend(d,[(label,c) for _,label,c in series]);fx,fy=axes(d,0,120,0,260000,range(0,260001,40000),'Day after first disbursement','Merchant cash KES')
for name,label,c in series:
    pts=[(fx(0),fy(50000))]+[(fx(r['day']),fy(r['closing_cash'])) for r in rows(name) if r['day']<=120];d.line(pts,fill=c,width=5)
y=fy(20000)
for x in range(170,1710,24):d.line((x,y,x+12,y),fill=C['red'],width=2)
d.text((70,1010),'The KES20,000 floor limits loan collection. Trading bills can still exhaust cash; household shortfalls are recorded.',font=ft(23),fill=C['muted'])
save(im,'MONIEPOINT_CASE_02_DAILY_CASH_AND_TIMING.png')

im,d=canvas('A schedule change has an observable cash cost','First loan only: original dues, approved revised dues and actual received payments')
legend(d,[('Original schedule',C['blue']),('Delayed cash received',C['orange']),('Revised schedule',C['teal'])]);fx,fy=axes(d,0,120,0,36000,range(0,36001,6000),'Day after disbursement','Cumulative payments KES')
for name,col,mode in [('baseline',C['blue'],'due'),('delayed_settlement',C['orange'],'paid'),('reviewed_reschedule',C['teal'],'due')]:
    pts=[];total=0
    for day in range(121):
        if mode=='due':total=sum(11000 for x in ((30,60,90) if name=='baseline' else (30,75,105)) if x<=day)
        else:
            row=next((r for r in rows(name) if r['day']==day),None)
            if row and day<=90: total+=row['new_loan_principal_paid']+row['new_loan_fee_paid']
        pts.append((fx(day),fy(total)))
    d.line(pts,fill=col,width=5)
d.text((70,1010),'The extension is approved on day45. Later repayments incur funding costs; the receipt ledger preserves original and revised terms.',font=ft(23),fill=C['muted'])
save(im,'MONIEPOINT_CASE_03_DUES_AND_RECEIPTS.png')

summary={x['scenario']:x for x in json.loads((OUT/'summary.json').read_text())}
im,d=canvas('Cash collection and lender contribution are reconciled','Three cycles are possible over 300 days; stress changes repeat eligibility and realised losses')
names=[('baseline','Baseline'),('delayed_settlement','Settlement delay'),('reviewed_reschedule','Reviewed extension'),('margin_stress','Margin pressure'),('sustained_stress','Persistent sales loss')]
L,R,T,B=170,1690,270,890;zero=B-(0+25000)/33000*(B-T);fy=lambda v:B-(v+25000)/33000*(B-T)
for y in (-25000,-20000,-15000,-10000,-5000,0,5000):
    yy=fy(y);d.line((L,yy,R,yy),fill=C['grid'],width=2);d.text((L-20,yy),f'{y:,}',font=ft(25),fill=C['muted'],anchor='rm')
d.text((170,210),'Lender contribution KES',font=ft(27,True),fill=C['ink'])
for i,(key,label) in enumerate(names):
    x=L+70+i*300;v=summary[key]['lender_contribution'];y=fy(v);col=C['blue'] if v>=0 else C['red'];d.rectangle((x,min(y,zero),x+150,max(y,zero)),fill=col)
    d.text((x+75,y-35 if v>=0 else y+15),f'{v:,.0f}',font=ft(28,True),fill=col,anchor='mt')
    for j,line in enumerate(label.split(' ')):d.text((x+75,920+j*32),line,font=ft(26),fill=C['ink'],anchor='mt')
d.text((70,1010),'Contribution includes fees, funding through default, origination, servicing, workout cost and net realised principal loss.',font=ft(24),fill=C['muted'])
save(im,'MONIEPOINT_CASE_04_LENDER_CONTRIBUTION.png')
manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in CHARTS.glob('MONIEPOINT_CASE_*.png')}
(CHARTS/'MONIEPOINT_CASE_CHART_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({'charts':list(manifest)},indent=2))
