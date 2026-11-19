# 0013 / I02-E04 — 年度訓練課程公開清單（R05 候選）

## 候選識別與來源

- 文件：`0013`；官方需求：`I02-E04`「公開公布訓練機構年度訓練課程。」
- 唯一 Blueprint row SHA-256：`b529f3c13e964b6edbec124158d3559df988b401ce3b97fd1984e90b0582d35b`
- `BLUEPRINT_CURRENT.jsonl` SHA-256：`406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`
- 官方來源 PDF（page 1）SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`
- 專屬來源包 SHA-256：`b87440b249ec78c6bbe69ff001fe9d7dbb5060d65f27fe61d21ec48cdb5bfa63`
- 原始 Worker Markdown SHA-256：`0f8f3961ec945e9e7fd6aa91464bb73ed65afcf0a31a3523ff303d7534175d4f`

## 文件與本次修正

- DOCX：`candidate/0013_I02-E04_R05.docx`
- DOCX SHA-256：`2bf0407de7f24ad580cbb39df8365cbf2bc69feef97d069575daa3012a1b16d6`
- 由 R04 的獨立語意審查 PARTIAL 導出三項最小修復：補正來源包現況、修正附件索引（版本狀態在第 14 節、合成清冊在第 13 節）、統一 R05 DOCX 候選身分與交付界線。沒有重寫四門課程、主要表格、數據或公式。R04 候選及完整原始審查回覆保存在 `history/R04/`。

## 可操作示範與驗收

- 20 張表、220 列、四門完整 SAMPLE/SYNTHETIC 課程，各含九項公開欄位。
- 訓練時數合計 `6+12+6+6=30` 小時；示範名額 `20+18+20+16=74`。
- 完整度示範：35/36 = 97.2%，補齊至 36/36 = 100%。
- 67 筆具唯一 ID 的 SYNTHETIC 事實替換清冊；示範網址均使用 `.invalid` 保留網域。
- 技術 QA：`PASS`，綁定上述 DOCX SHA；含來源、Blueprint、表格、數學、鄰件辨識、樣本界線、字級及 Word 開檔檢查。
- Word 原生 PDF 25 頁，版面：`PASS_LAYOUT_ONLY`。第 1–5、25 頁因修正而逐頁目視；第 6–24 頁與 R04 像素一致並承接其視覺檢查。
- 獨立語意審查：`PARTIAL`，exact SHA 為上列 R05。審查指出「已填欄位」不等於公開連結可用（四個示範網址皆是 `.invalid`，公開仍 HOLD）；Table 19 也欠逐事實責任角色與欄位精確定位。完整原回覆保存於 `evidence/receipts/semantic_review_R05_original_response.md`。收據 visual 狀態欄位矛盾已對齊；不影響 DOCX SHA。不得將 R05 標成 PASS，R06 必須完成定點修正並重新語意審查。

## 真實資料邊界

本件僅為 `CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED`。未取得協會真實課程發布、核准、招生、出席、授課或成果原件；不宣稱任何正式公開、核准或訓練成果。正式使用需以有權來源取得 REAL 資料與核准並保留公開讀回；Human 正式接受狀態為 `UNKNOWN`。

本包的 `package_manifest.json` 只列出自身以外的檔案 SHA-256 和位元組數。GitHub 遠端讀回收據及最終 manifest 將在同步後另行追加。
