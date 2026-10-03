# R04 HOTFIX5 — STABLE DUAL-AGENT PIPELINE — 2026-10-03

This supersedes HOTFIX3/HOTFIX4 runtime behavior where they conflict, while preserving all verified artifacts, CURRENT files, queue history, checkpoints, and Human Mission.

## Root-cause correction
The previous architecture duplicated semantic acceptance inside Codex and OpenCode, allowing WAITING_EXTERNAL_REVIEW/control bugs to be misclassified as document defects. This caused self-generated SHA churn and repeated repair/audit loops.

HOTFIX5 deletes that duplication.

## Stable pipeline
Codex = only canonical builder/control owner.
OpenCode = only independent semantic/usability acceptance reviewer.

Pipeline:
BUILD -> STATIC/LAYOUT/RECEIPT PASS -> immutable exact candidate SHA -> WAITING_OPENCODE_REVIEW -> OpenCode exact-SHA verdict -> PASS promotes / FAIL repairs exact scope.

No mandatory Codex semantic acceptance gate remains between static pass and OpenCode review.

## Hard invariants
- CONTROL_PLANE_DEFECT != DOCUMENT_DEFECT.
- REVIEW_INFRA_DEFECT != DOCUMENT_DEFECT.
- WAITING_OPENCODE_REVIEW != CONTENT_FAIL.
- NO_CONTENT_OR_LAYOUT_CHANGE => DOCX_SHA_MUST_NOT_CHANGE.
- Control metadata changes never resave DOCX.
- DONE/CURRENT artifacts are not reopened merely because policy/runtime/control code changed; only concrete source/artifact defect with exact locator invalidates covered evidence.
- self-generated SHA changes never reset churn counters.
- repeated same logical repair >=2 without exogenous material delta trips CHURN_FUSE; repair control/root cause only and continue other READY lanes.
- one BUILD + one OpenCode REVIEW max; shared writes serialized.
- no visible console/focus stealing.
- no full-corpus PDF/PNG.

## Two-cycle bootstrap acceptance
Before normal production resumes:
1. pause future supervisor triggers;
2. freeze DOCX mutation;
3. patch/reconcile control plane;
4. use two already-stable candidates from different families without changing their bytes;
5. prove exact-SHA request -> headless OpenCode -> exact-SHA verdict -> Codex consume;
6. zero Human relay, zero visible windows, zero duplicate requests, zero DOCX SHA changes caused by control work;
7. then re-enable hidden supervisor and normal queue.

## Quality
The review contract is TTQS_HANDOFF/DUAL_AGENT_REVIEW_CONTRACT_R01.md and is mandatory for OpenCode.
