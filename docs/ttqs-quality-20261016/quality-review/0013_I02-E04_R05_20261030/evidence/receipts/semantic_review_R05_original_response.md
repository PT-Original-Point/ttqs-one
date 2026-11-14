## Verdict：PARTIAL（僅對下列 SHA）

候選 [0013_I02-E04_R05.docx](E:/TTQS/TTQS_ONE_CODEX_RUNTIME/WORK/QUALITY_REBUILD_20261016/0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029/candidate/0013_I02-E04_R05.docx) 的 SHA-256 在審查前、後均為：

`2bf0407de7f24ad580cbb39df8365cbf2bc69feef97d069575daa3012a1b16d6`

大小 65,885 bytes。全程唯讀，未修改或重建任何檔案；語意判斷依候選正文及官方來源，不採納 Builder 的 QA 自述作為接受證據。

## 逐項結果

| 項目 | 結果 | 正文定位與判斷 |
|---|---|---|
| 官方 requirement、唯一 Blueprint、source packet | **PASS** | §2.1；Table 18 rows 2–3。自行重算 source packet SHA 為 `b87440b2…bfa63`、官方 PDF SHA 為 `805386b7…34709`、Blueprint 檔 SHA 為 `406d0495…6ef3e`、0013 唯一 row SHA 為 `b529f3c1…2d35b`；原 Worker 檔 SHA 亦與 packet 記錄相符。PDF 第 1 頁文字抽取核對到官方原文「公開公布訓練機構年度訓練課程。」來源狀態可確認為 `VERIFIED_SOURCE_AND_UNIQUE_BLUEPRINT`。 |
| 要求／文件類型與實際發布證據 | **PARTIAL** | 封面、§1–2、§6、§8、§11–12；Table 16。文件是對應 I02-E04 的年度課程清單與發布證據流程工作稿，類型符合 Blueprint；但它明確是 SAMPLE，沒有真實核准或公開頁讀回，因此本件不能證明已實際公開。 |
| 標題盲辨識 | **PASS** | §1、§5–8、§11（末段標題盲說明）。即使遮蔽標題，年度公開課程欄位、核對、發布閘門及公開頁讀回程序仍可辨認本件用途。 |
| 負向鄰件區隔 | **PASS** | §3.3、§11.2 Table 17。明確區分 0012／I02-E03 的優惠制度與 0014／I02-E05 的客戶需求申請表，並列出不可誤併的工作內容。與 Blueprint 鄰件定義一致。 |
| 四門課程欄位 | **PASS** | §6.2–6.5、Tables 7–10。每門均有課程代碼及九項課程欄位；四表無空格，日期、對象、成果、內容、方式、時段、淨時數、名額及通路均有填入。 |
| 35/36 → 36/36 計算意義 | **PARTIAL** | §7.1 bullets、§5 Table 5 row 10、§4.2 Table 4、§9 Table 13 row 2。算術本身正確：35÷36＝97.2%，36÷36＝100%。但公式稱分子是「通過欄位規則且有值」；Table 5 對報名通路要求實際開啟、核對版本，且無法測試或非正式網址應 HOLD。四門示例都使用不可用的 `.invalid` 網址，因此 R-B 的 36/36 只能代表欄位有填，不能代表依已列規則通過。 |
| 淨時數與規劃名額 | **PASS** | §6 Tables 7–10、§7.2。C01/C03/C04 各 09:00–16:00 扣一小時休息＝6 小時；C02 兩日各 6 小時＝12 小時。總計 30 小時。名額 20+18+20+16＝74 席。候選清楚標示為合成規劃量，非實際授課或報名人數。 |
| 67 筆 synthetic register | **PARTIAL** | §13 Table 19。直接檢查得 67 列、67 個唯一 ID；ID 集合為 F001–F027 與 F101–F140，無重複、空白列或缺漏。各列有合成值／類型、章節定位及 REAL 替換來源／方式；但沒有逐事實的責任角色欄，且部分定位只到章節，未標到表格列／欄位。§4 Table 3、§10 Table 15 提供角色與分類責任，可供參照，但尚未逐筆連結。 |
| SAMPLE／REAL、核准及公開邊界 | **PASS** | 封面、§1、§2.2、§8、§10–12；Tables 12、14–16、20及末段交付界線。合成日期、課程、角色與不可用網址均標示；未宣稱真人核准、實際公開、報名、受訓或成果，並維持正式發布 HOLD。 |
| 索引定位 | **PASS／PARTIAL** | §2.3 Table 1、§12 Table 18：官方 PDF 第 1 頁、Blueprint 唯一 row、課程示例及缺少的核准／公開原件均有索引。R05 已將 Table 1 row 13 修正為版本在 §14、合成清冊在 §13。惟 Table 19 的部分事實定位仍較粗，見上列。 |
| 版本與交付狀態 | **PASS** | 封面、§14 Table 20、末段交付界線。正文均指向 R05 DOCX 候選、SAMPLE/SYNTHETIC、未接受且未核准／公開。R04 原審查 SHA `276434c0…a4c23` 與實際 R04 檔相符；直接比對 R04/R05 正文，舊審查指出的 source packet 敘述、R01/Markdown 交付狀態及 Table 1 row 13 定位已修正，課程與計算內容未變。 |
| 協會人員與評核委員可用性 | **PARTIAL** | §1–12 含角色分工、欄位規則、例外、更正、發布讀回及調閱流程，可作內部 SAMPLE 操作示範；但報名連結均不可用，36/36 的指標語義需釐清，逐事實責任／精確定位不足，且無實際公開原件，尚不能作為正式發布紀錄使用。 |

## QA 與視覺檢查範圍

[技術 QA 收據](E:/TTQS/TTQS_ONE_CODEX_RUNTIME/WORK/QUALITY_REBUILD_20261016/0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029/qa/technical_qa_R05.json)、[版面 QA 收據](E:/TTQS/TTQS_ONE_CODEX_RUNTIME/WORK/QUALITY_REBUILD_20261016/0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029/qa/visual_qa_R05.json)及 [Build 收據](E:/TTQS/TTQS_ONE_CODEX_RUNTIME/WORK/QUALITY_REBUILD_20261016/0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029/qa/BUILD_RECEIPT_R05.json)所列候選 SHA 均為本次 SHA。收據仍標語意審查待辦、正式接受 UNKNOWN；另 Build 收據同時寫 `visual_review=PASS_LAYOUT_ONLY` 與 `visual_status=PENDING`，彼此不一致。這是收據狀態問題，不是我接受其自述為語意 PASS。

**本次沒有做版面目視**：未打開 Word 渲染頁、PNG 或 PDF 頁面影像。版面收據聲稱 25 頁均有對應圖，直接檢查頁 1–5、25，頁 6–24 沿用 R04 視覺檢查；這只是收據記載，不是本次目視驗證。

## 最小修復建議（未執行）

1. 在 §7.1 將「欄位有填」與「欄位規則／真實通路驗證」拆開：可保留 R-B 的 36/36 作填寫率；另列四個 `.invalid` 通路均未驗證、維持 HOLD。或按目前「通過欄位規則」定義重算，不能把不可開啟的連結算作通過。
2. Table 19 增加逐事實責任角色，並將章節定位補到明確的段落、表格／欄位；特別是 F001–F027 的非課程表事實。
3. 若整理 QA 收據，對齊 Build 收據中的 `visual_review` 與 `visual_status` 欄位。正式發布證據仍須由真實核准與公開讀回原件提供，不能以合成資料替代。


