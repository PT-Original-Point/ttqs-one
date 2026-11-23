WORK_ID=TTQS_ONE_0030_I06-E01_INDEPENDENT_SEMANTIC_REVIEW_R02_BUNDLED_20261118
DOC_ID=0030
REQUIREMENT_ID=I06-E01
REQUESTED_MODEL_ROUTE=opencode/nemotron-3.5-lightning-free
ROLE=independent semantic/usability Reviewer; not Writer
CANDIDATE_DOCX_SHA256=517C5BDB84033977505D691FC8983A7DDB023E0BD34213E35CFE007AE21B50AB
SOURCE_PACKET_SHA256=EB9C30258AEED09987EE6DCB859C871073C0F595A4F1BA4E8F7226826CB65784
UNIQUE_BLUEPRINT_SHA256=2DB9E1AA4DF4FE20C78EF52F647C9513B8158AF9C28EE38BA5F87DC1416FE4E9
EXTRACTED_BODY_SHA256=42EC0EADCEBB59C922F8656879C0DD6EB404237B5E1425D2D904F31AF2A6282A
REVIEW_SCOPE=Semantic, requirement alignment, usability, sample truth-boundary and consistency only. Visual rendering remains separate.

INSTRUCTIONS
Independently review whether the candidate correctly addresses I06-E01 and the dedicated Blueprint; is complete and directly usable as a training-institution SAMPLE/SYNTHETIC worked example; has operational process/evidence controls; has consistent calculations and logic; clearly separates SAMPLE from REAL; avoids unsupported third-party claims and placeholder-only content. Do not trust Builder/QA self-claims as proof. Do not edit files or call tools. Return exact candidate SHA; RESULT=PASS/SCOPED_FAIL/FAIL/INSUFFICIENT_EVIDENCE; findings with severity, paragraph/table locator, short excerpt max 25 Chinese characters, problem and minimal correction; confirm visibility of the evidence index, synthetic fact register, per-ID replacement register, and full workflow example; include REVIEWED_INPUT_SHA256 matching the extracted body; mark unverifiable claims UNKNOWN. Do not assess layout, claim visual pass, rewrite content, or return ACK-only.

===== SOURCE PACKET =====
# 來源包｜0030｜I06-E01

## 對應與就緒判定
- doc_id：0030；requirement_id：I06-E01。
- crosswalk 列：I06-E01｜deliverable_count=1｜split_extra_count=0｜deliverable_ids=0030｜document_titles=工作經驗的相關受訓證明_可直接使用成品。
- 本 stage 僅產生來源包及專屬 Blueprint；不建立 DOCX，不派 Writer，不修改共享狀態。
- READY_SOURCE_PACKET：PASS。官方來源、crosswalk、157 格 Blueprint 索引及頁文讀回可讀，且原始 SHA 已固定。
- READY_UNIQUE_BLUEPRINT：PASS。157 格索引第 029 列提供本件專屬文類邊界。

## 官方需求定位
- 正式來源：TTQS 官方評核指標及常見參考佐證資料表。
- PDF：docs/ttqs-quality-20261016/quality-review/0026_R11_20261117/source/inputs/OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf；SHA-256 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709。
- PDF 第 2 頁（共 9 頁），頁面下方印刷頁碼 2；分類「能力」；指標 6「訓練機構的行政管理能力及訓練主管相關職能」。
- 官方勾選文字：□ 工作經驗的相關受訓證明。
- crosswalk 交付標題逐字保留：工作經驗的相關受訓證明_可直接使用成品。
- 完整頁文 readback SHA-256：3C295E8861AD7775A78583E9111DF61AC8733A7CF40D771F942363F00572DE9C。本 sidecar 檔與 tracked page text input raw bytes 相同；input SHA-256：3C295E8861AD7775A78583E9111DF61AC8733A7CF40D771F942363F00572DE9C。
- 官方頁面 fresh raster：receipts/official_page2_R01.png，SHA-256 F917F8633BBF8C890A45CD02DB4D8EB72245D1AAE91AFFFF4D966417F9355842；直接視覺核對確認印刷頁碼、指標 6 與勾選文字。
- 精簡逐字節錄 SHA-256：ABB92E0EDF1F358809CEF67388853AE13CE9AEDB14F652D8CE02EDD33F3B86B2。

文字讀回方法：本機沒有 pdftotext，Python 3.15 亦未安裝 pypdf，因此不宣稱本輪重新執行 PDF 文字抽取。使用與同一官方 PDF SHA 綁定的既有整頁文字 readback，並以本輪從原 PDF 直接 raster 的第 2 頁核對所需文字。Poppler 曾提示 Symbol 及 ArialUnicode display font；目標段落清晰可辨，方框和文字均可核對。

## 範圍與收錄內容
1. 規定相關工作經驗／受訓證明索引欄位及來源定位。
2. 定義原件提出、取得、真偽查核、相關性判斷、保管與異常處理流程。
3. 對應證明與訓練機構角色／職務要求；每項連結可回查來源及頁碼。
4. 未取得原件時明列 UNKNOWN、追索步驟及結論限制。
5. 規定不冒充真實受訓或工作經驗的 SAMPLE/SYNTHETIC 流程案例和逐項事實登錄。

不包含實際證書、出勤證明、受訓名冊、雇主證明、第三方核驗結果、真實個資或真實能力結論；本階段不產生這些原件，不涉及其他 doc_id。

## 未知事項
以下均為 UNKNOWN，不得推定或填 0：實際人員身分、雇主、職務期間、課程／活動、日期、時數、出勤、結業、發證者、證書編號、原件位置與真偽、雇主／提供者聯絡與回覆、個資授權、保存期限、真實職能、真實績效及協會接受狀態。取得真實原件前，不得聲稱曾任職、曾參訓、已出席、已結業或已核驗；不得臆造取得、查核或認定責任人及授權。

## SAMPLE / REAL 邊界
- SAMPLE/SYNTHETIC 僅示範索引欄位、取得步驟、查核狀態與不成立時的決策；每個合成值須有唯一 SYN-0030-* ID 並登錄。
- 不編造真實姓名、雇主、課程提供者、任職期間、受訓日期、出勤、時數、證書、簽章、發證或核驗成功。
- 可用「合成流程案件，原件未提供」展示完整流程：需求明確、來源 UNKNOWN、索取未實際送出、核驗未執行，結論 NO CLAIM / NOT VERIFIED。此為流程示例，不是經驗證明。
- REAL 取代只可由真實第三方原件或可追溯的雇主／發證者確認支持；記錄來源機構、文件名稱、原始頁碼／定位、收件和核驗日期／方法／依據、保管位置及存取限制。未能核驗則保持 UNKNOWN。
- 替換登錄描述所需原件與核驗狀態；不留空白表單，不以合成內容填 REAL 欄。

## 負向近鄰
- 0029｜I05-E03｜訓練規劃及達到客戶課程績效目標的證明資料_可直接使用成品：課程規劃與客戶績效目標，不是個人經驗／受訓證明索引。
- 0031｜I06-E02｜專業訓練人員職能評估方法等證明_可直接使用成品：能力量規與職能評估方法，不代替本件來源取得及真偽查核。
- 0032｜I06-E03｜訓練機構具備執行訓練業務相關職能的說明_完整工作稿：機構層級能力說明，不代替個人經驗／受訓來源索引。
- 只用 crosswalk 標題及 157 格需求描述劃分近鄰；未讀取、引用或複製任何鄰件 DOCX 正文。

## Provenance
觀察時間：2026-11-18T00:00:12.163+08:00
Repository：PT-Original-Point/ttqs-one
Branch：work/ttqs-one-document-quality-contract-20261016
Local HEAD：03348e7811dfe57a5b6e46efed1598b929db563d
GitHub branch live HEAD（ls-remote）：03348e7811dfe57a5b6e46efed1598b929db563d

| 來源 | 路徑 | SHA-256 |
|---|---|---|
| Human 最新指令 | 本對話直接提供，非檔案 | 不適用 |
| AGENTS.md | E:\TTQS\AGENTS.md | 60F945A5C863CE654F3229EA999745BC06F34E4EF6D0C9120890A6553B0A6008 |
| 04 活躍控制副本 | E:\TTQS\_ttqs_one_r12_publish_20261108\docs\ttqs-quality-20261016\04_CODEX_GOAL_24X7_EXECUTION.md | 92631B381CF914396040782E4CACB7A5B496D95E1E1733C2E964CB209572719E |
| 05 活躍控制副本 | E:\TTQS\_ttqs_one_r12_publish_20261108\docs\ttqs-quality-20261016\05_HOURLY_NATIVE_WAKE_RESUME.md | 7FB9A77E6B26A4987CEBDDE9F33DE49FDF2C75DC523A6D3BDBF4C57FCB26379B |
| 06 最新增量副本 | E:\TTQS\_ttqs_one_r12_publish_20261108\docs\ttqs-quality-20261016\06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md | 0D14D4973010413620903CBCDD13527E6388A9D174226881F35AB589AA525C0F |
| R12 任務控制 | 0026 source/inputs/PR92_R12_EXECUTION_SPEC_R12_20261026.md | 8385BB2D33CB8497CC0864625D1DA57B96536014B134CED1E7F9B1B05225D23E |
| crosswalk | 0026 source/inputs/CROSSWALK_129_TO_142_R01.csv | 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679 |
| 157 格索引 | 0026 source/inputs/BLUEPRINT_157_CHECKBOXES_LIVE_R01.md | AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216 |
| 官方 PDF | 0026 source/inputs/OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf | 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709 |
| 整頁文字讀回輸入 | 0026 source/inputs/OFFICIAL_SOURCE_PAGE2_READBACK_R01.txt | 3C295E8861AD7775A78583E9111DF61AC8733A7CF40D771F942363F00572DE9C |

04/05/06 在 E:\tqrepo checkout 不存在。上述 SHA 是本輪實際讀取的 E:\TTQS R12 publish 本機副本，不宣稱它們屬於本 branch HEAD；R12 指揮書則位於本 branch 的 0026 source/inputs。本來源包僅記錄控制 provenance，不修改控制文件。

## 結論限制
- 本 source packet 通過不等同 DOCX 完成、真實原件存在、獨立審查、正式接受或 REAL。
- 真實原件、第三方回覆及正式認定未提供，只阻擋日後 REAL 替換／正式接受，不阻擋本 source/Blueprint stage。
- 無 Human Gate 阻擋本次來源包或 Blueprint。
===== UNIQUE BLUEPRINT =====
# 專屬 Unique Blueprint｜0030｜I06-E01

## 文件識別與對位

- 文件標題（逐字依目前 crosswalk）：工作經驗的相關受訓證明_可直接使用成品
- doc_id：0030；requirement_id：I06-E01。
- 官方來源：TTQS 評核指標及常見參考佐證資料表，PDF 第 2 頁／印刷頁碼 2；指標 6「訓練機構的行政管理能力及訓練主管相關職能」。
- 官方勾選文字：□ 工作經驗的相關受訓證明。
- 157 格 Blueprint 索引列：029｜受訓與工作經驗：真實證明索引及取得規程，不偽造。
- 上游來源包：source/SOURCE_PACKET_0030_I06-E01_R01.md
- 上游來源包 SHA-256：EB9C30258AEED09987EE6DCB859C871073C0F595A4F1BA4E8F7226826CB65784
- 本檔只規範 0030 後續文件；不是成品 DOCX、證書或第三方證明。

## 文類與使用目的

建立供訓練機構實際維護、供評核者抽查的「相關工作經驗／受訓證明索引與原件取得及查核流程」。使用者應能定位每件真實佐證的原始來源及頁碼，追蹤原件取得與來源核驗，並判斷資料是否與指定訓練角色／職務相關。

本文件本身不是證書、出勤證明、履歷、雇主證明、職能評估報告或機構能力說明；不得自行宣稱任何人曾任職、曾受訓或已符合職能。

## 文件必備結構與操作機制

1. **封面及狀態**：完整標題、0030、I06-E01、候選版本、SAMPLE/SYNTHETIC 範圍聲明。
2. **用途、對象與資料保護**：界定索引的維護、查核與閱覽角色；未經實際組織資料確認，不得填真名、授權職稱、保存期限或存取權限。
3. **證據索引**：每筆唯一 Evidence ID；欲支持的工作／訓練主張；證明類型；出具者／來源機構；文件名稱；原件／副本狀態；原始頁碼或定位；實際收件日期及方式；查核對象、管道、依據、時間和結果；對應角色；保管位置及存取限制；期限依據；當前狀態與後續處置。
4. **原件取得流程**：確認需求 → 確認資料保管者及合法授權 → 實際索取並保存送出證據 → 收件登錄、核對完整性及定位 → 以獨立且可追溯方式核對出具者和文件狀態 → 比對對象、日期、內容及角色關聯 → 記錄查核結論、限制和覆核者 → 依已證實的政策管理原件。
5. **查核及結論規則**：區分「文件被提及」「收到副本」「收到原件」「出具者核實」「內容相關」「職能已評估」。不把一種狀態合併成「已證明」；不由參訓紀錄直接推論任職、職能或績效。
6. **異常處理**：未取得、出具者無法聯絡、內容不一致、影本不完整、授權未知、保存依據未知等，各自記錄 UNKNOWN、原因及允許的下一步；不得猜補。
7. **SAMPLE/SYNTHETIC 流程案例**：依下節完整展示一個原件未提供、未作真實經驗主張的索引流程及結果。
8. **REAL 替換登錄**：逐欄說明實際資料、原件、授權與核驗條件；未提供處填明 UNKNOWN 及追索條件，不交付空白表單。
9. **來源及版本**：註記官方 PDF 頁碼與 checkbox、crosswalk 對應列、157 格索引 row 029、候選版本與來源變更方式。

## 完整 SAMPLE/SYNTHETIC 案例要求

示例必須是一個「合成流程案件」，不得虛構人物、雇主、機構、課程、活動或實際參訓；不建立或仿造證書、簽章、名冊、出勤、發證者回覆或核驗結果。用一筆唯一 SYN-0030-* 識別碼，走完需求辨識到決策及後續動作：

| 欄位 | 完整示例必須呈現 |
|---|---|
| 流程案 ID | 唯一 SYN-0030-*；醒目聲明只是文件內合成識別碼 |
| 待支持主張 | 需查找與指定訓練角色相關的工作經驗／受訓證明；不得聲稱主張已成立 |
| 真實主體、出具者、文件及來源 | 全部明列 UNKNOWN（未提供）；不得造姓名、雇主、課名或文件名 |
| 索取準備 | 記錄預期資料類型、合法聯絡及授權狀態；標示尚未實際寄送 |
| 收件與定位 | NOT_RECEIVED；原件、頁碼、保存位置均 UNKNOWN |
| 真偽及相關性查核 | NOT_PERFORMED；不得寫已確認、已驗證或已符合 |
| 決策 | NO CLAIM / NOT VERIFIED；不得計為已具備證明或能力 |
| 後續 | 由實際授權者確認可聯絡來源、取得真實第三方原件後，按本流程逐項查核 |
| 事實登錄 | 所有示範 ID、流程狀態、程序決策各有唯一 SYN-0030-*；UNKNOWN 是真實來源缺席狀態，不登錄成合成真實事件 |

完整標準：讀者可循步驟重現案件如何建立、如何停在未取得／未核驗、為何不作主張、最後決策及下一步。所有欄位須有值或有原因的 UNKNOWN；不得留下空白欄位，不得宣稱實際事件發生。

## 專屬事實登錄要求

每個 SAMPLE/SYNTHETIC 值至少記錄：

- 唯一 Fact ID：SYN-0030-001 起順序遞增。
- 欄位／事實、型別、值及明示分類 SYNTHETIC。
- 僅供示範的說明及在正文、表格、流程圖、摘要中的使用位置。
- 來源性質；沒有外部來源的程序狀態必須標「合成流程示例，非外部事件」。
- 日後改為 REAL 所需原件、授權來源、查核方法及當前狀態。
- 對應角色／需求，以及是否允許形成實質證明主張。

不得只登記日期與數字而漏掉角色、程序狀態、推論、決策或結論。正文任何地方的合成文字或狀態都須能回溯到唯一 ID。UNKNOWN 必須維持為未知，不得用 SAMPLE 值填補。

## REAL 替換條件

真實資料只能來自可追溯的第三方原件或可驗證的雇主／訓練提供者確認。至少核實：

- 資料主體、與機構關係及資料使用授權；
- 出具者、文件名稱、日期／期間、原件或副本狀態、原始頁碼／位置；
- 收件時間、方式、保管位置及存取控管（若適用）；
- 出具者核驗的聯絡來源、時間、方法、回覆及查核者；
- 與訓練角色／工作主張的關聯和限制；
- 「曾任職」「曾參訓」「出勤」「結業」等每一主張各自對應的證據；
- 保存期限及處置政策來源；無來源時保持 UNKNOWN。

自述、合成資料、無法核驗的影本、未授權個資或推測均不足以升格 REAL。沒有原件或授權不得作為已證明。

## 負向近鄰拒收測試

- 0029 I05-E03「訓練規劃及達到客戶課程績效目標的證明資料」：課程規劃／客戶目標證明，不是本件。
- 0031 I06-E02「專業訓練人員職能評估方法等證明」：職能量規／評估方法，不是本件來源索引。
- 0032 I06-E03「訓練機構具備執行訓練業務相關職能的說明」：機構能力說明，不是本件個人證明索引。
- 移除標題後仍可由索引欄位、原件取得和真偽查核內容識別本件；不得複用鄰件正文、表格或案例。

## 逐項驗收測試

| ID | PASS 條件 | FAIL 條件 |
|---|---|---|
| BP-01 對位 | 標題逐字符合 crosswalk；0030／I06-E01／官方 p.2 checkbox／索引 row 029 全部一致 | 任一 ID、標題、頁碼或 checkbox 錯置 |
| BP-02 文類 | 有可操作的證據索引、原件取得及真偽查核流程 | 泛用培訓說明、空白證書或職能量規 |
| BP-03 來源 | 每項實質主張可回查原件、頁碼、出具者及核驗依據 | 僅憑自述、內部草稿或無定位的「已證明」 |
| BP-04 合成案例 | 完整示範至 NO CLAIM / NOT VERIFIED，所有欄位有值或具因由 UNKNOWN | 假造工作期間、出勤、課程、原件、簽章或驗證 |
| BP-05 事實清冊 | 每個合成流程值有唯一 SYN-0030-*，無未登錄正文／圖表值 | ID 重複、值漏登或合成值進入 REAL 欄 |
| BP-06 未知界線 | 原件缺失明列 UNKNOWN、原因及取得條件 | UNKNOWN 被寫成 0、推定事實或完成 |
| BP-07 關聯判斷 | 說明資料與訓練角色的關聯與限制 | 把參訓、任職、能力或績效混為單一主張 |
| BP-08 近鄰 | 不複製且 title-blind 不會誤認 0029／0031／0032 | 落入客戶績效、量規評估或機構能力文類 |
| BP-09 可操作 | 有可直接照做的索引與取得程序，不是留待使用者設計的空表 | 大量待填／待核，或缺少處理步驟 |
| BP-10 可讀性 | Word 正文至少 10.5 pt、表格至少 9.5 pt，來源狀態易查 | 縮字或塞表以掩蓋缺漏 |
| BP-11 保護 | 個資授權、存取、保存期均有來源；未知明列 UNKNOWN | 編造期限、公開個資或無權傳閱 |
| BP-12 精確來源 | 收錄官方定位、crosswalk row、索引 row 與該候選的來源 SHA 綁定 | 泛稱來源或 SHA 與實際輸入不一致 |

## 狀態限制

Blueprint 通過僅代表後續 Writer 有足夠且專屬的規格，不表示 DOCX 已完成、品質已驗收或 REAL。未取得真實原件時，實際經驗、參訓、出勤、結業、發證和雇主確認均維持 UNKNOWN。不得升格為 CURRENT、REAL、正式接受或協會核准；後續候選仍需確定性 QA、適用視覺驗收及不同 Writer 的獨立語意審查。
===== EXACT DOCX BODY EXTRACT =====
工作經驗的相關受訓證明_可直接使用成品
文件文類：證據索引與原件取得及查核流程
SAMPLE/SYNTHETIC — 本文件為候選版本（CANDIDATE），包含合成範例僅示範流程，不主張真實人員、雇主、資歷或成就。
文件編號：0030
需求識別：I06-E01
版本狀態：CANDIDATE — 候選文件，僅供規格審查，不等同正式文件、真實原件或 REAL 替換。
適用對象：協會作業人員，用於工作經驗／受訓證明之證據索引、取得、查核與保管流程導向。
使用說明
何時使用：於 I06-E01 需求啟動時，或評核前進行索引建構與查核程序檢視。本文件適用於 I06-E01 之 157 格 Blueprint row 029 文類邊界。
如何執行：依次參照本文件結構：「封面及狀態」「目的與範圍」「證據索引」「原件取得流程」「查核及結論規則」「異常處理」「SAMPLE/SYNTHETIC 流程案例」「REAL 替換登錄」。每個步驟均有明確輸入與輸出說明。
預期輸出：完整的證據索引登錄（每項唯一 SYN-0030-* 識別碼）、取得狀態記錄、查核結果判斷（NO CLAIM / NOT VERIFIED 適用於 SAMPLE/SYNTHETIC 案例）、SAMPLE/SYNTHETIC 案例展示、異常處理記錄。
狀態標記：CANDIDATE 級候選文件；SAMPLE/SYNTHETIC 案例標示合成性質，不得作為 REAL 資料使用或宣稱具備真實資歷、認可或成就。
重要聲明
本文件不包含實際證書、出勤證明、履歷、雇主證明、職能評估報告或機構能力說明。
真實原件、第三方回覆及正式認定未提供，只阻擋日後 REAL 替換／正式接受，不阻擋本 source/Blueprint stage。
所有合成值均有唯一 SYN-0030-* ID，未提供之 REAL 欄位明列 UNKNOWN，並說明需 genuine source 支撐。
不得冒充真實受訓或工作經驗；不得填寫真實姓名、雇主、課程提供者、任職期間、受訓日期、出勤、時數、證書、簽章、發證或核驗成功。
鄰近需求（0029｜I05-E03、0031｜I06-E02、0032｜I06-E03）內容被明確排除，僅依 I06-E01 與 row 029 為準。
目的與範圍
本文件建立供訓練機構實際維護、供評核者抽查的「工作經驗／受訓證明索引與原件取得及查核流程」。使用者應能定位每件真實佐證的原始來源及頁碼，追蹤原件取得與來源核驗，並判斷資料是否與指定訓練角色／職務相關。
本文件本身不是證書、出勤證明、履歷、雇主證明、職能評估報告或機構能力說明；不得自行宣稱任何人曾任職、曾受訓或已符合職能。
範圍界定
適用需求：僅 I06-E01。鄰近需求 0029（I05-E03）、0031（I06-E02）、0032（I06-E03）內容被明確排除，僅依官方checkbox行 029 為準。
文類邊界：157 格 Blueprint row 029「受訓與工作經驗：真實證明索引及取得規程，不偽造」所定義之文類。
crosswalk 對應：I06-E01│deliverable_count=1│deliverable_ids=0030│document_titles=工作經驗的相關受訓證明_可直接使用成品。
官方定位：TTQS 評核指標及常見參考佐證資料表，PDF 第 2 頁／印刷頁碼 2；指標 6「訓練機構的行政管理能力及訓練主管相關職能」；官方勾選文字：□ 工作經驗的相關受訓證明。
文件類型說明
本文件屬「證據索引與取得規程」文類，而非成品 DOCX、證書或第三方證明。其目的是規範索引欄位、取得步驟、查核流程與異常處理，而非提供任何實際人員資料或能力結論。
證據索引
每筆唯一 Evidence ID；欲支持的工作／訓練主張；證明類型；出具者／來源機構；文件名稱；原件／副本狀態；原始頁碼或定位；實際收件日期及方式；查核對象、管道、依據、時間和結果；對應角色；保管位置及存取限制；期限依據；當前狀態與後續處置。
表 7-A：合成流程案例的證據索引列（不是實際第三方佐證）
欄位群組 | 索引欄位 | SAMPLE/SYNTHETIC流程示例記錄
識別 | 示例索引 ID | SYN-0030-001（僅此合成案例與索引列共用的示例識別碼；不是實際佐證編號）
主張 | 欲支持的主張 | SYN-0030-003：工作經驗與相關受訓證明之待支持主張；尚未成立
資料類型 | 證明類型 | SAMPLE/SYNTHETIC預期類型：工作經驗說明及相關受訓記錄；真實文件類型 UNKNOWN
來源 | 出具者／來源機構 | UNKNOWN（實際來源未提供）
來源 | 文件名稱 | UNKNOWN（原件未提供）
原件 | 原件／副本狀態 | SYN-0030-011：NOT_RECEIVED；本示例未實際提出索取
定位 | 原始頁碼／位置 | UNKNOWN（尚無原件）
收件 | 實際收件日期／方式 | UNKNOWN（尚未收件）
查核 | 對象／管道／依據／時間／結果 | SYN-0030-012：NOT_PERFORMED；本示例未執行第三方核驗
關聯 | 對應職務／訓練角色 | SYN-0030-015：UNKNOWN／NOT_ASSESSED；實際職務與訓練角色資料未提供
保管 | 原件保管位置／存取限制 | UNKNOWN（原件與機構政策未提供）
有效性 | 期限／保存依據 | UNKNOWN（須查核正式政策來源）
結論 | 目前狀態 | SYN-0030-011／012：NOT_RECEIVED／NOT_PERFORMED
處置 | 決策及下一步 | SYN-0030-013：NO CLAIM / NOT VERIFIED；依 SYN-0030-014 的規程，取得授權與真實原件後再查核
上表為登錄結構說明；實際填寫時請依本文件各流程節規範登錄。所有 REAL 未提供欄位必須明列 UNKNOWN，並說明需 genuine source 支撐方能升級。
原件取得流程
確認需求：驗證 I06-E01 與 157 格 Blueprint row 029 之對應關係，確認官方勾選文字「工作經驗的相關受訓證明」。
確認資料保管者及合法授權：識別文件持有單位，確認合法授權文件或授權聲明。若無法確認授權，本欄位明列 UNKNOWN，並說明需授權文件方能進行。
實際索取並保存送出證據：向來源機構或雇主提出索取；收件登錄、核對完整性及定位。若原件未送達，記錄 NOT_RECEIVED 並說明追索條件。
收件登錄、核對完整性及定位：錄入證據索引，比對原始頁碼或定位（對應官方 PDF 第 2 頁、印刷頁碼 2）。若影本不完整，記錄不完全並說明補足條件。
以獨立且可追溯方式核對出具者和文件狀態：聯絡出具者、驗證文件狀態。若出具者無法聯絡或文件狀態不明，各自記錄 UNKNOWN、原因及允許的下一步；不得猜補。
比對對象、日期、內容及角色關聯：比對工作經驗描述、訓練課程、日期期間與指定角色之關聯。關聯性不足者，說明限制與不適用理由。
記錄查核結論、限制和覆核者：區分「文件被提及」「收到副本」「收到原件」「出具者核實」「內容相關」「職能已評估」。不把一種狀態合併成「已證明」；不由參訓紀錄直接推論任職、職能或績效。
依已證實的政策管理原件：依政策管理原件歸檔，註記保管位置及存取限制。
各步驟如遇未取得、出具者無法聯絡、內容不一致、影本不完整、授權未知、保存依據未知等情形，各自記錄 UNKNOWN、原因及取得條件。見下節「異常處理」。
查核及結論規則
區分以下狀態，並分別記錄：
文件被提及：文件被參考或提及，但未收到實體或副本。
收到副本：已收到文件影本，但未收到原件。
收到原件：已收到原始文件。
出具者核實：出具者已確認文件真實性。
內容相關：文件內容與指定訓練角色或工作主張具備關聯。
職能已評估：已有職能評估報告或相關結論。
關鍵原則：
不把一種狀態合併成「已證明」。
不由參訓紀錄直接推論任職、職能或績效。
每一主張（曾任職、曾參訓、出勤、結業）各自對應各自的證據，不得互相代替。
查核結果呈現時，SAMPLE/SYNTHETIC 案例決策為「NO CLAIM / NOT VERIFIED」；不得計為已具備證明或能力。
異常處理
下列情形各自記錄 UNKNOWN、原因及允許的下一步，不得猜補：
未取得原件：記錄 UNKNOWN、原因（如：未提出索引、索取失敗、來源機構未回覆）及取得條件（如：需合法授權、需正式信函、需聯絡資訊）。
出具者無法聯絡：記錄 UNKNOWN、原因（聯絡方式過舊、機構已歇業）及允許的下一步（更新聯絡資訊、查詢相關協會）。
內容不一致：記錄 UNKNOWN、不一致處點及允許的下一步（覆核原始來源、補充說明）。
影本不完整：記錄 UNKNOWN、缺失處點及允許的下一步（索取原件、補充缺漏）。
授權未知：記錄 UNKNOWN、需求的授權依據及允許的下一步（取得授權文件）。
保存依據未知：記錄 UNKNOWN、保存期限的法律或政策依據及允許的下一步（查詢組織政策、法律諮詢）。
每種情形皆不得填寫 0、推定事實或完成；必須明列 UNKNOWN 並說明需要何種 genuine source 支撐方能升級。
SAMPLE/SYNTHETIC 流程案例
SAMPLE/SYNTHETIC — 本案例僅示範索引建構與查核流程，所有 REAL 欄位明列 UNKNOWN，不得主張真實人員、雇主、資歷或成就。
案例說明：合成流程案件，原件未提供
本案例展示一個「合成流程案件」，從需求辨識到決策及後續動作的完整流程。所有合成值須有唯一 SYN-0030-* ID 並登錄，UNKNOWN 是真實來源缺席狀態，不登錄成合成真實事件。
完整示例規格
表 7-B：合成事實與流程狀態登錄
Fact ID | 欄位／事實（型別） | 值 | 明示分類 | 示例位置／來源界線
SYN-0030-001 | 案例／索引列識別碼 | SAMPLE/SYNTHETIC：I06-E01 工作經驗受訓證明索引流程案例 | SAMPLE/SYNTHETIC | §7 案例及表 7-A；同一 ID 識別本合成流程案件與其示例索引列，非第三方證明編號。
SYN-0030-002 | 需求對位流程狀態 | SAMPLE/SYNTHETIC：在示例中依官方 I06-E01 checkbox 界定索引範圍，尚未提出個人資歷主張 | SAMPLE/SYNTHETIC 流程狀態 | §7；I06-E01、官方勾選文字與 Blueprint row 029 是正式來源事實，不是合成值。
SYN-0030-003 | 待支持主張（文字） | SAMPLE/SYNTHETIC：訓練講師相關工作經驗之待支持主張，無真實人員或雇主歸屬 | SAMPLE/SYNTHETIC 主張描述 | §7／表 7-A；不得描述成實際任職。REAL 需可追溯雇主原件及合法授權。
SYN-0030-004 | 工作與受訓連結（關聯 ID） | 示例關聯至 SYN-0030-005 的受訓來源欄位；目前沒有真實原件 | SAMPLE/SYNTHETIC 關聯 | §7／表 7-A；REAL 關聯須由同一受權主體的工作與受訓原件分別支持。
SYN-0030-005 | 訓練機構（來源欄位） | UNKNOWN | SAMPLE/SYNTHETIC 案例的未知欄位狀態；真實來源仍 UNKNOWN | 表 7-A；REAL 需訓練提供者原件或可追溯確認。UNKNOWN 非合成機構名稱。
SYN-0030-006 | 訓練課程（來源欄位） | UNKNOWN | SAMPLE/SYNTHETIC 案例的未知欄位狀態；真實來源仍 UNKNOWN | 表 7-A；REAL 需提供者課程紀錄或原始受訓證明。
SYN-0030-007 | 受訓日期／期間（日期欄位） | UNKNOWN | SAMPLE/SYNTHETIC 案例的未知欄位狀態；真實來源仍 UNKNOWN | 表 7-A；REAL 需原件所載日期及必要的來源核驗。
SYN-0030-008 | 工作期間（期間欄位） | UNKNOWN | SAMPLE/SYNTHETIC 案例的未知欄位狀態；真實來源仍 UNKNOWN | 表 7-A；REAL 需雇主出具或可驗證工作期間的原件。
SYN-0030-009 | 發證者（來源欄位） | UNKNOWN | SAMPLE/SYNTHETIC 案例的未知欄位狀態；真實來源仍 UNKNOWN | 表 7-A；REAL 需原件或發證者獨立可追溯確認。
SYN-0030-010 | 證書編號（來源欄位） | UNKNOWN | SAMPLE/SYNTHETIC 案例的未知欄位狀態；真實來源仍 UNKNOWN | 表 7-A；REAL 需真實原件或發證紀錄；不得臆造編號。
SYN-0030-011 | 收件狀態（流程狀態） | NOT_RECEIVED；本示例未實際寄送索取 | SAMPLE/SYNTHETIC 流程狀態 | 表 7-A；REAL 狀態須取自實際送件與收件紀錄。
SYN-0030-012 | 查核狀態（流程狀態） | NOT_PERFORMED；本示例未聯絡第三方或核驗 | SAMPLE/SYNTHETIC 流程狀態 | 表 7-A；REAL 狀態須取自實際核驗紀錄、方法、時間及查核者。
SYN-0030-013 | 決策（流程結論） | NO CLAIM / NOT VERIFIED；不得計為已具備證明或能力 | SAMPLE/SYNTHETIC 流程決策 | 表 7-A；REAL 結論需由授權覆核者根據已核驗原件逐項作成。
SYN-0030-014 | 後續步驟（程序指引） | 取得合法授權及真實第三方原件後，依本文件逐項登錄及查核；目前尚未執行 | SAMPLE/SYNTHETIC 程序指引 | 表 7-A；實際執行時需有授權紀錄、索取紀錄與收件／查核紀錄。
SYN-0030-015 | 角色關聯狀態（關聯判斷） | UNKNOWN／NOT_ASSESSED；實際職務與訓練角色未提供 | SAMPLE/SYNTHETIC 案例的未知欄位狀態；真實來源仍 UNKNOWN | 表 7-A；REAL 需正式職務描述、訓練角色要求及逐項關聯評估。
事實登錄規則
每個 SAMPLE/SYNTHETIC 值至少記錄：唯一 Fact ID（SYN-0030-001 起順序遞增）、欄位／事實、型別、值及明示分類 SYNTHETIC。
僅供示範的說明及在正文、表格、流程圖、摘要中的使用位置。
來源性質；沒有外部來源的程序狀態必須標「合成流程示例，非外部事件」。
日後改為 REAL 所需原件、授權來源、查核方法及當前狀態。
對應角色／需求，以及是否允許形成實質證明主張。
不得只登記日期與數字而漏掉角色、程序狀態、推論、決策或結論。
正文任何地方的合成文字或狀態都須能回溯到唯一 ID。
UNKNOWN 必須維持為未知，不得用 SAMPLE 值填補。
替換登錄說明
下列為本案例各 Fact ID 如需從 SAMPLE/SYNTHETIC 升級為 REAL 所需條件：
表 7-C：逐 ID REAL 替換／處理登錄
Fact ID | 目前示例值／狀態 | 文件區段定位 | REAL 替換／處理所需來源類別
SYN-0030-001 | SAMPLE/SYNTHETIC案例／索引列 ID | §7／表 7-A | 不得轉成 REAL 編號；依實際受控案件登錄來源另編 REAL ID。
SYN-0030-002 | SAMPLE/SYNTHETIC需求對位程序狀態 | §7／表 7-B | 官方 I06-E01 與 checkbox 保持官方來源；真實個人主張須另由核驗原件支持。
SYN-0030-003 | SAMPLE/SYNTHETIC待支持工作經驗主張 | §7／表 7-A | 可追溯雇主出具之工作經驗原件、主體授權及獨立核驗紀錄。
SYN-0030-004 | SAMPLE/SYNTHETIC工作／受訓關聯 | §7／表 7-A | 同一受權主體的工作與受訓原件、來源定位及角色關聯覆核。
SYN-0030-005 | UNKNOWN（來源未提供） | §7／表 7-A | 訓練提供者原件或可追溯的提供者確認。
SYN-0030-006 | UNKNOWN（課程未提供） | §7／表 7-A | 訓練提供者課程／受訓紀錄或原始證明。
SYN-0030-007 | UNKNOWN（日期未提供） | §7／表 7-A | 原始訓練證明或提供者紀錄中的日期／期間。
SYN-0030-008 | UNKNOWN（工作期間未提供） | §7／表 7-A | 雇主出具或可獨立驗證的工作期間原件。
SYN-0030-009 | UNKNOWN（發證者未提供） | §7／表 7-A | 原件所載發證者資訊及獨立可追溯核驗。
SYN-0030-010 | UNKNOWN（證書編號未提供） | §7／表 7-A | 真實證書原件或發證機構紀錄；不得人工編造。
SYN-0030-011 | NOT_RECEIVED（本示例未送件） | §7／表 7-A | 實際索取送件紀錄及收件登錄；新建 REAL 流程紀錄，不沿用示例狀態。
SYN-0030-012 | NOT_PERFORMED（本示例未核驗） | §7／表 7-A | 實際獨立核驗的時間、方法、依據、查核者與結果紀錄。
SYN-0030-013 | NO CLAIM / NOT VERIFIED | §7／表 7-A | 授權覆核者依已核驗第三方原件形成的逐項書面結論。
SYN-0030-014 | 僅為未執行的程序指引 | §7／表 7-A | 實際授權、索取、收件及查核的受控流程紀錄。
SYN-0030-015 | UNKNOWN／NOT_ASSESSED（角色關聯未評估） | §7／表 7-A | 真實職務／訓練角色描述、需求依據及有來源定位的關聯評估。
未提供處填明 UNKNOWN，不得以合成資料填入 REAL 欄位（見 BP-05、BP-06）。要升級為 REAL，須提供可追溯的第三方原件或可驗證的雇主／訓練提供者確認。
REAL 替換登錄
下表說明各欄位如需從 SAMPLE/SYNTHETIC 升級為 REAL 所需的實際資料、原件、授權與核驗條件：
欄位 | 目前狀態 | REAL 替換所需條件 | 來源機構
工作經驗描述 | UNKNOWN | 真實工作經驗說明，來自可追溯的第三方原件（雇主證明、工作合約、考勤紀錄等） | 雇主或提供者
受訓機構 | UNKNOWN | 真實訓練機構名稱，來自可追溯的第三方原件（課程結證、發證者確認等） | 訓練機構
訓練日期 | UNKNOWN | 真實受訓日期，來自可追溯的第三方原件（課程時間表、考勤簿、發證者簽署等） | 訓練機構
工作期間 | UNKNOWN | 真實工作期間，來自可追溯的第三方原件（雇主證明、考勤紀錄等） | 雇主
發證者 | UNKNOWN | 真實發證者姓名/機構，來自可追溯的第三方原件（證書、核驗記錄等） | 發證機構
證書編號 | UNKNOWN | 真實證書編號，來自可追溯的第三方原件（證書影本、發證紀錄等） | 發證機構
未能核驗則保持 UNKNOWN。自述、合成資料、無法核驗的影本、未授權個資或推測均不足以升格 REAL。沒有原件或授權不得作為已證明。
來源與版本
官方 PDF 定位：TTQS 評核指標及常見參考佐證資料表，PDF 第 2 頁／印刷頁碼 2；指標 6「訓練機構的行政管理能力及訓練主管相關職能」；官方勾選文字：□ 工作經驗的相關受訓證明。
crosswalk 對應列：I06-E01│deliverable_count=1│deliverable_ids=0030│document_titles=工作經驗的相關受訓證明_可直接使用成品。
157 格索引 row 029：受訓與工作經驗：真實證明索引及取得規程，不偽造。
候選版本與來源變更方式：本文件為候選版（CANDIDATE），未取得真實原件前維持候選狀態。如需升級為 REAL，須按本文件「REAL 替換登錄」條件補齊所有 UNKNOWN 欄位，並附可追溯的第三方原件或可驗證的雇主／訓練提供者確認。來源變更時，註記官方定位、crosswalk row、索引 row 029 與該候選的來源 SHA 綁定。
觀察時間：2026-11-18T00:00:12.163+08:00
