# TTQS ONE DOCX 0136 candidate R02

## Candidate identity

- DOCX: `0136_I19-E26_R02_CANDIDATE_20261025.docx`
- Exact SHA-256: `a9bd0fb528a1e22865fa5e07df44b314d48c1fd826a08149ecdd1d5915048b39`
- Official requirement: `I19-E26`
- Project 157 index: `150` (internal planning index, not the printed checkbox serial)
- Printed checkbox serial: `UNKNOWN`
- Source packet: `source/SOURCE_PACKET_0136_I19-E26_R01.md`, SHA-256 `7bebd3eb012b152f4568db6fedccf43c3337f436a5f339127e5afe71cf0678d7`
- Unique Blueprint: `source/UNIQUE_BLUEPRINT_0136_I19-E26_R01.md`, SHA-256 `32c1b818cc0b3957a23e319606f77b176a7979d1ee4ff58db72b9ae32ada8399`
- Source artifacts first published in branch commit `a19293ffae3096c5f7306d851b1fc1659ee8e82e`; per-file mapping and hashes are in `SOURCE_MATERIAL_MANIFEST_0136_R02.json`.

## Scope and evidence state

This is a usable operational register for receiving, verifying, classifying, and retrieving evidence about public-benefit activities, awards, and school-industry/research cooperation. The three completed case examples are explicitly SYNTHETIC. No real association activity, award, partnership, signatory, approval, outcome, or source document is asserted. The printed checkbox serial remains UNKNOWN.

The document contains three separate verification routes, source/role/result distinctions, rejection and hold conditions, adjacent-requirement separation, T1–T6 forms and field rules, three complete synthetic demonstrations, and a step-by-step SAMPLE-to-REAL replacement workflow. The standalone source packet and Blueprint are included beside the candidate.

## Revision history

- Superseded predecessor SHA-256: `21e208652930c491e2a93c07e829b101a7fb34b77151caa4ef1784dbbe3697e4`. The 15-page Word render contained an empty page 11 caused by an end-of-page manual break paragraph.
- R02 fixes that single layout defect by applying `page_break_before` to the following section heading. The document text was not changed for this repair.
- R02 renders through Microsoft Word 16.0 to 14 pages. Every page was visually inspected at original resolution. The resulting PDF is `render/0136_R02.pdf`; exact render and per-page hashes are in `LAYOUT_QA_RECEIPT_0136_R02.json`.
- DOCX package integrity, text presence and explicit font sizes passed deterministic checks: table text minimum 9.5 pt; body text minimum 10.5 pt.

## Worker and review disposition

Both original CLI writer responses, requests, stdout/stderr and dispatch receipts are preserved under `worker/writer_attempts/`. OpenCode v2 Mimo Free was stopped by provider HTTP 429 after its CLI syntax correction. Antigravity CLI returned exit 0 when `gemini-3.8-flash-high` was requested, but the response had no provider/model identity and included unsupported approval, deadline, signer, baseline-SHA, and storage-location claims. Its actual model identity and billing are UNKNOWN; its full raw response is UNADOPTED and was not used as manuscript or template.

A separate read-only OpenCode review was explicitly routed to `opencode/deepseek-v4.1-flash-free`, but the provider also returned HTTP 429 before producing a review. `semantic_review=UNKNOWN`; no semantic PASS is claimed. The exact target SHA for a later independent review is the R02 SHA above. Formal Human acceptance is NOT GRANTED.

See `BUILD_RECEIPT_0136_R02.json`, `LAYOUT_QA_RECEIPT_0136_R02.json`, `CANDIDATE_STATE_0136_R02.json`, and `WORKER_DISPOSITION_0136_R02.md` for machine-readable and detailed receipts.
