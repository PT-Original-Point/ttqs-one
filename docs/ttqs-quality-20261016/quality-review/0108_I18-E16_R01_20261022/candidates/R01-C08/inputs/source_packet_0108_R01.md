# 0108｜I18-E16「提高薪資紀錄」來源包 R01

## 身分與來源錨定

- TTQS ONE 文件 ID：**0108**；官方要求：**I18-E16**；文類：`evidence_record`；官方佐證表第 7 頁。
- 157 項專案藍圖內部索引：**117**；不是官方印刷流水號。官方序號維持 `UNKNOWN`，除非從正式原表直接讀得。
- 本次 GitHub PR #92 候選分支 HEAD：`3dad3490872be0169cfbe9bb1b6564434694a8a6`。
- 官方 mapping `quality-review/0036_R13/inputs/mapping/checkbox_mapping_compact.json` Git blob：`ee3fc17e4e0e89a5b5d404c6f0ca7bd92a1a4f9b`；映射 0108 → I18-E16、第 7 頁、`0108__提高薪資紀錄_可直接使用成品.docx`。
- 157 Blueprint registry `03_157_CHECKBOX_BLUEPRINTS.md` Git blob：`8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`；第 117 項明確要求「提高薪資紀錄：外部薪資證據合規取得」。

## 官方佐證原文與限制

- 官方 PDF：`quality-review/0036_R13/inputs/official/TTQS_evidence_table_training_institution_source.pdf`；Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0`；SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。
- 官方 PDF 第 7 頁列有「提高薪資紀錄。」；對應文字抽取檔 `official_full_text.txt` 第 649 行，Git blob `687044213a0a349fc5167f8627657674708ba74d`。同頁第 648、650 行分別為 I18-E15「高證照通過率之證明資料」與 I18-E17「社群網站知識討論區，人員使用網站頻率」，不得把它們混入本件。
- 共用第 7 頁原頁渲染圖位於 `quality-review/0107_I18-E15_R01_20261022/inputs/official/page7_render_0107_source.png`，SHA-256 `b4b229b154ae401cff6305f8dd413d967ac7a347165d112c355fa15689a358a1`。它是同一官方表第 7 頁的共用來源圖，不是 0108 成品或協會證據。
- 此勾選只列為參考佐證，不自帶薪資增加門檻、因果證明或評核分數保證。薪資變動只能由可比對的正式來源證明；參訓前後的時間關聯本身不能證明訓練造成加薪。

## 文件邊界與安全

- 0108 要呈現一個班別／觀察期間內可追溯、可覆核的薪資變動紀錄；不是薪資調查、勞動市場行情報告、協會員工名冊、薪資單仿件或加薪證明書。
- 目前沒有原始點協會或學員的真實薪資、雇主、薪資單、扣繳、投保或同意紀錄提供給本案。正文只能使用專屬合成資料，所有人名、單位、期間、金額及文件代碼均須 `SAMPLE/SYNTHETIC`；真實結果維持 `UNKNOWN`，正式接受 `NOT_GRANTED`。
- 真實薪資文件含高度個資。不得將真實薪資單、身分證號、帳號、雇主識別、簽名、章戳或可反查資料上傳公開 PR；僅在有權限的正式來源保管，公開版使用遮罩索引及替換清冊。

## 下一施工階段

`READY_SOURCE_PACKET / READY_UNIQUE_BLUEPRINT` 已成立；0108 尚無既有候選 DOCX 或 Writer。本文包與專屬 Blueprint 通過來源和算術驗收後，才可派一個受限純文字 Writer。Writer 路由須先具備可用、無費用、無模型回退且可留原生回覆收據的條件；目前 OpenCode free-tier CLI 有 403，Antigravity 模型身分／fallback 仍 UNKNOWN，因此本來源階段不等於 Writer 已派或文件已完成。