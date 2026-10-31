TTQS ONE independent exact-SHA semantic delta review
Review type: read-only; do not modify files or use tools.
Doc ID 0100; official requirement I18-E08; candidate R09b.
Candidate DOCX SHA-256: 0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c
Candidate body extraction SHA-256: 0c3c7370db89e529d7fd963f69eedaae2701956fea0c65956f7432066f71734e
Baseline R09a DOCX SHA-256: debd41e7ca1b18b88cad37db118c5b3474df411b3e2d1c87a8351d456245e0b2
The supplied previous R09a review applies only to the stated baseline. R09b changes are restricted to delta F1-F4; do not inherit coverage for changed text. Review every changed paragraph/table row in the supplied diff and current candidate body against the source packet and Unique Blueprint. Check the full document purpose and genre, usability, synthetic/real boundary, numeric consistency, and handoff to 0101. Use the technical, visual, and cross-document receipts only for their declared scopes; do not claim to have inspected rendered pages yourself.
Important: the prior Antigravity result reported PASS but actual serving model identity is UNKNOWN. Treat it only as a prior response for comparison, not as a model-qualified verdict. Do not claim any model/provider identity beyond your own OpenCode session metadata.
Do not assert real association approvals, learner records, signatures, or formal acceptance. REAL remains UNKNOWN/HOLD; formal acceptance remains NOT_GRANTED.
Return one compact JSON object with keys:
doc_id, requirement_id, candidate_sha256, body_sha256, verdict (PASS/PARTIAL/FAIL), scope, baseline_inheritance_basis, criteria (F1,F2,F3,F4, no_new_material_contradiction, sample_real_boundary, cross_document_handoff), findings (array; each with locator, evidence_excerpt, defect, required_change), limitations, formal_acceptance (must remain NOT_GRANTED), real_evidence (must remain UNKNOWN/HOLD).
A PASS is allowed only if all criteria are supported with precise paragraph/table locators and no material defect. If evidence is insufficient, use PARTIAL and say exactly what is missing.

===== OFFICIAL_SOURCE_PACKET SHA256=81caa978a17dda522850628e6e9b4b16453145a986d2bafd2598b6f5ac96b886 BYTES=5253 =====
# I18-E08 來源包 R09｜0100 自評表 + 0101 雷達分析報告

## 權威綁定（依目前 GitHub PR #92 live head）

- Repository/PR/branch: `PT-Original-Point/ttqs-one` / `#92` / `work/ttqs-one-document-quality-contract-20261016`
- Source commit observed: `ea43984228f70b99b7003f8cb70fdad67f3e20ba`
- GOAL contract `04_CODEX_GOAL_24X7_EXECUTION.md`, blob `4ee893218791ec9460e824fc559933c276414738`.
- 120-minute wake contract `05_HOURLY_NATIVE_WAKE_RESUME.md`, blob `35d3081c7e7fb979466c3a58a1e77b42f0d1441a`; its ACTIVE 2026-10-21 override supersedes old 60-minute terms.
- Worker/acceptance contract `06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md`, blob `4c7eff55748ff265b1e5a7d1122852b0d101acbd`; relevant §5.2–5.4 and §6.6–6.8.
- Official TTQS training-institution evidence PDF, p.7, indicator 18; Windows source SHA-256 `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709` (9 pages). Requirement: learner pre/post self-assessment and radar analysis that presents perceived change.
- 157-item writing contract `03_157_CHECKBOX_BLUEPRINTS.md`, blob `8c2bbe7ca9dcbb03088a48934b9e57e7147ede63`; project internal index 109 for I18-E08. This is not the official printed checkbox serial; that serial remains `UNKNOWN` unless read from the original form.
- 129-to-142 crosswalk blob `1ac4a8419088d947947031b758e29c35a3606514`: `I18-E08 -> 0100 | 0101`, names: learner pre/post self-assessment form; perceived-growth radar analysis report.

## Current Human override and scope

The live 04/05 documents direct the I18-E08 worked example to use an 8-person × 5-dimension × 2-phase synthetic fixture (80 original score cells), with pre sum 75, post sum 117, net +42, mean net +5.25. The prior local R08 source packet/blueprints and 0101 R08A candidate were based on 1 person × 6 dimensions. Those artifacts are preserved as historical, but are stale against the live 04/05 override and must not be treated as current acceptance evidence. Do not reuse R08A/R08B/R08C body as a template.

The common numeric fixture below is intentionally reused from 0099 R17 solely as an explicit, synthetic cross-document demonstration fixture, as permitted by live 04/05. It does not establish that 0099 rubric scores and I18-E08 self-reports are the same measurement, do not show agreement/correlation, and are not independent empirical evidence. In I18-E08 these values are only synthetic learner self-ratings. State this limitation plainly in both documents. Do not import the 0099 skill-rubric pass threshold or conclusions into the self-rating report.

## Shared synthetic fixture (authoritative within this sample package)

All A01–A08 codes and values are synthetic. Dimensions A–E are: A source facts/context; B record completeness/traceability; C task-to-output application; D data minimization/privacy awareness; E follow-up planning. Self-rating anchors are 0–4 and belong to this illustrative form only; no association-approved scale is asserted.

|Code|Pre A/B/C/D/E|Pre total|Post A/B/C/D/E|Post total|Change|
|---|---|---:|---|---:|---:|
|A01|2/2/1/2/1|8|3/3/3/3/3|15|+7|
|A02|2/2/2/2/2|10|3/3/3/3/4|16|+6|
|A03|3/2/2/2/2|11|3/3/3/3/2|14|+3|
|A04|2/2/1/2/2|9|3/3/2/3/2|13|+4|
|A05|3/3/2/2/2|12|4/4/3/3/4|18|+6|
|A06|1/2/1/1/2|7|3/2/2/3/2|12|+5|
|A07|2/2/2/2/2|10|3/3/3/3/3|15|+5|
|A08|2/1/2/1/2|8|3/3/3/3/2|14|+6|

Formula checks: 80 values; all 0–4; pre total 75; post total 117; total change 42; n=8; mean total 9.375 -> 14.625; mean change 5.25/20. Per dimension A pre17/post25 (2.125 -> 3.125; +1.000), B 16/24 (2.000 -> 3.000; +1.000), C 13/22 (1.625 -> 2.750; +1.125), D 14/24 (1.750 -> 3.000; +1.250), E 15/22 (1.875 -> 2.750; +0.875). The total score range is 0–20. All values are SAMPLE/SYNTHETIC, not training results.

## Companion artifacts and state

- 0099 R17 source sample DOCX SHA-256: `293be2dc0e3e0162fa368272851baed27e92990b4ac1871228ec37b51546776b`; its own requirement is I18-E07. Do not modify or formally reclassify it.
- Existing 0100 R08 candidate SHA-256 `f7f3addfed3bfe46aba1a3f282e22b7f92d36de8a1b1c8252e4a77bad1e270d1` is 1-person/6-dimension and is not the live 8×5 sample; preserve as historical.
- 0101 R08A `0f9e0713a8d98c0c28b2b33234c8a4bbd4548c21d17be209f1696965984932a1`, R08B `320e12bcd5c749ffcfd80f59853e9b784321fda6bb1f0eb7fe39fd1ca62a8a0e`, and R08C `7b779684bab9d050c4e160daefe62a15348a906cdb594a65fed496812b3980f6` are historical revisions of the stale 1×6 draft. R08B/R08C corrected font and pagination only; they are not current acceptance candidates.
- 0100 R09 and 0101 R09 are new candidate work and must each receive their own source mapping, Blueprint, SAMPLE replacement register, deterministic QA, Word visual review, and independent exact-SHA semantic review. No REAL input/original or formal acceptance is present.

## Current READY derivation

`READY_SOURCE_PACKET=VERIFIED` (this versioned packet now binds current contracts/source and fixture); `READY_BLUEPRINT=READY` for both 0100 and 0101 (separate files below); `READY_WRITER=0100` because no matching live writer was found and its output is a usable filled self-assessment instrument, not a blank title shell. 0101 becomes `READY_WRITER` only after a stable 0100 R09 candidate and its exact SHA exist.


===== UNIQUE_BLUEPRINT SHA256=c407af272823d0159bbbe0c1c9258ed74ee89e5328bd8338840cef26183b2817 BYTES=4829 =====
# Unique Blueprint 0100 R09｜學員訓練前後自我評量表

## Authority and document type
- Requirement: I18-E08; project internal index 109 (not the official printed checkbox serial; official serial UNKNOWN).
- Official source: TTQS training-institution evidence PDF p.7: learner pre/post self-assessment and radar analysis should present perceived change.
- Crosswalk: I18-E08 decomposes into 0100 and 0101. 0100 is a learner-facing self-rating instrument and completed synthetic response set; 0101 is the separate aggregate analysis/report. This form is not a skills-performance rubric, satisfaction survey, sign-in sheet, or training result.
- Current source package: `SOURCE_PACKET_I18-E08_0100_0101_R09.md`; live contract hashes recorded there.

## Required use
A training administrator issues the same five dimension statements before and after a sample training activity. Each learner uses the same private synthetic code at both times. The respondent selects one 0–4 self-rating per dimension and can add a short example. No name, phone, address, signature, or personal contact information is required. Use the completed responses as data for 0101 only after matching the same code and version. This sample contains both a reusable form and eight completed SAMPLE pairs.

## Five self-rating dimensions and anchors
A source facts/context; B record completeness/traceability; C task-to-output application; D data minimization/privacy awareness; E follow-up planning. Use the same prompt before and after. Scale anchors for this synthetic form: 0 = not yet able to describe/do the step; 1 = can begin only with step-by-step support; 2 = can complete some parts using an example/checklist; 3 = can complete a typical task independently; 4 = can explain, check and adapt the step to a new example. These are self-perception anchors, not validated competency standards and not an association-approved pass threshold.

## Required sections/tables
1. Cover/instructions showing I18-E08, doc_id 0100, SAMPLE/SYNTHETIC, intended user, time to administer and how 0101 uses the responses.
2. Course/sample metadata (synthetic course code/title/date; questionnaire version; pre/post dates; pair code; no real participant identity).
3. Five dimension prompts with respondent-facing wording and examples of what each dimension means.
4. Separate pre and post fillable response sheets with the same code/version, date, five score choices, optional short reflection and completeness check.
5. One complete synthetic dataset matrix for A01–A08 with five pre and five post scores, phase totals and per-person change (80 original numeric cells; calculated totals are derived). Data exactly matches the R09 source packet.
6. Intake/quality-control instructions: same person code; same version; date ordering; valid range 0–4; missing/duplicate/inconsistent entries are held, never imputed as zero; record exclusions and reason.
7. Privacy and replacement instructions: how to keep names separate or avoid collection; no actual code key in the published sample; access, retention and legal authority are not assumed.
8. A practical one-page administrator sequence, common mistakes, hold/reject criteria and handoff to 0101.
9. SAMPLE replacement register reference and warning that shared numbers are an illustrative fixture reused from 0099 R17 only by current Human override; this does not equate self-rating with observed skill evidence.

## Exact score fixture
Copy the 8×5 pre/post scores exactly from the R09 source packet. Totals must be pre 75, post 117, difference +42; no other sample score may be invented or substituted. Use the same A01–A08 pair codes in all 0100/0101 sample references. All sample course details and dates remain synthetic.

## Distinctive evidence / anti-substitution
The body must look and function as an actual respondent form: clear instructions, one answer per dimension and paired pre/post codes. It must not be primarily a radar report, skill rubric, satisfaction questionnaire or narrative case report. The completed numeric sample is present to demonstrate data flow, not evidence that the association conducted training.

## Reject / hold if
- Any score falls outside 0–4, any response missing, duplicate code, code mismatch, questionnaire version mismatch or date order invalid.
- Any missing value is imputed or the denominator is hidden.
- The shared sample is called real, association-approved, measured training success, or objective skill proof.
- The unapproved self-rating anchors are called official/validated; a score threshold is treated as formal pass.
- The same form text, code, course, date or scores disagree with the source packet or 0101.
- It lacks a respondent-operable sheet, complete 8-pair SAMPLE matrix, or concrete steps for data checking and 0101 handoff.


===== BASELINE_R09A_REVIEW SHA256=986c00397f2e075c56cb6874b7c18ee0262c441925cdc8cb257e7adbdc37df1b BYTES=5774 =====
{
  "receipt_id": "TTQS-I18E08-DOC0100-R09A-SEMANTIC-REVIEW-RESULT-20261021",
  "work_id": "TTQS-I18E08-DOC0100-R09A-SEMANTIC-REVIEW-OPENCODE-20261021",
  "doc_id": "0100",
  "official_requirement_id": "I18-E08",
  "revision": "R09a",
  "verdict": "PASS_SEMANTIC_ONLY",
  "candidate_state": "CANDIDATE_NOT_FORMALLY_ACCEPTED",
  "candidate_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09\\0100_I18-E08_R09.docx",
  "candidate_sha256": "debd41e7ca1b18b88cad37db118c5b3474df411b3e2d1c87a8351d456245e0b2",
  "candidate_bytes": 58574,
  "reviewer": "Independent OpenCode v2 CLI plan agent; read-only",
  "requested_model": "opencode/deepseek-v4.1-flash-free",
  "native_session_model": {
    "id": "deepseek-v4.1-flash-free",
    "providerID": "opencode"
  },
  "native_session_id": "ses_ea1cf5503ffe00DhJ9tzXxSzPG",
  "native_session_status": "succeeded",
  "native_session_directory": "E:/TTQS",
  "native_agent": "plan",
  "started_local": "2026-10-21T19:20:10.399000+08:00",
  "finished_local": "2026-10-21T19:27:04.142000+08:00",
  "duration_seconds": 413.743,
  "cli_exit_code": 0,
  "usage": {
    "input_tokens": 196596,
    "output_tokens": 14196,
    "reasoning_tokens": 45375,
    "cache_read_tokens": 2321408,
    "cache_write_tokens": 0,
    "local_cost": 0.0,
    "provider_billing": "UNKNOWN"
  },
  "stdout": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09\\review\\opencode_semantic_R09a_20261021\\reviewer_stdout.jsonl",
    "sha256": "fccdf17bfbfa84cdd15079d6a7bf1d654a72511848b8453af91f44cc9bc46203",
    "bytes": 355736
  },
  "stderr": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09\\review\\opencode_semantic_R09a_20261021\\reviewer_stderr.txt",
    "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "bytes": 0
  },
  "reviewer_final_text": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09\\review\\opencode_semantic_R09a_20261021\\reviewer_final_text.txt",
    "sha256": "c3b6a73d598556d90db6b25cd5f15d59addd52538490aeccd8723ff20d802d2f",
    "bytes": 16384
  },
  "reviewed_inputs": [
    {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09\\0100_I18-E08_R09.docx",
      "sha256": "debd41e7ca1b18b88cad37db118c5b3474df411b3e2d1c87a8351d456245e0b2",
      "bytes": 58574
    },
    {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\SOURCE_PACKET_I18-E08_0100_0101_R09.md",
      "sha256": "81caa978a17dda522850628e6e9b4b16453145a986d2bafd2598b6f5ac96b886",
      "bytes": 5253
    },
    {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\UNIQUE_BLUEPRINT_0100_I18-E08_R09.md",
      "sha256": "c407af272823d0159bbbe0c1c9258ed74ee89e5328bd8338840cef26183b2817",
      "bytes": 4829
    },
    {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\UNIQUE_BLUEPRINT_0101_I18-E08_R09.md",
      "sha256": "51b5a85d08c85550fa18de656ab7e9cdb3923831f4584ea7e9bf4da3ce35e8ce",
      "bytes": 4625
    },
    {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09\\synthetic_replacement_register_0100_R09.csv",
      "sha256": "889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8",
      "bytes": 65820
    },
    {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09\\review\\opencode_semantic_exact_sha_20261021\\reviewer_final_text.txt",
      "sha256": "fc162d9dcb033378e04f3ca15e82e890dc2c4d782ed026d1bca08250877b0321",
      "bytes": 12139
    }
  ],
  "scope": [
    "official requirement and unique blueprint",
    "genre and practical usability",
    "SAMPLE/REAL boundary",
    "80 raw score cells and arithmetic",
    "R1 repair criteria",
    "replacement register and cross-document boundaries"
  ],
  "not_in_scope": [
    "visual rendering (separate receipt)",
    "formal association acceptance",
    "real learner or course evidence"
  ],
  "findings": [
    {
      "id": "F1",
      "severity": "MINOR",
      "summary": "Cross-stage duplicate code pair cannot be verified as same respondent; hold/reject unmatched pair before delta."
    },
    {
      "id": "F2",
      "severity": "MINOR",
      "summary": "Operational privacy inspection checklist at §6.1/§4.4/§5.4 should explicitly include employer/client/service-recipient names already prohibited by §7."
    },
    {
      "id": "F3",
      "severity": "MINOR",
      "summary": "R09a visible version/status says no independent review while filename/register remain R09; clarify the filename convention and update status at final acceptance."
    },
    {
      "id": "F4",
      "severity": "TRIVIAL",
      "summary": "§10.1 uses shorthand “4碼”; blank value classification overlaps; sample CSV header has leading spaces."
    }
  ],
  "semantic_conclusion": "PASS for exact candidate SHA. Reviewer explicitly states F1–F4 do not meet Blueprint REJECT/HOLD threshold and do not invalidate current synthetic 80-cell sample; keep listed residuals visible. Do not convert to formal acceptance."
}

===== BASELINE_R09A_BODY SHA256=f88b508539380bb2a29824fbf53f0d39492016d5a3a6eecb10a96b5f7b2e610a BYTES=25543 =====
P001: 0100 學員訓練前後自我評量表
P002: 版次 R09a｜SAMPLE／SYNTHETIC 示範稿｜需求編號 I18-E08｜DOC_ID 0100
P003: 目錄
P004: 1. 文件識別與使用聲明
P005: 2. 使用方式與樣本基本資料
P006: 3. 五個自評維度與 0–4 錨點
P007: 4. 前測填答頁（可複印使用）
P008: 5. 後測填答頁（可複印使用）
P009: 6. 收回檢核、缺漏處理與退件條件
P010: 7. 隱私與資料最小化
P011: 8. 合成示範資料集（80 格）與驗算
P012: 9. 與 0101 的交接
P013: 10. 承辦人一頁式流程與常見錯誤
P014: 11. SAMPLE 替換登錄與版本限制
P015: 1. 文件識別與使用聲明
P016: 1.1 文件識別
P018: 1.2 這份文件是什麼、不是什麼
P019: 本文件是一份學員自己填答的前測／後測自評工具，用來記錄學員在五個維度上「自覺能做到的程度」在訓練前後的變化，並把檢核完成的資料交給 0101 製作雷達分析報告。
P020: 本文件不是技能檢定或技能評分量表，不是滿意度調查，不是簽到表，不是訓練成果的客觀證明，也不是任何機構已辦理訓練的紀錄。
P021: 本表所附的 8 人資料（A01–A08）全部為 SAMPLE／SYNTHETIC：其中的課程名稱、課程代碼、日期、機構名稱、人員代碼與分數均為示範值，不代表任何真實機構、真實人員、真實參與、真實核准、真實簽署或真實訓練結果。本稿亦不主張任何協會核定、認證或背書。
P022: 1.3 數值來源與限制聲明（必讀）
P023: 1. 本表第 8 節的 8 人 × 5 維度 × 2 階段共 80 格原始分數，是依現行契約指示，自 0099 R17 共用同一組合成數值，僅作為跨文件一致性的合成示範 fixture。
P024: 2. 這組數值在 0099 是技能評分示範，在本文件則只是學員自評值。兩者不是同一種測量，不得據此宣稱自評等於技能評分，不得宣稱兩者一致、相關或可互相驗證，也不得視為獨立實證資料。
P025: 3. 本表不引用 0099 的技能評分通過門檻，也不另行設定自評通過門檻。0–4 錨點僅供本示範表使用，非協會核定、非信效度驗證之量表。
P026: 4. 本表呈現的是「自覺改變」（perceived change），不是客觀能力提升量。
P027: 2. 使用方式與樣本基本資料
P028: 2.1 適用對象與使用時機
P029: 填答者：接受同一場訓練活動的成人學員。
P030: 前測：訓練開始前填寫，用於建立自覺起點。
P031: 後測：同一場訓練結束時（或依機構規劃於訓練後短期內）填寫，題目、版本、配對代碼必須與前測完全相同。
P032: 施測者：由承辦人或指定人員統一發放、說明、收回與檢核，不代填、不誘導、不改分數。
P033: 2.2 施測時間與方式
P035: 2.3 樣本課程與填答基本資料（全部為 SAMPLE）
P037: 2.4 配對代碼規則
P038: 1. 正式施測時，每位學員自行選一組四位數字配對代碼（僅 0–9），前測與後測必須完全相同。本文件資料表中的 A01–A08 是三字元的 SAMPLE／SYNTHETIC 示範識別碼，僅供展示合成數據，不是正式施測代碼，也不得轉用為真實學員代碼。
P039: 2. 代碼不得包含姓名、生日、電話、學號、身分證號、電子郵件或任何可直接或間接識別個人的資訊。
P040: 3. 承辦人不代選、不代填、不代改；若學員忘記代碼，由本人憑記憶重填，不得由承辦人翻查找回後代為填寫。
P041: 4. 本示範稿不含任何代碼對照表；正式使用時若機構自行建立對照表，須依第 7 節分開保管，且不得隨本表或 0101 流通。
P042: 5. 同一階段出現兩份以上相同代碼時，該代碼的全部表單立即 HOLD；不得挑選分數較完整或日期較清楚的一份。只有各填答者本人在場確認並留下更正註記後才可解除；無法安全確認歸屬時，全部 REJECT 並排除於有效分母。
P043: 3. 五個自評維度與 0–4 錨點
P044: 3.1 五個維度（前後測題目完全相同）
P046: 3.2 0–4 自評錨點（僅適用本示範表）
P048: 填答提醒：請依「現在」的實際感受選一個分數，不必與他人比較，也不必猜標準答案。本表沒有及格分數，高分或低分都不影響任何權益；低分只代表可再強化的地方。
P049: 4. 前測填答頁（可複印使用）
P050: 4.1 填答說明
P051: 1. 本表共 5 題，每題請只勾選 一個 0–4 分。
P052: 2. 正式施測請自選一組四位數字（0–9）配對代碼，後測填同一組；A01–A08 僅是本文件的合成示範識別碼，不是正式代碼。
P053: 3. 每題下方的「例子」欄可空白，寫一句自己的經驗即可。
P054: 4. 填完請完成 4.4 的完整性檢查再交回。
P055: 影印／回收方式：前測完整表單共兩頁；基本欄位、自評題、例子與檢查頁須按頁序整組使用及回收，不拆頁。
P056: 4.2 基本欄位
P058: 4.3 五題自評
P059: 本頁量尺速查（完整行為錨點見第 3.2 節）：0＝還無法描述或執行；1＝需逐步帶領；2＝看範例或檢核表可完成一部分；3＝可獨立完成典型任務；4＝可解釋、檢查並套用到新例。
P061: 我的例子（可空白）
P063: 4.4 前測完整性檢查（交回前自行確認）
P064: ☐ 正式填答代碼為四位數字，且不含姓名、生日、電話或證件號碼
P065: ☐ 五題都各只勾選一個分數；任何漏選或多選均先 HOLD，不自行補值
P066: ☐ 所有分數都在 0–4 之間
P067: ☐ 版本為 SR-0100-v1.0-SAMPLE
P068: ☐ 日期已填
P069: ☐ 我記得後測要使用同一組配對代碼與同一版本
P070: 5. 後測填答頁（可複印使用）
P071: 5.1 填答說明
P072: 1. 題目與前測完全相同，請依「現在」的感受重新評一次，不需要刻意與前測分數比較。
P073: 2. 請填入與前測完全相同的四位數字配對代碼與版本。A01–A08 是本文件合成資料識別碼，並非正式填答代碼。
P074: 3. 每題只勾一個 0–4 分；漏選或多選先 HOLD，請本人更正，例子欄可空白。
P075: 影印／回收方式：後測完整表單共兩頁；基本欄位、自評題、例子與檢查頁須按頁序整組使用及回收，不拆頁。
P076: 5.2 基本欄位
P078: 5.3 五題自評
P079: 本頁量尺速查（完整行為錨點見第 3.2 節）：0＝還無法描述或執行；1＝需逐步帶領；2＝看範例或檢核表可完成一部分；3＝可獨立完成典型任務；4＝可解釋、檢查並套用到新例。
P081: 我的例子（可空白）
P083: 5.4 後測完整性檢查（交回前自行確認）
P084: ☐ 配對代碼與前測完全相同
P085: ☐ 版本與前測相同（SR-0100-v1.0-SAMPLE）
P086: ☐ 五題各只勾選一個分數且在 0–4 之間；漏選或多選均先 HOLD，不由承辦人代選
P087: ☐ 後測日期不早於前測日期
P088: ☐ 未在表上書寫姓名或聯絡方式
P089: 6. 收回檢核、缺漏處理與退件條件
P090: 6.1 收回檢核步驟（承辦人）
P091: 1. 當場確認每人前、後測各一份，並核對代碼是否相同。
P092: 2. 逐份檢查五題是否各只有一個勾選、是否落在 0–4；漏選或多選均先 HOLD，請本人補正，不可自行選值。
P093: 3. 檢查版本欄是否一致；不一致者先隔離，不併入資料。
P094: 4. 檢查日期先後；後測早於前測者退件。
P095: 5. 檢查是否有學員自行寫上姓名、電話等個資；如有，當場遮蔽或請本人重填於新表。
P096: 6. 依配對代碼排序，重複代碼立即抽出，依 6.2 處理。
P097: 7. 登錄「收回份數、有效份數、保留份數、退件份數」，並記錄原因。
P098: 8. 只有在全部檢核完成後，才把資料交給 0101。
P099: 6.2 缺漏、重複與不一致的處理
P101: 6.3 退件與保留彙總清單
P102: HOLD（可補正後再用）：單題漏選或多選、字跡不清、代碼疑似打錯、日期未填、重複代碼待本人確認。重複代碼的全部相關表單一律先 HOLD，不得先選一份計分。
P103: REJECT（不得補正，直接排除）：版本不符、後測早於前測、承辦人代填、拒絕更正之個資欄位、本人無法確認歸屬的重複代碼或無法安全確認的配對。
P104: 必要原則：任何缺漏都不得補值；排除份數與原因必須與有效份數一起揭露，分母不得隱藏。
P105: 7. 隱私與資料最小化
P106: 1. 不收集：姓名、電話、地址、生日、身分證號、學號、簽名、照片、任職單位全名、雇主／客戶／服務對象名稱。
P107: 2. 只收集：四位數字配對代碼、版本、階段、日期、5 個 0–4 分數、可選的一句例子；例子不得寫入可識別的雇主、客戶或服務對象名稱。
P108: 3. 分開存放：若機構因報名或簽到而另有名冊，名冊與本表分開保管，不併入本表、不併入 0101、不放入同一資料夾。
P109: 4. 對照表：本示範稿不含任何代碼對照表。正式使用時若需對照，由單一窗口保管，設定存取權限，不隨報告流通，並在分析完成後依機構政策處理。
P110: 5. 紙本：收回後置於可上鎖空間；電子檔去識別化後僅保留代碼與分數。
P111: 6. 揭露：對外呈現僅用彙總數據；樣本數很小時不單獨呈現可辨識個人的分組。
P112: 7. 法律依據與保存期限：由使用機構依其適用規範自行確認；本文件不主張任何特定法規遵循狀態、不主張已完成告知同意程序、也不主張具有任何法定權限。
P113: 8. 當事人請求：由使用機構自訂窗口與流程；本示範稿不代為承諾任何處理時限。
P115: 8. 合成示範資料集（80 格）與驗算
P116: 8.1 完整矩陣（A01–A08，全部為 SAMPLE／SYNTHETIC）
P118: 表中前 A–E 與後 A–E 共 8 × 5 × 2 = 80 格，皆為原始自評值；「前總分」、「後總分」、「變化」為計算值，不計入 80 格。
P119: 8.2 精確合計與驗算
P121: 維度層級合計（交叉驗算用）
P123: 核對：維度前測合計 17 + 16 + 13 + 14 + 15 = 75，等於前測總分；維度後測合計 25 + 24 + 22 + 24 + 22 = 117，等於後測總分；117 − 75 = 42。八人變化 +7、+6、+3、+4、+6、+5、+5、+6 合計亦為 +42。
P124: 8.3 這組數值可以怎麼讀、不可以怎麼讀
P125: 可以：作為 0100 與 0101 之間的格式與計算示範，確認欄位對應、加總、平均、雷達圖軸向與分母揭露方式正確。
P126: 不可以：不可說這是真實訓練成果、不可說學員能力已被客觀驗證、不可說本表與 0099 技能評分一致或相關、不可引用 0099 的通過門檻、不可推論母體成效、不可作為招生或績效宣稱。
P128: 9. 與 0101 的交接
P129: 9.1 交接包內容（0101 只接收這些）
P131: 9.2 交接格式（欄位順序固定）
P132: 代碼, 前A, 前B, 前C, 前D, 前E, 前總分, 後A, 後B, 後C, 後D, 後E, 後總分, 變化
P133: 不得改名、不得重排、不得新增未經定義的欄位。若正式資料有 HOLD／REJECT 份數，須另附排除清單與原因。
P134: 9.3 0101 收到後應做與不得做
P135: 應做：重算每一列總分與變化、核對 80 格是否齊全、以同一 0–4 尺度繪製五維度前後雷達圖、標示 SAMPLE／SYNTHETIC、揭露 n = 8 與分母、保留限制說明。
P136: 不得做：修改或補值、刪除不利數值、把自評描述成技能證據、宣稱前後差異具統計顯著性或相關性、套用 0099 門檻、加入未經來源支持的人員或機構資訊。
P137: 9.4 文件層級交接
P138: 本 0100 完稿經審查後，連同版本、SHA 與本節交接包一併提供 0101 製作 DOCX 報告；0101 的產出不得回寫或改動本表數值。
P139: 10. 承辦人一頁式流程與常見錯誤
P140: 10.1 一頁式流程
P141: 1. 課前準備：印好前測表與後測表，版本同為 SR-0100-v1.0-SAMPLE，課程代碼預先印妥。
P142: 2. 開場說明（2 分鐘）：說明這是自評、沒有及格分數、不記名、需自選 4 碼代碼並記住。
P143: 3. 前測（8–12 分鐘）：學員自行填寫，承辦人不代填、不提示答案。
P144: 4. 收回檢查：當場確認五題各一格、分數 0–4、代碼已填。
P145: 5. 訓練進行：不改變題目、不中途追加題項。
P146: 6. 後測（8–12 分鐘）：提醒使用同一代碼與版本。
P147: 7. 配對與檢核：依第 6 節逐項檢查，登錄有效、保留、退件份數。
P148: 8. 交接 0101：依第 9 節格式交付，附限制註記。
P149: 10.2 常見錯誤
P150: 1. 前後測使用不同版本或不同題目文字。
P151: 2. 承辦人幫學員選代碼，導致無法確認是否同一人。
P152: 3. 學員在表上寫姓名或電話，增加辨識風險。
P153: 4. 缺漏時直接填 0 或填平均數。
P154: 5. 重複代碼未處理就全部計入。
P155: 6. 只報總分，未揭露有效樣本數與排除份數。
P156: 7. 把自評分數說成「能力已達標」或「訓練有效」。
P157: 8. 把本表數值與 0099 技能評分混用或宣稱一致。
P158: 9. 自行設定 60 分、80% 之類的通過門檻。
P159: 10. 在 0101 報告中改動 0100 的原始分數。
P160: 11. SAMPLE 替換登錄與版本限制
P161: 11.1 SAMPLE 替換登錄表（正式使用前必須逐項替換）
P163: 11.2 版本限制
P164: 1. 本稿為 SAMPLE／SYNTHETIC 候選工具，沒有真實填答、協會核准或正式接受聲明；獨立審查範圍與結論以候選 exact-SHA 外部收據為準，不得只依本文件狀態列推定通過。
P165: 2. 先前 1 人 × 6 維度之 R08 系列版本（含 0100 R08 與 0101 R08A／R08B／R08C）均為歷史檔，與現行 8 人 × 5 維度契約不一致，不得作為現行接受依據，亦不得作為本稿模板。
P166: 3. 0099 R17 之數值僅依現行契約作為合成示範重用，不改變其原需求（I18-E07）與原文件定位，亦不得修改或重新分類該文件。
P167: 4. 本表不提供、也不暗示任何自評通過標準；若機構日後自行訂定使用規則，應另立文件並明確標示其性質，不得回寫為本表之官方門檻。
T01R01: 項目 | 內容
T01R02: 文件名稱 | 學員訓練前後自我評量表（Learner Pre/Post Self-Assessment Form）
T01R03: DOC_ID | 0100
T01R04: 需求編號 | I18-E08
T01R05: 官方表單印刷序號 | UNKNOWN（未自原始表單讀取，不得推測或填寫）
T01R06: 對應文件 | 0100 本表；0101 自覺成長雷達分析報告
T01R07: 本稿版次 | R09a
T01R08: 文件性質 | SAMPLE／SYNTHETIC 示範稿，含可實際使用之空白表與 8 人合成示範資料
T01R09: 現況 | 尚未有真實學員填答、尚未經獨立審查與正式驗收
T02R01: 項目 | 建議作法
T02R02: 前測時間 | 約 8–12 分鐘（含說明）
T02R03: 後測時間 | 約 8–12 分鐘（含說明）
T02R04: 填答方式 | 紙本勾選或離線電子表單；不建議使用需輸入姓名之線上表單
T02R05: 題數 | 5 題，每題一個 0–4 分
T02R06: 必填 | 配對代碼、版本、階段、日期、5 個分數
T02R07: 選填 | 每題一句具體例子
T02R08: 分數範圍 | 每題 0–4；單一階段總分 0–20
T03R01: 欄位 | 示範值 | 說明
T03R02: 辦理單位 | SAMPLE 示範訓練機構 | 非真實機構
T03R03: 課程代碼 | SAMPLE-CRS-0100 | 由承辦人預先印妥
T03R04: 課程名稱 | SAMPLE「資料紀錄與隱私基礎示範課」 | 非真實課程
T03R05: 前測日期 | SAMPLE 2026-11-02 | 非真實日期
T03R06: 後測日期 | SAMPLE 2026-11-02（課後同日） | 非真實日期；後測不得早於前測
T03R07: 問卷版本 | SR-0100-v1.0-SAMPLE | 前後測必須相同
T03R08: 示範人數 | 8（A01–A08） | 合成資料
T03R09: 滿分 | 20（5 維度 × 4 分） | 僅供本表示範
T04R01: 維度 | 學員看到的題目 | 這個維度在問什麼 | 具體例子
T04R02: A 來源事實與情境 | 我能說清楚這份資料或任務的來源、目的與使用情境。 | 是否知道資料從哪裡來、為什麼要處理、要用在哪裡。 | 能說出這份資料是誰提供、為何收集、會用在哪個環節。
T04R03: B 紀錄完整性與可追溯 | 我能把該留下的欄位、版本、時間與來源留下來，讓別人可以追溯。 | 是否留下足以回溯的紀錄，而不是只靠記憶。 | 留下日期、版本、修改人與原始檔名，讓他人能回到源頭。
T04R04: C 任務與產出對應 | 我能把要求轉成具體產出，並確認產出真的對應要求。 | 是否能把交辦事項拆成可交付的成果並逐項核對。 | 把「整理一份名冊」拆成欄位、格式、完成時間，再逐項對回要求。
T04R05: D 資料最小化與隱私意識 | 我只收集與使用完成任務真正需要的資料，並知道誰可以看。 | 是否知道少收、少留、限制存取。 | 只留必要欄位，知道哪些資料不能放在公開雲端或群組。
T04R06: E 後續行動規劃 | 我能說出下一步、由誰負責、何時完成，以及如何確認做到。 | 是否能把所學轉成可執行的後續動作。 | 寫出下一步、負責人、完成時間與檢查方式。
T05R01: 分數 | 行為描述 | 白話提示
T05R02: 0 | 還無法描述或執行這一步。 | 完全不知道從何開始。
T05R03: 1 | 只能在他人一步一步帶領下開始。 | 需要有人帶著做。
T05R04: 2 | 看著範例或檢核表，可以完成其中一部分。 | 有範本才做得出部分內容。
T05R05: 3 | 可以自己完成一個典型任務。 | 一般情況可獨立完成。
T05R06: 4 | 可以解釋、檢查，並套用到新的例子。 | 能說明理由、找出錯誤、換情境也會做。
T06R01: 欄位 | 填寫內容
T06R02: 配對代碼（正式使用四位數字） | ＿＿＿＿
T06R03: 問卷版本 | SR-0100-v1.0-SAMPLE
T06R04: 階段 | 前測
T06R05: 填寫日期 | ＿＿＿＿ 年 ＿＿ 月 ＿＿ 日
T06R06: 課程代碼（承辦人預印） | SAMPLE-CRS-0100
T07R01: 題號 | 題目 | 0 | 1 | 2 | 3 | 4
T07R02: A | 我能說清楚這份資料或任務的來源、目的與使用情境。 | ☐ | ☐ | ☐ | ☐ | ☐
T07R03: B | 我能把該留下的欄位、版本、時間與來源留下來，讓別人可以追溯。 | ☐ | ☐ | ☐ | ☐ | ☐
T07R04: C | 我能把要求轉成具體產出，並確認產出真的對應要求。 | ☐ | ☐ | ☐ | ☐ | ☐
T07R05: D | 我只收集與使用完成任務真正需要的資料，並知道誰可以看。 | ☐ | ☐ | ☐ | ☐ | ☐
T07R06: E | 我能說出下一步、由誰負責、何時完成，以及如何確認做到。 | ☐ | ☐ | ☐ | ☐ | ☐
T08R01: 題號 | 一句具體經驗
T08R02: A | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T08R03: B | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T08R04: C | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T08R05: D | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T08R06: E | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T09R01: 欄位 | 填寫內容
T09R02: 配對代碼（正式使用四位數字，須與前測相同） | ＿＿＿＿
T09R03: 問卷版本 | SR-0100-v1.0-SAMPLE
T09R04: 階段 | 後測
T09R05: 填寫日期 | ＿＿＿＿ 年 ＿＿ 月 ＿＿ 日
T09R06: 課程代碼（承辦人預印） | SAMPLE-CRS-0100
T10R01: 題號 | 題目 | 0 | 1 | 2 | 3 | 4
T10R02: A | 我能說清楚這份資料或任務的來源、目的與使用情境。 | ☐ | ☐ | ☐ | ☐ | ☐
T10R03: B | 我能把該留下的欄位、版本、時間與來源留下來，讓別人可以追溯。 | ☐ | ☐ | ☐ | ☐ | ☐
T10R04: C | 我能把要求轉成具體產出，並確認產出真的對應要求。 | ☐ | ☐ | ☐ | ☐ | ☐
T10R05: D | 我只收集與使用完成任務真正需要的資料，並知道誰可以看。 | ☐ | ☐ | ☐ | ☐ | ☐
T10R06: E | 我能說出下一步、由誰負責、何時完成，以及如何確認做到。 | ☐ | ☐ | ☐ | ☐ | ☐
T11R01: 題號 | 一句具體經驗
T11R02: A | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T11R03: B | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T11R04: C | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T11R05: D | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T11R06: E | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T12R01: 情況 | 判定 | 處理方式
T12R02: 分數不在 0–4（例如 5、空白、塗改不清） | 無效 | 請本人重填該題；無法重填則整份 HOLD，不得以 0 代入
T12R03: 任一維度未勾選 | 缺漏 | 整份 HOLD，請本人補填；不得以平均數、前測值或 0 代入
T12R04: 同階段出現兩份以上相同代碼 | 重複／可能錯配 | 同代碼全部表單 HOLD；不可按完整度或分數擇一。須由各填答者本人在場確認並留下更正註記；不能確認時全部 REJECT，排除於有效分母
T12R05: 同一題勾選兩個以上分數 | 多選／無效 | 該份 HOLD，請本人重選一個；無法確認時該份 REJECT，不得由承辦人代選
T12R06: 前後測代碼不一致 | 無法配對 | 未經本人當場確認不得配對；確認後更正並留註記
T12R07: 問卷版本不一致 | 版本不符 | 該對 REJECT，不併入分析
T12R08: 後測日期早於前測 | 時序錯誤 | 該對 REJECT，查明後重填
T12R09: 代碼含姓名、電話、證件號 | 個資風險 | 立即更換代碼，舊表依第 7 節銷毀或遮蔽
T12R10: 承辦人代填或代改分數 | 程序違失 | 該份作廢，記錄原因
T12R11: 未揭露有效樣本數或分母 | 揭露不足 | 不得產出 0101 分析
T13R01: 代碼 | 前A | 前B | 前C | 前D | 前E | 前總分 | 後A | 後B | 後C | 後D | 後E | 後總分 | 變化
T13R02: A01 | 2 | 2 | 1 | 2 | 1 | 8 | 3 | 3 | 3 | 3 | 3 | 15 | +7
T13R03: A02 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 4 | 16 | +6
T13R04: A03 | 3 | 2 | 2 | 2 | 2 | 11 | 3 | 3 | 3 | 3 | 2 | 14 | +3
T13R05: A04 | 2 | 2 | 1 | 2 | 2 | 9 | 3 | 3 | 2 | 3 | 2 | 13 | +4
T13R06: A05 | 3 | 3 | 2 | 2 | 2 | 12 | 4 | 4 | 3 | 3 | 4 | 18 | +6
T13R07: A06 | 1 | 2 | 1 | 1 | 2 | 7 | 3 | 2 | 2 | 3 | 2 | 12 | +5
T13R08: A07 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 3 | 15 | +5
T13R09: A08 | 2 | 1 | 2 | 1 | 2 | 8 | 3 | 3 | 3 | 3 | 2 | 14 | +6
T14R01: 驗算項目 | 數值
T14R02: 原始分數格數 | 80
T14R03: 分數範圍檢查 | 全部介於 0–4
T14R04: 前測總分 | 75
T14R05: 後測總分 | 117
T14R06: 總變化 | +42
T14R07: 人數 n | 8
T14R08: 前測平均總分 | 9.375（滿分 20）
T14R09: 後測平均總分 | 14.625（滿分 20）
T14R10: 平均每人變化 | +5.25
T15R01: 維度 | 前測合計 | 前測平均 | 後測合計 | 後測平均 | 平均變化
T15R02: A 來源事實與情境 | 17 | 2.125 | 25 | 3.125 | +1.000
T15R03: B 紀錄完整性與可追溯 | 16 | 2.000 | 24 | 3.000 | +1.000
T15R04: C 任務與產出對應 | 13 | 1.625 | 22 | 2.750 | +1.125
T15R05: D 資料最小化與隱私意識 | 14 | 1.750 | 24 | 3.000 | +1.250
T15R06: E 後續行動規劃 | 15 | 1.875 | 22 | 2.750 | +0.875
T16R01: 交接項目 | 內容 | 狀態
T16R02: 表單版本 | SR-0100-v1.0-SAMPLE | 已確認
T16R03: 題目與錨點 | 第 3 節五維度、0–4 錨點 | 已確認
T16R04: 配對筆數 | 8 對（A01–A08） | 已確認
T16R05: 合成前／後測日期 | SAMPLE 2026-11-02／2026-11-02 | 僅供示範；不得當成實際施測紀錄
T16R06: 原始分數 | 80 格，見 8.1 | 已確認
T16R07: 階段總分 | 前 75、後 117、差 +42 | 已核算
T16R08: 有效／保留／退件 | 示範資料：8／0／0 | 已登錄
T16R09: 缺漏補值 | 無，未使用 0 或平均代入 | 已確認
T16R10: 來源文件 SHA-256 | 0100 最終 DOCX 凍結後，由 0101 從該檔實際位元組計算並記入 0101 的來源收據；本表不自我宣稱 SHA | 待 0101 收件時核對
T16R11: 隱私檢核 | 無個資欄位、無對照表 | 已確認
T16R12: 限制註記 | 自評、合成、不得宣稱相關或成效 | 已附
T17R01: 項目 | 目前示範值 | 正式使用前應替換為
T17R02: 辦理單位 | SAMPLE 示範訓練機構 | 實際辦理單位全名
T17R03: 課程代碼 | SAMPLE-CRS-0100 | 機構內部正式課程代碼
T17R04: 課程名稱 | SAMPLE「資料紀錄與隱私基礎示範課」 | 實際課程名稱
T17R05: 前測日期 | SAMPLE 2026-11-02 | 實際施測日期
T17R06: 後測日期 | SAMPLE 2026-11-02 | 實際施測日期
T17R07: 問卷版本 | SR-0100-v1.0-SAMPLE | 機構核定之版本號
T17R08: 配對代碼 | A01–A08 | 學員自選代碼
T17R09: 分數 | 80 格合成值 | 實際填答值
T17R10: 衍生統計 | 前 75、後 117、差 +42、每人平均變化 +5.25；A–E 平均變化 +1.000、+1.000、+1.125、+1.250、+0.875 | 由被替換後的原始分數與有效分母重新計算，不可沿用示範值
T17R11: 合成替換清冊 | synthetic_replacement_register_0100_R09.csv | SHA-256：889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8；替換原始分數後須重算所有總分、平均與維度統計
T17R12: 承辦人 | 未指定 | 實際承辦人
T17R13: 限制註記 | 已載明合成與自評性質 | 仍須保留，不得刪除


===== CURRENT_R09B_BODY SHA256=846bb5ab42b7a8c779eb76d3d3d4949ffae51c1d94a2686997218b88157e633a BYTES=26211 =====
P001: 0100 學員訓練前後自我評量表
P002: 版次 R09b｜SAMPLE／SYNTHETIC 示範稿｜需求編號 I18-E08｜DOC_ID 0100
P003: 目錄
P004: 1. 文件識別與使用聲明
P005: 2. 使用方式與樣本基本資料
P006: 3. 五個自評維度與 0–4 錨點
P007: 4. 前測填答頁（可複印使用）
P008: 5. 後測填答頁（可複印使用）
P009: 6. 收回檢核、缺漏處理與退件條件
P010: 7. 隱私與資料最小化
P011: 8. 合成示範資料集（80 格）與驗算
P012: 9. 與 0101 的交接
P013: 10. 承辦人一頁式流程與常見錯誤
P014: 11. SAMPLE 替換登錄與版本限制
P015: 1. 文件識別與使用聲明
P016: 1.1 文件識別
P018: 1.2 這份文件是什麼、不是什麼
P019: 本文件是一份學員自己填答的前測／後測自評工具，用來記錄學員在五個維度上「自覺能做到的程度」在訓練前後的變化，並把檢核完成的資料交給 0101 製作雷達分析報告。
P020: 本文件不是技能檢定或技能評分量表，不是滿意度調查，不是簽到表，不是訓練成果的客觀證明，也不是任何機構已辦理訓練的紀錄。
P021: 本表所附的 8 人資料（A01–A08）全部為 SAMPLE／SYNTHETIC：其中的課程名稱、課程代碼、日期、機構名稱、人員代碼與分數均為示範值，不代表任何真實機構、真實人員、真實參與、真實核准、真實簽署或真實訓練結果。本稿亦不主張任何協會核定、認證或背書。
P022: 1.3 數值來源與限制聲明（必讀）
P023: 1. 本表第 8 節的 8 人 × 5 維度 × 2 階段共 80 格原始分數，是依現行契約指示，自 0099 R17 共用同一組合成數值，僅作為跨文件一致性的合成示範 fixture。
P024: 2. 這組數值在 0099 是技能評分示範，在本文件則只是學員自評值。兩者不是同一種測量，不得據此宣稱自評等於技能評分，不得宣稱兩者一致、相關或可互相驗證，也不得視為獨立實證資料。
P025: 3. 本表不引用 0099 的技能評分通過門檻，也不另行設定自評通過門檻。0–4 錨點僅供本示範表使用，非協會核定、非信效度驗證之量表。
P026: 4. 本表呈現的是「自覺改變」（perceived change），不是客觀能力提升量。
P027: 2. 使用方式與樣本基本資料
P028: 2.1 適用對象與使用時機
P029: 填答者：接受同一場訓練活動的成人學員。
P030: 前測：訓練開始前填寫，用於建立自覺起點。
P031: 後測：同一場訓練結束時（或依機構規劃於訓練後短期內）填寫，題目、版本、配對代碼必須與前測完全相同。
P032: 施測者：由承辦人或指定人員統一發放、說明、收回與檢核，不代填、不誘導、不改分數。
P033: 2.2 施測時間與方式
P035: 2.3 樣本課程與填答基本資料（全部為 SAMPLE）
P037: 2.4 配對代碼規則
P038: 1. 正式施測時，每位學員自行選一組四位數字配對代碼（僅 0–9），前測與後測必須完全相同。本文件資料表中的 A01–A08 是三字元的 SAMPLE／SYNTHETIC 示範識別碼，僅供展示合成數據，不是正式施測代碼，也不得轉用為真實學員代碼。
P039: 2. 代碼不得包含姓名、生日、電話、學號、身分證號、電子郵件或任何可直接或間接識別個人的資訊。
P040: 3. 承辦人不代選、不代填、不代改；若學員忘記代碼，由本人憑記憶重填，不得由承辦人翻查找回後代為填寫。
P041: 4. 本示範稿不含任何代碼對照表；正式使用時若機構自行建立對照表，須依第 7 節分開保管，且不得隨本表或 0101 流通。
P042: 5. 同一階段出現兩份以上相同代碼時，該代碼的全部表單立即 HOLD；不得挑選分數較完整或日期較清楚的一份。只有各填答者本人在場確認並留下更正註記後才可解除；無法安全確認歸屬時，全部 REJECT 並排除於有效分母。
P043: 3. 五個自評維度與 0–4 錨點
P044: 3.1 五個維度（前後測題目完全相同）
P046: 3.2 0–4 自評錨點（僅適用本示範表）
P048: 填答提醒：請依「現在」的實際感受選一個分數，不必與他人比較，也不必猜標準答案。本表沒有及格分數，高分或低分都不影響任何權益；低分只代表可再強化的地方。
P049: 4. 前測填答頁（可複印使用）
P050: 4.1 填答說明
P051: 1. 本表共 5 題，每題請只勾選 一個 0–4 分。
P052: 2. 正式施測請自選一組四位數字（0–9）配對代碼，後測填同一組；A01–A08 僅是本文件的合成示範識別碼，不是正式代碼。
P053: 3. 每題下方的「例子」欄可空白，寫一句自己的經驗即可。
P054: 4. 填完請完成 4.4 的完整性檢查再交回。
P055: 影印／回收方式：前測完整表單共兩頁；基本欄位、自評題、例子與檢查頁須按頁序整組使用及回收，不拆頁。
P056: 4.2 基本欄位
P058: 4.3 五題自評
P059: 本頁量尺速查（完整行為錨點見第 3.2 節）：0＝還無法描述或執行；1＝需逐步帶領；2＝看範例或檢核表可完成一部分；3＝可獨立完成典型任務；4＝可解釋、檢查並套用到新例。
P061: 我的例子（可空白）
P063: 4.4 前測完整性檢查（交回前自行確認）
P064: ☐ 配對代碼為四位數字（0–9）；自由文字例子不含姓名、聯絡方式或任職單位／雇主／客戶／服務對象名稱；後測同碼同版。
P065: ☐ 五題都各只勾選一個分數；任何漏選或多選均先 HOLD，不自行補值
P066: ☐ 所有分數都在 0–4 之間
P067: ☐ 版本為 SR-0100-v1.0-SAMPLE
P068: ☐ 日期已填
P069: 5. 後測填答頁（可複印使用）
P070: 5.1 填答說明
P071: 1. 題目與前測完全相同，請依「現在」的感受重新評一次，不需要刻意與前測分數比較。
P072: 2. 請填入與前測完全相同的四位數字配對代碼與版本。A01–A08 是本文件合成資料識別碼，並非正式填答代碼。
P073: 3. 每題只勾一個 0–4 分；漏選或多選先 HOLD，請本人更正，例子欄可空白。
P074: 影印／回收方式：後測完整表單共兩頁；基本欄位、自評題、例子與檢查頁須按頁序整組使用及回收，不拆頁。
P075: 5.2 基本欄位
P077: 5.3 五題自評
P078: 本頁量尺速查（完整行為錨點見第 3.2 節）：0＝還無法描述或執行；1＝需逐步帶領；2＝看範例或檢核表可完成一部分；3＝可獨立完成典型任務；4＝可解釋、檢查並套用到新例。
P080: 我的例子（可空白）
P082: 5.4 後測完整性檢查（交回前自行確認）
P083: ☐ 配對代碼與前測完全相同
P084: ☐ 版本與前測相同（SR-0100-v1.0-SAMPLE）
P085: ☐ 五題各只勾選一個分數且在 0–4 之間；漏選或多選均先 HOLD，不由承辦人代選
P086: ☐ 後測日期不早於前測日期
P087: ☐ 未書寫姓名、聯絡方式、任職單位全名、雇主／客戶／服務對象名稱等可識別資訊
P088: 6. 收回檢核、缺漏處理與退件條件
P089: 6.1 收回檢核步驟（承辦人）
P090: 1. 當場確認每人前、後測各一份，並核對代碼是否相同。
P091: 2. 逐份檢查五題是否各只有一個勾選、是否落在 0–4；漏選或多選均先 HOLD，請本人補正，不可自行選值。
P092: 3. 檢查版本欄是否一致；不一致者先隔離，不併入資料。
P093: 4. 檢查日期先後；後測早於前測者退件。
P094: 5. 檢查代碼與自由文字例子是否含姓名、電話、地址、任職單位全名、雇主／客戶／服務對象名稱等可識別資訊；如有，先 HOLD，安全遮蔽或請本人重填，並依第 7 節處置舊表。
P095: 6. 依配對代碼排序，重複代碼立即抽出，依 6.2 處理。
P096: 7. 登錄「收回份數、有效份數、保留份數、退件份數」，並記錄原因。
P097: 8. 只有在全部檢核完成後，才把資料交給 0101。
P098: 6.2 缺漏、重複與不一致的處理
P100: 6.3 退件與保留彙總清單
P101: HOLD（可補正後再用）：單題漏選或多選、字跡不清、代碼疑似打錯、日期未填、重複代碼待本人確認。重複代碼的全部相關表單一律先 HOLD，不得先選一份計分。
P102: REJECT（不得補正，直接排除）：版本不符、後測早於前測、承辦人代填、拒絕更正之個資欄位、本人無法確認歸屬的重複代碼或無法安全確認的配對。
P103: 必要原則：任何缺漏都不得補值；排除份數與原因必須與有效份數一起揭露，分母不得隱藏。
P104: 7. 隱私與資料最小化
P105: 1. 不收集：姓名、電話、地址、生日、身分證號、學號、簽名、照片、任職單位全名、雇主／客戶／服務對象名稱。
P106: 2. 只收集：四位數字配對代碼、版本、階段、日期、5 個 0–4 分數、可選的一句例子；例子不得寫入可識別的雇主、客戶或服務對象名稱。
P107: 3. 分開存放：若機構因報名或簽到而另有名冊，名冊與本表分開保管，不併入本表、不併入 0101、不放入同一資料夾。
P108: 4. 對照表：本示範稿不含任何代碼對照表。正式使用時若需對照，由單一窗口保管，設定存取權限，不隨報告流通，並在分析完成後依機構政策處理。
P109: 5. 紙本：收回後置於可上鎖空間；電子檔去識別化後僅保留代碼與分數。
P110: 6. 揭露：對外呈現僅用彙總數據；樣本數很小時不單獨呈現可辨識個人的分組。
P111: 7. 法律依據與保存期限：由使用機構依其適用規範自行確認；本文件不主張任何特定法規遵循狀態、不主張已完成告知同意程序、也不主張具有任何法定權限。
P112: 8. 當事人請求：由使用機構自訂窗口與流程；本示範稿不代為承諾任何處理時限。
P114: 8. 合成示範資料集（80 格）與驗算
P115: 8.1 完整矩陣（A01–A08，全部為 SAMPLE／SYNTHETIC）
P117: 表中前 A–E 與後 A–E 共 8 × 5 × 2 = 80 格，皆為原始自評值；「前總分」、「後總分」、「變化」為計算值，不計入 80 格。
P118: 8.2 精確合計與驗算
P120: 維度層級合計（交叉驗算用）
P122: 核對：維度前測合計 17 + 16 + 13 + 14 + 15 = 75，等於前測總分；維度後測合計 25 + 24 + 22 + 24 + 22 = 117，等於後測總分；117 − 75 = 42。八人變化 +7、+6、+3、+4、+6、+5、+5、+6 合計亦為 +42。
P123: 8.3 這組數值可以怎麼讀、不可以怎麼讀
P124: 可以：作為 0100 與 0101 之間的格式與計算示範，確認欄位對應、加總、平均、雷達圖軸向與分母揭露方式正確。
P125: 不可以：不可說這是真實訓練成果、不可說學員能力已被客觀驗證、不可說本表與 0099 技能評分一致或相關、不可引用 0099 的通過門檻、不可推論母體成效、不可作為招生或績效宣稱。
P127: 9. 與 0101 的交接
P128: 9.1 交接包內容（0101 只接收這些）
P130: 9.2 交接格式（欄位順序固定）
P131: 代碼,前A,前B,前C,前D,前E,前總分,後A,後B,後C,後D,後E,後總分,變化
P132: 不得改名、不得重排、不得新增未經定義的欄位。若正式資料有 HOLD／REJECT 份數，須另附排除清單與原因。
P133: 9.3 0101 收到後應做與不得做
P134: 應做：重算每一列總分與變化、核對 80 格是否齊全、以同一 0–4 尺度繪製五維度前後雷達圖、標示 SAMPLE／SYNTHETIC、揭露 n = 8 與分母、保留限制說明。
P135: 不得做：修改或補值、刪除不利數值、把自評描述成技能證據、宣稱前後差異具統計顯著性或相關性、套用 0099 門檻、加入未經來源支持的人員或機構資訊。
P136: 9.4 文件層級交接
P137: 本 0100 完稿經審查後，連同版本、SHA 與本節交接包一併提供 0101 製作 DOCX 報告；0101 的產出不得回寫或改動本表數值。
P138: 10. 承辦人一頁式流程與常見錯誤
P139: 10.1 一頁式流程
P140: 1. 課前準備：印好前測表與後測表，版本同為 SR-0100-v1.0-SAMPLE，課程代碼預先印妥。
P141: 2. 開場說明（2 分鐘）：說明這是自評、沒有及格分數、不記名、需自選四位數字配對代碼並記住。
P142: 3. 前測（8–12 分鐘）：學員自行填寫，承辦人不代填、不提示答案。
P143: 4. 收回檢查：當場確認五題各一格、分數 0–4、代碼已填。
P144: 5. 訓練進行：不改變題目、不中途追加題項。
P145: 6. 後測（8–12 分鐘）：提醒使用同一代碼與版本。
P146: 7. 配對與檢核：依第 6 節逐項檢查，登錄有效、保留、退件份數。
P147: 8. 交接 0101：依第 9 節格式交付，附限制註記。
P148: 10.2 常見錯誤
P149: 1. 前後測使用不同版本或不同題目文字。
P150: 2. 承辦人幫學員選代碼，導致無法確認是否同一人。
P151: 3. 學員在表上寫姓名或電話，增加辨識風險。
P152: 4. 缺漏時直接填 0 或填平均數。
P153: 5. 重複代碼未處理就全部計入。
P154: 6. 只報總分，未揭露有效樣本數與排除份數。
P155: 7. 把自評分數說成「能力已達標」或「訓練有效」。
P156: 8. 把本表數值與 0099 技能評分混用或宣稱一致。
P157: 9. 自行設定 60 分、80% 之類的通過門檻。
P158: 10. 在 0101 報告中改動 0100 的原始分數。
P159: 11. SAMPLE 替換登錄與版本限制
P160: 11.1 SAMPLE 替換登錄表（正式使用前必須逐項替換）
P162: 11.2 版本限制
P163: 1. 本稿為 SAMPLE／SYNTHETIC 候選工具，沒有真實填答、協會核准或正式接受聲明；獨立審查範圍與結論以候選 exact-SHA 外部收據為準，不得只依本文件狀態列推定通過。
P164: 2. 先前 1 人 × 6 維度之 R08 系列版本（含 0100 R08 與 0101 R08A／R08B／R08C）均為歷史檔，與現行 8 人 × 5 維度契約不一致，不得作為現行接受依據，亦不得作為本稿模板。
P165: 3. 0099 R17 之數值僅依現行契約作為合成示範重用，不改變其原需求（I18-E07）與原文件定位，亦不得修改或重新分類該文件。
P166: 4. 本表不提供、也不暗示任何自評通過標準；若機構日後自行訂定使用規則，應另立文件並明確標示其性質，不得回寫為本表之官方門檻。
T01R01: 項目 | 內容
T01R02: 文件名稱 | 學員訓練前後自我評量表（Learner Pre/Post Self-Assessment Form）
T01R03: DOC_ID | 0100
T01R04: 需求編號 | I18-E08
T01R05: 官方表單印刷序號 | UNKNOWN（未自原始表單讀取，不得推測或填寫）
T01R06: 對應文件 | 0100 本表；0101 自覺成長雷達分析報告
T01R07: 本稿版次 | R09b（由 R09a 定點修補）
T01R08: 文件性質 | SAMPLE／SYNTHETIC 示範稿，含可實際使用之空白表與 8 人合成示範資料
T01R09: 現況 | 無真實學員填答；R09a 舊 SHA 語意審查 PASS。本 R09b 為局部修補候選，待本版 delta 複核；正式驗收 NOT_GRANTED。
T02R01: 項目 | 建議作法
T02R02: 前測時間 | 約 8–12 分鐘（含說明）
T02R03: 後測時間 | 約 8–12 分鐘（含說明）
T02R04: 填答方式 | 紙本勾選或離線電子表單；不建議使用需輸入姓名之線上表單
T02R05: 題數 | 5 題，每題一個 0–4 分
T02R06: 必填 | 配對代碼、版本、階段、日期、5 個分數
T02R07: 選填 | 每題一句具體例子
T02R08: 分數範圍 | 每題 0–4；單一階段總分 0–20
T03R01: 欄位 | 示範值 | 說明
T03R02: 辦理單位 | SAMPLE 示範訓練機構 | 非真實機構
T03R03: 課程代碼 | SAMPLE-CRS-0100 | 由承辦人預先印妥
T03R04: 課程名稱 | SAMPLE「資料紀錄與隱私基礎示範課」 | 非真實課程
T03R05: 前測日期 | SAMPLE 2026-11-02 | 非真實日期
T03R06: 後測日期 | SAMPLE 2026-11-02（課後同日） | 非真實日期；後測不得早於前測
T03R07: 問卷版本 | SR-0100-v1.0-SAMPLE | 前後測必須相同
T03R08: 示範人數 | 8（A01–A08） | 合成資料
T03R09: 滿分 | 20（5 維度 × 4 分） | 僅供本表示範
T04R01: 維度 | 學員看到的題目 | 這個維度在問什麼 | 具體例子
T04R02: A 來源事實與情境 | 我能說清楚這份資料或任務的來源、目的與使用情境。 | 是否知道資料從哪裡來、為什麼要處理、要用在哪裡。 | 能說出這份資料是誰提供、為何收集、會用在哪個環節。
T04R03: B 紀錄完整性與可追溯 | 我能把該留下的欄位、版本、時間與來源留下來，讓別人可以追溯。 | 是否留下足以回溯的紀錄，而不是只靠記憶。 | 留下日期、版本、修改人與原始檔名，讓他人能回到源頭。
T04R04: C 任務與產出對應 | 我能把要求轉成具體產出，並確認產出真的對應要求。 | 是否能把交辦事項拆成可交付的成果並逐項核對。 | 把「整理一份名冊」拆成欄位、格式、完成時間，再逐項對回要求。
T04R05: D 資料最小化與隱私意識 | 我只收集與使用完成任務真正需要的資料，並知道誰可以看。 | 是否知道少收、少留、限制存取。 | 只留必要欄位，知道哪些資料不能放在公開雲端或群組。
T04R06: E 後續行動規劃 | 我能說出下一步、由誰負責、何時完成，以及如何確認做到。 | 是否能把所學轉成可執行的後續動作。 | 寫出下一步、負責人、完成時間與檢查方式。
T05R01: 分數 | 行為描述 | 白話提示
T05R02: 0 | 還無法描述或執行這一步。 | 完全不知道從何開始。
T05R03: 1 | 只能在他人一步一步帶領下開始。 | 需要有人帶著做。
T05R04: 2 | 看著範例或檢核表，可以完成其中一部分。 | 有範本才做得出部分內容。
T05R05: 3 | 可以自己完成一個典型任務。 | 一般情況可獨立完成。
T05R06: 4 | 可以解釋、檢查，並套用到新的例子。 | 能說明理由、找出錯誤、換情境也會做。
T06R01: 欄位 | 填寫內容
T06R02: 配對代碼（正式使用四位數字） | ＿＿＿＿
T06R03: 問卷版本 | SR-0100-v1.0-SAMPLE
T06R04: 階段 | 前測
T06R05: 填寫日期 | ＿＿＿＿ 年 ＿＿ 月 ＿＿ 日
T06R06: 課程代碼（承辦人預印） | SAMPLE-CRS-0100
T07R01: 題號 | 題目 | 0 | 1 | 2 | 3 | 4
T07R02: A | 我能說清楚這份資料或任務的來源、目的與使用情境。 | ☐ | ☐ | ☐ | ☐ | ☐
T07R03: B | 我能把該留下的欄位、版本、時間與來源留下來，讓別人可以追溯。 | ☐ | ☐ | ☐ | ☐ | ☐
T07R04: C | 我能把要求轉成具體產出，並確認產出真的對應要求。 | ☐ | ☐ | ☐ | ☐ | ☐
T07R05: D | 我只收集與使用完成任務真正需要的資料，並知道誰可以看。 | ☐ | ☐ | ☐ | ☐ | ☐
T07R06: E | 我能說出下一步、由誰負責、何時完成，以及如何確認做到。 | ☐ | ☐ | ☐ | ☐ | ☐
T08R01: 題號 | 一句具體經驗
T08R02: A | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T08R03: B | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T08R04: C | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T08R05: D | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T08R06: E | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T09R01: 欄位 | 填寫內容
T09R02: 配對代碼（正式使用四位數字，須與前測相同） | ＿＿＿＿
T09R03: 問卷版本 | SR-0100-v1.0-SAMPLE
T09R04: 階段 | 後測
T09R05: 填寫日期 | ＿＿＿＿ 年 ＿＿ 月 ＿＿ 日
T09R06: 課程代碼（承辦人預印） | SAMPLE-CRS-0100
T10R01: 題號 | 題目 | 0 | 1 | 2 | 3 | 4
T10R02: A | 我能說清楚這份資料或任務的來源、目的與使用情境。 | ☐ | ☐ | ☐ | ☐ | ☐
T10R03: B | 我能把該留下的欄位、版本、時間與來源留下來，讓別人可以追溯。 | ☐ | ☐ | ☐ | ☐ | ☐
T10R04: C | 我能把要求轉成具體產出，並確認產出真的對應要求。 | ☐ | ☐ | ☐ | ☐ | ☐
T10R05: D | 我只收集與使用完成任務真正需要的資料，並知道誰可以看。 | ☐ | ☐ | ☐ | ☐ | ☐
T10R06: E | 我能說出下一步、由誰負責、何時完成，以及如何確認做到。 | ☐ | ☐ | ☐ | ☐ | ☐
T11R01: 題號 | 一句具體經驗
T11R02: A | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T11R03: B | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T11R04: C | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T11R05: D | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T11R06: E | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
T12R01: 情況 | 判定 | 處理方式
T12R02: 分數超出 0–4（例如 5、6、負數）或塗改不清 | 無效 | 請本人重填該題；無法重填則整份 HOLD，不得以 0 代入
T12R03: 任一維度未勾選（空白） | 缺漏 | 整份 HOLD，請本人補填；不得以平均數、前測值或 0 代入
T12R04: 同階段出現兩份以上相同代碼 | 重複／可能錯配 | 同代碼全部表單 HOLD；不可按完整度或分數擇一。須由各填答者本人在場確認並留下更正註記；不能確認時全部 REJECT，排除於有效分母
T12R05: 同一題勾選兩個以上分數 | 多選／無效 | 該份 HOLD，請本人重選一個；無法確認時該份 REJECT，不得由承辦人代選
T12R06: 前後測各一份同碼，未確認為同一人 | 身分配對未證實 | 先 HOLD；由本人確認為同一人並核對同版本、日期順序，留下核對註記後才可配對；未能確認或發現他人同碼碰撞時兩表 REJECT，排除有效分母。不得只因代碼相同就推定同一人。
T12R07: 前後測代碼不一致 | 無法配對 | 未經本人當場確認不得配對；確認後更正並留註記
T12R08: 問卷版本不一致 | 版本不符 | 該對 REJECT，不併入分析
T12R09: 後測日期早於前測 | 時序錯誤 | 該對 REJECT，查明後重填
T12R10: 代碼含姓名、電話、證件號 | 個資風險 | 立即更換代碼，舊表依第 7 節銷毀或遮蔽
T12R11: 承辦人代填或代改分數 | 程序違失 | 該份作廢，記錄原因
T12R12: 未揭露有效樣本數或分母 | 揭露不足 | 不得產出 0101 分析
T13R01: 代碼 | 前A | 前B | 前C | 前D | 前E | 前總分 | 後A | 後B | 後C | 後D | 後E | 後總分 | 變化
T13R02: A01 | 2 | 2 | 1 | 2 | 1 | 8 | 3 | 3 | 3 | 3 | 3 | 15 | +7
T13R03: A02 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 4 | 16 | +6
T13R04: A03 | 3 | 2 | 2 | 2 | 2 | 11 | 3 | 3 | 3 | 3 | 2 | 14 | +3
T13R05: A04 | 2 | 2 | 1 | 2 | 2 | 9 | 3 | 3 | 2 | 3 | 2 | 13 | +4
T13R06: A05 | 3 | 3 | 2 | 2 | 2 | 12 | 4 | 4 | 3 | 3 | 4 | 18 | +6
T13R07: A06 | 1 | 2 | 1 | 1 | 2 | 7 | 3 | 2 | 2 | 3 | 2 | 12 | +5
T13R08: A07 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 3 | 15 | +5
T13R09: A08 | 2 | 1 | 2 | 1 | 2 | 8 | 3 | 3 | 3 | 3 | 2 | 14 | +6
T14R01: 驗算項目 | 數值
T14R02: 原始分數格數 | 80
T14R03: 分數範圍檢查 | 全部介於 0–4
T14R04: 前測總分 | 75
T14R05: 後測總分 | 117
T14R06: 總變化 | +42
T14R07: 人數 n | 8
T14R08: 前測平均總分 | 9.375（滿分 20）
T14R09: 後測平均總分 | 14.625（滿分 20）
T14R10: 平均每人變化 | +5.25
T15R01: 維度 | 前測合計 | 前測平均 | 後測合計 | 後測平均 | 平均變化
T15R02: A 來源事實與情境 | 17 | 2.125 | 25 | 3.125 | +1.000
T15R03: B 紀錄完整性與可追溯 | 16 | 2.000 | 24 | 3.000 | +1.000
T15R04: C 任務與產出對應 | 13 | 1.625 | 22 | 2.750 | +1.125
T15R05: D 資料最小化與隱私意識 | 14 | 1.750 | 24 | 3.000 | +1.250
T15R06: E 後續行動規劃 | 15 | 1.875 | 22 | 2.750 | +0.875
T16R01: 交接項目 | 內容 | 狀態
T16R02: 表單版本 | SR-0100-v1.0-SAMPLE | 已確認
T16R03: 題目與錨點 | 第 3 節五維度、0–4 錨點 | 已確認
T16R04: 配對筆數 | 8 對（A01–A08） | 已確認
T16R05: 合成前／後測日期 | SAMPLE 2026-11-02／2026-11-02 | 僅供示範；不得當成實際施測紀錄
T16R06: 原始分數 | 80 格，見 8.1 | 已確認
T16R07: 階段總分 | 前 75、後 117、差 +42 | 已核算
T16R08: 有效／保留／退件 | 示範資料：8／0／0 | 已登錄
T16R09: 缺漏補值 | 無，未使用 0 或平均代入 | 已確認
T16R10: 來源文件 SHA-256 | 0100 最終 DOCX 凍結後，由 0101 從該檔實際位元組計算並記入 0101 的來源收據；本表不自我宣稱 SHA | 待 0101 收件時核對
T16R11: 隱私檢核 | 無個資欄位、無對照表 | 已確認
T16R12: 限制註記 | 自評、合成、不得宣稱相關或成效 | 已附
T17R01: 項目 | 目前示範值 | 正式使用前應替換為
T17R02: 辦理單位 | SAMPLE 示範訓練機構 | 實際辦理單位全名
T17R03: 課程代碼 | SAMPLE-CRS-0100 | 機構內部正式課程代碼
T17R04: 課程名稱 | SAMPLE「資料紀錄與隱私基礎示範課」 | 實際課程名稱
T17R05: 前測日期 | SAMPLE 2026-11-02 | 實際施測日期
T17R06: 後測日期 | SAMPLE 2026-11-02 | 實際施測日期
T17R07: 問卷版本 | SR-0100-v1.0-SAMPLE | 機構核定之版本號
T17R08: 配對代碼 | A01–A08 | 學員自選代碼
T17R09: 分數 | 80 格合成值 | 實際填答值
T17R10: 衍生統計 | 前 75、後 117、差 +42、每人平均變化 +5.25；A–E 平均變化 +1.000、+1.000、+1.125、+1.250、+0.875 | 由被替換後的原始分數與有效分母重新計算，不可沿用示範值
T17R11: 合成替換清冊 | synthetic_replacement_register_0100_R09.csv（沿用未改動的 R09 清冊） | SHA-256：889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8；替換原始分數後須重算所有總分、平均與維度統計
T17R12: 承辦人 | 未指定 | 實際承辦人
T17R13: 限制註記 | 已載明合成與自評性質 | 仍須保留，不得刪除


===== R09A_TO_R09B_DIFF SHA256=577715eddb33ae02889a5fab2de959333ffc44f6eede1fd57cf8ffc1463f07c0 BYTES=23862 =====
--- R09a (previously reviewed exact SHA)
+++ R09b (current exact SHA)
@@ -1,5 +1,5 @@
 P001: 0100 學員訓練前後自我評量表
-P002: 版次 R09a｜SAMPLE／SYNTHETIC 示範稿｜需求編號 I18-E08｜DOC_ID 0100
+P002: 版次 R09b｜SAMPLE／SYNTHETIC 示範稿｜需求編號 I18-E08｜DOC_ID 0100
 P003: 目錄
 P004: 1. 文件識別與使用聲明
 P005: 2. 使用方式與樣本基本資料
@@ -53,108 +53,107 @@
 P059: 本頁量尺速查（完整行為錨點見第 3.2 節）：0＝還無法描述或執行；1＝需逐步帶領；2＝看範例或檢核表可完成一部分；3＝可獨立完成典型任務；4＝可解釋、檢查並套用到新例。
 P061: 我的例子（可空白）
 P063: 4.4 前測完整性檢查（交回前自行確認）
-P064: ☐ 正式填答代碼為四位數字，且不含姓名、生日、電話或證件號碼
+P064: ☐ 配對代碼為四位數字（0–9）；自由文字例子不含姓名、聯絡方式或任職單位／雇主／客戶／服務對象名稱；後測同碼同版。
 P065: ☐ 五題都各只勾選一個分數；任何漏選或多選均先 HOLD，不自行補值
 P066: ☐ 所有分數都在 0–4 之間
 P067: ☐ 版本為 SR-0100-v1.0-SAMPLE
 P068: ☐ 日期已填
-P069: ☐ 我記得後測要使用同一組配對代碼與同一版本
-P070: 5. 後測填答頁（可複印使用）
-P071: 5.1 填答說明
-P072: 1. 題目與前測完全相同，請依「現在」的感受重新評一次，不需要刻意與前測分數比較。
-P073: 2. 請填入與前測完全相同的四位數字配對代碼與版本。A01–A08 是本文件合成資料識別碼，並非正式填答代碼。
-P074: 3. 每題只勾一個 0–4 分；漏選或多選先 HOLD，請本人更正，例子欄可空白。
-P075: 影印／回收方式：後測完整表單共兩頁；基本欄位、自評題、例子與檢查頁須按頁序整組使用及回收，不拆頁。
-P076: 5.2 基本欄位
-P078: 5.3 五題自評
-P079: 本頁量尺速查（完整行為錨點見第 3.2 節）：0＝還無法描述或執行；1＝需逐步帶領；2＝看範例或檢核表可完成一部分；3＝可獨立完成典型任務；4＝可解釋、檢查並套用到新例。
-P081: 我的例子（可空白）
-P083: 5.4 後測完整性檢查（交回前自行確認）
-P084: ☐ 配對代碼與前測完全相同
-P085: ☐ 版本與前測相同（SR-0100-v1.0-SAMPLE）
-P086: ☐ 五題各只勾選一個分數且在 0–4 之間；漏選或多選均先 HOLD，不由承辦人代選
-P087: ☐ 後測日期不早於前測日期
-P088: ☐ 未在表上書寫姓名或聯絡方式
-P089: 6. 收回檢核、缺漏處理與退件條件
-P090: 6.1 收回檢核步驟（承辦人）
-P091: 1. 當場確認每人前、後測各一份，並核對代碼是否相同。
-P092: 2. 逐份檢查五題是否各只有一個勾選、是否落在 0–4；漏選或多選均先 HOLD，請本人補正，不可自行選值。
-P093: 3. 檢查版本欄是否一致；不一致者先隔離，不併入資料。
-P094: 4. 檢查日期先後；後測早於前測者退件。
-P095: 5. 檢查是否有學員自行寫上姓名、電話等個資；如有，當場遮蔽或請本人重填於新表。
-P096: 6. 依配對代碼排序，重複代碼立即抽出，依 6.2 處理。
-P097: 7. 登錄「收回份數、有效份數、保留份數、退件份數」，並記錄原因。
-P098: 8. 只有在全部檢核完成後，才把資料交給 0101。
-P099: 6.2 缺漏、重複與不一致的處理
-P101: 6.3 退件與保留彙總清單
-P102: HOLD（可補正後再用）：單題漏選或多選、字跡不清、代碼疑似打錯、日期未填、重複代碼待本人確認。重複代碼的全部相關表單一律先 HOLD，不得先選一份計分。
-P103: REJECT（不得補正，直接排除）：版本不符、後測早於前測、承辦人代填、拒絕更正之個資欄位、本人無法確認歸屬的重複代碼或無法安全確認的配對。
-P104: 必要原則：任何缺漏都不得補值；排除份數與原因必須與有效份數一起揭露，分母不得隱藏。
-P105: 7. 隱私與資料最小化
-P106: 1. 不收集：姓名、電話、地址、生日、身分證號、學號、簽名、照片、任職單位全名、雇主／客戶／服務對象名稱。
-P107: 2. 只收集：四位數字配對代碼、版本、階段、日期、5 個 0–4 分數、可選的一句例子；例子不得寫入可識別的雇主、客戶或服務對象名稱。
-P108: 3. 分開存放：若機構因報名或簽到而另有名冊，名冊與本表分開保管，不併入本表、不併入 0101、不放入同一資料夾。
-P109: 4. 對照表：本示範稿不含任何代碼對照表。正式使用時若需對照，由單一窗口保管，設定存取權限，不隨報告流通，並在分析完成後依機構政策處理。
-P110: 5. 紙本：收回後置於可上鎖空間；電子檔去識別化後僅保留代碼與分數。
-P111: 6. 揭露：對外呈現僅用彙總數據；樣本數很小時不單獨呈現可辨識個人的分組。
-P112: 7. 法律依據與保存期限：由使用機構依其適用規範自行確認；本文件不主張任何特定法規遵循狀態、不主張已完成告知同意程序、也不主張具有任何法定權限。
-P113: 8. 當事人請求：由使用機構自訂窗口與流程；本示範稿不代為承諾任何處理時限。
-P115: 8. 合成示範資料集（80 格）與驗算
-P116: 8.1 完整矩陣（A01–A08，全部為 SAMPLE／SYNTHETIC）
-P118: 表中前 A–E 與後 A–E 共 8 × 5 × 2 = 80 格，皆為原始自評值；「前總分」、「後總分」、「變化」為計算值，不計入 80 格。
-P119: 8.2 精確合計與驗算
-P121: 維度層級合計（交叉驗算用）
-P123: 核對：維度前測合計 17 + 16 + 13 + 14 + 15 = 75，等於前測總分；維度後測合計 25 + 24 + 22 + 24 + 22 = 117，等於後測總分；117 − 75 = 42。八人變化 +7、+6、+3、+4、+6、+5、+5、+6 合計亦為 +42。
-P124: 8.3 這組數值可以怎麼讀、不可以怎麼讀
-P125: 可以：作為 0100 與 0101 之間的格式與計算示範，確認欄位對應、加總、平均、雷達圖軸向與分母揭露方式正確。
-P126: 不可以：不可說這是真實訓練成果、不可說學員能力已被客觀驗證、不可說本表與 0099 技能評分一致或相關、不可引用 0099 的通過門檻、不可推論母體成效、不可作為招生或績效宣稱。
-P128: 9. 與 0101 的交接
-P129: 9.1 交接包內容（0101 只接收這些）
-P131: 9.2 交接格式（欄位順序固定）
-P132: 代碼, 前A, 前B, 前C, 前D, 前E, 前總分, 後A, 後B, 後C, 後D, 後E, 後總分, 變化
-P133: 不得改名、不得重排、不得新增未經定義的欄位。若正式資料有 HOLD／REJECT 份數，須另附排除清單與原因。
-P134: 9.3 0101 收到後應做與不得做
-P135: 應做：重算每一列總分與變化、核對 80 格是否齊全、以同一 0–4 尺度繪製五維度前後雷達圖、標示 SAMPLE／SYNTHETIC、揭露 n = 8 與分母、保留限制說明。
-P136: 不得做：修改或補值、刪除不利數值、把自評描述成技能證據、宣稱前後差異具統計顯著性或相關性、套用 0099 門檻、加入未經來源支持的人員或機構資訊。
-P137: 9.4 文件層級交接
-P138: 本 0100 完稿經審查後，連同版本、SHA 與本節交接包一併提供 0101 製作 DOCX 報告；0101 的產出不得回寫或改動本表數值。
-P139: 10. 承辦人一頁式流程與常見錯誤
-P140: 10.1 一頁式流程
-P141: 1. 課前準備：印好前測表與後測表，版本同為 SR-0100-v1.0-SAMPLE，課程代碼預先印妥。
-P142: 2. 開場說明（2 分鐘）：說明這是自評、沒有及格分數、不記名、需自選 4 碼代碼並記住。
-P143: 3. 前測（8–12 分鐘）：學員自行填寫，承辦人不代填、不提示答案。
-P144: 4. 收回檢查：當場確認五題各一格、分數 0–4、代碼已填。
-P145: 5. 訓練進行：不改變題目、不中途追加題項。
-P146: 6. 後測（8–12 分鐘）：提醒使用同一代碼與版本。
-P147: 7. 配對與檢核：依第 6 節逐項檢查，登錄有效、保留、退件份數。
-P148: 8. 交接 0101：依第 9 節格式交付，附限制註記。
-P149: 10.2 常見錯誤
-P150: 1. 前後測使用不同版本或不同題目文字。
-P151: 2. 承辦人幫學員選代碼，導致無法確認是否同一人。
-P152: 3. 學員在表上寫姓名或電話，增加辨識風險。
-P153: 4. 缺漏時直接填 0 或填平均數。
-P154: 5. 重複代碼未處理就全部計入。
-P155: 6. 只報總分，未揭露有效樣本數與排除份數。
-P156: 7. 把自評分數說成「能力已達標」或「訓練有效」。
-P157: 8. 把本表數值與 0099 技能評分混用或宣稱一致。
-P158: 9. 自行設定 60 分、80% 之類的通過門檻。
-P159: 10. 在 0101 報告中改動 0100 的原始分數。
-P160: 11. SAMPLE 替換登錄與版本限制
-P161: 11.1 SAMPLE 替換登錄表（正式使用前必須逐項替換）
-P163: 11.2 版本限制
-P164: 1. 本稿為 SAMPLE／SYNTHETIC 候選工具，沒有真實填答、協會核准或正式接受聲明；獨立審查範圍與結論以候選 exact-SHA 外部收據為準，不得只依本文件狀態列推定通過。
-P165: 2. 先前 1 人 × 6 維度之 R08 系列版本（含 0100 R08 與 0101 R08A／R08B／R08C）均為歷史檔，與現行 8 人 × 5 維度契約不一致，不得作為現行接受依據，亦不得作為本稿模板。
-P166: 3. 0099 R17 之數值僅依現行契約作為合成示範重用，不改變其原需求（I18-E07）與原文件定位，亦不得修改或重新分類該文件。
-P167: 4. 本表不提供、也不暗示任何自評通過標準；若機構日後自行訂定使用規則，應另立文件並明確標示其性質，不得回寫為本表之官方門檻。
+P069: 5. 後測填答頁（可複印使用）
+P070: 5.1 填答說明
+P071: 1. 題目與前測完全相同，請依「現在」的感受重新評一次，不需要刻意與前測分數比較。
+P072: 2. 請填入與前測完全相同的四位數字配對代碼與版本。A01–A08 是本文件合成資料識別碼，並非正式填答代碼。
+P073: 3. 每題只勾一個 0–4 分；漏選或多選先 HOLD，請本人更正，例子欄可空白。
+P074: 影印／回收方式：後測完整表單共兩頁；基本欄位、自評題、例子與檢查頁須按頁序整組使用及回收，不拆頁。
+P075: 5.2 基本欄位
+P077: 5.3 五題自評
+P078: 本頁量尺速查（完整行為錨點見第 3.2 節）：0＝還無法描述或執行；1＝需逐步帶領；2＝看範例或檢核表可完成一部分；3＝可獨立完成典型任務；4＝可解釋、檢查並套用到新例。
+P080: 我的例子（可空白）
+P082: 5.4 後測完整性檢查（交回前自行確認）
+P083: ☐ 配對代碼與前測完全相同
+P084: ☐ 版本與前測相同（SR-0100-v1.0-SAMPLE）
+P085: ☐ 五題各只勾選一個分數且在 0–4 之間；漏選或多選均先 HOLD，不由承辦人代選
+P086: ☐ 後測日期不早於前測日期
+P087: ☐ 未書寫姓名、聯絡方式、任職單位全名、雇主／客戶／服務對象名稱等可識別資訊
+P088: 6. 收回檢核、缺漏處理與退件條件
+P089: 6.1 收回檢核步驟（承辦人）
+P090: 1. 當場確認每人前、後測各一份，並核對代碼是否相同。
+P091: 2. 逐份檢查五題是否各只有一個勾選、是否落在 0–4；漏選或多選均先 HOLD，請本人補正，不可自行選值。
+P092: 3. 檢查版本欄是否一致；不一致者先隔離，不併入資料。
+P093: 4. 檢查日期先後；後測早於前測者退件。
+P094: 5. 檢查代碼與自由文字例子是否含姓名、電話、地址、任職單位全名、雇主／客戶／服務對象名稱等可識別資訊；如有，先 HOLD，安全遮蔽或請本人重填，並依第 7 節處置舊表。
+P095: 6. 依配對代碼排序，重複代碼立即抽出，依 6.2 處理。
+P096: 7. 登錄「收回份數、有效份數、保留份數、退件份數」，並記錄原因。
+P097: 8. 只有在全部檢核完成後，才把資料交給 0101。
+P098: 6.2 缺漏、重複與不一致的處理
+P100: 6.3 退件與保留彙總清單
+P101: HOLD（可補正後再用）：單題漏選或多選、字跡不清、代碼疑似打錯、日期未填、重複代碼待本人確認。重複代碼的全部相關表單一律先 HOLD，不得先選一份計分。
+P102: REJECT（不得補正，直接排除）：版本不符、後測早於前測、承辦人代填、拒絕更正之個資欄位、本人無法確認歸屬的重複代碼或無法安全確認的配對。
+P103: 必要原則：任何缺漏都不得補值；排除份數與原因必須與有效份數一起揭露，分母不得隱藏。
+P104: 7. 隱私與資料最小化
+P105: 1. 不收集：姓名、電話、地址、生日、身分證號、學號、簽名、照片、任職單位全名、雇主／客戶／服務對象名稱。
+P106: 2. 只收集：四位數字配對代碼、版本、階段、日期、5 個 0–4 分數、可選的一句例子；例子不得寫入可識別的雇主、客戶或服務對象名稱。
+P107: 3. 分開存放：若機構因報名或簽到而另有名冊，名冊與本表分開保管，不併入本表、不併入 0101、不放入同一資料夾。
+P108: 4. 對照表：本示範稿不含任何代碼對照表。正式使用時若需對照，由單一窗口保管，設定存取權限，不隨報告流通，並在分析完成後依機構政策處理。
+P109: 5. 紙本：收回後置於可上鎖空間；電子檔去識別化後僅保留代碼與分數。
+P110: 6. 揭露：對外呈現僅用彙總數據；樣本數很小時不單獨呈現可辨識個人的分組。
+P111: 7. 法律依據與保存期限：由使用機構依其適用規範自行確認；本文件不主張任何特定法規遵循狀態、不主張已完成告知同意程序、也不主張具有任何法定權限。
+P112: 8. 當事人請求：由使用機構自訂窗口與流程；本示範稿不代為承諾任何處理時限。
+P114: 8. 合成示範資料集（80 格）與驗算
+P115: 8.1 完整矩陣（A01–A08，全部為 SAMPLE／SYNTHETIC）
+P117: 表中前 A–E 與後 A–E 共 8 × 5 × 2 = 80 格，皆為原始自評值；「前總分」、「後總分」、「變化」為計算值，不計入 80 格。
+P118: 8.2 精確合計與驗算
+P120: 維度層級合計（交叉驗算用）
+P122: 核對：維度前測合計 17 + 16 + 13 + 14 + 15 = 75，等於前測總分；維度後測合計 25 + 24 + 22 + 24 + 22 = 117，等於後測總分；117 − 75 = 42。八人變化 +7、+6、+3、+4、+6、+5、+5、+6 合計亦為 +42。
+P123: 8.3 這組數值可以怎麼讀、不可以怎麼讀
+P124: 可以：作為 0100 與 0101 之間的格式與計算示範，確認欄位對應、加總、平均、雷達圖軸向與分母揭露方式正確。
+P125: 不可以：不可說這是真實訓練成果、不可說學員能力已被客觀驗證、不可說本表與 0099 技能評分一致或相關、不可引用 0099 的通過門檻、不可推論母體成效、不可作為招生或績效宣稱。
+P127: 9. 與 0101 的交接
+P128: 9.1 交接包內容（0101 只接收這些）
+P130: 9.2 交接格式（欄位順序固定）
+P131: 代碼,前A,前B,前C,前D,前E,前總分,後A,後B,後C,後D,後E,後總分,變化
+P132: 不得改名、不得重排、不得新增未經定義的欄位。若正式資料有 HOLD／REJECT 份數，須另附排除清單與原因。
+P133: 9.3 0101 收到後應做與不得做
+P134: 應做：重算每一列總分與變化、核對 80 格是否齊全、以同一 0–4 尺度繪製五維度前後雷達圖、標示 SAMPLE／SYNTHETIC、揭露 n = 8 與分母、保留限制說明。
+P135: 不得做：修改或補值、刪除不利數值、把自評描述成技能證據、宣稱前後差異具統計顯著性或相關性、套用 0099 門檻、加入未經來源支持的人員或機構資訊。
+P136: 9.4 文件層級交接
+P137: 本 0100 完稿經審查後，連同版本、SHA 與本節交接包一併提供 0101 製作 DOCX 報告；0101 的產出不得回寫或改動本表數值。
+P138: 10. 承辦人一頁式流程與常見錯誤
+P139: 10.1 一頁式流程
+P140: 1. 課前準備：印好前測表與後測表，版本同為 SR-0100-v1.0-SAMPLE，課程代碼預先印妥。
+P141: 2. 開場說明（2 分鐘）：說明這是自評、沒有及格分數、不記名、需自選四位數字配對代碼並記住。
+P142: 3. 前測（8–12 分鐘）：學員自行填寫，承辦人不代填、不提示答案。
+P143: 4. 收回檢查：當場確認五題各一格、分數 0–4、代碼已填。
+P144: 5. 訓練進行：不改變題目、不中途追加題項。
+P145: 6. 後測（8–12 分鐘）：提醒使用同一代碼與版本。
+P146: 7. 配對與檢核：依第 6 節逐項檢查，登錄有效、保留、退件份數。
+P147: 8. 交接 0101：依第 9 節格式交付，附限制註記。
+P148: 10.2 常見錯誤
+P149: 1. 前後測使用不同版本或不同題目文字。
+P150: 2. 承辦人幫學員選代碼，導致無法確認是否同一人。
+P151: 3. 學員在表上寫姓名或電話，增加辨識風險。
+P152: 4. 缺漏時直接填 0 或填平均數。
+P153: 5. 重複代碼未處理就全部計入。
+P154: 6. 只報總分，未揭露有效樣本數與排除份數。
+P155: 7. 把自評分數說成「能力已達標」或「訓練有效」。
+P156: 8. 把本表數值與 0099 技能評分混用或宣稱一致。
+P157: 9. 自行設定 60 分、80% 之類的通過門檻。
+P158: 10. 在 0101 報告中改動 0100 的原始分數。
+P159: 11. SAMPLE 替換登錄與版本限制
+P160: 11.1 SAMPLE 替換登錄表（正式使用前必須逐項替換）
+P162: 11.2 版本限制
+P163: 1. 本稿為 SAMPLE／SYNTHETIC 候選工具，沒有真實填答、協會核准或正式接受聲明；獨立審查範圍與結論以候選 exact-SHA 外部收據為準，不得只依本文件狀態列推定通過。
+P164: 2. 先前 1 人 × 6 維度之 R08 系列版本（含 0100 R08 與 0101 R08A／R08B／R08C）均為歷史檔，與現行 8 人 × 5 維度契約不一致，不得作為現行接受依據，亦不得作為本稿模板。
+P165: 3. 0099 R17 之數值僅依現行契約作為合成示範重用，不改變其原需求（I18-E07）與原文件定位，亦不得修改或重新分類該文件。
+P166: 4. 本表不提供、也不暗示任何自評通過標準；若機構日後自行訂定使用規則，應另立文件並明確標示其性質，不得回寫為本表之官方門檻。
 T01R01: 項目 | 內容
 T01R02: 文件名稱 | 學員訓練前後自我評量表（Learner Pre/Post Self-Assessment Form）
 T01R03: DOC_ID | 0100
 T01R04: 需求編號 | I18-E08
 T01R05: 官方表單印刷序號 | UNKNOWN（未自原始表單讀取，不得推測或填寫）
 T01R06: 對應文件 | 0100 本表；0101 自覺成長雷達分析報告
-T01R07: 本稿版次 | R09a
+T01R07: 本稿版次 | R09b（由 R09a 定點修補）
 T01R08: 文件性質 | SAMPLE／SYNTHETIC 示範稿，含可實際使用之空白表與 8 人合成示範資料
-T01R09: 現況 | 尚未有真實學員填答、尚未經獨立審查與正式驗收
+T01R09: 現況 | 無真實學員填答；R09a 舊 SHA 語意審查 PASS。本 R09b 為局部修補候選，待本版 delta 複核；正式驗收 NOT_GRANTED。
 T02R01: 項目 | 建議作法
 T02R02: 前測時間 | 約 8–12 分鐘（含說明）
 T02R03: 後測時間 | 約 8–12 分鐘（含說明）
@@ -221,16 +220,17 @@
 T11R05: D | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
 T11R06: E | ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
 T12R01: 情況 | 判定 | 處理方式
-T12R02: 分數不在 0–4（例如 5、空白、塗改不清） | 無效 | 請本人重填該題；無法重填則整份 HOLD，不得以 0 代入
-T12R03: 任一維度未勾選 | 缺漏 | 整份 HOLD，請本人補填；不得以平均數、前測值或 0 代入
+T12R02: 分數超出 0–4（例如 5、6、負數）或塗改不清 | 無效 | 請本人重填該題；無法重填則整份 HOLD，不得以 0 代入
+T12R03: 任一維度未勾選（空白） | 缺漏 | 整份 HOLD，請本人補填；不得以平均數、前測值或 0 代入
 T12R04: 同階段出現兩份以上相同代碼 | 重複／可能錯配 | 同代碼全部表單 HOLD；不可按完整度或分數擇一。須由各填答者本人在場確認並留下更正註記；不能確認時全部 REJECT，排除於有效分母
 T12R05: 同一題勾選兩個以上分數 | 多選／無效 | 該份 HOLD，請本人重選一個；無法確認時該份 REJECT，不得由承辦人代選
-T12R06: 前後測代碼不一致 | 無法配對 | 未經本人當場確認不得配對；確認後更正並留註記
-T12R07: 問卷版本不一致 | 版本不符 | 該對 REJECT，不併入分析
-T12R08: 後測日期早於前測 | 時序錯誤 | 該對 REJECT，查明後重填
-T12R09: 代碼含姓名、電話、證件號 | 個資風險 | 立即更換代碼，舊表依第 7 節銷毀或遮蔽
-T12R10: 承辦人代填或代改分數 | 程序違失 | 該份作廢，記錄原因
-T12R11: 未揭露有效樣本數或分母 | 揭露不足 | 不得產出 0101 分析
+T12R06: 前後測各一份同碼，未確認為同一人 | 身分配對未證實 | 先 HOLD；由本人確認為同一人並核對同版本、日期順序，留下核對註記後才可配對；未能確認或發現他人同碼碰撞時兩表 REJECT，排除有效分母。不得只因代碼相同就推定同一人。
+T12R07: 前後測代碼不一致 | 無法配對 | 未經本人當場確認不得配對；確認後更正並留註記
+T12R08: 問卷版本不一致 | 版本不符 | 該對 REJECT，不併入分析
+T12R09: 後測日期早於前測 | 時序錯誤 | 該對 REJECT，查明後重填
+T12R10: 代碼含姓名、電話、證件號 | 個資風險 | 立即更換代碼，舊表依第 7 節銷毀或遮蔽
+T12R11: 承辦人代填或代改分數 | 程序違失 | 該份作廢，記錄原因
+T12R12: 未揭露有效樣本數或分母 | 揭露不足 | 不得產出 0101 分析
 T13R01: 代碼 | 前A | 前B | 前C | 前D | 前E | 前總分 | 後A | 後B | 後C | 後D | 後E | 後總分 | 變化
 T13R02: A01 | 2 | 2 | 1 | 2 | 1 | 8 | 3 | 3 | 3 | 3 | 3 | 15 | +7
 T13R03: A02 | 2 | 2 | 2 | 2 | 2 | 10 | 3 | 3 | 3 | 3 | 4 | 16 | +6
@@ -278,6 +278,6 @@
 T17R08: 配對代碼 | A01–A08 | 學員自選代碼
 T17R09: 分數 | 80 格合成值 | 實際填答值
 T17R10: 衍生統計 | 前 75、後 117、差 +42、每人平均變化 +5.25；A–E 平均變化 +1.000、+1.000、+1.125、+1.250、+0.875 | 由被替換後的原始分數與有效分母重新計算，不可沿用示範值
-T17R11: 合成替換清冊 | synthetic_replacement_register_0100_R09.csv | SHA-256：889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8；替換原始分數後須重算所有總分、平均與維度統計
+T17R11: 合成替換清冊 | synthetic_replacement_register_0100_R09.csv（沿用未改動的 R09 清冊） | SHA-256：889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8；替換原始分數後須重算所有總分、平均與維度統計
 T17R12: 承辦人 | 未指定 | 實際承辦人
 T17R13: 限制註記 | 已載明合成與自評性質 | 仍須保留，不得刪除


===== TECHNICAL_QA SHA256=bfa88bde02ca984194273cecc33164f5cdb806c249aac5f7d17c3d8b086db1f6 BYTES=8603 =====
{
  "receipt_id": "TTQS-0100-I18-E08-R09B-TECHNICAL-QA",
  "generated_local": "2026-10-26T06:19:19.443917+08:00",
  "doc_id": "0100",
  "official_requirement_id": "I18-E08",
  "project_internal_index": 109,
  "official_printed_checkbox_serial": "UNKNOWN",
  "revision": "R09b",
  "artifact_state": "CANDIDATE",
  "formal_acceptance": "NOT_GRANTED",
  "real_evidence": "UNKNOWN/HOLD",
  "candidate": {
    "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09b\\0100_I18-E08_R09b.docx",
    "sha256": "0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c",
    "bytes": 58934,
    "zip_integrity": "PASS",
    "word_paragraphs": 166,
    "word_tables": 17,
    "word_sections": 3
  },
  "inputs": {
    "source_packet": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\SOURCE_PACKET_I18-E08_0100_0101_R09.md",
      "sha256": "81caa978a17dda522850628e6e9b4b16453145a986d2bafd2598b6f5ac96b886",
      "bytes": 5253
    },
    "unique_blueprint_0100": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\UNIQUE_BLUEPRINT_0100_I18-E08_R09.md",
      "sha256": "c407af272823d0159bbbe0c1c9258ed74ee89e5328bd8338840cef26183b2817",
      "bytes": 4829
    },
    "official_evidence_pdf": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\INPUTS\\R04\\06_OFFICIAL_SOURCES\\TTQS查核佐證文件資料表-訓練機構版 (2).pdf",
      "sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
      "bytes": 303044
    },
    "synthetic_replacement_register": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09\\synthetic_replacement_register_0100_R09.csv",
      "sha256": "889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8",
      "bytes": 65820
    },
    "word_native_pdf": {
      "path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09b\\0100_I18-E08_R09b_LAYOUT2_WORD_NATIVE.pdf",
      "sha256": "8fa862618d46c5adf76b8b8c9b48f8ec11aa3f836aa7954851fcd01febe8f015",
      "bytes": 649899
    }
  },
  "content_checks": {
    "document_id_and_requirement": true,
    "internal_index_not_misrepresented": true,
    "revision_r09b": true,
    "sample_synthetic_boundary": true,
    "formal_acceptance_not_granted": true,
    "no_real_learner_response": true,
    "four_digit_wording": true,
    "employer_privacy_term": true,
    "client_privacy_term": true,
    "service_recipient_privacy_term": true,
    "no_zero_or_mean_imputation": true
  },
  "pairing_rule_text": "前後測各一份同碼，未確認為同一人 | 身分配對未證實 | 先 HOLD；由本人確認為同一人並核對同版本、日期順序，留下核對註記後才可配對；未能確認或發現他人同碼碰撞時兩表 REJECT，排除有效分母。不得只因代碼相同就推定同一人。",
  "sample_math": {
    "respondent_pairs": 8,
    "dimensions": 5,
    "phases": 2,
    "original_score_cells": 80,
    "range": [
      0,
      4
    ],
    "pre_total": 75,
    "post_total": 117,
    "delta": 42,
    "pre_mean": 9.375,
    "post_mean": 14.625,
    "mean_delta": 5.25,
    "rows": [
      {
        "code": "A01",
        "pre": [
          2,
          2,
          1,
          2,
          1
        ],
        "pre_total": 8,
        "post": [
          3,
          3,
          3,
          3,
          3
        ],
        "post_total": 15,
        "delta": 7
      },
      {
        "code": "A02",
        "pre": [
          2,
          2,
          2,
          2,
          2
        ],
        "pre_total": 10,
        "post": [
          3,
          3,
          3,
          3,
          4
        ],
        "post_total": 16,
        "delta": 6
      },
      {
        "code": "A03",
        "pre": [
          3,
          2,
          2,
          2,
          2
        ],
        "pre_total": 11,
        "post": [
          3,
          3,
          3,
          3,
          2
        ],
        "post_total": 14,
        "delta": 3
      },
      {
        "code": "A04",
        "pre": [
          2,
          2,
          1,
          2,
          2
        ],
        "pre_total": 9,
        "post": [
          3,
          3,
          2,
          3,
          2
        ],
        "post_total": 13,
        "delta": 4
      },
      {
        "code": "A05",
        "pre": [
          3,
          3,
          2,
          2,
          2
        ],
        "pre_total": 12,
        "post": [
          4,
          4,
          3,
          3,
          4
        ],
        "post_total": 18,
        "delta": 6
      },
      {
        "code": "A06",
        "pre": [
          1,
          2,
          1,
          1,
          2
        ],
        "pre_total": 7,
        "post": [
          3,
          2,
          2,
          3,
          2
        ],
        "post_total": 12,
        "delta": 5
      },
      {
        "code": "A07",
        "pre": [
          2,
          2,
          2,
          2,
          2
        ],
        "pre_total": 10,
        "post": [
          3,
          3,
          3,
          3,
          3
        ],
        "post_total": 15,
        "delta": 5
      },
      {
        "code": "A08",
        "pre": [
          2,
          1,
          2,
          1,
          2
        ],
        "pre_total": 8,
        "post": [
          3,
          3,
          3,
          3,
          2
        ],
        "post_total": 14,
        "delta": 6
      }
    ],
    "dimension_rows": [
      [
        "A",
        17,
        25,
        1.0
      ],
      [
        "B",
        16,
        24,
        1.0
      ],
      [
        "C",
        13,
        22,
        1.125
      ],
      [
        "D",
        14,
        24,
        1.25
      ],
      [
        "E",
        15,
        22,
        0.875
      ]
    ]
  },
  "replacement_register": {
    "rows": 145,
    "all_rows_sample_synthetic": true,
    "sha256": "889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8"
  },
  "word_render": {
    "method": "Microsoft Word native COM PDF export (existing PDF; no re-export in this QA run)",
    "pdf_sha256": "8fa862618d46c5adf76b8b8c9b48f8ec11aa3f836aa7954851fcd01febe8f015",
    "page_count": 16,
    "page_image_count": 16,
    "page_image_sha256": {
      "page-1.png": "ba72909b21696c41aa7c5a8b0f53b860bd31c8a00d25281dcf2aa71b33a5406d",
      "page-2.png": "b6e61802e4de66478ccf0153a27971e15e2780383b2e0403fa6b3c74dcf2cf68",
      "page-3.png": "9225fba3f5989e010a5e6cc49b1e3fbe0b34cd2bbc608572f5fa8d6d1d2ee93e",
      "page-4.png": "f09321b837e9d5ba6cfe9707d8a7f04e41ab112bd1fe970221f385681c1cca03",
      "page-5.png": "ac34b566889d5cd52aa7649260987567bad9a52acd0d881dcf270708d8ae46e4",
      "page-6.png": "ad5dff9768b32ca8ecbb1e0c362fe1cc0b758f69c3f66079ab302a1886be0e9c",
      "page-7.png": "d8d3a40e3bbba687350243cf765d30f4a077f08c66e13b63b24e213128e4969a",
      "page-8.png": "f4f2effeb16179d2df72eda871b556f385208b30933d1e199eacd6431ef35db4",
      "page-9.png": "f62c861f51e98b14d60460693546c5c847d0cf983d51841594cc70387456d42d",
      "page-10.png": "3859e76dfa31e536939198b17c70c17e1f0ce4db564efc8ec78cad5ad6b9d870",
      "page-11.png": "c8c1eb4af8ec6ff8b2715d024bf80a07a26bd0a56425f8f907033177dc88d088",
      "page-12.png": "6a42b2ccf2404d01a8cb2dcb8feb85f0f8069e11eeb05649d999326cf518a0bc",
      "page-13.png": "9fb16171b8d30d03dc27cbe28c758c35db4825f5a1c5850db486a183ecdf65a4",
      "page-14.png": "5a521418bc27c4d002ddf6879aac96e748a034995d5cdcd07d7cf040d5eaa3a7",
      "page-15.png": "2bcd7a83bba9546f5f195d880c633eab6f85204b68a19dd39394fc129db353a9",
      "page-16.png": "db70777c70b3f31c7d5540a4e894c5d08f0eeef5eb86e15b462b4a56e293544a"
    }
  },
  "semantic_review": "PENDING",
  "scope_limit": "Deterministic technical and consistency checks only; does not establish semantic acceptance or association approval.",
  "result": "TECHNICAL_PASS_FOR_EXACT_SHA; VISUAL_REVIEW_RECORDED_SEPARATELY; CANDIDATE_NOT_FORMALLY_ACCEPTED"
}

===== VISUAL_QA SHA256=5a20b1604f8857594244c82b01838454b421685edb99a5fb1618d05d914dea9b BYTES=1579 =====
{
  "receipt_id": "TTQS-0100-I18-E08-R09B-VISUAL-QA",
  "generated_local": "2026-10-26T06:19:19.592651+08:00",
  "doc_id": "0100",
  "official_requirement_id": "I18-E08",
  "revision": "R09b",
  "candidate_sha256": "0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c",
  "rendered_pdf_sha256": "8fa862618d46c5adf76b8b8c9b48f8ec11aa3f836aa7954851fcd01febe8f015",
  "rendered_page_count": 16,
  "rendered_page_image_count": 16,
  "pages_inspected": "1-16 individually at rendered page size; current layout2 set",
  "observations": [
    "Cover maps to 0100/I18-E08 and labels R09b and SAMPLE/SYNTHETIC.",
    "Respondent form, 0-4 scale, paired sample matrix, arithmetic, intake/hold/reject guidance, 0101 handoff, and replacement register are legible.",
    "No visible clipping, overlapping text, truncated table rows, orphan checkboxes, or broken continuations in the inspected 16-page render.",
    "Page 13 contains a short calculation interpretation section and substantial white space before section 9 starts on page 14; recorded as non-blocking whitespace, not a content or readability failure."
  ],
  "method": "Existing Microsoft Word native COM PDF export rendered to PNG; each page visually inspected; exact artifact/PDF/page image hashes listed in technical QA receipt.",
  "limitations": [
    "This visual review is separate from semantic review.",
    "No physical print test.",
    "No formal association acceptance."
  ],
  "result": "VISUAL_PASS_WITH_NONBLOCKING_WHITESPACE_FOR_EXACT_SHA; CANDIDATE_NOT_FORMALLY_ACCEPTED"
}

===== CROSSDOC_QA SHA256=a99dd00abb10a49783409324866d541a801e57dcf7334c437ac07d9bb19cd635 BYTES=3002 =====
{
  "receipt_id": "TTQS-I18E08-DOC0100-R09B-TO-DOC0101-R09-FINAL9-CROSSDOC-CHECK-R01",
  "generated_local": "2026-10-26T06:24:26.623576+08:00",
  "project_id": "TTQS_ONE",
  "doc_a": {
    "doc_id": "0100",
    "requirement_id": "I18-E08",
    "candidate_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09b\\0100_I18-E08_R09b.docx",
    "candidate_sha256": "0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c",
    "matrix_table_1_based": 13
  },
  "doc_b": {
    "doc_id": "0101",
    "requirement_id": "I18-E08",
    "candidate_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09_0101\\0101_I18-E08_R09.docx",
    "candidate_sha256": "56f433e095f32378f2fd8241c1a27948d2bfe6748da003af5623d265885edb68",
    "matrix_table_1_based": 11,
    "technical_receipt_path": "E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\QUALITY_REBUILD_20261016\\0100_0101_R08_SOURCE_BLUEPRINT_20261021\\candidate_R09_0101\\technical_qa_0101_R09_final9.json",
    "technical_receipt_sha256": "cc64f55564686f5e27e9c8df1ff2b28d35ed281ca8d8d0bdcf1150e80f95dd3d"
  },
  "raw_matrix_comparison": {
    "A01": [
      2,
      2,
      1,
      2,
      1,
      3,
      3,
      3,
      3,
      3
    ],
    "A02": [
      2,
      2,
      2,
      2,
      2,
      3,
      3,
      3,
      3,
      4
    ],
    "A03": [
      3,
      2,
      2,
      2,
      2,
      3,
      3,
      3,
      3,
      2
    ],
    "A04": [
      2,
      2,
      1,
      2,
      2,
      3,
      3,
      2,
      3,
      2
    ],
    "A05": [
      3,
      3,
      2,
      2,
      2,
      4,
      4,
      3,
      3,
      4
    ],
    "A06": [
      1,
      2,
      1,
      1,
      2,
      3,
      2,
      2,
      3,
      2
    ],
    "A07": [
      2,
      2,
      2,
      2,
      2,
      3,
      3,
      3,
      3,
      3
    ],
    "A08": [
      2,
      1,
      2,
      1,
      2,
      3,
      3,
      3,
      3,
      2
    ]
  },
  "calculations": {
    "pairs": 8,
    "dimensions": 5,
    "phases": 2,
    "raw_cells": 80,
    "pre_total": 75,
    "post_total": 117,
    "change": 42,
    "all_rows_match": true
  },
  "checks": {
    "same_8_pair_codes": true,
    "all_80_raw_scores_match": true,
    "pre_total_75": true,
    "post_total_117": true,
    "delta_42": true,
    "0100_r09b_candidate_unchanged": true,
    "0101_final9_candidate_unchanged": true,
    "no_real_evidence_promoted": true
  },
  "result": "PASS_CROSS_DOCUMENT_RAW_DATA_CONSISTENCY_FOR_EXACT_SHA_PAIR",
  "status_limits": {
    "both_are_candidates": true,
    "formal_acceptance": "NOT_GRANTED",
    "real_records": "UNKNOWN/HOLD",
    "does_not_extend_0101_semantic_or_visual_review": true
  }
}


===== PRIOR_W2_RESPONSE SHA256=c18e85e2c61cdb5fa8fa8bee5a9002bc02fe4c3550fbfae5ea5340b3210fb2c4 BYTES=3109 =====
{
  "doc_id": "0100",
  "requirement_id": "I18-E08",
  "candidate_sha256": "0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c",
  "body_extraction_sha256": "0c3c7370db89e529d7fd963f69eedaae2701956fea0c65956f7432066f71734e",
  "verdict": "PASS",
  "findings": [],
  "criterion_results": {
    "F1": {
      "status": "PASS",
      "assessment": "Closed. T12R06 explicitly establishes that a matching pre/post code across stages without identity verification must be placed on HOLD, requires respondent verification of identity, identical version, and chronological order with audit notes, and mandates REJECT with exclusion from the denominator if unverified or if collision occurs, prohibiting presumptive matching."
    },
    "F2": {
      "status": "PASS",
      "assessment": "Closed. Operational privacy checklists and handler checks in P064, P087, and P094 explicitly name employer/workplace, client, and service-recipient identifiers alongside personal contact data."
    },
    "F3": {
      "status": "PASS",
      "assessment": "Closed. P002, T01R07, T01R09, and P163 clearly differentiate prior R09a PASS on the old SHA from the pending R09b delta candidate review, and explicitly state that formal acceptance is NOT_GRANTED."
    },
    "F4": {
      "status": "PASS",
      "assessment": "Closed. Standardized to '四位數字配對代碼' in P064 and P141; blanks are consolidated into a single classification ('缺漏') in T12R03 while T12R02 is restricted to out-of-range/illegible; CSV header in P131 has all leading spaces removed; T17R11 explicitly notes retention of the unchanged R09 register."
    },
    "no_new_material_contradiction": {
      "status": "PASS",
      "assessment": "The targeted delta maintains internal consistency across learner forms, handler instructions, validation tables, and handoff specifications to 0101 without introducing contradictions or altering score matrices."
    },
    "sample_real_boundary": {
      "status": "PASS",
      "assessment": "SAMPLE/SYNTHETIC designations remain prominent; REAL UNKNOWN / HOLD statuses and NOT_GRANTED formal acceptance remain explicit across headers, metadata, and limitation sections."
    },
    "scope_inheritance": {
      "status": "PASS",
      "assessment": "All unchanged text and tables inherit coverage from the prior exact-SHA baseline PASS (debd41e7ca1b18b88cad37db118c5b3474df411b3e2d1c87a8351d456245e0b2); delta is strictly bounded to F1-F4 repairs."
    }
  },
  "review_scope": "Independent semantic delta review of candidate R09b against baseline R09a for doc_id 0100 (requirement I18-E08), covering structured text diff for paragraphs P001-P166 and table rows T01-T17, verification of F1-F4 closures, and cross-stage handoff coherence with 0101.",
  "limitations": "Text-only semantic review based strictly on the provided structured extraction diff and candidate metadata; no visual layout inspection performed; relies on cited baseline PASS and local deterministic checks for unchanged 80-cell synthetic matrices and register row counts."
}

