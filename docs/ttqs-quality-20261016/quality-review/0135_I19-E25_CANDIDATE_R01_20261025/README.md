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
- Antigravity CLI Writer：曾明確要求 `gemini-3.8-flash-high`；CLI 回傳文字，但原始結果未提供可核實的實際 serving model identity。回覆含無來源檔案路徑、REAL 占位及未有依據的正式扣分說法，故未採用。完整原始輸出及審核在 `worker/`；不可記成 Gemini 已驗證成功。
- 本份正文由 Codex 根據官方來源、Unique Blueprint 及 SAMPLE 資料重新整理撰寫。不得將其說成由任一外包 Worker 交付。
- exact-SHA 獨立語意審查：PENDING。依 2026-10-23 Human 提供的 OpenCode 模型監控資料，曾對目前目錄列出的 `opencode/deepseek-v4.1-flash-free` 發出一次短審查；原生回傳 429 免費額度耗盡，無審查正文。原始輸出和派工收據在 `worker/OPENCODE_0135_SEMANTIC_REVIEW_R01_*`。未重試其他模型，未將候選升格。

## SAMPLE / REAL 邊界

本件 20/80、24/80、28/80、15 組配對數據及其趨勢均為 SAMPLE / SYNTHETIC，僅示範分子、分母、回覆率、中央値與限制如何計算。它們不是原始點協會實績、正式市場母體、核准或評核結果。協會真實名冊、問卷原件、工時記錄、期限證據及決策紀錄目前為 UNKNOWN，取得前不得替換示範資料或聲稱成效。

## 計算摘要

- 年度市場覆蓋示範：20/80=25.0%、24/80=30.0%、28/80=35.0%；每年 +5.0 個百分點；相對增幅分別 +20.0%、+16.7%。固定 80 家母體僅為公式示範。
- 15 組配對示範：月報中位工時 120→90 分鐘，差 30 分鐘，下降 25.0%；準時率 8/15=53.3%→12/15=80.0%，提升 26.7 個百分點。
- 配對回覆率 15/28=53.6%；未回覆 13 家仍列分母，不外推到 28 家或更大市場。
- 無對照組，不作訓練因果推論。

## 目前不能宣告的事項

獨立 exact-SHA 語意驗收未完成；REAL 證據未提供；Human 正式接受未授權。視覺與計算檢查只對本 README 所列 SHA 有效，不代表 TTQS 正式分數或文件已可作為協會真實紀錄。

Official full source PDF and the page 7-8 extract remain in the existing public source package: `docs/ttqs-quality-20261016/quality-review/0135_I19-E25_SOURCE_PREP_R01_20261024/source`. They are not duplicated here. The candidate package includes the exact textual mapping, source packet, unique blueprint, evidence excerpts, synthetic data, and hashes needed to trace this candidate.
