from pathlib import Path
import hashlib,json,datetime,sys
import pypdfium2 as pdfium
root=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0103_I18-E10_R01_20261022')
pdf=root/'render'/'0103_R02_word_native.pdf'
docx=root/'candidate'/'0103__I18-E10__感謝函取得與真偽查核工作紀錄_R02.docx'
out=root/'visual'/'0103_R02'/'pages'
out.mkdir(parents=True,exist_ok=True)
source_sha=hashlib.sha256(docx.read_bytes()).hexdigest()
doc=pdfium.PdfDocument(str(pdf)); pages=[]
for i in range(len(doc)):
 page=doc[i]; bitmap=page.render(scale=1.35); image=bitmap.to_pil(); path=out/f'page-{i+1:02d}.png'; image.save(path,format='PNG',optimize=True)
 pages.append({'page':i+1,'width_px':image.width,'height_px':image.height,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'pdf_points':[round(float(x),2) for x in page.get_size()]}); page.close()
doc.close()
receipt={'receipt_id':'TTQS-0103-I18-E10-R02-WORD-PDF-RASTER','observed_at_local':datetime.datetime.now().astimezone().isoformat(timespec='seconds'),'candidate_docx_sha256':source_sha,'candidate_docx_sha256_after_render':hashlib.sha256(docx.read_bytes()).hexdigest(),'pdf_path':str(pdf),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'page_count':len(pages),'renderer':'Bundled pypdfium2 rasterizer; source PDF exported by Microsoft Word COM using isolated new PID','render_scale':1.35,'pages':pages}
rpath=root/'evidence'/'raster_qa_0103_R02.json'; rpath.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha_before':source_sha,'candidate_sha_after':receipt['candidate_docx_sha256_after_render'],'pdf_sha256':receipt['pdf_sha256'],'pages':len(pages),'receipt':str(rpath),'first_page_px':pages[0]['width_px'] if pages else None},ensure_ascii=False))
