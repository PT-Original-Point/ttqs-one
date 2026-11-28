from pathlib import Path
import hashlib,json
from datetime import datetime
root=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0128_I19-E17_SOURCE_PREP_R01_20261024")
wd=root/"writer"; src=wd/"MANUSCRIPT_0128_I19-E17_R03.md"; dst=wd/"MANUSCRIPT_0128_I19-E17_R04.md"
if dst.exists(): raise SystemExit("R04 exists; inspect before retry")
t=src.read_text(encoding="utf-8")
t=t.replace("* **資料來源：** 報名管理系統初審稽核日誌、作業抽樣紀錄簿、課堂技能實作測驗卷。", "* **REAL 資料來源類型：** 經授權的工作系統初審紀錄、可追溯的抽樣清冊與課堂實作原件。這些原件本範例尚未提供；稿內數值僅來自合成 SAMPLE 表。")
t=t.replace("**全體總計 / 加權**", "**合併分子分母 / 加權**")
if "報名管理系統初審稽核日誌、作業抽樣紀錄簿、課堂技能實作測驗卷。" in t: raise SystemExit("source statement replacement did not apply")
dst.write_text(t,encoding="utf-8",newline="")
log={"project_id":"TTQS_ONE","work_id":"TTQS-0128-I19-E17-CODEX-FACT-REPAIR-R04","doc_id":"0128","official_requirement_id":"I19-E17","input_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),"output_sha256":hashlib.sha256(dst.read_bytes()).hexdigest(),"changes":["reworded source types as REAL evidence to be obtained, not evidence currently held","clarified weighted total label"],"performed_at_local":datetime.now().astimezone().isoformat(),"status":"FACT_BOUNDARY_REPAIR_NOT_INDEPENDENT_ACCEPTANCE"}
lp=wd/"CODEX_FACT_BOUNDARY_REPAIR_0128_R04.json";lp.write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"manuscript":str(dst),"sha256":hashlib.sha256(dst.read_bytes()).hexdigest(),"bytes":dst.stat().st_size,"repair_log":str(lp),"repair_log_sha256":hashlib.sha256(lp.read_bytes()).hexdigest()},ensure_ascii=False))
