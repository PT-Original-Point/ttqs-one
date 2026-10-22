# DOCX 0102 / I18-E09 — R33 candidate

State: candidate only; SAMPLE/SYNTHETIC; independent semantic review pending at the time of this sync; formal acceptance not granted.

## Requirement and source binding

- DOCX ID: 0102 (not the official checkbox serial).
- Official requirement: I18-E09; project Blueprint index 110; printed checkbox serial: UNKNOWN.
- Source-control commit: ef4af2fb975cab9c701b52415ecaa2bd09d19808.
- Current source packet: SOURCE_PACKET_0102_I18-E09_R01.md; SHA-256 90E2C809914964039563C734881D9DEDC4E969F60179778F391E39FE2C156982.
- Unique Blueprint: UNIQUE_BLUEPRINT_0102_I18-E09_R01.md; SHA-256 211DE39325C3EE5811D25738161CC6C5AE6322AE6809FD056400ECD2181074A0. The source and Blueprint bytes were checked against the existing remote Git blobs before this sync.

## Candidate and repair

- R33 DOCX SHA-256: F17048266910F962D2B5DADBA62CB91863F1CECD2684486D80D3C9A0CEEF1C3A.
- R32 predecessor SHA-256: 2322EF89812DB2249B2A98729D4370C82E38F3BA646F340B6C4AD36B57615FB9.
- R33 makes a bounded repair to nine ambiguous replacement-register locators and keeps the closing heading, lead-in, and checklist together. It preserves synthetic case values, dates, statuses, calculation, conclusions, and all non-target content. See the repair script and exact-SHA receipt.
- The current replacement register is embedded in R33 §12.1. The older R06 CSV remains historical and is not asserted to be an R33 sidecar.

## Word and visual QA

- Microsoft Word 16.0 native export PDF: 78 pages; SHA-256 0BD64B8FE4BC5A1ACAAF88FE4E27F0C98ADB8D253ED17E8904281B1211420E6E.
- DOCX reopen and ZIP CRC: PASS. Explicit body font minimum: 10.5 pt; table font minimum: 9.5 pt. Non-target content preservation and locator checks: PASS.
- All 78 pages were reviewed in four overview sheets; full-size review covered pages 1, 52–54, 57, 61–62, and 74–78. Result: PASS_WITHIN_REVIEWED_SCOPE; this is visual/technical evidence, not semantic acceptance.
- The PDF, overview sheets, selected full-size pages, and QA receipts are included.

## Semantic review and evidence boundary

- Requested reviewer: OpenCode v2.0.32, opencode/deepseek-v4.1-flash-free; actual serving-model identity remains UNKNOWN.
- Exact review input and prompt are included. The reviewer process was still running, with no final response, at sync time. Its dispatch receipt records the launch method and window check.
- Every case/person/award detail is synthetic. No real award, third-party original, signature, association decision, approval, or formal acceptance is asserted.
- Candidate review state remains PENDING; do not promote this file based on the Builder's technical or visual checks.
