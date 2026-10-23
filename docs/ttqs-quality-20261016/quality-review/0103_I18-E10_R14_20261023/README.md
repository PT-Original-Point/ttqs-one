# 0103 / I18-E10 / official checkbox 111 — R14 candidate evidence

## Status

`CANDIDATE_SEMANTIC_PASS_VISUAL_QA_BLOCKED_NOT_FORMALLY_ACCEPTED`.
This package records a candidate for the original-point association. It does not represent Human acceptance, association approval, a received third-party letter, or a real-world event. All persons, cases, dates and records in the document are marked SAMPLE/SYNTHETIC; no original letter, signature, or approval is included.

## Identity and source binding

- Document ID: `0103`.
- Official requirement: `I18-E10`, official evidence-table page 7.
- Unique Blueprint/checkbox index: `111`.
- Distinct neighbor: `0096 / I18-E03` is official page 6; it is not interchangeable with this page-7 item.
- Candidate DOCX: `candidate/0103__I18-E10__感謝函取得與真偽查核工作紀錄_R14.docx`.
- DOCX SHA-256: `4548a0fba48bb59c08389a6ec13edb1ffe61b58f6e3df3b302c5c4fa7cb39cb0`.
- Body source SHA-256: `0ff3daa9cf5dfa7e5ef9b04456fbc6c00926ab1d268407b6e268fe8032a102ff`.
- SOURCE_PACKET SHA-256: `6d80c5f876bb419b9063003012c08bde6cd19241732af7d1a1550f51892aef77`.
- UNIQUE_BLUEPRINT SHA-256: `885e446a3c5eaf4af80b1665c7462515c5ba35b9979930c06f514a52ad0b205c`.
- Official page-7 excerpt SHA-256: `ed5c20e5d07faa6f717fab4981986c2b1fa11caa24fa46ef9dcacb864fdbd4a4`.
- Builder base SHA-256: `7b59a68f9a5e807604164f3e20e5fc92db70ff03e8822f61bba2d78376f9dd8d`; narrow R14 register patch SHA-256: `47f7f41414f0edf7a78ce46c2e580a3c48b6296b727ade892ea90c5c1bde9201` (`worker/consolidate_register_row_R14.py`).

## Exact-SHA checks

- Technical package receipt: ZIP CRC passed; 276 paragraphs, 26 tables, 11 sections; 35 unique SAMPLE codes mapped to 35 register entries; no missing codes; `SAMPLE-PURPOSE-02` mapped; exact unissued-template heading retained; official page crosswalk and Traditional Chinese wording checked. See `evidence/technical_R14.json`.
- Independent semantic review: **PASS** for the exact DOCX SHA above. The complete reviewer input packet, original CLI JSONL output, dispatch receipt, parsed review and execution receipt are included in `review/`. The reviewer read ordered text only and explicitly did not inspect rendered pages.
- Reviewer route: OpenCode v2 CLI; requested model `opencode/glm-5.3-flash-free`; exit code 0. Actual provider/model identity is `UNKNOWN`; billing/free eligibility is also `UNKNOWN`. The requested model name and non-empty output are not proof of zero cost.
- Visual QA: **BLOCKED** for this exact SHA. Word COM page statistics returned 31 pages, but that is not page-image inspection. Word `ExportAsFixedFormat` and `SaveAs2(PDF)` each timed out; the `PrintOut` diagnostic was rejected by the COM argument binder. Receipts are in `evidence/`. No PDF or PNG exists for R14. The previous revision's visual evidence is not inherited because R14 changed content.
- Overall quality acceptance: **NOT GRANTED** pending exact-SHA visual/page inspection. Do not promote this candidate based on semantic or technical PASS alone.

## R14 delta

R14 is a narrow semantic repair to R13: the `SAMPLE-PURPOSE-02` replacement entry was incorporated in S-06, and the redundant S-39 row was removed. The sample-register count remains 35/35. Other editorial-only observations in the independent review are preserved in its response and were not expanded into another content rebuild.

## Remaining lawful action

Resolve the Word rendering/inspection route for this candidate SHA (or make a concrete layout change only if visual evidence identifies a defect), then record visual results bound to the same exact SHA. The blocked 0103 render lane does not block independent READY documents. No further OpenCode or Antigravity worker should be dispatched on this same review task without a material change; model cost eligibility must be confirmed before any new OpenCode call.

