Prepare a narrowly scoped repair patch for the 0059 Unique Blueprint. Do not edit or regenerate the DOCX or its body.

Identity:
- TTQS_ONE; DOCX 0059 = I13-E03 = official checkbox 063.
- Candidate DOCX R03 SHA-256 is 0263017F16D81B1121BB97410DE9895B43B7A42F75632BF71A82B86426FBC2B0 and must remain unchanged.
- The attached final body R03 is the source of truth for what this candidate actually contains. The attached Unique Blueprint R01 is an earlier draft. The Beam independent audit flagged stale blueprint claims.

Find every outdated or conflicting occurrence throughout the whole Blueprint and return exact, minimal text replacements:
1. Mechanism usefulness index is 4.1/5 = 209/51, not 4.2/5.
2. Questionnaire timing in the final body is 113/12/01–113/12/08; do not retain “sixth week” or August timing from the old draft.
3. Mechanism C is a synthetic in-scenario process comparison (12/18=66.7%), not independent external issuer verification. The body does not claim completed real issuer checks. Correct titles, labels, metrics, examples, IMP-03, and any external verification claims as needed; preserve that real certificates and issuer replies remain unavailable/UNKNOWN.
4. Correct any typo treating the 113/12/15 consolidation cutoff as “11 years” to 113/12/15.
5. Scan for other specific body-versus-Blueprint divergences. Do not change content that already agrees with the final body or official authority.

Return exactly one JSON object with keys:
blueprint_r01_sha256_if_visible, candidate_docx_sha256, replacements, change_log, unresolved.
Each replacement must be an object with fields search_exact, replace_with, body_locator, reason, expected_occurrences. Use exact verbatim snippets present in the Blueprint for search_exact and enough surrounding text to apply safely. Keep replacements minimal, but include every occurrence of a conflicting claim. Use only facts stated in the body. If a requested detail is absent from the body, do not invent it; list it in unresolved.
The patch must preserve the Blueprint’s official source and requirement mapping, distinct doc_id/checkbox mapping, and all unrelated sections unchanged. No tools or external lookup. No markdown fences.
