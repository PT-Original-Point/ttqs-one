# TTQS_ONE raw evidence index

Raw logs and machine evidence remain in the local runtime and CLI profile; this repository records their exact paths and SHA256 values without copying CLI logs, prompts, credentials, or tokens into Git.

## Permission-denied attempts

| Work | Local session stream | SHA256 | CLI log | SHA256 |
|---|---|---|---|---|
| 0026 | E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0026_20261004_200104_127924\agy_stdout.stream.jsonl | 711bb4cdabed91392fc0625c4dd17389c07e28119f596cc6359b9b3ed6d68dbe | C:\Users\J\.gemini\antigravity-cli\log\cli-20261004_200109.log | 0ef79fbaff402fcedd15851528d476c14f4e03412623701406750a35dc3b8062 |
| 0027 | E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0027_20261004_200504_335945\agy_stdout.stream.jsonl | b41974a4262f39b93205c12634e339500d8a0be60e4ad898cd1e8d276024f693 | C:\Users\J\.gemini\antigravity-cli\log\cli-20261004_200510.log | 7cc78690400e87c84758ed5a0ff6804ab02e811ce073da01cde449ba9de622d8 |
| 0028 | E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0028_20261004_200905_192617\agy_stdout.stream.jsonl | 52409b0c0487415b94c63c9e805c30263eba55238b331db478f8de9dacdad11f | C:\Users\J\.gemini\antigravity-cli\log\cli-20261004_200919.log | 42dffb882cd504628a0730ac245ccbee119e76363e389351b9fb0fed06ed749d |

Official usage evidence for those attempts:

- 0026 before: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_BEFORE_20261004T200109_WF_ANTIGRAVITY_BUILD_0026_20261004_200104_127924.json — a44e0a28cf19203407c2c283da71c2a15bc6fe36d180ad47cbd459b5928f192f
- 0026 after: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_AFTER_20261004T200350_WF_ANTIGRAVITY_BUILD_0026_20261004_200104_127924.json — 6f220dab725110b97b5ccb623127f2604756eb3d9da15941326ca1dabd777000
- 0027 before: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_BEFORE_20261004T200509_WF_ANTIGRAVITY_BUILD_0027_20261004_200504_335945.json — a058b688c73101d005f9da95a884f947760b6d5c78118b3b6aa73fb197edb7ca
- 0027 after: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_AFTER_20261004T200702_WF_ANTIGRAVITY_BUILD_0027_20261004_200504_335945.json — 420d99a80da372fdfeda2702d9ca0b462c6d384a72c77e737547bd8c9554048f
- 0028 before: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_BEFORE_20261004T200919_WF_ANTIGRAVITY_BUILD_0028_20261004_200905_192617.json — c5524a3072eb7a4933e6403e0bb2c623b908b63164093d078cf34137fa9c9dcd
- 0028 after: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_AFTER_20261004T201142_WF_ANTIGRAVITY_BUILD_0028_20261004_200905_192617.json — 78c582e81dbdcf0b558a1e5b2d53aea267047daae6425efe4b426d6934bbabee

## Smoke and recorder evidence

- Session stream: E:\TTQS\TTQS_ONE_ANTIGRAVITY_WORK\ANTIGRAVITY_WRITE_SMOKE_20261004T203242\agy_stdout.stream.jsonl — c86fd4c292ea835c47cf43dec4dee85b37909c21d49e1329bf386281dd7eff5b
- Smoke content.json (73 bytes): E:\TTQS\TTQS_ONE_ANTIGRAVITY_WORK\ANTIGRAVITY_WRITE_SMOKE_20261004T203242\content.json — a7f7ca8dc77f764adea240189c544535514e4bd92f3fdb283defd0b39b3ce59a
- CLI permission log: C:\Users\J\.gemini\antigravity-cli\log\cli-20261004_203250.log — 462c97743a3c3d3d70f5f8558754efbf46ad38ca71bb57eaee2a915c4718f060
- Offline-reconstructed receipt: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_WRITE_SMOKE_20261004T203242.json — be4302b9962c4aebc3066e439600ac469e0f0355d0c65daecce7dfbf788dea18
- Usage before: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_BEFORE_20261004T203242_ANTIGRAVITY_WRITE_SMOKE_20261004T203242.json — 76525f31374d00d63a1aa8f4605a62efb672176f604832768b902fd36cfe40b7
- Usage after: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_AFTER_20261004T203242_ANTIGRAVITY_WRITE_SMOKE_20261004T203242.json — 1dbb2b340195c07e1a403e6a918a2ca0ce36d1ef56c296335aadbf49a8610a94
- 0033 pre-fix stream: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0033_20261004_201705_004616\agy_stdout.stream.jsonl — 19c932e952fe518d648e8c261f7b42ab299b4a482a7e6bd4ff1b67b169fbd7d9

## Runtime control evidence

- Fixed supervisor source: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\AUTOMATION\supervisor_core.py — 907ce8c53207976ee5df20c54bc0801bce783d1ee888df33fa93bd6f18969a45
- Offline recorder source: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\AUTOMATION\record_antigravity_write_smoke.py — 3a86d4e7181f9401cb6eec9dfad3ba200494e1c393ec4a225c17b5dcaced5870
- CLI settings after smoke cleanup: C:\Users\J\.gemini\antigravity-cli\settings.json — 3f528b91f0e9dfc5e6af72fa8cf17b69b87c18b964cc4b2e1f0d8a4baf5d236f; allow list is empty.
- Queue after parking 0033: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BUILD_QUEUE.json — 487201a91cc1052a6a30aec2e2d04b421bd0559fb2b5bda36f3d6083560a6dde
- Historical-only 0033 build receipt: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\BUILD_RECEIPTS\0033.json — a2e10f303fba5a40cffd878071d65cfc680a801fd9ece90a79d299af85742fba
- Cost-sample register before reclassification: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ARCHIVE\ANTIGRAVITY_COST_SAMPLE_REGISTER_PRE_CURRENT_QUALIFICATION_20261004.json — dc46895dcdebd13a3da6c6d59803116fbc00be5a739ba9c41c9099c9b54c70d5
- Cost-sample register after reclassification: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_COST_SAMPLE_REGISTER.json — eacf8883d2f2cb532b6a7604126194e77bdaad417d470a32c2b3a13346c6a745
- Local execution checkpoint: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CHECKPOINTS\20261004_ANTIGRAVITY_SCOPED_WRITE_RESUME.json — e894b6ca8af100f6019abb2bd695b43e3418678286df581b45e07040ffc6c9a5

Raw file contents remain local to the authorized runtime/profile. The hashes above make later readback comparisons deterministic.

## First resumed salvage turn — 0042

- Reused payload copy: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_CODEX_SALVAGE_0042_20261004_212511_552043\content.json — 556fd26f04885e1895bbabbe6a62b42c3faf54ebb5b189c8e6e16378a5f62f73
- Candidate (JSON-escaped local path): E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\CANDIDATES\\0042__\u57f7\u884c\u672c\u9805\u76ee\u8207\u4f5c\u696d\u6d41\u7a0b\u76f8\u95dc\u6587\u4ef6\u8cc7\u6599\uff08\u5c55\u73fe\u5229\u76ca\u95dc_\u5b8c\u6574\u5de5\u4f5c\u7a3f.docx — 22645a9e527efe51bfbf929eb029b23d2336845e42ac85df5fb36a0064edce15
- Static report (JSON-escaped local path): E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\QA\\0042__\u57f7\u884c\u672c\u9805\u76ee\u8207\u4f5c\u696d\u6d41\u7a0b\u76f8\u95dc\u6587\u4ef6\u8cc7\u6599\uff08\u5c55\u73fe\u5229\u76ca\u95dc_\u5b8c\u6574\u5de5\u4f5c\u7a3f.docx.static.json — 5aa8153fd4a70b87cc5cf823d0e891fc047977908ea293470b4e2a8e40a15027
- Outcome: FAIL_STATIC; lane parked. No Antigravity invocation, no layout/review, no CURRENT promotion.

## Persisted-artifact salvage — 0030

- Reused content: E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_CODEX_SALVAGE_0030_20261004_212706_133481\content.json — 8049bb49fad917c628ec5aa97229b5ca742b7916e883af0dd245776c1b3ce731
- New renderer candidate (JSON-escaped local path): E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\WORK\\CANDIDATES\\0030__\u5de5\u4f5c\u7d93\u9a57\u7684\u76f8\u95dc\u53d7\u8a13\u8b49\u660e_\u53ef\u76f4\u63a5\u4f7f\u7528\u6210\u54c1.docx — c29bd40a3cb3c73b174e7477c41a59d71f36e3e10284268de26c806d0a25c334
- Prior candidate preserved (JSON-escaped local path): E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\SUPERSEDED\\0030__\u5de5\u4f5c\u7d93\u9a57\u7684\u76f8\u95dc\u53d7\u8a13\u8b49\u660e_\u53ef\u76f4\u63a5\u4f7f\u7528\u6210\u54c1__WF_CODEX_SALVAGE_0030_20261004_212706_133481__3dd0bcd1549e.docx — 3dd0bcd1549e9ff33478834e17e66a5546d424b14bf1fef155a397adba996998
- Static report (JSON-escaped local path): E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\QA\\0030__\u5de5\u4f5c\u7d93\u9a57\u7684\u76f8\u95dc\u53d7\u8a13\u8b49\u660e_\u53ef\u76f4\u63a5\u4f7f\u7528\u6210\u54c1.docx.static.json — c97a24f984283a1e72c8537e4d070fa94bf8a3e8d23489cb88caba00f6621c72
- Outcome: FAIL_STATIC; lane parked. No Antigravity invocation, no layout/review, no CURRENT promotion.


## Production exact-scope proof and first gate result - 0031

- Stable payload: `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194\content.json` - SHA256 `c211dce8d4494e71092107ab45149ef6f3ec3d723a84b807c24968d8fc1e80f1`.
- Content receipt: `...\content_receipt.json` - SHA256 `282233EBF6A56CF9E16EE42559F4E1306CDBDBA4B1505114F8D70F1102807217`.
- Antigravity run receipt: `...\antigravity_run_receipt.json` - SHA256 `EFDA18D5B2D09F0C95BA048E70FD4DA42B9E8E52965B2CF7BC17FC25D4547B47`; requested/actual model both `gemini-3.8-flash-high`; CLI exit 0; exact-file grant readback PASS; removal/readback PASS; structured quota error false.
- Candidate `WORK\CANDIDATES\0031*.docx` - SHA256 `045ef0b1033ad9aaed205c074396619db2da8dd9eed30aab2eac35a050ec16e9` (stored DOCX SHA256 `5F009EC7B3E1C2AC2706EC95FF71576C6D5E6A567DCEED91FB6FC470C9E8908A`). Static report `CONTROL\QA\0031*.static.json` - SHA256 `1F108D68A452664BFB01677CB52C0AC286C9F6D39D4A745622B5909F89BD7235`.
- Static result: FAIL on `RAW_ENGLISH_SAMPLE_SYNTHETIC_LABEL_IN_BODY` and `FIRST_PAGE_30S_USE_CONTEXT_MISSING:timing`; no layout/review/promotion.
- Usage before: `CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_BEFORE_20261004T215715_WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194.json` - SHA256 `7EA54A6F5A5B1388D6B4464A2986A8C168479093C6842019524AA10635201E20`; five-hour 76.4892%, weekly 78.8545%.
- Usage after: `CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_AFTER_20261004T215949_WF_ANTIGRAVITY_BUILD_0031_20261004_215707_654194.json` - SHA256 `D3DBA7BD93B7E5591D6D8BE569E7D2A891FBE108D07EE97B38BEDD6C718F341A`; five-hour 75.1647%, weekly 78.6337%.
- Existing salvage evidence: 0044 candidate `47ba98891123dc6e89d609461af2e9842fde54cfff680378e25a15a4b0dacc22`, static `b62f4cd0518530a5f1d5e3abb42272807ae61fd2d2ff85b472f18a82734649a6`, layout `6dd389dafdc9de2fb9c2906250ca65622e248f5b048f3793cb4f6aea8a0a903c`, fresh review result `ee082fc182bfa7829609e718a4845a1a7086093215b2d197c2b1e1910f057ff9` (FAIL).
- 0050 candidate `d1a50ff6157c791030bd6a3073bd2921ce5666a5deb07fa57e1913117e7695a9`; static report `f57f936a92717ef66daa9732e958feffeed658de16884d4c490ea0d0b158a70d` (FAIL).
- 0047 corrected host copy `WORK\CONTENT_PAYLOADS\WF_CODEX_SALVAGE_0047_20261004_220104_927494\content.json` - SHA256 `6b8a2527a1bbe3c35249fcd9ad4cf38591e38130d31330348035641ce4ea0efc`; source-binding repair sidecar `6752abc24f3f0ec8efc8a8808147f278feed4ab6988b9b018ecaf646b2b67225`; candidate `903be30d0df2ef7e0303bc0dde4a17f0b7fea975e99fd0829d0fd6d9f6af70f0`; static report `896d16c9ec78bc4eb1655e664f4df3352802dfb9b3db17027f99a54e1b9a35a2` (FAIL).
- At checkpoint, exact scoped lease for 0032 was active at `CONTROL\ANTIGRAVITY_WRITE_PERMISSION_LEASE.json`; no hash is asserted while the lease is live.


## 2026-10-04 - 0031 Codex review timeout

- Runtime transcript: `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\LOGS\20261004_223302__codex_cross_review_0031_20261004_223302.log`; SHA256 `32717e863f08ff5a76793363d716642eeb0429a2fcfb1d423d6ef7c7f3c5b2ca`.
- Candidate: `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\CANDIDATES\0031__專業訓練人員職能評估方法等證明_可直接使用成品.docx`; SHA256 `756deaa32c1f159b4a0aeaf2ca75fbf376fcff3bb460e90dd612616490cf87a5`; candidate bytes unchanged across first review.
- Review ID: `codex_cross_review_0031_20261004_223302`; start 22:33:02 +08:00; exit 124 at 22:58:02; no review JSON.
- Retry ID: `codex_cross_review_0031_20261004_230355`; review-only, same candidate SHA, 45-minute timeout override; active at `2026-10-04 23:05:32 +0800`.
- Exact-file Antigravity permission lease readback: `PERMISSION_REMOVED`; scheduled supervisor remains disabled while the bounded review runs.


## 2026-10-05 offline recorder verification and 0042 promotion

- Repaired recorder source (no model invocation): `E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\AUTOMATION\\record_antigravity_write_smoke.py` — SHA256 `3a86d4e7181f9401cb6eec9dfad3ba200494e1c393ec4a225c17b5dcaced5870`.
- Original smoke receipt after deterministic offline regeneration: `E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\ANTIGRAVITY_WRITE_SMOKE_20261004T203242.json` — SHA256 unchanged at `be4302b9962c4aebc3066e439600ac469e0f0355d0c65daecce7dfbf788dea18`, result PASS, all 13 checks true. One existing smoke entry remains in `ANTIGRAVITY_QUOTA_LEDGER.jsonl`; line count stayed 44.
- Exact content file written in original smoke: `E:\\TTQS\\TTQS_ONE_ANTIGRAVITY_WORK\\ANTIGRAVITY_WRITE_SMOKE_20261004T203242\\content.json` — SHA256 `a7f7ca8dc77f764adea240189c544535514e4bd92f3fdb283defd0b39b3ce59a`. No smoke rerun.
- Work `WF_ANTIGRAVITY_BUILD_0037_20261004_221108_567364`: `content.json` SHA256 `c21e14d33dc3cd0ad6daa681ad1e53f41e44c1f75e1a91ecc880ce76882d22b4` (70,114 bytes); `antigravity_run_receipt.json` SHA256 `2be29073e9ed80d2cb8331d4523e293c243abab98875d613dff0178f43574007`; `agy_stdout.stream.jsonl` SHA256 `e6119b6ca4f85e63f4ebe04ba77148d4a77a79730997b5abe8708335f3e0dabf`; `TASK_PACKET.json` SHA256 `c14f03accdf37f9833305f1592c43cf47394d7f950d6200d29cde0224993ff3f`.
- 0037 official usage-before snapshot: `E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\ANTIGRAVITY_USAGE_EVIDENCE\\AGY_USAGE_BEFORE_20261004T221112_WF_ANTIGRAVITY_BUILD_0037_20261004_221108_567364.json` — SHA256 `a92192a58229abb30fe58881a8c1a7d6a8cc3f33cadd2adc3b89c885be0fcbfc`; five-hour 72.9793%, weekly 78.2695%.
- 0037 official usage-after snapshot: `E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\ANTIGRAVITY_USAGE_EVIDENCE\\AGY_USAGE_AFTER_20261004T221537_WF_ANTIGRAVITY_BUILD_0037_20261004_221108_567364.json` — SHA256 `50ba4cb2ce32c3f6b45ac8b913896daeb012db24b67f4fc71f0f4494aa9e43b4`; five-hour 71.1157%, weekly 77.9589%. Neither snapshot contains a structured quota error.
- 0042 CURRENT DOCX: `E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CURRENT\\0042__執行本項目與作業流程相關文件資料（展現利益關_完整工作稿.docx` — SHA256 `47bddaa2ba7d19f8401676553a37ba9aeb5878166e54276bdcbf1bfe3ab583d0`.
- 0042 final fresh review: `E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CONTROL\\REVIEWS\\0042.json` — SHA256 `bf23eaa8fb00e901b86c8773e080f08933257117711644a7836abb5c663e9118`; verdict PASS, reviewed exact SHA above, all requirement/genre, title-blind, negative-neighbor, duplication, SAMPLE/REAL, readability and evaluator-facing fields PASS.
- 0042 static report SHA256 `458f72205e6f0ef5a5ba8194c9bfbe450f12eec48a1c326d9bf78d2f70168995`; hidden layout report SHA256 `c7309156734416302ceaace258621feb596e7cbc0f726bd91ca1d023e50d2d7c`; five pages, no blank or sparse pages. Its receipt contains 19 synthetic facts and promotion evidence.
- Checkpoint `E:\\TTQS\\TTQS_ONE_CODEX_RUNTIME\\CHECKPOINTS\\CP_011_20261005_041337.zip` — SHA256 `132c5fe9859f4e30a601c4000bc548a153283009b708d77f20615bf884776223`; receipt SHA256 `391f3c416dddc8a35bac69e3768730676b7cc9d9649fdaa307d7bdad5506f869`.


## 2026-10-05 06:54 +0800 - scoped-write closeout and 0054 exact-SHA salvage evidence

- Antigravity route: `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_EXECUTOR_ROUTE.json` SHA256 `8ea7fb5edbb731f1bf55d1f1fec30f741cb3105df7bbda7b729a9fefc53bb3b3`; hidden CLI `--version` exit 0, version 1.2.16. Pinned model `gemini-3.8-flash-high`, max worker 1. No new Antigravity request.
- Smoke receipt: `E:\TTQS\TTQS_ONE_CODEX_RUNTIME\CONTROL\ANTIGRAVITY_WRITE_SMOKE_20261004T203242.json` SHA256 `be4302b9962c4aebc3066e439600ac469e0f0355d0c65daecce7dfbf788dea18`; smoke content SHA256 `a7f7ca8dc77f764adea240189c544535514e4bd92f3fdb283defd0b39b3ce59a`; no rerun. Permission lease `CONTROL\ANTIGRAVITY_WRITE_PERMISSION_LEASE.json` SHA256 `f2f0808ef8f0ff0c9aacd3857efc51a578820ee175a045cd78650aad89a9538b`, status `PERMISSION_REMOVED`, removal readback true; recovery `NO_STALE_TTQS_RULES`.
- 0054 host integration: `WORK\CONTENT_PAYLOADS\WF_CODEX_SCHEMA_NORMALIZE_0054_20261005_R02\content.json` SHA256 `489ed1553284455cbda9f226e34f0e8134cb965e3d292b9a7eed1cbd90a61d70`; no model call. Candidate SHA256 `0c799e810621357b2e2dc495ea93f37d3499c64ea2aeaf3ef1329ec745a2ca05`. Static report SHA256 `b5ed46427d2ef71a3d174f416d669dd02f734dc65c16fd6af12c1bdb0c751003`, `PASS_STATIC`; layout report SHA256 `c68ec36fde55b86b5811978f7c8cd3473665c134639021b9eb58f6421ea00488`, `PASS_LAYOUT`, 6 pages, zero blank/sparse.
- Independent review receipt `CONTROL\REVIEWS\0054.json` SHA256 `75d18a373eb891bff826c653d1f3a10e8ed5c3a360a681058b01ad68f3d504f5`, reviewed the exact candidate SHA and returned FAIL (D01-D04). Build receipt SHA256 `a8a1c3127620e9d0fa89dc822859592e7a8843054da52ea92100111c5db5ce36`. Candidate remains parked; CURRENT count 14.
- Codex usage snapshot `MASTER\CODEX_USAGE_SNAPSHOT.json` SHA256 `66c65e7b4ccaed24f344481d4358900487be612191267cb8e0d95480bffcae9c`: five-hour remaining 96%, weekly remaining 10%; preflight blocked at weekly reserve.


## 2026-10-05 07:32 +0800 — scoped-write and 0054 R06 readback

All paths below are under `E:\TTQS\TTQS_ONE_CODEX_RUNTIME` unless otherwise stated. Hashes are SHA256.

- Retained write-smoke receipt `CONTROL\ANTIGRAVITY_WRITE_SMOKE_20261004T203242.json`: `be4302b9962c4aebc3066e439600ac469e0f0355d0c65daecce7dfbf788dea18`; all 13 checks true. No rerun.
- Latest permission lease `CONTROL\ANTIGRAVITY_WRITE_PERMISSION_LEASE.json`: `f2f0808ef8f0ff0c9aacd3857efc51a578820ee175a045cd78650aad89a9538b`; scope was only `WF_ANTIGRAVITY_BUILD_0055_20261005_050127_993829\content.json`; status `PERMISSION_REMOVED`; removal readback true. CLI settings are empty.
- Pre-fix work 0033 receipt `WORK\CONTENT_PAYLOADS\WF_ANTIGRAVITY_BUILD_0033_20261004_201705_004616\antigravity_run_receipt.json`: `19c2efd4fb96c3b9208f4a270f2f77b620ed4d0575111e0f17003191cde2f7d8`; actual model `gemini-3.8-flash-high`, CLI exit 0, stable payload SHA256 `f1793119dd1c62d9cb38b6b11df747d5af95c93c61c79b50b991ba2e94aa03d9`. Historical only; no retry.
- Latest prior official Antigravity usage snapshots (0055; not a successful CURRENT sample): BEFORE `CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_BEFORE_20261005T050131_WF_ANTIGRAVITY_BUILD_0055_20261005_050127_993829.json`, SHA256 `5785903fa9b71678353217a948d8c33c4686c0bf687996a7078ecf785a153466`, five-hour 92.4829%, weekly 65.9350%; AFTER `CONTROL\ANTIGRAVITY_USAGE_EVIDENCE\AGY_USAGE_AFTER_20261005T050401_WF_ANTIGRAVITY_BUILD_0055_20261005_050127_993829.json`, SHA256 `36df634ab7c57ae68b7c08cf226e44e8620ecbcd2b3b71de08a4b96460be3c93`, five-hour 91.0415%, weekly 65.6948%. No new Antigravity call in this turn.
- 0054 host integration R06 `WORK\CONTENT_PAYLOADS\WF_CODEX_SCHEMA_NORMALIZE_0054_20261005_R06\content.json`: SHA256 `596d92b9c5d9c5fd8ad2d1840956958ede5720344e477188ad57bd03483c1c74`; content receipt `262b43d8a8c582b2decf1ded02b9fb9f29ccf09d8449d8cf4cd914086a19c6e5`; integration manifest `00ebb56dcdf4fefa5e77b79411e691733a9a30fe973151046b4f89cfc95c2782`. It derives only from same-lane R03 facts; no peer DOCX body and no model call.
- R06 candidate `WORK\CONTENT_PAYLOADS\WF_CODEX_SCHEMA_NORMALIZE_0054_20261005_R06\rendered\0054__依學員遴選標準及流程遴選，教材由講師及顧問推_完整工作稿.docx`: SHA256 `407a9ad07ecf67c2166cc416d834e48b28c37b6d5442e1f03205c3ce28dc58be`, 46,581 bytes. Build receipt SHA256 `7edf313b76add0449c643874ba18391c4383ee05f649f11143b7af89a12c48bf`; candidate receipt `61bca1621ac0f8e748d147e06bbf2b2688d888a08646158c3c2fbaa17025f5e9`.
- R06 candidate register copy SHA256 `f70443f0e5ce3170e7e2fe01aefec9c112aded3eb3a094b97cf4d612e1d51c7e`; 42 fact rows were appended only to this isolated copy and exact-matched to the payload. The canonical register was not changed.
- R06 static report SHA256 `8d8ff7f420e8f59ff109da6d6eec29cb786971fdd18fdab8c88be7e1f93a8090`: PASS_STATIC, substantive duplication PASS (37 peers, zero findings). Hidden layout report SHA256 `70f2dbbdf078060627ba91de1a26431fe0deaf25f968ad092e28c73b021f2f58`: PASS_LAYOUT, 7 pages, no blank/sparse pages, Word hidden.
- R06 has no fresh review receipt and is not in CURRENT. CURRENT count remains 14. Queue was not edited; `CONTROL\BUILD_QUEUE.json` SHA256 `b76c027107d8fdc7a8cf2fca787659a1d6028a9518a595c172c5c375c89bacf7`.
- Official Codex usage readback: 8% used in five-hour window, 90% used weekly (10% remaining). The local weekly reserve blocks launching a fresh reviewer; no reset credit was used.

## 2026-10-05 07:42 +0800 — Codex model-launch reserve

- Sanitized official usage readback: `TTQS_HANDOFF/CODEX_USAGE_READBACK_20261005_074254.json` (SHA256 `31aae122b8387e396e17d700b707e987cd434b7998d994b8b103bb74fab4cc37`); 92% five-hour remaining; 9% weekly remaining; weekly reset `2026-10-09T15:12:13Z`. Local 10% weekly reserve blocks a new model launch. No reset credit was used.
- Exact review target remains 0054 R06 candidate SHA256 `407a9ad07ecf67c2166cc416d834e48b28c37b6d5442e1f03205c3ce28dc58be`; no fresh review result exists and CURRENT was not modified.
- Readback JSON SHA256: `31aae122b8387e396e17d700b707e987cd434b7998d994b8b103bb74fab4cc37`.
