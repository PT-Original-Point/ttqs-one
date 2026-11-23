# 0112 / I18-E21 R11 candidate status

- Candidate DOCX SHA-256: `0cfb3d594b5ad13dbe6edd9f4c42feb38488938821736d621b23835a554908b0`.
- Source commit read back: `dd7eaaddc09b5cee4f42aa5536a4059b3190da5c`.
- Correct synthetic mapping: F001/F003/F005 for certification P1/P2/P3; F002/F004/F006 for retraining P1/P2/P3.
- Deterministic DOCX checks: ZIP integrity, 17 tables, table minimum 9.5 pt, body minimum 10.5 pt, table row width <=17.7 cm, fact IDs, I18-E21 binding, sample notices and arithmetic passed.
- Visual: BLOCKED. `render_docx.py` found no bundled `soffice.exe`; Microsoft Word rendering was not attempted because 23 pre-existing automation processes have unknown owners. No page images/PDF exist.
- Independent exact-SHA semantic review: PENDING. OpenCode free route returned HTTP 429; Antigravity delta returned no text after a denied `run_command`; permission was not bypassed.
- Status: CANDIDATE only; not REAL, not formally accepted, not quality accepted.
- Next legal action: obtain a safe visual-render route and independent exact-SHA review without reusing the denied Antigravity directory or paying for OpenCode.
