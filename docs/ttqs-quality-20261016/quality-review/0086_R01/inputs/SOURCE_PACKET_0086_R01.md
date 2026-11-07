# 0086 R01｜來源封包

## 文件身分與狀態
- 專案：TTQS_ONE；文件候選編號：0086（此編號屬歷史 142 文件序列，非官方方框號）。
- 候選對應：I17C-E05／官方方框 092；名稱方向為「神秘客實地稽核：程序與真實外部稽核原件邊界」。
- 狀態：來源支持的可逆候選施工；不表示原始點協會現已採用、曾執行外部稽核、核准本程序或取得任何評核分數。
- 真實個資／稽核原件／第三方報告：本封包沒有提供；所有完成示例一律標 SAMPLE/SYNTHETIC，REAL=UNKNOWN/HOLD。

## 一手官方來源
1. 勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》印刷第 6 頁，I17c「行為評估」。本機官方 PDF：`quality-review/0077_R01/inputs/upstream_snapshots/official_evidence_table_source.pdf`；Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0`；SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。此頁參考佐證含神秘客實地稽核／外部稽核課後機制。
2. 同頁 I17c 機構級 0–3 分文字：0 未執行；1 協助客戶執行課後行動計畫評估；2 有機制且有辦理或追蹤紀錄；3 相關紀錄呈現具體成效。這是機構層評分，不是本文件的神秘客量尺；本候選不替協會給分。
3. 可目視來源影像：`quality-review/0078_R01/evidence/official_evidence_table_page6-6.png`；SHA-256 `B7BD4C09B7D7E22993A1577647E10A421FB240222B46B531BA3F01EE047FA1D1`。已直接檢視，清楚顯示 I17c 及參考佐證清單。

## 現行品質控制來源（PR #92 分支快照）
- 分支 `work/ttqs-one-document-quality-contract-20261016`，觀測 head `e39bb393603e94fc79b0f8dd1eb73eab6ab6b874`（只作本封包來源快照，不固定未來 HEAD）。
- `01_HUMAN_MISSION_AND_ACCEPTANCE.md` Git blob `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`：原始點協會小型訓練機構適切性；真實資料缺漏要以完整 SYNTHETIC 示例替代，不能偽造授權、簽名或第三方證明；技術資訊不入正文。
- `02_GENRE_WRITING_MANUAL.md` Git blob `4ff863d9f534b6359fc1c7c1685bd8cce02da886`：指標 17c 五項作品分工；神秘客／外部稽核需有方法和法遵機制，不得聲稱已執行；行為觀察須交代來源。
- `03_157_CHECKBOX_BLUEPRINTS.md` Git blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`：方框 092 的專屬方向為「神秘客實地稽核：程序與真實外部稽核原件邊界」；須含來源定位、核心正文／示範、決策或結果、與其他文件事實連結。
- `04_CODEX_GOAL_24X7_EXECUTION.md` Git blob `62e3dd7dfd8579b6bc97952ffa6236e7494f3b4d`：候選須具體可用、數字可重算、SAMPLE/REAL 分開並經 exact-SHA 技術、視覺及獨立語意驗收；正式接受仍受 Human Gate 控制。
- `06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` Git blob `263aaca84891bba8dca087875804343c3670e921`：本任務外部稽核續工規則與成本／路由限制。

## 文件編號映射的證據限制
- 本機 `quality-review/0079_R01/inputs/UNIQUE_BLUEPRINT_0079_R02.md` SHA-256 `02AE81CB147D82F3A940BE9E1747B483264AA0F9DCB15FFBD19E8A1611FAA7B6` 的末段只用於相鄰文件身分更正：DOCX 0085/0086 對應 I17C-E04/E05。0085 R02 封包亦記載該更正。
- 被引用的歷史 `送審資料/05_填表建議_方法示範不等於實績/142份文件逐項檢查與填表建議.csv` 在現有 checkout 中未取得；本候選不聲稱該 CSV 已核對。官方方框 092 的本體與 0086→I17C-E05 候選映射分層保存，若後續取得權威 142 序列原件，僅更新 sidecar 映射，不因 metadata 重建 DOCX。

## 絕對界線
- 不執行實際神秘客訪查、不聯絡第三方、不假扮真實消費者、不建立或暗示真實稽核者、不錄音錄影、不填入真實個資。
- 任何真實訪查前，須由有權責者核定目的、範圍、委託與獨立性、告知／合法依據、隱私與安全、取樣與保存期限。缺一即 HOLD。
- 任何實際第三方稽核報告、簽章、日期、訪查結果、改善關閉或協會評分均需由真實來源驗證；本候選不得代作。
