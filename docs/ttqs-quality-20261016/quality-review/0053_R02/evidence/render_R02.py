from pathlib import Path
from pypdf import PdfReader
import pypdfium2 as pdfium
import hashlib,json,sys
from datetime import datetime,timezone
sys.stdout.reconfigure(encoding='utf-8')
pkg=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R02')
pdf=pkg/'evidence/render_final_R02/0053_R02_Word_export.pdf'; out=pdf.parent
reader=PdfReader(str(pdf)); doc=pdfium.PdfDocument(str(pdf)); pages=[]
for i in range(len(doc)):
    page=doc[i]; image=page.render(scale=2).to_pil().convert('RGB')
    path=out/f'page-{i+1:02d}.png'; image.save(path,optimize=True)
    pages.append({'page':i+1,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'width':image.width,'height':image.height})
manifest={'pdf_path':str(pdf),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_bytes':pdf.stat().st_size,'page_count':len(reader.pages),'rendered_png_count':len(pages),'pages':pages,'render_engine':'pypdfium2 4x scale from Microsoft Word-exported PDF','rendered_at_utc':datetime.now(timezone.utc).isoformat()}
(out/'render_manifest_R02.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in manifest.items() if k!='pages'},ensure_ascii=False,indent=2))
