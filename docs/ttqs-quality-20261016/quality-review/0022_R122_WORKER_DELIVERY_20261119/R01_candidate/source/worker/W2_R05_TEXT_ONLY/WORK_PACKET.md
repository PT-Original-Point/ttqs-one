# TTQS ONE exact-candidate scoped semantic review
work_id: TTQS_ONE_0022_I04-E01_R01_Q10_REPAIR_EXACT_SHA_SEMANTIC_W2_R05_20261119
project_id: TTQS_ONE
doc_id: 0022
requirement_id: I04-E01
role: independent semantic reviewer; text-only; no document editing or command execution
requested_model: gemini-3.8-flash-high
served_model: UNKNOWN unless native provider evidence establishes it

## Exact candidate binding
- Candidate DOCX SHA-256: 859B09906F9E7045E7C55090E81AB5AA84FA610423988BC870559BFDF0BB8F2F
- Candidate bytes: 48272
- Current full extracted review text SHA-256: D99C0DB5A32557022766B68AFC68C3C41A2098B2B39DF73A613574A6D6A568EC
- Rendered PDF SHA-256: 6563E9F5D68FD880981FC6894604F6AC0A60FD0EE645A20C8288D6621D7171AF (9 pages)
- This is a scoped follow-up to prior W2 review R04, which reviewed DOCX SHA BA3650445179F50FCE75E5F9EEFDFAAD813DC6978B40D80BEE201FA3CD2A8C3D and returned SEMANTIC_PASS with one nonblocking observation: Section 7 T2 Q10 count showed 1 while Section 6.3 and SYN-0022-013 showed 0.
- The sole DOCX text-node delta is Section 7 ranking row T2 Q10 `1 -> 0`; current DOCX is byte-bound by Codex-side SHA verification. Review only this repair and its immediate arithmetic/ranking consequences. Do not re-review unrelated sections or invalidate R04 unchanged-scope PASS.

## Exact current extracted excerpt (from the bound full-text SHA above)
Ranking rule: average descending; ties by demand ratio (>=4) descending; then by Q10 direct single-choice count descending.

Section 6.3 Q10 direct counts (n=6):
- T1=2 (33.3%)
- T2=0 (0.0%)
- T3=1 (16.7%)
- T4=1 (16.7%)
- T5=1 (16.7%)
- Other=1 (16.7%)
- Total=6 (100.0%)

Section 7 ranking rows (Q10 count column):
1 | T1 | average 3.83 | demand 66.7% | Q10 2
2 | T2 | average 3.83 | demand 66.7% | Q10 0
3 | T5 | average 3.50 | demand 50.0% | Q10 1
4 | T3 | average 3.20 | demand 40.0% | Q10 1
5 | T4 | average 3.17 | demand 33.3% | Q10 1

Synthetic register SYN-0022-013, value: T1=2,T2=0,T3=1,T4=1,T5=1,Other=1; total 6.

Current decision statement remains: SAMPLE priority is T1; T2 is the next priority. Figures are synthetic, n=6, not population inference or actual institutional performance.

## Required review
1. Check whether the three Q10 representations (Section 6.3, Section 7, SYN-0022-013) now agree exactly for T2 and totals.
2. Check whether the stated tie-break rule and displayed rank order are consistent: T1 and T2 tie on average and demand ratio, then T1 has 2 direct Q10 votes versus T2 0; T2 remains ahead of T5/T3/T4 by average/demand criteria.
3. Decide whether the one-cell correction introduces a blocking semantic, usability, arithmetic, or SAMPLE/REAL-boundary issue. Do not treat the prior R04 finding as still present if the supplied current excerpt resolves it.
4. Review only this bounded scope. State that unchanged R04 scope is carried forward only if the supplied before/after evidence supports that; no broad document re-review.

## Output format
Return a concise report with:
- exact work_id, candidate DOCX SHA, extracted-text SHA
- `identity_match: MATCH/MISMATCH`
- `scoped_verdict: PASS/FAIL`
- whether the R04 finding is resolved
- exact arithmetic and ranking check
- any blocking finding with exact locator, or NONE
- any nonblocking finding with exact locator, or NONE
- scope boundary and served model (`UNKNOWN` unless independently evidenced)

No edits, tools, command execution, or claims of formal acceptance.
