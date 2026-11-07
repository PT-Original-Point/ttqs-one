# TTQS ONE independent semantic review — bounded exact-SHA task

Review only the candidate content and mappings in this packet. Do not edit files, invoke tools, use Computer Use, infer formal acceptance, or claim visual checks beyond the attached visual receipt. Candidate: doc_id 0007, official requirement I01-E04, revision R12. DOCX SHA-256: 7e7509a2687396c4fa32a5bd8d8bf89691d8fb250026c96067eed74173f67f76. Extracted DOCX body SHA-256: 904a472cb4a3ff3d642a139c0ab10d4597902c94b0dd3e969987c90e2331877e. Requested model route: opencode/glm-5.3-flash-free; actual serving model must be reported only if provider/session evidence establishes it, otherwise UNKNOWN.

Return PASS, PARTIAL, or FAIL. Give exact paragraph/table/row locators for each finding and explicitly say whether each prior defect is closed. Check: official wording and unique Blueprint fit; correct analysis-report genre and title-blind purpose; usable small-association training context; complete distinct content; all source fields Q3_NEED1–3, Q4_URG, Q5_CONF, Q7_MODE, Q9_DURATION, Q10_BARRIER trace to facts F0002–F0009; formula facts F0101–F0114 are directly locatable; score weights, denominators, 4.50/4.10/3.65, 4/5 HOLD, 6/10 to 8/10, 90% gap, and 33.33% improvement recompute; each synthetic fact is in the register; SAMPLE/REAL boundary and neighboring requirements 0006/I01-E03 and 0008/I01-E05 are not conflated; no association approval, actual execution, or third-party evidence is fabricated; actionable conclusions and hold/reject triggers are clear. Do not accept builder claims as review findings. If content is missing or inconsistent, state the minimum repair and no more.

## Source packet and Unique Blueprint
{
  "source": "CONTROL/BLUEPRINT_CURRENT.jsonl",
  "blueprint_sha256": "406d0495365d0970dcf8113a42842663b8a54372a4e204cc492b7c3f8156ef3e",
  "blueprint_row_sha256": "4f7f55577ae42d0988e02e2112d73514dda173cb6232690a95d2149ac1851980",
  "official_source": "SOURCES/TTQS查核佐證文件資料表-訓練機構版 (2).pdf",
  "official_source_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
  "blueprint": {
    "deliverable_id": "0007",
    "requirement_id": "I01-E04",
    "final_filename": "0007__課程產品及流程檢討分析報告.docx",
    "document_genre": "分析／評估報告｜課程產品及流程檢討分析報告",
    "document_purpose": "本件專屬焦點：課程產品及流程檢討分析報告；需直接回應的官方佐證要求為：課程產品及流程的檢討分析。；產出一份可實際執行、可閱讀並可追溯的專屬成品；本分件職責與同要求其他分件清楚分開。",
    "primary_user_or_reader": "供主管與決策者讀取資料、理解計算、判斷差距並採取具體決策。",
    "evidence_role": "呈現方法、完整合成或已驗證結果、分析、限制及可追溯決策；不得冒充實績。 本文件只擁有 I01-E04 的直接紀錄／分析口徑；不得吞併其他要求的事實。",
    "source_of_truth": "官方查核佐證表精確原文『課程產品及流程的檢討分析。』，表內頁次 1，讀取狀態 PDF_TEXT_EXACT_PAGE_MATCH；REQ_157_MAP 對應 I01-E04；本行文件名稱與 ID 以 R04 142 交付 crosswalk/seed 為準。Phase2 歷史 Blueprint 僅作需求拆解參考，絕非可複製正文或現行標題權威。",
    "official_requirement_text": "課程產品及流程的檢討分析。",
    "official_checkbox_text": "課程產品及流程的檢討分析。",
    "official_evidence_table_page": "1",
    "official_source_readback_status": "PDF_TEXT_EXACT_PAGE_MATCH",
    "required_sections": "摘要、用途與決策問題；官方要求及分析範圍；資料來源、樣本與納入排除；指標定義、分母與計算方法；完整示範資料及逐步計算；分群／趨勢／差異結果；圖表解讀及品質限制；發現、原因與證據強度；結論與可執行建議；責任人、期限與追蹤指標；合成資料聲明及真實替換清單；附件索引、覆核與版本",
    "required_tables_or_figures": "資料欄位—定義—分母—來源—限制字典；合成明細／彙總結果與逐步計算；分群比較／差距優先排序矩陣；結論—證據—建議—責任—追蹤指標表；官方要求—結果—證據位置—覆核追溯表",
    "required_fields_or_questions": "資料是否足以支持結論？；差距來自需求、設計、執行或追蹤哪一段？；下一期用什麼指標驗證改善？；本文件中哪一段/哪一表直接證明：「課程產品及流程的檢討分析。」？；分析母數及排除說明；計算口徑與四捨五入；建議決策及適用限制；合成事實替換登錄鍵",
    "required_calculations_or_analysis": "差距=實績-目標；改善率=(改善後-改善前)/改善前。不得稱為組織實績。",
    "required_cross_references": "同要求分件 無；相鄰要求 I01-E03, I01-E05；共用原始來源時只引用核實結果，不複製別份文件正文。",
    "real_data_required": "升格為 REAL 前逐項取得可核實來源：正式日期；真實人名/角色；核准/簽章；真實班次/課程；實際數字/比例；真實附件與檔案位置。在無原件時標示 SAMPLE/SYNTHETIC；合成事實須登錄 replacement register，不得宣稱機構實績。",
    "third_party_evidence_required": "若結論依賴外部機關／第三方／真人正式簽章或證書，必須由合法來源取得可核對原件；本文件可提供清楚索引與合成流程示範，絕不代製、仿簽、補作或冒充第三方正式原件。",
    "prohibited_fabrication": "不得把擬真工作稿標成REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果或不存在的外部事實。；不得將舊檔內容、示範數據、未查證Drive候選或歷史草案標成 REAL；不得偽造核准、簽章、真人參與、辦訓、成績、成果、外部證據或來源定位。",
    "title_blind_test": "遮蔽本件標題、檔名與編號，只讀正文應可由專屬機制辨認為『課程產品及流程檢討分析報告』並證明『課程產品及流程的檢討分析。』；若可無修改移作其他要求即失敗。",
    "negative_choice_neighbors": "0006《業務發展計畫與人力資源訓練規劃》（I01-E03）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。\n0008《各類別訓練課程年度成長計畫》（I01-E05）：應證明不同工作物；本件不得代替、合併或複製其專屬事實。",
    "acceptance_tests": "移除標題及檔名後，讀者可由正文專屬欄位、操作或分析辨認為『課程產品及流程檢討分析報告』，且能指出直接回應『課程產品及流程的檢討分析。』的頁節／表格。\n逐項呈現官方要求、資料來源、記錄欄位、判定、證據定位及覆核；官方原文不被歷史草案改寫。\n依本文件文類實際可用：問卷含題目選項量尺；SOP含角色、輸入、判斷、控制點、異常和輸出；會議紀錄含議題、證據、決議、責任、期限；報告含資料、分母、公式、逐步計算、限制和決策。\n若沒有可驗證 REAL 資料，提供前後一致、完整填入的 SAMPLE/SYNTHETIC 案例；不得用空表、待填、待核或未來式充當完成品。\n每一項合成日期、角色、數字、比例、金額、決議、來源路徑與結果皆有逐事實替換簿記錄鍵、所在文件／頁表／欄位及真實替換方式。\n絕不偽造第三方原件、真人簽名、核准、出席、證書、政府、銀行、會計或外部機構事實；需要該等原件時只說明所需原件與取得路徑。\n所有公式可由展示數據重算；分母、單位、期間、四捨五入及N/A條件清楚，交叉引用不重複創造相異版本。\n對照負向鄰項，正文可拒絕至少兩個錯誤近鄰；指出可核對的差異欄位或章節。\n首頁30秒內說明目的、讀者、使用時點、操作、輸出和SAMPLE／REAL狀態；無評核工程內部術語。\n正文可供日常協會作業及評核閱讀；標題層級、欄位、步驟、表格能直接執行，無複製同儕 DOCX 正文。\n字體下限：正文至少10.5pt、表格至少9.5pt；資訊不足時加頁，不縮小字體。\n來源定位與交叉引用使用本 Blueprint 登錄的官方頁次／文件 ID；所有結論不超出來源支持範圍。",
    "synthetic_population_rule": "缺 REAL 即生成完整連貫 SAMPLE/SYNTHETIC worked example；事實粒度一筆一列登錄 SYNTHETIC_REPLACEMENT_REGISTER，含值、類型、定位、替換原件與責任；不得留待填或冒充 REAL。",
    "document_role": "analysis_report"
  },
  "repair_delta": {
    "synthetic_only": true,
    "from_revision": "R11",
    "register_rows_added": 0,
    "formula_or_score_values_changed": false,
    "previous_r11_candidate_sha256": "d9eeb4cf7f9168c46af12c535bd92fe77f067ff1eda5fb57ac290eefe73ba052",
    "register_values_changed": false,
    "to_revision": "R12",
    "reason": "Remove stale body claim that visual QA was not performed; no analytical values, source mappings, facts, formulas, or register rows changed."
  },
  "repair_history": [
    {
      "from_revision": "R04",
      "to_revision": "R05",
      "reason": "Independent semantic review found the Unique Blueprint required difference and improvement-rate formulas were absent.",
      "added_analysis": "§4.4; gap=actual−target; improvement rate=(after−before)/before; full synthetic 6/10→8/10 example, 90% target, units, N/A/HOLD rules.",
      "replacement_register_rows_added": 14,
      "synthetic_only": true,
      "unchanged_prior_candidate_sha256": "6c8c81e5f5381ed52e32f7fadc7f264a9543d8844e9ad06cc73e3c2a17e1dd51"
    },
    {
      "from_revision": "R05",
      "to_revision": "R06",
      "reason": "Independent exact-SHA review found missing gap priority matrix, source field dictionary, item-level checklist traceability, and rounding rule.",
      "new_fact_rows": 33,
      "synthetic_only": true
    },
    {
      "from_revision": "R06",
      "to_revision": "R07",
      "reason": "Deterministic QA found F0145-F0147 register cross-reference missing from body; additionally corrected table-count expectation from 11 to actual 10."
    },
    {
      "from_revision": "R07",
      "to_revision": "R08",
      "reason": "Word visual inspection found §5 heading and explanation stranded on portrait page 6 before the wide landscape priority matrix on page 7. Move the contiguous preamble with its wide table; no analysis, facts, or formulas changed.",
      "synthetic_only": true
    },
    {
      "from_revision": "R08",
      "to_revision": "R09",
      "reason": "Independent review found Q3_NEED1/Q3_NEED2 body locators absent and two table headers stranded at page ends. Added explicit source crosswalk rows and moved the analysis-field table plus §8 heading/table to clean page starts.",
      "synthetic_only": true
    },
    {
      "from_revision": "R09",
      "to_revision": "R10",
      "reason": "Full-page visual inspection found the §4.1 criteria-table header alone at the bottom of page 3, with rows on page 4. Move §4 weighted-comparison section to a new page; no analytic values, synthetic facts, or formulas changed.",
      "synthetic_only": true
    },
    {
      "from_revision": "R10",
      "to_revision": "R11",
      "reason": "Added direct §2 source-field crosswalk F0004-F0009 and §4.4 formula-fact crosswalk F0101-F0114 after independent semantic review; no values, denominators, scores, synthetic register rows, or formulas changed.",
      "new_fact_rows": 0,
      "synthetic_only": true,
      "unchanged_prior_candidate_sha256": "fa8273b2cb5270f7e00bc2315981e3017254b5b8c0054387ee53eb091f94bfd3"
    },
    {
      "new_fact_rows": 0,
      "previous_candidate_sha256": "d9eeb4cf7f9168c46af12c535bd92fe77f067ff1eda5fb57ac290eefe73ba052",
      "synthetic_only": true,
      "to_revision": "R12",
      "reason": "Removed stale visual-QA status claim from evaluator-facing body; no analysis, facts, formulas, or register values changed.",
      "from_revision": "R11"
    }
  ],
  "previous_r11_candidate_sha256": "d9eeb4cf7f9168c46af12c535bd92fe77f067ff1eda5fb57ac290eefe73ba052"
}


## Exact candidate body extracted from R12 DOCX
P001: 課程產品及流程檢討分析報告｜候選 R12
P002: 文件編號 0007  |  官方要求 I01-E04  |  版本 R12  |  候選文件  |  SAMPLE / SYNTHETIC
P003: doc_id 0007｜I01-E04｜分析／評估報告 狀態：DOCX_CANDIDATE_R12；以下均為 SAMPLE／SYNTHETIC；未經原始點協會正式接受。 情境界線： 以志工關懷協會可能採用的課程與流程作方法示例，不描述任何特定協會的實際課程、志工、服務、決定或績效。
P004: 30 秒使用指引
P005: 第 1 節界定官方要求；第 2 節說明來源限制；第 3–4 節比較三種課程設計並重算分數；第 6 節提供已填妥的生命週期檢核表。演練事實以 F 鍵連至同一候選證據包中的 SYNTHETIC_REPLACEMENT_REGISTER_0007_R12.csv。方案 A 只在這組合成評分下領先；設計檢核仍為 4/5，須維持 HOLD，不代表協會選定或核准。
P006: 第 4.4 節示範 Blueprint 指定的差距與改善率公式，列出分母、單位、逐步算式、N/A 條件及 HOLD 規則；範例為 SAMPLE／SYNTHETIC，不代表協會實績。
P007: 摘要
P008: 官方要求：「課程產品及流程的檢討分析。」（官方表第 1 頁）。本例以 0003 的一筆合成回覆作受限訊號，依同一組五項準則比較三種產品／流程方案。加權總分：A 4.50/5（F0034）、B 4.10/5（F0035）、C 3.65/5（F0036）。分數是合成分析，不是調查結果、課程實績或決議。A 的設計完整度 4/5=80%（F0044），低於本例 5/5=100%（F0045）門檻；樣例結論為 HOLD（F0046），補齊紀錄與回饋責任設計後才可供有權者審議。
P009: 1. 官方要求、問題與範圍
P010: 官方《TTQS 人才發展品質管理系統【查核佐證文件資料表】-訓練機構版》第 1 頁列有：「課程產品及流程的檢討分析。」本報告回答：在明確標為合成的志工關懷情境中，哪些課程產品較貼近可用示例訊號？設計與生命週期有哪些可查控制點，尚缺哪些證據？
P011: 範圍： 產品方案比較、流程設計檢核、算式、限制、修正與追蹤。不在範圍： 實際開課、真實招生或成效、群體需求比例、個案服務、機構整體績效、年度成長承諾、醫療／治療判斷或正式核定。沒有真實課程執行原件。
P012: 2. 資料來源、樣本及方法
P013: 本報告使用一筆 0003 合成回覆作為情境輸入，並比較三個假設課程方案；它不是協會實際問卷、開班紀錄或績效資料。下表逐欄界定計算口徑及資料邊界，所有引用值均可回到合成清冊的 fact_id。
P016: 樣本納入一筆合成情境及三個同口徑方案；排除真實學員、班次、成本、授課、出席、回饋、改善或核准資料。所有分數、比例與判斷均為 SAMPLE／SYNTHETIC。方法是逐項回到 fact_id 重算、比較差距並標示限制；缺少真實來源時不得轉列 REAL。
P017: 3. 三個不同產品／流程方案
P018: 方案均為新寫的假設概念，不是協會既有課程。
P021: 4. 加權比較
P022: 4.1 準則、錨點及公式
P024: 評分錨點（F0018）：1＝明顯不合；3＝部分符合但需補設計；5＝概念直接符合且可設計可觀察練習；2、4 介於相鄰錨點。權重合計 100%（F0064）。
P025: 共同比較假設：三方案採相同規劃時段：面對面、單次 3 小時；這兩項只沿用 0003 的合成答覆（F0007、F0008），並非協會實際班次（F0097）。為便於同尺度比較，假設三方案面對同一個人數未指定的志工小組及同一個尚未核實的場地；兩者都不是協會現況（F0098）。不假設帶領人力或設備已可用；實際配置維持 UNKNOWN（F0099）。因此 25% 可行性分數只比較共同 SAMPLE 框架下的相對準備量與練習設計，不代表協會已有資源、場地或排課能力；真實條件不同時須取得來源後重評（F0100）。
P026: 4.2 每格評分與理由
P028: 4.3 逐步重算
P029: A（F0034）＝(30×5＋25×4＋20×5＋15×4＋10×4)÷100＝(150＋100＋100＋60＋40)÷100＝4.50。
P030: B（F0035）＝(30×4＋25×4＋20×5＋15×4＋10×3)÷100＝(120＋100＋100＋60＋30)÷100＝4.10。
P031: C（F0036）＝(30×3＋25×4＋20×5＋15×3＋10×3)÷100＝(90＋100＋100＋45＋30)÷100＝3.65。
P032: A−B＝4.50−4.10＝0.40 分（F0037）；A−C＝4.50−3.65＝0.85 分（F0038）。差值只描述這張表的合成評分。
P033: 4.4 指標差距與改善率：完整 SAMPLE／SYNTHETIC 算例
P034: 以下十項是為說明檢核口徑而設計的合成清單，並非原始點協會已執行的查核。每項只有在條件完整且有同範圍的記錄定位時才算完成；本例 locator 是合成鍵，不是真實原件。T0 與 T1 沿用同一項目、同一條件及分母 10。
P035: 指標與事實鍵對照：本項完整率＝同一十項清單中完成且有定位的項目數÷10（F0101），T0、T1 使用相同十項與分母 10（F0102），本例目標 90%（F0103）。T0 為 6/10＝60%（F0104、F0105）；T1 為 8/10＝80%（F0106、F0107）。差距分別為 −30.00 與 −10.00 個百分點（F0108、F0109）；相對改善率為 33.33%，絕對變化為 +20.00 個百分點（F0110、F0111）。因 T1 低於 SAMPLE 目標，維持 SAMPLE／HOLD（F0112）；改善前為零時相對改善率標 N/A（F0113）；兩期清單、條件、分母或單位不同時先 HOLD 並重設可比基準（F0114）。本段所有數值均為 SAMPLE／SYNTHETIC，不代表協會實績。
P037: 本例目標值為 90%（F0103）。依「差距＝實績－目標」：T0 為 60%－90%＝−30.00 個百分點；T1 為 80%－90%＝−10.00 個百分點。T0/T1 僅第3與第8項由未完成轉為完成，故完整數由 6 增至 8；第6、第10項仍未完成，與 §5 差距排序完全一致。
P038: 相對改善率＝（改善後－改善前）÷改善前＝（80%－60%）÷60%＝33.333…%＝33.33%；絕對變化＝80%－60%＝+20.00 個百分點。計算時保留原始分子、分母及未四捨五入比率；不以已四捨五入的中間值再計算。最後呈現的比率與百分點差距均四捨五入至小數第二位，採一般四捨五入（第三位小於5捨去，5以上進位）。這個規則只控制呈現精度，不改變判定。
P039: T1 80% 仍低於 90% SAMPLE 目標，結論維持 SAMPLE／HOLD，不得寫成達標、改善已獲核准或協會實績。改善前為零時相對改善率標 N/A，只列原始計數與絕對變化；T0/T1 的清單、條件、母數或單位不同時先 HOLD、重新建立可比基準；任何真實來源未提供時維持 SAMPLE／UNKNOWN。全部十項定義、各期狀態與限制均在替換清冊 F0115–F0144 登錄。
P041: 5. 發現及證據強度
P042: 5.1 合成算例的差距優先矩陣
P043: 排序原則先處理課程發布前的師資資格佐證與適任性可追溯問題，再處理課後追蹤的責任與時點；本排序是本例的 SAMPLE 風險判斷，不是協會正式決議或核准，排序方法與限制登錄於 F0147。兩項均為 T1 未完成，整體結論仍 HOLD。
P046: 上述角色、風險及建議均屬合成工作範例；不代表協會已指派人員、核准師資、執行課程或形成決議。優先次序可在取得真實來源後依據風險與法定／契約條件重評，變更須保留理由與來源。
P047: 在這組假設評分下，A 最高，因同時納入流程／紀錄練習及交接界線；B、C 分別聚焦溝通／轉介及志工合作／安全。排序差距是評分算術，不是需求比例或效益差異。
P048: 官方要求及 Blueprint 支持來源身分；0003／0004 只是候選材料中的 SAMPLE/SYNTHETIC；選項、評分與檢核是本稿合成分析。沒有真實課綱、教材、授課、出席、練習、回饋、事件或修訂紀錄，不能判定既有課程品質或成效，也不能說協會已完成檢討。
P049: 6. 課程生命週期：已填 SAMPLE 檢核表
P050: 本報告差距與改善率公式及完整演算見 §4.4；下表的五項設計完整度另以 4／5 計算，兩者是不同指標，不可合併分母。無實際開課、授課、回饋或修訂原件時，相關執行結果維持 N/A／UNKNOWN。
P051: 以下是方案 A 的合成桌面檢核，不是機構正式表單、實際課程檔案或已完成活動紀錄。每列均有結果或具理由的 N/A。
P053: N/A 表示沒有可觀測證據，不是零分或沒有問題；未觀測階段不計入完成課程或成效。
P054: 7. 結論、HOLD／REJECT 及修正責任
P055: 7.1 僅供審議的 SAMPLE 建議
P056: A 是本組合成評分中的最高分，只可作「補齊設計後供有權者評估是否試行」的樣例建議（F0081）。設計完整度 4/5，未達 5/5，故維持 HOLD（F0046）。高分不等於選定、核准、排課或實施；本文沒有決議、真人姓名、簽章或授權紀錄。
P057: 7.2 樣例控制行動表
P058: 本表的師資資格與課後追蹤優先次序，須與 §5.1 的 P1／P2 差距矩陣一致；只在合成情境下示範，不構成正式分派或核准。
P060: PC＝規劃協調；IN＝課程設計／帶領；ER＝紀錄／品質覆核；AUTH＝有權決策角色（F0054–F0057）。這些代碼不代表已任命真人或授權；本報告不替任何人核准。
P062: 8. 跨文件責任及負向近鄰
P064: 標題盲辨識： 遮蔽標題及檔名後，正文仍以產品方案、生命週期檢核、加權比較、證據限制及修正閉環直接辨識為課程產品／流程分析（第 1、3–7 節），不會被誤認為問卷、樣本執行、業務計畫或年度成長計畫（F0063）。
P065: 9. 真實替換與使用限制
P066: 同一候選證據包中的 SYNTHETIC_REPLACEMENT_REGISTER_0007_R12.csv 是本候選專屬逐事實清冊：每列一個值、唯一鍵、精確章節／表格／欄位定位、生成或引用方式、需取得的真實原件、替換／覆核法及 SAMPLE_SYNTHETIC_ONLY 狀態；不代表更新中央共享登錄。
P067: 升格為 REAL 前，逐項取得合法可核對的實際課程版本、核定目的與對象、執行流程、角色權限、課程材料、出席／練習、回饋原件、改善前後版本、日期及決定紀錄。來源缺失或無法定位時保留 SAMPLE／UNKNOWN，不以候選來源包或本稿數字填補實績。
P068: 10. 官方要求—結果—位置—覆核

TABLE 01
分析欄位 | 定義與單位／分母 | 本例來源及定位 | 納入／排除規則 | 限制及可支持的結論
0003 情境輸入（總體） | 一筆完整合成回覆；逐項 fact 值是描述性類別或序位評分，沒有抽樣母數可推論母體 | 0003 SYNTHETIC replacement register F0001–F0009；本例只引用，不複製問卷 | 僅納入該筆標示為 SAMPLE 的情境欄位；排除真人樣本、機構比率、外部統計及實際服務結果 | 只能建立示範限制與方案情境；不得稱為需求調查結果或協會現況
0003 欄位 Q3_NEED1：服務流程與紀錄 | 單筆合成類別訊號；無母體推論分母，不計比例 | 0003 清冊 SYN-005（field=Q3_NEED1）；本件清冊 F0002 | 僅引用該筆 SAMPLE 情境輸入；排除真人樣本、機構比例、外部統計及實際服務結果 | 僅供三方案設計情境；不代表協會實際提供或執行該服務
0003 欄位 Q3_NEED2：溝通與轉介界線 | 單筆合成類別訊號；無母體推論分母，不計比例 | 0003 清冊 SYN-006（field=Q3_NEED2）；本件清冊 F0003 | 僅引用該筆 SAMPLE 情境輸入；排除真人樣本、機構比例、外部統計及實際服務結果 | 僅供三方案設計情境；不代表協會實際提供轉介或已執行服務
0003 欄位 Q3_NEED3：志工合作與安全 | 單筆合成類別訊號；無母體推論分母，不計比例 | 0003 清冊 SYN-007（field=Q3_NEED3）；本件清冊 F0004 | 僅引用該筆 SAMPLE 情境輸入；排除真人樣本、機構比例、外部統計及實際服務結果 | 僅供三方案設計情境；不代表協會實際提供或執行該服務
0003 欄位 Q4_URG：急迫度 | 單筆合成序位評分 4/5；不代表母體平均或實際需求程度 | 0003 清冊 SYN-008（field=Q4_URG）；本件清冊 F0005 | 僅引用該筆 SAMPLE 情境輸入；排除真人樣本、機構比例及外部統計 | 僅供三方案設計情境；不得推論協會需求或實際服務
0003 欄位 Q5_CONF：自信程度 | 單筆合成序位評分 2/5；不代表母體平均或課程成效 | 0003 清冊 SYN-009（field=Q5_CONF）；本件清冊 F0006 | 僅引用該筆 SAMPLE 情境輸入；排除真人樣本、機構比例及外部統計 | 僅供三方案設計情境；不得推論真實信心或訓練成效
0003 欄位 Q7_MODE：偏好方式 | 單筆合成類別選擇：面授；無母體推論分母，不計比例 | 0003 清冊 SYN-010（field=Q7_MODE）；本件清冊 F0007 | 僅引用該筆 SAMPLE 情境輸入；不外推至其他志工或班次 | 僅供三方案設計情境；不得宣稱協會已排課
0003 欄位 Q9_DURATION：偏好時長 | 單筆合成回答：單次 3 小時；不代表實際授課時數 | 0003 清冊 SYN-011（field=Q9_DURATION）；本件清冊 F0008 | 僅引用該筆 SAMPLE 情境輸入；排除實際班次、出席與授課紀錄 | 僅供三方案設計情境；不得宣稱協會已授課
0003 欄位 Q10_BARRIER：參與障礙 | 單筆合成類別訊號：交通距離／時間；無母體推論分母，不計比例 | 0003 清冊 SYN-012（field=Q10_BARRIER）；本件清冊 F0009 | 僅引用該筆 SAMPLE 情境輸入；排除真人出席、地點及交通資料 | 僅供三方案設計情境；不得推論實際參與障礙
方案加權分數 | 每項準則以 1–5 分評分；加權總分＝Σ（權重百分比×評分）÷100；單位為 5 分制分數，分母為總權重 100 | 準則與權重 F0013–F0018；方案逐項分數 F0019–F0033；總分 A/B/C 為 F0034–F0036；重算見 §4.3 | 三方案採同一五準則、同一權重與同一 1–5 量尺；不得混入未定義成本、實際成效或機構資源 | 分數只比較此合成方案；不能證明成本效益、真實可行性或方案已獲選
方案間分差 | 方案分數相減，單位為 5 分制分數差，不設比例分母 | A−B 與 A−C 分別為 F0037、F0038；§4.3 | 只比較同一量尺的加權總分；不把分差當百分比或效益值 | 反映排序距離，不代表統計顯著或實際成效差
五項設計完整度 | 完成且可追溯的設計欄位數 ÷ 5 ×100%；單位為百分比，分母固定 5 | 五項內容及 4/5 結果 F0039–F0045；§6 檢核表 | 僅限需求、目標、練習、界線、紀錄／回饋五項；未完成項按未完成計 | 4/5=80% 未達 5/5=100% 門檻，支持 SAMPLE/HOLD；與十項流程檢核是不同構念
十項流程檢核完整率 | 符合逐項通過準則的檢核數 ÷ 固定 10 項 ×100%；單位為百分比，分母固定 10 | 項目定義 F0115–F0124；T0 狀態 F0125–F0134；T1 狀態 F0135–F0144；§4.4 明細表 | T0、T1 必須用相同十項清單、條件及範圍；沒有記錄 locator 即視為未完成 | 本例為無日期合成演練；不能推論協會流程已改善或實際執行
差距 | 差距＝實績－目標；百分比指標的差距以百分點表示，不另設除數 | 目標 F0103、T0/T1 比率 F0105/F0107、差距 F0108/F0109；§4.4 | 只比較同指標、同分母、同單位和同範圍；分母或規則改變即 HOLD | 負值代表低於目標；不得將百分點差距稱為百分比改善
相對改善率／絕對變化 | 相對改善率＝（改善後－改善前）÷改善前；絕對變化＝改善後－改善前。前者為相對比例，後者以百分點表示 | F0110–F0111；§4.4 | 僅在改善前非零且 T0/T1 可比時計算；零基準標 N/A，不同口徑標 HOLD | 33.33% 是此合成算例的相對變化；不等於達標、因果效果或真實績效

TABLE 02
代碼 | SAMPLE 課程產品與流程 | 練習及可觀察輸出 | 界線
A（F0010） | 服務前確認（F0010）、過程紀錄（F0073）、結束交接（F0074） | 虛構情境中用清單練習確認、記錄、交接；同儕按清單回饋 | 不作診斷、治療或個案處置；超出志工角色即停止並依實際制度轉介
B（F0011） | 溝通（F0011）、傾聽（F0075）及轉介界線（F0076） | 不含真人個案資料的情境演練，辨識澄清、停止承諾及轉交有權角色 | 不承諾結果、不聲稱已有轉介服務
C（F0012） | 志工合作（F0012）、分工（F0077）、集合確認（F0078）、異常通報（F0079）及結束檢點（F0080） | 桌上演練分工、集合確認、異常通報及結束檢點 | 不描述真實活動／事故，不創設機構規章或外部認證

TABLE 03
準則 | 權重 | 評量焦點
對應示例訊號（F0013） | 30% | 方案目的與有限示例訊號的直接連結
小型志工團隊可行性（F0014） | 25% | 準備量及小組練習是否精簡；真實人力仍須核實
角色界線與安全（F0015） | 20% | 是否避免越權承諾或專業處置
可觀察練習與回饋（F0016） | 15% | 是否可觀察學習行為並留下回饋
時間及參與可及性（F0017） | 10% | 與單筆示例偏好的相合程度，不外推他人

TABLE 04
準則 | A | B | C
訊號對應（30%） | 5（F0019）：結合流程／紀錄並連到交接 | 4（F0024）：直接處理溝通／轉介；紀錄為次要 | 3（F0029）：符合合作／安全；紀錄連結較間接
志工可行性（25%） | 4（F0020）：清單及同儕練習精簡，仍需確認帶領人力 | 4（F0025）：可分組演練，需準備情境及界線提示 | 4（F0030）：桌上演練設備少，仍須核實場地／程序
界線安全（20%） | 5（F0021）：限確認、記錄、交接及依制度轉介 | 5（F0026）：練習停止承諾並轉交有權角色 | 5（F0031）：限合作／活動檢點，不涉及專業處置
可觀察練習（15%） | 4（F0022）：清單可觀察；保存及回饋責任待補 | 4（F0027）：情境檢核可觀察；回饋留存待定 | 3（F0032）：討論可觀察，個人評量設計較少
時間可及性（10%） | 4（F0023）：符合一筆形式偏好；交通／時段仍未知 | 3（F0028）：面對面可行但較依賴互動時間 | 3（F0033）：單筆偏好不能代表他人
總分 | 4.50/5（F0034） | 4.10/5（F0035） | 3.65/5（F0036）

TABLE 05
項次／檢核項目 | 通過條件 | T0 狀態 | T1 狀態 | 合成事實定位
1 需求對應課程目標 | 每個目標均連到一項明確需求及其來源鍵 | 完成 | 完成 | 定義 F0115；T0 F0125；T1 F0135
2 可觀察學習目標 | 目標含可觀察行為、條件及判定方式 | 完成 | 完成 | 定義 F0116；T0 F0126；T1 F0136
3 入班條件 | 對象資格與先備條件已明列且一致 | 未完成 | 完成 | 定義 F0117；T0 F0127；T1 F0137
4 教學方法連結目標 | 每項方法／練習能回指至少一項目標 | 完成 | 完成 | 定義 F0118；T0 F0128；T1 F0138
5 時程與流程 | 時數、順序及必要節點均已界定 | 完成 | 完成 | 定義 F0119；T0 F0129；T1 F0139
6 師資資格佐證定位 | 師資角色、資格判準及待核原件定位均明確；不得以本表宣稱資格已核實 | 未完成 | 未完成 | 定義 F0120；T0 F0130；T1 F0140
7 教材版本與來源 | 使用教材具版本標記、來源及課程對應 | 完成 | 完成 | 定義 F0121；T0 F0131；T1 F0141
8 學習環境條件 | 空間、設備、可近性及安全條件均有檢核欄位 | 未完成 | 完成 | 定義 F0122；T0 F0132；T1 F0142
9 評量方法及門檻 | 評量方式、時點、量尺及合格門檻均已明列 | 完成 | 完成 | 定義 F0123；T0 F0133；T1 F0143
10 後續追蹤安排 | 追蹤時點、責任角色及預定觀察指標均已界定 | 未完成 | 未完成 | 定義 F0124；T0 F0134；T1 F0144
合計 | 固定十項、同一判準 | 6／10＝60% | 8／10＝80% | T0 四項未完成；T1 僅第6及第10項未完成

TABLE 06
排序／差距 | 證據及目前狀態 | 風險與排序理由 | SAMPLE 建議行動／責任角色 | 觸發時點及追蹤指標 | 關閉條件／維持 HOLD 條件
P1／第6項：師資資格佐證定位未完成 | 十項檢核第6項 T0、T1 均未完成（F0120、F0130、F0140）；沒有可核實的資格原件；本差距定位與處理建議登錄於 F0145 | 課程發布前無法確認資格判準與文件位置，可能影響授課適任性；因此先於課後追蹤缺口處理 | 取得並核對適用資格文件、判準及來源位置；責任角色為 SAMPLE_ROLE_TRAINING_COORDINATOR，僅為角色代碼，不指涉真人或既有職務 | 課程計畫發布或師資安排前；追蹤「發布前資格佐證欄位完整率」的分子、分母與來源 | 原件、判準、核對結果及定位均可追溯後才可解除本項 HOLD；未取得原件、授權或核對記錄則維持 HOLD，不得宣稱資格已核實
P2／第10項：後續追蹤時點與責任角色未完成 | 十項檢核第10項 T0、T1 均未完成（F0124、F0134、F0144）；未界定追蹤時點、責任角色及觀察指標；本差距定位與處理建議登錄於 F0146 | 若沒有追蹤安排，無法在課後取得一致的改善或回饋證據；排在發布前師資佐證之後 | 在課程計畫中界定追蹤時點、責任角色及觀察指標；責任角色為 SAMPLE_ROLE_PROGRAM_OWNER，僅為合成角色代碼 | 課程計畫定稿及課後追蹤啟動前；追蹤「預定追蹤項目中具有時點、責任角色及指標的比例」 | 三欄均完整且有後續紀錄定位才可關閉；未定義時間或責任角色時維持 HOLD，不得推論訓練成效

TABLE 07
階段 | SAMPLE 輸入及計算 | 門檻 | 判定 | 已填修正／追蹤
需求—目的追溯 | 三項示例訊號均映射；3/3=100%（F0047） | 3/3 可追溯；不得外推（F0048） | PASS（僅限映射） | PC 仍須用真實需求資料重新確認
設計完整度 | 目的、可觀察目標、練習、界線、紀錄／回饋責任五項；前四項有內容（F0039–F0043）；4/5=80%（F0044） | 5/5 完成才可送審議（F0045） | HOLD（F0046） | IN 補紀錄及回饋欄；ER 查定位；PC 重算
課前就緒 | 無真實場地、帶領者、時段或可及性來源（F0049） | 實際排課前逐項核實；關鍵項缺一即 HOLD（F0058） | N/A（無真實輸入） | 不把合成假設當人力／場地確認
授課與觀察 | 無實際授課或觀察資料（F0050）；無可計算分子／分母 | 授課後依核定觀察表記錄 | N/A（未提供課程） | 不填 0% 或推定通過；有原件再分析
回饋、紀錄、修訂 | 無真實回饋、出席、作品、修訂或結案紀錄（F0051） | 實際結課必要紀錄完整率 100%（F0052）；回饋率低於 80% 限縮解讀（F0053） | N/A（無實際開課／回饋） | ER 核對原件索引；缺件標示；有修訂才比版本

TABLE 08
觸發 | 動作 | SAMPLE 角色 | 時點 | 關閉條件
必填設計項未完成（本例 4/5） | HOLD；補齊後按原表重算（F0058） | IN 填補缺欄（F0061）；ER 覆核（F0082）；PC 重算（F0083） | 公開邀請或排課提案前（F0084） | 新版本逐欄可定位且覆核（F0068）
無可核實需求來源，或將單筆答案寫成群體需求 | HOLD；撤回外推、取得合法來源或限縮為示例（F0059） | PC 負責來源追溯（F0065）；核對來源與限制（F0085） | 送審議前（F0086） | 來源、分母、納入排除及限制一致（F0069）
內容要求志工診斷／治療、保證效果或越過實際授權界線 | REJECT 越界內容；修正後重審；界線不清則 HOLD（F0060） | IN 提案（F0066）；ER 檢查（F0087）；AUTH 僅在實際授權成立時決策（F0088） | 設計審查及材料發布前（F0089） | 內容有可核對界線來源、無未解項（F0070）
真實結課紀錄缺漏 | 暫停宣稱完成／成效；依原件更正並留軌跡（F0062） | ER 核對；PC 追蹤（F0056） | 結課彙整時 | 必要原件及索引完整；未取得者標缺件（F0071）
回饋率低於本例 80% | 限縮滿意度結論，不推論整體（F0053） | ER 計算回收率（F0067）；PC 限縮解讀（F0090） | 分析回饋前（F0091） | 列明回收數、邀請分母及無效處理（F0072）

TABLE 09
文件 | 專屬責任 | 本報告的界線
0003／I01-E02 問卷 | 題目、選項、量尺、單筆示例回答（F0092） | 只引用有限訊號，不另做問卷或量尺
0004／I01-E02 執行與樣本紀錄 | 邀請、同意、回收、有效性、排除及交接（F0093） | 不宣稱調查已實際執行，不複製其樣本流向數字
0005／I01-E02 需求分析報告 | 調查彙整及逐題需求分析（F0094） | 不把 0005 當已接受來源；本件比較產品／流程，不取代需求分析
0006／I01-E03 業務發展計畫與人力資源訓練規劃 | 業務方向及人力資源訓練規劃（F0095） | 不決定機構策略、人力配置或年度經營目標
0008／I01-E05 各類別訓練課程年度成長計畫 | 類別年度成長目標與資源路徑（F0096） | 檢視產品／流程，不提出年度班次、招生或成長承諾

TABLE 10
官方要求 | 對應結果 | 精確位置 | 覆核及限制
課程產品及流程的檢討分析。 | 三方案比較、加權算式、設計完整度及生命週期證據狀態／門檻 | 第 1、3–4、6–7 節 | 獨立覆核者重算公式並逐列核 CSV；全部仍是 SAMPLE，無正式接受或 REAL 證據


## Candidate-specific synthetic replacement register
fact_id,fact_type,synthetic_value,exact_locator,source_or_generation_method,real_replacement_source,replacement_method,status
F0001,sample_n,1 synthetic response,§2 source table; response count,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0002,sample_signal,service process and records,§2 source table; Q3_NEED1,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0003,sample_signal,communication/referral boundaries,§2 source table; Q3_NEED2,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0004,sample_signal,volunteer cooperation/safety,§2 source table; Q3_NEED3,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0005,sample_rating,urgency 4/5,§2 source table; Q4_URG,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0006,sample_rating,self-confidence 2/5,§2 source table; Q5_CONF,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0007,sample_preference,face-to-face,§2 source table; Q7_MODE,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0008,sample_preference,"one session, 3 hours",§2 source table; Q9_DURATION,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0009,sample_barrier,transport distance/time,§2 source table; Q10_BARRIER,Bounded import from one 0003 synthetic response; no extrapolation.,E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0003_I01-E02_SOURCE_PREP_R01_20261029\source\SYNTHETIC_REPLACEMENT_REGISTER_0003_R01.csv,Replace with authorized anonymized item-level responses and recalculate all denominators.,SAMPLE_SYNTHETIC_ONLY
F0010,sample_option,Option A includes a pre-service confirmation activity.,"§3 options table, row A, product/process concept","New hypothetical concept, not existing association course.",Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0011,sample_option,Option B includes an interpersonal communication practice.,"§3 options table, row B, product/process concept","New hypothetical concept, not existing association course.",Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0012,sample_option,Option C trains volunteer cooperation as its central concept.,"§3 options table, row C, product/process concept","New hypothetical concept, not existing association course.",Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0013,rubric_weight,signal alignment=30%,§4.1 rubric row signal alignment; weight,New sample rubric; weights sum to 100%.,Approved evaluation rubric and documented priorities (not supplied),"Replace after authorized review, document weight rationale, recalculate.",SAMPLE_SYNTHETIC_ONLY
F0014,rubric_weight,small-volunteer feasibility=25%,§4.1 rubric row small-volunteer feasibility; weight,New sample rubric; weights sum to 100%.,Approved evaluation rubric and documented priorities (not supplied),"Replace after authorized review, document weight rationale, recalculate.",SAMPLE_SYNTHETIC_ONLY
F0015,rubric_weight,role boundary/safety=20%,§4.1 rubric row role boundary/safety; weight,New sample rubric; weights sum to 100%.,Approved evaluation rubric and documented priorities (not supplied),"Replace after authorized review, document weight rationale, recalculate.",SAMPLE_SYNTHETIC_ONLY
F0016,rubric_weight,observable practice/feedback=15%,§4.1 rubric row observable practice/feedback; weight,New sample rubric; weights sum to 100%.,Approved evaluation rubric and documented priorities (not supplied),"Replace after authorized review, document weight rationale, recalculate.",SAMPLE_SYNTHETIC_ONLY
F0017,rubric_weight,time/access fit=10%,§4.1 rubric row time/access fit; weight,New sample rubric; weights sum to 100%.,Approved evaluation rubric and documented priorities (not supplied),"Replace after authorized review, document weight rationale, recalculate.",SAMPLE_SYNTHETIC_ONLY
F0018,rating_anchors,1 poor; 3 partial; 5 strong; 2 and 4 intermediate,§4.1; rating scale,Sample ordinal scale defined for this comparison.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0019,option_rating_and_reason,A/signal alignment=5/5; combines process/record signal with handoff,§4.2 matrix criterion signal alignment; option A score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0020,option_rating_and_reason,A/small-volunteer feasibility=4/5; compact checklist; staffing unverified,§4.2 matrix criterion small-volunteer feasibility; option A score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0021,option_rating_and_reason,"A/role boundary/safety=5/5; bounded confirmation, recording, handoff, referral",§4.2 matrix criterion role boundary/safety; option A score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0022,option_rating_and_reason,A/observable practice/feedback=4/5; observable checklist; record owner missing,§4.2 matrix criterion observable practice/feedback; option A score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0023,option_rating_and_reason,A/time/access fit=4/5; matches one format preference; access unknown,§4.2 matrix criterion time/access fit; option A score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0024,option_rating_and_reason,B/signal alignment=4/5; direct communication/referral fit; records secondary,§4.2 matrix criterion signal alignment; option B score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0025,option_rating_and_reason,B/small-volunteer feasibility=4/5; small-group practice needs scenarios,§4.2 matrix criterion small-volunteer feasibility; option B score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0026,option_rating_and_reason,B/role boundary/safety=5/5; stopping/transfer to authorized role,§4.2 matrix criterion role boundary/safety; option B score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0027,option_rating_and_reason,B/observable practice/feedback=4/5; scenario checklist observable,§4.2 matrix criterion observable practice/feedback; option B score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0028,option_rating_and_reason,B/time/access fit=3/5; face-to-face fits one response but needs interaction time,§4.2 matrix criterion time/access fit; option B score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0029,option_rating_and_reason,C/signal alignment=3/5; cooperation/safety fit; record link indirect,§4.2 matrix criterion signal alignment; option C score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0030,option_rating_and_reason,C/small-volunteer feasibility=4/5; tabletop needs room/process verification,§4.2 matrix criterion small-volunteer feasibility; option C score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0031,option_rating_and_reason,C/role boundary/safety=5/5; limited to cooperation and safety,§4.2 matrix criterion role boundary/safety; option C score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0032,option_rating_and_reason,C/observable practice/feedback=3/5; discussion observable; individual check less specified,§4.2 matrix criterion observable practice/feedback; option C score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0033,option_rating_and_reason,C/time/access fit=3/5; one response cannot establish broad access,§4.2 matrix criterion time/access fit; option C score/reason cell,Sample analyst judgment from printed concept and limited synthetic signal; not performance data.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0034,derived_score,A=4.50/5,§4.2–4.3 total/calculation A,Recomputed as sum(weight percent × rating)/100 from displayed matrix.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0035,derived_score,B=4.10/5,§4.2–4.3 total/calculation B,Recomputed as sum(weight percent × rating)/100 from displayed matrix.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0036,derived_score,C=3.65/5,§4.2–4.3 total/calculation C,Recomputed as sum(weight percent × rating)/100 from displayed matrix.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0037,derived_score,A−B=0.40 points,§4.3 difference A−B,Recomputed as sum(weight percent × rating)/100 from displayed matrix.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0038,derived_score,A−C=0.85 points,§4.3 difference A−C,Recomputed as sum(weight percent × rating)/100 from displayed matrix.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0039,sample_design_check,purpose/scope:present,§6 design checklist item purpose/scope,Hypothetical desktop review of option A concept in this text; no real course file.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0040,sample_design_check,observable objective:present,§6 design checklist item observable objective,Hypothetical desktop review of option A concept in this text; no real course file.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0041,sample_design_check,practice activity:present,§6 design checklist item practice activity,Hypothetical desktop review of option A concept in this text; no real course file.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0042,sample_design_check,role boundary:present,§6 design checklist item role boundary,Hypothetical desktop review of option A concept in this text; no real course file.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0043,sample_design_check,record location and feedback/reviewer owner:missing,§6 design checklist item record location and feedback/reviewer owner,Hypothetical desktop review of option A concept in this text; no real course file.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0044,design_completeness,4/5=80%,§6 design row; result,Four present checklist items divided by five.,Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0045,design_gate,5/5=100% required,§6 design row; threshold,"Sample gate, not policy.",Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0046,design_result,HOLD: 4/5 below 5/5,§6 design row; result,Derived from F0044–F0045.,Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0047,mapping_coverage,3/3=100%,§6 mapping row; result,Three example signals mapped; not population demand.,Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0048,mapping_gate,"3/3 traceable, no generalization",§6 mapping row; threshold,Sample traceability rule.,Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0049,preclass_status,N/A; no real room/facilitator/schedule/access source,§6 readiness row; result,No real input supplied.,Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0050,delivery_status,N/A; no actual teaching/observation,§6 delivery row; result,No real course supplied.,Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0051,closure_status,N/A; no real attendance/feedback/work/revision records,§6 closure row; result,No real course supplied.,Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0052,record_threshold,100% of required records at actual course closeout,§6 closure row; threshold,"Sample threshold, no current records claimed.",Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0053,feedback_threshold,80%; below it limit conclusions,§6 closure row; threshold,"Sample threshold, not measured.",Approved design/delivery/feedback originals (not supplied),Use authorized policy and exact real records; otherwise N/A.,SAMPLE_SYNTHETIC_ONLY
F0054,sample_role,PC=planning coordinator,§7 action table/legend; role PC,Hypothetical role code; no real appointment/person/authority.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0055,sample_role,IN=course design/facilitation,§7 action table/legend; role IN,Hypothetical role code; no real appointment/person/authority.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0056,sample_role,ER=records/quality review,§7 action table/legend; role ER,Hypothetical role code; no real appointment/person/authority.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0057,sample_role,AUTH=authorized decision role,§7 action table/legend; role AUTH,Hypothetical role code; no real appointment/person/authority.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0058,hold_rule,Incomplete required design field => HOLD before invitation/scheduling proposal,§7 design row; trigger/action,Sample workflow control.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0059,hold_rule,No traceable real demand source or one answer generalized => HOLD,§7 unsupported demand row; trigger/action,Sample truth-boundary control.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0060,reject_rule,"Reject diagnosis/treatment instruction, guaranteed outcome or out-of-scope content",§7 boundary row; trigger/action,Sample volunteer-scope rule.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0061,action_owner_timing,IN fills the missing record and feedback fields in the sample design.,"§7.2 action table, design-incomplete row, IN action",Synthetic roles/relative timing.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0062,action_owner_timing,ER verifies originals; PC limits claims at real course closeout,§7 missing-record row; owner/timing,Synthetic roles; no course closeout asserted.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0063,cross_document_boundary,"Title-blind identification classifies the body as product/process analysis from its comparison, lifecycle checklist and evidence limits.",§8 title-blind identification paragraph,Current Blueprint responsibilities; no neighbor acceptance claim.,Actual approved source/original (not supplied),Replace only after source verification; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0064,derived_rubric_total,30%+25%+20%+15%+10%=100%,§4.1; rubric footer/weight total,Sum of the five displayed sample weights.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0065,action_owner_timing,PC is the sample role assigned ownership of demand-source traceability.,"§7.2 action table, unsupported-demand row, PC owner",Sample role and relative timing.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0066,action_owner_timing,IN is the sample role that proposes a boundary correction.,"§7.2 action table, boundary row, IN action",Sample role workflow; no actual decision or appointment.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0067,action_owner_timing,ER is the sample role that calculates feedback return rate.,"§7.2 action table, low-feedback row, ER action",Sample role workflow.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0068,close_condition,"Design action closes only with a new version, field-level locators and review evidence",§7 action row: design incomplete; close condition,Sample close criterion.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0069,close_condition,"Demand action closes only when source, denominator, inclusion/exclusion and limitation agree",§7 action row: unsupported demand; close condition,Sample close criterion.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0070,close_condition,Boundary action closes only after source-backed content check with no unresolved scope item,§7 action row: boundary violation; close condition,Sample close criterion.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0071,close_condition,Closeout action closes only with required originals and index; absent items remain identified as missing,§7 action row: missing course records; close condition,Sample close criterion.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0072,close_condition,"Feedback action closes with response count, invite denominator and invalid/missing handling documented",§7 action row: low feedback return; close condition,Sample close criterion.,"Actual authorized role assignment, source records and applicable approved procedure (not supplied)",Verify against exact source and authority; retain SAMPLE/UNKNOWN if unavailable.,SAMPLE_SYNTHETIC_ONLY
F0073,sample_option_component,Option A includes a process-record practice.,"§3 options table, row A, product/process concept",Hypothetical decomposition of the R02 sample option; no real association course or activity record was supplied.,"Actual approved course plan, teaching materials, and authorized activity records (not supplied).","Replace only after verifying the source, date, approval status and exact locator; otherwise retain SAMPLE/UNKNOWN.",SAMPLE_SYNTHETIC_ONLY
F0074,sample_option_component,Option A includes an end-of-service handoff practice.,"§3 options table, row A, product/process concept",Hypothetical decomposition of the R02 sample option; no real association course or activity record was supplied.,"Actual approved course plan, teaching materials, and authorized activity records (not supplied).","Replace only after verifying the source, date, approval status and exact locator; otherwise retain SAMPLE/UNKNOWN.",SAMPLE_SYNTHETIC_ONLY
F0075,sample_option_component,Option B includes listening practice.,"§3 options table, row B, product/process concept",Hypothetical decomposition of the R02 sample option; no real association course or activity record was supplied.,"Actual approved course plan, teaching materials, and authorized activity records (not supplied).","Replace only after verifying the source, date, approval status and exact locator; otherwise retain SAMPLE/UNKNOWN.",SAMPLE_SYNTHETIC_ONLY
F0076,sample_option_component,Option B includes referral-boundary practice.,"§3 options table, row B, product/process concept",Hypothetical decomposition of the R02 sample option; no real association course or activity record was supplied.,"Actual approved course plan, teaching materials, and authorized activity records (not supplied).","Replace only after verifying the source, date, approval status and exact locator; otherwise retain SAMPLE/UNKNOWN.",SAMPLE_SYNTHETIC_ONLY
F0077,sample_option_component,Option C includes volunteer task and role allocation.,"§3 options table, row C, exercise and observable output",Hypothetical decomposition of the R02 sample option; no real association course or activity record was supplied.,"Actual approved course plan, teaching materials, and authorized activity records (not supplied).","Replace only after verifying the source, date, approval status and exact locator; otherwise retain SAMPLE/UNKNOWN.",SAMPLE_SYNTHETIC_ONLY
F0078,sample_option_component,Option C includes an assembly confirmation check.,"§3 options table, row C, exercise and observable output",Hypothetical decomposition of the R02 sample option; no real association course or activity record was supplied.,"Actual approved course plan, teaching materials, and authorized activity records (not supplied).","Replace only after verifying the source, date, approval status and exact locator; otherwise retain SAMPLE/UNKNOWN.",SAMPLE_SYNTHETIC_ONLY
F0079,sample_option_component,Option C includes anomaly reporting.,"§3 options table, row C, exercise and observable output",Hypothetical decomposition of the R02 sample option; no real association course or activity record was supplied.,"Actual approved course plan, teaching materials, and authorized activity records (not supplied).","Replace only after verifying the source, date, approval status and exact locator; otherwise retain SAMPLE/UNKNOWN.",SAMPLE_SYNTHETIC_ONLY
F0080,sample_option_component,Option C includes a closing inspection.,"§3 options table, row C, exercise and observable output",Hypothetical decomposition of the R02 sample option; no real association course or activity record was supplied.,"Actual approved course plan, teaching materials, and authorized activity records (not supplied).","Replace only after verifying the source, date, approval status and exact locator; otherwise retain SAMPLE/UNKNOWN.",SAMPLE_SYNTHETIC_ONLY
F0081,sample_recommendation,Option A may be presented only as an example for an authorized person to consider after the missing design field is completed; no selection or approval is asserted.,§7.1 SAMPLE recommendation paragraph,Writer-generated conditional recommendation based only on hypothetical weighted scores and the 4/5 checklist.,Actual authorized decision and completed design record (not supplied).,Keep as SAMPLE unless an authorized dated decision and supporting record are provided; never infer approval from score.,SAMPLE_SYNTHETIC_ONLY
F0082,sample_action,ER checks the completed design fields.,"§7.2 action table, design-incomplete row, ER action",Synthetic division of responsibilities for the sample hold workflow.,Actual authorized role assignment and review evidence (not supplied).,Replace only from verified role assignment and review record; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0083,sample_action,PC recalculates the design checklist after correction.,"§7.2 action table, design-incomplete row, PC action",Synthetic division of responsibilities for the sample hold workflow.,Actual authorized role assignment and recalculation record (not supplied).,Replace only from verified assignment and recalculation record; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0084,sample_timing,Complete and review the corrected design before a public invitation or scheduling proposal.,"§7.2 action table, design-incomplete row, timing",Synthetic relative timing; not a real schedule.,Actual approved course schedule and dated workflow record (not supplied).,Replace only with source-backed date and authority; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0085,sample_action,PC traces each demand claim to its source and states its denominator and limitations.,"§7.2 action table, unsupported-demand row, PC action",Synthetic division of responsibilities for the sample hold workflow.,Actual authorized source-review assignment and source records (not supplied).,Replace only with verified assignment and source record; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0086,sample_timing,Complete source traceability before submitting the matter for review.,"§7.2 action table, unsupported-demand row, timing",Synthetic relative timing; not a real schedule.,Actual dated workflow record (not supplied).,Replace only with a verified timestamp and workflow record; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0087,sample_action,ER checks proposed boundary corrections against a verifiable source.,"§7.2 action table, boundary row, ER action",Synthetic division of responsibilities for the sample hold workflow.,Actual authorized review assignment and source evidence (not supplied).,Replace only with verified assignment and reviewed source; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0088,sample_authority_condition,AUTH may decide only when actual decision authority is documented.,"§7.2 action table, boundary row, AUTH condition","Synthetic safeguard; no appointment, delegation or decision is asserted.",Actual governing delegation or authorized decision record (not supplied).,Do not replace without verified authority; retain UNKNOWN otherwise.,SAMPLE_SYNTHETIC_ONLY
F0089,sample_timing,Resolve scope and authority before design review or material release.,"§7.2 action table, boundary row, timing",Synthetic relative timing; not a real schedule.,Actual dated workflow record and authorized release control (not supplied).,Replace only with verified record; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0090,sample_action,PC limits interpretation when feedback response is below the sample threshold.,"§7.2 action table, low-feedback row, PC action",Synthetic division of responsibilities for the sample hold workflow.,Actual authorized analysis assignment and feedback records (not supplied).,Replace only from verified assignment and records; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0091,sample_timing,"Document return count, invite denominator and invalid-response handling before interpreting feedback.","§7.2 action table, low-feedback row, timing",Synthetic relative timing; not a real schedule.,Actual dated feedback-analysis workflow (not supplied).,Replace only with verified record; otherwise SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0092,cross_document_boundary,"0003 owns questionnaire items, response choices, scales and any example response.","§8 cross-document responsibility table, row 0003",Unique Blueprint responsibility and current candidate split; not an acceptance claim.,"Verified current Blueprint row and accepted 0003 artifact, when available.",Reconcile against current official crosswalk; do not infer 0003 acceptance.,SAMPLE_SYNTHETIC_ONLY
F0093,cross_document_boundary,"0004 owns survey invitation, consent, collection, validity, exclusion and handoff records.","§8 cross-document responsibility table, row 0004",Unique Blueprint responsibility and current candidate split; not an execution claim.,"Verified current Blueprint row and authentic 0004 records, when available.",Keep actual execution UNKNOWN until original records are verified.,SAMPLE_SYNTHETIC_ONLY
F0094,cross_document_boundary,0005 owns demand synthesis and item-level demand analysis.,"§8 cross-document responsibility table, row 0005",Unique Blueprint responsibility and current candidate split; not an acceptance claim.,"Verified current Blueprint row and accepted 0005 artifact, when available.",Do not treat an unreviewed 0005 candidate as an accepted source.,SAMPLE_SYNTHETIC_ONLY
F0095,cross_document_boundary,0006 owns business direction and workforce training planning.,"§8 cross-document responsibility table, row 0006",Unique Blueprint responsibility and current candidate split; not an acceptance claim.,"Verified current Blueprint row and accepted 0006 artifact, when available.",Do not infer organizational strategy or real staffing.,SAMPLE_SYNTHETIC_ONLY
F0096,cross_document_boundary,0008 owns annual growth targets and resource paths by course category.,"§8 cross-document responsibility table, row 0008",Unique Blueprint responsibility and current candidate split; not an acceptance claim.,"Verified current Blueprint row and accepted 0008 artifact, when available.","Do not infer approved annual class counts, enrollment or growth commitments.",SAMPLE_SYNTHETIC_ONLY
F0097,comparison_assumption,"All three options use one shared hypothetical delivery window: face-to-face and one 3-hour session, drawn only from the 0003 SAMPLE response.","§4.1 shared comparison assumptions paragraph, sentence 1",Inherited from 0003 synthetic response fields F0007 and F0008 solely as a common comparison frame.,Actual approved schedule or course plan (not supplied).,Replace only from approved dated schedule; otherwise retain SAMPLE/UNKNOWN.,SAMPLE_SYNTHETIC_ONLY
F0098,comparison_assumption,The same unspecified volunteer group and same unverified venue are held constant across the three hypothetical options.,"§4.1 shared comparison assumptions paragraph, sentence 2",Explicit analytical assumption; headcount and venue are not association facts.,Actual enrollment/target group and venue confirmation (not supplied).,Replace only with verified source; do not infer headcount or venue.,SAMPLE_SYNTHETIC_ONLY
F0099,resource_limit,No trainer or equipment availability is assumed; actual staffing and equipment remain UNKNOWN.,"§4.1 shared comparison assumptions paragraph, sentence 3",Explicit conservative modeling limit; no resource availability data supplied.,Actual authorized staffing and equipment inventory (not supplied).,Update only after verifying current availability and role authorization.,SAMPLE_SYNTHETIC_ONLY
F0100,score_interpretation,"The 25% feasibility score compares relative preparation and practice design under the common SAMPLE frame; it does not establish actual resources, venue or scheduling capacity.","§4.1 shared comparison assumptions paragraph, sentence 4",Interpretation of the declared scoring model and explicit common assumptions.,Verified actual capacity and approved course plan (not supplied).,Re-score from verified actual conditions if the frame changes.,SAMPLE_SYNTHETIC_ONLY
F0101,indicator_definition,Course-process checklist completeness rate: complete binary checks divided by the same 10 hypothetical checks.,"§4.4, indicator definition row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).","Use an authorized, versioned checklist and a fixed completeness rule; the present label is synthetic.",SAMPLE_SYNTHETIC_ONLY
F0102,synthetic_denominator,10 identical hypothetical checklist items at T0 and T1.,"§4.4, indicator definition and T0/T1 rows",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Replace with the actual eligible-item denominator from the verified source register.,SAMPLE_SYNTHETIC_ONLY
F0103,synthetic_target,90% SAMPLE target.,"§4.4, target row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Replace only with an approved target source and effective date.,SAMPLE_SYNTHETIC_ONLY
F0104,synthetic_baseline_count,T0 SAMPLE: 6 complete checks out of 10.,"§4.4, T0 row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).","Replace with source-verified numerator, denominator, period and exclusion log.",SAMPLE_SYNTHETIC_ONLY
F0105,synthetic_baseline_rate,T0 SAMPLE rate: 60%.,"§4.4, T0 row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Recompute numerator / denominator × 100% from source records.,SAMPLE_SYNTHETIC_ONLY
F0106,synthetic_after_count,T1 SAMPLE: 8 complete checks out of 10.,"§4.4, T1 row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).","Replace with source-verified numerator, denominator, period and exclusion log.",SAMPLE_SYNTHETIC_ONLY
F0107,synthetic_after_rate,T1 SAMPLE rate: 80%.,"§4.4, T1 row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Recompute numerator / denominator × 100% from source records.,SAMPLE_SYNTHETIC_ONLY
F0108,synthetic_baseline_gap,T0 gap: 60% − 90% = −30 percentage points.,"§4.4, T0 gap row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Recompute actual minus approved target; for percent measures report percentage points.,SAMPLE_SYNTHETIC_ONLY
F0109,synthetic_after_gap,T1 gap: 80% − 90% = −10 percentage points.,"§4.4, T1 gap row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Recompute actual minus approved target; preserve sign and units.,SAMPLE_SYNTHETIC_ONLY
F0110,synthetic_improvement_rate,Relative improvement rate: (80% − 60%) / 60% = 33.33%.,"§4.4, improvement calculation row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Recompute (after − before) / before only when baseline is nonzero and series are comparable.,SAMPLE_SYNTHETIC_ONLY
F0111,synthetic_absolute_change,Absolute change: +20 percentage points.,"§4.4, improvement calculation row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Report after minus before in percentage points; do not label it as relative improvement rate.,SAMPLE_SYNTHETIC_ONLY
F0112,synthetic_decision,T1 80% remains below 90% SAMPLE target; maintain HOLD.,"§4.4, SAMPLE conclusion row",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Replace only after a verified real result and authorized decision; never infer approval.,SAMPLE_SYNTHETIC_ONLY
F0113,synthetic_zero_baseline_rule,"If before/improvement-baseline value is zero, the relative improvement rate is N/A because division by zero is undefined.","§4.4, N/A/HOLD rule",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Keep rate N/A; show raw counts and absolute change only.,SAMPLE_SYNTHETIC_ONLY
F0114,synthetic_comparability_rule,"If T0/T1 definitions, eligible checklist items, denominator or units differ, direct improvement-rate comparison is HOLD until rebaselined.","§4.4, N/A/HOLD rule",Created solely as a synthetic arithmetic example to satisfy the current Unique Blueprint formula requirement; no association source data or execution records were supplied.,"Same-scope authorized course-process checklist source records for each measurement point, approved target definition, dated source register and traceable inclusion/exclusion log (not supplied).",Record scope differences and establish a comparable baseline before calculating.,SAMPLE_SYNTHETIC_ONLY
F0115,check_definition,Check 1: each course objective maps to a stated need and a source key.,§4.4 item 1 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the authorized need analysis and course-plan crosswalk.,SAMPLE_SYNTHETIC_ONLY
F0116,check_definition,"Check 2: each objective states observable behavior, conditions, and a decision criterion.",§4.4 item 2 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the approved objective and assessment specification.,SAMPLE_SYNTHETIC_ONLY
F0117,check_definition,Check 3: target learner eligibility and prerequisite conditions are explicit and consistent.,§4.4 item 3 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the approved enrollment and prerequisite rules.,SAMPLE_SYNTHETIC_ONLY
F0118,check_definition,Check 4: every teaching method or exercise maps to at least one objective.,§4.4 item 4 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the course plan and aligned activity map.,SAMPLE_SYNTHETIC_ONLY
F0119,check_definition,"Check 5: instructional hours, sequence, and required milestones are defined.",§4.4 item 5 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the approved timetable and course plan.,SAMPLE_SYNTHETIC_ONLY
F0120,check_definition,"Check 6: trainer role, qualification criteria, and source-document locator are defined; this does not assert actual qualification verification.",§4.4 item 6 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Obtain the applicable original qualification record and verify it under authorized criteria.,SAMPLE_SYNTHETIC_ONLY
F0121,check_definition,"Check 7: teaching material has a version identifier, source, and course alignment.",§4.4 item 7 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the controlled material version and source record.,SAMPLE_SYNTHETIC_ONLY
F0122,check_definition,"Check 8: learning environment checks cover space, equipment, accessibility, and safety conditions.",§4.4 item 8 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the actual site and equipment checklist with traceable observations.,SAMPLE_SYNTHETIC_ONLY
F0123,check_definition,"Check 9: assessment method, timing, scale, and passing threshold are defined.",§4.4 item 9 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the approved assessment plan and rubric.,SAMPLE_SYNTHETIC_ONLY
F0124,check_definition,"Check 10: follow-up timing, responsible role, and observation indicator are defined.",§4.4 item 10 definition,Created only for a coherent SAMPLE/SYNTHETIC checklist demonstration; not sourced from an association record.,Same-scope authorized course-plan checklist and original linked records for each time point (not supplied).,Use the approved follow-up plan and later source records.,SAMPLE_SYNTHETIC_ONLY
F0125,synthetic_check_status_T0,T0 SAMPLE item 1 passes; status=complete; same fixed ten-item checklist.,§4.4 item 1 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0126,synthetic_check_status_T0,T0 SAMPLE item 2 passes; status=complete; same fixed ten-item checklist.,§4.4 item 2 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0127,synthetic_check_status_T0,T0 SAMPLE item 3 fails; status=incomplete; same fixed ten-item checklist.,§4.4 item 3 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0128,synthetic_check_status_T0,T0 SAMPLE item 4 passes; status=complete; same fixed ten-item checklist.,§4.4 item 4 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0129,synthetic_check_status_T0,T0 SAMPLE item 5 passes; status=complete; same fixed ten-item checklist.,§4.4 item 5 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0130,synthetic_check_status_T0,T0 SAMPLE item 6 fails; status=incomplete; same fixed ten-item checklist.,§4.4 item 6 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0131,synthetic_check_status_T0,T0 SAMPLE item 7 passes; status=complete; same fixed ten-item checklist.,§4.4 item 7 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0132,synthetic_check_status_T0,T0 SAMPLE item 8 fails; status=incomplete; same fixed ten-item checklist.,§4.4 item 8 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0133,synthetic_check_status_T0,T0 SAMPLE item 9 passes; status=complete; same fixed ten-item checklist.,§4.4 item 9 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0134,synthetic_check_status_T0,T0 SAMPLE item 10 fails; status=incomplete; same fixed ten-item checklist.,§4.4 item 10 T0 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T0 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0135,synthetic_check_status_T1,T1 SAMPLE item 1 passes; status=complete; same fixed ten-item checklist.,§4.4 item 1 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0136,synthetic_check_status_T1,T1 SAMPLE item 2 passes; status=complete; same fixed ten-item checklist.,§4.4 item 2 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0137,synthetic_check_status_T1,T1 SAMPLE item 3 passes; status=complete; same fixed ten-item checklist.,§4.4 item 3 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0138,synthetic_check_status_T1,T1 SAMPLE item 4 passes; status=complete; same fixed ten-item checklist.,§4.4 item 4 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0139,synthetic_check_status_T1,T1 SAMPLE item 5 passes; status=complete; same fixed ten-item checklist.,§4.4 item 5 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0140,synthetic_check_status_T1,T1 SAMPLE item 6 fails; status=incomplete; same fixed ten-item checklist.,§4.4 item 6 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0141,synthetic_check_status_T1,T1 SAMPLE item 7 passes; status=complete; same fixed ten-item checklist.,§4.4 item 7 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0142,synthetic_check_status_T1,T1 SAMPLE item 8 passes; status=complete; same fixed ten-item checklist.,§4.4 item 8 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0143,synthetic_check_status_T1,T1 SAMPLE item 9 passes; status=complete; same fixed ten-item checklist.,§4.4 item 9 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0144,synthetic_check_status_T1,T1 SAMPLE item 10 fails; status=incomplete; same fixed ten-item checklist.,§4.4 item 10 T1 cell,Synthetic state solely to demonstrate item-level numerator traceability.,Original same-scope T1 checklist and linked records (not supplied).,Replace with a source-verified pass/fail state under the same criteria; retain original record locator and any exclusions.,SAMPLE_SYNTHETIC_ONLY
F0145,synthetic_priority_gap,SAMPLE P1: item 6 remains incomplete at T1; require source-located trainer qualification criteria before course-plan release.,§5.1 P1 row; linked §4.4 item 6,Synthetic prioritization demonstration; no association decision or assignment exists.,"Authorized source risk review, approved role assignment, and original course-plan records (not supplied).",Reassess only from authorized original qualification evidence and documented criteria; never treat the sample as verification.,SAMPLE_SYNTHETIC_ONLY
F0146,synthetic_priority_gap,"SAMPLE P2: item 10 remains incomplete at T1; define follow-up timing, responsible role, and observation indicator.",§5.1 P2 row; linked §4.4 item 10,Synthetic prioritization demonstration; no association decision or assignment exists.,"Authorized source risk review, approved role assignment, and original course-plan records (not supplied).",Replace with the approved plan and later traceable follow-up record; do not infer an outcome.,SAMPLE_SYNTHETIC_ONLY
F0147,synthetic_priority_method,"SAMPLE ranking rule: resolve pre-release trainer qualification traceability before post-course follow-up planning; P1/P2 are example labels, not association-approved priorities.",§5.1 method paragraph and priority column,Synthetic prioritization demonstration; no association decision or assignment exists.,"Authorized source risk review, approved role assignment, and original course-plan records (not supplied).","Re-rank using verified source evidence, applicable safety/contract requirements, and documented authorized review.",SAMPLE_SYNTHETIC_ONLY
