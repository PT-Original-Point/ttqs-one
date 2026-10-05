# TTQS_ONE incident ledger

## INC-20261004-ANTIGRAVITY-WRITE-DENIAL

- **Classification:** executor permission-route defect; no provider quota evidence.
- **Severity/status:** mitigated; exact-file route passed a real production write/readback/removal cycle. That document failed content gates and did not qualify as a production cost sample.
- **Affected work:** 0026, 0027, 0028; 0033 is separately classified as pre-fix historical work.
- **Cause:** Antigravity CLI headless mode used request-review, but no interactive approval prompt was available and no matching write_file allow rule existed.
- **Evidence:** actual model gemini-3.8-flash-high; structured provider quota error absent; exact denials and before/after official usage are indexed in RAW_EVIDENCE_INDEX.md.
- **Smoke:** isolated smoke-directory permission produced content.json; host readback, JSON parse, expected content, SHA256, model attestation, and before/after usage checks passed. The receipt was reconstructed offline from raw evidence after a recorder bytes-serialization error. No smoke rerun.
- **Correction:** exact per-work content.json permission in official WORK/CONTENT_PAYLOADS staging only; exact allow-list readback before dispatch; fail closed on any pre-existing write allow/deny/ask rule; remove and read back the temporary permission after each work. No broad write permission and no skip-permissions flag.
- **0033:** PRE_SCOPED_WRITE_FIX_ATTEMPT=true; historical-only; candidate bytes retained; no retry.
- **Quota sample accounting:** 0030 and 0033 did not reach CURRENT and are retained as pending attempts, not production cost samples. Qualified sample count is zero.
- **Production control:** one Antigravity worker. Existing payload/candidate salvage precedes new work; first no-model salvage target is 0042. Hidden supervisor must remain disabled until repository durability readback, then may resume.
- **Owner/action:** Codex host control and promotion; next proof is one exact-file-scoped Antigravity production build through content validation, renderer, static/layout, fresh independent Codex review, and CURRENT.
- **References:** INCIDENT_ANTIGRAVITY_WRITE_FILE_AUTO_DENIED_20261004.md; RAW_EVIDENCE_INDEX.md; CHECKPOINT_ANTIGRAVITY_SCOPED_WRITE_20261004.md.


## 2026-10-05 04:28 +08:00 — scoped-write follow-up and recorder readback

- **Production route:** `WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194` proved the exact isolated `content.json` rule was loaded and removed/read back after use. Actual model was `gemini-3.8-flash-high`; there was no structured quota error. Its output failed deterministic content gates and did not promote.
- **Later attempt:** `WF_ANTIGRAVITY_BUILD_0037_20261004_221108_567364` also records exact write-scope and removal readbacks, but the CLI marked the response `ERROR` after an output-token-limit interruption. Its stable payload omits required schema and is rejected as `CONTENT_SCHEMA_INVALID`; no candidate or CURRENT promotion exists. This is output incompleteness, not a permission denial or quota event.
- **Recorder:** no model call was made. The repaired recorder was run against the original smoke evidence offline; 13 checks passed, generated receipt bytes matched the previously stored receipt hash, and the quota ledger retained a single smoke row. The receipt serialization issue is closed as a logging-control defect.
- **Smoke remains** based only on the original isolated smoke. It was not repeated. The allow-list is empty after cleanup. Work `0033` remains pre-scope historical-only and is not retried.
- **Successful recovery artifact:** 0042 used existing content and no Antigravity call; exact candidate SHA `47bddaa2ba7d19f8401676553a37ba9aeb5878166e54276bdcbf1bfe3ab583d0` passed static, layout, and fresh semantic review, then was published to CURRENT. This does not count as an Antigravity cost sample.
- **Resumption:** after GitHub fetch/readback of this update, re-enable only the existing hidden `wscript.exe //B //NoLogo` supervisor task with one worker and one-document wake; keep every gate unchanged.


## 2026-10-04 22:06 +08:00 - production route verification

The scoped write correction passed its first real CLI write: work `WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194` used only its exact isolated `content.json` target; the run receipt records permission scope readback and removal/readback PASS, model attestation, CLI exit 0, and official usage before/after. The generated payload and DOCX did not pass the evaluator-facing static gate (English SAMPLE/SYNTHETIC leakage and missing first-page timing), so no layout, review, promotion, or cost sample qualification occurred. Exact candidate and receipts are retained. The single-worker supervisor moved to 0032 under a fresh exact-file lease; no parallel Antigravity worker is active.


## INC-20261004-CODEX-REVIEW-EXECUTION-TIMEOUT-0031

- **Classification:** isolated Codex semantic-review execution timeout; no document mutation and no promotion.
- **Evidence:** first review ran 22:33:02–22:58:02 +08:00 and exited 124 at its 25-minute bound; exact candidate SHA `756deaa32c1f159b4a0aeaf2ca75fbf376fcff3bb460e90dd612616490cf87a5` unchanged; required review JSON absent.
- **Queue recovery:** lane 0031 is `PENDING` with `review_only_retry=true`, preserving the existing candidate and payload.
- **Mitigation:** one exact-SHA review-only retry started at 23:03:55 +08:00 with a 45-minute timeout; no semantic or deterministic gate changed; no Antigravity request.
- **Current status:** retry still active at checkpoint time `2026-10-04 23:05:32 +0800`; no CURRENT change.


## 2026-10-05 06:54 +0800 - follow-up: scoped Antigravity write route and offline recorder verification

This addendum closes the current evidence readback for the original `ANTIGRAVITY_WRITE_FILE_AUTO_DENIED` incident; it does not claim a production sample or promotion. The prior incident entry retains the 0026/0028 denials, the pre-fix 0033 attempt, denial evidence, and the initial root-cause and permission records.

- Smoke was not rerun. Existing receipt SHA256 `be4302b9962c4aebc3066e439600ac469e0f0355d0c65daecce7dfbf788dea18` still records 13/13 checks PASS; recorder serialization was corrected to serialize decoded evidence text and scalar metadata rather than raw bytes; the deterministic receipt was regenerated and verified offline from retained raw evidence.
- The currently read permission settings are empty; latest lease status is `PERMISSION_REMOVED`, exact target readback matched its one `content.json` grant, and removal readback is true. Recovery found no stale TTQS rule. No broad E: or runtime grant was added.
- The official CLI remains pinned at absolute path `C:\Users\J\AppData\Local\agy\bin\agy.exe`, version 1.2.16; route identity is `gemini-3.8-flash-high`; fallback is disabled and worker cap is one. This turn made no Antigravity model request.
- 0054's later semantic review failure is a document-content issue and is not reclassified as a write-permission incident. It remains unpromoted at exact candidate SHA `0c799e810621357b2e2dc495ea93f37d3499c64ea2aeaf3ef1329ec745a2ca05`.


## 2026-10-05 07:32 +0800 — verification follow-up

No new write-permission incident occurred in this follow-up. The R03 local-native route and one-file lease remain as previously documented; the retained smoke receipt still records 13/13 checks PASS and was not rerun. The latest lease (0055) is removed with exact readback, and CLI settings remain empty. Work 0033 is historical pre-fix work and was not retried.

The 0054 R06 work is host-side salvage of a persisted payload, not a permission test or a new Antigravity request. It passed static and hidden layout checks but remains unpromoted pending a fresh independent review. Current remains 14 DOCX. Exact artifact evidence is indexed in `RAW_EVIDENCE_INDEX.md`.

## 2026-10-05 12:25:02 +08:00 — workflow integration readback

- The earlier 0026/0027/0028 auto-denials and recorder serialization issue remain classified as executor permission/logging-control defects, not provider quota failures. Existing smoke evidence remains valid; it was not rerun.
- Integration is now verified by 22/22 offline cases, including the actual supervisor content-validation entrypoint rejecting a persisted 0013 prompt leak; 0 live model calls were made by this verification. Exact-write automation remains fail-closed and owned by the Master dispatcher. No broad permission was granted.
- 0033 remains PRE_SCOPED_WRITE_FIX_ATTEMPT=true, historical-only. Current production cost-sample count remains zero; a successful isolated smoke or a payload that later fails content gates is not a successful sample.
- Dispatch ownership changed to Master-only under the current workflow policy. This supersedes any earlier note suggesting the local scheduled supervisor should resume Antigravity auto-dispatch. No scheduler or lease state was changed here.
- Supporting source snapshots, test receipt, hashes, and usage/evidence limitations are in TTQS_HANDOFF/WORKFLOW_GUARD_INTEGRATION_20261005/ and RAW_EVIDENCE_INDEX.md.
