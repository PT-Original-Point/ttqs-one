# 0012 / I02-E03 — R05 candidate package

- State: `CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED`
- DOCX SHA-256: `a90340289d360a7705fad8137db3a33b648a126ca67b1454d66c0b9288f9d9b5`
- Official item: 補助參與機構公開招生課程或進階課程優惠辦法之規定。
- Unique Blueprint row SHA-256: `0ebf302b8b3601be6c645573e9e12887242c8e64a2244d5cf738a35ee2f5fc04`
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709` (page 1; local source readback recorded in the exact Blueprint row)
- Writer: GPT-6 Luna sub-agent text draft; original draft and receipt retained in `worker/`.
- Repair: R05 adds a page break before section 10.3 to keep its complete tracking table on one page. No substantive body text or table values changed from R04.
- QA: deterministic technical PASS; 17-page Word-native visual QA PASS_LAYOUT_ONLY. Semantic review remains PENDING_INDEPENDENT_REVIEW; formal acceptance UNKNOWN.
- Synthetic data: all 42 `SYN-001` to `SYN-042` entries are fictional examples, exported to the sidecar CSV and embedded in the DOCX. No REAL approvals, payments, attendance, identities, or third-party originals are asserted.
- Rendering: Microsoft Word COM exported the PDF; Poppler generated page PNGs at 120 dpi. LibreOffice/`soffice.exe` was unavailable, so the document skill's LibreOffice render script could not run.

This package is a review candidate only. It is not formally accepted, effective, or a real association record.
