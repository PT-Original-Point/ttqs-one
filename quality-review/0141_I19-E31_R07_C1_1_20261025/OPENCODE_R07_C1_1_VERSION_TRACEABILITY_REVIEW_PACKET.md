# TTQS ONE 0141 / I19-E31 — exact-SHA scope review

Review scope: resolve only prior finding R07-C1-m01 (current candidate version fields were inconsistent). Do not review or inherit formal acceptance. The prior exact-SHA semantic review of parent candidate 0922f737c19598b4448b60f25a6c39391bb444a1dde2536f8eef4e83cf44673a returned PARTIAL with no major findings; checks C01–C11 were PASS, and C12 was PARTIAL only for the three reader-visible version fields. Parent raw review SHA-256: 045e7f75e6bc8c405a4754abfc2305c4bc998d710a899827b07978a3d95b8e81.

Current exact candidate DOCX SHA-256: 8e0252ac4ba18edbd364e29c7f143744e801b062b3c2cd8d69f5c4a83aee7c2c
Current extracted-text SHA-256: ea52796e8609a38732f8b960eb81464813b4c88181da403b66d425dc77cd4815
Current manuscript SHA-256: 169e074c99954abebe16f72892adc557ed11c6152ca5648424daea3c2126dc83
Current 44-row replacement register SHA-256: 55f932a8b1dbc27bba002ad076aad6e4c51f47a2166bf09f2736f8dc70cefc37
Deterministic parent-to-candidate text-diff receipt SHA-256: 04e9110a3868e45d2593a3d75391dfd4c899eac34168f9960d0972f4398efc4e

The deterministic diff reports one changed paragraph and two table operations only:
1. The cover/version-boundary paragraph now identifies R07-C1.1 as a document-control subrevision and enumerates the four prior C1 repairs.
2. The basic-information version cell now says “正文修訂 R07-C1.1（R07-C1 之版控一致性子修訂）”.
3. One latest revision-history row was inserted for R07-C1.1-SYN, describing only version-field consistency. Existing R07-C1-SYN history is retained. No questionnaire, 36 response rows, formulas, official mapping, or substantive body changed.

The exact affected prose is:
「版本界線：本候選識別碼為 R07-C1.1（R07-C1 之版控一致性子修訂）。R07-C1 已完成四項 minor 內容修復：將 ASCII 來源缺口註記連結至抱怨條件、將替換流程統一為五步、明列 Q2 Top-2 嚴格 >75.00% 門檻、撤除舊版分析下限。本次 C1.1 僅修正基本資料版次欄與本段識別碼，使其與修訂歷史一致；未改 R01 問卷、36 筆合成分數、官方需求對應或 C1 實質正文。C1.1 仍待本版 exact-SHA 驗收，不構成正式接受。」

Assess whether all current version identifiers agree across the cover, basic-information table, and latest revision-history row; whether the current candidate is unambiguously R07-C1.1 and the prior four C1 repair scopes are explicit; and whether the wording makes no false claim about REAL data or Human acceptance. Verify the bounded diff receipt’s stated exact candidate SHA. Do not claim visual/layout review; it is pending separately. Do not infer actual model identity from requested model or catalog listing.

Return exactly one JSON object with schema ttqs-one-0141-r07-c1-1-version-delta-review-v1, doc_id 0141, requirement_id I19-E31, candidate_docx_sha256, extracted_text_sha256, verdict PASS/PARTIAL/FAIL, findings with exact locators, reviewer_scope SEMANTIC_VERSION_DELTA_ONLY, actual_model_identity (or UNKNOWN), limitations including that visuals are not reviewed, formal_acceptance NOT_GRANTED, real_data_status UNKNOWN/HOLD, official_score NOT_ASSIGNED. PASS only if the version-control mismatch is resolved; do not upgrade other semantic or visual scope.