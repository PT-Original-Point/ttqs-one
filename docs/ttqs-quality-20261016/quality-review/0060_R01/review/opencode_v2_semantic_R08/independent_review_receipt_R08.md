# 0060 R08 independent review receipt

## Candidate and authority
- DOCX ID: 0060
- Official requirement: I14-E01
- Official checkbox: 065
- Candidate: `candidate/0060_R08.docx`
- Exact SHA-256: `92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3` (71,613 bytes)
- The run record verifies the same SHA before and after review (`candidate_unchanged=true`).

## Independent review
- Route: OpenCode CLI v2.0.29; requested model `opencode/mimo-v2.6-flash-free`
- Status: **PASS**, CLI exit code 0; 1,295.007 seconds; stderr empty.
- Review packet SHA-256: `A199AF449FDAF991FFFA09C66585D76B873A3CADCA120E31AE1A70CB3E0C8645`
- Raw stdout SHA-256: `E996ADFD3E90BBE42CCA3142F9A3B842379B50746FC00ADFF39FA38E5D93A34D` (6,362,140 bytes)
- Extracted reviewer response SHA-256: `3FF43230E66AD33375DC06A35A2AC6EF52B492F586DF01473D0E1121B7452E23`
- Run receipt: `review/opencode_v2_semantic_R08/attempt01_mimo_v2_6_flash_free/run_R08_attempt01.json`
- Reviewer response: `review/opencode_v2_semantic_R08/independent_review_response_R08.md`

## Verified scope and limits
- All 11 packet checks passed; the four prior R07 semantic findings were closed, register parity was 12/12, and the 66-row SAMPLE register had no blank cells or forbidden literals.
- Arithmetic and cross-table lineage were independently recomputed. The candidate matches the packet and did not change during review.
- The 26-page Word export was verified; the four changed pages (18, 19, 20, 23) were inspected directly, and 22 unchanged page images matched the R07 baseline byte-for-byte. The reviewer directly inspected 15 full-resolution pages.
- One non-blocking observation: 17 table-caption runs are 10.0 pt. The reviewer found them legible; body prose is 11 pt and table body 9.5 pt.
- The official PDF page was checked using its hash and extracted text; direct visual reading of the official PDF was unavailable to the reviewer. PDF layout claims rely on rendered page images and text extraction.
- This is an independent candidate review, not Human or association formal acceptance. The document remains a SAMPLE/SYNTHETIC candidate; no real activity or approval is asserted.

## Related exact hashes
- Word-export PDF: `B9850431F0A002E788EC21B4432F47A4F8309E067759C3A7FAB6D95AD3B43BAB`
- Synthetic replacement register: `ADD1F2BCF77C77DF6BA921E1DFA68494AC867A3E3368B795AA56C439AA824C4B`
- Visual receipt: `evidence/visual_review_R08.json`
- Technical QA receipt: `evidence/technical_qa_R08.json`