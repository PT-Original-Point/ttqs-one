# 0013 / I02-E04 — 年度訓練課程公開清單（R06 候選）

## 候選與來源綁定

- 文件 ID：`0013`；官方需求：`I02-E04`「公開公布訓練機構年度訓練課程。」
- 候選：`candidate/0013_I02-E04_R06.docx`，SHA-256 `3e1b0ce939ea4e1b3fe22adec1cbdab492af78d6b9a5646f41ddd394c4aa3d09`，67,561 bytes。
- 前版 R05 SHA-256：`2bf0407de7f24ad580cbb39df8365cbf2bc69feef97d069575daa3012a1b16d6`；R06 是針對其獨立審查 PARTIAL 的定點修復，不是重寫無關正文。
- 官方 PDF SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；精確原文位於第 1 頁。
- 專屬來源包 SHA-256：`b87440b249ec78c6bbe69ff001fe9d7dbb5060d65f27fe61d21ec48cdb5bfa63`。
- `BLUEPRINT_CURRENT.jsonl` SHA-256：`406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`；唯一 Blueprint row SHA-256：`b529f3c13e964b6edbec124158d3559df988b401ce3b97fd1984e90b0582d35b`。完整唯一需求及鄰項映射在 `evidence/official_blueprint_mapping.json`。
- 原始 Worker 文稿 SHA-256：`0f8f3961ec945e9e7fd6aa91464bb73ed65afcf0a31a3523ff303d7534175d4f`；原始稿與其 Worker 收據存於 `worker/`。

## R06 實質修復與驗收範圍

- Table 19 的 67 筆 SYNTHETIC 事實均有精確正文定位及 SAMPLE 責任角色代碼；Word 與替換清冊逐項相符。
- 35/36 欄位填寫率（97.2%）與公開連結可用性分開判定；四個示範連結均使用 `.invalid`，因此 0/4 可驗證，公開狀態維持 HOLD。
- 四個完整示範課程合計 30 小時、規劃容量 74 人；全數為 SAMPLE/SYNTHETIC。
- 確定性技術 QA：`PASS`，26 項檢查均通過，收據綁定本候選 SHA。正文最低字級 10.5 pt，表格最低 9.5 pt。
- Word 原生 PDF：25 頁，SHA-256 `22b91588cca0a5323388121675e23b07f59abf8aad04ddd82098471193a791a3`。25 頁皆有頁面影像；版面結果 `PASS_LAYOUT_ONLY`。直接目視本次變動頁，未變頁以與 R05 逐像素一致及其既有驗收範圍承接，詳見 `evidence/receipts/visual_qa_R06.json`。
- 獨立 R06 語意審查：進行中；原始回覆與 exact-SHA 結論尚未寫入本包。此時不得宣稱 semantic PASS 或 CURRENT。

## 真實資料界線與狀態

本文件為 `CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED`。未取得協會真實課程核准、公開發布、招生、出席、授課或成果原件；不代表正式核准或機構實績。Human 正式接受狀態 `UNKNOWN`。完整替換清冊在 `sidecar/0013_R06_SYNTHETIC_REPLACEMENT_REGISTER.csv`。

## 前版審查記錄

R05 的原始獨立審查、結構化結果及技術收據以原始內容收錄於 `history/R05/`。R05 完整套件仍保留在既有 PR #92 的 `quality-review/0013_I02-E04_R05_20261030/`；其檔案不在本次改寫範圍。

本套件 manifest 會在同步前產生；同步後須從相同 GitHub branch 讀回並逐檔比對 SHA-256。