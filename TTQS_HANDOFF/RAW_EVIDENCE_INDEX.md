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
