```json
{
  "receipt_type": "independent_exact_sha_semantic_review",
  "review_id": "0010-I02-E01-R04b",
  "reviewed_at_utc": "2026-10-29T22:20:18Z",
  "candidate_sha256": "9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
  "candidate_sha256_before_review": "9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
  "candidate_sha256_after_review": "9e0cf56a96bd6139c6f90915e94ae820f9eb4fffed063b75c199b8da2e8965fe",
  "source_markdown_sha256": "b16f1c4e9f674b6b6a1258a09192a87f40d4e92430810091fe2eadfe228aba47",
  "extracted_text_sha256": "41212d79d37d23144c4305141f4e3b13e048a0e0dd02e51e64d01edd5ab30e74",
  "register_sha256": "6a424099b25613ad930cfc638bcb846b4914294d092c01902a943229186deecc",
  "verdict": "PARTIAL",
  "scope": "Read-only semantic review limited to the stated R04b DOCX SHA. Read the request, full packet, complete worker Markdown, extracted Word text, 157-row register, official requirement extract, and current unique Blueprint row. Parsed the DOCX package text without Word COM or Computer Use. No artifact was edited.",
  "checks": [
    {
      "id": "target_and_packet_binding",
      "result": "PASS",
      "locator": "REVIEW_REQUEST_R04b.md; REVIEW_PACKET_R04b.md §§3, 970–1326; candidate DOCX",
      "reason": "Request, packet, source Markdown, extracted-text file, register, PDF, and current Blueprint file hashes match their stated values. Packet body matches the worker Markdown; packet extraction matches the standalone extraction. Reconstructed DOCX text and all 12 tables match the extracted text. Candidate SHA before and after review is identical."
    },
    {
      "id": "official_requirement",
      "result": "PASS",
      "locator": "Official PDF printed p.1, indicator 2; OFFICIAL_REQUIREMENT_EXTRACT_R04.txt",
      "reason": "The official PDF hash matches 805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709. The exact requirement is present in the bound extract and in the PDF page-1 table text; the extracted cell wraps after 「訂」."
    },
    {
      "id": "unique_blueprint_identity_and_scope",
      "result": "PARTIAL",
      "locator": "BLUEPRINT_CURRENT.jsonl line 10, row 0010/I02-E01; row fields required_fields_or_questions and required_calculations_or_analysis; candidate §1 paragraph 2",
      "reason": "Current Blueprint file and unique row hashes match; the row copy matches the current row. The row also calls for outward-policy/public-disclosure fields and a policy-review completion calculation whose scope is unresolved against the exact learner-assessment requirement. The candidate correctly preserves F-05 as PARTIAL/UNKNOWN."
    },
    {
      "id": "title_blind_and_negative_neighbors",
      "result": "PASS",
      "locator": "§1 paragraph 1; §§14; negative neighbors 0009/I01-E06 and 0011/I02-E02",
      "reason": "Even without the document title, the learning objectives, question allocation, performance rubric, learner-level scoring, and retest mechanics identify this as learner-outcome assessment. The body distinguishes both neighboring requirements."
    },
    {
      "id": "question_allocation_and_key",
      "result": "PASS",
      "locator": "§3 allocation table; §4 Q1–Q20 table and answer-key line",
      "reason": "LO allocation is 10/4/3/3, totaling 20. All 20 questions have four options, and the stated key matches the best response for each item."
    },
    {
      "id": "rubric_weights_and_score_math",
      "result": "PASS",
      "locator": "§5 weight statement; §6 0–4 rubric; §§7–8 first-attempt cases; §§11–12 retests and summaries",
      "reason": "Weights total 100 (knowledge 20, P 40, C 25, M 15). Recalculated first-attempt totals are 84.75, 70.50, 69.50, and 74.75; retest totals are 82.00 and 80.25. Answer counts, EV rating vectors, four thresholds, rates, and displayed means reconcile."
    },
    {
      "id": "rubric_administration_consistency",
      "result": "FAIL",
      "locator": "§5 paragraph before the CASE-SYN-17 control card; §6 rubric level-2 anchors; §9 EV-SYN-002-C3-F, EV-SYN-002-M2-F, EV-SYN-003-P1-F through P4-F, EV-SYN-004-P3-F; §11 EV-SYN-003-P2-R1",
      "reason": "§5 says the assessor reads only the card and does not prompt. The rubric’s level-2 anchors depend on prompting, and the cited sample observations are explicitly scored as prompt-dependent. Under the stated procedure, those behaviors cannot be elicited or consistently rated."
    },
    {
      "id": "retest_provenance_and_register_locators",
      "result": "PARTIAL",
      "locator": "§2 feedback/retest workflow row; §4 single Q1–Q20 form and key; §11 RET-SYN-003/004 answer rows and retest EV rows; §15 ANS-SYN-003-RETEST and ANS-SYN-004-RETEST, field 精確欄位定位",
      "reason": "The §2 workflow calls for a new question version, but §11 retest vectors use the same Q1–Q20 set and §4 key; the register says to recalculate with the same-version key. §11’s new performance scenario is not bound to a named case/version or control card. Both retest answer-vector register locators incorrectly point to §8 rather than §11. The displayed arithmetic itself is correct."
    },
    {
      "id": "register_reconciliation",
      "result": "PARTIAL",
      "locator": "§15 embedded register; SYNTHETIC_REGISTER_R04.md; packet §§1327–1496; rows ANS-SYN-003-RETEST and ANS-SYN-004-RETEST",
      "reason": "All 157 entries are unique, have six populated fields, and match in order across the Markdown body, sidecar, and packet. The R03 broken register-table syntax is repaired. The two retest-vector locators cited above remain wrong; RET-003/RET-004 calculation locators are now specific."
    },
    {
      "id": "small_volunteer_association_usability",
      "result": "PARTIAL",
      "locator": "§13 role separation, backup, external-review, and HOLD rules",
      "reason": "The design permits two distinct case roles and combines only non-scoring administration; it requires qualified authorized backup or conditionally authorized external review and holds cases without independent coverage. Actual roster, qualifications, availability, and scheduling capacity are not evidenced."
    },
    {
      "id": "sample_real_boundary",
      "result": "PASS",
      "locator": "Status statement; §§5, 9–11, 13–15",
      "reason": "Examples and role codes are identified as SAMPLE/SYNTHETIC; the candidate does not assert real learners, execution, authorization, approval, adoption, or results. Replacement controls are stated."
    }
  ],
  "findings": [
    {
      "id": "SEM-01",
      "severity": "major",
      "locator": "§5 no-prompt instruction; §6 level-2 anchors (P1–P4, C1–C5, M1–M3); §9 cited EV rows; §11 EV-SYN-003-P2-R1",
      "evidence": "The procedure forbids assessor prompts, while the rubric and worked observations use prompted response levels. This makes those anchors and corresponding sample ratings non-reproducible under the defined administration.",
      "required_repair": "Either define standardized, bounded prompts and apply them consistently in the case procedure and records, or remove prompt-dependent anchors and rescore affected sample cases against observable unprompted behavior."
    },
    {
      "id": "SEM-02",
      "severity": "moderate",
      "locator": "§2 feedback/retest row; §4 question set/key; §11 RET-SYN-003/004 and retest EV table; §15 ANS-SYN-003-RETEST and ANS-SYN-004-RETEST, 精確欄位定位",
      "evidence": "The stated new-question-version workflow is not demonstrated by the retest vectors, which use the single §4 item set/key. Retest performance observations lack a named controlled scenario/version. The two answer-vector register locators point to §8, although the vectors are in §11.",
      "required_repair": "Bind each retest to a specified test form/version and key, or explicitly define and limit same-form reuse; identify the retest scenario/version and its controls; correct both register locators to §11 and reconcile any changed results."
    },
    {
      "id": "SEM-03",
      "severity": "moderate",
      "locator": "Current Blueprint row 0010/I02-E01 fields required_fields_or_questions and required_calculations_or_analysis; candidate §1 paragraph 2",
      "evidence": "The Blueprint’s outward-policy/public-disclosure and policy-review fields remain unresolved against the official learner-assessment requirement. The candidate accurately labels this conflict PARTIAL/UNKNOWN.",
      "required_repair": "Keep this scope unresolved and marked PARTIAL/UNKNOWN until an authoritative scope decision is available; do not infer or add unsupported policy claims."
    },
    {
      "id": "SEM-04",
      "severity": "moderate",
      "locator": "§13 final sentence on unknown roster/qualifications and preceding backup/coverage rules",
      "evidence": "The operating safeguards are clear, but the document supplies no actual qualified roster or schedule/availability example, so feasibility for a particular small association cannot be established.",
      "required_repair": "Before real adoption, verify authorized role coverage and availability; retain HOLD where independent coverage is unavailable."
    }
  ],
  "limitations": [
    "The local official PDF hash matched. Its extracted table text is interleaved by columns; no visual page review was performed.",
    "No actual learner, roster, authorization, assessment, or association approval evidence was supplied; all examples remain SAMPLE/SYNTHETIC.",
    "The recorded OpenCode route status is pending for R04b. The predecessor R04 attempt received provider HTTP 429 with retry-after 2026-10-30T00:34:47.523612Z, still future at this review time. OpenCode and Antigravity were not called.",
    "No visual/layout review or formal acceptance was performed or claimed."
  ],
  "does_not_claim": [
    "REAL evidence",
    "formal acceptance",
    "visual or layout review",
    "resolved Blueprint scope",
    "OpenCode or Antigravity review response"
  ]
}
```

