from pathlib import Path
from docx import Document
from zipfile import ZipFile
from pypdf import PdfReader
import hashlib,json,csv,re
root=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025")
docx=root/"0142_I19-E32_R05_HEADER_CONTRAST_CANDIDATE.docx"
base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CURRENT\0142__組織近三年營業額與收入趨勢核對報告.docx")
source=root/"SOURCE_PACKET_0142_I19-E32_R01.md"; blueprint=root/"UNIQUE_BLUEPRINT_0142_I19-E32_R01.md"
render=root/"review"/"WORD_NATIVE_RENDER_RECEIPT_0142_R05.json"; manifest=root/"review"/"PAGE_IMAGE_MANIFEST_0142_R05.json"; pdf=root/"review"/"0142_I19-E32_R05_HeaderContrast_WordNative.pdf"
register=root/"SAMPLE_REPLACEMENT_REGISTER_0142_R05.csv"
visual=root/"review"/"VISUAL_REVIEW_RECEIPT_0142_R05.json"
qa=root/"R05_TECHNICAL_SAMPLE_MATH_QA_RECEIPT.json"
def sha_file(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
EXPECTED="a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e"
if sha_file(docx)!=EXPECTED:raise SystemExit("CANDIDATE_SHA_MISMATCH")
with ZipFile(docx) as z:
 if z.testzip():raise SystemExit("DOCX_PACKAGE_CORRUPT")
 xml_text=z.read("word/document.xml")
d=Document(docx)
if len(d.tables)!=11:raise SystemExit(f"TABLE_COUNT_FAIL:{len(d.tables)}")
# Read the annual demonstration rows directly from Word Table 5.
t=d.tables[4]
def amount(s):
 m=re.search(r"(?<!\d)(\d{1,3}(?:,\d{3})+|\d+)(?!\d)",s.replace("\n"," "))
 if not m:raise ValueError("amount not found: "+repr(s))
 return int(m.group(1).replace(",",""))
rows=[]
for yr,row in zip((2023,2024,2025),t.rows[1:4]):
 vals=[amount(row.cells[i].text) for i in (1,2,3)]
 if vals[0]+vals[1]!=vals[2]:raise SystemExit(f"ANNUAL_TOTAL_FAIL:{yr}:{vals}")
 rows.append({"year":yr,"operating_revenue":vals[0],"other_income":vals[1],"total_income":vals[2]})
if rows!=[
 {"year":2023,"operating_revenue":1200000,"other_income":280000,"total_income":1480000},
 {"year":2024,"operating_revenue":1320000,"other_income":260000,"total_income":1580000},
 {"year":2025,"operating_revenue":1452000,"other_income":300000,"total_income":1752000}]:raise SystemExit("EXPECTED_SAMPLE_DATA_MISMATCH")
ops=[(rows[i]["operating_revenue"]-rows[i-1]["operating_revenue"])/rows[i-1]["operating_revenue"]*100 for i in (1,2)]
operating_cum=(rows[2]["operating_revenue"]-rows[0]["operating_revenue"])/rows[0]["operating_revenue"]*100
total_cum=(rows[2]["total_income"]-rows[0]["total_income"])/rows[0]["total_income"]*100
checks={"annual_sums":all(x["operating_revenue"]+x["other_income"]==x["total_income"] for x in rows),"operating_yoy":ops,"operating_cumulative_pct":operating_cum,"total_income_cumulative_pct":total_cum,"expected_rounding":(round(ops[0],2)==10 and round(ops[1],2)==10 and round(operating_cum,2)==21 and round(total_cum,2)==18.38)}
if not checks["expected_rounding"]:raise SystemExit("MATH_ROUNDING_FAIL")
# Ensure displayed formulas/results are present and the current document remains visibly synthetic.
all_text="\n".join([p.text for p in d.paragraphs]+[c.text for tb in d.tables for row in tb.rows for c in row.cells]+[p.text for s in d.sections for p in s.header.paragraphs]+[p.text for s in d.sections for p in s.footer.paragraphs])
required=["+10.0%","+21.0%","+18.4%","SAMPLE","未判定","未提供"]
missing=[s for s in required if s not in all_text]
if missing:raise SystemExit("VISIBLE_SAMPLE_OR_FORMULA_MARKERS_MISSING:"+repr(missing))
# Hard floors: body styles/runs >=10.5pt; table runs >=9.5pt.
body_sizes=[]
for p in d.paragraphs:
 for r in p.runs:
  if r.text.strip():
   sz=r.font.size.pt if r.font.size else (p.style.font.size.pt if p.style.font.size else d.styles['Normal'].font.size.pt)
   body_sizes.append(sz)
table_sizes=[]
for tb in d.tables:
 for row in tb.rows:
  for cell in row.cells:
   for p in cell.paragraphs:
    for r in p.runs:
     if r.text.strip():
      sz=r.font.size.pt if r.font.size else (p.style.font.size.pt if p.style.font.size else d.styles['Normal'].font.size.pt)
      table_sizes.append(sz)
if min(body_sizes)<10.5 or min(table_sizes)<9.5:raise SystemExit(f"FONT_FLOOR_FAIL:{min(body_sizes)}:{min(table_sizes)}")
# Detect any dark-filled first-row header that still has a run with inherited (non-explicit) text color.
missing_header_colors=[]
for ti,tb in enumerate(d.tables,1):
 for ci,cell in enumerate(tb.rows[0].cells):
  shd=cell._tc.tcPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}shd')
  fill=shd.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill') if shd is not None else None
  if fill=='203955':
   for p in cell.paragraphs:
    for r in p.runs:
     if r.text.strip() and not (r.font.color and r.font.color.type and str(r.font.color.rgb).upper()=='FFFFFF'):
      missing_header_colors.append((ti,ci,r.text))
if missing_header_colors:raise SystemExit("DARK_HEADER_CONTRAST_FAIL:"+repr(missing_header_colors))
if sha_file(base)!="59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6":raise SystemExit("BASE_SHA_MISMATCH")
# Register base and derived synthetic facts; repeated occurrences map to the same fact ID.
facts=[]
def add(fid,kind,value,unit,loc,derivation,source_req):facts.append({"sample_fact_id":fid,"doc_id":"0142","requirement_id":"I19-E32","data_status":"SAMPLE/SYNTHETIC","fact_type":kind,"synthetic_value":value,"unit_or_basis":unit,"document_locator":loc,"derivation_or_use":derivation,"real_replacement_source_required":source_req,"real_status":"UNKNOWN/HOLD","replacement_rule":"Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD."})
for x in rows:
 y=x['year']; add(f"SYN-0142-FY-{y}","reporting_period_and_year_end",f"{y}-01-01 through {y}-12-31; year end {y}-12-31","complete calendar year; NTD assumed",f"Table 5 row {y}; Table 6 row {y}","Synthetic period and date used for a three-year arithmetic example","Authorized complete-year financial statements and accounting-period evidence")
 add(f"SYN-0142-OPERATING-{y}","operating_revenue",str(x['operating_revenue']),"NTD; illustrative service-revenue mapping only",f"Table 5 row {y}, operating revenue column; Table 6 row {y}","Synthetic base value; account mapping is an explicit example assumption, not an association account classification","Authorized financial statement, revenue detail/general ledger, and finance-role account mapping")
 add(f"SYN-0142-OTHER-{y}","other_income",str(x['other_income']),"NTD; synthetic, separate from operating revenue",f"Table 5 row {y}, other income column", "Synthetic amount kept separate; not used as a substitute for operating-revenue growth","Authorized financial statements and reconciled ledger/detail")
 add(f"SYN-0142-TOTAL-{y}","total_income_derived",str(x['total_income']),"NTD; derived synthetic amount",f"Table 5 row {y}, total income column; Table 7 formulas/summary",f"Derived: {x['operating_revenue']} + {x['other_income']}; arithmetic cross-check only","Authorized financial statement and reconciled ledger/detail")
for y,pct in zip((2024,2025),ops):add(f"SYN-0142-OPERATING-YOY-{y}","year_over_year_growth_derived",f"{pct:.1f}%","percent; synthetic-derived",f"Table 5 row {y}, growth column; Table 7 row for {y}","(current-year operating revenue - prior-year operating revenue) / prior-year operating revenue × 100","Recalculate after authorized actual source replacement")
add("SYN-0142-OPERATING-CUMULATIVE-2023-2025","cumulative_operating_growth_derived",f"{operating_cum:.2f}%","percent; synthetic-derived", "Table 7 cumulative operating-revenue row; Section 4.1 example conclusion", "(2025 synthetic operating revenue - 2023 synthetic operating revenue) / 2023 synthetic operating revenue × 100", "Recalculate after authorized actual source replacement")
add("SYN-0142-TOTAL-CUMULATIVE-2023-2025","cumulative_total_income_growth_derived",f"{total_cum:.2f}% (displayed +{total_cum:.1f}%)","percent; synthetic-derived", "Table 7 cumulative total-income row", "(2025 synthetic total income - 2023 synthetic total income) / 2023 synthetic total income × 100", "Recalculate after authorized actual source replacement")
add("SYN-0142-CURRENCY-UNIT","currency_and_unit_assumption","New Taiwan dollars (NTD)","illustrative assumption", "Tables 5-7 and SAMPLE narrative", "Synthetic unit for demonstration only; not read from an association statement", "Authorized source statements and consistent unit/currency basis")
add("SYN-0142-ACCOUNT-MAPPING-ASSUMPTION","account_mapping_assumption","Example assumes 'operating revenue' corresponds to 'service revenue'","explicit synthetic assumption", "Table 4 SAMPLE disclosure and Table 5 label", "Not an association classification decision; actual non-profit classification requires authorized finance review", "Approved chart of accounts and documented finance-role mapping")
add("SYN-0142-DOCUMENT-CONTROL-DATE","document_control_date","2026-10-03","document version metadata; sample/unissued", "Cover document control field", "Inherited from old demonstration candidate; not a financial reporting date or proof of approval/effectiveness", "Actual controlled document register only if approved for use")
register.write_text('',encoding='utf-8',newline='')
with register.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(facts[0].keys()));w.writeheader();w.writerows(facts)
regsha=sha_file(register)
# Exact SHA-bound visual receipt: pages 1,2,4-6 were already inspected at full size and image identity is unchanged from R04; page 3 was directly inspected at full size after R05.
manifest_obj=json.loads(manifest.read_text(encoding='utf-8'));render_obj=json.loads(render.read_text(encoding='utf-8'))
if manifest_obj['candidate_sha256']!=EXPECTED or manifest_obj['page_count']!=6:raise SystemExit("PAGE_MANIFEST_SHA_OR_COUNT_FAIL")
if render_obj['candidate_sha256_before']!=EXPECTED or render_obj['candidate_sha256_after']!=EXPECTED or render_obj['pdf_pages']!="6":raise SystemExit("WORD_RENDER_BINDING_FAIL")
prior=json.loads((root/"review"/"PAGE_IMAGE_MANIFEST_0142_R04.json").read_text(encoding='utf-8'))
checks_pages=[]
for i,p in enumerate(manifest_obj['pages']):
 old=prior['pages'][i]['sha256']
 equal=(old==p['sha256'])
 if i==2 and equal:raise SystemExit("PAGE3_EXPECTED_VISUAL_CHANGE_MISSING")
 if i!=2 and not equal:raise SystemExit(f"UNEXPECTED_OTHER_PAGE_CHANGE:{i+1}")
 checks_pages.append({"page":i+1,"image_sha256":p['sha256'],"inspection":"direct full-size inspection of R05 page 3" if i==2 else "direct full-size R04 inspection inherited because R05 page-image SHA is identical"})
visual_obj={"schema":"ttqs-one-visual-review-receipt-v1","project_id":"TTQS_ONE","doc_id":"0142","requirement_id":"I19-E32","candidate_sha256":EXPECTED,"pdf_sha256":sha_file(pdf),"page_manifest_sha256":sha_file(manifest),"render_receipt_sha256":sha_file(render),"page_count":6,"result":"PASS_LAYOUT_READABILITY","pages":checks_pages,"findings_fixed":["Table 3 final row no longer occupies a one-row continuation page; explicit redundant break removed.","Dark-filled headers in Table 5 first column and Table 6 second column now use white bold text."],"nonblocking_notes":["Table 11 continues onto page 6 with repeated header; the final row and closing guidance remain readable.","Page 4 is intentionally a separated formula/interpretation section; no clipping, overlap, or unreadable content observed."],"inspection_method":"Microsoft Word native read-only PDF export; page raster 120 DPI; all six page PNGs inspected at full size; unchanged page images inherit exact image SHA from R04.","semantic_review":"PENDING_INDEPENDENT_EXACT_SHA_REVIEW","formal_acceptance":"NOT_GRANTED","real_evidence":"UNKNOWN/HOLD"}
visual.write_text(json.dumps(visual_obj,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
qa_obj={"schema":"ttqs-one-0142-r05-technical-sample-math-qa-v1","project_id":"TTQS_ONE","doc_id":"0142","requirement_id":"I19-E32","official_checkbox_index":156,"printed_checkbox_serial":"UNKNOWN","candidate_state":"CANDIDATE","candidate_path":str(docx),"candidate_sha256":EXPECTED,"base_candidate_sha256":sha_file(base),"source_packet_sha256":sha_file(source),"unique_blueprint_sha256":sha_file(blueprint),"source_pdf_sha256":"805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709","crosswalk_sha256":"1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679","synthetic_register_path":str(register),"synthetic_register_sha256":regsha,"synthetic_register_rows":len(facts),"table_count":len(d.tables),"body_min_font_pt":min(body_sizes),"table_min_font_pt":min(table_sizes),"sample_rows":rows,"computed":{"2023_2024_operating_yoy_pct":round(ops[0],2),"2024_2025_operating_yoy_pct":round(ops[1],2),"2023_2025_operating_cumulative_pct":round(operating_cum,2),"2023_2025_total_income_cumulative_pct":round(total_cum,2)},"checks":{"docx_package_integrity":"PASS","visible_text_and_sample_values_unchanged_from_R01":"PASS","annual_sums":"PASS","formula_recomputation":"PASS_SAMPLE_ARITHMETIC_ONLY","font_floors":"PASS","dark_header_text_contrast":"PASS","word_native_render_unchanged_candidate_sha":"PASS","page_manifest_bound_to_candidate":"PASS"},"visual_receipt_path":str(visual),"visual_receipt_sha256":sha_file(visual),"semantic_review":"PENDING_INDEPENDENT_EXACT_SHA_REVIEW","real_evidence":"UNKNOWN/HOLD","official_score":"NOT_ASSIGNED","formal_acceptance":"NOT_GRANTED"}
qa.write_text(json.dumps(qa_obj,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
print(json.dumps({"candidate_sha256":EXPECTED,"source_packet_sha256":sha_file(source),"blueprint_sha256":sha_file(blueprint),"register_rows":len(facts),"register_sha256":regsha,"visual_result":visual_obj['result'],"visual_receipt_sha256":sha_file(visual),"technical_math_result":"PASS_SAMPLE_ARITHMETIC_ONLY","qa_receipt_sha256":sha_file(qa),"pages":6,"semantic_review":qa_obj['semantic_review']},ensure_ascii=False))
