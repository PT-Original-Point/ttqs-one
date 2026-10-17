from pathlib import Path
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image,ImageDraw
import hashlib,json,sys
from datetime import datetime,timezone
sys.stdout.reconfigure(encoding='utf-8')
pkg=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R02')
pdf=pkg/'evidence/render_final_R02_final/0053_R02_Word_export.pdf'; out=pdf.parent
reader=PdfReader(str(pdf)); doc=pdfium.PdfDocument(str(pdf)); pages=[]; texts=[]
for i in range(len(doc)):
    page=doc[i]; image=page.render(scale=2).to_pil().convert('RGB')
    path=out/f'page-{i+1:02d}.png'; image.save(path,optimize=True)
    pages.append({'page':i+1,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'width':image.width,'height':image.height})
    texts.append(reader.pages[i].extract_text() or '')
manifest={'pdf_path':str(pdf),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_bytes':pdf.stat().st_size,'page_count':len(reader.pages),'rendered_png_count':len(pages),'pages':pages,'render_engine':'pypdfium2 from Microsoft Word-exported PDF','rendered_at_utc':datetime.now(timezone.utc).isoformat()}
(out/'render_manifest_R02_final.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
thumb_w,cols,margin,label_h=340,3,18,30; cards=[]
for i,f in enumerate([Path(x['path']) for x in pages],1):
 im=Image.open(f).convert('RGB'); h=round(im.height*thumb_w/im.width); im=im.resize((thumb_w,h),Image.Resampling.LANCZOS); c=Image.new('RGB',(thumb_w,h+label_h),'white'); c.paste(im,(0,label_h)); ImageDraw.Draw(c).text((8,7),f'PAGE {i:02d}',fill='#10243A'); cards.append(c)
rows=(len(cards)+cols-1)//cols; cell_h=max(c.height for c in cards); sheet=Image.new('RGB',(cols*thumb_w+(cols+1)*margin,rows*cell_h+(rows+1)*margin),'#DCE5EF')
for i,c in enumerate(cards): sheet.paste(c,(margin+(i%cols)*(thumb_w+margin),margin+(i//cols)*(cell_h+margin)))
contact=out.parent/'visual_contact_sheet_R02_final.png'; sheet.save(contact,optimize=True)
(out/'rendered_page_text_R02_final.txt').write_text('\n\n'.join(f'--- PAGE {i+1} ---\n{t}' for i,t in enumerate(texts)),encoding='utf-8')
print(json.dumps({'pdf_sha256':manifest['pdf_sha256'],'page_count':manifest['page_count'],'contact_sheet':str(contact),'contact_sheet_sha256':hashlib.sha256(contact.read_bytes()).hexdigest(),'page10_excerpt':texts[9][-900:]},ensure_ascii=False,indent=2))
