import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image
base=Path(sys.argv[1]); qa=base/'qa'; doc=base/'candidate'/'0011_I02-E02_R09.docx'; pdf=qa/'0011_I02-E02_R09_WORD_NATIVE.pdf'; renders=qa/'render_R09'; pages=[]
for i in range(1,29):
 p=renders/f'page-{i:02d}.png'; b=p.read_bytes()
 with Image.open(p) as im: pages.append({'page':i,'sha256':hashlib.sha256(b).hexdigest(),'dimensions':[im.width,im.height]})
receipt={
 'receipt_id':'0011_I02-E02_R09_WORD_NATIVE_VISUAL_QA',
 'observed_at_utc':datetime.now(timezone.utc).isoformat(),
 'document_id':'0011','requirement_id':'I02-E02','candidate_sha256':hashlib.sha256(doc.read_bytes()).hexdigest(),
 'native_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'native_pdf_bytes':pdf.stat().st_size,
 'page_count':len(pages),'visual_status':'PASS_FOR_LAYOUT_READABILITY_ONLY',
 'review_scope':'Direct visual inspection of all 28 page PNGs rendered from the R09 PDF exported through Microsoft Word COM. Pages 1-28 are enumerated by exact PNG SHA-256 below.',
 'confirmed_repairs':['Page 8: §6.6 heading and explanatory paragraph no longer leave a table header stranded at the page foot; full HOLD matrix starts on page 9.','Page 10: Table 7-5 caption is kept with the table at the start of page 11; no caption-only page foot.'],
 'visual_checks':{'all_28_pages_present':len(pages)==28,'no_missing_pages':True,'no_observed_clipping_or_overlap':True,'tables_readable_at_render_size':True,'sample_real_boundary_legible':True,'semantic_acceptance_included':False},
 'pages':pages,
 'semantic_review':'PENDING; independent OpenCode route cooling after HTTP 429; this visual receipt does not grant semantic PASS',
 'formal_acceptance':'UNKNOWN','artifact_state':'CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED'}
out=qa/'visual_qa_R09.json'; out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'visual_status':receipt['visual_status'],'candidate_sha256':receipt['candidate_sha256'],'pdf_sha256':receipt['native_pdf_sha256'],'pages':len(pages),'receipt':str(out)},ensure_ascii=True,indent=2))
