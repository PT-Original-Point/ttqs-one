# SOURCE PACKET｜0128 / I19-E17｜R01｜2026-10-24

## 工作身分

- 專案：TTQS_ONE。
- 文件編號：0128。
- 官方需求識別碼：I19-E17。
- 文件名稱：個人訓後績效改善個案分析表。
- 正式來源定位：訓練機構版《TTQS查核佐證文件資料表》第 8 頁。
- 官方原文：**「相關證據顯示個人訓練後之績效改善成果。」**
- 需求來源：官方 PDF 頁 8；PDF SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709；本機重抽第 8 頁文字 SHA-256 57c6b33d70b665bd41b8d58ff58f5c0d78f9c2c751ccd9c6dd1b740b2fbf374e。
- 權威對照：本機 REQUIREMENT_SOURCE_RECONCILIATION.csv (SHA-256 ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9) 將 I19-E17 對應唯一 doc_id 0128，且記載第 8 頁文字精確匹配；歷史 129→142 crosswalk (SHA-256 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679) 同樣映射 I19-E17 → 0128。
- 157 方框施工方向：候選規格 03_157_CHECKBOX_BLUEPRINTS.md 的 I19-L3 第 141 列描述「個人訓練績效：前後工作成果」。這是該文件中的 summary row 序號，不是 doc_id 0128，也沒有在本 packet 中主張它等於官方識別碼 I19-E17；它只作為正文專屬方向的佐證。
- 正文配方：候選 02_GENRE_WRITING_MANUAL.md 指標 19 實例要求樣例能力差距→課程目標→實作評量→30/60/90 日工作運用→主管觀察→前後工作數據與不確定因素；不得將學習、行為、組織成果混成滿意度表。
- 任務邊界：本工作是可逆 CANDIDATE。候選/合成案例不代表原始點協會已辦訓、已有該員工/志工、完成主管觀察、核定指標或取得 REAL 成效。

## 正式來源與政策 SHA

- Human Mission 01_HUMAN_MISSION_AND_ACCEPTANCE.md blob 538bedb9d87e8465f43151933b4a5c1bfa4bbc4e：REAL 未證實即 UNKNOWN；樣例清楚標示；不可捏造人物、課程、績效、簽核或第三方原件。
- 寫作手冊 02_GENRE_WRITING_MANUAL.md blob 4ff863d9f534b6359fc1c7c1685bd8cce02da886：指標 19 的專屬工作績效鏈與 30/60/90 日追蹤示例。
- 157 方框方向 03_157_CHECKBOX_BLUEPRINTS.md blob 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63：I19-L3 row 141；只作內容方向，不用序號替代文件編號/需求碼。
- R11 權限覆寫 AGENTS.md blob 2e8d4eddd68c650f38db8cb48d421b838e693ecb：候選工作可直接續作；失敗只停相應車道；stage 完成不必等兩小時；來源、Blueprint、writer owner、精確 SHA 與語意/版面驗收仍須保留。
- R11 schedule/continuation docs at branch head 45acf7917e9b7d8cf0d7912d416dd552f0dc53b3：04 blob 65e7fd5a406877e875174402a0d3ddc68b6111a1，05 blob dbdb2e567e8e5c2b7eb0632f060a45a7ae371a49，06 blob b566c5c71d1a88e012eca2eeac90c8a3e4ecc06c。

## 歷史文件狀態（不是現役合格候選）

本機 2026-10-05 audit matrix SHA-256 d206e7fe32173f65a0e5e19ae8085b414fc57564e687471e83bebd691b1f9e8c 曾將舊 0128 標為 VALID_DRAFT_WAITING_ORIGINAL / NO_CURRENT_ORIGINAL_OR_OUTCOME_FOUND；記錄 1,145 字元、12 段、7表、2頁、最小字 7.5pt、80.4% 字元小於 9pt，並列 FONT_LT_8; FONT_LT_9_MATERIAL; GOVERNANCE_CLUTTER / FAIL_REPAIR。這是 10/05 歷史快照，不證明目前無 REAL 來源，也不證明舊檔已修復。
- 10/05 快照另有多個 0128 舊位元組，SHA 包含 f71f8349a6ce3003887c9cad2d9d01ed5b0384ff0087f9d52ff5afb6fe022597、266dcb738b0ccec553dc4bf950a226d52981b720390a1fe0e2966d52c9ef0359、a842739094de149d5bb8c15788a4194ea7edc8e55c55b419870717f764ff3be1。它們是歷史版本，不作本次正文模板或 QA PASS。
- 本次來源預備開始前，本機 WORK/QUALITY_REBUILD_20261016 未有 0128 專屬 R01 work folder，GitHub branch 亦未有本次 SOURCE_PREP_RECEIPT；歷史快照仍保留。此為工作目錄/branch 範圍檢查，不是對所有個人來源資料的窮盡宣告。

## 專屬樣例輸入

本目錄 SAMPLE_INDIVIDUAL_PERFORMANCE_PANEL_R01.csv 含 6 個虛構、去識別的樣例案例，均以相同工作情境示範報名資料一次核對正確率；不宣稱協會存在該工作、課程或六位人員。
- 每案前後各 20 筆 SAMPLE 工作任務；六案分別為 +20、+10、-5、+5、+10、0 個百分點；不得刪除下降或無變化個案。
- 加權總率 93/120 = 77.50% → 101/120 = 84.17%，+6.67 個百分點。個案比例不得簡單平均替代加權重算。
- SAMPLE 實作檢核總分 33/60=55.00% → 48/60=80.00%，此為技能展示，不是實際工作績效，也不得替代 KPI。
- 課程日期、任務量、工作職責、訓後期間、觀察紀錄、來源定位及混雜因素全為 SAMPLE 設計假設，不含 REAL 原件。

## Writer 必須產出的正文

1. 文件用途與官方 I19-E17/0128 對照，30 秒內說清如何完成一個個人訓後績效案例。
2. 唯一主案例：課務報名資料核對的虛構情境，個人匿名樣例 S-EMP-01…06；清楚說非原始點協會實況。
3. P-D-Do-R-O 證據鏈：需求/能力缺口→訓練目標→課程與出席證據欄位→實作學習評量→30/60/90 日工作使用→個人職務 KPI→證據定位→結論/改進。空缺 REAL 欄位標 UNKNOWN，不得造填。
4. 完整列出六個配對樣例、分子/分母、前後率、百分點差、技能展示分數、任務窗口及品質限制；重算加權整體，保留正向、持平及負向案例。
5. 可直接使用的個人案例表、KPI 定義卡、前後資料查核單、主管觀察表、30/60/90 日追蹤表、資料缺漏/樣本不足/任務難度改變處理規則與結果判定樹。
6. 評估結果只使用「改善/無變化/下降/證據不足」描述觀測，不推論訓練為唯一原因；分析工作量、案件難度、工具改版、人力安排、季節變化與其他課程。
7. 0126/I19-E14 薪資或升遷、0127/I19-E16 市場與顧客價值僅作負鄰件界線，不重用它們的數據/正文。
8. 明示 SAMPLE/SYNTHETIC ONLY、REAL 替換清冊、資料保密與最小必要揭露、HOLD/REJECT 條件。
9. 措辭平實、臺灣繁體中文；不得假稱協會核准/課程已辦/主管已簽/REAL 成效已發生。

## 真實資料限制

目前只持有上述歷史稽核列與歷史檔案 SHA；沒有本次新查到的人員、課程、KPI 原始紀錄、雇主/主管證明、核准或簽名。這只表示本施工包尚無可引用 REAL 證據，並不表示協會實際上沒有。
