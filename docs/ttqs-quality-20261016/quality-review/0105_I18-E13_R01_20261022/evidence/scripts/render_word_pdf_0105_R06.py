from pathlib import Path
import hashlib,json,datetime
import pypdfium2 as pdfium
root=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022')
pdf=root/'visual/0105_R06/0105_R06_Word_native.pdf'
out=root/'visual/0105_R06/pages';out.mkdir(parents=True,exist_ok=True)
doc=pdfium.PdfDocument(str(pdf));pages=[]
for i in range(len(doc)):
 page=doc[i];bitmap=page.render(scale=150/72);img=bitmap.to_pil();p=out/f'page-{i+1:03d}.png';img.save(p,optimize=True)
 pages.append({'page':i+1,'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'width_px':img.width,'height_px':img.height})
receipt={'receipt_id':'TTQS-0105-VISUAL-RENDER-R06','rendered_at_tpe':datetime.datetime.now().astimezone().isoformat(),'doc_id':'0105','requirement_id':'I18-E13','candidate_sha256':hashlib.sha256((root/'candidate/0105_I18-E13_績效改善調查與課後行動計畫追蹤套件_R06.docx').read_bytes()).hexdigest(),'renderer':'Microsoft Word native PDF export + bundled pypdfium2 rasterizer at 150 dpi','input_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'page_count':len(doc),'pages':pages}
p=(root/'evidence/visual_render_receipt_0105_R06.json');p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'page_count':len(doc),'candidate_sha256':receipt['candidate_sha256'],'pdf_sha256':receipt['input_pdf_sha256'],'first_page':pages[0],'last_page':pages[-1],'page_dir':str(out)},ensure_ascii=False))
