from pathlib import Path
import hashlib, json, re
from datetime import datetime

root=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0128_I19-E17_SOURCE_PREP_R01_20261024")
wd=root/"writer"
src=wd/"MANUSCRIPT_0128_I19-E17_R02.md"
dst=wd/"MANUSCRIPT_0128_I19-E17_R03.md"
if dst.exists():
    raise SystemExit("R03 exists; refusing overwrite")
text=src.read_text(encoding="utf-8")
text=text.replace("**共 6 份日誌清冊**", "**6 個 SAMPLE 日誌定位碼示例**")
text=text.replace("## 玖、正式替換表格（REAL REPLACEMENT FORM，完全空白供實際填寫）", "## 玖、REAL 實際資料替換表單")
start="### 二、正式抽樣數據填報清冊（全空白）"
end="### 三、干擾變數排除審核簽核表（逐案勾稽）"
i=text.index(start)
j=text.index(end, i+len(start))
replacement=r"""### 二、個人訓前後工作資料

下表僅供取得授權後記錄 REAL 資料；目前每格均未填，不能當成已完成的訓後成果。若實際個案數不同，可依同一欄位定義增刪列，並保留版本紀錄。

|序號|受訓者代碼|訓前期間|訓前正確件／納入件|訓後期間|訓後正確件／納入件|百分點差|REAL 來源定位|
|:---:|:---|:---|:---:|:---|:---:|:---:|:---|
|1|||||||
|2|||||||
|3|||||||
|4|||||||
|5|||||||
|6|||||||

### 三、技能示範評量（與職場 KPI 分開）

|序號|受訓者代碼|訓前得分／滿分|訓後得分／滿分|題本、評分規準及原件定位|
|:---:|:---|:---:|:---:|:---|
|1|||||
|2|||||
|3|||||
|4|||||
|5|||||
|6|||||

填寫前先確認測驗題本及評分規準版本一致；本表的學習分數不可代替工作 KPI。"""
text=text[:i]+replacement+"\n\n"+text[j:]

log={
 "project_id":"TTQS_ONE","work_id":"TTQS-0128-I19-E17-CODEX-LAYOUT-REPAIR-R03",
 "doc_id":"0128","official_requirement_id":"I19-E17",
 "input_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
 "output_sha256":hashlib.sha256(text.encode("utf-8")).hexdigest(),
 "changes":["corrected sample log locator description", "replaced 14-column real form with two narrower, separately labeled work-KPI and learning-score tables", "preserved real fields as blank only inside explicit REAL replacement section"],
 "result":"LAYOUT_READY_MANUSCRIPT_NOT_INDEPENDENTLY_ACCEPTED",
 "performed_at_local":datetime.now().astimezone().isoformat()
}
dst.write_text(text,encoding="utf-8",newline="")
logp=wd/"CODEX_LAYOUT_REPAIR_0128_R03.json"
logp.write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"manuscript":str(dst),"sha256":hashlib.sha256(dst.read_bytes()).hexdigest(),"bytes":dst.stat().st_size,"repair_log":str(logp),"repair_log_sha256":hashlib.sha256(logp.read_bytes()).hexdigest()},ensure_ascii=False))
