# TTQS ONE — 0142 / I19-E32 R05 evidence index

State: `CANDIDATE`. This index records the exact R05 bytes and the checks performed; it does not grant semantic acceptance, an official score, real-evidence status, or formal acceptance.

## Requirement and source binding

- Project/document: `TTQS_ONE` / `0142`.
- Official requirement: `I19-E32`; official checkbox index `156`; printed serial `UNKNOWN`.
- Official source PDF SHA-256: `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`.
- Source packet `SOURCE_PACKET_0142_I19-E32_R01.md`: SHA-256 `e3e8b3a8ee1effe758608fee183440add4f37381988c5e352912b1a3d55c9e49`.
- Unique Blueprint `UNIQUE_BLUEPRINT_0142_I19-E32_R01.md`: SHA-256 `4841161d6e9aad3ace2a0b4ec4a5a3e1b7e92b68ff2b20f95e9edeae2b84070b`.
- Crosswalk SHA-256: `1ddfbb608bcad25170683ddb42a1dbb27bafa6f1f35ff0498f1b8d75b24f0679`.

## Candidate and delta

- DOCX: `0142_I19-E32_R05_HEADER_CONTRAST_CANDIDATE.docx`
- Candidate SHA-256: `a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e`.
- R05 fixes two located presentation defects without changing visible body text, data, or calculations: dark Table 5 and Table 6 header labels now use white bold text. The earlier R04 pagination repair removed the redundant break that had stranded the final Table 3 row and caused an empty page. R05 is six pages.

## Technical, sample, and layout evidence

- `R05_HEADER_CONTRAST_PATCH_RECEIPT.json`: SHA-256 `7e8ff61c0c578eb671d9fbe4ea10b394c6662ded91cc313b828f5092c7d73c40`.
- Deterministic patch script `PATCH_0142_R05_DARK_HEADER_CONTRAST.py`: SHA-256 `896c258cfeabb0b91078826d326702c7097ffded9a2edd701a7ad59df2ae01d2`.
- Technical QA/register script `CREATE_0142_R05_QA_AND_SAMPLE_REGISTER.py`: SHA-256 `34977b6c91bef57677bb50ec231475400e36417d2f586d19da98ee10109b62c5`.
- `R05_TECHNICAL_SAMPLE_MATH_QA_RECEIPT.json`: SHA-256 `f7a06a5159bfda13b720f2a78b2251ba7fbf55341f868ca91e8b783e3efd184e`; DOCX package, 11 tables, font floors (body 11 pt/table 10 pt), three annual sums, growth formulas, and header contrast pass. Arithmetic is SAMPLE-only.
- `SAMPLE_REPLACEMENT_REGISTER_0142_R05.csv`: 19 rows, SHA-256 `79db9aee9ebf016c575961d41479c16cce9d82647f0dad69c289ba2aabac2ff6`; every row is `SAMPLE/SYNTHETIC`, with source required and REAL status `UNKNOWN/HOLD`.
- `WORD_NATIVE_RENDER_RECEIPT_0142_R05.json`: SHA-256 `c33bc14e83cfec3c1e1dd39254d36ee33c70052c945c04ccea508508d5fee571`.
- Word read-only PDF: `0142_I19-E32_R05_HeaderContrast_WordNative.pdf`, six pages, SHA-256 `5c0be13903a73c76851f791105bfbb287960bdb841a9530c69e98661321da8aa`.
- `PAGE_IMAGE_MANIFEST_0142_R05.json`: SHA-256 `6098c11336140150aad24dba5cee4f0cc489e528cde2b980414f785799eb49fe`.
- `VISUAL_REVIEW_RECEIPT_0142_R05.json`: SHA-256 `ff0c54222586f1da0d94060da3d7ab75bff37326c2fee8bcdbd1ecff57f831e4`; six-page visual coverage. Pages 1, 2, 4, 5, and 6 reuse the prior direct inspection only where the exact page-image SHA is unchanged; page 3 was directly inspected at full size after R05.

## Independent review and truth boundary

- Antigravity CLI returned a text-only reviewer report for this exact SHA with reviewer-declared verdict `PARTIAL`; it used 29,084 reported tokens and returned no tool-call indicators. The raw response SHA-256 is `7a48ff471733275a462117d3f5d06f669de5185cd7acd60ff22d8b3a51a3f51a`; extracted response file SHA-256 is `0cd0270ed4ceb675d38113ab87fd7e35a4cd65748b3a73fa49eb90404b9d0f5f`.
- Requested model was `gemini-3.8-flash-high`, and the CLI model catalogue listed it; the native response exposed no serving-model field. Actual serving model and fallback status remain `UNKNOWN`, so this response is recorded as a reviewer-reported partial result and is not claimed as a verified Gemini review or semantic acceptance.
- Candidate SHA before and after dispatch was unchanged: `a213a30cd949948f7ce8c2b5d76fc79b5fdcd90117f6fba77139af6660c5ab6e`.
- Source/Blueprint comparison confirms substantive R05 gaps requiring repair: the body has uncaptioned physical tables 7 and 8 although §7 refers to tables 5–8; it lacks a complete source register, explicit account-mapping table, and statement-to-ledger annual reconciliation table; percentages use one decimal place although the Blueprint requires two; and the cover omits checkbox index 156 and printed serial `UNKNOWN`. The reviewer said tables 7 and 8 were missing; physical tables exist, but their missing captions make the cross-reference ambiguous.
- The reviewer input did not include the companion 19-row replacement CSV. That CSV is present and every row is registered `SAMPLE/SYNTHETIC` with `UNKNOWN/HOLD`; however, the DOCX appendix still lacks the Blueprint's row-level replacement fields. R06 should provide the usable register inside the document and keep the CSV as its companion.
- The older OpenCode R07 receipt concerns a different DOCX SHA (`dee4b45dcac7e32685f56cbf23d956443aa2810110b359472ab557dfcc0e8eea`) and an HTTP 429 with no review response; it is not a review of R05.
- The latest local OpenCode v2 free-route receipt for another review lane records `provider.free-limit` HTTP 429 and `retry_eligible_at_local=2026-10-28T07:59:59.7360000+08:00`. No new OpenCode review was dispatched for R05 during this interval; this route failure is not a semantic verdict on R05.
- This evidence bundle does not contain an account-level OpenCode model-availability test. Actual model identity for a future review remains `UNKNOWN`; no fallback is claimed.
- Real financial evidence: `UNKNOWN/HOLD`. Official score: `NOT_ASSIGNED`. Formal acceptance: `NOT_GRANTED`.
