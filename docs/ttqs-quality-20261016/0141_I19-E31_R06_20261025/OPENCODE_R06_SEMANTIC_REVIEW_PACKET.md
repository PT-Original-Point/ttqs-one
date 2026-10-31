# TTQS ONE Independent Semantic Review Packet — 0141 R06

Review target: doc_id 0141; official requirement I19-E31; 157-item index 155; printed checkbox serial UNKNOWN. This is a CANDIDATE only. DOCX SHA-256: `e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2`. Exact text extracted from that DOCX SHA-256: `b9d23ec3a917c13a3824a5f06a41f44a7be5f9d848d1f3537d1c8a22933b9416`. Do not merge any verdict from another candidate SHA.

## Review instructions

You are the independent semantic reviewer, not the Builder. Review the supplied full exact-candidate text and evidence against the complete official requirement, official source excerpt, unique Blueprint R02, source packet R02, crosswalk and nearest-neighbor requirements. Recalculate key published figures against the 36-row synthetic source CSV and summary. Compare each R05 exact-SHA minor finding to the R06 text and receipts; do not inherit R05 PASS. Check genre/use, actual operational usability, frozen Q1–Q7 wording and normalization notes, Q1–Q6 denominator separate from Q7, the Q5 proposal’s unsupported qualitative complaint condition remains UNKNOWN and is not inferred from empty sample responses, exact labels, math, register locators/fact IDs, real-data and human-acceptance boundaries, potential cross-document mismatch, and whether body text still fits its declared requirement rather than a nearest neighbor.

For every finding, cite exact section/table/appendix and quote only the minimum locator. Check Word render receipt as supplied evidence; do not claim to have seen pixels yourself. A separate visual review receipt covers all 25 rendered pages and full-resolution samples; verify its exact SHA binding as metadata. Do not call tools or edit files. Return one JSON object with keys: `doc_id`, `requirement_id`, `candidate_docx_sha256`, `text_sha256`, `verdict` (`PASS`, `PARTIAL`, or `FAIL`), `major_findings`, `minor_findings`, `checks` (each has `id`, `result`, `locator`, `evidence`), `review_scope`, `not_reviewed`, `real_data_status`, `formal_acceptance_status`. Distinguish textual reviewer opinion from native receipts and from association acceptance. If any mandatory requirement lacks a usable field, procedure, evidence, calculation, hold/reject rule, mark PARTIAL/FAIL rather than relying on document length. Keep SAMPLE/SYNTHETIC distinct from REAL; no invented approval or performance claim.

## Prior R05 exact-SHA review — findings to verify, not inherited

R05 reviewed DOCX SHA `3e9e6eef2769617dc4d515bb0d9abfa363a46e217b13b7c261b279306ced17d8` with verdict `PASS`. Original R05 response SHA-256: `39a50ae2c2d292155479e2c966f30c86731fc82d548451827635cf56300d78bc`.

### Original reviewer response

```json
{
  "reviewed_docx_sha256": "3e9e6eef2769617dc4d515bb0d9abfa363a46e217b13b7c261b279306ced17d8",
  "reviewed_text_sha256": "c13c350eb8fce0f891d36dc64c15682433b668df976708456d9e71ae31f59328",
  "verdict": "PASS",
  "review_scope": {
    "mode": "SEMANTIC_TEXT_ONLY",
    "target": "doc_id 0141 / requirement I19-E31 / 157 index 155 / candidate R05 (CANDIDATE, not CURRENT, not REAL, not formally accepted)",
    "inspected": "Only the extracted text asserted to belong to DOCX SHA-256 3e9e6eef2769617dc4d515bb0d9abfa363a46e217b13b7c261b279306ced17d8 (text SHA-256 c13c350e…). No DOCX binary, Word COM render, page image, PDF text layer or chart pixel was inspected by this review.",
    "independent_work": "Recalculated every published figure directly from the 36 data rows of SAMPLE_SURVEY_RESPONSES_0141_R01.csv (SHA-256 72325919…): per-item sums and means, pooled six-item ratios, Q7 means, Q7 Top-2 counts/rates, all point deltas and percentage-point deltas, return rates, the 72/216 valid-answer counts and the n=12 sensitivity figure. The R05 math/technical/visual receipts were read only as claimed surrounding evidence, not as my own findings.",
    "compared_against": [
      "OFFICIAL_REQUIREMENT_ROW_I19-E31.json (d18d41bd…)",
      "OFFICIAL_SOURCE_PAGE9_EXCERPT.txt (0733c1e3…)",
      "CROSSWALK_ROW_0141_AND_NEIGHBORS.json (d09422ce…), including I19-E29/E30/E32 neighbours",
      "UNIQUE_BLUEPRINT_0141_I19-E31_R02.md (e1976164…)",
      "SOURCE_PACKET_0141_I19-E31_R02.md (43c0e1bd…)",
      "QUESTIONNAIRE_ITEMS_0141_R01.csv (310745e5…)",
      "SAMPLE_PERIOD_SUMMARY_0141_R01.csv (537c39dc…)",
      "SAMPLE_REPLACEMENT_REGISTER_0141_R05.csv (5fff0f9b…)"
    ],
    "not_inherited": "The prior exact-SHA R04 PASS (a0dfec32…) and its six minor findings were treated as context to be re-verified, not as a verdict for this SHA.",
    "not_adjudicated": "Word-native layout/pagination, chart geometry, font floors and the 25-page visual receipt (5076475e…) are a separate lane; they are corroborating context only and are not re-adjudicated here.",
    "status_boundaries": "REAL evidence = UNKNOWN/HOLD; Official score = NOT_ASSIGNED; Human formal acceptance = NOT_GRANTED. This PASS is semantic-only for the exact SHA above and promotes nothing."
  },
  "requirement_mapping": {
    "official_requirement": "I19-E31, indicator 19, official criterion 「顧客滿意度提升。」, source = TTQS training-institution scoring evidence table, physical PDF page 9 (page extraction SHA 945949f3…).",
    "official_label_reading": "「4分」 appears inside the 1–5 計分標準 tier list on the page-9 extract; the extract shows no weight column. The document states this correctly at §貳-一 and in the 報告基本資訊 table (「將 4 分列在 1–5 分計分級距中，未顯示為權重欄」), and does not assert a weight, an association score or evaluator-granted points.",
    "identity_triangulation": "doc_id 0141, requirement I19-E31 and 157 index 155 are carried as three distinct identifiers in the header table, §貳-一 and 附錄五-2; printed checkbox serial is declared UNKNOWN rather than guessed.",
    "title_provenance": "The title 「顧客滿意度趨勢調查與分析報告」 is attributed to the 129→142 crosswalk I19-E31/0141 row and explicitly not to the page-9 PDF text (header table 「文件名稱來源」) — matches the crosswalk row and the Blueprint B note.",
    "blueprint_D_coverage": {
      "cover_status_D1": "Header table + 壹 declares whole-document SAMPLE/SYNTHETIC and REAL=UNKNOWN/HOLD.",
      "executive_finding_D2": "§壹-一/二 give three-period means, 15/12 denominators, Q6 as weakest dimension, interpretation and limits.",
      "comparability_protocol_D3": "§參-I/II/III/IV: audience definition, single synthetic segment, invitation-unit denominator rule, four comparability conditions, small-cell SAMPLE caveat.",
      "administration_SOP_D4": "§肆-I/II: dispatch timing, two-reminder cap, close at day 5, dedup, invalidity rules, no-imputation, item-specific valid n, 5/6 personal-index threshold.",
      "questionnaire_D5": "§伍-一/二: full 1–5 anchor definitions, N/A handling, 8 items with metadata fields; Q8 explicitly excluded from numeric means.",
      "results_D6": "§陸-I/II/III/IV: invitation/valid/return counts, six item means with n=12, separate Q7 mean and Top-2 table, multi-period table and same-axis line chart with caption note.",
      "interpretation_D7": "§柒-一/二: 2023→2024, 2024→2025 and baseline→final deltas, weakest item Q6, sample-size sensitivity, no-causality and single-segment limitations.",
      "sample_loop_D8": "§捌: two proposals with IDs, retrospective framing, proposed role, future check window, success measure, HOLD/REVISE rule, NOT_ADOPTED/NOT_EXECUTED status.",
      "limitations_decision_D9": "§捌 次期資料判讀與處置表 (CONTINUE/CHANGE/HOLD with required evidence) plus §柒-二.",
      "appendices_D10": "附錄一 blank printable form, 附錄二 filled SAMPLE example, 附錄三 36-row dataset, 附錄四 dictionary/formulas/label table, 附錄五 register template and revision history."
    },
    "blueprint_I_reject_checks": "None of the 13 reject/hold conditions is triggered by this text: IDs are not conflated; a filled SAMPLE example plus 36 rows exist; scale/wording held constant with an explicit TREND_NOT_COMPARABLE_HOLD rule; denominators and per-item n stated; N/A/blank not imputed or zeroed; Likert deltas labelled in points, not percent growth; nonresponse handled by invitation denominator and gate rule 7; segment blending prohibited; synthetic status labelled on every table; satisfaction not substituted for licensing/employment/system-use/revenue; causality explicitly barred; owner roles, checkpoints and HOLD rules supplied; SHA/source locators attached."
  },
  "document_genre_and_usability": {
    "genre": "調査與分析報告 (survey and analysis report) — not a scoring sheet, not a blank questionnaire, not an information-system uptake report, not a licensing/employment report, not a revenue report.",
    "title_blind_identification": "Reading only the body, an evaluator would identify a three-period customer-satisfaction trend report with protocol, instrument, statistics, limits and a proposal loop.",
    "practical_field_usability": "Usable before launch: the invitation unit and denominator rule (§參-II), dispatch/reminder/close timings (§肆-I), dedup and invalidity rules (§肆-II), the printable blank form (附錄一) and the filled example (附錄二) are all present. The 附錄四 dictionary now carries record_state, response_date_synthetic and customer_segment with vocabularies, so a future REAL export can be validated against the dictionary rather than the raw CSV header.",
    "evaluator_facing_readability": "Sections are numbered and cross-referenced (柒-一 points to 附錄四's label table; 方案二 points to 附錄四's item-level Top-2 formula; 陸-四's caption disambiguates the pooled index from any single item). Warning blocks and SAMPLE labels appear on every results table.",
    "label_consistency": "Short labels 需求契合/情境對應/師資支援/教材資源/行政溝通/環境設備/整體滿意 are used in §陸-二, §柒-一 and 附錄四, and §柒-一 now states that these are the single label source with no new aliases; 附錄四 fixes Q4＝教材資源 and Q6＝環境設備. Residual descriptive parentheticals in §壹-四 (e.g. 「Q5（行政溝通與課前通知）」, 「Q6（學習環境與設備）」) are the only remaining alias-like strings — cosmetic, see minor finding 4."
  },
  "sample_real_boundary": {
    "labelling": "Header table, §壹, §陸-I, 附錄二, 附錄三 row column 「資料屬性狀態」 and 附錄五 all state SAMPLE/SYNTHETIC; every 36 rows carries record_state=SAMPLE_SYNTHETIC and Q8='SAMPLE_ONLY; no actual respondent text'.",
    "real_status": "REAL = UNKNOWN / HOLD in the header table, §拾-二-1 and the closing line; 保存期限 UNKNOWN / REFER_TO_APPROVED_POLICY.",
    "authority_boundary": "§捌 次期 table step 3 (由協會實際授權人員決定) plus §拾-一 step 5 and §拾-二-4 state that computation alone never promotes: 「CURRENT ≠ REAL，也不等於正式接受」 and 「Human formal acceptance 未授予」. No meeting decision, signature, approval, certificate, third-party original or external achievement is fabricated.",
    "synthetic_segment": "Exactly one segment (TRAINING_PARTICIPANT_SYNTHETIC) exists in the 36 rows; §參-I and §柒-二-4 state that no corporate-client or other segment is surveyed and that no segment comparison may be drawn. No unsupported inference to other segments is made.",
    "no_causality": "§壹-二, §柒-一-5, §柒-二-3 and gate rule 11 bar any claim that the two proposals caused the Q5/Q2/Q7 movement; the proposals are labelled retrospective demonstrations with NOT_ADOPTED/NOT_EXECUTED status."
  },
  "math_and_data": {
    "method": "Recomputed from the 36 raw rows without using the R01 period summary or the R05 math receipt as authority.",
    "per_item_means_recomputed": {
      "2023": "Q1 42/12=3.5000; Q2 41/12=3.4167; Q3 42/12=3.5000; Q4 43/12=3.5833; Q5 42/12=3.5000; Q6 41/12=3.4167; Q7 43/12=3.5833",
      "2024": "Q1 3.5000; Q2 3.4167; Q3 3.5000; Q4 3.5833; Q5 48/12=4.0000; Q6 3.4167; Q7 47/12=3.9167",
      "2025": "Q1 3.5000; Q2 47/12=3.9167; Q3 3.5000; Q4 3.5833; Q5 51/12=4.2500; Q6 3.4167; Q7 51/12=4.2500"
    },
    "pooled_index_recomputed": "2023 251/72=3.4861; 2024 257/72=3.5694; 2025 266/72=3.6944 — matches §陸-二 六構面綜合均值 row and §壹-一-2/§柒-一-1.",
    "q7_top2_recomputed": "2023 7/12=58.33% (5 of 1–3, 7 of 4, 0 of 5); 2024 10/12=83.33% (2/9/1); 2025 11/12=91.67% (1/7/4) — matches §陸-三 including the 1–3/4/5 count columns and the 全期變化 row (-4 / 0 / +4).",
    "deltas_recomputed": "Pooled 2023→2024 +0.0833, 2024→2025 +0.1250, 2023→2025 +0.2083; Q7 +0.3333 / +0.3333 / +0.6667; Q5 +0.5000 / +0.2500 / +0.7500; Q2 +0.0000 / +0.5000 / +0.5000 — all match §陸-二 and §柒-一.",
    "percentage_points": "83.33−58.33=+25.00 pp; 91.67−83.33=+8.33 pp (unrounded 11/12−10/12=8.3333); full span +33.33 pp — matches §陸-三 and the 計算註 note.",
    "denominators": "15 invited / 12 valid per year = 80.00% (12/15); three-year totals 45 / 36 / 80.00%; Q1–Q6 valid answers 6×12=72 per year and 216 in total; every item n=12 — consistent with §陸-I and the 說明 under it.",
    "sensitivity": "2/12=0.1667 points (§柒-二-1) is arithmetically correct.",
    "pooled_vs_mean_of_means": "Because all item n=12, the pooled ratio equals the arithmetic mean of the six item means (251/72 etc.); 附錄四 states this equality and requires the pooled ratio instead once item n differ — correct and Blueprint-conformant.",
    "dataset_integrity": "附錄三 reproduces all 36 rows with IDs SYN-0141-YYYY-NNN, dates 2023-01-20…2025-12-20, cohort IDs and segment marks matching the canonical CSV; 附錄二 is declared outside the 36 rows and its answers (4,5,3,4,5,3,4) match FACT-SYN-0141-Q8-VIGNETTE.",
    "discrepancies_found": "None numeric. No percentage-growth mislabelling of Likert deltas occurs; no N/A or blank is scored as zero; no imputation is proposed."
  },
  "cross_document_identity": {
    "dataset_vs_per_row_ids": "Header table 「報告版本與合成事實識別碼」 and 附錄四's sample_case_id entry define the dataset-level ID FACT-SYN-0141-SAT-TREND-R01 and the per-row ID as dataset ID + '-YYYY-NNN', stating that the dataset ID must not be used as a row ID. This matches the 36 per-row fact_ids in SAMPLE_REPLACEMENT_REGISTER_0141_R05.csv (5fff0f9b…) and removes the R04 sidecar/report mismatch.",
    "shared_facts": "No shared real trainees, cohorts, years, rates or narrative are asserted with 0139/0140/0142; the adjacent documents appear only as exclusion boundaries (§貳-二 table and register related_docs).",
    "source_lineage": "The DOCX cites the canonical R01 CSV by name and SHA (附錄五: 72325919…) and states that R05 is a text revision, not a new dataset (版本界線 note). Sidecar register locator/lineage residue is noted as minor finding 5.",
    "no_cross_construct_metrics": "No employment, licensing, system-uptake or revenue metric is imported or blended into the satisfaction series."
  },
  "neighboring_requirement_differentiation": {
    "guard_present": "§貳-二 negative-neighbour guard and 附錄五 文件/要求 table pair 0141 with E29 (licensing/employment), E30 (information-system uptake), E32 (revenue) and state each is a different proof construct.",
    "negative_neighbour_rejection": "Feeding a licensing/employment rate, LMS login/download rate or revenue figure as evidence of 「顧客滿意度提升」 would be visibly rejected by this document, so it cannot be substituted for 0139/0140/0142 nor they for it.",
    "index_and_id_separation": "Index 155 is described as 「顧客滿意度上升：多期同量尺統計」 and kept distinct from the requirement ID and doc ID; the 4分 tier is not converted into an association score."
  },
  "r04_findings_resolution": [
    {
      "prior_finding": 1,
      "topic": "附錄二 Q1–Q7 題目 wording vs frozen instrument",
      "status": "RESOLVED_WITH_RESIDUAL_COSMETIC_NOTE",
      "body_locator": "附錄二 表「題號/題目（逐字引用凍結題項）」 Q1–Q7 rows, plus the note under the table",
      "evidence": "Appendix II now reads 本次訓練服務內容符合我在報名前表達的需求 / 課程內容能對應我預計運用的工作志工或學習情境 / … and is byte-identical to QUESTIONNAIRE_ITEMS_0141_R01.csv, with an explicit note naming that CSV as the frozen item file. Semantic content is now identical to §伍 and 附錄一; only punctuation/whitespace normalization differs (see minor finding 1).",
      "note": "The prior defect (paraphrased questions in a document presented as a completed record) is gone; remaining divergence is punctuation-level."
    },
    {
      "prior_finding": 2,
      "topic": "Dimension-label drift in §柒",
      "status": "RESOLVED",
      "body_locator": "§柒-一 opening sentence; §陸-二 row labels; 附錄四 題項標籤對照表",
      "evidence": "§柒-一 now declares the short-label set (需求契合、情境對應、師資支援、教材資源、行政溝通、環境設備、整體滿意) as the single source, and uses Q4（教材資源）, Q6（環境設備）; 附錄四 states 「Q4＝教材資源、Q6＝環境設備」 and maps each label to its CSV column and frozen text. 教材實用度/環境設備與線上平台 style drift is gone."
    },
    {
      "prior_finding": 3,
      "topic": "Retrospective vs future timing of the two SAMPLE proposals",
      "status": "RESOLVED",
      "body_locator": "§捌 preamble; 方案一 「方案性質」「對應期別轉折（回溯對照）」「回查檢驗期程」; 方案二 same fields",
      "evidence": "The preamble states both items are retrospective demonstrations on the completed 2023–2025 synthetic series and that 「不存在『先提案、後改善、再看到分數上升』的時序」. 方案一 anchors 2023→2025 and cites Q5 3.5000→4.2500 as a 累計量尺點差, not a before/after effect; 方案二 anchors 2024→2025 and cites Q2 3.4167→3.9167. Check windows are stated as not yet occurred and future-only, with the 10-working-day figure labelled a SAMPLE parameter."
    },
    {
      "prior_finding": 4,
      "topic": "Item-level Top-2 denominator for 方案二's 75% threshold",
      "status": "RESOLVED",
      "body_locator": "附錄四-2 「單題 Top-2 正面滿意率（Item-level Top-2 Proportion）」; 方案二 「具體成效檢驗指標」",
      "evidence": "A general item-level formula is added (分子/分母 both restricted to Qk valid answers, excluding N/A and blanks, not invitation count, not other items), with an explicit sentence that 方案二's Q2 Top-2 uses this Q2-specific denominator and that Q7 keeps its own formula. 方案二 now reads 「Top-2 佔比應突破 75%（分母為 Q2 自身有效回答數，見附錄四單題 Top-2 公式）」."
    },
    {
      "prior_finding": 5,
      "topic": "Data-dictionary omissions (record_state / response_date_synthetic / customer_segment)",
      "status": "RESOLVED",
      "body_locator": "附錄四-1 欄位定義資料字典",
      "evidence": "All three fields are now defined with type, value vocabulary and role: record_state (only allowed value SAMPLE_SYNTHETIC; REAL vocabulary UNKNOWN), response_date_synthetic (YYYY-MM-DD, fictional, not a real administration/sign-off date), customer_segment (only TRAINING_PARTICIPANT_SYNTHETIC present; declared the stratification key with a no-unstratified-merge rule). period_year, service_cohort_id, sample_case_id, Q1–Q8 remain defined."
    },
    {
      "prior_finding": 6,
      "topic": "§拾 flow diagram reading as automatic CURRENT promotion",
      "status": "RESOLVED",
      "body_locator": "§拾-一 真實資料替換四步檢核流程 diagram, steps 4–5 and the terminal state box",
      "evidence": "Step 4 now adds 「計算通過本身不會自動晉級，也不改變資料性質」; step 5 is 「授權角色審查（CURRENT 晉級關卡）」 with 由協會實際授權角色審查來源、權限、重算與獨立複核; the terminal box reads 「[狀態：CURRENT（候選）] CURRENT ≠ REAL，也不等於正式接受（formal acceptance）」, and §拾-二-4 repeats the same gate in prose."
    }
  ],
  "major_findings": [],
  "minor_findings": [
    {
      "severity": "MINOR",
      "body_locator": "附錄二 「題號/題目（逐字引用凍結題項）」 Q1–Q7 cells and the note beneath the table; 附錄四 題項標籤對照表 「凍結題目文字」 column — compared with §伍-二 and 附錄一, which print 「本次訓練服務內容符合我在報名前表達的需求。」 and 「…工作、志工或學習情境。」",
      "evidence": "Appendix II and the appendix IV label table omit the closing 。 and the enumeration mark 、 that appear in §伍 and 附錄一, because QUESTIONNAIRE_ITEMS_0141_R01.csv itself carries no punctuation or inter-word spaces. The note 「未增刪標點」 is literally true against the CSV but a reader comparing 附錄二 with §伍/附錄一 still sees two renderings of the frozen instrument, and an evaluator could ask which is the printed instrument.",
      "required_action": "Add one sentence to the 附錄二 note and to 附錄四's label table stating that the CSV export normalizes punctuation/whitespace and that §伍/附錄一 carries the printable canonical wording (or restore 。 and 、 in the appendix cells). Byte-neutral for all published statistics."
    },
    {
      "severity": "MINOR",
      "body_locator": "§陸-一 各期樣本回收與有效母數彙總表, column 「核心題有效總填答次數」 (72 / 72 / 72 / 216) — read against §伍-二 「7 題核心量化題目」 and §參-三 comparability row 「核心量化 7 題（Q1–Q7）」",
      "evidence": "The 72 figure is Q1–Q6 only (6 items × 12 responses), while two other passages define 「核心」 as seven items (Q1–Q7). The 說明 under the table does resolve it in prose, but the column header alone can be recomputed by an evaluator as 7×12=84 and read as an error.",
      "required_action": "Rename the column to 「Q1–Q6 六構面有效填答次數」 (or define 「核心題＝Q1–Q6，整體題＝Q7」 immediately above the table). Byte-neutral."
    },
    {
      "severity": "MINOR",
      "body_locator": "§捌 方案一 「具體成效檢驗指標」 — 「Q5 有效均值應達到 3.8000 分以上，且無行政聯繫延誤之負面抱怨」",
      "evidence": "The first half is measurable from the instrument (Q5 mean on the unchanged 1–5 scale). The second half has no defined collection source: 附錄三's Q8 is empty in all 36 rows and the document itself says no qualitative text exists, and no complaint/rework register, channel or counting rule is specified. §捌 方案一 also correctly disclaims using Q8 to support the problem statement, which makes the criterion's evidence base visibly undefined.",
      "required_action": "Either define the evidence object for 「負面抱怨」 (e.g. an administrative complaint/rework log with owner, count window and escalation rule) and mark it SAMPLE-proposed, or restate the criterion in Q5 scale points only and note that the qualitative condition is currently UNKNOWN-sourced."
    },
    {
      "severity": "MINOR",
      "body_locator": "§壹-一-4 「Q5（行政溝通與課前通知）」「Q2（課程內容對應情境適切度）」「Q6（學習環境與設備）」 versus the declared single label set in §柒-一 and 附錄四",
      "evidence": "§柒-一 states that no further aliases will be coined and 附錄四 freezes Q4＝教材資源 / Q6＝環境設備, yet §壹's executive bullets use longer descriptive parentheticals that differ from the frozen short labels. The numbers attached are correct, so only the label strings diverge, but a careful reader sees three label variants for Q2/Q5/Q6 across §壹, §柒 and 附錄四.",
      "required_action": "Align §壹's parentheticals to the frozen short labels plus item IDs (e.g. 「Q5 行政溝通」, 「Q2 情境對應」, 「Q6 環境設備」), or drop the parentheticals and point to 附錄四."
    },
    {
      "severity": "MINOR",
      "body_locator": "Sidecar SAMPLE_REPLACEMENT_REGISTER_0141_R05.csv (5fff0f9b…): source_artifact and docx_locator columns for FACT-SYN-0141-FRAME-2023/2024/2025, -Q8-VIGNETTE, -SOP-PARAMS, -SUPPRESSION, -ACT-01 and -ACT-02",
      "evidence": "Those eight non-row facts still cite MANUSCRIPT_0141_R02_REVIEWED.md as source_artifact and use English locators (「Appendix 3 row 1」, 「Section 6 summary」, 「Section 6 aggregates derive from this row」, 「Section 8 proposal one」) whereas the R05 DOCX uses 附錄三, §陸, §捌 and cites the R05 manuscript line. The 36 per-row fact IDs are corrected and consistent; only the non-row lineage pointers were not re-pointed for R05.",
      "required_action": "Re-point those locators to the R05 manuscript and the Chinese section names used in the DOCX. No DOCX byte change is implied; if the register is treated as a promotion artifact, cite one canonical lineage at promotion."
    }
  ],
  "residual_gaps": [
    "Printed checkbox serial remains UNKNOWN, declared honestly in the header table and not contradicted by 157 index 155; only an authoritative printed source can resolve it.",
    "REAL evidence status remains UNKNOWN/HOLD: authorised roles, retention period, access control and privacy policy are deferred by design (保存期限 UNKNOWN / REFER_TO_APPROVED_POLICY), and SAMPLE cannot become REAL by computation, by formatting or by passing this review.",
    "Q8 is empty across all 36 synthetic rows (declared in §壹, §陸 and both proposals), so the qualitative channel is structurally present but unexercised; the first REAL cycle must populate it before any qualitative claim or complaint-based criterion can be evidenced.",
    "No segment-level result table exists because only one synthetic segment is surveyed; the first REAL cycle that includes corporate client windows must add stratified output per §參-I and gate rule 8.",
    "The exact official meaning of the 4 分 cell remains a control-plane question; the page-9 extract shows a scoring tier and no weight column, and the document's neutral wording is consistent with that, but it cannot settle the printed label.",
    "This review did not inspect the DOCX binary, Word rendering, chart geometry or page layout; the 25-page visual receipt (5076475e…) and the technical QA receipt (d4014756…) are separate lanes with their own SHAs and are corroborating, not verified here. The chart plots the pooled six-item index plus Q7 and the Q2/Q5/Q6 series and omits Q1/Q3/Q4 (disclosed in §陸-四); the caption note disambiguating the pooled index from any single item is present and materially reduces the misreading risk.",
    "§拾-一 step 3 asks for 「不可逆對照表」 while §拾-二 and §伍 preserve an anonymous case-code mapping and §拾-一-2 allows retention of a re-identification key under approved policy; the phrase is defensible if read as file-level SHA lineage, but the wording could be tightened to 「檔案層級不可逆雜湊對照」 to avoid implying that identity re-linking is impossible.",
    "Official score NOT_ASSIGNED and Human formal acceptance NOT_GRANTED: this candidate remains SAMPLE/CANDIDATE and must not be treated as REAL, approved, promoted or scored evidence on the strength of this semantic PASS."
  ]
}
```

### R05 receipt

```json
{
  "work_id": "TTQS_ONE_0141_I19-E31_R05_SEMANTIC_REVIEW",
  "doc_id": "0141",
  "requirement_id": "I19-E31",
  "docx_sha256": "3e9e6eef2769617dc4d515bb0d9abfa363a46e217b13b7c261b279306ced17d8",
  "extracted_text_sha256": "c13c350eb8fce0f891d36dc64c15682433b668df976708456d9e71ae31f59328",
  "verdict": "PASS",
  "major_findings": 0,
  "minor_findings": 5,
  "requested_route": "OpenCode v2 CLI",
  "requested_model": "opencode/deepseek-v4.1-flash-free",
  "requested_alias_available_in_cli_models_list": true,
  "actual_model_identity": "UNKNOWN (CLI response contained no provider/model metadata)",
  "cli_pid": 84004,
  "cli_exit_code": 0,
  "stderr_bytes": 0,
  "stdout_sha256": "ecd318505d21ac99aac905ae90420a1508c894c66f1ee352ac6d1c412dcd5c81",
  "stdout_bytes": 26247,
  "reviewer_raw_response_sha256": "39a50ae2c2d292155479e2c966f30c86731fc82d548451827635cf56300d78bc",
  "parsed_review_sha256": "8123e441177378c454525123685d3eb878aa47e8a1acaebd6ec3373518e3efc4",
  "tool_use_events": 0,
  "cost_usd": "UNKNOWN",
  "token_usage": "UNKNOWN (CLI emitted no usage event)",
  "review_scope": "SEMANTIC_TEXT_ONLY",
  "not_inherited": "The prior exact-SHA R04 PASS (a0dfec32…) and its six minor findings were treated as context to be re-verified, not as a verdict for this SHA.",
  "candidate_state": "CANDIDATE_ONLY; PASS is semantic-only and does not promote",
  "real_data_status": "UNKNOWN/HOLD",
  "official_score": "NOT_ASSIGNED",
  "human_formal_acceptance": "NOT_GRANTED"
}
```

## Official and source packet (unchanged from R05 packet; SHA identity preserved)

## Source: OFFICIAL_REQUIREMENT_ROW_I19-E31.json

SHA-256: `d18d41bd68b7dc45a78b5c26292cca6ba422902da83d8b7dbed25a7a34af7fb6`

```text
{
  "requirement_id": "I19-E31",
  "indicator": "19",
  "points": "4分",
  "criterion": "顧客滿意度提升。",
  "source_document_type": "official TTQS scoring evidence-table PDF; physical page 9",
  "source_pdf": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\INPUTS\\R04\\06_OFFICIAL_SOURCES\\TTQS查核佐證文件資料表-訓練機構版 (2).pdf",
  "source_pdf_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
  "physical_pdf_page": 9,
  "page9_extraction_sha256": "945949f3fb82445f4f6a9571283a48b2de20ed016bb6712880a2296c30ed6318",
  "reconciliation_row": {
    "requirement_id": "I19-E31",
    "indicator_no": "19",
    "subitem_or_score_tier": "4分",
    "official_checkbox_text": "顧客滿意度提升。",
    "master_register_text_match": "True",
    "official_evidence_table_pdf": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\INPUTS\\R04\\06_OFFICIAL_SOURCES\\TTQS查核佐證文件資料表-訓練機構版 (2).pdf",
    "official_evidence_table_page": "9",
    "pdf_text_readback_status": "PDF_TEXT_EXACT_PAGE_MATCH",
    "visually_checked_pages": "",
    "deliverable_ids": "0141",
    "deliverable_titles": "顧客滿意度趨勢調查與分析報告",
    "deliverable_count": "1",
    "phase2_blueprint_status": "PHASE2_BLUEPRINT_EXPANDED_PREPRODUCTION",
    "production_mode_candidate": "SYNTHETIC_COMPLETE_DRAFT",
    "phase2_plan_count": "1",
    "phase2_title_alignment": "HISTORICAL_PLAN_NAMES_NOT_AUTHORITATIVE_R04_CROSSWALK_TITLE_USED"
  },
  "reconciliation_csv_sha256": "ff6de9f52a0affba7d5c4c57caac868812600305f4807e7b59b6db5b5cb1a2b9"
}

```

## Source: OFFICIAL_SOURCE_PAGE9_EXCERPT.txt

SHA-256: `0733c1e3a7fa7b88b79846aabf8667391e032165e78cf9bfc06b7363e71ffe11`

```text
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
 
 
```

## Source: CROSSWALK_ROW_0141_AND_NEIGHBORS.json

SHA-256: `d09422ce4bca4ff442b1c4fa266c56181c0f4c162d269f9cc02933d45ea4f786`

```text
{
  "crosswalk_csv": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv",
  "crosswalk_csv_sha256": "1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679",
  "target_row": {
    "requirement_id": "I19-E31",
    "deliverable_count": "1",
    "split_extra_count": "0",
    "deliverable_ids": "0141",
    "document_titles": "顧客滿意度趨勢調查與分析報告"
  },
  "neighbor_rows_I19_E30_E31_E32": [
    {
      "requirement_id": "I19-E30",
      "deliverable_count": "1",
      "split_extra_count": "0",
      "deliverable_ids": "0140",
      "document_titles": "訓練資訊系統使用普及率盤點與分析表"
    },
    {
      "requirement_id": "I19-E31",
      "deliverable_count": "1",
      "split_extra_count": "0",
      "deliverable_ids": "0141",
      "document_titles": "顧客滿意度趨勢調查與分析報告"
    },
    {
      "requirement_id": "I19-E32",
      "deliverable_count": "1",
      "split_extra_count": "0",
      "deliverable_ids": "0142",
      "document_titles": "組織近三年營業額與收入趨勢核對報告"
    }
  ]
}

```

## Source: UNIQUE_BLUEPRINT_0141_I19-E31_R02.md

SHA-256: `e19761674045b2defa7090ba1d8f1224943a89e54811180c20b9ea362de59cda`

```text
# 0141 I19-E31 專屬 Blueprint R02

## A. 唯一命題與文件用途
本件只處理「顧客滿意度提升」：用相同服務定義、固定問卷核心題、相同 1–5 量尺、可核對的有效分母與多期統計，呈現訓練服務顧客評價的變化，分析限制，並形成下一輪待核准改善建議。它是調查與分析報告，不是評分表、資訊系統使用報告、考照/就業成效報告或營收證明。

## B. 正式對應
- doc_id 0141
- requirement_id I19-E31
- indicator 19, criterion 「顧客滿意度提升。」. The checked physical PDF page 9 excerpt places 「4分」 in the 1–5 scoring-tier list; that excerpt does not identify a weight column. Do not infer a weight or association score from this label.
- 157 blueprint index 155: 「顧客滿意度上升：多期同量尺統計」
- official source locator: training-institution scoring evidence table, physical PDF page 9, criterion 「顧客滿意度提升。」 The 0141 deliverable title comes from the separate 129-to-142 crosswalk row.
- printed checkbox serial: UNKNOWN.
- Neighbor guard: 0139/I19-E29/index153 = licensing/employment; 0140/I19-E30/index154 = information-system uptake; 0142/I19-E32/index156 = revenue. All are different proof constructs.

## C. Intended reader and use
Training administration prepares, fields, cleans and summarizes surveys; responsible officers review customer groups and draft responses; an authorized association role decides whether any proposed change may be adopted. The document must be usable before launch: the questions, scale, timing, invitation denominator, nonresponse treatment, segment fields, analysis formulas, actions, follow-up and hold criteria are visible. Sample decisions are proposals only.

## D. Document structure and required content
1. Cover and status: document identity, report purpose, period, version; label the whole demonstration SAMPLE/SYNTHETIC and REAL evidence UNKNOWN/HOLD.
2. One-page executive finding: exact three-period sample means, response denominator, observed lowest service dimension, interpretation and limits; distinguish sample arithmetic from association performance.
3. Scope and comparability protocol: customer/participant definition, service cohort, sampling frame, invitation unit, response window, eligibility, segment policy, privacy and small-cell controls.
4. Reusable survey administration protocol: dispatch timing, reminder limit, collection channel, coding, invalid/duplicate exclusion, missing/N/A rules, file custody and audit trail.
5. Complete questionnaire: eight exact questions from the source packet, item type, response options, skip/NA handling, respondent segment and service-period metadata. Keep the seven 1–5 items unchanged across periods; Q8 is qualitative and excluded from numeric means.
6. Results: period-level invitation/valid/response counts; six domain-item means and valid n; separate Q7 overall mean and Top-2 rate; customer segment results if supplied; a multi-period table and readable line chart using the same axis. No cross-SHA or cross-construct metrics.
7. Interpretation: compare 2023→2024, 2024→2025 and baseline→final; identify the weakest item, check for scale/response/composition shifts, and state that a small synthetic sample cannot establish causal impact or represent all customers.
8. SAMPLE improvement loop: two hypothetical actions and measurable follow-up, each tied to the observed synthetic item, proposed responsible role, check date/window, success measure and explicit NOT_ADOPTED/NOT_EXECUTED status. Do not describe a proposal as a meeting decision or actual result.
9. Limitations and next-cycle decision table: continue/change/hold choices with explicit evidence required; if valid n, scale, service definition or denominator changed, mark trend not comparable and hold.
10. Appendices: blank reusable capture form plus filled SAMPLE example; data dictionary; 36 response-level SYNTHETIC records; replacement register; formula sheet; source locator and revision record.

## E. Survey protocol and scoring
- Core scale: 1 very dissatisfied, 2 dissatisfied, 3 neutral, 4 satisfied, 5 very satisfied; N/A/not known excluded per item.
- Six domain items are Q1–Q6. Q7 overall satisfaction is separate. Q8 is open text.
- Return rate = valid completed returns / issued invitations. Sample design: 15 invited and 12 valid per year (80%). This is a fictional teaching dataset, not actual sampling.
- Per-item mean = valid response score total / valid answers for that item.
- Six-item index = sum of valid Q1–Q6 scores / number of valid Q1–Q6 answers; only compute respondent-level index when at least 5 of 6 answered. Report item Ns and do not impute.
- Q7 Top-2 = respondents scoring 4 or 5 / valid Q7 answers.
- Trend = later-period value minus earlier-period value on the same five-point scale, reported in points. Do not call it percent improvement. If customer composition, question wording, channel or service changes materially, compare strata only or mark HOLD.
- No causal claim without a verified intervention log and a design supporting attribution.

## F. Canonical synthetic case and item alignment
Canonical SAMPLE fact ID: FACT-SYN-0141-SAT-TREND-R01. Case IDs SYN-0141-YYYY-NNN; 12 complete respondents/year, 3 years; 36 unique IDs; 15 invitations/year; no real personal information. Q5 admin communication is illustrated as improving after a hypothetical notification redesign; Q2 needs/content fit is illustrated as improving after a hypothetical pre-course clarification step; Q7 overall item rises in the sample. These are deliberately synthetic trajectories and cannot support a claim that the association performed either action.
Use the same data file, item wording, scale, period summary and replacement register in the DOCX and its sidecar receipts.

## G. Shared-fact / cross-document boundary
Cross-reference I19-E29/0139, I19-E30/0140, I19-E32/0142 only to distinguish constructs and prevent substitution. Do not reuse their generated narrative, datasets, rates, respondents or claims. Until a verified shared fact source exists, 0141 uses only its own synthetic fact ID and does not assert that the same actual trainees, years, or cohorts appear in adjacent deliverables.

## H. SAMPLE / REAL and authority restrictions
Every generated respondent, date, score, action and narrative is SAMPLE/SYNTHETIC. Real responses require authorized original forms or exports, auditable period and item mapping, protected identity matching, and permission to analyze. Do not invent actual members, instructors, clients, survey returns, approvals, committee decisions, signatures, causal findings, score attainment or formal acceptance. If real data are absent, the example remains complete but visibly synthetic; the real-performance conclusion is UNKNOWN/HOLD.

## I. Exact reject / hold criteria
Reject or hold if: (1) official IDs are conflated; (2) only a blank survey is supplied; (3) periods use different questions/scales without a comparability warning; (4) denominator or valid n is absent; (5) N/A/blank is treated as zero or imputed; (6) Likert point delta is mislabeled as percent growth; (7) nonrespondents disappear without response-rate handling; (8) customer segments are blended despite composition changes; (9) synthetic figures/actions are presented as real; (10) satisfaction is substituted for learning, employment, licensing, revenue or system-use results; (11) a causal claim lacks evidence; (12) no actionable follow-up, owner role, checkpoint or hold rule is provided; (13) no source locator or exact-SHA QA is attached.

## J. Pre-build acceptance gates
- Confirm the official source, row mapping, index 155 and neighbor guard.
- Recompute all sample aggregates from the canonical CSV; response counts and replacement-register IDs must match exactly.
- Confirm exact questionnaire wording, scale and missing-data rules match across manuscript and DOCX.
- Independent semantic reviewer assesses the exact candidate SHA for requirement fit, usefulness, completeness, claims and negative-neighbor distinction.
- Word-native render and all-page visual inspection are separate from semantic review.
- Candidate remains CANDIDATE until exact-SHA independent semantic PASS and any formal Human acceptance; SAMPLE never converts into REAL by formatting.

## R02 修訂界線
R02 只澄清官方實體 PDF 第 9 頁摘錄中「4分」位於計分級距，且摘錄未顯示為權重欄；不變更文件文類、I19-E31 對應、索引 155、題目、R01 合成資料或計算口徑。未核明的權重狀態不得推測。

```

## Source: SOURCE_PACKET_0141_I19-E31_R02.md

SHA-256: `43c0e1bda5dfeb12c1ba8fc8805b876641f5184e4bf95eb4ef6c3182cf8ee964`

```text
# 0141 I19-E31 來源包 R02

## 定位與證據層級
- 文件編號：0141。
- 官方具名要求：I19-E31；指標 19「目標市場與顧客價值」。目前核對的官方評分表實體 PDF 第 9 頁摘錄，將 4 分列在計分標準的 1–5 分級距中；摘錄未顯示本欄為權重欄，因此不據此推算權重或協會得分。
- 157 方框索引：155。157 索引、I19-E31 requirement ID、文件 0141 是三套不同識別；印刷版 checkbox serial 未由目前資料證明，寫 UNKNOWN。
- 交付文類：顧客滿意度趨勢調查與分析報告。不能用空白問卷或管理辦法替代實際可操作報告。

## 正式來源
- 官方佐證文件資料表（訓練機構版），PDF 實體第 9 頁；正式要求列原文「顧客滿意度提升。」。
- 文件名稱「顧客滿意度趨勢調查與分析報告」取自 129→142 交付 crosswalk 的 I19-E31／0141 列，不是官方 PDF 第 9 頁原文。
- GitHub 目前 03_157_CHECKBOX_BLUEPRINTS.md blob 8c2bbe7ca9dcbb03088a48934b9e57e7147ede63，索引 155：顧客滿意度上升、多期同量尺統計；需特定來源定位、核心正文/示範、決策或結果、與其他文件的事實連結，不可只留空欄位。
- GitHub 目前 02_GENRE_WRITING_MANUAL.md blob 4ff863d9f534b6359fc1c7c1685bd8cce02da886，調查類要求完整題目、抽樣方法、SAMPLE 原始例答、資料清理、統計、限制及用途；比率需明確分母，示例需有 case_id/fact_id。

## 相鄰要求的排除
- 0140 / I19-E30 / 157 索引 154 是資訊系統普及率；不是本文件的顧客滿意度。
- 0142 / I19-E32 / 157 索引 156 是三年營業額增長，涉及真實財報合法核實；不是顧客滿意度。
- 0139 / I19-E29 / 157 索引 153 是考照/就業率，不可拿就業率當滿意度。
- 官方頁面所示 4 分是計分標準的一個評分級距；不把它轉述成權重、協會得分或已達成結果。

## 專屬 SAMPLE 基礎
本包的 36 筆年度回覆、15 份邀請/年、12 份有效回覆/年及所有分數都是 SYNTHETIC。示範對象為虛構訓練服務參與者；不代表本協會真實客群、課程、回收率或績效。三期使用相同題目、同一 1–5 量尺和相同分母口徑，以展示趨勢計算。真實作業前須由協會確認顧客定義、實際服務清單、抽樣框和合法取得的原始問卷。不得將學員樣本代表所有委託單位；若委託單位是顧客，須另分層呈現。

## 報告要回答的問題
1. 三個年度如何界定同一項服務及其顧客；三期問卷、量尺、回收窗口是否一致。
2. 邀請、回覆、有效回覆及各題有效 n 的實際分子分母是多少；未回覆及無效件如何處理。
3. 整體滿意與六個服務構面各期變化為何；哪些項目較弱，哪些變化需要查證。
4. 問卷結果支持何種改善假設；哪些是樣本內觀察，哪些因樣本小、構成差異或無對照組而不能作因果結論。
5. 下一輪要採取什麼措施、由哪個建議角色負責、何時回查、用何指標判斷有效；凡未經授權的決定標示「SAMPLE 擬議、尚待核准」。

## 資料與計算口徑
- 回收率 = 有效問卷數 / 已發出邀請數；示例每年 12/15 = 80.00%。不可用有效問卷數除以全體會員、全體學員等未證實母體。
- 六構面均值 = 該構面有效 1–5 分總和 / 該構面有效回答數；不把 Q7 整體題混進六構面合成均值。
- 整體滿意均值另列 Q7；Top-2 比率 = Q7 評分 4 或 5 人數 / Q7 有效回答數。
- 跨年差以量尺點數列示，例如 2025 均值減 2023 均值；不得把 Likert 均值差誤寫成百分比成長。
- N/A 和空白不得計成 0；不臆補；逐題列有效 n。若受訪者少於 5/6 個構面有效答案，不計個人合成值，但仍保留該題可用答案作項目分析。
- 客群混合時先分層；若要彙總，需事先明示固定權重並另外報告各層，不可因樣本組成改變而誤讀為滿意度趨勢。
- 含少樣本的真實結果須遵守協會個資與小樣本揭露規則；本合成示範不包含真實識別資料。

## 問卷核心題目（擬議測量工具，並非官方核定問卷）
量尺：1 非常不滿意、2 不滿意、3 普通、4 滿意、5 非常滿意；另可選「不適用/不知道」，不計入該題分母。
1. 本次訓練服務內容符合我在報名前表達的需求。
2. 課程內容能對應我預計運用的工作、志工或學習情境。
3. 講師的說明、示範與回應有助於我理解課程。
4. 教材與學習資源容易取得，並能支持我完成學習。
5. 報名、課前通知與行政回覆清楚且及時。
6. 學習場地或線上環境與設備適合本次服務。
7. 整體而言，我對本次訓練服務感到滿意。（獨立總體題）
8. 本次最有幫助的是什麼？下一次最希望改善什麼？（開放題，SAMPLE 回答不得冒充真人引言）

## 來源檔及本包產物
以 SOURCE_PREP_RECEIPT_0141_R01.json 的 SHA-256 表為準。正式 PDF 頁面摘錄、交付 crosswalk 原列、需求 reconciliation 原列、157 索引鄰列與合成資料分開保存。

## R02 來源解讀修訂
本版只修正官方第 9 頁「4 分」標籤的來源解讀；官方要求 I19-E31、索引 155、文件編號 0141、相鄰要求排除、原始問卷題文與 R01 合成 CSV 均未變更。來源頁未明示權重欄，故此版保留該標註的未知狀態。

```

## Source: QUESTIONNAIRE_ITEMS_0141_R01.csv

SHA-256: `310745e5be17980ca9c623b23e15605cb221c9cbbdf1886913cb54db1acdf0e7`

```text
doc_id,requirement_id,item_id,item_type,question,scale
0141,I19-E31,Q1,LIKERT,本次訓練服務內容符合我在報名前表達的需求,1-5
0141,I19-E31,Q2,LIKERT,課程內容能對應我預計運用的工作志工或學習情境,1-5
0141,I19-E31,Q3,LIKERT,講師的說明示範與回應有助於我理解課程,1-5
0141,I19-E31,Q4,LIKERT,教材與學習資源容易取得並能支持我完成學習,1-5
0141,I19-E31,Q5,LIKERT,報名課前通知與行政回覆清楚且及時,1-5
0141,I19-E31,Q6,LIKERT,學習場地或線上環境與設備適合本次服務,1-5
0141,I19-E31,Q7,LIKERT_OVERALL,整體而言我對本次訓練服務感到滿意,1-5
0141,I19-E31,Q8,OPEN_TEXT,本次最有幫助的是什麼下一次最希望改善什麼,NOT_SCORED

```

## Source: SAMPLE_SURVEY_RESPONSES_0141_R01.csv

SHA-256: `723259199dd51973fc6473ec000234cc853fa1511be05864fdfd7b08bb452862`

```text
record_state,period_year,service_cohort_id,sample_case_id,response_date_synthetic,customer_segment,Q1_need_fit,Q2_content_applicability,Q3_instructor_support,Q4_materials_resources,Q5_admin_communication,Q6_learning_environment,Q7_overall_satisfaction,Q8_open_comment
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-001,2023-01-20,TRAINING_PARTICIPANT_SYNTHETIC,3,3,4,3,3,4,3,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-002,2023-02-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,3,3,4,3,3,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-003,2023-03-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,4,3,3,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-004,2023-04-20,TRAINING_PARTICIPANT_SYNTHETIC,3,3,3,4,3,3,3,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-005,2023-05-20,TRAINING_PARTICIPANT_SYNTHETIC,4,4,3,4,4,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-006,2023-06-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,4,4,3,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-007,2023-07-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,3,3,4,3,3,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-008,2023-08-20,TRAINING_PARTICIPANT_SYNTHETIC,4,4,4,4,3,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-009,2023-09-20,TRAINING_PARTICIPANT_SYNTHETIC,3,3,4,3,4,3,3,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-010,2023-10-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,3,4,3,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-011,2023-11-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,4,4,4,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2023,SYN-COURSE-2023-01,SYN-0141-2023-012,2023-12-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,3,4,4,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-001,2024-01-20,TRAINING_PARTICIPANT_SYNTHETIC,3,3,4,3,4,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-002,2024-02-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,3,3,4,3,3,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-003,2024-03-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,4,3,4,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-004,2024-04-20,TRAINING_PARTICIPANT_SYNTHETIC,3,3,3,4,3,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-005,2024-05-20,TRAINING_PARTICIPANT_SYNTHETIC,4,4,3,4,5,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-006,2024-06-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,4,4,3,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-007,2024-07-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,3,3,5,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-008,2024-08-20,TRAINING_PARTICIPANT_SYNTHETIC,4,4,4,4,3,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-009,2024-09-20,TRAINING_PARTICIPANT_SYNTHETIC,3,3,4,3,5,3,3,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-010,2024-10-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,3,4,3,4,5,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-011,2024-11-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,4,4,5,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2024,SYN-COURSE-2024-01,SYN-0141-2024-012,2024-12-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,3,4,4,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-001,2025-01-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,4,3,4,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-002,2025-02-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,3,3,4,3,3,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-003,2025-03-20,TRAINING_PARTICIPANT_SYNTHETIC,4,4,4,3,4,4,5,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-004,2025-04-20,TRAINING_PARTICIPANT_SYNTHETIC,3,3,3,4,4,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-005,2025-05-20,TRAINING_PARTICIPANT_SYNTHETIC,4,5,3,4,5,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-006,2025-06-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,4,4,3,4,5,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-007,2025-07-20,TRAINING_PARTICIPANT_SYNTHETIC,3,5,3,3,5,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-008,2025-08-20,TRAINING_PARTICIPANT_SYNTHETIC,4,4,4,4,4,4,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-009,2025-09-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,4,3,5,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-010,2025-10-20,TRAINING_PARTICIPANT_SYNTHETIC,4,3,3,4,3,4,5,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-011,2025-11-20,TRAINING_PARTICIPANT_SYNTHETIC,4,4,4,4,5,3,4,SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC,2025,SYN-COURSE-2025-01,SYN-0141-2025-012,2025-12-20,TRAINING_PARTICIPANT_SYNTHETIC,3,4,3,4,5,3,5,SAMPLE_ONLY; no actual respondent text

```

## Source: SAMPLE_PERIOD_SUMMARY_0141_R01.csv

SHA-256: `537c39dcc650d9818779ee3dd4572d64a820720828b9e632e9abb44358777c0b`

```text
period_year,SAMPLE_invited_n,SAMPLE_valid_n,SAMPLE_return_rate_pct,core_item_valid_n,six_item_mean_1_to_5,overall_Q7_mean_1_to_5,overall_Q7_top2_n,overall_Q7_top2_pct,same_scale,all_records,item_means
2023,15,12,80.0,72,3.4861,3.5833,7,58.33,1-5,SAMPLE_SYNTHETIC,"{""Q1_need_fit"": 3.5, ""Q2_content_applicability"": 3.4167, ""Q3_instructor_support"": 3.5, ""Q4_materials_resources"": 3.5833, ""Q5_admin_communication"": 3.5, ""Q6_learning_environment"": 3.4167, ""Q7_overall_satisfaction"": 3.5833}"
2024,15,12,80.0,72,3.5694,3.9167,10,83.33,1-5,SAMPLE_SYNTHETIC,"{""Q1_need_fit"": 3.5, ""Q2_content_applicability"": 3.4167, ""Q3_instructor_support"": 3.5, ""Q4_materials_resources"": 3.5833, ""Q5_admin_communication"": 4.0, ""Q6_learning_environment"": 3.4167, ""Q7_overall_satisfaction"": 3.9167}"
2025,15,12,80.0,72,3.6944,4.25,11,91.67,1-5,SAMPLE_SYNTHETIC,"{""Q1_need_fit"": 3.5, ""Q2_content_applicability"": 3.9167, ""Q3_instructor_support"": 3.5, ""Q4_materials_resources"": 3.5833, ""Q5_admin_communication"": 4.25, ""Q6_learning_environment"": 3.4167, ""Q7_overall_satisfaction"": 4.25}"

```


## R06 replacement register CSV: SAMPLE_REPLACEMENT_REGISTER_0141_R06.csv (sha256 `862df5957e732d3d0bce722c52c9dcca63e4555902aec96e31983dc586cbf2aa`)

```csv
fact_id,doc_id,requirement_id,sample_case_id,field_group,sample_value_or_locator,docx_locator,source_artifact,rationale,related_docs,real_replacement_source,verifier_role,status
FACT-SYN-0141-SAT-TREND-R01-2023-001,0141,I19-E31,SYN-0141-2023-001,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-01-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":3,""Q3"":4,""Q4"":3,""Q5"":3,""Q6"":4,""Q7"":3},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 1; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-002,0141,I19-E31,SYN-0141-2023-002,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-02-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":3,""Q4"":3,""Q5"":4,""Q6"":3,""Q7"":3},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 2; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-003,0141,I19-E31,SYN-0141-2023-003,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-03-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":4,""Q4"":3,""Q5"":3,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 3; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-004,0141,I19-E31,SYN-0141-2023-004,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-04-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":3,""Q3"":3,""Q4"":4,""Q5"":3,""Q6"":3,""Q7"":3},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 4; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-005,0141,I19-E31,SYN-0141-2023-005,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-05-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":4,""Q3"":3,""Q4"":4,""Q5"":4,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 5; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-006,0141,I19-E31,SYN-0141-2023-006,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-06-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":4,""Q4"":4,""Q5"":3,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 6; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-007,0141,I19-E31,SYN-0141-2023-007,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-07-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":3,""Q4"":3,""Q5"":4,""Q6"":3,""Q7"":3},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 7; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-008,0141,I19-E31,SYN-0141-2023-008,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-08-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":4,""Q3"":4,""Q4"":4,""Q5"":3,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 8; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-009,0141,I19-E31,SYN-0141-2023-009,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-09-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":3,""Q3"":4,""Q4"":3,""Q5"":4,""Q6"":3,""Q7"":3},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 9; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-010,0141,I19-E31,SYN-0141-2023-010,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-10-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":3,""Q4"":4,""Q5"":3,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 10; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-011,0141,I19-E31,SYN-0141-2023-011,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-11-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":4,""Q4"":4,""Q5"":4,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 11; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2023-012,0141,I19-E31,SYN-0141-2023-012,survey response/date/cohort/Q1-Q7,"{""year"":""2023"",""cohort"":""SYN-COURSE-2023-01"",""date"":""2023-12-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":3,""Q4"":4,""Q5"":4,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 12; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-001,0141,I19-E31,SYN-0141-2024-001,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-01-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":3,""Q3"":4,""Q4"":3,""Q5"":4,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 13; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-002,0141,I19-E31,SYN-0141-2024-002,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-02-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":3,""Q4"":3,""Q5"":4,""Q6"":3,""Q7"":3},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 14; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-003,0141,I19-E31,SYN-0141-2024-003,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-03-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":4,""Q4"":3,""Q5"":4,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 15; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-004,0141,I19-E31,SYN-0141-2024-004,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-04-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":3,""Q3"":3,""Q4"":4,""Q5"":3,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 16; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-005,0141,I19-E31,SYN-0141-2024-005,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-05-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":4,""Q3"":3,""Q4"":4,""Q5"":5,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 17; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-006,0141,I19-E31,SYN-0141-2024-006,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-06-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":4,""Q4"":4,""Q5"":3,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 18; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-007,0141,I19-E31,SYN-0141-2024-007,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-07-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":3,""Q4"":3,""Q5"":5,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 19; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-008,0141,I19-E31,SYN-0141-2024-008,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-08-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":4,""Q3"":4,""Q4"":4,""Q5"":3,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 20; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-009,0141,I19-E31,SYN-0141-2024-009,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-09-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":3,""Q3"":4,""Q4"":3,""Q5"":5,""Q6"":3,""Q7"":3},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 21; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-010,0141,I19-E31,SYN-0141-2024-010,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-10-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":3,""Q4"":4,""Q5"":3,""Q6"":4,""Q7"":5},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 22; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-011,0141,I19-E31,SYN-0141-2024-011,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-11-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":4,""Q4"":4,""Q5"":5,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 23; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2024-012,0141,I19-E31,SYN-0141-2024-012,survey response/date/cohort/Q1-Q7,"{""year"":""2024"",""cohort"":""SYN-COURSE-2024-01"",""date"":""2024-12-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":3,""Q4"":4,""Q5"":4,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 24; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-001,0141,I19-E31,SYN-0141-2025-001,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-01-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":4,""Q4"":3,""Q5"":4,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 25; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-002,0141,I19-E31,SYN-0141-2025-002,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-02-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":3,""Q4"":3,""Q5"":4,""Q6"":3,""Q7"":3},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 26; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-003,0141,I19-E31,SYN-0141-2025-003,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-03-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":4,""Q3"":4,""Q4"":3,""Q5"":4,""Q6"":4,""Q7"":5},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 27; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-004,0141,I19-E31,SYN-0141-2025-004,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-04-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":3,""Q3"":3,""Q4"":4,""Q5"":4,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 28; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-005,0141,I19-E31,SYN-0141-2025-005,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-05-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":5,""Q3"":3,""Q4"":4,""Q5"":5,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 29; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-006,0141,I19-E31,SYN-0141-2025-006,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-06-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":4,""Q4"":4,""Q5"":3,""Q6"":4,""Q7"":5},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 30; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-007,0141,I19-E31,SYN-0141-2025-007,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-07-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":5,""Q3"":3,""Q4"":3,""Q5"":5,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 31; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-008,0141,I19-E31,SYN-0141-2025-008,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-08-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":4,""Q3"":4,""Q4"":4,""Q5"":4,""Q6"":4,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 32; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-009,0141,I19-E31,SYN-0141-2025-009,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-09-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":4,""Q4"":3,""Q5"":5,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 33; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-010,0141,I19-E31,SYN-0141-2025-010,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-10-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":3,""Q3"":3,""Q4"":4,""Q5"":3,""Q6"":4,""Q7"":5},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 34; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-011,0141,I19-E31,SYN-0141-2025-011,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-11-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":4,""Q2"":4,""Q3"":4,""Q4"":4,""Q5"":5,""Q6"":3,""Q7"":4},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 35; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-SAT-TREND-R01-2025-012,0141,I19-E31,SYN-0141-2025-012,survey response/date/cohort/Q1-Q7,"{""year"":""2025"",""cohort"":""SYN-COURSE-2025-01"",""date"":""2025-12-20"",""segment"":""TRAINING_PARTICIPANT_SYNTHETIC"",""scores"":{""Q1"":3,""Q2"":4,""Q3"":3,""Q4"":4,""Q5"":5,""Q6"":3,""Q7"":5},""Q8"":""SAMPLE_ONLY; no actual respondent text""}",Appendix 3 row 36; section 6 aggregates derive from this row,SAMPLE_SURVEY_RESPONSES_0141_R01.csv,Synthetic worked example; not association performance.,0139/I19-E29;0140/I19-E30;0142/I19-E32 are exclusion boundaries only,Authorized de-identified original survey export and invitation records for corresponding period; UNKNOWN,"Association-authorized data custodian, not assigned",SAMPLE_SYNTHETIC; REAL_UNKNOWN; NOT_FORMALLY_ACCEPTED
FACT-SYN-0141-FRAME-2023,0141,I19-E31,FRAME-2023,invitation denominator,15 invited / 12 valid,§陸-一 各期樣本回收與有效母數彙總表（2023列）,MANUSCRIPT_0141_R06_CANDIDATE.md,Synthetic frame assumption only.,Adjacent IDs are negative-neighbor controls only.,Authorized association source/policy for corresponding real activity; UNKNOWN,"Association-authorized owner, not assigned",SAMPLE_SYNTHETIC; NOT_ADOPTED/NOT_EXECUTED; REAL_UNKNOWN
FACT-SYN-0141-FRAME-2024,0141,I19-E31,FRAME-2024,invitation denominator,15 invited / 12 valid,§陸-一 各期樣本回收與有效母數彙總表（2024列）,MANUSCRIPT_0141_R06_CANDIDATE.md,Synthetic frame assumption only.,Adjacent IDs are negative-neighbor controls only.,Authorized association source/policy for corresponding real activity; UNKNOWN,"Association-authorized owner, not assigned",SAMPLE_SYNTHETIC; NOT_ADOPTED/NOT_EXECUTED; REAL_UNKNOWN
FACT-SYN-0141-FRAME-2025,0141,I19-E31,FRAME-2025,invitation denominator,15 invited / 12 valid,§陸-一 各期樣本回收與有效母數彙總表（2025列）,MANUSCRIPT_0141_R06_CANDIDATE.md,Synthetic frame assumption only.,Adjacent IDs are negative-neighbor controls only.,Authorized association source/policy for corresponding real activity; UNKNOWN,"Association-authorized owner, not assigned",SAMPLE_SYNTHETIC; NOT_ADOPTED/NOT_EXECUTED; REAL_UNKNOWN
FACT-SYN-0141-Q8-VIGNETTE,0141,I19-E31,SYN-0141-EXAMPLE-001,separate completed questionnaire,"Q1-Q7=4,5,3,4,5,3,4; Q8 synthetic illustrative text",附錄二 SAMPLE填妥回覆範例Q8；不納入附錄三36筆趨勢資料或統計,MANUSCRIPT_0141_R06_CANDIDATE.md,Separate form example; no real respondent.,Adjacent IDs are negative-neighbor controls only.,Authorized association source/policy for corresponding real activity; UNKNOWN,"Association-authorized owner, not assigned",SAMPLE_SYNTHETIC; NOT_ADOPTED/NOT_EXECUTED; REAL_UNKNOWN
FACT-SYN-0141-SOP-PARAMS,0141,I19-E31,SOP-R02,proposed workflow parameters,"Dates, reminders, thresholds and roles are illustrative only",§肆 調查行政標準作業程序及提醒／截止規則,MANUSCRIPT_0141_R06_CANDIDATE.md,"Sample workflow, not association policy.",Adjacent IDs are negative-neighbor controls only.,Authorized association source/policy for corresponding real activity; UNKNOWN,"Association-authorized owner, not assigned",SAMPLE_SYNTHETIC; NOT_ADOPTED/NOT_EXECUTED; REAL_UNKNOWN
FACT-SYN-0141-SUPPRESSION,0141,I19-E31,PRIVACY-R02,small-cell suppression proposal,"n<5 is SAMPLE suggestion, not official/approved threshold",§參-四 小樣本單元保護與保密規則,MANUSCRIPT_0141_R06_CANDIDATE.md,Actual policy threshold unknown.,Adjacent IDs are negative-neighbor controls only.,Authorized association source/policy for corresponding real activity; UNKNOWN,"Association-authorized owner, not assigned",SAMPLE_SYNTHETIC; NOT_ADOPTED/NOT_EXECUTED; REAL_UNKNOWN
FACT-SYN-0141-ACT-01,0141,I19-E31,SAMPLE-ACT-0141-01,hypothetical improvement proposal,Notification checklist; timing/targets pending approval,§捌 方方案一：標準化課前通知與行政溝通單一窗口建置案,MANUSCRIPT_0141_R06_CANDIDATE.md,Not adopted or executed.,Adjacent IDs are negative-neighbor controls only.,Authorized association source/policy for corresponding real activity; UNKNOWN,"Association-authorized owner, not assigned",SAMPLE_SYNTHETIC; NOT_ADOPTED/NOT_EXECUTED; REAL_UNKNOWN
FACT-SYN-0141-ACT-02,0141,I19-E31,SAMPLE-ACT-0141-02,hypothetical improvement proposal,Optional expected-use question and example; scope pending approval,§捌 方方案二：課前需求對焦與課堂案例實務情境模組化案,MANUSCRIPT_0141_R06_CANDIDATE.md,Not adopted or executed.,Adjacent IDs are negative-neighbor controls only.,Authorized association source/policy for corresponding real activity; UNKNOWN,"Association-authorized owner, not assigned",SAMPLE_SYNTHETIC; NOT_ADOPTED/NOT_EXECUTED; REAL_UNKNOWN
```


## R06 source math QA receipt: R06_SOURCE_MATH_QA_RECEIPT.json (sha256 `b67ed7b7cf2cc44e19c1d66ab79c4f8455c97d81a9c937e5844c48d591b89543`)

```json
{
  "schema": "ttqs-one-0141-r06-source-math-qa-v1",
  "observed_at_local": "2026-10-25T09:27:11+08:00",
  "doc_id": "0141",
  "requirement_id": "I19-E31",
  "candidate_manuscript_sha256": "2c374341b936ab4e4bb13889f870f42c79e03f688b7e1d92478d1fe052d7d287",
  "verifier_script_sha256": "68f5603cfa308755aa41ab49e7aa6caf1f2033f4fadb0615cd639e7fb73419ce",
  "questionnaire_sha256": "310745e5be17980ca9c623b23e15605cb221c9cbbdf1886913cb54db1acdf0e7",
  "sample_responses_sha256": "723259199dd51973fc6473ec000234cc853fa1511be05864fdfd7b08bb452862",
  "period_summary_sha256": "537c39dcc650d9818779ee3dd4572d64a820720828b9e632e9abb44358777c0b",
  "replacement_register_sha256": "862df5957e732d3d0bce722c52c9dcca63e4555902aec96e31983dc586cbf2aa",
  "response_rows": 36,
  "all_rows_sample_synthetic": true,
  "period_recalculations": [
    {
      "year": "2023",
      "valid_n": 12,
      "return_pct": "80.00",
      "core_answers": 72,
      "pooled_q1_q6": "3.4861",
      "q7_mean": "3.5833",
      "q7_top2_n": 7,
      "q7_top2_pct": "58.33",
      "item_means": {
        "Q1": "3.5000",
        "Q2": "3.4167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "3.5000",
        "Q6": "3.4167",
        "Q7": "3.5833"
      }
    },
    {
      "year": "2024",
      "valid_n": 12,
      "return_pct": "80.00",
      "core_answers": 72,
      "pooled_q1_q6": "3.5694",
      "q7_mean": "3.9167",
      "q7_top2_n": 10,
      "q7_top2_pct": "83.33",
      "item_means": {
        "Q1": "3.5000",
        "Q2": "3.4167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "4.0000",
        "Q6": "3.4167",
        "Q7": "3.9167"
      }
    },
    {
      "year": "2025",
      "valid_n": 12,
      "return_pct": "80.00",
      "core_answers": 72,
      "pooled_q1_q6": "3.6944",
      "q7_mean": "4.2500",
      "q7_top2_n": 11,
      "q7_top2_pct": "91.67",
      "item_means": {
        "Q1": "3.5000",
        "Q2": "3.9167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "4.2500",
        "Q6": "3.4167",
        "Q7": "4.2500"
      }
    }
  ],
  "checks": [
    {
      "year": "2023",
      "metric": "valid_n",
      "match": true,
      "calculated": 12,
      "source": 12
    },
    {
      "year": "2023",
      "metric": "return_pct",
      "match": true,
      "calculated": "80.00",
      "source": "80.00"
    },
    {
      "year": "2023",
      "metric": "core_answers",
      "match": true,
      "calculated": 72,
      "source": 72
    },
    {
      "year": "2023",
      "metric": "pooled_q1_q6",
      "match": true,
      "calculated": "3.4861",
      "source": "3.4861"
    },
    {
      "year": "2023",
      "metric": "q7_mean",
      "match": true,
      "calculated": "3.5833",
      "source": "3.5833"
    },
    {
      "year": "2023",
      "metric": "q7_top2_n",
      "match": true,
      "calculated": 7,
      "source": 7
    },
    {
      "year": "2023",
      "metric": "q7_top2_pct",
      "match": true,
      "calculated": "58.33",
      "source": "58.33"
    },
    {
      "year": "2023",
      "metric": "item_means",
      "match": true,
      "calculated": {
        "Q1": "3.5000",
        "Q2": "3.4167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "3.5000",
        "Q6": "3.4167",
        "Q7": "3.5833"
      },
      "source": {
        "Q1": "3.5000",
        "Q2": "3.4167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "3.5000",
        "Q6": "3.4167",
        "Q7": "3.5833"
      }
    },
    {
      "year": "2024",
      "metric": "valid_n",
      "match": true,
      "calculated": 12,
      "source": 12
    },
    {
      "year": "2024",
      "metric": "return_pct",
      "match": true,
      "calculated": "80.00",
      "source": "80.00"
    },
    {
      "year": "2024",
      "metric": "core_answers",
      "match": true,
      "calculated": 72,
      "source": 72
    },
    {
      "year": "2024",
      "metric": "pooled_q1_q6",
      "match": true,
      "calculated": "3.5694",
      "source": "3.5694"
    },
    {
      "year": "2024",
      "metric": "q7_mean",
      "match": true,
      "calculated": "3.9167",
      "source": "3.9167"
    },
    {
      "year": "2024",
      "metric": "q7_top2_n",
      "match": true,
      "calculated": 10,
      "source": 10
    },
    {
      "year": "2024",
      "metric": "q7_top2_pct",
      "match": true,
      "calculated": "83.33",
      "source": "83.33"
    },
    {
      "year": "2024",
      "metric": "item_means",
      "match": true,
      "calculated": {
        "Q1": "3.5000",
        "Q2": "3.4167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "4.0000",
        "Q6": "3.4167",
        "Q7": "3.9167"
      },
      "source": {
        "Q1": "3.5000",
        "Q2": "3.4167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "4.0000",
        "Q6": "3.4167",
        "Q7": "3.9167"
      }
    },
    {
      "year": "2025",
      "metric": "valid_n",
      "match": true,
      "calculated": 12,
      "source": 12
    },
    {
      "year": "2025",
      "metric": "return_pct",
      "match": true,
      "calculated": "80.00",
      "source": "80.00"
    },
    {
      "year": "2025",
      "metric": "core_answers",
      "match": true,
      "calculated": 72,
      "source": 72
    },
    {
      "year": "2025",
      "metric": "pooled_q1_q6",
      "match": true,
      "calculated": "3.6944",
      "source": "3.6944"
    },
    {
      "year": "2025",
      "metric": "q7_mean",
      "match": true,
      "calculated": "4.2500",
      "source": "4.2500"
    },
    {
      "year": "2025",
      "metric": "q7_top2_n",
      "match": true,
      "calculated": 11,
      "source": 11
    },
    {
      "year": "2025",
      "metric": "q7_top2_pct",
      "match": true,
      "calculated": "91.67",
      "source": "91.67"
    },
    {
      "year": "2025",
      "metric": "item_means",
      "match": true,
      "calculated": {
        "Q1": "3.5000",
        "Q2": "3.9167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "4.2500",
        "Q6": "3.4167",
        "Q7": "4.2500"
      },
      "source": {
        "Q1": "3.5000",
        "Q2": "3.9167",
        "Q3": "3.5000",
        "Q4": "3.5833",
        "Q5": "4.2500",
        "Q6": "3.4167",
        "Q7": "4.2500"
      }
    },
    {
      "metric": "appendix_iii_text_equals_r05",
      "match": true,
      "r05_section_sha256": "15a6caddcfe38cce21ad0a4965d33da4802a66e3801831fa0046733e84d09a17",
      "r06_section_sha256": "15a6caddcfe38cce21ad0a4965d33da4802a66e3801831fa0046733e84d09a17"
    },
    {
      "metric": "all_36_rows_synthetic_and_scores_1_to_5",
      "match": true,
      "rows": 36
    },
    {
      "metric": "questionnaire_and_response_source_hashes_unchanged",
      "match": true,
      "questionnaire_sha256": "310745e5be17980ca9c623b23e15605cb221c9cbbdf1886913cb54db1acdf0e7",
      "responses_sha256": "723259199dd51973fc6473ec000234cc853fa1511be05864fdfd7b08bb452862"
    }
  ],
  "all_checks_pass": true,
  "scope": "Independent deterministic recalculation; no REAL evidence or formal acceptance inferred"
}
```


## R06 build receipt: DOCX_BUILD_RECEIPT_0141_R06_CANDIDATE.json (sha256 `f1c2a9438e44dcc7e9dbab3c78ff65c0ef047e08804ad1776514ca0f0ecb1113`)

```json
{
  "work_id": "TTQS_ONE_0141_I19-E31_R06_DOCX_BUILD",
  "doc_id": "0141",
  "requirement_id": "I19-E31",
  "source_manuscript_sha256": "2c374341b936ab4e4bb13889f870f42c79e03f688b7e1d92478d1fe052d7d287",
  "repair_receipt_sha256": "a4d0b8ce3d87ac5bb242131b56528cd9b9d067e27f44fac221449e52594a07b1",
  "docx_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0141_I19-E31_SOURCE_PREP_R01_20261025\\0141_I19-E31_R06_CANDIDATE.docx",
  "docx_sha256": "e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2",
  "docx_bytes": 163709,
  "native_word_tables": 18,
  "sections": 3,
  "section_layouts": [
    {
      "orientation": "portrait",
      "page_width_twips": 11906,
      "page_height_twips": 16838
    },
    {
      "orientation": "landscape",
      "page_width_twips": 16838,
      "page_height_twips": 11906
    },
    {
      "orientation": "portrait",
      "page_width_twips": 11906,
      "page_height_twips": 16838
    }
  ],
  "source_packet_sha256": "43c0e1bda5dfeb12c1ba8fc8805b876641f5184e4bf95eb4ef6c3182cf8ee964",
  "unique_blueprint_sha256": "e19761674045b2defa7090ba1d8f1224943a89e54811180c20b9ea362de59cda",
  "sample_csv_sha256": "723259199dd51973fc6473ec000234cc853fa1511be05864fdfd7b08bb452862",
  "replacement_register_sha256": "862df5957e732d3d0bce722c52c9dcca63e4555902aec96e31983dc586cbf2aa",
  "source_math_qa_receipt_sha256": "b67ed7b7cf2cc44e19c1d66ab79c4f8455c97d81a9c937e5844c48d591b89543",
  "chart_sha256": "83353077c44d0eb53509a6004767ce9137f67771f283a14b66e9a0031489aa08",
  "embedded_image_count": 1,
  "technical_checks": "PASS",
  "visual_review": "PASS",
  "independent_semantic_review": "PENDING",
  "real_data_status": "UNKNOWN/HOLD",
  "human_formal_acceptance": "NOT_GRANTED",
  "embedded_chart_byte_match": true,
  "visual_receipt_sha256": "6a94d19e5534c05a8600c1af7d3acf242c691b858eae5cbcf4a07484b7dc1386"
}
```


## R06 Word native render receipt: WORD_RENDER_RECEIPT_0141_R06_CANDIDATE.json (sha256 `da97658b5427ff17071033e9c0a34ffbde0773469d002d88f092c265b8f8fcf9`)

```json
{
  "renderer": "Microsoft Word COM",
  "word_version": "16.0",
  "docx_sha256_before": "e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2",
  "docx_sha256_after": "e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2",
  "pdf_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0141_I19-E31_SOURCE_PREP_R01_20261025\\0141_I19-E31_R06_WORD_RENDER_CANDIDATE.pdf",
  "pdf_sha256": "c3a52474035e4c4239a763c565922f071e7c071af817fd1faf89284b1a76367e",
  "pdf_bytes": 1029458,
  "word_reported_pages": 25,
  "visible_window": false,
  "read_only": true,
  "result": "PASS"
}
```


## R06 DOCX technical QA receipt: R06_DOCX_TECHNICAL_QA_RECEIPT.json (sha256 `e7baa0e271dbaf11a16932c097307edc47c7c5438eed7f4697323b496bac918f`)

```json
{
  "schema": "ttqs-one-0141-r06-docx-technical-qa-v1",
  "observed_at_local": "2026-10-25T09:29:34+08:00",
  "doc_id": "0141",
  "requirement_id": "I19-E31",
  "docx_sha256": "e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2",
  "docx_bytes": 163709,
  "pdf_sha256": "c3a52474035e4c4239a763c565922f071e7c071af817fd1faf89284b1a76367e",
  "pdf_pages": 25,
  "text_extraction_path": "DOCX_TEXT_EXTRACTION_0141_R06_CANDIDATE.txt",
  "text_extraction_sha256": "b9d23ec3a917c13a3824a5f06a41f44a7be5f9d848d1f3537d1c8a22933b9416",
  "native_tables": 18,
  "table_dimensions": [
    [
      13,
      2
    ],
    [
      5,
      2
    ],
    [
      5,
      3
    ],
    [
      7,
      4
    ],
    [
      9,
      3
    ],
    [
      5,
      6
    ],
    [
      9,
      7
    ],
    [
      5,
      8
    ],
    [
      5,
      3
    ],
    [
      4,
      4
    ],
    [
      5,
      2
    ],
    [
      9,
      3
    ],
    [
      5,
      2
    ],
    [
      9,
      3
    ],
    [
      37,
      8
    ],
    [
      9,
      4
    ],
    [
      9,
      2
    ],
    [
      6,
      5
    ]
  ],
  "sections": 3,
  "embedded_media_sha256": [
    "83353077c44d0eb53509a6004767ce9137f67771f283a14b66e9a0031489aa08"
  ],
  "checks": [
    {
      "check": "zip_crc",
      "pass": true,
      "detail": null
    },
    {
      "check": "docx_loads",
      "pass": true,
      "detail": null
    },
    {
      "check": "18_native_tables",
      "pass": true,
      "detail": 18
    },
    {
      "check": "3_sections",
      "pass": true,
      "detail": 3
    },
    {
      "check": "one_chart",
      "pass": true,
      "detail": 1
    },
    {
      "check": "36_csv_rows_match_docx_table_exactly",
      "pass": true,
      "detail": {
        "docx_data_table_rows": 36,
        "csv_rows": 36,
        "table_shape": [
          37,
          8
        ]
      }
    },
    {
      "check": "document_identity",
      "pass": true,
      "detail": null
    },
    {
      "check": "version_tag",
      "pass": true,
      "detail": null
    },
    {
      "check": "sample_boundary",
      "pass": true,
      "detail": null
    },
    {
      "check": "acceptance_boundary",
      "pass": true,
      "detail": null
    },
    {
      "check": "correct_q1_q6_header",
      "pass": true,
      "detail": null
    },
    {
      "check": "unknown_source_label",
      "pass": true,
      "detail": null
    },
    {
      "check": "no_unrendered_chart_marker",
      "pass": true,
      "detail": null
    },
    {
      "check": "no_warning_marker",
      "pass": true,
      "detail": null
    },
    {
      "check": "math_receipt_pass_and_bound",
      "pass": true,
      "detail": null
    },
    {
      "check": "build_receipt_binds_exact_docx",
      "pass": true,
      "detail": null
    },
    {
      "check": "word_render_same_docx_bytes",
      "pass": true,
      "detail": null
    },
    {
      "check": "rasterized_all_pages",
      "pass": true,
      "detail": null
    },
    {
      "check": "visual_receipt_exact_sha_pass",
      "pass": true,
      "detail": null
    },
    {
      "check": "correct_embedded_chart_bytes",
      "pass": true,
      "detail": null
    },
    {
      "check": "replacement_register_44_rows_and_r06_locators",
      "pass": true,
      "detail": null
    }
  ],
  "all_checks_pass": true,
  "visual_receipt_sha256": "6a94d19e5534c05a8600c1af7d3acf242c691b858eae5cbcf4a07484b7dc1386",
  "visual_verdict": "PASS",
  "independent_semantic_review": "PENDING",
  "human_formal_acceptance": "NOT_GRANTED",
  "real_data_status": "UNKNOWN/HOLD"
}
```


## R06 visual receipt: VISUAL_REVIEW_RECEIPT_0141_R06_CANDIDATE.json (sha256 `6a94d19e5534c05a8600c1af7d3acf242c691b858eae5cbcf4a07484b7dc1386`)

```json
{
  "schema": "ttqs-one-0141-r06-visual-review-v1",
  "observed_at_local": "2026-10-25T09:28:55+08:00",
  "doc_id": "0141",
  "requirement_id": "I19-E31",
  "docx_sha256": "e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2",
  "pdf_sha256": "c3a52474035e4c4239a763c565922f071e7c071af817fd1faf89284b1a76367e",
  "page_count": 25,
  "render_manifest_sha256": "c3b1e79ccdac263d26a3730ceea50b3b862336811cb02224a109e9f0df2673e0",
  "coverage": "All 25 pages reviewed in contact sheets; 8 representative/high-risk pages also inspected full resolution.",
  "checks": [
    {
      "check": "all_pages_contact_sheet_review",
      "result": "PASS",
      "pages_reviewed": [
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
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25
      ],
      "contact_sheets": [
        {
          "path": "R06_CONTACT_SHEET_1.jpg",
          "sha256": "3bf3bb3425d3c14921783d20cd65d3c699ecd79ce0a8d0327b5be979b1993b74"
        },
        {
          "path": "R06_CONTACT_SHEET_2.jpg",
          "sha256": "e141c524d973c9a630eca8359c8a8434498ae2ee2f86e06249158268ad409a16"
        },
        {
          "path": "R06_CONTACT_SHEET_3.jpg",
          "sha256": "bfc84d38cc5133addbcae3aa726d2949d8241d21ea8da0b7de7f6658ba204aa6"
        }
      ]
    },
    {
      "check": "selected_full_resolution_review",
      "result": "PASS",
      "pages": [
        1,
        8,
        11,
        12,
        14,
        16,
        24,
        25
      ],
      "page_image_sha256": {
        "01": "a0b5b4164ac2e5640ca89fea16e52830e0f5e7572bd685934d90dfaf53a36fd0",
        "08": "472efa49333d1e8cb0713d7eea18e0df29e4b707a0740f77c5fcb0d0aff134eb",
        "11": "977ad2f4ac8034e9b4157da7f37b78336fcbf1e6487221d1af4de779f9061a21",
        "12": "4317b33047bc2ee343ec5ad162c5bb51d8df3eb3b287bc50af66cd554a1b4229",
        "14": "a4b34e1580c3036cec325771f8b54c053c2be26e95d4466417538e1fe339b890",
        "16": "f82e57cbfa07818283e213f5d1738abf63398ccc8606b764432c98675fe4c9b8",
        "24": "1b13e520a0e32d2c3c0c45c9e43c21c32f4be05ce0f1afe970012c753bd2a23a",
        "25": "703c9e4b59e29427bcf971dd4c669e9dcd779dab48bd2ad828a9e6f81ac5d61d"
      }
    },
    {
      "check": "pagination_token_fix",
      "result": "PASS",
      "finding": "UNKNOWN-sourced is no longer split across pages 11/12; whole token starts page 12."
    },
    {
      "check": "tables_and_chart",
      "result": "PASS",
      "finding": "Tables readable; chart legible; no clipping/overlap detected across 25 pages."
    },
    {
      "check": "intentional_whitespace",
      "result": "NONBLOCKING",
      "finding": "Page 16 sample response form leaves lower-page whitespace; page 25 ends after revision history; no content appears clipped or orphaned."
    }
  ],
  "visual_verdict": "PASS",
  "independent_semantic_review": "PENDING"
}
```


## R06 targeted repair receipt: R06_TARGETED_REPAIR_RECEIPT.json (sha256 `a4d0b8ce3d87ac5bb242131b56528cd9b9d067e27f44fac221449e52594a07b1`)

```json
{
  "schema": "ttqs-one-0141-r06-targeted-repair-receipt-v1",
  "observed_at_local": "2026-10-25T09:22:27+08:00",
  "doc_id": "0141",
  "requirement_id": "I19-E31",
  "source_review": "OPENCODE_REVIEWER_ORIGINAL_0141_R05.md",
  "source_review_sha256": "39a50ae2c2d292155479e2c966f30c86731fc82d548451827635cf56300d78bc",
  "repair_packet": "OPENCODE_R06_TARGETED_REPAIR_PACKET.md",
  "repair_packet_sha256": "b3993a7204735664cd5637c42eabb00947af8ab6d92f64e98e98cb7d248d2b8a",
  "writer": "OpenCode v2 CLI",
  "requested_model": "opencode/deepseek-v4.1-flash-free",
  "actual_model_identity": "UNKNOWN",
  "writer_pid": 7420,
  "writer_exit_code": 0,
  "writer_tool_errors": 0,
  "target": "MANUSCRIPT_0141_R06_CANDIDATE.md",
  "target_sha256": "2c374341b936ab4e4bb13889f870f42c79e03f688b7e1d92478d1fe052d7d287",
  "items_addressed": [
    "punctuation-normalization note in Appendices II and IV",
    "rename Q1-Q6 six-dimension answer count and separate Q7 count",
    "make Q5 mean the sole measurable success threshold; qualitative complaint source UNKNOWN",
    "align Q5/Q2/Q6 short labels",
    "replace irreversible crosswalk wording with file hash/version/row manifest"
  ],
  "preserved": [
    "R05 manuscript and DOCX bytes",
    "R01 questionnaire CSV",
    "R01 synthetic response CSV and period summary",
    "Appendix III dataset text"
  ],
  "is_acceptance": false,
  "status": "MANUSCRIPT_REPAIR_COMPLETE_PENDING_DOCX_AND_EXACT_SHA_REVIEW",
  "layout_patch_receipt_sha256": "b74a8b82c5799b5a81268d0d58635b512de1c238c08811554fddbe245a0a17a7"
}
```


## R06 layout patch receipt: R06_LAYOUT_PATCH_RECEIPT.json (sha256 `214d9e35ae5121db338bab04e72559f0c1f799941da39646e6be6f342ae0cfbe`)

```json
{
  "schema": "ttqs-one-0141-r06-layout-token-fix-v1",
  "observed_at_local": "2026-10-25T09:27:11+08:00",
  "doc_id": "0141",
  "requirement_id": "I19-E31",
  "defect": "Word pagination split the live executive success-criterion token UNKNOWN-sourced across pages 11 and 12.",
  "repair": "Replace the first live occurrence hyphen with U+2011 nonbreaking hyphen. The later occurrence is historical revision text and was left unchanged.",
  "old_manuscript_sha256": "4edb0c271429b76176f523322c02f200371c53fce655b242546047f5dd09b7ea",
  "new_manuscript_sha256": "2c374341b936ab4e4bb13889f870f42c79e03f688b7e1d92478d1fe052d7d287",
  "replacements": 1,
  "historical_occurrence_preserved": true,
  "status": "VERIFIED_IN_WORD_RENDER_AND_VISUAL",
  "final_docx_sha256": "e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2",
  "visual_receipt_sha256": "6a94d19e5534c05a8600c1af7d3acf242c691b858eae5cbcf4a07484b7dc1386"
}
```


## Exact candidate text extracted from R06 DOCX (sha256 `b9d23ec3a917c13a3824a5f06a41f44a7be5f9d848d1f3537d1c8a22933b9416`)

The following text was extracted from the binary identified above. The DOCX SHA is `e2a5a981fd364b87a9bd3e096dbc97abeb6b58ed7fb27891d575f12e1d75bdc2`.

顧客滿意度趨勢調查與分析報告
報告基本資訊與狀態標註

版本界線：R06 承接 R05 之 exact-SHA 獨立語意審查所列五項語意 minor 意見與檔案雜湊措辭修正，包含題項標點正規化說明、Q1–Q6 有效填答欄名、方案一質性門檻來源、執行摘要短標籤及替換登記表清冊措辭；未改 R01 CSV、36 筆合成分數與逐期摘要。趨勢圖沿用 R04 同一 SAMPLE 圖檔；R06 為正文修訂標記，不是新資料集。
壹、執行摘要與管理判讀限制
本報告依據 TTQS 指標 19（I19-E31）之品質規範編製，旨在建立一套具備「多期一致量尺」、「明確母體抽樣分母」、「去識別化清理」與「限縮統計推論」之顧客滿意度調查作業體系。本期示範資料涵蓋 2023、2024、2025 連續三個年度之虛構培訓服務顧客滿意度調查結果。
一、三期合成調查核心數據摘要
1. 調查樣本與回收分母：
• 2023 年度：發出邀請 15 份，有效回收 12 份，有效回收率為 80.00%。
• 2024 年度：發出邀請 15 份，有效回收 12 份，有效回收率為 80.00%。
• 2025 年度：發出邀請 15 份，有效回收 12 份，有效回收率為 80.00%。
• 三年合計示範發出邀請 45 份、有效回覆 36 份。36 筆資料的 Q1–Q7 量化欄位均完整；Q8 無文字，不作質性分析。
2. 六大服務構面合成均值（1–5 分 Likert 量尺）：
• 2023 年度六題均值：3.4861 分。
• 2024 年度六題均值：3.5694 分。
• 2025 年度六題均值：3.6944 分。
• 量尺變化趨勢：2025 年度相對 2023 年度基準線，六構面均值增加 0.2083 量尺點（絕不可宣稱為百分比成長率）。
3. 整體滿意度獨立題（Q7，1–5 分 Likert 量尺）：
• 2023 年度 Q7 均值：3.5833 分；正面滿意評價（Top-2，評分 4 或 5 分）人數為 7 人，佔比 58.33%。
• 2024 年度 Q7 均值：3.9167 分；正面滿意評價（Top-2，評分 4 或 5 分）人數為 10 人，佔比 83.33%。
• 2025 年度 Q7 均值：4.2500 分；正面滿意評價（Top-2，評分 4 或 5 分）人數為 11 人，佔比 91.67%。
• 量尺變化趨勢：2025 年度相對 2023 年度基準線，Q7 整體滿意度均值增加 0.6667 量尺點（絕不可宣稱為百分比成長率）。
4. 構面表現觀察：
• 在合成樣本中，Q5 行政溝通由 2023 年之 3.5000 分上升至 2024 年之 4.0000 分，再上升至 2025 年之 4.2500 分；Q2 情境對應由 2023/2024 年之 3.4167 分上升至 2025 年之 3.9167 分。
• 歷年相對偏低之弱項為 Q6 環境設備，三年均值均維持在 3.4167 分，顯示硬體與線上環境為潛在需列管觀察之項目。
二、嚴格管理判讀與推論邊界宣告
警示：嚴禁因果推論與虛假績效宣稱：
1. 本報告中 Q5 與 Q2 之滿意度變化，屬於模擬樣本內之數值變化；報告中所列之「標準化開課前通知訊息」及「課前學習需求對焦確認」兩項改善動作，均為純合成情境之提議（標記為 SAMPLE擬議，NOT_ADOPTED/NOT_EXECUTED）。
2. 嚴禁宣稱「協會已實施上述改善措施」或「改善措施直接促成滿意度提升」。在缺乏真實對照組、嚴謹實驗控制及真實協會簽核執行紀錄前，本報告純粹展示運算邏輯，不得作出任何實質因果宣稱。
3. 每年 12 筆樣本屬於小規模示範資料，無法代表協會全體會員、異質委託單位或所有訓練班別之母體感受。
貳、需求定位、官方來源與相鄰要求界限
為確保評核資料精確聚焦，避免文件混淆，本報告嚴格界定其專屬性與排除範圍：
一、官方規範與藍圖索引定位
• 指標關聯：TTQS 訓練機構版指標 19「目標市場與顧客價值」（成果構面 Outcome）。
• 官方查核項目：I19-E31，查核佐證著重於「顧客滿意度提升」之客觀記錄與跨期趨勢。
• 157 方框索引：編號 155，規範重點在於「多期一致量尺統計、明確調查對象、可比性口徑、實質問題機制、弱項改善追蹤」。
• 評分級距非權重或得分：目前核對的官方第 9 頁摘錄將「4 分」列在 1–5 分計分級距中，未顯示為權重欄；本報告不推算權重，也不得誤植為「協會自評 4 分」或「評核委員已核定給予 4 分」。
二、相鄰要求之嚴格排除與負向比鄰防護（Negative-Neighbor Guard）
本報告僅衡量訓練服務接受者對「服務過程與品質之滿意評價」，嚴禁與下列相鄰績效指標混為一談或相互替代：

1. 排除考照與就業成果（`0139` / `I19-E29` / 索引 153）：學員通過專業證照測驗或成功就業媒合，屬於學習與行為轉化成果，不可作為「顧客滿意度」之佐證數據。
2. 排除資訊系統普及率（`0140` / `I19-E30` / 索引 154）：學員使用 LMS 線上系統、下載講義或打卡之系統普及率，屬於工具採納行為數據，不可直接等同於主觀滿意度評價。
3. 排除營收與業務財務指標（`0142` / `I19-E32` / 索引 156）：訓練業務營業額之增長涉及會計憑證與真實財報核實，與學員對個別課程之滿意度分屬不同構面，絕不得互相混用。
參、調查客群、服務範圍、抽樣框與可比性協定
為使多期調查具備學術與實務上的「可比較性（Comparability）」，本作業程序明確規定調查之受眾定義、抽樣母體與可比性門檻。
一、調查客群與服務範圍定義
• 目標受眾：參與本協會所主辦之特定專業職能進修模組（示範代碼為 SYN-COURSE-YYYY-01）並已完成全期總時數達 80% 以上之學員。
• 客群分層分類原則：
• 個人自費/在職參訓學員（Training Participant）：本報告之 36 筆示範樣本純屬此類別。
• 企業委託包班窗口（Corporate Client）：若未來納入企業委訓業務，由於其關注焦點包含投報率、派訓成效與行政配合，必須獨立建立「企業顧客滿意度調查表」，嚴禁將個人學員回覆與企業委託窗口回覆混合計算，避免樣本構成混雜導致趨勢誤判。
二、抽樣框與分母口徑管理
1. 抽樣母體名冊（Sampling Frame）：每次調查必須產出受邀名冊，名冊應自學員出勤與結訓名單中產生，排除中途退訓或請假逾期之學員。
2. 有效回收分母界定：
有效回收率 = 有效回覆份數 ÷ 實際發出之有效邀請份數 × 100%。
• 嚴格分母規定：計算回收率時，分母僅能為「實際寄發/派發問卷之受邀學員總數」（本示範每年固定為 15 人），嚴禁用全體註冊會員、歷年累計學員或非當期學員作為虛擬分母。
三、三期調查可比性控制條件
多期趨勢若要具備比對價值，必須維持下列四項要素不變：

四、個人隱私與小樣本單元保護（Small-Cell Protection）
以下是降低可識別風險的 SAMPLE 操作建議，不是法律意見、協會已核定政策或已完成的個資作業；正式使用前須由協會授權人員依適用規範與現行政策確認：
1. 去識別化作業：正式問卷不得強制要求填寫姓名或身分證號。原始調查檔中，學員僅以獨立虛擬編號標示（如 SYN-0141-YYYY-NNN）。
2. 小樣本抑制示範：本例提出以 n < 5 作為暫不單獨揭露細格的 SAMPLE 門檻；此數字不是官方門檻或協會既定政策。真實揭露門檻須由有權人員依適用規範、資料組合風險及核定政策確認。
肆、調查行政標準作業程序（SOP）
以下為便於小型協會評估的 SAMPLE 作業方案，尚未經原始點關懷協會核定。日期、次數、截止時點、角色、樣本數及回覆時限均是示範參數；實際採用前由協會有權人員確認並另行發布。

一、發送、催收與收件流程
1. 施測準備（結訓前 1 日）：行政窗口自班務系統匯出符合結訓標準之學員名冊，確認受邀名額（每期標準示範為 15 人），建立受邀名冊（包含唯一發送代碼）。
2. 問卷發送（結訓當日）：於課程最後一單元結束時，由行政人員發放紙本問卷或提供加密線上問卷專屬連結。現場保留 10 分鐘讓學員安靜填答。
3. 催收提醒（結訓後第 2 日與第 4 日）：若結訓當日未達預期回收率，行政人員得透過簡訊或電子郵件發送溫和提醒通知。催收上限為 2 次，嚴禁疲勞轟炸或施加壓力，以維護填答真實性。
4. 收件截止與鎖定（結訓後第 5 日）：收件窗口於結訓後第 5 個工作天下班時（17:00）準時關閉。自系統匯出原始回覆試算表，由行政主管與經辦人員共同確認總收件數，並即刻將原始檔案建立唯讀備份與產生 SHA-256 檢查碼。
二、重複填答、無效回覆與缺漏值清理協定
1. 去重複處理（Deduplication）：若同一位學員因網路斷線等問題提交多次線上回覆，行政人員應依填答時間戳記，保留最後一次完整填答資料，並於清理日誌載明排除之舊時間戳記紀錄。
2. 無效件判定：
• 全份問卷除基本背景外，核心量化題目全部勾選「不適用/不知道（N/A）」者。
• 紙本問卷同一單選題出現雙重勾選且無法辨識原意者，該特定題目計為無效值。
• 疑似無效回覆須依事前明定、可重複判定的客觀規則逐題檢查並記錄理由；單有空白或不適當的 Q8 文字，不應自動使其他有效量化答案失效。若需整份排除，應由實際有權角色按已核定政策覆核。此處角色與政策為 SAMPLE 提議，尚未核定。
3. 缺漏值與「不適用/不知道（N/A）」之統計處理協定：
• 絕對禁止隨意臆補（No Imputation）：嚴禁將未填答之空白處填入「平均值（3 分）」或隨機補值；嚴格禁止將 N/A 或未填答計為 0 分。
• 逐題計算有效回答數（Item-Specific Valid n）：若學員在 Q3 勾選 N/A，則 Q3 之計算分母扣除該人，其餘正常填答題目（如 Q1、Q2）仍屬有效並計入個別題項統計。
• 構面個人合成值門檻（5/6 門檻規定）：若欲計算個別學員之「個人六題合成滿意度」，該學員於 Q1 至 Q6 中必須至少具有 5 題（含）以上 之有效數值（非空白且非 N/A）；若有效題數少於 5 題，則該名學員不計算個人總合成得分，但其已作答之各單題仍保留於各題分母中進行項目分析。
伍、正式量測工具：調查問卷全文與量尺定義
本問卷包含 7 題核心量化題目（均採 1–5 分 Likert 量尺）及 1 題質性開放回饋題。此工具為本報告專屬之標準測量工具，非官方已核定問卷。
一、量尺標準定義
• 【1 分】非常不滿意：各項服務或安排完全不符合期待，遭遇嚴重阻礙或重大瑕疵。
• 【2 分】不滿意：部分服務未達基本標準，整體體驗低於原先預期，需顯著改善。
• 【3 分】普通：各項安排符合基本要求，但無特別突出之處，維持一般水準。
• 【4 分】滿意：服務安排周延合宜，能良好支援個人學習需求，符合或略高於預期。
• 【5 分】非常滿意：各項表現極為卓越，完全契合並超越期待，具極佳之學習支持力。
• 【N/A】不適用/不知道：未接觸該項服務（如線上課程無實體場地需求），不計入該題量化評分分母。
二、問卷完整題項內容
填答前：本表為 SAMPLE 示範工具，並非官方核定問卷。實際使用前由服務單位確認題目與必要性。填答者可不寫姓名或身分證字號；其他資料依核定政策辦理。
班別代碼：________________　日期：________________　匿名回覆編號：________________　客群：□個人參訓 □企業派訓 □其他

量尺：1=非常不滿意，2=不滿意，3=普通，4=滿意，5=非常滿意；N/A=未接觸/不適用，不計該題分母。每題單選；誤選依核定規則標記，不自行補值。
陸、多期調查統計結果與趨勢分析
本章完整載錄 2023、2024、2025 三期合成數據；均值由未四捨五入的原始分數計算後呈現至小數點後四位，百分比至小數點後兩位。Q8 未提供文字，不作質性分析。
一、各期樣本回收與有效母數彙總表

說明：每年 Q1–Q6 六題 × 12 份 = 72 次有效量化填答；Q7 整體滿意度為獨立題，另按每年 12 份計算，不列入本欄。附錄三36筆資料的 Q8 均無文字；附錄二是獨立示範，不納入36筆統計。
二、六大核心構面與整體滿意度逐題歷年統計表

重要說明：均值增減以「量尺點數（Scale Points）」表示，嚴禁以百分比成長率（如宣稱成長幾%）描述 Likert 等距/順序量尺之變動。
三、Q7 整體滿意度正面評價（Top-2 分析）統計表
Top-2 率定義為填答「4（滿意）」或「5（非常滿意）」之受訪者人數佔該題有效總受訪人數之比例：

計算註：跨期百分點差以未四捨五入的比例相減後再四捨五入至小數點後兩位；例如 2025 對 2024 為 (11/12−10/12)×100%=8.3333…，顯示為 8.33 百分點，直接相減已顯示的 91.67%−83.33% 可能得 8.34。
四、三期趨勢視覺化走勢（1–5 分共用量尺）

圖中以同一 1–5 分縱軸呈現六題 pooled index、Q7 整體滿意度及 Q2、Q5、Q6 示範序列；其餘 Q1、Q3、Q4 精確均值見本節逐題表。所有數值均為 SAMPLE/SYNTHETIC，圖表不推論因果。
圖說註記：圖中「六題 pooled index」為 Q1–Q6 六題合併計算之複合指標，不是問卷中的任何單一題目，也不對應 Q1–Q7 任一題；閱讀時不得將該線與個別題項或 Q7 整體題混為同一量測。
柒、樣本數據判讀與推論邊界
一、統計表之客觀描述
本節題項一律沿用第伍章問卷與第陸章統計表之簡短標籤（需求契合、情境對應、師資支援、教材資源、行政溝通、環境設備、整體滿意），不再另創別名；完整題項對照見附錄四之題項標籤對照表。
1. 六構面均值走勢：六題平均分數由 2023 年之 3.4861 分，緩步微升至 2024 年之 3.5694 分（+0.0833 點），至 2025 年達到 3.6944 分（+0.1250 點），三年累計上升 0.2083 量尺點。
2. 關鍵推升構面：
• Q5 行政溝通：為三期中變動幅度最大之構面，自 2023 年的 3.5000 分攀升至 2024 年之 4.0000 分，2025 年更達 4.2500 分，累計上升 0.7500 量尺點。
• Q2 情境對應：在 2023 及 2024 年均維持在相對低點之 3.4167 分，於 2025 年上升至 3.9167 分，單期提升 0.5000 量尺點。
3. 穩定維持構面：Q1（需求契合，3.5000 分）、Q3（師資支援，3.5000 分）、Q4（教材資源，3.5833 分）在三期中數值呈現高度穩定，未出現波動。
4. 相對滯後弱項：Q6（環境設備）連續三年均維持在 3.4167 分，在 2025 年成為全體題項中表現最低之構面。
5. 整體感受（Q7）之敏感度：Q7 總體題上升 0.6667 量尺點，高於六題 pooled index 的 0.2083 點；Top-2 佔比由 58.33% 升至 91.67%。惟本報告只有彙總數據，不足以判斷個人層級關聯，不能推論光環效應，也不能說明變化原因。
二、方法學與推論限制（Methodological Limitations）
為維持評核與管理誠信，本報告特別申明下列推論限制：
1. 極小樣本數限制：每年僅 12 份有效回覆，單一回答若相差 2 分，在 n=12 時會令該題均值相差 0.1667 點。這是本示範的數值敏感度說明；資料沒有證明採用機率抽樣，也未追蹤同一批受訪者，因此不能據此推論母體或個人變化。
2. 無對照組設計：本調查未導入隨機對照實驗（RCT）或準實驗設計，無法排除霍桑效應（Hawthorne Effect）、學員自我選擇偏誤（Self-Selection Bias）或當期社會環境變遷之外部干擾。
3. 因果關係阻斷：雖然資料上呈現 Q5 與 Q2 之上升，但「不可推論」係因行政人員實施了特定改善。任何未經嚴謹驗證之措施宣稱，均屬違反 TTQS 實證精神。
4. 單一客群之限制：36 筆 SAMPLE 全部標記為 TRAINING_PARTICIPANT_SYNTHETIC 單一客群，未含企業委託或其他客群分層；因此本章之數值變化僅描述此一示範客群，不得引申為任何客群間（segment）比較結論，也不能作為分層政策或資源配置之依據。
捌、SAMPLE 擬議持續改善循環（PDCA）
本章所列兩項均為回溯示範（retrospective demonstration）：以已完成的 2023–2025 SAMPLE 系列為素材，說明如何把觀察到的數值差異轉成待核定問題。兩項方案本身、其後的執行與後續查證均尚未發生（NOT_ADOPTED / NOT_EXECUTED），下一個可比較週期屬未來工作；因此不存在「先提案、後改善、再看到分數上升」的時序。年度分數本身為合成資料，方案與年度變化沒有時間因果關係；真實使用時應先收集可核實問題證據，再由有權人員設定目標與核准方案。

次期資料判讀與處置表（SAMPLE 決策工具，非協會核定政策）

本表僅示範如何把證據連到次期決策，並非協會現行規章、已核准門檻或已作成的決議；正式採用須由實際授權人員確認。
兩項 SAMPLE 擬議行動方案內容
【方案一】標準化課前通知與行政溝通單一窗口建置案
• 行動方案識別碼：SAMPLE-ACT-0141-01
• 方案性質：回溯示範（retrospective demonstration），素材為已完成的 2023–2025 SAMPLE 系列；方案、執行與後續查證均未發生，下一個可比較週期屬未來工作。
• 對應期別轉折（回溯對照）：2023 年度 → 2025 年度；此為既有 SAMPLE 資料的回溯對照，不是方案實施前後的前後比較。
• 提案數據依據：合成 Q5 均值由2023年3.5000點變為2025年4.2500點（2023→2025 累計量尺點差，非方案前後差異）；附錄三的Q8沒有文字，因此沒有質性回覆支持「信件混亂」或「回信窗口不一」等說法。提案只示範如何把量化弱項轉為待核定問題，不代表曾採取行動。
• 擬議具體作法：若經授權採用，可先試用一份課前通知清單，列出已核實的上課資訊與教材取得方式，並指定一個已核定的聯絡管道。7日前通知與4小時回覆僅為待核定的 SAMPLE 參數，不代表協會現有承諾或服務水準。
• 建議負責角色：訓練行政專員（Training Administration Role）
• 回查檢驗期程：尚未發生；下一個可比較週期屬未來工作。若未來經協會授權採用，方於該未來週期調查收件截止後 10 個工作天內回查（10 個工作天為 SAMPLE 參數，非既定期程）。
• 具體成效檢驗指標：在維持 Q5 題目文字與 1–5 量尺完全不變下，Q5 有效均值應達到 3.8000 分以上；此為本方案唯一可量測之成功門檻。原擬附加之「無行政聯繫延誤之負面抱怨」條件屬 UNKNOWN‑sourced：本 SAMPLE 樣本沒有真實抱怨紀錄或 Q8 證據，且不得由空白 SAMPLE 註解推定抱怨不存在；若未來採用該質性條件，須先由協會授權人員界定可核實之來源、負責角色、統計期間與升級處理規則。
• 當前狀態標註：SAMPLE_HYPOTHETICAL_NOT_ADOPTED（純合成示範，未正式立案核准，未實際執行，亦未進行後續查證）。
• 未達標處理機制（HOLD / REVISE）：若經協會事前核定的示範目標未達，先暫停擴大此方案，檢查可取得的發送完成狀態及匿名回饋，再提出修訂案；不得由本 SAMPLE 文字直接決定採購或實際支出。
【方案二】課前學習需求對焦與課堂案例實務情境模組化案
• 行動方案識別碼：SAMPLE-ACT-0141-02
• 方案性質：回溯示範（retrospective demonstration），素材為已完成的 2023–2025 SAMPLE 系列；方案、執行與後續查證均未發生，下一個可比較週期屬未來工作。
• 對應期別轉折（回溯對照）：2024 年度 → 2025 年度；此為既有 SAMPLE 資料的回溯對照，不是方案實施前後的前後比較。
• 提案數據依據：合成 Q2 均值在 2024 年為3.4167點、2025 年為3.9167點（2024→2025 量尺點變化；2023 年同為3.4167點）。36筆Q8沒有文字，不能推論「理論偏多」或學員實際應用困難；此提案只示範如何調查問題。
• 擬議具體作法：如獲授權，可先試行一題自願填答的「預計應用情境」，由講師與行政窗口共同挑選一個示範案例。20字上限與課前3日是 SAMPLE 參數；實際蒐集前須核定且不得要求不必要的個人或敏感資料。
• 建議負責角色：課程協調專員與授課師資組（Course Coordination Role）
• 回查檢驗期程：尚未發生；下一個可比較週期屬未來工作。若未來經協會授權採用，方於該未來週期調查收件截止後 10 個工作天內回查（10 個工作天為 SAMPLE 參數，非既定期程）。
• 具體成效檢驗指標：在維持 Q2 題目文字與 1–5 量尺完全不變下，Q2 有效均值應達到 3.7000 分以上，且 Top-2 佔比應突破 75%（分母為 Q2 自身有效回答數，見附錄四單題 Top-2 公式）。
• 當前狀態標註：SAMPLE_HYPOTHETICAL_NOT_ADOPTED（純合成示範，未正式立案核准，未實際執行，亦未進行後續查證）。
• 未達標處理機制（HOLD / REVISE）：若事前核定的示範目標未達，先由實際負責課程的人員檢視題目與案例是否對應，再決定是否提出修訂；本文件不假定協會設有排課委員會，也不授權調整師資。
玖、調查拒收、分析退回與趨勢暫停判準（Gate & Hold Rules）
以下13項是本文件提出的 SAMPLE 內部品質檢核建議，並非 TTQS 官方退件規則或原始點關懷協會現行政策。若協會採用，須由實際有權人員核定角色、例外及申訴處理；是否正式提交仍按正式權責決定：
1. 識別碼混淆（Conflation of IDs）：將官方第 9 頁的 4 分級距誤寫為權重或協會實得分數，或混淆 0141、I19-E31 與 157 索引 155 者，立即退回修正。
2. 空白制度模板替代實質報告：僅檢附未經施測填寫之空白問卷樣張，缺乏多期具體有效回收分母與真實/合成回覆記錄者，判定為未具備佐證效力。
3. 跨期量尺或題意變更未設警告：若任一期私自更動 Q1–Q7 之中文題目字句、順序，或將 5 點量尺竄改為 7 點量尺，跨期趨勢線必須標記 TREND_NOT_COMPARABLE_HOLD，不得直接接續繪製趨勢圖。
4. 缺乏有效分母（Missing Denominator）：僅提供百分比或均值，卻未揭露發出邀請數（N）與有效回覆數（n）之詳細人次者，一律退回。
5. 違規補值或計零（N/A Treated as Zero or Imputed）：將空白題、N/A 視為 0 分計入平均，或擅自以全體平均數補植遺漏值者，判定為資料污染，統計無效。
6. 點數差錯報為百分比成長（Percent Growth Error）：將 Likert 量尺點數之相減差距（如 0.2083 點）誤報為「成長 20.83%」或將滿意度均值除以基準線宣稱成長率者，退回重寫。
7. 無效件或流失樣本無交代：回收率低於 100% 時，未交代未回覆者與流失者之處理原則，逕自將分母等同於分子者，予以糾正。
8. 客群結構異質混合（Segment Confounding）：將不同性質之客群（如個人在職班與企業派訓班）在未分層之情況下強行合併，因樣本組成改變引致之分數變化，不得列為常態滿意度趨勢。
9. 合成數據冒充真實紀錄（Synthetic as Real）：將 SAMPLE 示範資料記載為協會歷年學員之真實姓名、真實評核表現者，屬重大誠信缺失，立即撤銷。
10. 績效指標偷換（Construct Substitution）：試圖以滿意度調查替代就業率（I19-E29）、資訊系統使用率（I19-E30）或營收獲利（I19-E32）者，嚴格予以剔除。
11. 缺乏實證之因果宣稱（Unverified Causal Leap）：在無對照實驗或完整驗證日誌下，宣稱「某行政措施成功讓整體滿意度顯著躍升」者，必須刪除因果關聯文句。
12. 缺乏權責追蹤與回查機制：分析報告未指出弱項，或提出的改善計畫未載明負責角色、檢核期程、未達標因應機制者，視為無效管理報告。
13. 稽核軌跡缺失（Missing SHA / Source Trace）：報告數據無法對應至原始問卷存檔或去識別化匯出檔之 SHA-256 雜湊碼者，不得送交審查。
拾、真實資料替換、個資保護與稽核軌跡保存機制
以下為真實資料替換的 SAMPLE 檢核流程，不是已核定的協會政策；正式蒐集前由協會授權人員依適用規範與現行政策確認：
一、真實資料替換四步檢核流程（SAMPLE）
[步驟 1：母體清點與真實抽樣]
   │ 產出真實學員受邀名單 (確認發出數 N)
   ▼
[步驟 2：原始數據匯入與去識別化]
   │ 抹除真實身分識別，賦予唯一隨機代碼 (SYN/REAL-ID)
   ▼
[步驟 3：填寫替換登記表 (Replacement Register)]
   │ 記錄新舊檔案之 SHA-256 雜湊值與資料筆數，建立檔案版本／SHA-256／筆數清冊（manifest）
   ▼
[步驟 4：重新執行確定性檢驗腳本]
   │ 重新運算逐題均值與 Top-2，確認可重算、無邏輯矛盾
   │ 計算通過本身不會自動晉級，也不改變資料性質
   ▼
[步驟 5：授權角色審查（CURRENT 晉級關卡）]
   │ 由協會實際授權角色審查來源、權限、重算與獨立複核結果
   ▼
[狀態：CURRENT（候選）]
   │ CURRENT ≠ REAL，也不等於正式接受（formal acceptance）
   │ 僅表示經授權角色審查後之候選狀態
1. 真實抽樣與名冊建立：由訓練主管自教務資料庫匯出結訓名冊，依核定之抽樣比例產生受邀受訪者清冊，確認發放分母 N。
2. 去識別化與代碼轉換（Anonymization）：在匯入統計軟體前，必須將姓名、電話、電子郵件、服務公司等直接識別資訊完全移除，改以隨機識別碼取代。如確需保存識別對照資料，保管方式、存取角色、加密與刪除期限均須由協會依核定政策決定；本文件不指定實體媒體或人員職權。公開 GitHub 不放識別資料。
3. 填寫真實資料替換登記表（Replacement Register）：詳細記錄替換日期、經辦人員、真實資料筆數、資料來源系統、新資料庫之 SHA-256 檔案檢查碼。
4. 驗證與狀態更新：執行自動化資料校驗腳本，重新產出統計表。合成樣例不得因計算通過而自動變為 REAL 或正式接受。晉級 CURRENT 須另經協會實際授權角色審查，且 CURRENT 僅為候選狀態，不是 REAL，也不是正式接受；計算通過本身不會促成任何晉級。真實替換須先核驗來源與權限、重算及獨立複核；任何正式狀態由協會實際授權人員決定，Human formal acceptance 未授予。
二、資料庫稽核軌跡（Audit Trail）保存辦法
1. 保存期限：`UNKNOWN / REFER_TO_APPROVED_POLICY`。本示範不設定年限，也不推定主管機關要求。真實資料的保留/刪除期限、存取權及保存位置須依協會核定政策及適用規範確認後再執行。
2. 電子檔案防竄改機制：每一期調查收件截止當日產出之最終 CSV 原始檔，必須立即產出 SHA-256 雜湊值，並記載於工作日誌中。後續任何統計分析均需以此基準檔進行，嚴禁直接修改原始檔案內容。
拾壹、附錄
附錄一：可直接印製/發送之單次調查空白紀錄表樣張
(本表供訓練行政人員於課堂現場直接列印使用，版面配置已針對 A4 紙張最佳化)


量尺端點：1=非常不滿意；2=不滿意；3=普通；4=滿意；5=非常滿意；N/A=不適用，不計入該題分母。此表為 SAMPLE，非協會已核定或已施測紀錄。
附錄二：完整填妥之 SAMPLE 調查回覆紀錄範例
(以下為獨立完整填答示範，使用合成案號 `SYN-0141-EXAMPLE-001`；不屬於附錄三36筆統計資料，也不參與計算。)


（Q1–Q7 題目文字逐字取自凍結版題項檔 `QUESTIONNAIRE_ITEMS_0141_R01.csv`。該 CSV 以正規化後之題目字串儲存，未含中文列舉頓號與句末標點；列印用正式題項文字見第伍章與附錄一。此僅為標點與空格之正規化，不改變凍結題項語意；示範答案均維持原合成分數。）
此獨立填答範例全屬 SAMPLE，未加入36筆趨勢資料、未在協會系統建檔，不能當成真實回收或審查紀錄。

附錄三：三期完整 36 筆合成原始回覆資料集（Canonical Dataset）
本表逐列載錄36筆合成回覆；分數依序為 Q1 至 Q7。36筆均為 SAMPLE，Q8 欄均標示無文字；附錄二是獨立填答示例，不進入統計。


附錄四：資料字典與計算公式手冊
1. 欄位定義資料字典
• record_state：資料列屬性旗標，字串。本 SAMPLE 資料集唯一允許值為 SAMPLE_SYNTHETIC（表示該列全為合成示範，不是真實回覆）。REAL 對應詞彙與任何正式狀態值為 UNKNOWN，本文件不推定、不自創。
• period_year：調查所屬年度（西元年整數，如 2023、2024、2025）。
• service_cohort_id：參訓服務梯次唯一識別碼。
• sample_case_id：單一受訪回覆去識別化隨機案號，格式為 SYN-0141-YYYY-NNN。逐列事實識別碼為資料集層級 ID FACT-SYN-0141-SAT-TREND-R01 加上本欄案號尾碼 -YYYY-NNN；資料集 ID 本身不得當成單列 ID 使用。
• response_date_synthetic：合成回覆日期（YYYY-MM-DD 文字）。本示範全部為虛構日期，僅供列內排序與期間對照，不得當成真實施測、收件或簽核日期。
• customer_segment：客群分層欄，字串。本示範唯一出現值為 TRAINING_PARTICIPANT_SYNTHETIC（個人參訓學員之合成標記）。此欄為分層鍵（stratification key）：任何跨期、跨方案或跨客群比較均須先以此欄分層，不得把不同客群未分層合併。其他客群詞彙（例如企業委託）未出現於本示範，實際允許值須由協會依核定政策決定，UNKNOWN。
• Q1_need_fit 至 Q6_learning_environment（正文簡寫 Q1–Q6）：核心服務構面評分，有效數值為整數 1 至 5；N/A 記為 null，不參與該題平均值計算。
• Q7_overall_satisfaction（正文簡寫 Q7）：整體滿意度獨立題評分，有效數值為整數 1 至 5。
• Q8_open_comment（正文簡寫 Q8）：質性開放回饋意見，文字型態，不進行量化分數編碼。
題項標籤對照表（正文含§柒之唯一標籤來源）

正文之題項標籤一律以上表為準（Q4＝教材資源、Q6＝環境設備）；上表題目文字逐字對應凍結版題項檔 QUESTIONNAIRE_ITEMS_0141_R01.csv，該檔以正規化字串儲存題目（未含中文列舉頓號與句末標點），列印用正式題項文字見第伍章與附錄一；此標點與空格之正規化不改變凍結題項語意。
2. 標準統計運算公式
• 單題有效平均值（Item Mean）：
第 k 題平均值 = 該題有效分數總和 ÷ 該題有效回答人數。
計算僅使用該題有效分數；排除 N/A 與空白，並逐題揭露該題實際有效回答人數，不能用全問卷回覆數代替單題分母。
• 六構面綜合指數均值（Six-Item Index Mean）：
六題 pooled index = Q1–Q6 所有有效 1–5 分數總和 ÷ Q1–Q6 所有有效回答數；Q7 不納入。
本組 SAMPLE 各題有效 n 均為 12，因此 pooled index 與六個題目均值的算術平均相等；若未來任一題有 N/A 或有效 n 不同，必須採 pooled ratio，不得平均六個題目均值替代。
• Top-2 正面滿意率（Top-2 Proportion）：
Q7 Top-2比例 = Q7評分4或5的有效回答人數 ÷ Q7有效回答總人數 × 100%。
分子只計 Q7 有效答案中評分為 4 或 5 的人數；分母是 Q7 的有效回答數，不使用受邀人數或其他題項分母。
• 單題 Top-2 正面滿意率（Item-level Top-2 Proportion）：
第 k 題（Qk）Top-2比例 = Qk評分4或5的有效回答人數 ÷ Qk全部有效回答人數 × 100%。
分子與分母都限定同一題 Qk：分母是該題的有效回答數（排除 N/A 與空白），不是受邀人數、不是全問卷回覆數，也不是其他題項的分母。方案二之 Q2 Top-2（目標 75%）即採此 Q2 專屬分母計算；Q7 仍依上一項 Q7 公式，不得改用 Q1–Q6 的分母。
• 跨期量尺點數差距（Point Delta）：
量尺點差 = 期末均值 − 期初均值；先用未四捨五入均值相減，再呈現至小數點後四位。
結果以「量尺點（Points）」標示，嚴禁計算百分比變更。
附錄五：真實資料替換登記表（Replacement Register Template）與版本控制紀錄
1. 真實資料替換登記表（目前為範本與合成狀態記錄）

2. 版本修訂歷史紀錄

本報告正文至此結束。本文件為候選方法示範（SAMPLE）；示例組織、時間、數字、答案與提案均為合成。REAL=UNKNOWN/HOLD；Human formal acceptance=NOT_GRANTED；Official score=NOT_ASSIGNED。
項目
內容說明
文件名稱
顧客滿意度趨勢調查與分析報告
文件編號
0141
官方指標與要求編號
指標 19「目標市場與顧客價值」／ 要求編號 I19-E31
157 方框清單索引
索引編號 155（顧客滿意度上升：多期同量尺統計）
官方佐證資料定位
勞動部勞動力發展署 TTQS 評核佐證文件資料表（訓練機構版）實體 PDF 第 9 頁，正式要求文字：「顧客滿意度提升。」
官方第 9 頁 4 分標註
目前核對的第 9 頁摘錄將 4 分列在 1–5 分計分級距中，未顯示為權重欄；本報告不據此推算權重或本協會得分。官方實得分數 NOT_ASSIGNED。
文件名稱來源
「顧客滿意度趨勢調查與分析報告」取自 129→142 交付對照表（Crosswalk）之 I19-E31／0141 欄位，非官方原始 PDF 第 9 頁標題
印刷版核選序號
UNKNOWN（現有檔案資料庫尚未證明印刷版 checkbox serial，依誠信原則標示為未知）
報告版本與合成事實識別碼
正文修訂 R06 ／ 資料集層級合成事實識別碼：FACT-SYN-0141-SAT-TREND-R01（代表36筆 SAMPLE 資料集整體，不是單筆回覆的識別碼）。逐列登錄用事實識別碼為此基礎 ID 加上對應案號尾碼 -YYYY-NNN（例：基礎 ID 加 -2023-001）；兩者層級不同，不得互相替代。
本報告資料屬性宣告
全份資料為 SAMPLE / SYNTHETIC。年份、邀請數、回覆、課程情境、答案、分析與改善提案均為合成示範；不代表原始點關懷協會或任何單位的真實活動、受訪者、回收率或辦訓績效。REAL = UNKNOWN / HOLD。
真實資料狀態 (REAL)
REAL = UNKNOWN / HOLD；實際蒐集、保存及使用方式須由協會授權人員依適用規範與已核定政策確認。
外部核定狀態
Human formal acceptance = NOT_GRANTED；Official score = NOT_ASSIGNED（候選候審文件，未獲主管機關或正式評核員實質核定）
文件/要求
本件衡量或排除的內容
本件 0141 / I19-E31 / 索引155
顧客對訓練服務過程的滿意感受；使用同量尺、多期分母與限制說明。
0139 / I19-E29 / 索引153
考照與就業成果；不能用證照或就業率代替滿意度。
0140 / I19-E30 / 索引154
訓練資訊系統使用情形；登入/下載率不能代替主觀滿意度。
0142 / I19-E32 / 索引156
訓練業務營收與財務資料；營收不能代替滿意度。
檢驗維度
可比性維持條件
異常處理與凍結機制（HOLD）
問卷題項與語意
核心量化 7 題（Q1–Q7）文字、意涵與題目順序跨期保持完全一致。
若題目文字經修正，該題視為新題項，中斷歷史連續趨勢比對。
量尺標準
統一採用 1 至 5 分 Likert 量尺，語意端點嚴格固定（1=非常不滿意，5=非常滿意）。
若變更為 1–7 分或百分制，跨期均值即刻宣告不可比，啟動趨勢比對中止（HOLD）。
施測時機與管道
均於課程結訓當週（結訓當日至結訓後 5 個工作天內）透過標準線上/紙本管道完成。
若某期改為結訓半年後電訪，因遺忘效應不可與即時回覆直接合併趨勢。
樣本構成比例
受訪學員背景構成（職級、專業領域）跨期應維持相當。
若某期學員突然全數變更為初階志工或高階主管，須分層揭露，不可盲目計算全體總均值。
步驟
SAMPLE 建議做法
輸入/檢查
產出與停點
1. 定義名冊
依實際服務與核定範圍建立受邀母體；示範 N=15，不代表協會班級規模。
受邀資格、當期服務定義。
受邀人數 N；範圍不清先 HOLD。
2. 發送與提醒
使用核定管道發送；提醒次數與時點由協會核定。
發送紀錄、回覆狀態。
已發送份數與未回覆清單；避免施壓。
3. 鎖定與去重
匯出原始答覆、保留唯讀副本及 SHA-256；依事前規則去重。
原始回覆、時間戳、排除理由。
可追溯清理資料；規則不明先 HOLD。
4. 清理
逐題檢查 1–5、N/A、空白與無效值；不補平均、不將 N/A 當 0。
題項字典、有效回答數。
每題有效 n；不足時不計個人合成值。
5. 計算
分別計算 Q1–Q6 與 Q7，揭露分母、點數差與 Top-2。
經核對的乾淨資料。
可重算表與品質檢查。
6. 解讀與改善
描述弱項與限制，形成 SAMPLE 待核定提案；不得推論因果。
統計表、可用的 Q8 文字。
擬議行動、待核定角色/期限及未達標 HOLD 條件。
題號/構面
題目
作答選項
Q1 需求契合
本次訓練服務內容符合我在報名前表達的需求。
□1非常不滿意　□2不滿意　□3普通　□4滿意　□5非常滿意　□N/A
Q2 情境對應
課程內容能對應我預計運用的工作、志工或學習情境。
□1　□2　□3　□4　□5　□N/A；端點語意同上
Q3 師資支援
講師的說明、示範與回應有助於我理解課程。
□1　□2　□3　□4　□5　□N/A
Q4 教材資源
教材與學習資源容易取得，並能支持我完成學習。
□1　□2　□3　□4　□5　□N/A
Q5 行政溝通
報名、課前通知與行政回覆清楚且及時。
□1　□2　□3　□4　□5　□N/A
Q6 環境設備
學習場地或線上環境與設備適合本次服務。
□1　□2　□3　□4　□5　□N/A
Q7 整體滿意
整體而言，我對本次訓練服務感到滿意。
□1　□2　□3　□4　□5　□N/A
Q8 開放回饋
本次最有幫助的是什麼？下一次最希望改善什麼？
自由填答；不計入量化均值。
年度
發出邀請數 (N)
有效回收數 (n)
有效回收率 (%)
Q1–Q6 六構面有效填答次數
資料屬性狀態
2023
15
12
80.00%
72
SAMPLE / SYNTHETIC
2024
15
12
80.00%
72
SAMPLE / SYNTHETIC
2025
15
12
80.00%
72
SAMPLE / SYNTHETIC
全期合計
45
36
80.00%
216
SAMPLE / SYNTHETIC
題號與評量向度
2023 年均值 (n=12)
2024 年均值 (n=12)
2025 年均值 (n=12)
2023→2024 點數變化
2024→2025 點數變化
2023→2025 全期點數變化
Q1 需求契合
3.5000
3.5000
3.5000
+0.0000
+0.0000
+0.0000
Q2 情境對應
3.4167
3.4167
3.9167
+0.0000
+0.5000
+0.5000
Q3 師資支援
3.5000
3.5000
3.5000
+0.0000
+0.0000
+0.0000
Q4 教材資源
3.5833
3.5833
3.5833
+0.0000
+0.0000
+0.0000
Q5 行政溝通
3.5000
4.0000
4.2500
+0.5000
+0.2500
+0.7500
Q6 環境設備
3.4167
3.4167
3.4167
+0.0000
+0.0000
+0.0000
六構面綜合均值 (Q1–Q6)
3.4861
3.5694
3.6944
+0.0833
+0.1250
+0.2083
Q7 整體滿意度（獨立總體題）
3.5833
3.9167
4.2500
+0.3333
+0.3333
+0.6667
年度
Q7 有效受訪數 (n)
評分 1-3 分人數
評分 4 分人數
評分 5 分人數
Top-2 人數 (4+5 分)
Top-2 佔比 (%)
趨勢變化 (百分點)
2023
12
5
7
0
7
58.33%
基準線
2024
12
2
9
1
10
83.33%
+25.00 百分點
2025
12
1
7
4
11
91.67%
+8.33 百分點
全期變化
--
-4 人
0 人
+4 人
+4 人
--
+33.33 百分點
順序
工作內容
核對與決策
1. 讀取示範結果
只描述有資料的 Q5/Q2 數值；本例 Q8 無文字。
不自行補造受訪者理由。
2. 提出 SAMPLE 方案
寫清問題、擬議做法、量尺/目標、角色與 HOLD 條件。
標示 NOT_ADOPTED / NOT_EXECUTED。
3. 權責確認
由協會實際授權人員決定是否採用、修改或拒絕。
當前正式核准狀態 UNKNOWN。
4. 後續查證
若未來真實採用，保留前後來源與同口徑問卷，再比較下一期。
資料未取得前不得宣稱效果或因果。
選項
何時考慮
必須先有的證據
示範處置與狀態
CONTINUE 維持觀察
服務定義、核心題目、量尺與分母口徑可比，資料檢核未發現明確異常；僅延續觀察，不等同宣告改善有效。
當期問卷版本、邀請與有效回覆分母、逐題有效 n、原始檔檢查碼及與前期的可比性檢核。
保留既有量測，下一期依同一口徑重算；SAMPLE 建議，待有權人員決定。
CHANGE 提出修訂
有可追溯的題項弱點或重複問題資料，且證據足以指出要檢查的服務環節；不得僅由總體均值推測原因。
對應題項統計、可核實的匿名回饋或服務流程紀錄、問題與構面對照、修訂理由及修訂前後版本。
先提出待核准修訂；若題目或服務定義改變，另起可比性基線，不直接接續舊趨勢。
HOLD 暫停比較／採用
權限、來源、分母或原始檔不可核；核心題意、量尺、服務範圍或客群構成改變而尚無可比處理；重要欄位缺失。
來源與授權查核、原始問卷/邀請清冊、去重與排除紀錄、變更前後題目及客群構成證據。
暫停發布趨勢結論與採用改善成效，先補證或重新設定基線；目前 REAL 仍為 UNKNOWN / HOLD。
欄位
填答
班別代碼
______________________________
填答日期
______________________________
匿名回覆編號
______________________________
客群
□個人參訓　□企業派訓　□其他
題號/構面
題目
請勾選一項
Q1 需求契合
本次訓練服務內容符合我在報名前表達的需求。
□1　□2　□3　□4　□5　□N/A
Q2 情境對應
課程內容能對應我預計運用的工作、志工或學習情境。
□1　□2　□3　□4　□5　□N/A
Q3 師資支援
講師的說明、示範與回應有助於我理解課程。
□1　□2　□3　□4　□5　□N/A
Q4 教材資源
教材與學習資源容易取得，並能支持我完成學習。
□1　□2　□3　□4　□5　□N/A
Q5 行政溝通
報名、課前通知與行政回覆清楚且及時。
□1　□2　□3　□4　□5　□N/A
Q6 環境設備
學習場地或線上環境與設備適合本次服務。
□1　□2　□3　□4　□5　□N/A
Q7 整體滿意
整體而言，我對本次訓練服務感到滿意。
□1　□2　□3　□4　□5　□N/A
Q8 開放回饋
本次最有幫助的是什麼？下一次最希望改善什麼？
______________________________________________
基本欄位
SAMPLE 示範內容
班別
SAMPLE 訓練服務模組
日期
SAMPLE 示範日期；不屬於附錄三36筆資料
案號
SYN-0141-EXAMPLE-001（獨立示範）
客群
個人參訓（僅示範選項）
題號
題目（逐字引用凍結題項）
示範答案
Q1
本次訓練服務內容符合我在報名前表達的需求
4（滿意）
Q2
課程內容能對應我預計運用的工作志工或學習情境
5（非常滿意）
Q3
講師的說明示範與回應有助於我理解課程
3（普通）
Q4
教材與學習資源容易取得並能支持我完成學習
4（滿意）
Q5
報名課前通知與行政回覆清楚且及時
5（非常滿意）
Q6
學習場地或線上環境與設備適合本次服務
3（普通）
Q7
整體而言我對本次訓練服務感到滿意
4（滿意）
Q8
本次最有幫助的是什麼？下一次最希望改善什麼？
【合成示範文字，非真實訪談】課前資訊清楚、教材容易取得；可再檢查教室舒適度與插座需求。
狀態
年度
班別代碼
合成案號
日期
客群
Q1→Q7（依序）
Q8文字狀態
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-001
2023-01-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 3 / 4 / 3 / 3 / 4 / 3
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-002
2023-02-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 3 / 3 / 4 / 3 / 3
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-003
2023-03-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 4 / 3 / 3 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-004
2023-04-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 3 / 3 / 4 / 3 / 3 / 3
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-005
2023-05-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 4 / 3 / 4 / 4 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-006
2023-06-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 4 / 4 / 3 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-007
2023-07-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 3 / 3 / 4 / 3 / 3
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-008
2023-08-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 4 / 4 / 4 / 3 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-009
2023-09-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 3 / 4 / 3 / 4 / 3 / 3
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-010
2023-10-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 3 / 4 / 3 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-011
2023-11-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 4 / 4 / 4 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2023
SYN-COURSE-2023-01
SYN-0141-2023-012
2023-12-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 3 / 4 / 4 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-001
2024-01-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 3 / 4 / 3 / 4 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-002
2024-02-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 3 / 3 / 4 / 3 / 3
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-003
2024-03-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 4 / 3 / 4 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-004
2024-04-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 3 / 3 / 4 / 3 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-005
2024-05-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 4 / 3 / 4 / 5 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-006
2024-06-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 4 / 4 / 3 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-007
2024-07-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 3 / 3 / 5 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-008
2024-08-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 4 / 4 / 4 / 3 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-009
2024-09-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 3 / 4 / 3 / 5 / 3 / 3
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-010
2024-10-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 3 / 4 / 3 / 4 / 5
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-011
2024-11-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 4 / 4 / 5 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2024
SYN-COURSE-2024-01
SYN-0141-2024-012
2024-12-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 3 / 4 / 4 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-001
2025-01-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 4 / 3 / 4 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-002
2025-02-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 3 / 3 / 4 / 3 / 3
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-003
2025-03-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 4 / 4 / 3 / 4 / 4 / 5
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-004
2025-04-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 3 / 3 / 4 / 4 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-005
2025-05-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 5 / 3 / 4 / 5 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-006
2025-06-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 4 / 4 / 3 / 4 / 5
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-007
2025-07-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 5 / 3 / 3 / 5 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-008
2025-08-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 4 / 4 / 4 / 4 / 4 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-009
2025-09-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 4 / 3 / 5 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-010
2025-10-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 3 / 3 / 4 / 3 / 4 / 5
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-011
2025-11-20
TRAINING_PARTICIPANT_SYNTHETIC
4 / 4 / 4 / 4 / 5 / 3 / 4
SAMPLE_ONLY; no actual respondent text
SAMPLE_SYNTHETIC
2025
SYN-COURSE-2025-01
SYN-0141-2025-012
2025-12-20
TRAINING_PARTICIPANT_SYNTHETIC
3 / 4 / 3 / 4 / 5 / 3 / 5
SAMPLE_ONLY; no actual respondent text
題項
CSV 欄位
簡短標籤（問卷／統計表）
凍結題目文字
Q1
Q1_need_fit
需求契合
本次訓練服務內容符合我在報名前表達的需求
Q2
Q2_content_applicability
情境對應
課程內容能對應我預計運用的工作志工或學習情境
Q3
Q3_instructor_support
師資支援
講師的說明示範與回應有助於我理解課程
Q4
Q4_materials_resources
教材資源
教材與學習資源容易取得並能支持我完成學習
Q5
Q5_admin_communication
行政溝通
報名課前通知與行政回覆清楚且及時
Q6
Q6_learning_environment
環境設備
學習場地或線上環境與設備適合本次服務
Q7
Q7_overall_satisfaction
整體滿意
整體而言我對本次訓練服務感到滿意
Q8
Q8_open_comment
開放回饋
本次最有幫助的是什麼下一次最希望改善什麼
欄位名稱
系統登記內容
登記代碼
REG-0141-20261025-01
對應指標與文件
TTQS 指標 19 / I19-E31 / 文件編號 0141
當前數據性質
SAMPLE_SYNTHETIC（合成教學範例數據）
真實資料狀態
REAL = UNKNOWN / HOLD；目前材料均為 SAMPLE，真實資料蒐集狀態 UNKNOWN。
示範資料集筆數
36 筆完整受訪紀錄（每年 12 筆，共 3 年）
36筆合成回覆 CSV SHA-256 檢查碼
723259199dd51973fc6473ec000234cc853fa1511be05864fdfd7b08bb452862（檔名 SAMPLE_SURVEY_RESPONSES_0141_R01.csv；SHA-256 為檔案檢查碼，不是數位簽章）
真實資料替換責任角色
由協會授權人員決定（尚未指派；不代表已有該職務或委任）
未來替換檢核條件
確認資料來源、授權、必要性與適用政策；以原始問卷與邀請紀錄核實分母；由授權人員核對去識別化與計算；獨立複核新檔 SHA-256。實際核准流程及簽署角色 UNKNOWN。
版本
修訂日期
修訂人員
變更摘要說明
審查核可狀態
R06-SYN
2026-10-25
OpenCode v2 依 R05 exact-SHA 獨立語意審查之五項 minor 與檔案雜湊措辭修正（非協會核定）
修正附錄二／附錄四題項標點正規化說明；§陸-I 欄名改為「Q1–Q6 六構面有效填答次數」；方案一移除無來源之抱怨條件並標示 UNKNOWN-sourced；執行摘要改用凍結短標籤；替換登記表改稱檔案版本／SHA-256／筆數清冊。R01 回覆列與摘要數字不變。
R06 候選；待 Word 全頁版面及本版 exact-SHA 獨立語意驗收；未獲正式接受
R05-SYN
2026-10-25
依 R04 exact-SHA 審查 minor 意見修訂；OpenCode CLI v2 原始文稿已回收，實際模型身分 UNKNOWN，並以凍結題目、原始 36 筆 CSV 與統計重算核對
完整 Q1–Q7 題目與標籤對照；明示 pooled index、單一合成客群及回溯示範／未執行方案；補單題 Top-2 分母與 CURRENT 授權審查閘；逐列事實 ID 明確為資料集基礎 ID 加 -YYYY-NNN；R01 數據不變
R05 候選；待 Word 全頁版面及本版 exact-SHA 獨立語意驗收
R04-SYN
2026-10-25
Codex 依 R03 exact-SHA 獨立審查之 minor findings 修訂（非協會核定）
將 ASCII 刻度示意改為同一 1–5 縱軸折線圖；統一 R01 合成事實識別碼；採 Blueprint pooled index 公式；修正官方 4 分級距措辭；新增明示 CONTINUE/CHANGE/HOLD 證據表；修正警示與句子。R01 CSV、36 筆分數與逐期摘要不變。
R04 候選；待 exact-SHA 語意與 Word 全頁驗收
R03-SYN
2026-10-25
Codex 依 exact-SHA 審查意見校正（非協會核定）
對齊 Q8 原始題文；將 Q7/Q5 相同 4.2500 標在同一量尺列；明示百分點以未四捨五入比例計算；移除公式孤立符號；說明 R03 正文沿用 R01 合成資料且不改分數。
R03 候選；待本版 exact-SHA 語意複核與 Word 版面驗收
R02-SYN
2026-10-25
Codex 文字校正（非協會核定）
修正 Q8 資料界線、未核定隱私/保存規則、虛構組織/職權、未支持的質性解釋、Top-2 百分點及 Q7 點數差；將圖與表單改為可讀表格。
歷史候選；OpenCode exact-SHA 語意 PASS（含已由 R03處理之次要發現），非現行驗收版
