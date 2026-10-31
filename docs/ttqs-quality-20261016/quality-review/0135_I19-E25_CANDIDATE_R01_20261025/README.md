# 0135 I19-E25 市場與顧客價值成效分析報告 R01

## 候選狀態

DOCX 0135 對應官方 I19-E25，並以專案 157 指標第 140 項作內容設計。官方印刷方框流水號仍為 UNKNOWN。第 141、142 項及 28 個未命名 Other 均另有用途，本件不代替它們。

本地已完成完整候選文稿、12 張表、15 組合成配對示例、替換清冊、計算檢查、Word 原生 PDF 匯出及 10 頁逐頁視覺檢查。它仍是 CANDIDATE；沒有協會 REAL 原件，也沒有 Human 正式接受。

## 候選與驗收位元組

- DOCX SHA-256：`cae8be8280456b51a1294ee90eafca0ac1ae8a12738289d6ebbca35b3a05a3da`
- 正文 Markdown SHA-256：`e251cec14fc1e80244a206b4ba852e4b30356c786013f248dcf43459d2136e0b`
- 替換清冊 SHA-256：`044bb6428e5b36fa6d1c0b7c162ac7c771f8fbd7f9fc97a5a86a3e012d790f88`
- Word 原生 PDF SHA-256：`836ce81d08d096fa856e5a20ed40e005b2ac5a4c58d056397d151505e29e8362`
- 版面收據：`qa/VISUAL_QA_0135_R01.json`；技術與數據收據：`qa/TECHNICAL_QA_0135_R01.json`
- 正式需求、Blueprint 與合成資料來源：見 `source/SOURCE_MANIFEST_0135_R01.json` 及其引用檔。來源內容以分支 commit `8ff5f8cbe6df80be9ed60577ed324e5a0a18f382` 建立；R11 控制規格已在目前 PR HEAD 重新讀回。

## Worker 真實狀態

- OpenCode v2 Writer：曾要求 `opencode/glm-5.3-flash-free`，原生回傳 429 `Free usage limit reached`，沒有文稿，沒有採用。原始回覆在 `worker/OPENCODE_0135_R01_RAW.jsonl`。
- Antigravity CLI Writer：曾要求 `gemini-3.8-flash-high`；原始結果未提供可核實的實際 serving model identity，且含無來源檔案路徑、REAL 占位及未有依據的正式扣分說法，故未採用。完整歷史原始輸出及審核保存在既有 `worker/`。
- 本份正文由 Codex 根據官方來源、Unique Blueprint 及 SAMPLE 資料整理撰寫。不得將正文說成由任一外包 Writer 交付。
- 本頁所列 R12 是針對既有 Codex 候選的獨立 CLI 審查，請求模型為 `gemini-3.8-flash-high`，但實際服務端身分 UNKNOWN；它不改變 Writer 歷史，也不證明 Gemini 配額或模型路由。

## SAMPLE / REAL 邊界

本件 20/80、24/80、28/80、15 組配對數據及其趨勢均為 SAMPLE / SYNTHETIC，僅示範分子、分母、回覆率、中央値與限制如何計算。它們不是原始點協會實績、正式市場母體、核准或評核結果。協會真實名冊、問卷原件、工時記錄、期限證據及決策紀錄目前為 UNKNOWN，取得前不得替換示範資料或聲稱成效。

## Antigravity R12 獨立語意審查（同一候選 SHA）

- 結果：reviewer 原始 JSON 回覆為 `PASS`、無 blocking/nonblocking findings；本地裁定標示 `PASS_TEXT_ONLY_WITH_PROVIDER_IDENTITY_UNKNOWN`。
- 審查精確綁定 DOCX SHA-256：`cae8be8280456b51a1294ee90eafca0ac1ae8a12738289d6ebbca35b3a05a3da`；review packet SHA-256：`120ebf90abc83e931c5a34f505142d706d0c0ae6c11dcc98989302981878c9f9`。候選 DOCX 前後 SHA 相同，未重建或修改。
- 工作 ID：`TTQS-0135-I19-E25-R01-W2-ANTIGRAVITY-R12-EXACT-SHA-REVIEW`。Antigravity CLI 1.4.7；要求模型 `gemini-3.8-flash-high`，但實際 serving model／供應端身分為 `UNKNOWN`，不宣稱 Gemini 路由已證實。CLI exit 0，PID 82660，conversation `b1dcba37-8eb8-49ec-8515-9628ad18c090`；28,286 tokens（input 20,300 / output 7,986 / thinking 6,175 / cache 0）；費用／計價狀態 UNKNOWN。
- 審查涵蓋正文語意、計算、SAMPLE/REAL、相鄰需求區分及操作可用性；**不涵蓋** DOCX 二進位結構、Word 版面或視覺。既有同 SHA 技術與 10/10 頁視覺收據仍分別維持原範圍，不把文字審查擴大成全項品質 PASS。
- 原始 request、完整 stdout/stderr、response、dispatch/input/terminal 收據及 CLI/model-list 觀測保存在 `independent_review/ANTIGRAVITY_R12_20261027/`。R11 的歷史審查／部分裁定保留在歷史收據；R12 不覆寫其來源。
- 候選仍為 `CANDIDATE`；REAL 原件仍 UNKNOWN；沒有 Human 正式接受。

## OpenCode v2 R12 補充獨立語意審查（2026-10-27 08:22 TPE）

- 結果：`PASS_TEXT_ONLY_WITH_TWO_NONBLOCKING_FINDINGS`；原始 reviewer verdict 為 `PASS`，0 項阻擋、2 項低度非阻擋。審查對象仍是同一 DOCX SHA-256：`cae8be8280456b51a1294ee90eafca0ac1ae8a12738289d6ebbca35b3a05a3da`，沒有改 Word 位元組。
- 實際模型由 sanitized OpenCode session export 證實為 `providerID=opencode / model=glm-5.3-flash-free`，與請求 slug `opencode/glm-5.3-flash-free`一致；捕獲紀錄沒有 fallback 或工具事件。OpenCode v2 CLI 2.1.4、PID 92176、session `ses_e8544289bffeNRi5T4R1l2X87Y`、exit 0、56.686 秒；session 回報 cost $0，tokens input 14,697 / output 1,791 / reasoning 718 / cache-read 2,432 / cache-write 0。
- 審查輸入綁定 source packet SHA `fe4e433924b21b9891ca61ca52907e56a9dbd9ac62a4fd6fc43a9e4faef19696`、Unique Blueprint SHA `cb936466e92bb2d5976a2be1a013d85ccdd3a8bbe434dd8b51ac3d77e12d25c1`、request SHA `27559a01d07d0adcf1222287865ea2de6e9aadad6ad430974b7570786f08d7c5`，以及正文抽取 P001–P396。Reviewer 檢查 I19-E25 文類與 12 項 Blueprint、數學、SAMPLE/REAL、0133/0134 近鄰、141/142 排除、實際可用性及遮住標題後的辨識度。
- 非阻擋發現：① 分析與限制內容已在第 7 節等處，但沒有獨立編號「8. 分析」標題；只是 Blueprint 編號一對一呈現的可選改善。② 15/28=53.6%、13/28=46.4% 的一位小數四捨五入正確，顯示 53.57% 僅為可選補充。
- Reviewer 本身沒有開啟／重新計算 DOCX 二進位 SHA；它依提供的正文抽取及 SHA 欄位審查。本機派工前後均重新計算候選 SHA，確認一致。這份語意審查不覆蓋 DOCX 結構或版面；原技術收據 `e775c8ed9a143ba8d67fd808ac0d191b4095ce0cfaa27e9adfb412345c11358d` 與視覺收據 `0e4bb3b9bf5256c8fd082697e2f9376f709516271b989df5de375334b4ac3acb` 僅保有各自範圍。
- 原始 response SHA `f5d73a8d010da4ceec811f5cb3754af1d8baf100f53b1211ba5b679275ca7af7`、stdout SHA `5b743e90485525ee05cddc6c57eb9a017bccfbb6aed950bb7700a3c98df2433e`、session export SHA `f80deda674cb7304152029009228d14d0697b409acd0a6762da18a357827966f`、terminal SHA `e5a5d165260703bd54e20cec61720e3551a9befa64f0452c27ba74e8bce6bc72`、adjudication SHA `6eb3bf68a33c52ae49a2e2a507118bf4984b31d5eeb9c036feae9aa63d441ee3`。完整原始收據位於 `independent_review/OPENCODE_R12_20261027T0819/`。
- 上面的 Antigravity R12 是另一份同 SHA 審查；其要求 Gemini 的實際 serving identity 仍 UNKNOWN。OpenCode 這次的模型確認不能替 Antigravity 或 Gemini 額度作證。

## 計算摘要

- 年度市場覆蓋示範：20/80=25.0%、24/80=30.0%、28/80=35.0%；每年 +5.0 個百分點；相對增幅分別 +20.0%、+16.7%。固定 80 家母體僅為公式示範。
- 15 組配對示範：月報中位工時 120→90 分鐘，差 30 分鐘，下降 25.0%；準時率 8/15=53.3%→12/15=80.0%，提升 26.7 個百分點。
- 配對回覆率 15/28=53.6%；未回覆 13 家仍列分母，不外推到 28 家或更大市場。
- 無對照組，不作訓練因果推論。

## 目前不能宣告的事項

同一候選 SHA 現有 Antigravity 與 OpenCode 兩份 R12 文字審查。OpenCode session export 證實實際模型為 opencode/glm-5.3-flash-free；Antigravity 所要求的 Gemini serving identity 仍 UNKNOWN。OpenCode 審查有兩項低度非阻擋發現，且沒有檢查 DOCX 二進位或版面；技術與 10/10 頁視覺收據維持各自範圍。REAL 證據未提供，Human 正式接受未授權；候選不得視為 TTQS 正式分數或協會真實紀錄。

Official full source PDF and the page 7-8 extract remain in the existing public source package: `docs/ttqs-quality-20261016/quality-review/0135_I19-E25_SOURCE_PREP_R01_20261024/source`. They are not duplicated here. The candidate package includes the exact textual mapping, source packet, unique blueprint, evidence excerpts, synthetic data, and hashes needed to trace this candidate.

GitHub raw-byte readback: `GITHUB_READBACK_RECEIPT_R01.json` records 55/55 package files exact at commit `353ce83f5efb582876310c1885cba5a4bfe33cbd`; the receipt covers byte identity only.
