# W1 exact-SHA full semantic review | TTQS_ONE_0018_I03-E01_FULL_SEMANTIC_REVIEW_R21_20261125
Candidate SHA-256: 44e15653475d3f20b120e250c7c7600970390cf29176004e666726bde84cadcb
Candidate bytes: 102070
Source SHA-256: 165ad4947e734b712ff5056f7807f88b70f28f584332c0f53855e8a0c679c66a
Blueprint SHA-256: f3e12f4f0924b439ff60fdbaebae80bce524ef00394ce64db696c2a5bc05da30

Independently review the entire candidate against the authoritative source packet and dedicated Blueprint. Check requirement fit, operational completeness, consistent class/category/key references, arithmetic, SAMPLE/SYNTHETIC truth boundaries, and replacement instructions. Do not edit files. Return PASS only if no material blocker remains. Any blocker must identify exact table/record/field and evidence. Ignore non-blocking style preferences. Repeat the exact candidate SHA.

## SOURCE PACKET
# 0018 I03-E01 官方來源包 R01

## 工作定位
- work_id：TTQS_ONE_0018_I03-E01_SOURCE_PACKET_AND_BLUEPRINT_R01_20261116
- doc_id：0018；requirement_id：I03-E01
- PR #92 來源 ref：`c139d76caa033868376b2427d31f69c6166eeb46`，本次開始前已由遠端 ref 確認。
- 官方交付名稱（crosswalk）：PDDRO訓練體系圖與核心訓練類別說明。
- 成品檔名：`0018__PDDRO訓練體系圖與核心訓練類別說明.docx`。

## 官方要求與直接證據
官方查核佐證表《TTQS 人才發展品質管理系統【查核佐證文件資料表】-訓練機構版》第 1 頁，項目 3「明確的 PDDRO 訓練課程及明確的核心訓練類別」的參考佐證文字為：

> 訓練體系圖解及核心訓練類別名稱。

同列內涵說明要求展示完整教育訓練規劃，並適當反映訓練定位、發展重點及核心能力。此件只承接 I03-E01；不吸收其他要求的證明事實。本工作包允許的交叉參照僅為 I02-E05 與 I03-E02。

## 來源位元組與映射
| 來源 | ref/path | 位元組識別 |
|---|---|---|
| 官方查核佐證 PDF | PR #92 commit `c139d76caa033868376b2427d31f69c6166eeb46`；`docs/ttqs-quality-20261016/quality-review/0064_R05/official_source.pdf`，本地來源快照 `inputs/official_source.pdf` | SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`；9 頁；第 1 頁已視覺核對 |
| 官方 129→142 對照表 | 同 commit；`docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/official_129_to_142_crosswalk.csv` | SHA-256 `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`；Git Blob SHA-1 `1ac4a8419088d947947031b758e29c35a3606514` |
| 142 件專屬 Blueprint | 同 commit；`docs/ttqs-quality-20261016/quality-review/0040_R04/inputs/BLUEPRINT_CURRENT.jsonl` | SHA-256 `406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e`；Git Blob SHA-1 `cab446ede479001334289d18062e6b8bb2340dc3` |
| crosswalk 精確列 | `I03-E01,1,0,0018,PDDRO訓練體系圖與核心訓練類別說明` | 1 件，沒有拆分額外件 |
| Blueprint 精確列 | `deliverable_id=0018`、`requirement_id=I03-E01` | 原列記載專屬用途、證明角色、欄位、章節、表圖、驗證與禁造規則，見 `inputs/BLUEPRINT_CURRENT.jsonl` |

## 證明界線與樣本界線
上述官方資料只證明評核要求和 0018 對照，不證明協會已採行任何特定課程、類別、年度計畫、學員數、授課、評量結果或成效。成品應提供能操作的完整 SAMPLE/SYNTHETIC 工作示例與逐項替換清單，清楚標為 CANDIDATE、未核准、未公開；不得製造真人、核准、簽章或第三方原件。PDDRO 的英文展開若未被來源明文確認，須標示為本候選示範作業口徑，不得宣稱是協會已核定用語。

## 完整合成紀錄、欄位驗證與替換簿
示例年度 2027、全部日期、類別、班碼、人數、評分、目標、比例、角色碼及定位皆為 SAMPLE/SYNTHETIC，並非真實計畫或實績。責任碼僅為 ROLE-SAMPLE-PLAN-01、ROLE-SAMPLE-DESIGN-01、ROLE-SAMPLE-DELIVERY-01、ROLE-SAMPLE-REVIEW-01、ROLE-SAMPLE-APPROVER-01。

| 類別／合成班碼 | 日期 | 名額／錄取／出席／完成／問卷／評分總分／30日行動紀錄 |
|---|---|---|
| C01 照護理念與安全服務基礎；S18-CLS-C01-A/B | 2027-03-15、03-22 | 24／18／17／15／14／58／11 |
| C02 照護溝通與倫理應對；S18-CLS-C02-A/B | 2027-06-14、06-21 | 24／19／18／17／16／69／12 |
| C03 訓練設計與教學帶領；S18-CLS-C03-A/B | 2027-09-13、09-20 | 24／18／16／15／14／59／10 |
| C04 訓練評估與機構品質循環；S18-CLS-C04-A/B | 2027-11-08、11-15 | 24／17／15／13／10／42／8 |
| 合計 | 8 班、每班 12 個示範名額 | 96／72／66／60／54／228／41 |

可重算指標：名額填充 72/96=75.00%；出席 66/72=91.67%；完成 60/66=90.91%；問卷回收 54/60=90.00%；反應均分 228/54=4.22/5；30日行動記錄 41/60=68.33%。樣本目標為 4.00/5 與 80.00%；行動記錄比樣本目標低 11.67 個百分點。例外 EX-SYN-01：檢視追蹤記錄回收並把結果輸入下一輪計畫；ROLE-SAMPLE-REVIEW-01 負責；狀態 PROPOSED_NOT_EXECUTED，未宣稱已執行。

| 合成鍵 | 登錄事實 | REAL 替換原件／責任 |
|---|---|---|
| S18-SYN-01 | 2027 示範年度及八個日期 | 核准年度計畫、真實日期／計畫管理者 |
| S18-SYN-02 | C01–C04 名稱、代碼與定位 | 現行核准分類表／制度管理者 |
| S18-SYN-03 | 八個 S18-CLS 班碼、每班 12 名額 | 核准課程計畫及班級清冊／課程承辦人 |
| S18-SYN-04 | 五個 ROLE-SAMPLE 角色碼 | 現行權責與指派紀錄／主管 |
| S18-SYN-05 | 四列七項計數及合計 | 報名、出席、完成、問卷與追蹤原件／資料責任人 |
| S18-SYN-06 | 評分總分 58/69/59/42、合計 228、量尺 5 | 原始問卷、量尺與計算底稿／評量責任人 |
| S18-SYN-07 | 比率、4.00/5 與 80.00% 樣本門檻、11.67pp 差距 | 真實分子分母和核定門檻／分析覆核者 |
| S18-SYN-08 | EX-SYN-01 提案及未執行狀態 | 真實缺失、決議與執行證據／有權責任人 |
| S18-SYN-09 | SAMPLE://0018/I03-E01/2027/ 虛構定位 | 真實附件路徑、版次與 SHA／檔案管理者 |

必填紀錄欄含 record_id、SAMPLE 標籤、日期／版次、requirement_id、原文、類別碼／名稱、節點、輸入／活動／輸出、責任碼、來源定位、分子／分母／單位、判定／理由、覆核／行動、例外碼、保存規則與 replacement_key。例外追加記錄原值、原因、修正、覆核者、附件 SHA 和狀態。保存年限與真實制度來源未提供，標 UNKNOWN。

本件僅交叉參照 I02-E05（對外揭露邊界）與 I03-E02（相鄰獨立證據邊界）；均不代替本件圖解或類別清單。

## DEDICATED BLUEPRINT
# 0018 I03-E01 專屬 Blueprint R01

## 身分與範圍
- `doc_id=0018`；`requirement_id=I03-E01`；專屬文類：PDDRO訓練體系圖與核心訓練類別說明之專屬佐證紀錄。
- 唯一直接焦點：訓練體系圖解及核心訓練類別名稱；規劃須反映候選機構定位、發展重點、核心能力與課程之連結。
- 邊界：交叉參照僅允許 I02-E05 與 I03-E02；不複製其正文或吸收其事實。

## 成品的必要結構
1. 文件目的、責任角色、適用範圍和 CANDIDATE/SAMPLE 標示。
2. 官方原句、來源頁次及要求到成品證據位置的追溯表。
3. PDDRO 五階段關係圖／流程表，逐階段列輸入、工作、輸出、責任與留下的證據；PDDRO 英文展開未獲來源直接證實時，標示為示範口徑。
4. 核心訓練類別矩陣：類別代碼、定位、核心能力、對象、可觀察目標、課程主題、方法、評量、預期證據。
5. SAMPLE/SYNTHETIC 年度訓練體系及完整填寫案例；有時程、容量、責任角色、計算和成效判讀，非空白範本。
6. 來源／欄位／填寫者／驗證規則字典與附件定位。
7. 完整合成紀錄、例外與更正追蹤、覆核步驟、版本／保管／調閱規則。
8. 真實資料替換清單：每個需改用真實資料的欄位列明必要合法來源、責任、核驗步驟；不得留下無說明空格。

## 固定合成資料（全部須逐項登錄為 SAMPLE/SYNTHETIC）
- 示範規劃年度 `2027`；只為示範，不是協會既定年度計畫。
- 四個示範核心類別：C01 照護理念與安全服務基礎；C02 照護溝通與倫理應對；C03 訓練設計與教學帶領；C04 訓練評估與機構品質循環。不得聲稱這是協會現行課程目錄。
- 每一類兩個示範班次、每班 12 個示範名額：共 8 班、96 個名額。
- 示範班期：C01 2027-03-15/2027-03-22；C02 2027-06-14/2027-06-21；C03 2027-09-13/2027-09-20；C04 2027-11-08/2027-11-15。均為計畫示例日期。
- 每類依序使用（名額/錄取/出席/完成/問卷回收/評分總分/30 日行動紀錄數）：C01 `(24/18/17/15/14/58/11)`；C02 `(24/19/18/17/16/69/12)`；C03 `(24/18/16/15/14/59/10)`；C04 `(24/17/15/13/10/42/8)`。
- 總計 `(96/72/66/60/54/228/41)`；名額填充率 `72÷96=75.00%`；出席率 `66÷72=91.67%`；完成率 `60÷66=90.91%`；問卷回收率 `54÷60=90.00%`；加權反應均分 `228÷54=4.22/5`；30日行動紀錄率 `41÷60=68.33%`。
- 目標示例：反應均分至少 `4.00/5`；30日行動紀錄率至少 `80.00%`。後者的示範結果低於目標 `11.67` 個百分點，必須記錄一項具責任角色和期限的改善行動，不能宣稱真實改善已發生。
- 角色僅用虛構代碼 `ROLE-SAMPLE-PLAN-01`、`ROLE-SAMPLE-DESIGN-01`、`ROLE-SAMPLE-DELIVERY-01`、`ROLE-SAMPLE-REVIEW-01`、`ROLE-SAMPLE-APPROVER-01`；不得放真人姓名或冒稱批准。

## 完整度／數學驗收
- 表格總數逐欄等於四個類別合計；8 班×12 名額=96。
- 所有比例明列分子、分母、單位、期間、四捨五入；同一數值跨摘要、表格和結論完全一致。
- 評量資料只示範程序。分清名額、錄取、出席、完成、問卷、評分和 30 日行動紀錄的母數。
- 每一合成日期、角色、課程名稱、名額、計數、評分和目標均有合成事實 ID 和替換來源。
- 例外示例限於合成數據：30日行動紀錄率未達示範目標；指定追查證據、責任角色、完成期限、覆核條件與回寫 Plan 的欄位，不把未執行的行動寫成已完成。
- 禁止：空白考卷、只列大綱、待填式大段佔位、虛構正式核准／第三方原件／真實辦訓／成效；不可使用同類 peer DOCX 正文或表格作模板。

## 專屬合成替換簿與追溯欄
Writer 只用來源包已登錄的固定示例資料，不另造日期、類別、班碼、角色、人數、評分、目標或結果。替換鍵 S18-SYN-01 至 S18-SYN-09 對應來源包逐項登錄的值、文件定位和 REAL 替換原件。正文逐項標 SAMPLE/SYNTHETIC；沒有核准分類表、實施課程與評量原件、正式角色指派或附件定位時均標 UNKNOWN。紀錄 schema 至少含 record_id、狀態、日期、版本、requirement_id、官方原文、類別碼／名稱、節點、輸入／活動／輸出、責任碼、班碼、分子／分母／單位、判定／理由、覆核、行動、例外碼、附件定位、retention_rule 與 replacement_key。

## COMPLETE CANDIDATE TEXT
[PARA 1] PDDRO訓練體系圖與核心訓練類別說明
[PARA 2] 文件編號：0018
[PARA 3] 指標項目：I03-E01
[PARA 4] 文類屬性：專屬佐證紀錄
[PARA 5] 文件版本：第 1.0 版（CANDIDATE 候選樣本）
[PARA 6] 管制狀態：範例候選稿／未正式核准／未對外發布
[PARA 7] 基準年度：2027 示範年度
[PARA 9] 1. 文件目的、適用範圍、責任角色與候選樣本聲明
[PARA 10] 1.1 文件目的與制度定位
[PARA 11] 本文件係依據勞動部勞動力發展署「人才發展品質管理系統（TTQS）訓練機構版」評核標準指標 3（明確的 PDDRO 訓練課程及明確的核心訓練類別）之第一項佐證要求「訓練體系圖解及核心訓練類別名稱」所制定之專屬佐證規範。其核心宗旨為建立一套兼具策略性、系統性與可操作性之教育訓練發展架構，透過系統化之圖解與分類機制，具體呈現機構之辦訓定位、年度策略發展焦點、組織核心能力以及各職能訓練類別間之結構性連動關係，使評核委員及內部管制作業人員均能清晰查核訓練流程之邏輯性與嚴密性。
[PARA 12] 1.2 適用範圍與邊界聲明
[PARA 13] 本文件之適用範圍嚴格受限於 TTQS 指標 3 查核佐證表第 1 頁第一項（I03-E01）所規範之「訓練體系圖解及核心訓練類別名稱」專屬佐證範疇。本文件僅負責定義訓練體系架構圖、PDDRO 階段作業循環標準、四大核心訓練類別矩陣、示範年度開班配置規劃與模擬營運數據稽核模型。
[PARA 14] 本件只承接 I03-E01；允許的交叉參照僅為 I02-E05（對外揭露邊界）與 I03-E02（相鄰獨立證據邊界）。不複製其他文件正文，也不把其事實據為本件。
[PARA 15] 1.3 組織責任角色定義
[PARA 16] 為確保本訓練體系運作符合職能分工與品質稽核軌跡，本文件全篇採用標準化虛擬角色代碼，嚴禁使用任何真實個人姓名。各角色權責定義如下：
[PARA 17] ROLE-SAMPLE-PLAN-01（規劃人員）：負責年度訓練需求分析、訓練體系圖維護、年度示範計畫擬定、開班容量配置及預算參數之建立。
[PARA 18] ROLE-SAMPLE-DESIGN-01（設計人員）：負責各核心訓練類別之課程架構展開、教學目標與評量機制設計、教材教案審查與師資基準設定。
[PARA 19] ROLE-SAMPLE-DELIVERY-01（執行人員）：負責招生作業執行、學員資格檢核、課堂出缺勤控管、教學現場支援及滿意度問卷發放與回收。
[PARA 20] ROLE-SAMPLE-REVIEW-01（查核人員）：負責出勤率、結訓率、滿意度分數與行動紀錄等數據之稽核計算、異常指標分析及提出改善建議。
[PARA 21] ROLE-SAMPLE-APPROVER-01（核准權限）：負責品質手冊及重大制度架構之形式審定、年度教育訓練示範框架之合規核可，本角色於本候選稿僅具流程位置，不代表真實簽核。
[PARA 22] 1.4 CANDIDATE 候選樣本與非真實資料防偽嚴正聲明
[PARA 23] 本文件所載之所有內容，包括但不限於 2027 示範年度、四大核心訓練類別名稱、各類別課程代碼、授課日期、招生名額、錄取人數、出席人數、結訓人數、問卷評分及 30 日行動紀錄等，均為作為展示系統化作業機制之「合成示範數據（Synthetic Candidate Data）」。本文件為尚未正式發布、尚未正式簽核之候選樣本文件（Unpublished Candidate）。
[PARA 24] 本文件嚴正聲明：
[PARA 25] 本文件不代表機構過去或現在之真實開課清冊、真實學員名單、真實簽到紀錄或真實滿意度成績。
[PARA 26] 本文件所載之任何日期、數據、比例及示範成效，均係依照指定之嚴密數學模型推導建置，絕無任何向政府機關、評核委員或社會大眾偽造營運實績之意圖。
[PARA 27] 文中所述之 PDDRO 流程名詞（Plan-規劃、Design-設計、Do-執行、Review-查核、Outcome-成果）係作為本候選樣本之示範性作業口徑與流程映射模型，非指官方標準已唯一僵化限定此等英文字詞之解釋，實際評核仍以主管機關現行有效之正式規範文字為準。
[PARA 29] 2. 官方要求追溯與佐證定位表
[PARA 30] 2.1 官方規範來源與比對基準
[PARA 31] 依據勞動力發展署發布之《TTQS 人才發展品質管理系統【查核佐證文件資料表】-訓練機構版》第 1 頁，指標項目 3 載明之核心要求如下：
[PARA 32] 查核項目名稱：明確的 PDDRO 訓練課程及明確的核心訓練類別。
[PARA 33] 官方審查佐證參考：「訓練體系圖解及核心訓練類別名稱。」
[PARA 34] 官方同列內涵說明：展示完整教育訓練規劃，並適當反映訓練定位、發展重點及核心能力；章節映射與驗收表則為專案 Blueprint 的候選操作化展開。
[PARA 35] 本文件產出依循專案所鎖定之嚴格位元組指紋（Hash Fingerprints），確保完全追溯至官方來源，不產生內容漂移：
[PARA 36] 官方查核佐證 PDF 來源：SHA-256 雜湊值為 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709（第 1 頁指標 3 原文直接核對）。
[PARA 37] 官方 129 轉 142 條目對照表（Crosswalk）：SHA-256 雜湊值為 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679（確認條目代碼為 I03-E01,1,0,0018,PDDRO訓練體系圖與核心訓練類別說明，無拆分件）。
[PARA 38] 142 件專屬 Blueprint 基準：SHA-256 雜湊值為 406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e（定義 deliverable_id=0018 之欄位規範、防造規則與合成數據矩陣）。
[PARA 39] 本次對照基礎來源於 PR #92 commit c139d76caa033868376b2427d31f69c6166eeb46，為受控基線。
[PARA 40] 2.2 官方評核要點與本文件章節證據定位矩陣
[PARA 41] 為利逐項核對，下表把 I03-E01 唯一具名要求轉成候選文件內部檢核點；這些檢核點是專案 Blueprint 的驗收展開，不另稱官方子項。
[PARA 44] 3. PDDRO 訓練體系架構與全流程作業圖解
[PARA 45] 3.1 PDDRO 體系架構理念與五階段循環意涵
[PARA 46] 本候選架構導入 PDDRO 品質循環模式，做為辦訓全流程之核心骨架。本文件特別註記：本模型中採用 Plan（規劃）、Design（設計）、Do（執行）、Review（查核）、Outcome（成果）之五階段英文展開與作業定義，為本候選文件體系之示範性作業口徑，目的在落實各階段輸入與產出之結構化連結；若官方指引另有特定語意規範，則以正式公布之指引為準。
[PARA 47] 各階段之管理意涵定義如下：
[PARA 48] Plan（訓練規劃）：以機構宗旨與願景為出發點，進行年度營運發展需求調查與職能落差分析，擬定年度訓練總目標、體系架構、開班規模與預算配置。
[PARA 49] Design（課程設計）：依據規劃階段產出之核心類別，展開具體學習目標、課程綱要、教學方法、講師遴聘標準、教材編撰與評量工具設計。
[PARA 50] Do（教學執行）：落實招生宣傳、學員資格審查、教學場地配置、課堂教學實施、出缺勤管理與即時學習支援，確保課程按計畫嚴謹執行。
[PARA 51] Review（監控查核）：對執行過程之各項量化指標（招生率、出席率、結訓率、滿意度調查）進行統計稽核，辨識異常落差並分析根因。
[PARA 52] Outcome（成果評估）：追蹤學習成果轉化、產出課後 30 日行動實踐紀錄，評估行為改變與機構效益，並將評估結論回饋至次年度 Plan 階段，達成閉環改善。
[PARA 53] 3.2 PDDRO 全流程階段關係圖
[PARA 54] 本體系之階段流轉與資料回饋關係如下所示：
[PARA 55] 閉環：閉環回饋至次年度 Plan 規劃，作為下一輪訓練需求與規劃輸入。
[PARA 57] 3.3 PDDRO 各階段作業標準規範表
[PARA 58] 下表詳細定義 PDDRO 每一階段之作業標準、指定輸入要件、核心工作內容、具體產出物件、指派責任角色及候選留存證據清冊：
[PARA 61] 3.4 閉環回饋機制與持續改善連動規則
[PARA 62] 本節示範如何把查核結果回寫至規劃與設計；這是候選流程，不表示機構已有自動化系統或現行改善程序。
[PARA 63] 示範判定條件：本案例只以反應均分低於 4.00/5.00，或課後 30 日行動紀錄率低於 80.00% 作為示例品質落差。出席率及結訓率僅列示計算，不另設定未經核定的門檻。
[PARA 64] 分析與回饋：由 ROLE-SAMPLE-REVIEW-01 依機構核定的時限及程序整理異常證據，將分析結果送交 ROLE-SAMPLE-PLAN-01 與 ROLE-SAMPLE-DESIGN-01；原因在查證前均標為假設。
[PARA 65] 回饋路徑示例：
[PARA 66] 若查證顯示教學內容與工作情境不符，可評估回饋至 Design 修訂案例。
[PARA 67] 若查證顯示出席或報名流程有可改善因素，可評估回饋至 Do 調整聯繫作業。
[PARA 68] 若查證顯示目標設定或課後支持需要調整，可提出 Plan 修訂建議；是否採納須依核定程序決定。
[PARA 70] 4. 核心訓練類別矩陣與能力指標對照
[PARA 71] 4.1 核心訓練類別定位與組織發展策略
[PARA 72] 本節所列組織定位、能力與課程連結均為合成情境假設，不代表協會已核實的現行策略或課程目錄。
[PARA 73] 依官方要求呈現訓練定位、發展重點及核心能力的連結，本節以候選合成情境展示四個固定示範類別。類別名稱與定位均為 SAMPLE/SYNTHETIC，不代表協會現行課程目錄或已核定策略：
[PARA 74] C01 照護理念與安全服務基礎：示範聚焦照護理念、安全服務與風險辨識，課程主題及評量方式依候選案例設計，不宣稱為協會既有要求。
[PARA 75] C02 照護溝通與倫理應對：示範聚焦溝通、倫理情境辨識與回應，透過案例或角色演練觀察學習表現。
[PARA 76] C03 訓練設計與教學帶領：示範聚焦課程規劃、教案形成及教學活動帶領，透過教案與試教觀察呈現能力。
[PARA 77] C04 訓練評估與機構品質循環：示範聚焦辦訓資料計算、例外辨識與改善回饋；數值只使用本件登錄的合成資料。
[PARA 78] 4.2 核心訓練類別展開矩陣
[PARA 79] 下表展示四大核心訓練類別、對象、可觀察學習目標、課程主題、實施方法、評量方式與預期佐證之完整對照關係：
[PARA 82] 4.3 核心能力與評量設計對照
[PARA 83] 以下為候選評量設計示例，不預設能力編碼、合格分數、量表項數或協會現行工具；實際評量規準須依授權程序建立。
[PARA 86] 5. 2027 年度示範訓練計畫與執行數據完整工作示例
[PARA 87] 5.1 2027 年度示範計畫架構與班期配置
[PARA 88] 本候選規範以 2027 示範年度為基準，規劃四大核心訓練類別，每類別開辦 2 個示範班次，合計開辦 8 個班次。本示例依固定合成資料配置每班 12 個名額、年度共 96 個名額；此為示範容量，不推論實際品質上限。日期只表示來源包列出的合成班期，不代表機構已排定：
[PARA 90] 5.2 年度示範訓練執行數據總表
[PARA 91] 為驗證本體系數據串接之嚴密性，各類別依固定合成數據元組（名額／錄取／出席／結訓／問卷回收／評分總分／30日行動紀錄數）登錄，各欄位數值完全相符，絕無缺漏或矛盾。
[PARA 93] 5.3 綜合營運指標計算與成效判讀分析
[PARA 94] 本示範體系定義之六大綜合營運指標，嚴格依據下列指定公式進行計算，所有比率計算均四捨五入至小數點後兩位，並明列分子與分母：
[PARA 95] 名額填充率（Seat-fill Rate）：
[PARA 96] 名額填充率 = frac年度總錄取人數年度總規劃名額 × 100% = (72 ÷ 96) × 100% = 75.00%
[PARA 97] 計算說明：合成案例錄取 72 人／規劃 96 名額，填補率為 75.00%；此數值只呈現名額比例，不推論教學品質或承載上限。
[PARA 98] 學員出席率（Attendance Rate）：
[PARA 99] 學員出席率 = frac年度總出席人數年度總錄取人數 × 100% = (66 ÷ 72) × 100% = 91.67%
[PARA 100] 計算說明：合成案例出席 66／錄取 72，比例為 91.67%（66/72=0.91666...）；此計算不推論提醒機制的效果。
[PARA 101] 學員結訓率（Completion Rate）：
[PARA 102] 學員結訓率 = frac年度總結訓人數年度總出席人數 × 100% = (60 ÷ 66) × 100% = 90.91%
[PARA 103] 計算說明：合成案例完成 60／出席 66，比例為 90.91%（60/66=0.90909...）；不據此推論學習進度或真實成效。
[PARA 104] 問卷回收率（Survey Return Rate）：
[PARA 105] 問卷回收率 = frac有效問卷回收總數年度總結訓人數 × 100% = (54 ÷ 60) × 100% = 90.00%
[PARA 106] 計算說明：合成案例回收 54／完成 60，比例為 90.00%；此比例只描述問卷回收，不推論代表性或真實滿意度。
[PARA 107] 加權反應均分（Weighted Reaction Mean）：
[PARA 108] 加權反應均分 = frac滿意度評分總分有效問卷回收總數 = (228 ÷ 54) = 4.22 分（滿分 5.00 分）
[PARA 109] 計算說明：合成評分總分 228／有效問卷 54，平均為 4.22 分（228/54=4.2222...）；此數值僅為合成示例，不援引官方評等區間或宣稱協會實績。
[PARA 110] 30 日行動紀錄率（30-day Action-record Rate）：
[PARA 111] 30 日行動紀錄率 = frac30 日行動實踐紀錄數年度總結訓人數 × 100% = (41 ÷ 60) × 100% = 68.33%
[PARA 112] 成效判讀：結訓 60 人中於課後 30 日主動回傳實務工作行動紀錄表者共 41 人，實踐率為 68.33%（分母為結訓人數，41/60=0.68333...）。
[PARA 113] 5.4 成效目標差距分析與示範矯正行動計畫
[PARA 114] 本候選以 Blueprint 指定的兩項合成目標示範一次計算與回饋流程；不據此宣稱機構已實施稽核或具備既有改善績效：
[PARA 115] 目標一：學員反應評分均分（滿意度）門檻：預設目標為 ≥ 4.00 分。
[PARA 116] 實績檢驗：合成示例加權平均為 4.22 分。
[PARA 117] 示例判讀：合成數值 4.22 高於合成目標 4.00 共 0.22 分；不據此推論實際教學或師資表現。
[PARA 118] 目標二：課後 30 日工作行動紀錄實踐率門檻：預設目標為 ≥ 80.00%。
[PARA 119] 實績檢驗：示例回收率為 68.33%。
[PARA 120] 達成判定：未達目標標準。示例值（68.33%）低於示範目標（80.00%），產生具體品質落差：
[PARA 121] 目標落差差距 = 80.00% - 68.33% = 11.67 個百分點（Percentage Points）
[PARA 122] 針對此項 11.67 個百分點之品質落差，本體系落實 PDDRO 閉環精神，不隱匿缺點，嚴格依據異常處理機制建立「示範矯正與預防措施行動表（Illustrative Corrective Action Plan）」。
[PARA 123] 重要管制宣告：本表只示範如何記錄一項候選改善行動；不證明機構已具備或已執行該機制。角色、原因及作法均為合成示例，實際採用前須以資料查證並依核定程序決定；不得宣稱改善已執行或完成。
[PARA 125] 5.4.1 EX-SYN-01 例外紀錄（SAMPLE/SYNTHETIC）
[PARA 126] 此列只固定例外原值、門檻及尚未執行狀態。沒有核准決議或附件原件；矯正行動不得由本候選文字轉成已執行。
[PARA 129] 6. 資料來源、欄位定義、填寫責任與驗證字典
[PARA 130] 6.1 欄位屬性與資料驗證字典
[PARA 131] 以下為候選欄位字典示例，用於定義資料型態、來源、填寫角色及邏輯檢查；DOC-S18-* 是本候選內的合成來源索引，不表示相關原件或資訊系統已存在：
[PARA 133] 6.2 跨表一致性稽核檢查點與勾稽規則
[PARA 134] 各級數據查核人員在覆核本文件時，必須逐項執行下列 5 項剛性勾稽檢驗，若有任一項不符，本候選文卷即判定為邏輯瑕疵：
[PARA 135] 容量與名額一致性：表 5-1 班期名額總和（8 班 × 12 名額 = 96）必須等於表 5-2 規劃名額欄位總數（96）。
[PARA 136] 階梯收斂性檢驗：每一類別之數字必須嚴格滿足下列遞減或相等約束：
[PARA 137] 規劃名額 (24) ≥ 錄取人數 ≥ 出席人數 ≥ 結訓人數 ≥ 問卷回收數
[PARA 138] 且 結訓人數 ≥ 30日行動紀錄數。四類別檢驗結果完全合規：
[PARA 139] C01: 24 ≥ 18 ≥ 17 ≥ 15 ≥ 14 且 15 ≥ 11（通過）。
[PARA 140] C02: 24 ≥ 19 ≥ 18 ≥ 17 ≥ 16 且 17 ≥ 12（通過）。
[PARA 141] C03: 24 ≥ 18 ≥ 16 ≥ 15 ≥ 14 且 15 ≥ 10（通過）。
[PARA 142] C04: 24 ≥ 17 ≥ 15 ≥ 13 ≥ 10 且 13 ≥ 8（通過）。
[PARA 143] 加權均分分母勾稽：加權均分之分母必須為問卷回收數（54），不得誤植為結訓人數（60）或出席人數（66）。
[PARA 144] 行動紀錄率母數勾稽：行動紀錄率之分母必須為合格結訓人數（60），不得誤植為出席人數（66）或錄取人數（72）。
[PARA 145] 落差值精確度勾稽：成效差距計算必須剛好等於目標值（80.00%）扣除實績值（68.33%），其數值必須精確表述為 11.67 個百分點，禁止隨意捨入為 11.7% 或 12%。
[PARA 148] 7. 合成事實登錄、例外管理、覆核程序與檔案保管
[PARA 149] 7.1 合成事實代碼總表（Synthetic Fact Register）
[PARA 150] 本表一列一筆，保留原 30 項 SAMPLE 合成事實與其名稱、值、屬性及替換關係，另將 5.1 已出現的八個班碼／課名以 REC-CLS-001～008 明確登錄。欄位以四組呈現，逐列包含來源包要求的 record_id、SAMPLE 狀態、日期／版次、requirement_id／官方原文、類別碼／名稱、PDDRO、Input／Activity／Output、責任碼、來源定位、分子／分母／單位、判定／理由、覆核／行動、例外碼、保存規則與 replacement_key。所有未有真實原件支持的日期、附件 SHA、保存年限、授權與核准狀態均為 UNKNOWN；合成值只供候選示例，不構成正式紀錄。
[PARA 151] 班別紀錄｜REC-CLS-001
[PARA 152] 班別紀錄｜REC-CLS-002
[PARA 153] 班別紀錄｜REC-CLS-003
[PARA 154] 班別紀錄｜REC-CLS-004
[PARA 155] 班別紀錄｜REC-CLS-005
[PARA 156] 班別紀錄｜REC-CLS-006
[PARA 157] 班別紀錄｜REC-CLS-007
[PARA 158] 班別紀錄｜REC-CLS-008
[PARA 160] 7.2 例外事件識別、更正追蹤與偏差處理作業程序
[PARA 161] 本候選以可追溯、可隔離、可覆核的方式示範例外處理；異常門檻與時限須依機構核定程序設定，不在此虛構既有 SLA。
[PARA 162] 識別與通報：若課程執行、資料完整性或學員申訴出現足以影響判讀的異常，由執行角色記錄發現時間、事實、來源及影響範圍，按核定流程通知查核角色。
[PARA 163] 登錄與隔離：在受控紀錄中建立案件識別碼；若數據可靠性未明，標記為待查，不併入已核定統計。不得為了補齊結果而覆寫原始紀錄。
[PARA 164] 原因分析：由查核角色蒐集證據、區分事實與假設，必要時使用 5-Whys 或魚骨圖；證據不足時保留 UNKNOWN，不把假設寫成根因。
[PARA 165] 改善提案與核准：提出可檢驗的改善措施、責任角色、期限與驗證指標，送交具權限者核定後才執行。
[PARA 166] 追蹤與結案：依核定週期檢查措施證據及指標；若未達條件或證據不全，維持未結案並記錄後續處理。
[PARA 167] 7.3 多層級覆核機制與品質簽核節點
[PARA 168] 以下為候選文件採用的責任分工示例；覆核層級依機構實際授權核定，任何流程均不能保證零缺陷：
[PARA 169] 一級自主校驗（業務承辦層）：由資料產出人員（如 ROLE-SAMPLE-DELIVERY-01 於課堂結束後）針對簽到人數、問卷張數與原始評分逐一清點核算，確認無誤後於原始單據簽名（示範期間以角色代碼標註）。
[PARA 170] 二級數據勾稽（品質查核層）：由品質查核人員 ROLE-SAMPLE-REVIEW-01 依據第 6.2 節所述之 5 大勾稽檢驗規則，透過試算模型進行公式驗證，檢核四捨五入與邏輯收斂性，確認無矛盾後編制統計摘要。
[PARA 171] 三級形式核定（體系決策層）：由主管角色 ROLE-SAMPLE-APPROVER-01 檢視全案是否符合年度策略架構，確認未達標項目是否已妥善排定改善行動與回饋路徑，完成全案審定。
[PARA 172] 7.4 文件管制、保存年限與評核調閱規範
[PARA 173] 文件編號與版本受控：本文件正式編號為 0018，現行版本為 v1.0-SAMPLE。任何章節架構、指標公式或核心類別之增刪變更，均須啟動文件修訂程序，並保留版本修訂歷史對照表。
[PARA 174] 保存與調閱：保存年限、存取權限、備份與銷毀方式，須依適用規範、個資/隱私要求及機構核定的文件管制程序設定；本候選不虛構年限或特定卷宗。
[PARA 175] 評核調閱：依核定的調閱流程提供本件、體系圖及相關計算底稿；提供前確認資料來源、版本與存取權限，並依適用隱私規範遮蔽非必要個人資料。
[PARA 178] 8. 真實資料替換清單與營運轉換指引
[PARA 179] 8.1 替換清單作業說明
[PARA 180] 本章「真實資料替換清單」是候選稿的轉換控制區。來源欄列出可考慮的來源類型與核驗方法，不表示相關資料已存在，也不限制只能採用某種紙本或系統。未取得可追溯真實來源、完成核驗及必要授權前，本文件維持 CANDIDATE/SAMPLE，不得當作真實績效。
[PARA 181] 8.2 逐項欄位替換對照表
[PARA 182] 表內「內部 fact_id」為 30 項合成登錄識別碼；箭頭右側使用來源包固定的 S18-SYN-01～09 replacement_key。S18-SYN-09 的共用虛構定位為 SAMPLE://0018/I03-E01/2027/，目前沒有實體附件，故附件版次與 SHA-256 均為 UNKNOWN。以下八個 REC-CLS 記錄另外明確連結 S18-SYN-03 的班碼／課名及 S18-SYN-09 的示範定位。
[PARA 187] 8.3 後續轉換與驗收檢核清單
[PARA 188] 本清單是未來轉換工作的檢核項目，不表示目前已有真實原件、正式制度或核准。完成前，本文件維持候選標示：
[PARA 189] ☐ 候選標示與發布控制：保留 CANDIDATE、SAMPLE/SYNTHETIC 及未核准標示；只有真實來源已核驗、內容已更新且有權者依正式發布程序核准後，才可依核定文管流程調整狀態標示。
[PARA 190] ☐ 角色與責任核對：確認示範角色代碼對應到實際授權責任；只在取得任命/職務依據及必要同意後更新，不在候選文件中填入未核實個資。
[PARA 191] ☐ 來源與數據核對：依實際資料型態查驗錄取、出席、完成、問卷、評分與課後行動紀錄的來源、期間、分子、分母及版本；不預設紙本、簽名、特定系統或固定檔案櫃存在。
[PARA 192] ☐ 例外與改善核對：只有取得異常來源、原因分析與核准紀錄後，才把候選假設更新為查證結論；未執行的改善保持未執行，未達條件不得標示結案。
[PARA 193] ☐ 官方範圍對照：核對成品仍對應 I03-E01「訓練體系圖解及核心訓練類別名稱」；其他需求仍按正式 crosswalk 分件，不把本件說成 I03-E02～E04 或 I02-E05 的證明。
[PARA 194] ☐ 版本與核准：依機構正式授權流程完成內容審查、版本控制及發布核准；本候選不假定存在特定法定簽章層級或版本字串。

[TABLE 1]
[ROW 1] 本候選檢核點（依 I03-E01 操作化） || 對應重點 || 本文件對應章節 || 具體佐證圖表編號與名稱 || 查核驗證要點
[ROW 2] 檢核點 1 || 具備完整明確之 PDDRO 訓練體系圖解 || 第 3 章 || 3.2 節 圖 3-1 PDDRO 全流程階段關係圖；表 3-1 PDDRO 各階段作業標準規範表 || 檢視規劃、設計、執行、查核、成果五階段之輸入、工作、輸出與責任角色是否具備閉環管理。
[ROW 3] 檢核點 2 || 明確界定機構核心訓練類別名稱 || 第 4 章 || 表 4-1 核心訓練類別展開與策略定位矩陣 || 確認候選示例明列四個核心類別名稱；名稱不表示協會現行課程目錄。
[ROW 4] 檢核點 3 || 訓練規劃適當反映辦訓定位與發展重點 || 第 4 章 || 4.1 節 機構辦訓定位說明；表 4-1 策略定位欄 || 查核四大核心類別是否與機構照護專業、安全、教學及品質循環定位具備邏輯因果關係。
[ROW 5] 檢核點 4 || 課程規劃具體連結核心能力指標 || 第 4 章 || 表 4-2 核心能力分級與評量基準定義表 || 檢查候選矩陣是否將能力、目標及評量連結；不表示代碼為協會既有制度。
[ROW 6] 檢核點 5 || 具備可操作之完整年度教育訓練規劃與示例 || 第 5 章 || 表 5-1 2027 年度示範計畫架構表；表 5-2 年度示範訓練執行數據總表 || 查驗合成班期、96 個示範名額及計算欄位完整；不據此主張協會實際辦訓。
[ROW 7] 檢核點 6 || 建立可查證之品質異常檢討與改善機制 || 第 5 章、第 7 章 || 5.4 節 成效目標差距分析與示範矯正行動表；7.2 節 例外管理機制 || 檢視合成示例的行動紀錄率 68.33% 與示例目標差距是否計算正確、列出候選責任及未執行狀態。
[ROW 8] 檢核點 7 || 欄位定義明確、驗證規則嚴謹且具替換指引 || 第 6 章、第 8 章 || 表 6-1 欄位屬性與資料驗證字典；表 8-1 真實資料替換清單 || 查核 S18-SYN 合成事實至未來真實資料的替換來源、責任與驗證步驟。

[TABLE 2]
[ROW 1] PDDRO 階段 || 工作流程與佐證
[ROW 2] 1 · Plan 規劃 || 輸入：機構章程、策略目標、歷年評核回饋、年度職能需求調查 / 責任：ROLE-SAMPLE-PLAN-01 / 產出：年度訓練計畫書、PDDRO訓練體系圖、年度預算書、開班容量規劃 / 留存佐證：年度訓練需求分析報告、訓練體系圖核定版、開班計畫總表
[ROW 3] 2 · Design 設計 || 輸入：核心訓練類別、目標學員職能落差、能力指標 (K/S/A) / 責任：ROLE-SAMPLE-DESIGN-01 / 產出：課程規劃大綱、教學手冊、講師遴選標準表、學習成效評量工具 / 留存佐證：課程設計審查紀錄、師資資歷審核表、教材教案審定紀錄
[ROW 4] 3 · Do 執行 || 輸入：開班核准名冊、教材印製件、合格師資名冊、受訓場地確認單 / 責任：ROLE-SAMPLE-DELIVERY-01 / 產出：學員簽到退紀錄、教學日誌、課後反應問卷回收件、出勤紀錄 / 留存佐證：學員出缺勤表、實體/線上教學照片、滿意度原始問卷、結訓證明發放清冊
[ROW 5] 4 · Review 查核 || 輸入：出勤清冊、原始問卷評分數據、課堂客觀異常通報單 / 責任：ROLE-SAMPLE-REVIEW-01 / 產出：辦訓指標統計分析表、異常項目原因分析報告、教學品質稽核週報 / 留存佐證：滿意度統計分析表、異常指標落差分析表、品質稽核紀錄表
[ROW 6] 5 · Outcome 成果 || 輸入：辦訓成果統計、課後 30 日工作行動實踐紀錄表、成效評估報告 / 責任：ROLE-SAMPLE-REVIEW-01 / ROLE-SAMPLE-PLAN-01 / 產出：年度總體成效評核報告、持續改善行動方案（CAPA）、次年度訓練規劃建議書 / 留存佐證：30日實踐紀錄追蹤清冊、年度成效檢討會議紀錄、次年度規劃輸入清單

[TABLE 3]
[ROW 1] 階段代碼 || 階段名稱 || 指定輸入要件 || 核心作業標準與步驟 || 具體產出物件 || 責任角色代碼 || 必備留存佐證清冊
[ROW 2] P || 規劃 (Plan) || 1. 機構中長程策略目標 / 2. 照護從業人員職能現況 / 3. 前一年度成效回饋建議 || 1. 執行年度訓練需求調查與統計 / 2. 定義四大核心訓練類別 / 3. 擬定 8 班次開班時程與 96 名額配置 / 4. 編列各班次教學預算 || 1. 年度示範訓練計畫書 / 2. PDDRO 訓練體系結構圖 / 3. 年度資源與時程排程表 || ROLE-SAMPLE-PLAN-01 || 1. 訓練需求調查問卷分析報告 / 2. 訓練體系核定簽呈（示範用） / 3. 開班排程配置總表
[ROW 3] D || 設計 (Design) || 1. 核心訓練類別矩陣 / 2. 職能指標（K/S/A） / 3. 評量標準作業指引 || 1. 展開課程具體單元目標與大綱 / 2. 訂定授課師資專業資歷與遴聘基準 / 3. 設計教學法（講授/演練/案例） / 4. 編撰 L1 反應問卷與 L3 追蹤表 || 1. 課程標準規格書 / 2. 講師聘任檢核清單 / 3. 學習成效評量工具套件 || ROLE-SAMPLE-DESIGN-01 || 1. 課程大綱審查紀錄表 / 2. 師資審查證明文件庫 / 3. 評量工具設計審查表
[ROW 4] D || 執行 (Do) || 1. 審定課程規格書 / 2. 聘任講師合約 / 3. 報名學員資料表 || 1. 辦理招生作業與資格初審 / 2. 產出 12 名額錄取名冊並發布通知 / 3. 執行課堂簽到退與出勤登錄 / 4. 維護教學場地、設備與課室安全 / 5. 課末發放並回收 L1 評量問卷 || 1. 參訓學員報到清冊 / 2. 每日課室教學紀錄表 / 3. L1 滿意度問卷回收件 / 4. 結訓測驗評分成績單 || ROLE-SAMPLE-DELIVERY-01 || 1. 學員簽到退原始單據 / 2. 授課現場影像紀錄庫 / 3. 滿意度原始紙本/電子卷 / 4. 結訓合格證書核發清單
[ROW 5] R || 查核 (Review) || 1. 學員出勤原始單據 / 2. 滿意度原始問卷卷宗 / 3. 課室異常狀況通報 || 1. 名額填充率、出席率、結訓率 / 2. 統計問卷均分並計算加權反應分數 / 3. 查核各項數據是否符合品質閾值 / 4. 召開階段性辦訓品質檢討會議 || 1. 辦訓指標統計報表 / 2. 評量數據分析摘要 / 3. 品質異常通報與檢討表 || ROLE-SAMPLE-REVIEW-01 || 1. 各班辦訓指標計算底稿 / 2. 滿意度統計分析報告 / 3. 辦訓品質檢討會議紀錄
[ROW 6] O || 成果 (Outcome) || 1. 結訓學員合格清單 / 2. 課後 30 日工作行動實踐表 / 3. 跨階段品質查核報告 || 1. 發送並追蹤課後 30 日行動紀錄 / 2. 評估學員工作行為實踐率 / 3. 比對目標差距並分析未達標成因 / 4. 擬定具體改善行動（CAPA）方案 / 5. 彙整總體成果輸入次年規劃 || 1. 年度訓練成果總結報告 / 2. 30 日行動轉化追蹤報告 / 3. 示範矯正與預防措施單 / 4. 次年度訓練規劃修正建言 || ROLE-SAMPLE-REVIEW-01 / ROLE-SAMPLE-PLAN-01 || 1. 30 日行動紀錄追蹤清冊 / 2. 行動成效落差分析專案表 / 3. 示範矯正行動管制卡（未執行標註） / 4. 年度成果呈核簽呈（示範用）

[TABLE 4]
[ROW 1] 類別代碼 || 類別名稱 || 核心能力焦點（示例） || 對象（候選情境） || 可觀察學習表現 || 示範課程主題 || 建議教學方法 || 評量與觀察方式 || 預期留存證據（樣本）
[ROW 2] C01 || 照護理念與安全服務基礎 || 理解照護理念並辨識安全風險 || 照護服務相關學習者（示例） || 能說明安全作業原則，並在模擬情境中示範合宜處置 || 照護理念、安全服務與風險辨識 || 講授、案例與情境演練 || 依核定評量規準觀察說明與操作；本候選不另設分數門檻 || SAMPLE 課程計畫、觀察紀錄樣張
[ROW 3] C02 || 照護溝通與倫理應對 || 傾聽需求並依情境提出適切回應 || 照護服務相關學習者（示例） || 能辨識情境中的核心訴求，並提出尊重權益的回應方式 || 溝通、倫理與情境應對 || 個案研討、角色演練 || 依核定評量規準檢視情境分析與回應；本候選不另設量化門檻 || SAMPLE 案例分析、回饋紀錄樣張
[ROW 4] C03 || 訓練設計與教學帶領 || 將學習需求轉成教學活動 || 內部訓練設計相關學習者（示例） || 能形成教學活動規劃，並帶領一段與目標相符的學習活動 || 教案設計與教學帶領 || 工作坊、微型教學、同儕回饋 || 依核定評量規準檢視教案及教學觀察；本候選不另設時間或分數門檻 || SAMPLE 教學計畫、觀察紀錄樣張
[ROW 5] C04 || 訓練評估與機構品質循環 || 正確計算指標並區分事實、假設與改善提案 || 訓練規劃與品質查核相關學習者（示例） || 能重算本件合成指標、辨識 30 日行動紀錄差距，提出 EX-SYN-01 候選追蹤 || 辦訓指標、例外檢視與改善回饋 || 數據案例演算、品質議題研討 || 以分子／分母、單位、差距及證據定位核對；不作真實績效判定 || SAMPLE 計算底稿、EX-SYN-01 提案樣張

[TABLE 5]
[ROW 1] 類別代碼 || 能力構面（示例） || 行為表現 || 評量方式（示例） || 待留存證據
[ROW 2] C01 || 理解與操作 || 說明安全作業原則並示範情境處置 || 情境觀察及核定檢核規準 || 候選觀察紀錄與評量規準版本
[ROW 3] C02 || 溝通與倫理 || 辨識需求並提出合宜回應 || 案例分析及角色演練觀察 || 候選案例、觀察及回饋紀錄
[ROW 4] C03 || 設計與引導 || 形成教學活動並帶領學習 || 教案檢視及教學活動觀察 || 候選教案與觀察紀錄
[ROW 5] C04 || 計算與改善 || 重算合成指標、區分事實與假設，提出 EX-SYN-01 追蹤 || 數學勾稽與證據定位檢查 || 合成計算底稿及未執行提案

[TABLE 6]
[ROW 1] 核心類別代碼 || 示範班次代碼 || 示範課程名稱 || 示範排定開課日期 || 示範排定結訓日期 || 規劃容量名額 || 責任規劃角色 || 責任執行角色
[ROW 2] C01 || S18-CLS-C01-A || C01 照護理念與安全服務基礎示範課程 A || 2027-03-15 || 2027-03-15 || 12 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-DELIVERY-01
[ROW 3] C01 || S18-CLS-C01-B || C01 照護理念與安全服務基礎示範課程 B || 2027-03-22 || 2027-03-22 || 12 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-DELIVERY-01
[ROW 4] C02 || S18-CLS-C02-A || C02 照護溝通與倫理應對示範課程 A || 2027-06-14 || 2027-06-14 || 12 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-DELIVERY-01
[ROW 5] C02 || S18-CLS-C02-B || C02 照護溝通與倫理應對示範課程 B || 2027-06-21 || 2027-06-21 || 12 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-DELIVERY-01
[ROW 6] C03 || S18-CLS-C03-A || C03 訓練設計與教學帶領示範課程 A || 2027-09-13 || 2027-09-13 || 12 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-DELIVERY-01
[ROW 7] C03 || S18-CLS-C03-B || C03 訓練設計與教學帶領示範課程 B || 2027-09-20 || 2027-09-20 || 12 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-DELIVERY-01
[ROW 8] C04 || S18-CLS-C04-A || C04 訓練評估與機構品質循環示範課程 A || 2027-11-08 || 2027-11-08 || 12 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-DELIVERY-01
[ROW 9] C04 || S18-CLS-C04-B || C04 訓練評估與機構品質循環示範課程 B || 2027-11-15 || 2027-11-15 || 12 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-DELIVERY-01
[ROW 10] 全年度總計 || 共 4 類別 || 共 8 個示範班次 || 2027-03-15 至 2027-11-15 || -- || 96 || -- || --

[TABLE 7]
[ROW 1] 核心類別代碼 || 規劃名額 (Seats) || 錄取人數 (Admitted) || 出席人數 (Attended) || 結訓人數 (Completed) || 問卷回收數 (Surveys) || 滿意度評分總分 (Points) || 30日行動紀錄數 (Actions) || 示範數據完整元組表示 (Seats, Admitted, Attended, Completed, Surveys, Points, Actions)
[ROW 2] C01 || 24 || 18 || 17 || 15 || 14 || 58 || 11 || (24, 18, 17, 15, 14, 58, 11)
[ROW 3] C02 || 24 || 19 || 18 || 17 || 16 || 69 || 12 || (24, 19, 18, 17, 16, 69, 12)
[ROW 4] C03 || 24 || 18 || 16 || 15 || 14 || 59 || 10 || (24, 18, 16, 15, 14, 59, 10)
[ROW 5] C04 || 24 || 17 || 15 || 13 || 10 || 42 || 8 || (24, 17, 15, 13, 10, 42, 8)
[ROW 6] 年度總計 || 96 || 72 || 66 || 60 || 54 || 228 || 41 || (96, 72, 66, 60, 54, 228, 41)

[TABLE 8]
[ROW 1] 品質管理要項 || 具體管制內容與示範記錄 || 備註說明
[ROW 2] 檢驗指標名稱 || 課後 30 日工作行動實踐紀錄回收率 (30-day Action-record Rate) || 年度指標代碼：IND-S18-ACT-01
[ROW 3] 品質目標門檻 || 必須達到結訓人數之 80.00% 以上 || 目標值：≥ 80.00%
[ROW 4] 示範實績結果 || 結訓 60 人之 SAMPLE/SYNTHETIC 數據中示例回收 41 份，換算達成率為 68.33% || 落差值：差距 11.67 個百分點
[ROW 5] 待驗證原因假設（非已知事實） || 1. 可查核課後追蹤是否僅由學員自行回報，以及是否有合適的主管覆核。 / 2. 可檢視表單欄位是否造成填報負擔，須以使用者回饋或實際記錄確認。 / 3. 可查核目前是否有核定的提醒與追蹤節點；本文件不預設日期或自動化工具。 || ROLE-SAMPLE-REVIEW-01 提出查證項目；未取得證據前不判定根因
[ROW 6] 候選改善作法（須授權後採用） || 1. 依使用者回饋評估精簡行動紀錄欄位，並在試用後核對填報完整性。 / 2. 若符合實際職務與個資規範，評估加入主管覆核欄位。 / 3. 依核定流程設定提醒節點；是否採用自動化工具須另行確認。 || 候選責任：ROLE-SAMPLE-PLAN-01；協作角色：ROLE-SAMPLE-DESIGN-01
[ROW 7] 指派追蹤責任角色 || ROLE-SAMPLE-REVIEW-01（稽核追蹤）；ROLE-SAMPLE-DELIVERY-01（執行稽催） || 採雙軌分工追蹤機制
[ROW 8] 預定改善期限 || 期限由授權決策者於核准時設定並記入受控清冊；未有決議與期限紀錄前，EX-SYN-01 維持 PROPOSED_NOT_EXECUTED，不得轉入執行 || 本候選不主張已排程
[ROW 9] 覆核驗證條件 || 依核定覆核週期檢查適用資料、分子、分母及差距；達標與否均留存依據，未達核定條件不得結案。 || 本候選不預設班次數或週期
[ROW 10] 當前實施狀態標記 || 未執行（ILLUSTRATIVE CANDIDATE ONLY）：僅作為流程展示，真實改善措施尚未實施。 || 防偽控制標註，嚴禁冒稱已結案

[TABLE 9]
[ROW 1] record_id／狀態／日期版次 || requirement_id／官方原文 || 原值／目標／分子分母單位 || 原因／判定 || 修正內容／行動狀態 || 覆核者 || SAMPLE定位／附件 SHA-256 || 保存規則／replacement_key
[ROW 2] REC-EX-001／SAMPLE/SYNTHETIC／日期 UNKNOWN／版本 R04／EX-SYN-01 || I03-E01／訓練體系圖解及核心訓練類別名稱。 || 原值 41/60=68.33%；目標 80.00%；分子 41／分母 60／單位 %；差距 11.67 個百分點 || 成因 UNKNOWN；僅依 SAMPLE 數值判定低於 SAMPLE 目標，不推論真實績效 || 維持 PROPOSED_NOT_EXECUTED；未經授權決策者核定前不得執行或結案 || ROLE-SAMPLE-REVIEW-01（SAMPLE） || SAMPLE://0018/I03-E01/2027/；附件 SHA-256=UNKNOWN（無實體附件） || UNKNOWN／S18-SYN-08、S18-SYN-09

[TABLE 10]
[ROW 1] 欄位中文名稱 || 欄位英文識別碼 || 資料型態 || 合法取值範圍 || 資料來源憑證代碼 || 填寫責任角色 || 驗證責任角色 || 資料邏輯驗證規則 (Validation Rule)
[ROW 2] 核心類別代碼 || Category_Code || 文字 (String) || C01, C02, C03, C04 || DOC-S18-CAT-01 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 必須完全符合 C01 至 C04 代碼之一，不得為空白。
[ROW 3] 規劃容量名額 || Planned_Seats || 整數 (Integer) || 12 至 24 之整數 || DOC-S18-PLAN-01 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 每一班次必須固定為 12；類別小計必須為 24；全年度總計必須等於 96。
[ROW 4] 實際錄取人數 || Admitted_Count || 整數 (Integer) || 0 ≤ Count ≤ Seats || DOC-S18-ADMIT-01 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 錄取人數不得大於規劃名額（Admitted ≤ Seats）；全年度總和必須等於 72。
[ROW 5] 實際出席人數 || Attended_Count || 整數 (Integer) || 0 ≤ Count ≤ Admitted || DOC-S18-ATTEND-01 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 出席人數不得大於錄取人數（Attended ≤ Admitted）；全年度總和必須等於 66。
[ROW 6] 評量合格結訓數 || Completed_Count || 整數 (Integer) || 0 ≤ Count ≤ Attended || DOC-S18-COMP-01 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 結訓人數不得大於出席人數（Completed ≤ Attended）；全年度總和必須等於 60。
[ROW 7] 有效問卷回收數 || Survey_Returned || 整數 (Integer) || 0 ≤ Count ≤ Completed || DOC-S18-SURV-01 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 回收問卷數不得大於結訓人數（Surveys ≤ Completed）；全年度總和必須等於 54。
[ROW 8] 滿意度評分總分 || Rating_Points_Sum || 整數 (Integer) || Surveys × 1 ≤ Sum ≤ Surveys × 5 || DOC-S18-SURV-01 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 總分必須介於回收問卷數之 1 倍至 5 倍之間；全年度加總必須嚴格等於 228。
[ROW 9] 30日行動紀錄數 || Action_Record_Count || 整數 (Integer) || 0 ≤ Count ≤ Completed || DOC-S18-ACT-01 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 行動紀錄數不得大於結訓人數（Actions ≤ Completed）；全年度加總必須等於 41。
[ROW 10] 名額填充率 || Seat_Fill_Rate || 百分比 (Decimal) || 0.00% 至 100.00% || 計算欄位 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 計算公式：Admitted / Seats；年度值必須等於 75.00%。
[ROW 11] 學員出席率 || Attendance_Rate || 百分比 (Decimal) || 0.00% 至 100.00% || 計算欄位 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 計算公式：Attended / Admitted；年度值必須等於 91.67%。
[ROW 12] 學員結訓率 || Completion_Rate || 百分比 (Decimal) || 0.00% 至 100.00% || 計算欄位 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 計算公式：Completed / Attended；年度值必須等於 90.91%。
[ROW 13] 問卷回收率 || Survey_Return_Rate || 百分比 (Decimal) || 0.00% 至 100.00% || 計算欄位 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 計算公式：Surveys / Completed；年度值必須等於 90.00%。
[ROW 14] 加權反應均分 || Weighted_Reaction_Mean || 數值 (Decimal) || 1.00 至 5.00 || 計算欄位 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 計算公式：Points / Surveys；年度值必須等於 4.22。
[ROW 15] 30日行動紀錄率 || Action_Record_Rate || 百分比 (Decimal) || 0.00% 至 100.00% || 計算欄位 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 計算公式：Actions / Completed；年度值必須等於 68.33%。

[TABLE 11]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-FACT-001 / S18-SYN-001 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=示範基準年度 / 示範登錄值=2027 年度 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=營運時程 / PDDRO_node=Plan / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE） || Input=2027 年度 [SAMPLE/SYNTHETIC] / Activity=示範界定年度訓練體系之基準年度 / Output=2027 年度訓練體系示範基準設定 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-01, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-01, S18-SYN-09
[ROW 3] REC-FACT-002 / S18-SYN-002 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=核心訓練類別一 / 示範登錄值=C01 照護理念與安全服務基礎 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C01 照護理念與安全服務基礎 / 屬性分類=課程範疇 / PDDRO_node=Plan / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE） || Input=C01 照護理念與安全服務基礎 [SAMPLE/SYNTHETIC] / Activity=示範規劃核心訓練類別一之範疇名稱 / Output=C01 照護理念與安全服務基礎類別架構示範 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-02, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-02, S18-SYN-09
[ROW 4] REC-FACT-003 / S18-SYN-003 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=核心訓練類別二 / 示範登錄值=C02 照護溝通與倫理應對 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C02 照護溝通與倫理應對 / 屬性分類=課程範疇 / PDDRO_node=Plan / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE） || Input=C02 照護溝通與倫理應對 [SAMPLE/SYNTHETIC] / Activity=示範規劃核心訓練類別二之範疇名稱 / Output=C02 照護溝通與倫理應對類別架構示範 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-02, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-02, S18-SYN-09
[ROW 5] REC-FACT-004 / S18-SYN-004 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=核心訓練類別三 / 示範登錄值=C03 訓練設計與教學帶領 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C03 訓練設計與教學帶領 / 屬性分類=課程範疇 / PDDRO_node=Plan / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE） || Input=C03 訓練設計與教學帶領 [SAMPLE/SYNTHETIC] / Activity=示範規劃核心訓練類別三之範疇名稱 / Output=C03 訓練設計與教學帶領類別架構示範 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-02, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-02, S18-SYN-09
[ROW 6] REC-FACT-005 / S18-SYN-005 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=核心訓練類別四 / 示範登錄值=C04 訓練評估與機構品質循環 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C04 訓練評估與機構品質循環 / 屬性分類=課程範疇 / PDDRO_node=Plan / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE） || Input=C04 訓練評估與機構品質循環 [SAMPLE/SYNTHETIC] / Activity=示範規劃核心訓練類別四之範疇名稱 / Output=C04 訓練評估與機構品質循環類別架構示範 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-02, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-02, S18-SYN-09
[ROW 7] REC-FACT-006 / S18-SYN-006 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=示範班次容量 / 示範登錄值=每班 12 名，年度 8 班，共 96 名額 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=容量規模 / PDDRO_node=Plan / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE） || Input=每班 12 名，年度 8 班，共 96 名額 [SAMPLE/SYNTHETIC] / Activity=示範規劃年度班次容量與總名額規模 / Output=每班 12 名、年度 8 班共 96 名額容量示範清單 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-03, S18-SYN-09
[ROW 8] REC-FACT-007 / S18-SYN-007 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=C01 示範班期 / 示範登錄值=2027-03-15、2027-03-22 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C01 照護理念與安全服務基礎 / 屬性分類=授課日程 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-DESIGN-01（SAMPLE） || Input=2027-03-15、2027-03-22 [SAMPLE/SYNTHETIC] / Activity=示範編排 C01 類別之課程班期排程 / Output=S18-CLS-C01-A｜C01 照護理念與安全服務基礎示範課程 A｜2027-03-15｜2027-03-15｜12名額 [SAMPLE/SYNTHETIC]；S18-CLS-C01-B｜C01 照護理念與安全服務基礎示範課程 B｜2027-03-22｜2027-03-22｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09
[ROW 9] REC-FACT-008 / S18-SYN-008 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=C02 示範班期 / 示範登錄值=2027-06-14、2027-06-21 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C02 照護溝通與倫理應對 / 屬性分類=授課日程 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-DESIGN-01（SAMPLE） || Input=2027-06-14、2027-06-21 [SAMPLE/SYNTHETIC] / Activity=示範編排 C02 類別之課程班期排程 / Output=S18-CLS-C02-A｜C02 照護溝通與倫理應對示範課程 A｜2027-06-14｜2027-06-14｜12名額 [SAMPLE/SYNTHETIC]；S18-CLS-C02-B｜C02 照護溝通與倫理應對示範課程 B｜2027-06-21｜2027-06-21｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09
[ROW 10] REC-FACT-009 / S18-SYN-009 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=C03 示範班期 / 示範登錄值=2027-09-13、2027-09-20 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C03 訓練設計與教學帶領 / 屬性分類=授課日程 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-DESIGN-01（SAMPLE） || Input=2027-09-13、2027-09-20 [SAMPLE/SYNTHETIC] / Activity=示範編排 C03 類別之課程班期排程 / Output=S18-CLS-C03-A｜C03 訓練設計與教學帶領示範課程 A｜2027-09-13｜2027-09-13｜12名額 [SAMPLE/SYNTHETIC]；S18-CLS-C03-B｜C03 訓練設計與教學帶領示範課程 B｜2027-09-20｜2027-09-20｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09
[ROW 11] REC-FACT-010 / S18-SYN-010 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=C04 示範班期 / 示範登錄值=2027-11-08、2027-11-15 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C04 訓練評估與機構品質循環 / 屬性分類=授課日程 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-DESIGN-01（SAMPLE） || Input=2027-11-08、2027-11-15 [SAMPLE/SYNTHETIC] / Activity=示範編排 C04 類別之課程班期排程 / Output=S18-CLS-C04-A｜C04 訓練評估與機構品質循環示範課程 A｜2027-11-08｜2027-11-08｜12名額 [SAMPLE/SYNTHETIC]；S18-CLS-C04-B｜C04 訓練評估與機構品質循環示範課程 B｜2027-11-15｜2027-11-15｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09
[ROW 12] REC-FACT-011 / S18-SYN-011 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=C01 示範數據組 / 示範登錄值=(24, 18, 17, 15, 14, 58, 11) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C01 照護理念與安全服務基礎 / 屬性分類=營運指標 / PDDRO_node=Do / responsibility_code=ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=(24, 18, 17, 15, 14, 58, 11) [SAMPLE/SYNTHETIC] / Activity=示範彙整 S18-CLS-C01-A 與 S18-CLS-C01-B 之模擬執行成效數據 / Output=C01 示範數據組彙整紀錄 (24, 18, 17, 15, 14, 58, 11) (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-09
[ROW 13] REC-FACT-012 / S18-SYN-012 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=C02 示範數據組 / 示範登錄值=(24, 19, 18, 17, 16, 69, 12) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C02 照護溝通與倫理應對 / 屬性分類=營運指標 / PDDRO_node=Do / responsibility_code=ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=(24, 19, 18, 17, 16, 69, 12) [SAMPLE/SYNTHETIC] / Activity=示範彙整 S18-CLS-C02-A 與 S18-CLS-C02-B 之模擬執行成效數據 / Output=C02 示範數據組彙整紀錄 (24, 19, 18, 17, 16, 69, 12) (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-09
[ROW 14] REC-FACT-013 / S18-SYN-013 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=C03 示範數據組 / 示範登錄值=(24, 18, 16, 15, 14, 59, 10) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C03 訓練設計與教學帶領 / 屬性分類=營運指標 / PDDRO_node=Do / responsibility_code=ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=(24, 18, 16, 15, 14, 59, 10) [SAMPLE/SYNTHETIC] / Activity=示範彙整 S18-CLS-C03-A 與 S18-CLS-C03-B 之模擬執行成效數據 / Output=C03 示範數據組彙整紀錄 (24, 18, 16, 15, 14, 59, 10) (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-09
[ROW 15] REC-FACT-014 / S18-SYN-014 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=C04 示範數據組 / 示範登錄值=(24, 17, 15, 13, 10, 42, 8) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C04 訓練評估與機構品質循環 / 屬性分類=營運指標 / PDDRO_node=Do / responsibility_code=ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=(24, 17, 15, 13, 10, 42, 8) [SAMPLE/SYNTHETIC] / Activity=示範彙整 S18-CLS-C04-A 與 S18-CLS-C04-B 之模擬執行成效數據 / Output=C04 示範數據組彙整紀錄 (24, 17, 15, 13, 10, 42, 8) (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-09
[ROW 16] REC-FACT-015 / S18-SYN-015 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=年度總計數據組 / 示範登錄值=(96, 72, 66, 60, 54, 228, 41) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=營運總計 / PDDRO_node=Do / responsibility_code=ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=(96, 72, 66, 60, 54, 228, 41) [SAMPLE/SYNTHETIC] / Activity=示範彙總全年度 4 類別共 8 班期之年度模擬執行數據 / Output=年度總計示範數據組統計紀錄 (96, 72, 66, 60, 54, 228, 41) (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-09
[ROW 17] REC-FACT-016 / S18-SYN-016 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=名額填充率指標 / 示範登錄值=75.00% (72/96) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=衍生比率 / PDDRO_node=Outcome / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=75.00% (72/96) [SAMPLE/SYNTHETIC] / Activity=示範依據年度報名總數與名額計算填充率指標 / Output=名額填充率指標 75.00% (72/96) 示範成果 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=72 / denominator=96 / unit=% / judgment/reason=75.00% = 72 / 96 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 18] REC-FACT-017 / S18-SYN-017 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=學員出席率指標 / 示範登錄值=91.67% (66/72) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=衍生比率 / PDDRO_node=Outcome / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=91.67% (66/72) [SAMPLE/SYNTHETIC] / Activity=示範依據學員出席數與報名數計算出席率指標 / Output=學員出席率指標 91.67% (66/72) 示範成果 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=66 / denominator=72 / unit=% / judgment/reason=91.67% = 66 / 72 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 19] REC-FACT-018 / S18-SYN-018 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=學員結訓率指標 / 示範登錄值=90.91% (60/66) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=衍生比率 / PDDRO_node=Outcome / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=90.91% (60/66) [SAMPLE/SYNTHETIC] / Activity=示範依據學員結訓數與出席數計算結訓率指標 / Output=學員結訓率指標 90.91% (60/66) 示範成果 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=60 / denominator=66 / unit=% / judgment/reason=90.91% = 60 / 66 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 20] REC-FACT-019 / S18-SYN-019 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=問卷回收率指標 / 示範登錄值=90.00% (54/60) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=衍生比率 / PDDRO_node=Outcome / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=90.00% (54/60) [SAMPLE/SYNTHETIC] / Activity=示範依據問卷回收數與結訓數計算回收率指標 / Output=問卷回收率指標 90.00% (54/60) 示範成果 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=54 / denominator=60 / unit=% / judgment/reason=90.00% = 54 / 60 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 21] REC-FACT-020 / S18-SYN-020 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=加權反應均分指標 / 示範登錄值=4.22 分 (228/54) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=衍生數值 / PDDRO_node=Outcome / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=4.22 分 (228/54) [SAMPLE/SYNTHETIC] / Activity=示範依據問卷總分與有效份數計算加權反應均分 / Output=加權反應均分指標 4.22 分 (228/54) 示範成果 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=228 / denominator=54 / unit=分 / judgment/reason=4.22 = 228 / 54 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 22] REC-FACT-021 / S18-SYN-021 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=30日行動紀錄率 / 示範登錄值=68.33% (41/60) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=衍生比率 / PDDRO_node=Outcome / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=68.33% (41/60) [SAMPLE/SYNTHETIC] / Activity=示範依據30日行動紀錄提交數計算行動紀錄率 / Output=30日行動紀錄率指標 68.33% (41/60) 示範成果 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=41 / denominator=60 / unit=% / judgment/reason=68.33% = 41 / 60 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 23] REC-FACT-022 / S18-SYN-022 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=滿意度目標門檻 / 示範登錄值=≥ 4.00 分 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=品質閾值 / PDDRO_node=Review / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=≥ 4.00 分 [SAMPLE/SYNTHETIC] / Activity=示範設定反應評估滿意度之查核門檻基準 / Output=滿意度目標門檻 ≥ 4.00 分示範基準 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=分 / judgment/reason=門檻為 SAMPLE；不得視為已核定標準 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 24] REC-FACT-023 / S18-SYN-023 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=行動率目標門檻 / 示範登錄值=≥ 80.00% || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=品質閾值 / PDDRO_node=Review / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=≥ 80.00% [SAMPLE/SYNTHETIC] / Activity=示範設定30日行動紀錄率之查核門檻基準 / Output=行動率目標門檻 ≥ 80.00% 示範基準 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=% / judgment/reason=門檻為 SAMPLE；不得視為已核定標準 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 25] REC-FACT-024 / S18-SYN-024 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=示範品質落差值 / 示範登錄值=差距 11.67 個百分點 (80.00% - 68.33%) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=異常分析 / PDDRO_node=Review / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=差距 11.67 個百分點 (80.00% - 68.33%) [SAMPLE/SYNTHETIC] / Activity=示範比對行動率目標與實際成效以計算落差值 / Output=示範品質落差值差距 11.67 個百分點分析紀錄 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=80.00%-68.33% / denominator=UNKNOWN / unit=百分點 / judgment/reason=差距 11.67 個百分點；僅為 SAMPLE 計算 || replacement_source_keys=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09
[ROW 26] REC-FACT-025 / S18-SYN-025 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=示範矯正計畫單 / 示範登錄值=EX-SYN-01 (狀態：未執行) || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=改善管理 / PDDRO_node=Review / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=EX-SYN-01 (狀態：未執行) [SAMPLE/SYNTHETIC] / Activity=示範登錄品質落差對應之模擬矯正計畫單 / Output=示範矯正計畫單 EX-SYN-01 (狀態：未執行) (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=41 / denominator=60 / unit=% / judgment/reason=原值 68.33%，相對 SAMPLE 目標 80.00%；改善尚未執行 || replacement_source_keys=S18-SYN-07, S18-SYN-08, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核者=ROLE-SAMPLE-REVIEW-01 / 行動=待授權核定；未核准前維持未執行 / exception_code=EX-SYN-01 / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-07, S18-SYN-08, S18-SYN-09
[ROW 27] REC-FACT-026 / S18-SYN-026 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=規劃責任人員 / 示範登錄值=ROLE-SAMPLE-PLAN-01 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=人員代碼 / PDDRO_node=Plan / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE） || Input=ROLE-SAMPLE-PLAN-01 [SAMPLE/SYNTHETIC] / Activity=示範指派體系規劃階段之權責人員代碼 / Output=規劃責任人員 ROLE-SAMPLE-PLAN-01 示範配置 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-04, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-04, S18-SYN-09
[ROW 28] REC-FACT-027 / S18-SYN-027 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=設計責任人員 / 示範登錄值=ROLE-SAMPLE-DESIGN-01 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=人員代碼 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-DESIGN-01（SAMPLE） || Input=ROLE-SAMPLE-DESIGN-01 [SAMPLE/SYNTHETIC] / Activity=示範指派課程設計階段之權責人員代碼 / Output=設計責任人員 ROLE-SAMPLE-DESIGN-01 示範配置 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-04, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-04, S18-SYN-09
[ROW 29] REC-FACT-028 / S18-SYN-028 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=執行責任人員 / 示範登錄值=ROLE-SAMPLE-DELIVERY-01 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=人員代碼 / PDDRO_node=Do / responsibility_code=ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=ROLE-SAMPLE-DELIVERY-01 [SAMPLE/SYNTHETIC] / Activity=示範指派教學執行階段之權責人員代碼 / Output=執行責任人員 ROLE-SAMPLE-DELIVERY-01 示範配置 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-04, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-04, S18-SYN-09
[ROW 30] REC-FACT-029 / S18-SYN-029 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=查核責任人員 / 示範登錄值=ROLE-SAMPLE-REVIEW-01 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=人員代碼 / PDDRO_node=Review / responsibility_code=ROLE-SAMPLE-REVIEW-01（SAMPLE） || Input=ROLE-SAMPLE-REVIEW-01 [SAMPLE/SYNTHETIC] / Activity=示範指派成效查核階段之權責人員代碼 / Output=查核責任人員 ROLE-SAMPLE-REVIEW-01 示範配置 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-04, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-04, S18-SYN-09
[ROW 31] REC-FACT-030 / S18-SYN-030 / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 名稱=核准權限代碼 / 示範登錄值=ROLE-SAMPLE-APPROVER-01 || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / ALL／UNKNOWN（跨類別或非單一類別資料） / 屬性分類=人員代碼 / PDDRO_node=Plan / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE） || Input=ROLE-SAMPLE-APPROVER-01 [SAMPLE/SYNTHETIC] / Activity=示範對應體系架構之權限角色代碼（純屬範例模擬，不具實質簽核效力） / Output=核准權限代碼 ROLE-SAMPLE-APPROVER-01 示範配置 (日期 UNKNOWN, 版本 R03) [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=UNKNOWN / judgment/reason=UNKNOWN || replacement_source_keys=S18-SYN-04, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / 覆核=ROLE-SAMPLE-REVIEW-01（SAMPLE角色） / 行動=取得對應真實原件後覆核；目前不表示已實施 / exception_code=UNKNOWN / retention_rule=UNKNOWN（機構制度未提供） / replacement_key=S18-SYN-04, S18-SYN-09

[TABLE 12]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-CLS-001 / S18-CLS-C01-A / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 示範課程名稱=C01 照護理念與安全服務基礎示範課程 A / 示範班碼=S18-CLS-C01-A || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C01 照護理念與安全服務基礎 / 屬性分類=示範班碼與課名 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE）／ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=C01／C01 照護理念與安全服務基礎示範課程 A；示範日期=2027-03-15至2027-03-15；容量=12名（均為SAMPLE） / Activity=示範規劃C01類別班次與名稱；不表示正式核定或已排課 / Output=S18-CLS-C01-A｜C01 照護理念與安全服務基礎示範課程 A｜2027-03-15｜2027-03-15｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=名額／班期 / judgment/reason=示範規劃資料；REAL 替換時以正式課程清冊核實班碼與課名 || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / review=ROLE-SAMPLE-REVIEW-01（SAMPLE） / action=核對正式課程計畫及班級清冊後替換 / exception_code=UNKNOWN / retention_rule=UNKNOWN / replacement_key=S18-SYN-03

[TABLE 13]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-CLS-002 / S18-CLS-C01-B / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 示範課程名稱=C01 照護理念與安全服務基礎示範課程 B / 示範班碼=S18-CLS-C01-B || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C01 照護理念與安全服務基礎 / 屬性分類=示範班碼與課名 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE）／ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=C01／C01 照護理念與安全服務基礎示範課程 B；示範日期=2027-03-22至2027-03-22；容量=12名（均為SAMPLE） / Activity=示範規劃C01類別班次與名稱；不表示正式核定或已排課 / Output=S18-CLS-C01-B｜C01 照護理念與安全服務基礎示範課程 B｜2027-03-22｜2027-03-22｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=名額／班期 / judgment/reason=示範規劃資料；REAL 替換時以正式課程清冊核實班碼與課名 || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / review=ROLE-SAMPLE-REVIEW-01（SAMPLE） / action=核對正式課程計畫及班級清冊後替換 / exception_code=UNKNOWN / retention_rule=UNKNOWN / replacement_key=S18-SYN-03

[TABLE 14]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-CLS-003 / S18-CLS-C02-A / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 示範課程名稱=C02 照護溝通與倫理應對示範課程 A / 示範班碼=S18-CLS-C02-A || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C02 照護溝通與倫理應對 / 屬性分類=示範班碼與課名 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE）／ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=C02／C02 照護溝通與倫理應對示範課程 A；示範日期=2027-06-14至2027-06-14；容量=12名（均為SAMPLE） / Activity=示範規劃C02類別班次與名稱；不表示正式核定或已排課 / Output=S18-CLS-C02-A｜C02 照護溝通與倫理應對示範課程 A｜2027-06-14｜2027-06-14｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=名額／班期 / judgment/reason=示範規劃資料；REAL 替換時以正式課程清冊核實班碼與課名 || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / review=ROLE-SAMPLE-REVIEW-01（SAMPLE） / action=核對正式課程計畫及班級清冊後替換 / exception_code=UNKNOWN / retention_rule=UNKNOWN / replacement_key=S18-SYN-03

[TABLE 15]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-CLS-004 / S18-CLS-C02-B / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 示範課程名稱=C02 照護溝通與倫理應對示範課程 B / 示範班碼=S18-CLS-C02-B || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C02 照護溝通與倫理應對 / 屬性分類=示範班碼與課名 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE）／ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=C02／C02 照護溝通與倫理應對示範課程 B；示範日期=2027-06-21至2027-06-21；容量=12名（均為SAMPLE） / Activity=示範規劃C02類別班次與名稱；不表示正式核定或已排課 / Output=S18-CLS-C02-B｜C02 照護溝通與倫理應對示範課程 B｜2027-06-21｜2027-06-21｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=名額／班期 / judgment/reason=示範規劃資料；REAL 替換時以正式課程清冊核實班碼與課名 || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / review=ROLE-SAMPLE-REVIEW-01（SAMPLE） / action=核對正式課程計畫及班級清冊後替換 / exception_code=UNKNOWN / retention_rule=UNKNOWN / replacement_key=S18-SYN-03

[TABLE 16]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-CLS-005 / S18-CLS-C03-A / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 示範課程名稱=C03 訓練設計與教學帶領示範課程 A / 示範班碼=S18-CLS-C03-A || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C03 訓練設計與教學帶領 / 屬性分類=示範班碼與課名 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE）／ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=C03／C03 訓練設計與教學帶領示範課程 A；示範日期=2027-09-13至2027-09-13；容量=12名（均為SAMPLE） / Activity=示範規劃C03類別班次與名稱；不表示正式核定或已排課 / Output=S18-CLS-C03-A｜C03 訓練設計與教學帶領示範課程 A｜2027-09-13｜2027-09-13｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=名額／班期 / judgment/reason=示範規劃資料；REAL 替換時以正式課程清冊核實班碼與課名 || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / review=ROLE-SAMPLE-REVIEW-01（SAMPLE） / action=核對正式課程計畫及班級清冊後替換 / exception_code=UNKNOWN / retention_rule=UNKNOWN / replacement_key=S18-SYN-03

[TABLE 17]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-CLS-006 / S18-CLS-C03-B / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 示範課程名稱=C03 訓練設計與教學帶領示範課程 B / 示範班碼=S18-CLS-C03-B || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C03 訓練設計與教學帶領 / 屬性分類=示範班碼與課名 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE）／ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=C03／C03 訓練設計與教學帶領示範課程 B；示範日期=2027-09-20至2027-09-20；容量=12名（均為SAMPLE） / Activity=示範規劃C03類別班次與名稱；不表示正式核定或已排課 / Output=S18-CLS-C03-B｜C03 訓練設計與教學帶領示範課程 B｜2027-09-20｜2027-09-20｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=名額／班期 / judgment/reason=示範規劃資料；REAL 替換時以正式課程清冊核實班碼與課名 || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / review=ROLE-SAMPLE-REVIEW-01（SAMPLE） / action=核對正式課程計畫及班級清冊後替換 / exception_code=UNKNOWN / retention_rule=UNKNOWN / replacement_key=S18-SYN-03

[TABLE 18]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-CLS-007 / S18-CLS-C04-A / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 示範課程名稱=C04 訓練評估與機構品質循環示範課程 A / 示範班碼=S18-CLS-C04-A || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C04 訓練評估與機構品質循環 / 屬性分類=示範班碼與課名 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE）／ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=C04／C04 訓練評估與機構品質循環示範課程 A；示範日期=2027-11-08至2027-11-08；容量=12名（均為SAMPLE） / Activity=示範規劃C04類別班次與名稱；不表示正式核定或已排課 / Output=S18-CLS-C04-A｜C04 訓練評估與機構品質循環示範課程 A｜2027-11-08｜2027-11-08｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=名額／班期 / judgment/reason=示範規劃資料；REAL 替換時以正式課程清冊核實班碼與課名 || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / review=ROLE-SAMPLE-REVIEW-01（SAMPLE） / action=核對正式課程計畫及班級清冊後替換 / exception_code=UNKNOWN / retention_rule=UNKNOWN / replacement_key=S18-SYN-03

[TABLE 19]
[ROW 1] Record identity (record_id; fact_id; status; record_date; version; value) || Requirement/classification (requirement_id; official wording; category; PDDRO; responsibility) || Process/measures (Input; Activity; Output; numerator; denominator; unit; judgment/reason) || Traceability/control (source keys; locator; attachment SHA; review/action; exception; retention; replacement_key)
[ROW 2] REC-CLS-008 / S18-CLS-C04-B / 狀態=SAMPLE/SYNTHETIC / record_date=UNKNOWN / version=R04 / 示範課程名稱=C04 訓練評估與機構品質循環示範課程 B / 示範班碼=S18-CLS-C04-B || I03-E01 / 訓練體系圖解及核心訓練類別名稱。 / C04 訓練評估與機構品質循環 / 屬性分類=示範班碼與課名 / PDDRO_node=Design / responsibility_code=ROLE-SAMPLE-PLAN-01（SAMPLE）／ROLE-SAMPLE-DELIVERY-01（SAMPLE） || Input=C04／C04 訓練評估與機構品質循環示範課程 B；示範日期=2027-11-15至2027-11-15；容量=12名（均為SAMPLE） / Activity=示範規劃C04類別班次與名稱；不表示正式核定或已排課 / Output=S18-CLS-C04-B｜C04 訓練評估與機構品質循環示範課程 B｜2027-11-15｜2027-11-15｜12名額 [SAMPLE/SYNTHETIC] / numerator=UNKNOWN / denominator=UNKNOWN / unit=名額／班期 / judgment/reason=示範規劃資料；REAL 替換時以正式課程清冊核實班碼與課名 || replacement_source_keys=S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 / source_locator=SAMPLE://0018/I03-E01/2027/ / attachment_SHA256=UNKNOWN / review=ROLE-SAMPLE-REVIEW-01（SAMPLE） / action=核對正式課程計畫及班級清冊後替換 / exception_code=UNKNOWN / retention_rule=UNKNOWN / replacement_key=S18-SYN-03

[TABLE 20]
[ROW 1] 內部合成 fact_id／來源包 replacement_key || 待替換欄位名稱 || 當前示範登錄值 (SAMPLE) || 可核對來源類型（依核定治理方式；非既存事實） || 替換執行角色 || 轉換審核角色 || 正式抽換核驗步驟與判定標準 || 當前管制狀態標註
[ROW 2] S18-SYN-001 → S18-SYN-01, S18-SYN-09 || 訓練基準年度 || 2027 年度 || 機構理事會或最高行政會議核定之年度營運計畫書編號與公文。 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-APPROVER-01 || 查驗公文發文字號，確認計畫實施期程與年度預算書一致。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 3] S18-SYN-002 → S18-SYN-02, S18-SYN-09 || 核心訓練類別一 || C01 照護理念與安全服務基礎 || 依據年度職能分析產出並經訓練委員會審定之第 1 類正式類別名稱。 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 查對委員會會議紀錄與簽名出席清冊，核對課程範疇與定位。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 4] S18-SYN-003 → S18-SYN-02, S18-SYN-09 || 核心訓練類別二 || C02 照護溝通與倫理應對 || 依據年度職能分析產出並經訓練委員會審定之第 2 類正式類別名稱。 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 查對委員會會議紀錄與簽名出席清冊，核對課程範疇與定位。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 5] S18-SYN-004 → S18-SYN-02, S18-SYN-09 || 核心訓練類別三 || C03 訓練設計與教學帶領 || 依據年度職能分析產出並經訓練委員會審定之第 3 類正式類別名稱。 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 查對委員會會議紀錄與簽名出席清冊，核對課程範疇與定位。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 6] S18-SYN-005 → S18-SYN-02, S18-SYN-09 || 核心訓練類別四 || C04 訓練評估與機構品質循環 || 依據年度職能分析產出並經訓練委員會審定之第 4 類正式類別名稱。 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 查對委員會會議紀錄與簽名出席清冊，核對課程範疇與定位。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 7] S18-SYN-006 → S18-SYN-03, S18-SYN-09 || 班次容量規模 || 8 班次，每班 12 名，共 96 名額 || 正式招生簡章、教室立案容留人數及講師授課師生比核定表。 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 現場測量並核對工安申報容留證明，確認開班人數合法合規。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 8] S18-SYN-007 → S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 || C01 開班日程 || 2027-03-15、2027-03-22 || 正式行事曆公告、場地租借契約及講師確認聘函。 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-PLAN-01 || 檢驗場地租約起訖日、外部講師課表回條與官網開課公告。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 9] S18-SYN-008 → S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 || C02 開班日程 || 2027-06-14、2027-06-21 || 正式行事曆公告、場地租借契約及講師確認聘函。 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-PLAN-01 || 檢驗場地租約起訖日、外部講師課表回條與官網開課公告。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 10] S18-SYN-009 → S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 || C03 開班日程 || 2027-09-13、2027-09-20 || 正式行事曆公告、場地租借契約及講師確認聘函。 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-PLAN-01 || 檢驗場地租約起訖日、外部講師課表回條與官網開課公告。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 11] S18-SYN-010 → S18-SYN-01, S18-SYN-02, S18-SYN-03, S18-SYN-09 || C04 開班日程 || 2027-11-08、2027-11-15 || 正式行事曆公告、場地租借契約及講師確認聘函。 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-PLAN-01 || 檢驗場地租約起訖日、外部講師課表回條與官網開課公告。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 12] S18-SYN-011 → S18-SYN-05, S18-SYN-06, S18-SYN-09 || C01 數據元組 || (24, 18, 17, 15, 14, 58, 11) || C01 實體簽到簿正本、及格評分表、問卷紙本與 30 日追蹤卡。 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 依核定來源核對計數、分子分母及資料間一致性，不要求額外個人簽名。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 13] S18-SYN-012 → S18-SYN-05, S18-SYN-06, S18-SYN-09 || C02 數據元組 || (24, 19, 18, 17, 16, 69, 12) || C02 實體簽到簿正本、及格評分表、問卷紙本與 30 日追蹤卡。 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 依核定來源核對計數、分子分母及資料間一致性，不要求額外個人簽名。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 14] S18-SYN-013 → S18-SYN-05, S18-SYN-06, S18-SYN-09 || C03 數據元組 || (24, 18, 16, 15, 14, 59, 10) || C03 實體簽到簿正本、及格評分表、問卷紙本與 30 日追蹤卡。 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 依核定來源核對計數、分子分母及資料間一致性，不要求額外個人簽名。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 15] S18-SYN-014 → S18-SYN-05, S18-SYN-06, S18-SYN-09 || C04 數據元組 || (24, 17, 15, 13, 10, 42, 8) || C04 實體簽到簿正本、及格評分表、問卷紙本與 30 日追蹤卡。 || ROLE-SAMPLE-DELIVERY-01 || ROLE-SAMPLE-REVIEW-01 || 依核定來源核對計數、分子分母及資料間一致性，不要求額外個人簽名。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 16] S18-SYN-015 → S18-SYN-05, S18-SYN-06, S18-SYN-09 || 年度總計數據組 || (96, 72, 66, 60, 54, 228, 41) || 全年度四大類別原始佐證彙整清冊及年度辦訓總決算報告。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 執行電腦試算表加總查核，驗算總和數值與各分班清冊一致。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 17] S18-SYN-016 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 名額填充率 || 75.00% || 可追溯的核定報名紀錄或系統匯出（依實際來源）。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 驗算錄取人次與名額容量比值，確認報名繳費單據齊全。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 18] S18-SYN-017 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 學員出席率 || 91.67% || 門禁打卡、線上登入系統日誌或實體簽到清冊彙整底稿。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 驗證缺席假單、請假補課紀錄與實際在席人數完全相符。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 19] S18-SYN-018 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 學員結訓率 || 90.91% || 正式成績考核登錄清冊與結訓證書核發存根聯底冊。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 查對授課講師親筆批改之試卷及格標準，證書編號連續完整。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 20] S18-SYN-019 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 問卷回收率 || 90.00% || 可追溯的問卷回收紀錄或核定資料匯出（依實際來源）。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 核對問卷回收、適用對象及班次標記是否一致；不自行設定時間門檻或推定未代填。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 21] S18-SYN-020 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 加權反應均分 || 4.22 分 || 可重算的評分明細、量尺定義及計算底稿（依實際來源）。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 重新匯入問卷原始資料重新執行均值計算，驗收四捨五入值。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 22] S18-SYN-021 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 30日行動紀錄率 || 68.33% || 實際回收之「課後 30 日工作行動實踐表」正本簽名歸檔清單。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 抽檢實踐內容是否包含具體個案照護行為，確認主管評語無偽。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 23] S18-SYN-022 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 滿意度目標門檻 || ≥ 4.00 分 || 機構正式品質手冊（QM）所載之年度教育訓練服務品質水準。 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-APPROVER-01 || 查驗品質管理審查會議紀錄與品質手冊當前有效版本條文。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 24] S18-SYN-023 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 行動率目標門檻 || ≥ 80.00% || 機構正式品質手冊（QM）所載之學習成效轉化管理標準。 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-APPROVER-01 || 查驗品質管理審查會議紀錄與品質手冊當前有效版本條文。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 25] S18-SYN-024 → S18-SYN-05, S18-SYN-06, S18-SYN-07, S18-SYN-09 || 示範品質落差值 || 差距 11.67 個百分點 || 正式品質稽核年報所載之指標異常分析章節。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-PLAN-01 || 審核落差分析數據，確認計算依據為真實目標值與真實實績。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 26] S18-SYN-025 → S18-SYN-07, S18-SYN-08, S18-SYN-09 || 示範矯正計畫單 || EX-SYN-01 || 經有權角色核定的改善紀錄與驗證證據（如適用）。 || ROLE-SAMPLE-REVIEW-01 || ROLE-SAMPLE-APPROVER-01 || 查驗真實 CAPA 單之實施證據、照片、修改後表單及改善後驗收成效。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 27] S18-SYN-026 → S18-SYN-04, S18-SYN-09 || 規劃責任人員代碼 || ROLE-SAMPLE-PLAN-01 || 實際承辦訓練規劃之專責人員真實姓名、職稱與人事派令。 || ROLE-SAMPLE-APPROVER-01 || ROLE-SAMPLE-APPROVER-01 || 核對必要的任用或職務指派來源及授權範圍；僅處理完成核驗所需資料。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 28] S18-SYN-027 → S18-SYN-04, S18-SYN-09 || 設計責任人員代碼 || ROLE-SAMPLE-DESIGN-01 || 實際承辦課程設計之專業人員或外部顧問真實姓名、聘任合約。 || ROLE-SAMPLE-APPROVER-01 || ROLE-SAMPLE-APPROVER-01 || 核對適用的資格依據、職務範圍及授權成果紀錄；不收集無關個資。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 29] S18-SYN-028 → S18-SYN-04, S18-SYN-09 || 執行責任人員代碼 || ROLE-SAMPLE-DELIVERY-01 || 實際負責課務現場執行之專員真實姓名、職稱及排班表。 || ROLE-SAMPLE-APPROVER-01 || ROLE-SAMPLE-APPROVER-01 || 依核定資料治理方式核對執行紀錄、版本及來源一致性。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 30] S18-SYN-029 → S18-SYN-04, S18-SYN-09 || 查核責任人員代碼 || ROLE-SAMPLE-REVIEW-01 || 機構品保專員或內部稽核主管之真實姓名、內部稽核員證書。 || ROLE-SAMPLE-APPROVER-01 || ROLE-SAMPLE-APPROVER-01 || 核對查核授權、適用的利益衝突管理方式及實際覆核紀錄。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）
[ROW 31] S18-SYN-030 → S18-SYN-04, S18-SYN-09 || 核准權限代碼 || ROLE-SAMPLE-APPROVER-01 || 依機構核定權限建立的正式簽核紀錄（來源樣例，不表示已有該記錄）。 || ROLE-SAMPLE-APPROVER-01 || ROLE-SAMPLE-APPROVER-01 || 依機構核定授權及版本發布紀錄核對；本候選不預設特定印章或法定文件。 || UNKNOWN（目前無真實原件；僅 SAMPLE/SYNTHETIC，待取得受控 REAL 原件後核對）

[TABLE 21]
[ROW 1] 內部合成 fact_id／來源包 replacement_key || 待替換欄位名稱 || 當前示範登錄值 (SAMPLE) || 可核對來源類型（依核定治理方式；非既存事實） || 替換執行角色 || 轉換審核角色 || 正式抽換核驗步驟與判定標準 || 當前管制狀態標註
[ROW 2] REC-CLS-001／S18-CLS-C01-A → S18-SYN-03、S18-SYN-09 || C01 示範班碼與示範課名 || S18-CLS-C01-A；C01 照護理念與安全服務基礎示範課程 A；2027-03-15 至 2027-03-15；12 名 [SAMPLE/SYNTHETIC] || 核准課程計畫及班級清冊／課程承辦人 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 以核准課程計畫與班級清冊核對班碼、名稱、日期和每班容量；未取得原件前標 UNKNOWN，不據本樣本認定已開課。 || UNKNOWN（目前無真實原件；SAMPLE/SYNTHETIC）
[ROW 3] REC-CLS-002／S18-CLS-C01-B → S18-SYN-03、S18-SYN-09 || C01 示範班碼與示範課名 || S18-CLS-C01-B；C01 照護理念與安全服務基礎示範課程 B；2027-03-22 至 2027-03-22；12 名 [SAMPLE/SYNTHETIC] || 核准課程計畫及班級清冊／課程承辦人 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 以核准課程計畫與班級清冊核對班碼、名稱、日期和每班容量；未取得原件前標 UNKNOWN，不據本樣本認定已開課。 || UNKNOWN（目前無真實原件；SAMPLE/SYNTHETIC）
[ROW 4] REC-CLS-003／S18-CLS-C02-A → S18-SYN-03、S18-SYN-09 || C02 示範班碼與示範課名 || S18-CLS-C02-A；C02 照護溝通與倫理應對示範課程 A；2027-06-14 至 2027-06-14；12 名 [SAMPLE/SYNTHETIC] || 核准課程計畫及班級清冊／課程承辦人 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 以核准課程計畫與班級清冊核對班碼、名稱、日期和每班容量；未取得原件前標 UNKNOWN，不據本樣本認定已開課。 || UNKNOWN（目前無真實原件；SAMPLE/SYNTHETIC）

[TABLE 22]
[ROW 1] 內部合成 fact_id／來源包 replacement_key || 待替換欄位名稱 || 當前示範登錄值 (SAMPLE) || 可核對來源類型（依核定治理方式；非既存事實） || 替換執行角色 || 轉換審核角色 || 正式抽換核驗步驟與判定標準 || 當前管制狀態標註
[ROW 2] REC-CLS-004／S18-CLS-C02-B → S18-SYN-03、S18-SYN-09 || C02 示範班碼與示範課名 || S18-CLS-C02-B；C02 照護溝通與倫理應對示範課程 B；2027-06-21 至 2027-06-21；12 名 [SAMPLE/SYNTHETIC] || 核准課程計畫及班級清冊／課程承辦人 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 以核准課程計畫與班級清冊核對班碼、名稱、日期和每班容量；未取得原件前標 UNKNOWN，不據本樣本認定已開課。 || UNKNOWN（目前無真實原件；SAMPLE/SYNTHETIC）
[ROW 3] REC-CLS-005／S18-CLS-C03-A → S18-SYN-03、S18-SYN-09 || C03 示範班碼與示範課名 || S18-CLS-C03-A；C03 訓練設計與教學帶領示範課程 A；2027-09-13 至 2027-09-13；12 名 [SAMPLE/SYNTHETIC] || 核准課程計畫及班級清冊／課程承辦人 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 以核准課程計畫與班級清冊核對班碼、名稱、日期和每班容量；未取得原件前標 UNKNOWN，不據本樣本認定已開課。 || UNKNOWN（目前無真實原件；SAMPLE/SYNTHETIC）
[ROW 4] REC-CLS-006／S18-CLS-C03-B → S18-SYN-03、S18-SYN-09 || C03 示範班碼與示範課名 || S18-CLS-C03-B；C03 訓練設計與教學帶領示範課程 B；2027-09-20 至 2027-09-20；12 名 [SAMPLE/SYNTHETIC] || 核准課程計畫及班級清冊／課程承辦人 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 以核准課程計畫與班級清冊核對班碼、名稱、日期和每班容量；未取得原件前標 UNKNOWN，不據本樣本認定已開課。 || UNKNOWN（目前無真實原件；SAMPLE/SYNTHETIC）

[TABLE 23]
[ROW 1] 內部合成 fact_id／來源包 replacement_key || 待替換欄位名稱 || 當前示範登錄值 (SAMPLE) || 可核對來源類型（依核定治理方式；非既存事實） || 替換執行角色 || 轉換審核角色 || 正式抽換核驗步驟與判定標準 || 當前管制狀態標註
[ROW 2] REC-CLS-007／S18-CLS-C04-A → S18-SYN-03、S18-SYN-09 || C04 示範班碼與示範課名 || S18-CLS-C04-A；C04 訓練評估與機構品質循環示範課程 A；2027-11-08 至 2027-11-08；12 名 [SAMPLE/SYNTHETIC] || 核准課程計畫及班級清冊／課程承辦人 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 以核准課程計畫與班級清冊核對班碼、名稱、日期和每班容量；未取得原件前標 UNKNOWN，不據本樣本認定已開課。 || UNKNOWN（目前無真實原件；SAMPLE/SYNTHETIC）
[ROW 3] REC-CLS-008／S18-CLS-C04-B → S18-SYN-03、S18-SYN-09 || C04 示範班碼與示範課名 || S18-CLS-C04-B；C04 訓練評估與機構品質循環示範課程 B；2027-11-15 至 2027-11-15；12 名 [SAMPLE/SYNTHETIC] || 核准課程計畫及班級清冊／課程承辦人 || ROLE-SAMPLE-PLAN-01 || ROLE-SAMPLE-REVIEW-01 || 以核准課程計畫與班級清冊核對班碼、名稱、日期和每班容量；未取得原件前標 UNKNOWN，不據本樣本認定已開課。 || UNKNOWN（目前無真實原件；SAMPLE/SYNTHETIC）
