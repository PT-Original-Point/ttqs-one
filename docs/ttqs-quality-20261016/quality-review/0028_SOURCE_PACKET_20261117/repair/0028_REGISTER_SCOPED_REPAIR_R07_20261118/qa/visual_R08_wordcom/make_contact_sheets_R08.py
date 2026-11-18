from pathlib import Path
from PIL import Image, ImageDraw
from hashlib import sha256
import json
folder=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118\qa\visual_R08_wordcom')
pages=sorted((folder/'pages').glob('page-*.png'))
if len(pages)!=21: raise SystemExit('EXPECTED_21_R08_PAGES')
made=[]
for batch,start in enumerate(range(0,21,6),1):
    group=pages[start:start+6]
    cell_w,cell_h,label_h=460,665,24
    sheet=Image.new('RGB',(cell_w*2+30,(cell_h+label_h)*3+30),'#e7e9ec')
    draw=ImageDraw.Draw(sheet)
    for k,path in enumerate(group):
        im=Image.open(path).convert('RGB')
        im.thumbnail((cell_w,cell_h),Image.Resampling.LANCZOS)
        x=15+(k%2)*(cell_w+10)+(cell_w-im.width)//2
        y=15+(k//2)*(cell_h+label_h+5)+label_h
        draw.text((15+(k%2)*(cell_w+10)+10,15+(k//2)*(cell_h+label_h+5)+4),f'PAGE {start+k+1:02d}',fill='#222')
        sheet.paste(im,(x,y))
    name=f'CONTACT_SHEET_R08_{start+1:02d}_{start+len(group):02d}.png'
    out=folder/name
    if out.exists(): raise SystemExit(f'EXISTS {out}')
    sheet.save(out,optimize=True)
    made.append({'file':str(out),'sha256':sha256(out.read_bytes()).hexdigest().upper(),'pages':[start+1,start+len(group)]})
print(json.dumps(made,ensure_ascii=False))

