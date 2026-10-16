"""Render Article 4 hedge quantities with independent numeric annotation positions."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
base=Path(__file__).resolve().parent.parent
im=Image.new("RGB",(2400,1500),"white");d=ImageDraw.Draw(im)
navy="#19384b";grey="#657d89";grid="#dde6eb";blue="#4d839c";orange="#dd8a32"
def font(n,bold=False):return ImageFont.truetype("C:/Windows/Fonts/"+("segoeuib.ttf" if bold else "segoeui.ttf"),n)
def text(x,y,s,size=34,color=navy,bold=False,anchor="la"):d.text((x,y),s,font=font(size,bold),fill=color,anchor=anchor)
text(170,72,"Illustrative hedge trade-off",64,bold=True)
text(170,170,"Risk reduction and funding demand under the same hypothetical joint stress",36,grey)
d.line((170,225,2230,225),fill=grid,width=3)
for x,c,label in [(680,blue,"Before hedge"),(1180,orange,"With hedge")]:
 d.rectangle((x,257,x+48,305),fill=c);text(x+70,256,label,36,bold=True)
left,right,top,bottom=255,2250,325,1110
for value in range(6):
 y=bottom-(bottom-top)*value/5;d.line((left,y,right,y),fill=grid,width=2);text(left-28,y,f"{value:.1f}",34,grey,anchor="rm")
d.line((left,top,left,bottom,right,bottom),fill=grey,width=3)
text(68,680,"KES bn",32,grey)
for center,values,caption,annotation,color in [(830,[2.0,1.2],"EVE loss magnitude","40% less EVE loss","#148c82"),(1700,[1.0,4.0],"Peak collateral need","300% more collateral","#bf4c4f")]:
 text(center,365,annotation,35,color,True,anchor="ma")
 for x,v,c in [(center-150,values[0],blue),(center+150,values[1],orange)]:
  y=bottom-(bottom-top)*v/5;d.rectangle((x-110,y,x+110,bottom),fill=c);text(x,y-55,f"{v:.1f}",36,bold=True,anchor="ma")
 text(center,1170,caption,35,bold=True,anchor="ma")
text(170,1370,"The swap reduces EVE loss by KES 0.8bn; modelled peak collateral increases by KES 3.0bn.",31,grey)
text(170,1420,"Hypothetical joint stress; same figures as Article 4 and Appendix A4.",27,grey)
im.save(base/"linkedin_diagrams/04_hedge_eve_collateral_tradeoff.png")
