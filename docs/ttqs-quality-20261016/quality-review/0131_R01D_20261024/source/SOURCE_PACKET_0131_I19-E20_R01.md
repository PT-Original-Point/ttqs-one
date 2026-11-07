# 0131｜來源包｜I19-E20｜R01

狀態：`SOURCE_PREP_COMPLETE_WRITER_READY`（可逆候選施工來源；尚無本版 Word 候選、REAL 結果或正式接受）。

## 文件與要求識別

| 欄位 | 經核實值 |
|---|---|
| project_id | `TTQS_ONE` |
| doc_id | `0131` |
| 文件名稱 | 學員證照通過與就業追蹤統計表 |
| internal_requirement_id | `I19-E20`，僅為內部 142 序列 crosswalk |
| project 157 Blueprint index | `144`，位於 `I19-L3`／官方資料表第 8 頁 |
| 官方方框原文 | 「學員證照通過、就業率高。」 |
| printed_official_checkbox_serial | `UNKNOWN`；不得把內部 index 144 或 doc_id 0131 當成印刷流水號 |
| 文類 | 以固定 cohort 為範圍的證照通過及訓後就業追蹤統計表，附逐筆來源索引、口徑、計算與限制 |

## 正式來源與精確定位

1. 官方《TTQS 查核佐證文件資料表－訓練機構版》PDF，第 8 頁。SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。目前 PR #92 分支中可讀來源位於 `docs/ttqs-quality-20261016/quality-review/0031_R06/inputs/official_source.pdf`；該檔 Git blob：`9c7621decdad585b743bf2b3d949ee5518b7bee0`。該頁參考佐證清單逐項列出「學員證照通過、就業率高。」；此文字本身不證明原始點協會已有任何學員通過證照或就業成果。
2. 現行 `03_157_CHECKBOX_BLUEPRINTS.md`：Git blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`，SHA-256 `ad03323d591cbea62814a8a59d233110587f2741bed8f944380b1faa2d04d216`。`I19-L3` 的 index 144 名稱為「考照/就業率：分母與可追溯數據」，要求具體來源定位、完整正文／示範、決策或結果及跨文件事實連結；除第三方原件索取型文件外，不得以空白欄位交差。
3. 遠端內部交付物 crosswalk `docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/official_129_to_142_crosswalk.csv`：Git blob `1ac4a8419088d947947031b758e29c35a3606514`。精確列為 `I19-E20,1,0,0131,學員證照通過與就業追蹤統計表`。這是內部 142 序列轉換表，不是官方印刷方框流水號。
4. Human Mission `01_HUMAN_MISSION_AND_ACCEPTANCE.md` blob `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`；Genre Writing Manual `02_GENRE_WRITING_MANUAL.md` blob `4ff863d9f534b6359fc1c7c1685bd8cce02da886`。均要求文類專屬、可操作正文、示範與真實證據清楚區分、不得捏造法人、第三方來源、簽章、核准或協會成果。

## 專屬施工邊界

- 本文件要讓小型訓練機構行政人員按同一 cohort 逐筆彙整：訓練完成、證照適用／報考／通過，以及固定追蹤期限內的就業狀態；每個統計數均能回到來源 ID、欄位定位、日期與驗證狀態。
- 證照「通過率」要明列分母口徑，至少區分已報考者通過比率與符合報考資格 cohort 的取得比率；不能把未報考、未符合資格或尚未查明者藏入或移出分母。
- 就業需明列 cohort 完訓人數、追蹤應答／未應答、就業／未就業／未知，分開呈現應答者比率與全體 cohort 的已確認數；不得把未回覆者直接算成就業或失業，也不得以訓練時間相近推論因果。
- 表單需支持小型協會逐筆追蹤、複核、補件、退回、HOLD、資料更正及安全保存；不得要求把身分證號、私人聯絡資料或未授權原件放進公開 GitHub。
- 本次未提供可公開使用的真實 cohort、考試機關證照清冊、雇主確認、學員授權或原始追蹤證據。因此所有演示數據只能標為 `SAMPLE/SYNTHETIC`；REAL 成效、原始點協會實際統計及正式接受均為 `UNKNOWN/NOT_GRANTED`。

## 鄰件排除與歷史候選

- `0130 / I19-E19 / index 143` 是訓後創業案例，不是證照或就業率；不得借用 0130 的 synthetic case 或其真實性判定。
- `0132 / I19-E21 / index 145` 是個人產品不良件數前後比較，不是本件指標。
- 遠端舊版封存資料中曾有 0131 DOCX，但它們位於歷史交接資料夾，未見本工作目錄下與 R01 來源鏈相符的現行候選。封存 DOCX 不自動承接本版來源、口徑或 QA。

## 下一階段交接

Writer 必須依同目錄 `UNIQUE_BLUEPRINT_0131_I19-E20_R01.md` 產生完整可操作的候選正文；原稿先落地並記錄 Worker 原始回覆、requested model、實際模型身分（無證據則 UNKNOWN）、CLI exit/session 與 SHA。Windows 原生建置再產生 DOCX。來源準備完成不等於正文、Word、視覺或語意驗收完成。
