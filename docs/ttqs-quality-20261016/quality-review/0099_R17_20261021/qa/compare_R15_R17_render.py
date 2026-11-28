from PIL import Image, ImageChops
from pathlib import Path
import json
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0099_R01_BLUEPRINT_R01\render')
a=sorted((root/'R15_compare').glob('page-*.png')); b=sorted((root/'R17_compare').glob('page-*.png'))
rows=[]
for x,y in zip(a,b):
 i=Image.open(x).convert('RGB'); j=Image.open(y).convert('RGB')
 if i.size!=j.size: rows.append({'page':x.stem,'different':True,'size15':i.size,'size17':j.size}); continue
 d=ImageChops.difference(i,j); h=d.histogram(); n=i.width*i.height*3
 mean=sum(v*(idx%256) for idx,v in enumerate(h))/n
 rows.append({'page':int(x.stem.split('-')[-1]),'different':mean>0,'mean_abs_channel_diff':round(mean,6)})
print(json.dumps({'r15_pages':len(a),'r17_pages':len(b),'changed_pages':[r for r in rows if r['different']]},ensure_ascii=False))
