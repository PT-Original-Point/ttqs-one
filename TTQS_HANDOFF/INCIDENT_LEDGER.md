# TTQS_ONE incident ledger

## INC-20261004-ANTIGRAVITY-WRITE-DENIAL

- **Classification:** executor permission-route defect; no provider quota evidence.
- **Severity/status:** mitigated locally; production exact-file route verification pending first real E2E.
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


## 2026-10-04 22:06 +08:00 - production route verification

The scoped write correction passed its first real CLI write: work `WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194` used only its exact isolated `content.json` target; the run receipt records permission scope readback and removal/readback PASS, model attestation, CLI exit 0, and official usage before/after. The generated payload and DOCX did not pass the evaluator-facing static gate (English SAMPLE/SYNTHETIC leakage and missing first-page timing), so no layout, review, promotion, or cost sample qualification occurred. Exact candidate and receipts are retained. The single-worker supervisor moved to 0032 under a fresh exact-file lease; no parallel Antigravity worker is active.
