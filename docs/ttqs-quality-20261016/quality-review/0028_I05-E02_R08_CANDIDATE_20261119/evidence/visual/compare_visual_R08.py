from pathlib import Path
from hashlib import sha256
from PIL import Image, ImageChops
import json
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118')
new=base/'qa'/'visual_R08_wordcom'/'pages'
old=base/'qa'/'visual_R07_wordcom'/'poppler_110dpi'
newfiles=sorted(new.glob('page-*.png'));oldfiles=sorted(old.glob('page-*.png'))
if len(newfiles)!=21 or len(oldfiles)!=24: raise SystemExit(f'PAGE_COUNT_MISMATCH new={len(newfiles)} old={len(oldfiles)}')
def pixelsha(p):
    im=Image.open(p).convert('RGB')
    return sha256(im.tobytes()).hexdigest().upper(), im.size, sum(Image.open(p).convert('L').histogram()[:250])
matches=[]
for i in range(20):
    n=Image.open(newfiles[i]).convert('RGB');o=Image.open(oldfiles[i]).convert('RGB')
    matches.append({'page':i+1,'same_pixels':n.size==o.size and ImageChops.difference(n,o).getbbox() is None,'new_size':n.size,'old_size':o.size,'new_pixel_sha256':sha256(n.tobytes()).hexdigest().upper(),'old_pixel_sha256':sha256(o.tobytes()).hexdigest().upper()})
n=Image.open(newfiles[20]).convert('RGB');o=Image.open(oldfiles[23]).convert('RGB')
last={'new_page':21,'old_page':24,'same_pixels':n.size==o.size and ImageChops.difference(n,o).getbbox() is None,'new_size':n.size,'old_size':o.size,'new_pixel_sha256':sha256(n.tobytes()).hexdigest().upper(),'old_pixel_sha256':sha256(o.tobytes()).hexdigest().upper()}
ink=[]
for i,p in enumerate(newfiles,1):
    im=Image.open(p).convert('L'); hist=im.histogram(); nonwhite=sum(hist[:250]); ink.append({'page':i,'nonwhite_pixels_lt250':nonwhite,'nonwhite_ratio':round(nonwhite/(im.width*im.height),6),'image_sha256':sha256(p.read_bytes()).hexdigest().upper()})
receipt={'schema':'TTQS_ONE_0028_VISUAL_COMPARE_R08','work_id':'TTQS_ONE_0028_I05-E02_VISUAL_COMPARE_R08_20261118','candidate_docx_sha256':'1EB4E9D26F761B57885AF7DC304BB76324AD85C7513FC858C82AF199D5273F70','r07_pdf_page_count':24,'r08_pdf_page_count':21,'rasterizer':'Poppler pdftoppm 110 dpi for both exact PDFs','unchanged_page_visual_comparison':matches,'last_page_comparison':last,'r08_page_ink_metrics':ink,'first_20_pixels_identical':all(x['same_pixels'] for x in matches),'r08_last_page_matches_r07_old_page24':last['same_pixels'],'blank_pages_detected':[x['page'] for x in ink if x['nonwhite_ratio']<0.0001],'result':'PENDING_RECEIPT_REVIEW'}
out=base/'qa'/'visual_R08_wordcom'/'VISUAL_COMPARE_R08.json'
if out.exists(): raise SystemExit('VISUAL_COMPARE_RECEIPT_EXISTS')
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'first_20_pixels_identical':receipt['first_20_pixels_identical'],'last_page_matches_old_page24':last['same_pixels'],'blank_pages':receipt['blank_pages_detected'],'page_ink':[(x['page'],x['nonwhite_ratio']) for x in ink],'receipt':str(out)},ensure_ascii=False))

