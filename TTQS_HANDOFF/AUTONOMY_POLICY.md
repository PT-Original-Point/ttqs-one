# Autonomy policy

Default loop:
BUILD -> STATIC HARD GATES -> FRESH SEMANTIC REVIEW -> PUBLISH PASSING DOCS TO CURRENT -> DELTA CHECKPOINT -> CONTINUE.

Human is not workflow heartbeat.
Every 10 docs may emit a concise NON-BLOCKING status. Continue automatically if gates pass.

## Throughput / anti-churn policy
- One scheduling turn gives each lane at most one build-or-repair attempt. If it does not pass, move that lane to the back of the READY queue; do not retry the same lane immediately while other READY work exists.
- Builder responsibility ends when a stable DOCX + build receipt are written. Builder MUST NOT run duplicate PowerShell/Word/LibreOffice/CUA/PDF self-check pipelines that are already owned by the static gate or reviewer.
- If a builder exits non-zero but leaves a stable new DOCX + valid receipt, salvage that exact candidate: run static gate + fresh review before deciding to rebuild. Never discard a completed candidate merely because builder cleanup/self-check failed.
- Static gate owns deterministic checks: DOCX/OOXML integrity, placeholders, font floors, required markers, arithmetic/source consistency that is machine-checkable, candidate/receipt SHA binding.
- Fresh reviewer owns semantic/usability checks only: exact requirement fit, genre mechanics, title-blind identification, negative-neighbor rejection, middle-school first-glance readability, evaluator-facing professionalism, SAMPLE/REAL truth boundary. Reviewer MUST NOT launch Word COM, CUA, PDF/PNG rendering, or nested Codex probes unless an exact layout anomaly has already been identified.
- Allow at most two active execution units on this home PC: one BUILD lane and one REVIEW lane for a different document. All shared writes (central synthetic register, queue promotion, CURRENT publish, checkpoint) are serialized under one promotion lock.
- Cache authoritative source readback per deliverable by exact source SHA + Blueprint row hash. Reuse only when both hashes are unchanged; do not repeatedly re-read Drive/PDF sources without an evidence delta.
- A timed-out/crashed build or review is TRANSIENT for that exact lane. Return it to queue tail and continue other READY lanes.
- Do not rescan/re-hash the full 142 corpus after every document. Use delta-only verification except at explicit final QA.
- No full-corpus PDF/PNG rendering. Render only an exact document/page when a concrete layout anomaly is detected.
- After two consecutive Canary documents PASS under the same builder/static/reviewer contract, freeze that acceptance contract for the remaining Canary/production run. A later control change may invalidate prior PASS only when tied to a concrete source defect or exact artifact defect with body locators; policy drift alone is not enough.

## Non-blocking failure policy
- A single document failure parks only that document lane.
- A single canary failure parks only that canary lane; continue all other READY canaries.
- Passing canaries are published to CURRENT immediately so Human may inspect them without blocking execution.
- Two failed repair epochs on the same logical defect trigger CHURN_FUSE on that exact lane: stop blind rebuild, perform root-cause audit, fix the builder/reviewer/validator contract or source interpretation, then retry only after a material delta.
- CHURN_FUSE is NOT a Human Gate and NOT a Project blocker.
- Full production rollout still requires the required representative Canary set to pass, but the system must autonomously repair parked canaries while continuing every other legal READY lane.

## Escalate to Human only when
1. Mission/spec or major quality policy must change and the answer cannot be derived from current authority;
2. SAMPLE vs REAL / third-party authority is genuinely ambiguous;
3. legal/signature/identity/OAuth/MFA is required;
4. a missing third-party original or real-world fact materially changes the required deliverable and cannot be obtained automatically;
5. bounded readback/root-cause reconciliation leaves external side effect or authority ambiguity unresolved;
6. final evaluation package needs Human acceptance.

Do NOT escalate merely because:
- one document fails;
- one canary fails;
- two repair attempts fail;
- a local script/validator/parser is defective;
- a reviewer issue can be resolved from official sources.

## Automatic defect handling
- single defect -> rebuild exact doc from source;
- same requirement inconsistency -> rebuild requirement slice;
- same-family anti-pattern -> family impact scan/rebuild;
- cross-family template/old-policy pollution -> taint affected quality epoch;
- forged third-party or SAMPLE represented as REAL -> quarantine affected epoch immediately;
- repeated same defect with no material delta -> park exact lane, root-cause audit, repair contract, continue other READY lanes.

Human may randomly inspect CURRENT anytime. A Human finding outranks automated PASS, but Human is never required to keep the queue moving.

## Anti-garbage rule for efficiency work
Efficiency changes are invalid if they reduce semantic review coverage. No fast path may skip fresh review, reuse peer document bodies as templates, or promote on technical validity alone. Every promotion still requires requirement-specific genre mechanics, title-blind identification, negative-neighbor rejection, substantive-duplication screening, evaluator-facing readability, and SAMPLE/REAL truth-boundary PASS. Caching may reuse source readback, calculations, and shared fact IDs only; not generated prose or document bodies.

## HOTFIX5 delete-first dual-agent pipeline
The stable acceptance path is BUILD -> STATIC/LAYOUT/RECEIPT -> OpenCode exact-SHA independent semantic review -> promotion. Remove duplicate mandatory Codex semantic acceptance from the critical path. Codex may diagnose repairs but cannot self-accept content.
Defect classes are CONTENT_DEFECT, LAYOUT_DEFECT, CONTROL_PLANE_DEFECT, REVIEW_INFRA_DEFECT, TRANSIENT_EXECUTION_DEFECT. Only the first two may mutate DOCX.
NO_CONTENT_OR_LAYOUT_CHANGE => DOCX_SHA_MUST_NOT_CHANGE.
WAITING_OPENCODE_REVIEW != CONTENT_FAIL.
Control/review infrastructure defects repair only their own lane/control surface, never document bytes.

## Deadline dual-worker execution
When HOTFIX5 liveness/evidence bootstrap has passed, two model workers may be active: one Codex task and one OpenCode task. Each worker prioritizes cross-review of the other worker's ready candidate, then exact repair of its own rejected candidate, then new build. Do not concurrently build deliverables with overlapping shared_fact_groups. Shared writes/promotion remain serialized by Codex. This changes throughput only; all semantic/anti-garbage gates remain unchanged.


## Deadline execution override — 2026-10-04
Until the 2026-10-05 evaluation handoff:
- Canary status is lane/family scoped, not a global production gate. Unrelated READY production continues.
- OpenCode remains pinned exclusively to Muse Spark 1.3 Free. If Muse is unavailable due provider 429/backpressure, use a fresh isolated Codex semantic reviewer for the exact candidate rather than blocking all production. Do not use another OpenCode model.
- New control/review metadata requirements are not retroactive artifact defects. Do not demote unchanged prior CURRENT solely because an older PASS lacks newly introduced model-attestation fields.
- Freeze control-plane architecture; patch it only for a concrete all-production blocker.
- Two identical transient attempts without material delta park the lane to queue tail; do not immediately start a third identical attempt.


## Human executor migration — 2026-10-04
OpenCode / Muse is explicitly deprecated for TTQS_ONE active execution. Do not dispatch new BUILD/REVIEW/REPAIR/quota-probe work to OpenCode. Preserve historical evidence only.

Active workers are now:
- Codex: canonical dispatcher, shared-state owner, deterministic integration, independent review of Antigravity artifacts, promotion.
- Antigravity on the WIN10 host using Gemini 3.8 Flash High: preferred long-running content builder, exact content repair worker, and independent semantic reviewer of Codex artifacts.

WIN10 has no MCP dependency for Antigravity. Codex must discover and use the official local Antigravity execution/session route directly from WIN10. Do not guess executable paths, ports, or model identifiers. Do not use visible GUI automation unless there is no official headless/local route and Human explicitly approves it.

Outsource as much long-running model work as practical to Antigravity. Codex should remain available for orchestration, deterministic gates, exact independent review, integration and promotion. Keep no-self-review and shared-fact collision rules unchanged.


## Antigravity 主力生產模式 — 2026-10-04
Human 明確要求將 WIN10 Antigravity / Gemini 3.8 Flash High 作為主力施工者，Codex 退出例行長時間內容生成。

執行規則：
- 起始 2 個彼此隔離的 Antigravity 內容 worker，同時 1 個 Codex 控制/獨立複核 worker。
- Antigravity 只產生 content.json 或做 exact content repair；固定 host renderer 與 deterministic gates 不占用模型 worker。
- Codex 主要做派工、shared-fact 衝突檢查、fresh independent semantic review、整合與 promotion；除 Antigravity 不可用外，不做例行長時間 BUILD。
- 各階段流水化；Antigravity 生成下一份時，host 同時 render/check 上一份，Codex 同時 review 已通過 deterministic gate 的更早一份。
- 維持 2~4 份已通過 deterministic gate 的候選緩衝。少於 2 時 Antigravity 優先 BUILD；達 4 時優先 exact repair / 下一批內容準備，避免無限堆積。
- 兩個 Antigravity worker 各成功至少 2 份且無 quota/session/shared-fact 衝突後，可自動升到 3。若 3-worker 在 30 分鐘內有效候選吞吐至少提升 20% 且錯誤率不惡化，可升到 4。最大 4。
- 若並行導致 quota、session collision、shared-state race、吞吐下降或主機資源壓力，自動降一級，不等待 Human。
- no-self-review、SAMPLE/REAL、title-blind、negative-neighbor、substantive duplication、layout 等品質門檻完全不變。


## Antigravity 額度保護修正 — 2026-10-04
Antigravity 的速度不得被解讀為無限額度。預設只允許 1 個 Antigravity 長時間模型工作。取消先前 2→3→4 自動擴張規則。

第二個 Antigravity worker 只有在同時滿足以下條件才可做有界短測：
- 官方本機介面可讀回可驗證的五小時/每週使用額度或其他等價 headroom；
- 已完成最多 3 份真實 READY 文件的單 worker 額度成本樣本；
- 樣本期間無 quota/rate-limit/session 衝突；
- 根據剩餘文件與評核期限，增加 worker 不會高機率提前耗盡可用額度。

Antigravity 額度優先花在新 content payload 與 exact content repair。固定 renderer、static/layout、SHA/receipt、queue/checkpoint、重複來源讀取與可由 Codex 短時間完成的驗收不得消耗 Antigravity 額度。

OpenCode/Muse 不再送任何新 probe。只離線分析既有 logs/session exports，能讀到多少 token/成功次數/quota 時間序列就記多少；缺失欄位必須標 UNKNOWN，不得反推或猜測官方 quota threshold。
