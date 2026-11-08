# 0133 I19-E22 R07 candidate package

**State:** CANDIDATE. This package does not claim REAL evidence or formal TTQS acceptance.

## Candidate and repair

- Candidate: `candidate/0133_I19-E22_CANDIDATE_R07.docx`
- Candidate SHA-256: `a8cc1a7740c854fc3cad1dfa229bc829d54d12153b477c7049aafc5e62e0bfb2`
- Parent R06 SHA-256: `cceae5b8781fe503bd15993409ba616adb53a99d9923816d44afe019ee48b821`
- W1 (OpenCode v2 CLI, selected route `opencode/beam-free`) changed only four Table 10 locator cells. The raw process output, work package, dispatch start and terminal status are retained under `worker_review/w1_opencode_scoped_repair/`.
- Deterministic QA passed: the DOCX ZIP CRC is valid, only `word/document.xml` changed, the four target rows are unique, and no other cell text changed.

## Review and rendering

- The parent R06 full-document review was `PASS_WITH_MINOR` on the parent SHA. Its two minor locator findings were the exact scope repaired here; the parent review is retained under `history/` and is not represented as an R07 full-document review.
- W2 returned `PASS` for a fresh, exact-R07-SHA semantic review of all four repaired locators and their section contexts. No full-document re-review or formal acceptance is claimed. The raw W2 stream, response, input packet and dispatch receipt are retained under `worker_review/w2_antigravity_scoped_review/`.
- Microsoft Word COM 16.0 rendered 12 pages. Compared with R06, pages 1–10 and 12 are byte-identical; page 11 was visually inspected and all four updated locators fit their cells without clipping, overlap or pagination change.
- Actual Antigravity serving model identity is UNKNOWN. `gemini-3.8-flash-high` is the requested route only.

## Evidence boundaries

The R07 semantic review is scoped to the four locator repairs. REAL organizational records remain unverified. This candidate is not formally accepted, approved or promoted.
