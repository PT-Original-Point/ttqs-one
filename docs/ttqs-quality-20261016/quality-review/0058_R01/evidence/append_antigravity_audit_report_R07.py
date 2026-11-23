from pathlib import Path
from hashlib import sha256
import json
import shutil

repo = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016")
qa = repo / "docs/ttqs-quality-20261016/quality-review/0058_R01"
review = qa / "review/opencode_v2_semantic_R05"
reports = repo / "docs/ttqs-quality-20261016/reports"
base = reports / "TTQS_ONE_ANTIGRAVITY_OUTSOURCING_INCIDENT_AUDIT_20261018_R06.md"
target = reports / "TTQS_ONE_ANTIGRAVITY_OUTSOURCING_INCIDENT_AUDIT_20261018_R07.md"
assert base.exists(), f"Missing base report: {base}"
assert not target.exists(), f"Refusing to overwrite existing report: {target}"
shutil.copy2(base, target)

def sha(path):
    return sha256(path.read_bytes()).hexdigest().upper()

def rel(path):
    return str(path.relative_to(repo)).replace("\\", "/")

def raw_block(title, path):
    data = path.read_text(encoding="utf-8", errors="replace")
    return f"\n#### {title}\n\nPath: `{rel(path)}`  \nBytes: {path.stat().st_size}  \nSHA-256: `{sha(path)}`\n\n`````text\n{data}\n`````\n"

def receipt_block(title, path):
    data = path.read_text(encoding="utf-8-sig", errors="replace")
    return f"\n#### {title}\n\nPath: `{rel(path)}`  \nSHA-256: `{sha(path)}`\n\n`````json\n{data}\n`````\n"

ag = [
    ("R01", "antigravity_gemini38_0058_R08_semantic_R01"),
    ("R02", "antigravity_gemini38_0058_R08_semantic_R02"),
    ("R03", "antigravity_gemini38_0058_R08_semantic_R03"),
    ("R04", "antigravity_gemini38_0058_R08_semantic_R04"),
]
app = []
app.append("""

---

# Addendum R07 — 2026-10-18: 0058 R08 review and cross-route recovery

This is an additive audit record. R06 remains unchanged as the prior report version. The report now includes the complete raw Antigravity CLI outputs and route receipts for the 0058 R08 review, plus the OpenCode v2 fallback evidence. No Computer Use was invoked.

## 0058 R08 document result

- Mapping: `doc_id=0058` → `I13-E02` → official checkbox `062`; Unique Blueprint R06 SHA-256 `7606D16B80A4886CF6871943EF46DE0407D3EFB921FD6DB63597615F4C5B81F4`.
- Final candidate SHA-256: `0DFCAAE1FF9943E46C1B9D527C3DF34FA61048547268C482D0DD378E44D7C58B`.
- Word-render PDF SHA-256: `97A83ADD1FC52342AB9FD4D0035EBCC79488B023B6FE5F2DB299FD71A85A8F61`, 32 pages.
- R06 had the Table 10-3 caption/header stranded at the foot of page 30. R07 moved the caption but left the R06 row alone on page 33; R07 is preserved as a failed historical candidate. R08 was derived directly from R06 and changes only a page break plus 35 Table 10-3 data-cell line spacings (13.8pt to 12pt); table type remains 9.5pt. All 759 DOCX text nodes and every other OOXML part are unchanged; the R06 and R08 JSON/CSV sidecars are byte-identical.
- Technical QA: PASS. Visual QA: PASS; all eight contact sheets for pages 1–32 and full-resolution pages 29–32 were directly inspected in Codex. The table caption/header with rows R00–R03 now occupies page 31; the repeated header and rows R04–R06 occupy page 32. No row is stranded on page 33.
- Independent exact-SHA semantic delta review: PASS, qualified, by OpenCode CLI v2.0.29 using `opencode/longcat-2.5-preview-free`, distinct from the Antigravity Builder. The reviewer independently hashed R08/R06, checked package/XML/text-node and sidecar identity, and found no semantic risk. It did not directly inspect page images; visual PASS is based on the separate direct Codex inspection. Formal acceptance remains NOT CLAIMED; all demonstration facts remain SAMPLE/SYNTHETIC.

## Antigravity R08 route attempts — complete sequence

All model invocations specified only `gemini-3.8-flash-high`; effort was high; mode was plan with sandbox; Computer Use was false. The candidate SHA remained unchanged across every attempt.

| Attempt | Result | Exact observed issue and repair |
|---|---|---|
| R01 | CLI exit 2; model was not invoked | `--print` consumed `--print-timeout` as its prompt. Repaired by removing the standalone `--print` flag and using `--prompt <text>`. |
| R02 | CLI exit 2; model was not invoked | The duration parser rejected `1200` because it required a unit. Repaired with `20m`. |
| R03 | CLI exit 0, but response empty | The model called `RunCommand`; headless mode denied the command permission. Exact read-only packet-directory `read_file(...)` allow rule was added; no command permission and no broad auto-approval were added. The same Antigravity conversation was resumed with instructions to use only read_file and no command. |
| R04 | CLI exit 0; full response returned | Same conversation `36d655c5-9a04-4030-9c6f-69b46e9c2dc3`; 2 turns including the blocked turn; candidate unchanged; settings unchanged during this attempt. Response verdict: PASS, qualified. Because Antigravity also built R06, this is recorded as same-platform corroboration and is not counted as the independent semantic acceptance. |

The Antigravity response did not claim direct page-image inspection. It identified the same exact candidate SHA and the same bounded layout delta. The independent OpenCode exact-SHA receipt is the semantic acceptance evidence for R08.

## OpenCode v2 reviewer route recovery

- The original `opencode/beam-free` request reached the session but returned `provider.quota`, HTTP 429 `FreeUsageLimitError`; no review text was produced. Candidate SHA did not change.
- `opencode/space-bunny-free` was attempted as a recovery and returned the same 429 quota error. The route was then switched, without a new Codex thread, to `opencode/longcat-2.5-preview-free`, which is available in the installed CLI model list and had a recent usable-case report supplied by Human.
- LongCat completed successfully (exit 0, stderr empty, 7m35s measured route interval). It independently checked R08 and R06 DOCX SHA values; 18 tables/105 paragraphs/759 text nodes; one changed OOXML entry; exact XML layout delta; the R06/R08 content JSON and CSV; Blueprint and official-source SHA; and PDF page flow. It created temporary read-only verification scripts under `%TEMP%\opencode`; it did not write to the candidate or QA evidence directory. The invocation receipt confirms the candidate SHA was unchanged.
- OpenCode raw JSONL and final review are included in the linked review packet and synchronized with this report. The model returned **PASS — qualified semantic delta review only**; it expressly states visual pages were not directly viewed and formal acceptance is NOT CLAIMED.

## Settings and permission state

- Antigravity settings SHA before adding a narrowly scoped read rule: `97699E28319D6748FFC5EE27CA843C36E547F5F91F766AC7D84783EC53F4763F`.
- After adding the exact R08 review-packet `read_file` rule: `DDDBF7B8B80ACEE1BD24355AC8C1BCC0C992BC43F47F5B0B7580A5A80C75FAF3`.
- The R03 Antigravity CLI interaction changed the settings file digest to `9CADFDAE533DAD7C333DCF0279CEDFDFCBAB926D518C84E2AA9E60FE7E977D07`; R04 left it unchanged. The final `permissions.allow` list contains the three pre-existing exact rules plus the one exact R08 packet `read_file` rule. No command permission, `--dangerously-skip-permissions`, or Computer Use permission was added. The byte-level cause of the R03 settings digest change is not isolated beyond the verified final permission list.

## Exact files and hashes

- R08 candidate: `docs/ttqs-quality-20261016/quality-review/0058_R01/candidate/0058_R08.docx` — `0DFCAAE1FF9943E46C1B9D527C3DF34FA61048547268C482D0DD378E44D7C58B`.
- R07 failed layout note: `docs/ttqs-quality-20261016/quality-review/0058_R01/evidence/visual_review_0058_R07_failure.md`.
- R08 technical QA: `docs/ttqs-quality-20261016/quality-review/0058_R01/evidence/technical_qa_0058_R08.json`.
- R08 visual review: `docs/ttqs-quality-20261016/quality-review/0058_R01/evidence/visual_review_0058_R08.md`.
- R08 combined state: `docs/ttqs-quality-20261016/quality-review/0058_R01/evidence/final_status_0058_R08.json`.
- OpenCode exact-SHA response and raw outputs: `docs/ttqs-quality-20261016/quality-review/0058_R01/review/opencode_v2_semantic_R05/`.

## Full Antigravity raw files

The sections below preserve each Antigravity R01–R04 prompt result, raw stdout, stderr, exit status, and route receipt. Empty stdout is explicitly retained for failed/empty-response attempts.
""")

for attempt, prefix in ag:
    baseprefix = review / prefix
    app.append(f"\n### Antigravity {attempt}\n")
    for kind, suffix in (("raw stdout", "_stdout.json"), ("raw stderr", "_stderr.txt"), ("exit code", "_exit_code.txt"), ("route receipt", "_route_receipt.json")):
        path = Path(str(baseprefix) + suffix)
        if path.exists():
            app.append(receipt_block(f"{attempt} {kind}", path) if suffix.endswith("_route_receipt.json") else raw_block(f"{attempt} {kind}", path))
    if attempt == "R04":
        response = Path(str(baseprefix) + "_response.md")
        if response.exists():
            app.append(raw_block("R04 complete human-readable model response", response))

app.append("\n## OpenCode route raw files\n\nOpenCode full traces and exact responses are separately preserved and SHA-bound; the independent LongCat response is included below as readable text, while the full 90,814-byte raw JSONL remains at the linked path.\n")
for name in ("opencode_longcat_R01_independent_review.md", "opencode_longcat_R01_stdout.jsonl", "opencode_space_bunny_R01_stdout.jsonl", "stdout_R05.jsonl"):
    path = review / name
    if path.exists():
        app.append(raw_block(f"OpenCode {name}", path))

with target.open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(app))

print(json.dumps({"base_report_sha256": sha(base), "updated_report": str(target), "updated_report_bytes": target.stat().st_size, "updated_report_sha256": sha(target), "appendix_chars": sum(map(len, app))}, ensure_ascii=False))
