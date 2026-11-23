# 0132 I19-E21 候選與驗收證據

## 狀態

- 文件 0132；內部要求 I19-E21；157 Blueprint I19-L3 index 145；官方資料表第 8 頁；印刷方框流水號 UNKNOWN。
- DOCX CANDIDATE R01，SHA-256 e2f263c2c130d1939ebdaab1a253700935c54c8a26c937b8a77e7000a9a2d925。本次未改 DOCX 位元組。
- 確定性內容/算式、Microsoft Word 原生輸出與 10/10 頁視覺檢查 PASS。
- 既有 exact-SHA 獨立語意審查 PASS_TEXT_SEMANTIC，僅正文語意/可用性，綁定上述 DOCX SHA；原始回覆及仲裁位於 review/W2_EXACT_SHA_20261026/。Antigravity CLI 要求 gemini-3.8-flash-high，但原生回覆未提供 serving-model 身分，實際模型 UNKNOWN。
- 正式接受 NOT_GRANTED；REAL 協會資料/原件 UNKNOWN。

## 來源與內容邊界

官方要求原文為「個人產品不良件數有下降趨勢。」來源為官方佐證資料表第 8 頁 I19-L3。正文是產品不良率分析，不套用相鄰 0131 學員就業/證照或 0133 訓練班次/參訓人次證據。所有案例、日期、產品、批次、責任代碼和數據皆為 SAMPLE/SYNTHETIC；沒有聲稱原始點協會已有相同實績、核准或第三方原件。

訓前 13/66=19.7%，訓後 8/70=11.4%，差 −8.27 個百分點；訓後另更換材料批號並導入裁切導板，文件不把變化直接歸因於訓練。

## Worker 與回收狀態

原始 OpenCode Writer 曾請求免費 DeepSeek 路由並收到 HTTP 429，沒有可採用稿件；候選正文另由 Codex 建置，不冒稱為 OpenCode 產物。10/26 已有一份 Antigravity exact-SHA 獨立文字審查 PASS，實際 serving model UNKNOWN。

10/27 又發生一次不必要的同一候選審查派工：本機狀態索引缺少遠端審查樹，錯誤判定審查尚未執行。新回覆未採用，也不增加驗收範圍；DOCX 前後 SHA 相同。OpenCode GLM-5.3 free 同時回 HTTP 429，沒有文稿。原始請求、回覆及終態收據位於 PR #92 reports/R12_20261027/R12_CURRENT_DELTA_20261027/。

無 Computer Use、付費路由或權限繞過。模型實際身分及 provider 計費資料未知時均維持 UNKNOWN。

## 驗收範圍

qa/CONTENT_QA_0132_R01.json 保存來源、分母、算式及替換簿檢查；qa/TECHNICAL_QA_0132_R01.json 綁定 DOCX/Word PDF/頁面影像；qa/WORD_RENDER_VISUAL_QA_0132_R01.json 保存視覺範圍。獨立審查只涵蓋正文語意，不冒稱審查者目視 Word。合成資料清冊在 evidence/SYNTHETIC_REPLACEMENT_REGISTER_0132_R01.csv。
