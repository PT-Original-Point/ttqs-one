# TTQS ONE — DOCX 0140 R06 candidate

**State:** CANDIDATE only; not formally accepted. **REAL data:** UNKNOWN/HOLD. **Human acceptance:** NOT_GRANTED.

## Identity and official scope

- DOCX: 0140 — 訓練資訊系統使用普及率盤點與分析表
- Official requirement: I19-E30; 157-item index 154; printed checkbox serial UNKNOWN.
- WDA training-institution evidence table, page 9: 「運用資訊系統普及率。」 This is an example evidence item, not a score or proof of association achievement.
- R06 DOCX SHA-256: `3eecd34369de6768ede430f2bd1c4343d3c20c25e4d28e06d1ca6733f3470144` (125,511 bytes).

## R06 candidate and quality evidence

- Word-native PDF: 29 pages; SHA-256 `821ee673e936c9b392351dbbae9728cda8fee0b1a12cf2ab3f713973f60496d4`. All 29 rendered page PNGs were opened and visually inspected locally. The complete PDF is included for audit.
- Structural/static checks: valid DOCX ZIP; 18 tables / 273 rows; body text minimum 10.5 pt; table text minimum 9.5 pt. The 80 unique synthetic user-year IDs in the DOCX match 80 dataset rows and 80 replacement-register rows. All annual/role totals and rates were recomputed.
- Visual status: PASS for pages 1–29, Codex visual inspection. This is not an independent semantic verdict.
- Independent semantic review: BLOCKED. OpenCode v2 free attempts with `opencode/beam-free` and `opencode/glm-5.3-flash-free` each returned provider HTTP 429 `Free usage limit reached`; no review response was produced, actual model completion and token usage UNKNOWN. The target SHA remains unchanged.

## Build history and bounded repairs

The initial candidate exposed small-table-font, orphaned-header and clipped first-column issues. R04 raised body/table typography to the required 10.5/9.5 pt floor. R05 repaired the section/header flow. R06 widened the first column in five-column tables. No further visual defect was found in the full 29-page inspection, so R06 bytes are retained.

The manuscript began with an Antigravity CLI plain-text writer request for `gemini-3.8-flash-high`; the CLI did not emit model identity, so actual model is UNKNOWN. Its raw response, dispatch record, deterministic repair script, repaired manuscript and repair receipt are included. Unsupported association/system assertions were removed; the complete quantitative appendix is generated from the canonical synthetic CSV, not copied from model prose.

## SAMPLE/REAL boundary

The 2023–2025 case is fully synthetic: 80 unique user-year records, 62 active users, 52 complete users. Annual adoption rates are 60.00%, 78.57% and 87.50%; eligible completion is 45.00%, 64.29% and 78.13%; active-user completion is 75.00%, 81.82% and 89.29%. No live system, roster, activity logs, association approval, official score or actual performance claim is represented. Real substitution requires authorized source records and protected identity matching.

## Contents

See `MANIFEST_R06.json` for the path, byte count and SHA-256 of each included artifact. The bundle includes official mapping, unique Blueprint, source packet, 80-row synthetic dataset and replacement register, writer request/raw output/repair evidence, build script, DOCX, Word-native PDF, QA receipt, and both unsuccessful independent-review attempts with original raw errors.
