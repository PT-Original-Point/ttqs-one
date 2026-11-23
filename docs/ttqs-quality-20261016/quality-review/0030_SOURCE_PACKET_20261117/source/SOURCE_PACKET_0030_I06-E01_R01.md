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