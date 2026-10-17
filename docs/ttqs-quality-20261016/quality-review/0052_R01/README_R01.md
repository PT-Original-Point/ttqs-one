# DOCX 0052 R01 候選套件

## 身分與狀態

- DOCX 0052；Unique Blueprint `I11-E04`；官方方框流水號 `054`。
- 文類：課程意見回流與課程修訂策略／計畫。
- 狀態：`CANDIDATE_NOT_PROMOTED`；全案均為 `SAMPLE / SYNTHETIC`，未取得正式接受。
- DOCX SHA-256：`406d1ef2c6e9b6266ea1adaeadedc5dfac77964fe76f73c2471168220ee6d455`。

## 驗收摘要

- OpenCode CLI V2 獨立語意結果：`PASS_WITH_SCOPE_LIMITATION`；reviewer 未自行逐頁目視 PDF。
- 另行以同一 DOCX exact SHA 產生 Word 固定版 PDF，16/16 頁原解析度目視 PASS。
- 技術 QA：正文最低 10.5 pt、表格最低 9.5 pt；186 筆替換資料皆有定位及 REAL 替換欄；數字與 360 分鐘課程總時數重新計算一致。
- 真實協會回饋、課程執行、授權核准仍是 UNKNOWN／未取得。

## 套件索引

- `candidate/0052_R01.docx`：候選文件。
- `inputs/`：官方原始頁面影像、Source Map、Unique Blueprint 列副本。
- `evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`：逐事實替換清冊。
- `evidence/render_final_406d1ef2/`：固定版 PDF、16 頁 PNG、4 張聯絡表；只同步此 final render，舊版 render 資料夾不屬於候選交付。
- `evidence/build/`：可重現建置程式與 build metadata。
- `evidence/qa/`：技術／版面 QA 程式及結果。
- `review/packet_R01/`：送獨立 reviewer 的內容與請求。
- `review/opencode_v2_R01/`：OpenCode V2 原始 stdout/stderr、exit code 及 exact-SHA 結果摘要。

`artifact_manifest_R01.json` 列出本套件正式保存的檔案 SHA-256 與大小；manifest 自身不列入其檔案清單。
