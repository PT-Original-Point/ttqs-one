# DOCX 0052 R02 候選套件

## 身分與狀態

- DOCX 0052（交付文件編號）；Unique Blueprint I11-E04；官方 157 方框流水號 054。
- 文類：依學員與結訓學員意見規劃課程修訂的操作計畫。
- 狀態：CANDIDATE_NOT_PROMOTED；完整正文含 186 筆合成替換事實；沒有原始點協會真實課程回饋或核定紀錄。
- DOCX SHA-256：9129aff2bb730d31f76a5cb457ed069f1cafd2460b4069219f697b35d2c11afa。

## 本版內容變更

R02 是針對已定位的正文控制欄位外露與三處表頭對比問題所做的窄幅修復。保留原有意見問卷、結訓追蹤、數據分析、替代方案、360 分鐘課程修訂示範、表單和 186 筆 SAMPLE/SYNTHETIC 替換清冊事實；不因 metadata 更新或新收據重建內容。修復明細見 evidence/REPAIR_AND_VISUAL_QA_R02.md。

## 驗收狀態

- ZIP/XML 完整性與正文/表格/頁首頁尾控制資訊掃描：PASS。
- Word COM 固定版 16 頁 PDF；16/16 頁視覺覆蓋：PASS，頁面證據在 evidence/render_final/。
- 最新 exact SHA 的獨立語意審查：PASS（OpenCode CLI v2，逐頁檢視 16/16 頁；候選仍未正式接受）。
- 正式 TTQS 接受／協會核定：NOT GRANTED。
- R01 的歷史語意 PASS 只屬 R01 SHA；R02 有獨立 PASS 綁定本版 SHA。
- Reviewer 提出的三筆定位欄名稱已只修正替換清冊，保留原始 reviewer packet 與原始回覆，未改 DOCX 位元組。
- Word 核心屬性仍有 R01 舊標題，reviewer 判定為非阻擋外觀 metadata；未為 metadata-only 原因改寫候選位元組。

## 套件索引

- candidate/0052_R02.docx：可開啟的 R02 候選文件。
- inputs/：現行文類手冊、157 方框清單、Blueprint 與官方要求、歷史來源圖。
- evidence/SYNTHETIC_REPLACEMENT_REGISTER_R02.csv：完整替換清冊。
- evidence/render_final/：同 SHA 固定版 PDF 與頁面影像。
- evidence/REPAIR_AND_VISUAL_QA_R02.md：精確修復與視覺覆蓋範圍收據。
- review/packet_R02/：保留當時送審來源與更正補件。
- review/INDEPENDENT_SEMANTIC_REVIEW_R02.json：獨立 reviewer exact-SHA 結論與限制。
- review/opencode_v2_R02/：原始回覆、公開版工具紀錄及中止嘗試收據。
- evidence/CROSS_DOCUMENT_LINKAGE_R02.md：0033／0049／0050 的精確 SHA 與同案例事實核對。
- evidence/REGISTER_LOCATOR_CORRECTION_R02.md：修正三筆替換清冊定位，不改 Word 位元組。
- PROGRESS_R02.json：來源 SHA、候選狀態、驗收結果與真實缺口。
- artifact_manifest_R02.json：正式保存檔案 SHA-256 與位元組數；manifest 不列入自己的檔案清單。
