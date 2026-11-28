# 0107｜I18-E15「高證照通過率之證明資料」來源包 R01

## 證據身分與對應

- 專案：TTQS_ONE；本件 DOCX ID：**0107**。
- 官方要求代碼：**I18-E15**；文件角色：`evidence_record`；官方證據表頁：第 7 頁。
- 157 項寫作藍圖的專案內部索引：**116**。這是專案內部索引，不能當成官方 PDF 印製流水號。
- GitHub PR #92 分支在來源讀取時的 HEAD：`5a1eeef474fb036607310013718bb24ab7f36b01`（候選 Draft）。
- 對應規格來源：`03_157_CHECKBOX_BLUEPRINTS.md` Git blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`，第 116 項為「高證照通過率證明：可追溯原始紀錄」。
- 官方映射：`quality-review/0036_R13/inputs/mapping/checkbox_mapping_compact.json` Git blob `ee3fc17e4e0e89a5b5d404c6f0ca7bd92a1a4f9b`；其 0107 條目映射 I18-E15、page 7 與此文件名稱。

## 官方原始來源（直接核對）

- PDF：`quality-review/0036_R13/inputs/official/TTQS_evidence_table_training_institution_source.pdf`
- Git blob：`9c7621decdad585b743bf2b3d949ee5518b7bee0`；PDF SHA-256：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；9 頁。
- 第 7 頁以 PDF 原頁抽取文字並將原頁渲染成 1191×1685 PNG 目視核對；渲染圖 SHA-256：`b4b229b154ae401cff6305f8dd413d967ac7a347165d112c355fa15689a358a1`。頁面圖隨本來源包保存於 `inputs/official/page7_render_0107_source.png`。
- 第 7 頁常見參考佐證資料的一般清單列「證照獲取率。」；其後明標「3分之常見參考佐證資料」的清單列「高證照通過率之證明資料。」。這些是參考佐證例示，不代表單一通過率自動保證分數、門檻或因果效果。
- 本來源包同時以官方映射核對 I18-E15 身分；不因 PDF 跨頁而把相鄰指標第 19 項或 I18-E09 競賽獲獎套入本件。

## 與鄰近文件的負向區分

- 0100／0101 = I18-E08：前後自我評量表及能力雷達分析；衡量能力變化，不能替代證照考試結果。
- 0102 = I18-E09：技能競賽獲獎的外部證據取得與查核；獎項不是證照通過率。
- 0107 = I18-E15：證照考試之考生、考試次數、通過結果、證照取得及來源可追溯的「證明紀錄」。正文須能在遮住標題後與問卷、雷達圖、競賽獲獎紀錄區別。
- 專案目前未提供原始點協會真實證照名冊、考試院／發證單位原始成績或證照原件。本件只准先做完整 SAMPLE/SYNTHETIC 示範與 REAL 原件替換流程；真實通過率及正式接受維持 `UNKNOWN`／`NOT_GRANTED`。

## 此來源包授權的下一階段

`READY_UNIQUE_BLUEPRINT`：依本來源與專案索引 116 建立文件專屬藍圖，再進入一個 OpenCode v2 CLI Writer 工作。Writer 只能提交完整正文文字，不可寫檔、呼叫工具、改 DOCX 或製造第三方證件；Word 由本機確定性工具產生，之後另做 exact-SHA 技術、視覺及獨立語意驗收。