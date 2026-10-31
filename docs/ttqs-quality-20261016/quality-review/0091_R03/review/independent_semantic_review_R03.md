**Verdict: PARTIAL** — semantic/content review only.  
**Exact candidate SHA:** `8c9b8f7ec6fa37f9ad833fa5df406ef2c9d120e675eea28cc3d3b15e5b9c4ac3`  
**Layout/visual status: UNKNOWN** — text extraction only; no page-layout inference.

### 1. Criterion-level findings

- **Exact requirement fit — PASS.** §1 and §2.1 correctly identify I17D-E05, official checkbox serial 098, text “學員就業證明。”, PDF page 6, and distinguish 098 from DOCX 0098.
- **Correct genre / non-imitation — PASS.** Title, §2.3, and §6.2’s “此為協會發出之請求格式，非雇主回覆” establish an association-side manual/form set, not an employer or government certificate.
- **Association-side workflow and traceability — PARTIAL.** §4–§9 cover request, intake, inspection, authorization, disposition, access log, correction, and replacement. Several gate and register fields are missing or inconsistent.
- **Evidence-grade logic — PARTIAL.** §2.2 defines G0–G3/GX well, but §7.3 conflicts with it (see defect 4).
- **Source gate and complete worked hold case — FAIL as written.** §7.1 opens and reviews a case despite no confirmed REAL source; it should stop at `HOLD_SOURCE_NOT_CONFIRMED`.
- **Privacy / authorization gate — PARTIAL.** §4.2’s explicit pass rules omit several required conditions, including `AUTH_TARGET`, `AUTH_SCOPE`, `AUTH_DATE`, `CHECKER`, and `WITHDRAWAL_STATUS = UNKNOWN`.
- **Full forms and decision branches — PARTIAL.** The forms and branches exist, but §6.1/§6.2/§6.4/§8.1 have field or precedence gaps.
- **Small-association suitability — PARTIAL.** §3 avoids invented departments, but dual sign-off fields and single-staff closure rules are unclear.
- **SAMPLE/REAL boundary and replacement register — PARTIAL.** Disclaimers are strong, but “原始點協會,” §6.2’s case-ID reuse, and §9’s unconditional checklist weaken the boundary.
- **No fabricated third-party proof/approval — PASS with caveat.** No employer reply, certificate, or approval is fabricated; §7.2 explicitly says no contact. §6.2’s “已取得…書面授權” is a residual implication risk.
- **Cross-document separation — PASS.** §2.3 and §10 correctly separate 0090, 0092, and 0088.
- **Math/date/case consistency — PARTIAL.** Dates are ordered, but contact and decision dates are missing; no rate math is performed.
- **Title-blind identification — PASS.** §1’s “當學員自願提供就業證明時，協會端如何安全地…” and §2.3’s “收案與查核痕跡” make the purpose clear without the title.

### 2. Remaining concrete defects

1. **§5 Step 1 vs §7.1 — source gate contradiction.**  
   §5 says: “任一缺失 → 處置 HOLD_SOURCE_NOT_CONFIRMED，不得開案.” §7.1 nevertheless uses `SYN-COHORT-2026-Q1（← 須以 REAL 班期定位碼替換）`, says `CHECKS_PERFORMED ... 未核對REAL班期、期間或用途`, and assigns `DISPOSITION | HOLD_NO_AUTHORIZATION_OR_ORIGINAL`. Under §8.1, missing REAL source means `HOLD_SOURCE_NOT_CONFIRMED ... 未開案`, not an opened G0 case with review and access log.

2. **§4.2 — authorization gate can pass without complete authorization.**  
   The “判定規則” only explicitly blocks missing `EVIDENCE_LOCATOR`, missing/empty `AUTH_EXPIRY`, `WITHDRAWN`, `AUTH_BASIS = NOT_PROVIDED`, or unspecified `PERMITTED_CHANNEL`. It does not explicitly block `AUTH_TARGET = NOT_PROVIDED`, missing `AUTH_SCOPE`, missing `AUTH_DATE`, missing `CHECKER`, `WITHDRAWAL_STATUS = UNKNOWN`, or an expired `AUTH_EXPIRY`. The “empty” versus “NOT_PROVIDED” wording is also inconsistent.

3. **§6.2 — employer request can exceed the authorized scope.**  
   The template always asks for “在職狀態” and “到職日期” while only stating “授權範圍為【AUTH_SCOPE】.” If `AUTH_SCOPE` covers only employment status, the request still asks for start date, contrary to §5 Step 6’s requirement that the authorization cover the requested fields. The template needs conditional fields or an explicit pre-send scope check.

4. **§7.3 — evidence-grade wording contradicts §2.2.**  
   §7.3 says: “就業證明之所以為證明，是因為存在一份由核發者具名、可追溯、可受檢視的文件（G1/G2）…” But §2.2 says G1/G2 do not prove authenticity, content, or employment and are not independent verification. G1/G2 are intake/inspection states; only G3 within scope supports a verified statement.

5. **§6.4 — register omits fields referenced elsewhere.**  
   §9 refers to `APPROVED_PURPOSE`, `NOTICE_VERSION`, and `LEARNER_CHANNEL`, but §6.4 has only `LEARNER_CONTACT_BASIS / LEARNER_GATE_RESULT`. The register also lacks an `AUTH_*` gate reference, `CHECKER`, `WITHDRAWAL_DATE`, `DECLINED_DATE`, `CONTACT_DATE`/`SELF_REPORT_DATE`, `REVIEW_DATE`/`DISPOSITION_DATE`, `RECEIVED_BY`, and `INSPECTED_BY`. §7.1 combines `LEARNER_CONTACT_BASIS / LEARNER_GATE_RESULT` and supplies only `INBOUND_VOLUNTARY`, so the contact basis itself is not recorded.

6. **§6.1 — learner template uses the wrong channel field and has a dangling alternatives reference.**  
   It says “透過協會授權管道【PERMITTED_CHANNEL 欄位】送達,” but §4.1 defines `LEARNER_CHANNEL`; §4.2 defines `PERMITTED_CHANNEL` for employer/issuer verification. It also says “見替代選項,” while §6.3 only says “依正式政策提供非雇主選項” without listing the alternatives. The template does not explicitly attach or reference the retention/notice version required by §4.1.

7. **§9 — pre-opening checklist conflicts with G0/no-original cases.**  
   The heading says “開案前逐項打勾,” but the list requires “REAL 同意／授權文件定位碼已取得” and “REAL 限制存取儲存位置已指定.” A learner self-report with no employer authorization or original—such as §7.1—cannot satisfy this. These items should be conditional on external contact or receipt of an original. “非單人兼任 G3” is also imprecise because G3 is an evidence grade, not a role.

8. **§3 / §6.3 / §6.4 — sign-off, withdrawal, and single-staff rules are incomplete.**  
   §3 requires `PRIV-ROLE` fields to be “分開簽” and two different people to sign, but §6.4 records only `REVIEWER_ROLE`, with no unique staff identifiers, sign-off dates, or original-recipient field, so distinctness cannot be evidenced. §6.3 says “記錄撤回時間,” but there is no `WITHDRAWAL_DATE`. Its script says “停止尚未進行的外部聯繫,” while §5 says “停止一切對外聯繫.” The single-staff rule says no G3 but does not clearly state whether a G0–G2 case may close.

9. **SAMPLE/REAL boundary wording.**  
   The cover uses the undefined proper noun “原始點協會”: “不代表原始點協會曾執行、核准或收件.” This should be “本協會” or “任何協會.” §6.2 uses `SYN-0091-CASE-01` and says “已取得…書面授權,” while §7.2 records `AUTH_BASIS NOT_PROVIDED` and `GATE_RESULT HOLD`. The template is marked SAMPLE, but the shared case ID creates an implication that an employer request was prepared for a case with no authorization.

10. **Minor consistency issues.**  
   §8.1 has overlapping dispositions (`G2_NO_EXTERNAL_CHECK`, `HOLD_NO_AUTHORIZATION`, `HOLD_NO_AUTHORIZATION_OR_ORIGINAL`) without precedence. §6.4 allows `NOT_APPLICABLE` but §7.1 uses `ITEM_TYPE | 無`. `PUBLIC_LOCATOR` is defined in §8.3 and §9 but is absent from §6.4/§7.1.

### 3. Math/date/case consistency

- Dates in §7.1/§8.4 are internally ordered: `2026-06-01 ≤ 2026-06-20 ≤ 2026-07-15 ≤ 2026-08-31`.
- No rate or denominator is calculated; `NO_RATE_UNKNOWN_DENOMINATOR` is present. No math error found.
- `AUTH_DATE`/`AUTH_EXPIRY = NOT_PROVIDED` and `NOTICE_VERSION = NOT_APPLICABLE` are consistent with the no-authorization/inbound scenario.
- The case lacks a self-report/contact date and a review/disposition date. The `2026-06-20` access-log date is a read event, not necessarily the decision date, so full chronology cannot be verified.
- `SYN-0091-CASE-01` and `SYN-0091-ACCESS-01` are consistent. `SYN-PUBLIC-0091-01` appears only in the replacement mapping, not in the sample or register.

### 4. SAMPLE/REAL boundary

The official source block correctly isolates the REAL identifiers: PDF page 6, I17D-E05, checkbox 098, official text, and PDF SHA. The document repeatedly marks cases, templates, access logs, and statuses as SAMPLE/SYNTHETIC. No employer reply, government approval, or third-party certificate is fabricated, and §7.2 expressly says no employer contact.

The boundary is not clean because of “原始點協會,” §6.2’s use of the hold case ID with “已取得…書面授權,” §7.1’s opened case despite no REAL source, and §9’s unconditional REAL-authorization checklist. These are implication and consistency risks, not evidence of actual fabrication.

### 5. Cross-document separation

**PASS.** §2.3 and §10 clearly distinguish:

- **0090 / I17D-E04:** supervisor-observed learning outcome, not employer evidence.
- **0092 / I17D-E06:** thank-you-letter request and original tracking, not employment proof.
- **0088 / I17D-E02:** broader post-training follow-up; no reuse of cases, results, denominator, or conclusions unless a shared REAL source is confirmed.
- Checkbox **098** is explicitly distinguished from DOCX ID **0098**.

### 6. Title-blind identification

**PASS.** Even without the title, §1’s “當學員自願提供就業證明時，協會端如何安全地…” and §2.3’s “本文件只是該證明之『收案與查核痕跡』” identify this as association-side employment-proof intake/verification, not a certificate. §6.2’s “非雇主回覆” reinforces the distinction.

This is a candidate review only; it is not formal acceptance, approval, certification, or a layout review.

**Exact candidate SHA repeated:** `8c9b8f7ec6fa37f9ad833fa5df406ef2c9d120e675eea28cc3d3b15e5b9c4ac3`
