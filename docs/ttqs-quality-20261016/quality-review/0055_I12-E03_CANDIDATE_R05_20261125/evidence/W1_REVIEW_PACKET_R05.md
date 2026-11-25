# Bounded independent semantic review
work_id=TTQS_ONE_0055_I12-E03_W1_SEMANTIC_REVIEW_R05_EXACT_SHA_20261125
doc_id=0055
requirement_id=I12-E03
candidate_revision=R05
candidate_status=CANDIDATE_ONLY
candidate_docx_path=E:\TTQS\TTQS_ONE_CODEX_RUNTIME\EXTERNAL_WORK\TTQS_ONE_0055_I12-E03_R04_EXACT_SHA_SEMANTIC_W2_20261125_DOT\R05_SCOPED_CANDIDATE_VERIFIED_BUILD\0055_I12-E03_R05_CANDIDATE.docx
candidate_docx_bytes=54652
candidate_docx_sha256=b30cebc0e5a7df10095d4a20271109e2e3e2eab278938e6ff1a1cfb764e9b6f1
body_extraction_method=OpenXML word/document.xml text and table cells, read-only
body_extract_sha256=48b68238315617c30239a8d11c22f36827322e5cdc89d44cc1471f16f6ef17c9
PR92_live_head_at_dispatch=165cf3b7de54b647a5f42dc79f9df5d1d8e03d9a
remote_readback_for_this_candidate=NOT_YET_PUBLISHED; do not claim GitHub delivery
role=independent semantic/usability/title-blind reviewer; no file, CLI, shell, network, or GitHub actions
prior_wrong-route_attempt=gemini-4-hydrogen-high on R04 was rejected and is not evidence for R05
R05 technical QA exact SHA:
{
  "project_id": "TTQS_ONE",
  "doc_id": "0055",
  "revision": "R05",
  "candidate_sha256": "b30cebc0e5a7df10095d4a20271109e2e3e2eab278938e6ff1a1cfb764e9b6f1",
  "technical_status": "PASS_SCOPED_TECHNICAL_EXACT_SHA",
  "observed_at": "2026-11-25T10:07:32.934250+08:00",
  "check": [
    "zip CRC and XML parse",
    "single changed DOCX member and three text edits; all structure, layout settings, styles and font specifications unchanged",
    "52 unique records and two authorized row changes",
    "read-only Word native open, PDF export and 11 images"
  ],
  "formal_acceptance": "NOT_GRANTED"
}
R05 visual QA exact SHA:
{
  "project_id": "TTQS_ONE",
  "doc_id": "0055",
  "revision": "R05",
  "candidate_sha256": "b30cebc0e5a7df10095d4a20271109e2e3e2eab278938e6ff1a1cfb764e9b6f1",
  "pdf_sha256": "130be0b8a1c895d5d72a0b86affe944933a6c31310ab952ba988f9f4abb92e2b",
  "word_native_page_count": 11,
  "pages_same_sha_as_previously_reviewed_word_render": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    9,
    10,
    11
  ],
  "pages_directly_inspected": [
    8
  ],
  "visual_status": "PASS_FULL_PAGE_EXACT_SHA",
  "inspection_note": "All 11 final Word pages rasterized. Ten have identical PNG bytes to previously inspected R04 pages. Final page 8 directly inspected: three edited rows and footer fully readable, no cut text, overlap, page spill, missing glyph, or unexpected whitespace.",
  "observed_at": "2026-11-25T10:03:48.192067+08:00",
  "formal_acceptance": "NOT_GRANTED"
}
R05 body exact-screen receipt:
{
  "doc_id": "0055",
  "candidate_sha256": "b30cebc0e5a7df10095d4a20271109e2e3e2eab278938e6ff1a1cfb764e9b6f1",
  "peer_results": [],
  "method": "Exact normalized substantive paragraphs and multirow tables; title/front matter excluded. Does not claim paraphrase detection.",
  "status": "REVIEW_REQUIRED"
}
R05 remote neighbor check pinned to older HEAD f36b0b16feb5b8718d141c4410cee1e025b8dacd; historical evidence only, not current live readback:
{
  "candidate_sha256": "b30cebc0e5a7df10095d4a20271109e2e3e2eab278938e6ff1a1cfb764e9b6f1",
  "verified_head": "f36b0b16feb5b8718d141c4410cee1e025b8dacd",
  "checks": [
    {
      "doc_id": "0053",
      "revision": "R03",
      "git_blob_sha1": "0187ef01337a3f9829bc9bdd3881a63d6021dedb",
      "sha256": "cc75583238dba42eede61de990992770f8de75e96d1bcfe1313e57629551f8e8",
      "exact_overlaps": [],
      "near_overlaps": [],
      "bytes": 68614,
      "remote": "https://raw.githubusercontent.com/PT-Original-Point/ttqs-one/f36b0b16feb5b8718d141c4410cee1e025b8dacd/docs/ttqs-quality-20261016/quality-review/0053_R03/candidate/0053_R03.docx"
    },
    {
      "doc_id": "0054",
      "revision": "R14",
      "git_blob_sha1": "24ef96aa1e86783571ca8bde645b353d25a86c65",
      "sha256": "3d000e580b9cb1247fd984ebb0c8f5f817fce08ce7c368cc1799c95a111a979c",
      "exact_overlaps": [],
      "near_overlaps": [],
      "bytes": 49230,
      "remote": "https://raw.githubusercontent.com/PT-Original-Point/ttqs-one/f36b0b16feb5b8718d141c4410cee1e025b8dacd/docs/ttqs-quality-20261016/quality-review/0054_R14/candidate/0054_R14.docx"
    },
    {
      "doc_id": "0056",
      "revision": "R05",
      "git_blob_sha1": "b2dab74823d6133764241082f2ab5faf701e6a9b",
      "sha256": "a8ac2f2487bd40ff00784980bbe2ef9a84c0cfe326c9b37e6dceaeebc3e750cf",
      "exact_overlaps": [],
      "near_overlaps": [],
      "bytes": 60746,
      "remote": "https://raw.githubusercontent.com/PT-Original-Point/ttqs-one/f36b0b16feb5b8718d141c4410cee1e025b8dacd/docs/ttqs-quality-20261016/quality-review/0056_R01/0056_R05.docx"
    }
  ],
  "method": "Verified Git blob bytes. Excludes title and front matter. Exact normalized substantive paragraph/table and character five-gram Jaccard >= 0.72. Conceptual genre differences supported separately by W2.",
  "status": "NO_FLAG"
}
source_map_sha256=4dc7807d921848e3b47f5d1d28eb06e99124fdb32ef0c26286fc6ca4348b37c4
unique_blueprint_sha256=e255a2397b47868e3c0a740320bda0bd022b9e540f7adeb7211f66d32840c45b
synthetic_register_sha256=e30fade6b37604140d051d65d6152deb8d56c9e95a6ef5ee72b31354e75228da
## Source map
# Source map for DOCX 0055 R02

## Control versions

- GitHub repository: `PT-Original-Point/ttqs-one`
- Branch: `work/ttqs-one-document-quality-contract-20261016`
- PR #92 live branch head: `fdfd3b4dbd7c8cc52dd0e315406294bab83f1093`
- Formal mission candidate: `docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md`.
- Mission Git blob: `538bedb9d87e8465f43151933b4a5c1bfa4bbc4e`; body text minimum 10.5 pt, table text minimum 9.5 pt, and no generic first-look tables.
- Indicator-specific writing manual: `02_GENRE_WRITING_MANUAL.md`, current Git blob `4ff863d9f534b6359fc1c7c1685bd8cce02da886`.
- 157-checkbox blueprint direction: `03_157_CHECKBOX_BLUEPRINTS.md`, current Git blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`.
- External continuation audit: `docs/ttqs-quality-20261016/06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md`, Git blob `263aaca84891bba8dca087875804343c3670e921`.
- Official checklist PDF copy: `inputs/official_checklist_source.pdf`, 303,044 bytes, SHA-256 `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`, Git blob `9c7621decdad585b743bf2b3d949ee5518b7bee0`; page 4, indicator 12c.
- Page image used for visual text cross-check: `inputs/official_evidence_table_page4.png`.

## Requirement alignment

DOCX 0055 = Unique Blueprint I12-E03 = official sequence 058. The source PDF page 4 states that instructor recruitment must follow selection standards and process, receive training management committee approval, then receive an appointment letter. The 157-grid row 058 specifically calls for scoring rubric, teaching demonstration, authorization checks and retrieval of the original appointment letter. The writing manual’s indicator 10 asks for instructor standards and weights, comparison of at least three candidates, conflict-of-interest handling and a complete SAMPLE selection record; indicator 12 requires instructor fit to objectives, standards, weights, demonstration, review, authority and a real appointment original.

## Same-case facts

The synthetic teaching case is `SYN-0033-PLAN-01`, course `志工服務紀錄、交接與工作界線實務`, 360 minutes across 90+90+120+60-minute units. These are copied only from the existing synthetic chain in 0033 R03, 0049 R01, 0050 R01 and 0052 R02. Their candidate SHA-256 values are listed in `UNIQUE_BLUEPRINT_0055_R02.md`. The new instructor comparison, simulated decision and appointment specimen are newly created synthetic extensions and do not assert that any course was delivered or any candidate was real.

## Authorization and real-data limits

The current association’s governing authority, committee constitution, delegated approval levels, actual candidates, credentials, teaching activity, appointment, fee authorization and signatures were not found in the public sample chain. Each remains UNKNOWN and must be replaced by a source-backed REAL record before real use. No committee authority or original credential is invented here.

## Unique Blueprint
# Unique Blueprint for DOCX 0055 R02

## Identity and official purpose

- Project: TTQS_ONE
- DOCX ID: 0055
- Unique requirement: I12-E03
- Official evidence-table location: page 4, indicator 12c
- Official 157-checkbox sequence: 058. DOCX ID 0055 and checkbox 058 are different identifiers.
- Required genre: instructor selection and appointment evidence package, containing the selection rule, completed comparative review, teaching demonstration, qualification and authority checks, authorized committee decision record, and appointment-letter specimen.
- Official requirement text: “講師的遴聘依師資遴選標準及流程評選並經訓練管理委員會通過後發給聘書。”

## Unique purpose and adjacent-item boundaries

This file shows how a training organization can select an instructor against course objectives, compare at least three candidates using a disclosed weighted rubric, record a teaching demonstration and conflicts, verify the authority and qualifications required for the role, submit the recommendation to an actually authorized training management committee, and issue an appointment letter only after the required decision. The example is fully SAMPLE/SYNTHETIC. It does not claim that the Original Point Association has a currently constituted committee, has selected or verified a real instructor, has approved an appointment, or has issued a letter.

- DOCX 0053 / I12-E01 / checkbox 056 concerns evaluation of learner, material, instructor, method, environment and equipment fit, then adjustment. It is not the instructor selection record.
- DOCX 0054 / I12-E02 / checkbox 057 concerns learner selection and material review. It is not the instructor selection record.
- DOCX 0055 / I12-E03 / checkbox 058 concerns instructor selection and appointment. It must include a comparative selection process and appointment-letter handling.
- DOCX 0059 / I12-E05 / checkbox 059 concerns equipment inspection and venue insurance. A lecturer qualification or appointment letter cannot satisfy it.
- DOCX 0050 / I11-E02 provides unit objectives and assessment examples; it is not evidence that this sample instructor has actually taught.

## Cross-document sample case

Use the existing SAMPLE/SYNTHETIC case identifier `SYN-0033-PLAN-01` and the exact course title `志工服務紀錄、交接與工作界線實務`. The linked planning package defines 360 teaching minutes across four units of 90, 90, 120 and 60 minutes. These facts are carried over as sample planning facts only. This Blueprint adds a synthetic instructor-selection scenario and a proposed staffing assignment; it does not change the course plan or imply delivery. The example assigns one selected instructor to the 360 planned teaching minutes solely to make the appointment specimen complete. A real course plan must be updated and reauthorized if actual staffing differs.

Exact source candidates to read as same-case context:

- DOCX 0033 R03 / I07-E01 / checkbox 033 / SHA-256 `fe5f3cfd84c761da86435a71e0fd899daa725be78628c4d2d3f2324c1fdb5f4f`.
- DOCX 0049 R01 / I11-E01 / checkbox 051 / SHA-256 `e8212788b1f7b201ca4af4f4c5fb83ab131627dbfa815987f7cf6344edfda727`.
- DOCX 0050 R01 / I11-E02 / checkbox 052 / SHA-256 `d0d37c2c69b161a2cdd37ee3097306722c4a65a1afd844ae92e1dff58b43381a`.
- DOCX 0052 R02 / I11-E04 / checkbox 054 / SHA-256 `9129aff2bb730d31f76a5cb457ed069f1cafd2460b4069219f697b35d2c11afa`.

## Document-specific content architecture

1. First-page purpose, intended users, official locator, case identity, SAMPLE boundary and a document-specific workflow table without a generic first-look summary.
2. Official requirement crosswalk and explicit separation from DOCX 0053, 0054, 0050 and 0059.
3. Synthetic course need and observable instructor competencies linked to the existing 360-minute case plan.
4. Decision authority, role allocation, minimum authorization evidence and HOLD gates.
5. Weighted rubric with observable anchors, numeric thresholds, non-compensable gates and reject/HOLD conditions.
6. Candidate intake, qualification and authorization checks, conflict declarations and privacy controls.
7. Same-condition teaching demonstration plan and observation evidence.
8. Three-candidate, three-reviewer completed scorecards, formulas, independently recalculable totals, ranking and evidence-based rationale.
9. Conflict response and recommendation rules with disclosure, recusal and record fields.
10. Fully marked simulated committee agenda and decision record, quorum/authority checks, dissent/recusal, owner and deadline.
11. Complete SAMPLE appointment-letter specimen and issue/acceptance sequence, marked NOT ISSUED and NOT VALID.
12. Future post-course follow-up design, explicitly not represented as delivered or evaluated.
13. A 52-row REAL replacement register and ordered evidence chain with source, responsible verifier and HOLD rule for every synthetic datum.
14. Revision/status controls that distinguish this candidate, independent review and formal Human acceptance.

The visible section sequence in R02 is: §1 requirement boundary; §2 case need; §3 authority; §4 rubric; §5 candidate checks; §6 demonstration; §7 score comparison; §8 conflicts; §9 committee; §10 appointment; §11 future follow-up; §12 replacement register; §13 version control. The cover workflow points to these exact sections.

## Synthetic scoring design

Criterion weights total 100: subject accuracy 25; teaching demonstration 25; fit for adult volunteer learners and accessibility 20; practical application and transfer 20; privacy, role and safety boundaries 10. Three synthetic reviewers each score 0-100. Criterion panel mean is the arithmetic mean of the three scores. Weighted points equal panel mean multiplied by weight divided by 100. Total score equals the sum of five weighted-point values.

Sample candidate score vectors by criterion, in the order above:

- C-01: reviewer scores `(85,86,87)`, `(80,83,83)`, `(78,76,80)`, `(82,80,78)`, `(90,92,88)`; means `86,82,78,80,90`; weighted points `21.5,20.5,15.6,16.0,9.0`; total `82.6`.
- C-02: `(76,78,80)`, `(90,86,88)`, `(74,76,75)`, `(78,80,82)`, `(84,86,85)`; means `78,88,75,80,85`; weighted points `19.5,22.0,15.0,16.0,8.5`; total `81.0`.
- C-03: `(90,92,88)`, `(84,86,88)`, `(88,90,86)`, `(84,86,85)`, `(92,90,88)`; means `90,86,88,85,90`; weighted points `22.5,21.5,17.6,17.0,9.0`; total `87.6`.

Illustrative pass rule: total at least 80; subject accuracy, teaching demonstration, and learner fit each at least 75; safety/boundary score at least 80; no unresolved conflict; and all qualification/authorization checks recorded. A missing original, unverified qualification, unauthorized committee, undisclosed conflict, or failed safety gate overrides any numeric score and results in HOLD or REJECT. Tie-break: higher subject-accuracy weighted points, then teaching-demonstration weighted points, then a documented second demonstration.

## Non-negotiable evidence boundary

All candidate codes, scores, raters, dates, committee discussion, credentials-check outcomes, appointment terms and signatures shown in the DOCX are SAMPLE/SYNTHETIC. No fabricated certificate, external reference, real approval, actual committee, actual appointment, signature or course-delivery record may be represented. The specimen letter is marked NOT ISSUED and NOT VALID. The public replacement register must identify each synthetic datum, its real source to obtain, the person who must verify it, and the hold condition.

## Replacement register
register_id,fact_id,case_id,doc_id,docx_locator,synthetic_value_or_field,assumption_rationale,cross_doc_reference,real_source_to_obtain,responsible_verifier,evidence_status,hold_condition
FAC-0055-001,FAC-0055-001,SYN-0033-PLAN-01,0055,封面案例行「案例 SYN-0033-PLAN-01」；第 13 節一致性核對列,合成案例識別碼,沿用既有四份同案例文件的合成案例碼，僅作跨文件對齊,0033 R03／0049 R01／0050 R01／0052 R02（同一合成案例）,正式課程計畫與核准版次,課程承辦,SYNTHETIC,未取得正式計畫不得沿用此 ID
FAC-0055-002,FAC-0055-002,SYN-0033-PLAN-01,0055,封面案例行；第 10 節聘書表「課程與工作範圍」列,合成課程名稱,沿用同案例課程名稱，供招募與聘書草案一致,0033 R03／0049 R01／0050 R01／0052 R02（同一合成案例）,正式課程計畫,課程承辦,SYNTHETIC,名稱或範圍不一致即 HOLD
FAC-0055-003,FAC-0055-003,SYN-0033-PLAN-01,0055,封面案例行「合成規劃 360 分鐘」；第 10 節聘書表「課程與工作範圍」列,合成總時數 360 分鐘,沿用同案例 360 分鐘，使聘任範圍完整,0033 R03／0049 R01／0050 R01／0052 R02（同一合成案例）,核定課程計畫及時程,課程承辦,SYNTHETIC,未核定時數不得寫入聘書
FAC-0055-004,FAC-0055-004,SYN-0033-PLAN-01,0055,封面案例行「（90+90+120+60）」；第 13 節一致性核對列,合成單元時數 90+90+120+60,沿用同案例四單元時數，證明 90+90+120+60=360,0033 R03／0049 R01／0050 R01／0052 R02（同一合成案例）,核定課程計畫各單元頁,課程設計者,SYNTHETIC,總和不等於 360 即 HOLD
FAC-0055-005,FAC-0055-005,SYN-0033-PLAN-01,0055,第 2 節需求表「志工紀錄欄位易漏、事實與推測混寫」列,合成需求缺口：紀錄欄位漏填,自同案例需求轉寫為可觀察的講師職能落差,0033 R03 需求調查；0049 R01 計畫,需求調查原表及彙整方法,需求提出人,SYNTHETIC,無可追溯需求來源則重做需求分析
FAC-0055-006,FAC-0055-006,SYN-0033-PLAN-01,0055,第 2 節需求表「志工紀錄欄位易漏、事實與推測混寫」列,合成需求缺口：事實與推測混寫,同上，用於設計事實／推測辨識的試教情境,0033 R03 需求調查；0049 R01 計畫,去識別化需求案例及分析,需求提出人,SYNTHETIC,不得把虛構案例標為真實個案
FAC-0055-007,FAC-0055-007,SYN-0033-PLAN-01,0055,第 2 節需求表「交接時責任、期限、未結事項不清」列,合成需求缺口：交接責任與期限不清,自同案例交接需求轉寫，供試教評分情境,0033 R03 需求調查；0049 R01 計畫,需求訪談／工作流程紀錄,需求提出人,SYNTHETIC,缺原始資料則標 UNKNOWN
FAC-0055-008,FAC-0055-008,SYN-0033-PLAN-01,0055,第 2 節需求表「志工容易越過角色界線或傳遞敏感資訊」列,合成需求缺口：角色界線與敏感資訊,自同案例角色界線需求轉寫，支撐安全面向量尺,0033 R03 需求調查；0049 R01 計畫,正式服務規範與匿名化需求資料,治理責任人,SYNTHETIC,未核准規範不得當協會政策
FAC-0055-009,FAC-0055-009,SYN-0033-PLAN-01,0055,第 2 節需求表「成人學員背景差異大、部分以手機參與」列,合成需求缺口：成人學員可近性,示範成人學員可近性面向，非真實學員資料,0033 R03 需求調查；0049 R01 計畫,學員需求／合理調整紀錄,課程承辦,SYNTHETIC,未確認需求不得宣稱已滿足
FAC-0055-010,FAC-0055-010,SYN-0033-PLAN-01,0055,第 4 節量尺表「權重」欄；第 7 節排序核對與同分處理。,合成評選權重 25/25/20/20/10；同分處理（未核定 SAMPLE／SYNTHETIC 提案）：加權總分相同時，先比較『專業內容正確性』加權點數，再比較『教學示範與引導』加權點數；仍同分時，安排相同題目、準備時間、時長及量尺的第二次試教，記錄評審觀察與分數；仍同分或無法核實具權限者與已核定之後續規則，即 HOLD，依真實章程與授權處理。,示範事前公告、可重算的遴選與同分處理程序；非協會已核定採用之政策。,無（本件新增合成，無跨文件事實引用）,權責治理單位與正式核定之遴選辦法，以及（如使用）第二次試教評分表。,權限經核實後之具權限者／權責單位。,SYNTHETIC,權限與同分規則核定前不得正式使用；已觸發但缺證據或權限即 HOLD。
FAC-0055-011,FAC-0055-011,SYN-0033-PLAN-01,0055,第 4 節狀態表「通過門檻（合成示例）」列,合成遴選門檻總分 80,設定示例總分門檻，使推薦有明確判準,無（本件新增合成，無跨文件事實引用）,正式核定遴選辦法,權責主管／委員會,SYNTHETIC,門檻未授權不得宣稱合格
FAC-0055-012,FAC-0055-012,SYN-0033-PLAN-01,0055,第 4 節狀態表「通過門檻（合成示例）」列,合成個別面向最低分 75,設定示例面向門檻，避免單項高分掩蓋弱項,無（本件新增合成，無跨文件事實引用）,正式核定量尺,權責主管／委員會,SYNTHETIC,不可事後為候選人改門檻
FAC-0055-013,FAC-0055-013,SYN-0033-PLAN-01,0055,第 4 節狀態表「通過門檻（合成示例）」列,合成安全界線最低分 80,設定示例安全門檻，配合非補償性條件,無（本件新增合成，無跨文件事實引用）,正式核定量尺及風險規則,權責主管／委員會,SYNTHETIC,安全低於門檻即 HOLD/REJECT
FAC-0055-014,FAC-0055-014,SYN-0033-PLAN-01,0055,第 3 節角色表「評審甲／乙／丙」列；第 7 節分解表「評審甲／乙／丙」欄,虛構評審代碼 評審甲／乙／丙,用角色代碼代替真實評審姓名,無（本件新增合成，無跨文件事實引用）,真實委任／評審名單與簽到,遴選承辦,SYNTHETIC,未確認身份不得把代碼當實際評審
FAC-0055-015,FAC-0055-015,SYN-0033-PLAN-01,0055,第 5 節候選核驗表「C-01（合成）」欄,虛構候選代碼 C-01；SAMPLE 履歷索引 S-C01（僅示例索引，本包未附履歷或資格文件）,用候選代碼代替真實候選人，避免識別,無（本件新增合成，無跨文件事實引用）,候選人正式申請與同意,遴選承辦,SYNTHETIC,無本人申請與同意即不得列名
FAC-0055-016,FAC-0055-016,SYN-0033-PLAN-01,0055,第 5 節候選核驗表「C-02（合成）」欄,虛構候選代碼 C-02；SAMPLE 履歷索引 S-C02（僅示例索引，本包未附履歷或資格文件）,用候選代碼代替真實候選人，避免識別,無（本件新增合成，無跨文件事實引用）,候選人正式申請與同意,遴選承辦,SYNTHETIC,無本人申請與同意即不得列名
FAC-0055-017,FAC-0055-017,SYN-0033-PLAN-01,0055,第 5 節候選核驗表「C-03（合成）」欄,虛構候選代碼 C-03；SAMPLE 履歷索引 S-C03（僅示例索引，本包未附履歷或資格文件）,用候選代碼代替真實候選人，避免識別,無（本件新增合成，無跨文件事實引用）,候選人正式申請與同意,遴選承辦,SYNTHETIC,無本人申請與同意即不得列名
FAC-0055-018,FAC-0055-018,SYN-0033-PLAN-01,0055,第 7 節「C-01｜候選評分分解（SAMPLE）」表「專業內容正確性」列,C-01 專業內容正確性評分 85/86/87,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及試教紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-019,FAC-0055-019,SYN-0033-PLAN-01,0055,第 7 節「C-01｜候選評分分解（SAMPLE）」表「教學示範與引導」列,C-01 教學示範與引導評分 80/83/83,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及試教紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-020,FAC-0055-020,SYN-0033-PLAN-01,0055,第 7 節「C-01｜候選評分分解（SAMPLE）」表「成人志工適配與可近性」列,C-01 成人志工適配與可近性評分 78/76/80,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及可近性觀察,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-021,FAC-0055-021,SYN-0033-PLAN-01,0055,第 7 節「C-01｜候選評分分解（SAMPLE）」表「實務應用與移轉」列,C-01 實務應用與移轉評分 82/80/78,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分與演練紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-022,FAC-0055-022,SYN-0033-PLAN-01,0055,第 7 節「C-01｜候選評分分解（SAMPLE）」表「個資、角色與安全界線」列,C-01 個資、角色與安全界線評分 90/92/88,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分及風險情境答覆,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-023,FAC-0055-023,SYN-0033-PLAN-01,0055,第 7 節「C-02｜候選評分分解（SAMPLE）」表「專業內容正確性」列,C-02 專業內容正確性評分 76/78/80,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及試教紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-024,FAC-0055-024,SYN-0033-PLAN-01,0055,第 7 節「C-02｜候選評分分解（SAMPLE）」表「教學示範與引導」列,C-02 教學示範與引導評分 90/86/88,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及試教紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-025,FAC-0055-025,SYN-0033-PLAN-01,0055,第 7 節「C-02｜候選評分分解（SAMPLE）」表「成人志工適配與可近性」列,C-02 成人志工適配與可近性評分 74/76/75,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及可近性觀察,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-026,FAC-0055-026,SYN-0033-PLAN-01,0055,第 7 節「C-02｜候選評分分解（SAMPLE）」表「實務應用與移轉」列,C-02 實務應用與移轉評分 78/80/82,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分與演練紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-027,FAC-0055-027,SYN-0033-PLAN-01,0055,第 7 節「C-02｜候選評分分解（SAMPLE）」表「個資、角色與安全界線」列,C-02 個資、角色與安全界線評分 84/86/85,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分及風險情境答覆,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-028,FAC-0055-028,SYN-0033-PLAN-01,0055,第 7 節「C-03｜候選評分分解（SAMPLE）」表「專業內容正確性」列,C-03 專業內容正確性評分 90/92/88,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及試教紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-029,FAC-0055-029,SYN-0033-PLAN-01,0055,第 7 節「C-03｜候選評分分解（SAMPLE）」表「教學示範與引導」列,C-03 教學示範與引導評分 84/86/88,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及試教紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-030,FAC-0055-030,SYN-0033-PLAN-01,0055,第 7 節「C-03｜候選評分分解（SAMPLE）」表「成人志工適配與可近性」列,C-03 成人志工適配與可近性評分 88/90/86,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分表及可近性觀察,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-031,FAC-0055-031,SYN-0033-PLAN-01,0055,第 7 節「C-03｜候選評分分解（SAMPLE）」表「實務應用與移轉」列,C-03 實務應用與移轉評分 84/86/85,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分與演練紀錄,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-032,FAC-0055-032,SYN-0033-PLAN-01,0055,第 7 節「C-03｜候選評分分解（SAMPLE）」表「個資、角色與安全界線」列,C-03 個資、角色與安全界線評分 92/90/88,以合成評分向量示範可重算平均與加權,無（本件新增合成，無跨文件事實引用）,三份原始評分及風險情境答覆,各評審,SYNTHETIC,無原始分數不得保留平均
FAC-0055-033,FAC-0055-033,SYN-0033-PLAN-01,0055,第 5 節候選核驗表「利益衝突」列；第 8 節說明,合成評審無衝突申報,示範衝突申報欄位填寫，非真實申報結果,無（本件新增合成，無跨文件事實引用）,各評審本人簽署申報與處理決定,評審／遴選承辦,SYNTHETIC,空白或未申報即 HOLD
FAC-0055-034,FAC-0055-034,SYN-0033-PLAN-01,0055,第 5 節候選核驗表「專業資格」列,合成資格查核 PASS 標記,示範資格核驗欄位值，無任何真實證照,無（本件新增合成，無跨文件事實引用）,資格原件及發證單位查驗紀錄,遴選承辦,SYNTHETIC／REAL 未知,無原件和獨立查驗即 HOLD
FAC-0055-035,FAC-0055-035,SYN-0033-PLAN-01,0055,第 5 節候選核驗表「教學授權／可用時段」列,合成候選人可授課時段,示範可用時段欄位，非真實承諾,無（本件新增合成，無跨文件事實引用）,候選人書面同意與核定時程,課程承辦,SYNTHETIC,未確認時段不得承諾
FAC-0055-036,FAC-0055-036,SYN-0033-PLAN-01,0055,第 5 節候選核驗表「個資及作品使用」列,合成限本次遴選的資料同意,示範個資授權欄位，非真實同意書,無（本件新增合成，無跨文件事實引用）,本人告知、同意與撤回紀錄,資料管理責任人,SYNTHETIC,無合法依據不得保存或公開
FAC-0055-037,FAC-0055-037,SYN-0033-PLAN-01,0055,封面 SAMPLE 說明框；第 9 節「完全合成的會議情境」說明框,模擬委員會存在與權限（明示為假設）,明示委員會權限為假設，避免假稱已成立,無（本件新增合成，無跨文件事實引用）,章程、設置文件、任期及授權原件,治理責任人,SYNTHETIC／REAL 未知,權限 UNKNOWN 即不得正式開會決議
FAC-0055-038,FAC-0055-038,SYN-0033-PLAN-01,0055,第 9 節議程表「出席及法定人數」列,合成：應到 3 人、出席門檻 2 人、實到 3 人；P-01 與 S-01 不表決。,示範法定人數記錄格式，非真實簽到,無（本件新增合成，無跨文件事實引用）,真實通知、簽到及法定人數規則,委員會紀錄員,SYNTHETIC／REAL 未知,無原始簽到／法定人數來源即 HOLD
FAC-0055-039,FAC-0055-039,SYN-0033-PLAN-01,0055,第 9 節議程表「會議基本資料」列,模擬會議日期 2026-11-10,用未來合成日期示範會議基本資料欄位,無（本件新增合成，無跨文件事實引用）,實際會議通知、簽到與議事錄,委員會紀錄員,SYNTHETIC／REAL 未知,不可倒填或沿用示範日期
FAC-0055-040,FAC-0055-040,SYN-0033-PLAN-01,0055,第 9 節議程表「合成決議」列；第 7 節排序表；第 9 節「反對／迴避／附件」列,合成：3 名表決委員，通過門檻 2 票、贊成 3 票；反對 0、棄權 0、迴避 0，附條件推薦 C-03。,示範附條件的模擬決議，非真實核准,無（本件新增合成，無跨文件事實引用）,有權委員會逐項決議及表決紀錄,委員會主席／紀錄員,SYNTHETIC／REAL 未知,無有效決議不得稱已核准
FAC-0055-041,FAC-0055-041,SYN-0033-PLAN-01,0055,第 9 節議程表「責任與期限」列,虛構責任人代碼 A-01,用代碼示範責任人欄位，非真實指派,無（本件新增合成，無跨文件事實引用）,實際分工授權與責任確認,課程主管,SYNTHETIC／REAL 未知,未指派不得假填責任完成
FAC-0055-042,FAC-0055-042,SYN-0033-PLAN-01,0055,第 9 節議程表「責任與期限」列,虛構期限 2026-11-17,示範追蹤期限欄位，非真實決議期限,無（本件新增合成，無跨文件事實引用）,實際會議決議及追蹤紀錄,委員會紀錄員,SYNTHETIC／REAL 未知,不可冒用或倒填期限
FAC-0055-043,FAC-0055-043,SYN-0033-PLAN-01,0055,第 10 節聘書表「受聘人／編號」列,虛構聘書草稿編號 SAMPLE-APPT-001,示範聘書編號欄位，非正式發文編號,無（本件新增合成，無跨文件事實引用）,正式文件編碼台帳,文件管制人,SYNTHETIC／REAL 未知,未核准不得登錄為正式發文
FAC-0055-044,FAC-0055-044,SYN-0033-PLAN-01,0055,第 10 節聘書表「日期與地點」列,虛構聘書日期 2026-12-05,用未來合成日期示範聘書日期欄位,無（本件新增合成，無跨文件事實引用）,正式決議、實際發文與送達證明,授權簽發人,SYNTHETIC／REAL 未知,不可預簽、倒填或提前發出
FAC-0055-045,FAC-0055-045,SYN-0033-PLAN-01,0055,第 10 節聘書表「費用條件」列,"合成酬金 NT$4,800",示範酬金欄位與計算，明示未經核准,無（本件新增合成，無跨文件事實引用）,核准預算、契約、稅務及支付依據,財務／授權主管,SYNTHETIC／REAL 未知,無核准預算與授權不得承諾或支付
FAC-0055-046,FAC-0055-046,SYN-0033-PLAN-01,0055,第 10 節聘書表「費用條件」列,合成費率 NT$800／小時,示範費率欄位，由 360 分鐘×800 得 4800,無（本件新增合成，無跨文件事實引用）,核准費率表／契約,財務／授權主管,SYNTHETIC／REAL 未知,不得將示例數字當協會標準
FAC-0055-047,FAC-0055-047,SYN-0033-PLAN-01,0055,第 10 節聘書表「履約條件」列,示範教材授權範圍,示範教材授權條款，真實範圍以待契約,無（本件新增合成，無跨文件事實引用）,真實授權契約與教材權利來源,課程承辦／權責主管,SYNTHETIC,未授權不得重製或公開
FAC-0055-048,FAC-0055-048,SYN-0033-PLAN-01,0055,第 8 節衝突處理表「候選人資料涉及不必要個資」列；第 10 節聘書表「取消／變更」列,未指定的資料保存期限,示範保存期限欄位，真實規則未知,無（本件新增合成，無跨文件事實引用）,現行保存規則及核定表單,資料管理責任人,SYNTHETIC／REAL 未知,規則未知時限制存取且不得任意銷毀
FAC-0055-049,FAC-0055-049,SYN-0033-PLAN-01,0055,第 10 節聘書表「取消／變更」列,示範取消與變更條件,示範變更條件條款，非真實契約,無（本件新增合成，無跨文件事實引用）,雙方有效契約及核准變更紀錄,契約承辦,SYNTHETIC,無授權條款不得主張已同意
FAC-0055-050,FAC-0055-050,SYN-0033-PLAN-01,0055,第 11 節追蹤表「課中」列,實際授課完成（未發生／UNKNOWN）,明示課程尚未發生，避免假造成果,0033 R03／0049 R01／0050 R01／0052 R02（同一課程鏈）,出席、課程紀錄、講師回報及成果,課程承辦,SYNTHETIC／REAL 未知,未發生前不得填成果或評語
FAC-0055-051,FAC-0055-051,SYN-0033-PLAN-01,0055,第 11 節追蹤表「課後 5 個工作日（示例時限）」列,課後回饋與效能評估（待未來資料）,示範課後回饋工具，非真實回收資料,0033 R03／0049 R01／0050 R01／0052 R02（同一課程鏈）,匿名回饋、作業、評估工具與判讀紀錄,評估責任人,SYNTHETIC／REAL 未知,無資料時結論 UNKNOWN
FAC-0055-052,FAC-0055-052,SYN-0033-PLAN-01,0055,第 11 節追蹤表「下次遴選前」列,改進／續聘／停聘決定（待未來有權決定）,示範改善／續聘判讀欄位，非真實決定,0033 R03／0049 R01／0050 R01／0052 R02（同一課程鏈）,課後證據、改善追蹤及正式核准,有權委員會／主管,SYNTHETIC／REAL 未知,不得預先宣稱續聘或成效

## Candidate body extracted from the exact DOCX SHA above
講師遴選與聘任流程範例
從課程需求、評選量尺、同條件試教、三人比較，到委員會決定與聘書處理的完整示範
| SAMPLE / SYNTHETIC｜未核准、未發聘、不可作為真實任命證明｜本範例所有人選代碼、分數、評審、資格核驗狀態、會議、決議、日期、費用及聘書文字均為合成示範。原始點協會目前是否設有有效訓練管理委員會、其權限、真實講師與資格、真實核准及聘任均為 UNKNOWN。 |

本範例供課程需求提出人、遴選承辦人、評審及具有效授權的決策者使用，說明如何為一門特定課程訂出講師能力需求、以一致且可重算的量尺比較候選人、記錄試教與利益衝突、核對資格與授權，並在取得有權決定後才處理聘書；正文依下方作業順序所標示的章節閱讀。
案例 SYN-0033-PLAN-01｜志工服務紀錄、交接與工作界線實務，合成規劃 360 分鐘（90+90+120+60）；沿用既有合成規劃資料，不表示課程已開辦。
| 遴選作業順序與正文位置 \| 形成資料與放行條件 |
| 建立需求與核對權限（第 2–3 節） \| 先確認課程職能缺口與決策授權；委員會、評審或簽發權任何一項缺少來源即 HOLD。 |
| 設定量尺並查核候選人（第 4–5、8 節） \| 使用同一版標準；完成資格、授權與利益衝突檢查，缺原件或未揭露即 HOLD。 |
| 安排同條件試教並比較（第 6–7 節） \| 保存觀察依據、三人評分、可重算總分及排序；示例分數只作推薦參考，不等於錄用。 |
| 有權決議後處理聘書（第 9–10 節），再依第 12 節逐筆替換 SAMPLE \| 先核對有效權限、出席、表決與附件；正式決議、簽發與接受未完成前，不得把聘書當作已發出。 |

官方來源定位：訓練品質評核表第 4 頁指標 12c（需求代碼 I12-E03；官方方框 058）：「講師的遴聘依師資遴選標準及流程評選並經訓練管理委員會通過後發給聘書。」
1｜需求、用途與相鄰需求界線
這份文件要回答：為這一門特定課程，需要什麼講師能力？如何用一致、可重算的標準比較候選人？哪個機關有權決定？核准後如何形成聘任文件？它不是講師授課後的評估、學員招生，也不是設備或場地檢查。
| 相鄰需求（需求代碼／官方方框） \| 本包如何區分 |
| 訓前五項適配檢視與調整（I12-E01／方框 056） \| 檢視學員、教材、講師、方法與環境／設備的適配並調整；不能代替講師候選人比較與任命。 |
| 學員遴選與教材審查（I12-E02／方框 057） \| 入班遴選條件與教材審查；不判斷講師資格、試教分數或聘書。 |
| 本包：講師遴選與聘任（I12-E03／官方方框 058） \| 本包：標準、三人比較、試教、資格／授權／利益衝突核驗、委員會決定、核准後聘書處理。 |
| 設備檢查與場地保險（I12-E05／方框 059） \| 設備清點與場地投保證明；聘任資料不能代替場地／設備證據。 |
| 單元目標與評量設計（I11-E02／方框 052） \| 同案例課程單元與評量設計可供對照；不能證明任何一位講師實際授課或表現。 |

2｜合成課程需求與可驗證能力
| 需求／職能落差（合成） \| 本課程講師須可示範的行為 \| 可收集的原始依據 |
| 志工紀錄欄位易漏、事實與推測混寫 \| 示範逐欄填寫；能辨認觀察、引述、推論；使用情境題修正錯誤紀錄。 \| 課程需求摘要、講師既有作品或試教講義；取用與個資授權紀錄。 |
| 交接時責任、期限、未結事項不清 \| 以交接清單說明待辦、責任人、期限、風險和回覆確認。 \| 試教評分表、情境演練觀察紀錄。 |
| 志工容易越過角色界線或傳遞敏感資訊 \| 能辨認何時停止、保護資料並轉介；不以志工課程取代專業服務。 \| 邊界情境試教、資料保護口頭提問及答案紀錄。 |
| 成人學員背景差異大、部分以手機參與 \| 指令分段、使用易讀材料、提供口頭與書面步驟及替代參與方式。 \| 試教可近性觀察表、教材版本與無障礙需求紀錄。 |

| 設計決策｜本示範將講師效能拆成五項可觀察能力；講師履歷年資本身不直接等同教學能力。試教使用同一題目、同時長、同一量尺與相同提示，避免只憑印象排序。 |

3｜權限、角色與不可跳過的關卡
| 角色 \| 工作與留存紀錄 \| 獨立性／停止條件 |
| 課程需求提出人 \| 說明職能落差、目標、對象及時數；簽名／日期須用真實來源替換。 \| 不得自行宣稱具委員會核准權。 |
| 遴選承辦人 \| 收件、編碼、檢核完整性、安排一致試教、保管檔案與版本。 \| 若同時是候選人或利害關係人，須揭露並退出受影響步驟。 |
| 評審甲／乙／丙 \| 按同一評分表獨立評分，寫具體觀察，揭露利益衝突。 \| 合成案例中的代碼非真實人員；真實名單與資格尚未確認。 |
| 委員會主席／記錄 \| 先核對章程、有效任期、出席及表決規則；記錄討論、決定、反對／迴避、責任與期限。 \| 目前協會是否有該委員會或授權均 UNKNOWN。證據未齊就不得表決或把草稿標為已核准。 |
| 聘任承辦／核准人 \| 依有權決議核定課程、期間、費用及條件，出具並送達聘書，取得回簽。 \| 不可倒填日期；未核准不得發書；真實簽章須由權責者親簽。 |

最小權限檢查清單（逐項勾選並附來源）：□ 現行章程／組織規程；□ 委員會設置與任期；□ 委員名冊與迴避規則；□ 決議門檻；□ 課程與費用核定權；□ 聘書簽發權；□ 文件保存與個資存取規則。任何一格缺來源，狀態維持 HOLD。
4｜標準、量尺、通過門檻與退件規則
| 評分面向 \| 權重 \| 0 分錨點 \| 60 分錨點 \| 100 分錨點 |
| 專業內容正確性 \| 25% \| 多項關鍵資訊錯誤，或不承認未知。 \| 主要概念正確，仍有部分例子／界線需釐清。 \| 內容準確、說明證據界線，能辨認不確定並正確轉介。 |
| 教學示範與引導 \| 25% \| 未交代目標、步驟或檢核理解。 \| 有基本說明與一個練習，回饋較單向。 \| 目標可觀察、步驟清楚，提問／練習／回饋形成閉環。 |
| 成人志工適配與可近性 \| 20% \| 假設所有人背景相同，材料不可讀或參與門檻高。 \| 可跟上一般學員，少量調整可提供。 \| 節奏、語言、字級、替代參與及休息安排均具體。 |
| 實務應用與移轉 \| 20% \| 只有抽象講述，沒有工作情境演練。 \| 有示範與練習，但回到工作後的步驟不完整。 \| 以真實可替換情境練習，提供可執行檢核及回到工作後的追蹤。 |
| 個資、角色與安全界線 \| 10% \| 洩露敏感資訊、越權承諾或鼓勵危險做法。 \| 能說明基本注意事項，但停止／轉介條件不完整。 \| 最小必要資料、保密、角色界線及停止／轉介點均說清楚。 |

評分公式：面向平均＝三位評審原始分數加總 ÷ 3；加權分＝面向平均 × 權重 ÷ 100；總分＝五項加權分總和。面向分數取整數記錄；加權分至小數一位；總分依未四捨五入的平均值計算至小數一位。權重合計 25+25+20+20+10=100%。
| 狀態 \| 規則 \| 處置 |
| 通過門檻（合成示例） \| 總分 ≥80；專業內容正確性、教學示範與引導、成人志工適配與可近性各 ≥75；個資、角色與安全界線 ≥80；無未解利益衝突；資格、授權及原始資料檢核完成；委員會有權且合法開會。 \| 列入可推薦名單；仍須經有權委員會決定。 |
| HOLD \| 原件缺漏／未驗證、權限未知、利益衝突未解、評分證據不一致、合理調整未確認。 \| 暫停排序或聘任；列明缺件、責任人及期限；不得先發聘書。 |
| REJECT \| 明顯不實資料；重大專業錯誤；安全／個資紅線；門檻未達且無可補正方案。 \| 記錄具體證據與告知／申覆途徑；不得私下刪除不利紀錄。 |

| 非補償性條件｜總分再高也不能抵銷資格未核、未授權、無效委員會、未揭露衝突或安全紅線。通過分數只形成推薦依據，不自動等於聘任。 |

5｜候選人收件、資格與衝突核驗
| 核驗欄位 \| C-01（合成） \| C-02（合成） \| C-03（合成） \| 真實使用時的原始證據 |
| 履歷／相關經驗 \| 樣本履歷索引 S-C01 \| 樣本履歷索引 S-C02 \| 樣本履歷索引 S-C03 \| 本人提交的履歷、服務證明；逐項標來源及核驗日期。 |
| 專業資格 \| 樣本核驗標記：PASS \| 樣本核驗標記：PASS \| 樣本核驗標記：PASS \| 證照影本與發證機構查驗紀錄；不得只靠自述。 |
| 教學授權／可用時段 \| 樣本：可配合 \| 樣本：可配合 \| 樣本：可配合 \| 本人同意、課程需求與排程確認；不可代替正式聘任。 |
| 利益衝突 \| 樣本：無衝突申報 \| 樣本：無衝突申報 \| 樣本：無衝突申報 \| 本人簽署申報及評審迴避紀錄；未申報先 HOLD。 |
| 個資及作品使用 \| 樣本：同意限本次遴選 \| 樣本：同意限本次遴選 \| 樣本：同意限本次遴選 \| 有日期、用途、保存期與撤回管道的真實授權。 |

上表的 PASS 都只是虛構流程欄位值，沒有任何真實證照或查詢結果附在本包。真實承辦人須把狀態改為「已驗證」並附原件位置、驗證人、日期、方式與結果；若不能核對，填「未驗證／HOLD」，不得照抄 PASS。
6｜一致試教與觀察紀錄
| 項目 \| 三位候選人共用條件（合成） |
| 題目與時長 \| 12 分鐘微型試教：「如何把一筆志工服務紀錄寫成可交接、可查核且不洩露多餘個資的紀錄」。每人同一題目、同一預備時間。 |
| 必備教學元素 \| 開場說明學習目標；用一份合成錯誤紀錄示範修正；帶學員完成一次交接欄位練習；用兩題口頭檢核確認事實／推測及停止／轉介界線。 |
| 共同觀察環境 \| 相同教室／視訊設定、相同投影設備、同一套大字版樣本、相同提問卡；合理調整以不改變評量目的為原則並記錄。 |
| 評審紀錄 \| 三人先獨立填表，記錄可觀察行為或原話；評分後才討論。不得把個人好惡寫成能力結論。 |
| 試教後確認 \| 詢問候選人如何處理錯誤答案、敏感資料、學員不同步及課後移轉；將回答摘要與面向分數分開保存。 |

| 觀察提示 \| 應記錄的具體證據（例） \| 不可直接推論 |
| 目標 \| 候選人是否用可觀察動詞說明學員課後要完成什麼。 \| 「看起來很專業」不能代替目標證據。 |
| 示範 \| 是否指出欄位、事實來源、交接責任與完成期限。 \| 投影片漂亮不能代替示範。 |
| 回饋 \| 是否指出錯誤位置、原因及修正方法。 \| 只說「很好」不能證明理解。 |
| 安全界線 \| 是否說明停止蒐集、保護資料並轉介的具體條件。 \| 沒有提到風險，不得記成「無風險」。 |

7｜三人三評審比較與可重算結果
以下是依相同量尺完成的虛構評分示例。評審甲、乙、丙為示範角色代碼，不代表協會人員。各面向原始分數範圍 0–100。
C-01｜候選評分分解（SAMPLE）
| 評分面向 \| 權重% \| 評審甲／乙／丙 \| 平均 \| 加權分 |
| 專業內容正確性 \| 25 \| 85 / 86 / 87 \| 86 \| 21.5 |
| 教學示範與引導 \| 25 \| 80 / 83 / 83 \| 82 \| 20.5 |
| 成人志工適配與可近性 \| 20 \| 78 / 76 / 80 \| 78 \| 15.6 |
| 實務應用與移轉 \| 20 \| 82 / 80 / 78 \| 80 \| 16.0 |
| 個資、角色與安全界線 \| 10 \| 90 / 92 / 88 \| 90 \| 9.0 |

C-01 合計 = 21.5 + 20.5 + 15.6 + 16.0 + 9.0 = 82.6 分。
試教步驟清楚，學習者適配尚可；評審認為需增加多元學員的替代練習與回到工作後的追蹤提示。界線面向高分只表示示範情境符合量尺，不代表真實資格核驗。
C-02｜候選評分分解（SAMPLE）
| 評分面向 \| 權重% \| 評審甲／乙／丙 \| 平均 \| 加權分 |
| 專業內容正確性 \| 25 \| 76 / 78 / 80 \| 78 \| 19.5 |
| 教學示範與引導 \| 25 \| 90 / 86 / 88 \| 88 \| 22.0 |
| 成人志工適配與可近性 \| 20 \| 74 / 76 / 75 \| 75 \| 15.0 |
| 實務應用與移轉 \| 20 \| 78 / 80 / 82 \| 80 \| 16.0 |
| 個資、角色與安全界線 \| 10 \| 84 / 86 / 85 \| 85 \| 8.5 |

C-02 合計 = 19.5 + 22.0 + 15.0 + 16.0 + 8.5 = 81.0 分。
試教引導分數高，能帶動短練習；專業內容正確性與學員適配仍需在教材可讀性及例題涵蓋面補強。安全界線分數達示例門檻，資格仍須原件確認。
C-03｜候選評分分解（SAMPLE）
| 評分面向 \| 權重% \| 評審甲／乙／丙 \| 平均 \| 加權分 |
| 專業內容正確性 \| 25 \| 90 / 92 / 88 \| 90 \| 22.5 |
| 教學示範與引導 \| 25 \| 84 / 86 / 88 \| 86 \| 21.5 |
| 成人志工適配與可近性 \| 20 \| 88 / 90 / 86 \| 88 \| 17.6 |
| 實務應用與移轉 \| 20 \| 84 / 86 / 85 \| 85 \| 17.0 |
| 個資、角色與安全界線 \| 10 \| 92 / 90 / 88 \| 90 \| 9.0 |

C-03 合計 = 22.5 + 21.5 + 17.6 + 17.0 + 9.0 = 87.6 分。
示範能連接紀錄、交接和界線情境，並為不同背景提供替代參與方式。以加權總分排序第一；推薦仍受資格原件、利益衝突及正式權限核驗條件拘束。
| 排序 \| 候選代碼 \| 總分 \| 分數門檻 \| 示例決定 |
| 1 \| C-03 \| 87.6 \| 達標 \| 可提出條件式推薦；先核原件及權限。 |
| 2 \| C-01 \| 82.6 \| 達標 \| 備選；依相同條件完成核驗。 |
| 3 \| C-02 \| 81.0 \| 達標 \| 備選；其學員適配補強事項列入條件。 |

排序核對：C-03 87.6 > C-01 82.6 > C-02 81.0。各候選的專業內容正確性、教學示範與引導、成人志工適配與可近性，以及個資、角色與安全界線均達示例門檻；若真實原件或權限有任何一項無法核驗，該候選立即 HOLD，不因排序高而例外。
同分處理（SAMPLE / SYNTHETIC，提案規則）：若加權總分相同，先比較『專業內容正確性』加權點數，再比較『教學示範與引導』加權點數；仍同分時，安排相同題目、準備時間、時長及量尺的第二次試教，記錄評審觀察與分數。若仍同分，或無法核實具權限者與已核定的後續規則，立即 HOLD，依真實章程與授權處理，不另創規則。本例三組加權總分互異，未觸發此程序。此提案須由具權限者核定後始得正式採用。
評審觀察摘要（合成）
| 候選 \| 支持分數的具體觀察 \| 待確認／改善事項 |
| C-01 \| 使用三欄示例指出事實、來源、交接責任，練習後要求學員復述。 \| 增加較大字版及口頭替代回覆；補上課後交接檢核。 |
| C-02 \| 先示範錯誤紀錄，再邀請學員提出修改，並用問題確認學習。 \| 教學材料需補不同閱讀程度例子；授權與原件仍須核驗。 |
| C-03 \| 用同一案例完成紀錄與交接，明確指出不記錄推測及停止／轉介點。 \| 取得真實資格原件、確認授課時段與費用授權後才可聘任。 |

8｜利益衝突處理與推薦規則
| 狀況 \| 處理方式 \| 紀錄欄位 |
| 評審與候選人有近親、財務、督導、競爭或其他可能影響公正的關係 \| 評審於看分前申報；承辦判斷迴避範圍；需要時由有權者指定替代評審。 \| 申報人、關係類型、評估者、處置、替代人、日期。 |
| 候選人資料涉及不必要個資 \| 只保留評選必要欄位；限制存取；依組織正式保存規則處理到期刪除。 \| 資料項目、用途、存取人、保存期限、刪除核准。 |
| 資料不一致或資格查不到 \| 先凍結該候選評分結論；要求補件或以獨立來源查驗；保留往返紀錄。 \| 缺件、查驗來源、聯絡日期、期限、結果。 |

本合成情境設定三名評審均申報「無已知衝突」，僅供示範表單填寫。真實評審必須分別簽署日期與申報內容；空白不等於無衝突。
9｜訓練管理委員會議程與決定紀錄（模擬）
| 完全合成的會議情境｜以下會議日期、出席、權限、討論與決定均為虛構。文件以「假設權限已由真實文件證明」示範決議記錄形式，並不證明原始點協會已成立委員會或作出決議。 |

| 欄位 \| SAMPLE 填寫示例／真實替換要求 |
| 會議基本資料 \| 合成日期：2026-11-10（未來示例）；14:00–15:00；會議方式：合成實體會議；地點：SAMPLE。正式使用需填實際日期、場地、通知與簽到原件。 |
| 出席及法定人數 \| 主席 P-01、紀錄員 S-01 均不表決；表決委員 M-01／M-02／M-03（皆合成）。示範門檻：3 人中至少 2 人出席；實到 3／3。真實規則須依章程、任期及簽到原件驗證，未驗證即 HOLD。 |
| 議程一：權限確認 \| 示範決定前先檢視章程、委員會任期、決議門檻、聘書簽發權與費用核定權；本樣本假設附件均已驗證，真實情形目前 UNKNOWN。 |
| 議程二：需求與流程 \| 確認課程需求摘要、評選量尺、同題試教、三位評審的利益衝突申報及資格查驗清單。 |
| 議程三：比較結果 \| 審閱 C-01 82.6、C-02 81.0、C-03 87.6；討論 C-03 教學適配較完整，但須在實際聘任前完成原件查驗及排程確認。 |
| 合成決議 \| SAMPLE：示範假設 3 名表決委員中至少 2 票同意才通過。示範實得 3 票同意，僅附條件推薦 C-03；未核完資格、權限及其他 HOLD，不得簽發。此非真實決議。 |
| 反對／迴避／附件 \| 合成計票：贊成 3 票、反對 0 票、棄權 0 票、迴避 0 人。真實會議應逐項登錄票數、迴避與附件版本及頁數；未記錄不得以零或「無」代替。 |
| 責任與期限 \| 承辦 A-01（合成）於 2026-11-17 前核對 C-03 原件、授課時段與費用授權；主席 P-01（合成）於核驗後依真實權限決定是否簽發；未完成則維持 HOLD。 |

決議確認欄（真實使用）：主席簽名／日期：________________；紀錄員簽名／日期：________________；附件清單：________________。此處空白且不得由本樣本代簽。
10｜聘書處理流程與未發出聘書樣本
| 步驟 \| 必須先有的證據 \| 不得越過的關卡 |
| 1. 形成推薦 \| 完整評分、試教、資格／授權／衝突檢核。 \| 未達門檻或有 HOLD 不推薦。 |
| 2. 委員會決定 \| 有效權限、通知、簽到、議事規則、逐項決議及附件。 \| 草稿、口頭意見或不明權限不能當正式核准。 |
| 3. 核定條件 \| 課程版本、日期、總時數、費用來源、支付條件、教材及個資條款。 \| 未經授權不得自行承諾費用或期間。 |
| 4. 簽發與送達 \| 正式聘書編號、核准人簽章、送達證明。 \| 不得預簽、倒填、代簽或以此樣本冒充原件。 |
| 5. 接受與歸檔 \| 講師簽收／接受、版本、保存位置及權限。 \| 未接受不視為已完成任命。 |

| SAMPLE｜NOT ISSUED｜NOT VALID｜以下文字只示範聘書欄位與條件。不得列印後簽發；不得使用協會真實印信；日期、費用與角色代碼全為虛構。正式發出前須替換並核實所有資料，取得有權委員會決議及核定人簽章。 |

| 聘書欄位 \| 示範文字（全部為合成草稿） |
| 受聘人／編號 \| C-03（虛構代碼；非真實講師姓名）；聘書草稿編號 SAMPLE-APPT-001。 |
| 課程與工作範圍 \| 課程：志工服務紀錄、交接與工作界線實務；四單元，共 360 分鐘。工作：依核定教案授課、帶領練習、回報學習狀況、完成必要教材修訂及課後紀錄。 |
| 日期與地點 \| 樣本期間：2026-12-05；日期為虛構未來日期，實際開課時間與地點待核定。 |
| 費用條件 \| 示例酬金 NT$4,800（360 分鐘 × 合成每小時 NT$800）。此數字未經協會核准，不代表支付承諾；正式使用需有預算、稅務與支付規則來源。 |
| 履約條件 \| 遵守核定課程目標、角色界線、個資保護與場地安全規則；未經同意不得另行蒐集或公開學員資料；教材授權範圍以真實契約為準。 |
| 取消／變更 \| 日期、時數、費用或教材有變更時，由雙方以可追溯方式確認並依授權程序核准；不可單方補填。 |
| 簽章欄 \| 委任單位有權代表：________________／日期：____；受聘人接受：________________／日期：____。本樣本未簽發、未送達、未接受。 |

11｜授課後回饋與改進閉環（尚未發生）
此節是任命後的追蹤表單設計，不是本案例已授課或已有成效。實際授課後應把觀察與學員回饋連回遴選面向，並作成續聘、補強或停止合作的有權決定。
| 追蹤時點 \| 收集資料 \| 判讀問題 \| 責任／處置 |
| 課前 \| 核定課程、教材版本、講師資格原件、場地與個資說明。 \| 人、課程、版本和核准條件是否一致？ \| 承辦核對；任一不一致先暫停開課。 |
| 課中 \| 出席、授課完成度、學員練習、重大偏差或安全事件。 \| 教學是否達標；是否需即時調整？ \| 授課承辦記錄事實，不把未觀察寫成通過。 |
| 課後 5 個工作日（示例時限） \| 學員回饋、成果作品、講師自評及改進建議。 \| 目標達成情形如何；資料是否足以支持結論？ \| 承辦彙整；不足時標 UNKNOWN 並補證據。 |
| 下次遴選前 \| 歷次回饋、改進閉環、申訴或事件處理。 \| 是否調整量尺、教材或聘任條件？ \| 有權者核定變更並保留版次。 |

12｜真實使用替換清冊與完整證據鏈
本節隨附一份逐筆替換清冊，逐筆列出合成資料、假設理由、跨文件引用、應取得的真實原始來源、負責核實角色、真實／合成狀態及 HOLD 條件，共 52 筆；不得直接把示範值複製為真實紀錄。下表列出主要證據鏈。
| 順序 \| 真實原始證據 \| 形成／保管責任 \| 缺件時狀態 |
| 1 \| 現行章程、委員會設置／任期／權限及聘書簽發授權。 \| 秘書／有權治理者核對正本或受控副本。 \| HOLD：不得開會作成正式決議。 |
| 2 \| 有日期的職能需求、課程目標、對象與課程計畫版次。 \| 需求提出人與課程承辦；版本連結至課程檔案。 \| HOLD：不得以本合成需求代替。 |
| 3 \| 候選人本人履歷、資格原件及獨立查驗紀錄。 \| 遴選承辦；保留來源、日期、方式與核驗人。 \| HOLD：未查驗不得列為資格 PASS。 |
| 4 \| 三位評審原始評分、試教觀察、利益衝突申報。 \| 各評審獨立簽署；承辦保留原始版本。 \| HOLD：不可補寫一致意見掩蓋差異。 |
| 5 \| 合法通知、簽到、會議記錄、附件、逐項決議及表決結果。 \| 有權主席與紀錄員；保存更正軌跡。 \| HOLD：不得稱已核准。 |
| 6 \| 有權核定的聘書、簽發與送達證明、講師接受／回簽。 \| 授權簽發人及聘任承辦；登錄原件位置。 \| HOLD：不得授課或支付，除非另有有效授權依據。 |
| 7 \| 課前核對、課程執行、課後評估及改進紀錄。 \| 課程承辦與評估責任人。 \| UNKNOWN：未實際發生前不可填結果。 |

13｜文件狀態與驗收控制
| 欄位 \| 狀態／內容 |
| 範例定位 \| 講師遴選與聘任流程範例；對應官方指標 12c（需求代碼 I12-E03；官方方框 058）。 |
| 候選狀態 \| 候選示範文件；不是協會正式核准、任命或真實證據。 |
| 來源依據 \| 官方訓練品質評核表第 4 頁指標 12c；寫作手冊指標 10 與 12；官方方框 058 的內容方向。來源版本資訊另存於驗收附屬檔案。 |
| 一致性核對 \| 課程 360 分鐘＝90+90+120+60；五權重合計 100%；加權總分 C-01 82.6、C-02 81.0、C-03 87.6；排序一致。 |
| 形式與樣本界線 \| 全文件及表單標為 SAMPLE/SYNTHETIC；無真實人名、證照影本、核准簽章或任命事實。聘書標 NOT ISSUED / NOT VALID。 |
| 正式使用前的驗收要求 \| 須完成技術版面檢查、全頁目視、獨立語意複核與人工驗收；本文件目前僅為候選示範，尚未取得任何正式驗收。 |
