# DOCX 0040 R05 — semantic review disposition

**State:** candidate only. Technical and primary visual checks passed; the independent exact-SHA semantic review returned **PARTIAL**. R05 is preserved unchanged as the reviewed parent; no promotion or formal acceptance is granted.

- Official requirement: I08-E03 / evidence-table sequence 040; training-institution evidence table PDF p.3.
- R05 candidate SHA-256: `95531ac5f8a79eed7c605f3ab1f42da3948e8f15316499d325b606bd6d434384`; it remains byte-identical to the reviewed artifact.
- Independent verdict: PARTIAL — see `evidence/qa/0040_semantic_review_r05_crossreview_raw.md` and normalized receipt `evidence/qa/0040_semantic_review_r05_exact.json`.
- Reviewer raw-response SHA-256: `4c0cb2d6ba44a232d1aa5eb6707820893d56b9a78fd3da0f8a15e12c981e03df`.
- R05 findings: (1) add a usable original-evidence identifier and file/attachment/page field to the p.3 matrix and p.5 D04 example; (2) separate the p.1 30-day authorization rule from the p.6 D04 rescore status in the synthetic register; (3) correct core properties that still identify the file as R04/revision 4.
- R05 technical receipt: PASS; primary visual review of all eight pages: PASS. Those results do not override the semantic PARTIAL.
- R05 remains `CANDIDATE_NOT_PROMOTED`; formal acceptance is `NOT_GRANTED`.

The findings are being addressed in a new R06 candidate with changes limited to those specific locations and document properties. No other R05 content is silently promoted or overwritten.
