# 0100 R09b candidate and evidence package

## Identity and status

- Project: TTQS_ONE
- Document: 0100
- Official requirement: I18-E08
- Internal registry index: 109
- Printed official checkbox serial: UNKNOWN
- State: CANDIDATE
- Formal acceptance: NOT_GRANTED
- Real association / learner evidence: UNKNOWN/HOLD
- No real names, signatures, approvals, execution records, or association decisions are asserted.

## Exact candidate and inputs

- DOCX: candidate/0100_I18-E08_R09b.docx
- DOCX SHA-256: 0262d68826181a4b5f6209c3422a2d5c61a0b9820790c4e43a2e483b94de884c
- Source packet SHA-256: 81caa978a17dda522850628e6e9b4b16453145a986d2bafd2598b6f5ac96b886
- Unique Blueprint 0100 SHA-256: c407af272823d0159bbbe0c1c9258ed74ee89e5328bd8338840cef26183b2817
- Official checklist PDF SHA-256: 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709
- Synthetic replacement register SHA-256: 889c202a6e49435d9100e3bf906883410b4ae7160166126f24d9af27c876dbd8

The R09 source packet, unique Blueprint, and synthetic replacement register already exist at their established R09 paths in PR #92. Their raw base64 bytes were re-read at parent HEAD a3dd9584216c8d10ca549cdd2f438b0a96d27ce0 and matched the local QA inputs byte-for-byte. Their SHA-256 values are recorded above. The established source paths are preserved; this package does not overwrite them. The official checklist PDF used by QA is included under inputs/.

## Work and quality evidence

R09b is a deterministic targeted repair of R09a, not a regenerated manuscript. It addresses four recorded findings: same-code cross-stage pairing must be held until identity/version/date order is confirmed; additional employer/client/service-recipient privacy checks; explicit distinction between the R09a baseline review and R09b delta review; and corrected four-digit wording/CSV separators.

- Technical QA: PASS for the exact DOCX SHA; 17 tables; 8 synthetic pairs x 5 dimensions x 2 phases = 80 cells; all scores in 0-4; totals 75 pre / 117 post / +42; 145 replacement-register rows are SAMPLE/SYNTHETIC.
- Word render: Microsoft Word native COM PDF, SHA-256 8fa862618d46c5adf76b8b8c9b48f8ec11aa3f836aa7954851fcd01febe8f015; 16 pages.
- Visual QA: pages 1-16 inspected individually; no clipping, overlap, broken table continuation, or orphan checkbox; page 13 whitespace before section 9 is recorded as non-blocking.
- Semantic review: Antigravity CLI returned an exact-SHA delta PASS over F1-F4 and the SAMPLE/REAL boundary. Requested and CLI-init model: gemini-3.8-flash-high. Actual backend model: UNKNOWN. The reviewer did not inspect rendered pages. R09a's prior PASS remains limited to its own SHA; inheritance is limited to unchanged body scope.
- Cross-document QA: 0100 R09b's 80 raw cells match 0101 R09 final9 exactly. The check does not extend 0101 semantic or visual review.

## Evidence files

- receipts/: patch, technical, visual, independent semantic adjudication, and cross-document receipts.
- review/: exact review manifest, prompt, changed-text diff, original response, CLI dispatch record, stdout, and stderr.
- render/: Word-native PDF used for the 16-page visual inspection.
- inputs/: official checklist PDF used by this candidate. The byte-matched source packet, unique Blueprint, and SAMPLE/SYNTHETIC replacement register remain at their established R09 paths.
- methods/: deterministic repair, build-QA, adjudication, and cross-document scripts.

The package is a candidate evidence record, not formal acceptance, promotion, or Production deployment. Remote raw-byte readback is recorded separately after synchronization.