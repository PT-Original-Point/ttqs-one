# 0009｜I01-E06 年度績效目標訂定與分析紀錄｜來源包 R01

## 狀態與範圍

SOURCE_PACKET=CANDIDATE_SOURCE_PREP
OBSERVED_AT_TPE=2026-10-31
這是候選文件施工來源包，不是協會真實績效、正式核定、正式接受或 TTQS 評核結果。文書編號 0009 經 129 具名需求至 142 歷史交付序號交叉表對應官方要求 I01-E06；不得把 0009 誤稱官方方框流水號。現有來源表將 I01-E06 列在指標 1、PDF 第 1 頁，未另提供可用來替代 I01-E06 的 157 序號欄位。

## 官方要求與來源定位

- 官方要求 ID：I01-E06
- 官方佐證文字：單位工作達成年度績效目標的訂定及目標分析等佐證資料。
- 原始 PDF：E:\TTQS\TTQS_ONE_CODEX_RUNTIME\INPUTS\R04\06_OFFICIAL_SOURCES\TTQS查核佐證文件資料表-訓練機構版 (2).pdf
- PDF SHA-256：805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709
- 官方查核表頁：1
- 已有來源對帳狀態：PDF_TEXT_EXACT_PAGE_MATCH（SOURCE_RECONCILIATION）
- 交叉對照：SOURCES\DRIVE_READBACKS\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv；完整檔案 SHA-256 1DDFBB608BCAD25170683DDB42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679；該列為 I01-E06,1,0,0009,年度績效目標訂定與分析紀錄。
- 要求來源核對表：SOURCES\REQUIREMENT_SOURCE_RECONCILIATION.csv；SHA-256 FF6DE9F52A0AFFBA7D5C4C57CAAC868812600305F4807E7B59B6DB5B5CB1A2B9；對應頁面 1、PDF 文字精確比對、交付件 0009。

## 專屬 Blueprint 綁定

- 唯一 Blueprint：CONTROL\BLUEPRINT_CURRENT.jsonl，檔案 SHA-256 406D0495365D0970DCF8113A42842663B8A54372A4E204CC492B7C3F8156EF3E。
- 唯一列：deliverable_id=0009、requirement_id=I01-E06。
- Blueprint 列 SHA-256：4D00595289266D8126E8E890FC9E503037ACC43D296C0A176DB5025EC01BC3F0（逐列 JSON 去除行尾後綁定；與 draft receipt 的 expected_row_sha256 一致）。
- 文類：分析／評估報告｜年度績效目標訂定與分析紀錄。
- 分析公式：差距＝實績－目標；改善率＝(改善後－改善前)／改善前。分母為 0 時不得硬算百分比；缺少證據時不得稱為組織實績。
- 相鄰但不可混件：I01-E05／0008「各類別訓練課程年度成長計畫」；I02-E01／0010「學員訓練成果評核標準與說明」。共用來源只能引用已核實結果，不複製相鄰文件正文。

### Blueprint 必須落實的章節

摘要、用途與決策問題；官方要求及分析範圍；資料來源、樣本與納入排除；指標定義、分母與計算方法；完整示範資料及逐步計算；分群／趨勢／差異結果；圖表解讀及品質限制；發現、原因與證據強度；結論與可執行建議；責任人、期限與追蹤指標；合成資料聲明及真實替換清單；附件索引、覆核與版本。

### Blueprint 必須落實的表格／圖表

1. 資料欄位、定義、分母、來源及限制字典。
2. 合成明細、彙總結果及逐步計算。
3. 分群比較與差距優先排序矩陣。
4. 結論、證據、建議、責任及追蹤指標。
5. 官方要求、分析結果、文件證據位置及覆核追溯表。

### 必須回答的分析問題

- 資料是否足以支持結論？
- 差距屬於需求、設計、執行或追蹤哪一環節？
- 下一期以何種指標驗證改善？
- 哪一章節／表格直接回應 I01-E06？
- 母數、排除規則、計算口徑及四捨五入方式為何？
- 建議決策及其適用限制為何？
- 每一筆合成事實對應哪個替換登錄鍵？

## SAMPLE／REAL 邊界與禁止事項

- 缺少經授權、可追溯的協會原始年度目標、工作清冊及結果資料時，只能製作完整的 SAMPLE/SYNTHETIC worked example。
- 合成日期、角色、分子、分母、比例、門檻、原因、措施及追蹤結果須有替換清冊鍵；不得寫成原始點協會的實績、核准、會議、簽章或第三方證明。
- REAL 替換區可保留供合法使用，但不得以空白模板代替 SAMPLE 完整示範；資料不足的真實欄位須標 UNKNOWN/HOLD。
- 不得沿用歷史 0009 DOCX 正文作為新稿模板。舊文件只可用於來源發現及缺陷定位。

## 現有稿件與未完成階段

- 現有 Markdown 稿：worker\luna_subagent_draft_R01.md，檔案 SHA-256 A9EECDFD1B469E990203830729F14015F262546B9B37072F404DBBDF302059BE，31,766 bytes。
- 原始收據 receipt_R01.json 將狀態標為 TEXT_DRAFT_ONLY_NOT_QA；未有 DOCX、技術／版面 QA、獨立語意 PASS 或正式接受。
- 目前沒有在本工作資料夾內找到與該 Markdown 綁定的新 0009 DOCX。
- 下一階段須逐項檢查草稿是否實際包含 Blueprint 指定的分群／趨勢分析、差距排序矩陣、圖表解讀與品質限制、官方要求—結果—證據位置—覆核表；不得只憑章節名稱或關鍵字判定通過。數學重算須使用表內原始分子／分母；之後才可建立 Word 候選並驗收同一 SHA。