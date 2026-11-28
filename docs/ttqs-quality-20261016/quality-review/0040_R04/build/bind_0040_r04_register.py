from pathlib import Path
import csv, hashlib, sys
p=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0040_R04\sources\0040_SOURCES_AND_SYNTHETIC_REPLACEMENT_REGISTER_R04.csv")
docx=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0040_R04\candidate\0040__訓練評估方法與成效指標對照表_R04.docx")
docsha=hashlib.sha256(docx.read_bytes()).hexdigest()
M={
"0040-REF-001":"第1頁「官方要求（逐字引用）」及「來源」段；第7頁「目前文件控制」表之「官方映射」列／目前記錄欄（0040→I08-E03→官方 checkbox 040；來源 PDF 第3頁及 SHA）。",
"0040-SYN-001":"第1頁「示範界線」段末句「該示範案例代碼：SAMPLE-0039-01」。",
"0040-SYN-002":"第1頁「示範界線」段；課程名稱「社區服務志工接待與活動引導」。",
"0040-SYN-003":"第1頁表頭「工具主題｜資料狀態｜使用時點與用途｜示範資料日期」；資料列／第4欄「示範資料日期」。",
"0040-SYN-004":"第3頁表頭「差距與目標｜直接評量／工具｜時點與門檻｜證據欄位、定位及責任」；K1、K2、K3、K4列／第1欄。",
"0040-SYN-005":"第3頁表頭「構面｜0分：未達｜1分：部分達成｜2分：完整達成｜直接觀察重點」；K1–K4列及其後「計分」段。",
"0040-SYN-006":"第3頁「計分」段（四項完整、總分至少6/8、K3至少1分）；第4頁表頭「合成代碼｜前測…｜後測…｜總分變化｜依門檻判定」／依門檻判定欄。",
"0040-SYN-007":"第1頁表頭「步驟｜操作｜完成後留下的可查結果」；「4 定時點」列／操作欄（開課前做基線）。",
"0040-SYN-008":"第1頁表頭「步驟｜操作｜完成後留下的可查結果」；「4 定時點」列／操作欄（最後一次練習後、結訓前做後測）。",
"0040-SYN-009":"第1頁表頭「步驟｜操作｜完成後留下的可查結果」；「4 定時點」列／操作欄（30日追蹤另行核准）。",
"0040-SYN-010":"第3頁評量矩陣表頭「差距與目標｜直接評量／工具｜時點與門檻｜證據欄位、定位及責任」之責任欄；第5頁表頭「欄位｜完整合成填寫示例｜實際使用時檢查」／「後續行動（示範待辦）」列。",
}
for k in ("K1","K2","K3","K4"):
    label={"K1":"K1 開場與角色說明","K2":"K2 澄清與摘要確認","K3":"K3 同意與隱私界線","K4":"K4 收尾與交接"}[k]
    M["0040-SYN-BL-"+k]=f"第3頁表頭「差距與目標｜直接評量／工具｜時點與門檻｜證據欄位、定位及責任」；「{label}」列／第1欄（基線與差距）。"
for stage in ("PRE","POST"):
    col="前測 K1/K2/K3/K4；總分" if stage=="PRE" else "後測 K1/K2/K3/K4；總分"
    for n in range(1,6):
        ident=f"D{n:02d}"
        M[f"0040-SYN-{stage}-{ident}"]=f"第4頁表頭「合成代碼｜前測 K1/K2/K3/K4；總分｜後測 K1/K2/K3/K4；總分｜總分變化｜依門檻判定」；「{ident}」列／「{col}」欄。"
M.update({
"0040-SYN-CALC-001":"第2頁「設計覆蓋率」段（4÷4＝100%）；第2頁表頭「流程節點｜可核對輸出」／「01 需求與差距」列。",
"0040-SYN-CALC-002":"第4頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；「平均前測」列／「代入合成資料」與「結果及解讀限制」欄。",
"0040-SYN-CALC-003":"第4頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；「平均後測」列／「代入合成資料」與「結果及解讀限制」欄。",
"0040-SYN-CALC-004":"第4頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；「配對平均變化」列／「代入合成資料」與「結果及解讀限制」欄。",
"0040-SYN-CALC-005":"第4頁表頭「合成代碼｜前測…｜後測…｜總分變化｜依門檻判定」；D01、D02、D03、D05列／「依門檻判定」欄；另見「後測達標率」列。",
"0040-SYN-CALC-006":"第4頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；「後測達標率」列／「代入合成資料」及「結果及解讀限制」欄。",
"0040-SYN-CALC-007":"第4頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；「構面平均」列／「代入合成資料」欄之前測K1–K4數列。",
"0040-SYN-CALC-008":"第4頁表頭「指標｜定義／分母｜代入合成資料｜結果及解讀限制」；「構面平均」列／「結果及解讀限制」欄之後測K1–K4平均數列。",
"0040-SYN-CALC-009":"第5頁表頭「欄位｜完整合成填寫示例｜實際使用時檢查」；「後續行動（示範待辦）」列／「完整合成填寫示例」欄；另見第6頁D04追蹤列。"
})
cols={
"0040-SYN-034":"差距／未達門檻",
"0040-SYN-035":"示範風險",
"0040-SYN-036":"責任角色",
"0040-SYN-037":"示範期限／狀態",
"0040-SYN-038":"交接資料／結案規則"
}
for fid,col in cols.items():
    M[fid]=f"第6頁表頭「差距／未達門檻｜示範風險｜責任角色｜示範期限／狀態｜交接資料／結案規則」；D04資料列／「{col}」欄。"
with p.open("r",encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f)); fields=list(rows[0].keys())
if len(rows)!=39 or len({x["fact_id"] for x in rows})!=39:
    raise SystemExit("Expected 39 unique R03 facts.")
if set(M)!=set(x["fact_id"] for x in rows):
    raise SystemExit("Locator map IDs mismatch: "+repr(set(x["fact_id"] for x in rows)-set(M)))
for row in rows:
    row["body_locator"]=M[row["fact_id"]]
    row["bound_candidate_sha256"]=docsha
    if row["fact_id"]=="0040-SYN-001":
        row["synthetic_value"]="SAMPLE-0039-01"
    if row["fact_id"]=="0040-SYN-010":
        row["synthetic_value"]="課程設計角色（示範職務）；評量角色（示範職務）；評量覆核角色（示範職務）"
        row["real_owner_role"]="實際人員、職務權責與授權須依現行真實權責資料核實；本件僅為示範角色標籤。"
with p.open("w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields,lineterminator="\r\n")
    w.writeheader();w.writerows(rows)
digest=hashlib.sha256(p.read_bytes()).hexdigest()
print("DOCX_SHA256",docsha)
print("REGISTER_ROWS",len(rows),"UNIQUE",len(set(x["fact_id"] for x in rows)))
print("MAPPED_ROWS",len(M),"SECTION_MARKERS",sum("§" in x["body_locator"] for x in rows))
print("REGISTER_SHA256",digest)
