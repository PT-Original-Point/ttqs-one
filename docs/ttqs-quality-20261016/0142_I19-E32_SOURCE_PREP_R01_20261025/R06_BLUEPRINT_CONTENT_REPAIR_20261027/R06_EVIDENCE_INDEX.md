# TTQS ONE - 0142 / I19-E32 R06 evidence index

State: CANDIDATE. This evidence index binds the R06 document, source mapping, sample register, native Word render, technical checks and direct visual inspection. It does not grant semantic acceptance, official score, REAL status, or formal acceptance.

## Requirement and source binding

- Project/document: TTQS ONE / 0142.
- Official requirement: I19-E32; 157-checkbox index 156; printed checkbox serial UNKNOWN.
- Official source PDF SHA-256: 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709.
- Source packet: SOURCE_PACKET_0142_I19-E32_R01.md, SHA-256 e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49; retained in the R05 source package in this same branch.
- Unique Blueprint: UNIQUE_BLUEPRINT_0142_I19-E32_R01.md, SHA-256 4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b; retained in the R05 source package in this same branch.
- Crosswalk SHA-256: 1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679.
- R06 repairs the exact R05 review findings: missing formal table captions/references, missing structured account-mapping and source/annual-reconciliation mechanics, one-decimal displays where the Blueprint requires two decimals, cover metadata missing the official index/unknown printed serial, and no in-document row-level replacement register.
- R06 adds a 19-row embedded replacement register (18 SAMPLE/SYNTHETIC fact rows plus one control-metadata row) and retains the companion CSV. This does not create any REAL financial evidence.

## Exact candidate and associated files

- DOCX: 0142_I19-E32_R06_BLUEPRINT_REPAIR_CANDIDATE.docx
- DOCX SHA-256: 3781cb4cb2d26625fb5676181f4faa4176ca0bb80e2e3fac518245bbdc42f97e (49,924 bytes).
- Companion CSV: SAMPLE_REPLACEMENT_REGISTER_0142_R06.csv; SHA-256 52491fabdd1358c894e113c29f5f2a60f680c925ea09c3a8782a40552107058d.
- Word-native PDF: 0142_I19-E32_R06_WordNative.pdf; SHA-256 e2f2de94a0aefcf8c07ce8ec6f6852398e4bfdc0b1a0ba82105da87459cacdae; 10 pages.
- Page manifest: PAGE_IMAGE_MANIFEST_0142_R06.json; SHA-256 f37223facebedd5d069a8a157efe47a7d5f668be3fd2cfad0f42fd08a679d6e0.
- Word render receipt: WORD_NATIVE_RENDER_RECEIPT_0142_R06.json; SHA-256 a58bf2caed96baff7eae79ddfb0f3aefd8a74af89c17f26f5865b4da62b3fbb3.
- Build receipt: DOCX_BUILD_RECEIPT_0142_R06.json.
- Technical QA receipt: TECHNICAL_QA_RECEIPT_0142_R06.json; current exact-SHA check reports PASS_TECHNICAL_CONTENT_GATES_ONLY. It verifies document/requirement binding, package integrity, tables, the embedded register against the CSV, sample arithmetic, font floors, and nearest-neighbor separation. It does not confer semantic PASS.
- Visual receipt: VISUAL_REVIEW_RECEIPT_0142_R06.json; all 10 Word-exported page images were directly inspected. Result is PASS_LAYOUT_READABILITY. Page 7 has substantial lower-page whitespace but the table is readable and unclipped; no cosmetic rebuild was made. Visual inspection is not independent semantic review.
- Semantic review: PENDING_INDEPENDENT_EXACT_SHA_REVIEW.

## GitHub publication and raw-byte readback

- Candidate package commit: 678c81f9a2990c5c60344fe3db2afd7550d8c8a1 on the existing PR #92 branch.
- GitHub Contents API readback at that commit verified all 33 package files, including the DOCX, Word PDF, CSV, 10 page images, technical/layout receipts, and preserved R05 review evidence. For each file, the returned Git blob SHA-1 and byte count matched the local no-filter Git object and file byte count. Local file SHA-256 values remain separately recorded in R06_PACKAGE_MANIFEST.json.
- Readback receipt: ../R06_PUBLICATION_READBACK/GITHUB_RAW_READBACK_RECEIPT_0142_R06.json. This post-publication receipt is outside the package manifest to avoid a circular listing.
## Historical R05 independent-review evidence

The R05 review is historical repair input only and is not an R06 review. The original response and dispatch files are preserved under historical_R05_review/.

- R05 candidate SHA reviewed: a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e.
- R05 response body states PARTIAL and identifies structural/data-display gaps; response SHA-256 0cd0270ed4ceb675d38113ab87fd7e35a4cd65748b3a73fa49eb90404b9d0f5f. The dispatch terminal SHA-256 is 1b23df58e8165ad1987e1afc316d98ec3b6a92c0edae6adc8b3e99ae0a975e40; raw stdout SHA-256 is 7a48ff471733275a462117d3f5d06f669de5185cd7acd60ff22d8b3a51a3f51a.
- R05 dispatch terminal records requested model gemini-3.8-flash-high but actual serving model UNKNOWN, fallback UNKNOWN, 29,084 reported tokens, no tool calls, and unchanged R05 candidate. Its parsed verdict field says NO_EXPLICIT_VERDICT; this metadata/body discrepancy is retained as-is and not used to claim R06 acceptance.
- The R05 request, input manifest, raw stdout/stderr and model-catalogue stdout/stderr are preserved so the original reviewer output can be audited. No R06 independent reviewer has yet evaluated the R06 SHA.

## OpenCode route context supplied by Human

The attached 2026-10-27 free-model report says the public free-inference service was Operational at its 08:17 Taiwan-time cutoff, while describing two incidents totaling 3 hours 39 minutes and multiple user reports about quota/reset problems. The same report explicitly says it did not perform logged-in account-level tests of the ten models. Therefore it does not establish this Windows account's availability, a completed OpenCode dispatch, or a reviewer result for R06. Attachment SHA-256: ff3ca9886e3a345d78be358b2883296b7e5454408d23bc940fee239ba826c900.

## Latest OpenCode exact-SHA semantic-review attempt (2026-10-28)

The hidden OpenCode V2 2.1.4 CLI request for `opencode/big-pickle` was dispatched once for the R06 candidate. It terminated in 10 seconds with a pre-inference `provider.free-limit` HTTP 429, no review text, no provider-reported tokens, and no candidate mutation. The server retry interval estimates 2026-10-28 07:59:57 +08:00. This is a quota rejection, not a service-health incident or semantic result. The earlier GLM 5.3 Flash Free request for this exact candidate also returned a pre-inference 429; quota scope is not conclusively established. See `independent_review/OPENCODE_BIGPICKLE_20261028T015432_R01/` for the request, original stdout/stderr, start/terminal records and route adjudication. R06 semantic status remains PENDING.
## Truth boundary and disposition

- SAMPLE/SYNTHETIC calculations only; no association financial originals were supplied.
- REAL evidence: UNKNOWN/HOLD.
- Official score: NOT ASSIGNED.
- Formal acceptance: NOT GRANTED.
- Candidate bytes remained unchanged during visual review. Any later semantic receipt must bind exactly to the R06 DOCX SHA above.

## Latest OpenCode GLM 5.3 Flash Free exact-SHA review dispatch (2026-10-28 08:28 TPE)

- Work ID: TTQS-0142-I19-E32-R06-W1-OPENCODE-GLM53-FREE-EXACT-SHA-SEMANTIC-REVIEW-20261028T0830. The Windows OpenCode V2 2.1.4 CLI was launched hidden, noninteractive, with tools and fallback disabled.
- Requested model: opencode/glm-5.3-flash-free. Provider rejected before inference with provider.free-limit HTTP 429; no reviewer response was produced. Actual model: NOT_REACHED_PROVIDER_REJECTED; token usage was not returned; billing is UNKNOWN.
- Provider retry estimate: 2026-10-29T07:59:59.854+08:00 Asia/Taipei. This is an estimate from retryAfterMs, not proof the quota will reset then. Do not retry this identical request before that time.
- Candidate DOCX SHA-256 remains 3781cb4cb2d26625fb5676181f4faa4176ca0bb80e2e3fac518245bbdc42f97e; no candidate bytes were changed. R06 semantic review remains PENDING; this 429 is not a semantic verdict.
- Public monitoring report SHA-256 ff3ca9886e3a345d78be358b2883296b7e5454408d23bc940fee239ba826c900 reports service Operational at 2026-10-27 08:17 TPE but no account-level model tests; it does not override this local pre-inference rejection.
- Local original stdout SHA-256: 09c672ec3d260c07b229990a98a3bcf59660b186bdabba682e14a7757bf96218; the public sanitized stdout SHA-256 is 5a113f7282a297e39b19aed6aa3e1ebde673375f329f2d182d3a0b43d6478551. The provider session identifier is omitted from public receipts.
- Route scope: this request/model attempt is quota-blocked pending the estimate; no global outage or account-wide quota conclusion is made. Other READY work remains eligible.
