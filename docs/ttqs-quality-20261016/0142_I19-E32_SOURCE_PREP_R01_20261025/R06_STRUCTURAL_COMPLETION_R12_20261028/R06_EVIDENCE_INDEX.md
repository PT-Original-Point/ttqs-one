# TTQS ONE｜0142／I19-E32 R06 候選證據索引

記錄日：2026-10-28（Windows 本機，Asia/Taipei）
GitHub：PT-Original-Point/ttqs-one；PR #92；分支 `work/ttqs-one-document-quality-contract-20261016`
同步前分支 HEAD：`05b7c8847a83062c0902a7f9303011f7f257f350`

## 狀態裁定

- 文件：0142；官方 requirement：I19-E32；157 方框索引 156；印刷 checkbox serial：UNKNOWN。
- 文件狀態：CANDIDATE；REAL 證據 UNKNOWN/HOLD；官方分數 NOT_ASSIGNED；正式接受 NOT_GRANTED。
- Antigravity CLI 對 R06 exact SHA 回傳語意審查 PASS。CLI 生成 metadata 與 resolver log 記錄 gemini-3.8-flash-high 選擇，但啟動曾記錄 defaulting to CCPA，conversation backend 欄位為 unspecified，沒有 provider 端服務模型證明；原始 PASS 已保存，合格模型路由的語意驗收仍 PENDING/ROUTE IDENTITY UNKNOWN。OpenCode 本機額度狀態未因公開服務狀態改變。
- 本次可判定的範圍限於確定性結構／算術檢查及 Word 版面檢視；不得將其描述為完整語意驗收或協會正式接受。

## 官方來源與唯一 Blueprint

| 來源 | 路徑 | 本機 SHA-256 | 遠端來源讀回 |
|---|---|---|---|
| Source Packet | `docs/ttqs-quality-20261016/0142_I19-E32_SOURCE_PREP_R01_20261025/R05_CANDIDATE_20261027/SOURCE_PACKET_0142_I19-E32_R01.md` | `e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49` | 以 Base64 位元組比對，與本機相同 |
| Unique Blueprint | `docs/ttqs-quality-20261016/0142_I19-E32_SOURCE_PREP_R01_20261025/R05_CANDIDATE_20261027/UNIQUE_BLUEPRINT_0142_I19-E32_R01.md` | `4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b` | 以 Base64 位元組比對，與本機相同 |

## 候選與驗收

| 項目 | 本機 SHA-256 | 判定 |
|---|---|---|
| `0142_I19-E32_CANDIDATE_R06.docx` | `60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6` | 候選；本機 Word 輸出前後 SHA 相同 |
| `SAMPLE_REPLACEMENT_REGISTER_0142_R06.csv` | `70eee17d5848be375ff4218e0f39324e1e81881991f9997f5ee5499d7455251e` | 19 列；保留原始 sample_fact_id，display_id F01–F19 對照 |
| `R06_REVIEW/0142_I19-E32_R06_WordNative.pdf` | `e88d5f5d9bd0020a04a2df8dd2094e15f48e0804afea0c267f9ef50de1e38000` | Microsoft Word 原生 COM 匯出；10 頁 |
| `R06_REVIEW/WORD_NATIVE_RENDER_RECEIPT_0142_R06.json` | `52c31076ef73bec6353096a6c9e6896ed1badb90b19e7b791f89194675ce18af` | read-only；匯出前後 DOCX SHA 一致 |
| `R06_REVIEW/PAGE_IMAGE_MANIFEST_0142_R06.json` | `e5703381250ac0b369da523c631014f31eead181d5e7b365a719fa0032f0d994` | 綁定 DOCX `60563d…f0e6`、PDF `e88d5f…38000`、10 頁及逐頁影像 SHA |
| `R06_REVIEW/VISUAL_QA_RECEIPT_0142_R06.json` | `0eb073a014e499266c9f20a9001c4f12ed9ae6ed6e5990c42b7c673f9e169258` | 版面 PASS；全 10 頁 contact sheet 檢視，9–10 頁全尺寸檢視；不是獨立語意審查 |
| `TECHNICAL_SEMANTIC_STRUCTURE_QA_0142_R06.json` | `f3838cde695754c572c4a0d732a21bf241c55be12747cf01c6107cf97537ea6b` | 收據列出的結構、來源界線及算術檢查全 PASS；不是語意 PASS |
| `BUILD_RECEIPT_0142_R06.json` | `c5070a8417cf990c211751d5db97e05a89f133c961906c222b41b7173c601967` | 記錄候選 SHA、來源 SHA、register SHA 及變更範圍 |


## Antigravity R06 exact-SHA 語意審查派工

- 原始回覆對 DOCX SHA `60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6` 給出 PASS；範圍只含提供的完整正文、Source Packet 及 Unique Blueprint，未作視覺檢查。完整 request、JSON stdout、兩次 stderr 及派工收據均已保存。
- 第二次有效 CLI 回合：Antigravity CLI 1.4.8、PID 75888、55.35 秒、conversation `eb226e65-0f89-4111-a87c-7691b25decc7`；input 19,830、output 7,024、thinking 5,045、total 26,854 tokens。第一次因 `--print` 旗標用法在本機解析失敗，exit 2，沒有有效審查回覆；修正旗標後只執行一次。
- CLI 的選定模型與 generation metadata 記錄 `gemini-3.8-flash-high`；log 同時有啟動時 `defaulting to CCPA` 訊息，conversation backend 為 `BACKEND_TYPE_UNSPECIFIED`，最終 stdout 不含 served-model 欄位。因此模型選擇有證據，provider 實際服務模型/無 fallback 證明仍 UNKNOWN；審查回覆保留，但不升格為合格路由最終 semantic PASS。
- conversation DB 唯讀讀回僅有兩個 step（14、15），均無子 trajectory；沒有觀察到 tool step。CLI stderr 另提示 plan mode 與停用 slash expansion 不相容。未使用 Computer Use，未執行檔案編輯或接受權限繞過。
- 此結果不變更 CANDIDATE、REAL UNKNOWN/HOLD、NOT_ASSIGNED 分數或 NOT_GRANTED 正式接受狀態。
## 實質修復與版面結果

1. 16 張實體表格均有 caption；逐列替換清冊 19 列含 18 項合成財務事實及 1 項非財務版次中繼資料。
2. 合成收入加總及成長率顯示到小數點後兩位；REAL 財報／總帳未提供，所有實際財務替換維持 UNKNOWN/HOLD。
3. 修復前清冊最後三列曾孤立於第 11 頁。最終 R06 移除第 12 節前的強制分頁，保持表格字級 9.5 pt；清冊在第 9–10 頁自然續接，第二頁重複表頭，F01–F19 全數可見。
4. 視覺影像輸出產生器曾沿用舊候選 SHA。已修正為每次從當前 DOCX 計算，並以 QA 收據檢查 DOCX、PDF 與影像 manifest 的 SHA 綁定。
5. 舊本機候選 `052fa925…91422`、`b424acbc…103c1`、`235a2335…87ffa` 均已保留在本機歷史資料夾；目前索引僅將 `60563d…f0e6` 定義為 R06 候選。

## 門檻仍未完成

- Antigravity 對 exact SHA `60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6` 已有原始 PASS 回覆；因 provider-served model attestation UNKNOWN，回覆尚不計為合格路由的最終獨立語意 PASS。派工收據與完整原始回覆見 `R06_REVIEW/ANTIGRAVITY_DISPATCH_RECEIPT_0142_R06.json` 及同資料夾 ATTEMPT02_STDOUT。
- 不得把 R05 回覆、另一候選 SHA 的審查、社群 OpenCode 狀態或本機 Builder／版面 QA 合併成 R06 語意 PASS。
- 無真實財務原件、法人資料或正式核准已在本候選被宣稱；REAL 仍 UNKNOWN/HOLD，正式接受仍 NOT_GRANTED。
