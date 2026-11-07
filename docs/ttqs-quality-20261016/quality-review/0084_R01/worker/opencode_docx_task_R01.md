# OpenCode v2 task｜DOCX 0084 R01 content + Word build

Use only these authoritative inputs for this task:

1. `inputs/UNIQUE_BLUEPRINT_0084_R02.md` (exact SHA-256 is recorded in the blueprint review receipt).
2. `inputs/SOURCE_PACKET_0084_R01.md`.

Do not perform a repository-wide search, load unrelated project history, or change any other document/control file. The source packet contains the official 090 / I17C-E03 binding, official 17c source, 17c/17d boundaries, and exact 0083 synthetic cross-document anchors. Follow Blueprint R02; where its values differ from the old task files, R02 controls. Do not repeat the earlier R01 inconsistency.

## Deliverables

Write the full evaluator-facing document body and create a real editable Word file:

- `candidate/0084_R01_body.md`
- `candidate/0084_R01.docx`
- `worker/build_0084_R01_docx.py`
- `evidence/build_receipt_R01.json`
- `evidence/synthetic_replacement_register_R01.csv`

Keep all generated files inside `docs/ttqs-quality-20261016/quality-review/0084_R01/`. Preserve input files. Do not promote, submit, publish outside the existing PR branch, mark formally accepted, or claim real execution.

## Content requirements

- Implement the full 17-section Blueprint R02 and appendices. Include the quick-start, task-specific B1–B4 behavior dictionary and per-level anchors, workflow, form field instructions, completed synthetic observations, fact-based feedback, learner response/next action, N/O and disagreement handling, official 17c `UNSCORED` map, 17d exclusion, privacy rules, explicit hold/return/reject/reverify decisions, clean reusable blank Form-O, and 46-entry atomized synthetic replacement register.
- The completed example must be operationally coherent at every field. Each rating must be supported by same-observation facts and a locator; prompts, valid opportunities, dates and individual rating anchors must match Blueprint R02.
- Keep `0084` (DOCX ID), `I17C-E03` (requirement ID), and `090` (official checkbox serial) distinct. Keep `SYN-0084-B01` (local observation form ID) distinct from linked source case `SYN-0083-B01`.
- Use the exact shared anchors: `LRN-B01`, `SYN-COURSE-0083-B`, course end `2026-03-06`; 0083 baseline 4, T1 3/4 at `2026-04-03`, T2 cumulative 7/8 at `2026-05-01`, T3 cumulative 10/12 at `2026-05-29` (83.3%); `AID-01` requested `2026-04-03` and provided `2026-04-13`; `AID-02` remains requested/pending; 0083 remains `PARTIAL` and its evidence locator/authorization remains `PENDING`. These event counts are not behavior ratings and cannot be used as behavior evidence.
- Use Blueprint R02 observation ratings exactly: O0 `2026-03-05`: B1=1, B2=1, B3=1, B4=N/O; O1 `2026-04-13`: 2/2/2/2; O2 `2026-05-01`: 2/3/3/2; O3 `2026-05-29`: 3/3/3/3. All are newly authored synthetic observations, not data found in 0083. Preserve the separate opportunity and feedback notes in R02.
- Recompute only ordinal direction counts, never sum/average the ratings: 16 possible cells, 15 valid, one N/O; B1–B3 have 9 paired comparisons (9 higher, 0 unchanged, 0 lower); B4 has zero paired comparisons because O0 is N/O. No percentage for a zero denominator, no causal claim.
- Mark every new person/role, score, observation note and feedback `SAMPLE/SYNTHETIC`; `NOT_EXECUTED`; `REAL=UNKNOWN/HOLD`; `FORMAL_ACCEPTANCE=NOT_GRANTED`. No names, signatures, actual supervisors, association approvals, clients, private health data, third-party originals, or claimed policy/adoption.
- Treat the official 17c 0–3 institutional evidence scale as an unscored reference only; never put those levels into individual B1–B4 ratings and never state that the association achieved a level. Do not turn the artifact into 17d outcomes.
- Avoid vague filler. Include concrete use steps, field-level examples, the actual tables and completed case decisions. The document must remain useful if the title is covered; do not merely restate the Blueprint.

## Word/layout and technical evidence

- Use readable Traditional Chinese, A4 pages, clear heading styles/TOC, page numbers, repeating table headers, non-splitting rows where feasible, and a visible but unobtrusive `SAMPLE / SYNTHETIC` watermark/stamp on example pages. Use landscape pages only for tables that need them and place headings with their tables; avoid orphan headings and a trailing blank page.
- Ensure the Word document is editable, opens with `python-docx`, has no truncated/empty required section, and extracted text corresponds to the Markdown body. Include exact SHA-256 for the body and DOCX in the build receipt. Record the Blueprint R02 SHA and all six source SHA-256 values.
- Do not claim visual PASS without an actual render and page inspection. If a bounded Word rendering attempt stalls, preserve the DOCX and report `BLOCKED_VISUAL_VERIFICATION` with the exact attempt/exit/time; do not loop or rebuild to refresh metadata.
- Technical/build self-checks are not independent acceptance. Do not write `PASS` for semantic or formal acceptance.

Return a concise result with the exact output paths and hashes. Use the existing OpenCode v2 CLI model `opencode/deepseek-v4.1-flash-free`; no Antigravity and no Computer Use.
