from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import json,math
root=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0103_I18-E10_R01_20261022')
pages=sorted((root/'visual'/'0103_R03'/'pages').glob('page-*.png'))
out=root/'visual'/'0103_R03'/'contact_sheets';out.mkdir(parents=True,exist_ok=True)
thumb_w=402; cols=2; rows=3; pad=22; title_h=34; cell_h=thumb_w*1137//804
sheets=[]
for start in range(0,len(pages),cols*rows):
 batch=pages[start:start+cols*rows]
 canvas=Image.new('RGB',(pad+(thumb_w+pad)*cols,pad+(cell_h+title_h+pad)*rows),'#e7e9ed')
 d=ImageDraw.Draw(canvas)
 for j,p in enumerate(batch):
  idx=start+j; im=Image.open(p).convert('RGB').resize((thumb_w,cell_h),Image.Resampling.LANCZOS)
  x=pad+(j%cols)*(thumb_w+pad); y=pad+(j//cols)*(cell_h+title_h+pad)
  d.text((x,y),f'PAGE {idx+1:02d}',fill='#111827')
  canvas.paste(im,(x,y+title_h))
 f=out/f'contact-{start//(cols*rows)+1:02d}.jpg';canvas.save(f,quality=88,optimize=True)
 sheets.append({'path':str(f),'bytes':f.stat().st_size})
print(json.dumps({'page_count':len(pages),'contact_sheets':sheets},ensure_ascii=False))
