**VERDICT: PARTIAL**

**Candidate exact SHA-256:** `a945f7b780bb3c9ef9edbe5b416687db6d19845cf70c804f32d0fd1482562bd9` (as stated in the task; extraction text SHA `35ae9c87…fde41` per packet header; neither recomputed — no tools used, per review constraints)

---

## Review scope

Semantic review of candidate DOCX 0118 (I19-E05, 感謝函原件收存與核驗登錄表) against: official page-8 excerpt, unique Blueprint R01, crosswalk/mapping JSON, synthetic dataset CSV, and replacement register CSV. Text-only; layout unverifiable (see Limitations).

## Findings

### What is correct (verified)

| Check | Location | Result |
|---|---|---|
| Official purpose/genre — reference corroboration only, not causal proof; reusable intake/custody/verification form, not a letter template | §1.1–1.5, §2 | ✅ Matches Blueprint 核心用途 and page-8 「感謝函」 context |
| Official binding — doc 0118 / I19-E05 / crosswalk 1+0 / seed SHA / PDF SHA / page-8 text SHA / internal index 129 / printed serial UNKNOWN_NOT_ASSERTED | §1.3 table | ✅ Matches mapping_evidence_0118.json field-for-field, including exact SHAs |
| Intake fields (log code, doc/req ID, date, method, operator role, count, custody) | Table A | ✅ All Blueprint 必備欄位 present |
| Letter-content fields (issuer, title, recipient, date, subject, faithful summary, training/service, period, scope, pages, attachments) | Table B | ✅ Complete; anti-inflation summary rule attached |
| Original-type matrix (PAPER / SENDER_NATIVE / SCAN / PHOTOCOPY / SCREENSHOT / FORWARDED / REQUEST_DRAFT / NONE) | §1.5, Table C | ✅ Separately flagged as required |
| Custody chain — location, custodian, transfer, access, byte preservation, SHA with hashed-object label | Table C, §3 item 7, §6.2 | ✅ |
| Source authentication — independent channel + independence justification + NOT_RUN state | Table D, §3 item 2 | ✅ |
| Completeness/relevance/privacy checks | §3 items 3/5/6, Table E, §6.3 | ✅ |
| HOLD rules — HOLD_NO_ORIGINAL / HOLD_SOURCE_UNVERIFIED / HOLD_SCOPE_OR_PRIVACY_REVIEW; suspicious modifications not labeled fraud until confirmed | §4 matrix, §4.2 | ✅ Matches Blueprint verbatim |
| Return-for-supplement — corrective items, responsible role, deadline | §4, Table F | ✅ |
| Reject — NOT_ACCEPTED_CONFIRMED_COPY_OR_MISMATCH only on confirmed grounds with evidence | §4, §4.2 | ✅ No confirmed-mismatch example fabricated |
| Human-review gateway — all four checks + second reviewer; ELIGIBLE ≠ formal acceptance | §3, §4, §4.1, §8.5 | ✅ Stated consistently (matrix, §1.4, §5.2 step 8, closing note) |
| SAMPLE/REAL — single demo row SYN-0118-001, all NOT_PROVIDED/NOT_RUN/NONE, HOLD_NO_ORIGINAL, no letter/name/date/signature/decision | §5.1–5.3 | ✅ Verbatim match to SYNTHETIC_DATASET_0118_R01.csv, incl. `author=NOT_PROVIDED` and `display_boundary=SYNTHETIC_NOT_EVIDENCE` |
| Replacement register — all 11 field_paths match register CSV values and instructions, RESTRICTED_ASSOCIATION_REPOSITORY throughout | §5.4 | ✅ |
| Neighbor distinctions — 0092/I17D-E06, 0096/I18-E03, 0103/I18-E10, 0116/I19-E03, 0117/I19-E04 + intake triage | §7, §7.1 | ✅ Matches mapping JSON |
| No fake statistics/calculations | §5.2, §8.4, §8.5 | ✅ "逐步演算" is a decision walkthrough, no arithmetic; no invented metrics anywhere |
| Usability as a form — fill-in tables A–F, checkbox states (完成/未完成/N/A), status codes, restricted-field markers | §2–§4 | ✅ Operable, not generic prose |

### Defects

1. **[MAJOR] Retention (保存期限) check missing entirely.** Blueprint 必備章節 #4 requires “來源真實性、完整性、關聯性、隱私**及保存期限**核驗". The candidate covers privacy/use-authorization (§6.3, Table E, §3 item 6) but contains no retention-period, storage-duration, or disposition/periodic-review rule anywhere (checked §2 Table E, §3 checklist, §6.2–6.4, §8.2 — all absent). Checklist has 9 items exactly mirroring the Blueprint's 9-item list, which itself omits retention — so the omission is traceable to the checklist source, but the chapter-level Blueprint mandate is unmet.
2. **[MINOR-MODERATE] Broken cross-references.** §2 rule after Table A: “第 2 表與第 3 表相關欄位維持 NOT_APPLICABLE" — §2's tables are labeled A–F, not numbered; §5.2 step 7: "第 2 表第 1 項即未通過" — the receipt item is §3 checklist item 1, not "表 2". Neither reference resolves to an actual labeled object.
3. **[MINOR] Trigger overlap without tie-break.** "缺頁附件" is a trigger for HOLD_SCOPE_OR_PRIVACY_REVIEW (§4 matrix row 4) and 缺頁/缺附件 triggers RETURN_FOR_SUPPLEMENT (§4.2 RETURN), while §4.2 HOLD says "HOLD 或 RETURN_FOR_SUPPLEMENT". The Blueprint permits "HOLD 或 RETURN", but within a single matrix one trigger should resolve to one default status or state the choosing rule.
4. **[MINOR] Garbled privacy sentence.** §6.4: “公開層不得出現機構名、人名、聯絡方式、地址、發函日以外可識別組合” — ambiguous parse; as written it could be misread to permit disclosure of 發函日， which conflicts with the faithful-summary and de-identification intent (and Table B records 發函日 without a [受限] marker).
5. **[MINOR] Typo.** §1.1 角色聲明： “候選作職責描述” → should be “候選作業職責描述” (source packet: “候選作業職責").
6. **[INFO] §1 heading** is “證據效力及邊界”， omitting the Blueprint's explicit "SAMPLE/REAL" label; substance is present but only in §5/§8, not §1.

## Minimum repair

1. Add a retention element: a 保存期限／屆期處理 field in Table E (or one new checklist item) plus one rule line in §6 covering retention duration and disposition before any release or archive decision.
2. Fix the two cross-references (§2 rule; §5.2 step 7) to actual labels (表 A–F / §3 checklist item numbers).
3. Correct the 候選作業 typo; rewrite the §6.4 sentence unambiguously.
4. (Optional but recommended) Add a one-line tie-break: 缺頁附件 defaults to RETURN_FOR_SUPPLEMENT when the missing part can be supplied, HOLD_SCOPE when unreadable/unresolved.
5. Items 1–4 do not require rerunning binding or dataset work; rows in §5.1/§5.4 are untouched.

## Limitations

- **Visual inspection was not performed.** Review is based solely on the exact text extraction; table borders, page layout, checkbox rendering, font/shading of [受限] markers, and the stray `[TABLE]` wrapper around the §1.1 角色聲明 paragraph could not be checked. These are extraction artifacts and may be layout blocks, but layout compliance is unverified.
- SHA-256 values are quoted from the packet and were not independently recomputed (no shell/read/search tools used).
- The official source was examined only via the page-8 excerpt and its stated text-extraction SHA; the full PDF was not accessed.

**No claim of formal acceptance is made.** The candidate itself records `real_original_supplied: false`, `formal_acceptance: NOT_GRANTED`, and its §8.3 QA items (Word QA, per-page visual check, independent exact-SHA semantic review) remain unchecked — this review addresses only the semantic-review gate and does not discharge the other two.
