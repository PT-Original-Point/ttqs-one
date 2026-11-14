**Verdict: `PARTIAL` — blocking count: 1**

Bound to the packet-declared DOCX SHA-256 `bde9a803c18137c98cf64992d75066b0722b5c3d3794eb7d6ab38667b88d0f19` (46-page PDF SHA `6220a5641d6963badad457da99a05cb13e5c76d92088136e504da5bddb4a4918` as stated). This is a packet-only consistency review: no files opened, no rehash, no independent arithmetic or image inspection. State remains `CANDIDATE_ONLY`; no formal TTQS acceptance and no REAL survey, approval, signature, or execution is asserted.

**R12 observations**

| Observation | Status | Evidence |
|---|---|---|
| `OB-R12-01` | `CLOSED` | §9.1–§9.4 are reproduced in full. §9.1 separates 0093/I17D-E07 (expressly unverified), 0094/I18-E01, 0095/I18-E02, and 0096/I18-E03; §9.3–§9.4 refuse to fabricate 0094 interview material or a 0096 issuer/original. |
| `OB-R12-02` | `CLOSED` | Sensitivity is placed in §7.2; §1.4 maps §7.2 to PDF pp.31–34, and p.33 is listed in the packet’s high-resolution visual scope. |
| `OB-R12-03` | `CLOSED` | Case-opening metadata → p.23; §7.1 → p.31; §7.2 → pp.31–34; Figure A → pp.33–34; §7.3–§7.4 → p.34. These anchors are mutually consistent and within 46 pages. |
| `OB-R12-04` | `CLOSED` | §9.5 names the current `qa/0095_R14_synthetic_replacement_register.csv` and its SHA; R07/R08/R11/R12/R13 are expressly historical. Identity is unambiguous. The stale locator in F-01 is a content error, not an identity ambiguity. |

**Required checks**

- **(a) PASS** — Official requirement remains 指標18 and the exact I18-E02 checkbox text; the genre remains system/process mechanism design, not a claim of completed survey results.
- **(b) PASS** — 0094/I18-E01 and 0096/I18-E03 are distinguished by official text and role; 0093 is marked unverified; no neighboring original, issuer, signature, or content is fabricated.
- **(c) PARTIAL** — §1.4 and §9.5 agree internally: §9.5 pp.39–42, row 3 p.39, rows 7–8 p.41; §10 pp.42–46. But the current-register locator for `UNK-0095-UNK_FORMAL_EFFECTIVE_DATE` says `PDF pp. 11, 15, 38`, which conflicts with §9.5 row 3 at p.39. See F-01.
- **(d) PASS** — Current R14 register versus historical R07/R08/R11/R12/R13 is explicit, with a distinct filename and SHA. No current/historical ambiguity.
- **(e) PASS** — §1.4 marks the relevant rows PROPOSED/SYNTHETIC; §9.5 rows 1–8 all state 未提供/UNKNOWN; REAL date fields are described as blank; no REAL survey, approval, signature, or execution is claimed.
- **(f) PASS, nonblocking** — p.5 (last §1.4 row), p.9 (last two §3.2 rows), p.20 (short §4 continuation), and p.46 (closing panel) are readable with no clipping/overlap. No blocking presentation defect; optional header/orphan polish only.

**Blocking finding F-01 — stale current-register locator**

`UNK-0095-UNK_FORMAL_EFFECTIVE_DATE` is cited to `PDF pp. 11, 15, 38`. The manuscript places §9.5 at pp.39–42 and row 3 at p.39. The packet’s own `UNK-0095-UNK_IMPROVEMENT_ORIGINALS` locator places §8.5 at pp.37–38, so p.38 cannot also be §9.5 row 3. The “0 out of bounds / 0 empty pages” check cannot catch this because p.38 is a valid page.

**Precise repair:** align the register locator with §9.5 row 3 as `PDF pp. 11, 15, 39`; verify against the PDF, and if the PDF actually places row 3 on p.38, correct §1.4 and §9.5 instead. If the CSV changes, re-issue the register/manifest SHA; the DOCX SHA need not change on the packet’s evidence.

**Limits:** Page and visual findings are tested for internal consistency, not re-observed. High-resolution visual scope excludes pp.11, 15, 25–30, and 35–38; those locators rest on contact sheets/extracted text per the packet. The DOCX body shows no blocking semantic defect; the single blocking item is the current-register locator excerpt.
