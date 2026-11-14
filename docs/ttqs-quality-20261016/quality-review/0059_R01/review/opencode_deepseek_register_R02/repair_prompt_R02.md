You are repairing a supplemental SAMPLE/SYNTHETIC replacement register for a stable Word candidate. Do not edit or regenerate the DOCX.

Authority and identity:
- Project TTQS_ONE.
- DOCX 0059 = I13-E03 = official checkbox 063 (these identifiers are distinct).
- Candidate DOCX SHA-256: 0263017F16D81B1121BB97410DE9895B43B7A42F75632BF71A82B86426FBC2B0.
- Case SAMPLE-SYN-113. All data are synthetic, not Association records.
- The final body R03 is the primary authority for exact values and locators. The attached Blueprint is an R01 draft and may diverge; do not copy stale values from it.
- Existing 190-row register is attached. Preserve its rows and fact IDs. Add only facts materially absent from the register; do not duplicate already registered facts. Correct only locator granularity for existing F063 and F105-F116 where needed.

The independent MiMo audit found the 190 existing rows structurally sound and their inspected values/arithmetic consistent, but PARTIAL for these coverage gaps:
1. Questionnaire sections 8.3, 8.6, 8.8, 10.2: consent/skip logic (Q0); N/A/nonresponse exclusion rules; each item’s n/sum/mean (Q1 63/15, Q2 48/15, Q3 60/15, Q4 38/9, Q5-Q8 each 57/15, Q9-Q10 each 60/15); and all three index calculations (209/51=4.1, 228/60=3.8, 120/30=4.0). Copy exact item labels, denominators and rules from the final body.
2. Deduplication: section 10.4 cross-mechanism consolidated table, 16/18=88.9% real-participation rate, and any component facts needed to identify its denominator.
3. Assessment/retest: section 9.2 dimension means (22/10, 22/10, 20/10, 23/10, 29/10), sections 9.3/9.4 count entering remediation (2) and retest pass rate (1/2=50.0%), with exact source locators.
4. Improvement/authorization: section 11 IMP-01 through IMP-05, each proposal’s NOT ADOPTED status, proposed owner role, HOLD/authorization rule, and target date (114/03/31-114/06/30 as applicable); section 11.2 rejection rate 4/12=33.3%.
5. HOLD/REAL replacement: all six section 12.1 replacement-map items and Appendix B E-A1 through E-D1 hold items, with exact criteria and responsible proposed role if stated.
6. Other omitted controls: section 2 exact official-quote/source-page anchor; section 7.2.1 scenario and safety-stop/no-real-PII controls; sections 12.6-12.7 precheck items. Include only facts explicitly present in the body.
7. Locator granularity: make F063 locator cite both section 4.3 step 5 and the section 4.4 preamble, and each F105-F116 locator cite the exact table/section(s) supplying that row’s facts. Do not change their values.

Return exactly one JSON object, no markdown fences, with keys:
- additional_rows: array of objects with exactly fact_id, locator, value, why_synthetic, source_to_replace, role_to_verify, status
- locator_corrections: array of objects {fact_id, new_locator}
- coverage_map: array {gap, covered_by_fact_ids}
- limitations: array of any body fact you could not locate or verify.

Assign new IDs sequentially from SYN-0059-113-F191 onward. Each row must be one fact or one indivisible control, not a paragraph summary. Use exact body values and concise exact locators. Every new row status must be SAMPLE_UNVERIFIED. Keep replacement sources prospective or UNKNOWN; never claim a real original exists. Keep role_to_verify as a proposed role, not an appointed person. Do not invent details. If the body does not state a requested fact, report the gap in limitations rather than filling it.

No tools or external lookup. Return only the requested JSON.
