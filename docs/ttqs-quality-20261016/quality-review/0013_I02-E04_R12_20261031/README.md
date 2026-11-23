# 0013 / I02-E04 R12 candidate

State: CANDIDATE_SAMPLE_SYNTHETIC_NOT_ACCEPTED.

R12 applies one localized layout correction to the verified R11 candidate. In section 11.1 on rendered page 16, the first data-row identifier cell is shortened to I02-E04; the full official title remains elsewhere in the document. R11 base SHA-256: c6570ac11ac06e889628937069c4d66944e4a59e287f8df3cbcd3fa468f5dc95. R12 DOCX SHA-256: $docSha.

Deterministic package verification found identical ZIP entry names and exactly one changed entry, word/document.xml. The target cell equals I02-E04; official title remains present; 20 tables remain; explicit body/table font minima are 10.5/9.5 pt.

Word native export produced a 25-page PDF (SHA-256: $pdfSha). Page 16 was directly inspected and the narrow-column wrapping defect is corrected. This is a partial visual inspection, not a full R12 page-by-page visual PASS.

The scoped exact-SHA OpenCode review did not return a verdict: the requested free route returned HTTP 429 FreeUsageLimitError. Independent semantic review remains pending. The candidate is not formally accepted and contains SAMPLE/SYNTHETIC material only.