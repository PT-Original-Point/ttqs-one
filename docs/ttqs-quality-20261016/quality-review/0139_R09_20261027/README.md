# 0139 R09 candidate package

This package contains the current repair candidate and the evidence needed to inspect its source mapping, one-paragraph correction, Word render, visual scope, and independent review.

**Current artifact:** DOCX 0139 / official requirement I19-E29 / Unique Blueprint row 153, revision R09, SHA-256 `1deaf540425e38b4ad0017e6cf6a90057dc372cf5af69bbe27346c7ac834df5e`.

**Status:** CANDIDATE. The R08 synthetic L-2 contradiction with §9.2 was removed. The R09 delta review returned PASS for its stated scope, with two nonblocking wording notes. Word rendered 23 pages; the changed page 13 was directly inspected, and the 22 unchanged pages render pixel-identically to the directly inspected R08 baseline. The 34-row synthetic replacement register and calculations are unchanged.

**Truth boundary:** SAMPLE/SYNTHETIC only; REAL=UNKNOWN/HOLD; formal acceptance NOT_GRANTED. This package does not assert association decisions, real outcomes, approvals, or signatures.

See `SOURCE_MAPPING.md` and `receipts/` for exact source/artifact hashes, worker request/output/session evidence, repair, technical and visual receipts, and the exact review scope. `history/R08_parent/` is explicitly historical and contains the prior R08 defect; do not treat it as current.

The first R09 previsual wording was rejected for awkward wrapping; the retry and an unrelated in-place file-write PermissionError are recorded in `receipts/R09_PREVISUAL_ITERATION_RECORD.json`. No unknown process was terminated. The final file was rendered from a separate path.