from pathlib import Path
from hashlib import sha256
from docx import Document
from docx.oxml.ns import qn
import json,re,datetime
base=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118')
candidate=base/'candidate_0028_R08_20261118.docx'
html=base/'candidate_0028_R07_20261118.html'
static_path=base/'STATIC_QA_R07.json';math_path=base/'MATH_QA_R07.json'
repair_path=base/'qa'/'DOCX_LAYOUT_REPAIR_R08.json'
out=base/'qa'/'DOCX_DETERMINISTIC_QA_R08_RECHECK.json'
if out.exists(): raise SystemExit('R08_DOCX_QA_RECEIPT_EXISTS')
sha=lambda b:sha256(b).hexdigest().upper()
doc=Document(candidate)
def effective_size(run, paragraph):
    size=run.font.size
    if size is not None:return size.pt
    style=paragraph.style
    while style is not None:
        if style.font.size is not None:return style.font.size.pt
        style=style.base_style
    normal=doc.styles['Normal'].font.size
    return normal.pt if normal is not None else None
body_runs=[]
for p in doc.paragraphs:
    for r in p.runs:
        if r.text.strip():body_runs.append((r.text,effective_size(r,p)))
table_runs=[]
for table in doc.tables:
  for row in table.rows:
    for cell in row.cells:
      for p in cell.paragraphs:
        for r in p.runs:
          if r.text.strip():table_runs.append((r.text,effective_size(r,p)))
body_missing=[t[:80] for t,s in body_runs if s is None]
table_missing=[t[:80] for t,s in table_runs if s is None]
body_min=min((s for t,s in body_runs if s is not None),default=None)
table_min=min((s for t,s in table_runs if s is not None),default=None)
row_counts=[len(t.rows) for t in doc.tables]
all_text='\n'.join(p.text for p in doc.paragraphs)+'\n'+'\n'.join(c.text for t in doc.tables for row in t.rows for c in row.cells)
ids=sorted(set(re.findall(r'SYN-0028-(?:[A-Z]+-)+\d{3}',all_text)))
static=json.loads(static_path.read_text(encoding='utf-8-sig'));math=json.loads(math_path.read_text(encoding='utf-8-sig'));repair=json.loads(repair_path.read_text(encoding='utf-8-sig'))
html_sha=sha(html.read_bytes());candidate_sha=sha(candidate.read_bytes())
checks={
 'docx_opens':True,
 'candidate_sha_matches_layout_repair':candidate_sha==repair['output_candidate_sha256'],
 'visible_body_text_preserved_by_repair':repair['visible_body_text_unchanged'],
 'non_document_package_parts_byte_identical':repair['non_document_package_parts_byte_identical'],
 'static_qa_pass_for_exact_source_html':static['result']=='PASS_STATIC_HTML_ONLY' and static['candidate_html_sha256']==html_sha,
 'math_qa_pass_for_same_source_html':math['result']=='PASS_DETERMINISTIC_MATH_AND_FACT_REGISTER_R07' and math['candidate_html_sha256']==html_sha,
 'table_count_matches_source_html':len(doc.tables)==static['table_count'],
 'all_table_row_counts_match_source_html':row_counts==static['table_row_counts'],
 'registered_synthetic_id_count_91':len(ids)==91 and len(ids)==static['synthetic_id_count'],
 'body_font_floor_10_5pt':body_min is not None and body_min>=10.5 and not body_missing,
 'table_font_floor_9_5pt':table_min is not None and table_min>=9.5 and not table_missing,
 'kpi2_exact_2_over_3_display_66_7':'2/3' in all_text and '66.7%' in all_text,
 'kpi3_exact_5_over_6_threshold_833_over_1000_display_83_3':all(v in all_text for v in ['5/6','833/1000','83.3%']),
 'date006_absent_from_candidate':'DATE-006' not in all_text,
}
receipt={'schema':'TTQS_ONE_0028_DOCX_DETERMINISTIC_QA_R08_RECHECK','work_id':'TTQS_ONE_0028_I05-E02_DOCX_DETERMINISTIC_QA_R08_RECHECK_20261118','doc_id':'0028','requirement_id':'I05-E02','candidate_docx_sha256':candidate_sha,'candidate_docx_bytes':candidate.stat().st_size,'source_html_sha256':html_sha,'source_packet_sha256':static['source_sha256'],'blueprint_sha256':static['blueprint_sha256'],'static_qa_file_sha256':sha(static_path.read_bytes()),'math_qa_file_sha256':sha(math_path.read_bytes()),'layout_repair_receipt_sha256':sha(repair_path.read_bytes()),'table_count':len(doc.tables),'table_row_counts':row_counts,'registered_id_count':len(ids),'body_run_count':len(body_runs),'body_font_min_pt':body_min,'body_runs_missing_resolved_size':len(body_missing),'table_run_count':len(table_runs),'table_font_min_pt':table_min,'table_runs_missing_resolved_size':len(table_missing),'checks':checks,'result':'PASS_DOCX_DETERMINISTIC_QA_R08' if all(checks.values()) else 'FAIL_DOCX_DETERMINISTIC_QA_R08','semantic_review':'PENDING_W1_EXACT_SHA','visual_review':'PASS_FULL_PAGE_VISUAL_R08','formal_acceptance':'NOT_CLAIMED','measured_at_local':datetime.datetime.now().astimezone().isoformat()}
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'candidate_sha256':candidate_sha,'body_font_min_pt':body_min,'table_font_min_pt':table_min,'tables':len(doc.tables),'ids':len(ids),'missing_body_size':len(body_missing),'missing_table_size':len(table_missing),'result':receipt['result'],'failed_checks':[k for k,v in checks.items() if not v],'receipt':str(out)},ensure_ascii=False))

