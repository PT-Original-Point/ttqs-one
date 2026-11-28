# DOCX 0065｜I15-E01｜R02

## 狀態

R02 是可供閱讀與候選驗收的 SAMPLE / SYNTHETIC 示範文件，尚未取得 Human 正式接受，也不是原始點協會的真實會議、核准或辦訓紀錄。

- DOCX：candidate/TTQS_ONE_0065_R02.docx
- SHA-256：43eac240f56e1dc3dcd2d26820ae2a309b3db98eff7ef26af129f73ec1bbb856
- 官方具名需求：I15-E01
- 官方 checkbox 流水號：071
- Word 文件編號：0065
- 070 Other 不得替代 checkbox 071。

## 寫作與獨立審查

- Writer：OpenCode CLI v2.0.29，session 匯出確認模型為 opencode/deepseek-v4.1-flash-free；原始回覆與 session export 均附於 worker/opencode_deepseek_R01/。
- 獨立 Reviewer：OpenCode CLI v2.0.29，session 匯出確認模型為 opencode/beam-free；對上述 exact DOCX SHA 判定 PASS。原始 JSONL、完整回覆、session export 與 receipt 均附於 review/opencode_beam_R02/。
- Reviewer 未使用 Computer Use，也未修改檔案。

## 品質證據

- 技術：DOCX ZIP 完整；33 個表格；正文明列 0065 / I15-E01 / 071、SAMPLE / UNKNOWN / HOLD；正文最低 10.5 pt、表格最低 9.5 pt。
- 數學：出席、評量、問卷、追蹤、自述應用、模擬預算與 80 分鐘議程均獨立重算一致。
- 內容 parity：從正文 Markdown 抽出的 912 個文字項目均可在 exact-SHA DOCX 讀到；0060 R08 引用的 26 個 fact ID 全部列入 replacement register；正文附錄與 sidecar CSV 19/19 列完全一致。
- 版面：Word 唯讀匯出 PDF 共 21 頁，PDF 與頁面影像均附於 evidence/。R01 發現的四處孤立表題／表頭已在 R02 修正；12 頁直接目視檢查，另 9 頁以與 R01 完全相同的 PNG SHA-256 繼承既有目視結果。頁首每頁重複 SAMPLE / SYNTHETIC 警語。
- 0060 R08 跨文件來源 DOCX SHA-256：92962df774a7a16546829d8968dc274394fc1efcc12421c1a355f45127e9b5c3。官方原始佐證 PDF 與需求映射已在同一分支的正式來源資料中。

## 真實資料界線

會議、功能角色出席、意見、決議、日期及經費均為合成示範。協會實際授權、通知、簽到、核准、憑證與會議成果仍為 UNKNOWN / HOLD；不得作為正式實績或正式接受證明。

## 套件

- candidate/：可直接開啟的 DOCX。
- inputs/：0065 Unique Blueprint、R02 正文與 SAMPLE 替換清冊。
- evidence/：Word 匯出 PDF、21 頁 PNG 與技術／版面／parity receipts。
- worker/：OpenCode DeepSeek Writer 原始回覆及 session export。
- review/：Beam Free Reviewer 原始回覆、session export、審查 packet 與 exact-SHA receipt。
