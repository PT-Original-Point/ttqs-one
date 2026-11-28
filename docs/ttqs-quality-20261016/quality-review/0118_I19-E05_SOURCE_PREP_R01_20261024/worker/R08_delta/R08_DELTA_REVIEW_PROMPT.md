# Independent exact-SHA delta review — 0118 / I19-E05

You are an independent reviewer, not the Builder. Read the attached packet. Review only whether the narrowly described R07→R08 pagination-only change alters semantic content, creates a semantic ambiguity, or makes the target record materially less usable. The candidate is the exact R08 SHA stated in the packet. Do not infer full-document semantic review from this delta task. Do not claim to inspect pixels or DOCX binaries; those checks are explicitly outside your scope.

The existing R07 independent reviewer response is PASS and was adjudicated PASS for R07 semantic scope only after checking its exact SHA, all checklist items, zero findings, and execution provenance. Its previous receipt wrapper had been pending coordinator adjudication; that discrepancy is now separately recorded. R08 must receive its own delta result.

Return one compact JSON object only with keys: doc_id, requirement_id, candidate_sha256, review_scope, verdict (PASS/PARTIAL/FAIL), findings (array), rationale, limitations, formal_acceptance (must be NOT_GRANTED). PASS means only that this specific layout-only delta has no adverse semantic/operational effect and the R07 semantic finding remains applicable to unchanged text. If the supplied evidence is insufficient, use PARTIAL. Do not edit files or request tools.
