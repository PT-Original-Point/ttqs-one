# 公益活動、獎項與學校合作原件驗證登錄表

**DOCX 0136 ｜ 需求編號 I19-E26 ｜ 專案 157 規劃索引 150 ｜ 官方印刷勾選序號：UNKNOWN**

---

## 0. 文件封面與控制區塊（Cover / Control Block）

> **狀態標示：CANDIDATE / SAMPLE TEMPLATE / NOT ISSUED**
> 本文件為候選稿（CANDIDATE）、樣本範本（SAMPLE TEMPLATE）、**尚未核發（NOT ISSUED）**。
> 本文件**不是**已核准、已生效、已備查或已提交之版本；核准狀態：**NOT_GRANTED**；生效日期：**NOT_ISSUED**。
> 於人工來源（Human source）出現前，本封面任何「核准／生效／核章」欄位一律維持 NOT_GRANTED / NOT_ISSUED，**不得填入任何實際核章、簽名或日期**。

| 控制欄位 | 值 | 說明 |
|---|---|---|
| 專案 Project | TTQS_ONE | 內部專案代號 |
| 文件編號 Document ID | 0136 | 內部 DOCX 編號，**非**印刷勾選序號 |
| 官方需求編號 Requirement | I19-E26 | 142 份交叉對照列 |
| 官方交付標題 | 公益活動、獎項與學校合作原件驗證登錄表 | 逐字 |
| 文件體裁 Genre | 原件驗證登錄表 / 營運型證據日誌 | **非**成果報告 |
| 官方證據表來源 | official_source.pdf 印刷第 8–9 頁 | 指標 19 參考證據 |
| 專案 157 內容索引 | 150 — 公益/表揚/產學/研發社會影響：原件與來源 | **內部規劃索引，非印刷序號** |
| 官方印刷勾選序號 | **UNKNOWN** | 不得以 0136、I19-E26 或索引 150 代填 |
| 觀察到之來源 commit | 03d73cb900e28d7cd8ea02ec0c43c4564b521e33 | 準備來源包時觀察值 |
| 來源分支 | work/ttqs-one-document-quality-contract-20261016 | — |
| 文件狀態 | CANDIDATE / SAMPLE TEMPLATE / NOT ISSUED | 非 CURRENT、非 REAL、非 APPROVED |
| 核准 | **NOT_GRANTED** | 無人工來源，禁止核章 |
| 生效日期 | **NOT_ISSUED** | 禁止填寫生效日 |
| 真實證據現況 | **REAL EVIDENCE: NOT PROVIDED / UNKNOWN** | 本文件零真實來源仍可運作 |
| 版本 | R02 MANUSCRIPT | 文稿階段；非 DOCX、非驗收收據 |

**身份四分離原則（禁止混淆）：** 內部文件編號 `0136` ≠ 官方需求編號 `I19-E26` ≠ 專案 157 索引 `150` ≠ 官方印刷勾選序號（**UNKNOWN**）。任何表格、頁眉、頁尾、檢索清單中，四者必須各自獨立呈現，**不得互相代填**。

---

## 1. 快速使用與適用範圍（Quick Use & Scope）

### 1.1 一句話定位

本表是協會內部用來「**收件 → 保存 → 驗證 → 分類 → 檢索 → 複核**」他人提出之原件證據的**受控登錄表**；它記錄「**有人提出了一項主張，以及該主張對到了什麼來源**」，**不主張**協會已辦理任何活動、已獲得任何獎項、已完成任何學校合作。

### 1.2 誰負責、何時建列

| 情境 | 是否建列 | 負責人 |
|---|---|---|
| 任何人提出一項「我們參與公益／我們得獎／我們與學校合作」的證據或口頭主張 | **必須建列**（即使只有口頭主張） | 指定收件管理員（Intake Custodian） |
| 收到紙本正本、影本、掃描檔、電子郵件附件、公開網頁連結 | **必須建列** | 同上 |
| 同一事件被第二個人再次提出 | **不新建列**，掛入既有 `event_project_key` 之重複群組 | 複核人（Reviewer） |
| 僅為新聞報導、社群貼文 | **建列為定位器（locator）**，主證據欄位指向底下原件；若底下原件不存在則維持 PENDING_SOURCE | 同上 |
| 本表三類以外（市場/顧客價值趨勢、人時總數、會員會費） | **不建列**，依第 9 節改道至 0135 / 0133 / 0134 | 改道人 |

### 1.3 操作順序（六步）

1. **收件**：開立不可變 `record_id`，記錄收件日期、保管人，當場計算 SHA-256（第 3 節）。
2. **保存**：正本以唯讀方式入受限儲存；僅可公開的中繼資料進本表（第 3 節）。
3. **分類**：選定證據類別 A（公益活動）/ B（獎項）/ C（學校產學研發），進入對應驗證路徑（第 4 節）。
4. **驗證**：依 T3 核對「來源鑑真 / 協會角色 / 成果」三條獨立軌；任一軌未過，狀態不得為 VERIFIED_PRIMARY（第 4、6 節）。
5. **複核**：填 T1/T2/T3，複核人做判定；建置者不得自行判定（第 6 節）。
6. **歸檔與檢索**：產出 T5 允許措辭、T6 替換清單，完成第 11 節檢索測試。

### 1.4 狀態速查（完整定義見第 6 節）

| 狀態 | 一句話 | 可否計為協會表現 |
|---|---|---|
| `VERIFIED_PRIMARY` | 合法正本／第一方數位原件已取得、已雜湊、權威與關係已核、隱私已清 | 僅就**已記錄之限縮主張**成立 |
| `VERIFIED_SECONDARY` | 可歸屬的公開／第三方來源**僅**支持限縮主張，正本未持有 | 不得稱為「原件已驗證」 |
| `PENDING_SOURCE` | 來源缺，或發給方／參與者／成果未查 | **否** |
| `HOLD_PRIVACY` | 同意、法律基礎、去識別、存取或公布未解 | **否**，且不得公布 |
| `REJECTED` | 造假、 bounded 檢查後仍不可驗、無關、矛盾、無來源變造、重複計數、角色/成果未證 | **否** |
| `SAMPLE_ONLY` | 示範資料 | **永遠否** |

### 1.5 鐵律：登錄 ≠ 已驗證

> **「已登錄的主張（logged claim）」只是被收進來的敘述；只有當狀態升為 `VERIFIED_PRIMARY` 且 T3 三軌皆過，才代表「本表持有人確實檢視過一份可追溯來源」。** 即便如此，驗證的對象是「來源為真、角色如述」，**不是**「協會達成某成果」。

### 1.6 本表零真實來源仍可運作

當 `REAL EVIDENCE = NOT PROVIDED / UNKNOWN` 時：
- T1 可只含 `SAMPLE_ONLY` 列與 `PENDING_SOURCE` 空缺路徑列；
- 每個真實欄位以「**所需確切來源 + HOLD 條件**」表達（見 5.3 節），**不得**留下會被誤讀為已驗證的空白，亦**不得**使用未限定的「待填」；
- 第 12 節的放行/拒絕清單仍可逐項勾選。

---

## 2. 官方來源對照（Official-Source Mapping）

### 2.1 官方原文（逐字，跨印刷頁 8/9 頁斷）

> 提出參與社會公益活動、獲頒公民營單位獎項、結合學校單位產學或研發成果社會面。

**來源位置：** 指標 19「訓練系統的市場功能—目標市場及顧客的價值創造」項下，**高階水準**參考證據示例之一；該筆條目自印刷第 8 頁延續至第 9 頁。原始 PDF 與兩頁摘錄（`official_source.pdf`、`OFFICIAL_SOURCE_P8_P9_EXTRACT.pdf`、`OFFICIAL_SOURCE_P8_P9_TEXT.txt`）已隨來源包提供。

### 2.2 這句話**代表什麼**、**不代表什麼**

| 代表 | 不代表 |
|---|---|
| 官方列出的**參考證據類型示例** | 協會**已具備**這三類證據 |
| 三類可以**各自獨立**成立 | 不代表「三類必須同時存在」才算過 |
| 本表的**收錄範圍依據** | 不代表任何**評分、等第或通過與否** |
| 指標 19 高階水準的舉例敘述 | 不得由單一參考示例推導「協會在指標 19 得分為何」 |

### 2.3 權威對照（不得互相代填）

| 欄位 | 已驗證值 | 來源 | 狀態 |
|---|---|---|---|
| 專案 | TTQS_ONE | — | 已驗證 |
| 文件編號 | 0136 | 交叉對照 + seed 一致 | 已驗證 |
| 需求編號 | I19-E26 | `official_129_to_142_crosswalk.csv`：`I19-E26,1,0,0136,公益活動、獎項與學校合作原件驗證登錄表`；`blueprint_seed_142.csv`：`0136,I19-E26,0136__公益活動、獎項與學校合作原件驗證登錄表.docx` | 已驗證（兩來源獨立一致） |
| 標題 | 公益活動、獎項與學校合作原件驗證登錄表 | 同上 | 已驗證 |
| 專案 157 索引 | 150 — 公益/表揚/產學/研發社會影響：原件與來源 | `quality-review/0133_R01_20261024/source/PROJECT_157_BLUEPRINT_INDEX144_146_EXCERPT.md`（Git blob `c130800e924479e7d8d891f97ece21cd586c20ed`） | 已驗證，且**與印刷序號分離** |
| 官方印刷勾選序號 | **UNKNOWN** | 未經實體核對 | **不得代填** |
| 來源雜湊 | 見 `SOURCE_MANIFEST_0136_R01.json`、`qa/SOURCE_PREP_QA_0136_R01.json` | 隨來源包 | 已記錄 |

### 2.4 禁止事項

- **禁止自我評分**：本表不得填入任何 TTQS 評等、分數、比率、達成率或「通過／不通過」之官方結論。評分權屬評核程序，不屬本文件。
- **禁止以三類齊備作為過關條件**：一筆記錄**不得**為了「好看」而虛構齊備三類。
- **禁止以單一參考示例推論成果**：參考證據示例不等於證據存在。
- **禁止混淆索引與序號**：索引 150 內部規劃用；印刷勾選序號維持 UNKNOWN，須實體來源確認後才可由人工填入。

---

## 3. 收件與保全標準作業程序（Intake & Preservation SOP）

### 3.1 收件當場（T0，同一工作時段內完成）

| 步驟 | 動作 | 判定/記錄欄位 |
|---|---|---|
| 1 | 開立**不可變**記錄編號 | `record_id` 格式：`REG-0136-[CLASS]-[YYYY]-[NNNN]`，CLASS ∈ {ACT, AWD, SCH}；**一旦建立禁止改寫**，修正以 `correction_note` 追加 |
| 2 | 記錄收件 | `received_date`、`custodian`（角色代號，如 `CUST-ROLE-01`）、`delivery_channel`（親交/郵寄/電子郵件/受控上傳） |
| 3 | **不開啟修改**地計算檔案雜湊 | `exact_original_sha256`（SHA-256，小寫 hex 64 碼）、`byte_size` |
| 4 | 記錄格式與版本 | `format`（PDF/DOCX/JPG/紙本→掃描件等）、`format_version`、`page_or_item_locator`（頁/節/項次） |
| 5 | 分配來源層級 | `storage_tier` ∈ {T-RESTRICTED（正本/受限）, T-SANITIZED（可公開中繼資料）} |
| 6 | 指定存取群組 | `access_group`（見第 10 節） |
| 7 | 指定保管鏈 | `chain_of_custody` 首列：`IN | from | to | timestamp | reason` |

### 3.2 保全原則（不可違反）

1. **唯讀保存**：正本以唯讀/防篡改方式保存；任何轉檔產生的衍生檔**另立新 sha**，不得覆蓋原始 `exact_original_sha256`。
2. **原件不動**：不得在原件上書寫、蓋章、裁切、修圖；如需標註，於衍生副本進行並記錄衍生檔雜湊。
3. **先雜湊、後觀看內容**：先取得位元組層級完整性，再做語意驗證；若驗證過程發現檔案變動，立即記錄差異並轉 T4。
4. **雙軌存放**：
   - **T-RESTRICTED**：正本、含個資頁面、受限定位器（`restricted_original_locator`）→ 存於受限位置，**不上 GitHub**。
   - **T-SANITIZED**：僅中繼資料（不含個資、不含正本位址）→ 可進版本庫。
5. **公開/私有切割**：GitHub 只放 `safe_public_locator` 與去識別後的中繼資料；任何可識別個人之位址、信件抬頭、帳號、電話、住址一律留在 T-RESTRICTED。
6. **保管鏈不可斷**：每一次移交都要有一列（`transfer_id`、時間、交出角色、接收角色、原因、雙方確認）。鏈斷即轉 `HOLD_PRIVACY` 或 `PENDING_SOURCE` 並記入 T4。
7. **無法雜湊的紙本**：記錄「紙本正本 + 現場見證角色 + 收件日期 + 頁數 + 尺寸 + 獨特識別（浮水印/騎縫/流水號之**存在與否**）」，狀態**不得**因此升為 VERIFIED_PRIMARY，維持 `PENDING_SOURCE` 直至完成可信數位化與雙人覆核。

### 3.3 保管鏈日誌（每筆記錄必附）

| transfer_id | 時間戳 | 交出角色 | 接收角色 | 原因 | 位置/層級 | 確認 |
|---|---|---|---|---|---|---|
| CF-0136-…-001 | YYYY-MM-DDThh:mm | 提出者角色 | CUST-ROLE-01 | 初次收件 | T-RESTRICTED | 雙方確認欄 |
| CF-0136-…-002 | （範例） | CUST-ROLE-01 | VER-ROLE-02 | 驗證查核 | T-RESTRICTED | 雙方確認欄 |

> 鏈中任一列缺「原因」或「確認」，該筆不得升 `VERIFIED_PRIMARY`。

### 3.4 收件拒絕（不開列或開列即拒）

- 提出者拒絕提供可雜湊檔案、拒絕透露來源、要求「先寫成已驗證」→ 建列並直接 `REJECTED`（理由：不可驗/來源隱匿），保留審計註記，**不暴露來源細節**。
- 僅能提供「我們內部自己做的摘要」→ 建列 `PENDING_SOURCE`，摘要本身不作為原件。
- 檔案已損壞無法開啟 → 保留原位元組、記錄雜湊、`PENDING_SOURCE`，轉 T4 排程重新索取。

---

## 4. 三條獨立驗證路徑（Three Verification Workflows）

> **共同結構：每一類都把三條軌分開驗證，任一軌未過即不得為 VERIFIED_PRIMARY。**
> - **軌 I：來源鑑真（Source authenticity）** — 這份文件本身是不是真的、可否歸屬到宣稱的發出方？
> - **軌 II：協會角色（Association role）** — 協會在其中**實際**做了什麼？是否 `NOT ESTABLISHED`？
> - **軌 III：成果/影響（Outcome）** — 是否有**獨立來源**支持成果？無則 `UNKNOWN`，**不得推論**。

---

### 4.1 路徑 A：社會公益活動（Social-benefit activity）

**A-I 來源鑑真（事件本身）**

| # | 檢查 | 可接受來源 | 不可接受來源 |
|---|---|---|---|
| A1 | 主辦單位識別 | 主辦單位官方網站/正式公告/公文/可回訪之第一方聯絡窗口 | 轉發截圖、未署名海報 |
| A2 | 活動名稱、日期、地點 | 主辦單位活動辦法、正式議程、第一方活動紀錄 | 個人臉書貼文、自製時間軸 |
| A3 | 檔案完整性 | 正本或第一方數位檔（含雜湊） | 未標來源之翻拍、可編輯文字檔 |
| A4 | 一致性 | 名稱/日期/地點與其他來源不矛盾 | 與其他來源衝突且無解釋 |

**A-II 協會參與（與 A-I 分開）**

| # | 檢查 | 可接受來源 | 不可接受來源 |
|---|---|---|---|
| A5 | 協會**出席/參與** | 主辦單位出具之確認（邀請函回覆、出席名單之**主辦方持有版**、簽到之主辦方留存版）、或受控內部紀錄**經主辦方事後確認** | 單張合影、自我宣稱、己方自製簽到表**單獨**存在 |
| A6 | 協會**角色與實際貢獻** | 主辦單位對協會角色的敘述（承辦、協辦、資源提供、講者、志工團帶隊等）之**明確文字** | 只出現協會名稱而無角色文字 |
| A7 | 角色階層 | 講者/承辦 → 有角色文字 + 議程佐證；協辦 → 有聯合署名文件；出席 → 有主辦方確認 | 只有照片背景中有協會logo |

**A-III 成果/影響（與 A-II 分開，且**必**須各自建列）**

| # | 檢查 | 規則 |
|---|---|---|
| A8 | 受益人數 | 需**自己的**來源、**自己的**單位、**自己的**期間、**自己的**分母；缺一即 `UNKNOWN` |
| A9 | 捐贈/物資金額 | 需來源（收據/主辦方公告）+ 幣別 + 期間；不得由參與人數推算 |
| A10 | 志工時數 | 需工時紀錄 + 期間 + 口徑（人時 or 人日） |
| A11 | 觸及/曝光 | 需平台後台或可稽核公開數據 + 期間 + 口徑；不得以「廣泛好評」表述 |
| A12 | 因果/成效 | **禁止推論**；無獨立成效來源即 `UNKNOWN`，並在 `limitation` 註明 |

**A 路徑判定門檻**
- `VERIFIED_PRIMARY`：A1–A4 皆過 **且** A5/A6 至少一條過 **且** 隱私 cleared。**A8–A12 可為 UNKNOWN 而不阻擋 A-I/A-II 的成立**，但該筆**成果欄**維持 `PENDING_SOURCE`，整筆不得以「已達成成果」名義對外。
- **單獨不足以成立**：報名表、單張照片、宣傳貼文、活動花絮 —— 僅可作為 `VERIFIED_SECONDARY` 之佐證定位器或 `PENDING_SOURCE`。
- **報名 ≠ 參與；參與 ≠ 影響。**

---

### 4.2 路徑 B：公民營單位獎項（Award / recognition）

**B-I 來源鑑真（獎項本身）**

| # | 檢查 | 可接受來源 | 不可接受來源 |
|---|---|---|---|
| B1 | 頒發單位識別 | 頒發單位官方公告、官方獎項登錄/名冊、可回訪第一方窗口 | 來源不明的獎狀翻拍、論壇轉貼 |
| B2 | 獎項**確切**名稱/類別 | 與原件逐字一致之官方名稱與類別 | 簡稱、自創譯名、包裝用語 |
| B3 | 頒獎日期/期別 | 頒發方公告日期或原件載明日期 | 「去年」等模糊表述 |
| B4 | 受獎者身份 | **依原件所載**之受獎主體名稱逐字 | 由承辦人記憶填寫 |
| B5 | 評選標準/期別 | 公開評選辦法或頒發方說明 | 無辦法即記錄「未取得」 |
| B6 | 頒發方記錄可驗 | 公開獎項登錄網址（`safe_public_locator`）或頒發方書面確認 | 僅有己方留存獎狀**而無**任何外部可核點 |

**B-II 協會角色/受獎身份（與 B-I 分開）**

| # | 檢查 | 規則 |
|---|---|---|
| B7 | 原件所載受獎者是否為**協會本身** | 若受獎者為個人、會員或他方，協會角色**非**受獎者 → 記 `association_role = NOT ESTABLISHED`（就「協會得獎」而言）或如實記錄為「協辦/推薦單位」**且需來源** |
| B8 | 若為「推薦/提名」 | 明確記錄為 nomination，**不得**寫成得獎 |

**B-III 成果/影響**

| # | 規則 |
|---|---|
| B9 | 獎項**本身即為結果**（received award），但**不得**由獎項推論社會影響、服務量能或品質提升 |
| B10 | 由獎項推導「成效」一律 `UNKNOWN`，除非另有獨立成效來源（此時應另開一列） |

**B 路徑判定門檻**
- `VERIFIED_PRIMARY`：B1–B6 皆過 **且** B7 成立（受獎者=協會，或角色如實記錄）**且** 隱私 cleared **且** 依法取得公布同意（涉及個人姓名時）。
- **明確不足**（僅下列任一 → 最多 `VERIFIED_SECONDARY`，多為 `PENDING_SOURCE` 或 `REJECTED`）：
  - 提名資料 nomination
  - 申請表 application
  - 參與證明 participation certificate
  - 自撰成果摘要 self-written summary
  - 未經驗證之影像 unverified image
- **保護**：受獎人姓名、職稱、個資屬受限；公布前需 lawful disclosure consent，否則 `HOLD_PRIVACY`。

---

### 4.3 路徑 C：學校合作／產學／研發之社會面（School partnership / industry-academia / R&D social impact）

**C-I 來源鑑真（學校與專案）**

| # | 檢查 | 可接受來源 | 不可接受來源 |
|---|---|---|---|
| C1 | 學校/單位識別 | 學校官方頁面、系所/單位公開頁、第一方窗口 | 來源不明的合作照 |
| C2 | 專案/協議存在 | 簽署之合約、契約、專案任務書、學校承辦紀錄 | 僅 MOU 意向書**單獨**、僅會議紀錄 |
| C3 | 專案名稱/期間逐字 | 依合約/任務書所載 | 概括稱「產學合作中」 |
| C4 | 對方可回訪 | 學校承辦人或授權第一方窗口可確認 | 無法回訪且無第一方紀錄 |

**C-II 協會實際貢獻與交付（與 C-I 分開）**

| # | 檢查 | 規則 |
|---|---|---|
| C5 | 協會**實際**角色與工作項 | 需合約/任務書/工作分配之明確文字；無即 `NOT ESTABLISHED` |
| C6 | 協會**交付物（deliverable）** | 具名交付物 + 交付日期 + 接收方；「參與會議」不構成交付物 |
| C7 | 驗收/公開產出 | 學校或授權第一方之**驗收紀錄、成果報告簽收、公開產出頁面**；MOU 與會議**不能**證明完成 |

**C-III 社會面成果（與 C-II 分開）**

| # | 規則 |
|---|---|
| C8 | 研發成果之社會面需指明：**產出(output)**、**使用/使用情境(use/context)**、**社會效益來源(source of social benefit)** 三者**各自**有來源 |
| C9 | **禁止**在無證據下暗示商業化、社區改變、政策影響或普及效果 |
| C10 | 數字型社會效益須有分母與期間，否則 `UNKNOWN` |
| C11 | 標題含「產學」「研發」**不等於**已有社會影響 |

**C 路徑判定門檻**
- `VERIFIED_PRIMARY`：C1–C4 過 **且** C5/C6 至少一條過 **且**（若主張「已完成/有產出」）C7 過 **且** 隱私 cleared。C8–C11 可為 `UNKNOWN`，此時成果欄 `PENDING_SOURCE`，**不得**對外敘述社會影響。
- **單獨不足以成立**：MOU、會議紀錄、簽約合影、合作貼文。
- **注意**：成果若表現為新聞/媒體敘事，**本表只保留定位器**，主證據請改道 0137（見第 9 節）。

---

### 4.4 三路徑對照速查

| 面向 | A 公益活動 | B 獎項 | C 學校產學研發 |
|---|---|---|---|
| 軌 I 要證明 | 事件真實存在 | 獎項真實且如述頒發 | 學校/專案真實存在 |
| 軌 II 要證明 | 協會**實際參與角色與貢獻** | 受獎者=協會（或角色如實） | 協會**實際貢獻與交付物** |
| 軌 III 要證明 | 獨立來源之效益（含分母） | **通常不推論**（獎項即結果） | 產出+使用情境+效益來源 |
| 最常見誤判 | 照片=參與=影響 | 提名=得獎 | MOU=完成=社會影響 |
| 最弱可接受狀態 | VERIFIED_SECONDARY（限縮） | VERIFIED_SECONDARY（限縮） | VERIFIED_SECONDARY（限縮） |

---

## 5. 營運登錄表：欄位字典與表單（Operational Register & Field Dictionary）

### 5.1 T1 證據登錄表 — 欄位字典（每筆離散主張/來源一列）

> 表頭：**T1 證據登錄表（Evidence Register）｜ DOCX 0136 ｜ I19-E26 ｜ 索引 150 ｜ 印刷序號 UNKNOWN**

| # | 欄位 | 定義 | 填寫規則 | 允許值/格式 | 空白是否允許 |
|---|---|---|---|---|---|
| 1 | `record_id` | 不可變記錄編號 | 建立後禁改 | `REG-0136-[ACT\|AWD\|SCH]-YYYY-NNNN` | 否 |
| 2 | `evidence_class` | 證據類別 | 對應第 4 節路徑 | `A\|B\|C` | 否 |
| 3 | `shared_event_project_key` | 跨表共用事件/專案鍵 | 同事件/專案一律共用，供去重 | `EVT-…` / `PRJ-…` | 否 |
| 4 | `docx_id` | 文件編號 | 固定 | `0136` | 否 |
| 5 | `requirement_id` | 需求編號 | 固定 | `I19-E26` | 否 |
| 6 | `project_index` | 專案 157 索引 | 固定（**非**序號） | `150` | 否 |
| 7 | `printed_checkbox_serial` | 印刷勾選序號 | **未經實體核對** | `UNKNOWN` | 否（不得代填） |
| 8 | `neutral_claim` | 中性主張 | 只寫「可被來源支持的事」，不含評價詞 | 自由文本 ≤ 200 字 | 否 |
| 9 | `counterparty_category` | 對方類別 | 用**類別**不用真名 | 主辦單位／頒發單位／學校單位／協力單位；SAMPLE 時用「示例…」 | 否 |
| 10 | `association_role` | 協會角色 | 無來源即 `NOT ESTABLISHED` | 文本 或 `NOT ESTABLISHED` | 否 |
| 11 | `event_project_award_date` | 事件/專案/獎項日期或期間 | 不確定寫 `UNKNOWN`，禁猜 | `YYYY-MM-DD` 或 `YYYY-MM-DD/…` 或 `UNKNOWN` | 否 |
| 12 | `source_record_date` | 來源文件自身日期 | 與活動日期分開 | 同上 | 否 |
| 13 | `custodian` | 保管人 | 用角色代號 | `CUST-ROLE-nn` | 否 |
| 14 | `original_evidence_type` | 原件類型 | 例：紙本獎狀正本、第一方 PDF | 枚舉+自由文本 | 否 |
| 15 | `authority` | 權威來源主體 | 誰有資格發出 | 類別/代碼 | 否 |
| 16 | `source_title` | 來源標題（逐字） | 不改寫 | 文本 | 否 |
| 17 | `restricted_original_locator` | 受限正本位址 | **僅**存 T-RESTRICTED | 路徑/保管編號 | 否（無則 `UNKNOWN` + 原因） |
| 18 | `safe_public_locator` | 可公開定位器 | 可無 | URL/庫存號 或 `NOT_APPLICABLE`+原因 | 否 |
| 19 | `page_section_item_locator` | 頁/節/項次 | 精確到項 | 例：`p.2 §3 表1 第5列` | 否 |
| 20 | `format_version` | 格式/版本 | 例 `PDF/1.7`、`A4 第2版` | 文本 | 否 |
| 21 | `exact_original_sha256` | 正本 SHA-256 | 小寫 hex | 64 碼 或 `UNKNOWN`+原因（紙本） | 否 |
| 22 | `capture_date` | 雜湊/擷取日期 | — | `YYYY-MM-DD` | 否 |
| 23 | `custody_transfers` | 保管鏈 | 對應 T2 | `CF-…` 清單 | 否 |
| 24 | `verification_method` | 驗證方法 | 逐字描述做法 | 文本 | 否 |
| 25 | `verification_endpoint` | 驗證端點 | 回訪之第一方窗口/URL | 文本 或 `UNKNOWN` | 否 |
| 26 | `verification_date` | 驗證日期 | — | `YYYY-MM-DD` | 否 |
| 27 | `verifier_role` | 驗證者角色 | 非建置者 | `VER-ROLE-nn` | 否 |
| 28 | `check_result` | 三軌結果 | 分軌記錄 | `I/II/III: PASS\|FAIL\|UNKNOWN` | 否 |
| 29 | `party_identity_checked` | 對方身份是否核 | — | `YES/NO/UNKNOWN` | 否 |
| 30 | `actual_participation_or_contribution` | 實際參與/受獎/貢獻 | 逐字/量化皆需來源 | 文本 或 `NOT ESTABLISHED` | 否 |
| 31 | `social_outcome` | 社會成果 | **獨立**於 30 | 文本 或 `UNKNOWN` | 否 |
| 32 | `outcome_denominator` | 數值之分母/單位/期間 | 數值必填三件套 | `n / unit / period` 或 `NOT_APPLICABLE`+原因 | 數值時否 |
| 33 | `relevance_rationale` | 相關性理由 | 為何屬指標 19 參考證據範圍 | 文本 | 否 |
| 34 | `evidence_status` | 狀態 | 見第 6 節 | 6 態枚舉 | 否 |
| 35 | `primary_secondary_class` | 主/次證據類 | 正本=PRIMARY；僅第三方=SECONDARY | `PRIMARY\|SECONDARY\|NONE` | 否 |
| 36 | `limitations` | 限制 | 必須**可見** | 文本 | 否（無則 `NONE_RECORDED`） |
| 37 | `duplicate_group` | 重複群組 | 對應第 9 節 | `DG-…` 或 `NONE` | 否 |
| 38 | `consent_legal_basis` | 同意/法律基礎 | 個資必填 | 文本 或 `NOT_APPLICABLE`+原因 | 否 |
| 39 | `data_class_access_group` | 資料分級/存取群組 | 見第 10 節 | `RESTRICTED/INTERNAL/SANITIZED` + 群組碼 | 否 |
| 40 | `retention_review_date` | 保留覆核日 | **不得自行編年** | `HOLD - NO SCHEDULE` 或 依核准表日期 | 否 |
| 41 | `decision` | 判定 | 複核人填 | 見第 6 節 | 否 |
| 42 | `decision_reason` | 判定理由 | 引 T3 項號 | 文本 | 否 |
| 43 | `reviewer_role_date` | 複核角色/日期 | — | `REV-ROLE-nn / YYYY-MM-DD` | 否 |
| 44 | `correction_note` | 修正註記 | 追加不覆寫 | 文本 或 `NONE` | 否 |
| 45 | `owner_due_date` | 待辦負責/到期 | PENDING/HOLD 必填 | 角色 + `YYYY-MM-DD` | 態為 PENDING/HOLD 時否 |
| 46 | `safe_retrieval_instruction` | 安全檢索指引 | 讓第三方重複驗證 | 文本 | 否 |
| 47 | `countable_for_performance` | 可否計為表現 | 系統依狀態推導 | `NO`（預設）/`LIMITED-TO-CLAIM` | 否 |

**空值語意（三值紀律）**
- `UNKNOWN` = 查了但不知道 / 未查 → **明示不知道**。
- `NOT_APPLICABLE` + **原因** = 此欄對本筆不適用 → 必須附原因，否則不合法。
- **空白 = 禁止**。空白會被誤讀為「已驗證」，任何情況下不得以空白表達未填。

---

### 5.2 T1 空白表單（可直接使用）

**T1 證據登錄表（每筆離散主張/來源一列）**

| record_id | class | event_project_key | docx | req | index | printed_serial | neutral_claim | counterparty_category | association_role | event/project/award date | source_record_date | custodian | original_type | authority | source_title | restricted_locator | safe_public_locator | page/section/item | format/version | sha256 | capture_date | custody | verify_method | endpoint | verify_date | verifier_role | I/II/III result | party_identity | actual_participation/contribution | social_outcome | denominator (n/unit/period) | relevance_rationale | status | primary/secondary | limitations | duplicate_group | consent/legal_basis | data_class/access | retention_review_date | decision | decision_reason | reviewer/date | correction_note | owner/due | safe_retrieval_instruction | countable |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| （格式：REG-0136-—…；禁改） | A/B/C | EVT-/PRJ- | 0136 | I19-E26 | 150 | **UNKNOWN** |  | 類別（SAMPLE 用「示例…」） | 文本 或 `NOT ESTABLISHED` | 日期或 `UNKNOWN` | 日期或 `UNKNOWN` | CUST-ROLE-nn |  |  |  | 受限位址或 `UNKNOWN`+原因 | URL 或 `NOT_APPLICABLE`+原因 |  |  | 64hex 或 `UNKNOWN`+原因 |  | CF-… |  |  |  |  | I:/II:/III: | YES/NO/UNKNOWN |  |  |  |  |  | PRIMARY/SECONDARY/NONE |  | DG-/NONE |  |  | `HOLD - NO SCHEDULE` 或 核准日 |  |  | REV-ROLE-nn/日期 |  |  |  | NO/LIMITED-TO-CLAIM |

---

### 5.3 真實證據區（REAL evidence area）— 現況：**NOT PROVIDED / UNKNOWN**

> **真實紀錄區狀態：REAL EVIDENCE NOT PROVIDED / UNKNOWN。**
> 以下每一欄**不得**留下會被誤讀為已核的空白，也**不得**使用未限定的「待填」；每一欄以「**所需確切來源 + HOLD 條件**」表達。

| 真實欄位 | 目前狀態 | **所需確切來源（Required real source）** | HOLD 條件（滿足前維持 PENDING_SOURCE / HOLD_PRIVACY） |
|---|---|---|---|
| 真實公益活動紀錄 | NOT PROVIDED / UNKNOWN | 主辦單位第一方活動紀錄（活動辦法、議程、主辦方持有之出席/角色紀錄）＋主辦單位可回訪窗口 | 主辦方拒絕確認、僅有己方照片/貼文、日期地點矛盾 → `PENDING_SOURCE` 或 `REJECTED` |
| 真實獎項原件 | NOT PROVIDED / UNKNOWN | 頒發單位之獎狀正本或第一方數位檔 **＋** 頒發方公開獎項登錄/名冊或書面確認 | 僅提名/申請/參與證明/自撰摘要/未驗影像 → `PENDING_SOURCE`；確認造假 → `REJECTED` |
| 真實學校合作/產學研發紀錄 | NOT PROVIDED / UNKNOWN | 已簽署合約/契約/專案任務書 ＋ 學校授權第一方之驗收紀錄或公開產出 | 僅 MOU/會議紀錄/簽約合影 → `PENDING_SOURCE` |
| 真實社會面成果 | NOT PROVIDED / UNKNOWN | 獨立於上項的效益來源（含明確分母、單位、期間） | 無分母/無期間/由參與或獎項推論 → `UNKNOWN`，成果欄 `PENDING_SOURCE` |
| 可公開正本位址 | NOT PROVIDED / UNKNOWN | 經授權可公開之官方 URL ＋ 其雜湊 | 無授權或含個資 → `HOLD_PRIVACY`，僅存受限層 |
| 印刷勾選序號 | **UNKNOWN** | 實體/官方文件上的印刷序號（人工核對後填入） | 未核對前**禁止**以 0136 / I19-E26 / 150 代填 |
| 核准與生效 | **NOT_GRANTED / NOT_ISSUED** | 人工來源之核准紀錄（含核准者角色與日期） | 無人工來源 → 永遠維持 NOT_GRANTED / NOT_ISSUED |

---

### 5.4 T2 原件清單與保全（Original Inventory & Custody）

**T2｜DOCX 0136 ｜ I19-E26 ｜ 索引 150 ｜ 印刷序號 UNKNOWN**

| record_id | sha256（64hex 或 UNKNOWN+原因） | bytes | format | format_version | page/item locator | receipt_date | 入庫角色 | transfer_id | 從 → 到 | 時間戳 | 原因 | storage_tier | access_group | disclosure（可否公開/依據） |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  | T-RESTRICTED / T-SANITIZED |  | ALLOWED / DENIED / HOLD_PRIVACY |

**T2 填寫要點**
1. `bytes` 與 `sha256` 必須同時存在；缺一 → 該筆不得 `VERIFIED_PRIMARY`。
2. `receipt_date` 與 `source_record_date`（文件自身日期）分開填，**不得互代**。
3. 每次移動**新增一列**，不得覆寫舊列。
4. `disclosure = HOLD_PRIVACY` 時，T-SANITIZED 層不得寫入任何位址或個資。

---

### 5.5 T3 驗證核對表（Verification Checklist）

**T3｜按筆填寫；建置者不可自判，複核者逐項簽**

| 項 | 檢查項 | 通過標準 | 結果 | 證據定位（頁/節/項） | 檢查角色/日期 |
|---|---|---|---|---|---|
| T3-1 | 權威 authority | 發出方確實有資格發出該文件 | PASS/FAIL/UNKNOWN |  |  |
| T3-2 | 完整性 integrity | sha256 與取得時一致；無未解釋變更 | PASS/FAIL/UNKNOWN |  |  |
| T3-3 | 對方身份 party identity | 宣稱之主辦/頒發/學校可回訪確認 | PASS/FAIL/UNKNOWN |  |  |
| T3-4 | 協會角色 role | 有**明確文字**支持實際角色/貢獻，否則 `NOT ESTABLISHED` | PASS/FAIL/UNKNOWN |  |  |
| T3-5 | 成果 outcome | **獨立**來源＋分母＋期間；無則 `UNKNOWN` | PASS/FAIL/UNKNOWN |  |  |
| T3-6 | 相關性 relevance | 屬指標 19 參考證據範圍，且非鄰居範圍 | PASS/FAIL/UNKNOWN |  |  |
| T3-7 | 隱私 privacy | 最小化、法律基礎、去識別、存取、公布同意 | PASS/FAIL/UNKNOWN |  |  |
| T3-8 | 重複 duplicate check | `shared_event_project_key` + `duplicate_group` 已查，無雙計 | PASS/FAIL/UNKNOWN |  |  |
| T3-9 | 複核判定 reviewer decision | 依第 6 節門檻判定並署角色/日期 |  |  |  |

**T3 判讀**
- T3-1/2/3 任一 FAIL → 該筆 `REJECTED`（若 bounded 檢查後仍不可驗）或 `PENDING_SOURCE`（若僅缺來源）。
- T3-4 FAIL（無角色文字）→ `association_role = NOT ESTABLISHED`，狀態最高 `PENDING_SOURCE`。
- T3-5 UNKNOWN → 成果欄維持 `UNKNOWN`/`PENDING_SOURCE`；**不得**以 T3-1..4 通過而暗示成果。
- T3-7 FAIL → `HOLD_PRIVACY`，**禁止公布、禁止計數**。
- T3-9 由**非建置者**簽署；`BUILD_OWNER = REVIEW_OWNER` 時該判定無效，需另派複核角色。

---

### 5.6 T4 HOLD / REJECTED / 修正日誌

**T4｜任何失敗檢查、修正、重檢皆留痕**

| log_id | record_id | failed_check（T3 項號） | 判定類別 | 問題描述（不含受限來源細節） | 採取行動 | owner | due_date | 重檢結果 | 重檢角色/日期 | 關閉理由 |
|---|---|---|---|---|---|---|---|---|---|---|
| HRC-0136-… |  |  | HOLD_PRIVACY / REJECTED / CORRECTION |  |  |  |  | PASS/FAIL |  |  |

**T4 使用規則**
1. **不暴露來源**：問題描述欄不得抄錄受限定位器、個資或來源內容；只寫檢查項與結論。
2. **修正以追加**：`correction_note` 與 T4 新列，不得回改 T1 已判定列的歷史值。
3. **兩次失敗即停該線**：同一邏輯缺陷連續兩輪重檢仍 FAIL → **停止該確切筆的重建**，改做根因檢視（來源是否根本不存在？），修復驗證契約後，**僅在有實質新來源**時才重啟；**不得**僅因兩次失敗就上呈人工。
4. **其他 READY 線不因單筆 HOLD/REJECTED 停擺**。
5. `REJECTED` 仍保留審計列（供追溯），但不得暴露來源。

---

### 5.7 T5 主張—來源對照（Claim-to-Source Matrix）

**T5｜每一項「可對外/對評委陳述的主張」都必須能指到一個確切來源；不能指到就不陳述**

| claim_id | 對外允許措辭（allowed wording） | 來源類型 | 確切原件/頁碼（原件） | 或 官方 URL | 或 sha256 | status | 禁止措辭（不得使用） |
|---|---|---|---|---|---|---|---|
| CL-… | 例：「本會於示例期間參與由示例主辦單位辦理之示例活動，角色如來源所載。」 | 原件/第一方 | p./§/項 | （若有） |  | VERIFIED_* / PENDING_SOURCE / HOLD_PRIVACY / REJECTED / SAMPLE_ONLY | 例：「本會透過該活動達成顯著社會影響」（無獨立成果源時**禁止**） |

**T5 三分欄原則**：一列只能落在「原件定位」「官方 URL」「sha256」**其中可支持者**；若只有第三方報導 → 欄位填「定位器」，`status` 最高 `VERIFIED_SECONDARY`，且 `allowed wording` 必須降格為「據〈第三方名稱〉報導…」，**不得**稱原件已驗證。

**允許/禁止措辭範例（依類別）**

| 類別 | 允許（有對應來源時） | 禁止 |
|---|---|---|
| A | 「參與（主辦單位）辦理之（活動名稱），角色為（角色）。」 | 「參與後改善了（弱勢群體）處境。」（無獨立成果源） |
| B | 「獲（頒發單位）頒發（獎項全名/類別），日期（日期），受獎者依原件所載為（主體）。」 | 「獲獎證明本會服務品質達業界標竿。」 |
| C | 「與（學校/單位）就（專案名稱）合作，協會交付（交付物），驗收依（驗收紀錄）。」 | 「透過產學合作產生重大社會影響／已成功商品化。」（無 C8 來源） |

---

### 5.8 T6 合成替換登記表（Synthetic Replacement Register）

> **完整清單見第 11 節。** T6 與第 11 節為同一控制的表單形式：**每一筆合成事實（欄位、角色、日期、發出方、成果、狀態、來源定位器）各佔一列**，並註明「**所需確切真實來源**」。

---

## 6. 判定、權責與狀態（Decision Authority & Statuses）

### 6.1 狀態定義與門檻

| 狀態 | 成立門檻（全部滿足） | 明確**不**成立於 | 計數規則 |
|---|---|---|---|
| `VERIFIED_PRIMARY` | (1) 取得合法正本或可驗第一方數位來源；(2) 確切位元組已雜湊；(3) 權威與當事方/角色已核；(4) 相關性已記錄；(5) 隱私 cleared；(6) T3-1..4 皆 PASS | 只有己方副本、只有照片/貼文、鏈斷 | 僅「限縮至已記錄主張」 |
| `VERIFIED_SECONDARY` | (1) 真實且可歸屬的公開/第三方來源；(2) **僅**支持限縮主張；(3) 限制**visible**；(4) 正本未持有之事實**明示** | 被描述為「原件已驗證」 | 可作佐證，**不得**當正本 |
| `PENDING_SOURCE` | 來源不存在/未取得，或發給方、參與者、成果未查 | 任何 VERIFIED_* | **不可計** |
| `HOLD_PRIVACY` | 同意、法律基礎、去識別、存取或公布任一未解 | 可公布或可計數 | **不可計、不可公布** |
| `REJECTED` | (a) 造假；(b) bounded 檢查後仍不可驗；(c) 無關；(d) 矛盾；(e) 無來源變造；(f) 重複計數；(g) 未能證明角色/成果 — 任一 | — | **不可計**，保留審計 |
| `SAMPLE_ONLY` | 示範資料 | 任何 REAL 用途 | **永不計**，永不入表現/評分 |

### 6.2 判定權責（Decision Authority）

| 判定/動作 | 可執行角色 | 不可執行 |
|---|---|---|
| 開列 `record_id`、記錄收件、雜湊 | Intake Custodian | — |
| 執行 T3 檢查 | Verifier（`VER-ROLE-nn`） | 同筆之建置者 |
| **授予** `VERIFIED_PRIMARY` / `VERIFIED_SECONDARY` | Reviewer（`REV-ROLE-nn`），且 ≠ 建置者 | 建置者自判（`BUILD_OWNER = REVIEW_OWNER` 無效） |
| 裁 `REJECTED` | Reviewer；或 T3-1/2/3 直接 FAIL 之自動規則後由 Reviewer 確認 | 提出者自裁 |
| 裁 `HOLD_PRIVACY` | Custodian 或 Privacy role，**任一人**可觸發，**僅** Privacy/Reviewer 可解除 | 一般使用者解除 |
| 解除 HOLD | Privacy role + Reviewer 雙方，且需記 T4 | 單方解除 |
| 升級（Escalation） | 依 6.3 | — |
| 修正歷史值 | 以 `correction_note` + T4 追加 | 回改原列 |
| **賦予 APPROVED/EFFECTIVE** | **僅人工來源（Human source）** | 本表任何角色（本文件維持 NOT_GRANTED/NOT_ISSUED） |
| **TTQS 評分** | 評核程序 | **本表任何人，禁止自我評分** |

### 6.3 證據充分性與升級（Escalation）

**充分性規則**
1. **三軌分立**：來源真 + 角色實 + 成果有據，**各自**成立；不得以一軌替代另一軌。
2. **最小充分**：`VERIFIED_PRIMARY` 只對**已記錄的那一條限縮主張**充分，不外擴。
3. **推論禁止**：出席、夥伴名義、獎項、媒體報導**四者皆不得**推導數值影響或因果。
4. **分母強制**：任何數值效益必附 `n / unit / period`，否則改寫為定性或 `UNKNOWN`。

**升級觸發（非人工門檻，僅內部位階升級）**
- 疑似偽造/變造 → Reviewer → 保留證據、`REJECTED`、記 T4，**不外流**。
- 疑似個資外洩 → Privacy role → 立即轉 `HOLD_PRIVACY`、暫停公布、記 T4 事件列。
- 兩輪重檢失敗同缺陷 → 停該筆、做根因檢視 → 有實質新來源才重啟。
- 需要**人工決斷**之情形（見 AGENTS 之 Human Gate）：範圍/規範變更、SAMPLE vs REAL 權限歧義、法律/簽章/身份、第三方正本**確實無法取得**且實質改變交付、最終驗收。**單筆失敗、驗證器缺陷、個別筆停擺都不是人工門檻。**

---

## 7. 三個完整 SAMPLE / SYNTHETIC 走查（Worked Examples）

> **全區警示：以下三筆皆為 SAMPLE / SYNTHETIC — NOT REAL EVIDENCE。**
> - 未附任何真實原件；無真實頒發單位、無真實合作夥伴、無真實人名、無真實簽名、無真實核准。
> - **不主張**協會曾辦理任何活動、獲得任何獎項、完成任何學校合作。
> - **不得計數**為協會表現，**不得**用於評分。
> - 每一項合成事實（含欄位、角色、日期、發出方、成果、狀態、來源定位器）皆列入**第 11 節替換登記表**。
> - 合成 ID 一律以 `SAMP-` 前綴；對手方一律使用**通用類別標籤**（「示例主辦單位甲」等）。

---

### 走查 1（類別 A：社會公益活動）`SAMPLE_ONLY`

| T1 欄位 | 值（SAMPLE / SYNTHETIC） |
|---|---|
| record_id | `REG-0136-ACT-2026-0001`（SAMP） |
| evidence_class | A |
| shared_event_project_key | `EVT-SAMP-A-01` |
| docx_id / req / index / printed | 0136 / I19-E26 / 150 / **UNKNOWN** |
| neutral_claim | 「示例主辦單位甲」於示例日期辦理示例公益活動，協會以示例角色參與。 |
| counterparty_category | 主辦單位（示例；無真實單位） |
| association_role | 示例協辦角色（**合成**；真實情形應為 `NOT ESTABLISHED` 直至有來源） |
| event date | 2026-05-17（**合成**） |
| source_record_date | 2026-05-20（**合成**） |
| custodian | `CUST-ROLE-01`（角色代號，非真人） |
| original_evidence_type | 第一方活動紀錄 PDF（**合成描述；未附任何實際檔案**） |
| authority | 「示例主辦單位甲」（**合成類別**） |
| source_title | 示例活動紀錄（合成標題） |
| restricted_original_locator | `UNKNOWN — 真實正本 NOT PROVIDED`（**未附**） |
| safe_public_locator | `NOT_APPLICABLE（無授權公開位址）+ 原因` |
| page/section/item | `UNKNOWN`（無實際檔案可定位） |
| format/version | `UNKNOWN` |
| exact_original_sha256 | `UNKNOWN（未附任何實際位元組）` |
| capture_date | `NOT_APPLICABLE（無擷取）+ 原因：示範列無實際檔案` |
| custody | `CF-SAMP-A-01`：IN `提出者角色(示例)` → `CUST-ROLE-01`，**合成** |
| verification_method | 以**想像中**之第一方回訪流程示範 T3-1..8 欄位用法 |
| endpoint | `UNKNOWN（無真實窗口）` |
| verification_date / role | `NOT_APPLICABLE + 原因` / `VER-ROLE-02`（角色代號） |
| check_result | I: **UNKNOWN**（未做真實驗證）／II: **UNKNOWN**／III: **UNKNOWN** |
| party_identity_checked | **NO** |
| actual_participation | **未建立 — NOT ESTABLISHED**（無來源） |
| social_outcome | **UNKNOWN** |
| outcome_denominator | `NOT_APPLICABLE + 原因：無任何數值主張` |
| relevance_rationale | 對應官方 p8–9「參與社會公益活動」參考證據類型 |
| evidence_status | **`SAMPLE_ONLY`** |
| primary/secondary | `NONE`（未持有任何正本） |
| limitations | **「本列純示範；未附原件；無真實活動；不得計數。」** |
| duplicate_group | `DG-SAMP-A-01` |
| consent/legal_basis | `NOT_APPLICABLE + 原因：無真實個資` |
| data_class/access | `SANITIZED / DEMO-GROUP` |
| retention_review_date | **`HOLD — NO SCHEDULE`**（無核准保留表） |
| decision | `SAMPLE_ONLY` |
| decision_reason | 為示範欄位與流程而建列；T3 三軌皆未做真實驗證 |
| reviewer/date | `REV-ROLE-03 / 2026-10-27`（角色代號＋文稿日期，**非核准**） |
| correction_note | `NONE` |
| owner/due | `CUST-ROLE-01 / NOT_APPLICABLE + 原因：示範列無待辦` |
| safe_retrieval_instruction | 僅供閱讀本節；無可檢索真實來源 |
| countable | **`NO`** |

**走查 1 判讀（示範錯誤情形）**
- 即使有人提供了照片、報名表或宣傳貼文，**A5 仍不成立** → 狀態只能 `PENDING_SOURCE`。
- 若此列被誤植為 VERIFIED_PRIMARY → 立即 T4 記錄、更正狀態，並追加 `correction_note`（**不回改原列歷史值**）。
- **本列不主張任何真實活動。**

---

### 走查 2（類別 B：公民營單位獎項）`SAMPLE_ONLY`

| T1 欄位 | 值（SAMPLE / SYNTHETIC） |
|---|---|
| record_id | `REG-0136-AWD-2026-0002`（SAMP） |
| evidence_class | B |
| shared_event_project_key | `EVT-SAMP-B-01` |
| docx / req / index / printed | 0136 / I19-E26 / 150 / **UNKNOWN** |
| neutral_claim | 「示例頒發單位乙」就示例獎項類別頒予示例受獎主體（**合成**）。 |
| counterparty_category | 頒發單位（示例；無真實頒發方） |
| association_role | **`NOT ESTABLISHED`** — **示範「角色未建立」的正確填法**（原件所載受獎者非協會，或未有來源） |
| award date | `UNKNOWN`（**合成列未給日期**） |
| source_record_date | `UNKNOWN` |
| custodian | `CUST-ROLE-01` |
| original_evidence_type | 「示例獎狀之**描述**」— **未附任何實際獎狀、影本或影像** |
| authority | 「示例頒發單位乙」（**合成類別**） |
| source_title | `UNKNOWN（未提供）` |
| restricted_original_locator | `UNKNOWN — 真實正本 NOT PROVIDED` |
| safe_public_locator | `NOT_APPLICABLE + 原因：無官方獎項登錄可提供` |
| page/section/item | `NOT_APPLICABLE + 原因：無實際檔案` |
| format/version | `UNKNOWN` |
| sha256 | `UNKNOWN（無實際位元組）` |
| custody | `CF-SAMP-B-01`（**合成**） |
| verification_method | 示範 B1–B6 欄位；**未執行任何真實查核** |
| endpoint | `UNKNOWN` |
| check_result | I: **UNKNOWN**／II: **FAIL（角色未建立）**／III: `NOT_APPLICABLE + 原因：獎項本身不推論影響` |
| party_identity_checked | **NO** |
| actual_participation | 受獎者如原件所載 — **原件未提供 → UNKNOWN** |
| social_outcome | **UNKNOWN**（B10：不得由獎項推論） |
| denominator | `NOT_APPLICABLE + 原因：無數值主張` |
| relevance_rationale | 對應官方 p8–9「獲頒公民營單位獎項」參考證據類型 |
| evidence_status | **`SAMPLE_ONLY`** |
| primary/secondary | `NONE` |
| limitations | **「示範列；未附獎狀、公告或登錄；角色 NOT ESTABLISHED；不得稱本會得獎。」** |
| duplicate_group | `DG-SAMP-B-01` |
| consent/legal_basis | `NOT_APPLICABLE + 原因：無真實個資；若真實含姓名須另取得公布同意` |
| data_class/access | `SANITIZED / DEMO-GROUP` |
| retention_review_date | **`HOLD — NO SCHEDULE`** |
| decision | `SAMPLE_ONLY` |
| decision_reason | 示範「提名≠得獎」「角色 NOT ESTABLISHED」之填法 |
| reviewer/date | `REV-ROLE-03 / 2026-10-27`（非核准） |
| countable | **`NO`** |

**走查 2 判讀（示範最常見誤判）**
- 提名函、申請表、參與證明、自撰摘要、未驗證影像 → **皆不足**為「獲獎」。
- 受獎者非協會 → `association_role = NOT ESTABLISHED`，**不得**寫成協會得獎。
- **本列不主張任何真實獎項。**

---

### 走查 3（類別 C：學校合作／產學研發之社會面）`SAMPLE_ONLY`

| T1 欄位 | 值（SAMPLE / SYNTHETIC） |
|---|---|
| record_id | `REG-0136-SCH-2026-0003`（SAMP） |
| evidence_class | C |
| shared_event_project_key | `PRJ-SAMP-C-01` |
| docx / req / index / printed | 0136 / I19-E26 / 150 / **UNKNOWN** |
| neutral_claim | 「示例學校單位丙」與協會就示例專案合作；協會角色與交付物**如實記錄為未建立**。 |
| counterparty_category | 學校單位（示例；無真實學校） |
| association_role | **`NOT ESTABLISHED`**（無合約/任務書文字支持） |
| project period | `UNKNOWN` |
| source_record_date | `UNKNOWN` |
| custodian | `CUST-ROLE-01` |
| original_evidence_type | 「示例合作意向文件之**描述**」— **未附任何合約、MOU 或驗收紀錄** |
| authority | 「示例學校單位丙」（**合成類別**） |
| source_title | `UNKNOWN（未提供）` |
| restricted_original_locator | `UNKNOWN — 真實正本 NOT PROVIDED` |
| safe_public_locator | `NOT_APPLICABLE + 原因：無授權公開頁` |
| page/section/item | `NOT_APPLICABLE + 原因：無實際檔案` |
| format/version | `UNKNOWN` |
| sha256 | `UNKNOWN（無實際位元組）` |
| custody | `CF-SAMP-C-01`（**合成**） |
| verification_method | 示範 C1–C11 欄位；**未執行真實查核** |
| endpoint | `UNKNOWN` |
| check_result | I: **UNKNOWN**（僅有意向層文件時 C2 FAIL）／II: **FAIL（無貢獻文字）**／III: **UNKNOWN** |
| party_identity_checked | **NO** |
| actual_participation/contribution | **NOT ESTABLISHED**；交付物：**UNKNOWN**；驗收：**UNKNOWN** |
| social_outcome | **UNKNOWN**（C8 三要素：產出/使用情境/效益來源 皆無來源） |
| denominator | `NOT_APPLICABLE + 原因：無數值主張` |
| relevance_rationale | 對應官方 p8–9「結合學校單位產學或研發成果社會面」參考證據類型 |
| evidence_status | **`SAMPLE_ONLY`** |
| primary/secondary | `NONE` |
| limitations | **「示範列；未附合約/任務書/驗收；MOU 與會議紀錄不能證明完成或社會影響；不得計數。」** |
| duplicate_group | `DG-SAMP-C-01` |
| consent/legal_basis | `NOT_APPLICABLE + 原因：無真實個資` |
| data_class/access | `SANITIZED / DEMO-GROUP` |
| retention_review_date | **`HOLD — NO SCHEDULE`** |
| decision | `SAMPLE_ONLY` |
| decision_reason | 示範「MOU≠完成≠社會影響」；三軌皆未建立 |
| reviewer/date | `REV-ROLE-03 / 2026-10-27`（非核准） |
| countable | **`NO`** |

**走查 3 判讀**
- 若真實只有 MOU → C7 FAIL → 「已完成」**不得**陳述；狀態 `PENDING_SOURCE`。
- 社會面若表現為新聞敘事 → 本表僅留定位器，主證據改道 **0137**。
- **本列不主張任何真實學校合作、產學或研發成果。**

---

### 7.4 三筆走查的共同聲明（每筆必附）

1. **未附任何真實原件** — 無證書、無信函、無 MOU、無簽到、無獎項登錄、無簽名、無核准、無真實人名/單位名/受益人數。
2. **無真實協會活動、獎項或夥伴關係之主張。**
3. **不可計數**：`countable_for_performance = NO`；永不進入表現彙總或評分。
4. **全部事實皆入 T6/第 11 節替換登記表。**
5. **狀態一律 `SAMPLE_ONLY`**，**不得**升級為任何 `VERIFIED_*`（除非未來以真實來源**另開新列**，而非改寫本列）。

---

## 8. 跨證據非重複控制（Cross-Evidence / Non-Duplication Control）

### 8.1 共用鍵與去重

- 每筆必填 `shared_event_project_key`（`EVT-…` 或 `PRJ-…`），同一事件/專案的多份來源共用同一鍵。
- 同鍵多列時，**僅一列**可為 `PRIMARY`，其餘標 `SECONDARY` 或併入 `duplicate_group (DG-…)`。
- **雙計禁止**：同一筆資料不得同時以「活動參與」「成果」「媒體曝光」三種身分計為三項表現。

### 8.2 本文件（0136 / I19-E26）範圍

**範圍內**：來源出處、鑑真與相關性檢查、參與/貢獻、**另列**的成果支持、機密/存取、狀態、複核痕跡、後續追蹤、檢索。

### 8.3 負鄰居分流規則（不得誤入）

| 鄰居 | 需求 | 範圍 | 本表遇到時的處置 |
|---|---|---|---|
| **0135** | I19-E25 | 市場/顧客價值分析、趨勢 | **改道**：本表**不得**匯入市場/顧客價值分析內容；T5 中不得出現該類主張 |
| **0137** | I19-E27 | 正面媒體報導為**主**證據 | **改道**：媒體報導僅作**定位器/佐證**；不得取代底層獎項/參與/合作/研發原件；主證據屬 0137 |
| **0133** | I19-E22 | 訓練班次/人時總數 | **改道**：人時數字不入本表；本表效益欄若涉及訓練數字 → 指向 0133 |
| **0134** | I19-E23 | 會員/會費名冊 | **改道**：會員與會費資料不入本表 |

**判定順序（遇到內容先問三題）**
1. 這是在分析「市場/顧客價值趨勢」嗎？→ **0135**。
2. 這主要是一則媒體/新聞/社群報導本身嗎？→ **0137**（可留定位器）。
3. 這是班次/人時或會員/會費數字嗎？→ **0133 / 0134**。
4. 都不是，且是「原件本身 + 協會角色 + 獨立成果」→ **留在 0136**。

### 8.4 常見重複陷阱

| 陷阱 | 正確處置 |
|---|---|
| 同一活動既有新聞又有主辦方原件 | 原件 → 0136 PRIMARY；新聞 → 0137 或 0136 之 `safe/secondary locator`，`DG` 同群，僅計一次 |
| 同一獎項既有獎狀又有報導 | 獎狀 → 0136 PRIMARY；報導 → 0136 SECONDARY 或 0137；**不計兩次** |
| 同一產學案既有合約又有新聞稿 | 合約/驗收 → 0136；新聞稿 → 0137；MOU **不能**單獨成立 |
| 用活動照片帶出「受益人數」 | 照片不支持數字 → 數字欄 `UNKNOWN`，另尋 0133 或獨立成果來源 |

---

## 9. 隱私、存取、去識別、檢索與保留（Privacy / Access / Redaction / Retrieval / Retention）

### 9.1 最小個資原則

| 規則 | 內容 |
|---|---|
| 收集最小化 | 只收**驗證所必需**的欄位；姓名、電話、地址、帳號、身分字號預設不收 |
| 用途限定 | 僅用於驗證、複核、檢索；不得另作行銷或他用 |
| 去識別 | 公開層一律以角色代號（`CUST-ROLE-01`）、類別標籤（「示例主辦單位甲」）取代 |
| 法律基礎/同意 | 涉及可識別個人（例：受獎人姓名）→ 需 lawful disclosure consent，否則 `HOLD_PRIVACY` |
| 敏感內容 | 醫療、兒童、個案、帳務一律 `RESTRICTED`，預設不公開 |

### 9.2 存取分級（Access Groups）

| 分級 | 內容 | 可存取角色 | 可否上 GitHub |
|---|---|---|---|
| `RESTRICTED` | 正本、受限定位器、個資頁 | Custodian、指定 Verifier、Reviewer | **否** |
| `INTERNAL` | 去識別後的完整 T1/T2/T3（不含正本位址） | 內部授權角色 | 否（預設） |
| `SANITIZED` | 中繼資料、狀態、允許措辭 | 部分公開 | **是**（僅此層） |

**GitHub 唯一準則**：僅 `SANITIZED` 可進版本庫；**任何**可識別個人或正本位址的欄位一律留在 `RESTRICTED`。

### 9.3 去識別作業（Redaction）

1. 以**代號替換**（不是塗黑後仍可辨）：姓名→角色代號；單位→類別標籤；地址→區域層級。
2. 去識別後**另存新檔**並**另計 sha256**，原正本雜湊不變。
3. 記錄 `redaction_note`：改了哪些欄、由誰執行、日期。
4. **不可逆去識別**優先；若需可逆映射，映射表本身屬 `RESTRICTED`。

### 9.4 檢索（Retrieval）

- **檢索指引**（`safe_retrieval_instruction`）必須讓**另一位複核者**能獨立重做：找哪一層、哪個 `record_id`、哪個頁/節/項、要核什麼、期望看到什麼。
- **檢索測試**：每輪覆核抽一筆，由**非原保管人**依 `safe_retrieval_instruction` 重取 → 記 T4（`retrieval_test`），失敗即為缺陷，須修復指引而非改證據。
- 評委視角：**能重複驗證**才算合格（對應驗收第 9 項）。

### 9.5 保留與「無核准保留表」之 HOLD 路徑（不得編造年限）

> **規則：若未提供經核准的保留時程表（approved retention schedule），本表不得自行編造保存年限，亦不得提供法律建議。**

**HOLD 與升級路徑（Operational HOLD）**

| 步驟 | 動作 | 欄位 |
|---|---|---|
| 1 | `retention_review_date = "HOLD — NO SCHEDULE"` | T1 #40 |
| 2 | 指定 `owner` 與 `due_date`（覆核而非銷毀） | T1 #45 |
| 3 | 建立 T4 保留議題列：`failed_check = "NO APPROVED RETENTION SCHEDULE"` | T4 |
| 4 | **不得銷毀、不得自動過期刪除**；維持現行存取分級 | — |
| 5 | **升級**至「資料治理/保留表核准」位階（內部），取得**核准來源**後才填入日期 | T4 關閉理由須引用核准來源 |
| 6 | 在核准前，任何對外陳述**不得**宣稱「已依規保存 N 年」 | T5 允許措辭 |

**明確禁止**：編造保存年限、引用未經核准的法規年限、在本文件中給予法律建議。

### 9.6 事件應對（Incident Response，簡明四步）

1. **攔**：發現疑似外洩/誤公開 → 立即轉 `HOLD_PRIVACY`、暫停公布、停止該層同步。
2. **記**：T4 開事件列（時間、範圍、涉及欄位、發現者角色）— **不含**外洩內容本體。
3. **評**：Privacy role + Reviewer 評估涉及之同意/法律基礎/去識別缺口。
4. **復/關**：修復後雙方解除 HOLD 並記關閉理由；無法修復則維持 HOLD 並保留審計。

---

## 10. 決策摘要與改善追蹤（Decision Summary & Improvement Follow-up）

> **聲明：本節不產生任何真實協會決策或績效結論；不填入 TTQS 分數。**

### 10.1 未解來源佇列（Unresolved-Source Queue）

| queue_id | record_id | class | 缺什麼（確切來源） | 狀態 | owner | target_date | 下一步 | 升級條件 |
|---|---|---|---|---|---|---|---|---|
| UQ-0136-001 | （真實列） | A | 主辦方第一方活動紀錄與角色確認 | `PENDING_SOURCE` | `CUST-ROLE-0n` | `YYYY-MM-DD` | 發出索取（第一方窗口） | 兩次 bounded 索取無果 → 該筆停線+根因檢視 |
| UQ-0136-002 | （真實列） | B | 頒發方公開獎項登錄或書面確認 | `PENDING_SOURCE` |  |  |  |  |
| UQ-0136-003 | （真實列） | C | 合約/任務書 ＋ 學校驗收紀錄 | `PENDING_SOURCE` |  |  |  |  |
| UQ-0136-004 | （真實列） | — | 保留時程表核准來源 | `HOLD — NO SCHEDULE` |  |  | 升級至資料治理位階 | 取得核准前不得銷毀、不得稱年限 |
| UQ-0136-005 | — | — | **印刷勾選序號**實體核對 | `UNKNOWN` |  |  | 人工比對實體文件 | 未核前禁止代填 |

> 上表 `record_id`/日期/owner 為**結構示例**，未填值處一律以「確切所需來源 + 狀態」表達；**不得**填入未經驗證的真實單位或日期。

### 10.2 追蹤規則

- **每筆 PENDING/HOLD 必有** `owner` + `due_date`；到期未解 → 自動列入下輪摘要並記 T4（**非**人工門檻）。
- **到期不是銷毀**：到期未解僅表示「升級/改道/停該筆」，不得刪除證據列。
- **反覆缺陷**：同一檢查項（如 T3-2 完整性）反覆 FAIL → 修**流程/契約**（收件 SOP 或核對表），不是重印該筆。
- **其他 READY 線不停**：單筆佇列不阻擋其他可推進工作。

### 10.3 檢索測試與下一輪覆核

| 項 | 內容 |
|---|---|
| 檢索測試 | 每輪抽 ≥1 筆，由非原保管人依 `safe_retrieval_instruction` 重取並重做 T3-1/2/3 |
| 測試結果 | 記 T4 `retrieval_test`；PASS/FAIL 皆記錄，FAIL 須修指引 |
| 常見缺陷型態 | 缺 sha、保管鏈斷、頁/節/項不精確、允許措辭超出來源、狀態誤升 |
| 下次覆核 | `next_review_date = HOLD — NO SCHEDULE`（同 9.5：無核准表前不編日期） |
| 改善輸出 | 修 SOP/核對表/欄位字典，而非改歷史判定 |

---

## 11. SAMPLE → REAL 替換登記表（Replacement Register，逐項完整）

> **用途：每一項合成事實各佔一列，指明「需要什麼確切真實來源」才能替換。**
> **未完成替換前，對應欄位維持 `SAMPLE_ONLY` 或 `PENDING_SOURCE`，不得以真實口吻陳述。**

### 11.1 合成身分與定位

| T6 id | 合成事實/欄位 | 出現位置（走查） | 目前值（SAMPLE/SYNTHETIC） | **所需確切真實來源** | 替換後應有狀態 | 未替換時的 HOLD 條件 |
|---|---|---|---|---|---|---|
| R-01 | 文件編號 0136 | 全文 | 0136（內部編號，非序號） | 無需替換（**內部**編號已由 crosswalk+seed 驗證） | 維持 | **不得**當作印刷序號使用 |
| R-02 | 需求編號 I19-E26 | 全文 | I19-E26 | 無需替換（已由兩獨立來源一致驗證） | 維持 | — |
| R-03 | 專案 157 索引 150 | 全文 | 150（內部規劃索引） | 無需替換（已由索引摘錄檔驗證） | 維持 | **不得**當作印刷序號 |
| R-04 | **印刷勾選序號** | 表頭/各表 | **UNKNOWN** | **實體或官方文件上之印刷序號（人工核對）** | 由人工填入實值 | 未核對前 `PENDING_SOURCE`；**禁止代填** |
| R-05 | 來源 commit | 封面 | `03d73cb…b521e33` | 觀察值；正式以來源清單為準 | 以 manifest 為準 | 變更須記 T4 |
| R-06 | 官方 p8–9 原文 | §2.1 | 逐字引用 | 已由來源包提供（extract + 全 PDF） | 維持（**參考證據示例**） | **不得**改寫或當作協會成果 |
| R-07 | 文件狀態 | 封面 | CANDIDATE / SAMPLE TEMPLATE / NOT ISSUED | **人工核准紀錄（核准者角色＋日期）** | 先維持 | **禁止**改為 APPROVED |
| R-08 | 核准 | 封面 | **NOT_GRANTED** | 人工來源 | 先維持 | **無人工來源即永遠 NOT_GRANTED** |
| R-09 | 生效日期 | 封面 | **NOT_ISSUED** | 人工來源 | 先維持 | **禁止填生效日** |
| R-10 | 真實證據現況 | 封面/§5.3 | NOT PROVIDED / UNKNOWN | 依 §5.3 各列之確切來源 | 逐列升級 | 全部未取得前維持 |

### 11.2 走查 1（A：公益活動）合成事實

| T6 id | 合成事實/欄位 | 目前值 | **所需確切真實來源** | 替換後狀態 | HOLD 條件 |
|---|---|---|---|---|---|
| R-11 | record_id | `REG-0136-ACT-2026-0001` | 新建**真實**列（不得改寫本列） | 真實列依 T3 判定 | 本列永維 `SAMPLE_ONLY` |
| R-12 | shared_event_project_key | `EVT-SAMP-A-01` | 真實事件鍵（來自主辦方文件之事件識別） | — | — |
| R-13 | 主辦單位 | 「示例主辦單位甲」 | 主辦單位**官方**識別（網站/公告/公文/可回訪窗口） | T3-1/3 PASS 後可升 | 無可回訪窗口 → `PENDING_SOURCE` |
| R-14 | 活動名稱 | 示例公益活動 | 主辦方活動辦法/公告之**逐字名稱** | — | 僅海報/貼文 → `PENDING_SOURCE` |
| R-15 | 活動日期 | 2026-05-17 | 主辦方紀錄之確切日期 | — | 與他源矛盾未解 → `REJECTED` 或 HOLD |
| R-16 | 來源文件日期 | 2026-05-20 | 該來源文件自身載明日期 | — | — |
| R-17 | 協會角色 | 示例協辦角色（合成） | 主辦方**明確角色文字**（邀請/議程/主辦方紀錄） | 有文字才可填實角色 | 無文字 → `NOT ESTABLISHED` |
| R-18 | 實際貢獻 | 未建立 | 主辦方對協會工作項的具體敘述 | — | 無 → `NOT ESTABLISHED` |
| R-19 | 保管人 | `CUST-ROLE-01` | **真實保管角色**指派紀錄 | — | — |
| R-20 | 來源文件（原件） | 第一方活動紀錄 PDF（描述） | **實際**第一方檔案（可雜湊位元組） | 得 sha + T3-1..3 過 → 可升 PRIMARY | 無實際檔案 → `UNKNOWN`+原因 |
| R-21 | 受限正本位址 | `UNKNOWN — NOT PROVIDED` | 受控儲存中的實際位址 | — | 無位址 → `PENDING_SOURCE` |
| R-22 | 可公開位址 | `NOT_APPLICABLE`+原因 | 授權可公開之官方 URL | 有授權才填 | 無授權 → 保持 NOT_APPLICABLE/HOLD |
| R-23 | 頁/節/項定位 | `UNKNOWN` | 確切頁/節/項 | — | 未給 → 不得 VERIFIED |
| R-24 | 格式/版本 | `UNKNOWN` | 實際格式與版本 | — | — |
| R-25 | **sha256** | `UNKNOWN（無位元組）` | 對實際正本計算之 SHA-256 | 有值才可能 PRIMARY | 紙本無 sha → `PENDING_SOURCE` |
| R-26 | 擷取日期 | `NOT_APPLICABLE`+原因 | 實際雜湊/擷取日期 | — | — |
| R-27 | 保管鏈 | `CF-SAMP-A-01`（合成） | 真實 IN/轉移列（含原因與確認） | — | 鏈斷 → HOLD/PENDING |
| R-28 | 驗證端點 | `UNKNOWN` | 真實第一方回訪窗口 | — | 無窗口 → `PENDING_SOURCE` |
| R-29 | 驗證者/複核者 | `VER-ROLE-02` / `REV-ROLE-03` | 真實指派之角色（且 ≠ 建置者） | — | 同人自判 → 判定無效 |
| R-30 | 三軌結果 | I/II/III **UNKNOWN** | 依 T3-1..8 之真實結果 | 依實測 | 任一 UNKNOWN → 不得 PRIMARY |
| R-31 | 參與證明 | 未建立 | 主辦方確認（出席/角色）或受控紀錄**經主辦確認** | — | 僅照片/報名表 → `PENDING_SOURCE` |
| R-32 | 社會成果 | **UNKNOWN** | **獨立**成果來源（含 n/unit/period） | 有來源才填 | 推論/無分母 → 維持 UNKNOWN |
| R-33 | 分母/單位/期間 | `NOT_APPLICABLE`+原因 | 數值主張之三件套來源 | — | 缺一 → 數值改 UNKNOWN |
| R-34 | 相關性理由 | 對應 p8–9 類型一 | 保持（依官方原文） | — | 不得擴張含 0135/0137 內容 |
| R-35 | 狀態 | **`SAMPLE_ONLY`** | 真實列另建並依 T3 判定 | 真實列獨立判定 | 本列**禁止**升級 |
| R-36 | 限制 | 「本列純示範…」 | 真實列依實況填 | — | — |
| R-37 | 重複群組 | `DG-SAMP-A-01` | 真實 DG（同事件鍵） | — | 雙計 → `REJECTED` |
| R-38 | 同意/法律基礎 | `NOT_APPLICABLE`+原因 | 涉個資時之同意或法律基礎 | — | 未解 → `HOLD_PRIVACY` |
| R-39 | 資料分級/存取 | `SANITIZED / DEMO-GROUP` | 真實分級指派 | — | — |
| R-40 | 保留覆核日 | **`HOLD — NO SCHEDULE`** | **經核准的保留時程表** | 取得核准來源才填日期 | 無表 → 維持 HOLD、禁銷毀、禁稱年限 |
| R-41 | 判定/理由/複核日期 | `SAMPLE_ONLY` / 見上 / `2026-10-27` | 真實判定由 Reviewer 為之 | — | 文稿日期**非**核准日期 |
| R-42 | 檢索指引 | 僅供閱讀本節 | 真實可重取之指引（層/ID/頁項） | — | 指引不可重做 → 檢索測試 FAIL |
| R-43 | 可計數 | **`NO`** | 真實列依狀態與限縮主張 | `LIMITED-TO-CLAIM` | 狀態非 VERIFIED → 永遠 NO |

### 11.3 走查 2（B：獎項）合成事實

| T6 id | 合成事實/欄位 | 目前值 | **所需確切真實來源** | 替換後狀態 | HOLD 條件 |
|---|---|---|---|---|---|
| R-44 | record_id | `REG-0136-AWD-2026-0002` | 另建真實列 | 依 T3 | 本列維 `SAMPLE_ONLY` |
| R-45 | 頒發單位 | 「示例頒發單位乙」 | 頒發方**官方**識別與可回訪窗口 | T3-1/3 PASS | 無登錄/無回訪 → `PENDING_SOURCE` |
| R-46 | 獎項名稱/類別 | 示例獎項類別 | 頒發方公告之**逐字**名稱與類別 | — | 簡稱/自創譯名 → 更正或 REJECT |
| R-47 | 頒獎日期 | `UNKNOWN` | 頒發方公告或原件所載日期 | — | 模糊（「去年」）→ 不接受 |
| R-48 | 受獎者身份 | 未提供 | **原件逐字**所載受獎主體 | — | 若非協會 → `NOT ESTABLISHED`（就協會得獎） |
| R-49 | 評選標準/期別 | `UNKNOWN` | 公開評選辦法或頒發方說明 | — | 未取得 → 記「未取得」 |
| R-50 | 協會角色 | **`NOT ESTABLISHED`** | 原件所載受獎者或明確角色文字 | 有來源才改 | 持續無 → 維持 |
| R-51 | 頒發方登錄 | `NOT_APPLICABLE`+原因 | 公開獎項登錄 URL 或書面確認 | 有 → 可支持 PRIMARY | 無 → 最高 SECONDARY/PENDING |
| R-52 | 獎狀正本 | **未附（僅描述）** | 獎狀正本或第一方數位檔（＋sha） | 有原件+核對 → PRIMARY | 無 → `PENDING_SOURCE` |
| R-53 | 受限正本位址 | `UNKNOWN — NOT PROVIDED` | 受控儲存實際位址 | — | — |
| R-54 | 頁/節/項、格式 | `UNKNOWN` / `NOT_APPLICABLE`+原因 | 實際檔案之定位與格式 | — | — |
| R-55 | sha256 | `UNKNOWN（無位元組）` | 對實際獎狀雜湊 | 有 → 才可能 PRIMARY | — |
| R-56 | 保管鏈 | `CF-SAMP-B-01`（合成） | 真實保管列 | — | — |
| R-57 | 驗證端點/結果 | `UNKNOWN` / I:UNKNOWN II:FAIL III:N/A+原因 | 真實查核（T3-1..7） | 依實測 | — |
| R-58 | 社會成果 | `UNKNOWN`（B10） | **另立一列**之獨立成果來源（若要主張） | 不得由獎項推導 | — |
| R-59 | 個資/公布同意 | `NOT_APPLICABLE`+原因 | 受獎人姓名之 lawful disclosure consent | 有同意才可公布姓名 | 未解 → `HOLD_PRIVACY` |
| R-60 | 狀態 | **`SAMPLE_ONLY`** | 真實列另建判定 | 依 T3 | 本列禁止升級 |
| R-61 | 限制 | 「示範列；未附獎狀/公告/登錄；角色未建立」 | 依真實情況 | — | — |
| R-62 | 重複群組 | `DG-SAMP-B-01` | 真實 DG | — | 與 0137 雙計 → REJECT |
| R-63 | 保留覆核日 | **`HOLD — NO SCHEDULE`** | 核准保留表 | 有表才填 | 禁編造年限 |
| R-64 | 判定/複核/可計數 | `SAMPLE_ONLY` / `2026-10-27` / **NO** | 真實複核 | 依狀態 | 本列永遠 NO |

### 11.4 走查 3（C：學校產學研發）合成事實

| T6 id | 合成事實/欄位 | 目前值 | **所需確切真實來源** | 替換後狀態 | HOLD 條件 |
|---|---|---|---|---|---|
| R-65 | record_id | `REG-0136-SCH-2026-0003` | 另建真實列 | 依 T3 | 維 `SAMPLE_ONLY` |
| R-66 | 學校/單位 | 「示例學校單位丙」 | 學校官方頁/系所頁/授權第一方窗口 | T3-1/3 PASS | 無可回訪 → `PENDING_SOURCE` |
| R-67 | 專案/協議名稱 | 示例專案（描述） | 已簽署合約/契約/專案任務書之逐字名稱 | 有 → 支持 C2 | **僅 MOU → C2 不足** |
| R-68 | 專案期間 | `UNKNOWN` | 合約/任務書所載期間 | — | — |
| R-69 | 協會角色 | **`NOT ESTABLISHED`** | 合約/任務書/工作分配之明確文字 | 有 → 才改 | 無 → 維持 |
| R-70 | 協會交付物 | `UNKNOWN` | 具名交付物＋交付日期＋接收方 | 有 → C6 PASS | 「參與會議」不算 |
| R-71 | 驗收/公開產出 | `UNKNOWN` | 學校或授權第一方之驗收紀錄/成果報告簽收/公開產出頁 | 有 → 才可說「已完成」 | **MOU/會議/合影 → 不足** |
| R-72 | 社會面—產出 output | `UNKNOWN` | 研發產出之第一方紀錄 | 三要素齊才可主張 | 缺 → UNKNOWN |
| R-73 | 社會面—使用情境 use/context | `UNKNOWN` | 使用/應用情境之來源 | — | 無證據禁暗示商業化/社區效果 |
| R-74 | 社會面—效益來源 source of social benefit | `UNKNOWN` | 獨立效益來源（n/unit/period） | — | 推論 → REJECT/UNKNOWN |
| R-75 | 來源檔案/位址/sha | `UNKNOWN / NOT PROVIDED` | 實際檔案＋雜湊＋受限位址 | 有 → 才可能 PRIMARY | — |
| R-76 | 保管鏈 | `CF-SAMP-C-01`（合成） | 真實保管列 | — | — |
| R-77 | 驗證結果 | I:UNKNOWN II:FAIL III:UNKNOWN | 真實 T3-1..8 | 依實測 | — |
| R-78 | 媒體/新聞素材 | **未納入（僅可作定位器）** | 底層原件（主證據屬 0137） | — | 新聞**不能**取代原件 |
| R-79 | 狀態/限制 | **`SAMPLE_ONLY`** / MOU≠完成≠影響 | 真實列另建 | 依 T3 | 禁升級 |
| R-80 | 重複群組 | `DG-SAMP-C-01` | 真實 DG（同專案鍵） | — | — |
| R-81 | 保留覆核日 | **`HOLD — NO SCHEDULE`** | 核准保留表 | 有表才填 | — |
| R-82 | 判定/複核/可計數 | `SAMPLE_ONLY` / `2026-10-27` / **NO** | 真實複核 | 依狀態 | 永遠 NO |

### 11.5 其餘全區合成項

| T6 id | 合成事實 | 目前值 | 所需真實來源 | HOLD 條件 |
|---|---|---|---|---|
| R-83 | 覆核日期 `2026-10-27` | 文稿撰寫日 | **非**核准日；核准日需人工來源 | 不得當作生效/核准日 |
| R-84 | 角色代號 `CUST/VER/REV-ROLE-nn` | 通用代號 | 真實角色指派（仍建議用代號不寫真名） | 涉真名 → 個資控管 |
| R-85 | 隊列/日誌結構列（§10.1、T4） | 結構示例 | 真實佇列資料 | 未填處須給「確切來源+狀態」，禁空白 |
| R-86 | T5 允許措辭範例 | 合成句子 | 依真實來源降格改寫 | 超出來源 → REJECT |
| R-87 | `DG/EVT/PRJ/CF/HRC/UQ/CL` 等編號 | 合成 ID | 真實建列時新發 | 本表合成 ID 不得挪用 |
| R-88 | 印刷序號以外之全部「官方」字樣 | 依來源包 | 皆須回指來源包檔名 | 未驗證者不得聲稱 |

> **替換紀律**：替換 = **另建真實列**（真實 `record_id`），**不得**直接改寫 `SAMPLE_ONLY` 列的歷史值；改動一律 `correction_note` + T4 追加，保留可追溯性。

---

## 12. 版本、驗證、交接與驗收/拒絕清單（Version / Verification / Handoff / Acceptance Checklist）

### 12.1 版本與驗證控制

| 欄位 | 值 |
|---|---|
| 版本 | R02 MANUSCRIPT（文稿）；非 DOCX、非驗收收據 |
| 文稿日期 | 2026-10-27（**非**核准日/生效日） |
| 來源 revision | 依來源包：分支 `work/ttqs-one-document-quality-contract-20261016`；commit `03d73cb900e28d7cd8ea02ec0c43c4564b521e33`；雜湊見 `SOURCE_MANIFEST_0136_R01.json` |
| 覆核角色/日期 | `REV-ROLE-nn / YYYY-MM-DD`（待指派；**不得**與建置者同人） |
| 未解問題 | (1) 印刷勾選序號 UNKNOWN；(2) 全部 REAL 來源 NOT PROVIDED；(3) 無核准保留時程表；(4) 核准/生效 NOT_GRANTED / NOT_ISSUED |
| 交接物 | 本 Markdown 文稿 → Word 原生建置 → 渲染頁檢視 → 技術 QA → **最終精確 SHA** 之獨立語意覆核 → GitHub 原始位元組核對 |
| 狀態 | CANDIDATE / SAMPLE TEMPLATE / NOT ISSUED |

**驗證綁定要求**：Word 原生渲染、視覺 QA、技術檢查與獨立語意覆核**必須綁定最終精確 DOCX SHA**；本 Blueprint/本文稿**不是** DOCX，也**不是**驗收收據。`BUILD_OWNER ≠ REVIEW_OWNER`；覆核者不得使用同筆之建置內容作為唯一依據。

### 12.2 交接（Handoff）

| 步 | 交接物 | 接收方 | 驗收條件 |
|---|---|---|---|
| 1 | 本 Markdown 文稿 | 建置者 | 章節 0–12 齊備、T1–T6 齊備、三筆走查齊備 |
| 2 | 原生 DOCX | 技術 QA | 可開啟、字級下限（內文 ≥10.5pt、表格 ≥9.5pt）、無空白表/無未限定「待填」 |
| 3 | 渲染頁 | 視覺 QA | 無截斷、無溢出、表頭重複、頁碼正常 |
| 4 | 最終精確 SHA | 獨立語意覆核 | 覆核者 ≠ 建置者；逐項過 12.3 |
| 5 | GitHub 原始位元組 | 集成者 | 僅 SANITIZED 層；位元組一致 |

### 12.3 驗收清單（Acceptance Checklist）— 全部為 YES 才放行

| # | 驗收項 | YES/NO |
|---|---|---|
| A1 | 官方 p8–9 原文**逐字**存在，且明確標為「參考證據示例」而非協會成果 | ☐ |
| A2 | 頁首/對照綁定 `0136 ↔ I19-E26`；索引 150 **分列**；印刷序號維持 **UNKNOWN**，未代填 | ☐ |
| A3 | **零真實來源仍可運作**：真實區以「確切來源 + HOLD 條件」表達，無誤導空白、無未限定「待填」 | ☐ |
| A4 | 三條驗證路徑**各自分離**「來源鑑真 / 協會角色 / 成果」，門檻明確 | ☐ |
| A5 | 欄位字典完整（T1 47 欄含定義、規則、允許值、空值紀律） | ☐ |
| A6 | 狀態 6 態、判定權責、充分性與升級、兩輪失敗停線規則可用 | ☐ |
| A7 | HOLD / REJECTED / 修正標準明確（含 T4 對抗雙計與回改） | ☐ |
| A8 | 隱私/存取/去識別/檢索/保留可用；**無編造年限**，保留走 `HOLD — NO SCHEDULE` + 升級路徑 | ☐ |
| A9 | 三筆 SAMPLE/SYNTHETIC 走查**清楚非真實**，無偽造原件/簽名/核准；**全部事實**入替換登記表 | ☐ |
| A10 | 替換登記表**逐項**涵蓋事實/欄位/角色/日期/發出方/成果/狀態/定位器 + 所需確切真實來源 | ☐ |
| A11 | 鄰居分流：0135（市場/顧客價值）、0137（媒體主證據）、0133（人時）、0134（會員會費）**不可誤認**；媒體僅作定位器 | ☐ |
| A12 | 數字/主張可歸屬；無來源之影響為 `UNKNOWN`；**無 TTQS 自我評分** | ☐ |
| A13 | 複核者可依 `safe_retrieval_instruction` **取回並重做**驗證（檢索測試可執行） | ☐ |
| A14 | 未推論影響、因果、資格或分數；MOU/照片/出席/提名/貼文/報導**明列**不證成果 | ☐ |
| A15 | 核准/生效維持 **NOT_GRANTED / NOT_ISSUED**；**無**偽造核章區 | ☐ |
| A16 | T1–T6 六表齊備且可直接填用（非空殼） | ☐ |
| A17 | Word 原生渲染 + 視覺 QA + 技術檢查 + 獨立語意覆核**綁定最終精確 DOCX SHA** | ☐ |
| A18 | 僅 SANITIZED 層進 GitHub；受限定位器留在受限位置 | ☐ |

### 12.4 拒絕清單（Reject if ANY is true）— 任一成立即不得放行

| # | 拒絕條件 | YES=拒絕 |
|---|---|---|
| R1 | 把 p8–9 參考證據寫成協會已具備/已達成 | ☐ |
| R2 | 以 0136 或 I19-E26 或索引 150 **代填**印刷勾選序號 | ☐ |
| R3 | 出現空白欄、無原因的 `NOT_APPLICABLE`，或**未限定的**「待填/待核/空白表/會後填寫」 | ☐ |
| R4 | 三筆走查任一被標為 VERIFIED_*、被計入表現，或含真實單位/人名/簽名 | ☐ |
| R5 | 任一合成事實**未**列入替換登記表 | ☐ |
| R6 | 出現自創的保存年限、法規年限引用或法律建議 | ☐ |
| R7 | 由出席/夥伴名義/獎項/媒體**推論**數值影響或因果，或未附分母 | ☐ |
| R8 | 出現任何 TTQS 分數/評等/自我「通過」結論 | ☐ |
| R9 | 核准或生效欄填入非 NOT_GRANTED / NOT_ISSUED 之值，或存在偽造核章/簽名區 | ☐ |
| R10 | 媒體報導取代底層原件，或 0135/0137/0133/0134 內容混入本表 | ☐ |
| R11 | 提名/申請/參與證明/自撰摘要/未驗影像被當作「獲獎」；MOU/會議被當作「完成/影響」 | ☐ |
| R12 | `BUILD_OWNER = REVIEW_OWNER` 之判定，或覆核未綁定最終精確 SHA | ☐ |
| R13 | 公開層（GitHub）含正本位址或個資 | ☐ |
| R14 | 單一記錄為求「三類齊備」而混入不相干或虛構內容 | ☐ |

### 12.5 最終停止/放行閘（Stop / Go）

- **STOP（維持 CANDIDATE / NOT ISSUED）**：12.3 任一為 NO，或 12.4 任一為 YES。
- **GO（僅指「可進入下一階段：Word 建置」）**：12.3 全 YES **且** 12.4 全 NO。
- **注意**：GO **不等於**核准、不等於生效、不等於任何 TTQS 結論；**APPROVED / EFFECTIVE 僅能由人工來源授予**，在此之前一律 `NOT_GRANTED` / `NOT_ISSUED`。

---

**— 文稿結束 —**

*DOCX 0136 ｜ I19-E26 ｜ 專案 157 索引 150 ｜ 官方印刷勾選序號：UNKNOWN ｜ CANDIDATE / SAMPLE TEMPLATE / NOT ISSUED ｜ 核准：NOT_GRANTED ｜ 生效：NOT_ISSUED ｜ REAL EVIDENCE: NOT PROVIDED / UNKNOWN*