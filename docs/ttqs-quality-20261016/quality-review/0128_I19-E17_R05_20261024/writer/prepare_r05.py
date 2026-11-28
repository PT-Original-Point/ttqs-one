from pathlib import Path
from datetime import datetime
import hashlib,json
root=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0128_I19-E17_SOURCE_PREP_R01_20261024")
wd=root/"writer"; src=wd/"MANUSCRIPT_0128_I19-E17_R04.md"; dst=wd/"MANUSCRIPT_0128_I19-E17_R05.md"
if dst.exists(): raise SystemExit("R05 exists; inspect before retry")
t=src.read_text(encoding="utf-8")
old1="### 三、干擾變數排除審核簽核表（逐案勾稽）"
old2="### 四、審核決策與核決簽章欄"
if t.count(old1)!=1 or t.count(old2)!=1: raise SystemExit("Expected exact subsection headings not found uniquely")
t=t.replace(old1,"### 四、干擾變數排除審核簽核表（逐案勾稽）").replace(old2,"### 五、審核決策與核決簽章欄")
dst.write_text(t,encoding="utf-8",newline="")
log={"project_id":"TTQS_ONE","work_id":"TTQS-0128-I19-E17-CODEX-HEADING-CORRECTION-R05","doc_id":"0128","official_requirement_id":"I19-E17","input_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),"output_sha256":hashlib.sha256(dst.read_bytes()).hexdigest(),"change":"REAL replacement form subsection numbering corrected 3/3/4 to 3/4/5; no content, data, formula or meaning changed","performed_at_local":datetime.now().astimezone().isoformat(),"status":"BOUNDED_EDITORIAL_REPAIR"}
lp=wd/"CODEX_HEADING_CORRECTION_0128_R05.json";lp.write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding="utf-8")
builder=(wd/"build_docx_0128_r04.py").read_text(encoding="utf-8")
builder=builder.replace("MANUSCRIPT_0128_I19-E17_R04.md","MANUSCRIPT_0128_I19-E17_R05.md")
builder=builder.replace("0128_I19-E17_R04.docx","0128_I19-E17_R05.docx")
builder=builder.replace("BUILD_RECEIPT_0128_R04.json","BUILD_RECEIPT_0128_R05.json")
builder=builder.replace("TTQS-0128-I19-E17-BUILD-R04","TTQS-0128-I19-E17-BUILD-R05")
bp=wd/"build_docx_0128_r05.py";bp.write_text(builder,encoding="utf-8",newline="")
qa=(root/"candidate"/"extract_qa_0128_r04.py").read_text(encoding="utf-8")
qa=qa.replace("0128_I19-E17_R04","0128_I19-E17_R05").replace("-R04","-R05").replace("R04","R05").replace("r04","r05")
qp=root/"candidate"/"extract_qa_0128_r05.py";qp.write_text(qa,encoding="utf-8",newline="")
print(json.dumps({"manuscript":str(dst),"sha256":hashlib.sha256(dst.read_bytes()).hexdigest(),"bytes":dst.stat().st_size,"repair_log":str(lp),"repair_log_sha256":hashlib.sha256(lp.read_bytes()).hexdigest(),"builder":str(bp),"extract_qa_script":str(qp)},ensure_ascii=False))
