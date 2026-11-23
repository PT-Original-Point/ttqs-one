# Independent content review bundle — attempt 07

Binding: doc_id 0106; official requirement I18-E14; project crosswalk index 115 (not official checkbox serial); candidate DOCX SHA-256 `204bc47e1d7049b872c667a07b1f9fe7d9148bb867ca13b59c89ccaad36d515e`; extracted text snapshot SHA-256 `eed0cfe267d12c8d253f209f63294b5a7c3c7e2ab3c72c420dd73b997e452894`. The technical receipt binds this snapshot to the candidate bytes. Candidate remains not formally accepted.

Review the current complete content independently against the official requirement and unique Blueprint. Recompute material calculations; assess genre, practicality, form completeness, cross-document boundaries, authority and SAMPLE/REAL separation. Recheck attempt-06 findings F07R, F08R, F09, F13-F16; do not assume repairs succeeded. Use exact section/table locators and classify PASS/PARTIAL/FAIL/UNKNOWN. Visual receipt is provided only as another QA scope and does not imply that you performed visual review.

Return compact JSON only, under 1600 words: exact candidate SHA; overall verdict; check-level verdicts; any findings with minimal repair; scope and exclusions. No formal acceptance or REAL promotion.

## Current technical receipt
```json
{
  "doc_id": "0106",
  "requirement_id": "I18-E14",
  "project_157_index": 115,
  "candidate_state": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
  "candidate_sha256": "204bc47e1d7049b872c667a07b1f9fe7d9148bb867ca13b59c89ccaad36d515e",
  "candidate_bytes": 351339,
  "text_snapshot_sha256": "eed0cfe267d12c8d253f209f63294b5a7c3c7e2ab3c72c420dd73b997e452894",
  "text_snapshot_bytes": 47374,
  "paragraph_count": 139,
  "table_count": 25,
  "table_rows": 250,
  "embedded_images": 2,
  "media_details": [
    {
      "name": "word/media/rId31.png",
      "width": 1800,
      "height": 1000,
      "nonblank_colors": 1616
    },
    {
      "name": "word/media/rId47.png",
      "width": 2200,
      "height": 820,
      "nonblank_colors": 2852
    }
  ],
  "page_inches": [
    [
      11.69,
      8.27
    ]
  ],
  "normal_pt": 10.5,
  "body_min_pt": 10.5,
  "table_min_pt": 9.5,
  "t03_pair_rows_recomputed": 10,
  "figure1_data": {
    "前期支出": "100,000",
    "後期名目支出": "94,000",
    "後期標準化支出": "95,918.37",
    "直接訓練成本": "8,000",
    "估算淨財務效益": "-3,918.37"
  },
  "survey_recalculation": {
    "item_sums": [
      39,
      37,
      38,
      40,
      33,
      36
    ],
    "high_4_5_counts": [
      8,
      6,
      7,
      8,
      5,
      6
    ],
    "low_1_2_counts": [
      1,
      1,
      1,
      0,
      2,
      1
    ],
    "total": 223,
    "respondents": 10
  },
  "finance_recalculation": {
    "pre": 100000,
    "post_nominal": 94000,
    "price_index": 0.98,
    "direct_cost": 8000,
    "post_normalized": 95918.37,
    "gross": 4081.63,
    "net": -3918.37,
    "roi_percent": -48.98
  },
  "checks": {
    "zip_integrity": true,
    "two_embedded_images": true,
    "zip_media_count": true,
    "media_nonblank": true,
    "body_font_floor_10_5pt": true,
    "table_font_floor_9_5pt": true,
    "a4_landscape": true,
    "page_field_each_footer": true,
    "sample_header_each_section": true,
    "sample_banner_and_real_hold": true,
    "reader_body_has_no_builder_figure_specs": true,
    "t09_caption_and_mapping": true,
    "t13_caption": true,
    "cross_reference_points_to_both_sections": true,
    "noncash_values_unquantified": true,
    "break_even_value_explained": true,
    "q5_count_reconciled": true,
    "c1_specific_scale_anchors": true,
    "fact_key_view_unique": true,
    "traditional_chinese_heading": true,
    "no_internal_hash_or_control_leak": true,
    "t13_not_a_self_acceptance_receipt": true,
    "reader_facing_figure1_data_table": true,
    "survey_rows_and_sums": true,
    "core_finance_math": true,
    "t03_all_10_pairs_recomputed": true,
    "expected_table_inventory": true,
    "document_title_and_scope": true
  },
  "technical_verdict": "PASS",
  "failed_checks": [],
  "visual_QA": "PENDING_NATIVE_WORD_EXPORT_AND_PAGE_INSPECTION",
  "semantic_QA": "PENDING_FRESH_INDEPENDENT_REVIEW_ON_THIS_EXACT_SHA",
  "remote_readback": "PENDING"
}
```

## Visual receipt (scope reference only)
```json
{
  "doc_id": "0106",
  "requirement_id": "I18-E14",
  "project_157_index": 115,
  "candidate_state": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
  "candidate_sha256": "204bc47e1d7049b872c667a07b1f9fe7d9148bb867ca13b59c89ccaad36d515e",
  "pdf_sha256": "94b44ba1805612f1da7620d1b922db1b1d60471b71e9a26e0b9ff52e57aeb9ad",
  "page_count": 29,
  "renderer": "Microsoft Word 16.0 COM read-only export + Poppler 120 dpi raster",
  "visual_reviewer": "Codex visual QA in this task; independent from the DOCX builder",
  "scope": "All pages 1–29 were inspected in five contact sheets; selected pages 1, 10–13, 18, and 29 were also inspected at native 120 dpi. Checked table splitting/repeated headers, page fields, chart labels, content clipping, margins, sample/real labels and final pagination.",
  "findings_resolved": [
    "SAMPLE notice, calculation statement, survey instructions and attribution boundary no longer display raw/doubled Markdown dashes.",
    "T05 review header retained the shorter original label after an expanded label caused T07 header-only page; current DOCX is 29 pages and T07 header plus Q1–Q5 remain together on page 13.",
    "Removed the terminal horizontal rule that created an empty trailing page.",
    "T05 table continues with repeated header; no clipping observed."
  ],
  "remaining_visual_findings": [],
  "page_manifest_sha256": "6aba53b55c84c97c8bc20562dc4d2238fc29597de4199723b31acc7da4f124de",
  "visual_verdict": "PASS",
  "formal_acceptance": false
}
```


---

## Official requirement page 7

                   內涵說明（以下為        常見參考佐證資料
  項目     評核指標項目     例，但不以此為      （並註明資料來源及頁碼）
                       限）
                  的效果。           認為訓練有達成能力提升的效
                  4分 目標客戶及學員     果。
                  認為訓練有顯著具體     執行目標客戶及學員滿意度調查
                  績效。            及分析（系統及流程面）。
                                提出目標客戶及學員對訓練達能
                                 力提升之說明（學習技能面）。
                                學員培訓前後自我評量表及雷達
                                 分析圖呈現提升效果。
                                指導學員參加技能競賽獲獎。
                                感謝函。
                                證照獲取率。
                                其他：
                              3分之常見參考佐證資料：
                                問卷調查及課後行動計畫評估表
                                 等顯示目標客戶及學員認為訓練
                                 有績效改善的效果。
                                提出目標客戶及學員對訓練達組
                                 織績效改善之說明（財務面）。
                                高證照通過率之證明資料。
                                提高薪資紀錄。
                                社群網站知識討論區，人員使用
                                 網站頻率高。
                                其他：
                              4分之常見參考佐證資料：
                                問卷調查及課後行動計畫評估表
                                 等顯示目標客戶及學員認為訓練
                                 對組織績效的改善及提升均有顯
                                 著的效果。
                                提出目標客戶及學員對訓練達特
                                 殊績效之說明（社會面、其
                                 他）。
                                輔導考照 及學員回訓率持續提
                                 高。
                                會員人數逐年增加。
                                其他：





                  評分標準：       1 分之常見參考佐證資料：
        19.訓練系統的市1分 目標市場及顧客     目標市場及顧客價值均有提升，
                  價值均有提升，然而      然而未有具體紀錄及評量。
          場功能     未有具體紀錄及評      提出心得與知識分享執行成效
          ─目標市場   量。             （系統及流程面）。
          及顧客的價   2分 目標市場及顧客    口頭說明學員訓後就業狀況，但
          值創造     價值均有部分提升效      未有具體紀錄及評量。

                  果。            學員考照通過率有增加，但未有


                         7\n

---

## Official crosswalk row

doc_id,requirement_id,deliverable_title,project_157_index,project_157_indicator,official_source_page,official_pdf_sha256,scope_note,status
0106,I18-E14,提出目標客戶及學員對訓練達組織績效改善之說明_分析報告,115,I18-L3,7,805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709,財務面前後計算與限制；115 為專案序列索引不是 PDF 印刷 checkbox serial,DERIVED_SOURCE_MAPPING


---

## SOURCE_PACKET

# 0106 / I18-E14 / 157 項目 115 — SOURCE PACKET R01

**狀態：**候選施工來源包；不是協會實績、正式接受或評核結論。
**文件名稱：**《提出目標客戶及學員對訓練達組織績效改善之說明（財務面）分析報告》
**預定檔名：**`0106__提出目標客戶及學員對訓練達組織績效改善之說明_分析報告.docx

## 1. 唯一需求映射

| 欄位 | 對應 | 來源及限制 |
|---|---|---|
| 文件 ID | `0106` | 142 件文件序列；不是方框序號。 |
| 官方需求 ID | `I18-E14` | `official_129_to_142_crosswalk.csv` 第 94 行將此需求連到 0106。 |
| 文件標題 | 提出目標客戶及學員對訓練達組織績效改善之說明_分析報告 | `blueprint_seed_142.csv` 第 107 行。 |
| 157 項目索引 | `115` | `03_157_CHECKBOX_BLUEPRINTS.md` 的 I18-L3／官方資料表第 7 頁項目序列；這是本專案的項目索引，不宣稱是 PDF 印刷 checkbox serial。115 的獨特內容為組織績效財務效果、前後計算及限制。 |
| 官方來源 | 勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》頁 7 | PDF SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0`。 |
| 官方頁面要旨 | 3 分級的參考佐證涵蓋目標客戶及學員認為訓練帶來組織績效改善的財務面說明；本件聚焦可核算的財務效果與其證據限制。 | 只作精確定位及必要短語，不複製整頁受保護表格。官方完整用語以原始 PDF 為準。 |

## 2. 來源版本及逐項內容

本來源包依下列同一分支 HEAD `90d3ab2e69eae00817312aa101f800d4dd7ac0f1` 建立：

| 來源 | Git blob SHA-1 | 使用範圍 |
|---|---|---|
| `01_HUMAN_MISSION_AND_ACCEPTANCE.md` | `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e` | 小型協會情境、禁止推定現況、SAMPLE/SYNTHETIC 欄位、拒收條件。 |
| `03_157_CHECKBOX_BLUEPRINTS.md` | `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63` | 項目 115 的獨特目的及專屬文件要求。 |
| `official_129_to_142_crosswalk.csv` | `1ac4a8419088d947947031b758e29c35a3606514` | `I18-E14` → 0106。 |
| `blueprint_seed_142.csv` | `f20ac9ae37700eb03a93b8da4407e7bf4788b602` | 0106 專屬文件名稱及文件 ID。 |
| 官方 PDF | PDF SHA 上列；本機 Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0` | 9 頁官方來源；以第 7 頁為本需求主要定位。 |

### 2.1 需求界線

本件要能呈現「目標客戶及學員對訓練是否帶來組織績效改善」的財務面說明，並把可核對的前後財務數據、訓練成本、計算方式、受訪者意見、歸因限制與決策連在一起。只有滿意度高分，不能證明財務改善；只有支出下降，也不能證明由訓練造成。報告須分開列示觀察差異、受訪者認知、合理推論及尚待查證之因果關係。

### 2.2 相關但不同的需求

- 0105／I18-E13／157 項目 114：調查及課後行動計畫追蹤，是財務影響的可連結補充，不取代本件的財務前後核算。
- 0106／I18-E14／157 項目 115：本件只處理組織績效財務面及核算限制。
- 157 項目 120（I18-L4）：顯著組織績效問卷／行動方案量化與歸因，範圍較廣；不得把該需求內容直接搬到本件，也不得以本件代替項目 120。
- 0104 證照獲取率及 0103 第三方感謝函與本件不是同一證據。不得共用人數、案例 ID、分子分母或結論。

## 3. 真實資料現況及公開界線

截至本來源包建立時，沒有取得可公開且可追溯的原始點協會訓練成本、財務帳、採購明細、目標客戶調查、學員回覆、核定或第三方查證資料。上述真實資料狀態為 `UNKNOWN`，不得將缺件解讀成零、不得用推估代替真實紀錄、不得上傳受限制財務或個資。

因此文件須是完整的 `SAMPLE/SYNTHETIC` 示範稿，封面、頁眉或正文首段明確註明非協會實績、非真實客戶／學員／課程、非會計紀錄、未核定、不得作正式評核佐證。所有合成日期、金額、樣本、角色、意見及決策都要有事實鍵及替換來源。不得偽造第三方證明、實際客戶評語、協會核准、財務憑證或簽名。

## 4. 唯一示範案例約束

採用單一且與其他文件不共用受訪者的合成案例：小型非營利組織辦理「活動採購比價及核銷文件整理」訓練，觀察訓練前後各 6 個月共 10 組相同規格採購籃。案例 ID 固定為 `SYN-0106-FIN-01`；目標客戶代碼 `SYN-CUST-01`；學員代碼 `SYN-L01` 至 `SYN-L10`；不得使用真實姓名或指稱原始點協會實際辦理。

### 4.1 固定合成財務輸入

| 採購籃序號 | 訓練前金額（NT$） | 訓練後金額（NT$） |
|---:|---:|---:|
| 1 | 8,000 | 7,500 |
| 2 | 12,000 | 11,500 |
| 3 | 9,000 | 8,600 |
| 4 | 11,000 | 10,400 |
| 5 | 7,000 | 6,800 |
| 6 | 15,000 | 14,000 |
| 7 | 10,000 | 9,500 |
| 8 | 8,000 | 7,600 |
| 9 | 10,000 | 9,400 |
| 10 | 10,000 | 8,700 |
| **合計** | **100,000** | **94,000** |

同規格、同數量是示範假設，須標 `SAMPLE/SYNTHETIC`。訓練後價格指數 0.98（基期 1.00）亦是合成假設。按基期價格標準化：`94,000 ÷ 0.98 = 95,918.37`；估算毛額差異：`100,000 − 95,918.37 = 4,081.63`，占基期 `4.08%`。不得將名目差額 6,000 與標準化差額 4,081.63 混為同一結果。

### 4.2 固定合成訓練成本與結論

| 成本項 | 金額（NT$） |
|---|---:|
| 講師 | 4,500 |
| 教材 | 1,000 |
| 場地與交通 | 2,500 |
| **直接訓練成本** | **8,000** |

`估算淨財務效益 = 4,081.63 − 8,000 = −3,918.37`。`示範 ROI = (4,081.63 − 8,000) ÷ 8,000 × 100% = −48.98%`。本示範結論必須承認：標準化後的採購支出差異為正向，但扣除直接訓練成本後，觀察期內的示範淨額為負，未達損益平衡。不得選擇性刪除成本或將未實現時間價值算成現金節省。

### 4.3 固定合成問卷

學員邀請 12 人、有效回覆 10 人，回覆率 `10 ÷ 12 = 83.33%`。1–5 分量尺：1 完全不同意、2 不同意、3 普通、4 同意、5 非常同意；另設「不適用／未觀察」但不計入均值。合成 10 份回覆，以匿名代碼呈現：

| ID | Q1 財務流程改善 | Q2 能運用比價 | Q3 會算前後差異 | Q4 核銷文件完整 | Q5 價值高於成本 | Q6 願意持續使用 |
|---|---:|---:|---:|---:|---:|---:|
| SYN-L01 | 5 | 5 | 4 | 4 | 4 | 4 |
| SYN-L02 | 4 | 4 | 4 | 5 | 3 | 4 |
| SYN-L03 | 4 | 3 | 4 | 4 | 4 | 3 |
| SYN-L04 | 4 | 4 | 5 | 4 | 3 | 4 |
| SYN-L05 | 3 | 3 | 3 | 4 | 3 | 2 |
| SYN-L06 | 5 | 5 | 5 | 5 | 4 | 5 |
| SYN-L07 | 4 | 4 | 4 | 4 | 4 | 4 |
| SYN-L08 | 4 | 4 | 3 | 3 | 2 | 3 |
| SYN-L09 | 4 | 2 | 4 | 4 | 4 | 4 |
| SYN-L10 | 2 | 3 | 2 | 3 | 2 | 3 |
| **合計／10 人均值** | **39／3.9** | **37／3.7** | **38／3.8** | **40／4.0** | **33／3.3** | **36／3.6** |

Q1 為 4–5 分 8/10；Q4 為 4–5 分 8/10；Q5 為 4–5 分 5/10。表內只示範學員自述，不證明組織財務改善。合成目標客戶回覆僅 1 人 `SYN-CUST-01`、Q1 4/5；只能作單一個案觀點，不可推論所有客戶。

## 5. 必須保留的限制

比較範圍須交代匹配規則、6 個月窗口、10 組資料及價格指數來源在真實轉換時所需的憑證。合成個案不得自稱採用經審計或已核實之價格指數。列出通膨、供應商更換、規格／數量、採購季節、議價權、物價、採購人員經驗、預算限制及其他制度改變等混淆因素。樣本小、非隨機且無對照，不能認定訓練造成差異；回覆意見與財務結果不得互相證明。

## 6. 正式替換最低來源

欲由 SAMPLE 升為 REAL，至少須由授權角色核對：課程計畫／出席／完成名冊；訓練直接成本原始憑證；訓練前後可比較的採購或會計明細及數量／規格；市場價格或物價調整依據；客戶及學員問卷原始資料與同意／個資處理依據；資料期間與 cutoff 核准；雙人獨立重算；對混淆因素的說明；權責核定。每份資料保持原正式保管處，公開儲存庫僅留去識別、獲授權、可公開的摘要及替換狀態。

缺一或對帳差額不為零時，維持 `REAL=UNKNOWN/HOLD`，凍結受影響財務結論，不阻擋其他不相依文件。


---

## UNIQUE_BLUEPRINT

# UNIQUE BLUEPRINT — DOCX 0106 / I18-E14 / 157 項目 115

**狀態：**候選寫作藍圖；不等於正式接受。
**最終成品類型：**可操作的財務成果分析報告，不是政策手冊、空白表單集、滿意度問卷報告或會計憑證。
**唯一案例：**`SYN-0106-FIN-01`（合成採購流程訓練案例）。

## A. 唯一身份、需求和來源

| Blueprint 欄位 | 規格 |
|---|---|
| doc_id | 0106 |
| requirement_id | I18-E14 |
| 142 序列名稱 | 提出目標客戶及學員對訓練達組織績效改善之說明_分析報告 |
| 157 專案項目索引 | 115，位於 03 文件 I18-L3／官方 PDF 第 7 頁的項目序列；不是 PDF 印刷 checkbox serial。 |
| 官方佐證目的 | 財務面呈現訓練與組織績效改善間可查核的前後說明，並將目標客戶／學員觀點、數字來源和限制說清楚。 |
| 官方來源 | `TTQS_evidence_table_training_institution_source.pdf` 第 7 頁；PDF SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；本機 Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0`。 |
| 142 對照來源 | `official_129_to_142_crosswalk.csv`，Git blob `1ac4a8419088d947947031b758e29c35a3606514`；I18-E14 → 0106。 |
| 標題來源 | `blueprint_seed_142.csv`，Git blob `f20ac9ae37700eb03a93b8da4407e7bf4788b602`。 |
| 157 藍圖來源 | `03_157_CHECKBOX_BLUEPRINTS.md`，Git blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`；索引 115 為組織績效財務效果之前後計算與限制。 |
| 編輯原則 | 依 `01_HUMAN_MISSION_AND_ACCEPTANCE.md` blob `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`：小型協會適切性、SAMPLE/REAL 區隔、完整正文、事實鍵清冊、禁止假核准／財務或第三方原件。 |

## B. 讀者、用途和判讀

主要讀者為訓練行政承辦、財務資料提供角色、品質覆核者及評核委員。讀者應可從報告直接查出：比較對象與期間、訓練成本、財務前後數據、標準化處理、算式、受訪者意見、限制、結論及要補的真實來源。管理者需能依本件判斷「現有證據只能支持到哪一層」；不得將問卷高分等同財務效益，也不得將同期支出下降寫成訓練的因果成效。

## C. 文件必須有的專屬正文

1. 首頁醒目標示「完整 SAMPLE/SYNTHETIC 示範；不是原始點協會實績、財務帳、核定或評核證據」。30 秒導讀說明財務成果報告用途及主要限制。
2. 官方要求定位及本件範圍：I18-E14、項目 115、官方 PDF 第 7 頁；說明財務面，不取代 0105 調查與課後行動追蹤。
3. 案例範圍與方法：合成訓練活動、參與者、目標客戶代碼、期間、匹配採購籃、觀察單位、納入／排除規則、數據品質及價格指數假設。
4. 完整財務前後資料表：逐筆列出 10 組同規格採購籃，訓練前後原始金額、差額、來源欄、證據狀態。
5. 完整成本表及公式；把直接現金成本與不計入的志工／時間機會成本分開。不得將「估算時間價值」列為已節省現金。
6. 逐步核算：名目差額、價格調整、標準化差額、差異率、淨效益、ROI、損益平衡差距及敏感度區間；數字需全部重算一致。
7. 完整問卷工具及已填合成結果：10 名合成學員的 6 個 1–5 分題、有效數、回覆率、題項均值、4–5 分人數比例、缺答處理；另列單一合成客戶觀點並限制推論。
8. 財務結果與感知結果分開分析；畫出可讀的邏輯鏈（訓練投入 → 學習 → 實際採購行為 → 文件／成本產出 → 組織財務結果），標出每段證據及未知。
9. 混淆因素、資料弱點及歸因邊界：至少涵蓋市場價格、供應商、規格／數量、季節、議價、預算、制度、人員更動、樣本與自陳偏差；不用因果詞。
10. 結論與管理行動：誠實說明合成例的毛差異正向、扣除直接訓練成本後淨值負、觀察期未損益兩平；提出不預設已核准的後續檢查、責任角色（SAMPLE）、期限及觸發條件。
11. 可直接使用的空白正式替換表、資料來源清單、雙人重算紀錄、異常與暫緩條件、核定前檢查表；同時保留完整填妥的 SAMPLE 範例。
12. 事實鍵索引與 REAL 替換清冊：每一金額、日期、角色、樣本、回覆、價格指數、判斷均有 fact_id、case_id、doc_id、正文位置、假設理由、真實替換來源、負責角色 UNKNOWN 與狀態。

## D. 固定案例輸入與驗收算式

Writer 必須原樣使用 SOURCE_PACKET 的單一案例資料，不可自行更動數字。10 組金額合計：訓練前 NT$100,000、訓練後 NT$94,000、名目差額 NT$6,000。後期市場價格指數 0.98；標準化後支出 `94,000/0.98=95,918.37`；標準化毛差額 NT$4,081.63；相對基期差異 4.08163%。直接訓練成本 NT$8,000；淨效益 -NT$3,918.37；示範 ROI -48.9796%。敏感度價格指數 0.96–1.00 時，標準化毛差額約 NT$2,083.33–6,000，扣直接成本後淨值約 -NT$5,916.67 至 -NT$2,000。不得宣稱真實現金節省或實際因果效果。

問卷固定 12 人邀請、10 份有效，回覆率 83.33%。Q1/Q4 各 8/10 評 4–5；Q5 5/10；題均值依 SOURCE_PACKET 的合成明細重算。客戶觀點 n=1，只作單一個案敘述。所有資料維持 SYNTHETIC。

## E. 必備表格／圖示

| 編號 | 名稱與最低欄位 |
|---|---|
| T01 | 來源與需求對照：doc_id、requirement_id、157 索引、官方頁次、用途、限制。 |
| T02 | 案例及配對範圍：期間、10 個採購籃、匹配規則、排除規則、資料狀態。 |
| T03 | 10 組財務原始示範列：序號、前期、後期、名目差、價格指數、標準化值、fact_id。 |
| T04 | 訓練成本明細：項目、金額、現金／非現金、假設、來源鍵。 |
| T05 | 計算對帳表：公式、代入值、結果、四捨五入、覆核。 |
| T06 | 敏感度與損益平衡：價格指數、毛差異、淨值、ROI、是否損平。 |
| T07 | 完整學員問卷：題幹、量尺、選項、適用性、填寫方式、保密告知。 |
| T08 | 10 份合成問卷逐列摘要及題項彙總；另列客戶 n=1。 |
| T09 | 訓練至財務結果邏輯鏈與每段證據／缺口。 |
| T10 | 混淆因素及敏感性處理：可能影響、目前證據、替代解釋、處理／限制。 |
| T11 | 樣本改善行動表：問題、下一步、責任角色、期限、完成證據、暫緩條件。 |
| T12 | REAL 替換清冊：fact_id、位置、SYN 值、正式來源、授權／保管位置、覆核角色、目前 UNKNOWN/HOLD。 |
| T13 | 交付前判定：資料完整、對帳零差、雙人重算、個資、因果語言、授權與發布。 |

必備圖：前後費用及成本拆解比較圖；訓練邏輯鏈／證據強度圖。每張圖標註單位、期間、n、合成狀態；不能以圖表隱藏負淨效益。

## F. 跨文件連結與錯件排除

- 0105／I18-E13 的課後問卷與行動追蹤可作為方法旁證，但其資料、數值、case_id、對象不得被搬作 0106 財務證據。
- 0104 是證照獲取率；不得用合格／報考／取得證照人數替代財務前後比較。
- 157 項目 120 涉及更廣的顯著組織績效量化與歸因；本件不宣稱滿足該項。
- 文件在遮住標題、封面、頁眉及通用前言後，讀者仍應辨識它是「訓練之組織財務效果分析」，不是滿意度調查、活動核銷單、財務報表或成果宣傳稿。

## G. 拒收、暫緩及修復條件

**FAIL／需返工：**未保留負淨值；算式或任何合計不一致；問卷數與回覆率矛盾；改寫固定輸入；無期間、單位、配對範圍；將自陳意見當財務證據；用因果字眼；把合成資料寫成協會、客戶或財務真實紀錄；與 0105 共用案例／個資；只給空白表；無法遮標題辨識用途。

**HOLD／REAL 不可升格：**沒有獲授權帳務／採購明細、成本憑證、價格基準、有效樣本、客戶／學員原始回覆、資料期間核定或第二人重算。HOLD 只凍結真實財務結論，不阻擋其他文件。

**PASS 範圍只能逐項標示：**來源映射、正文完整、技術／數學、SAMPLE/REAL、Word 視覺、獨立語意、遠端讀回；任何未查項目為 UNKNOWN，不可用整體 PASS 遮蔽。

## H. Writer 輸出要求

依 `SOURCE_PACKET_0106_I18-E14_R01.md` 產出完整繁體中文報告正文，必須把 T01–T13、完整已填 SYN 問卷、10 組財務資料、全部計算、負向淨結果、管理解讀、空白正式替換表及退件條件逐項落入正文。不得輸出摘要、提綱、製作計畫、技術規格或 Markdown 代替實質報告。輸出純 Markdown 原稿作為後續 Windows DOCX builder 的輸入，不得寫入／改動檔案、呼叫工具、宣稱真實成效、聲稱正式核准或替協會做決策。遇到來源未提供之真實事實，明示 `UNKNOWN/HOLD`。


---

## Attempt-06 independent review response

{
  "binding": {
    "doc_id": "0106",
    "requirement_id": "I18-E14",
    "project_157_index": 115,
    "candidate_sha256": "a061814fe7f1708cb0aff02a9bd9ba6f72e599e1e1bc359d35938250b5306e8c",
    "text_snapshot_sha256": "c23e40cfe810b0fa45524e1bc2d1cc3b36bc08a4925121c2df360a5df83ec333",
    "candidate_state": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
    "hashes_recomputed_by_reviewer": false,
    "basis": "supplied text snapshot bound by the supplied technical receipt"
  },
  "overall_verdict": "PASS_TEXT_SEMANTIC_ONLY",
  "verdict_note": "No blocking content, arithmetic, SAMPLE/REAL, genre or authority defect found in the snapshot. F07 is substantially repaired; F08 and F09 are resolved. Residual items are LOW/INFO wording only. This is not formal acceptance, not CURRENT promotion, not REAL upgrade, and not visual/remote verification.",
  "checks": [
    {
      "id": "C1_requirement_mapping_identity",
      "verdict": "PASS",
      "locator": "T01 §1; cover; §13.1",
      "note": "0106 / I18-E14 / index 115 / official p.7 all stated; T01 explicitly denies being the printed 核取欄序號; seed title preserved verbatim in T01 while cover adds （財務面）."
    },
    {
      "id": "C2_genre_distinctiveness",
      "verdict": "PASS_TEXT",
      "locator": "§3–§6, §8–§9, §13.1",
      "note": "Blind-read core is 10 paired baskets, index 0.98, cost table, negative net, break-even, sensitivity band — recognisably a training→organisational-finance analysis, not a survey report, voucher, financial statement or publicity piece. Actual blind test remains unexecuted (document itself marks it UNKNOWN)."
    },
    {
      "id": "C3_blueprint_coverage_T01_T13",
      "verdict": "PASS",
      "locator": "T01 §1; T02 §2; T03 §3; T04 §4; T05 §5; T06 §6; T07 §7.1; T08 §7.2; T09 §8; T10 §9; T11 §10; T12 §12; T13 §11.5",
      "note": "All 13 tables present with the Blueprint-minimum fields; both required figures carry unit/period/n/SYN labels; T04 separates cash vs non-cash."
    },
    {
      "id": "C4_survey_instrument",
      "verdict": "PASS",
      "locator": "§7.1 T07; §7.2 T08",
      "note": "6 learner items + 1 client item, 1–5 anchors spelled out, 不適用 excluded from means, missing-answer <8 → UNKNOWN/HOLD rule, 12 invited / 10 valid / 83.33%, low scorers L05/L08/L10 retained, C1 n=1 explicitly non-inferential."
    },
    {
      "id": "C5_calc_trail_sensitivity_conclusion_actions",
      "verdict": "PASS",
      "locator": "T05 16 rows; T06 6 rows; §10.1; T11 8 rows; §11.4; §13.2",
      "note": "Every formula substituted; negative net retained in all four conclusions; sensitivity band all-negative; actions carry SAMPLE role/date/evidence/HOLD trigger."
    },
    {
      "id": "C6_math_and_cross_table_consistency",
      "verdict": "PASS",
      "locator": "T03, T05, T06, T08, §4",
      "note": "Independently recomputed; see recomputation block. Only the declared ≤0.05 column rounding and one 7-dp theoretical-threshold display remain."
    },
    {
      "id": "C7_cross_document_separation",
      "verdict": "PASS_DECLARED_BODY_SCREEN_UNKNOWN",
      "locator": "§0 item 4; §1.2; §13.1",
      "note": "0105 / 0104 / 0103 / item 120 separations stated; unique case_id SYN-0106-FIN-01; no shared respondents, IDs or numerators declared. Actual peer-body duplication screening is UNKNOWN — peer bodies were not supplied."
    },
    {
      "id": "C8_sample_real_boundary",
      "verdict": "PASS",
      "locator": "cover banner; header; footer; §11.4; §12; §13.3",
      "note": "SAMPLE/SYNTHETIC + REAL=UNKNOWN/HOLD repeated; roles SYN-ROLE-xx; §11.3 forbids 代簽; 決策狀態 不升格; no fabricated letter, certificate, quote, approval or signature; causal verbs confined to confounder alternatives and the banned-wording list."
    },
    {
      "id": "C9_human_facing_boundary",
      "verdict": "PASS_WITH_LOW_RESIDUAL",
      "locator": "§11.5 preamble; §11.5 分項判定原則; §13.4",
      "note": "exact SHA / GitHub ref / raw DOCX bytes / Blueprint strings are gone from reader-facing rows; rows 1, 13, 14 and §13.4 are now plain language. Residual jargon only in the two §11.5 scope sentences."
    },
    {
      "id": "C10_small_nonprofit_usability",
      "verdict": "PASS_WITH_LOW_RESIDUAL",
      "locator": "§0 30-second guide + 使用說明; §11.1; §11.4; §13.2",
      "note": "Reader path, four-step workflow and HOLD triggers are usable; one wrong chapter referent in §0 item 2."
    },
    {
      "id": "C11_prior_F07_F09",
      "verdict": "F07 RESOLVED_WITH_RESIDUAL; F08 RESOLVED; F09 RESOLVED",
      "locator": "§11.5 rows 1/13/14; §13.4; §0 item 2; T05 row 14; T06 last row",
      "note": "See findings."
    },
    {
      "id": "C12_visual_layout",
      "verdict": "UNKNOWN",
      "locator": "n/a",
      "note": "Not in this scope; no page, figure, footer-field or font rendering was inspected. The technical receipt's shadow-QA claims were not independently verified."
    },
    {
      "id": "C13_remote_readback",
      "verdict": "UNKNOWN",
      "note": "No remote bytes fetched."
    },
    {
      "id": "C14_formal_acceptance_real_promotion",
      "verdict": "NOT_GRANTED",
      "note": "Reviewer has no acceptance authority; candidate remains CANDIDATE_NOT_FORMALLY_ACCEPTED, REAL=UNKNOWN/HOLD."
    }
  ],
  "findings": [
    {
      "id": "F07R",
      "severity": "LOW",
      "status": "RESIDUAL_OF_RESOLVED_F07",
      "locators": [
        "§11.5 preamble: 「不等於獨立審查、全頁視覺、標題盲測、遠端位元組讀回或 REAL 核准已完成」",
        "§11.5 分項判定原則: 「來源映射、內容完整、技術／數學、SAMPLE／REAL、頁面視覺、獨立語意及遠端讀回必須分開判定」"
      ],
      "evidence": "The former MEDIUM defect is largely repaired: 「逐項對照唯一 Blueprint」, 「exact SHA」, 「指定 GitHub ref」, 「raw DOCX bytes」 and 「Word 視覺、獨立語意、遠端讀回」 no longer appear in the rows previously cited, and §13.4 now uses plain 「來源映射、正文、技術／數學及 SAMPLE/REAL 界線」. The Blueprint §G scope labels themselves mandate naming each gate separately, so only the residual technical phrasing 「遠端位元組讀回」/「遠端讀回」 is exposed to an administrator.",
      "repair": "Optionally soften the two residual phrases to 「發布檔案取回一致性查核」 and keep the four-scope separation; no content or number change. Non-blocking."
    },
    {
      "id": "F08R",
      "severity": "LOW",
      "status": "RESOLVED_WITH_NEW_LOCATOR_SLIP",
      "locators": [
        "§0 使用說明 item 2: 「重算結果須依本章四捨五入政策一致才算技術通過（列示差額 ≤ NT$0.05 依第 3 章政策）」"
      ],
      "evidence": "The substantive tolerance contradiction is fixed: ≤NT$0.05 is now stated and matches §3, §11.4 and §13.2. The sentence still says 「本章」 while the rounding policy lives in §3, so the two halves of one sentence point to different chapters.",
      "repair": "Change 「依本章四捨五入政策」 to 「依第 3 章四捨五入政策」."
    },
    {
      "id": "F09",
      "severity": "INFO",
      "status": "RESOLVED",
      "locators": [
        "T05 row 14: 「1.0217391（七位小數；代入回算差額約 NT$0.003）」",
        "T06 last row: 「1.0217391 … | 92,000.00 | 8,000.00 | 0.00 | 0.00%」"
      ],
      "evidence": "Exact ratio is 94,000 ÷ 92,000 = 1.0217391304. Substituting the printed 7-dp value gives 94,000 ÷ 1.0217391 = 92,000.0027, i.e. Δ ≈ 0.0027 (rounded to the stated ~0.003) — inside the document's own ≤0.05 policy, and 92,000.00 / 8,000.00 / 0.00 all reproduce at 2 dp. The prior 0.08 discrepancy is gone.",
      "repair": "None required."
    },
    {
      "id": "F13",
      "severity": "INFO",
      "status": "PERSISTS_FROM_F11",
      "locators": [
        "T05 覆核 column rows 1–9 「待雙人重算」; rows 10–16 advisory text"
      ],
      "evidence": "Column mixes status and instruction. All substantive cells are filled, so anti-placeholder rule 7 is not breached; 「待雙人重算」 is an honest UNKNOWN and is consistent with §11.3 remaining blank.",
      "repair": "Optional tidy-up only; no content change needed."
    },
    {
      "id": "F14",
      "severity": "INFO",
      "status": "PERSISTS_FROM_F12",
      "locators": [
        "cover: 「…之說明（財務面）分析報告」 vs T01 seed title 「…之說明_分析報告」"
      ],
      "evidence": "Exact seed title is preserved verbatim in T01, so identity stays traceable.",
      "repair": "None."
    },
    {
      "id": "F15",
      "severity": "INFO",
      "locators": [
        "T11 row 8 期限欄: 「依替代進度」"
      ],
      "evidence": "Seven actions carry synthetic dates; row 8 carries no date. It is an honest SAMPLE statement and the completion evidence column still holds a verifiable condition (T12 全列狀態非 UNKNOWN/HOLD).",
      "repair": "Optional: state 「依第 11 章替換完成日（SAMPLE）」."
    },
    {
      "id": "F16",
      "severity": "INFO_TECHNICAL_NOT_SEMANTIC",
      "locators": [
        "[FOOTER 0] 原始點協會 TTQS ONE｜候選稿，未正式接受｜第 1 頁"
      ],
      "evidence": "Text extraction shows a literal 「第 1 頁」, identical to the prior candidate. The supplied technical receipt asserts page_field_each_footer=true, but a text snapshot cannot distinguish a live PAGE field from a static string.",
      "repair": "Verify in the native page gate; this review does not confirm pagination on pages 2+."
    }
  ],
  "recomputation": {
    "t03_rows": "All 10 rows reproduce to 2 dp (7,653.06/346.94; 11,734.69/265.31; 8,775.51/224.49; 10,612.24/387.76; 6,938.78/61.22; 14,285.71/714.29; 9,693.88/306.12; 7,755.10/244.90; 9,591.84/408.16; 8,877.55/1,122.45). Column sums 100,000 / 94,000 / 6,000; rounded standardized sum 95,918.36 and rounded-difference sum 4,081.64, i.e. the documented Δ0.01 versus direct totals 95,918.37 / 4,081.63.",
    "core": "94,000 ÷ 0.98 = 95,918.3673 → 95,918.37; gross 4,081.63; rate 4.08163% → 4.08%; net −3,918.37; ROI −48.9796% → −48.98%; gross return 51.02%; nominal net −2,000; break-even gross 8,000; gap 3,918.37; cost cap 4,081.63; break-even index 94,000 ÷ 92,000 = 1.02173913; monthly 680.27; 8,000 ÷ 680.27 = 11.76 (~11.8).",
    "t06": "0.96 → 97,916.67 / 2,083.33 / −5,916.67 / −73.96%; 0.97 → 96,907.22 / 3,092.78 / −4,907.22 / −61.34%; 0.98 → 95,918.37 / 4,081.63 / −3,918.37 / −48.98%; 0.99 → 94,949.49 / 5,050.51 / −2,949.49 / −36.87%; 1.00 → 94,000.00 / 6,000.00 / −2,000.00 / −25.00%; critical row as in F09. All negative; none break-even.",
    "cost": "4,500 + 1,000 + 2,500 = 8,000; non-cash rows unquantified and excluded from the ROI denominator, consistent with §4 and §12.",
    "survey": "Item sums 39/37/38/40/33/36 = 223; means 3.9/3.7/3.8/4.0/3.3/3.6; personal totals 26/24/22/24/18/29/24/19/22/15 = 223; 4–5 counts 8/6/7/8/5/6; 1–2 counts 1/1/1/0/2/1; Q5 split 4–5:5, 3分:3 (L02/L04/L05), 2分:2 (L08/L10); response rate 10/12 = 83.33%.",
    "fixed_input_fidelity": "10 basket amounts, index 0.98, cost split 4,500/1,000/2,500, 12-invited/10-valid, and all 60 item scores match SOURCE_PACKET §4.1–4.3 exactly; no fixed input was rewritten.",
    "agreement_with_technical_receipt": "Recomputed survey and finance figures independently match the receipt's survey_recalculation / finance_recalculation / t03_pair_rows_recomputed fields."
  },
  "authorized_blank_areas": "§11.1 replacement form, §11.2 source list and §11.3 double-recompute record are explicitly labelled REAL replacement/blank forms with filled SAMPLE companions, so they are not anti-placeholder rule 7 violations.",
  "review_scope": {
    "kind": "text-only independent semantic/content review on the two stated hashes",
    "read": [
      "supplied current candidate text snapshot",
      "technical receipt",
      "official page-7 extraction",
      "crosswalk row",
      "SOURCE_PACKET 0106 R01",
      "UNIQUE_BLUEPRINT 0106",
      "attempt-05 findings"
    ],
    "performed": [
      "arithmetic recomputation",
      "fixed-input fidelity check",
      "SAMPLE/REAL language and authority scan",
      "causal-wording scan",
      "locator/cross-reference check",
      "resolution test of F07–F09",
      "new-defect probe"
    ],
    "not_performed": [
      "no file edits",
      "no DOCX/ZIP opening",
      "no SHA recomputation",
      "no rendering, page, figure or footer-field inspection",
      "no font measurement",
      "no peer-body duplication run",
      "no remote fetch",
      "no second-model consultation"
    ]
  },
  "explicit_exclusions": [
    "Visual/layout, figure legibility, header/footer page-field behaviour, pagination, per-run font floors and DOCX internals are OUT of scope; the supplied visual/technical receipt is a different QA scope and is not endorsed here.",
    "Remote raw-byte readback is not verified.",
    "Second-person independent recompute and signed reconciliation are not established.",
    "Actual cross-document body-duplication outcome against 0105 / 0104 / 0103 / item 120 is UNKNOWN.",
    "Officially corrected page-7 wording is corroborated only by the bundle extraction, not by the PDF file.",
    "No REAL source exists or was authorised; nothing here asserts association facts, third-party evidence, approval or signature.",
    "No formal acceptance, no CURRENT promotion, no REAL=APPROVED, no evaluator-facing certification is granted or implied."
  ]
}


---

## Exact text snapshot of current candidate

提出目標客戶及學員對訓練達組織績效改善之說明（財務面）分析報告
文件 ID： 0106　官方需求 ID： I18-E14　157 項目索引： 115 案例 ID： SYN-0106-FIN-01　稿件版本： R01（SAMPLE）
本稿產出日期： 2026-10-22（日期本身亦為示範排程用合成日期，fact_id: F0106-DATE-99）
重要聲明｜SAMPLE 示範稿
本文件為完整 SAMPLE／SYNTHETIC 示範稿。
非真實機構紀錄： 本文件不是原始點協會或任何真實訓練機構的實績、財務帳、會計紀錄或採購明細。
非真實訪談： 本文件不是任何真實客戶或學員的意見、問卷或感謝。
非正式核定或佐證： 本文件不是協會核定文件、第三方查證結果、審計報告或 TTQS 評核佐證；目前未核定、未覆核，不得作正式評核佐證或對外宣稱為實際成效。
合成資料範圍： 案例中的日期、人物、角色、金額、樣本、問答回覆、價格指數、判斷與決策均為虛構合成，只用來示範文件結構與核算方法。
REAL 狀態： UNKNOWN/HOLD（詳見第 11 章與第 12 章）。
結果完整性： 本報告保留負向淨效益結果；不得選擇性刪除成本、以問卷高分替代財務證據，或使用因果用語描述訓練效果。
0. 三十秒導讀（給承辦、覆核者與評核委員）

讀者最想知道的問題 | 本報告的答案 | 位置
這份文件在證明什麼？ | 訓練前後「可核算的組織財務面差異」及其證據限制；不是滿意度調查，也不是會計憑證。 | 第 1、2 章
用什麼案例？ | 單一合成案例 SYN-0106-FIN-01：小型非營利單位「活動採購比價及核銷文件整理」訓練，前後各 6 個月、10 組同規格採購籃。 | 第 3 章
數字怎麼來的？ | 固定合成輸入（前 100,000／後 94,000／指數 0.98／成本 8,000），逐步算式全部可重算。 | 第 4–6 章
結果是正是負？ | 毛差異為正（+NT$4,081.63，+4.08%）；扣除直接訓練成本後淨效益為負（-NT$3,918.37），示範 ROI -48.98%，觀察期內未達損益平衡。 | 第 6 章
問卷能證明財務改善嗎？ | 不能。問卷僅為學員自陳感知（10 份有效，回覆率 83.33%）；客戶觀點僅 n=1，不得推論全體。 | 第 7 章
能說是訓練造成的嗎？ | 不能。樣本小、非隨機、無對照，且有至少 10 類混淆因素未排除；本報告一律使用非因果措辭。 | 第 9 章
缺什麼才能升 REAL？ | 授權帳務／採購明細、成本憑證、價格基準、原始問卷與同意依據、期間核定、雙人獨立重算、混淆因素說明、權責核定；缺一即維持 REAL=UNKNOWN/HOLD。 | 第 11–12 章

使用說明（可操作性）： 1. 評核讀者可只讀第 0 章、第 6 章、第 7 章、第 9 章、第 10 章，即可判斷「現有證據支持到哪一層」。 2. 財務覆核者可依第 5 章 T05 對帳表逐格重算；所有公式均已代入數值，重算結果須依第 3 章四捨五入政策判定才算技術通過（列示差額 ≤ NT$0.05 依第 3 章政策）。 3. 承辦者若要轉為真實版本，只能使用第 11 章的空白正式替換表與第 12 章的 REAL 替換清冊，逐欄填入獲授權來源；不得直接改寫本示範數字。 4. 本件不取代 0105（I18-E13，調查及課後行動追蹤），不取代 157 項目 120（I18-L4，顯著組織績效量化與歸因），與 0104（證照獲取率）、0103（第三方感謝函）不得共用任何人數、案例 ID、分子分母或結論。
1. 官方要求定位與本件範圍（T01）
T01 來源與需求對照表

欄位 | 正式對應 | 文件用途與限制
文件 ID | 0106 | 142 件文件中的文件編號；與官方資料表印製的核取欄序號不同。
官方需求 ID | I18-E14 | 對應本文件的 TTQS 財務面佐證用途。
157 項目索引 | 115 | 本專案項目序列，不是 PDF 上印製的核取欄序號；範圍是組織績效財務效果、前後計算及限制。
文件標題 | 提出目標客戶及學員對訓練達組織績效改善之說明_分析報告 | 以財務面前後比較及證據限制呈現本項用途。
官方來源 | 勞動力發展署《TTQS 查核佐證文件資料表—訓練機構版》第 7 頁 | 用於定位官方佐證目的；完整用語以官方原件為準。
唯一文件範圍 | 目標客戶及學員對訓練與組織績效財務面差異的說明 | 不取代課後行動追蹤、證照獲取率、第三方感謝函或較廣泛組織績效量化與歸因。
示例及真實狀態 | 全文數字、角色、日期及回覆均為 SAMPLE／SYNTHETIC | 不是協會實績、財務帳或正式核准；REAL=UNKNOWN/HOLD。

下列對照說明本報告的官方佐證用途與適用範圍；後續章節提供可重算的示範案例、結果判讀及實務查核步驟。
1.1 本件要做什麼
以可核對的財務前後數據呈現「目標客戶及學員所認知的訓練後組織績效改善」在財務面的說明，並把下列各項串在一起：前後財務數據、訓練成本、計算方式、受訪者意見、歸因限制、決策與後續檢查。
1.2 本件不做什麼（需求界線）

不屬於本件的內容 | 原因
只有滿意度高分 | 滿意度不等於財務改善，不得作為財務效益證據
只有支出下降 | 支出下降不等於由訓練造成；本件須分開列示觀察差異、受訪者認知、合理推論、尚待查證之因果關係
調查及課後行動計畫追蹤（0105／I18-E13／項目 114） | 可作為方法旁證，不取代本件財務前後核算；資料、數值、case_id、對象不得搬入本件
證照獲取率（0104） | 不同證據；不得以合格／報考／取得證照人數替代財務前後比較，不得共用分子分母
第三方感謝函（0103） | 不同證據；不得作為財務差異來源
顯著組織績效問卷／行動方案量化與歸因（157 項目 120／I18-L4） | 範圍較廣；本件不宣稱滿足項目 120，項目 120 內容亦不得搬入本件
會計憑證、財務報表、核銷單、成果宣傳稿 | 文件類型不同；本件為「訓練之組織財務效果分析報告」

1.3 目標讀者與判讀原則
主要讀者：訓練行政承辦、財務資料提供角色、品質覆核者、評核委員。 判讀原則：管理者須能依本件判斷「現有證據只能支持到哪一層」——問卷高分 ≠ 財務效益；同期支出下降 ≠ 訓練的因果成效。
2. 案例範圍與方法（T02）
T02 案例及配對範圍表

項目 | 內容（全部 SYNTHETIC） | fact_id | 資料狀態
案例 ID | SYN-0106-FIN-01 | F0106-CASE-01 | SYNTHETIC
訓練活動（合成） | 「活動採購比價及核銷文件整理」內部訓練 | F0106-TRN-01 | SYNTHETIC；非原始點協會實際辦理
辦理單位（合成） | 小型非營利組織（代號 SYN-ORG-01） | F0106-ORG-01 | SYNTHETIC；真實機構名稱 UNKNOWN
目標客戶代碼 | SYN-CUST-01（1 人） | F0106-CUS-01 | SYNTHETIC
學員代碼 | SYN-L01–SYN-L10（10 人，另有 2 人未回覆） | F0106-LRN-01 | SYNTHETIC；無真實姓名
訓練日期（合成） | 2026-04-10（1 日，6 小時） | F0106-DATE-01 | SYNTHETIC
訓練前期間 | 2025-09-01 至 2026-02-28（6 個月） | F0106-PER-01 | SYNTHETIC
訓練後期間 | 2026-04-11 至 2026-10-10（6 個月） | F0106-PER-02 | SYNTHETIC
資料 cutoff（合成） | 2026-10-15；後期窗口結束後 5 日 | F0106-DATE-02 | SYNTHETIC；真實 cutoff 核准 UNKNOWN/HOLD
觀察單位 | 1 組「同規格採購籃」＝同一品項規格與數量的一次採購合計 | F0106-UNIT-01 | SYNTHETIC 定義
樣本數 | 10 組採購籃（前後配對） | F0106-SMP-01 | SYNTHETIC
納入規則 | ①同品項、同規格、同數量；②前後期間各歸屬一窗口；③金額含稅總額；④可追溯至示範明細列 | F0106-RULE-01 | SYNTHETIC 規則
排除規則 | ①規格或數量變更者；②一次性設備採購；③跨窗口訂單；④無法配對之零星支出；⑤贈與或實物抵充 | F0106-RULE-02 | SYNTHETIC 規則
匹配規則說明 | 依品項代碼＋規格＋數量一一對應；一一對應失敗則該組不得納入，須改列 UNKNOWN | F0106-RULE-03 | SYNTHETIC；真實憑證需求見第 11 章
價格指數假設 | 後期價格指數 0.98（基期＝1.00，基期＝訓練前期間） | F0106-IDX-01 | SYNTHETIC 假設；非經審計或已核實之價格指數
數據品質 | 前後各 10 筆，無缺漏、無異常值；為示範而設計 | F0106-QLT-01 | SYNTHETIC；真實帳務核對 UNKNOWN/HOLD
觀察視角 | 目標客戶及學員對訓練帶來組織績效改善的財務面認知 | F0106-VIEW-01 | SYNTHETIC

方法聲明（不可省略）： 本比較為同一品項前後配對之描述性比較，不是實驗設計；無隨機分派、無對照組、樣本 n=10；同規格、同數量為示範假設。所有差異一律稱為「觀察差異」，不得稱為「訓練成效」或「訓練造成」。
3. 完整財務前後資料表（T03）
單位：NT$（含稅總額）；期間：前期 2025-09-01～2026-02-28、後期 2026-04-11～2026-10-10；n=10 組配對；狀態：SAMPLE/SYNTHETIC。
T03 10 組財務原始示範列

序號 | 品項代碼（SYN） | 前期金額 | 後期金額 | 名目差額（前-後） | 價格指數 | 後期標準化值（後÷0.98） | 標準化差額（前-標準化） | fact_id
1 | SYN-BID-01 | 8,000 | 7,500 | 500 | 0.98 | 7,653.06 | 346.94 | F0106-FIN-01
2 | SYN-BID-02 | 12,000 | 11,500 | 500 | 0.98 | 11,734.69 | 265.31 | F0106-FIN-02
3 | SYN-BID-03 | 9,000 | 8,600 | 400 | 0.98 | 8,775.51 | 224.49 | F0106-FIN-03
4 | SYN-BID-04 | 11,000 | 10,400 | 600 | 0.98 | 10,612.24 | 387.76 | F0106-FIN-04
5 | SYN-BID-05 | 7,000 | 6,800 | 200 | 0.98 | 6,938.78 | 61.22 | F0106-FIN-05
6 | SYN-BID-06 | 15,000 | 14,000 | 1,000 | 0.98 | 14,285.71 | 714.29 | F0106-FIN-06
7 | SYN-BID-07 | 10,000 | 9,500 | 500 | 0.98 | 9,693.88 | 306.12 | F0106-FIN-07
8 | SYN-BID-08 | 8,000 | 7,600 | 400 | 0.98 | 7,755.10 | 244.90 | F0106-FIN-08
9 | SYN-BID-09 | 10,000 | 9,400 | 600 | 0.98 | 9,591.84 | 408.16 | F0106-FIN-09
10 | SYN-BID-10 | 10,000 | 8,700 | 1,300 | 0.98 | 8,877.55 | 1,122.45 | F0106-FIN-10
合計 | — | 100,000 | 94,000 | 6,000 | 0.98 | 95,918.37（總數直算） | 4,081.63 | F0106-TOT-01/02

來源欄與證據狀態

欄位 | 示範填值 | 真實轉換所需來源 | 目前狀態
前期金額來源 | SYN 示範明細列 | 採購或會計明細（含數量／規格） | UNKNOWN/HOLD
後期金額來源 | SYN 示範明細列 | 同上，且須可與前期配對 | UNKNOWN/HOLD
數量／規格憑證 | SYN 示範假設「同規格、同數量」 | 請購單、驗收單、報價單 | UNKNOWN/HOLD
價格指數來源 | SYN 假設 0.98 | 市場價格或物價調整依據 | UNKNOWN/HOLD
期間與 cutoff | SYN 日期 | 資料期間與 cutoff 核准 | UNKNOWN/HOLD

四捨五入政策： 逐列顯示至小數點後 2 位；總數以總額直算為準（94,000 ÷ 0.98 = 95,918.37；100,000 − 95,918.37 = 4,081.63）。逐列四捨五入加總為 95,918.36 與 4,081.64，與總數直算相差 NT$0.01，屬列示四捨五入差異，不影響任何結論；覆核時須確認差額 ≤ NT$0.05，否則判 FAIL。
名目差額與標準化差額不得混用： 名目差額 NT$6,000 是「後期實付低於前期」的原始觀察；標準化毛差額 NT$4,081.63 是「剔除價格變動後的估算差異」。兩者是不同結果，不得稱為同一數字，也不得互相替代。
圖 1　前後支出、價格標準化與直接訓練成本比較
圖 1 以同一單位及相同六個月期間呈現五項合成數值。前期支出 100,000、後期名目支出 94,000、後期標準化支出 95,918.37、直接訓練成本 8,000；扣除成本後估算淨財務效益為 −3,918.37。負值表示本示範未達損益平衡，不代表真實財務結果。
圖 1 所用數值

類別 | 數值（NT$） | 說明
前期支出 | 100,000 | 10 組合計
後期名目支出 | 94,000 | 10 組合計
後期標準化支出 | 95,918.37 | 94,000 ÷ 0.98
直接訓練成本 | 8,000 | 講師＋教材＋場地交通
估算淨財務效益 | -3,918.37 | 4,081.63 - 8,000

圖 1 前後費用與訓練成本拆解。SAMPLE/SYNTHETIC；NT$；前後各六個月；配對 n=10。
4. 訓練成本明細（T04）
T04 訓練成本明細表（SYNTHETIC）

成本項 | 金額（NT$） | 現金／非現金 | 假設 | 來源鍵 | fact_id
講師費 | 4,500 | 現金支出 | 1 日 6 小時，示範費率 | SYN 示範成本表 | F0106-COST-01
教材 | 1,000 | 現金支出 | 講義與示範表單印製 | SYN 示範成本表 | F0106-COST-02
場地與交通 | 2,500 | 現金支出 | 場地租借＋講師交通 | SYN 示範成本表 | F0106-COST-03
直接訓練成本合計 | 8,000 | 現金支出 | 4,500＋1,000＋2,500 | 對帳 T05 第 7 列 | F0106-COST-TOT
志工籌備時間 | 未量化 | 非現金／機會成本 | 本示範未提供工時與估值依據；不計入直接成本與 ROI 分母 | 政策：分開揭露 | F0106-COST-04
學員時間投入 | 未量化 | 非現金／機會成本 | 本示範未提供工時與估值依據；不計入直接成本與 ROI 分母 | 政策：分開揭露 | F0106-COST-05
「估算時間價值」 | — | 非現金 | 不得列為已節省現金，不得併入淨效益 | 硬規則 | F0106-COST-06

志工及學員時間投入均為非現金機會成本。由於本示範未提供可核實的工時與估值依據，兩者都不量化，也不計入直接成本或 ROI 分母；正式採計須取得授權依據並重新計算。
成本完整性聲明： 示範 ROI 的分母只使用直接現金成本 8,000；若真實轉換時把機會成本納入，分母將變動，必須重算並重新標示 ROI 口徑，不得沿用本稿數字。不得選擇性刪除任何一項直接成本（講師、教材、場地交通）以美化結果。
5. 逐步核算與對帳（T05）
T05 計算對帳表（全部數值須可逐步重算）

# | 項目 | 公式 | 代入值 | 結果 | 四捨五入 | 覆核 | fact_id
1 | 前期合計 | Σ 前期 10 組 | 8,000+12,000+9,000+11,000+7,000+15,000+10,000+8,000+10,000+10,000 | 100,000 | 整數 | 待雙人重算 | F0106-CALC-01
2 | 後期合計 | Σ 後期 10 組 | 7,500+11,500+8,600+10,400+6,800+14,000+9,500+7,600+9,400+8,700 | 94,000 | 整數 | 待雙人重算 | F0106-CALC-02
3 | 名目差額 | 前期 - 後期 | 100,000 - 94,000 | 6,000 | 整數 | 待雙人重算 | F0106-CALC-03
4 | 後期標準化支出 | 後期 ÷ 價格指數 | 94,000 ÷ 0.98 | 95,918.367… | 95,918.37 | 待雙人重算 | F0106-CALC-04
5 | 標準化毛差額 | 前期 - 標準化支出 | 100,000 - 95,918.37 | 4,081.63 | 2 位小數 | 待雙人重算 | F0106-CALC-05
6 | 相對基期差異率 | 標準化毛差額 ÷ 前期 × 100% | 4,081.63 ÷ 100,000 × 100% | 4.08163% | 4.08% | 待雙人重算 | F0106-CALC-06
7 | 直接訓練成本 | 講師＋教材＋場地交通 | 4,500+1,000+2,500 | 8,000 | 整數 | 待雙人重算 | F0106-CALC-07
8 | 估算淨財務效益 | 標準化毛差額 - 直接成本 | 4,081.63 - 8,000 | -3,918.37 | 2 位小數 | 待雙人重算 | F0106-CALC-08
9 | 示範 ROI | (毛差額 - 成本) ÷ 成本 × 100% | (4,081.63 - 8,000) ÷ 8,000 × 100% | -48.9796% | -48.98% | 待雙人重算 | F0106-CALC-09
10 | 毛額報酬率（僅供參考） | 毛差額 ÷ 成本 × 100% | 4,081.63 ÷ 8,000 × 100% | 51.02% | 2 位小數 | 不得單獨引用為 ROI | F0106-CALC-10
11 | 名目口徑淨額（不標準化，僅對照） | 6,000 - 8,000 | -2,000 | -2,000 | 整數 | 不得與第 8 列混用 | F0106-CALC-11
12 | 損益平衡所需毛差額 | 毛差額 ≥ 成本 | 8,000 | 8,000 | 整數 | 差距 = 8,000 - 4,081.63 = 3,918.37 | F0106-CALC-12
13 | 損益平衡所需成本上限 | 成本 ≤ 毛差額 | 4,081.63 | 4,081.63 | 2 位小數 | 現成本 8,000，超出 3,918.37 | F0106-CALC-13
14 | 損益平衡所需價格指數 | 100,000 - 94,000 ÷ x = 8,000；x = 94,000 ÷ 92,000 | 1.0217391 | 1.0217391（七位小數；代入回算差額約 NT$0.003） | 七位小數 | 指數達臨界值恰好損平；高於才為正 | F0106-CALC-14
15 | 觀察期均攤月毛差額 | 4,081.63 ÷ 6 | 680.272 | 680.27 | 2 位小數 | 僅為算術外推，非已實現節省 | F0106-CALC-15
16 | 外推損平月數（參考） | 8,000 ÷ 680.27 | 11.76 | 約 11.8 個月 | 1 位小數 | 不得列為已達成；屬未查證外推 | F0106-CALC-16

核算聲明：
不同結果不得混用： 第 3 列（6,000）與第 5 列（4,081.63）是兩個不同結果；任何表格、圖表或結論均不得將其合併、替換或互稱。
外推限制： 第 15、16 列是未經驗證的算術外推，只能用於後續檢查規劃，不得記為現金節省或已實現效益。
損益平衡判定： 尚未達損益平衡，因毛差額 4,081.63 小於成本 8,000，缺口為 3,918.37。
6. 敏感度與損益平衡（T06）
T06 敏感度表（價格指數 0.96–1.00；成本固定 8,000）

價格指數 | 後期標準化支出（94,000 ÷ x） | 標準化毛差額 | 淨值（毛 - 8,000） | 示範 ROI | 是否損益平衡 | fact_id
0.96 | 97,916.67 | 2,083.33 | -5,916.67 | -73.96% | 否 | F0106-SEN-01
0.97 | 96,907.22 | 3,092.78 | -4,907.22 | -61.34% | 否 | F0106-SEN-02
0.98（基準） | 95,918.37 | 4,081.63 | -3,918.37 | -48.98% | 否 | F0106-SEN-03
0.99 | 94,949.49 | 5,050.51 | -2,949.49 | -36.87% | 否 | F0106-SEN-04
1.00 | 94,000.00 | 6,000.00 | -2,000.00 | -25.00% | 否 | F0106-SEN-05
1.0217391（＝94,000÷92,000；理論臨界值） | 92,000.00 | 8,000.00 | 0.00 | 0.00% | 是（理論值；非觀測值；位於 0.96–1.00 之外） | F0106-SEN-06

損益平衡臨界價格指數為 1.0217391（94,000 ÷ 92,000）：達此值恰好損平，高於此值才可能轉正。因 x 代表後期價格指數，1.0217391 高於基期 1.00，等同後期價格水準須比基期高約 2.17%；此為理論門檻，不是觀測值。本例檢視的 0.96–1.00 區間未達該門檻，因此在這個六個月窗口內，全區間均未損平。
敏感度結論（必保留）： 在指數 0.96–1.00 區間內，標準化毛差額約 NT$2,083.33–6,000，扣除直接成本後淨值約 −NT$5,916.67 至 −NT$2,000，全區間皆為負，全部未達損益平衡。即使採用最有利假設（指數 1.00，即不作價格調整、等同名目口徑），淨額仍為 −2,000。敏感度分析不能把負結果翻成正結果。
7. 問卷工具與合成填答結果（T07、T08）
7.1 T07 學員問卷工具（完整可直接使用）
標題： 訓練後財務面感知調查（學員用）— SYNTHETIC 示範版
填寫方式與保密告知：
匿名填寫： 使用匿名代碼（例如 SYN-L01），不填真實姓名。
量尺： 1–5 分，依序為完全不同意、不同意、普通、同意、非常同意。
不適用選項： 可選「不適用／未觀察」；該選項不計入均值，分母改為有效填答數。
缺答與最低樣本： 任一題缺答，該題有效分母減 1；單題有效填答少於 8 份時，結果標為 UNKNOWN/HOLD。
保密告知： 填答僅供內部品質分析。真實版須另附個資告知、同意依據與保存期限；目前真實依據為 UNKNOWN/HOLD。

題號 | 題幹 | 適用對象 | 計分
Q1 | 本次訓練後，我所屬單位的財務相關流程（請款、核銷、採購文件整理）有所改善。 | 學員 | 1–5，反向題無
Q2 | 我能運用比價方式辦理採購。 | 學員 | 1–5
Q3 | 我能計算同一品項訓練前後的支出差異。 | 學員 | 1–5
Q4 | 核銷文件的完整度較訓練前提升。 | 學員 | 1–5
Q5 | 相較於本次訓練成本，我認為訓練的價值較高。 | 學員 | 1–5（感知題，不等同財務效益）
Q6 | 我願意在後續工作中持續使用所學方法。 | 學員 | 1–5
C1 | 依本案例所列資料，我認為訓練前後呈現可觀察的財務面差異；此觀察不表示該差異由訓練造成。 | 目標客戶（1 人） | 1–5（個案感知）

C1 專用計分錨點： 1＝完全不同意；2＝不同意；3＝中立／無法判斷；4＝同意；5＝非常同意。此題只記錄單一合成個案對「資料呈現觀察差異」的意見，不作財務數據證據，也不推論訓練造成差異。
7.2 T08 已填合成問卷逐列摘要（n=10，SYNTHETIC）
邀請 12 人、有效回覆 10 人，回覆率 = 10 ÷ 12 = 83.33%（F0106-SRV-RT）。無缺答；「不適用／未觀察」使用數 = 0。

ID | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | 個人總分 | fact_id
SYN-L01 | 5 | 5 | 4 | 4 | 4 | 4 | 26 | F0106-SRV-01
SYN-L02 | 4 | 4 | 4 | 5 | 3 | 4 | 24 | F0106-SRV-02
SYN-L03 | 4 | 3 | 4 | 4 | 4 | 3 | 22 | F0106-SRV-03
SYN-L04 | 4 | 4 | 5 | 4 | 3 | 4 | 24 | F0106-SRV-04
SYN-L05 | 3 | 3 | 3 | 4 | 3 | 2 | 18 | F0106-SRV-05
SYN-L06 | 5 | 5 | 5 | 5 | 4 | 5 | 29 | F0106-SRV-06
SYN-L07 | 4 | 4 | 4 | 4 | 4 | 4 | 24 | F0106-SRV-07
SYN-L08 | 4 | 4 | 3 | 3 | 2 | 3 | 19 | F0106-SRV-08
SYN-L09 | 4 | 2 | 4 | 4 | 4 | 4 | 22 | F0106-SRV-09
SYN-L10 | 2 | 3 | 2 | 3 | 2 | 3 | 15 | F0106-SRV-10
合計 | 39 | 37 | 38 | 40 | 33 | 36 | 223 | F0106-SRV-TOT
10 人均值 | 3.9 | 3.7 | 3.8 | 4.0 | 3.3 | 3.6 | 22.30 | F0106-SRV-AVG

題項彙總

題號 | 合計 | 均值 | 4–5 分人數 | 4–5 分比例 | 1–2 分人數 | 有效數 | fact_id
Q1 財務流程改善 | 39 | 3.9 | 8/10 | 80% | 1（L10） | 10 | F0106-SUM-01
Q2 能運用比價 | 37 | 3.7 | 6/10 | 60% | 1（L09） | 10 | F0106-SUM-02
Q3 會算前後差異 | 38 | 3.8 | 7/10 | 70% | 1（L10） | 10 | F0106-SUM-03
Q4 核銷文件完整 | 40 | 4.0 | 8/10 | 80% | 0 | 10 | F0106-SUM-04
Q5 價值高於成本 | 33 | 3.3 | 5/10 | 50% | 2（L08、L10）；未達 4 分合計 5/10（其中 3 分 3 人、2 分 2 人） | 10 | F0106-SUM-05
Q6 願意持續使用 | 36 | 3.6 | 6/10 | 60% | 1（L05 為 2 分） | 10 | F0106-SUM-06

讀法限制（不可省略）： 1. Q5 均值 3.3、僅 5/10 給 4–5 分，學員自身對「價值高於成本」的看法就存在分歧，與第 5 章負淨值方向一致，不得只引用 Q1、Q4 的高分。 2. Q1、Q4 各 8/10 為 4–5 分，僅代表自陳感知，不證明組織財務改善，也不證明財務數字。 3. 低分回覆（L05、L08、L10）必須保留在表內，不得剔除。
目標客戶觀點（n=1，嚴格限縮推論）

對象 | 題號 | 得分（1–5） | 說明 | fact_id
SYN-CUST-01 | C1 | 4 | 認同本案例資料呈現訓練前後可觀察的財務面差異；不代表因果 | F0106-CUS-02

推論限制： 客戶回覆僅 1 人，只能作單一個案敘述；不得寫成「目標客戶普遍認為」、「多數客戶肯定」或任何全體推論；不可與財務數字互相證明。
8. 財務結果與感知結果分開分析及邏輯鏈（T09）
8.1 兩條證據線必須分開

證據線 | 內容 | 能支持什麼 | 不能支持什麼
A. 財務計算線 | 10 組前後金額、價格標準化、成本、淨值、ROI | 「在本示範假設下，觀察到的支出差異及其算術結果」 | 不能支持「訓練造成差異」；不能支持感知滿意
B. 感知問卷線 | 10 份學員問卷、1 份客戶問卷 | 「受訪者自陳的認同程度」 | 不能支持任何金額、成本或財務結論

交叉禁則： 不得用 B 線高分「補強」A 線的財務結論，也不得用 A 線的支出下降「證實」B 線的感知；兩線只在第 8 章並列，並於第 9 章標示歸因邊界與「尚待查證」。
表 T09｜訓練至財務結果邏輯鏈與證據缺口（SAMPLE／SYNTHETIC）

段 | 邏輯節點 | 目前證據 | 證據強度 | 缺口（UNKNOWN） | fact_id
① | 訓練投入（1 日 6 小時、成本 8,000） | SYN 成本表（T04） | 弱（合成、無憑證） | 真實成本原始憑證、出席與完成名冊 | F0106-LOG-01
② | 學習（懂比價、會算差異） | 問卷 Q2=3.7、Q3=3.8 自陳 | 弱（自陳、無前測） | 前後測、實作評量 | F0106-LOG-02
③ | 實際採購行為改變（比價、核銷整理） | 問卷 Q1、Q4 自陳＋採購籃差異（間接） | 弱～中（無行為直接觀測） | 採購流程紀錄、比價單、核銷退件率 | F0106-LOG-03
④ | 文件／成本產出（文件完整、支出較低） | T03 觀察差異（標準化 +4,081.63） | 中（算術可重算，來源為合成） | 真實可比明細、數量規格憑證 | F0106-LOG-04
⑤ | 組織財務結果（淨效益） | T05：-3,918.37、ROI -48.98% | 中（算術一致）；結論為負 | 混淆因素排除、雙人重算、期間核定 | F0106-LOG-05
⑥ | 因果歸因「訓練導致改善」 | 無證據 | 不足 | 對照組、隨機化、行為中介證據 | F0106-LOG-06

圖 2 訓練邏輯鏈與證據強度。SAMPLE/SYNTHETIC；前後各六個月；配對 n=10、問卷 n=10、客戶 n=1。
圖 2 圖說： 訓練至財務結果之邏輯鏈與證據強度（SAMPLE/SYNTHETIC；10 組配對、學員問卷 10 份、目標客戶 1 人）。圖中依序呈現訓練投入、學習、採購行為、文件與成本產出、財務結果及因果歸因；淨額為負，因果證據不足。
9. 混淆因素、資料弱點與歸因邊界（T10）
T10 混淆因素及敏感性處理

# | 混淆因素 | 可能影響 | 目前證據 | 替代解釋 | 處理／限制 | fact_id
1 | 市場價格／通膨變動 | 後期價格下降造成支出減少 | 僅 SYN 指數 0.98 | 支出下降可能與訓練無關 | 已作標準化；指數為合成，真實依據 UNKNOWN | F0106-CONF-01
2 | 供應商更換 | 更便宜供應商壓低價格 | 無供應商資料 | 降價來自換廠議價 | 真實版須列供應商一致性檢查；缺件即 HOLD | F0106-CONF-02
3 | 規格／數量變更 | 數量少導致總額低 | SYN 假設同規格同數量 | 實際可能縮量 | 須憑請購／驗收單核對；未核對前不成立 | F0106-CONF-03
4 | 採購季節 | 淡旺季價差 | 前後窗口日期為 SYN | 季節性降價 | 須同期歷史資料比對 | F0106-CONF-04
5 | 議價權／採購規模 | 大量採購取得折扣 | 無議價紀錄 | 折扣來自採購量 | 須調閱議價紀錄 | F0106-CONF-05
6 | 物價水準整體變動 | 實質購買力改變 | 無外部物價資料 | 全體物價下跌 | 須接合法物價指標 | F0106-CONF-06
7 | 採購人員經驗／異動 | 資深者本就會比較價格 | 無人員異動資料 | 資深員工上任導致降價 | 須核對期間內人事異動 | F0106-CONF-07
8 | 預算限制 | 預算上限迫使節流 | 無預算文件 | 因預算緊縮而少買 | 須比對預算與執行數 | F0106-CONF-08
9 | 其他制度改變（系統、簽核層級、新表單） | 流程改善來自制度而非訓練 | 無制度變更紀錄 | 新系統上線造成改善 | 須列期間內制度變更清單 | F0106-CONF-09
10 | 樣本太小、非隨機、無對照 | 差異可能來自偶然 | n=10、無對照組 | 隨機波動即可解釋 | 結論只能寫「觀察差異」 | F0106-CONF-10
11 | 自陳與社會期許偏差 | 問卷分數偏高 | 問卷為 SYN 自陳 | 受訪者傾向給正面分 | 不得以問卷證明財務；低分必須保留 | F0106-CONF-11
12 | 回覆偏差（2 人未回覆） | 未回覆者意見不同 | 10/12，回覆率 83.33% | 未回覆者可能較不滿 | 未回覆原因 UNKNOWN | F0106-CONF-12

歸因邊界（固定措辭）：
允許措辭：「在示範假設下觀察到前後支出差異」、「受訪者自陳」、「與訓練時序相近」、「尚待查證」。
禁止措辭：「訓練使成本下降」、「訓練提升組織績效 4.08%」、「因為訓練所以省了 6,000」、「已證實訓練具 ROI」。
因果限制： 樣本小、非隨機且無對照，不能認定訓練造成差異；回覆意見與財務結果不得互相證明。
外推標記： 任何外推（含 T05 第 15、16 列）一律標示為「未查證外推」。
10. 結論與管理行動（T11）
10.1 結論（固定四點，不得刪改方向）
毛差異為正： 按基期價格標準化後，10 組採購籃的支出差異為 +NT$4,081.63，占基期 4.08%（名目差額 NT$6,000 為另一不同結果）。
淨額為負、未損平： 扣除直接訓練成本 NT$8,000 後，示範淨財務效益 −NT$3,918.37，示範 ROI −48.98%；觀察期內未達損益平衡，缺口 NT$3,918.37。
敏感度全區間為負： 價格指數 0.96–1.00 之下，淨值介於 −NT$5,916.67 至 −NT$2,000，無任何情景轉為正數。
證據層級有限： 問卷（學員 n=10、回覆率 83.33%、Q1/Q4 各 8/10、Q5 僅 5/10；客戶 n=1、C1=4）僅為感知；混淆因素未排除、無對照，不得作因果陳述；一切資料為 SYNTHETIC，REAL=UNKNOWN/HOLD。
T11 樣本改善行動表（已填 SAMPLE 範例；角色、日期、決定均為虛構示範）

# | 問題 | 下一步 | 責任角色（SAMPLE，虛構） | 期限（SYN） | 完成證據 | 暫緩（HOLD）條件 | fact_id
1 | 淨效益為負、未損平 | 調閱 6 個月後追蹤期間之同規格採購資料，重算是否改善至損平 | 財務窗口 SYN-ROLE-02 | 2026-11-12 | 經覆核之重算表（差額=0） | 無可配對明細即 HOLD | F0106-ACT-01
2 | 價格指數 0.98 為合成假設 | 取得合法可引用之物價／市場價格依據，重新標準化 | 訓練承辦 SYN-ROLE-01 | 2026-11-05 | 指數來源文件＋重算紀錄 | 無合法來源則維持 SYN，不升 REAL | F0106-ACT-02
3 | 直接成本僅 3 項，缺原始憑證 | 收齊講師費、教材、場地交通原始憑證 | 財務窗口 SYN-ROLE-02 | 2026-10-29 | 憑證清冊（去識別） | 憑證不全即凍結 ROI 口徑 | F0106-ACT-03
4 | 混淆因素未排除 | 建立供應商／規格／季節／人事／制度變更檢查表並逐項核對 | 品質覆核 SYN-ROLE-03 | 2026-11-19 | 已填檢查表＋未解項目清單 | 未解項目 ≥1 時禁止因果敘述 | F0106-ACT-04
5 | 問卷僅自陳、客戶 n=1 | 補做前後測與實作評量；客戶樣本擴充（須先取得同意與個資依據） | 訓練承辦 SYN-ROLE-01 | 2026-12-03 | 原始問卷（去識別）＋同意紀錄 | 無同意／個資依據即不得收集 | F0106-ACT-05
6 | 無雙人獨立重算 | 指派第二人以 T05 對帳表逐列重算並簽署 | 品質覆核 SYN-ROLE-03 | 2026-11-05 | 第二人重算紀錄（差額=0） | 差額 ≠ 0 即不得交付 | F0106-ACT-06
7 | 損益平衡缺口 3,918.37 | 評估是否調整訓練成本結構或延長觀察窗口（須先核算，不得預設可行） | 決策主管 SYN-ROLE-04 | 2026-11-26 | 評估備忘（標示未核定） | 未經權責核定前不得執行變動 | F0106-ACT-07
8 | 本稿為 SAMPLE | 依第 11 章逐欄替換為真實來源後重新覆核 | 分析角色 SYN-ROLE-05 | 依第 11 章替換完成日（SAMPLE） | T12 全列狀態非 UNKNOWN/HOLD | 任一必要來源缺件即維持 HOLD | F0106-ACT-08

決策狀態（示範）： SAMPLE → 不升格；REAL=UNKNOWN/HOLD；未提出、亦不得推定任何協會核准。本表僅示範「若為真實情境，後續檢查可如何安排」；所有角色、日期與決定皆為虛構（F0106-DEC-01，SYNTHETIC）。
11. 空白正式替換表與交付前判定
11.1 空白正式替換表（可直接複製填寫）

# | 待替換項目 | 本稿 SYN 值 | 正式來源（憑證名稱／編號） | 取得日期 | 保管位置 | 授權依據 | 覆核人 | 備註
1 | 前期 10 組金額（合計 100,000） |  |  |  |  |  |  | 
2 | 後期 10 組金額（合計 94,000） |  |  |  |  |  |  | 
3 | 數量／規格配對憑證 | 同規格同數量（SYN 假設） |  |  |  |  |  | 
4 | 價格指數（0.98） | SYN 假設 |  |  |  |  |  | 
5 | 直接訓練成本 3 項（8,000） | SYN 成本表 |  |  |  |  |  | 
6 | 訓練出席／完成名冊 | 12 人邀請（SYN） |  |  |  |  |  | 
7 | 學員問卷原始資料（10 份） | SYN 明細 |  |  |  |  |  | 
8 | 客戶問卷原始資料（1 份） | SYN-CUST-01 |  |  |  |  |  | 
9 | 個資告知／同意依據 | UNKNOWN |  |  |  |  |  | 
10 | 資料期間與 cutoff 核准 | SYN 日期 |  |  |  |  |  | 
11 | 混淆因素說明文件 | 無 |  |  |  |  |  | 
12 | 權責核定 | 無 |  |  |  |  |  | 

11.2 資料來源清單（空白）

來源編號 | 來源名稱 | 類型（帳務／採購／問卷／核准／物價） | 期間 | 去識別狀態 | 可否公開 | 對應 fact_id
 |  |  |  |  |  | 
 |  |  |  |  |  | 
 |  |  |  |  |  | 

11.3 雙人獨立重算紀錄（空白）

重算項目 | 第一人結果 | 第二人結果 | 差額 | 是否 = 0 | 簽署（真實欄位保持空白，不得代簽）
前期合計 |  |  |  | □是 □否 | 
後期合計 |  |  |  | □是 □否 | 
標準化支出 |  |  |  | □是 □否 | 
標準化毛差額 |  |  |  | □是 □否 | 
直接成本合計 |  |  |  | □是 □否 | 
淨效益 |  |  |  | □是 □否 | 
ROI |  |  |  | □是 □否 | 
題項均值與回覆率 |  |  |  | □是 □否 | 

11.4 異常與暫緩（HOLD）條件
對帳差額 不為零（容許列示四捨五入 ≤ NT$0.05）→ 凍結受影響財務結論。
必要來源 缺一（帳務／採購明細、成本憑證、價格基準、有效樣本、原始回覆、期間核定、第二人重算）→ REAL=UNKNOWN/HOLD。
供應商、規格／數量、期間不一致而無法配對 → 該組剔除並列 UNKNOWN；剔除後 n < 6 → 整體財務結論 HOLD。
問卷單題有效填答 < 8 → 該題 UNKNOWN/HOLD。
出現個資未去識別、無同意依據 → 立即停止使用該資料。
HOLD 只凍結真實財務結論，不阻擋其他不相依文件。
11.5 交付前判定（T13；SAMPLE／SYNTHETIC 示範）
下表演示承辦者可採用的判讀欄位，不是本稿的驗收收據。表中有資料可見或算式可重算，不等於獨立審查、全頁視覺、標題盲測、發布檔案取回一致性查核或 REAL 核准已完成；正式使用時必須依該次原件與可查證證據重新判定。本表示範狀態不預先宣告任何語意驗收 PASS。
表 T13｜交付前判定（SAMPLE／SYNTHETIC 示範）

# | 檢查項目 | 判定標準 | 本稿示範觀察（非驗收） | 未達標處理
1 | 內容完整 | 來源定位、財務資料、計算、問卷、結果分析、事實索引與替換清冊逐項依本文件所列佐證範圍核對 | SAMPLE 各節已有示範內容；仍須由未參與撰寫者依本文件所列需求核對，未作正式判定 | 缺項 → 退回補齊
2 | 數學可重算 | 財務明細、合計及四捨五入差額可按表列資料重算；容差 ≤ 0.05，並留第二人紀錄 | 本稿提供可重算的 SYN 算式；第二人獨立重算尚未完成 | 未重算 → 維持 UNKNOWN，不得判技術全過
3 | 負向結果保留 | 淨值 -3,918.37、ROI -48.98% 均完整呈現 | SYN 範例列出負值；不代表真實效益或驗收結論 | 刪除或弱化 → 退回修正
4 | 固定資料一致 | 所有合成數字與本案例設定一致，並可回查來源 | 本稿明示合成輸入；REAL 原始來源仍 UNKNOWN/HOLD | 任一改動 → 重新核算
5 | 金額口徑分開 | 名目差額 6,000 與標準化毛差額 4,081.63 分列 | SAMPLE 表分欄呈現；正式件仍須核對原始憑證與口徑 | 混用 → 退回修正
6 | 問卷數據一致 | 邀請 12 人、有效 10 人、回覆率 83.33%，題項合計一致 | 表列合成填答與彙總供重算；不是實際回收紀錄 | 矛盾 → 重新彙整並保留原始回覆
7 | SAMPLE／REAL 界線 | 正文與頁眉標示合成示範；REAL 維持 UNKNOWN/HOLD | 本稿文字含 SAMPLE/SYNTHETIC；頁面呈現仍 UNKNOWN，須完成全頁目視 | 標示缺漏或頁面不可讀 → 暫緩使用
8 | 因果判讀 | 獨立覆核判斷是否把財務差異歸因於訓練，並辨別感知題、替代解釋及禁用例句 | UNKNOWN；本稿尚未由獨立覆核者完成本項語意判定 | 未完成覆核或出現因果結論 → 不得標 PASS
9 | 個資及第三方文件 | 不含未授權個資、代簽或虛構第三方證明 | 本稿以合成代碼示範；真實使用時的授權及個資核對尚未執行 | 發現未授權或虛構正式文件 → 停用並查核
10 | 不同佐證用途分開 | 不與課後追蹤、證照獲取率、第三方感謝函或廣泛績效歸因混用 | 本稿列出範圍界線；跨文件原始證據比對尚未完成 | 混用 → 拆分文件與資料
11 | 遮標題辨識 | 遮蔽文件標題與封面後，由未參與撰寫者說明文件用途 | UNKNOWN；尚未實際執行標題盲測 | 未完成盲測或誤認為其他文類 → 退回改寫
12 | 頁面視覺 | 逐頁查看表格、圖說、字級、分頁、頁眉頁腳及字元 | UNKNOWN；全頁渲染與目視尚未完成 | 未檢項 → 維持 UNKNOWN，不得標 PASS
13 | 獨立語意覆核 | 由未參與撰寫者依定稿文件與適用需求獨立審查 | UNKNOWN；本版尚未完成未參與撰寫者的獨立內容審查 | 未檢項 → 維持 UNKNOWN，不得標 PASS
14 | 遠端原始位元組讀回 | 發布後由指定公開位置取回文件，比對檔案版本與內容是否一致 | UNKNOWN；本版尚未從指定公開位置取回並比對 | 尚未取回或內容不一致 → 不得判定通過，先查明版本差異
15 | 真實資料升格 | 必要來源、授權、雙人重算及差額檢查均完成 | FAIL → HOLD；目前只有 SYNTHETIC 示範，REAL=UNKNOWN/HOLD | 維持 REAL=UNKNOWN/HOLD，不得作實績佐證

分項判定原則： 來源映射、內容完整、技術／數學、SAMPLE／REAL、頁面視覺、獨立語意及發布檔案取回一致性查核必須分開判定；任何未查項目一律標示 UNKNOWN，不可用整體 PASS 遮蔽。
12. 事實鍵索引與 REAL 替換清冊（T12）
事實鍵索引（本稿使用的合成資料）

fact_id | 類別 | SYN 值 | doc_id | case_id | 正文位置 | 假設理由 | 真實替換來源 | 負責角色 | 狀態
F0106-CASE-01 | 案例 | SYN-0106-FIN-01 | 0106 | SYN-0106-FIN-01 | T02 | 單一示範案例，避免跨文件共用 | 不適用（案例代號可保留） | SYN-ROLE-05 | SYNTHETIC
F0106-ORG-01 | 組織 | SYN-ORG-01（小型非營利） | 0106 | SYN-0106-FIN-01 | T02 | 情境適切性示範 | 真實機構基本資料 | UNKNOWN | UNKNOWN/HOLD
F0106-TRN-01 | 課程 | 活動採購比價及核銷文件整理 | 0106 | SYN-0106-FIN-01 | T02 | 對應需求之課程型態 | 課程計畫／大綱 | UNKNOWN | UNKNOWN/HOLD
F0106-DATE-01 | 日期 | 2026-04-10 | 0106 | SYN-0106-FIN-01 | T02 | 示範排程 | 出席紀錄 | UNKNOWN | UNKNOWN/HOLD
F0106-PER-01/02 | 期間 | 2025-09-01～2026-02-28；2026-04-11～2026-10-10 | 0106 | SYN-0106-FIN-01 | T02 | 前後各 6 個月示範窗口 | 資料期間核定 | UNKNOWN | UNKNOWN/HOLD
F0106-DATE-02 | cutoff | 2026-10-15 | 0106 | SYN-0106-FIN-01 | T02 | 示範截止 | cutoff 核准 | UNKNOWN | UNKNOWN/HOLD
F0106-FIN-01～10 | 金額 | 10 組前後金額（100,000／94,000） | 0106 | SYN-0106-FIN-01 | T03 | 固定示範輸入 | 採購／會計明細＋數量規格 | UNKNOWN | UNKNOWN/HOLD
F0106-TOT-01/02 | 合計 | 100,000；94,000 | 0106 | SYN-0106-FIN-01 | T03、T05 | 由逐列加總 | 同上 | UNKNOWN | UNKNOWN/HOLD
F0106-IDX-01 | 價格指數 | 0.98（基期 1.00） | 0106 | SYN-0106-FIN-01 | T02、T03 | 標準化示範假設 | 市場價格／物價指標 | UNKNOWN | UNKNOWN/HOLD
F0106-COST-01～03 | 成本 | 4,500／1,000／2,500 | 0106 | SYN-0106-FIN-01 | T04 | 成本結構示範 | 成本原始憑證 | UNKNOWN | UNKNOWN/HOLD
F0106-COST-TOT | 成本合計 | 8,000 | 0106 | SYN-0106-FIN-01 | T04、T05 | 加總 | 同上 | UNKNOWN | UNKNOWN/HOLD
F0106-COST-04/05/06 | 非現金成本 | 志工與學員時間均未量化／不計入 | 0106 | SYN-0106-FIN-01 | T04 | 不以缺失的工時或估值資料推估 | 如正式採計須取得工時紀錄及授權估值依據並重算 ROI | UNKNOWN | UNKNOWN/HOLD
F0106-CALC-01～16 | 計算 | 見 T05 | 0106 | SYN-0106-FIN-01 | T05 | 依固定輸入推導 | 重算紀錄（雙人） | UNKNOWN | SYNTHETIC（算術）／來源 HOLD
F0106-SEN-01～06 | 敏感度 | 0.96–1.0217391 情景 | 0106 | SYN-0106-FIN-01 | T06 | 含理論臨界值的敏感度示範 | 同上 | UNKNOWN | SYNTHETIC（算術）
F0106-LRN-01 | 樣本 | SYN-L01～L10（另 2 人未回覆） | 0106 | SYN-0106-FIN-01 | T08 | 匿名代碼示範 | 完成名冊（去識別） | UNKNOWN | UNKNOWN/HOLD
F0106-SRV-01～10 | 問卷 | 見 T08 六題分數 | 0106 | SYN-0106-FIN-01 | T08 | 合成填答 | 問卷原始資料 | UNKNOWN | UNKNOWN/HOLD
F0106-SRV-TOT/AVG | 彙總 | 39/37/38/40/33/36；均值 3.9/3.7/3.8/4.0/3.3/3.6 | 0106 | SYN-0106-FIN-01 | T08 | 由明細加總 | 重算紀錄 | UNKNOWN | SYNTHETIC（算術）
F0106-SRV-RT | 回覆率 | 10÷12=83.33% | 0106 | SYN-0106-FIN-01 | T08 | 固定輸入 | 邀請與回收紀錄 | UNKNOWN | UNKNOWN/HOLD
F0106-SUM-01～06 | 題項彙總 | Q1 8/10、Q4 8/10、Q5 5/10 等 | 0106 | SYN-0106-FIN-01 | T08 | 由明細重算 | 重算紀錄 | UNKNOWN | SYNTHETIC（算術）
F0106-CUS-01/02 | 客戶 | SYN-CUST-01、C1=4 | 0106 | SYN-0106-FIN-01 | T08 | 單一個案觀點 | 客戶問卷＋同意依據 | UNKNOWN | UNKNOWN/HOLD
F0106-CONF-01～12 | 混淆因素 | 12 項未排除 | 0106 | SYN-0106-FIN-01 | T10 | 限制揭露 | 混淆因素說明文件 | UNKNOWN | UNKNOWN/HOLD
F0106-LOG-01～06 | 邏輯鏈 | ①～⑥ 證據強度 | 0106 | SYN-0106-FIN-01 | T09 | 證據分層 | 各節點對應憑證 | UNKNOWN | SYNTHETIC／多數 HOLD
F0106-ROLE-01～05 | 角色 | SYN-ROLE-01～05（承辦／財務／覆核／決策／分析） | 0106 | SYN-0106-FIN-01 | T11 | 責任分工示範 | 真實職稱與權責 | UNKNOWN | UNKNOWN/HOLD（角色虛構）
F0106-ACT-01～08 | 行動 | 8 項後續檢查 | 0106 | SYN-0106-FIN-01 | T11 | 示範排程 | 實際執行紀錄 | UNKNOWN | SYNTHETIC（未執行）
F0106-DEC-01 | 決定 | SAMPLE → 不升格；未核准 | 0106 | SYN-0106-FIN-01 | T11、T13 | 拒絕推定核准 | 權責核定文件 | UNKNOWN | UNKNOWN/HOLD（未核定）
F0106-DATE-99 | 稿件日期 | 2026-10-22 | 0106 | SYN-0106-FIN-01 | 封面 | 產稿排程 | 實際產製日期 | UNKNOWN | SYNTHETIC
F0106-SMP-01 | 樣本數 | 10 組前後配對採購籃 | 0106 | SYN-0106-FIN-01 | T02 | 固定合成輸入 | 真實採購明細與納入名冊 | UNKNOWN | UNKNOWN/HOLD
F0106-RULE-01～03 | 納入、排除與配對規則 | 同品項規格數量、窗口歸屬及排除條件 | 0106 | SYN-0106-FIN-01 | T02 | 方法示範規則 | 正式核定方法與原始明細 | UNKNOWN | UNKNOWN/HOLD
F0106-UNIT-01 | 觀察單位 | 同規格、同數量的一次採購合計 | 0106 | SYN-0106-FIN-01 | T02 | 操作定義示範 | 可追溯採購資料 | UNKNOWN | UNKNOWN/HOLD
F0106-QLT-01 | 數據品質 | 前後各 10 筆、示範無缺漏及異常值 | 0106 | SYN-0106-FIN-01 | T02 | 合成資料設定 | 原始資料完整性檢核 | UNKNOWN | UNKNOWN/HOLD
F0106-VIEW-01 | 觀察視角 | 目標客戶及學員對財務面觀察差異的認知 | 0106 | SYN-0106-FIN-01 | T01、T02、T07 | 需求範圍示範 | 有效問卷與個資處理依據 | UNKNOWN | UNKNOWN/HOLD

真實資料替換清冊（正式升格前逐列處理；目前均暫緩）

fact_id | 位置 | SYN 值 | 正式來源（最低要求） | 授權／保管位置 | 覆核角色 | 目前狀態
F0106-FIN-01～10 | T03 | 100,000／94,000 | 訓練前後可比較之採購或會計明細（含數量／規格） | 原正式保管處（不入公開庫） | 財務＋第二人 | UNKNOWN/HOLD
F0106-IDX-01 | T02、T03 | 0.98 | 市場價格或物價調整依據 | 同上 | 財務＋第二人 | UNKNOWN/HOLD
F0106-COST-01～TOT | T04 | 8,000 | 訓練直接成本原始憑證 | 同上 | 財務＋第二人 | UNKNOWN/HOLD
F0106-TRN-01、F0106-LRN-01 | T02、T08 | 12 人邀請 | 課程計畫／出席／完成名冊 | 同上 | 承辦 | UNKNOWN/HOLD
F0106-SRV-01～10、F0106-CUS-01/02 | T08 | 10＋1 份回覆 | 問卷原始資料＋同意／個資處理依據 | 同上 | 承辦＋個資窗口 | UNKNOWN/HOLD
F0106-PER-01/02、F0106-DATE-02 | T02 | SYN 期間 | 資料期間與 cutoff 核准 | 同上 | 決策角色 | UNKNOWN/HOLD
F0106-CALC-01～16、F0106-SEN-01～06 | T05、T06 | 各算式結果 | 雙人獨立重算（差額=0） | 同上 | 第二人 | UNKNOWN/HOLD
F0106-CONF-01～12 | T10 | 12 項 | 混淆因素書面說明 | 同上 | 覆核角色 | UNKNOWN/HOLD
F0106-DEC-01 | T11、T13 | 未核定 | 權責核定 | 同上 | 決策角色 | UNKNOWN/HOLD

升格規則： 上列必要來源缺一，或對帳差額不為零，一律維持 REAL=UNKNOWN/HOLD，凍結受影響財務結論；不阻擋其他不相依文件。每份真實資料保持原正式保管處；公開儲存庫僅留去識別、獲授權、可公開的摘要及替換狀態。不得上傳受限制財務或個資；不得偽造第三方證明、實際客戶評語、協會核准、財務憑證或簽名。
13. 跨文件區隔與退件／暫緩條件
13.1 與相關但不同需求的區隔

文件／項目 | 內容 | 與本件關係
0105／I18-E13／項目 114 | 調查及課後行動計畫追蹤 | 方法旁證；資料、數值、case_id、對象不得搬入本件；不可共用受訪者
0104 | 證照獲取率 | 不同證據；不得共用人數、案例 ID、分子分母或結論
0103 | 第三方感謝函 | 不同證據；不得作為財務差異來源；不得偽造第三方文件
157 項目 120（I18-L4） | 顯著組織績效問卷／行動方案量化與歸因 | 範圍較廣；本件不宣稱滿足項目 120，項目 120 內容不得移入
本件 0106／I18-E14／項目 115 | 組織績效財務效果之前後計算與限制 | 唯一範圍

遮標辨識測試： 遮住標題、封面、頁眉及通用前言後，讀者仍應辨識本件為「訓練之組織財務效果分析」；若被辨識為滿意度調查、活動核銷單、財務報表或成果宣傳稿，即屬 FAIL。
13.2 FAIL／需返工條件（任一成立即退件）
未保留負淨值（−3,918.37／−48.98%）或隱藏成本。
T05 任何算式或合計不一致（列示四捨五入 ≤ 0.05 者除外）。
問卷數與回覆率矛盾（12 邀請／10 有效／83.33%）。
改寫固定輸入（10 組金額、0.98、8,000、問卷明細）。
缺期間、單位或配對範圍。
將自陳意見當財務證據，或以財務數字「證明」感知。
使用因果字眼（造成、導致、提升了績效等）。
把合成資料寫成協會、客戶或財務真實紀錄。
與 0105／0104 共用案例、個資、人數或分子分母。
只給空白表、提綱或製作計畫，無完整已填正文。
遮標後無法辨識文件用途。
出現代簽、第三方證明、核准宣稱或真實姓名。
13.3 HOLD／REAL 不可升格條件
無獲授權帳務／採購明細、成本憑證、價格基準、有效樣本、客戶／學員原始回覆、資料期間核定或第二人重算 → REAL=UNKNOWN/HOLD；HOLD 只凍結真實財務結論，不阻擋其他文件。
13.4 衝突與不足之處理聲明
來源衝突或無佐證者一律列為 UNKNOWN/HOLD，不得推定。待補項目包括機構與角色、期間與 cutoff、金額憑證、價格指數、問卷與個資同意、混淆因素、雙人重算及權責核定。未解除前僅驗來源映射、正文、技術／數學及 SAMPLE/REAL 界線；其餘驗收與 REAL 升格仍為 UNKNOWN 或 FAIL/HOLD，不得宣稱整體 PASS。
[HEADER 0]
0106｜I18-E14｜SAMPLE / SYNTHETIC｜REAL=UNKNOWN/HOLD
[FOOTER 0]
原始點協會 TTQS ONE｜候選稿，未正式接受｜第 1 頁
