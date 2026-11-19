# DOCX 0057 Blueprint R06 — deterministic change audit

Snapshot: 2026-10-18 +08:00. Candidate: `inputs/0057_UNIQUE_BLUEPRINT_R06.md`, SHA-256 `f724c2c46b44667988bab125bd30297728cf8e743a6d5ef6109fd5e452cccab6`. Source R05 SHA-256 `efdfcfa52a4b7338ae7688e118f6b700cf1e6f4ee3ef423aa89ac3f253bc3f95`. Patch SHA-256 `cbe2fb44982c4000bd0de11cdcb4b3bd04c5ca1d609922488d389f68cb33ae1c`.

## Deterministic checks — PASS

- R01–R05 source files retain their previously recorded exact SHA-256 values; R05 matches the required input SHA before and after the R06 build.
- R05→R06 `git diff --no-index --unified=0` contains exactly six hunks: title; current R06/R05 historical notes and R04 heading demotion; §0 provenance summary; §12.2 date rationale; `SF-0057-191` rationale; closing marker. All other lines are unchanged. No hunk touches the T1 schema, example, cutoff note or any other analysis/register content.
- Current title, R06 bounded-repair note, R05 historical note, R04 historical note, §0 chronology, and closing marker consistently identify R06 as current. Historical R04 feature labels remain intact.
- The two changed date-rationale locations now state one calendar month. Adding one calendar month to `2025-03-15` yields `2025-04-15`; the elapsed interval is 31 days. Both original dates and all other calculations/register values remain unchanged.
- Old phrases `訓練後 30 天內首次應用` and `訓練後 30 天內` occur zero times in R06. The exact replacement phrase occurs 3 times (R06 note, §0, and `SF-0057-191`); the shorter phrase occurs 4 times, including §12.2.
- Register has 232 data rows, 232 unique sequential IDs `SF-0057-001`–`SF-0057-232`, ten cells per row, and no added or removed IDs.
- DOCX 0057 does not yet exist. This candidate is a Blueprint sidecar only; no DOCX was created or edited.

## Writer receipt cross-check

OpenCode v2.0.29 used `opencode/deepseek-v4.1-flash-free`, session `ses_eb5614d98ffeRtQxbpElM1jc3t`, CLI exit 0. The build receipt's phrase counts are correct: the full replacement phrase appears 3 times; the shorter phrase appears 4 times including §12.2. A follow-up count-check was stopped after this was confirmed; no candidate or receipt edit was made. Writer stdout and the session export are retained beside this record.

## Status and limits

R06 passes this deterministic delta audit only. The fresh exact-SHA semantic review is pending. Prior R05 review limitations remain: historical 142-registry readback is a promotion HOLD; official binary/PDF and neighboring documents were outside the prior review scope; there is no DOCX visual/layout acceptance or association approval. This record does not grant semantic PASS, formal acceptance, or production status.
