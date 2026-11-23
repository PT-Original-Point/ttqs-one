# 0118 R05 exact-SHA review packet
Candidate DOCX SHA-256: `aa6ee02e2b3ae7c0ef06e74cad6333f2ddcc3bc306651f4e3e5694ecf5838707`

## SOURCE: SOURCE_PACKET_0118_I19-E05_R01.md
SHA-256: `4ccb3a5676d4c618d072a2347e9661f193546b3dc8b7bcab7aa67f4dfc396869`

# 0118 I19-E05 來源包 R01

## 身分與唯一來源
- 文件 ID：0118。官方需求 ID：I19-E05。文件名稱：感謝函原件收存與核驗登錄表。
- 正式 129-to-142 crosswalk 的 I19-E05 列指定 1 份文件、0 份拆分文件，文件 ID 0118；檔案 SHA-256：1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679。
- R04 blueprint seed 將 0118 對應 I19-E05；seed SHA-256：280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0。
- GitHub PR #92 的 03_157_CHECKBOX_BLUEPRINTS.md 內部索引 129 將此項定義為「感謝函：真實原件取得，不偽造」。內部索引 129 不是官方印製流水號。正式印製序號尚未從原件確認，標記 UNKNOWN_NOT_ASSERTED。
- 官方檢核表來源為 official_source_0108_r11.pdf 第 8 頁，PDF SHA-256：805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709。第 8 頁的常見參考佐證列有「感謝函」。逐頁文字抽取 SHA-256：57c6b33d70b665bd41b8d58ff58f5c0d78f9c2c751ccd9c6dd1b740b2fbf374e。
- 本文件記錄真實第三方來函的取得、收存、來源核驗、完整性、關聯性、限制及後續人工判讀。它不是感謝函範本，也不代替原件。

## 證據用途與限制
感謝函可以作為官方檢核表列示的一種參考佐證，但函件本身不自動證明訓練造成特定績效、服務結果或顧客價值提升。登錄者必須記錄原件由誰、何時、如何取得，文件是否完整，來源如何獨立確認，以及內容與 I19-E05 的關聯。未取得原件或未能核驗來源時，採 HOLD，不得填成已驗證。

紙本原件、寄件者原生電子檔及由原件製成的掃描副本要分開標記。掃描檔不是紙本原件；螢幕截圖或轉寄內容也不自動等同寄件者原生檔。保存原件的位置、接觸個資的身份對照與聯絡紀錄放在協會授權的受限位置。公開證據包只保留去識別化的證據代碼、檔案雜湊與必要核驗摘要。

## 適用讀者與作業順序
協會指定的承辦人負責收件登錄及原件保管；協會指定的覆核人確認文件完整、來源核驗及指標關聯。此處角色是候選作業職責，不代表協會已任命任何人或已核准流程。

1. 先登記收到的實際檔案或紙本原件，記下收件方式、時間、件數和保管位置；沒有原件時不得建立「已收件」紀錄。
2. 檢查頁數、附件、可讀性、修改痕跡及文件來源；保留收到的原始位元組，不覆寫原檔。數位副本計算 SHA-256；紙本原件記錄封存或檔案盒索引。
3. 透過獨立取得的正式聯絡管道核對發函單位及真實性。只依函件內自列的電話、電郵或標誌，不足以完成來源驗證。不得假造聯絡、回覆或簽章查核結果。
4. 對照函件所述訓練、服務、期間及受益內容，評估它是否支援 I19-E05。感謝語句、無法辨認對象的截圖或與訓練無關的函件，不得推論為績效證據。
5. 記錄缺件、疑點、補件責任與期限。只有完成來源、完整性、關聯及資料保護檢核後，才標記「可送人工審閱」；這個狀態仍不是協會正式接受。

## 近似文件與分流
- 0092／I17D-E06 是第三方感謝函索取稿及證據驗證登錄；索取函本身不是收到的感謝函原件。
- 0096／I18-E03 與 0103／I18-E10 是其他官方需求的感謝函相關文件，不能借用其指標、案例或結論代替 I19-E05。
- 0117／I19-E04 記錄考照結果；0116／I19-E03 記錄訓後就業狀態。它們不是同一證據來源，未經真實來源證明不得合併人員、期間或成果。
- 本文件只登錄 0118 自己實際收到的第三方原件及核驗鏈，不撰寫或重製第三方函文。

## 真實化前須補齊的來源
目前沒有原始點協會的真實感謝函、寄件者確認、收件紀錄、授權或正式核准資料。所有示範值均為 SYNTHETIC；「沒有原件」的示範不得用來佐證 TTQS 成果。正式使用前由協會授權人員逐件替換示範資料，保存真實原件及受限身份對照，並依機構正式流程決定是否納入送審資料。


## SOURCE: UNIQUE_BLUEPRINT_0118_I19-E05_R01.md
SHA-256: `76aabf18eba37f44b352390516b4b8392fb7dfac50e87a6324526bad5bbe9214`

# 0118 I19-E05 專屬 Blueprint R01

## 核心用途
建立協會可直接使用的感謝函原件收存與核驗登錄工具。表單管理真實第三方來函的來源、收件、原件位置、完整性、核驗、隱私及 I19-E05 關聯。文件不能代替感謝函原件，也不能把感謝內容推論為訓練成效或績效提升。

## 官方綁定
- Document ID：0118
- Requirement ID：I19-E05
- 129-to-142 crosswalk：1 個交付項、0 拆分、文件 ID 0118
- 157 Blueprint 內部索引：129；不是官方印製 checkbox 序號
- 官方來源：official_source_0108_r11.pdf 第 8 頁；列示「感謝函」
- 印製 checkbox 序號：UNKNOWN_NOT_ASSERTED，直到依正式原始頁面核實

## 文件文類與讀者
文類為可重複使用的收件登錄表、原件保管紀錄及核驗清單。主要讀者是協會授權的訓練行政承辦人與第二位指定覆核人。正文要使讀者能逐件登錄、判斷缺件或疑點、保全原件及決定能否送交人工審閱。

## 必備章節
1. 文件用途、官方來源、證據效力及 SAMPLE/REAL 邊界
2. 單件收存登錄表
3. 原件型態與保管鏈
4. 來源真實性、完整性、關聯性、隱私及保存期限核驗
5. HOLD、補正、不得採用及送人工審閱判定
6. 完整 SYNTHETIC 示範：沒有原件、沒有第三方確認，結果為 HOLD
7. 與相鄰官方需求及既有文件的證據分界
8. 真實使用前的替換與升格檢核

## 必備欄位
- 登錄代碼、需求 ID、收件日期時間、收件方式、收件操作者角色
- 來函機構、寄件者職稱、收件人/部門、發函日、函件主旨或內容摘要
- 涉及之訓練/服務名稱、班次或期間、函件所述支持內容及其範圍
- 原件型態：紙本、寄件者原生電子檔、掃描副本、影本、截圖或其他
- 頁數/附件、可讀性、收到時檔案雜湊、掃描副本雜湊
- 紙本封存索引或受限數位路徑、保管人角色、移交時間與紀錄
- 來源核驗管道及其獨立來源、查證日期、查證對象/角色、回覆或參考代碼
- 完整性檢查、I19-E05 關聯判斷、隱私/使用授權狀態、缺件/疑點
- 判定、理由、補正事項/責任角色/期限、覆核人角色、覆核日期
- 去識別化公開證據代碼及實際資料受限位置

## 核驗清單與判定
每個核驗項目須分開記錄觀察、狀態與證據位置：
1. 原件是否實際收到；僅有請求稿、轉述、截圖或掃描影本時明確標記型態。
2. 來源身份是否由不依賴函件自述的正式管道確認。
3. 文件頁數、附件、字跡/檔案可讀性與收到版本是否完整。
4. 寄件機構、發函角色、收件對象與日期是否可追溯。
5. 函件是否連結正確訓練/服務與期間；不得把稱謝推論為因果成果。
6. 是否有個資、保密、同意或用途限制；不適合公開的細節留在受限位置。
7. 紙本/數位保管位置、存取權限、移交紀錄及數位副本 SHA-256 是否完整。
8. 證據摘要是否忠實描述函文，不擴張成未證明的成效。
9. 登錄結果是否有另一位協會指定覆核人檢視；未覆核不代表核驗通過。

狀態：RECEIVED_PENDING_CHECK、HOLD_NO_ORIGINAL、HOLD_SOURCE_UNVERIFIED、HOLD_SCOPE_OR_PRIVACY_REVIEW、RETURN_FOR_SUPPLEMENT、ELIGIBLE_FOR_HUMAN_REVIEW、NOT_ACCEPTED_CONFIRMED_COPY_OR_MISMATCH。只有已取得原件且來源/完整性/關聯/隱私檢核完成，才可送人工審閱。該狀態不是正式接受；只有人類依正式規則決定才能記錄接受/送審。

## 專屬示範
唯一示範列為 SYNTHETIC-SAMPLE：SYN-0118-001。沒有實際感謝函檔案，寄件機構、寄件者、收件者與日期均 NOT_PROVIDED，來源查證 NOT_RUN，保管位置 NONE，原件 SHA 不適用，判定 HOLD_NO_ORIGINAL。示範只用來測試缺件處理，不製作仿真的信箋、第三方名稱、簽名、印章、回覆或收件紀錄。

## 具體輸出與圖表
- 單件登錄表：可列印/填寫，保留受限欄位提示。
- 核驗清單：逐項勾選、結果/證據位置及覆核。
- 判定矩陣：狀態、觸發條件與下一步。
- 一筆完整合成資料列及替換清冊。
- 不需要計算或效益圖；禁止添加無法由原件支持的績效統計。

## 拒收、補件與保留條件
- 沒有原件：HOLD_NO_ORIGINAL；取得原件前不得登錄為已收件/已核驗。
- 只有截圖、轉寄、影本、空白稿：記錄實際型態並 HOLD；除非正式規則允許且來源已核實，不納入原件結論。
- 來源未獨立確認、內容關聯不明、缺頁附件、疑似修改、個資使用未釐清：HOLD 或 RETURN_FOR_SUPPLEMENT。
- 僅在可確認為非原件、錯置文件、內容/發函者不符或違反資料授權時，才標 NOT_ACCEPTED，寫明證據；疑點未確認不能寫成造假。
- 不建立或補寫任何真實第三方原件、寄件紀錄、查證回覆、核准或簽章。

## 相鄰需求分界
標題隱去後仍可辨認本文件是 I19-E05 的「收存與核驗登錄工具」。不得與 0092/I17D-E06 索取稿、0096/I18-E03 或 0103/I18-E10 的其他指標感謝函文件混件；不得以 0116 就業或 0117 考照資料替代原件。

## 完整驗收
- 官方需求、crosswalk、internal Blueprint index 129 綁定正確；印製序號保持 UNKNOWN_NOT_ASSERTED。
- 表單、原件保管、來源查證、完整性、關聯、隱私、補正/保留/拒收條件齊全且可實際操作。
- 唯一示範清楚標為合成；沒有假函、真人、第三方回覆、簽章、核准或真實協會決定。
- 所有示範值與替換項登錄一致；沒有虛構計算或成果圖。
- 與相鄰文件的證據所有權清楚。
- Word 技術 QA、每頁視覺檢查及獨立 exact-SHA 語意審查分別完成；未完成不得升格。


## SOURCE: mapping_evidence_0118.json
SHA-256: `16db9d1e5f103ecac826eb2a25204f23a9bfec090be0ff53e5e7faf5aaf9c83e`

{
  "project_id": "TTQS_ONE",
  "doc_id": "0118",
  "requirement_id": "I19-E05",
  "title": "感謝函原件收存與核驗登錄表",
  "deliverable_count": 1,
  "split_extra_count": 0,
  "official_printed_checkbox_serial": "UNKNOWN_NOT_ASSERTED",
  "blueprint_internal_index": 129,
  "crosswalk": {
    "path": "TTQS_ONE_CODEX_RUNTIME/INPUTS/R04/04_EVIDENCE/TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv",
    "sha256": "1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679",
    "exact_row": {
      "requirement_id": "I19-E05",
      "deliverable_ids": "0118",
      "document_titles": "感謝函原件收存與核驗登錄表"
    }
  },
  "blueprint_seed": {
    "path": "TTQS_ONE_CODEX_RUNTIME/INPUTS/R04/00_CONTROL/BLUEPRINT_SEED_142.csv",
    "sha256": "280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0"
  },
  "official_source": {
    "path": "WORK/QUALITY_REBUILD_20261016/official_source_0108_r11.pdf",
    "pages": [
      8
    ],
    "sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
    "page8_text_sha256": "57c6b33d70b665bd41b8d58ff58f5c0d78f9c2c751ccd9c6dd1b740b2fbf374e",
    "excerpt": "常見參考佐證列示「感謝函」。"
  },
  "github_sources": {
    "repository": "PT-Original-Point/ttqs-one",
    "pr": 92,
    "branch": "work/ttqs-one-document-quality-contract-20261016",
    "head": "a7c8917d2c70453006da690970c9be8a1a0490b7",
    "blueprint_blob": "8c2bbe7ca9dcbb03088a48934b9e57e7147ede63",
    "writing_manual_blob": "4ff863d9f534b6359fc1c7c1685bd8cce02da886",
    "mission_blob": "538bedb9d87e8465f43151933b4a5c1bfa4bbc4e"
  },
  "negative_neighbors": [
    {
      "doc_id": "0092",
      "requirement_id": "I17D-E06",
      "distinction": "third-party thank-you request draft; not a received original"
    },
    {
      "doc_id": "0096",
      "requirement_id": "I18-E03",
      "distinction": "different official evidence requirement"
    },
    {
      "doc_id": "0103",
      "requirement_id": "I18-E10",
      "distinction": "different official evidence requirement"
    },
    {
      "doc_id": "0116",
      "requirement_id": "I19-E03",
      "distinction": "post-training employment evidence"
    },
    {
      "doc_id": "0117",
      "requirement_id": "I19-E04",
      "distinction": "exam pass-rate evidence"
    }
  ],
  "mapping_status": "SUPPORTED_BY_CROSSWALK_BLUEPRINT_AND_OFFICIAL_PAGE8",
  "real_original_supplied": false,
  "formal_acceptance": "NOT_GRANTED"
}


## SOURCE: official_source_page_08_text.txt
SHA-256: `57c6b33d70b665bd41b8d58ff58f5c0d78f9c2c751ccd9c6dd1b740b2fbf374e`

 
8 
項目 評核指標項目 
內涵說明（以下為
例，但不以此為
限） 
常見參考佐證資料 
（並註明資料來源及頁碼） 
3分 目標市場及顧客
價值均有一定程度提
升的效果。 
4分 目標市場及顧客
價值均有顯著具體的
提升績效。 
具體紀錄及評量。 
 感謝函。 
 其他： 
2 分之常見參考佐證資料： 
 有具體紀錄可辨識目標市場及顧
客價值均有部份提升效果。 
 相關證據顯示有初步訓練成果，
且有部份佐證資料。 
 提出學員滿意度、考試測驗或心
得報告（學習技能面） 。 
 提出課後追蹤調查與分析結果、
證照通過情形（學習技能面） 。 
 部份會員透過訓練後，事業成就
上突破原有格局。 
 企業主雇用結訓後學員，肯定機
構訓練的成效。 
 部份學員能運用所學於職務中。 
 進行訓後薪資調查，部份訓後學
員微幅調薪。 
 其他： 
3 分之常見參考佐證資料： 
 有量化之效益可呈現目標市場及
顧客價值均有一定程度提 升的效
果。 
 相關證據顯示個人訓練後之績效
改善成果。 
 提出市場競爭力、營業額、工作
流程、成本控制或客訴率等營運
表現（財務面） 。 
 學員訓後創業案例。 
 學員證照通過、就業率高。 
 個人產品不良件數有下降趨勢。 
 每年訓練班次、人次均持續成
長。 
 會員人數及會費收入均逐年增
加。 
 其他： 
4 分之常見參考佐證資料： 
 經營績效中之數據呈現目標市場
及顧客價值均有顯著具體的提 升
績效。 
 提出參與社會公益活動、獲頒公
民營單位獎項、結合學校單位產

## SOURCE: SYNTHETIC_DATASET_0118_R01.csv
SHA-256: `96865d080ad441a2a2ea3d3f2c9f3fcecc7d8956f284b80bb3681d85bfab0d39`

record_class,record_id,doc_id,requirement_id,original_received,issuer,author,recipient,issue_date,source_verification,original_location,digital_sha256,relationship_status,decision,display_boundary
SYNTHETIC_SAMPLE_ONLY,SYN-0118-001,0118,I19-E05,NO,NOT_PROVIDED,NOT_PROVIDED,NOT_PROVIDED,NOT_PROVIDED,NOT_RUN,NONE,NOT_APPLICABLE,UNKNOWN,HOLD_NO_ORIGINAL,SYNTHETIC_NOT_EVIDENCE


## SOURCE: SYNTHETIC_REPLACEMENT_REGISTER_0118_R01.csv
SHA-256: `acfc9aac8b04760f34df5a55db6bbc1f867a02e20c18fafdc893b4a9eecddd8d`

field_path,sample_value,status,replacement_or_verification_required,real_evidence_location
record_class,SYNTHETIC_SAMPLE_ONLY,SYNTHETIC,Replace only with a real controlled record when one exists,RESTRICTED_ASSOCIATION_REPOSITORY
record_id,SYN-0118-001,SYNTHETIC,Assign a unique association-controlled case ID,RESTRICTED_ASSOCIATION_REPOSITORY
original_received,NO,SYNTHETIC,Record actual receipt date method and custodian only after original arrives,RESTRICTED_ASSOCIATION_REPOSITORY
issuer,NOT_PROVIDED,SYNTHETIC,Identify the issuing organization from the original and verify independently,RESTRICTED_ASSOCIATION_REPOSITORY
recipient,NOT_PROVIDED,SYNTHETIC,Replace only after authorized handling of actual recipient information,RESTRICTED_ASSOCIATION_REPOSITORY
issue_date,NOT_PROVIDED,SYNTHETIC,Transcribe from the original and cross-check context,RESTRICTED_ASSOCIATION_REPOSITORY
source_verification,NOT_RUN,SYNTHETIC,Record a real independent verification channel and response reference,RESTRICTED_ASSOCIATION_REPOSITORY
original_location,NONE,SYNTHETIC,Record restricted paper archive or native file location after receipt,RESTRICTED_ASSOCIATION_REPOSITORY
digital_sha256,NOT_APPLICABLE,SYNTHETIC,Hash the preserved original digital bytes or scan derivative and label which was hashed,RESTRICTED_ASSOCIATION_REPOSITORY
relationship_status,UNKNOWN,SYNTHETIC,Verify relevance to the actual training or service and period,RESTRICTED_ASSOCIATION_REPOSITORY
decision,HOLD_NO_ORIGINAL,SYNTHETIC,Replace only after all source integrity relevance and privacy checks,RESTRICTED_ASSOCIATION_REPOSITORY


## SOURCE: candidate_text_exact_R05.md
SHA-256: `0265e405f43dfa5d0fe3a295a5d413745d9aa94dd4ce3d6cae4f3913b988af78`

# Exact DOCX body extraction | SHA-256 `aa6ee02e2b3ae7c0ef06e74cad6333f2ddcc3bc306651f4e3e5694ecf5838707`

感謝函原件收存與核驗登錄表

文件 ID：0118 ｜ 官方需求 ID：I19-E05 ｜ 版本：R05

1. 文件用途、官方來源、證據效力及邊界

1.1 本文件是什麼

本文件是可重複使用的收件登錄表、原件保管紀錄與核驗清單，供協會授權的訓練行政承辦人逐件登錄實際收到的第三方來函，並由第二位指定覆核人確認。

主要讀者：

承辦角色：協會指定的訓練行政承辦人，負責收件登錄與原件保管。

覆核角色：協會指定的第二位覆核人，負責確認文件完整性、來源核驗與指標關聯。

[TABLE]

角色聲明：上述角色為候選作業職責描述，不代表協會已任命任何人，也不代表協會已核准任何流程。實際任命與授權依協會正式程序辦理。

[/TABLE]

1.2 本文件不是什麼

禁止： 不是感謝函範本，不提供可套用的信箋版型。

禁止： 不代替感謝函原件；登錄表本身不構成第三方來函。

禁止： 不是感謝函內容的轉錄本，不重製第三方函文。

禁止： 不是正式接受、送審或核准文件。

1.3 官方綁定

[TABLE]

項目 | 值

Document ID | 0118

Requirement ID | I19-E05

文件名稱 | 感謝函原件收存與核驗登錄表

129-to-142 crosswalk | 1 份交付文件、0 份拆分、文件 ID 0118

Crosswalk SHA-256 | 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679

R04 Blueprint seed SHA-256 | 280783e0df4dc0b7aaaf4a8fbe826bc65e9ed9c683146eea1dfd25c0ae1c92e0

官方檢核表來源 | official_source_0108_r11.pdf 第 8 頁

PDF SHA-256 | 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709

第 8 頁逐頁文字抽取 SHA-256 | 57c6b33d70b665bd41b8d58ff58f5c0d78f9c2c751ccd9c6dd1b740b2fbf374e

第 8 頁摘錄 | 常見參考佐證列示「感謝函」

157 Blueprint 內部索引 | 129（非官方印製 checkbox 序號）

官方印製 checkbox 序號 | UNKNOWN_NOT_ASSERTED（待依正式原始頁面核實）

[/TABLE]

內部索引 129 在 03_157_CHECKBOX_BLUEPRINTS.md 中定義為「感謝函：真實原件取得，不偽造」。該索引屬內部定位用途，不得對外表述為官方印製流水號；在從正式原始頁面核實前，印製序號一律保持 UNKNOWN_NOT_ASSERTED。

1.4 證據效力與限制

感謝函可以作為官方檢核表列示的一種參考佐證。但是：

函件不自動證明訓練造成特定績效、服務結果或顧客價值提升。

感謝語句本身不等於因果成果。

無法辨認對象的截圖、與訓練無關的函件，不得推論為績效證據。

未取得原件或未能核驗來源時，一律採 HOLD，不得填成「已驗證」。

「可送人工審閱」不是協會正式接受；只有人類依正式規則決定，才能記錄接受或送審。

1.5 原件型態邊界（必須分開標記）

[TABLE]

型態代碼 | 定義 | 是否等同紙本原件 | 是否等同寄件者原生檔

PAPER_ORIGINAL | 實體紙本來函 | 是 | 不適用

SENDER_NATIVE_FILE | 寄件者提供之原生電子檔（來源仍須獨立核驗） | 不適用 | 是

SCAN_FROM_ORIGINAL | 由紙本原件製成之掃描副本 | 否 | 否

PHOTOCOPY | 影本 | 否 | 否

SCREENSHOT | 螢幕截圖 | 否 | 否（截圖不自動等同寄件者原生檔）

FORWARDED_CONTENT | 轉寄內容 | 否 | 否（轉寄不自動等同寄件者原生檔）

REQUEST_DRAFT | 索取稿／請求稿 | 否 | 否

NONE | 未收到任何原件 | 否 | 否

[/TABLE]

2. 單件收存登錄表

[TABLE]

使用方式：一筆來函一張表。可列印填寫或於受控系統中填寫。標示 [受限] 之欄位僅可填入協會授權的受限儲存位置，不得出現在公開證據包。

[/TABLE]

表 A｜基本收件登錄

[TABLE]

欄位 | 填寫內容

登錄代碼（唯一案號） | ________________________________

文件 ID | 0118（固定）

需求 ID | I19-E05（固定）

收件日期時間 | ________________________________

收件方式（紙本寄送／電子郵件／專人送達／其他：____） | ________________________________

收件操作者角色 | ________________________________

收件時件數（紙本件數／附件件數） | ________________________________

保管位置 [受限] | ________________________________

[/TABLE]

[TABLE]

規則：沒有原件時不得建立「已收件」紀錄。未收到原件者，表 B、表 C 中需依原件填寫的欄位標 NOT_APPLICABLE；表 D、表 E 依實際可查證範圍填寫 NOT_RUN、UNKNOWN 或已確認結果，不得由無原件推定來源或關聯；表 F 記錄 HOLD_NO_ORIGINAL（見第 5、6 章）。

[/TABLE]

表 B｜來函內容登錄

[TABLE]

欄位 | 填寫內容

來函機構 | ________________________________

寄件者職稱 | ________________________________

收件人／部門 | ________________________________

發函日 | ________________________________

函件主旨 | ________________________________

函件內容摘要（忠實描述，不擴張） | ________________________________

函件自述之訓練／服務名稱 | ________________________________

班次或期間 | ________________________________

函件所述支持內容及其範圍 | ________________________________

函件頁數 | ________________________________

附件件數與種類 | ________________________________

[/TABLE]

[TABLE]

摘要規則：內容摘要必須忠實反映函文，不得改寫為未經原件支持的成效聲明（例如「提升績效」「達成目標」等因果性表述）。

[/TABLE]

表 C｜原件型態與完整性

[TABLE]

欄位 | 填寫內容

原件型態（依 1.5 之代碼） | ________________________________

收到時檔案 SHA-256（數位件） | ________________________________

掃描副本 SHA-256（如另製掃描） | ________________________________

所雜湊之對象（原生檔／掃描副本，須明標） | ________________________________

紙本封存索引或檔案盒編號 [受限] | ________________________________

受限數位路徑 [受限] | ________________________________

保管人角色 | ________________________________

移交時間與紀錄 | ________________________________

可讀性（完整可讀／部分模糊／不可讀） | ________________________________

修改痕跡檢查（無／有，說明：____） | ________________________________

[/TABLE]

[TABLE]

規則：保留收到的原始位元組，不覆寫原檔。數位副本一律計算 SHA-256 並註明雜湊對象；紙本原件記錄封存索引或檔案盒位置。

[/TABLE]

表 D｜來源核驗

[TABLE]

欄位 | 填寫內容

查證日期 | ________________________________

查證管道（須為獨立取得之正式聯絡管道） | ________________________________

管道獨立性說明（如何獨立取得，非依函件自列） | ________________________________

查證對象／角色 | ________________________________

回覆或參考代碼 | ________________________________

核驗結論（已確認／未完成／NOT_RUN） | ________________________________

[/TABLE]

[TABLE]

規則：僅依函件內自列的電話、電郵或標誌，不足以完成來源驗證。不得假造聯絡、回覆或簽章查核結果；未執行者填 NOT_RUN。

[/TABLE]

表 E｜關聯性、隱私與保存期限

[TABLE]

欄位 | 填寫內容

與 I19-E05 關聯判斷（支持／不支持／不明） | ________________________________

關聯依據（函文所述訓練、服務、期間、受益內容） | ________________________________

是否涉及個資（是／否） | ________________________________

是否涉及保密或用途限制（是／否） | ____________________

使用授權狀態（已取得／未取得／待釐清） | ____________________

保存期限依據（正式規則／適用法規名稱、版本或來源） | ________________________________

保存起算點與預定屆期日（未查明填 UNKNOWN） | ________________________________

屆期處置方式／授權角色（未獲授權不得自行銷毀） | ________________________________

不適合公開之細節之受限位置 [受限] | ____________________

缺件／疑點 | ________________________________

[/TABLE]

表 F｜判定與覆核

[TABLE]

欄位 | 填寫內容

判定狀態（依第 4 章代碼） | ________________________________

判定理由 | ________________________________

補正事項 | ________________________________

補正責任角色 | ________________________________

補正期限 | ________________________________

覆核人角色 | ________________________________

覆核日期 | ________________________________

覆核結果 | ________________________________

去識別化公開證據代碼 | ________________________________

實際資料受限位置 [受限] | ________________________________

[/TABLE]

3. 核驗清單（逐項記錄觀察、狀態與證據位置）

[TABLE]

填寫方式：每一項分開記錄「觀察」「狀態」「證據位置」三欄。任一項未完成，不得跳至 ELIGIBLE_FOR_HUMAN_REVIEW。

[/TABLE]

[TABLE]

# | 核驗項目 | 觀察 | 狀態 | 證據位置 [受限]

1 | 原件是否實際收到；僅有請求稿、轉述、截圖或掃描影本時明確標記型態 | ________________________________ | □完成 □未完成 □N/A | ________________________________

2 | 來源身份是否由不依賴函件自述的正式管道確認 | ________________________________ | □完成 □未完成 □N/A | ________________________________

3 | 頁數、附件、字跡／檔案可讀性與收到版本是否完整 | ________________________________ | □完成 □未完成 □N/A | ________________________________

4 | 寄件機構、發函角色、收件對象與日期是否可追溯 | ________________________________ | □完成 □未完成 □N/A | ________________________________

5 | 函件是否連結正確訓練／服務與期間；不把稱謝推論為因果成果 | ________________________________ | □完成 □未完成 □N/A | ________________________________

6 | 是否有個資、保密、同意或用途限制；不適合公開之細節留在受限位置 | ________________________________ | □完成 □未完成 □N/A | ________________________________

7 | 紙本／數位保管位置、存取權限、移交紀錄及數位副本 SHA-256 是否完整 | ________________________________ | □完成 □未完成 □N/A | ________________________________

8 | 證據摘要是否忠實描述函文，未擴張為未證明之成效 | ________________________________ | □完成 □未完成 □N/A | ________________________________

9 | 是否有另一位協會指定覆核人檢視（未覆核＝未通過） | ________________________________ | □完成 □未完成 □N/A | ________________________________

10 | 保存期限依據、起算點、屆期日期及處置授權是否查明；未查明填 UNKNOWN 並依第 6.3 節保留 | ________________________________ | □完成 □未完成 □N/A | ________________________________

[/TABLE]

4. 判定矩陣（狀態、觸發條件與下一步）

[TABLE]

狀態代碼 | 觸發條件 | 下一步

RECEIVED_PENDING_CHECK | 已實際收到原件，核驗項目尚未全部完成 | 繼續逐項核驗；維持待檢，不得對外表述為已核驗

HOLD_NO_ORIGINAL | 未取得任何原件（僅有請求稿、轉述、空白稿或無件） | 取得原件前不得登錄為已收件／已核驗；啟動補件追蹤

HOLD_SOURCE_UNVERIFIED | 已有原件，但來源身份未由獨立正式管道確認 | 以獨立管道續查；查證未完成前維持 HOLD

HOLD_SCOPE_ / OR_PRIVACY_REVIEW | 關聯範圍、個資／用途授權或保存期限未釐清；缺漏妨礙來源／範圍判定；或疑似修改 | 先保留並送範圍／隱私審閱；疑點釐清前不採用

RETURN_FOR_SUPPLEMENT | 缺件、缺頁、缺附件、內容不足以致無法判讀 | 開立補正事項、責任角色與期限，退回補件

ELIGIBLE_FOR_ / HUMAN_REVIEW | 已取得原件，且來源、完整性、關聯、隱私／用途授權、保存期限／屆期處置等必要檢核全部完成，並經第二位覆核人檢視 | 送人工審閱；此狀態不是正式接受

NOT_ACCEPTED_ / CONFIRMED_COPY_ / OR_MISMATCH | 已確認為非原件、錯置文件、內容／發函者不符，或違反資料授權 | 寫明證據後拒絕採用；疑點未確認前不得使用本狀態

[/TABLE]

4.1 狀態流轉原則

未收到原件時，起始狀態是 HOLD_NO_ORIGINAL；在原件到達前不因任何補述而改變。

原件到達後 → RECEIVED_PENDING_CHECK → 依核驗結果分流至各 HOLD、RETURN_FOR_SUPPLEMENT 或 ELIGIBLE_FOR_HUMAN_REVIEW。

ELIGIBLE_FOR_HUMAN_REVIEW 僅表示可送人工審閱，不是協會正式接受；只有人類依正式規則決定才能記錄接受／送審。

NOT_ACCEPTED_CONFIRMED_COPY_OR_MISMATCH 僅在「已確認為非原件／錯置／不符／違反授權」時使用，並須寫明證據。疑點未確認時不得寫成造假，只能維持 HOLD 或 RETURN_FOR_SUPPLEMENT。

4.2 拒收、補正與保留條件

HOLD（保留待處）

沒有原件 → HOLD_NO_ORIGINAL；取得原件前不得登錄為已收件／已核驗。

只有截圖、轉寄、影本、空白稿 → 記錄實際型態並 HOLD；除非正式規則允許且來源已核實，否則不納入原件結論。

來源未獨立確認 → HOLD_SOURCE_UNVERIFIED。

關聯、個資／用途授權或保存期限未釐清，或疑似修改 → HOLD_SCOPE_OR_PRIVACY_REVIEW。缺頁／缺附件可由送件者補齊，且不妨礙來源、範圍與隱私判斷時，預設 RETURN_FOR_SUPPLEMENT；若缺漏妨礙上述判斷，先 HOLD，風險釐清後再決定補件或不採用。

RETURN（補件）

缺頁、缺附件、可讀性不足、內容無法判讀 → RETURN_FOR_SUPPLEMENT，須記錄補正事項、責任角色與期限。

REJECT（不採用）

僅在下列已確認情形標記 NOT_ACCEPTED_CONFIRMED_COPY_OR_MISMATCH：非原件、錯置文件、內容或發函者不符、違反資料授權。

必須寫明證據位置。

疑點未確認前不得寫成造假，不得標 NOT_ACCEPTED。

絕對禁止

禁止： 不建立或補寫任何真實第三方原件、寄件紀錄、查證回覆、核准或簽章。

禁止： 不因感謝語句而推論績效或成果。

禁止： 未覆核不得視同核驗通過。

5. 完整 SYNTHETIC 示範：沒有原件、沒有第三方確認（維持 HOLD_NO_ORIGINAL）

[TABLE]

邊界宣告：以下為唯一示範列，record_class = SYNTHETIC_SAMPLE_ONLY，display_boundary = SYNTHETIC_NOT_EVIDENCE。全部數值均為 SYNTHETIC，僅用於測試缺件處理流程。本示範不出現任何信箋內容、第三方名稱、真人、日期、簽名、印章、回覆、收件紀錄或協會決定，亦不得用來佐證 TTQS 成果。

[/TABLE]

5.1 示範資料列

[TABLE]

欄位 | 值

record_class | SYNTHETIC_SAMPLE_ONLY

record_id | SYN-0118-001

doc_id | 0118

requirement_id | I19-E05

original_received | NO

issuer | NOT_PROVIDED

author | NOT_PROVIDED

recipient | NOT_PROVIDED

issue_date | NOT_PROVIDED

source_verification | NOT_RUN

original_location | NONE

digital_sha256 | NOT_APPLICABLE

relationship_status | UNKNOWN

decision | HOLD_NO_ORIGINAL

display_boundary | SYNTHETIC_NOT_EVIDENCE

[/TABLE]

5.2 逐步演算（示範如何判定）

[TABLE]

步驟 | 檢查動作 | 示範觀察值 | 結果

1 | 是否實際收到原件？ | original_received = NO；original_location = NONE | 未收到 → 觸發 HOLD_NO_ORIGINAL

2 | 原件型態為何？ | 無件，型態 NONE | 不得建立「已收件」紀錄；表 B～表 E 之實體欄位維持 NOT_PROVIDED／NOT_APPLICABLE

3 | 來源是否已獨立核驗？ | source_verification = NOT_RUN（從未執行，非「查無結果」） | 未執行 → 不得填「已驗證」；即便未來執行，亦須以獨立管道為之

4 | 雜湊是否可計算？ | digital_sha256 = NOT_APPLICABLE（無檔案可雜湊） | 不得填任何雜湊值；不得以占位值冒充雜湊

5 | 與 I19-E05 關聯？ | relationship_status = UNKNOWN | 無函文即無關聯可判 → 維持 UNKNOWN，不得推論

6 | 決定 | — | HOLD_NO_ORIGINAL

7 | 能否送人工審閱？ | — | 否。原件未取得，§3 核驗清單第 1 項未通過；來源、完整性、關聯、隱私及保存期限均不能據此判定完成

8 | 能否記為正式接受？ | — | 否。任何狀態皆非接受；本筆更因缺件而完全排除於送審之外

[/TABLE]

5.3 示範邊界自白（須隨示範一併保存）

本筆沒有任何實際感謝函檔案。

寄件機構、寄件者、收件者、發函日均為 NOT_PROVIDED，不指向任何真實組織或個人。

來源查證 NOT_RUN，不存在任何查證回覆、聯絡紀錄或參考代碼。

保管位置 NONE，不存在任何封存索引、檔案盒或數位路徑。

未產生任何簽名、印章、核准、回覆、收件事件或協會決定。

本示範不得用於佐證 TTQS 成果，不得改寫為仿真信件。

5.4 替換清冊（真實化前須逐項替換）

[TABLE]

field_path | 示範值 | 狀態 | 替換／核驗要求 | 真實資料位置

record_class | SYNTHETIC_SAMPLE_ONLY | SYNTHETIC | 僅在存在真實受控紀錄時替換 | RESTRICTED_ASSOCIATION_REPOSITORY

record_id | SYN-0118-001 | SYNTHETIC | 改由協會指派唯一受控案號 | RESTRICTED_ASSOCIATION_REPOSITORY

original_received | NO | SYNTHETIC | 僅在原件實際到達後記錄真實收件日期、方式與保管人 | RESTRICTED_ASSOCIATION_REPOSITORY

issuer | NOT_PROVIDED | SYNTHETIC | 依原件辨識發函機構，並獨立核驗 | RESTRICTED_ASSOCIATION_REPOSITORY

recipient | NOT_PROVIDED | SYNTHETIC | 僅在授權處理真實收件人資訊後替換 | RESTRICTED_ASSOCIATION_REPOSITORY

issue_date | NOT_PROVIDED | SYNTHETIC | 自原件抄錄並與脈絡交叉核對 | RESTRICTED_ASSOCIATION_REPOSITORY

source_verification | NOT_RUN | SYNTHETIC | 記錄真實獨立查證管道與回覆參考代碼 | RESTRICTED_ASSOCIATION_REPOSITORY

original_location | NONE | SYNTHETIC | 收件後記錄受限紙本封存或原生檔位置 | RESTRICTED_ASSOCIATION_REPOSITORY

digital_sha256 | NOT_APPLICABLE | SYNTHETIC | 對保留之原始位元組或掃描副本計算 SHA-256，並標明雜湊對象 | RESTRICTED_ASSOCIATION_REPOSITORY

relationship_status | UNKNOWN | SYNTHETIC | 核驗與實際訓練／服務及期間之關聯 | RESTRICTED_ASSOCIATION_REPOSITORY

decision | HOLD_NO_ORIGINAL | SYNTHETIC | 僅在來源、完整性、關聯、隱私全部檢核完成後方可改判 | RESTRICTED_ASSOCIATION_REPOSITORY

[/TABLE]

6. 證據保管、隱私與資料分層

6.1 三層資料分層

[TABLE]

層級 | 內容 | 位置

公開證據包 | 經授權可公開之去識別化代碼及摘要；檔案雜湊依資料規則核准後提供 | 可對外之證據包

受限作業層 | 原件本體、保管位置、存取權限、移交紀錄 | 協會授權受限儲存 [受限]

受限身分對照層 | 接觸個資之身份對照、聯絡紀錄、實際收件人／寄件者資訊 | 協會授權受限儲存 [受限]

[/TABLE]

6.2 保管鏈要求

（1）收件：記錄實際收件方式、時間、件數與保管位置；無原件不建「已收件」紀錄。

（2）保全：保留收到的原始位元組，不覆寫原檔；數位件計 SHA-256 並標明雜湊對象；紙本記錄封存索引／檔案盒編號。

（3）移交：每次移交記錄移交時間、交出方角色、接收方角色；保管人變更須留紀錄。

（4）存取：受限位置僅開放協會授權人員；存取權限本身亦屬受控欄位。

（5）對照隔離：個資身份對照與聯絡紀錄只放受限位置，不得進入公開證據包。

6.3 隱私與使用限制規則

涉及個資、保密、同意或用途限制者，判定為 HOLD_SCOPE_OR_PRIVACY_REVIEW，直至釐清。

不適合公開的細節一律留在受限位置；公開層僅保留去識別化代碼與摘要。

未取得使用授權前，不得將函件內容納入任何對外資料。

保存期限、起算點與屆期處置須依正式規則或適用法規的名稱、版本／來源核驗；未查明填 UNKNOWN，維持 HOLD_SCOPE_OR_PRIVACY_REVIEW。不得自行設定期限、對外公開或銷毀；屆期後僅依已授權處置程序辦理並留存紀錄。

違反資料授權且已確認者，方可標 NOT_ACCEPTED_CONFIRMED_COPY_OR_MISMATCH。

6.4 公開證據代碼規則

公開層僅使用去識別化證據代碼（例如依協會規則編配之代碼）。

代碼與受限資料之對照表僅存於受限位置。

公開層不得出現可識別機構、自然人或個案的資料。機構名、人名、聯絡方式、地址、發函日期及可組合識別的資訊先留在受限層；僅於正式授權範圍內核准揭露，並記錄授權依據。

7. 與相鄰文件的證據分界（負面鄰居辨識）

[TABLE]

原則：本文件標題隱去後，仍可由內容辨認其為 I19-E05 的「收存與核驗登錄工具」。本文件只登錄 0118 自己實際收到的第三方原件及核驗鏈，不撰寫或重製第三方函文。

[/TABLE]

[TABLE]

文件 ID | 需求 ID | 性質 | 與 0118 的分界

0092 | I17D-E06 | 第三方感謝函索取稿及證據驗證登錄 | 索取函不是收到的感謝函原件；0092 的請求稿不得充當 0118 之原件

0096 | I18-E03 | 其他官方需求之感謝函相關文件 | 不同指標；不得借用其指標、案例或結論代替 I19-E05

0103 | I18-E10 | 其他官方需求之感謝函相關文件 | 不同指標；不得借用其指標、案例或結論代替 I19-E05

0116 | I19-E03 | 訓後就業狀態證據 | 非同一證據來源；未經真實來源證明不得合併人員、期間或成果

0117 | I19-E04 | 考照結果證據 | 非同一證據來源；未經真實來源證明不得合併人員、期間或成果

[/TABLE]

7.1 分流檢查（收件時執行）

(1) 來件若為索取稿／請求稿 → 屬 0092 面向，不是 0118 原件；即使收到，也只記錄實際型態並 HOLD。

(2) 來件若為 I18-E03／I18-E10 面向之感謝函 → 不得併入 0118；指標與結論不可借用。

(3) 來件若為就業（0116）或考照（0117）資料 → 不得替代原件，亦不得與本筆合併人員、期間或成果。

(4) 只有實際到達 0118 之第三方原件及其核驗鏈，才登入本表。

8. 真實使用前的替換與升格檢核

8.1 現況宣告

目前沒有原始點協會的真實感謝函、寄件者確認、收件紀錄、授權或正式核准資料。所有示範值均為 SYNTHETIC；「沒有原件」之示範不得用來佐證 TTQS 成果。

8.2 逐件替換檢核（每筆真實資料上線前）

[ ] 由協會授權人員逐件替換全部示範值（依第 5.4 節替換清冊）。

[ ] 真實原件已保存於受限位置，紙本／原生檔／掃描副本三者分開標記。

[ ] 受限身分對照與聯絡紀錄已置於受限位置，未流入公開證據包。

[ ] 來源核驗以獨立取得之正式管道完成，回覆參考代碼已記錄。

[ ] 完整性、關聯、隱私三項檢核完成。

[ ] 第二位協會指定覆核人已檢視。

[ ] 判定狀態依第 4 章矩陣改判，理由與證據位置齊備。

[ ] 依機構正式流程決定是否納入送審資料（本表不作此決定）。

8.3 升格前技術 QA（三項分別完成，未完成不得升格）

[ ] Word 技術 QA 完成。

[ ] 每頁視覺檢查 完成。

[ ] 獨立 exact-SHA 語意審查 完成。

8.4 完整驗收對照

[TABLE]

驗收項 | 狀態

官方需求 I19-E05、crosswalk（1 交付／0 拆分／0118）、internal Blueprint index 129 綁定正確 | 已完成： 於第 1.3 節列示

印製序號保持 UNKNOWN_NOT_ASSERTED | 已完成： 於第 1.3 節列示

表單、原件保管、來源查證、完整性、關聯、隱私、補正／保留／拒收條件齊全且可操作 | 已完成： 第 2～4 章

唯一示範清楚標為合成；無假函、真人、第三方回覆、簽章、核准或真實協會決定 | 已完成： 第 5 章

所有示範值與替換項登錄一致；無虛構計算或成果圖 | 已完成： 第 5.1、5.4 節；本文件不含任何效益統計圖

與相鄰文件的證據所有權清楚 | 已完成： 第 7 章

Word 技術 QA、每頁視覺檢查、獨立 exact-SHA 語意審查分別完成 | □ 待執行（第 8.3 節）；未完成不得升格

[/TABLE]

8.5 全域禁止清單（適用於本表全部欄位）

禁止： 不撰寫或重製任何第三方函文、信箋或範本。

禁止： 不虛構人物、組織、日期、聯絡方式、回覆、簽章、印章、核准或簽收紀錄。

禁止： 不記錄任何真實收件事件、查證結果或協會決定，除非該事件確已發生並留有真實證據。

禁止： 不將任何 SYNTHETIC 值表述為 REAL。

禁止： 不添加無法由原件支持的績效統計、計算或成果圖。

禁止： 不將「可送人工審閱」表述為正式接受或送審完成。

本文件為候選作業工具，非正式接受文件。文件 ID 0118 ｜ Requirement ID I19-E05 ｜ 印製序號 UNKNOWN_NOT_ASSERTED ｜ 現階段 real_original_supplied: false，formal_acceptance: NOT_GRANTED。


## SOURCE: visual_R02_findings.json
SHA-256: `a164def1e749cbc91c12aa9e9937b3a47b42876437655d6c1bd06344902cd195`

{
  "doc_id": "0118",
  "requirement_id": "I19-E05",
  "candidate_sha256": "20ed29f9fc9934c7a5009d05f338844375a2fcf35d0b40d37dfd4493c089d127",
  "pdf_sha256": "556cc0c63f81cd7a109d1a5a177581aff4ed9df112e40af310a461b0d4820ef5",
  "pdf_bytes": 830893,
  "renderer": "Microsoft Word COM PrintOut to Microsoft Print to PDF",
  "word_pages": 13,
  "pdf_pages": 13,
  "page_pngs": 13,
  "pages_inspected": "1-13 all rendered at 983x1390 and visually reviewed",
  "visual_verdict": "FAIL_REPAIR_REQUIRED",
  "findings": [
    {
      "pages": [
        2,
        3
      ],
      "location": "§1.5 original-type matrix, first type-code column",
      "finding": "Codes such as PAPER_ORIGINAL and SENDER_NATIVE_FILE were fragmented into narrow character groups due to Word AutoFit.",
      "severity": "major readability/layout"
    },
    {
      "pages": [
        6,
        7
      ],
      "location": "§4 status decision matrix, status-code column",
      "finding": "Long status identifiers were fragmented into narrow character groups.",
      "severity": "major readability/layout"
    },
    {
      "pages": [
        9,
        10
      ],
      "location": "§5.4 replacement register, field_path column",
      "finding": "Field paths such as record_class and original_received were fragmented across many short lines.",
      "severity": "major readability/layout"
    },
    {
      "pages": [
        11
      ],
      "location": "§7 negative-neighbor table, Document ID column",
      "finding": "Four-digit document IDs wrapped (e.g. 0092 split into 009 and 2).",
      "severity": "minor readability/layout"
    },
    {
      "pages": [
        11
      ],
      "location": "§6.2 custody-chain list",
      "finding": "Automatic numbering continued at 5–9 rather than restarting at 1–5.",
      "severity": "material usability/sequence"
    }
  ],
  "other_pages": "No additional clipping, overlap, missing content, or footer defect observed in the inspected pages.",
  "candidate_modified_after_render": false,
  "observed_at": "2026-10-24T08:17:58+08:00"
}


## SOURCE: opencode_reviewer_R02_PASS_response.md
SHA-256: `cbad5a7a2742d4ca5caa57c601725492c3a849745f1ece030b3e550e8c4e2fb0`

**VERDICT: PASS**

**Exact candidate SHA-256 (as printed in packet):**
- Candidate DOCX: `20ed29f9fc9934c7a5009d05f338844375a2fcf35d0b40d37dfd4493c089d127`
- Exact body extraction: `344b49198b8b1b7fd483b374e95bda8dea4730829e7d02998db753ed72fdf523`

**Scope:** Read-only semantic review of the R02 candidate text for doc 0118 / I19-E05 (感謝函原件收存與核驗登錄表)， compared against the official page-8 source excerpt, unique Blueprint, crosswalk/mapping JSON, and the SYNTHETIC sample/replacement registers supplied in the packet. Text extraction only; no tool use.

**Findings (by section/table/item; severity):**

1. §1.3 official binding table — all cross-references match the packet exactly: crosswalk SHA (`1ddfbb60…`), blueprint seed SHA (`280783e0…`), PDF SHA (`805386b7…`), page-8 text SHA (`57c6b33d…`), crosswalk row (1 deliverable / 0 splits / 0118), internal index 129, printed serial UNKNOWN_NOT_ASSERTED. Page-8 excerpt quote is faithful to `official_source_page_08_text.txt`. — **No defect.**
2. §2 Tables A–F — all Blueprint 必備欄位 present: 登錄代碼， 收件日期時間/方式/件數/角色， 保管位置[受限]， 來函機構/職稱/收件人/發函日/主旨/摘要， 訓練/服務/期間/支持範圍， 原件型態(1.5 codes), 收件時及掃描 SHAs with hashed-object labeling, 封存索引/受限路徑/保管人/移交， 修改痕跡， 來源核驗(獨立管道/日期/對象/回覆代碼/NOT_RUN), 關聯判斷及依據， 個資/保密/授權， 缺件疑點， 判定/理由， 補正(事項/責任角色/期限)， 覆核(人/日期/結果)， 去識別化代碼及受限位置. — **Complete and usable.**
3. §3 checklist (items 1–10) — matches Blueprint's 9 items; item 10 (retention, with UNKNOWN fallback and §6.3 linkage) is a consistent, non-inventing addition. Gating: any incomplete item blocks ELIGIBLE_FOR_HUMAN_REVIEW. — **No defect.**
4. §4/4.1/4.2 — all 7 Blueprint status codes present with triggers and next steps; HOLD_NO_ORIGINAL default when no original; RETURN for supplementable gaps vs HOLD when gaps block source/scope/privacy review is coherent; REJECT (NOT_ACCEPTED) restricted to confirmed cases with recorded evidence, rebutting "疑點未確認不能寫成造假”. Escalation to human review correctly stated as NOT formal acceptance. — **No defect.**
5. §5.1/5.3/5.4 — sample row字面一致 with `SYNTHETIC_DATASET_0118_R01.csv` (all 15 fields including `display_boundary: SYNTHETIC_NOT_EVIDENCE`); replacement register matches `SYNTHETIC_REPLACEMENT_REGISTER_0118_R01.csv` (all 11 field rows, equivalent guidance, RESTRICTED_ASSOCIATION_REPOSITORY). No fabricated letterhead, names, dates, signatures, seals, replies, receipt events, or association decisions. — **No defect.**
6. §6.3 retention/privacy — retention period requires citing a formal rule/regulation name/version/source; start/end dates UNKNOWN when unidentified; no self-authorized destruction or publication; disposition only via authorized procedure with records. **No invented retention policy and no unauthorized destruction path.** — **No defect.**
7. §7/7.1 — the 5 negative-neighbor rows match `mapping_evidence_0118.json` exactly (0092/I17D-E06, 0096/I18-E03, 0103/I18-E10, 0116/I19-E03, 0117/I19-E04) with correct distinctions and intake routing tests. — **No defect.**
8. §8.1–8.5 — real-use gap declared verbatim-consistent with the source packet; QA/visual/semantic review marked □待執行， correctly NOT asserted complete; footer states `real_original_supplied: false, formal_acceptance: NOT_GRANTED`; no performance statistics or benefit charts added (per Blueprint prohibition). — **No defect.**
9. Minor / informational: (a) §1.1「角色聲明」and several §2 rules appear wrapped in `[TABLE]` extraction markers — likely single-cell tables or extraction artifacts; semantic content is correct, but layout requires later visual QA (already flagged pending in §8.3). (b) §8.3 checkbox lines read "[ ] … 完成。" — wording could be misread as completed; §8.4's「□待執行」disambiguates. — **Severity: informational only; no repair required for semantic correctness.**

**Minimum repair:** None required. Optional: clarify §8.3 wording (e.g., 「□ 待執行」per line) at next revision.

**Limitations:** No visual inspection of the rendered DOCX (no fonts, pagination, checkbox rendering, or table layout checked) — only the exact text extraction was reviewed, with tables represented as `[TABLE]` blocks. **SHA values were not recomputed in this review**; both SHAs are taken as stated in the packet. No tool use and no file access were employed. This review is a semantic assessment only and does not constitute, claim, or imply formal acceptance, approval, or authorization by any organization; the §8.3 QA items and formal disposition remain unexecuted.


## Current R05 technical check (candidate exact SHA bound)

SHA-256: `a0dc16e53d20e17b0687136b551842c1b5b1881d187f474961837dee144656f6`

```json
{
  "candidate_sha256": "aa6ee02e2b3ae7c0ef06e74cad6333f2ddcc3bc306651f4e3e5694ecf5838707",
  "bytes": 54957,
  "zip_integrity": "PASS",
  "python_docx_reopen": "PASS",
  "paragraphs": 138,
  "tables": 25,
  "rows": 166,
  "body_extraction_sha256": "0265e405f43dfa5d0fe3a295a5d413745d9aa94dd4ce3d6cae4f3913b988af78",
  "required_checks": {
    "版本：R05": true,
    "I19-E05": true,
    "保存期限依據": true,
    "預定屆期日": true,
    "不得自行銷毀": true,
    "SYNTHETIC_NOT_EVIDENCE": true,
    "HOLD_NO_ORIGINAL": true,
    "NOT_GRANTED": true,
    "（1）收件": true,
    "（5）對照隔離": true
  },
  "fixed_width_tables_inches": {
    "2": [
      1.7,
      1.7,
      2.05,
      1.66
    ],
    "15": [
      0.35,
      1.75,
      1.55,
      1.35,
      2.11
    ],
    "16": [
      1.8,
      2.75,
      2.56
    ],
    "20": [
      1.35,
      1.1,
      0.8,
      2.25,
      1.61
    ],
    "23": [
      0.6,
      1.0,
      2.1,
      3.41
    ]
  },
  "auto_fit_disabled": {
    "2": true,
    "15": true,
    "16": true,
    "20": true,
    "23": true
  },
  "warnings": [],
  "render_pdf_sha256": "9111274aa0b3932b43d4ceab6d42a27dae8cde3e6a155962715103e9ebd5e9e0",
  "render_manifest_sha256": "93c04d38df892c9b9521469e2950dae6c3671752b0cb977b7009652762dab024",
  "visual_receipt_sha256": "02d344c32f228b004079aa8a64baa5e3b90e2b068851dd7241c9cd6fb3210bb9",
  "candidate_state": "CANDIDATE",
  "formal_acceptance": "NOT_GRANTED"
}
```

## Current R05 full-page visual inspection (all pages)

SHA-256: `02d344c32f228b004079aa8a64baa5e3b90e2b068851dd7241c9cd6fb3210bb9`

```json
{
  "doc_id": "0118",
  "requirement_id": "I19-E05",
  "blueprint_index": 129,
  "candidate_state": "CANDIDATE",
  "candidate_docx_sha256": "aa6ee02e2b3ae7c0ef06e74cad6333f2ddcc3bc306651f4e3e5694ecf5838707",
  "render_method": "Microsoft Word COM PrintOut to Microsoft Print to PDF; rendered PNGs with pypdfium2 scale 1.65",
  "pdf_sha256": "9111274aa0b3932b43d4ceab6d42a27dae8cde3e6a155962715103e9ebd5e9e0",
  "pdf_page_count": 11,
  "render_manifest_sha256": "93c04d38df892c9b9521469e2950dae6c3671752b0cb977b7009652762dab024",
  "verdict": "PASS",
  "inspected_pages": [
    {
      "page": 1,
      "png_sha256": "4c233d056c7df95d2a5b4c762102f3dc34c9e0ce2428ca1f23adc672f55dc537",
      "inspection": "PASS"
    },
    {
      "page": 2,
      "png_sha256": "6018d74729a9f5d69c30e8744babbbcadbf9f8e3bc183c58a022e9c6fa180909",
      "inspection": "PASS"
    },
    {
      "page": 3,
      "png_sha256": "e7ca94c9dfefcb306d7e265e1c0c826676f49b613ceaddbb7213f804e7fff7b2",
      "inspection": "PASS"
    },
    {
      "page": 4,
      "png_sha256": "53604b107a10df42ac07b2dd33cb3240571d464b03a20cf2e0820ac2d5007d25",
      "inspection": "PASS"
    },
    {
      "page": 5,
      "png_sha256": "98604b51009ee3a041217bf74bcd413854f896373c60e06a638625ce19de48b1",
      "inspection": "PASS"
    },
    {
      "page": 6,
      "png_sha256": "6795f9e2f5cbc119396ace0853024ffac0b1b98bd2e2d8ed426ebcd9d0d13c3a",
      "inspection": "PASS"
    },
    {
      "page": 7,
      "png_sha256": "3d15898026f2ed22903c15f751522e009d4a9f8d7c1737424c4b2421c36c0675",
      "inspection": "PASS"
    },
    {
      "page": 8,
      "png_sha256": "0aa2042a73f3d998808dba39316619bf9bf371f29146f2162961873e5aea2a5c",
      "inspection": "PASS"
    },
    {
      "page": 9,
      "png_sha256": "de4378431a44fb4dc6f343bfbe440780e2a91e3fb8718a68a559f8c3eca522ca",
      "inspection": "PASS"
    },
    {
      "page": 10,
      "png_sha256": "a181de81797b7384bb57e1c972b43c0730a0ac1b0bdb9fce64834e1c12a622a8",
      "inspection": "PASS"
    },
    {
      "page": 11,
      "png_sha256": "754898fcdb691abb8836eea4c3fd739a6453e8d8f193fda63a1e8583a63d22eb",
      "inspection": "PASS"
    }
  ],
  "page_specific_checks": {
    "1": "R05 title black; no title rule; no clipping.",
    "2": "Source-form codes SCAN_FROM_ORIGINAL and FORWARDED_CONTENT fit without mid-token splits.",
    "3": "Table C integrity notice stays together; no orphaned final word.",
    "4": "Tables D and E readable and intact.",
    "5": "Table F heading and header are together at page start; table body readable.",
    "6": "Checklist and decision matrix readable; long state identifiers break only at underscores.",
    "7": "Decision rules readable; synthetic example clearly introduced and separated.",
    "8": "Worked synthetic decision table complete and readable.",
    "9": "Replacement register continuation readable; no clipped columns.",
    "10": "Cross-document boundary table readable; I19-E05 routing steps restart and run (1) through (4).",
    "11": "Pre-use checklist, status and footer readable; no clipping/overlap."
  },
  "resolved_findings_from_R03": [
    "Title blue bottom border removed; title/headings black.",
    "Table C notice row no longer breaks at its final word.",
    "Table F caption/header no longer stranded on the previous page.",
    "Long form-code identifiers no longer split inside a word.",
    "Section 7.1 numbering restarts at (1); no inherited list continuation.",
    "Table 2 OOXML grid widths now match every row cell width."
  ],
  "limitations": [
    "Visual inspection does not constitute semantic acceptance.",
    "No REAL thank-you letter, third-party identity, approval or receipt is present.",
    "Formal association acceptance is NOT_GRANTED."
  ]
}
```
