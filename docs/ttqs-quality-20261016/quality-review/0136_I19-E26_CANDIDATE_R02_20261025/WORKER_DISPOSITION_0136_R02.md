# 0136 CLI worker attempts and disposition

This record covers the source-ready manuscript work for DOCX 0136 / I19-E26 / project-157 index 150. The official printed checkbox serial is UNKNOWN. All original CLI stdout, stderr, requests and dispatch receipts are retained in this folder. A non-empty output, zero exit code, or model listing is not treated as proof of adoption, provider identity, billing, semantic acceptance, or real association evidence.

## OpenCode CLI v2

- CLI version: 2.1.4.
- Writer attempt 1: requested `opencode/mimo-v2.6-flash-free`; exit 1 after 0.222 s because `--prompt` is not a supported `opencode run` flag. No model response; no manuscript; no tokens known.
- Writer attempt 2: corrected to positional message, same explicitly requested model, exit 1 after 1.657 s. Provider returned HTTP 429 `provider.free-limit`, retryAfterMs 25,277,000. No manuscript or model usage response. No model fallback was authorized or observed.
- Independent reviewer attempt: explicitly requested `opencode/deepseek-v4.1-flash-free`, exact candidate SHA `a9bd0fb528a1e22865fa5e07df44b314d48c1fd826a08149ecdd1d5915048b39`, exit 1 after 1.533 s. Provider again returned HTTP 429 `provider.free-limit`, retryAfterMs 23,824,000. No review response was produced. Semantic review therefore remains UNKNOWN, not PASS.
- OpenCode free-limit output does not establish whether every free model/provider is unavailable or whether any later quota reset occurred. Do not retry without new availability evidence.

## Antigravity CLI

- CLI version: 1.4.7; `agy models` listed `gemini-3.8-flash-high` as available. Listing availability is not proof of the model that served a call.
- Writer attempt 1: requested Gemini 3.8 Flash High; local CLI argument-order error, exit 2 after 0.450 s; empty stdout; no model served.
- Writer attempt 2: explicitly requested `gemini-3.8-flash-high`, text-only, no Computer Use, no filesystem tools, no permission bypass, no fallback. Exit 0 after 209.196 s. CLI JSON reported 11,386 input, 22,625 output, 2,522 thinking, 34,011 total tokens. Provider billing and actual served model identity remain UNKNOWN because the response omitted model/provider identity.
- Raw JSON SHA-256: `0dd387f0a6a54baed4ad98254e7ea2a3a8b38a1c847e7ec7641f9a37670e37f5`.
- Extracted raw response SHA-256: `cb1b507bf2ff3f3c23af083ef988eef861887ada81374386faf1bf3ba80d7f77`.
- The response is retained as UNADOPTED. It introduced unsupported claims including a 24-hour deadline, dual approval/sign-off, fake effective date/signers, a false baseline commit SHA, and fabricated `SECURE_SERVER://` / `VAULT_BOX_REAL_0136` locations. None of that response was used as the candidate manuscript or template.

## Adopted result and current gate

- Neither worker produced an adopted manuscript. The Word candidate was authored from the official source packet and the unique Blueprint; `worker_raw_response_adopted=false` and `worker_output_used_as_template=false` are recorded in the build receipt.
- Candidate R02 SHA-256: `a9bd0fb528a1e22865fa5e07df44b314d48c1fd826a08149ecdd1d5915048b39`.
- Technical package validation: PASS; 14-page Microsoft Word 16.0 render: all pages visually inspected; full-page visual QA PASS after removal of the empty page.
- Independent semantic review: UNKNOWN/BLOCKED by OpenCode provider free-limit 429. Candidate is not formally accepted.
- No Antigravity 0110 writer task was dispatched or resumed; its previously paused 0110 scope remains unchanged.

All attempted CLI processes were created without a visible console window. This applies to these bounded attempts; it does not prove every older schedule or worker was hidden.
