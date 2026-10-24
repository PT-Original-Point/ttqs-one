# R09 current disposition — 2026-10-22

This is a short current-state addendum, not a completion claim. Its **pre-sync observation** was made at PR #92 branch HEAD `95d7c2e856f70cfb883d186aee1c87d1c2720370`; R09 source file Git blob `4c7eff55748ff265b1e5a7d1122852b0d101acbd`.

## Windows / scheduler / panel

- Native Goal readback is **PAUSED**. No `/goal resume` was executed, and the Goal API exposes no paused-reason detail in this readback.
- `automation_update(mode=view)` only rendered the existing task card; it returned no schedule ID/configuration, interval, last/next run, or local-path capability. The Windows task `TTQS_ONE_Codex_Supervisor` is **Disabled**; last recorded run is 2026-10-05 05:03 +08. Do not treat the task's reported next-run field as an enabled trigger. A live 120-minute schedule and natural trigger are **UNKNOWN**.
- The tested dashboard is the legacy `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\MASTER\dashboard.html` (last modified 2026-10-05); listeners on ports 8765/8766 were absent and project/host/head freshness is not represented. Current panel alignment is **UNKNOWN / stale**.
- OpenCode PID 45628 is `opencode-cli.exe serve --service`, not a Writer session. No Antigravity CLI process was active in the snapshot. Nineteen `WINWORD.EXE /Automation -Embedding` processes remained; owners are UNKNOWN and none were killed or counted as document Writers.

## Document dispositions

- **0105 / I18-E13 R04:** DOCX SHA-256 `17f7d680cbb992db93a6f67df84415500050953eecf426b477f675810177b4cb`; technical QA 32/32 PASS; independent semantic review PASS on the exact SHA. Requested Antigravity model was `gemini-3.8-flash-high`; serving identity/fallback UNKNOWN. Word visual export is BLOCKED after three distinct bounded COM output methods; no R04 PDF/page images exist. Candidate remains unaccepted. The complete public package and failure evidence are in `quality-review/0105_I18-E13_R01_20261022/`.
- **0103 / I18-E10 R03:** SHA-256 `7b95524d9e0c0010ebd45938dad25afe2432e2d6f0c83bba4cafbf7d180375e2`; technical package checks PASS, visual `FAIL_REPAIRABLE_LAYOUT`, semantic review not requested, NOT ADOPTED. Existing PR evidence has the DOCX, Word PDF, and six contact sheets. The exact readback receipt is now synced; it records 30/30 Git blobs and 17/17 raw binary SHA-256 matches at its referenced commit.
- **0101 / I18-E08 R09 final9:** existing remote candidate SHA-256 `56f433e095f32378f2fd8241c1a27948d2bfe6748da003af5623d265885edb68` matches the local prepared package. It is reused; no rebuild is authorized or needed for this sync.

## Worker-window evidence

The prior retained rolling snapshot ended 2026-10-22 03:57 +08: OpenCode reported 38 session rows (not an invocation count), selected free-model IDs, 2,478,098 input / 330,727 output / 947,845 reasoning / 11,855,644 cache-read tokens, local cost 0, with serving identity and vendor billing UNKNOWN. Antigravity recorded 10 attempts, 3 CLI exit 0, 6 nonzero/error, 5 text returns, 149,265 known-token lower bound, 2 text calls with unknown tokens, zero direct DOCX, zero confirmed serving-model identities, and quota/billing UNKNOWN.

After that snapshot, 0105 added two OpenCode CLI attempts (first DeepSeek `finish=length`, zero output; second Mimo returned the manuscript) and two Antigravity CLI attempts (one `--print-timeout` parser error before a model result; one exit-0 semantic review with 46,557 reported tokens). The precise new rolling 24-hour aggregate is **not asserted** because the earlier window boundary and some native attempt start times do not support exact subtraction. Original prompts, raw responses, stderr, exits, tokens and receipts are retained with the 0105 package.

## T01–T14 disposition

Statuses below are from `r09_T01_T14_recheck_20261022.json`; they are guard-test outcomes, not proof that the whole Windows workflow is healthy.

| Test | Recorded status | Disposition |
|---|---|---|
| T01 | PASS_OBSERVED_SERVICE_NOT_WRITER | Applied: service PID is not classified as a Writer. |
| T02 | PASS_OBSERVED_NO_PROCESS_KILL | Applied: 19 owner-unknown Word processes preserved. |
| T03 | PASS_STALE_PANEL_DETECTED | Stale dashboard state recorded; live panel alignment remains UNKNOWN. |
| T04 | SIMULATION_ONLY | No live mismatched panel exists to observe. |
| T05 | FAIL_NOT_RESUMED_NATURAL_RUN_UNKNOWN | Goal remains paused; native 120m execution/resume remains unresolved. |
| T06 | PASS_OBSERVED_READY_DERIVED_FROM_SOURCE | Source-derived readiness is allowed without a READY queue label. |
| T07 | PASS_OBSERVED_LANE_ISOLATION | 0097 render failure did not stop the separate 0100/0101 lane. |
| T08 | PASS_GUARD_APPLIED | Exit 0 without a deliverable is not treated as a completed DOCX. |
| T09 | PASS_OBSERVED_BOUNDED_SALVAGE | Stable reviewer output was salvaged without rebuilding the DOCX. |
| T10 | PARTIAL_TEXT_ONLY_EXACT_PACKET_BINDING | Exact text packet binding exists; reviewer did not rehash the DOCX or inspect pages. |
| T11 | PASS_GUARD_MODEL_UNKNOWN | Gemini was requested, but actual provider/fallback and quota remain UNKNOWN. |
| T12 | PASS_SCOPED_SAMPLE_AND_QA | Prior sample candidate passed its recorded scope; no REAL/approval claim. |
| T13 | PASS_REMOTE_READBACK_COMMIT4_AND_0105_ABB10FC | Readback verified through commit 4 and 0105 commit `abb10fcb`: 84/84 changed-path Git blob IDs and 6/6 binary raw SHA-256 values match; R04 DOCX raw SHA-256 is exact. |
| T14 | PARTIAL_SAFE_PUSH_CASE_ONLY | No live competing Writer or ambiguous push was induced; unknown-push guard not live-tested. |

## Closure state

Resolved defects and stable evidence are synced below/alongside this addendum. The schedule/Goal, live panel, 0105 visual export, 0103 repairable layout, T04 live mismatch, T10 visual/hash scope, and T14 live race remain explicitly unresolved or untested. These are isolated blockers; they do not authorize a project-wide stop or a false `AUTONOMOUS_GOAL_WORK_RESUMED=PASS`.
