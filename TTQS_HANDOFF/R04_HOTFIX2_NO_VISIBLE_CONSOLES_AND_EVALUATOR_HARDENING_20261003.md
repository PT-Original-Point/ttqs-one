# R04 HOTFIX2 — NO VISIBLE CONSOLES + EVALUATOR-FACING DOCX HARDENING — 2026-10-03

## Scope
Narrow correction only. Do not restart Mission, rebuild queue, or create a new runtime. Preserve existing CURRENT/queue/candidates/checkpoints.

## A. Stop desktop-interrupting windows immediately
The home Win10 PC is also an interactive personal computer. TTQS automation MUST NOT open visible PowerShell/cmd/conhost/Word/LibreOffice windows or steal focus.

1. Fresh-read prestate before mutation:
   - Scheduled Tasks matching TTQS/Codex/PowerShell;
   - current TTQS supervisor/task actions, triggers, principal, Hidden, LastRunTime/NextRunTime/LastTaskResult;
   - startup folders;
   - HKCU/HKLM Run and RunOnce values created by this TTQS runtime;
   - TTQS-related services;
   - WMI permanent event subscriptions;
   - current processes powershell.exe/pwsh.exe/cmd.exe/conhost.exe/python.exe/pythonw.exe/wscript.exe/cscript.exe/codex.exe with PID/PPID/command line.
2. Correlate recent process launches with Task Scheduler history. Do not delete unrelated Windows/system tasks.
3. The known TTQS task TTQS_ONE_Codex_Supervisor is a primary suspect because it wakes repeatedly. If its action can create a visible console, disable future triggers first, let any in-flight exact lane finish or reach a stable checkpoint, then replace ONLY the launcher with a truly hidden background launcher.
4. Preferred hidden launcher:
   - use wscript.exe //B //NoLogo with a small .vbs wrapper, or pythonw.exe if the supervisor supports explicit file logging;
   - do NOT rely only on powershell.exe -WindowStyle Hidden if it still flashes a console on this host;
   - no visible console, no focus stealing, no toast/dialog for normal wakes.
5. Re-enable only after same-host verification that:
   - supervisor still resumes from the same queue/checkpoint;
   - no visible window appears during at least 3 consecutive wake cycles;
   - logs/checkpoints still update;
   - no duplicate task/launcher remains active.
6. Disable/remove duplicate TTQS launchers discovered in Task Scheduler/startup/Run/WMI only after exact scope + same-source readback confirms they are TTQS-owned and redundant.
7. If a hidden replacement cannot be verified safely, leave the visible launcher DISABLED rather than continuing to interrupt the desktop. Continue the current interactive Codex session manually until a hidden launcher is fixed. Do not disable unrelated system maintenance.

## B. Evaluator-facing DOCX hardening from Human audit
Primary artifact remains DOCX. Do not create full-corpus PDF/PNG.

Before CURRENT promotion, evaluator-facing DOCX must additionally satisfy:
1. First-page 30-second comprehension: plain Chinese stating purpose, user, timing, how to use, and output.
2. No internal factory/control language in evaluator-facing body: no Blueprint, Gatekeeper, reviewer, queue, root-cause, SHA, internal paths, receipt IDs, Fxxx/E3 replacement IDs, or similar control-plane metadata.
3. Synthetic disclosure is concise human language: e.g. 「示範資料｜非本會實際紀錄」. Detailed replacement-register IDs remain in internal control sidecars, not evaluator body.
4. No completely blank page.
5. No sparse orphan page with only a short heading/paragraph unless intentionally declared as a separator page.
6. No manual page break that creates blank/sparse pages.
7. Formal document-control strip: organization name from authoritative source if available, document title/number, version, status (示範/未生效 or 正式生效 only when supported), revision/effective date, preparer/reviewer/approver only when real authority exists. Never invent approval.
8. SAMPLE may be complete and operational, but must never imply actual historical execution, approval, performance, or third-party evidence.
9. Keep document-specific genre mechanics. No shared prose/table/question/SOP-body reuse across unrelated deliverables.

## Known Human-audit corrections
- 0025: remove the full blank page caused by pagination/page-break behavior.
- 0100: remove the full blank page.
- 0067: remove the sparse/orphan page and keep the limitations with the relevant analysis section.
- 0087: move the long per-fact replacement register out of evaluator-facing DOCX into internal control sidecar; keep only concise human-readable SAMPLE/REAL replacement guidance in the Word document.
- 0003: keep questionnaire mechanics, but move internal coding-field names/IDs out of the main evaluator-facing body or translate them to plain Chinese.
- Apply an impact scan for the same layout/internal-metadata pattern across CURRENT and remaining candidates. Do not rewrite clean bodies just because they share the same family.

## Lightweight layout verification
Do not persist PDFs/PNGs.
Use a non-interactive hidden method to inspect pagination only for the exact candidate before promotion. Preferred: Word COM with Visible=false/DisplayAlerts=0 or equivalent headless page-range inspection. Temporary files must be deleted after the check.
Hard fail: a completely blank page.
Review: a page with very low substantive text area unless it is an intentional separator.

## Promotion contract
Existing semantic gates remain mandatory:
- exact requirement/genre;
- title-blind;
- negative-neighbor;
- substantive duplication;
- evaluator-facing readability;
- SAMPLE/REAL truth boundary.
The new presentation/layout checks are additive and must not weaken those gates.

## Completion/readback
After mutation:
- same-source readback of TTQS scheduled tasks/startup/Run/WMI;
- list exactly what was disabled, deleted, replaced, or left unchanged;
- prove no visible TTQS console launch during 3 consecutive wake cycles;
- report CURRENT count and exact documents changed by this hotfix.
