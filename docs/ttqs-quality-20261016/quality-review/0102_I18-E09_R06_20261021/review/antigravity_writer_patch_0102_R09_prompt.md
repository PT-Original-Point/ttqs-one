WORK_ID=TTQS-0102-I18-E09-TARGETED-CONTENT-REPAIR-WRITER-R09-20261022-01
DOC_ID=0102
REQUIREMENT=I18-E09
CANDIDATE_BEFORE_SHA256=40d0b9ecaebfdc3fba435811f57d89b797ec5512105995e808328f39a819cac9
REQUESTED_MODEL=gemini-3.8-flash-high

Produce only a compact Traditional Chinese JSON patch proposal for this existing SAMPLE/SYNTHETIC Word candidate. Do not call tools, read/write files, use a browser or Computer Use. If the requested model is unavailable, return BLOCKED without fallback. Do not introduce REAL people, organizations, awards, approvals, signatures or results.

Verified source fact from direct visual inspection of official evidence-table PDF p.7 (file SHA-256 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709): before the separately labeled 3-point and 4-point reference-evidence lists, the common-evidence block includes 「指導學員參加技能競賽獲獎」; do not describe this bullet as located in the 4-point block or as a score guarantee. A winning claim still requires source verification and must not imply training causation.

Give patch proposals for:
1. Replace the erroneous 4-point-placement sentence with one concise, accurate, cautious sentence.
2. In Form A sample table 9 CASE-02, set evidence_state to RECEIVED_UNVERIFIED; keep case status HOLD and next action clearly on hold until evidence/consent checks.
3. Clarify that R01 is the body/content version and R09 is this Word candidate revision.
4. Register the synthetic internal dates 2026-10-01, 2026-10-02, 2026-10-06, 2026-10-07, 2026-10-12 without implying actual events.
5. Clarify that 2026-10-20 is an internal SAMPLE review date, not an external due date.
6. Correct these mixed Simplified Chinese strings to Traditional Chinese: 写明, 五个問題, 我推论的, 待联系, 组别, 不等于, 这是, 邊界声明, 仅为主張.

Return JSON with keys: status, revised_official_source_sentence, table9_case02_evidence_state, table9_case02_case_status, table9_case02_next_action, version_label, synthetic_date_register_text, due_date_text, traditional_chinese_replacements. Do not add commentary.