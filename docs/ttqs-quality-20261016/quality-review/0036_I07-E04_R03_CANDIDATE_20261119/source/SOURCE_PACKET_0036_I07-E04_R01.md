# SOURCE PACKET｜0036 / I07-E04｜R01

## 階段與狀態

- Work ID：TTQS_ONE_0036_I07-E04_SOURCE_BLUEPRINT_R01_20261118
- 階段：READY_SOURCE_PACKET；READY_UNIQUE_BLUEPRINT
- 本階段只完成正式來源定位、crosswalk 對照及專屬 Blueprint；沒有撰寫 DOCX、建立合成事實、派 Writer 或宣稱品質 PASS。
- 輸出性質：CANDIDATE 施工準備材料；不代表協會已執行、核准或正式接受。

## 交付物身分

- doc_id：0036
- requirement_id：I07-E04
- Crosswalk：1 個 deliverable、0 個 split extra；deliverable_ids=0036。
- Crosswalk 標題原文：有課程設計進度表、課程規劃流程圖說明、訓練規_完整工作稿
- 官方證據表使用的完整佐證描述：有課程設計進度表、課程規劃流程圖說明、訓練規劃書等佐證資料。
- Crosswalk 標題末段為截短文字；文件文類依官方證據表的「訓練規劃書」解讀，不將其改成未經來源支持的「訓練規章」。

## 權威來源與 SHA-256

| 用途 | 本機來源 | SHA-256 |
|---|---|---|
| 129→142 交叉對照 | E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0048_SOURCE_PACKET_20261118\source\CROSSWALK_129_TO_142_R01.csv | 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679 |
| 官方 157 checkbox 對應規格 | E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0026_R11_20261117\source\inputs\BLUEPRINT_157_CHECKBOXES_LIVE_R01.md | AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216 |
| 官方 TTQS 證據表 R04 | E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0026_R11_20261117\source\inputs\OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf | 805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709 |
| 官方 PDF 第 2 頁 pypdf 讀回 | E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0031_SOURCE_PACKET_20261118\OFFICIAL_PAGE2_READBACK_PYPDF.txt | 3C295E8861AD7775A78583E9111DF61AC8733A7CF40D771F942363F00572DE9C |
| 官方 PDF 第 2 頁原頁渲染 | E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0031_SOURCE_PACKET_20261118\OFFICIAL_PAGE2_RENDER.png | 35A71CB3D892DD81428CE607CE0C0BC2F43694C9B6F080F38F8A55BAFB96EED4 |

PDF 為 9 頁；官方頁面定位採紙面第 2 頁、PDF page object index 1。pypdf 讀回第 97–101 行含指標 7 的佐證項目，原頁影像確認該列位於「設計（Design）」指標 7「訓練需求相關的職能分析及應用」之最右欄第 4 個 checkbox。pdfplumber 扁平化會交錯鄰欄內容，因此只作輔助讀回，不將其宣稱為逐字連續相符。

## 官方要求與 crosswalk 對照

官方 checkbox 原文（依讀回文字及原頁影像核對）：
「有課程設計進度表、課程規劃流程圖說明、訓練規劃書等佐證資料。」

同列的內涵要求是展現課程設計過程中適當確認客戶或市場訓練需求，據以進行職能落差分析，並展現職能分析及運用的方法與紀錄。I07-E04 是該指標下第 4 個具名佐證，不把同列其他 checkbox 的工作重做。

Crosswalk 同列映射：
- I07-E01 → 0033：需求調查與需求配適。
- I07-E02 → 0034：學員職能盤點／分析與課程適配。
- I07-E03 → 0035：職能分析及運用方法的檢討改進。
- I07-E04 → 0036：課設進度表、流程圖及訓練規劃書；本列 1 件，不拆分。
- I11-E01 → 0049：業主、受訓者及職能需求對應的下游課程計畫。

官方 Blueprint 157 的 row 036 原文：
「課設進度表/流程圖/規劃書：三份對應可用成品」。其共通驗收要求包括特定來源定位、核心正文／示範、決策或結果、與其他文件的事實連結；非第三方原件索取型文件不得用空白欄位交差。

## 來源可得性與限制

- 本次確認 0036 專屬 source-prep 目錄原先不存在；工作樹檔名搜尋未找到 0036 或 I07-E04 的既有 DOCX／專屬來源包。這只表示目前可存取工作樹未提供該檔，不代表外部所有儲存位置均不存在。
- 未取得真實協會年度課程設計排程、已核准流程圖、實際訓練規劃書、真實學員或師資資料、核定紀錄、課程執行結果；一律維持 UNKNOWN。
- 下一階段若建立示範，所有日期、職務角色、課程名稱、目標、課時、分數、計畫、核准節點及結果必須以 SAMPLE／SYNTHETIC 標記並登錄專屬 FACT_ID；不得寫成協會已發生或已核准的事實。
- 本工作只授權可逆 CANDIDATE 文件施工；無真實簽核／核准時不得標成 REAL、正式公告或正式接受。

## 接續決策

下一合法階段：依本 Blueprint 執行 0036 專屬 Writer 工作，交付一份文件內彼此一致的「設計進度表、流程圖說明、完整訓練規劃書」示範；之後以該 exact DOCX SHA 驗收。不要重寫 0033／0034／0035 的正文，也不要把 0049 下游課程計畫混入本件。