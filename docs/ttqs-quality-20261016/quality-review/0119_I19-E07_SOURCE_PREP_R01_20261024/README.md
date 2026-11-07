# TTQS ONE｜0119 I19-E07 候選與品質證據 R01H

## 狀態

- 文件：`doc_id=0119`；正式需求：`I19-E07`；候選版：`R01H`。
- 官方 PDF 第 8 頁；該方框沒有印刷流水號，故 `official_printed_checkbox_serial=UNKNOWN_NOT_ASSERTED`。
- 候選清單第 131 項、142 種子第 119 列、129→142 crosswalk 第 106 資料列，彼此不可互換。
- 候選 DOCX SHA-256：`60169b73895fc24bb1a0397534aa0ede37776c1ca3b7631a848bf4b69a9d312a`；67,078 bytes。
- 原生 Word PDF SHA-256：`365f1b9cc1d3190cd796b0bed775e8ce4b37d76a625cc63cdf03bbd8f3f8afd9`；23 頁。
- 正式接受：`NOT_GRANTED`。本文所有案例均為 `SAMPLE/SYNTHETIC_ONLY`，不代表原始點協會實績。

## 唯一來源與內容

- 來源包 SHA-256：`935a5cbc91c7dadfdcd0d9f3a7a45f56dcc5013ee9dd81fef1cfedd6b5b73656`。
- 專屬 Unique Blueprint SHA-256：`d097c7491235e323ebca4a31ff147ee5be2e6e5f893041087fd3076664aa0473`。
- Requirement mapping SHA-256：`f31661eb03b992c903f41c86076908deaf51e8a83fb26ff87d1cef2752d3d4a8`。
- 官方來源 SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`，定位 p.8；本包提供該頁文字定位摘錄與原始雜湊，不重複散布完整官方 PDF。
- `source/mapping_evidence_0119_R01.json` 保留 SOURCE_PREPARED 當時的 `review_status=NOT_STARTED` 歷史狀態；目前候選與 QA 狀態以 R01H 收據及 qa_concordance 為準。`R01G`（SHA-256 `effc5faaf957a42719da89f8457bdc1ae4865090f7d6957b8ec49eb1523d1da1`）是被替換的歷史父件，因表 12-1 表頭孤立而不作目前候選；其 DOCX 只保存在 `history/` 並標示為 superseded。\n- 文件是目標市場／顧客價值雙構面成對分析與核驗工作表。SAMPLE 公式涵蓋 M-01 `8/20=40%` 對 `12/25=48%`（`+8pp`）、C-01 `10/16=62.5%` 對 `15/20=75%`（`+12.5pp`）、兩期回覆率均 `80%`、及負向案例。分母、排除、資料來源、可比性、限制及 HOLD/NOT_DEMONSTRATED 規則均有表單欄位。
- SAMPLE 全欄位替換清冊位於 DOCX 表 12-1（R-01 至 R-16）；沒有獨立清冊檔。
- 0118 感謝函收存、0120 初步訓練成果、0117 考照與 0116 就業資料均明確劃界，不可代替雙構面證據。

## R01H 變更及驗收

- R01H 僅修正 R01G 的 Table 12-1 孤立表頭分頁，並更新三處可見版本標籤；實質段落及表格內容未變（不含版本標籤）。DOCX 只以 R01H 位元組為當前候選。
- 技術檢查：21 項；Word 可開啟、DOCX ZIP 完整、26 表、欄位/交叉引用、最小字級、公式與 SAME SHA 原生輸出等均通過。技術收據列出各項結果。
- 視覺：`PASS_LAYOUT_ALL_23_PAGES`；23 頁逐頁以原尺寸檢查，未見裁切、重疊、缺字、空白孤頁或孤立表頭。
- 獨立語意：Antigravity CLI 1.4.7；初始化回報實際模型 `gemini-3.8-flash-high`；exit 0、無工具呼叫；審查 10 項全 PASS、0 blocker，兩項資訊性發現。審查綁定 DOCX SHA 上列及完整抽取文字 SHA `fed3c440eb8d8c25e2dabd6d38637f315a73d7b91ed0b93b77f4ca173ec29c04`。此 PASS 只涵蓋語意/來源對照，不代表真實協會證據或正式接受。
- 收據欄位對帳：已修正技術收據過期的頂層 `PENDING`，並令語意收據指向目前技術收據 SHA。原始 Antigravity 回覆在 Windows 檔案 SHA 使用 CRLF；將 CRLF 正規化為 LF 後與派遣時回覆 SHA 完全一致，非內容差異。DOCX 位元組沒有改動。

## Worker 來源與限制

- OpenCode v2 CLI 2.0.32 實際回傳 35,219 bytes 稿件；R01A/R01G Builder 明確讀取同一 Writer response SHA `2e91b0051ce09ea37bf0e1f74db3658c588c7fde7ea57682585ab8d41fd4fbdd`，R01H 沿用 R01G 並作上述版面/標籤修正。
- Writer 收據為啟動快照，仍顯示 `RUNNING`。最後事件為 `step_finish / stop`，PID 36712 在事後讀回時不存在。原始 CLI exit code、實際服務模型與供應端成本均 `UNKNOWN`；不得把 OpenCode 服務存活或請求模型名稱當成模型身分/成功證明。
- Antigravity 原始審查回覆、派遣收據及回覆事件流均隨包保留。沒有 Computer Use。

## 遠端收錄界線

此為 PR #92 候選分支上的品質證據包；不是合併、正式送審或協會接受。所有示範資料只作方法演練。真實資料、核准、簽名及第三方原件均未提供，也未被此包宣稱。