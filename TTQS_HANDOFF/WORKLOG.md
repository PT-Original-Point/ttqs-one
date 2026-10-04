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

## 2026-10-04 21:28 +08:00 — 0030 salvage gate

- 0030 reused its persisted valid content payload (SHA256 8049bb49fad917c628ec5aa97229b5ca742b7916e883af0dd245776c1b3ce731); no model call occurred.
- The fixed renderer produced candidate SHA256 c29bd40a3cb3c73b174e7477c41a59d71f36e3e10284268de26c806d0a25c334. The pre-existing candidate SHA256 3dd0bcd1549e9ff33478834e17e66a5546d424b14bf1fef155a397adba996998 is preserved under SUPERSEDED.
- Static gate failed on RAW_ENGLISH_SAMPLE_SYNTHETIC_LABEL_IN_BODY and FIRST_PAGE_30S_USE_CONTEXT_MISSING:timing. No layout/review/promotion followed; lane 0030 is PARKED_CONTROL. Next reusable candidate target: 0044.


## 2026-10-04 22:06 +08:00 - 0031 exact scope production run

- The first post-fix Antigravity production route was exercised by work `WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194`. The verified model was `gemini-3.8-flash-high`; CLI exit was 0; duration was 154.047 seconds; the content payload is stable and valid (SHA256 `c211dce8d4494e71092107ab45149ef6f3ec3d723a84b807c24968d8fc1e80f1`).
- Exact permission readback was `write_file(E:/TTQS/TTQS_ONE_CODEX_RUNTIME/WORK/CONTENT_PAYLOADS/WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194/content.json)`. The run receipt records pre-dispatch scope readback PASS and permission removal/readback PASS after completion. No broad allow rule was used.
- Official usage readback: five-hour remaining `76.4892%` before and `75.1647%` after; weekly remaining `78.8545%` before and `78.6337%` after. No structured quota error. Cost sample register still has zero qualified CURRENT promotions.
- Fixed renderer produced candidate SHA256 `045ef0b1033ad9aaed205c074396619db2da8dd9eed30aab2eac35a050ec16e9`. Static gate failed on `RAW_ENGLISH_SAMPLE_SYNTHETIC_LABEL_IN_BODY` and `FIRST_PAGE_30S_USE_CONTEXT_MISSING:timing`. No layout, semantic review, or CURRENT promotion followed. The exact lane has repair feedback and the content/candidate bytes are retained. This is not a successful production cost sample.
- Persisted-artifact salvage outcomes are now recorded for 0030, 0042, 0044, 0047, and 0050. 0030/0042/0047/0050 failed static review; 0044 passed static/layout but its fresh exact-SHA Codex review failed. None was promoted. 0033 remains historical-only.
- At 22:05:14 +08:00 the hidden scheduler dispatched the next single Antigravity task, `WF_ANTIGRAVITY_BUILD_0032_20261004_220508_165870`, with the exact-file scope under its own isolated directory. Its lease was ACTIVE at this checkpoint; no second model worker was observed.
- CURRENT remains 10 DOCX; queue snapshot is 121 PENDING, 1 BUILDING_ANTIGRAVITY, 7 DONE, 8 PARKED_CONTROL, and 5 PARKED_ROOT_CAUSE_REPAIR.


## 2026-10-04 23:05:32 +08:00 - 0031 fresh-review execution timeout and bounded retry

- Candidate `0031__專業訓練人員職能評估方法等證明_可直接使用成品.docx` remains byte-identical at SHA256 `756deaa32c1f159b4a0aeaf2ca75fbf376fcff3bb460e90dd612616490cf87a5`. It passed current static gate; hidden pagination reported 16 pages, no blank pages, and one sparse final page (112 characters).
- Fresh isolated reviewer `codex_cross_review_0031_20261004_223302` started at 22:33:02 +08:00 and reached its configured 25-minute execution bound at 22:58:02 +08:00 (exit 124). It produced no review JSON and did not promote or modify the DOCX. The lane returned to `PENDING` with `review_only_retry=true`.
- Reviewer output identified concrete traceability concerns: no current replacement-register rows shared the receipt fact IDs; several synthetic value locators did not match the body; the DOCX references “table 2/table 5” although the extracted OOXML has only the first-page guide table. These are review findings to resolve, not a verdict.
- A single exact-SHA review-only retry `codex_cross_review_0031_20261004_230355` is active in a hidden no-window process with a 45-minute timeout override. The candidate SHA and every quality gate are unchanged; Task Scheduler remains disabled, Antigravity is not dispatched, and its exact-file permission lease is removed.
- First reviewer transcript: `LOGS/20261004_223302__codex_cross_review_0031_20261004_223302.log`, SHA256 `32717e863f08ff5a76793363d716642eeb0429a2fcfb1d423d6ef7c7f3c5b2ca`.


## 2026-10-05 04:28 +08:00 — recorder offline verification, 0042 promotion, and scoped-write resumption

- Re-read the R03 handoff state and local runtime before resuming. The hidden Task Scheduler task `TTQS_ONE_Codex_Supervisor` is Disabled, Hidden=true, principal `J`, and its action is `wscript.exe //B //NoLogo` with `supervisor_hidden_launcher.vbs`; the wrapper starts one bounded supervisor turn with `--max-docs 1`. Antigravity CLI `settings.json` has an empty allow-list. No Antigravity process or Human Gate is active.
- No smoke/model invocation was made. Re-ran the already-fixed `record_antigravity_write_smoke.py` strictly offline against the retained stream, CLI permission log, actual smoke `content.json`, and official before/after usage snapshots. All 13 receipt checks passed. Deterministic receipt readback stayed SHA256 `be4302b9962c4aebc3066e439600ac469e0f0355d0c65daecce7dfbf788dea18`; the quota ledger still contains exactly one smoke row and its line count did not change. This confirms the prior serialization repair without spending Antigravity quota.
- Exact production write-scope proof remains work `WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194`: actual model `gemini-3.8-flash-high`, exit 0, one-file `content.json` permission readback and removal/readback PASS. Its content/DOCX failed static checks, so it is not a completed production sample. Work `0033` remains `PRE_SCOPED_WRITE_FIX_ATTEMPT=true`, historical-only, candidate SHA256 `784ed41a6bd955d2b40e212add7316c5c3fc39b1e474c8df7175d46d0a9f1247`; it will not be retried.
- Existing Antigravity work `WF_ANTIGRAVITY_BUILD_0037_20261004_221108_567364` is preserved, not rebuilt. Its stable 70,114-byte payload SHA256 is `c21e14d33dc3cd0ad6daa681ad1e53f41e44c1f75e1a91ecc880ce76882d22b4`. The receipt attests the exact file grant/removal and actual Gemini model, but records CLI status `ERROR` because the response exceeded the output token limit; host validation fails `CONTENT_SCHEMA_INVALID` because the required payload schema is absent. No candidate was rendered and it did not enter CURRENT or qualify as a cost sample. The structured usage snapshots are readable: five-hour remaining 72.9793%→71.1157%, weekly 78.2695%→77.9589%; no structured quota error. The stable bytes and receipts remain available for later exact salvage assessment.
- Salvaged existing 0042 content without an Antigravity call, passed static/duplication and hidden layout gates, then completed three fresh independent Codex reviews; the final exact-SHA review passed every semantic/usability gate. Candidate SHA256 `47bddaa2ba7d19f8401676553a37ba9aeb5878166e54276bdcbf1bfe3ab583d0`, five pages, no blank or sparse pages; its 19 synthetic facts were registered. Promotion to CURRENT is verified. Current DOCX count is 14. Checkpoint `CP_011_20261005_041337.zip` SHA256 `132c5fe9859f4e30a601c4000bc548a153283009b708d77f20615bf884776223`; receipt SHA256 `391f3c416dddc8a35bac69e3768730676b7cc9d9649fdaa307d7bdad5506f869`.
- Work `0032` remains parked after its bounded repair and fresh review; six blocking content/evidence defects remain. It is not to be promoted or counted as a successful sample. Unused READY item `0048` has no existing payload. Continue one Antigravity worker only, salvage current persisted work first, read official quota before/after each actual model work, and retain all semantic/static/layout gates. No Muse/OpenCode work is dispatched.
- Production resume is authorized after this record is committed and fetched back byte-for-byte. Then re-enable only the verified hidden supervisor route; do not change its architecture or broaden the scoped permission.

Durability references: `INCIDENT_ANTIGRAVITY_WRITE_FILE_AUTO_DENIED_20261004.md`; `INCIDENT_LEDGER.md`; `RAW_EVIDENCE_INDEX.md`; `CHECKPOINT_ANTIGRAVITY_SCOPED_WRITE_20261004.md`.


## 2026-10-05 06:54 +0800 - scoped-write closeout verification and 0054 salvage review

- Re-read the R03 runtime route. Hidden `agy.exe --version` readback exited 0 at version 1.2.16; the pinned model identity remains `gemini-3.8-flash-high`, maximum Antigravity concurrency is one, and fallback models remain disabled. No Antigravity model work was dispatched in this turn.
- Did not repeat the write smoke. The prior recorder fix serializes decoded evidence text and scalar metadata instead of raw bytes; its offline receipt remains PASS with all 13 checks true, receipt SHA256 `be4302b9962c4aebc3066e439600ac469e0f0355d0c65daecce7dfbf788dea18`, and content SHA256 `a7f7ca8dc77f764adea240189c544535514e4bd92f3fdb283defd0b39b3ce59a`. The last exact permission lease is `PERMISSION_REMOVED`, its readback was one isolated `content.json` path, local CLI settings are empty, and stale-permission recovery returned `NO_STALE_TTQS_RULES`.
- `0033` remains a historical pre-scoped-write attempt. Existing 0051-0055 Antigravity payloads remain preserved for salvage; no cost sample qualifies yet and no payload was regenerated by a model.
- Salvaged 0054 from its persisted payload into isolated host integration R02; no model call and no renderer change. Content SHA256 `489ed1553284455cbda9f226e34f0e8134cb965e3d292b9a7eed1cbd90a61d70` rendered as candidate SHA256 `0c799e810621357b2e2dc495ea93f37d3499c64ea2aeaf3ef1329ec745a2ca05`. Static/duplication passed, hidden layout passed at 6 pages with no blank or sparse pages. Fresh exact-SHA Codex review returned FAIL with D01-D04 (operational selection/exception rules, completed synthetic decision/material handoff, fact-to-body traceability, and zero-denominator/score rounding rules). The lane remains `PARKED_CONTROL`; no promotion; CURRENT remains 14 DOCX.
- Official Codex usage after review was 96% five-hour remaining and 10% weekly remaining. Local preflight reports `WEEKLY_RESERVE_REACHED`; no further model review was started. Continue offline salvage/gates. The existing hidden supervisor task remains Disabled and Hidden while persisted salvage work is being prioritized; no visible launcher is enabled.

Evidence paths and hashes are indexed in `RAW_EVIDENCE_INDEX.md`; the scoped-write incident addendum is in `INCIDENT_LEDGER.md`.
