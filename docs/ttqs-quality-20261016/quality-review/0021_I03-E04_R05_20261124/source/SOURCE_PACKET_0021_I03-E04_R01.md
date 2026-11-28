# TTQS ONE 來源包｜0021 / I03-E04

- 狀態：`READY_SOURCE_PACKET=PASS`（僅來源包階段；候選資料）
- source-prep work_id：`TTQS_ONE_0021_I03-E04_SOURCE_PACKET_BLUEPRINT_R01_20261116`
- GitHub：`PT-Original-Point/ttqs-one`，PR #92，`work/ttqs-one-document-quality-contract-20261016`；本次讀取 live HEAD `c139d76caa033868376b2427d31f69c6166eeb46`。
- 本包範圍：只含官方來源定位、單一 crosswalk row、單一 142 Blueprint row 與施工界線；沒有 DOCX、正文或合成事實。

## 官方具名需求與定位

- requirement：`I03-E04`
- 官方原文：**學員訓練及學員職務相稱的證明。**
- 正式來源：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf`；PDF 第 1 頁；TTQS 訓練機構版查核佐證表「計畫（Plan）」指標 3 之具名方框項目。
- PDF SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；共 9 頁。以 `pypdf 6.21.4` 讀取第 1 頁後移除空白比對，原文 exact match；此處未執行頁面視覺檢查。
- 來源登錄：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\REQUIREMENT_SOURCE_RECONCILIATION.csv`，SHA-256 `ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9`；`I03-E04` 列記錄 `PDF_TEXT_EXACT_PAGE_MATCH`、page 1、deliverable `0021`。
- 輸入快照：`inputs/OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf`、`inputs/official_source_page1_extracted.txt`、`inputs/requirement_source_reconciliation_I03-E04_excerpt.csv`。

## Crosswalk 對應

- 129-row crosswalk：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv`；SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`。
- 相同 raw bytes 已由 PR #92 live branch 的 0137 R03 source bundle 讀回，SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`；與本機 hash 相同。
- 唯一列：`{"requirement_id": "I03-E04", "deliverable_count": "1", "split_extra_count": "0", "deliverable_ids": "0021", "document_titles": "學員訓練及學員職務相稱的證明_可直接使用成品"}`。因此此需求只映射 `0021`，無拆分額外件。
- 單列快照：`inputs/crosswalk_I03-E04_excerpt.csv`，SHA-256 `6d564d93a06f50b361f5c7624dfc92b3f9b020662175c1baa0bd3a0bb81ed17d`；完整 branch bytes 保存在 `inputs/LIVE_BRANCH_CROSSWALK_129_TO_142_R01.csv`。

## 唯一 Blueprint 的來源依據

- 142-row master：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl`；SHA-256 `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`，本次逐行解析為 142 筆。
- 唯一選取 row：`deliverable_id=0021`、`requirement_id=I03-E04`；raw row SHA-256 `2a507e66c61c4fa5c7d7f14aa23250fea54395aeca474f05e19eedf228030160`。
- row 的文類：`專屬佐證紀錄｜學員訓練及學員職務相稱的證明_可直接使用成品`；角色：`evidence_record`；source status：`PDF_TEXT_EXACT_PAGE_MATCH`。
- 完整唯一 Blueprint 見 `UNIQUE_BLUEPRINT_0021_I03-E04_R01.md`；來源 row 原始位元組見 `inputs/blueprint_current_0021.jsonl`。
- PR branch 的 157 checkbox map 是導覽用 candidate：`docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md`，SHA-256 `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216`；不是官方來源，也不覆蓋 129-to-142 crosswalk 或 142 master。

## 負向近鄰及排除邊界

1. `0020 / I03-E03`：學員訓練類型與 KPI；不承接其 KPI 定義、訓練類型或績效成果。
2. `0022 / I04-E01`：訓練需求定期調查與分析；不承接其需求調查樣本、分析結果或決策。
3. 本件只承接 `I03-E04` 的學員訓練與學員職務相稱證明索引／紀錄；不取代原始簽到、課程、職務或第三方原件。

## READY 判定與歷史候選

- Crosswalk、官方來源登錄、142 Blueprint 均獨立映射到 `0021 / I03-E04`；queue `PENDING` 只作佐證，不作唯一 READY 判據。
- 本次 OS 查核：沒有 0021 的 `CURRENT` 候選、QA 收據、`BUILD_RECEIPTS/0021.json`、同範圍 WORK/EXTERNAL_WORK 目錄或命令列帶有 0021/I03-E04 的 Worker 程序。
- PR #92 live tree 未截斷；6 個 `0021` DOCX 路徑全在既有歷史文件封存／歷次版本路徑；`quality-review` 中沒有 `0021` 或 `I03-E04` 的當前審查封包／QA 路徑。R02 歷史件 `1558` 的本機 exact file SHA-256 為 `6dff6a9e7016f08209e10870d1fd0ba33b012152957fbc8fde18e9a468ec8dd1`；Git Blob SHA-1 為 `e2596a03c9ed04746980769e053319f4302c97c5`（兩者不同演算法）。此檔標記為歷史未重新驗收，沒有以其正文作範本。
- 因此目前真正 READY 的只有獨立來源包／Blueprint 階段；`READY_WRITER` 尚不得開始新建正文，需先對歷史候選做 exact-SHA 回收／品質證據核對，避免重複重建。
- 已明確排除 0016、0133、0005；0018 R02 完全不在本包讀寫範圍。

## 合成／真實資料界線

本階段沒有建立、變更或登錄任何合成事實。後續若無可核實 REAL 原件，依 Blueprint 以 `SAMPLE/SYNTHETIC` 完整示例處理並逐事實登錄替換簿；不得虛構真人、核准、簽章、班次、訓練結果或第三方證明。

## 產物與狀態

- 來源包收據：`SOURCE_PREP_RECEIPT_R01.json`。
- 此文件為施工用候選來源包，不是 DOCX，不代表評核通過或正式接受。
