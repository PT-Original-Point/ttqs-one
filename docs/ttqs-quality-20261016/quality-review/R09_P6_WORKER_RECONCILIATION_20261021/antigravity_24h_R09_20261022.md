# Antigravity CLI — retained attempts, rolling 24 hours

Observed: 2026-10-22T03:57:34+08:00; window: 2026-10-21T03:57:34+08:00 to 2026-10-22T03:57:34+08:00 (Asia/Taipei).

Retained attempts: 10 (not a provider-side complete invocation log). Exit 0: 3; exit 2: 5; exit -1: 1; exit unknown: 1. Text returned: 5; directly produced final DOCX: 0.
Known token lower bound: 149265; token data unknown for 2 text-return calls. Actual model/provider/fallback, quota delta, and vendor billing: UNKNOWN.

Requested model for each retained attempt was `gemini-3.8-flash-high`; this does not attest actual serving identity. PIDs and native session IDs are absent from retained receipts.

| Work ID | DOCX / requirement | Attempt | CLI exit | Text | Known tokens | Outcome / adoption |
|---|---|---|---:|---|---:|---|
| TTQS-0097-I18-E05-ANTIGRAVITY-A01-20261021 | 0097 / I18-E05 | A01 | 2 | no | UNKNOWN | CLI argument/parser error; empty output.; No manuscript; no candidate. |
| TTQS-0097-I18-E05-ANTIGRAVITY-A02-20261021 | 0097 / I18-E05 | A02 | 0 | yes | 44572 | Raw text returned; not a final DOCX.; Raw response/manuscript present; downstream exact candidate linkage UNKNOWN. |
| TTQS-0098-I18-E06-ANTIGRAVITY-A01-20261021 | 0098 / I18-E06 | A01 | 2 | no | UNKNOWN | CLI argument/parser failure; empty output.; No manuscript; no candidate. |
| TTQS-0098-I18-E06-ANTIGRAVITY-A02-20261021 | 0098 / I18-E06 | A02 | -1 | yes | UNKNOWN | Text returned, but shell exit was -1.; Raw manuscript/register returned; downstream exact candidate linkage UNKNOWN. |
| TTQS-0098-I18-E06-ANTIGRAVITY-R03-20261021 | 0098 / I18-E06 | R03 | 0 | yes | UNKNOWN | Text response returned; no final DOCX directly from call.; Response-review artifact exists; exact final candidate linkage UNKNOWN. |
| TTQS-0098-I18-E06-ANTIGRAVITY-R04-01-20261021 | 0098 / I18-E06 | R04-01 | 2 | no | UNKNOWN | Invalid --print-timeout duration missing unit; exit 2.; Rejected before model dispatch; no model response. |
| TTQS-0098-I18-E06-ANTIGRAVITY-R04-02-20261021 | 0098 / I18-E06 | R04-02 | UNKNOWN_NOT_RECORDED | yes | 65187 | Proposal/raw output retained; no final DOCX directly from call.; Bounded proposal returned; exact final candidate linkage UNKNOWN. |
| TTQS-0099-I18-E07-ANTIGRAVITY-A01-20261021 | 0099 / I18-E07 | A01 | 2 | no | UNKNOWN | CLI argument-parser failure; empty output.; No manuscript; no candidate. |
| TTQS-0099-I18-E07-ANTIGRAVITY-A02-20261021 | 0099 / I18-E07 | A02 | 2 | no | UNKNOWN | --print-timeout duration missing unit; empty output.; No manuscript; no candidate. |
| TTQS-0099-I18-E07-ANTIGRAVITY-A03-20261021 | 0099 / I18-E07 | A03 | 0 | yes | 39506 | Baseline manuscript adopted; no final DOCX directly from call.; Raw response adopted as manuscript baseline by matching hash; later DOCX lineage separate. |

## Evidence limits

- Five calls returned text, but none directly created a final DOCX.
- The 0099 A03 response was adopted as a manuscript baseline by exact raw-response hash; later DOCX lineage is recorded separately.
- For 0097 and 0098, downstream candidate linkage is UNKNOWN.
- No actual model identity, provider fallback, quota movement, vendor charge, or complete account-side invocation count is proven.
- Raw output, stderr and input evidence remain in the adjacent `antigravity_24h_R09_20261022/` directory; this summary does not replace the original receipts.
