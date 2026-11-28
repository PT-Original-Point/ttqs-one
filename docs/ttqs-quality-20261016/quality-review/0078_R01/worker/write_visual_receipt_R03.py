from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1]
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
receipt={
 'schema':'TTQS_ONE_0078_R03_VISUAL_REVIEW.v1','document_id':'0078','requirement_id':'I17B-E01','official_checkbox_serial':'084',
 'candidate_docx_sha256':h(r/'candidate'/'0078_R03.docx'),
 'render_method':'Microsoft Word COM ExportAsFixedFormat to PDF; Poppler pdftoppm rasterized at 115 DPI',
 'pdf_path':'evidence/render_R03/0078_R03_word_render.pdf','pdf_sha256':h(r/'evidence'/'render_R03'/'0078_R03_word_render.pdf'),'page_count':20,
 'contact_sheets':[
  {'path':'evidence/render_R03/contact_1.png','sha256':h(r/'evidence'/'render_R03'/'contact_1.png'),'pages':'1-12'},
  {'path':'evidence/render_R03/contact_2.png','sha256':h(r/'evidence'/'render_R03'/'contact_2.png'),'pages':'13-20'}],
 'visual_scope':'Viewed contact sheets covering all 20 pages; enlarged individual renders for pages 7-13 and 20.',
 'observations':[
  'All 8 activity cards are complete; cards end at page boundaries without a record split across pages.',
  'The 24-field register repeats its header on the continuation page; F24 and subsequent blank forms remain readable.',
  'The daily cross-check table continues onto the next page with its header repeated and usable rows intact.',
  'The last page has a short source/hash locator table and substantial white space but is not an empty or orphan-status page.',
  'No clipped tables, overlapping text, unreadably compressed wide tables, or missing page numbers were observed in the inspected renders.'
 ],
 'result':'PASS','formal_acceptance':'NOT_GRANTED','real_evidence':'UNKNOWN/HOLD','checkbox_084':'PARTIAL/HOLD',
 'limitations':['No actual photos are included; this is a complete synthetic intake/index demonstration.','Visual PASS does not establish semantic acceptance or formal acceptance.']}
(r/'evidence'/'visual_review_R03.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
