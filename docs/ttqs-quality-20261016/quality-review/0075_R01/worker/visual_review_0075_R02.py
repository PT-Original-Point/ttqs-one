from pathlib import Path
import hashlib,json
root=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0075_R01')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
docx=root/'candidate'/'0075_R02.docx'; pdf=root/'evidence'/'0075_R02_word_render_ca81a479.pdf'; render=root/'evidence'/'render_word_R02'
pages=sorted(render.glob('page-*.png'))
result={
 'schema':'TTQS_ONE_0075_R02_VISUAL_REVIEW.v1',
 'document_id':'0075','requirement_id':'I17A-E03','official_checkbox_serial':'082',
 'candidate_docx_sha256':sha(docx),'renderer':'Microsoft Word COM ExportAsFixedFormat to PDF; Poppler rasterization at 120 dpi',
 'pdf':{'path':str(pdf.relative_to(root)),'sha256':sha(pdf),'page_count':len(pages)},
 'page_images':[{'page':i+1,'path':str(p.relative_to(root)),'sha256':sha(p),'bytes':p.stat().st_size} for i,p in enumerate(pages)],
 'inspection':{'full_resolution_pages_inspected':len(pages),'contact_sheet_pages_inspected':len(pages),'focused_pages':[5,11,12,13,14,15,16,21], 'page_15_10_1_orphan_header':'FIXED_IN_R02; section heading and checklist header now stay with first body row on page 16', 'page_21':'Contains calculation continuation and glossary; intentional content, not blank', 'clipping':'NONE_OBSERVED','overlap':'NONE_OBSERVED','unreadable_or_truncated_tables':'NONE_OBSERVED','visual_readability':'PASS for screen rendering at 120 dpi; physical print output not tested'},
 'result':'PASS_WITH_SCOPE','scope_note':'All 21 pages visually inspected at full resolution. Dense tables were focused at original resolution; 0075 R02 only changes page-binding of the 10.1 checklist heading/header and does not alter substantive text. Human print-device fidelity was not evaluated.'
}
out=root/'evidence'/'visual_review_R02.json';out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'receipt':str(out),'candidate_sha256':result['candidate_docx_sha256'],'pdf_sha256':result['pdf']['sha256'],'pages':len(pages),'result':result['result']},ensure_ascii=False,indent=2))
