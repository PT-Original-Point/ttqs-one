from pathlib import Path
import json, hashlib, datetime
root=Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01")
worker=root/"worker/opencode_R01/worker_output_R01.md"
source=root/"inputs/0063_MANUSCRIPT_SOURCE_R01.md"
blueprint=root/"inputs/0063_UNIQUE_BLUEPRINT_R01.md"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
raw=source.read_text(encoding="utf-8")
raw_hash=sha(source)
# Remove the model's postscript pointing back to its chat sections; it is not document content.
for marker in ("\n---\n\n## Unique Blueprint", "\n---\n## Unique Blueprint"):
    if marker in raw:
        raw=raw.split(marker,1)[0].rstrip()+"\n"
        break
else:
    raise SystemExit("Expected model postscript separator not found")

patches=[
("candidate purpose, no claim of current association operation",
"**目的。** 本文件要讓小型志工型協會能用一套簡單、可重複的作法，處理外界或內部對訓練資料的查詢：從受理、查詢、回覆、記錄，到發現問題後的矯正、重測與追蹤。目的有三：一是讓每一次查詢都有受理與回應的依據；二是讓查詢失敗能被記錄與修正，而不是默默消失；三是留下可被查核的證據鏈。",
"**目的。** 本文件提供一套供協會審閱與調整的候選作法，示範如何處理外界或內部對訓練資料的查詢：從受理、查詢、回覆、記錄，到發現問題後的矯正、重測與追蹤。協會實際是否採用、由誰執行及其權責，均待協會核定；本文不證明現況。候選流程旨在讓每次查詢有可追溯的處理方式，並讓查詢失敗能被記錄、修正和覆核。"),
("candidate procedure wording",
"以下流程為可操作的順序，每一步都說明輸入、動作與輸出，讓志工幹部可以照著做。",
"以下為供協會審查、調整後採用的候選流程。每一步列出輸入、動作與輸出；實際使用前須確認權責、來源及個資處理規範。"),
("generic escalation role",
"- 方案督導／理監事代表：於爭議或升級時做最後判定。",
"- 升級決策功能：依協會核定章則處理爭議或升級；實際職務與任命均 UNKNOWN。"),
("matrix escalation role",
"| 方案督導／理監事代表 | 爭議或升級之最後判定 | 依章程行使，不代填真實派任 | UNKNOWN／待協會確認 |",
"| 升級決策功能（待確認） | 爭議或升級時依核定權責決定 | 依正式章則，不由本文件指派 | UNKNOWN／待協會確認 |"),
("sample correction title with synthetic label",
"## 11. 矯正計畫、決策/結案與 30 天追蹤",
"## 11. 矯正計畫、決策/結案與 30 天追蹤（SAMPLE／SYNTHETIC 桌上演練）"),
("sample evidence checklist label",
"## 15. 取代/證據檢核清單",
"## 15. 取代/證據檢核清單（SAMPLE 值待真實來源替換）"),
("correct sample record title",
"報到表→出缺席簽到紀錄名冊／TT-2026-SYN60A-DO-ATT-RST-S3-006-V01",
"報到表→示範專案出缺席簽到紀錄名冊／TT-2026-SYN60A-DO-ATT-RST-S3-006-V01"),
("avoid claiming official record title in failure root cause",
"正式紀錄名與口語詞不一致，缺受控別名",
"本演練顯示名稱與口語詞不一致，缺少受控別名"),
("role function in evidence table",
"訓練行政／方案督導",
"訓練行政功能／升級決策功能（任命待確認）"),
("role function in evidence table 2",
"方案督導／理監事代表",
"升級決策功能（任命待確認）"),
("role function in evidence table 3",
"文管／訓練行政",
"文管功能／訓練行政功能（任命待確認）"),
("role function in evidence table 4",
"訓練行政／複核人",
"訓練行政功能／複核功能（任命待確認）"),
]
counts=[]
for label,old,new in patches:
    n=raw.count(old)
    if n<1: raise SystemExit(f"Missing patch target: {label}")
    raw=raw.replace(old,new)
    counts.append({"label":label,"occurrences":n})
# The human-facing examples are templates, not approved messages.
old="## 7. 回應語句範例（不含敏感資料）\n\n"
new=old+"以下文字僅為候選回覆範本；協會確認程序、權限、用詞及聯絡方式後才可採用。方括號欄位須依已核對結果填入；未核准或未核實者不得發出。\n\n"
if raw.count(old)!=1: raise SystemExit("Missing response-template heading")
raw=raw.replace(old,new)
counts.append({"label":"response templates require adoption before sending","occurrences":1})
# Synthetic permission assumption must not be read as actual authorization.
old="| 權限決定 | 允許（內部查核用途，合成） |"
new="| 權限決定 | SAMPLE 演練假設可查詢；不構成真實授權或揭露核准 |"
if raw.count(old)!=1: raise SystemExit("Missing sample permission row")
raw=raw.replace(old,new)
old="| 結案/後續 | 澄清後回覆 10 |"
new=old+"\n\n本列的「假設可查詢」只是桌上演練前提；真實查詢仍須由協會權責功能依來源、目的與範圍另行判斷。"
if raw.count(old)!=1: raise SystemExit("Missing sample intake closure row")
raw=raw.replace(old,new)
counts.append({"label":"synthetic permission decision limitation","occurrences":1})
# Make the two linked sample cards explicit without changing 0061's one-record index.
anchor="## 9. 基準 8 筆查詢矩陣（SAMPLE／SYNTHETIC，2026-10-26）"
fixture="""### 8.3 合成查詢測試資料卡（SAMPLE／SYNTHETIC；不增補 0061 索引）

| 測試卡 | 可查詢的合成內容 | 來源與界線 |
|---|---|---|
| A｜來源資料卡 | 案例 SYN-0060-2026-A01；課程「社區志工接待與資源轉介界線」；日期 2026-08-15；報名 12、到課 10、缺席 2；示範出缺席簽到紀錄碼 TT-2026-SYN60A-DO-ATT-RST-S3-006-V01 | 引用 0060 R08 的 SAMPLE 事實 SYN-0060-FACT-001～007、FACT-027；均非協會真實辦訓紀錄 |
| B｜索引參照卡 | file_id F-0061-2026-0001，來源 doc_id 0060，連結同一案例 SYN-0060-2026-A01 | 引用 0061 R03 唯一一筆 SAMPLE 索引；本測試卡只是查詢演練標籤，不是新增 0061 索引列 |

卡 A 與卡 B 是本件的兩張演練查詢卡，並非兩筆 0061 索引紀錄，也不代表協會已部署查詢系統。案例、資料與結果均為 SAMPLE／SYNTHETIC。

"""
if raw.count(anchor)!=1: raise SystemExit("Missing baseline section anchor")
raw=raw.replace(anchor,fixture+anchor)
counts.append({"label":"explicit source-card and single-index boundary","occurrences":1})
# State that table 11 is a synthetic tabletop action plan.
anchor="| 新增最小範圍澄清 | F-03 | 權限複核人員 | 2026-10-27 | 補件後可查且權限清楚 |\n"
note="本表日期、職務功能分工與結案均為桌上演練設定，不代表協會已採用流程、派任人員或完成真實改善。\n\n"
if raw.count(anchor)!=1: raise SystemExit("Missing correction table end")
raw=raw.replace(anchor,anchor+"\n"+note)
counts.append({"label":"synthetic action-plan boundary","occurrences":1})
# Metric result means query-intent resolution, never permission or disclosure success.
anchor="## 13. KPI 可重現計算（全部為合成）\n\n"
definition="本節「首次可解」只指無需再次澄清即可唯一定位預期紀錄或欄位；「一次澄清內總解」只指查詢意圖於最多一次澄清後已釐清。兩者都不代表資料已送出、已交付或取得揭露權限。搜尋命中與權限決定分開記錄；未通過權限檢核仍須 HOLD／REJECT。\n\n"
if raw.count(anchor)!=1: raise SystemExit("Missing KPI heading")
raw=raw.replace(anchor,anchor+definition)
counts.append({"label":"KPI scope excludes disclosure authorization","occurrences":1})
# The post-retest count is a query-intent result, not an access-success result.
anchor="計數：首次成功 6 筆（1–5、8）；一次澄清後解決 2 筆（6、7）。"
note="以上「成功／解決」僅代表合成查詢任務已找到預期紀錄或釐清欄位；不表示任何資料已對查詢人揭露，亦不構成權限核准。"
if raw.count(anchor)!=1: raise SystemExit("Missing retest count")
raw=raw.replace(anchor,anchor+"\n\n"+note)
counts.append({"label":"retest scope excludes disclosure authorization","occurrences":1})
# Improve the reusable improvement record so it can drive a real future action.
anchor="| 失敗與矯正 | |\n| 重測結果 | |\n| 結案/追蹤日 | |\n"
expanded="""| 失敗分類與影響 | |
| 根因（以可查證事實填寫） | |
| 圍堵／風險控制 | |
| 矯正措施與負責功能 | |
| 預定完成日 | |
| 矯正證據定位 | |
| 重測方法與結果 | |
| 獨立複核功能／日期 | |
| 結案條件與狀態 | |
| 後續追蹤日／結果 | |
"""
if raw.count(anchor)!=1: raise SystemExit("Missing reusable improvement form rows")
raw=raw.replace(anchor,"| 失敗與矯正 | |\n"+expanded)
counts.append({"label":"complete reusable improvement form","occurrences":1})
# Limit the evidence replacement table to clearly synthetic examples.
anchor="要把本文件任一 SAMPLE 換成 REAL，須先取得下列實際紀錄，並由對應功能角色查證（不記真人姓名）："
replace="下表所列數值皆是 SAMPLE；要把任一項換成 REAL，須先取得對應實際紀錄，並由協會確認的權責功能查證。表中的角色名稱只是功能描述，不是既有人員任命："
if raw.count(anchor)!=1: raise SystemExit("Missing replacement-register boundary")
raw=raw.replace(anchor,replace)
counts.append({"label":"replacement table sample and role boundary","occurrences":1})
# Replace an unsupported organization-structure phrase with only a conditional rule.
raw=raw.replace("實際協會的人員派任、核准與簽署，皆為 UNKNOWN，須由協會另行確認。","協會實際的人員派任、核准與簽署均為 UNKNOWN，須由協會另行確認。")
if "方案督導／理監事" in raw: raise SystemExit("Unresolved named office assumption remains")
if "沒有專職品管" in raw: raise SystemExit("Unresolved staffing assumption remains")
# Check end is the intended document ending, not the model response wrapper.
if not raw.rstrip().endswith("均不得視為真實已發生之事實。"):
    raise SystemExit("Unexpected manuscript ending")
out=root/"inputs/0063_MANUSCRIPT_R01.md"
out.write_text(raw,encoding="utf-8")
# Correct the Blueprint's unsupported staffing claim and identify all real appointments as unknown.
bp=blueprint.read_text(encoding="utf-8")
bp_hash=sha(blueprint)
old="2. 小型志工型訓練機構沒有專職品管部门，文件必須以平實語言、少量角色、可重複使用的表單寫成，讓志工幹部看得懂、用得下去。"
new="2. 本案沒有可核實的協會人力配置或品質職務資料，因此 Blueprint 不把「沒有專職品管」當成既成事實；文件以平實語言、少量功能角色與可重用表單作為設計選擇，適用性與實際派任仍由協會確認。"
if bp.count(old)!=1: raise SystemExit("Missing unsupported Blueprint staffing statement")
bp=bp.replace(old,new)
bp=bp.replace("次要使用者：負責複核的理監事或方案督導（覆核回應內容與權限決定）。","次要使用者：依正式章則授權的覆核或升級決策功能（實際職稱與任命 UNKNOWN）。")
bp=bp.replace("方案督導／理監事","升級決策功能（待確認）")
bp=bp.replace("訓練行政／方案督導","訓練行政功能／升級決策功能（待確認）")
if "沒有專職品管部门" in bp or "理監事" in bp: raise SystemExit("Unsupported Blueprint office wording remains")
blueprint.write_text(bp,encoding="utf-8")
receipt={
 "project_id":"TTQS_ONE","doc_id":"0063","candidate_revision":"R01",
 "source_worker_output_sha256":sha(worker),"source_manuscript_sha256_before_patch":raw_hash,
 "patched_manuscript_path":str(out),"patched_manuscript_sha256":sha(out),
 "blueprint_path":str(blueprint),"blueprint_sha256_before_patch":bp_hash,"blueprint_sha256_after_patch":sha(blueprint),
 "patches":counts,
 "reasons":["remove unsupported assertion about association staffing","keep functional roles generic and appointment state UNKNOWN","explicitly separate query-intent resolution from permission or disclosure","clarify two-card test fixture does not add a 0061 index record","complete reusable improvement form and label synthetic action tables","remove non-document model postscript"],
 "status":"CONTENT_PATCHED_PENDING_BUILD_AND_INDEPENDENT_REVIEW"
}
rp=root/"evidence/content_patch_receipt_R01.json"
rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"manuscript_chars":len(raw),"manuscript_sha256":sha(out),"blueprint_sha256":sha(blueprint),"patch_count":len(counts),"receipt":str(rp)},ensure_ascii=False))
