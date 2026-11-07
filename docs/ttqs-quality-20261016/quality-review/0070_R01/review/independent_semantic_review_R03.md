# Independent exact-SHA semantic review — DOCX 0070 R03

**Verdict: PASS**

Independent semantic review of candidate `docx_extracted_R03.md` (SHA `55af406663f29e6a3ea8fb644d61c029c74df42934166e6076a991fdcd895bba`) against official page‑5 extract (PDF SHA `805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709`) and Blueprint `0070 R01`.

Verification summary (anchors):

- **Identity / genre**: Cover line “文件識別：DOCX 0070｜官方要求 I16-E02｜官方勾選序號 077”; title “訓練異常處理程序與工具”; explicit “SAMPLE／SYNTHETIC 示範稿，尚未生效、未經協會核定.” Matches operational abnormal‑handling procedure/tools, not routine control/CAPA/audit/course plan (§2.2 table).
- **Roles**: §3 table, R1–R5 (5 functional roles), with trigger/responsibility/decision‑authority‑pending/outputs/prohibitions/proxy; independent‑reviewer separation stated (“R2 不得同時擔任 R4”).
- **Classification/severity**: §4.1/§4.2 tables, 6 categories + L1–L4 proposal values marked “待核定”.
- **SOP**: §5 steps 1–10, each with input/who/output/rejection conditions.
- **Filled synthetic case**: §6.1–§6.9, `SYN-0070-CASE-01`, facts match Blueprint (2026‑09‑25; 08:42/08:44/08:48/08:55; 12 registered; 0 entered; 09:00–09:30 12/12 notified; 09:30 10/12; 11:00 2/2; total 12/12; checks 2026‑10‑02/10‑09/10‑16 each 3/3; closure proposal 2026‑10‑17). Record IDs consistent with §8 replacement register.
- **Arithmetic**: §7.1 (10÷12=83.3%, 2÷2=100%, 12÷12=100%); §7.2 (9÷9=100%, 3÷3=100%); denominators/periods stated; explicitly “不是協會實績/正式再發率” (§7.3).
- **SAMPLE vs REAL**: §2.4, §6.1, §6.3, §6.9, §12.2 consistently `UNKNOWN／HOLD`; no fabricated people/signatures/execution/third‑party responsibility; notification counts only, no PII.
- **Hold/reject criteria**: §1.2 (H1–H7), §9 (C1–C10).
- **Blank tools**: §10.1–§10.6 each with filler/timing/required source/rejection conditions; stated auxiliary only.
- **Cross‑document non‑linkage**: §11 (0069/0071/0072/0033) with case_id/date/denominator/source rule; sample explicitly not linked.
- **Last‑page proposals/REAL source register**: §12.1 (P1–P6), §12.2 (S1–S6).

No blocking defect identified. Minor cosmetic note: cover identity fields are pipe‑separated on one line rather than separate rows, but all three identifiers are present and unambiguous. Font size/layout cannot be verified from text extraction (visual QA separate).

## Execution and scope

- Route: OpenCode CLI v2.0.29; model selected by CLI: `opencode/beam-free`.
- Session: `ses_eaf6a82f1ffeKXqVmEaCKJeS09`.
- CLI exit: 0; stderr bytes: 0.
- Candidate DOCX SHA-256 before/after review: `55af406663f29e6a3ea8fb644d61c029c74df42934166e6076a991fdcd895bba` (unchanged).
- Reviewer input: official page-5 extract, unique Blueprint and exact-candidate DOCX text extraction.
- The CLI did not return a separate runtime-model attestation. The requested model and session output are preserved in the raw JSONL.
- This is semantic review only; it is not visual acceptance or Association approval.
