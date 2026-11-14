```json
{
  "verdict": "PASS",
  "candidate_sha256": "cae8be8280456b51a1294ee90eafca0ac1ae8a12738289d6ebbca35b3a05a3da",
  "review_packet_sha256": "120ebf90abc83e931c5a34f505142d706d0c0ae6c11dcc98989302981878c9f9",
  "binding": {
    "doc_id": "0135",
    "official_requirement": "I19-E25",
    "official_157_item_index": "140",
    "official_checkbox_serial": "UNKNOWN"
  },
  "scope": "Independent semantic and usability review of DOCX candidate 0135 against official requirement I19-E25 (Indicator 19), project item 140, and unique blueprint R01. Read-only review without file editing, external tools, visual claims, or assertion of formal institutional acceptance.",
  "checks": {
    "requirement_and_unique_blueprint_fit": {
      "status": "PASS",
      "details": "Candidate covers all 14 mandatory sections and 12 structured tables required by UNIQUE_BLUEPRINT_0135_I19-E25_R01.md. Accurately addresses both target-market reach and customer value without confounding them.",
      "evidence_locators": ["Header", "Sections 1–14", "Tables 1–12"]
    },
    "genre_and_neighbor_distinction": {
      "status": "PASS",
      "details": "Conforms strictly to the quantified market-and-customer-value outcome analysis report genre. Explicitly differentiates from neighbor item 141 (individual performance), item 142 (operational performance), 0133/I19-E22 (course sessions/person-times), and 0134/I19-E23 (member counts/dues revenue).",
      "evidence_locators": ["Section 1", "Section 2", "Section 9", "Table 2", "Table 9"]
    },
    "usability_and_methodology": {
      "status": "PASS",
      "details": "Contextualized realistically for a small volunteer non-profit association (monthly service-record administrative burden). Provides operational definitions, inclusion/exclusion/deduplication rules, a paired pre/post 90-day measurement design, and a complete 7-item tracking survey tool.",
      "evidence_locators": ["Section 3", "Section 5", "Section 8", "Section 10", "Table 3", "Table 5", "Table 8", "Table 10"]
    },
    "arithmetic_and_data_consistency": {
      "status": "PASS",
      "details": "All calculations are verified exact: (1) Market reach rates 20/80=25.0%, 24/80=30.0%, 28/80=35.0% (+5.0 pp/yr, relative +20.0% and +16.7%, cumulative +10.0 pp / +40.0%); (2) Matched pairs (n=15) median baseline=120 min, follow-up=90 min (-30 min, -25.0%); (3) On-time rate 8/15 (53.3%) to 12/15 (80.0%) (+26.7 pp); (4) Response rate 15/28 (53.6%) with nonresponse 13/28 (46.4%) explicitly preserved and reported. Synthetic Case IDs SYN-0135-VALUE-2025-01 through 15 match the CSV source row-for-row.",
      "evidence_locators": ["Section 4", "Section 6", "Section 7", "Table 4", "Table 6", "Table 7"]
    },
    "sample_real_boundary_and_causality": {
      "status": "PASS",
      "details": "Clear labeling of all metrics and case rows as SAMPLE/SYNTHETIC throughout. Strictly refrains from claiming association performance, real member endorsements, or self-awarded TTQS level 3/4. Explicitly acknowledges lack of a control group, nonresponse bias (13 unreturned), and external confounding variables.",
      "evidence_locators": ["Header", "Section 1", "Section 5.1", "Section 7", "Section 11", "Table 1", "Table 6", "Table 7", "Table 11"]
    },
    "evaluator_and_admin_readiness": {
      "status": "PASS",
      "details": "Includes a comprehensive REAL data replacement register (Table 11) specifying acceptable primary artifacts, storage owners, privacy masking rules, and release gates. Table 12 provides a clear 7-point evaluator verification checklist.",
      "evidence_locators": ["Section 11", "Section 12", "Table 11", "Table 12"]
    },
    "hold_reject_gates": {
      "status": "PASS",
      "details": "Establishes concrete, actionable HOLD triggers (e.g. unstable frame without reconciliation, hidden nonresponse, differing pre/post definitions) and REJECT conditions (e.g. presenting synthetic data as real, unsubstantiated causal claims, relying solely on subjective satisfaction).",
      "evidence_locators": ["Section 13", "Table 8"]
    },
    "exact_sha_binding": {
      "status": "PASS",
      "details": "Binds exactly to candidate SHA-256 cae8be8280456b51a1294ee90eafca0ac1ae8a12738289d6ebbca35b3a05a3da and packet SHA-256 120ebf90abc83e931c5a34f505142d706d0c0ae6c11dcc98989302981878c9f9.",
      "evidence_locators": ["Header", "Section 14"]
    }
  },
  "findings": [
    {
      "severity": "INFO",
      "category": "Official Checkbox Serial Identification",
      "finding": "Official printed checkbox serial is recorded as UNKNOWN in candidate metadata, preserving strict fidelity to source constraints.",
      "minimal_fix": "Maintain UNKNOWN until the physical official TTQS assessment checklist with printed checkbox numbers is inspected."
    }
  ],
  "inheritance_limits": [
    "SAMPLE/SYNTHETIC data cannot be inherited or transferred as real organizational track record or verified market size.",
    "Data and case IDs cannot be co-mingled or merged with 0133/I19-E22 (sessions/person-times) or 0134/I19-E23 (member counts/dues).",
    "Self-awarded TTQS score levels (Levels 1–4) must not be inherited; formal scoring remains strictly within evaluator jurisdiction."
  ],
  "unknowns": [
    "official_printed_checkbox_serial",
    "real_association_target_market_eligible_frame",
    "real_association_served_organizations_registry",
    "real_pre_and_post_training_operational_questionnaires_and_timestamps",
    "real_accountable_decision_makers_and_action_approval_dates"
  ]
}
```