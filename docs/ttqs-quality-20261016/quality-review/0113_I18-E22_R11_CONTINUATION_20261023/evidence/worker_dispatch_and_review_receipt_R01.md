# 0113 R01 worker and reviewer execution receipt

Scope
- TTQS ONE document_id 0113; project crosswalk I18-E22; official printed checkbox serial UNKNOWN.
- All writer inputs and numerical examples are synthetic. No real association roster, approval, person, signature, or performance fact was created.
- This receipt distinguishes requested CLI/model from evidence of a served model. Antigravity stdout did not expose a reliable actual-model identity.

Antigravity CLI writer
- Executable: C:\Users\J\AppData\Local\agy\bin\agy.exe, version 1.4.6.
- Requested model: gemini-3.8-flash-high. Actual served model: UNKNOWN.
- Observed OS writer PID during the final-generation call: 41220. It was not treated as a continuing writer after stdout was collected.
- Tool/Computer Use: no tool directory was supplied; returned JSON showed no tool-call record. No Computer Use was invoked.
- Attempt 1: CLI option-parser error; stderr SHA-256 A56E70B151B6BC03877544BFE622D52286C41B4AEB1328223EEDA62C9110C21C; no model dispatch/output.
- Attempt 2: CLI returned output, but Windows UTF-8 console decoding corrupted captured Chinese. Raw JSON SHA-256 1AE23A5658EDCCA123600B514DEF07163E3C17CD601842F84D77E16F8BCBCC3C; 39,026 bytes; not adopted.
- Repair: switched the same process capture to UTF-8 and used the existing conversation ID rather than starting a duplicate writer. Recovery request SHA-256 9EDE86DEA4FD55746FD4F60A594945DBFDB5755DF934F4EB6A6A7951B5E7474F.
- Recovery raw JSON SHA-256 D5CD71236EEC8552A9D6D86A49E06DA66353ABCD0E0BF6B5B99B4A481D0A71D0; 25,494 bytes; CLI exit 0, stderr empty.
- Reported usage is cumulative for two conversation turns: input 38,158; output 24,522; thinking 4,134; total 62,680 tokens. The CLI did not expose exact per-call usage or actual served model; do not treat the total as one invocation.
- The response was not adopted verbatim. Adoption review removed unsupported association roles, invented governance rules, arbitrary thresholds, unsupported statistical claims, and unsafe data-handling suggestions. The corrected manuscript SHA-256 is 24A496CE239C1A01D657F9FB2A68AC811F64D80AF5D5CD0CFB9B84899D87187B.

OpenCode v2 reviewer
- Requested free model: opencode/glm-5.3-flash-free, selected from the current CLI model list.
- One reviewer invocation returned provider.quota HTTP 429 “Free usage limit reached” before generating a review. Exit code 1, duration about 1.8 seconds; no reviewer text and no semantic result.
- That failed attempt targeted a superseded DOCX SHA C058C1AF2CA416EB8C10C953924EEAB3EF82465D461CF3C8AEFA49AFCA56AE1A. It cannot be transferred to the current final candidate.
- Current final DOCX SHA-256: 5F6D86A11FF884F7D0F1C251BF9B0DD4AA10B41DEFC68E2D1EA51B1AFB329821. Independent semantic review on this exact SHA is BLOCKED / NOT RUN. The 429 is not a PASS, PARTIAL, or FAIL.
- No retry was made after the free quota error. OpenCode’s resident service PID is not evidence of a live reviewer.

Current document state
- DOCX exists and is technically/layout checked; 10 pages rendered through a separate Word COM instance and every page was visually inspected.
- Technical/layout QA receipt: docx_technical_visual_qa_R01.json.
- Semantic result: BLOCKED / NOT RUN for the exact current SHA; see semantic_review_status_R01.md.
- Formal association acceptance and REAL evidence: NOT CLAIMED.
