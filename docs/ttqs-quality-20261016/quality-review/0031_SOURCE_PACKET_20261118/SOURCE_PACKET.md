# SOURCE_PACKET — 0031 / I06-E02

## 階段狀態

- READY_SOURCE_PACKET
- READY_UNIQUE_BLUEPRINT
- 本封包只完成來源與唯一 Blueprint。沒有撰寫或產生 DOCX。

## 任務綁定

- Windows checkout：E:\tqrepo
- Git HEAD：03348e7811dfe57a5b6e46efed1598b929db563d
- doc_id：0031
- requirement_id：I06-E02
- crosswalk 標題：專業訓練人員職能評估方法等證明_可直接使用成品
- 官方 Blueprint 157：I06 區段 row 030
- 封包產生時間（UTC）：2026-11-17T16:48:07.710Z

Crosswalk 對應列只有 1 份 deliverable、沒有 split extra；deliverable_ids 為 0031，標題與上述完全相同。

## 指定正式來源與 SHA-256

| 來源 | 路徑 | SHA-256 |
|---|---|---|
| Crosswalk | E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0026_R11_20261117\source\inputs\CROSSWALK_129_TO_142_R01.csv | 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679 |
| Blueprint 157 checkbox list | E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0026_R11_20261117\source\inputs\BLUEPRINT_157_CHECKBOXES_LIVE_R01.md | AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216 |
| Official TTQS evidence table R04 | E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0026_R11_20261117\source\inputs\OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf | 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709 |

封包包括官方 PDF 第 2 頁的 pypdf 與 pdfplumber 全頁文字讀回、頁面影像及定位核對。原始 PDF 未修改。

## Official checkbox 原文與定位

- Official PDF 紙面頁碼 2；PDF 第 2 頁（零起算 page object index 1），全檔共 9 頁。
- 表格指標 6「訓練機構的行政管理能力及訓練主管相關職能」；最右欄「常見參考佐證資料（並註明資料來源及頁碼）」的第 2 個核取項。
- 核取項原文：**專業訓練人員職能評估方法等證明。**
- pypdf 文字讀回移除版面空白後可還原完整 checkbox。pdfplumber 的表格文字流將相鄰欄位插入換行，封包保留其原始讀回，不把扁平字串誤報為完整連續吻合；原頁影像核對確認位置及原文。

## Blueprint row 030 原文

030｜**訓練人員職能評估：量規、角色分數、落差、改善、複評**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。

row 030 是此 deliverable 的獨特範圍：量規、角色分數、落差、改善、複評。共通要求包括特定來源定位、核心正文／示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外，不得以空白欄位交差。

## 範圍與負向近鄰

- row 029：029｜**受訓與工作經驗：真實證明索引及取得規程，不偽造**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。
  - 0031 不是訓練／工作經驗真實證明索引或第三方原件取得規程；不得以職歷、證照或其他第三方原件冒充本文件。
- row 031：031｜**辦訓行政職能：小型協會分工、替補、權限、作業案例**。 必須包含：特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結；除第三方原件索取型文件外不得用空白欄位交差。
  - 0031 不是小型協會辦訓行政職能、分工、替補、權限或行政作業案例文件。
- row 032：032｜**其他：** 未有獨特補充證據前不生成文件；狀態 BLOCKED_UNTIL_UNIQUE_OTHER_NAMED。
  - 0031 已明確映射 I06-E02；不增造 Other 補充文件。
- Official PDF 第 2 頁指標 7「訓練需求相關的職能分析及應用」談客戶／市場／學員需求確認與課程設計使用的職能分析、落差方法及紀錄；這與訓練人員自身的職能評分、改善和複評不同，不把學員需求分析當作 0031 主體。
- Official PDF 指標 6 同列的工作經驗受訓證明、訓練機構執行訓練業務職能說明及「其他」是相鄰 checkbox，不替代本次指定的第 2 個項目。

## 未來成品不可缺的功能機制

1. **量規：**逐項能力指標、可觀察行為描述、評分尺度與評分規則。來源沒有規定官方分數尺度、權重或門檻；若採用數值方案，須說明為本地方法，並用 SAMPLE/SYNTHETIC 範例示範。
2. **角色分數：**分開顯示職務／角色、職能指標、評分者角色、目標及實得分數；讀者能看出各角色分數如何產生與比較。
3. **落差：**明列目標與實得分數的比較規則、計算方法及門檻來源；演算與結果一致，超標情形也有明確處理方式。
4. **改善：**每個需改善落差連到具體行動、責任角色、期限、支持、可查證完成證據及判定標準。
5. **複評：**沿用或說明可比較的量規，記錄複評日期、分數／證據、前後差異及結案或續行改善判定。
6. **完整示例：**核心正文含一個可照做的 SAMPLE/SYNTHETIC 閉環，呈現可區分的角色分數及評分→落差→改善→複評→決策；不可用空白表單或標題代替。
7. **定位和連結：**列出特定官方來源定位；其他文件的事實連結須有識別資訊及定位，不能只寫泛稱。
8. **Synthetic register：**虛構人員代碼、角色、日期、分數、門檻、落差、改善、結果及決策逐項登錄並註明假設依據；正文與 register 對應一致。

## SAMPLE/SYNTHETIC 與 REAL / UNKNOWN 邊界

- 範例人員代碼、角色配置、評分者、分數、門檻、日期、改善結果、複評及決策須標示 SAMPLE/SYNTHETIC，不得寫成協會已發生的事實。
- 真實人員名冊、實際任職角色／指派、真實評分及原始評估紀錄、誰有權評分／核定／授權、真實改善與複評結果，目前均為 UNKNOWN，除非另有可核驗來源。
- 真實授權、簽核、認證、證照及第三方證明不得從示範推論或代造；缺證時維持 UNKNOWN。
- REAL 區域須標示可核驗來源與定位；不得把 SAMPLE 轉述成 REAL。

## 可驗收條件

- doc_id、requirement_id、crosswalk 標題、row 030 及 official PDF p.2 定位完全一致。
- title-blind reviewer 能識別為訓練人員職能評估方法，且能拒絕 row 029、031、032 和 PDF 指標 7 的負向近鄰。
- 量規、角色分數、落差、改善、複評形成可操作且可重算的流程，含決策／結果及完整示例。
- 官方來源及跨文件事實連結均有識別資料與可追查定位。
- SAMPLE/SYNTHETIC 數值邏輯一致並逐項有 register；REAL 人員、分數、授權未知處保持 UNKNOWN。
- 無空白表單／待填欄位冒充成品，無偽造第三方原件或未證實的協會決策。
- 本封包不代表 DOCX 已建置、審查或接受。

## Writer 占用檢查（封包開始前）

- 0031 / I06-E02 命令列程序命中：0。
- 0031 輸出 DOCX 檔名命中：0。
- 0031 writer／lock／lease 檔名命中：0。
- 輸出目錄開始前不存在；封包建置使用專屬獨占 lock，核驗完成後移除。
- 本次工作僅建立本目錄中的專屬來源與 Blueprint 工件。

## 後續接續方式

後續 Writer 可直接使用本 SOURCE_PACKET、UNIQUE_BLUEPRINT 及官方 p.2 讀回；引用來源前比對本封包的 SHA。來源 SHA 不同時先重新核對。後續只處理 0031 專屬輸出；共享 register、queue、CURRENT、dashboard 與其他 deliverable 不在本封包寫入範圍。
