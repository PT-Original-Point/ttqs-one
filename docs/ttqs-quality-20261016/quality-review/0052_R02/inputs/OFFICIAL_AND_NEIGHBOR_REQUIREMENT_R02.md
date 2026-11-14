# 官方要求與相鄰項目核對（R02）

## 文件身分
- DOCX 0052 是交付文件編號；正式 Unique Blueprint requirement_id 為 I11-E04；官方方框流水號為 054。
- 官方查核佐證表第 4 頁要求：「規劃課程依學員及結訓學員意見訂定訓練課程，且流程有完整紀錄。」
- 現行 157 項清單於 Indicator 11 下的 054 摘要為：「依結訓學員回饋訂課：意見統計、取捨與修正閉環」；這是流水號，不是 DOCX 編號。
- 0051 = I11-E03 / 053，處理課程產出討論、確認與核定紀錄。
- 0053 = I12-E01 / 056，處理訓練課程切合性檢討與調整。0052 不取代這兩項。

## 來源
- 官方方框頁面影像見 official_evidence_table_page4.png。
- 官方文字、原始頁面 SHA、Blueprint 與來源範圍的歷史詳細記錄見 SOURCE_MAP_R01_HISTORICAL.md。
- 文件專屬 Unique Blueprint 原始列見 UNIQUE_BLUEPRINT_0052.jsonl。
- 最新逐指標文類手冊與 157 方框清單見 02_GENRE_WRITING_MANUAL_CURRENT.md 和 03_157_CHECKBOX_BLUEPRINTS_CURRENT.md。
- 以下為同一合成案例鏈：SYN-0033-PLAN-01。所有跨文件數據仍為 SAMPLE/SYNTHETIC；不得推定真實辦訓或正式核定。

## Historical source map retained verbatim for source provenance

# DOCX 0052 R01｜來源與範圍圖

## 身分與官方要求
- doc_id: 0052; Unique Blueprint requirement_id: I11-E04; 官方 checkbox: 054; 官方資料表頁: 4。
- 官方原文: 規劃課程依學員及結訓學員意見訂定訓練課程，且流程有完整紀錄。
- 文類: strategy_plan（課程意見回流與課程修訂策略／計畫），不是 0051 的產出審查紀錄，也不是 0053 的課程切合性檢討。
- official source PDF SHA-256: 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709。
- 官方 p.4 方框影像 SHA-256: 0e00b46586ad0ee181046d4a13d0023654bb07537f7eebc3429dad3bfa29d35f。
- BLUEPRINT_CURRENT.jsonl 全檔 SHA-256: 406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e。
- 本件 Unique Blueprint 原始列副本 SHA-256: 3ffbfd8e62762d0de54022e96c49397b7b547a724ebf6aa2c765a1ac994d7445。
- 工作分支於建置前讀回 HEAD: bdfa5a675ca77ff460530b96971b26ff44c455c4。

## 唯一合成案例與跨文件事實界線
- Case ID: SYN-0033-PLAN-01；課程名稱: 志工服務紀錄、交接與工作界線實務。所有 0052 問卷列、追蹤、日期、分母、評分、取捨和版本變更均為 SYNTHETIC。
- 0033 R03 I07-E01 / checkbox 033 DOCX SHA: fe5f3cfd84c761da86435a71e0fd899daa725be78628c4d2d3f2324c1fdb5f4f。僅作同案例的合成需求上游，不在本件複製其問卷或將其結果當 REAL。
- 0049 R01 I11-E01 / checkbox 051 DOCX SHA: e8212788b1f7b201ca4af4f4c5fb83ab131627dbfa815987f7cf6344edfda727。來源只支持合成課程計畫、四單元與 12 人規劃假設，不證明實際排課。
- 0050 R01 I11-E02 / checkbox 052 DOCX SHA: d0d37c2c69b161a2cdd37ee3097306722c4a65a1afd844ae92e1dff58b43381a。來源只支持同案示範單元目標與評量，不證明課程實施或學員表現。
- 0051 R01 I11-E03 / checkbox 053 DOCX SHA: 6f575ebb41c6c26b4d6b36262fb4d9a5abdae53cbdc1ff4e75acda46d5f0b495。該件處理課程產出討論／確認；本件不代替會議或核准原件。
- 0053 I12-E01 是另一官方要求；本件不處理課程切合性檢討。

## 資料來源與方法
- 合成案例回覆數：學員 8 列，假設邀請 12；結訓追蹤 5 列，假設邀請 12。每個原始回答和衍生頻數、平均、比例、選項分數均在 SYNTHETIC_REPLACEMENT_REGISTER_R01.csv 以唯一 fact_id 登錄。清冊共 186 筆資料列，另有 1 列 CSV 欄名列。
- 學員題目 1–7 為五點同意量尺；平均=有效分數合計÷該題有效 n。缺答不補 0。
- 結訓追蹤 G3–G5 同量尺；三項支持需求分母為有效回答者、選項可重疊；「目前不需要」與支持項互斥。自陳不是客觀行為稽核。
- 本例內部觸發線 mean<3.5/5 與權重 30/25/20/15/10 均為 SAMPLE POLICY EXAMPLE，不是官方門檻或協會政策。
- 加權評分公式: sum(weight_percent × score_1_to_5)/100。三案 A/B/C 的原始權重、評分、乘積與合計均在正文及替換簿可重算。

## 未取得／不得聲稱
- 未取得本要求專屬協會真實學員意見或結訓追蹤原件；未證明有真實課程、學員、受邀分母、課後回覆、服務使用或辦訓成果。
- 未取得協會核定權限、實際責任人、個資保存政策、正式課程修訂核准或正式會議紀錄。這些狀態維持 UNKNOWN。
- 本件不得冒稱 REAL、正式接受或已核定。人名、簽章、核准、第三方原件及學員個資均未偽造。

## Build output
- Candidate: candidate/0052_R01.docx; SHA-256 406d1ef2c6e9b6266ea1adaeadedc5dfac77964fe76f73c2471168220ee6d455。
- Synthetic replacement register: evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv; SHA-256 71e5f87f8d5a829601077fb1b98f5715c61159fddb5e5afb6420353d03779474; 186 筆資料列，另有 1 列 CSV 欄名列。
- Independent exact-SHA reviewer and final visual receipts are stored separately under review/ and evidence/qa/ after completion.
