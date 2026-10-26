# 0133 / I19-E22 — R01 Candidate Evidence Package

State: CANDIDATE. Deterministic technical checks and the 11-page Word-native visual receipt are recorded for the exact DOCX SHA below. An independent OpenCode v2 CLI semantic review returned PASS_TEXT_ONLY_WITH_NONBLOCKING_FINDINGS: zero blocking and four nonblocking findings. The reviewer assessed text only and did not inspect the DOCX binary or page layout. Formal acceptance is NOT GRANTED. REAL association records and source documents remain UNKNOWN / not supplied.

## Official mapping

- Internal deliverable: doc_id=0133 (142-document crosswalk), mapped to official requirement I19-E22.
- 157 Blueprint: index 146, project code I19-L3, official page 8. Printed official checkbox serial is UNKNOWN; 0133 and I19-E22 are not presented as printed serials.
- Official wording: “每年訓練班次、人次均持續成長。” The source is the TTQS checklist reference PDF, page 8. The page excerpt is included; SOURCE_MANIFEST.json identifies the full source PDF blob and SHA-256.
- Nearest negative neighbors: 0132 / I19-E21 covers product defects and improvement; 0134 / I19-E23 covers membership and fee income. This candidate handles annual completed training classes and attendee person-times only.

## Candidate bytes and verification

- DOCX SHA-256: 25116afb8206e0828c8b3a4a763845a9c3e672a4cb49969a64a2a3737d87256b (101,910 bytes).
- Body SHA-256: 0b04da27b9f95b567e2a4828ed94c6c8d517c406c6c3e178725d302b0b3289b7.
- Word-native PDF: 11 pages; its SHA-256 is in qa/TECHNICAL_QA_0133_R01.json.
- Render: Microsoft Word COM ExportAsFixedFormat, then Poppler page rasterization. All 11 final pages were visually checked; pages 1–7 and 11 were exact pixel matches to an already inspected render, while pages 8–10 were directly inspected after page-reference edits. The final page has no orphaned paragraph.
- Technical receipt checks DOCX ZIP integrity, section count, sample row counts, sums, growth calculations, and minimum explicit content/table text sizes (10.5 pt / 9.5 pt). These checks are not independent semantic acceptance.

## What the document contains

A usable annual class/person-times ledger and comparison procedure; definitions for calendar-year attribution, completed class and attendee person-time; a source chain and data dictionary; eight-step annual SOP; 24 completed SAMPLE classes plus one cancelled exception; annual totals 6/72, 8/104 and 10/141 and total 24/317; adjacent-year and endpoint formulas; two separately scaled trend panels; duplicate sign-in and non-comparable-period examples; blank REAL registration and totals forms; a 29-row physical-page-indexed SAMPLE replacement register; and READY/HOLD/REJECT rules.

All sample dates, names, attendee counts, identifiers, role labels, corrections, totals and conclusions are synthetic. They do not state that the association conducted or approved these activities. No signatures, real attendance, real policy, official score or association decision is asserted.

## Worker and review trace

The manuscript was authored in the Codex task and the deterministic local builder created the DOCX. A separate OpenCode v2 CLI reviewer was later dispatched against this same candidate SHA. The retained session export identifies `glm-5.3-flash-free` and matches the request metadata; upstream provider billing is UNKNOWN. The exact-SHA review response is `worker/OPENCODE_GLM_SEMANTIC_R02_20261026T0805/SEMANTIC_REVIEW_RESPONSE_R02.md` (SHA-256 `437a43e31542249f093f9f68e8e8777d9e92939f75305fa74ace0bb2f4f62d1f`); its dispatch receipt is `worker/OPENCODE_GLM_SEMANTIC_R02_20261026T0805/DISPATCH_RECEIPT.json` (SHA-256 `833c88ab2cf3f281a5b5efdd36885948c520acc19ba68ae992cb7d0d919b6690`). The review scope is TEXT_ONLY; it makes no layout-review claim. Four findings are nonblocking; no reviewer prose was adopted into the DOCX. Antigravity CLI was not dispatched for this item.

The title-blind, negative-neighbor semantic review is complete for the exact DOCX SHA above within TEXT_ONLY scope. Result: PASS_TEXT_ONLY_WITH_NONBLOCKING_FINDINGS (0 blocking, 4 nonblocking); the separate visual and technical receipts cover only their declared scopes. No formal acceptance is implied.

## Package map

- source/: official source page, source packet, crosswalk and unique Blueprint lineage.
- candidate/: complete manuscript and openable DOCX.
- worker/: reproducible local DOCX builder.
- qa/: builder receipt, technical and visual scope receipts, truthful worker-routing record, and GitHub raw-byte readback receipt.
- render/: Word-native PDF, all 11 page images and chart image.
