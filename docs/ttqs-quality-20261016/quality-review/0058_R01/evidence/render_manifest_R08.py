from pathlib import Path
import hashlib, json, math, re
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0058_R01')
out=root/'evidence'/'render_R08'
pdf=out/'0058_R08.pdf'
pages_dir=out/'pages'; pages_dir.mkdir(parents=True,exist_ok=True)
doc=pdfium.PdfDocument(str(pdf)); pages=[]; records=[]
for i in range(len(doc)):
    page=doc[i]; bitmap=page.render(scale=1.6); im=bitmap.to_pil().convert('RGB')
    p=pages_dir/f'page-{i+1:02d}.png'; im.save(p,optimize=True)
    records.append({'page':i+1,'png':str(p.relative_to(root)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'width':im.width,'height':im.height})
    pages.append(im)
for start in range(0,len(pages),4):
    group=pages[start:start+4]; thumbs=[]
    for im in group:
        cp=im.copy(); cp.thumbnail((650,900)); canvas=Image.new('RGB',(670,940),'white'); canvas.paste(cp,((670-cp.width)//2,25));
        d=ImageDraw.Draw(canvas); d.text((12,8),f'Page {start+len(thumbs)+1}',fill='black'); thumbs.append(canvas)
    sheet=Image.new('RGB',(1340,1880),(235,235,235))
    for j,im in enumerate(thumbs): sheet.paste(im,((j%2)*670,(j//2)*940))
    name=f'contact-{start+1:02d}-{min(start+4,len(pages)):02d}.jpg'; sheet.save(out/name,quality=88,optimize=True)
reader=PdfReader(str(pdf)); all_text='\n'.join((p.extract_text() or '') for p in reader.pages)
text_hash=hashlib.sha256(re.sub(r'\s+',' ',all_text).encode()).hexdigest()
manifest={'candidate_sha256':'0DFCAAE1FF9943E46C1B9D527C3DF34FA61048547268C482D0DD378E44D7C58B','pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'page_count':len(pages),'render_scale':1.6,'whole_pdf_normalized_text_sha256':text_hash,'pages':records,'contact_sheets':[p.name for p in sorted(out.glob('contact-*.jpg'))]}
(out/'render_manifest_R08.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
r06=root/'evidence'/'render_R06_final'/'0058_R06.pdf'; r07=root/'evidence'/'render_R07'/'0058_R07.pdf'
for label,fp in [('R06',r06),('R07',r07)]:
    rr=PdfReader(str(fp)); tx='\n'.join((p.extract_text() or '') for p in rr.pages); print(label,'pages',len(rr.pages),'normtext_sha',hashlib.sha256(re.sub(r'\s+',' ',tx).encode()).hexdigest(),'chars',len(tx))
print('R08 pages',len(pages),'pdf_sha',manifest['pdf_sha256'],'normtext_sha',text_hash,'chars',len(all_text),'contacts',manifest['contact_sheets'])