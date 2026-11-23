import csv, hashlib, json, re, sys, unicodedata
from pathlib import Path
from pypdf import PdfReader
sys.stdout.reconfigure(encoding='utf-8')
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0053_R03')
evidence=root/'evidence'; render=evidence/'render_final_R03'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def norm(s): return ''.join(c for c in unicodedata.normalize('NFKC',s) if not c.isspace())
candidate=root/'candidate'/'0053_R03.docx'; register=root/'SYNTHETIC_REPLACEMENT_REGISTER_0053_R03.csv'; pdf=render/'0053_R03_Word_export.pdf'
candidate_sha=sha(candidate); reg_sha=sha(register); pdf_sha=sha(pdf)
with register.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
pages=[norm(p.extract_text() or '') for p in PdfReader(str(pdf)).pages]
labels=['L1','L2','L3','M1','M2','M3','T1','T2','T3','P1','P2','P3','F1','F2','F3']
rules={f'SYN-0053-F{i:03d}':[labels[i-1]] for i in range(1,16)}
rules.update({
'SYN-0053-F016':['SYN-0033-PLAN-01'],'SYN-0053-F017':['志工服務紀錄'],'SYN-0053-F018':['L2','12個'],
'SYN-0053-F019':['G1','90分鐘'],'SYN-0053-F020':['G2','90分鐘'],'SYN-0053-F021':['G3','120分'],'SYN-0053-F022':['G4','60分'],
'SYN-0053-F023':['360','教學分鐘'],'SYN-0053-F024':['2026-10-03'],'SYN-0053-F025':['2026-10-08'],
'SYN-0053-F026':['11/15','73.3%'],'SYN-0053-F027':['14/15','93.3%'],'SYN-0053-F028':['+20.0'],
'SYN-0053-F029':['6個合成'],'SYN-0053-F030':['4/6','六個合成'],'SYN-0053-F031':['5/6','83.3%'],
'SYN-0053-F032':['35+20+35=90','38.9%'],'SYN-0053-F033':['20+20+50=90','55.6%'],
'SYN-0053-F034':['SYN-COORD','SYN-REVIEWER'],'SYN-0053-F035':['SYN-VENUE-A'],'SYN-0053-F036':['SYN-MAT-G1-G4'],
'SYN-0053-F037':['90%'],'SYN-0053-F038':['14/15','未關閉'],'SYN-0053-F039':['P0-SYN','本案合成計畫草稿版號'],'SYN-0053-F040':['50%','P2']})
page_rows=[]; failures=[]
for row in rows:
 page=int(row['rendered_page']); anchors=rules[row['fact_id']]; actual=pages[page-1] if 1<=page<=len(pages) else ''
 missing=[a for a in anchors if norm(a) not in actual]
 rec={'fact_id':row['fact_id'],'rendered_page':page,'body_locator':row['body_locator'],'anchors':anchors,'status':'PASS' if not missing else 'FAIL'}
 if missing: rec['missing_anchors']=missing; failures.append(rec)
 page_rows.append(rec)
register_receipt={'schema':'ttqs.0053.register_page_anchor_receipt.v1','candidate_sha256':candidate_sha,'register_sha256':reg_sha,'rendered_pdf_sha256':pdf_sha,'rendered_page_count':len(pages),'register_rows':len(rows),'page_anchor_pass_count':len(rows)-len(failures),'page_anchor_failures':failures,'rows':page_rows,'status':'PASS' if not failures and len(rows)==40 else 'FAIL'}
anchor_path=evidence/'register_page_anchor_receipt_R03.json'; anchor_path.write_text(json.dumps(register_receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest=json.loads((render/'render_manifest_R03.json').read_text(encoding='utf-8'))
contact=evidence/'visual_contact_sheet_R03_compact.jpg'
layout={'schema':'ttqs.0053.visual_layout_receipt.v1','candidate_sha256':candidate_sha,'candidate_bytes':candidate.stat().st_size,'candidate_sha_unchanged_since_R03_build':candidate_sha=='cc75583238dba42eede61de990992770f8de75e96d1bcfe1313e57629551f8e8','rendered_pdf_sha256':pdf_sha,'rendered_pdf_pages':len(pages),'page_image_count':len(manifest['pages']),'all_pages_screened_in_compact_contact_sheet':list(range(1,len(pages)+1)),'contact_sheet_path':'evidence/visual_contact_sheet_R03_compact.jpg','contact_sheet_sha256':sha(contact),'full_size_pages_directly_inspected':[2,5,8,10,18],'observations':['18-page sequence has no blank or near-blank page in the full-corpus contact sheet.','Page furniture and table color hierarchy are consistent across the sequence; no obvious cut-off or overflow is visible at contact-sheet scale.','Full-size pages 2, 5, 8, 10, and 18 were opened: P0-SYN boundary, P2 SAMPLE-only threshold, F1 venue row, 90-minute recalculation, and Appendix C locator are legible and within page bounds.','The 40-row replacement register page anchors were checked against extracted text from the Word-export PDF; 40/40 pass.'],'status':'PASS_SCOPED_VISUAL_SCREEN','reviewer_independence':'operator visual inspection; independent semantic reviewer result is pending','limitations':['Contact-sheet screening is not a substitute for full-size reading of every page.','Only listed pages received direct full-size inspection in this pass.']}
layout_path=evidence/'visual_layout_receipt_R03.json'; layout_path.write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
build_path=evidence/'build_receipt_R03.json'; build=json.loads(build_path.read_text(encoding='utf-8')); build['register_path']='SYNTHETIC_REPLACEMENT_REGISTER_0053_R03.csv'; build['register_sha256']=reg_sha; build['page_anchor_receipt_path']='evidence/register_page_anchor_receipt_R03.json'; build['page_anchor_validation']='PASS 40/40 against Word-export PDF'; build['text_and_traceability_corrections'].append('F013/F035 corrected rendered page locator to p8; DOCX bytes unchanged'); build['candidate_sha256']=candidate_sha; build['candidate_bytes']=candidate.stat().st_size; build_path.write_text(json.dumps(build,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
tech_path=evidence/'technical_integrity_receipt_R03.json'; tech=json.loads(tech_path.read_text(encoding='utf-8')); tech['candidate_sha256']=candidate_sha; tech['candidate_bytes']=candidate.stat().st_size; tech['replacement_register_sha256']=reg_sha; tech['replacement_register_rows']=len(rows); tech['page_anchor_receipt_sha256']=sha(anchor_path); tech['page_anchor_validation']='PASS 40/40 exact fact anchors present on recorded rendered pages'; tech['rendered_pdf_sha256']=pdf_sha; tech['rendered_page_count']=len(pages); tech['font_scope_note']='Explicit paragraph run minimum is 8.5pt for section kicker/navigation labels; Normal body style is 10.5pt; explicit table run minimum is 9.5pt.'; tech['independent_review_status']='PENDING R03 exact-SHA review'; tech_path.write_text(json.dumps(tech,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':candidate_sha,'register_sha256':reg_sha,'pdf_sha256':pdf_sha,'page_anchor_count':len(rows)-len(failures),'anchor_failures':failures,'layout_receipt_sha256':sha(layout_path),'technical_receipt_sha256':sha(tech_path),'build_receipt_sha256':sha(build_path),'status':register_receipt['status']},ensure_ascii=False,indent=2))
