from pathlib import Path
from pypdfium2 import PdfDocument
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib,json
base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029")
qa=base/'qa'/'R08E_REPORT_TABLE_START_20261031'
pdf=qa/'0012_I02-E03_R08E_WORD_RENDER.pdf'
pages=qa/'pages';pages.mkdir(parents=True,exist_ok=True)
old=base/'qa'/'R08B_SCOPED_LAYOUT_REPAIR_20261031'/'WORD_RENDER_INDEX_R08E.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
olditems={}
if old.exists():
 o=json.loads(old.read_text(encoding='utf-8'))
 olditems={int(x['page']):x['png_sha256'] for x in o.get('pages',[])}
pdfdoc=PdfDocument(str(pdf));items=[]
for i in range(len(pdfdoc)):
 page=pdfdoc[i]; bmp=page.render(scale=120/72); im=bmp.to_pil(); path=pages/f'page-{i+1:02d}.png';im.save(path,optimize=False)
 h=sha(path);items.append({'page':i+1,'width':im.width,'height':im.height,'png_sha256':h,'path':str(path),'same_as_r08d_page':(olditems.get(i+1)==h)})
report={'receipt_id':'0012_I02-E03_R08E_PAGE_RENDER_INDEX','observed_at_local':datetime.now(ZoneInfo('Asia/Taipei')).isoformat(timespec='seconds'),'candidate_sha256':sha(base/'candidate'/'0012_I02-E03_R08E.docx'),'pdf_sha256':sha(pdf),'pdf_pages':len(pdfdoc),'render_dpi':120,'renderer':'pypdfium2','pages':items}
(qa/'WORD_RENDER_INDEX_R08E.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pdf_pages':len(pdfdoc),'pdf_sha256':report['pdf_sha256'],'unchanged_page_numbers':[x['page'] for x in items if x['same_as_r08d_page']],'changed_page_numbers':[x['page'] for x in items if not x['same_as_r08d_page']],'index_sha256':sha(qa/'WORD_RENDER_INDEX_R08E.json')},ensure_ascii=False,indent=2))
