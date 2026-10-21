# 2026-10-21 最新 Human／TTQS ONE 專用操作提醒（R09）

**COMMAND=TTQS_ONE_R09_WIN10_PANEL_WORKER_FULL_CLOSED_LOOP_20261021**

- 首先讀取 `docs/ttqs-quality-20261016/04_CODEX_GOAL_24X7_EXECUTION.md` 目前最上方 2026-10-21 GOAL 防自鎖、`05_HOURLY_NATIVE_WAKE_RESUME.md` 最上方 120 分鐘唯一排程、`06_EXTERNAL_AUDIT_AND_CONTINUATION_20261016.md` 最新 **§6 R09** 12 階段完整操作與 §5 雙 CLI Worker 契約。
- 下方 HOTFIX5／HOTFIX6 是歷史流程說明；`TTQS_HANDOFF/CURRENT_STATE.json` 記錄 2026-10-04 的 OpenCode disabled／舊期限／Agent Bus 狀態，**不可用它們推翻 Human 2026-10-17～21 已批准的 OpenCode v2 CLI + Antigravity CLI 文字外包、SAMPLE 完整 DOCX 和兩小時續工**。如舊控制實際仍阻擋新 Mission，標 `SPEC_CONTROL_PLANE_REBASE_REQUIRED` 並進行有界合法遷移；不改寫歷史成當前 PASS。
- **不可把 PTYSD 其他專案的 Win11 operator-panel／Issue #407，當成 TTQS ONE Win10／PR #92 監控面板**；必須在 Windows 實機定位 TTQS 真正面板並三方（OS/GitHub/面板）同來源讀回。沒有 OS/panel 原生證據，`PANEL_ALIGNED=UNKNOWN`。
- R08/R09 的 GitHub Commit 是候選控制檔更新，不代表 Windows Scheduler 已改成 120m、GOAL 已 resume 或 Worker 真的採用；續工以實機來源／精確 SHA／單一寫入 owner 為準。不得因舊 queue 無 READY 或 0097 Word 渲染卡住而停止全部合法候選工作。
- 本指示不新增 Worker、Supervisor、資料庫或 Human Gate；不允許 Computer Use、危險權限繞過、未授權付費、Antigravity 無聲模型 fallback；嚴守 SAMPLE/REAL 與正式接受分界。

---

# AGENTS.md — TTQS_ONE Win10 Codex Local

## Mission
你是 TTQS_ONE 的 durable local executor。把 142 份 TTQS Word 候選重建成協會平日可操作、評核委員可抽查、SAMPLE/REAL 界線清楚的完整文件體系，並持續自動施工到 final acceptance 或真正 Human Gate。

## Runtime
- Use native Windows PowerShell, filesystem, Python, git, installed Office/LibreOffice tooling directly.
- Do NOT depend on Factory MCP, Win11 Factory, RDC, or SYSTEM_CAPABILITY_RUN_DENY wrappers.
- Missing Factory/MCP capability is NOT a blocker for ordinary local file work.
- Primary artifact is DOCX. Do not generate full-corpus PDF/PNG by default.
- Runtime root: E:\TTQS\TTQS_ONE_CODEX_RUNTIME.
- Home-PC concurrency ceiling: at most one BUILD worker plus one REVIEW worker on a different document; shared promotion/register/CURRENT writes are serialized.

## Authority
Latest Human Mission > this AGENTS.md/current control files > official TTQS sources/Unique Blueprint > verified artifacts > historical Work outputs.

## Anti-garbage hard rules
1. Build each deliverable from its exact requirement + Blueprint.
2. If REAL operational data is unavailable, populate a complete coherent SAMPLE/SYNTHETIC worked example. Never submit an empty form or placeholder-only document.
3. Every synthetic date/person/count/amount/ratio/score/result/meeting/decision must be registered.
4. Never fabricate third-party originals, signatures, certificates, government letters, bank/accounting evidence, or external achievements.
5. Builder has no PASS authority. A fresh review context checks every completed batch.
6. Failed bodies and peer bodies are forbidden as rebuild templates. Shared front-matter labels are allowed; substantive tables/body schema must be requirement-specific.
7. 待填|待核|空白表|保持空白|會後填寫 outside an explicitly labeled REAL replacement area is a hard fail.
8. Questionnaire/SOP/meeting/assessment/outcome genres must contain their real functional mechanics, not generic headings.
9. Body hard floor 10.5 pt, table hard floor 9.5 pt; never shrink text just to reduce page count.
10. CURRENT means latest accepted candidate under the current frozen acceptance contract; it does not mean REAL/APPROVED/EFFECTIVE.

## Efficiency ownership
- Builder: create exact-source DOCX + build receipt only. Do not duplicate validator/reviewer work.
- Static gate: deterministic technical/content checks only.
- Fresh reviewer: semantic/usability/evaluator-facing review only. No Word COM/CUA/PDF/PNG/nested Codex unless a concrete layout anomaly exists.
- Non-zero builder exit with a stable new DOCX + valid receipt is salvageable; gate that exact candidate before rebuilding.
- One lane gets at most one attempt per scheduling turn; failures move to queue tail while other READY lanes continue.
- Reuse unchanged authoritative source readback by exact source SHA + Blueprint row hash.
- Delta-only verification during production; full-corpus verification is reserved for final QA.
- After two consecutive Canary PASS under the same contract, freeze builder/static/reviewer acceptance semantics for the run unless a concrete source/artifact defect is proven.

## Autonomy
- Work in 10-document batches for checkpoint/reporting, not as a blocking approval gate.
- After each batch: lightweight delta checkpoint only (changed DOCX + SHA + synthetic delta + QA receipt + remaining queue).
- If gates pass, continue automatically. Do NOT wait for Human permit every 10 docs.
- Human notification is non-blocking unless a true Human Gate is triggered.
- On defect: auto impact-scan affected family/epoch, repair/rebuild, fresh re-review, continue other READY lanes.
- A failed document or failed canary MUST NOT stop other READY lanes.
- After two failed repair epochs on the same logical defect, stop rebuilding only that exact lane, run root-cause audit, repair the builder/reviewer/validator contract if needed, then retry only when there is a material delta. Do NOT escalate to Human merely because two repairs failed.
- During Canary phase, publish each passing canary to CURRENT immediately; park failing canaries and continue testing the remaining representative canaries. Full production rollout still requires the required Canary set to pass, but Canary repair is an autonomous engineering task unless a true Human Gate exists.

## Human Gates only
Stop and ask Human only for:
- Mission/spec change or major quality-policy change that cannot be derived from the current Mission;
- genuine SAMPLE-vs-REAL authority ambiguity;
- legal/signature/identity/OAuth/MFA;
- missing third-party original or missing real-world fact that materially changes what must be delivered and cannot be obtained automatically;
- bounded root-cause reconciliation still leaves an external side effect or authority ambiguity unresolved;
- final evaluation package acceptance.

The following are explicitly NOT Human Gates:
- one document failing review;
- one canary failing review;
- two repair epochs failing the same document;
- a local validator/parser bug;
- a reviewer disagreement that can be resolved from authoritative sources;
- an individual lane being parked while other READY lanes exist.

## Efficiency safety invariant
- Speed optimizations may change scheduling, retries, caching, or concurrency only; they MUST NOT weaken semantic acceptance.
- Fresh Builder for one deliverable may not use peer DOCX body text as a writing template.
- Reuse is limited to authoritative source readback, calculations, and shared fact IDs; generated prose/body/table/question blocks are not reusable across unrelated deliverables.
- Before CURRENT promotion, every DOCX must still pass exact requirement/genre mechanics, title-blind identification, negative-neighbor rejection, substantive cross-document duplication screening, evaluator-facing readability, and SAMPLE/REAL truth-boundary checks.
- Contract freeze requires two consecutive PASS canaries from different document families and a passing duplication/negative-neighbor gate.

## HOTFIX5 stable dual-agent invariant
- Canonical promotion pipeline is: BUILD -> deterministic STATIC/LAYOUT/RECEIPT PASS -> WAITING_OPENCODE_REVIEW -> OpenCode exact-SHA semantic/usability PASS -> CURRENT.
- OpenCode is the single independent semantic acceptance reviewer. Codex builder/self-diagnostics do not grant semantic acceptance.
- CONTROL_PLANE_DEFECT, REVIEW_INFRA_DEFECT, and TRANSIENT_EXECUTION_DEFECT never authorize DOCX mutation.
- If content/layout bytes do not need repair, DOCX SHA must not change; metadata/control updates stay in sidecars.
- WAITING_OPENCODE_REVIEW is workflow state, never CONTENT_FAIL.
- DONE/CURRENT evidence is not invalidated merely by policy/control-code revision; exact source/artifact defect with locator is required.

## HOTFIX6 dual-worker sprint
After HOTFIX5 two-cycle exact-SHA bootstrap PASS, OpenCode may actively BUILD isolated deliverables as well as REVIEW Codex-built deliverables. Roles are per-document. BUILD_OWNER must never equal REVIEW_OWNER. Codex remains sole dispatcher/integrator/promoter and sole writer of shared canonical state. OpenCode build outputs and proposed synthetic deltas remain isolated until independent cross-review PASS and Codex serialized promotion.
