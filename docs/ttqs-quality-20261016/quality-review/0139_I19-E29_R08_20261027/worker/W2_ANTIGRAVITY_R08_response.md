### TTQS ONE 0139 R08 Exact-SHA Delta Semantic Review

**Verdict:** `PASS_DELTA`  
**Target Candidate DOCX SHA-256:** `d31ef2d8b8615f3dd314572c4e50b6604198e8f24faafb144bcbaea7373c696f`  
**Extracted Text SHA-256:** `04ec584f28f71295ddc0f701c82df655ab6de07e7f7ec990a2ff20462fb97df1`  
**Serving Model Identity:** Not exposed by CLI response headers/payload (unverified routing; per protocol, unexposed runtime metadata is not presumed).

---

### Delta Verification & Corrected Findings

The deterministic delta between R07 and R08 consists of five exact text substitutions in `word/document.xml`. Each item has been verified against the exact extracted text:

| Item | Finding / Scope | Locator | Exact R08 Excerpt | Verification Status |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Parentheses addition (2023, $n=10$) | §7.2 A.2 | `追蹤狀態涵蓋率 = (4 + 2)/10 = 6/10 = 60.00%` | **VERIFIED** |
| **2** | Parentheses addition (2024, $n=12$) | §7.2 B.2 | `追蹤狀態涵蓋率 = (7 + 2)/12 = 9/12 = 75.00%` | **VERIFIED** |
| **3** | Parentheses addition (2025, $n=12$) | §7.2 C.2 | `追蹤狀態涵蓋率 = (8 + 2)/12 = 10/12 = 83.33%` | **VERIFIED** |
| **4** | Key naming alignment in QC check | §13.1 (QC-08) & §12.1 | §13.1 QC-08: `第 12 節已登錄自 KEY-COH-001 至 KEY-DATE-001 等全要素管制鍵`<br>§12.1: `KEY-DATE-001` (`90 日考照窗、D+180、D+170 至 D+190`) | **VERIFIED** |
| **5** | Document version descriptor | §14 | `文件版本：DOCX 0139 候選 R08` | **VERIFIED** |

---

### Governance & Semantic Boundary Confirmation

- **Syntactic & Arithmetic Precision:** All three tracking coverage formulas now include strict grouping parentheses, eliminating precedence ambiguity while remaining mathematically identical to table summaries (§7.1 and §7.3).
- **Register Consistency:** QC-08 now cites `KEY-DATE-001`, fully matching the data dictionary key definition in §12.1.
- **Candidate Discipline Preserved:** §1, §13.2, and §14 strictly maintain `SAMPLE / SYNTHETIC`, `REAL=UNKNOWN/HOLD`, and `NOT_GRANTED` designations. No formal approval is inferred.
- **Remaining Blockers:** None (`0`).