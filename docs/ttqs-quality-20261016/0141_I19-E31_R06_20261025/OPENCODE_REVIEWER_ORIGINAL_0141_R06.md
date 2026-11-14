```json
{
  "doc_id": "0141",
  "requirement_id": "I19-E31",
  "candidate_docx_sha256": "e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2",
  "text_sha256": "b9d23ec3a917c13a3824a5f06a41f44a7be5f9d848d1f3537d1c8a22933b9416",
  "verdict": "PASS",
  "major_findings": [],
  "minor_findings": [
    {
      "severity": "MINOR",
      "body_locator": "Sidecar SAMPLE_REPLACEMENT_REGISTER_0141_R06.csv (sha256 862df595…): docx_locator cells of the 36 per-row facts, e.g. FACT-SYN-0141-SAT-TREND-R01-2023-001 = 「Appendix 3 row 1; section 6 aggregates derive from this row」",
      "evidence": "The eight non-row facts (FRAME-2023/2024/2025, Q8-VIGNETTE, SOP-PARAMS, SUPPRESSION, ACT-01, ACT-02) were re-pointed to MANUSCRIPT_0141_R06_CANDIDATE.md with Chinese locators (「§陸-一 各期樣本回收與有效母數彙總表」, 「附錄二」, 「§肆」, 「§參-四」, 「§捌」), which closes R05 minor finding 5 as stated in the R06 targeted-repair receipt. The 36 row-level locators, however, remain in English and still say the section-6 aggregates 「derive from this row」 — they derive from all 36 rows plus the invitation counts, not from one row. The DOCX itself uses 附錄三 and §陸 throughout, so an auditor matching sidecar locators to the document still meets a second vocabulary.",
      "required_action": "Re-point the 36 row locators to 「附錄三 第N列（另見§陸-一、§陸-二彙總）」 and record the R06 manuscript SHA-256 in the register header/metadata. Byte-neutral for the DOCX."
    },
    {
      "severity": "MINOR",
      "body_locator": "§伍 首句 「本問卷包含 7 題核心量化題目（均採 1–5 分 Likert 量尺）」 and §參-三 comparability row 「核心量化 7 題（Q1–Q7）」 — read against §陸-一 column header 「Q1–Q6 六構面有效填答次數」 and its 說明 「每年 Q1–Q6 六題 × 12 份 = 72 次…Q7 整體滿意度為獨立題…不列入本欄」",
      "evidence": "R05 minor finding 2 (72 vs 7×12=84 misreading) is functionally resolved: the column is now explicitly Q1–Q6 and the note states the Q7 exclusion. The word 「核心」 nonetheless still denotes seven items in two other places while the results column now implicitly reserves 「核心」 for six, so the same term carries two scopes in one document; the prose 說明 removes any arithmetic ambiguity.",
      "required_action": "Cosmetic only: change §伍 to 「7 題量化題目（6 構面題 Q1–Q6 ＋ 1 獨立整體題 Q7）」 and align the comparability table wording. No numeric change."
    },
    {
      "severity": "MINOR",
      "body_locator": "§捌 方案一 「Q5 有效均值應達到 3.8000 分以上；此為本方案唯一可量測之成功門檻」 and 方案二 「Q2 有效均值應達到 3.7000 分以上，且 Top-2 佔比應突破 75%（分母為 Q2 自身有效回答數）」",
      "evidence": "Recomputed from the 36 CSV rows: terminal SAMPLE Q5 2025 = 4.2500, so the Q5 floor of 3.8000 is already exceeded at the demonstration end-point; Q2 2025 item-level Top-2 = 9/12 = 75.00%, exactly the stated 75% bar, so 「突破 75%」 means strictly more than the last demonstrated value while the document publishes item-level Top-2 for Q7 only (§陸-三) and never states the Q2 baseline. The thresholds are therefore measurable against 附錄四's item-level formula, but they are absolute floors not derived from a disclosed baseline, and an evaluator cannot see from the document what improvement the 75%/3.8000 combination would represent.",
      "required_action": "Publish the Q2 (and Q5) item-level Top-2 baselines in §陸 or in the proposal, or restate the criteria as baseline + explicit point/percentage-point delta, and label them SAMPLE parameters. No change to existing published aggregates."
    },
    {
      "severity": "MINOR",
      "body_locator": "§捌 方案一 「…原擬附加之「無行政聯繫延誤之負面抱怨」條件屬 UNKNOWN‑sourced：本 SAMPLE 樣本沒有真實抱怨紀錄或 Q8 證據…」",
      "evidence": "R05 minor finding 3 is resolved in substance: the qualitative condition is now excluded from the success threshold and explicitly marked UNKNOWN-sourced with a requirement that an authorised role define source, owner, counting window and escalation rule before use. The token is written with U+2011 (non-breaking hyphen) per R06_LAYOUT_PATCH_RECEIPT to stop Word splitting it across pages 11/12, so a plain ASCII search for 「UNKNOWN-sourced」 in this candidate will not find it; the visual receipt's 「pagination_token_fix PASS」 is receipt metadata, not something I inspected.",
      "required_action": "Optional: also state the same UNKNOWN provenance once in plain ASCII form (e.g. in §柒-二 limitations or §玖 gate table) so the live condition remains machine-locatable. Cosmetic/searchability only."
    }
  ],
  "checks": [
    {
      "id": "C01_identity_triangulation",
      "result": "PASS",
      "locator": "報告基本資訊與狀態標註 表；§貳-一；§玖 規則1",
      "evidence": "doc_id 0141, requirement I19-E31 and 157 index 155 appear as three separate identifiers; 印刷版核選序號 is declared 「UNKNOWN（現有檔案資料庫尚未證明…）」 rather than guessed; gate rule 1 makes conflation of these IDs a reject condition. Matches the crosswalk row and Blueprint B."
    },
    {
      "id": "C02_official_4pt_label_reading",
      "result": "PASS",
      "locator": "報告基本資訊 表「官方第 9 頁 4 分標註」；§貳-一 「評分級距非權重或得分」",
      "evidence": "Text states the 4分 sits in the 1–5 計分級距 on the page-9 extract with no weight column and expressly refuses to convert it into a weight, an association self-score or an evaluator-granted score (Official score = NOT_ASSIGNED). This matches OFFICIAL_SOURCE_PAGE9_EXCERPT.txt, whose tier list carries no weight column."
    },
    {
      "id": "C03_genre_and_title_blind_identification",
      "result": "PASS",
      "locator": "Whole document; §壹 / §參 / §陸 / §柒 / §捌",
      "evidence": "Title-blind, the body reads as a three-period customer-satisfaction survey-and-analysis report with comparability protocol, instrument, statistics, chart, limitations and a proposal loop. It is not a scoring sheet, blank questionnaire, information-system usage report, licensing/employment report or revenue report."
    },
    {
      "id": "C04_blueprint_D_coverage",
      "result": "PASS",
      "locator": "壹 (D1/D2), 參 (D3), 肆 (D4), 伍 (D5), 陸 (D6), 柒 (D7), 捌 (D8/D9), 拾壹 附錄一–五 (D10)",
      "evidence": "Cover/status with SAMPLE/SYNTHETIC and REAL UNKNOWN/HOLD; executive figures with denominators and weakest dimension; audience/cohort/frame/denominator and four comparability conditions; dispatch, two-reminder cap, day-5 close, dedup, invalidity, no-imputation, per-item n and the 5/6 individual-index rule; full 1–5 anchors plus N/A and 8 items with metadata fields; counts, six-item means with n=12, separate Q7 mean and Top-2, multi-period table and same-axis line chart; three delta comparisons with weakest item and limits; two retrospective proposals with IDs, role, check window, success measure, HOLD/REVISE and NOT_ADOPTED/NOT_EXECUTED status; CONTINUE/CHANGE/HOLD table; blank printable form, filled example, 36 rows, dictionary/formulas, register template and revision record."
    },
    {
      "id": "C05_frozen_wording_and_normalization_note",
      "result": "PASS",
      "locator": "§伍-二 題項表; 附錄一 題項表; 附錄二 表下註; 附錄四 題項標籤對照表 及其後說明",
      "evidence": "R05 minor finding 1 is resolved: 附錄二 now carries 「Q1–Q7 題目文字逐字取自凍結版題項檔 QUESTIONNAIRE_ITEMS_0141_R01.csv。該 CSV 以正規化後之題目字串儲存，未含中文列舉頓號與句末標點；列印用正式題項文字見第伍章與附錄一」 and 附錄四 repeats the same sentence, so the two renderings no longer compete for authority. The appendix cells are byte-identical to the CSV (e.g. Q2 「課程內容能對應我預計運用的工作志工或學習情境」, Q3 「講師的說明示範與回應有助於我理解課程」); §伍/附錄一 carry the printable punctuated form."
    },
    {
      "id": "C06_scale_NA_and_missing_data_rules",
      "result": "PASS",
      "locator": "§伍-一 量尺標準定義；§肆-二-3；§玖 規則5",
      "evidence": "1–5 anchors are defined with wording, N/A is excluded from that item's denominator, blanks are never imputed or scored zero, an item-specific valid n is required, and a personal six-item composite requires at least 5 of 6 valid answers while single-item answers stay usable. Gate rule 5 makes zeroing/imputation a data-pollution reject."
    },
    {
      "id": "C07_denominators_and_return_rate",
      "result": "PASS",
      "locator": "§參-二 「有效回收率 = 有效回覆份數 ÷ 實際發出之有效邀請份數 × 100%」; §陸-一 表; 附錄四 公式區",
      "evidence": "Per-year 15 invited / 12 valid = 80.00%, three-year 45 / 36 / 80.00%. Denominators are the issued invitations, with an express prohibition on using all members or cumulative trainees as a denominator; gate rules 4 and 7 make missing denominators and disappearance of nonrespondents reject conditions."
    },
    {
      "id": "C08_q1_q6_index_separate_from_q7",
      "result": "PASS",
      "locator": "§陸-一 欄名「Q1–Q6 六構面有效填答次數」與其說明; §陸-二 六構面綜合均值列與 Q7 列; 附錄四 六構面綜合指數公式",
      "evidence": "R05 minor finding 2 is resolved at the point of risk: the column is renamed Q1–Q6 and the note states 「Q7 整體滿意度為獨立題，另按每年 12 份計算，不列入本欄」. 附錄四 defines pooled index as Q1–Q6 only, excludes Q7, and requires the pooled ratio (not the mean of six means) once item n differ. Residual terminology is the separate minor finding 2."
    },
    {
      "id": "C09_aggregate_math_recomputed",
      "result": "PASS",
      "locator": "§陸-二 逐題表; §壹-一-2/3; §柒-一-1/2/3/4/5",
      "evidence": "Recomputed from the 36 CSV rows without using the R01 period summary: 2023 Q1 42/12=3.5000, Q2 41/12=3.4167, Q3 3.5000, Q4 3.5833, Q5 42/12=3.5000, Q6 41/12=3.4167, Q7 43/12=3.5833; 2024 Q5 48/12=4.0000, Q7 47/12=3.9167; 2025 Q2 47/12=3.9167, Q5 51/12=4.2500, Q7 51/12=4.2500; pooled 251/72=3.4861, 257/72=3.5694, 266/72=3.6944. Deltas +0.0833/+0.1250/+0.2083 (index), Q5 +0.5000/+0.2500/+0.7500, Q2 0/+0.5000/+0.5000, Q7 +0.3333/+0.3333/+0.6667 all match the tables. Sensitivity 2/12=0.1667 points (§柒-二-1) is correct."
    },
    {
      "id": "C10_q7_top2_table_internal_consistency",
      "result": "PASS",
      "locator": "§陸-三 表與 計算註; 附錄四 Top-2 公式",
      "evidence": "Recomputed counts: 2023 5 of 1–3 / 7 of 4 / 0 of 5 → 7 (58.33%); 2024 2/9/1 → 10 (83.33%); 2025 1/7/4 → 11 (91.67%); 全期變化 −4 / 0 / +4 / +4 and +25.00 pp, +8.33 pp, +33.33 pp all correct. The 計算註 correctly warns that subtracting the rounded 91.67%−83.33% would give 8.34 rather than the unrounded 8.33 pp."
    },
    {
      "id": "C11_chart_scope_and_axis_disclosure",
      "result": "PASS",
      "locator": "§陸-四 說明與 圖說註記",
      "evidence": "The caption states the chart plots the pooled Q1–Q6 index, Q7 and the Q2/Q5/Q6 series on one shared 1–5 axis, discloses that Q1/Q3/Q4 appear only in the item table, and expressly forbids reading the pooled line as any single item or as Q7. Single embedded image with a build-receipt/technical-receipt SHA (83353077…) — receipt metadata, not pixels I saw."
    },
    {
      "id": "C12_retrospective_proposal_framing",
      "result": "PASS",
      "locator": "§捌 preamble；方案一/方案二 「方案性質」「對應期別轉折（回溯對照）」「回查檢驗期程」",
      "evidence": "R05 minor finding 3's timing half remains resolved: both items are declared retrospective demonstrations and the text says 「不存在『先提案、後改善、再看到分數上升』的時序」; check windows are 「尚未發生；下一個可比較週期屬未來工作」 with the 10-working-day figure labelled a SAMPLE parameter; status is SAMPLE_HYPOTHETICAL_NOT_ADOPTED."
    },
    {
      "id": "C13_q5_unsupported_qualitative_condition",
      "result": "PASS",
      "locator": "§捌 方案一 「具體成效檢驗指標」；「提案數據依據」",
      "evidence": "R05 minor finding 3 is resolved: the complaint clause is removed from the measurable threshold, Q5 mean ≥3.8000 is declared the sole measurable success threshold, and the discarded qualitative condition is marked UNKNOWN‑sourced with an explicit bar on inferring absence of complaints from empty SAMPLE Q8 cells. 提案數據依據 likewise states Q8 has no text and that 「信件混亂」/「回信窗口不一」 are not supported. Searchability caveat is minor finding 4."
    },
    {
      "id": "C14_item_level_top2_denominator_defined",
      "result": "PASS",
      "locator": "附錄四-2 「單題 Top-2 正面滿意率（Item-level Top-2 Proportion）」；§捌 方案二 指標",
      "evidence": "R05 minor finding 4 remains resolved: the general Qk formula restricts numerator and denominator to that item's valid answers, excludes invitation counts, total responses and other items, states 方案二 uses the Q2-specific denominator, and states Q7 keeps its own formula. Baseline transparency is the separate minor finding 3."
    },
    {
      "id": "C15_label_consistency",
      "result": "PASS",
      "locator": "§柒-一 首句；§陸-二 列標籤；§壹-一-4；附錄四 題項標籤對照表",
      "evidence": "R05 minor finding 4 is resolved: §壹 now reads 「Q5 行政溝通」「Q2 情境對應」「Q6 環境設備」, matching §柒-一's declared single label set (需求契合、情境對應、師資支援、教材資源、行政溝通、環境設備、整體滿意) and 附錄四's frozen mapping (Q4＝教材資源, Q6＝環境設備). No residual alias strings for Q2/Q5/Q6 were found in the reviewed text."
    },
    {
      "id": "C16_sample_real_boundary",
      "result": "PASS",
      "locator": "報告基本資訊 表；§壹-二；§陸-一 資料屬性欄；附錄二；附錄三 狀態欄；附錄五；結尾句",
      "evidence": "SAMPLE/SYNTHETIC is declared at document level and per table row; all 36 rows carry record_state=SAMPLE_SYNTHETIC with Q8 marker text; 附錄二 is declared outside the 36 rows and outside computation; REAL = UNKNOWN/HOLD; no invented approval, signature, certificate, complaint log, meeting decision or performance result appears anywhere in the text."
    },
    {
      "id": "C17_current_vs_real_vs_formal_acceptance",
      "result": "PASS",
      "locator": "§拾-一 流程圖 步驟4–5 與終端框；§拾-一-4；§拾-二-4；結尾句",
      "evidence": "R05 minor finding 6 remains resolved and the 「不可逆對照表」 residual gap is closed: step 3 now requires a 檔案版本／SHA-256／筆數清冊(manifest); step 4 states computation does not auto-promote or change data nature; step 5 is an authorised-role CURRENT gate; terminal box reads 「CURRENT ≠ REAL，也不等於正式接受（formal acceptance）」 and the closing line states REAL=UNKNOWN/HOLD, Human formal acceptance=NOT_GRANTED, Official score=NOT_ASSIGNED."
    },
    {
      "id": "C18_neighbor_requirement_rejection",
      "result": "PASS",
      "locator": "§貳-二 排除表; §玖 規則10; 附錄五 文件／要求 對照表",
      "evidence": "0139/I19-E29 (index 153, licensing/employment), 0140/I19-E30 (154, system uptake) and 0142/I19-E32 (156, revenue) are excluded by construct and substitution is made a reject condition, so a licensing/employment rate, LMS login rate or revenue figure cannot satisfy 「顧客滿意度提升」 and this document cannot be substituted for them."
    },
    {
      "id": "C19_gate_and_hold_rules_complete",
      "result": "PASS",
      "locator": "§玖 13 條；§參-三 可比性表; 次期資料判讀與處置表",
      "evidence": "All 13 Blueprint-I conditions are represented (ID conflation, blank template, scale/wording change with TREND_NOT_COMPARABLE_HOLD, missing denominator, N/A-as-zero or imputation, Likert delta mislabelled as percent growth, unexplained nonresponse, unstratified segment blending, synthetic-as-real, construct substitution, uncited causality, missing owner/checkpoint/HOLD, missing SHA/source trace), and the CONTINUE/CHANGE/HOLD table attaches required evidence to each branch."
    },
    {
      "id": "C20_dataset_and_register_alignment",
      "result": "PASS",
      "locator": "附錄二 表; 附錄三 36 列; 報告基本資訊 「報告版本與合成事實識別碼」; 附錄四 sample_case_id 定義",
      "evidence": "附錄三 reproduces all 36 CSV rows (status, year, cohort, case ID SYN-0141-YYYY-NNN, date, segment, Q1→Q7 string, Q8 marker) with no divergence from SAMPLE_SURVEY_RESPONSES_0141_R01.csv found on inspection; the dataset-level ID FACT-SYN-0141-SAT-TREND-R01 is expressly not to be used as a row ID, and row fact IDs equal base + -YYYY-NNN, matching the R06 register's 36 row facts. 附錄二's answers 4,5,3,4,5,3,4 match FACT-SYN-0141-Q8-VIGNETTE. Sidecar locator language is the separate minor finding 1."
    },
    {
      "id": "C21_R05_finding_1_punctuation",
      "result": "RESOLVED",
      "locator": "附錄二 表下註; 附錄四 標籤表後說明",
      "evidence": "Normalization note added in both places, naming the CSV as the normalized source and §伍/附錄一 as the printable canonical wording; semantics unchanged."
    },
    {
      "id": "C22_R05_finding_2_column_name",
      "result": "RESOLVED",
      "locator": "§陸-一 欄名與說明",
      "evidence": "Column renamed 「Q1–Q6 六構面有效填答次數」 (72/72/72/216) with the Q7 exclusion stated immediately beneath; arithmetic no longer invites a 7×12=84 misreading."
    },
    {
      "id": "C23_R05_finding_3_q5_criterion",
      "result": "RESOLVED",
      "locator": "§捌 方案一 具體成效檢驗指標",
      "evidence": "Qualitative complaint condition removed from the measurable threshold and labelled UNKNOWN‑sourced with an explicit evidence requirement before future use; see C13."
    },
    {
      "id": "C24_R05_finding_4_labels",
      "result": "RESOLVED",
      "locator": "§壹-一-4",
      "evidence": "Executive bullets now use the frozen short labels with item IDs (Q5 行政溝通, Q2 情境對應, Q6 環境設備); see C15."
    },
    {
      "id": "C25_R05_finding_5_register_locators",
      "result": "PARTIAL",
      "locator": "SAMPLE_REPLACEMENT_REGISTER_0141_R06.csv",
      "evidence": "The eight non-row facts were re-pointed to MANUSCRIPT_0141_R06_CANDIDATE.md with Chinese locators; the 36 row-level locators remain English and retain the imprecise 「section 6 aggregates derive from this row」. Sidecar-only and byte-neutral for the DOCX — recorded as minor finding 1, not a document defect."
    },
    {
      "id": "C26_no_causality_no_percent_growth",
      "result": "PASS",
      "locator": "§壹-一 各趨勢句; §貳-二; §陸-二 重要說明; §柒-一 全部; §柒-二-2/3; §玖 規則6/11",
      "evidence": "Every Likert change is reported in scale points, with explicit 「絕不可宣稱為百分比成長率」 and 「嚴禁計算百分比變更」; no passage claims the two proposals caused the Q5/Q2/Q7 movement; Hawthorne/self-selection/external-shift confounds are named and causality is blocked in §柒-二-3 and gate rule 11."
    },
    {
      "id": "C27_privacy_and_small_cell_scoping",
      "result": "PASS",
      "locator": "§參-四; §拾-一-2; §拾-二-1",
      "evidence": "Anonymisation, the n<5 suppression figure, retention period and access roles are all presented as SAMPLE proposals explicitly not law, not association policy and not completed privacy work; 保存期限 is `UNKNOWN / REFER_TO_APPROVED_POLICY`; no real personal data or re-identification key handling is asserted as existing."
    },
    {
      "id": "C28_receipt_sha_binding_metadata",
      "result": "PASS",
      "locator": "Packet receipts (read as metadata only)",
      "evidence": "Text SHA b9d23ec3… is declared bound to DOCX e2a5a981… by the technical QA receipt; the Word render receipt records identical docx SHA before/after with 25 pages and read_only=true; the visual receipt (6a94d19e…) is bound to the same DOCX and PDF c3a52474…; the math receipt binds manuscript 2c374341…, register 862df595… and questionnaire/responses 72325919…/310745e5…; build and repair receipts bind the same DOCX and layout patch. These are supplied receipt claims, not my own native verification, and none of them grants acceptance."
    }
  ],
  "review_scope": {
    "mode": "SEMANTIC_TEXT_ONLY",
    "target": "doc_id 0141 / requirement I19-E31 / 157 index 155 / candidate R06 (CANDIDATE only — not CURRENT, not REAL, not formally accepted)",
    "inspected": "Only the text asserted to belong to DOCX SHA-256 e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2 (text SHA-256 b9d23ec3a917c13a3824a5f06a41f44a7be5f9d848d1f3537d1c8a22933b9416), plus the supplied official/source/blueprint/crosswalk artefacts and sidecar CSVs. No DOCX binary, Word COM render, page image, PDF text layer or chart pixel was inspected by this review.",
    "independent_work": "Every published aggregate was recomputed directly from the 36 data rows of SAMPLE_SURVEY_RESPONSES_0141_R01.csv (sha256 723259199…): per-item sums and means, the three pooled Q1–Q6 ratios, Q7 means, Q7 Top-2 counts/rates and the 1–3/4/5 rows, all point deltas, the percentage-point deltas, return rates and the 15/12, 45/36, 72/216 and 2/12 sensitivity figures; additionally the item-level Q2 Top-2 series (2023 5/12=41.67%, 2024 5/12=41.67%, 2025 9/12=75.00%) was computed to test the 方案二 threshold and is not published in the document.",
    "receipt_use": "The R06 build, math-QA, technical-QA, Word-render, visual and repair/layout receipts and the R05 review plus its receipt were read only as surrounding evidence with their stated SHAs; none of their PASS verdicts is inherited, and the visual receipt's page coverage is reported as its own claim rather than as my observation.",
    "not_inherited": "R05 exact-SHA PASS (docx 3e9e6eef…, reviewer response 39a50ae2…) and its five minor findings were re-verified against the R06 text and sidecars, not carried forward as a verdict for this SHA.",
    "status_boundaries": "REAL evidence = UNKNOWN/HOLD; Official score = NOT_ASSIGNED; Human formal acceptance = NOT_GRANTED; association acceptance not granted. This PASS is semantic-only for the exact SHA above and promotes nothing."
  },
  "not_reviewed": [
    "DOCX binary, OOXML validity, native table geometry, section/orientation handling and embedded image bytes — covered by the technical QA receipt, not re-adjudicated here.",
    "Word rendering, pagination, font floors, chart legibility and clipping — covered by the Word render and visual receipts (PASS claims, 25 pages, 8 full-resolution pages), not verified by me.",
    "Whether the U+2011 token actually stays on one page in Word — the layout patch and visual receipts assert this; my review only notes the resulting searchability side-effect.",
    "Truthfulness of the official page-9 label beyond the supplied excerpt (no weight column visible); the printed checkbox serial remains UNKNOWN and is only an authoritative printed source question.",
    "Any content of adjacent deliverables 0139/0140/0142 beyond the crosswalk neighbour rows used for construct-distinction checking.",
    "Whether the n<5 small-cell figure, retention period, or any SOP parameter is acceptable association policy — all are declared SAMPLE proposals with real status UNKNOWN."
  ],
  "real_data_status": "UNKNOWN/HOLD — every year, invitation count, response, score, date, cohort, comment and proposal in this candidate is SAMPLE/SYNTHETIC; Q8 is empty across all 36 rows; authorised roles, retention period, access control and privacy thresholds are deferred to approved policy; SAMPLE cannot become REAL by computation, formatting or this review.",
  "formal_acceptance_status": "NOT_GRANTED — CANDIDATE only. Official score NOT_ASSIGNED; Human formal acceptance and association acceptance not granted; this semantic PASS neither promotes the document to CURRENT nor converts any synthetic figure into real evidence."
}
```