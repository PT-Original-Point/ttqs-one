# Independent register locator follow-up - DOCX 0051 R01

This is a bounded supplement to the full OpenCode v2 semantic review. Do not edit files and do not repeat the full-document review.

- Candidate DOCX exact SHA-256: 6f575ebb41c6c26b4d6b36262fb4d9a5abdae53cbdc1ff4e75acda46d5f0b495.
- Replacement register: evidence/SYNTHETIC_REPLACEMENT_REGISTER_R01.csv.
- Required register SHA-256: 57da26117ebaf3a517af4fe040d54661ca1021faa1202d19d651b3a51866f707.
- Earlier full review returned PASS on the same DOCX SHA and the preceding register SHA cddc262b205850d9bbdc9297c316d901783b56b66d03d05e3e7af33889d94266. It noted the unit-objective rows F024-F027 omitted section 6 table 12 from their locators. The register-only repair added §6表12; DOCX bytes were not changed.

Recompute both hashes. Verify the new register is 227 rows, has 227 unique IDs F001-F227, no blank locator/replacement/status fields, and every status is SAMPLE_ONLY_NOT_VERIFIED_AS_REAL. Inspect F024-F027 and confirm each locator includes §3表6, §5表7 / 表9–10, and §6表12. Confirm these locators agree with the candidate body and that the repaired register does not change any sample values. Return PASS/PARTIAL/FAIL with concise exact evidence. Do not grant Human acceptance or association approval.
