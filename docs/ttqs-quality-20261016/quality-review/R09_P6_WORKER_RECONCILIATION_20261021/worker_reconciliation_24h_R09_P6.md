# R09 P6 Worker reconciliation (rolling 24 hours)

Observed 2026-10-21T22:10:06.718552+08:00 (TPE). This is a bounded evidence summary, not a completion declaration.

## OpenCode v2

- Native SQLite scope: 39 TTQS sessions created between 2026-10-20T14:10:06.718552+00:00 and 2026-10-21T14:10:06.718552+00:00; 39 session lifecycles ended `succeeded`. Exact shell invocation count is UNKNOWN because the DB records sessions rather than every process launch.
- Recorded model session counts: {"mimo-v2.6-flash-free": 1, "deepseek-v4.1-flash-free": 25, "minimax-m3.1-flash-free": 6, "glm-5.3-flash-free": 1, "nemotron-3-ultra-free": 6}. Aggregate tokens: input 2,825,665, output 265,374, reasoning 1,078,193, cache-read 11,914,721; local DB cost 0.00; provider billing UNKNOWN. Provider-side served model/fallback UNKNOWN.
- 0100/0101 subset: 8 sessions; tokens input 672,314, output 72,615, reasoning 248,255, cache-read 4,179,712. The two Writer sessions recovered manuscript outputs; the other six were semantic reviews of evolving exact candidates. Those prior-SHA reviews remain historical; final9 has its own current review.
- 0101 writer session `ses_ea1a826fcffeumwDg7f4giu6By` recorded `deepseek-v4.1-flash-free`; native recovered manuscript SHA `1ebae3f14dd34210311f1bbc7c269b3ba8c471ae31199faf2cd62e741e76b227` (59,858 bytes), and its text equals the assistant final-text parts recovered from OpenCode SQLite after line-ending normalization: `True`. No shell PID was persisted.
- Final9 semantic review `ses_ea142a4b5ffeDVFhelB5TIrBrN`: CLI exit 0, 221.582s from its execution record, 100,493 input / 4,106 output / 40,828 reasoning / 76,416 cache-read tokens, local cost 0.00, billing UNKNOWN. Requested/runtime recorded `deepseek-v4.1-flash-free`; actual serving/fallback UNKNOWN. A-I PASS, arithmetic PASS, zero blocking defects; formal acceptance NOT_GRANTED. Review packet SHA `ed9897ab4d0cdd7200b5771a618c5f259f3aebf6a0c308478594e6856917c11f`; DOCX SHA `56f433e095f32378f2fd8241c1a27948d2bfe6748da003af5623d265885edb68`.

## Antigravity CLI

- Three attempts recorded: R01 exit 2/empty stdout (argument parsing), R02 exit 2/empty stdout (`--print-timeout` duration unit), R03 exit 0/nonempty 34,905-char response (reported 39,506 input+output tokens; thinking 5,467 separate). Requested model `gemini-3.8-flash-high`; actual model/provider/fallback and billing/quota delta UNKNOWN. The R03 raw manuscript was adopted as a 0099 baseline, but these attempts directly produced zero final DOCX.
- The R03 duration field reports 221.867s, while its recorded start/end timestamps share the same second; timing precision is inconsistent and should remain as reported with this limitation. No fresh Antigravity probe was run.
- The 3-failure/3-repair pause threshold is not established from these attempts (two CLI syntax failures followed by a successful text response); keep model-specific identity verification BLOCKED, not all document work.

## Closure status

The 0101 CLI → recovered manuscript → Word/PDF → exact-SHA technical/visual/semantic QA chain is complete locally. GitHub publication/readback is pending until the parent commit and exact blobs are verified. Current native Goal is paused; 120-minute task is configured but natural execution is UNKNOWN; legacy panel is offline/stale.
