# DOCX 0099 R17 — I18-E07 candidate package

**Current state:** `CANDIDATE_NOT_FORMALLY_ACCEPTED`; every example is `SAMPLE/SYNTHETIC`; real target-customer evidence remains `UNKNOWN/HOLD`.

- DOCX: `candidate/0099_R17.docx`, SHA-256 `293be2dc0e3e0162fa368272851baed27e92990b4ac1871228ec37b51546776b`, 167038 bytes.
- Official requirement: I18-E07, page 7. Project 157-item index is 108; official printed serial is UNKNOWN/not printed.
- Blueprint: R02 only; SHA-256 `cafe5d8ade0fd1c8feac8933018aea50597b4bbd3e86a9eb2234a39e91d51577`; blob `5ec600d4fe2bed76b448daf80382d39dacc5d93b`. R01's historical 160-cell error is not reopened.
- Calculation fixture: 8 learners × 2 stages × 5 dimensions = 80 raw scores; pre 75, post 117, gain 42, mean +5.25; synthetic threshold 6/8. These are sample teaching values, not official outcome claims.
- Manuscript: R14 SHA-256 `7e28d4e626453ced5594a1fafd246f58b51b14fed265135afa6fc8cc8b457476`; replacement register 383 unique synthetic facts, SHA-256 `9f49b166ea7afd267084a2a7dbe0d9e1e5c02f7b61767238f3b5fd7654a99174`.
- Word PDF: 6a84bacf62b20778308830b742f5bb7fc3224a3112ecfc7b572032e742ae07ea, 37 pages. All-page overview and full-size changed pages 1, 22, 23 plus continuation page 24 are included.
- Technical/layout: `PASS_TECHNICAL_AND_SCOPED_VISUAL` on exact R17 SHA; detailed limits in `qa/technical_visual_receipt.json`.
- Independent OpenCode v2 review: text-only PASS for sample text; full requirement is PARTIAL because real target-customer evidence is UNKNOWN/HOLD. Reviewer did not inspect DOCX binary or rendered pages; real novice test NOT_TESTED. Original packet, response, CLI stdout/stderr/exit and sanitized session export are included.
- No association acceptance, real execution, approval or third-party evidence is asserted.

## Package integrity

`SHA256SUMS.json` lists SHA-256 and byte size for each file except itself. `mapping/source_binding_R17.json` binds the candidate, sources, workbook values and exact-SHA QA.
