# TTQS_ONE permanent worklog

## 2026-10-04 21:14 +08:00 — Antigravity scoped-write recovery

- Synced and read R03 from branch ttqs-win10-handoff-20261002 at base commit ce76270e15a9ff0466615190f0df2a98e2fb466a.
- Confirmed 0026, 0027, and 0028 failed because the headless CLI had no write_file allow rule while request-review required approval that could not be shown in headless mode. Gemini 3.8 Flash High was attested in each session; no structured quota error or stable content payload was produced.
- Rebuilt the 203242 smoke receipt offline using the retained raw session stream, CLI permission log, file bytes, SHA256, and official quota readbacks. All 13 checks pass. No Antigravity call was made for recorder repair.
- The existing smoke used a dedicated smoke-directory permission. The production runner is narrower: one exact content.json file rule for one work ID under WORK/CONTENT_PAYLOADS, with pre-dispatch permission readback and remove/readback in the completion/failure/timeout path. The production exact-file rule remains unverified until the first real E2E build.
- 0033 completed before the scoped-write fix. Marked PRE_SCOPED_WRITE_FIX_ATTEMPT=true and historical-only, parked exact lane, preserved its candidate SHA. It will not be retried.
- Salvage ordering now puts existing valid payloads/candidates ahead of any new model dispatch. 0042 is first because it has a valid payload without repair feedback and no candidate. Existing candidates are re-gated and lane-parked on deterministic/content review failure. Existing payload bytes are copied unchanged to a new host work directory; original evidence is retained.
- Reclassified unpromoted 0030 and 0033 as pending attempts, not cost samples. Qualified Antigravity cost samples remain zero; a distinct-family document qualifies only after full E2E and CURRENT publication.
- Current checkpoint: CURRENT=10; queue=128 PENDING, 7 DONE, 5 PARKED_ROOT_CAUSE_REPAIR, 2 PARKED_CONTROL; Antigravity max workers=1; no active Antigravity process; CLI permissions allow-list empty; hidden supervisor task verified but disabled pending durability readback.
- Next: commit and read back this worklog, incident ledger, raw evidence index, and checkpoint; then enable the hidden supervisor. Queue starts with 0042 no-model salvage and continues through one-worker R03 production.

Incident detail: INCIDENT_ANTIGRAVITY_WRITE_FILE_AUTO_DENIED_20261004.md
Raw evidence hashes and local paths: RAW_EVIDENCE_INDEX.md
Checkpoint: CHECKPOINT_ANTIGRAVITY_SCOPED_WRITE_20261004.md

## 2026-10-04 21:25 +08:00 — first salvage turn

- GitHub commit cf4c50f was fetched back from origin; normalized text readback matched all five durability files.
- Re-enabled and started the hidden Task Scheduler supervisor after that readback. Task state is Enabled=true, Hidden=true. It used one queue turn and created no Antigravity task.
- 0042 reused its persisted valid payload with byte-identical host copy SHA256 556fd26f04885e1895bbabbe6a62b42c3faf54ebb5b189c8e6e16378a5f62f73. The fixed renderer created candidate SHA256 22645a9e527efe51bfbf929eb029b23d2336845e42ac85df5fb36a0064edce15. Static gate failed on RAW_ENGLISH_SAMPLE_SYNTHETIC_LABEL_IN_BODY, FIRST_PAGE_30S_USE_CONTEXT_MISSING:user,timing, and DOCUMENT_CONTROL_STRIP_INCOMPLETE:version. No layout or reviewer step followed a static failure. Lane 0042 is PARKED_CONTROL; no model was called.
- Next queue target remains existing candidate 0030. Fresh Antigravity dispatch is withheld until the existing persisted-artifact salvage order is exhausted.
