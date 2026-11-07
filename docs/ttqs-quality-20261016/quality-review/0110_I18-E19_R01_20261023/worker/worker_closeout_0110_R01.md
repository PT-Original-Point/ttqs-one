# TTQS ONE 0110 Worker Incident Closeout R01

**work_id:** `TTQS-0110-I18-E19-R01`  
**doc_id / requirement:** `0110` / `I18-E19`  
**source and unique Blueprint:** `SOURCE_PACKET_0110_I18-E19_R01.md` and `UNIQUE_BLUEPRINT_0110_I18-E19_R01.md`; both were previously synchronized and exact-readback checked on PR #92. Their local SHA-256 values are in `worker_artifact_manifest_R01.json`.  
**branch head observed before this closeout:** `f275dc6acf7b2da25dec75de3b7c6a182a232d8e`; fresh-read the branch before publication.  
**candidate state:** No complete manuscript, no DOCX, no DOCX SHA, no technical/layout/visual QA, and no independent exact-SHA review. The partial outputs listed below are rejected worker evidence, not a candidate.

## Dispatch and return reconciliation

| Attempt | Requested model / role | Native evidence | Result and disposition |
|---|---|---|---|
| OpenCode R01 | `opencode/deepseek-v4.1-flash-free`, Writer | CLI v2.0.32 session `ses_e998b05ccffeft7jpiW3UTNcJ6`; native session reports finish `length`, 8,648 input, 0 output, 32,000 reasoning, cost field 0. Child PID 68464 was stopped after no manuscript. | No usable text. Native session model was DeepSeek; invoice/account billing remains UNKNOWN. |
| Antigravity A1 | `gemini-3.8-flash-high`, Writer | 09:59:32 local argument-parser rejection; no model request. | 0 manuscript bytes; no model request evidenced. |
| Antigravity A2 | `gemini-3.8-flash-high`, Writer | 09:59:46 local timeout-option parser rejection (`180` lacked a unit); no model request. | 0 manuscript bytes; no model request evidenced. |
| Antigravity A3 | `gemini-3.8-flash-high`, Writer | CLI reached the print call; conversation `c792639e-96da-49d3-bbc6-8742e4402b70`; print timed out after 3 minutes and returned a partial output. `--mode plan` was ineffective because slash-command expansion was disabled. | Partial 17,634-character manuscript ended in the middle of Chapter 11's replacement register. CLI `SUCCESS` did not mean complete. Actual serving model identity and quota use UNKNOWN. |
| Antigravity continuation | Same requested model and conversation | CLI exit 0; stdout 14,984 bytes (about 6,440 decoded Chinese characters). | Invalid seam: starts with a detached fragment and supplies only later sections. It adds an unsupported three-year retention rule, claims physical folders were inspected and title-blind QA passed, instructs removing SAMPLE marking, and says the tool fully complies. Rejected. Actual serving model identity and quota use UNKNOWN. |
| OpenCode R02 | `opencode/mimo-v2.6-flash-free`, Writer | New native session `ses_e9976a387ffeaVXcxNgW47qguV`, PID 70564. Current model catalogue listed this SKU. Session export remained user-only; stdout contained only `step_start` (251 bytes), stderr 0. Configured bound 360 seconds; measured process lifetime 396.47 seconds, then only this CLI PID was stopped. | No assistant response and no manuscript text. Serving model identity and provider/account charge UNKNOWN. The wrapper hit a PowerShell reserved `$PID` variable after starting the child; the process was identified by native PID and not duplicated. |

## Content defects found before any Word build

1. The learner form has nine scaled items (L01–L09), but Table 8-1 carries only four construct scores per learner. The item-to-construct mapping and treatment of the other scaled items are undefined. The client form has five scaled items (C03–C07), while Table 8-2 carries only three values. L04 uses a 4–1 frequency code plus 0 and cannot be pooled into the generic 4–5 favorable formula. The item mapping and analysis need a mathematically consistent repair.
2. Retain the existing numbers only as `SYN-0110-CASE-01`: baseline `6/8=75.0%`, follow-up `7/8=87.5%`, change `+12.5 percentage points`, target `90.0%`, decision `REVISE`, not `CLOSE`. They do not prove Original Point Association activity, real respondents, consent, logs, approvals, or physical records.
3. No statistical-significance or single-cause claim is supported by these small synthetic samples.
4. Replace the continuation's fixed three-year retention claim with a process tied to the Association's applicable approved record policy; if that authority is unknown, restrict access and do not destroy records. Remove claims of physical inspection, passed title-blind review, or full compliance. SAMPLE cannot be promoted by watermark removal or one signature.
5. No complete manuscript or DOCX candidate exists for this work_id.

## Route state and next action

- **Antigravity:** Three consecutive command/model-return failures were followed by three corrections (fix `--print` argument placement, add timeout unit, continue the same conversation), but no complete usable manuscript resulted. New Antigravity Writer dispatch is **PAUSED** under the Human stop-dispatch rule pending a material root-cause change. Other READY lanes are unaffected. No Computer Use, GUI, fallback model, permission bypass, or paid model selection was used.
- **OpenCode:** Two distinct 0110 Writer failures occurred (DeepSeek returned 0 output; Mimo emitted no assistant response by timeout). The three-error/three-repair route-wide pause threshold is not evidenced; this document's Writer lane received no usable return and was not retried again in this turn. A free-looking model listing is not an invoice readback; provider cost remains UNKNOWN.
- **Next lawful action:** Publish the source-bound failure evidence to PR #92 and read it back. Then continue a different independent READY source/Blueprint stage, or return to 0110 in a later turn with a materially smaller/differently scoped OpenCode task. Before Word build, repair item-to-construct mapping and the replacement inventory; then build, render, inspect, and commission independent exact-SHA review. Do not reuse/promote the rejected worker text unchanged.

## Evidence index

`worker_artifact_manifest_R01.json` lists each included file's local name, planned remote path, byte length, SHA-256, and evidence class. Empty local streams are omitted from GitHub and their zero lengths are documented above.

## GitHub synchronization byte-integrity correction

The first evidence commit (`675ed18efe08a6044fa3cb270415d4fb4823d7c4`) was pushed, but the first native readback **failed** exact-byte comparison: `AGY_writer_input_R01.md` was 22,361 bytes locally and 22,354 bytes remotely; local SHA-256 was `D00600F37DD0E70084EE713146009FE2A85F50E5FF9DEF06601CBA898DFB8952`, remote SHA-256 was `2150FEBFDC3A1876314F4FA5FE52956F0FFC38C0802BE4436C2A4AE8DAA62047`. The Git clean conversion normalized line endings. This first upload is not claimed byte-identical. A corrective commit will store the exact local bytes without clean filters; final per-file GitHub readback is recorded in `github_readback_receipt_R01.json`.
