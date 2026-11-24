# UNIQUE_BLUEPRINT_0019_I03-E02_R01.md

**Work package:** TTQS_ONE_0019_I03_E02_UNIQUE_BLUEPRINT_W1_LONGCAT_R01_20261119
**Project:** TTQS_ONE · **Doc:** 0019 · **Requirement:** I03-E02 · **Stage:** READY_UNIQUE_BLUEPRINT
**Role:** source-bounded blueprint author (not DOCX writer, not semantic reviewer)
**Artifact status:** blueprint body only — no file written, no tools run, no QA claimed, no candidate-pass claim.

---

## 1. Requirement and source binding

### 1.1 Binding anchors (as supplied; not independently re-hashed in this run)

| Anchor | Value | Status |
|---|---|---|
| Candidate | `0019_I03-E02_R03.docx` · SHA-256 `A6DCFF55A916F8D52087B09D260CE1888252D1D4530EA37F63439045960B0CA7` · 48,468 bytes | Current candidate binding (provided context) |
| Official evidence table | `OFFICIAL_TTQS_EVIDENCE_TABLE_R04.pdf` · SHA-256 `805386B77DF045B396FABAFED7A47D12491C25A0B5744EDD9A04876CAEE34709` | Anchor hash provided |
| Crosswalk | `CROSSWALK_129_TO_142_R01.csv` · SHA-256 `1DDFBB608BCAD25170683DDA42A1DBB27BAFA6F1F35FF0498F1B8D75B24F0679` · exact row `I03-E02,1,0,0019,學員訓練及訓練機構事業發展相關的證明_可直接使用成品` | Anchor hash + row provided |
| 157-checkbox map | `BLUEPRINT_157_CHECKBOXES_LIVE_R01.md` · SHA-256 `AD03323D591CBEA62814A8A59D233110587F2741BED8F944380B1FAA2D04D216` | Literal search for `I03-E02` and `0019` → **no match**; no blueprint row exists to reuse |
| Stale QA receipt | SHA-256 `5A204A6B3F24CD275A2B79DA86A82A4CB8E23F914040A41CA9E60FF8BCB2DF7E` · 48,321 bytes · FAIL | **Stale — not QA of this candidate.** Its false checks `calculations_reconciled` and `source_sha_present` require independent bounded verification, not automatic acceptance |

### 1.2 Requirement text
- Historical source-readback quote: **“學員訓練及訓練機構事業發展相關的證明。”**
- Locator: **page 1, `PDF_TEXT_EXACT_PAGE_MATCH`**.
- Status: **HISTORICAL READBACK** — supplied in the work package; the PDF was **not** re-opened or re-verified here.

### 1.3 UNKNOWN (unsupported by available anchors)
- Underlying real activity sources for every identifier/date/hour/outcome: **UNKNOWN**.
- Official source content beyond the listed anchors: **UNKNOWN** (not verified).
- Original third-party records (certificates, approvals, signatures, attendance, outcomes): **UNKNOWN**.
- Whether the candidate bytes in this environment still match `A6DCFF…` / 48,468 bytes: **UNKNOWN** pending bounded re-hash (no tools used here).

---

## 2. Purpose, reader, use moment, genre, sections, workflow

- **Purpose (DERIVED):** an evidence-record/index that shows learner-training/completion evidence and institution-business-development evidence exist, are tracked **separately**, and are traceable to source locators — without representing the candidate as a third-party original.
- **Reader (DERIVED):** internal QA, TTQS reviewers, and audit package assemblers.
- **Use moment (DERIVED):** evidence audit / review-package assembly and replacement verification.
- **Genre (DERIVED from SAMPLE facts):** evidence-record/index; **not** a third-party original, **not** a certification, **not** an original certificate.
- **Required operational sections/fields (DERIVED):**
  1. Binding header (doc/requirement/candidate hash).
  2. Requirement quote + locator + readback status.
  3. Learner-training evidence path.
  4. Institution-business-development evidence path.
  5. Verification status and exceptions.
  6. Correction trail.
  7. SAMPLE→REAL replacement register.
  8. Review and access controls.
  9. Residual source limitations.
- **Evidence workflow (DERIVED):** source identification → locator/version capture → SAMPLE tagging → verification attempt → exception logging → correction trail → replacement-register update → review → access control.

---

## 3. Two separate evidence paths

### Path A — Learner training / completion evidence
| Aspect | Value |
|---|---|
| Scope | Learner training and completion evidence only |
| Source type | Learner training/completion records (SAMPLE synthetic) |
| Real source | **UNKNOWN** |
| Locator/version | Candidate-relative locator + version tag; original locator **UNKNOWN** |
| Traceability | Candidate item ID → replacement-register ID → correction-trail ID |
| Verification | **N/A** until originals obtained |
| Exceptions | Log any missing/unverifiable learner item; do not substitute |
| Correction trail | Record every SAMPLE→REAL substitution attempt and outcome |
| Review | QA review of path completeness and tagging |
| Access controls | Restricted to QA/review roles; no external distribution of SAMPLE data |

### Path B — Institution business-development evidence
| Aspect | Value |
|---|---|
| Scope | Institution business-development evidence only |
| Source type | Institution business-development evidence (SAMPLE synthetic) |
| Real source | **UNKNOWN** |
| Locator/version | Candidate-relative locator + version tag; original locator **UNKNOWN** |
| Traceability | Candidate item ID → replacement-register ID → correction-trail ID |
| Verification | **N/A** until originals obtained |
| Exceptions | Log any missing/unverifiable institution item; do not substitute |
| Correction trail | Record every SAMPLE→REAL substitution attempt and outcome |
| Review | QA review of path completeness and tagging |
| Access controls | Restricted to QA/review roles; no external distribution of SAMPLE data |

**Separation rule (DERIVED):** Paths A and B must remain distinct; no cross-merge, no shared synthetic values, no blending of learner outcomes with institution outcomes.

---

## 4. SAMPLE/REAL truth boundary and replacement register

- **Boundary:** All identifiers, dates, hours, and outcomes in the candidate are **SAMPLE/SYNTHETIC** and must remain so until replaced.
- **Prohibited fabrication:** names, attendance, certificates, signatures, institutional approval, outcomes, third-party records.
- **Verification status:** **N/A** while underlying real activity sources are **UNKNOWN**.
- **Replacement register (required fields, DERIVED):**
  - Field/item ID
  - Current SAMPLE value (or descriptor)
  - Real source location (path/locator/version)
  - Replacement owner
  - Status (`SAMPLE` / `IN_PROGRESS` / `REPLACED` / `BLOCKED`)
  - Verification evidence reference
  - Date of change
  - Correction-trail reference
- **Rule:** No field may leave `SAMPLE` status without a real-source reference and verification evidence; otherwise it stays explicitly `BLOCKED`/`UNKNOWN`.

---

## 5. Negative-neighbor exclusions

| Neighbor | Identity | Exclusion |
|---|---|---|
| 0018 | I03-E01 — training-system chart | Do **not** merge its content or requirements into 0019 |
| 0020 | I03-E03 — training types/KPI | Do **not** merge its content or requirements into 0019 |

No shared rows, no borrowed fields, no cross-requirement claims.

---

## 6. Acceptance checks

**Deterministic QA (concise):**
- **QA-1:** Candidate name = `0019_I03-E02_R03.docx`, SHA-256 = `A6DCFF…0CA7`, size = 48,468 bytes; stale receipt hash/size not used.
- **QA-2:** Exact quote “學員訓練及訓練機構事業發展相關的證明。” present and tagged HISTORICAL READBACK (page 1, `PDF_TEXT_EXACT_PAGE_MATCH`).
- **QA-3:** Exact crosswalk row `I03-E02,1,0,0019,學員訓練及訓練機構事業發展相關的證明_可直接使用成品` present.
- **QA-4:** 157-checkbox map recorded as **no match** for `I03-E02`/`0019`; no invented row.
- **QA-5:** Paths A and B present, separate, and free of 0018/0020 content.
- **QA-6:** Every identifier/date/hour/outcome tagged SAMPLE/SYNTHETIC; replacement register complete.
- **QA-7:** Verification = N/A where originals UNKNOWN; zero fabricated names/attendance/certificates/signatures/approval/outcomes/third-party records.
- **QA-8:** Percentages recomputed and shown as **unverified claims**: 12/16 = 75.0%, 17/18 = 94.4%, 16/18 = 88.9% (arithmetic consistent; underlying counts unverified).
- **QA-9:** Exceptions and correction trail present.
- **QA-10:** Review and access controls present.
- **QA-11:** Residual limitations present.
- **QA-12:** No claim that the candidate passes; no DOCX rewrite.

**Independent semantic reviewer:**
- Coherence of purpose/reader/use-moment/genre.
- No generic TTQS filler; no invented fields or rows.
- Clear SAMPLE/REAL boundary and traceability completeness.
- Negative-neighbor exclusion respected.

---

## 7. Residual source limitations

- Requirement quote is **historical readback**; the PDF was not re-opened here.
- Candidate hash/size not re-hashed in this run (no tools used).
- Stale QA receipt is **not** valid QA of this candidate; `calculations_reconciled` and `source_sha_present` remain **unverified** pending independent bounded checks.
- 157-checkbox map has **no** I03-E02/0019 row; blueprint cannot derive a checkbox obligation from it.
- Underlying real activity sources are **UNKNOWN**; all verification is **N/A**.
- Percentages 12/16=75.0%, 17/18=94.4%, 16/18=88.9% are **claims to re-compute**, not trusted evidence.
- Official source verification is limited to the anchors listed in §1.1; nothing further is claimed.

---

**Blocker note:** No blockers to producing this blueprint. Two items remain open for the downstream stage: (1) independent bounded re-hash/verification of the candidate against `A6DCFF…` / 48,468 bytes, and re-check of `source_sha_present` and `calculations_reconciled` (the stale receipt must not be reused); (2) confirmation that the 157-checkbox map genuinely has no I03-E02/0019 row, so no checkbox obligation is asserted. No files were written and no tools were called.