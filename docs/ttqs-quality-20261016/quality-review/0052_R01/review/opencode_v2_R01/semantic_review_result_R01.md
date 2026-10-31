# 0052 R01｜獨立 exact-SHA 語意審查結果

## 審查身分

- 路由：OpenCode CLI V2 `opencode v2.0.29`；執行回報：OpenCode runtime、`opencode/beam-free`（Beam Free）。
- 原始回覆：`opencode_v2_stdout_R01.txt`，SHA-256 `46fe63123e5e4c988e674a9ac1a5abae3780002343f0d5a06572b08f32f265c4`。
- stderr：`opencode_v2_stderr_R01.txt`，SHA-256 `c80e29fa4f4a3b278d9fd48ce252b119965dc454e524d64548be4760b7cf1f4d`；CLI exit code `0`。
- 審查請求及提供來源列於 `packet_R01/REVIEW_REQUEST_R01.md`；原始 stdout/stderr 保留，不以本摘要取代。

## 綁定候選

- DOCX `0052 R01`；Unique Blueprint `I11-E04`；官方方框流水號 `054`。
- reviewer 實際讀取 64,310 bytes，並重算 SHA-256：`406d1ef2c6e9b6266ea1adaeadedc5dfac77964fe76f73c2471168220ee6d455`，與本機候選相符。
- 候選及所有例子保持 `SAMPLE / SYNTHETIC / UNKNOWN`；正式接受、核准與升格均未授予。

## 審查結果

| 項目 | 結果 | reviewer 定位／範圍 |
|---|---|---|
| 官方要求、Blueprint 身分與策略計畫文類 | PASS | 封面、§1 pp.1–2、§14 p.14 |
| 標題盲辨識：回饋→分析取捨→課程修訂→下輪驗證 | PASS | §§4–11 pp.5–12 |
| 問卷、逐列合成資料、分母/缺答、流程、責任、例外與追蹤之可操作性 | PASS | §§2–8、§§10–14、附錄 A/B pp.3–15 |
| 數學、比例、加權方案與課程分鐘數 | PASS | §§5–10 pp.6–11；未發現差異 |
| 跨文件案例與非因果限制 | PASS | §§1、12、14；未發現衝突 |
| SAMPLE/REAL、UNKNOWN、替換清冊與反造假界線 | PASS | 封面、§§3、13、15、186 筆資料清冊 |
| 協會承辦及評核人員實際使用 | PASS | 全文與附錄 A/B |
| reviewer 本身的頁面目視 | PARTIAL | reviewer 說明未在其 runtime 逐頁目視 PDF/圖片；只確認文字抽取、表格及程式化字級下限 |

reviewer 逐題重算學員 Q01–Q07、結訓追蹤 G3–G5、8/12 與 5/12 示範回覆比例、支持選項的重疊/互斥，以及 A/B/C 的 4.30/4.20/4.25 加權分與 360 分鐘課程總時數，均相符。「目前不需要」為互斥選項，三項支持可重疊。

**整體語意結果：`PASS_WITH_SCOPE_LIMITATION`。** reviewer 未找到實質語意缺陷；其第 8 項頁面目視範圍為 PARTIAL。DOCX 不因本審查重建。另以 Word 固定版 PDF 對同一 DOCX 做 16/16 頁原始解析度目視及版面檢查，技術/版面收據為 PASS，PDF SHA-256 `3497e56e05774101a5365ab56e6f452a73f55c32dbb9aee7109d51fbc8414e1d`；該項是分開的 Codex 視覺驗收，不冒稱 OpenCode reviewer 已看圖。

## 範圍說明及非阻擋控制修正

1. reviewer 未獨立重算上游 DOCX 0033 R03、0049 R01、0050 R01、0051 R01 的位元組 SHA；其候選內引用與 SOURCE_MAP 一致。本機 QA 另逐一讀取上游候選位元組並重算 SHA，結果見 `evidence/qa/TECHNICAL_VISUAL_QA_R01.json`。
2. reviewer 發現 SOURCE_MAP 的清冊列數註記語意不清。審查後只更正該控制檔為「186 筆資料列，另有 1 列 CSV 欄名列」，並同步 `BUILD_METADATA_R01.json` 的來源圖 SHA；修正前 SHA `dd3d9b00967cc7a2eb7c147e052e04fa7b1c456c1edcc86c8ba73ce1f72e5159`，修正後 SHA `0b4d1a4f403633eed9db7d3b0164671ce5241231cbbe8fff078e2869e2ec319e`。此更正不改 DOCX bytes、不改案例數字或審查結論。
3. 官方 p.4 影像 bytes 之 SHA 與 Blueprint 列及 replacement register SHA，reviewer 已與提供值核對；上游來源文件的上述交叉檔案 hash 另由本機技術 QA 核實。

## 候選狀態

本審查是針對精確 SHA 的獨立候選審查，不是原始點協會正式接受、核准或 REAL 資料認證。候選維持 `CANDIDATE_NOT_PROMOTED`；真實學員/結訓學員回饋、實際課程活動、實際權限及正式核定原件仍為 `UNKNOWN` 或未取得。
