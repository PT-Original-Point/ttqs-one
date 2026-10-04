# Incident: Antigravity `write_file` auto-denied

**Project:** TTQS_ONE
**Date:** 2026-10-04 (Asia/Taipei)
**Model:** `gemini-3.8-flash-high`
**Official CLI:** `C:\Users\J\AppData\Local\agy\bin\agy.exe` (`1.2.16`)
**Status:** isolated smoke-directory write smoke PASS; production now uses a narrower exact-`content.json` permission lease. The production exact-file route has not yet been exercised by a real build.

## Affected attempts

| Work ID | Time (+08:00) | Session | Requested path | CLI result | Official usage before → after |
|---|---|---|---|---|---|
| `WF_ANTIGRAVITY_BUILD_0026_20261004_200104_127924` | 20:01:09–20:03:50 | `e1c758b8-e80b-4187-b157-aeecab2f82b2` | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0026_20261004_200104_127924\content.json` | model success; result listed denied `write_file`; no stable payload | 5h 96.9653%→95.8389%; weekly 82.2672%→82.0794% |
| `WF_ANTIGRAVITY_BUILD_0027_20261004_200504_335945` | 20:05:09–20:07:02 | `96441c0a-7373-4e59-b5be-4e0d608768cf` | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0027_20261004_200504_335945\content.json` | model success; result listed denied `write_file`; no stable payload | 5h 95.8389%→94.9937%; weekly 82.0794%→81.9386% |
| `WF_ANTIGRAVITY_BUILD_0028_20261004_200905_192617` | 20:09:19–20:11:42 | `64a68aff-c709-4bb5-8c3a-814ce4e734ad` | `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0028_20261004_200905_192617\content.json` | model success; `write_to_file` ERROR; no stable payload | 5h 94.9937%→93.9465%; weekly 81.9386%→81.7640% |

Exact 0028 rejection from the session stream:

```text
permission check failed for write_file "E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0028_20261004_200905_192617\content.json": user denied permission for write_file(E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0028_20261004_200905_192617\content.json)
Do not attempt to circumvent this denial by rephrasing the command, using alternative tools/scripts (e.g. python, sh, curl), or accessing the same target resource. Proceed without performing this action.
```

The headless CLI also reported that `write_file` could not be prompted for and was auto-denied. For these three attempts, `permission_mode=request-review`, CLI `settings.json` was absent, and initialized permissions were nil. The shared config's other grants did not provide a job-directory `write_file` allow rule. Actual model was attested as `gemini-3.8-flash-high`; all three receipts show no structured provider quota error. This was an executor permission-route defect, not a content or provider-quota defect.

## Root cause and correction

**Root cause:** headless CLI defaulted to `request-review`; without a scoped `permissions.allow` rule it cannot display an approval prompt, so its file tool was denied. The affected requested paths had no corresponding exact-directory allow rule.

**Correction:** the supervisor now adds one temporary `write_file(<exact work directory>/content.json)` rule in `C:\Users\J\.gemini\antigravity-cli\settings.json` for a work directory that is a direct child of the official `WORK\CONTENT_PAYLOADS` staging root and whose directory name equals the work ID. It reads back that sole write grant before dispatch, refuses any pre-existing write grant/deny, removes the exact grant at completion/failure/timeout, and reads back removal. The grant is serialized through one active worker lease; it never includes `E:\`, `E:\TTQS`, runtime root, `CURRENT`, queue, or supervisor. The Antigravity prompt permits only reading the exact task packet and one write to that job's `content.json`. Host-side response-to-file fallback was removed; missing or denied file output fails the lane. The official CLI permission guide documents `write_file(/path)` as an exact target rule and Windows path normalization [Antigravity permissions](https://antigravity.google/docs/permissions/).

## Exact write smoke

- **Smoke:** `ANTIGRAVITY_WRITE_SMOKE_20261004T203242`
- **Session:** `8a7e0271-926d-49a7-affb-cfad44976ab3`
- **Requested path:** `E:\TTQS\TTQS_ONE_ANTIGRAVITY_WORK\ANTIGRAVITY_WRITE_SMOKE_20261004T203242\content.json`
- **Only allowed path during smoke:** `write_file(E:/TTQS/TTQS_ONE_ANTIGRAVITY_WORK/ANTIGRAVITY_WRITE_SMOKE_20261004T203242/)` (isolated smoke directory; production is now narrower at the exact file path).
- **Permission evidence:** CLI log confirms that isolated smoke allow rule loaded while `toolPermission=request-review` remained in force.
- **Model response:** `TTQS_ANTIGRAVITY_WRITE_READY`
- **Actual model:** `gemini-3.8-flash-high`
- **Direct tool write / file exists / host readback / JSON parse / exact content:** PASS
- **SHA256:** `A7F7CA8DC77F764ADEA240189C544535514E4BD92F3FDB283DEFD0B39B3CE59A`
- **Official usage before:** 5h 87.4183%; weekly 80.6760% (20:32:50)
- **Official usage after:** 5h 87.3141%; weekly 80.6586% (20:34:16)
- **Structured quota error:** none
- **Broader permissions / skip-permissions:** not used
- **Smoke receipt:** `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_WRITE_SMOKE_20261004T203242.json`

The separate 0033 job that was already running was allowed to finish. It produced a host-persisted payload under the old response-return contract, then failed deterministic static gates for an English synthetic label and missing first-page user/timing context. Its queue item and build receipt are now marked `PRE_SCOPED_WRITE_FIX_ATTEMPT=true` / historical-only; its candidate bytes remain unchanged and it will not be retried.

## Salvage and single-worker resumption

- Current count is 10 DOCX. Queue has 128 pending items after 0033 was parked.
- Existing payload inventory: 0030, 0033, 0042, 0044, and 0050 pass host payload validation; 0047 fails `CONTENT_SOURCE_EXACT_READBACK_NOT_TEXT` and has no candidate; 0048 has no payload. 0042 is the clean no-feedback payload and is prioritized for renderer → static → layout → fresh Codex review → CURRENT salvage. Existing candidates are re-gated before any new content dispatch; failed existing artifacts are parked lane-local. Existing payload bytes are copied exactly into a new host work directory so prior payload/receipt evidence remains intact.
- Pending content attempts 0030 and 0033 were incorrectly counted as cost samples even though neither reached CURRENT. They remain in the quota ledger as attempt evidence and have been removed from the qualified sample count. Only a distinct-family document that passes review and is published to CURRENT counts toward the three-document cost sample.
- Antigravity concurrency remains 1. No OpenCode/Muse request is part of this recovery.
- At this checkpoint the hidden supervisor task is still disabled; it will be resumed only after the local checkpoint and GitHub durability readback are complete. No Antigravity process is active and the CLI settings allow-list is empty.

## Production disposition

Production was paused while the smoke was run. The direct-write smoke passed. The supervisor remains limited to one Antigravity worker; the exact-scoped write route is now enabled for the next READY production lane. Existing queue, candidates, CURRENT, and checkpoints were preserved.


## 2026-10-04 22:06 +08:00 - production route verification

The scoped write correction passed its first real CLI write: work `WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194` used only its exact isolated `content.json` target; the run receipt records permission scope readback and removal/readback PASS, model attestation, CLI exit 0, and official usage before/after. The generated payload and DOCX did not pass the evaluator-facing static gate (English SAMPLE/SYNTHETIC leakage and missing first-page timing), so no layout, review, promotion, or cost sample qualification occurred. Exact candidate and receipts are retained. The single-worker supervisor moved to 0032 under a fresh exact-file lease; no parallel Antigravity worker is active.
