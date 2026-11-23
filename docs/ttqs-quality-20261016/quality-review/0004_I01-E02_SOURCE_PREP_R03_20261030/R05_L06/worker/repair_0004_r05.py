from pathlib import Path
import csv,hashlib,json,re,sys
sys.stdout.reconfigure(encoding="utf-8")
base=Path(__file__).resolve().parent.parent
src=base/"worker"/"0004_WRITER_MANUSCRIPT_CANDIDATE_R04.md"
out=base/"worker"/"0004_WRITER_MANUSCRIPT_CANDIDATE_R05.md"
reg=base/"SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R05.csv"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if sha(src)!="cba7dc71696108970d570f03bb09d1f3385bb7493192582e658cd9cdbd81a165": raise SystemExit("R04_SHA_MISMATCH")
lines=src.read_text(encoding="utf-8").splitlines()
# Align U004 outcome and U005 consent values to their exact registered enums.
i=next((i for i,x in enumerate(lines) if x.startswith("| SYN-0004-U004 |") and "SAMPLE_INDEX_SLOT_" in x),None)
if i is None or "NO_RETURN_BY_DEFINED_SAMPLE_CUTOFF" not in lines[i]: raise SystemExit("U004_TABLE4_ROW")
lines[i]=lines[i].replace("NO_RETURN_BY_DEFINED_SAMPLE_CUTOFF","NO_RETURN",1)
i=next((i for i,x in enumerate(lines) if x.startswith("| SYN-0004-U005 |") and "SAMPLE_INDEX_SLOT_" in x),None)
if i is None or "NOT_APPLICABLE_SAMPLE" not in lines[i]: raise SystemExit("U005_TABLE4_ROW")
lines[i]=lines[i].replace("NOT_APPLICABLE_SAMPLE","NOT_APPLICABLE",1)
# Identify future responsibility as a suggested role, not an existing assignment.
i=next((i for i,x in enumerate(lines) if x.startswith("| 合成事實代碼") and "Gate Criteria" in x),None)
if i is None or "責任角色" not in lines[i]: raise SystemExit("TABLE10_HEADER")
lines[i]=lines[i].replace("責任角色","建議角色／待實際指派",1)
# State the shared period directly before the rate table; rates are synthetic workflow arithmetic only.
i=next((i for i,x in enumerate(lines) if x.startswith("### 表 7-1")),None)
if i is None or (i>0 and "2026-10-28 至 2026-10-29" in lines[i-1]): raise SystemExit("TABLE7_PERIOD_ANCHOR")
note="本表四項比率均依本批次 SAMPLE 調查日期範圍 2026-10-28 至 2026-10-29 計算；截止設定以 Asia/Taipei 2026-10-29 23:59 為準。邀請情境未外送，數值僅為合成流程演算，不代表真實調查績效。"
lines.insert(i,note)
s="\n".join(lines)+"\n"
old="TTQS-0004-I01-E02-WRITER-R04-CODEX-20261030"
if s.count(old)!=1: raise SystemExit("FOOTER_R04")
s=s.replace(old,"TTQS-0004-I01-E02-WRITER-R05-CODEX-20261030",1)
out.write_text(s,encoding="utf-8",newline="\n")
body=out.read_text(encoding="utf-8")
rr=list(csv.DictReader(reg.open(encoding="utf-8-sig",newline="")))
checks=[]
def ck(n,b,d): checks.append({"name":n,"result":"PASS" if b else "FAIL","detail":d})
missing=[r["fact_id"] for r in rr if r["fact_id"] not in body]
ck("all_registered_ids_in_body",not missing,f"{len(rr)-len(missing)}/{len(rr)}; missing={missing}")
u4=next((x for x in body.splitlines() if x.startswith("| SYN-0004-U004 |") and "SAMPLE_INDEX_SLOT_" in x),"")
u5=next((x for x in body.splitlines() if x.startswith("| SYN-0004-U005 |") and "SAMPLE_INDEX_SLOT_" in x),"")
ck("U004_outcome_register_alignment","NO_RETURN" in u4 and "NO_RETURN_BY_DEFINED_SAMPLE_CUTOFF" not in u4,"outcome exact enum")
ck("U004_reason_register_alignment","NO_RESPONSE_BY_CLOSE" in u4,"reason exact enum")
ck("U005_consent_register_alignment","NOT_APPLICABLE" in u5 and "NOT_APPLICABLE_SAMPLE" not in u5,"consent exact enum")
ck("rate_period_explicit","2026-10-28 至 2026-10-29" in body and "Asia/Taipei 2026-10-29 23:59" in body,"shared period and cutoff")
ck("suggested_roles_not_assigned","建議角色／待實際指派" in body,"Table 10 role header")
ck("negative_neighbor_0001_0006","0001《中長程業務發展策略地圖》" in body and "0006《業務發展計畫與人力資源訓練規劃》" in body,"purpose and genre boundaries")
ck("R04_source_sha",sha(src)=="cba7dc71696108970d570f03bb09d1f3385bb7493192582e658cd9cdbd81a165",sha(src))
ck("register_sha",sha(reg)=="bbf6ec66d58cd93df63c90ecd611b6aae3e8587265890b33a5daf061c96ec3f9",sha(reg))
compact=re.sub(r"\s+","",body)
for expr in ["5=1+4","4=2+1+1","2=1+1","3=2+1"]: ck("flow_"+expr,expr in compact,expr)
result={"receipt_id":"STATIC_CONTENT_QA_0004_R05","doc_id":"0004","requirement_id":"I01-E02","source_revision":"R04","candidate_revision":"R05","source_sha256":sha(src),"candidate_sha256":sha(out),"register_sha256":sha(reg),"checks":checks,"passed":sum(x["result"]=="PASS" for x in checks),"total":len(checks),"status":"PASS_DETERMINISTIC_CONTENT_CANDIDATE_ONLY" if all(x["result"]=="PASS" for x in checks) else "FAIL","semantic_review":"PENDING_EXACT_SHA_R05","layout_visual":"NOT_CHECKED","docx":"NOT_BUILT","formal_acceptance":"UNKNOWN"}
(base/"worker"/"STATIC_CONTENT_QA_R05.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
receipt={"receipt_id":"MANUSCRIPT_PATCH_RECEIPT_0004_R05","doc_id":"0004","official_requirement_id":"I01-E02","input_file":src.name,"input_sha256":sha(src),"output_file":out.name,"output_sha256":sha(out),"register_file":reg.name,"register_sha256":sha(reg),"patches":["U004 outcome enum aligned with register; U005 consent enum aligned with register; Table 7-1 shared SAMPLE period stated; Table 10 role column labelled suggested roles pending actual assignment"],"status":"CANDIDATE_MANUSCRIPT_ONLY","semantic_review":"PENDING_EXACT_SHA_R05","docx":"NOT_BUILT","formal_acceptance":"UNKNOWN"}
(base/"worker"/"MANUSCRIPT_PATCH_RECEIPT_R05.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"patch":receipt,"qa":result},ensure_ascii=False,indent=2))
