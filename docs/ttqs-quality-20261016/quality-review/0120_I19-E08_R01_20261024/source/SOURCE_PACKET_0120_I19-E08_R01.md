# 0120 I19-E08 來源包 R01

## 1. 文件身分與來源狀態

- 專案：TTQS_ONE
- 唯一文件代號：0120
- 對應需求代號：I19-E08
- 需求名稱（依 R04 129→142 crosswalk）：訓練成果初步證據彙整與評量表
- 官方方框印刷流水號：UNKNOWN_NOT_ASSERTED。0120 是文件代號，I19-E08 是 crosswalk 需求代號；兩者都不是頁面上可見的方框流水號。
- 作品狀態：候選施工的來源包；尚非協會正式接受或實績。
- 本包未提供協會真實班級名冊、課程評量原件、問卷、學員反思、追蹤調查、證照原件、簽核或其他實績。凡完整數值案例一律另標 SAMPLE／SYNTHETIC。

## 2. 官方依據及可支持的結論

直接依據是勞動力發展署《TTQS 查核佐證文件資料表－訓練機構版》，本機 R04 官方來源檔案，SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`。PDF 共 9 頁；第 8 頁影像與文字已直接核對，頁腳印刷頁碼為 8。

官方第 8 頁的第 19 項說明：2 分常見參考佐證包括「相關證據顯示有初步訓練成果，且有部分佐證資料」；另列「學員滿意度、考試測驗或心得報告（學習技能面）」及「課後追蹤調查與分析結果、證照通過情形（學習技能面）」等參考資料。這些是舉例，不表示本協會已取得資料，也不授權本文件替任何單位評分。

本件應呈現可追溯的課程目標、學員學習評量、初步結果、原始佐證定位、資料缺口與下一步。滿意度只能作為學習經驗的輔助指標，不能單獨代替技能或學習成果；課後自陳不能冒充第三方驗證或因果證明。

## 3. 需求至文件的映射

- 來源 crosswalk：`TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv`，SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`。列 I19-E08 指向 doc_id 0120、單一交付件及標題「訓練成果初步證據彙整與評量表」。
- 舊 BLUEPRINT_SEED_142 列 0120 對應 I19-E08，但 genre、目的、欄位與驗收欄尚空。該列只供識別，不視為獨特 Blueprint；本工作包另提供 doc_id 專屬 Blueprint R01。
- 僅把第 19 項第 2 分參考資料中「初步訓練成果及部分佐證」作為本件範圍。不得將第 3、4 分市場／顧客價值成長內容誤當本件主體。

## 4. 與相鄰文件的分界

- 0119／I19-E07「目標市場及顧客價值部分提升證據分析表」分析市場或顧客價值變化；不可被本件的課程後測或滿意度取代。
- 0117／I19-E04 證照或測驗結果，以實際考試、證照與主辦者原件為準。本件只在同一課程、同一 cohort、同一資料來源能逐筆連結時引用。
- 0116／I19-E03 就業情形不等於學習成效，不得將就業或薪資值填入本件分數。
- 0121／I19-E09 為學員滿意度與學習評量報告；本件是初步成效佐證彙整與可操作的評量表，兩件須有不同用途。尚未證明相同 cohort 時不得跨件共用 case_id。

## 5. SYNTHETIC 示範情境（非協會事實）

- case_id：`SYN-0120-2026-A01`；課程示例：社區志工服務紀錄與溝通基礎；示例班期：2026-08-01；追蹤示例日期：2026-08-31。
- 8 位虛構代碼學員 SYN-L01 至 SYN-L08；全部數值均為合成資料。8 人皆符合示例完訓條件（出席至少 80% 且提交課程練習）。6 人有可配對的前後測，另 2 人各缺一側資料；不得刪除這 2 人或把 paired n=6 說成全班。
- 合成前測：[40, 50, 60, 55, 70, 45]，合計 320、n=6、平均 53.33。
- 合成後測：[60, 70, 70, 55, 80, 65]，合計 400、n=6、平均 66.67；六人配對平均差 13.33 分，5 人上升、1 人持平、0 人下降。通過門檻示例 70/100，前測 1/6、後測 3/6；它不是官方分數。
- 配對完整度 6/8=75%；兩人缺一側資料，占全班 2/8=25%。
- 滿意度七份有效回覆，分數 [5,4,4,5,3,4,5]，平均 30/7=4.29/5；回覆率 7/8=87.5%。此數值不替代後測技能資料。
- 30 日追蹤六份回覆，四人自陳已運用示例技巧、兩人尚未運用，另兩人未回覆；回覆率 6/8=75%，運用比例 4/6=66.7%（僅回覆者）或 4/8=50%（全班分母）。此為自陳示例，不是外部查證。

## 6. 真實資料替換原則

每個 SAMPLE 值均須在 replacement register 登記：欄位／表格位置、合成值、替換所需 REAL 原始來源、來源保管角色（未知時填 UNKNOWN）、授權狀態、覆核方式、替換狀態。未取得合法原件前不得把 SAMPLE 改標 REAL。不得杜撰學員姓名、授課者資格、簽名、機構核准、課程實施、雇主或第三方證明、證照結果及正式結論。

## 7. 引用檔案與版本

| 來源 | 本機路徑或版本 | SHA-256 / 定位 | 用途 |
|---|---|---|---|
| 官方佐證資料表 PDF | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\INPUTS\R04\06_OFFICIAL_SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf` | `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；PDF 第 8 頁／印刷頁 8 | 需求原文與參考證據 |
| 官方第 8 頁文字 | `source/official_requirement_page08.txt` | `c34ead45cad406150de5622e157f44727157776ce5c6abf5343c7db5dca42520` | 可搜尋來源摘錄 |
| 官方第 8 頁影像 | `source/official_requirement_page08.png` | `907176e44c4ccb42d86c84566baf9f1b3b6494e6c67d5a8e899decaebb065f9a` | 原頁視覺核對 |
| 129→142 crosswalk R01 | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\INPUTS\R04\04_EVIDENCE\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv` | `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679` | 需求代號到 doc_id 映射 |
| 142 BLUEPRINT_SEED | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BLUEPRINT_SEED_142.csv` | `280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0` | 舊種子列識別；本列內容欄仍空 |
| 人工作業 Mission 草案 | PR #92 HEAD `fd35ce9cc64877268b923b31aa85f2f03ee7fc7e`, `01_HUMAN_MISSION_AND_ACCEPTANCE.md` | blob `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` | SAMPLE/REAL、低維護、不得推定協會現況 |
| 文類寫作手冊草案 | 同 PR HEAD, `02_GENRE_WRITING_MANUAL.md` | blob `4ff863d9f534b6359fc1c7c1685bd8cce02da886` | 文字與文類品質約束 |
| 157 方框設計規格草案 | 同 PR HEAD, `03_157_CHECKBOX_BLUEPRINTS.md` | blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` | 方框與獨特 Blueprint 控制 |

*本來源包是候選製作資料，不是協會原始成效證據或正式 TTQS 評核決定。*

## 8. 本工作包檔案雜湊

- mapping_evidence_0120_R01.json: `9dbef661f3deeab2ff8fd1e0f0bfcd077a2315727495e4c90b7568d1c4ef8776`。
- UNIQUE_BLUEPRINT_0120_I19-E08_R01.md: `09a3aec874c14f97d5d6a1bed85d3cd75d617a9cf4bd33871973e5cb27c088ad`。
- SYNTHETIC_DATASET_0120_R01.csv: `ef04ed006079845be03ecbc51e5f2af72b34d565c69ee384cfda9677db2ab737`。
- SYNTHETIC_REPLACEMENT_REGISTER_0120_R01.csv: `97f19c56c51d835289bee94479cdad12165b0be388d203eafe082753dd5ff675`。