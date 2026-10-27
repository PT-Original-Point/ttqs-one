# DOCX 0139 · I19-E29 · R08 candidate

**Artifact state:** CANDIDATE (not formal acceptance)  
**Official requirement:** I19-E29, official evidence table page 9: 「證照通過率高及就業率大幅提升。」  
**Unique Blueprint:** index 153; Blueprint SHA-256 `090169968e3df59a6cecaac665a99b2cb625a9cbc355bf84528d08b27c98052a`  
**Source packet SHA-256:** `3c9c310e086a86c03d38bea68bba1ca53bcb2fc927d8949fb6b91c45379d9d47`  
**Printed checkbox serial:** UNKNOWN; it is not inferred from the document ID or Blueprint index.

## Candidate and repairs

DOCX SHA-256: `d31ef2d8b8615f3dd314572c4e50b6604198e8f24faafb144bcbaea7373c696f` (116,372 bytes). It is a minimal R07-derived repair: three formula-parenthesis corrections, the QC-08 synthetic-register key correction to `KEY-DATE-001`, and the visible revision label R08. The R07 parent SHA-256 is `9e9f65b962f2a6b0e3b1a14c8d4615b6a70c98b140d672943adb5de636843241`. Only `word/document.xml` changed; the failed earlier ElementTree serialization is retained locally and is not part of this candidate.

The formula checks now read `(4 + 2)/10 = 6/10 = 60.00%`, `(7 + 2)/12 = 9/12 = 75.00%`, and `(8 + 2)/12 = 10/12 = 83.33%`. All illustrative data remain SAMPLE/SYNTHETIC; real association performance is `UNKNOWN/HOLD`; formal evaluation acceptance is `NOT_GRANTED`.

## QA evidence

- Static package, XML/ZIP integrity, direct font floors (body 10.5 pt; table 9.5 pt), formula/key checks: PASS.
- Microsoft Word 16.0 native read-only export: 23-page PDF, PASS; PDF SHA-256 `0f9d1408082dcb14871c3f2d01a3c5989fe3e230cb6825747da30dc9aa75ebe7`.
- Visual: all 23 R08 pages directly inspected; PASS. Pages 8, 22, and 23 contain the changed text and are included as page-image evidence. R07-to-R08 pixel equivalence is not asserted because R07 rasterizer configuration was not recorded.
- Independent reviewer: exact-R08-SHA `PASS_DELTA`, zero blockers, verified the repaired formulas, dictionary key, visible version and retained SAMPLE/REAL boundary. The requested model was `gemini-3.8-flash-high`; actual serving model is `UNKNOWN`, as is fallback state. The CLI wrapper failed to capture a trustworthy exit code; the provider transcript response was recovered from the same conversation and its exact SHA is recorded. This is not a full-body re-review or formal acceptance.

See `receipts/` and `worker/` for the exact repair, static, Word, visual, and reviewer scope/evidence. `candidate/SYNTHETIC_REPLACEMENT_REGISTER_34_ROWS.md` records all 34 inherited synthetic rows.