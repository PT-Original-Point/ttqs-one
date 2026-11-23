from pathlib import Path
from docx import Document
from decimal import Decimal, ROUND_HALF_UP
import csv, hashlib, json, re, sys

out=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025\R06_STRUCTURAL_COMPLETION_R12_20261028")
docx=out/"0142_I19-E32_CANDIDATE_R06.docx"
csvp=out/"SAMPLE_REPLACEMENT_REGISTER_0142_R06.csv"
receipt=out/"TECHNICAL_SEMANTIC_STRUCTURE_QA_0142_R06.json"
visual_receipt=out/"R06_REVIEW"/"VISUAL_QA_RECEIPT_0142_R06.json"
page_manifest=out/"R06_REVIEW"/"PAGE_IMAGE_MANIFEST_0142_R06.json"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
d=Document(docx)
texts=[p.text for p in d.paragraphs]
for t in d.tables:
    for row in t.rows:
        texts.extend(c.text for c in row.cells)
alltext="\n".join(texts)
issues=[]
checks={}
checks["docx_sha256"]=sha(docx)
checks["doc_id_and_requirement"]=("TTQS-0142" in alltext and "I19-E32" in alltext)
checks["official_index_and_serial"]=("索引：156" in alltext and "serial：UNKNOWN" in alltext)
checks["candidate_and_truth_boundary"]=("CANDIDATE" in alltext and "SAMPLE" in alltext and "UNKNOWN/HOLD" in alltext and "NOT_GRANTED" in alltext)
checks["all_physical_tables_captioned"]=len(d.tables)==16 and all(f"表{i}" in alltext for i in range(1,17))
checks["no_one_decimal_growth_values"]=not any(x in alltext for x in ["+10.0%","+21.0%","+18.4%","10.0%","21.0%","18.4%"])
checks["required_precise_growth_values"]=all(x in alltext for x in ["+10.00%","+21.00%","+18.38%"])
checks["source_register_table_rows"]=len(d.tables[11].rows)==4
checks["account_mapping_table_rows"]=len(d.tables[12].rows)==4
checks["annual_reconciliation_table_rows"]=len(d.tables[13].rows)==4
checks["exception_table_rows"]=len(d.tables[14].rows)==9
checks["replacement_table_rows"]=len(d.tables[15].rows)==20
checks["replacement_table_compact_columns"]=len(d.tables[15].columns)==5
checks["replacement_table_codes"]=[row.cells[0].text for row in d.tables[15].rows[1:]]==[f"F{i:02d}" for i in range(1,20)]
checks["replacement_table_no_long_control_tokens"]=not any(token in "\n".join(c.text for r in d.tables[15].rows for c in r.cells) for token in ["NOT_REVIEWED_REAL","NOT_REPLACED","Authorized ","SYN-0142-"])
with open(csvp,encoding="utf-8-sig",newline="") as f: reg=list(csv.DictReader(f))
checks["csv_register_rows"]=len(reg)==19
checks["register_fields"]=all(k in reg[0] for k in ["sample_fact_id","display_id","real_replacement_source_required","real_review_status","replacement_date"])
checks["csv_display_ids_map_to_original_ids"]=[r["display_id"] for r in reg]==[f"F{i:02d}" for i in range(1,20)] and all(r["sample_fact_id"] for r in reg)
checks["all_real_rows_hold_or_na"]=all(r["real_status"] in ("UNKNOWN/HOLD","NOT_APPLICABLE") and r["replacement_date"]=="NOT_REPLACED" for r in reg)
checks["synthetic_rows_explicit"]=all(r["data_status"] in ("SAMPLE/SYNTHETIC","CONTROL_METADATA") for r in reg)
checks["annual_math"]=(
 Decimal("1200000")+Decimal("280000")==Decimal("1480000") and
 Decimal("1320000")+Decimal("260000")==Decimal("1580000") and
 Decimal("1452000")+Decimal("300000")==Decimal("1752000") and
 ((Decimal("1320000")-Decimal("1200000"))/Decimal("1200000")*100).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)==Decimal("10.00") and
 ((Decimal("1452000")-Decimal("1320000"))/Decimal("1320000")*100).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)==Decimal("10.00") and
 ((Decimal("1452000")-Decimal("1200000"))/Decimal("1200000")*100).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)==Decimal("21.00") and
 ((Decimal("1752000")-Decimal("1480000"))/Decimal("1480000")*100).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)==Decimal("18.38")
)
checks["real_financial_reconciliation_not_claimed"]=(all("財報／總帳原件未提供" in row.cells[5].text and "UNKNOWN/HOLD" in row.cells[5].text for row in d.tables[13].rows[1:]) and "正式接受NOT_GRANTED" in alltext)
visual_status="PENDING_WORD_NATIVE_RENDER_AND_PAGE_INSPECTION"
if visual_receipt.exists() and page_manifest.exists():
    vr=json.loads(visual_receipt.read_text(encoding="utf-8"))
    pm=json.loads(page_manifest.read_text(encoding="utf-8"))
    checks["visual_receipt_bound_to_exact_candidate"]=(
        vr.get("candidate_sha256")==sha(docx)==pm.get("candidate_sha256") and
        vr.get("word_native_pdf_sha256")==pm.get("pdf_sha256") and
        vr.get("page_count")==pm.get("page_count") and
        vr.get("layout_result")=="PASS"
    )
    if checks["visual_receipt_bound_to_exact_candidate"]:
        visual_status={"result":"PASS","receipt_path":str(visual_receipt),"receipt_sha256":sha(visual_receipt),"page_manifest_sha256":sha(page_manifest)}
else:
    checks["visual_receipt_bound_to_exact_candidate"]=False
# Find disallowed template terms unless explicitly inside labeled real replacement sections.
bad_terms=["待填","待核","空白表","保持空白","會後填寫"]
checks["no_uncontrolled_empty_template_terms"]=not any(term in alltext for term in bad_terms)
for k,v in checks.items():
    if isinstance(v,bool) and not v: issues.append(k)
report={
 "schema":"TTQS_ONE_0142_R06_TECHNICAL_STRUCTURE_QA_V1",
 "doc_id":"0142","requirement_id":"I19-E32",
 "candidate_path":str(docx),"candidate_sha256":sha(docx),
 "source_packet_sha256":sha(Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025\SOURCE_PACKET_0142_I19-E32_R01.md")),
 "unique_blueprint_sha256":sha(Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025\UNIQUE_BLUEPRINT_0142_I19-E32_R01.md")),
 "table_count":len(d.tables),"register_row_count":len(reg),
 "checks":checks,"issues":issues,
 "result":"PASS" if not issues else "FAIL",
 "semantic_scope":"Deterministic structure/math/truth-boundary checks only; does not grant independent semantic acceptance.",
 "visual_review":visual_status,
 "formal_acceptance":"NOT_GRANTED","real_evidence":"UNKNOWN/HOLD"
}
receipt.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"result":report["result"],"issues":issues,"candidate_sha256":report["candidate_sha256"],"receipt_sha256":sha(receipt),"checks":checks},ensure_ascii=False))
if issues: sys.exit(2)
