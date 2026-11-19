# DOCX 0091 R03 candidate evidence

- Official requirement: I17D-E05, checkbox 098, 學員就業證明。
- Candidate DOCX SHA-256: `8c9b8f7ec6fa37f9ad833fa5df406ef2c9d120e675eea28cc3d3b15e5b9c4ac3`
- Candidate state: CANDIDATE; not formally accepted.
- Samples are SYNTHETIC; no real association, learner, employer or verification events are asserted.
- Technical checks: static ZIP/content/font checks recorded in `evidence/technical_QA_R03.json`.
- Visual checks: all 16 final Word-rendered pages were directly inspected; see `evidence/visual_review_R03_exact.json`.
- Independent semantic review: **PARTIAL** on this exact SHA. See the raw OpenCode v2 response in `review/independent_semantic_review_R03.md`; the concrete findings are summarized in `PROGRESS.json`.
- Next action: repair only the cited 0091 defects, then create and review a new exact-SHA candidate.

GitHub readback: candidate DOCX remote raw SHA-256 matches the exact local candidate. Text assets were normalized from CRLF to LF by Git; the manifest records GitHub raw blob hashes and the readback receipt confirms each text asset matches after newline-only normalization.
