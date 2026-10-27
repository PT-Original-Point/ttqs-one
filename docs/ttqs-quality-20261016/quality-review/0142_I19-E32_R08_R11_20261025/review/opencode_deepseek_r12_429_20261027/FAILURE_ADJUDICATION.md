# 0142 R08 DeepSeek Free review route result

Candidate SHA-256: `dd6bfd2bb75ed9708065578f435b54fc7c85c9492f35edcddf614f962db41e0a` (unchanged; verified against PR #92 head `fb18af41559665350b87d38479d0cb8743f110ef`).
Source packet SHA-256: `e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49`; Unique Blueprint SHA-256: `4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b`.

The one bounded OpenCode v2.1.4 CLI request explicitly selected `opencode/deepseek-v4.1-flash-free`. The provider rejected it before inference with `provider.free-limit` / HTTP 429. The session export records the selected model ID and provider, but no inference response exists, so serving-model identity and semantic verdict remain unknown. Cost and token counters are reported as zero; upstream billing is unknown. No fallback, model switch, subscription, or retry was used.

Provider retry estimate: 2026-10-28 08:00:00.236 TPE (61964000 ms after the request error); not a guarantee.

## Same-day free-route observations

| Local time (TPE) | Requested free model | Work | Result | Candidate changed |
|---|---|---|---|---|
| 14:47 | `deepseek-v4.1-flash-free` | 0142 R08 | 429 before inference; 0 tokens | No |
| 16:06 | `beam-free` | 0124 R02 | 429 before inference; no semantic response | No |
| 19:44 | `glm-5.3-flash-free` | 0122 R02 | 429 before inference; 0 tokens | No |

These are three observed failures from the same Windows OpenCode CLI environment. They do not prove that every officially listed free model is unavailable, nor do they identify a single account-wide quota mechanism. The attached community monitoring report is global evidence only; these 429 receipts are direct local observations. Do not change models to evade the current provider limit. Continue unrelated lawful stages.
