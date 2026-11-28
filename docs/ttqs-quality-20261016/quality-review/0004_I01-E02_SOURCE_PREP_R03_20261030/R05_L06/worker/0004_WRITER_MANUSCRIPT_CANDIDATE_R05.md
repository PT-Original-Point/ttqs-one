# 《目標市場調查執行與樣本紀錄》

> **文件狀態宣告（SAMPLE / SYNTHETIC WORKED EXAMPLE）**  
> 本文件為 TTQS 評核佐證之**候選示範本（CANDIDATE SAMPLE/SYNTHETIC WORKED EXAMPLE）**，全案採用合成數據（Synthetic Data）示範調查流程控制、流向對帳與品質檢核架構。  
> **重要聲明**：本文件所載之執行流程、處置規則均為**擬議作業範例（PROPOSED WORKFLOW EXAMPLE）**，非勞動部勞動力發展署或本機構之正式核准辦法；真實調查施測事實、真實抽樣名冊、真實同意憑證與正式資料保存年限目前皆處於**未取得／未確定（UNKNOWN）**狀態。未取得合規之真實原始佐證前，本文件嚴禁宣稱完成正式評核查驗或主張獨立審查通過（QA PASS）。

---

## 1. 首頁操作卡（文件基本控制與身分說明）

### 1.1 文件基本身分與對應指標
- **文件編號（Doc ID）**：`0004`
- **對應指標編號（Requirement ID）**：`I01-E02`
- **專案清單識別序號**：`002`（註：此編號為專案內部 157 項次對照序號，**絕非**官方評核表上方框之正式印製流水號）。
- **官方依據文字**：依據官方《TTQS查核佐證文件資料表－訓練機構版》第 1 頁，計畫（Plan）構面／「訓練機構未來經營方向及目標之訂定」常見參考佐證項目：「`目標市場需求調查。`」（查核頁次：第 1 頁）。
- **現行文類職責**：`執行與樣本紀錄｜目標市場調查執行與樣本紀錄`。本件專責記錄單一調查批次之母體篩選、邀請發送、受訪同意、收件受理、有效性判定、重複排除、覆核及交接紀錄；本件不承擔問卷題目設計（由 0003 負責），亦不承擔市場需求分析與開課決策（由 0005 負責）；本件亦不取代 0001《中長程業務發展策略地圖》及 0006《業務發展計畫與人力資源訓練規劃》，該二件的策略地圖與人力資源規劃不屬本執行紀錄。
- **示範批次識別碼**：`SYN-0004-CYCLE-01` [SAMPLE_SYNTHETIC_ONLY]（登記事實代碼：`SYN-0004-CYCLE-01`）

### 1.2 作業操作資訊卡

| 項目 | 規範內容 | 登記事實 / 規則代碼 |
| :--- | :--- | :--- |
| **文件用途** | 記錄目標市場調查之接觸歷程、邀請回應狀態、樣本收件檢驗、重複排除及樣本流向對帳，建立完整可追溯稽核軌跡。 | `I01-E02` / `doc_id=0004` |
| **使用時點** | 真實調查須先核對核定方案、有效的 0003 版本、欄位完整度清單及資格準則；之後記錄發放、回收、有效性判定至交付 0005 的流程。本示範對 0003 R09 僅作候選跨件代碼參照，不表示已審定。 | 真實作業前置條件 |
| **操作責任角色** | 執行操作員：`SYN-OPS-01` [SAMPLE_SYNTHETIC_ONLY] | `SYN-0004-ROLE-OPS-01` |
| **覆核責任角色** | 品質覆核員：`SYN-REV-01` [SAMPLE_SYNTHETIC_ONLY]（嚴格落實角色分離） | `SYN-0004-ROLE-REV-01` |
| **輸入要件** | (1) 目標客群抽樣框及核定方案；(2) 本次採用之 0003 版本、欄位完整度清單與發布管道（使用前核實有效狀態）；(3) 經核定的資格審查準則。 | 真實作業前置條件 |
| **輸出要件** | (1) 完整樣本收件與流向對帳紀錄；(2) 流程品質指標；(3) 交付 0005 之有效樣本代碼清單。 | 階段產出規範 |
| **真實資料狀態** | **UNKNOWN**（真實調查施測事實目前未知，保留 HOLD 狀態等待替換）。 | `UNK-0004-REAL-EXECUTION` |
| **保存政策狀態** | **UNKNOWN**（來源未提供正式保存期限；本文件不指定保存年限，也不表示已建立封存政策）。 | `UNK-0004-REAL-RETENTION` |

### 1.3 官方要求與本件紀錄欄位追溯表

| 官方要求／Blueprint範圍 | 0004專屬紀錄欄位 | 來源及狀態 | 獨立覆核方法 | 預期輸出 |
| :--- | :--- | :--- | :--- | :--- |
| I01-E02；官方佐證表第1頁「目標市場需求調查」；本件只負責執行及樣本流向，不取代問卷或分析 | 文件身分、責任範圍、前置與輸出 | 官方PDF SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709；0004 Blueprint SHA-256 0a439bd16b3b1f04e7082d74a62f32f9b9a3ae7d89588c88c7b3451a37c8064c；現行列 SHA-256 6d65168cf812eed9c6e2714f5d3d2e8221b5f8d25c2e88812a57f3d16c842b1b | 核對 doc_id=0004、requirement_id=I01-E02、官方原文與 0003/0005 負向近鄰 | 可辨識的執行與樣本紀錄，不產出需求排序或問卷題目 |
| 目標對象、抽樣框、納入／排除、抽樣方法及限制 | §2.1、表4-1、五筆 attendance flags、SAMPLE規則 | 0004 R03 Blueprint §B–E；僅使用 SYN-0004 例值；REAL frame UNKNOWN | 逐筆按同一納入規則重算資格，確認 U005 排除理由，確認不是機率抽樣 | 五筆篩選結果、四筆合資格情境、無代表性宣稱 |
| 聯絡／邀請／同意及期限 | 表4-1；日期、管道、狀態、期限、索引欄位 | 合成 replacement register R05；每列明確標註未外送 | 查 invitation scenario 不被誤寫成實際送達；同意只能作 SAMPLE 情境，不當 REAL 證明 | 可追溯的情境接觸表及真實替換欄 |
| 回覆、有效性、缺漏、重複、更正及原始件定位 | 表5-2、表5-3；唯一回覆碼、收件狀態、判定、索引欄位 | 0003 R09 僅凍結參照兩個 SAMPLE ID；R05 為本件值清冊 | 核對每列匿名碼、缺漏理由、重複關聯及索引欄；SAMPLE slot 不得冒充檔案 | 有效／無效唯一回覆及重複事件紀錄 |
| 流向整數及 Blueprint 指標 | 表6-1、表7-1；分子、分母、事件／唯一值及公式 | R05 登記的 SAMPLE counts、flows、rates | 重新計算四個平衡式及四個比率；分母為0時 N/A | 對帳與流程指標；不作市場需求推論 |
| 覆核、交接、隱私及真實化 | §8–10；角色分離、0005交接限制、原件替換清冊 | 真實角色、政策、原件及施測狀態均 UNKNOWN；擬議控制明標 | 確認無簽章／核准／真人執行宣稱；核對 0005 只接有效匿名碼與限制 | SAMPLE 可重算範例及逐項 REAL 替換清單 |

> 0003 跨件版本狀態：本示範僅引用 0003 R09 候選的匿名樣本碼；該候選 DOCX SHA-256 為 4bb761ca6e147dba0f9203566def6e971a50c58ebc17e2cc88a03804191eb1e7，證據 manifest SHA-256 為 cb2b87db7ecced4105f8a2a7cab6705db1a48ccc9038774bd8c8004e36e995d7，manifest 記載預審／語意審查進行中、正式接受 UNKNOWN。不得以本跨件樣本引用宣稱 0003 已審定或接受。

---

## 2. 調查範圍、母體界定與抽樣框管制

### 2.1 目標客群與抽樣框界定
本示範批次 SYN-0004-CYCLE-01 以虛構志工培訓目標市場展示可重算的資格判定及抽樣框處理；本段是 SAMPLE 方法示例，不是本機構核准的市場定義或真實名冊。
- **目標市場定義（SAMPLE）**：在虛構批次 SYN-0004-CYCLE-01 中，曾完成至少一項志工培訓活動的虛構接觸紀錄（SYN-0004-SAMPLE-TARGET-SEGMENT）。這是為示範資格判定而建立的例子，不能外推至任何真實協會服務對象。
- **納入條件（SAMPLE）**：虛構框內紀錄的「本示範週期完成志工培訓」欄為 YES；不另加年齡、地區、服務意願或其他未登記條件（SYN-0004-SAMPLE-INCLUSION-RULE）。
- **排除條件（SAMPLE）**：同欄為 NO 時排除；U005 為唯一示範排除列，值及理由均列於合成清冊（SYN-0004-SAMPLE-EXCLUSION-RULE；SYN-0004-U005-TRAINING-ATTENDANCE）。
- **抽樣方法（SAMPLE）**：對本虛構框內全部 5 筆紀錄逐筆篩選（complete-frame enumeration），不是機率抽樣；小樣本不具母體代表性或推論能力（SYN-0004-SAMPLE-SAMPLING-METHOD；SYN-0004-COUNT-SCREENED）。
- **抽樣框來源**：僅為五筆合成代碼，不代表任何真實組織名冊、會員資料或個人資料（SYN-0004-FRAME-01）。U001 至 U005 的完成狀態逐筆登記於 R05 replacement register；真實母體、來源授權與資格準則仍為 UNKNOWN（UNK-0004-REAL-FRAME）。
- **調查涵蓋期間**：
  - 啟動日期：2026-10-28（SAMPLE_SYNTHETIC_ONLY；SYN-0004-DATE-OPEN）。
  - 截止日期：2026-10-29（SAMPLE_SYNTHETIC_ONLY；SYN-0004-DATE-CLOSE）。
  - 示例截止時刻：2026-10-29 23:59，時區 Asia/Taipei（SAMPLE_SYNTHETIC_ONLY；SYN-0004-CLOSE-TIME、SYN-0004-CLOSE-TZ）。這只用於演算 U004 的情境狀態，真實期限必須取自核定方案。

### 2.2 抽樣限制與去重判定原則
- **去重識別規則**：以系統授權之唯一匿名回覆識別碼為準；同一授權代碼之首次收件視為唯一回覆，後續再次送達之相同代碼副本一律列為重複收件事件，自唯一回覆數中扣除（登記規則代碼：`RULE-0004-DUPLICATE-01` [PROPOSED_RULE_NOT_REAL_POLICY]）。
- **抽樣限制聲明**：本示範案最終僅產出 1 筆有效合成回覆（`n=1 synthetic response`），純屬流程驗證，**絕不具備任何母體推論能力、統計顯著性或代表性**（登記事實代碼：`SYN-0004-LIMIT-N` [SAMPLE_SYNTHETIC_ONLY]）。
- **真實抽樣框缺漏處置**：真實抽樣框來源現況標記為 `UNKNOWN`（登記事實代碼：`UNK-0004-REAL-FRAME` [UNKNOWN_REAL_SOURCE]）。未來替換為真實資料時，必須檢附經權限主管簽核之正式名冊來源證明，否則維持 HOLD 狀態。

---

## 3. 執行流程控制與異常路徑處置規範

### 3.1 調查執行八大循序階段管制表 [SAMPLE_SYNTHETIC_ONLY]
本流程嚴格執行「操作者」與「覆核者」權責分離，依序辦理。

| 階段編號 | 階段名稱 | 輸入要件 | 操作角色 | 覆核角色 | 控制查核點 | 產出紀錄 | 異常處置路徑 |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **S1** | **接觸資格篩選** | 待篩選名單 | `SYN-OPS-01` | `SYN-REV-01` | 核對納入與排除條件 | 資格符合名冊 | 不符合者標註原因排除，終止流程 |
| **S2** | **發送調查邀請** | 合資格名單 | `SYN-OPS-01` | `SYN-REV-01` | 邀請管道與發送時戳 | 發放發送日誌 | 發送失敗者嘗試重發，失敗列無效發送 |
| **S3** | **受訪意願同意** | 線上問卷說明 | 受訪對象 | `SYN-OPS-01` | 查驗受訪同意聲明勾選 | 意願確認紀錄 | 明確拒絕者列為 REFUSAL，結案留存 |
| **S4** | **回覆收件受理** | 問卷提交事件 | 系統/`SYN-OPS-01` | `SYN-REV-01` | 截止時限與收件完整性 | 收件事件日誌 | 逾期收件列入 HOLD，不計入有效分析 |
| **S5** | **有效性審查判定** | 原始收件紀錄 | `SYN-OPS-01` | `SYN-REV-01` | 依據 `RULE-0004-ELIGIBILITY-01` 審查 | 有效性判定表 | 必填欄缺漏判定為 INVALID 並註明原因 |
| **S6** | **重複與異常處理** | 判定完成資料 | `SYN-OPS-01` | `SYN-REV-01` | 比對唯一匿名代碼 | 去重與例外清冊 | 重複送達列為 DUP 排除，不可計為新增人 |
| **S7** | **批次流向覆核** | 全流程清冊 | `SYN-REV-01` | 權責主管 | 100% 勾稽各階段總數 | 對帳審查表 | 數字不平觸發 REWORK，退回重新清點 |
| **S8** | **交接封存作業** | 審核通過樣本 | `SYN-OPS-01` | `SYN-REV-01` | 僅移轉有效碼與流程限制 | 0005 交接表 | 涉及個資或分析需求者一律 REJECT 阻擋 |

### 3.2 流程決策處置準則（ACCEPT / REJECT / HOLD / REWORK）
1. **ACCEPT（納入本示範有效樣本計數）**：符合本示範所列資格結果、同意狀態、唯一回覆、核心欄位完整，且收件發生於記錄的截止點之前；本 SAMPLE 截止點為 2026-10-29 23:59 Asia/Taipei（SYN-0004-CLOSE-TIME、SYN-0004-CLOSE-TZ）；兩項均為合成設定，不是真實機構期限。真實期限未由核定方案證實前，REAL 同日收件維持 HOLD。這是擬議判定例，不代表機構已核准政策。真實收件期限須依核定方案確認（`RULE-0004-ELIGIBILITY-01` [PROPOSED_RULE_NOT_REAL_POLICY]）。
2. **REJECT（判定排除）**：
   - 篩選資格不符者（如 `SYN-0004-U005`，原因：`OUTSIDE_FICTIONAL_TARGET_SEGMENT`）。
   - 明確拒絕受訪者（如 `SYN-0004-U003`，原因：`EXPLICIT_REFUSAL`）。
   - 核心必要欄位缺漏不全者（如 `SYN-0004-U002`，原因：`REQUIRED_FIELD_MISSING`）。
   - 重複提交之副本（如 `SYN-0004-DUP-01`，處置：`EXCLUDE_EXTRA_COPY_FROM_UNIQUE_COUNTS`）。
3. **HOLD（暫緩凍結）**：真實調查施測憑證、真實抽樣名冊、真實同意撤回證明及正式保存政策未具備前，全案處於 HOLD，不得交付實質開課決策。
4. **REWORK（退回重整）**：凡各階段流向對帳等式不吻合、整數計數不一致、或覆核發現漏列異常者，立即退回 S1 或 S5 重新清點。

---

## 4. 接觸篩選與邀請逐筆紀錄（樣本示範表）

> 本表所列 5 筆接觸紀錄均為虛構資料代碼，未包含任何真實個人姓名、聯絡電話、電子郵件、網路 IP 或實體通訊地址。

### 表 4-1：接觸對象篩選與邀請處理逐筆清冊 [SAMPLE_SYNTHETIC_ONLY]

| 匿名接觸代碼 | 篩選日期 | 本示範週期完成培訓 | 資格判定 | 邀請狀態（未外送） | 邀請情境日期 | 邀請管道情境 | 同意狀態情境（非真實同意） | 示例截止點 | 回覆情境結果 | 判定理由 | 登記事實代碼 (Fact ID) | SAMPLE索引欄位（非現存檔案） |
| :--- | :---: | :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SYN-0004-U001 | 2026-10-28 | YES | ELIGIBLE | INVITATION_SCENARIO_ONLY_NOT_SENT | 2026-10-28 | 虛構線上邀請情境；無連結、未外送 | SAMPLE_CONSENT_YES_NOT_ACTUAL | 2026-10-29 23:59 Asia/Taipei | UNIQUE_RETURN_COMPLETE_VALID | 完整有效之合成情境；非真實提交 | SYN-0004-U001-ID<br>SYN-0004-U001-SCREEN-DATE<br>SYN-0004-U001-TRAINING-ATTENDANCE<br>SYN-0004-U001-ELIGIBILITY<br>SYN-0004-U001-INVITE-STATE<br>SYN-0004-U001-INVITE-DATE<br>SYN-0004-U001-CONSENT<br>SYN-0004-U001-OUTCOME<br>SYN-0004-U001-SAMPLE-INDEX-SLOT | SAMPLE_INDEX_SLOT_U001; NOT_A_RECORD; NO_FILE_OR_LOG |
| SYN-0004-U002 | 2026-10-28 | YES | ELIGIBLE | INVITATION_SCENARIO_ONLY_NOT_SENT | 2026-10-28 | 虛構線上邀請情境；無連結、未外送 | SAMPLE_CONSENT_YES_NOT_ACTUAL | 2026-10-29 23:59 Asia/Taipei | UNIQUE_RETURN_INCOMPLETE_INVALID | 核心欄位缺漏情境（REQUIRED_FIELD_MISSING） | SYN-0004-U002-ID<br>SYN-0004-U002-SCREEN-DATE<br>SYN-0004-U002-TRAINING-ATTENDANCE<br>SYN-0004-U002-ELIGIBILITY<br>SYN-0004-U002-INVITE-STATE<br>SYN-0004-U002-INVITE-DATE<br>SYN-0004-U002-CONSENT<br>SYN-0004-U002-OUTCOME<br>SYN-0004-U002-DISPOSITION-REASON<br>SYN-0004-U002-SAMPLE-INDEX-SLOT | SAMPLE_INDEX_SLOT_U002; NOT_A_RECORD; NO_FILE_OR_LOG |
| SYN-0004-U003 | 2026-10-28 | YES | ELIGIBLE | INVITATION_SCENARIO_ONLY_NOT_SENT | 2026-10-28 | 虛構線上邀請情境；無連結、未外送 | SAMPLE_REFUSAL_NOT_ACTUAL | 2026-10-29 23:59 Asia/Taipei | NO_RETURN | 明確拒絕之合成情境；非真實拒答 | SYN-0004-U003-ID<br>SYN-0004-U003-SCREEN-DATE<br>SYN-0004-U003-TRAINING-ATTENDANCE<br>SYN-0004-U003-ELIGIBILITY<br>SYN-0004-U003-INVITE-STATE<br>SYN-0004-U003-INVITE-DATE<br>SYN-0004-U003-CONSENT<br>SYN-0004-U003-OUTCOME<br>SYN-0004-U003-DISPOSITION-REASON<br>SYN-0004-U003-SAMPLE-INDEX-SLOT | SAMPLE_INDEX_SLOT_U003; NOT_A_RECORD; NO_FILE_OR_LOG |
| SYN-0004-U004 | 2026-10-28 | YES | ELIGIBLE | INVITATION_SCENARIO_ONLY_NOT_SENT | 2026-10-28 | 虛構線上邀請情境；無連結、未外送 | SAMPLE_NO_RESPONSE_NO_CONSENT_EVIDENCE | 2026-10-29 23:59 Asia/Taipei | NO_RETURN | 截止點後仍無回覆之合成情境；非真實未回覆  (NO_RESPONSE_BY_CLOSE)| SYN-0004-U004-ID<br>SYN-0004-U004-SCREEN-DATE<br>SYN-0004-U004-TRAINING-ATTENDANCE<br>SYN-0004-U004-ELIGIBILITY<br>SYN-0004-U004-INVITE-STATE<br>SYN-0004-U004-INVITE-DATE<br>SYN-0004-U004-CONSENT<br>SYN-0004-U004-OUTCOME<br>SYN-0004-U004-DISPOSITION-REASON<br>SYN-0004-CLOSE-TIME<br>SYN-0004-CLOSE-TZ<br>SYN-0004-U004-SAMPLE-INDEX-SLOT | SAMPLE_INDEX_SLOT_U004; NOT_A_RECORD; NO_FILE_OR_LOG |
| SYN-0004-U005 | 2026-10-28 | NO | INELIGIBLE | NOT_INVITED | N/A | 未進入邀請情境 | NOT_APPLICABLE | N/A | NO_RETURN | 完成培訓欄為 NO，依本示範排除條件排除 | SYN-0004-U005-ID<br>SYN-0004-U005-SCREEN-DATE<br>SYN-0004-U005-TRAINING-ATTENDANCE<br>SYN-0004-U005-ELIGIBILITY<br>SYN-0004-U005-INVITE-STATE<br>SYN-0004-U005-CONSENT<br>SYN-0004-U005-OUTCOME<br>SYN-0004-U005-DISPOSITION-REASON<br>SYN-0004-U005-SAMPLE-INDEX-SLOT | SAMPLE_INDEX_SLOT_U005; NOT_A_RECORD; NO_FILE_OR_LOG |

- 註1：表內四筆邀請均為情境演示，不曾外送邀請或建立連結；四筆「同意／拒絕」亦只是 SAMPLE 情境狀態，不是真實受訪者的同意或拒答證明。
- 註2：五個 SAMPLE_INDEX_SLOT 值均已列入 R05 register，且明確代表「沒有現存原件、檔案或日誌」。真實化只能以實際取得且獲准引用的原件定位取代；不能把 slot 當成證據。
- 註3：U004 的 no-response 分類只在本示範截止點 2026-10-29 23:59 Asia/Taipei 後成立；真實紀錄必須依核定期限重算。

---

## 5. 樣本收件、有效性判定與重複紀錄（樣本示範表）

### 5.1 有效性判定準則
依據擬議作業準則 `RULE-0004-ELIGIBILITY-01` [PROPOSED_RULE_NOT_REAL_POLICY]：
> 「本示範有效樣本判定要件：登記為合資格 ＋ 同意狀態為已同意 ＋ 於示範收件期間內提交 ＋ 0003 所列必填欄位完整 ＋ 具備唯一匿名回覆代碼。此為擬議判定規則，不是機構已核定之政策；真實適用時須先取得核定方案及該版 0003 的欄位完整度規則。」

### 5.2 唯一回覆收件與有效性逐筆紀錄表 [SAMPLE_SYNTHETIC_ONLY]

以下兩列為合成情境，不代表任何真實收件或真人覆核。U001 引用 0003 R09 的 SAMPLE 匿名回覆碼；U002 是 0004 自有的無答案收件識別碼。兩列均沒有可供外部查驗的原始檔案，索引欄只展示應填位置，不是證據。

| 匿名接觸代碼 | 原始收件日戳（SAMPLE） | 0004收件識別／0003回覆碼（無答案內容） | 完整度 | 有效性 | 排除／處置理由 | 重複／更正關聯 | 示範覆核角色（未核簽） | 登記事實代碼 (Fact ID) | 0003凍結參照 | 原始件索引欄（SAMPLE slot；無檔案） |
| :--- | :---: | :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| SYN-0004-U001 | 2026-10-28 | SYN-0003-001；僅匿名 SAMPLE 代碼 | SAMPLE完整 | VALID（情境） | 無排除；只示範欄位完整的有效路徑 | 唯一首筆；無更正 | SYN-REV-01（示範角色，非真人簽核） | SYN-0004-U001-RETURN-DATE<br>SYN-0004-U001-RESPONSE-REF<br>SYN-0004-U001-RECEIPT-LOCATOR<br>SYN-0004-ROLE-REV-01 <br>XREF-0003-SYN-001| 0003 R09 的 SYN-0003-001 與 2026-10-28 均為 SAMPLE；0003 語意審查進行中、非正式接受 | SAMPLE_RECEIPT_SLOT_U001; NOT_A_RECORD; NO_SOURCE_FILE |
| SYN-0004-U002 | 2026-10-28 | SYN-0004-RETURN-002_NO_ANSWER_CONTENT_CARRIED；0004唯一收件 ID，非0003答案碼 | SAMPLE缺漏 | INVALID（情境） | 必填欄位缺漏情境；不補造答案 | 唯一首筆但無效封存 | SYN-REV-01（示範角色，非真人簽核） | SYN-0004-U002-RETURN-DATE<br>SYN-0004-U002-RESPONSE-REF<br>SYN-0004-U002-DISPOSITION-REASON<br>SYN-0004-U002-RECEIPT-LOCATOR | 不引用 0003 答案；0004 只示範缺漏處置 | SAMPLE_RECEIPT_SLOT_U002; NOT_A_RECORD; NO_SOURCE_FILE |

### 表 5-3 原始重複收件事件及索引紀錄表 [SAMPLE_SYNTHETIC_ONLY]

重複規則 RULE-0004-DUPLICATE-01 為 SAMPLE 擬議規則，非機構政策。重複事件只增加收件事件數，不增加唯一回覆數；本例沒有對應真實系統日誌。

| 收件事件代碼 | 收件日期 | 重複關聯之授權匿名代碼 | 去重判定（情境） | 處置 | 示範覆核角色（未核簽） | 登記事實代碼 (Fact ID) | 原始件索引欄（SAMPLE slot；無日誌） |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| SYN-0004-DUP-01 | 2026-10-28 | SYN-0003-001 | EXCLUDE_EXTRA_COPY_FROM_UNIQUE_COUNTS | 留存為事件；從唯一回覆與有效率分母排除 | SYN-REV-01（示範角色，非真人簽核） | SYN-0004-DUP-01-ID<br>SYN-0004-DUP-01-DATE<br>SYN-0004-DUP-01-LINK<br>SYN-0004-DUP-01-DECISION<br>SYN-0004-DUP-01-RECEIPT-LOCATOR | SAMPLE_RECEIPT_SLOT_DUP01; NOT_A_RECORD; NO_SOURCE_LOG |

---

## 6. 批次流向對帳表（樣本示範表）

本對帳表完整呈現原始整數計數、唯一值（Unique Persons/Submissions）與事件值（Events）之分離規則，嚴格落實四重平衡檢驗。

### 表 6-1：調查批次全流程流向對帳平衡表 [SAMPLE_SYNTHETIC_ONLY]

| 流向對帳節點 | 項目分類名稱 | 登記數值 (整數) | 納入與排除統計原則說明 | 登記事實代碼 (Fact ID) |
| :--- | :--- | :---: | :--- | :--- |
| **節點 A：名單篩選** | 已篩選接觸代碼總數（Screened Contacts） | **5** | 初始進入篩選之虛構接觸清冊總筆數 | `SYN-0004-COUNT-SCREENED` |
| | 不符合資格代碼數（Ineligible before Invite） | **1** | 判定非屬目標市場區隔者（`SYN-0004-U005`） | `SYN-0004-COUNT-INELIGIBLE` |
| | 合資格邀請情境數（未曾外送） | **4** | 符合合成流向設定的邀請狀態數；未實際外送 | `SYN-0004-COUNT-ELIGIBLE_INVITATION_SCENARIOS` |
| **節點 B：邀請回應** | 合資格邀請情境數（公式示範分母；未外送） | **4** | 與節點 A 登記的合成邀請情境數一致；不代表真實送達 | `SYN-0004-COUNT-ELIGIBLE_INVITATION_SCENARIOS` |
| | 唯一回覆問卷數（Unique Returned Questionnaires） | **2** | 排除重複後之唯一回覆問卷筆數（U001, U002） | `SYN-0004-COUNT-UNIQUE_RETURNS` |
| | 明確拒絕受訪數（Explicit Refusals） | **1** | 表明拒絕填答者（`SYN-0004-U003`） | `SYN-0004-COUNT-REFUSALS` |
| | 截止時限未回覆數（No Response by Close） | **1** | 逾期未回覆或未接觸者（`SYN-0004-U004`） | `SYN-0004-COUNT-NO_RESPONSE` |
| **節點 C：有效性判定** | 唯一回覆問卷數（基準分母） | **2** | 與節點 B 產出之唯一回覆數完全一致 | `SYN-0004-COUNT-UNIQUE_RETURNS` |
| | 有效唯一回覆數（Valid Unique Returns） | **1** | 完整填答且審核通過之樣本（`SYN-0004-U001`） | `SYN-0004-COUNT-VALID_UNIQUE` |
| | 無效/不完整回覆數（Invalid Unique Returns） | **1** | 必填欄缺漏判定無效者（`SYN-0004-U002`） | `SYN-0004-COUNT-INVALID_UNIQUE` |
| **節點 D：收件事件清查** | 原始收件事件總次數（Raw Receipt Events） | **3** | 合成情境所列的收件事件總數；沒有對應的真實系統日誌 | `SYN-0004-COUNT-RAW_RECEIPT_EVENTS` |
| | 唯一回覆問卷數（Unique Returns） | **2** | 經授權碼確認之唯一問卷回覆筆數 | `SYN-0004-COUNT-UNIQUE_RETURNS` |
| | 重複額外收件副本數（Duplicate Extra Receipts） | **1** | 後續重複送達並排除之事件數（`SYN-0004-DUP-01`） | `SYN-0004-COUNT-DUPLICATE_EXTRAS` |

### 6.2 對帳等式驗證結果（四重平衡檢驗）
1. **篩選流向平衡式**：  
   $$\text{篩選數 (5)} = \text{不合資格 (1)} + \text{合資格邀請情境 (4)} \implies 5 = 1 + 4$$  
   （核對事實代碼：`SYN-0004-FLOW-SCREEN` [SAMPLE_SYNTHETIC_ONLY]，平衡無誤）
2. **邀請流向平衡式**：  
   $$\text{合資格邀請情境 (4)} = \text{唯一回覆 (2)} + \text{明確拒絕 (1)} + \text{無回覆 (1)} \implies 4 = 2 + 1 + 1$$  
   （核對事實代碼：`SYN-0004-FLOW-INVITE` [SAMPLE_SYNTHETIC_ONLY]，平衡無誤）
3. **有效判定平衡式**：  
   $$\text{唯一回覆 (2)} = \text{有效唯一回覆 (1)} + \text{無效唯一回覆 (1)} \implies 2 = 1 + 1$$  
   （核對事實代碼：`SYN-0004-FLOW-VALID` [SAMPLE_SYNTHETIC_ONLY]，平衡無誤）
4. **收件事件平衡式**：  
   $$\text{原始收件事件 (3)} = \text{唯一回覆 (2)} + \text{重複副本 (1)} \implies 3 = 2 + 1$$  
   （核對事實代碼：`SYN-0004-FLOW-RECEIPT` [SAMPLE_SYNTHETIC_ONLY]，平衡無誤）

---

## 7. 調查流程品質指標計算表

本表四個比率均由 R05 合成事實清冊計算，僅示範定義、分子、分母與算式；邀請情境未外送，所有比率都不是實際調查績效，回覆率尤其僅為公式演算。所有指標均載明精確算式及取至小數點後第一位的百分比。

> **分母為零之處理規則說明**：若遇分母為 0 之情境，指標欄位一律填寫為「`N/A`」並註明原因（例如「無發送邀請分母為零」），嚴禁逕行填報 0% 或虛構填補分母數值。

本表四項比率均依本批次 SAMPLE 調查日期範圍 2026-10-28 至 2026-10-29 計算；截止設定以 Asia/Taipei 2026-10-29 23:59 為準。邀請情境未外送，數值僅為合成流程演算，不代表真實調查績效。
### 表 7-1：調查流程關鍵品質指標清冊 [SAMPLE_SYNTHETIC_ONLY]

| 指標名稱 | 官方/規格依據口徑 | 分子項目與數值 | 分母項目與數值 | 精確計算式 | 指標結果 (%) | 登記事實代碼 (Fact ID) |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |
| **回覆率**<br>(Response Rate) | Blueprint回覆率公式的情境演算；本示範未實際發送邀請，不代表觀測回覆績效 | 唯一回覆數<br>($n=2$) | 合資格邀請情境數（未外送）<br>($N=4$) | $$\frac{2}{4} = 0.500$$ | **50.0%** | `SYN-0004-RATE-RESPONSE` |
| **有效率**<br>(Effective Rate) | **Blueprint 指定口徑**：衡量已回收問卷中之合格純度 | 有效唯一回覆數<br>($n=1$) | 唯一回覆數<br>($N=2$) | $$\frac{1}{2} = 0.500$$ | **50.0%** | `SYN-0004-RATE-EFFECTIVE` |
| **有效樣本產出率**<br>(Valid Yield Rate) | 額外流程指標：衡量初始邀請之最終實質有效產出比率 | 有效唯一回覆數<br>($n=1$) | 合資格邀請情境數（未外送）<br>($N=4$) | $$\frac{1}{4} = 0.250$$ | **25.0%** | `SYN-0004-RATE-YIELD` |
| **資格通過率**<br>(Eligibility Pass Rate) | 額外流程指標：衡量名單接觸品質與目標客群契合度 | 合資格邀請情境數<br>($n=4$) | 已篩選接觸數<br>($N=5$) | $$\frac{4}{5} = 0.800$$ | **80.0%** | `SYN-0004-RATE-ELIGIBLE` |

---

## 8. 資料品質、隱私防護與保管政策

### 8.1 缺漏值與更正歷程管制
1. **缺漏欄位判定**：收件後僅依本次實際採用之 0003 版本和其必填欄位清單核對完整性；0004 不重列題目、選項、量尺或個別答案。示範案例 `SYN-0004-U002` 登記為 `REQUIRED_FIELD_MISSING`，不得由操作員猜測或代填。真實作業須先記錄所用 0003 版本與欄位清單來源。
2. **更正軌跡留存（擬議流程）**：若調查過程涉及任何接觸代碼異動或狀態更正，應由操作員 `SYN-OPS-01` 提出更正申請，記錄更正前、更正後數值與更正原因，並經覆核員 `SYN-REV-01` 簽核後始得異動，原始日誌維持唯讀留存。

### 8.2 拒答與撤回程序
1. **拒絕受訪**：受訪者於受邀後若明確表示不參與（如 `SYN-0004-U003`），系統即刻終止後續提醒通知，標記為 `DECLINED_BEFORE_SUBMISSION`，保留拒絕紀錄以供對帳，不強行催填。
2. **同意撤回**：如收到撤回要求，先停止該筆資料的後續分析與交接，依正式核定的同意告知及撤回程序處理；本合成登記沒有撤回事件，真實同意／撤回憑證為 `UNKNOWN`（`UNK-0004-REAL-CONSENT`）。未取得適用規範前不得自行宣稱已刪除、已撤回或已排除。

### 8.3 去識別化與最小存取權限
以下均為擬議的示範控制，不宣稱為本機構已核定政策；真實化前須核對適用法規及正式個資管理規範。
1. **全面去識別化**：問卷調查全程使用匿名接觸代碼（如 `SYN-0004-U001`）與授權回覆代碼（如 `SYN-0003-001`），不得儲存或向分析端傳遞姓名、身分證字號、電話、Email 等真實個人識別資訊。
2. **最小存取限制**：操作人員僅具備資料受理與編碼權限；覆核人員僅具備檢核與對帳權限；交接至 0005 之資料嚴格限定為無個資之匿名代碼。

### 8.4 資料保管與銷毀政策現況宣告
- **真實資料保存政策狀態**：**UNKNOWN**（`UNK-0004-REAL-RETENTION`）。來源封包沒有正式保存期限，本文件不設定期限。
- **真實化前置控制（擬議、未核准）**：取得並核對正式保存／銷毀規範前，不開始 REAL 紀錄的保存、移轉或刪除決策（RULE-0004-REAL-RETENTION-GATE-01；此為建議控制，不表示已有政策或已實施）。
- **真實化控制**：開始處理任何 REAL 紀錄前，先取得現行正式保存／銷毀規範並確認適用期限與權責；未確認前，REAL 保存、刪除或移轉決策維持 HOLD，不得自定年限。
- **本示範資料界線**：本件 SAMPLE 不含真實個資或真實調查原件；上述 UNKNOWN 不代表已有真實資料被封存，也不聲稱 SAMPLE 的保存政策已核定。

---

## 9. 作業覆核與 0005 資料交接紀錄

### 9.1 操作與覆核角色分離紀錄狀態 [SAMPLE_SYNTHETIC_ONLY]
本節只展示 SAMPLE 角色分離欄位，不代表本機構人員實際執行、覆核、簽署或核准；兩個角色代碼僅為示範值：
| 示範角色欄位 | 登記角色代碼 | 本次合成範例可支持的範圍 | 未被登記、不得推定的事項 |
| :--- | :--- | :--- | :--- |
| 執行操作角色 | `SYN-OPS-01` (`SYN-0004-ROLE-OPS-01`) | 僅代表示範用角色代碼 | 實際執行者、執行完成、簽名及日期均未登記 |
| 品質覆核角色 | `SYN-REV-01` (`SYN-0004-ROLE-REV-01`) | 僅代表示範用角色代碼 | 實際逐筆覆核、核准、簽名及日期均未登記 |
| 真實角色與執行狀態 | `UNKNOWN` (`UNK-0004-REAL-ROLES`; `UNK-0004-REAL-EXECUTION`) | 維持 HOLD | 未取得真實人員指派、原始作業日誌及合法簽核憑證前，不得填成已完成 |

### 9.2 交付 0005《目標市場需求分析報告》狹義交接表 [SAMPLE_SYNTHETIC_ONLY]

> **文類邊界嚴格管制**：  
> 本紀錄（0004）僅交付樣本流向計數、有效樣本匿名識別碼及樣本限制；**嚴禁**承載問卷題目文字、選項定義、個別題目答案內容（此屬 0003《目標市場需求調查問卷》專屬範圍），亦**嚴禁**承載各題平均分數、需求程度排序、課程開設建議或辦訓決策解讀（此屬 0005《目標市場需求分析報告》專屬範圍）；本件亦不替代 0001《中長程業務發展策略地圖》及 0006《業務發展計畫與人力資源訓練規劃》。

| 交付項目 | 交付內容 / 數據值 | 登記事實代碼 (Fact ID) | 0005 接收與運用限制規範 |
| :--- | :--- | :--- | :--- |
| **調查批次識別** | `SYN-0004-CYCLE-01` | `SYN-0004-CYCLE-01` | 限供分析報告標註調查批次來源，不得跨批次混算。 |
| **有效分析樣本數** | **1 筆** ($n=1$) | `SYN-0004-HANDOFF-N` | 0005 分析分母嚴格限定為 $N=1$，不得自行灌水或追加樣本。 |
| **有效匿名樣本代碼** | `SYN-0003-001` | `SYN-0004-HANDOFF-ID`<br>(`XREF-0003-SYN-002`) | 僅交接此一匿名識別碼，0005 僅得依此代碼調閱經授權之問卷答案結構。 |
| **樣本代表性限制** | `n=1 synthetic response; no population inference` | `SYN-0004-LIMIT-N` | **重大限制**：本樣本為合成資料且樣本數為 1，不具備任何統計推論能力，0005 報告中嚴禁宣稱代表全體市場需求。 |
| **分析與結論邊界** | 0004 不提供需求排序、因果推論或開課決策 | 邊界隔離原則 | 0005 須自行依有效數據執行描述性統計，不得將 0004 流程指標混充為市場需求強度。 |

---

## 10. 真實化替換清單與佐證索引對照表（Real Replacement Gate）

當本文件自「候選示範本（CANDIDATE SAMPLE/SYNTHETIC）」轉換為「評核正式佐證（REAL OFFICIAL EVIDENCE）」時，評核人員或後續接辦者必須依下表清單逐項查驗，取得具備正式核決權限之原始真實憑證，進行全面替換。在未完成替換並經外部評核員獨立查驗前，全案維持 **HOLD** 狀態。

### 表 10-1：合成事實代碼對應真實替換佐證需求清冊

| 合成事實代碼 (Fact ID) | 目前示範狀態 | 正文呈現位置 | 真實化必須替換之正式佐證文件與原始憑證要求 | 建議角色／待實際指派 | 替換檢核標準 (Gate Criteria) |
| :--- | :---: | :--- | :--- | :---: | :--- |
| `SYN-0004-CYCLE-01`<br>`SYN-0004-DATE-OPEN`<br>`SYN-0004-DATE-CLOSE` | SAMPLE | 首頁 / 第 1、2 章 | (1) 機構年度核定之實際調查實施計畫書；<br>(2) 調查執行公文或專案簽呈，載明真實調查啟始與截止日期。 | 計畫主持人 | 替換事實 `UNK-0004-REAL-EXECUTION` 為真實日期，不可留有 SYN 標記。 |
| `SYN-0004-FRAME-01`<br>`SYN-0004-LIMIT-N` | SAMPLE | 第 2 章 | (1) 實際目標客群抽樣母體來源名冊清冊（如會員名錄、企業名冊）；<br>(2) 符合個資保護法之名冊取得與使用授權證明文件。 | 調查督導員 | 替換事實 `UNK-0004-REAL-FRAME`，明載抽樣母體數與真實限制。 |
| `SYN-0004-SAMPLE-TARGET-SEGMENT`<br>`SYN-0004-SAMPLE-INCLUSION-RULE`<br>`SYN-0004-SAMPLE-EXCLUSION-RULE`<br>`SYN-0004-SAMPLE-SAMPLING-METHOD`<br>`SYN-0004-U001-TRAINING-ATTENDANCE`<br>`SYN-0004-U002-TRAINING-ATTENDANCE`<br>`SYN-0004-U003-TRAINING-ATTENDANCE`<br>`SYN-0004-U004-TRAINING-ATTENDANCE`<br>`SYN-0004-U005-TRAINING-ATTENDANCE` | SAMPLE | 第 2 章、表 4-1 | (1) 真實核定抽樣方案；<br>(2) 有權使用之母體框及逐筆篩選紀錄；<br>(3) 經核定的納入與排除條件。 | 調查督導員 | 逐筆按核定條件重算；完整框枚舉不得宣稱機率抽樣或具母體代表性。 |
| `SYN-0004-CLOSE-TIME`<br>`SYN-0004-CLOSE-TZ`<br>`SYN-0004-U004-DISPOSITION-REASON` | SAMPLE | §2.1、表 4-1 U004、表 6-1 | 核定調查方案載明的截止日期、時間及時區；延長須留存正式變更紀錄。 | 調查督導員／覆核員 | 依同一時區與截止點核對 U004；只有截止後才可記為 NO_RESPONSE_BY_CLOSE，缺任一時間要素即 HOLD。 |
| `SYN-0004-U001-SAMPLE-INDEX-SLOT`<br>`SYN-0004-U002-SAMPLE-INDEX-SLOT`<br>`SYN-0004-U003-SAMPLE-INDEX-SLOT`<br>`SYN-0004-U004-SAMPLE-INDEX-SLOT`<br>`SYN-0004-U005-SAMPLE-INDEX-SLOT` | SAMPLE slot；NOT_A_RECORD | 表 4-1 各列 | 有授權的篩選原始紀錄或可核實的受控來源定位；原件不存在則保留 UNKNOWN，不建立假檔名或路徑。 | 執行操作員 | 逐筆連回真實原始來源；slot 本身不是佐證，未取得來源不得升為 REAL。 |
| `SYN-0004-U001-RECEIPT-LOCATOR`<br>`SYN-0004-U002-RECEIPT-LOCATOR`<br>`SYN-0004-DUP-01-RECEIPT-LOCATOR` | SAMPLE slot；NOT_A_RECORD | 表 5-2、表 5-3 | 有權限之原始回覆／收件系統定位及去重事件原件；僅記受控位置與匿名代碼，不複製不必要個資。 | 執行操作員／覆核員 | 逐列核對狀態、缺漏判定、重複關聯及原件存在性；沒有原件時維持 NOT_A_RECORD。 |
| `XREF-0003-SYN-001`<br>`XREF-0003-SYN-002` | SAMPLE cross-document reference | 表 5-2 U001、表 9-2 | 0003 對應候選的受控匿名回覆碼、日期與來源 register；真實化時須用獲授權的 0003 原始來源。 | 0004 覆核員／0005 負責人 | 逐一核對來源版本、Fact ID、日期及有效狀態；跨件候選參照不表示 0003 已接受。 |
| `RULE-0004-REAL-RETENTION-GATE-01` | PROPOSED；未核准 | §8.4、表 10-1 | 現行且經有權單位核准的保存／銷毀政策及適用範圍。 | 行政主管 | 僅在核實來源、核准權責、生效日與範圍後更新；核實前 REAL 保存、移轉或刪除決策維持 HOLD。 |
| `SYN-0004-CHANNEL-01` | SAMPLE | 第 3、4 章 | 實際發送紀錄原件，如：EDM 發送後台報告、郵寄送達簽收聯或線上平台發送日誌（Log）。 | 執行操作員 | 佐證須包含發送時間戳記、送達狀態與系統發送序號。 |
| `SYN-0004-ROLE-OPS-01`<br>`SYN-0004-ROLE-REV-01` | SAMPLE | 全文各表 | (1) 實際機構承辦人員與主管之真實職稱、姓名簽章；<br>(2) 職務指派通知或內部工作職掌分工表（證明落實角色分離）。 | 單位主管 | 替換事實 `UNK-0004-REAL-ROLES`，操作者與覆核者不得為同一人。 |
| `RULE-0004-ELIGIBILITY-01`<br>`RULE-0004-DUPLICATE-01` | PROPOSED | 第 3、5 章 | 機構內部正式核定公布之《調查資料品質檢核與去重作業規範》或相關標準作業程序（SOP）。 | 品質主管 | 具備正式文號與發布核決紀錄，取代 PROPOSED 擬議標籤。 |
| `RULE-0004-RETENTION-01` | UNKNOWN | 第 8 章 | 機構正式頒布之《文件與個資檔案保存與銷毀管理辦法》，明確規範調查原始憑證之法定或制度保存年限。 | 行政主管 | 替換事實 `UNK-0004-REAL-RETENTION`，以正式年限取代 UNKNOWN。 |
| `SYN-0004-U001` 至 `SYN-0004-U005`<br>(全體接觸紀錄) | SAMPLE | 第 4 章表 4-1 | (1) 真實受訪對象之篩選原始紀錄表單；<br>(2) 具備明確同意註記或拒絕填答之電子歷程紀錄（Consent Logs）；<br>(3) 實際催填與送達證明文件。 | 執行操作員 | 替換事實 `UNK-0004-REAL-CONSENT`，嚴格落實去識別化編碼對照。 |
| `SYN-0004-U001` (有效)<br>`SYN-0004-U002` (無效)<br>`SYN-0004-DUP-01` (重複) | SAMPLE | 第 5 章表 5-2、5-3 | (1) 系統收件之原始提交資料庫日誌或問卷回覆存檔；<br>(2) 原始問卷缺漏值判定查核表；<br>(3) 僅以授權匿名回覆代碼進行比對的去重紀錄；時間戳只供事件排序，不用 IP 或其他個人識別資料作為去重鍵。原始材料留在有權限的來源系統，0004 僅記來源定位及必要匿名代碼。 | 執行操作員 / 覆核員 | 逐筆對應真實問卷收件編號，無效與排除原因須具備具體客觀佐證。 |
| `SYN-0004-COUNT-*`<br>`SYN-0004-FLOW-*`<br>`SYN-0004-RATE-*` | SAMPLE | 第 6、7 章 | 依據真實收件總數重新計算之流向對帳表與品質指標計算底稿，須檢附覆核簽章。 | 品質覆核員 | 數據必須滿足各節點對帳等式，計算式需經 100% 重新驗算。 |
| `SYN-0004-HANDOFF-*` | SAMPLE | 第 9 章表 9-2 | (1) 經雙方簽署之《0004 至 0005 資料交接簽收單》；<br>(2) 交付需求分析之有效問卷真實編碼清冊（去識別化）。 | 0004 覆核員 / 0005 負責人 | 僅限交接有效樣本代碼及樣本數，嚴禁跨越文類承載分析結論。 |

---
*本文件完結｜TTQS-0004-I01-E02-WRITER-R05-CODEX-20261030｜候選示範文本*
