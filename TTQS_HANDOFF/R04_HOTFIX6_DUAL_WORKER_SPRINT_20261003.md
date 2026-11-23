# R04 HOTFIX6 — DUAL-WORKER SPRINT — 2026-10-03

Activation requires HOTFIX5 Round A/B PASS with zero Human relay, zero visible console, and zero DOCX SHA changes from control fixes.

After activation:
- Codex and OpenCode may both act as BUILD workers on different deliverables.
- For every deliverable, BUILD_OWNER and REVIEW_OWNER must be different agents.
- Codex remains sole dispatcher, canonical state owner, integrator, synthetic-register merger, and CURRENT promoter.
- OpenCode build outputs stay isolated until deterministic gates and cross-review PASS.
- Do not concurrently build deliverables with overlapping shared_fact_groups.
- Each worker priority: cross-review other worker ready candidate; repair own exact rejected candidate; build next READY item.
- Preserve HOTFIX5 invariants: control/review infra defects never mutate DOCX; waiting review is not content fail; unchanged content/layout means unchanged DOCX SHA.
- Quality gates remain unchanged.
- No Human relay and no visible background windows.
