# DOCX 0102 / I18-E09 — R33 candidate

State: candidate only; SAMPLE/SYNTHETIC; independent semantic review returned PARTIAL; formal acceptance not granted.

## Requirement and source binding

- DOCX ID: 0102 (not the official checkbox serial).
- Official requirement: I18-E09; project Blueprint index 110; printed checkbox serial: UNKNOWN.
- Source-control commit used by the builder: ef4af2fb975cab9c701b52415ecaa2bd09d19808.
- Source packet SHA-256: 90E2C809914964039563C734881D9DEDC4E969F60179778F391E39FE2C156982.
- Unique Blueprint SHA-256: 211DE39325C3EE5811D25738161CC6C5AE6322AE6809FD056400ECD2181074A0.

## Candidate and technical/visual QA

- R33 DOCX SHA-256: F17048266910F962D2B5DADBA62CB91863F1CECD2684486D80D3C9A0CEEF1C3A.
- Word 16.0 native PDF: 78 pages; SHA-256 0BD64B8FE4BC5A1ACAAF88FE4E27F0C98ADB8D253ED17E8904281B1211420E6E.
- DOCX reopen, ZIP CRC, content-preservation checks, locator checks, and typography floor checks passed.
- Visual review covered four overview sheets for all 78 pages and full-size pages 1, 52–54, 57, 61–62, and 74–78. Result: PASS_WITHIN_REVIEWED_SCOPE. This is not a semantic acceptance.

## Independent semantic review

- Exact candidate SHA reviewed: F17048266910F962D2B5DADBA62CB91863F1CECD2684486D80D3C9A0CEEF1C3A.
- Verdict: PARTIAL, with 10 findings. Two High findings concern the transposed §12.1 case register and incomplete/wrong §12.2 locators. Remaining findings concern synthetic consent/request state, course_source values, identity state, overdue review date, Form F gate mapping, missing consent/authority in CASE-01 hold, duplicate fact indexing, and overbroad wording about replies.
- Original response: review/R33/opencode_semantic_R33_response.md. Exact-SHA receipt: evidence/R33/semantic_review_receipt_R33.json.
- Coverage limitation: reviewer read all 78 pages of the supplied text and both source documents, but did not recompute the DOCX SHA, assess visuals, or reopen the underlying official PDFs. Actual serving model and CLI exit code are UNKNOWN.
- Dispatch record notes that the CLI was launched with Python CREATE_NO_WINDOW rather than the PowerShell ProcessStartInfo specified by the saved automation. No visible window was observed. Future CLI dispatch must use the required PowerShell method.

## Evidence boundary

The document's sample cases are synthetic. No real award, third-party original, actual consent, association decision, signature, approval, or formal acceptance is claimed. The current replacement register is embedded in R33 §12.1; the older R06 CSV remains historical.
