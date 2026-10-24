# 0134 I19-E23 candidate R01

This package contains a new SAMPLE/SYNTHETIC analysis report candidate. It answers only the official evidence requirement “會員人數及會費收入均逐年增加。” and is distinct from 0133/I19-E22 (training classes and attendee person-times) and 0135/I19-E25 (customer-value outcomes).

## Current state

- Candidate DOCX SHA-256: `a003ad1906194d1cb30a37a313f2ebd004cee129d6c231c6a3bef40b321cee08
- Word-native PDF SHA-256: `464f844f116587bcac55f71e3fa6358fd4101f29af3feae0cbcc9076a9a6445e
- Word-native export: 20 pages; all page images are included under `render/pages/`; the 20 pages were inspected using four contact sheets in `qa/contact_sheets/`.
- Technical checks: 23 tables; 55 synthetic replacement-register entries; body minimum 10.5 pt; table minimum 9.5 pt; calculations rechecked. See `qa/TECHNICAL_QA_0134_R01.json`.
- Content data: SAMPLE/SYNTHETIC only. Real association membership, dues, refund, accounting-policy, and approval records were not supplied; those conclusions remain UNKNOWN.
- Independent semantic review of this exact SHA: PENDING. No reviewer response is included or represented as received.
- Formal acceptance: NOT_GRANTED.

## Sources and mapping

- Official requirement: official evidence-table PDF page 8; exact source is included in `source/official_source.pdf` and the page extract.
- Crosswalk: deliverable 0134 maps to requirement I19-E23. The printed checkbox serial is UNKNOWN and is not inferred from the document ID, requirement ID, or index.
- Project 157 index 147 covers membership/dues ledger and sensitive-data separation. The report keeps identifiable and financial source records out of this public package.
- Unique current Blueprint and complete source packet are included under `source/`. Source prep commit: `eddbcd7f248026d212e85d199aa12738684a50d6`.
- The report contains a synthetic replacement register; the CSV copy is `candidate/0134_SYNTHETIC_REPLACEMENT_REGISTER_R01.csv`.

## Worker and review trace

`qa/WORKER_DISPATCH_AND_RETURN_0134.json` records the per-document dispatch and adoption facts. OpenCode service liveness was not treated as a document Writer session. No OpenCode or Antigravity generation call is claimed for this candidate; no model identity is asserted. The document was authored in the current local task and built with the bundled local Python/docx tooling, then exported through Microsoft Word automation.

The LibreOffice-based renderer could not run because `soffice.exe` is absent; Word-native PDF export and page images were produced instead. This limitation is explicit and does not imply a semantic PASS.

## Reproduce / inspec

- Body manuscript: `candidate/0134_I19-E23_BODY_R01.md
- Openable DOCX: `candidate/0134__會員人數及會費收入逐年變化分析報告_R01.docx
- Word-native PDF: `render/0134_R01_WordNative.pdf
- Builder and QA code: `builder/` and `qa/
