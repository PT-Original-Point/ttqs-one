# TTQS ONE independent semantic review — 0142 / I19-E32 / R08
Review mode: read-only semantic review. Do not call tools, open files, modify the DOCX, or claim visual inspection. All review material is embedded below.
Candidate revision: R08-TR01; exact DOCX SHA-256: 7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78; bytes: 53207.
Candidate extracted-body SHA-256: 350713d9b10e258edc819eb294a2b1456cf129537b98a58b8b3547f26f165e4d. The reviewer receives the extracted body below; no claim is made that the reviewer opened the DOCX binary.
Requested model: OpenCode v2 CLI opencode/glm-5.3-flash-free; no fallback authorized. The reviewer must report only its own session metadata if available. Do not call this Antigravity/Gemini.
Existing status: prior Antigravity response was PARTIAL because the reviewer was not given the lineage annex/JSON or the 19-row CSV; its reported PASS is not accepted. Prior OpenCode DeepSeek attempt was rejected HTTP 429 before inference and returned no review; do not reuse it. Current candidate has deterministic technical PASS and separate Word-native visual PASS for 14/14 pages; your semantic review must not claim to inspect those pages.
Task: independently assess only what the supplied sources and exact extracted body support. Cover official requirement mapping, document genre/usefulness, all required 3-year source and classification mechanics, the SAMPLE calculation fixture, cross-table math, rejection/HOLD controls, SAMPLE/REAL truth boundary, replacement-register coverage, candidate lineage claims and the R01 binary/build-date UNKNOWN limitation, and negative-neighbor separation from 0139/I19-E29, 0140/I19-E30, 0141/I19-E31. Use precise paragraph/table/CSV/lineage locators and brief evidence excerpts. Flag every material unsupported claim. If any key evidence is insufficient, return PARTIAL; do not infer REAL financial performance, approvals, signatures, or official score.
Expected arithmetic checks from the Blueprint are test vectors, not a required conclusion: 2023 to 2024 +10.00%; 2024 to 2025 +10.00%; first-to-third-year revenue +21.00%; total income 1,480,000 / 1,580,000 / 1,752,000 with first-to-third-year +18.38%. Verify against the body and register, and state that this proves only synthetic arithmetic.
Return exactly one compact JSON object with keys: project_id, doc_id, requirement_id, candidate_sha256, candidate_body_sha256, verdict (PASS/PARTIAL/FAIL), scope, criteria (official_mapping, genre_and_usability, source_and_classification, three_year_math, cross_table_consistency, hold_reject_controls, sample_real_boundary, replacement_register, lineage_truth, negative_neighbors), findings (array of locator/evidence_excerpt/defect/required_change), limitations, formal_acceptance (NOT_GRANTED), real_evidence (UNKNOWN/HOLD), official_score (NOT_ASSIGNED). A PASS requires all semantic criteria supported on the supplied evidence; do not claim the candidate's visual or formal acceptance.


===== BEGIN Official requirement page 9 excerpt | SHA256=0733c1e3a7fa7b88b79846aabf8667391e032165e78cf9bfc06b7363e71ffe11 | BYTES=2221 =====
Source: TTQS查核佐證文件資料表-訓練機構版 (2).pdf, physical page 9 of 9.
This is extracted text for locator support; consult the cited PDF page for the visual source.

 
9 
項目 評核指標項目 
內涵說明（以下為
例，但不以此為
限） 
常見參考佐證資料 
（並註明資料來源及頁碼） 
學或研發成果社會面。 
 提出報章雜誌採訪或電子媒體訪
問之正面消息（其他） 。 
 個人績效提 升（薪資提 升或獎勵
升遷之紀錄） 。 
 證照通過率高及就業率大幅提
升。 
 運用資訊系統普及率。 
 顧客滿意度提升。 
 組織近三年營業額持續成長。 
 其他： 
 
※計分標準（以是否有無紀錄或書面文字評定） 
1分：具本項目基礎認知。 
2分：對本項目僅具認知且部分執行，但無明確紀錄或文件證明。 
3分：有執行本項目及作業流程，但無完整文書紀錄及手冊。 
4分：有執行本項目，且有一致性的作業流程、完整過程紀錄與文書手冊；即具有「說、
做、寫」及「流程上下連結」的一致性。 
5分：有執行本項目及完整文書手冊與紀錄，分析相關資料並持續改善達到標竿水準。 
備註： 
1.計分單位：最小單位為0.5分，以整數1-5或加上0.5為評分標準。除成果（Outcome）之評
核指標項目，17、18及19項未執行為0分，惟1分後始具0.5分之調整，其他則依據標尺分
數評分。 
2.計分級距：評核委員應參酌各指標內涵，依據前揭計分標準級距評分，經評定級距後，
再視申請單位實際評核情形、該級距之表現、與下一級距之程度差距，經專業判斷形成
共識後，酌予以0.5分為調整範圍。 
3.評核公開事項：現場評核結束後給予單位整體回饋及分享，收到評核結果公文後，即可
上網查詢各項指標建議改善事項。 
3-1.回饋及分享：現場請評核委員就評核綜合意見給予單位回饋及分享。 
3-2.各項指標建議改善事項：委員就各項評核指標項目，依據申請單位現有制度、資料或
文件手冊等說明，給予具體改善建議事項。 
 
 
===== END Official requirement page 9 excerpt =====


===== BEGIN Official requirement row I19-E32 | SHA256=b6abdafe457e7aa9353a963bb8606bdecf21e92d289878cf80bfc1885d5c4033 | BYTES=1194 =====
{
  "project_id": "TTQS_ONE",
  "doc_id": "0142",
  "requirement_id": "I19-E32",
  "157_index": 156,
  "printed_checkbox_serial": "UNKNOWN",
  "official_text": "組織近三年營業額持續成長。",
  "official_source": {
    "file": "TTQS查核佐證文件資料表-訓練機構版 (2).pdf",
    "physical_page": 9,
    "total_pages": 9,
    "sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
    "excerpt_sha256": "0733c1e3a7fa7b88b79846aabf8667391e032165e78cf9bfc06b7363e71ffe11"
  },
  "blueprint_source": {
    "repo": "PT-Original-Point/ttqs-one",
    "branch": "work/ttqs-one-document-quality-contract-20261016",
    "blob_sha": "8c2bbe7ca9dcbb03088a48934b9e57e7147ede63",
    "157_index_excerpt_sha256": "9cc71e28910043fe20017702ce81f4efc0fbda3af821dfedffb17549f1573734"
  },
  "crosswalk_row": {
    "requirement_id": "I19-E32",
    "deliverable_count": "1",
    "split_extra_count": "0",
    "deliverable_ids": "0142",
    "document_titles": "組織近三年營業額與收入趨勢核對報告"
  },
  "candidate_status": "SAMPLE_CANDIDATE_ONLY",
  "real_evidence": "UNKNOWN_HOLD",
  "formal_acceptance": "NOT_GRANTED"
}

===== END Official requirement row I19-E32 =====


===== BEGIN Source packet | SHA256=e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49 | BYTES=3748 =====
# 0142｜I19-E32 來源包 R01

## 範圍與狀態
- 專案 TTQS ONE；文件 0142；官方要求 I19-E32；157 索引 156；印刷 checkbox serial UNKNOWN。
- 官方原文：「組織近三年營業額持續成長。」交付 crosswalk 對應一份文件，名稱「組織近三年營業額與收入趨勢核對報告」；標題是交付映射，不是新增官方要求。
- 目前只有舊 SAMPLE 候選，尚待新來源包下的數學、版面與獨立語意驗收。正式接受 NOT_GRANTED；官方分數 NOT_ASSIGNED。

## 正式來源與定位
1. TTQS 查核佐證文件資料表－訓練機構版，實體 PDF 第9頁/共9頁；原 PDF SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709。
2. PR #92 現行分支的 03_157_CHECKBOX_BLUEPRINTS.md Git blob 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63，索引156：三年營業額增長須由真實財報合法核實，含特定來源定位、核心正文/示範、決策/結果及跨文件連結。
3. Windows 交付 crosswalk TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv SHA-256 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679；I19-E32 列一份交付、0142、上述報告文名。
4. 歷史 selection_rows.json SHA-256 fe95f207a04265f9ff0cb0768479b8567fb7f5f2ffdce180760d47b00059a330，只作候選風險線索：舊樣例數學正確，但沒有協會財報，非營利組織科目適用性未確認，不能作實績；此清單不是正式來源或接受證據。
5. 官方第9頁文字摘錄 SHA-256 0733c1e3a7fa7b88b79846aabf8667391e032165e78cf9bfc06b7363e71ffe11；157鄰列摘錄 SHA-256 9cc71e28910043fe20017702ce81f4efc0fbda3af821dfedffb17549f1573734。

## 既有候選讀回
- CURRENT 與 WORK/CANDIDATES 兩份 0142 DOCX 完全同 SHA-256 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6，44,970 bytes，最後變動 2026-10-04；版本1.0，自述示範/未生效。
- 文件內2023–2025數字明示為 SAMPLE/SYNTHETIC，財報、收入明細/總帳原件及真實附件未提供，實際趨勢標未判定。保留此 SHA，先只讀驗算與 Word 視覺檢查，不因來源包更新重建 DOCX。
- 未找到 0142 專屬新版 quality-review 包。其他位置是否存在經授權的真實財務原件未全域盤點，REAL=UNKNOWN/HOLD。
- 不得以 0141 顧客滿意度、0140 系統採用率或 0139 考照/就業率替代本要求。

## 真實資料界線
判斷依據須為三個連續完整會計年度的正式財報與可調回收入明細/總帳，記錄年度、版本、頁/科目列、幣別/單位、會計基礎、核准/簽證狀態及受控保存位置。非營利組織可能沒有一般企業同義的「營業額」科目；財務權責者及適當覆核者須核實科目映射與基礎。未確認前，不把服務收入、捐款、補助、會費、利息或代收款自行合併。不得公開未授權財報、帳戶資料或個資。
合成數據只測試算式與表間勾稽，不能成為協會實績。未取得真實原件時 REAL=UNKNOWN/HOLD、官方分數 NOT_ASSIGNED、正式接受 NOT_GRANTED。

## SAMPLE 算例與下一階段
既有 Word 表列營業額 1,200,000、1,320,000、1,452,000；其他收入 280,000、260,000、300,000；總收入 1,480,000、1,580,000、1,752,000。這些是示範值，不是本會數字。
接續階段：以 exact SHA 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6 重算表間總額及所有分母/期間；用 Word read-only 原生渲染並檢查全頁；再以相同候選 SHA 做獨立語意驗收，檢查財報定位、收入分類、年度連續性、SAMPLE/REAL、近鄰排除。僅發現明確內容/版面缺陷才另存新 SHA 修復。真實財務原件未提供時不得判定達成。

===== END Source packet =====


===== BEGIN Unique Blueprint | SHA256=4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b | BYTES=4447 =====
# 0142｜I19-E32 專屬 Blueprint R01
文件編號 0142 · Requirement I19-E32 · 157索引156 · 印刷 checkbox serial UNKNOWN

## 唯一佐證目的
以可調回、同期間、同幣別/單位及同分類口徑的三個連續完整財務年度原件，核對組織營業額/營業收入是否逐年持續成長。這是財務趨勢核對報告，不能以空白財報欄位或填表說明替代。

## 近鄰要求排除
- 0139 / I19-E29 / 索引153：考照/就業率與分母。
- 0140 / I19-E30 / 索引154：訓練資訊系統使用定義、期間及數據。
- 0141 / I19-E31 / 索引155：顧客滿意度多期同量尺統計。
- 0142 / I19-E32 / 索引156：三年營業額成長與真實財報核實。不得借用近鄰資料、受訪者、期間、結論或分數。

## 正文結構
1. 文件控制與狀態：doc_id、requirement、索引、版本及生效狀態；REAL證據、SAMPLE示範、正式接受、官方評分分開。
2. 核對目的、期間及責任分工：三個連續完整結帳年度；以職務類別描述整理、保管、覆核角色，不填造人名或簽核。
3. 來源調回定位：財報、簽證/查核報告、收入明細/總帳、科目表的年度、版本、文件名稱、頁碼/科目列、受控原件位置、核准狀態及覆核日期。
4. 分類及比較基礎：分列營業/服務收入、其他收入、代收款及調整；記錄幣別、單位、期間、權責/現金基礎、重分類、退款/折讓和沖銷。非營利組織的「營業額」科目必須由財務權責者確認。
5. 三年度逐年勾稽：年度財報與總帳/明細金額、差異、調整理由及證據定位；差額未解或來源不一致即 HOLD。
6. SAMPLE完整算例：營業額1,200,000→1,320,000→1,452,000，其他收入另列；列出逐年及首末累計算式、分子、分母、單位與四捨五入。全頁標示SAMPLE/SYNTHETIC。
7. 判讀與決策：只有來源可核實、期間可比、分類一致、逐年勾稽完成且相鄰年度營業額均增加，才可判示例的「逐年上升」。總收入不得掩蓋營業額下降或分類不適用。
8. 限制/異常：科目重分類、短年度、缺財報、帳表不合、基準年≤0、重大一次性收入、退款、捐款/補助混入、未簽核等，登錄影響及停止條件；不可比時百分比=N/A。
9. 真實替換與追蹤：原件需求清單、授權/保管、逐列替換登錄、覆核角色/日期、差異更正。缺原件時 REAL=UNKNOWN/HOLD，分數 NOT_ASSIGNED，接受 NOT_GRANTED。
10. 版本及交叉參照：跨文件事實須附 source_id/fact_id；沒有共同真實來源不得推定數字相同。

## 必要表格與欄位
- 來源登錄：年度、來源/版本、頁碼或科目列、幣別/單位、會計基礎、核准/簽證狀態、擷取與覆核職務、差異。
- 科目映射：原帳科目、分類、是否納入營業額、決定依據、權責確認及版本。
- 年度勾稽：營業額、其他收入分項、總收入、財報列、總帳/明細、差異、調整、原件位置。
- 趨勢算式：本年/前期、分子、分母、公式、結果、單位、可比性結論。
- 例外停審：缺件/差異、受影響年度、待辦責任職務、期限欄、解除證據、重算日。
- SAMPLE替換清冊：sample_fact_id、表/列/欄、合成值、真實來源定位、覆核狀態及替換日期；空白不得視為完成。

## 計算與停止條件
逐年增幅=(本年營業額−前一年營業額)/前一年營業額×100%；首年為基準年，不適用。累計變化=(第三年−第一年)/第一年×100%。保留原值，展示兩位小數。分母≤0、幣別/單位不同、年度不連續、會計基礎不同或分類不可調和時，標 N/A 並 HOLD，不自行轉換或估算。其他收入與總收入另行勾稽，不得替代營業額趨勢。

示例預期：2023→24營業額+10.00%；2024→25+10.00%；三年營業額累計+21.00%；總收入1,480,000、1,580,000、1,752,000，首末累計+18.38%。這只證明算術示範正確。
SAMPLE PASS僅代表算式可重算，不代表協會成長或要求完成。REAL HOLD適用於缺授權三年財報/明細、科目映射未確認或帳表差異未解。
退件條件：漏年度、錯分母/期間、未核實捐款/補助混入營業額、表間不平、以近鄰要求替代、把SAMPLE標為REAL、偽造核准/簽名/財報、把官方級距寫成協會分數。

===== END Unique Blueprint =====


===== BEGIN Exact extracted candidate body | SHA256=350713d9b10e258edc819eb294a2b1456cf129537b98a58b8b3547f26f165e4d | BYTES=28948 =====
三年營業額成長與財務來源核對
組織近三年營業額與收入趨勢核對報告
目的：依連續年度財務資料核對營業額趨勢，並將營業額與其他收入分開呈現。
示範資料｜非本會實際紀錄。組織財務原件尚未提供，實際營業額趨勢目前未判定。
文件編號：TTQS-0142｜官方要求：I19-E32｜157清單索引：156｜印刷checkbox serial：UNKNOWN｜內容版本：1.3／R08；建置標籤：R08-TR01｜文件狀態：CANDIDATE｜示範資料：SAMPLE/SYNTHETIC｜REAL證據：UNKNOWN/HOLD｜官方分數：NOT_ASSIGNED｜正式接受：NOT_GRANTED｜生效：未生效｜修訂日：2026-10-28
表1　快速閱讀與本報告用途
表2　官方要求來源基礎
本件只處理上述營業額趨勢核對。合成案例示範完整欄位、計算與判讀；正式實績須以組織可核對的財務原件替換後重算。 本次候選版次沿革及R06→R07逐項變更另見品質旁件，來源包R01保留為歷史來源快照。
1　責任、適用界線與核對路徑
核對範圍是三個連續且已完成結帳的年度。本文中的「營業額」須對應到組織正式財務資料內可跨年度比較的營業收入科目；在實際替換前，由具權限的財務資料保管者確認科目對照。不得以0139／I19-E29考照或就業率及其分母、0140／I19-E30訓練資訊系統採用或使用率、0141／I19-E31顧客滿意度多期量尺或統計替代營業額趨勢；不得借用其資料、期間、樣本、結論或分數。
資料整理者負責從正式財務資料抄錄期間、科目、金額與位置；獨立覆核者重新計算增幅並確認原件、單位、科目及總額一致。真實姓名、職稱、日期與簽核只可由實際經手者如實記錄。
2　來源形成時點及納入規則
優先使用組織正式核准的年度財務報表；如有簽證或查核報告，連同報表及相關附註保存原件定位。
以收入明細、總帳或會計科目表確認營業收入的科目範圍；記錄幣別、單位、會計期間及採用的帳務基礎。
三年資料須使用一致口徑。若科目重分類、期間長短不一、單位不同或來源不完整，先記錄例外並取得可比數據，再作趨勢判定。
來源定位須能由另一位覆核者調回原件，至少記錄文件名稱、年度、頁碼或科目列、組織核准的保存位置。
3　欄位定義與驗證責任
表3　核對欄位定義與驗證責任
4　完整合成核對示例
表4　SAMPLE資料聲明與使用界線
示例期間均為完整年度，幣別單位假設為新臺幣元。表內收入總額只按本示例列出的營業額及其他收入相加；真實報表如有其他收入項目，須一併勾稽正式總額。
金額保留來源原值；百分比以未四捨五入的原始分子與分母計算，最後依四捨五入規則顯示至小數第二位；不先將中間值四捨五入。
表5　三年度營業額與其他收入示例｜SAMPLE資料集A
首年度判讀：2023年度為基準年，沒有前一期可供計算年增率。
示例來源定位（本件內的合成列，並非外部原件）：
表6　示例資料定位與核對責任
示例分工：角色甲整理展示數值；角色乙獨立覆算。兩者均為合成角色，沒有真人簽核或實際財務審查。
4.1　逐步計算與示例判讀
表7　逐年及首末累計趨勢算式
算式覆核結果：本示例表列總額與增幅均可按展示數值重算一致；這是合成算例檢查，不是組織財務查核。
表8　SAMPLE算例判讀
REAL逐年成長的聯合判定規則（下列條件必須全部成立）：(1) 三個連續完整年度的正式財務原件可調回、來源可核實且授權有效；(2) 期間、幣別、單位及會計基礎可比，或已有可查證的正式調節；(3) 營業收入科目由具權責財務角色依正式科目表確認，收入分類一致；(4) 每一年度財報與收入明細／總帳均已勾稽，差異及調整有原件定位並完成覆核；(5) 2024營業額大於2023，且2025大於2024。任一條件不成立、缺件或未覆核，REAL維持UNKNOWN/HOLD；不得以示例算術推論協會持續成長。
5　證據限制、例外處理與追蹤
目前可用資料含官方要求文字及核對方法，未提供組織正式財報、收入明細／總帳原件或真實附件，也沒有可引用的真實檔名、頁碼或附件定位。因此組織近三年實際營業額趨勢為「未判定」。
表9　證據限制與例外處理
6　真實資料替換與升格條件
表10　真實資料替換與升格條件
7　要求追溯、相鄰要求及文件保管
表11　官方要求、欄位及證據位置追溯
相鄰要求辨別：0139／I19-E29為考照／就業率與分母；0140／I19-E30為訓練資訊系統採用／使用率；0141／I19-E31為顧客滿意度多期量尺統計。三者的資料、期間、樣本、結論或分數均不得替代本件營業額與財報核實。
保管與附件：取得正式財報、收入明細／總帳原件及真實附件後，將原件定位及本報告修訂版一併保存於組織核准的受控位置，僅授權人員調閱。本文未附任何組織財務原件或真實附件；官方第9頁僅作文字引用，合成示例位置見第4節表5至表8；來源登錄、科目映射、帳表勾稽、停審條件及逐列替換見第8至12節表12至表16。內容版本：1.3／R08（候選文件；SAMPLE/SYNTHETIC示範；未生效）；建置標籤：R08-TR01；父候選：R07-LF01；修訂日期及生效狀態依首頁文件控制資訊（I19-E32；157索引156；印刷序號UNKNOWN），不代表財務資料日期、覆核或核准日期。
8　年度來源登錄與原件調回
表12以同一組合成資料示範逐年如何記錄來源識別、版本、期間、頁列、幣別與帳務基礎、核准狀態、整理／覆核角色及差異。列出的來源識別只指向本文件的SAMPLE資料集，並非實際財報、總帳或外部原件；REAL來源尚未提供，所有年份維持HOLD。
表12　年度來源登錄（SAMPLE例示；REAL原件未提供）
9　科目映射與收入分類
表13示範把「營業額」的案例假設和其他收入分開。非營利組織實際科目是否屬營業收入，必須由有權的財務資料保管者依組織會計科目表確認；本表的SAMPLE分類不是協會會計政策或正式核准。
表13　營業收入與其他收入科目映射（示例假設與REAL關卡）
10　年度帳表勾稽與差異調節
表14先核對三年度示範收入合計，再把「算術差異」與「財報對總帳差異」分開。表內加總差異為SAMPLE數學檢查；未取得財報及總帳原件，因此正式帳表差異不是零，而是UNKNOWN/HOLD。
表14　年度收入勾稽與帳表差異調節（SAMPLE）
11　例外停審與解除條件
以下任一情形都必須先停下受影響年度或分類，不得以估算補值或SAMPLE結論解除REAL停審。實際責任人與期限只能由協會指定；在原件、權限或差異證據未完成前，維持UNKNOWN/HOLD。
表15　例外、停審責任與解除證據
REAL退件條件（適用真實佐證包或正式送審主張；本候選的SAMPLE完整示例不等於REAL通過）：漏任一完整年度；期間不連續或短年度不可比；分母≤0仍計算或未標N/A/HOLD；來源、會計基礎或科目分類不可追溯；捐款、補助、會費、代收款、一次性收入、退款／折讓／沖銷未分類即併入；表間差異未調節；調整無憑證或原件位置；以0139考照／就業率、0140系統使用率或0141滿意度替代；把SAMPLE標為REAL；偽造簽名、核准、財報、第三方原件或官方分數。
12　逐列SAMPLE替換清冊
表16列碼F01–F19逐列對應隨附CSV的display_id；CSV保留完整sample_fact_id供追溯。金額均為SAMPLE/SYNTHETIC，幣別以新臺幣為示範假設。REAL財務原件尚未提供者一律UNKNOWN/HOLD、未覆核、未替換；封面修訂資料不是財務證據，也不代表核准生效。 實務替換時另存獨立REAL版本，保留本文SAMPLE列不覆寫；逐列替換狀態以隨附CSV為準。
表16　SAMPLE逐列替換清冊（19列；18項合成事實及1項文件控制中繼資料）
[TABLE 1]
快速閱讀 | 本報告說明
閱讀對象 | 執行人員、主管、財務資料保管者及評核閱讀者。
使用時點 | 年度結帳後整理評核佐證，或覆核近三個完整年度的收入趨勢時。
操作方式 | 取三個可比完整年度的正式財務原件，核對科目與單位，再按本文公式覆算。
輸出內容 | 年度營業額、其他收入、總收入、逐年增幅、來源定位、限制及覆核狀態。
目前狀態（分項） | CANDIDATE；SAMPLE/SYNTHETIC示範；REAL=UNKNOWN/HOLD；官方分數=NOT_ASSIGNED；正式接受=NOT_GRANTED；未生效。組織實際趨勢未判定。
[TABLE 2]
官方勾選原文：「組織近三年營業額持續成長。」Requirement：I19-E32；157清單索引156。 本機來源檔名：TTQS查核佐證文件資料表-訓練機構版 (2).pdf；PDF SHA-256：805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709；共9頁，本件引用第9頁／9頁。 原件版次／官方發布日／本機下載日：UNKNOWN；本機檔案修改時間2026-10-02 01:37:44+08:00僅為檔案系統中繼資料，不視為發布或下載證據；SHA與頁數於2026-10-28本機核對。 PDF內嵌CreationDate/ModDate：2026-01-07 15:56+08:00（檔案中繼資料，非正式版次）。以上引用不代表已取得或核實組織財務原件。
[TABLE 3]
欄位與定義 | 來源、填寫者及驗證規則
年度及期末日 財報所列完整會計期間。 | 正式財報期間；整理者填列。覆核者確認三年度連續、均已結帳且比較期間一致。
幣別及單位 原件的金額表示方式。 | 正式財報或附註；整理者照錄。覆核者確認全期一致；如換算，保留原值、換算依據與計算。
營業額 經確認可代表營業收入的正式科目或科目彙總。 | 正式財報及收入明細；整理者照錄。覆核者對照科目表及總帳，確認三年歸類一致。
其他收入 與營業額分列的其他收入金額。 | 正式財報及附註；整理者照錄。覆核者確認未重複併入營業額，並能勾稽總收入。
總收入 依正式報表口徑呈現的收入總額。 | 正式財報及收入彙總；整理者填列。覆核者與報表總額勾稽；不得漏列其他收入科目。
年增率 （本年營業額－前一年營業額）÷前一年營業額。 | 由已核實的年度金額計算；整理者計算，覆核者獨立重算。前一年基數須大於零；否則列明原因並標示不適用。
來源定位 可回到原始財務證據的位置。 | 正式檔名、年度、頁碼、科目列及受控保存位置；整理者記錄。覆核者實際調閱並確認版本。
判定與例外 逐年增減、限制及處置結果。 | 按完整、可比年度及計算結果判讀；覆核者確認每個比較區間及異常處理均有追蹤記錄。
[TABLE 4]
示例資料聲明 以下為完整合成資料集，只示範如何逐年核對與重算。示例假設「營業額」對應「服務收入」；這不是任何組織的真實科目、財報或會計結論。正式使用須以實際財報科目對照取代。
[TABLE 5]
年度（期末） | 營業額 新臺幣元 | 其他收入 新臺幣元 | 總收入 新臺幣元 | 營業額年增率
2023年度 12月31日 | 1,200,000 | 280,000 | 1,480,000 | 基準年
2024年度 12月31日 | 1,320,000 | 260,000 | 1,580,000 | +10.00%
2025年度 12月31日 | 1,452,000 | 300,000 | 1,752,000 | +10.00%
[TABLE 6]
年度 | 示例資料位置／覆核欄位
2023 | 第4節表5第2列（示例資料集 A；僅為合成示例）。覆核欄位：營業額與總收入按表列值算術勾稽；本年為基準年，年增率不適用。真實原件覆核：正式財報、收入明細／總帳原件及真實附件未提供。
2024 | 第4節表5第3列（示例資料集 A；僅為合成示例）。覆核欄位：營業額、總收入及年增率按表列值重算一致。真實原件覆核：正式財報、收入明細／總帳原件及真實附件未提供。
2025 | 第4節表5第4列（示例資料集 A；僅為合成示例）。覆核欄位：營業額、總收入及年增率按表列值重算一致。真實原件覆核：正式財報、收入明細／總帳原件及真實附件未提供。
[TABLE 7]
核對項目與期間 | 逐步算式（含分子／分母） | 結果、單位與可比性
2024營業額年增率｜本年1,320,000；前期1,200,000 | 分子=1,320,000−1,200,000=120,000；分母=1,200,000；120,000÷1,200,000×100% | +10.00%；百分比。僅在完整年度、幣別／單位及分類一致時可比；本例為SAMPLE假設。
2025營業額年增率｜本年1,452,000；前期1,320,000 | 分子=1,452,000−1,320,000=132,000；分母=1,320,000；132,000÷1,320,000×100% | +10.00%；百分比。僅在完整年度、幣別／單位及分類一致時可比；本例為SAMPLE假設。
2023至2025營業額累計變動｜末年1,452,000；基年1,200,000 | 分子=1,452,000−1,200,000=252,000；分母=1,200,000；252,000÷1,200,000×100% | +21.00%；百分比。此值不替代逐年正成長檢查；本例為SAMPLE假設。
2023至2025總收入累計變動｜末年1,752,000；基年1,480,000 | 分子=1,752,000−1,480,000=272,000；分母=1,480,000；272,000÷1,480,000×100% | +18.38%；百分比。總收入僅作旁列，不能替代營業額趨勢。
[TABLE 8]
示例判定 在本組合成數值中，2024及2025營業額均高於前一年；三年營業額累計增加21.00%。按本文的逐年正增幅核對方法，算例符合持續成長的計算條件。此結論只描述示例，不能移作組織實績或外部財務證明。
[TABLE 9]
問題／目前狀態 | 修正或後續處理 | 覆核與追蹤
未附組織財務原件；組織實績維持「未判定」。 | 取得最近三個完整會計年度正式財報及可勾稽的收入明細；按正式科目與單位替換本報告示例數值及示例位置。 | 第二位具權限人員調閱原件，重算期間、分類、總額與每段年增率。保留取得日期、原件定位、差異及修正版本；原件取得前不得採用示例結論。
[TABLE 10]
替換項目 | 完成條件
三年度來源 | 以實際最近三個完整年度的正式財報取代示例；保留核准版本及可調閱的文件名稱、年度、頁碼或科目列。
科目與總額 | 由具權限財務資料保管者確認哪些正式科目構成營業額及總收入；與總帳、收入明細或報表附註勾稽。
期間、單位及公式 | 記錄實際期間、幣別、金額單位及帳務口徑；重算每一年度增幅與三年變動。基期為零或資料不可比時，說明限制，不套用一般增幅。
分工及覆核 | 以真實經手角色完成抄錄與獨立覆算；姓名、職務、日期、簽核只由本人按組織程序如實填寫。
保存及調閱 | 將核准原件與核對紀錄存於組織核准的受控位置，按既有權限保護及調閱；另保留修訂前後的差異軌跡。
[TABLE 11]
追溯事項 | 本件位置及判斷
官方要求與文件定位 | 官方原文：組織近三年營業額持續成長。｜Requirement：I19-E32｜157清單索引：156｜印刷 checkbox serial：UNKNOWN｜來源：TTQS訓練機構版查核佐證資料表實體第9頁。
資料、方法與判讀 | 第4節表5至表8提供三年度SAMPLE資料、來源定位、逐步算式及示例判讀；第8至12節表12至表16提供來源登錄、科目映射、帳表勾稽、例外停審及逐列替換。表5至表8均為SAMPLE/SYNTHETIC，不能證明本會實績。
限制、跨文件與升格 | 沒有受權三年財報、收入明細／總帳、科目映射及逐年調節證據；REAL=UNKNOWN/HOLD、官方分數NOT_ASSIGNED、正式接受NOT_GRANTED。只以本件SAMPLE ID追蹤；沒有共享REAL source_id/fact_id，不推定0139、0140、0141或其他文件的數字、期間或結論可沿用。
[TABLE 12]
年度與期間／SAMPLE來源ID | SAMPLE來源、版本及文件定位 | 幣別／單位 會計基礎 | 整理角色 獨立覆核角色／日期 核准狀態 | 示例金額摘要 | REAL原件定位與狀態 | 差異（SAMPLE／REAL分開）
SYN-SRC-2023-A｜2023-01-01至2023-12-31 | 本文件SAMPLE資料集A；表5第2023列；版本SYN-R01；非外部原件 | 新臺幣元；完整曆年 SAMPLE：未指定權責制或現金制 REAL：照正式財報／附註記錄；未確認或年度間不一致即HOLD | 整理角色：SAMPLE合成角色甲 獨立覆核角色：SAMPLE合成角色乙（示例、非真人／非實際覆核） 日期：N/A（無真實覆核日期） 核准狀態：無真人調閱或簽核 | 示例營業額1,200,000；其他收入280,000；總收入1,480,000 | 正式財報名稱／版本／頁碼、收入明細或總帳科目列、幣別與基礎、受控原件位置均未提供；REAL=UNKNOWN/HOLD | SAMPLE勾稽差異：0元；REAL財報／總帳差異：UNKNOWN/HOLD，未取得原件。
SYN-SRC-2024-A｜2024-01-01至2024-12-31 | 本文件SAMPLE資料集A；表5第2024列；版本SYN-R01；非外部原件 | 新臺幣元；完整曆年 SAMPLE：未指定權責制或現金制 REAL：照正式財報／附註記錄；未確認或年度間不一致即HOLD | 整理角色：SAMPLE合成角色甲 獨立覆核角色：SAMPLE合成角色乙（示例、非真人／非實際覆核） 日期：N/A（無真實覆核日期） 核准狀態：無真人調閱或簽核 | 示例營業額1,320,000；其他收入260,000；總收入1,580,000 | 正式財報名稱／版本／頁碼、收入明細或總帳科目列、幣別與基礎、受控原件位置均未提供；REAL=UNKNOWN/HOLD | SAMPLE勾稽差異：0元；REAL財報／總帳差異：UNKNOWN/HOLD，未取得原件。
SYN-SRC-2025-A｜2025-01-01至2025-12-31 | 本文件SAMPLE資料集A；表5第2025列；版本SYN-R01；非外部原件 | 新臺幣元；完整曆年 SAMPLE：未指定權責制或現金制 REAL：照正式財報／附註記錄；未確認或年度間不一致即HOLD | 整理角色：SAMPLE合成角色甲 獨立覆核角色：SAMPLE合成角色乙（示例、非真人／非實際覆核） 日期：N/A（無真實覆核日期） 核准狀態：無真人調閱或簽核 | 示例營業額1,452,000；其他收入300,000；總收入1,752,000 | 正式財報名稱／版本／頁碼、收入明細或總帳科目列、幣別與基礎、受控原件位置均未提供；REAL=UNKNOWN/HOLD | SAMPLE勾稽差異：0元；REAL財報／總帳差異：UNKNOWN/HOLD，未取得原件。
[TABLE 13]
科目ID／狀態 | 合成科目與分類 | 納入營業額？ | 示例依據及適用範圍 | REAL權責確認、版本與狀態 | 正式分類決定依據
SYN-REV-SVC-01 | 示例服務收入；合成科目，不是真實科目代碼 | 本算例假設納入 | 只為示範逐年營業額公式；不代表協會科目映射 | REAL科目表與權責確認未提供；UNKNOWN/HOLD | SAMPLE假設僅供算例；REAL須以正式科目表、財報列與收入明細／總帳定位，經有權財務角色確認並記錄年度及版本。未確認即HOLD。
SYN-OTHER-AGG-01 | 示例其他收入合計；合成總額，不推定其構成 | 不納入本例營業額；另列 | 280,000／260,000／300,000只作其他收入欄，未拆成實際來源類別 | REAL分類、原始科目與版本未確認；UNKNOWN/HOLD | 示範金額不得推定科目；REAL須對正式科目表、財報列與收入明細／總帳，保留分類及排除依據。未確認即HOLD。
REAL-CLASSIFICATION-GATE | 捐款、補助、會費、利息、代收款、退款／折讓等候核項目 | 未核實前不自行納入 | 逐項比對財報列、總帳明細及分類依據；不以總收入替代營業額 | 由實際財務權責角色確認；原件、核准依據及版本未提供；HOLD | 逐項比對正式核准科目表、財報與收入明細／總帳；有權財務角色確認分類、會計基礎、適用年度與版本，並記錄決定日期；任何缺件均HOLD。
[TABLE 14]
年度 | 營業額（SAMPLE） | 其他收入（SAMPLE） | 總收入（SAMPLE） | 示例加總差異 | REAL財報／總帳差異 | 調整金額與理由 | 原件定位（REAL）
2023 | 1,200,000 | 280,000 | 1,480,000 | SAMPLE差異0元；1,200,000＋280,000−1,480,000＝0 | UNKNOWN/HOLD；財報／總帳原件未提供；不得填成零。 | SAMPLE不作REAL調整；REAL調整分錄、金額及理由未提供／UNKNOWN。 | SAMPLE定位：表5第2023列；REAL財報頁碼／總帳科目列未提供／UNKNOWN/HOLD。
2024 | 1,320,000 | 260,000 | 1,580,000 | SAMPLE差異0元；1,320,000＋260,000−1,580,000＝0 | UNKNOWN/HOLD；財報／總帳原件未提供；不得填成零。 | SAMPLE不作REAL調整；REAL調整分錄、金額及理由未提供／UNKNOWN。 | SAMPLE定位：表5第2024列；REAL財報頁碼／總帳科目列未提供／UNKNOWN/HOLD。
2025 | 1,452,000 | 300,000 | 1,752,000 | SAMPLE差異0元；1,452,000＋300,000−1,752,000＝0 | UNKNOWN/HOLD；財報／總帳原件未提供；不得填成零。 | SAMPLE不作REAL調整；REAL調整分錄、金額及理由未提供／UNKNOWN。 | SAMPLE定位：表5第2025列；REAL財報頁碼／總帳科目列未提供／UNKNOWN/HOLD。
[TABLE 15]
停止條件 | 受影響範圍 | 判定／停止規則 | 責任角色與期限 | 解除證據及後續重算 | 重算日期（SAMPLE／REAL分開）
正式年度財報或必要附註缺件 | 受影響年度；三年趨勢不得定案 | HOLD；不外推 | 財務資料保管角色；實際期限由單位指定 | 取得授權版本、完整年度與可調回頁碼／科目列後重算 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
年度不連續、短年度或結帳狀態不明 | 相關年度與相鄰成長率 | 不可比；N/A／HOLD | 資料整理角色與財務覆核角色；期限由單位指定 | 確認起訖日、結帳完成狀態及可比較的連續期間 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
前期基數≤0或金額單位不同 | 受影響公式與累計比較 | 該增幅=N/A並標記HOLD；不得除以零或自行換算。 | 覆核角色；期限由單位指定 | 取得權威幣別／單位及可用基期；保留原值與換算依據 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
營業收入科目尚未核定 | 所有營業額欄及成長結論 | HOLD；其他收入不得代替 | 具權限財務資料保管角色；期限由單位指定 | 核對核准科目表、分類依據、年度適用版本及授權確認 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
財報與總帳／收入明細不相符 | 差異涉及年度、科目與總額 | HOLD；差異不得寫成零 | 整理角色與獨立覆核角色；期限由單位指定 | 逐項定位差異、調整分錄及原件；重算並保留前後金額 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
捐款、補助、會費、代收款或一次性收入混入 | 受影響分類及趨勢 | 分類未決則排除並HOLD | 財務權責角色；期限由單位指定 | 取得收入明細與分類依據；確認是否屬營業收入後重算 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
財報版本、核准狀態或來源位置不可追溯 | 相關年度原件與計算 | HOLD；不得以截圖或未授權副本替代 | 原件保管角色；期限由單位指定 | 記錄正式名稱、版本、頁列、核准狀態及受控保存位置 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
REAL原件缺授權或不可公開 | 原件調閱／分享範圍 | 不得上傳或公開；維持UNKNOWN/HOLD | 資料保管角色；期限由單位指定 | 在有權限的受控來源完成核對；公開版只列不敏感的驗收狀態 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
會計基礎不同（權責／現金）且未調節 | 受影響年度、營業額比較與累計結果 | 不可比；相關百分比=N/A並HOLD；不得自行換算 | 財務權責角色與獨立覆核角色；期限由單位指定 | 取得各年度正式基礎、調節明細及可比證據；保留原值、調節分錄、來源位置後重算 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
退款、折讓或沖銷未分類／未勾稽 | 受影響年度、收入科目及淨額趨勢 | 分類未決或金額未勾稽即HOLD；不得忽略或重複扣除 | 財務權責角色與獨立覆核角色；期限由單位指定 | 取得原始憑證、正式科目、總帳位置與計算依據；確認淨額處理後重算 | SAMPLE算例重算日：2026-10-28；REAL：N/A（未取得原件、未重算，UNKNOWN/HOLD）。解除後記錄實際覆核日期。
[TABLE 16]
列碼 | 文件位置 | SAMPLE示例值／單位 | REAL替換必要來源 | REAL狀態／覆核／日期
F01 | 表5／6｜2023年度 | 2023完整曆年；SAMPLE | 授權年度財報＋會計期間佐證 | UNKNOWN/HOLD 未覆核；未替換
F02 | 表5營業收入／表6｜2023 | 1,200,000元；NTD假設 | 授權財報＋收入明細／總帳＋科目映射 | UNKNOWN/HOLD 未覆核；未替換
F03 | 表5其他收入｜2023 | 280,000元；分列SAMPLE | 授權財報＋已勾稽收入明細／總帳 | UNKNOWN/HOLD 未覆核；未替換
F04 | 表5總收入／表14勾稽｜2023 | 1,480,000元；合成加總 | 授權財報＋收入明細／總帳勾稽 | UNKNOWN/HOLD 未覆核；未替換
F05 | 表5／6｜2024年度 | 2024完整曆年；SAMPLE | 授權年度財報＋會計期間佐證 | UNKNOWN/HOLD 未覆核；未替換
F06 | 表5營業收入／表6｜2024 | 1,320,000元；NTD假設 | 授權財報＋收入明細／總帳＋科目映射 | UNKNOWN/HOLD 未覆核；未替換
F07 | 表5其他收入｜2024 | 260,000元；分列SAMPLE | 授權財報＋已勾稽收入明細／總帳 | UNKNOWN/HOLD 未覆核；未替換
F08 | 表5總收入／表14勾稽｜2024 | 1,580,000元；合成加總 | 授權財報＋收入明細／總帳勾稽 | UNKNOWN/HOLD 未覆核；未替換
F09 | 表5／6｜2025年度 | 2025完整曆年；SAMPLE | 授權年度財報＋會計期間佐證 | UNKNOWN/HOLD 未覆核；未替換
F10 | 表5營業收入／表6｜2025 | 1,452,000元；NTD假設 | 授權財報＋收入明細／總帳＋科目映射 | UNKNOWN/HOLD 未覆核；未替換
F11 | 表5其他收入｜2025 | 300,000元；分列SAMPLE | 授權財報＋已勾稽收入明細／總帳 | UNKNOWN/HOLD 未覆核；未替換
F12 | 表5總收入／表14勾稽｜2025 | 1,752,000元；合成加總 | 授權財報＋收入明細／總帳勾稽 | UNKNOWN/HOLD 未覆核；未替換
F13 | 表5年增率／表7｜2024 | 10.00%；合成重算 | REAL來源替換後重算並覆核 | SAMPLE重算日：2026-10-28；REAL：N/A（未替換、未覆核），UNKNOWN/HOLD
F14 | 表5年增率／表7｜2025 | 10.00%；合成重算 | REAL來源替換後重算並覆核 | SAMPLE重算日：2026-10-28；REAL：N/A（未替換、未覆核），UNKNOWN/HOLD
F15 | 表7營業收入累計 | 21.00%；合成重算 | REAL來源替換後重算並覆核 | SAMPLE重算日：2026-10-28；REAL：N/A（未替換、未覆核），UNKNOWN/HOLD
F16 | 表7總收入累計 | 18.38%；合成重算 | REAL來源替換後重算並覆核 | SAMPLE重算日：2026-10-28；REAL：N/A（未替換、未覆核），UNKNOWN/HOLD
F17 | 表5–7幣別／單位 | 新臺幣元；示範假設 | 核定財報幣別與計量單位 | UNKNOWN/HOLD 未覆核；未替換
F18 | 表4假設／表13科目映射 | 營業收入＝服務收入；合成假設 | 核定科目表＋財務角色確認 | UNKNOWN/HOLD 未覆核；未替換
F19 | 封面版次控制欄 | 候選內容版本1.3/R08；建置R08-TR01（針對獨立審查發現的版本、登錄與替換指示修復）；修訂日2026-10-28（控制中繼資料，不是財務事實） | 受控候選版次紀錄；生效核准另查 | 不適用於REAL財務；候選未生效／未核准

===== END Exact extracted candidate body =====


===== BEGIN 19-row SAMPLE replacement register | SHA256=b9ef1b7f1c9b703377f0284582cc72c4251d483cbeeae3adf8f6279e6aaa372b | BYTES=11131 =====
sample_fact_id,doc_id,requirement_id,data_status,fact_type,synthetic_value,unit_or_basis,document_locator,derivation_or_use,real_replacement_source_required,real_status,replacement_rule,real_review_status,replacement_date,display_id,sample_recalculation_date
SYN-0142-FY-2023,0142,I19-E32,SAMPLE/SYNTHETIC,reporting_period_and_year_end,2023-01-01 through 2023-12-31; year end 2023-12-31,complete calendar year; NTD assumed,Table 5 row 2023; Table 6 row 2023,Synthetic period and date used for a three-year arithmetic example,Authorized complete-year financial statements and accounting-period evidence,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F01,
SYN-0142-OPERATING-2023,0142,I19-E32,SAMPLE/SYNTHETIC,operating_revenue,1200000,NTD; illustrative service-revenue mapping only,"Table 5 row 2023, operating revenue column; Table 6 row 2023","Synthetic base value; account mapping is an explicit example assumption, not an association account classification","Authorized financial statement, revenue detail/general ledger, and finance-role account mapping",UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F02,
SYN-0142-OTHER-2023,0142,I19-E32,SAMPLE/SYNTHETIC,other_income,280000,"NTD; synthetic, separate from operating revenue","Table 5 row 2023, other income column",Synthetic amount kept separate; not used as a substitute for operating-revenue growth,Authorized financial statements and reconciled ledger/detail,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F03,
SYN-0142-TOTAL-2023,0142,I19-E32,SAMPLE/SYNTHETIC,total_income_derived,1480000,NTD; derived synthetic amount,"Table 5 row 2023, total income column; Table 7 formulas/summary",Derived: 1200000 + 280000; arithmetic cross-check only,Authorized financial statement and reconciled ledger/detail,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F04,
SYN-0142-FY-2024,0142,I19-E32,SAMPLE/SYNTHETIC,reporting_period_and_year_end,2024-01-01 through 2024-12-31; year end 2024-12-31,complete calendar year; NTD assumed,Table 5 row 2024; Table 6 row 2024,Synthetic period and date used for a three-year arithmetic example,Authorized complete-year financial statements and accounting-period evidence,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F05,
SYN-0142-OPERATING-2024,0142,I19-E32,SAMPLE/SYNTHETIC,operating_revenue,1320000,NTD; illustrative service-revenue mapping only,"Table 5 row 2024, operating revenue column; Table 6 row 2024","Synthetic base value; account mapping is an explicit example assumption, not an association account classification","Authorized financial statement, revenue detail/general ledger, and finance-role account mapping",UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F06,
SYN-0142-OTHER-2024,0142,I19-E32,SAMPLE/SYNTHETIC,other_income,260000,"NTD; synthetic, separate from operating revenue","Table 5 row 2024, other income column",Synthetic amount kept separate; not used as a substitute for operating-revenue growth,Authorized financial statements and reconciled ledger/detail,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F07,
SYN-0142-TOTAL-2024,0142,I19-E32,SAMPLE/SYNTHETIC,total_income_derived,1580000,NTD; derived synthetic amount,"Table 5 row 2024, total income column; Table 7 formulas/summary",Derived: 1320000 + 260000; arithmetic cross-check only,Authorized financial statement and reconciled ledger/detail,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F08,
SYN-0142-FY-2025,0142,I19-E32,SAMPLE/SYNTHETIC,reporting_period_and_year_end,2025-01-01 through 2025-12-31; year end 2025-12-31,complete calendar year; NTD assumed,Table 5 row 2025; Table 6 row 2025,Synthetic period and date used for a three-year arithmetic example,Authorized complete-year financial statements and accounting-period evidence,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F09,
SYN-0142-OPERATING-2025,0142,I19-E32,SAMPLE/SYNTHETIC,operating_revenue,1452000,NTD; illustrative service-revenue mapping only,"Table 5 row 2025, operating revenue column; Table 6 row 2025","Synthetic base value; account mapping is an explicit example assumption, not an association account classification","Authorized financial statement, revenue detail/general ledger, and finance-role account mapping",UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F10,
SYN-0142-OTHER-2025,0142,I19-E32,SAMPLE/SYNTHETIC,other_income,300000,"NTD; synthetic, separate from operating revenue","Table 5 row 2025, other income column",Synthetic amount kept separate; not used as a substitute for operating-revenue growth,Authorized financial statements and reconciled ledger/detail,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F11,
SYN-0142-TOTAL-2025,0142,I19-E32,SAMPLE/SYNTHETIC,total_income_derived,1752000,NTD; derived synthetic amount,"Table 5 row 2025, total income column; Table 7 formulas/summary",Derived: 1452000 + 300000; arithmetic cross-check only,Authorized financial statement and reconciled ledger/detail,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F12,
SYN-0142-OPERATING-YOY-2024,0142,I19-E32,SAMPLE/SYNTHETIC,year_over_year_growth_derived,10.00%,percent; synthetic-derived,"Table 5 row 2024, growth column; Table 7 row for 2024",(current-year operating revenue - prior-year operating revenue) / prior-year operating revenue × 100,Recalculate after authorized actual source replacement,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F13,2026-10-28
SYN-0142-OPERATING-YOY-2025,0142,I19-E32,SAMPLE/SYNTHETIC,year_over_year_growth_derived,10.00%,percent; synthetic-derived,"Table 5 row 2025, growth column; Table 7 row for 2025",(current-year operating revenue - prior-year operating revenue) / prior-year operating revenue × 100,Recalculate after authorized actual source replacement,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F14,2026-10-28
SYN-0142-OPERATING-CUMULATIVE-2023-2025,0142,I19-E32,SAMPLE/SYNTHETIC,cumulative_operating_growth_derived,21.00%,percent; synthetic-derived,Table 7 R4 (cumulative operating revenue); Table 8 R1 (SAMPLE conclusion),(2025 synthetic operating revenue - 2023 synthetic operating revenue) / 2023 synthetic operating revenue × 100,Recalculate after authorized actual source replacement,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F15,2026-10-28
SYN-0142-TOTAL-CUMULATIVE-2023-2025,0142,I19-E32,SAMPLE/SYNTHETIC,cumulative_total_income_growth_derived,18.38%,percent; synthetic-derived,Table 7 cumulative total-income row,(2025 synthetic total income - 2023 synthetic total income) / 2023 synthetic total income × 100,Recalculate after authorized actual source replacement,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F16,2026-10-28
SYN-0142-CURRENCY-UNIT,0142,I19-E32,SAMPLE/SYNTHETIC,currency_and_unit_assumption,New Taiwan dollars (NTD),illustrative assumption,Tables 5-7 and SAMPLE narrative,Synthetic unit for demonstration only; not read from an association statement,Authorized source statements and consistent unit/currency basis,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F17,
SYN-0142-ACCOUNT-MAPPING-ASSUMPTION,0142,I19-E32,SAMPLE/SYNTHETIC,account_mapping_assumption,Example assumes 'operating revenue' corresponds to 'service revenue',explicit synthetic assumption,Table 4 SAMPLE disclosure and Table 5 label,Not an association classification decision; actual non-profit classification requires authorized finance review,Approved chart of accounts and documented finance-role mapping,UNKNOWN/HOLD,Replace only from authorized actual financial statements and reconciled ledger/detail; confirm account mapping with authorized finance role; otherwise remain UNKNOWN/HOLD.,NOT_REVIEWED_REAL,NOT_REPLACED,F18,
SYN-0142-DOCUMENT-CONTROL-DATE,0142,I19-E32,CONTROL_METADATA,document_revision_metadata,候選內容版本1.3/R08；建置R08-TR01（針對獨立審查發現的版本、登錄與替換指示修復）；修訂日2026-10-28（控制中繼資料，不是財務事實）,candidate control metadata; not financial evidence,Cover document control field,R06 candidate revision date; does not establish approval or effectiveness,Not applicable as financial evidence; any effectiveness requires a separate authorized document-control record,NOT_APPLICABLE,Do not treat as a synthetic financial fact or as approval. Record effectiveness only from the controlled register and authorized approval.,NOT_REVIEWED_REAL,NOT_REPLACED,F19,

===== END 19-row SAMPLE replacement register =====


===== BEGIN Candidate lineage chain | SHA256=ef44a720a9857d6455c76a25496bbc4a6fe82eb2b634bc955f8bc28c94bf435c | BYTES=8014 =====
# 0142 I19-E32 Candidate Lineage Chain R08-TR01

## Identity and evidence boundary

Project TTQS ONE; doc_id 0142; official requirement I19-E32; checkbox index 156; printed checkbox serial UNKNOWN.
Source packet SHA-256: e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49.
Unique Blueprint SHA-256: 4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b.
Current R08-TR01 candidate SHA-256: 7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78. Candidate remains SAMPLE/SYNTHETIC; REAL=UNKNOWN/HOLD; formal acceptance NOT_GRANTED.
Parent lineage JSON CANDIDATE_LINEAGE_0142_R07.json SHA-256: 26649bd598d3f57739dee7e353e51cf181264d446580445462a2f78c27c639bc. R07-LF01 extension CANDIDATE_LINEAGE_0142_R07_LAYOUTFIX_R01.json SHA-256: f805ee51ee1a4a3b09d78eded51477e59f8a5bacd4ccf8a6e386dccb42a764e5.
R01 baseline hash is preserved exactly as recorded in the parent lineage. Original bytes were not found in the searched 0142 source tree, so the historical baseline hash is not claimed as independently recalculated.

## Selected parent chain

| Revision | Parent SHA-256 | Candidate SHA-256 | Local byte verification and note |
|---|---|---|---|
| R01 baseline | — | 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6 | Hash recorded in parent lineage; original DOCX bytes not found in searched 0142 source tree, so not independently recomputed. |
| R03 selected table-cell margin | 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6 | c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861 | Local SHA-256 recomputed. |
| R04 selected table flow | c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861 | e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c | Local SHA-256 recomputed. |
| R05 header contrast | e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c | a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e | Local SHA-256 recomputed. |
| R06 structural completion | a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e | 60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6 | Local SHA-256 recomputed; prior semantic review PARTIAL applies only to this exact SHA. |
| R07 targeted semantic repair | 60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6 | 35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd | Local SHA-256 recomputed. |
| R07-LF01 layout-only repair | 35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd | ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f | Local SHA-256 recomputed; only empty manual page-break paragraph before Section 5 removed; non-empty body/table text unchanged. |
| R08-TR01 targeted semantic repair | ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f | 7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78 | Local SHA-256 recomputed; repairs F1-F6 in the exact parent review. |

R02 math/flow candidates and the separate R03 flow-fix lineage are parallel historical branches in the supplied parent JSON; they are not ancestors of the selected R06 to R07 chain, and their verdicts are not transferred.

## Exact-SHA review and QA

R07-LF01 OpenCode review returned PARTIAL on exact candidate SHA ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f. Actual OpenCode route: opencode/deepseek-v4.1-flash-free; session ses_e7f5bb7edffeTU85K8yTYjVT8R; session outcome succeeded; reported cost 0; account billing remains UNKNOWN.
Original reviewer response SHA-256: 2adc48777fe86b044258b2aa79f00a104d11b734332bfa742f95342750b0f6a9; sanitized session export SHA-256: 3089622869d1de32bb4e28e0f203f8b35e3c81d0edab0e505acd9398fefdcae1; dispatch receipt SHA-256: 8d0c062d102a16806d20219e707318f2c480711fb3813a774e2b89970fc780b5.
The six findings and their R08 repairs are enumerated in PATCH_RECEIPT_0142_R08_TARGETED_REPAIR_R01.json.
R08 technical QA receipt SHA-256: 474094109308849a9bcfeddb7d94b0c068f93199082b8c72e19e48b81b38b1f1 (PASS).
Word-native render receipt SHA-256: d2d93a1fd7c8fb54c14da3ff180257ea02547bba60d9b5696c56d6f220eefc0e; PDF SHA-256: 718b5807164bec5e1d519f8ac52236f3e45ae17f040edc5b25f76791a4ca6c2e; 14 pages; DOCX unchanged by render.
Page-image manifest SHA-256: d5b7ab71332583549b1971f3599dae5cbc712712bc5e697f8f84a0c2ba5a561f; visual QA SHA-256: 0f08c04c7b9ae98ae3888703f1126537b16c5a37b2d8b74c19219997499530dc (all 14 pages visually inspected at original resolution, PASS).
Replacement register SHA-256: b9ef1b7f1c9b703377f0284582cc72c4251d483cbeeae3adf8f6279e6aaa372b.

No candidate evidence here establishes REAL association performance, formal acceptance, or an official score.

## R12 per-stage metadata readback

This table separates recorded build dates from filesystem timestamps. Filesystem mtime is observational metadata only and is not represented as a build event. R01 source bytes remain unavailable; its historical SHA is not independently verified. For each present selected-chain DOCX, the local SHA-256 and byte count below were read from the exact Windows path.

| Stage | Revision/version label | Candidate SHA-256 | Bytes | Recorded build date | Filesystem mtime (not build-date proof) | Change type | Verifier/evidence |
|---|---|---|---:|---|---|---|---|
| R01 baseline | R01 baseline | 59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6 | UNKNOWN | UNKNOWN | NOT_AVAILABLE | baseline candidate; original bytes absent from searched local source tree | No original binary; SHA exists only in historical parent lineage; not independently recomputed. |
| R03 selected table-cell margin | R03 | c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861 | 44984 | UNKNOWN unless a separate build receipt proves it | 2026-10-27T23:19:38+08:00 | selected table-cell margin repair | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R04 selected table flow | R04 | e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c | 44991 | UNKNOWN unless a separate build receipt proves it | 2026-10-27T23:21:38+08:00 | table-flow repair | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R05 header contrast | R05 | a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e | 44998 | UNKNOWN unless a separate build receipt proves it | 2026-10-27T23:23:50+08:00 | header-contrast repair | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R06 structural completion | R06 | 60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6 | 50454 | UNKNOWN unless a separate build receipt proves it | 2026-10-28T10:48:30+08:00 | structural completion | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R07 targeted semantic repair | R07 | 35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd | 52863 | UNKNOWN unless a separate build receipt proves it | 2026-10-28T11:37:42+08:00 | targeted semantic repair | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R07-LF01 layout-only repair | R07-LF01 | ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f | 50156 | UNKNOWN unless a separate build receipt proves it | 2026-10-28T11:46:42+08:00 | remove one empty manual page-break paragraph; non-empty body/table text unchanged | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |
| R08-TR01 targeted repair | content version 1.3/R08; build R08-TR01 | 7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78 | 53207 | UNKNOWN unless a separate build receipt proves it | 2026-10-28T12:03:08+08:00 | targeted repairs for prior F1-F6; no financial figures changed | Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH |

R12 finding: the selected R01→R08 chain is recorded, but R01 bytes and build date remain UNKNOWN. Do not promote the historical R01 hash to a locally verified binary. This sidecar inventory does not change the R08 DOCX bytes.

===== END Candidate lineage chain =====


===== BEGIN Machine-readable candidate lineage | SHA256=c7cb1888f72aeee30b22d84362aa268c95a2ef06d70de244bf05903d1137a682 | BYTES=14524 =====
{
  "schema": "TTQS_ONE_0142_R08_CANDIDATE_LINEAGE_V1",
  "project_id": "TTQS_ONE",
  "doc_id": "0142",
  "requirement_id": "I19-E32",
  "official_checkbox_index": 156,
  "printed_checkbox_serial": "UNKNOWN",
  "candidate_version": "1.3/R08",
  "build_label": "R08-TR01",
  "candidate_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\0142_I19-E32_CANDIDATE_R08_TARGETED_REPAIR_R01.docx",
  "candidate_sha256": "7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78",
  "candidate_bytes": 53207,
  "parent_candidate_sha256": "ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f",
  "parent_build_label": "R07-LF01",
  "parent_lineage_json_sha256": "26649bd598d3f57739dee7e353e51cf181264d446580445462a2f78c27c639bc",
  "parent_layoutfix_lineage_sha256": "f805ee51ee1a4a3b09d78eded51477e59f8a5bacd4ccf8a6e386dccb42a764e5",
  "lineage_annex_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\LINEAGE_CHAIN_0142_R08_TARGETED_REPAIR_R01.md",
  "lineage_annex_sha256": "ef44a720a9857d6455c76a25496bbc4a6fe82eb2b634bc955f8bc28c94bf435c",
  "source_packet_sha256": "e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49",
  "unique_blueprint_sha256": "4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b",
  "official_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
  "selected_chain": [
    {
      "revision": "R01 baseline",
      "candidate_sha256": "59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6",
      "parent_sha256": "—",
      "verification": "Hash recorded in parent lineage; original DOCX bytes not found in searched 0142 source tree, so not independently recomputed."
    },
    {
      "revision": "R03 selected table-cell margin",
      "candidate_sha256": "c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861",
      "parent_sha256": "59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6",
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\0142_I19-E32_R03_TABLE3_CELL_MARGIN_CANDIDATE.docx",
      "bytes": 44984,
      "verification": "Local SHA-256 recomputed."
    },
    {
      "revision": "R04 selected table flow",
      "candidate_sha256": "e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c",
      "parent_sha256": "c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861",
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\0142_I19-E32_R04_TABLE3_FLOW_CANDIDATE.docx",
      "bytes": 44991,
      "verification": "Local SHA-256 recomputed."
    },
    {
      "revision": "R05 header contrast",
      "candidate_sha256": "a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e",
      "parent_sha256": "e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c",
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\0142_I19-E32_R05_HEADER_CONTRAST_CANDIDATE.docx",
      "bytes": 44998,
      "verification": "Local SHA-256 recomputed."
    },
    {
      "revision": "R06 structural completion",
      "candidate_sha256": "60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6",
      "parent_sha256": "a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e",
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\0142_I19-E32_CANDIDATE_R06.docx",
      "bytes": 50454,
      "verification": "Local SHA-256 recomputed; prior semantic review PARTIAL applies only to this exact SHA."
    },
    {
      "revision": "R07 targeted semantic repair",
      "candidate_sha256": "35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd",
      "parent_sha256": "60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6",
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R07_TARGETED_REPAIR_FINAL_20261028\\0142_I19-E32_CANDIDATE_R07.docx",
      "bytes": 52863,
      "verification": "Local SHA-256 recomputed."
    },
    {
      "revision": "R07-LF01 layout-only repair",
      "candidate_sha256": "ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f",
      "parent_sha256": "35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd",
      "bytes": 50156,
      "verification": "Local SHA-256 recomputed; only empty manual page-break paragraph before Section 5 removed; non-empty body/table text unchanged."
    },
    {
      "revision": "R08-TR01 targeted semantic repair",
      "candidate_sha256": "7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78",
      "parent_sha256": "ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f",
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\0142_I19-E32_CANDIDATE_R08_TARGETED_REPAIR_R01.docx",
      "bytes": 53207,
      "verification": "Local SHA-256 recomputed; repairs F1-F6 in the exact parent review."
    }
  ],
  "parent_review": {
    "candidate_sha256": "ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f",
    "verdict": "PARTIAL",
    "actual_provider": "opencode",
    "actual_model": "deepseek-v4.1-flash-free",
    "session_id": "ses_e7f5bb7edffeTU85K8yTYjVT8R",
    "session_outcome": "succeeded",
    "reported_cost": 0,
    "billing_status": "UNKNOWN",
    "response_sha256": "2adc48777fe86b044258b2aa79f00a104d11b734332bfa742f95342750b0f6a9",
    "session_export_sha256": "3089622869d1de32bb4e28e0f203f8b35e3c81d0edab0e505acd9398fefdcae1",
    "dispatch_receipt_sha256": "8d0c062d102a16806d20219e707318f2c480711fb3813a774e2b89970fc780b5"
  },
  "replacement_register_sha256": "b9ef1b7f1c9b703377f0284582cc72c4251d483cbeeae3adf8f6279e6aaa372b",
  "technical_qa": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\TECHNICAL_QA_R08_TARGETED_REPAIR_R01.json",
    "sha256": "474094109308849a9bcfeddb7d94b0c068f93199082b8c72e19e48b81b38b1f1",
    "result": "PASS"
  },
  "word_render": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\WORD_NATIVE_RENDER_RECEIPT_0142_R08_TARGETED_REPAIR_R01.json",
    "sha256": "d2d93a1fd7c8fb54c14da3ff180257ea02547bba60d9b5696c56d6f220eefc0e",
    "pdf_sha256": "718b5807164bec5e1d519f8ac52236f3e45ae17f040edc5b25f76791a4ca6c2e",
    "page_count": 14
  },
  "page_manifest": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\PAGE_IMAGE_MANIFEST_0142_R08_TARGETED_REPAIR_R01.json",
    "sha256": "d5b7ab71332583549b1971f3599dae5cbc712712bc5e697f8f84a0c2ba5a561f",
    "page_count": 14
  },
  "visual_qa": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\VISUAL_QA_R08_TARGETED_REPAIR_R01.json",
    "sha256": "0f08c04c7b9ae98ae3888703f1126537b16c5a37b2d8b74c19219997499530dc",
    "result": "PASS"
  },
  "semantic_state": "PARTIAL_REVIEW_RESPONSE_RECEIVED; F1_LINEAGE_BASELINE_BYTES_UNKNOWN; MODEL_IDENTITY_UNKNOWN; NOT_PROMOTED",
  "real_evidence": "UNKNOWN/HOLD",
  "official_score": "NOT_ASSIGNED",
  "formal_acceptance": "NOT_GRANTED",
  "semantic_review_response": {
    "work_id": "TTQS-0142-I19-E32-AGY-REVIEW-R08-R01",
    "candidate_sha256": "7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78",
    "requested_model": "gemini-3.8-flash-high",
    "actual_model_identity": "UNKNOWN",
    "cli_exit_code": 0,
    "response_verdict": "PASS",
    "response_sha256": "f47a82834d2e41d8cb39dccf671971b63361447ae0fe48de20dd0c8c6107dd2c",
    "scope_adjudication": "PARTIAL: reviewer input was text-only and did not include lineage annex/JSON or companion CSV; F1 claim was not independently supported by its input. Local R12 audit added per-stage metadata, while R01 bytes remain unavailable.",
    "formal_acceptance": "NOT_GRANTED"
  },
  "lineage_audit_r12": {
    "observed_at": "2026-10-28T12:47:44+08:00",
    "stage_inventory": [
      {
        "stage": "R01 baseline",
        "version_or_build_label": "R01 baseline",
        "candidate_sha256": "59f9b500eafd0b283a6df898d337e888da37cb6bcfc98cb180a6fd452b8034a6",
        "bytes": "UNKNOWN",
        "recorded_build_date": "UNKNOWN",
        "filesystem_mtime": "NOT_AVAILABLE",
        "change_type": "baseline candidate; original bytes absent from searched local source tree",
        "verifier": "No original binary; SHA exists only in historical parent lineage; not independently recomputed."
      },
      {
        "stage": "R03 selected table-cell margin",
        "version_or_build_label": "R03",
        "candidate_sha256": "c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861",
        "expected_chain_sha256": "c731c94ec54ea2980564fd580907a291d7bd93a050933e28a3fde7643d15a861",
        "bytes": 44984,
        "recorded_build_date": "UNKNOWN unless a separate build receipt proves it",
        "filesystem_mtime_observed_not_build_date": "2026-10-27T23:19:38+08:00",
        "change_type": "selected table-cell margin repair",
        "verifier": "Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH"
      },
      {
        "stage": "R04 selected table flow",
        "version_or_build_label": "R04",
        "candidate_sha256": "e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c",
        "expected_chain_sha256": "e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c",
        "bytes": 44991,
        "recorded_build_date": "UNKNOWN unless a separate build receipt proves it",
        "filesystem_mtime_observed_not_build_date": "2026-10-27T23:21:38+08:00",
        "change_type": "table-flow repair",
        "verifier": "Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH"
      },
      {
        "stage": "R05 header contrast",
        "version_or_build_label": "R05",
        "candidate_sha256": "a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e",
        "expected_chain_sha256": "a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e",
        "bytes": 44998,
        "recorded_build_date": "UNKNOWN unless a separate build receipt proves it",
        "filesystem_mtime_observed_not_build_date": "2026-10-27T23:23:50+08:00",
        "change_type": "header-contrast repair",
        "verifier": "Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH"
      },
      {
        "stage": "R06 structural completion",
        "version_or_build_label": "R06",
        "candidate_sha256": "60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6",
        "expected_chain_sha256": "60563d4a56ac4502e522feb2665edef07771824ab4c2b2fb596862bb0e84f0e6",
        "bytes": 50454,
        "recorded_build_date": "UNKNOWN unless a separate build receipt proves it",
        "filesystem_mtime_observed_not_build_date": "2026-10-28T10:48:30+08:00",
        "change_type": "structural completion",
        "verifier": "Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH"
      },
      {
        "stage": "R07 targeted semantic repair",
        "version_or_build_label": "R07",
        "candidate_sha256": "35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd",
        "expected_chain_sha256": "35f7e3c42d599a3c123786c997a4e4ee010e6b623d6cf93a919469fd59a044cd",
        "bytes": 52863,
        "recorded_build_date": "UNKNOWN unless a separate build receipt proves it",
        "filesystem_mtime_observed_not_build_date": "2026-10-28T11:37:42+08:00",
        "change_type": "targeted semantic repair",
        "verifier": "Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH"
      },
      {
        "stage": "R07-LF01 layout-only repair",
        "version_or_build_label": "R07-LF01",
        "candidate_sha256": "ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f",
        "expected_chain_sha256": "ac6f2820027a206a6cd3db284d923f4bad22d11d52ef8afb1e59d6ce4d19684f",
        "bytes": 50156,
        "recorded_build_date": "UNKNOWN unless a separate build receipt proves it",
        "filesystem_mtime_observed_not_build_date": "2026-10-28T11:46:42+08:00",
        "change_type": "remove one empty manual page-break paragraph; non-empty body/table text unchanged",
        "verifier": "Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH"
      },
      {
        "stage": "R08-TR01 targeted repair",
        "version_or_build_label": "content version 1.3/R08; build R08-TR01",
        "candidate_sha256": "7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78",
        "expected_chain_sha256": "7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78",
        "bytes": 53207,
        "recorded_build_date": "UNKNOWN unless a separate build receipt proves it",
        "filesystem_mtime_observed_not_build_date": "2026-10-28T12:03:08+08:00",
        "change_type": "targeted repairs for prior F1-F6; no financial figures changed",
        "verifier": "Windows-local SHA-256 recomputed 2026-10-28T12:47:44+08:00; MATCH"
      }
    ],
    "R01_original_bytes": "NOT_FOUND_IN_SEARCHED_SOURCE_TREE",
    "docx_candidate_sha256_unchanged": "7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78"
  }
}

===== END Machine-readable candidate lineage =====


===== BEGIN Deterministic technical QA receipt | SHA256=474094109308849a9bcfeddb7d94b0c068f93199082b8c72e19e48b81b38b1f1 | BYTES=2775 =====
{
  "schema": "TTQS_ONE_0142_R08_TARGETED_REPAIR_TECHNICAL_QA_V1",
  "doc_id": "0142",
  "requirement_id": "I19-E32",
  "official_checkbox_index": 156,
  "candidate_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\0142_I19-E32_CANDIDATE_R08_TARGETED_REPAIR_R01.docx",
  "candidate_sha256": "7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78",
  "candidate_bytes": 53207,
  "register_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0142_I19-E32_SOURCE_PREP_R01_20261025\\R06_STRUCTURAL_COMPLETION_R12_20261028\\R06_REVIEW\\R08_TARGETED_REPAIR_R01_20261028\\SAMPLE_REPLACEMENT_REGISTER_0142_R08.csv",
  "register_sha256": "b9ef1b7f1c9b703377f0284582cc72c4251d483cbeeae3adf8f6279e6aaa372b",
  "register_rows": 19,
  "source_packet_sha256": "e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49",
  "unique_blueprint_sha256": "4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b",
  "official_requirement_row_sha256": "b6abdafe457e7aa9353a963bb8606bdecf21e92d289878cf80bfc1885d5c4033",
  "crosswalk_row_sha256": "e060fd313fc5c553f9f53e6ac246ab12d7ac83d728a7918a3dfd65b448af5891",
  "checks": {
    "docx_zip_integrity": true,
    "document_identity": true,
    "official_source_identity": true,
    "source_packet_blueprint_present": true,
    "candidate_version_build_label": true,
    "sample_real_acceptance_states": true,
    "negative_neighbors_and_rounding": true,
    "replacement_workflow_preserves_sample": true,
    "table_count_16": true,
    "table12_separate_labels_and_basis": true,
    "table12_rows_disclose_sample_basis_and_roles": true,
    "table15_dates_split_sample_real": true,
    "table16_derived_dates_and_f19_version": true,
    "register_19_rows_and_ids": true,
    "f15_locator_corrected": true,
    "recalculation_dates_only_derived_rows": true,
    "f19_register_matches_document": true,
    "register_real_states_held": true,
    "no_uncontrolled_placeholders": true,
    "sample_math": true,
    "body_font_floor_10_5": true,
    "table_font_floor_9_5": true,
    "source_hashes_expected": true
  },
  "body_font_min_pt": 10.5,
  "table_font_min_pt": 9.5,
  "font_issues": [],
  "issues": [],
  "result": "PASS",
  "scope": "Deterministic OOXML integrity, official mapping, version/control fields, register alignment, arithmetic, SAMPLE/REAL controls and font floors; no semantic acceptance or visual acceptance.",
  "formal_acceptance": "NOT_GRANTED",
  "real_evidence": "UNKNOWN/HOLD",
  "official_score": "NOT_ASSIGNED",
  "checked_local": "2026-10-28T12:04:38.383107+08:00"
}

===== END Deterministic technical QA receipt =====


===== BEGIN Word-native visual QA receipt (scope context only) | SHA256=0f08c04c7b9ae98ae3888703f1126537b16c5a37b2d8b74c19219997499530dc | BYTES=1709 =====
{
  "schema": "TTQS_ONE_0142_R08_VISUAL_QA_V1",
  "doc_id": "0142",
  "requirement_id": "I19-E32",
  "candidate_sha256": "7efc848ed18decf665c423c03d4784e681a5d911ae5185885f614b391d92cc78",
  "renderer": "Microsoft Word COM to PDF; Poppler 150 dpi page images",
  "pdf_sha256": "718b5807164bec5e1d519f8ac52236f3e45ae17f040edc5b25f76791a4ca6c2e",
  "page_count": 14,
  "pages_inspected": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14
  ],
  "inspection_method": "All 14 page PNGs opened at original image resolution in the current review session.",
  "checks": {
    "all_pages_present": true,
    "no_clipping_or_overlap": true,
    "no_missing_glyphs": true,
    "tables_readable_and_headers_repeat": true,
    "table_rows_not_cut": true,
    "sample_real_headers_and_footers_consistent": true,
    "repaired_table12_roles_basis_and_dates_readable": true,
    "repaired_table15_and_table16_dates_readable": true,
    "page5_section5_begins_without_blank_orphan": true
  },
  "observations": [
    "Page 8-9 Table 12 continues with its header repeated; rows remain readable and are not clipped.",
    "Page 10 has whitespace after Table 14 naturally splits; no orphaned table row or clipped text.",
    "Page 14 ends after the final F19 control-metadata row; SAMPLE/REAL status remains explicit.",
    "The prior R07 nearly blank page-5 break is absent; page 5 begins Section 5."
  ],
  "result": "PASS",
  "inspector": "Codex visual review of the page images in this task",
  "formal_acceptance": "NOT_GRANTED",
  "real_evidence": "UNKNOWN/HOLD",
  "checked_local": "2026-10-28T12:07:19.902209+08:00"
}

===== END Word-native visual QA receipt (scope context only) =====
