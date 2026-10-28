# DOCX 0139 / I19-E29 — source mapping and exact candidate state

- Document ID: **0139** (document sequence ID; not a printed checkbox serial).
- Official requirement: **I19-E29** —「證照通過率高及就業率大幅提升。」
- Internal 157-item list index: **153**. Printed official checkbox serial: **UNKNOWN**; index 153 is not substituted for it.
- Unique Blueprint: row 153, R01; SHA-256 `090169968e3df59a6cecaac665a99b2cb625a9cbc355bf84528d08b27c98052a`; genre is cross-year outcome analysis/evaluation report.
- Authoritative source packet: R01 SHA-256 `3c9c310e086a86c03d38bea68bba1ca53bcb2fc927d8949fb6b91c45379d9d47`.
- Existing source evidence is in `docs/ttqs-quality-20261016/quality-review/0139_I19-E29_R05_20261025/source/`; existing Blueprint evidence is in the corresponding `blueprint/` folder. Their exact source identities are repeated in the R07/R08 source mapping and review records included here.
- Candidate: **R09**, `0139_R09.docx`; SHA-256 `1deaf540425e38b4ad0017e6cf6a90057dc372cf5af69bbe27346c7ac834df5e`; 116,371 bytes.
- R09 is derived from R08 SHA-256 `d31ef2d8b8615f3dd314572c4e50b6604198e8f24faafb144bcbaea7373c696f` by changing exactly one body paragraph in `word/document.xml`. No data, formula, sample register, or other OOXML package part changed.
- R09 changes the ACT-03 statement that previously claimed a synthetic L-2 rating. It now says the employment evidence has not been rated and points to the Section 9 limitation. The independent delta reviewer marked the core correction PASS and recorded two nonblocking wording notes; see the raw response and adjudication.
- R08's complete-body OpenCode review is the baseline; R09's independent OpenCode review covers only the ACT-03/§9.2 delta. Together with the one-paragraph package diff, this is not represented as a second fresh full-body review.
- Technical: ZIP integrity PASS; exactly one paragraph changed; all other package members byte-identical; synthetic register unchanged; inherited arithmetic unchanged and independently recalculated in the R08 review.
- Word/visual: Word 16.0 read-only export PASS, 23 pages. R09 page 13 was directly inspected; pages 1–12 and 14–23 are pixel-identical at 118.8 dpi to the corresponding R08 pages previously directly inspected.
- All values remain SAMPLE/SYNTHETIC. REAL evidence is UNKNOWN/HOLD. Formal acceptance is NOT_GRANTED. No association approval, achievement, signature, or third-party source is asserted.
- Antigravity's earlier R08 response is not used for the R09 acceptance because its actual serving model was UNKNOWN. R09's scoped independent review used OpenCode v2 with actual provider/model `opencode/glm-5.3-flash-free`, reported cost USD 0.