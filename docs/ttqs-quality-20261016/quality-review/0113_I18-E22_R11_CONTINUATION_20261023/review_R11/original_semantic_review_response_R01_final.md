# Independent Read-Only Semantic Review

- **Document ID / Requirement:** 0113 / I18-E22 (*會員人數年度變化追蹤分析表*)
- **Candidate DOCX SHA-256:** `5f6d86a11ff884f7d0f1c251bf9b0dd4aa10b41defc68e2d1ea51b1afb329821`
- **Review Packet SHA-256:** `bfdb8a08ec00b258bf6bf905a8d60bedfb8211a470766d66d77864a9f6c10dc6`
- **Verdict:** **PASS**
- **Finding Counts:** Blocking: **0** | Nonblocking: **0**
- **Serving Model:** **UNKNOWN** (runtime provenance attests `served_model: "UNKNOWN"`)
- **Formal Acceptance:** **NOT GRANTED** (strictly `SAMPLE / SYNTHETIC ONLY`; synthetic counts must not be cited as association facts)

---

## 1. Official Example, Genre & Cross-Document Boundaries

- **Official Source Grounding:** Correctly grounds I18-E22 in the TTQS Training Institution Checkpoint Guide (p. 7, Indicator 18, 4-point reference example: *「會員人數逐年增加。」*). It explicitly notes that the 4-point example provides no mandated growth rate, minimum cohort size, or automatic scoring guarantee (P2, P31, P50).
- **Conflation Protection:** Distinguishes the 4-point example from the 3-point example (*「會員人數及會費收入均逐年增加」*). Dues/fee revenue, course attendees, and social service counts are strictly barred from membership headcount (P13, Table 11).
- **Genre Distinction from 0112 (I18-E21):** The candidate is an annual de-duplicated membership tracking sheet, clearly separated from certification/refresher training in 0112/I18-E21, social performance in 0111, and trainee surveys in 0100/0101 (P13, Table 11).
- **Identity Safeguards:** Checkbox sequence is marked `UNKNOWN` (P2, P25, Table 13 R7), avoiding unverified numbering or confusion with 157 project index 123.

---

## 2. Four-Year Worked Use, Arithmetic & Denominators

The document executes a complete, four-period worked example (`SYN-0113-CASE-01`) using consistent annual cutoffs (December 31):

- **2022-12-31 (SYN-0113-F01):** Baseline = 42 members; Net = Baseline; YoY = N/A (P42; Tables 2, 3, 5).
- **2023-12-31 (SYN-0113-F02):** Opening 42 + Additions 8 − Exits 4 = Closing 46; Net = +4; YoY = $+4 / 42 = +9.5\%$ (P43; Tables 2, 3, 5).
- **2024-12-31 (SYN-0113-F03):** Opening 46 + Additions 9 − Exits 4 = Closing 51; Net = +5; YoY = $+5 / 46 = +10.9\%$ (P44; Tables 2, 3, 5).
- **2025-12-31 (SYN-0113-F04):** Opening 51 + Additions 10 − Exits 4 = Closing 57; Net = +6; YoY = $+6 / 51 = +11.8\%$ (P45; Tables 2, 3, 5).
- **Cumulative (2022→2025):** $57 - 42 = +15$ members; $+15 / 42 = +35.7\%$ (P46; Table 12 R8).
- **Formulas & Safeguards:** Reconciles $\text{Closing} = \text{Opening} + \text{Additions} - \text{Exits}$ across all years. The YoY denominator is strictly the prior-period closing balance; zero denominators are handled with `N/A` and `HOLD` to prevent division by zero (P9, P34). All values match identically between text (Chapter 5), tables (Tables 2, 3, 5, 12), and the synthetic dataset.

---

## 3. SAMPLE / REAL Boundaries & Data Minimization

- **Explicit Demarcation:** Every chapter and table carries prominent `SAMPLE / SYNTHETIC ONLY` labels (P2, P4, P15, P36).
- **REAL Readiness Boundaries:** Tables 1, 4, 8, 10, and 13 record all REAL prerequisites (governing definitions, approved cutoff dates, access permissions, de-duplication logs, and reviewing roles) as `UNKNOWN / HOLD`.
- **Clean-Break Rule:** Mandates that REAL implementation must be created as an independent version rather than partially overwriting synthetic cells (P83).
- **Data Minimization & Privacy:** Prohibits exporting PII (names, government IDs, phone numbers, addresses, raw member IDs) into public reports; only aggregated de-duplicated totals and non-sensitive source pointers are permitted (P8, P54, P87; Table 6).

---

## 4. Rejection Criteria & Decision Logic

Chapter 8 and Table 9 establish a robust two-tier triage:
- **HOLD Criteria:** Triggered by unconfirmed definitions, shifting cutoff dates without restatement, zero denominators, unverified permissions, or missing reviewer roles (P81, Table 9 R2).
- **REJECT Criteria:** Triggered by duplicate member counting, mixing fee revenue into member counts, mismatched comparative periods, mathematical balance failure ($\text{Opening} + \text{Additions} - \text{Exits} \neq \text{Closing}$), chart/table discrepancies, disguised synthetic data, concealing down periods, or asserting ungrounded causal claims (P81, Table 9 R3).

---

## 5. Administrator & Evaluator Usability

- **Operational Guidance:** Chapter 1 provides an executive 30-second workflow (P5–P10).
- **Audit Protocols:** Chapter 6 details internal de-duplication rules (P57–P62), Chapter 7 provides a comprehensive data dictionary and a 6-item minimum source request list (P63–P74), Chapter 10 specifies year-end closing and error-restatement paths (P91–P99), and Section 12.2 / Table 13 presents an actionable REAL pre-work gap register.

---

## 6. Review Limitations

1. **Text & Data Scope:** This semantic evaluation is based strictly on the text extractions (P1–P108) and tabular records (Tables 1–13) provided in the review packet.
2. **Visual Inspection:** Visual layout, page pagination (10 pages), typography, and embedded chart formatting are separately certified by `docx_technical_visual_qa_R01.json` (PASS).

