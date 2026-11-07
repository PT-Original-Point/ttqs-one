# Rolling 24-hour OpenCode v2 reconciliation

Observed 2026-10-22T03:27:13.631759+08:00; window 2026-10-21T03:27:13.631759+08:00 to 2026-10-22T03:27:13.631759+08:00 (Asia/Taipei).

- Native SQLite TTQS session rows: **36**. These are not exact CLI launch attempts; invocation count remains **UNKNOWN**.
- Token totals from native `session_v2`: input 2,436,930; output 321,864; reasoning 937,223; cache-read 11,815,580; cache-write 0.
- Local SQLite cost sum: 0.00; vendor billing remains **UNKNOWN**.
- Selected model IDs are recorded by OpenCode; actual serving-model identity/fallback is **UNKNOWN**.

| Selected model (not serving attestation) | Sessions | Input | Output | Reasoning | Cache read | Local cost |
|---|---:|---:|---:|---:|---:|---:|
| deepseek-v4.1-flash-free | 23 | 1,659,438 | 227,361 | 835,362 | 10,747,520 | 0.00 |
| glm-5.3-flash-free | 3 | 127,930 | 50,266 | 2,676 | 98,432 | 0.00 |
| mimo-v2.6-flash-free | 2 | 132,970 | 13,575 | 74,571 | 965,760 | 0.00 |
| minimax-m3.1-flash-free | 2 | 74,044 | 12,182 | 13,869 | 3,868 | 0.00 |
| nemotron-3-ultra-free | 6 | 442,548 | 18,480 | 10,745 | 0 | 0.00 |

R15 review `ses_ea030cfffffeWft8qAw18cKX1E` is a terminal native session (`idle_outcome=succeeded`) on selected `mimo-v2.6-flash-free`, with 70,570 input / 8,130 output / 41,871 reasoning / 680,960 cache-read, local cost 0.00. Its shell CLI exit was 1; raw response was recovered, and the independent verdict is PARTIAL.
