### Independent Review: DOCX 0139 R06 Formula Changes

**Target Artifact:** DOCX 0139 R06  
**Exact Candidate SHA-256:** `75e7a55461e3ffd067c154cfd48a4e67256bf432e379affcda84b2ed04e33938`  
**Requirement Mapping:** Official Requirement I19-E29 (“證照通過率高及就業率大幅提升。”), Blueprint Row 153  
**Data Status:** SAMPLE / SYNTHETIC (REAL = UNKNOWN / HOLD)  
**Acceptance Status:** Formal acceptance **NOT_GRANTED**  
**Inspection Scope:** Restricted exclusively to the two formula changes specified below. Document layout and unedited document sections were **not** inspected.

---

### Review Verdict: **PASS**
*(Tied strictly to candidate SHA-256: `75e7a55461e3ffd067c154cfd48a4e67256bf432e379affcda84b2ed04e33938`)*

---

### 1. Independent Calculations & Analysis

#### Change 1: Exam Pass Rate Relative Change
* **Source Counts:**
  * 2023 Baseline: $5 \text{ passes} / 8 \text{ examined} = 0.625000 = 62.5000\%$
  * 2025 Current: $8 \text{ passes} / 11 \text{ examined} = \frac{8}{11} = 0.\overline{72}\% \approx 72.72727...\% \xrightarrow{\text{round to 4 dp}} 72.7273\%$
* **Absolute Change (Percentage Points, pp):**
  * Exact: $\frac{8}{11} - \frac{5}{8} = \frac{64 - 55}{88} = \frac{9}{88} \approx +0.1022727... \text{ (+10.2273 pp)}$
  * Displayed rates difference: $72.7273\% - 62.5000\% = +10.2273\text{ percentage points}$
* **Relative Change Calculation:**
  * Theoretical exact: $\frac{9/88}{5/8} = \frac{9}{55} \approx 0.16363636... \approx +16.3636\%$
  * Computed from displayed 4-decimal rates as rendered:
    $$\frac{72.7273\% - 62.5000\%}{62.5000\%} \times 100\% = \frac{10.2273\%}{62.5000\%} \times 100\% = 16.36368\%$$
  * Rounding to 2 decimal places:
    $$16.36368\% \approx +16.36\%$$
* **Formula Evaluation:**
  * **R05 Form:** `72.7273% - 62.5000%/62.5000% = 10.2273%/62.5% ≈ +16.36%` suffered from standard operator precedence ambiguity (without parentheses, division binds before subtraction: $A - B/B = A - 1$).
  * **R06 Form:** `(72.7273% − 62.5000%) / 62.5000% × 100% = 16.36368% ≈ +16.36%` explicitly introduces grouping parentheses `( ... )`, clarifying that the numerator difference is taken first, followed by baseline division and scaling by $100\%$. The intermediate calculated value `16.36368%` and final rounded figure `+16.36%` are strictly accurate.

---

#### Change 2: Employment Confirmation Rate Relative Change
* **Source Counts:**
  * 2023 Baseline: $4 \text{ confirmed} / 10 \text{ in cohort} = 0.400000 = 40.0000\%$
  * 2025 Current: $8 \text{ confirmed} / 12 \text{ in cohort} = \frac{2}{3} = 0.\overline{6}\% \approx 66.66666...\% \xrightarrow{\text{round to 4 dp}} 66.6667\%$
* **Absolute Change (Percentage Points, pp):**
  * Exact: $\frac{2}{3} - \frac{2}{5} = \frac{10 - 6}{15} = \frac{4}{15} \approx +0.2666666... \text{ (+26.6667 pp)}$
  * Displayed rates difference: $66.6667\% - 40.0000\% = +26.6667\text{ percentage points}$
* **Relative Change Calculation:**
  * Theoretical exact: $\frac{4/15}{2/5} = \frac{4}{15} \times \frac{5}{2} = \frac{2}{3} \approx 0.666666... \approx +66.6667\%$
  * Computed from displayed 4-decimal rates as rendered:
    $$\frac{66.6667\% - 40.0000\%}{40.0000\%} \times 100\% = \frac{26.6667\%}{40.0000\%} \times 100\% = 66.66675\%$$
  * Rounding to 2 decimal places:
    $$66.66675\% \approx +66.67\%$$
* **Formula Evaluation:**
  * **R05 Form:** `66.6667% - 40.0000%/40.0000% = 26.6667%/40.0% ≈ +66.67%` suffered from the same operator precedence defect ($A - B/B = A - 1$).
  * **R06 Form:** `(66.6667% − 40.0000%) / 40.0000% × 100% = 66.66675% ≈ +66.67%` adds explicit parentheses around the numerator difference. Both the intermediate value `66.66675%` and the final rounded figure `+66.67%` are mathematically exact.

---

### 2. Distinction: Percentage-Point Change vs. Percent Relative Change

| Metric | Percentage-Point Change (Absolute Difference) | Percent Relative Change (Proportional Growth) |
| :--- | :--- | :--- |
| **Formula** | $\text{Rate}_{2025} - \text{Rate}_{2023}$ | $\frac{\text{Rate}_{2025} - \text{Rate}_{2023}}{\text{Rate}_{2023}} \times 100\%$ |
| **Exam Pass Rate** | $+10.2273\text{ pp}$ ($\approx +10.23\text{ pp}$) | $+16.36368\% \approx \mathbf{+16.36\%}$ |
| **Employment Confirmation Rate** | $+26.6667\text{ pp}$ ($\approx +26.67\text{ pp}$) | $+66.66675\% \approx \mathbf{+66.67\%}$ |

R06 accurately computes and labels **relative change**, correctly using the absolute percentage-point difference in the numerator over the base rate.

---

### 3. Precedence Ambiguity and Boundary Assessment

1. **Resolution of Precedence Ambiguity:**  
   R06 successfully resolves the mathematical syntax flaw present in R05 by enforcing standard grouping parentheses `(Rate_current − Rate_baseline) / Rate_baseline × 100%`.
2. **Preservation of the Sample / Real Boundary:**  
   The revision modifies only the mathematical presentation of the formula paragraphs. It does not alter counts, introduce real data, or violate data governance constraints. All figures remain strictly **SAMPLE / SYNTHETIC (REAL = UNKNOWN / HOLD)**.

---

### 4. Defect Summary

* **Defects Found:** **0**
* **Conclusion:** PASS for SHA-256 `75e7a55461e3ffd067c154cfd48a4e67256bf432e379affcda84b2ed04e33938`. Formal acceptance is **NOT_GRANTED**.

