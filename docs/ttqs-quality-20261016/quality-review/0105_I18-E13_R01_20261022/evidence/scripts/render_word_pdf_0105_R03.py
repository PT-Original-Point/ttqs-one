from pathlib import Path
import hashlib,json,datetime
import pypdfium2 as pdfium
root=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022')
pdf=root/'visual/0105_R03/0105_R03_word_native.pdf'
out=root/'visual/0105_R03/pages';out.mkdir(parents=True,exist_ok=True)
doc=pdfium.PdfDocument(str(pdf)); pages=[]
for i in range(len(doc)):
 page=doc[i];bitmap=page.render(scale=150/72);img=bitmap.to_pil();p=out/f'page-{i+1:03d}.png';img.save(p,optimize=True)
 pages.append({'page':i+1,'path':str(p),'width_px':img.width,'height_px':img.height,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
receipt={'receipt_id':'TTQS-0105-VISUAL-RENDER-R03','rendered_at_tpe':datetime.datetime.now().astimezone().isoformat(),'renderer':'Microsoft Word native PDF export + bundled pypdfium2 rasterizer at 150 dpi','input_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'page_count':len(doc),'pages':pages}
(root/'evidence/visual_render_receipt_0105_R03.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'page_count':len(doc),'pdf_sha':receipt['input_pdf_sha256'],'first_page':pages[0],'last_page':pages[-1],'page_dir':str(out)}))