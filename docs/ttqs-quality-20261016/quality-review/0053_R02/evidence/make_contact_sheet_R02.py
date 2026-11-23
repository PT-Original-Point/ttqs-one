from pathlib import Path
from PIL import Image,ImageDraw
p=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R02\evidence\render_final_R02')
files=sorted(p.glob('page-*.png'))
thumb_w,cols,margin,label_h=340,3,18,30
cards=[]
for i,f in enumerate(files,1):
 im=Image.open(f).convert('RGB'); h=round(im.height*thumb_w/im.width); im=im.resize((thumb_w,h),Image.Resampling.LANCZOS)
 card=Image.new('RGB',(thumb_w,h+label_h),'white'); card.paste(im,(0,label_h)); ImageDraw.Draw(card).text((8,7),f'PAGE {i:02d}',fill='#10243A'); cards.append(card)
rows=(len(cards)+cols-1)//cols; ch=max(x.height for x in cards)
s=Image.new('RGB',(cols*thumb_w+(cols+1)*margin,rows*ch+(rows+1)*margin),'#DCE5EF')
for i,im in enumerate(cards): s.paste(im,(margin+(i%cols)*(thumb_w+margin),margin+(i//cols)*(ch+margin)))
out=p.parent/'visual_contact_sheet_R02.png'; s.save(out,optimize=True); print(out)
