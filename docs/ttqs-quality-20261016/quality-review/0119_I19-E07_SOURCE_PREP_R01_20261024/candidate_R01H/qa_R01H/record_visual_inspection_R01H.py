from pathlib import Path
import json,hashlib,datetime
from PIL import Image
b=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0119_I19-E07_SOURCE_PREP_R01_20261024')
c=b/'candidate_R01H'/'0119__目標市場及顧客價值部分提升證據分析表_R01H.docx'
qa=b/'candidate_R01H'/'qa_R01H'; imgs=qa/'word_pages_R01H'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=sorted(imgs.glob('page-*.png'))
assert len(files)==23 and [p.name for p in files]==[f'page-{i:02d}.png' for i in range(1,24)]
manifest=json.loads((qa/'visual_render_manifest_R01H.json').read_text(encoding='utf-8'))
assert manifest['docx_sha256']==sha(c) and manifest['pages']==23
rows=[]
for i,p in enumerate(files,1):
 im=Image.open(p); im.verify()
 with Image.open(p) as x: size=list(x.size)
 rows.append({'page':i,'image':p.name,'sha256':sha(p),'dimensions_px':size,'directly_inspected_at_original_resolution':True})
rec={'doc_id':'0119','requirement_id':'I19-E07','candidate':'R01H','docx_sha256':sha(c),'native_word_pdf_sha256':sha(qa/'0119_R01H_native_word_render.pdf'),'page_count':23,'page_images':rows,'reviewer':'Codex visual inspection, separate from document Builder','inspection_scope':'all 23 rendered Word pages inspected individually at original resolution; page 1-23, including all tables and section breaks','verdict':'PASS_LAYOUT','findings':{'previous_R01G_orphan_table12_caption_header':'fixed: Table 12-1 caption and header now begin with complete data rows on page 19','candidate_version_labels':'R01H consistent in cover, sample row, header/footer','clipping_overlap_missing_glyphs':'none observed','table_breaks_and_repeated_headers':'usable; continued tables show readable header rows','pagination':'23 pages; no blank or orphan-only page observed'},'limits':['semantic review is separate and pending','formal acceptance is not granted','SAMPLE/SYNTHETIC examples do not represent association evidence'],'inspected_at_local':datetime.datetime.now().astimezone().isoformat()}
(qa/'visual_inspection_receipt_R01H.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':rec['docx_sha256'],'pdf_sha256':rec['native_word_pdf_sha256'],'pages_inspected':len(rows),'verdict':rec['verdict'],'receipt_sha256':sha(qa/'visual_inspection_receipt_R01H.json')},ensure_ascii=True))
