# DOCX 0064 R06 audit bundle

- Project: TTQS_ONE; official requirement I14-E05, checkbox 069, official source page 5.
- Unique Blueprint R02 SHA-256: `0f521debdaeeef17f2c47d11cccbb193e2a4b0f8370bf4dd56da86d512c0f3d8`.
- Candidate DOCX `0064_R06.docx`: SHA-256 `f83eeda42589da66c23918d522ad983178a252da9b6dd2240b725e9c9cfb50a1`, 148387 bytes. Quality gates pass; candidate remains unaccepted and unpromoted.
- Preserved R05 candidate SHA-256: `54888e13f954478051a49839d8b67ff845992c72811e41e09d90045e512c69e1`.

## Targeted repair

Direct inspection found the §13.3 timing-table header stranded at the bottom of R05 page 19. R06 sets keep-with-next on the six paragraphs in the repeated header row so it moves with the first data page. The document-control revision label changes from R05 to R06. No substantive text, table data, formulas, source mapping or register entries changed. Only `word/document.xml` changed; style definitions and run font/style signatures are unchanged.

## Verification

- Technical: `evidence/technical_qa_R06.json` — PASS on exact R06 SHA; includes recomputation of the 24 paired observations.
- Render: `render_R06/0064_R06.pdf`, SHA-256 `85bdf183f31ec48aeacf95f9e2c12cf5cbd7cb675f5bf1da8d4429be88d2a565`, 28 pages.
- Visual: `evidence/visual_review_R06.json` — PASS_LAYOUT on exact R06 SHA. Pages 1 and 19 directly inspected after repair; the other 26 page images are pixel-identical to the directly inspected R05 render. Page 19 no longer has an orphan header.
- Semantic: `review/semantic_review_R06_receipt.json` — PASS on exact R06 SHA; OpenCode v2.0.29 CLI requested `opencode/beam-free`, exit 0, stderr empty. The raw response is preserved. Runtime model identity is not attested.
- Evidence boundary: SAMPLE/SYNTHETIC only; no actual Association measurements. REAL evidence remains unverified/HOLD. Formal acceptance and promotion are not granted.

Official PDF, Unique Blueprint, R05 manuscript lineage and synthetic replacement register are included. Exact cross-document DOCX SHA hashes and relevant excerpts for 0060 R08, 0061 R03, 0062 R04 and 0063 R02 are recorded in `review/cross_document_source_extract_R06.md`.
