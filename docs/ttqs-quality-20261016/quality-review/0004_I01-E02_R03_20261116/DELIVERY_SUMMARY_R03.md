# 0004 I01-E02 R03 施工交付摘要

- 文件：目標市場調查執行與樣本紀錄；狀態 `CANDIDATE` / `SAMPLE-SYNTHETIC`，未取得正式接受或 REAL 核准。
- DOCX SHA-256：`e3914144f13079b0673428a42d5b930c252ba0a223379deded49ea5ad1c5f08c`（59,306 bytes）；正文 SHA-256：`e61798ac0c63951e27d369e596c15d13711074fec253e9ddf09f000688e4e129`。
- W1 OpenCode Writer：`TTQS-0004-I01-E02-WRITER-R03-20261116`，route `opencode/beam-free`；匯出終態 `succeeded/stop`，費用 0，輸入 25,777、輸出 12,428、reasoning 13,499 tokens。原始啟動 receipt 的 RUNNING 已由 `WORKER_STATUS_RECONCILIATION_R01.json` 對帳；OS process exit code 未保存，故 UNKNOWN。
- W1 範圍修補：`TTQS-0004-I01-E02-SCOPED-REPAIR-R04-20261116`，exit 0、費用 0；修補正文 SHA `c76cadac11314f720f8e94ecb9774932a65c019afa9bbc3a4d8602356eb0dc31`。確定性 build QA 的 worker-response SHA 與此 SHA 相同，證明修補稿已用於候選。
- W2 Antigravity 語意審查：`TTQS_ONE_0004_I01E02_GEMINI38_FLASH_HIGH_SEMANTIC_R02_20261116`，要求模型 `gemini-3.8-flash-high`、實際服務模型 `UNKNOWN`；exit 0、0 tool call、語意 PASS、0 findings，精確綁定上述 DOCX SHA。用量：input 37,823 / output 5,297 / thinking 4,645 / total 43,120 tokens。
- QA：final exact-SHA 19/19 PASS；Word 原生開啟與 21 頁 PDF render PASS；正文最低 11pt、表格最低 9.5pt、22 表；全頁視覺審查 PASS。最終文件 SHA 及 W1/W2 收據採同一候選版本。
- 視覺收據範圍只證明版面；語意收據只證明文字內容。兩者均不授予 REAL、正式接受或協會核准。