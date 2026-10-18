# 0069 R01 OpenCode writer reconciliation

Status: incident reconciled; candidate remains unqualified.

The initial wrapper incident note said no candidate body had been created. That was only the wrapper's incomplete snapshot and is superseded by later native OpenCode session-list/export evidence. Both dispatched V2 sessions completed successfully and each produced a full body. The first CLI attempt was therefore not a confirmed model/provider failure.

| Attempt | OpenCode session | Model | Result | Body SHA-256 | Bytes |
|---|---|---|---|---|---:|
| 1 | `ses_eafcc0d12ffeLf7dznQ5IZhCTV` | `opencode/deepseek-v4.1-flash-free` | succeeded | `e2fa5c2a3337b4133824e86bbc154ecd4436808ec4bf1877e53ff726c6787dd4` | 27,912 |
| 2 | `ses_eafcb4b13ffe4UnPIy0SrCZptV` | `opencode/deepseek-v4.1-flash-free` | succeeded | `5c9f09ea540c278265a6338c81a024ad9b1174c74f2e5d4f9c12964244252772` | 29,225 |

The sessions overlapped while targeting the same candidate-body path from 2026-10-19 02:09:53 through 02:11:50 Asia/Taipei. Attempt 2 wrote its version first; attempt 1 completed its write at 02:12:30, so attempt 1 overwrote the shared path. Both exact bodies and session exports have been preserved locally. The pre-repair body matches attempt 1 exactly; attempt 2 remains an alternate draft. The current repaired body SHA is `d3e903b478d784aa45f6b7042007b70ac009d1ee4d86d2226b6061e3ab1b4e2f`; the current DOCX SHA is `1edf81e2e8830862d77936d8b7db8851b755f8500779313c2f7d2ddf886d30cf`. Neither has passed final visual or independent semantic review.

Cause: a PowerShell native-command wrapper error was interpreted as completion/failure before the OpenCode session had settled. A second writer was dispatched without first reconciling the session list and live process state. The resulting issue was orchestration and same-path write contention, not a provider outage. No Computer Use or permission bypass was used.

Repair: preserve both exact outputs; designate only the repaired body as the current candidate input; do not dispatch another 0069 writer. After any wrapper stderr/timeout, first inspect `opencode session list` and the session's terminal/export state, then confirm the per-document writer is gone before any retry. Enforce one active writer per document and use unique draft paths if an explicitly authorized subsequent attempt is ever needed.

Evidence scope: this receipt records the two session IDs, outcomes, exact body hashes, byte counts, overlap, current body/DOCX hashes and containment action. Full session JSON exports and their tool traces remain in the local runtime because they contain extensive reasoning/tool context; they are not represented here as public review evidence.