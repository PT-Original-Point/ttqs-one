# TTQS ONE 來源包｜0022 / I04-E01

- 階段：`READY_SOURCE_PACKET=PASS`（只準備單件來源；候選工件）
- work_id：`TTQS_ONE_0022_I04-E01_SOURCE_PREP_R01_20261116`
- GitHub：`PT-Original-Point/ttqs-one` PR #92；branch `work/ttqs-one-document-quality-contract-20261016`；live HEAD `c139d76caa033868376b2427d31f69c6166eeb46`（PR head 相同）。
- 本包只支援 `0022 / I04-E01`，不讀取舊批次 DOCX 正文或表格，不產生 DOCX/正文/合成數字。

## 官方具名需求與來源定位

- 官方要求：**訓練需求的定期調查與分析。**
- 來源：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf`；PDF 第 2 頁，TTQS 訓練機構版查核佐證表「計畫（Plan）」指標 4。
- PDF SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；9 頁。以本機 pypdf 6.21.4 讀取第 2 頁並移除空白後，官方要求文字 exact match；`visually_checked_pages` 未記錄，故本階段不宣稱頁面視覺檢查。
- 單頁抽取文字：`inputs/official_source_page2_extracted.txt`；SHA-256 `3c295e8861ad7775a78583e9111df61ac8733a7cf40d771f942363f00572de9c`。官方 PDF 原始位元組副本：`inputs/OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf`。

## Crosswalk 與 Blueprint 依據

- 本機 129-row crosswalk：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv`；master SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`。
- 從 PR #92 live branch 0137 R03 source bundle 原始讀回完整 crosswalk；SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`，與本機 master 相同。
- 唯一列：`{"requirement_id": "I04-E01", "deliverable_count": "1", "split_extra_count": "0", "deliverable_ids": "0022", "document_titles": "訓練需求的定期調查與分析_分析報告"}`；選取原始列 SHA-256 `96078050897b628f4bd5d1bc3471a03902295ba431a28a8fb411b9a07960b467`；單列摘錄 SHA-256 `e4841a0e842b097dfec52e1cba43b8c9cec8a263084a5b0d7cdd388d5f9e5d8d`。
- 142-row master：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_CURRENT.jsonl`；SHA-256 `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`，解析筆數 142。唯一 row 為 `0022 / I04-E01`，raw row SHA-256 `9b8c1beecbcfe92344b28230649671fa2fd23f73672347e16a94d1a00534aac2`；單列快照 `inputs/blueprint_current_0022.jsonl`。
- 來源 reconciliation：`E:\TTQS\TTQS_ONE_CODEX_RUNTIME\SOURCES\REQUIREMENT_SOURCE_RECONCILIATION.csv`；master SHA-256 `ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9`；單列摘錄 `inputs/requirement_source_reconciliation_I04-E01_excerpt.csv`。記錄 page 2、`PDF_TEXT_EXACT_PAGE_MATCH`、deliverable `0022`。
- PR branch 的 `03_157_CHECKBOX_BLUEPRINTS.md` 僅是導覽用候選索引，SHA-256 `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216`；不作官方需求或交付映射權威。

## 唯一文類與負向近鄰

Crosswalk 唯一映射 `I04-E01 → 0022`；142 Blueprint 唯一文類為「分析／評估報告｜訓練需求的定期調查與分析_分析報告」。本件只分析有來源支持的訓練需求調查，不承接：

1. `0021 / I03-E04` 學員訓練及學員職務相稱證明。
2. `0023 / I04-E02` 不同訓練課程的設計與規劃方向。

Blueprint 的 historical body use 為 `PROHIBITED`。PR #92 雖含 0022 舊 DOCX，但只在歷史封存/歷次版本路徑；本次只讀 Git tree 的路徑、大小與 blob metadata，未讀取舊 DOCX 位元組、正文或表格，亦未把它們作為範本。

## 來源缺項（UNKNOWN）與 SAMPLE 邊界

以下實際資料在本來源包中均標 `UNKNOWN`，不以舊文件或推測補值：
- 實際調查期間、調查母體、抽樣框、樣本數、回收數與缺答紀錄：UNKNOWN（本來源包未取得真實調查原始資料）
- 真實需求問卷/訪談原件、題項版本、回覆資料及形成日期：UNKNOWN（本來源包未取得）
- 各課程目標、目標值/實績值、基準值、指標來源及核准紀錄：UNKNOWN（本來源包未取得）
- 真實分群/趨勢分析、原因證據、主管決議、責任人、期限及後續追蹤結果：UNKNOWN（本來源包未取得）
- 可核對的真人/第三方簽核、會議紀錄、附件路徑與保管紀錄：UNKNOWN（本來源包未取得）

後續 Writer 若仍無法取得 REAL 原始資料，可以依任務規範製作完整、內部一致的 `SAMPLE/SYNTHETIC` 分析示例；逐項登錄合成日期、樣本數、目標/實績、分群、原因、決議、責任與追蹤值及其真實替換方式。不得稱為機構實績，不得偽造問卷回覆、簽核、第三方原件或訓練成果。本階段未新增任何合成事實。

## Ready 與外部狀態

- 本機/PR live crosswalk 與 Blueprint 唯一指向 `0022 / I04-E01`；來源包與專屬 Blueprint 可在不碰其他 doc scope 下完成。
- PR #92 tree 完整讀回，沒有 `0022_I04-E01` 來源包/Blueprint/receipt，也沒有 0022/I04-E01 的 live `quality-review` QA package；遠端僅見歷史 DOCX 路徑。
- OS 沒有命令列可辨識的 0022/I04-E01 Writer；相符 WORK/EXTERNAL_WORK 目錄、CURRENT 候選與 QA/建置收據均未找到。完整觀測見 `inputs/PREFLIGHT_OBSERVATION_R01.json`。
- 不寫 GitHub；不改候選 Word、shared facts 或 CURRENT；不宣稱 QA PASS 或正式接受。

收據：`SOURCE_PREP_RECEIPT_R01.json`。
