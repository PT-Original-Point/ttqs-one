# 0040 R05 獨立語意審查

**總 verdict：PARTIAL**，綁定本次直接讀取的候選 DOCX SHA-256 `95531ac5f8a79eed7c605f3ab1f42da3948e8f15316499d325b606bd6d434384`。

本次未修改或重建任何檔案，也未寫審查收據；Git worktree 審查後仍無變更。候選、PDF、清冊雜湊均與指定值相符，分別為：

- DOCX：`95531ac5f8a79eed7c605f3ab1f42da3948e8f15316499d325b606bd6d434384`
- Word PDF：`dd4d8ea87cdb8ca22ef549ef496e61a5da38ffd0720c548413895988f39daf7e`，8 頁
- 清冊：`35cdb226aa14f8b36304ed5d22031e3ccd5f1c77d98851e968f8ca64ee0e1788`
- 官方 PDF：`805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`
- 唯一 Blueprint row：`ab080a2e6d85cc13a706f0c10bda7c208ddc191a1fea20a670fd5a174ab14943`

實際核對的[候選 DOCX](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R05/candidate/0040_R05.docx>)、[Word PDF](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R05/evidence/render/candidate.pdf>)、[替換清冊](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R05/evidence/SYNTHETIC_REPLACEMENT_REGISTER_R05.csv>)、[官方來源 PDF](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R05/inputs/official_evidence_table.pdf>)、[Blueprint row](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R05/inputs/unique_blueprint_row.jsonl>)、[來源對照表](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R05/inputs/source_requirement_map.csv>)、[R04 原審查回覆](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R04/evidence/qa/0040_semantic_review_r04_crossreview_raw.md>)與[0039 R09 會議示範](<E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0040_R04/evidence/0039_R09_companion_candidate.docx>)。Repo branch/head 符合指定值：`work/ttqs-one-document-quality-contract-20261016` / `9c9bbfe537af6aecd616fcba85cfd1a10bbdb057`。

## 各項判定

| 面向 | 結果 | 正文證據與定位 |
|---|---|---|
| 官方要求、正式映射、文類 | **PASS** | 官方 PDF p.3 的要求與 DOCX p.1「官方要求（逐字引用）」相符。來源對照及 Blueprint 將 DOCX 0040 對應 I08-E03、官方序號 040；不是依 DOCX 編號推定。此件是評量方法與成效指標矩陣，p.1–2 說明它供課前設計、課後計算，會議紀錄另由配套文件呈現，沒有冒稱自己就是會議紀錄。 |
| 標題盲與鄰項區分 | **PASS** | 隱去標題後，p.1 的官方要求、評量工具用途與 K1–K4 評量內容仍能辨識為評估方法矩陣。p.2、p.8「區分相鄰工作文件」明確區分會議討論紀錄、需求調查、系統改善檢討、課程計畫。這符合 0038/I08-E02 的改善執行結果、0039/I08-E03 的會議決策紀錄、0041/I09-E01 的課程規劃用途。0038、0041 的比較依本件來源對照／Blueprint 與 R05 正文邊界核實；本次未另讀它們的候選 DOCX。 |
| 操作成熟度與欄位 | **PARTIAL** | p.1 說明使用者、使用時點、步驟與輸出；p.3 有 K1–K4 目標、工具、時點、量尺和責任；p.3 量規定義 0/1/2 分；p.4 列逐筆前後測與摘要計算；p.5 有 D04 填寫示例、缺漏及異常處理；p.6 有責任、期限、交接及結案條件；p.7–8 有工作時點操作導覽。**但 p.3 矩陣雖以「證據欄位、定位及責任」為欄名，K1–K4 實際欄值未提供可填入的原始評量證據識別碼／檔案或附件位置；p.5 D04 表也沒有該欄。** p.7–8 的「操作位置」是本工具頁碼導覽，不是原始證據位置。這使操作人員無法按本工具逐筆記錄可查證據的存放位置，與 p.1 承諾核對「證據位置」及官方「有佐證資料可查」仍有落差。 |
| 算式、門檻與資料一致 | **PASS** | p.3 規定四構面各 0–2 分、總分 0–8，四項完整、總分 ≥6/8 且 K3 ≥1 才通過；缺漏不補 0。p.3 基線 K1–K4 為 1.0、0.6、1.2、0.6，對目標 2 的差距重算為 1.0、1.4、0.8、1.4。p.4 D01–D05 前測總分 2、3、4、3、5，合計 17，平均 17/5=3.4；後測 6、7、6、5、7，合計 31，平均 31/5=6.2；配對變化 4、4、2、2、2，合計 14，平均 14/5=2.8。D01、D02、D03、D05 達標，D04 為 5/8 未達；4/5=80%。構面平均前測 1.0/0.6/1.2/0.6、後測 2.0/1.6/1.6/1.0 均重算相符；設計覆蓋率 4/4=100%，且正文正確限制為設計覆蓋，不代表學會或因果。 |
| 與 0039 R09 案例一致 | **PASS** | p.1 案例代碼 `SAMPLE-0039-01`、日期 2026-06-12；p.3 基線；p.4 D01–D05 前後測向量、門檻及結論，與 0039 R09 表03、表12–15 的合成資料一致。p.6 的 2026-06-19 是明標 SAMPLE 的 D04 待辦期限，尚未執行，並未寫成已完成結果。 |
| SAMPLE／REAL、授權與第三方界線 | **PASS** | p.1、各頁頁首及頁尾標明 SAMPLE/SYNTHETIC；p.1 說明不是協會實際調查、開課或成效；p.6 明示無實際簽到、評分、核准、課程執行或成效原件，也不製作第三方原件或真人簽名；p.7 說明未經權責人員核准或採用，不代表已辦訓或已評量。角色皆為示範職務，不冒稱真人、法人核准、第三方證明或實際成果。 |
| 替換清冊及回歸項目 | **PARTIAL** | 清冊 39 列、39 個唯一 fact_id、全欄非空；38 列為 SAMPLE/SYNTHETIC、1 列為官方來源引用且註明非協會證據；全部綁定候選 SHA。`0040-SYN-006` 已改為 p.3 計分段及 p.4 完整前後測表頭與判定欄，定位吻合；`0040-SYN-CALC-005` 已列 p.4 完整表頭、通過列及未達列，定位吻合。**`0040-SYN-009` 的 p.6 定位已補上，但 p.6 D04 表指的是 2026-06-19 的補強／重評待辦，不是 p.1 所說的「課後 30 日追蹤」；該列不能單獨證明 30 日追蹤未執行。**這個合併值仍須拆分或提供精確定位。其餘列逐筆對照正文，未見其他定位錯列。 |
| R04 的 p.7–8 缺陷回歸 | **PASS（原缺陷已解除）** | R05 p.7–8 不再列內部 DOCX／requirement／checkbox IDs、SHA、R04 審查歷史或逐事實 evaluator audit map。新版「依工作時點操作導覽」以工作步驟連到本工具頁碼，是面向使用者的操作導覽，且頁碼與步驟相符；不等同 R04 的內部逐筆證據稽核表。 |
| 頁面可讀性 | **PASS** | 直接檢視既有 PDF 與 p.1–8 八張 PNG。無空白頁、裁切或重疊；p.3–5 資訊較密但仍可讀；p.5–6 與 p.7–8 的表格續頁有可辨識欄頭，內容未被不當截斷。 |
| DOCX 版本一致性 | **PARTIAL** | DOCX ZIP 內 `docProps/core.xml` 的 description 仍寫「候選修訂 R04」，`cp:revision` 仍為 4；與本次 R05 候選身分不符。這不出現在八頁列印畫面，但 Word 文件屬性仍暴露舊版標記，需修正才能讓 R05 版本資訊一致。 |

## 阻擋完整 PASS 的具體事項

1. **補足可實際填用的證據位置欄位。** p.3 K1–K4「證據欄位、定位及責任」及 p.5 D04 表需要可記錄原始評分表／附件的識別碼或存放位置；p.7–8 的工具頁碼導覽不能代替原始證據定位。
2. **修正清冊 `0040-SYN-009` 的事實與定位邊界。** p.1 是 30 日追蹤需另行授權；p.6 是 D04 補強重評未執行。兩者是不同追蹤事項，現行合併值把 p.6 誤連成 30 日追蹤的未執行證明。
3. **更新 `docProps/core.xml` 的版本屬性。** R05 候選不應在文件屬性中仍標為 R04／revision 4。

本次語意判斷是直接閱讀 R05 候選、官方來源、唯一 Blueprint row、清冊、0039 R09 及八張現有頁面圖所得；沒有把 Builder 或技術／視覺收據當作語意證明。R04 原審查只用作回歸基線。審查任務與 Builder 回報分開，但現有資料未提供 Builder 個人身分，故不能證明個人身分層級的隔離。本結果是候選層級審查，不是升格或 Human acceptance；候選應保持 CANDIDATE。


