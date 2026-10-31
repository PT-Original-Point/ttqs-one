from pathlib import Path
from PIL import Image, ImageChops
import hashlib,json,re
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029')
old=root/'qa'/'render_R06_final6'; new=root/'qa'/'render_R09_instrumented'
pat=re.compile(r'page-(\d+)\.png$',re.I)
def pages(folder):
 d={}
 for p in folder.glob('page-*.png'):
  m=pat.search(p.name)
  if m:d[int(m.group(1))]=p
 return d
a,b=pages(old),pages(new)
ident=[]; changed=[]; missing=[]; rows=[]
for n in sorted(set(a)|set(b)):
 if n not in a or n not in b: missing.append(n); continue
 with Image.open(a[n]) as im1,Image.open(b[n]) as im2:
  x=im1.convert('RGB'); y=im2.convert('RGB')
  same=x.size==y.size and ImageChops.difference(x,y).getbbox() is None
  (ident if same else changed).append(n)
  rows.append({'page':n,'old_size':list(x.size),'new_size':list(y.size),'pixel_identical_to_R06':same,'new_png_sha256':hashlib.sha256(b[n].read_bytes()).hexdigest()})
out={'document_id':'0013','requirement_id':'I02-E04','candidate_sha256':hashlib.sha256((root/'candidate'/'0013_I02-E04_R09.docx').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((new/'0013_I02-E04_R09_WORD_NATIVE.pdf').read_bytes()).hexdigest(),'old_R06_visual_sha':'3e1b0ce939ea4e1b3fe22adec1cbdab492af78d6b9a5646f41ddd394c4aa3d09','old_R06_page_count':len(a),'new_R09_page_count':len(b),'all_pages_accounted':len(a)==25 and len(b)==25 and not missing,'pixel_identical_pages':ident,'changed_pages':changed,'missing_pages':missing,'page_details':rows,'visual_verdict':'PENDING_DIRECT_INSPECTION'}
path=new/'pixel_comparison_R06_R09.json';path.write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
