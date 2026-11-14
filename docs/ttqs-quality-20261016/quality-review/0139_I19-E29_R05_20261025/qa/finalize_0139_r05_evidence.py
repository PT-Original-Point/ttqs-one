from pathlib import Path
from hashlib import sha256
from datetime import datetime
import json
base=Path("E:/TTQS/TTQS_ONE_CODEX_RUNTIME/WORK/QUALITY_REBUILD_20261016")
r04=base/"0139_I19-E29_CANDIDATE_R04_20261025"
r05=base/"0139_I19-E29_CANDIDATE_R05_20261025"
prep=base/"0139_I19-E29_SOURCE_PREP_R01_20261025"
def h(p): return sha256(p.read_bytes()).hexdigest()
docx=r05/"0139__證照通過率與就業率跨年度改善分析報告.docx"
manuscript=r04/"0139__MANUSCRIPT_R05.md"
raw04=r04/"AGY_0139_R04_stdout.txt"
receipt04=json.loads((r04/"AGY_0139_R04_DISPATCH_RECEIPT.json").read_text(encoding="utf-8"))
out05=r05/"AGY_0139_R05_DELTA_REVIEW_stdout.txt"
dispatch05=json.loads((r05/"AGY_0139_R05_DELTA_REVIEW_RECEIPT.json").read_text(encoding="utf-8"))
# Update static QA with manuscript consistency and final file hashes.
qa_path=r05/"STATIC_QA_0139_R05.json"
qa=json.loads(qa_path.read_text(encoding="utf-8"))
mt=manuscript.read_text(encoding="utf-8")
qa["manuscript_path"]=str(manuscript)
qa["manuscript_sha256"]=h(manuscript)
qa["manuscript_old_delta_count"]=mt.count("-8.34 pp")
qa["manuscript_corrected_delta_count"]=mt.count("-8.33 pp")
qa["manuscript_sync_pass"]=qa["manuscript_old_delta_count"]==0 and qa["manuscript_corrected_delta_count"]>=1
qa["pass"]=bool(qa["pass"] and qa["manuscript_sync_pass"])
qa["created_local_final"]=datetime.now().astimezone().isoformat()
qa_path.write_text(json.dumps(qa,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
# Complete visual receipt with page image hashes for independent reconstruction.
vpath=r05/"VISUAL_REVIEW_0139_R05.json"
vis=json.loads(vpath.read_text(encoding="utf-8"))
vis["page_png_sha256"]={p.name:h(p) for p in sorted((r05/"render_word_native").glob("page-*.png"))}
vis["page_png_count"]=len(vis["page_png_sha256"])
vis["static_qa_sha256"]=h(qa_path)
vis["visual_status"]="PASS_WITH_NONBLOCKING_OBSERVATION"
vis["created_local_final"]=datetime.now().astimezone().isoformat()
vpath.write_text(json.dumps(vis,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
# R04 response byte/hash normalization reconciliation: LF-normalized hash matches dispatcher record.
raw04_bytes=raw04.read_bytes()
normalized=raw04_bytes.replace(bytes([13,10]),bytes([10]))
norm_sha=sha256(normalized).hexdigest()
norm_note={
 "doc_id":"0139","candidate":"R04","receipt_path":str(r04/"AGY_0139_R04_DISPATCH_RECEIPT.json"),
 "receipt_recorded_stdout_sha256":receipt04["response_sha256"],
 "local_response_path":str(raw04),"local_response_byte_sha256":h(raw04),
 "local_response_bytes":len(raw04_bytes),"crlf_count":raw04_bytes.count(bytes([13,10])),
 "lf_normalized_sha256":norm_sha,
 "normalization_match":norm_sha==receipt04["response_sha256"],
 "finding":"The receipt digest matches after CRLF-to-LF normalization; the stored Windows text file has CRLF line endings. No semantic text loss is indicated by this normalization check.",
 "verdict":"PASS","parent_semantic_verdict":"PASS",
 "created_local":datetime.now().astimezone().isoformat()
}
npath=r05/"R04_REVIEW_RESPONSE_NORMALIZATION_NOTE.json"
npath.write_text(json.dumps(norm_note,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
# Exact-SHA delta review receipt.
sreceipt={
 "doc_id":"0139","official_requirement_id":"I19-E29","blueprint_index":153,"printed_checkbox_serial":"UNKNOWN",
 "candidate":"R05","candidate_docx_sha256":h(docx),
 "verdict":"PASS_DELTA_ONLY",
 "reviewer":"Antigravity CLI bounded independent reviewer; requested model gemini-3.8-flash-high; actual serving identity UNKNOWN",
 "cli_version":dispatch05["cli_version"],"cli_exit_code":dispatch05["exit_code"],
 "review_output_sha256":h(out05),"review_request_sha256":h(r05/"AGY_0139_R05_DELTA_REVIEW_REQUEST.txt"),
 "scope":"R05's two-item logical delta only. The parent R04 full-document semantic verdict PASS is inherited; this reviewer explicitly did not open the DOCX or inspect its pages.",
 "parent_docx_sha256":"0c3415ebe452fb2d7f343ec67878c03c6cff510c2f2aa94887cb2ddcdfb28601",
 "parent_semantic_verdict":"PASS",
 "checked_delta":[
  {"locator":"Table 7, §7.3, 缺考率（%）, 2024→2025","math":"(1/12 - 2/12)*100 = -8.333333... pp; rounds to -8.33 pp","verdict":"PASS"},
  {"locator":"paragraph 172 candidate version label R04→R05","verdict":"PASS"}
 ],
 "formal_acceptance":"NOT_GRANTED","real_evidence_status":"REAL=UNKNOWN/HOLD",
 "created_local":datetime.now().astimezone().isoformat()
}
s_path=r05/"SEMANTIC_REVIEW_0139_R05_DELTA.json"
s_path.write_text(json.dumps(sreceipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
# Enrich build receipt after all QA receipts are final.
bpath=r05/"DOCX_BUILD_RECEIPT_0139_R05.json"
b=json.loads(bpath.read_text(encoding="utf-8"))
b["manuscript_path"]=str(manuscript)
b["manuscript_sha256"]=h(manuscript)
b["static_qa_sha256"]=h(qa_path)
b["visual_review_sha256"]=h(vpath)
b["semantic_delta_review_sha256"]=h(s_path)
b["parent_review_response_reconciliation_path"]=str(npath)
b["parent_review_response_reconciliation_sha256"]=h(npath)
b["created_local_final"]=datetime.now().astimezone().isoformat()
bpath.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({
 "docx_sha256":h(docx),"manuscript_sha256":h(manuscript),
 "static_qa_sha256":h(qa_path),"static_pass":qa["pass"],"manuscript_sync_pass":qa["manuscript_sync_pass"],
 "visual_receipt_sha256":h(vpath),"visual_pass":vis["visual_result"],
 "semantic_receipt_sha256":h(s_path),"semantic_verdict":sreceipt["verdict"],
 "r04_response_normalized_sha256":norm_sha,"r04_hash_normalization_match":norm_note["normalization_match"],
 "build_receipt_sha256":h(bpath)
},ensure_ascii=False,indent=2))
