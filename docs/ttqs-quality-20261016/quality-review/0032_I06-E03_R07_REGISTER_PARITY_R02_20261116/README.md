# 0032 / I06-E03 / R07 登錄簿同位修復 R02

- Work ID: `TTQS_ONE_0032_R07_REGISTER_PARITY_R02_20261116`
- 狀態：`CANDIDATE_ONLY`; 正式接受未授予；REAL 原件仍為 `UNKNOWN/HOLD`。
- 限定變更：只修正 `SYN-032-152.synthetic_value`，由 DOCX 表格 33、列 6 的 cell 1 + cell 3 精確串接；cell 2 是替換指示，不納入。R01/R02 逐列比較確認 153 筆資料只有此一欄位改變。
- QA 範圍：重新抽取同一候選 SHA 的表格 33、列 1–7，147–153 七筆全數 exact match (`PASS_SCOPED_7_OF_7`)。這不是整份 153 筆 register 的全面 PASS。
- DOCX 未改寫，SHA-256=`e1d6311e9828f464aba7b9bc47c20fa8b5392951dba96cf9a71d77be73fb691f`。既有 semantic/visual receipts 均綁定此 SHA；本次未重跑視覺檢查。
- 官方需求：I06-E03「訓練機構具備執行訓練業務相關職能的說明。」官方佐證表第 2 頁。Blueprint extract 的來源檔 SHA-256=`406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`；raw row SHA-256=`8edcf9bc9cf412657d6a702e0da3c8dc5ddb22b4aa6c53ff52e1fbe8f310f07f`；canonical row SHA-256=`05bf2e51d1968830c7f1afb699d74202bc944eab00ef4a313893cc5665e95c1f`。官方 PDF SHA-256=`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。
- Worker：W1 OpenCode v2 requested route `opencode/beam-free`; session outcome succeeded, CLI exit `UNKNOWN`, serving identity `UNKNOWN`。W2 Antigravity CLI requested `gemini-3.8-flash-high`; exit 0, `PASS_SCOPED`, observed tool invocations 0; actual serving model and provider billing `UNKNOWN`。兩次錯誤呼叫及原始 stdout/stderr 均保存。
- W1/W2 的用途是限定 cell-binding proposal/review；不替代全文 semantic review，也不授予 formal acceptance。
- 收錄範圍：候選 DOCX 原始位元組、official Blueprint extract/source register、R01/R02 derived registers、確定性 QA、原有 same-SHA semantic/visual receipts、兩名 Worker 的輸入/輸出/程序收據及失敗嘗試原始輸出。