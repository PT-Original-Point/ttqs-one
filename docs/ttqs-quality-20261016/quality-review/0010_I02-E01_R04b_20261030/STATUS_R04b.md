# 0010 / I02-E01｜R04b 候選與驗收狀態

- 官方要求：對學員訓練成果有評核標準的訂定及說明。（正式來源列印頁 1，指標 2）
- 唯一 Blueprint：I02-E01；範圍衝突維持 PARTIAL/UNKNOWN。
- Word 候選 SHA-256：`9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe`；狀態 CANDIDATE / SAMPLE / SYNTHETIC。
- 確定性檢查：PASS_WITHIN_LISTED_DETERMINISTIC_SCOPE；19 項檢查均通過。包括 DOCX/原生 Word PDF、字級下限、20 題/四構面、初評及複評計算、157 筆清冊與內嵌順序一致。
- 視覺檢查：PASS_WITH_LAYOUT_NOTE；28 頁全數以 contact sheets 檢視，另全尺寸檢視第 5、14、16、24、27、28 頁。第 28 頁保留兩筆延續資料及較多留白，沒有空白頁或資料截斷。
- 獨立語意審查：PENDING。舊 R04 OpenCode 呼叫在 2026-10-30 00:08 TPE 回 HTTP 429/free-limit，無語意回覆；其審查包綁舊 Markdown SHA `131b703267feebfbef3ec49fc8aa9beaab2ded0818415e9e5d86771b84925d90`，不得套用至 R04b。R04b 精確審查包已準備，未在冷卻期內重試；供應端提供的 `retryAfterMs=30381000` 所示最早可重試時間為 2026-10-30 08:34:47 TPE。
- REAL 資料、協會採用、正式核准及 Human 最終接受：UNKNOWN / 未授權，不宣稱完成。

## 獨立語意審查結果（2026-10-30）

- 審查者：獨立 Codex 子代理；審查時間 2026-10-29T22:20:18Z。
- 結果：PARTIAL，綁定候選 SHA-256 9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe；審查前後候選 SHA 相同，文件未修改。
- 主要缺陷 SEM-01：第 5 節禁止評核者提示，但第 6 節 Level-2 錨點與第 9、11 節示範觀察紀錄依賴提示，現行操作法無法重現該評分。需定義一致、界限清楚的標準提示程序並套用到案例，或移除提示依賴並重評受影響案例。
- 缺陷 SEM-02：複測流程稱使用新題本版本，但複測仍使用第 4 節 Q1–Q20 與同一答案鍵；複測情境／版本缺少具名控制卡；兩筆複測答案向量清冊定位指向第 8 節，實際資料在第 11 節。
- 其他限制：Blueprint 對外政策／公開揭露欄位適用範圍維持 PARTIAL/UNKNOWN；缺少真實合格人員名冊與可用時程，實際採用前仍須確認並維持無獨立覆核者即 HOLD。
- 語意審查未檢查版面；先前 28 頁 Word 原生匯出與視覺收據仍各自維持原有範圍。本結果不代表正式接受、REAL 證據或協會核准。
- 原始獨立審查回覆：evidence/CODEX_INDEPENDENT_REVIEW_R04b_ORIGINAL_RESPONSE.md；檔案 SHA-256 f45a7e50469e2d7d8f895f0b930709d71600bdce5ad980bdd13f9f34bf997988。
