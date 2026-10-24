# 0132 I19-E21 候選與驗收證據

## 狀態

- 文件：0132；內部要求：I19-E21；157 項 Blueprint：I19-L3 index 145；官方資料表第 8 頁。印刷方框流水號：UNKNOWN。
- DOCX：CANDIDATE R01，SHA-256 `e2f263c2c130d1939ebdaab1a253700935c54c8a26c937b8a77e7000a9a2d925`。
- 內容及算式確定性檢查：PASS。Microsoft Word 原生輸出及 10 頁逐頁目視版面檢查：PASS。
- 獨立 exact-SHA 語意審查：PENDING；正式接受：NOT_GRANTED；真實協會績效及原件：UNKNOWN。

## 來源與內容邊界

官方要求原文為「個人產品不良件數有下降趨勢。」官方 PDF、157 指標 Blueprint、142 文件 crosswalk、正式 Mission 與寫作手冊的來源 blob 均列於 `source/SOURCE_PROVENANCE_0132_R01.json`。本文件採專屬產品不良單位及受檢產品單位分母，不套用相鄰的 0131 學員就業／證照或 0133 班次／人次內容。所有案例、日期、產品、批次、責任代碼和數據都是 SAMPLE/SYNTHETIC；沒有原始點協會實績、核准或第三方原件。

訓前 13/66=19.7%，訓後 8/70=11.4%，差 −8.27 個百分點；訓後同時更換材料批號並導入裁切導板，不能據此歸因於訓練。算式與替換來源逐項記錄於正文、CSV 清冊及 QA 收據。

## CLI 派工回收

- OpenCode v2 CLI 2.0.32 曾請求 `opencode/deepseek-v4.1-flash-free`。供應端回覆 Free usage limit reached / HTTP 429，程序 exit 1，1.18 秒，stdout 681 bytes；實際模型身分 UNKNOWN，沒有可採用文稿。原始輸入、提示、JSONL 回覆及派工收據一併保留於 `worker/`。
- 本候選正文由 Codex 在免費 CLI 拒絕後撰寫，不冒稱為 OpenCode 產物。Antigravity 本文件未派工：現有證據不足以保證實際 Gemini 3.8 Flash High 身分且排除 fallback；不以非空回覆冒充模型驗證。
- 沒有使用 Computer Use、付費路由或權限繞過。Token 用量：UNKNOWN。

## 驗收範圍

`qa/CONTENT_QA_0132_R01.json` 保存來源對照、逐批算式、分母和替換簿檢查；`qa/TECHNICAL_QA_0132_R01.json` 綁定 DOCX、建置收據、Word PDF 及 10 張頁面影像 SHA。Word 輸出由 Microsoft Word Office16 COM 隱藏、唯讀開啟並匯出；每頁均已逐頁目視。技術／版面 PASS 不代表獨立語意 PASS 或正式接受。

此套件所列 `quality-review/` 路徑為此次 PR 同步目標；推送與遠端讀回另以提交和 exact-byte 收據確認。
## GitHub 位元組同步校正

首次推送提交 `57610e6e44aa16e7eb9cad36eb8017c345651b23` 後，原始位元組回讀辨識出 Windows `core.autocrlf=true` 將 10 個文字收據轉成 LF；DOCX 位元組一致。完整失敗清單見 `qa/GITHUB_RAW_BYTE_READBACK_INITIAL_FAILURE_0132_R01.json`。本套件加入只作用於 0132 子目錄的 `.gitattributes` `* -text` 規則，保存現有本機 bytes；沒有改全域 Git 設定，也沒有重建 DOCX。修正推送後逐檔回讀待本次提交確認。