```json
{
  "doc_id": "0121",
  "requirement_id": "I19-E09",
  "candidate_sha256": "ba067fdb2b90f99b9b354a6edc9d176d5af9527febdaaa71e6c550125f22b539",
  "verdict": "PASS",
  "assessment": {
    "genre": "PASS — P001–P003, T01–T03: analysis/evaluation report with embedded usable instruments and evidence tables, not an empty shell or policy essay; matches Blueprint §2.",
    "title_blind_identity": "PASS — P001 title『學員滿意度與學習評量報告』+ T01 mapping 0121/I19-E09; body unambiguously identifies a learner-satisfaction/skill-learning report serving I19-E09『提出學員滿意度、考試測驗或心得報告（學習技能面）』.",
    "negative_neighbors": "PASS — §2.2 (P014–P022) separates 0120/I19-E08 (P015–P017) and 0122/I19-E10 (P018–P020); no shared cohort, no re-labeled 0120 data, no 0122 follow-up claims; fixed case ID SAMPLE-0121-C01 asserted at P017.",
    "operational_usability": "PASS — T02 use card, §3 timings marked SAMPLE, §3.3 inclusion/exclusion, §4 data dictionary T05 with formulas/missing rules/keys, §12.2 register; an administrator/instructor could execute the flow.",
    "complete_instrument_data_calculation_case": "PARTIAL→effective PASS — 10-item 1–5 scale instrument §5.2 with all Blueprint §3.5 dimensions except a scored 'improvement priority' item (see NBL-02); full row-level data T07/T10/T11, flow T06, rubric T09, CAPA T15; T03 medium nonconformity in title quotation noted below."),
    "arithmetic_and_denominators": "PASS — all figures recomputed from included rows: column sums 40/39/40/34/31/37/34/33/35/32 with n_i=9/9/9/9/9/9/8/8/8/8; positive counts 9/9/9/6/4/8/8/7/8/6; rates 100/100/100/66.7/44.4/88.9/100/87.5/100/75.0%; composite Σ=333, 333÷80=4.1625≡ΣX̄ 33.30÷8; flow 10=8+1+1; paired pre 310→38.75, post 690→86.25, Δ=380÷8=+47.50; pass 7÷8=87.5%; per-task T01/T02/T03/T04/T05 sums 60/60/40/70/80 pre, 150/150/110/130/150 post, full-mark rates 87.5/87.5/37.5/62.5/87.5% — all exact. Item means use n_i (never invited count); N/A never counted as zero; pass-rate denominator = assessable tests (8).",
    "sample_real_boundary": "PASS — P003, T01, T03, T09, §7.2, §10.1, T15, T16: every synthetic fact flagged; §12.2 all keys HELD; REAL EVIDENCE NOT PROVIDED; 70-point threshold SAMPLE (P101–P102); no association performance claims.",
    "anti_fabrication": "PASS — §12.3 T17 sign-off not prefilled; serial UNKNOWN_NOT_ASSERTED; no fabricated attendance/signatures/approvals/certificates; P010 disclaimer that methods are demonstrative, not association-approved.",
    "evaluator_use": "PASS — recomputation instructions §9.1/P116, closure/hold triggers per CAPA row, HOLD criteria P005, evaluator columns T15/T17; external reviewer can re-derive each statistic.",
    "rendering_typography": "UNKNOWN — text-only review: fonts (≥10.5pt/9.5pt), page inspection and clipped-cell checks cannot be evidenced."
  },
  "blocking_findings": [],
  "nonblocking_findings": [
    { "id": "NBL-01", "locator": "T01, row『官方要求原文』(P000 block)", "reason": "Quoted official wording renders『提出學員滿意度、考試測驗或心得報告（學習技能面）。』with the period outside the parenthesis, whereas the packet-stated official wording is『…（學習技能面。）』with the period inside. Semantically identical 9-character string; correct at Human Gate if byte-exact quotation of the official source is required." },
    { "id": "NBL-02", "locator": "§5.2 (P063–P080)", "reason": "Blueprint §3.5 lists 'improvement priority' among required distinct dimensions; in the candidate it is addressed by the optional open item Q12 and the CAPA §11 priority ranking, not by a scored 1–5 item. Instrument still meets ≥10 scaled items; flag for completeness of dimension coverage." },
    { "id": "NBL-03", "locator": "§6.1 T06 row P10 vs §8.2 P111 and T11 P10 remark", "reason": "P10's absence reason is described as『未出席示範課程』in T06 and the T11 remark, but『因病請假全日缺考』in §8.2 — inconsistent synthetic-fact detail; harmonize in the register." },
    { "id": "NBL-04", "locator": "§4 T05 rows (綜合滿意度有效率/綜合總平均) vs §12.2 T16", "reason": "Register key REP-0121-004-RATE defined in T05 has no corresponding row in the replacement register T16 (REP-0121-004-P01..P10 and REP-0121-010 exist); minor register gap." },
    { "id": "NBL-05", "locator": "§2.2 P017 vs §6.2/§12.2", "reason": "Case ID SAMPLE-0121-C01 is declared as the fixed case code but does not appear in data-table rows or in T16 register keys (which use REP-0121-CASE-001); add the case ID to the register for airtight traceability." }
  ],
  "limitations": {
    "review_scope": "Text-only semantic review of the packet body; no binary, visual, layout or hash recomputation performed. Documented SHAs (source fbeb11b9…, Blueprint 99320fdc…, candidate ba067fdb…, body extract 4ea875c2…) taken as asserted, not verified.",
    "staleness_note": "Packet internal metadata cites PR #92 HEAD 70d7ca0fb0fe8e56e2da8b3c54f67e37bef59e64 (R12 W1; content dated 2026-10-27, R03), while the current-state override fixes HEAD at 3cfabbc9aade6c6bf0383e604ccbc2b3b0063cda (R14). Treated as packet-metadata staleness only: the candidate DOCX SHA above is unchanged per the current-state override and remains the sole review anchor; this review does not change the candidate SHA.",
    "blueprint_coverage": "Blueprint sections 6 (synthetic-data design) and 11 (freshness metadata) were not pasted into the packet; conformance to those sections is assessed only indirectly from body coverage and is PARTIAL/UNKNOWN.",
    "source_access": "Official evidence-table page 8 not independently viewable; page-8 locator taken from packet.",
    "not_granted": "This review is not association approval and does not constitute formal acceptance; Human Gate remains NOT_GRANTED, REAL evidence NOT PROVIDED."
  }
}
```