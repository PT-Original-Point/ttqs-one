from __future__ import annotations
from pathlib import Path
from datetime import datetime
import hashlib, re

HERE = Path(__file__).resolve()
REPO = HERE.parents[5]
DOCS = REPO / 'docs' / 'ttqs-quality-20261016'
QR = DOCS / 'quality-review'
REPORTS = DOCS / 'reports'
BASE = REPORTS / 'TTQS_ONE_ANTIGRAVITY_OUTSOURCING_INCIDENT_AUDIT_20261018_R02.md'
OUT = REPORTS / 'TTQS_ONE_ANTIGRAVITY_OUTSOURCING_INCIDENT_AUDIT_20261018_R03.md'
PKG = QR / '0058_R01'

raw = BASE.read_bytes()
base_sha = hashlib.sha256(raw).hexdigest().upper()
base_text = raw.decode('utf-8')
bell_count = base_text.count('\x07')
clean = re.sub(r'\x07(?=gy)', 'a', base_text)
remaining_controls = [(ord(ch), clean.count(ch)) for ch in set(clean) if ord(ch) < 32 and ch not in '\n\r\t']

files = sorted(p for p in QR.rglob('*') if p.is_file() and 'antigravity' in str(p).lower() and re.search(r'(stdout|response|execution|stderr|exit_code|prompt)', p.name, re.I) and p.suffix.lower() in {'.json','.md','.txt','.raw'})
base_norm = clean.replace('\r\n','\n')
records = []
missing = []
for p in files:
    rel = p.relative_to(REPO).as_posix()
    content_bytes = p.read_bytes()
    sha = hashlib.sha256(content_bytes).hexdigest().upper()
    content = content_bytes.decode('utf-8-sig', errors='replace')
    norm = content.replace('\r\n','\n').strip()
    in_base = bool(norm) and norm in base_norm
    if not norm:
        status = 'EMPTY; path/hash retained in this manifest'
    elif in_base and not rel.startswith('docs/ttqs-quality-20261016/quality-review/0058_R01/'):
        status = 'full text already present in R02 body'
    else:
        status = 'full text appended below'
        missing.append((p, rel, content, sha, len(content_bytes)))
    records.append((rel, sha, len(content_bytes), status))

now = datetime.now().astimezone().isoformat(timespec='seconds')
pkg = PKG
hashes = {}
for label, path in {
    'DOCX candidate R05': pkg/'candidate'/'0058_R05.docx',
    'PDF render R05': pkg/'evidence'/'render_R05'/'0058_R05.pdf',
    'R05 render manifest': pkg/'evidence'/'render_R05'/'render_manifest.json',
    'Unique Blueprint R05': pkg/'worker'/'antigravity'/'0058_UNIQUE_BLUEPRINT_R05.md',
    'Content JSON R05': pkg/'worker'/'antigravity'/'0058_CONTENT_R05.json',
    'Synthetic replacement register R05': pkg/'worker'/'antigravity'/'0058_SYNTHETIC_REPLACEMENT_REGISTER_R05.csv',
    'R04 Antigravity execution receipt': pkg/'evidence'/'antigravity_0058_R04'/'execution.json',
}.items():
    b = path.read_bytes()
    hashes[label] = (path.relative_to(REPO).as_posix(), len(b), hashlib.sha256(b).hexdigest().upper())

update = f'''\n\n# Antigravity incident audit — R03 continuation (2026-10-18)\n\n> This R03 report preserves the complete prior R02 report text and adds the latest 0058 outsourcing history, all previously unembedded Antigravity prompts/responses/receipts, current document production state, and the independent review route status. R02 is retained unchanged.\n\n- Report generated (local time): `{now}`\n- Preserved base: `{BASE.name}`; original bytes `{len(raw)}`; SHA-256 `{base_sha}`.\n- R02 had `{bell_count}` U+0007 control characters inside the literal text for “antigravity”; this copy replaces only the malformed `\\x07gy` sequences with `agy`. Other control characters found after sanitization: `{remaining_controls}`.\n- Antigravity response/provenance inventory under `quality-review`: `{len(files)}` text artifacts. R02 already contains `{sum(1 for r in records if 'already present' in r[3])}` complete non-empty artifact bodies; this R03 appendix adds the remaining `{len(missing)}` bodies verbatim. Empty files are marked EMPTY and identified by exact SHA.\n\n## Current production and acceptance state\n\n- **Current document:** DOCX `0058`; official requirement `I13-E02`; official checkbox serial `062`; official source page 4, indicator 13, second checkbox. These identifiers are distinct; “0058” is the document sequence, not checkbox row 058.\n- **R05 candidate SHA-256:** `{hashes['DOCX candidate R05'][2]}` (`{hashes['DOCX candidate R05'][1]}` bytes). It remains a SAMPLE/SYNTHETIC draft candidate. No association approval, real execution, real participant evidence, Human acceptance, or promotion is claimed.\n- **R05 mapping/working files:**\n\n| Artifact | Bytes | SHA-256 |\n|---|---:|---|\n''' + ''.join(f'| `{label}` (`{path}`) | {size} | `{sha}` |\n' for label,(path,size,sha) in hashes.items()) + f'''\n- The R05 candidate contains 10 document-specific sections, 17 tables, and 41 registered synthetic facts for case `SYN-0058-202608`. It maps to I13-E02 / checkbox 062 and is explicitly distinguished from 0057 / I13-E01 / 061 and 0059 / I13-E03 / 063.\n- Word COM exported the R05 DOCX to a 32-page PDF because the packaged LibreOffice renderer was unavailable (`soffice.exe` missing). All 32 pages were rendered to PNG and visually inspected in eight four-page contact sheets. The three located R04 pagination defects were corrected: the front-matter use sequence no longer leaves an orphan at page 2; step-six text no longer leaves an isolated tail line; Table 7-2 caption/header starts with its data on page 23. The final page contains only the continuation of the revision-history table (minor whitespace concern, not treated as semantic acceptance).\n- Local visual inspection is not independent acceptance. Exact-SHA independent OpenCode v2 semantic review is recorded separately under `quality-review/0058_R01/review/`; candidate remains unaccepted until a usable independent terminal result and any findings are resolved.\n\n## Why Antigravity outsourcing did not proceed smoothly\n\nThe evidence shows two different failure classes; a successful CLI exit is not proof of useful or correct work.\n\n1. **Headless permission failure masked by exit 0 (R01).** Antigravity returned `status=SUCCESS` and exit code 0, but stderr records a denied `read_file`, the response field is empty, and no usable deliverable was recovered. Usage counters are non-zero despite the empty response. The repair was to back up the settings, grant only the exact current prompt/source reads and the 0058 work-package output writes, avoid global permission bypass, and restore the original settings after the scoped invocation.\n2. **Self-reported completeness exceeded verified content (R02–R04).** R02 and R03 returned substantial responses and output files, but later review identified inaccurate rounding explanations, unsupported claims about historical association practice, assumed existing roles/approval authority/current systems, proposal thresholds presented as if operational, and ambiguous blank-form/SAMPLE instructions. R03 reported these corrected. The R04 response again claimed the authorization and proposal boundary was fixed; deterministic readback still found residual administrative/supervisory roles, a specific approving body, and “current system” wording. Therefore R04 model self-report was not accepted as evidence that those issues were removed.\n3. **Deterministic integrator repairs were required.** An integrator-side R04 patch changed the content, blueprint and build metadata to remove the residual unsupported claims, label procedures and incentives as unapproved proposals, and preserve all 41 synthetic facts. A separate R05 layout patch corrected the three observed page-flow defects without changing the case data. These are integrator changes, not Antigravity outputs.\n4. **Renderer dependency issue (separate from Antigravity).** The prescribed document renderer could not start because `soffice.exe` was unavailable. This was repaired by exporting with local Microsoft Word COM and rendering the PDF pages with `pypdfium2`; it did not involve Computer Use.\n5. **Independent reviewer route is separately rate-limited.** OpenCode CLI v2.0.29 listed free models, but the first GLM and second Mimo review attempts returned provider quota HTTP 429 with no review. A third Beam-free attempt is running/has its own receipt under the review folder; this OpenCode problem is not attributed to Antigravity.\n\n### 0058 Antigravity attempt chronology\n\n| Attempt | CLI status / exit | Conversation | Actual outcome and defect | Corrective action / disposition |\n|---|---|---|---|---|\n| R01 | `SUCCESS` / 0, 15.769 s | `ea9288a7-4848-4d89-a944-c1af9ba7ebac` | `response` empty (0 bytes); headless `read_file` denied. CLI status concealed a non-usable result. Usage: input 34,418; output 1,638; thinking 1,421; cache 0; reported total 36,056. | Backed up settings; added narrowly scoped source/prompt read and package-only output grants; no permission bypass; exact settings SHA restored after run. |\n| R02 | `SUCCESS` / 0 | `8f678926-388c-4322-8cf7-df548f38f60c` | 6,076 response bytes; generated draft Blueprint/JSON/CSV/build materials, reported 41 synthetic facts and extensive calculations. Subsequent repair instructions exposed unresolved content/truth-boundary issues. Usage: input 128,428; output 67,937; thinking 22,464; cache read 648,077; reported total 196,365. | Preserve R02 outputs; send targeted R02 repair prompt; do not treat worker self-QA as acceptance. |\n| R03 | `SUCCESS` / 0 | Same R02 conversation | 9,214 response bytes. Claimed correction of rounded percentage-point arithmetic, unsupported history/roles/policies, proposal state, blank forms and REAL replacement directions. Integrator later found residual authority/current-role assertions. Usage: input 198,975; output 127,777; thinking 32,703; cache read 1,915,116; reported total 326,752. | Preserve response; formulate narrower authorization-boundary repair; verify actual files independently. |\n| R04 | `SUCCESS` / 0, 347.668 s | Same R02/R03 conversation | 9,510 response bytes. Stderr: account warning says `--mode auto` unavailable and CLI continued in default mode. Model still asserted correction was complete; actual R03 content retained unsupported role/approver/current-system assertions. Usage: input 440,641; output 189,981; thinking 44,466; cache read 3,209,241; reported total 630,622. | Do not accept the self-report. Apply deterministic integrator R04 content/Blueprint patch; then build R04 and apply only the three visually located pagination repairs in integrator R05. |\n\nAll four calls requested only `gemini-3.8-flash-high`; no Computer Use was used. Sum of provider-reported `total_tokens` fields is 1,189,795 (a usage field sum, not a bill or cost). Monetary cost is not independently returned and is `UNKNOWN`; do not call it zero. R01 is one permission/empty-response failure followed by successful transport on R02–R04. The evidence does not meet the earlier route-pause rule of three consecutive execution failures after three repair attempts: the later CLI calls executed and returned, although their content still required integration repair. Antigravity route is not represented as flawless or paused.\n\n### Exact repair trail and evidence paths\n\n- Scoped R04 invocation and settings restoration: `docs/ttqs-quality-20261016/quality-review/0058_R01/evidence/antigravity_0058_R04_scoped_invoke.ps1`; receipt `{hashes['R04 Antigravity execution receipt'][0]}` SHA `{hashes['R04 Antigravity execution receipt'][2]}`.\n- R04 integrator truth-boundary patch: `evidence/patch_0058_integrator_R04.py` and `.json`. This changed integrator copies; it did not rewrite Antigravity’s raw R03 response.\n- R05 layout-only patch: `evidence/patch_0058_layout_R05.py` and `.json`. It records the R04 DOCX SHA, three page-specific defects and the repaired R05 output SHA.\n- Full Antigravity prompts, stdout JSON, stderr, exit codes, R04 execution receipt and any older project Antigravity prompt/response artifact absent from R02 are reproduced in the appendices below. The current raw response files remain available at their repository paths listed in the manifest.\n\n## OpenCode v2 independent review attempts (separate route)\n\n| Attempt | Model | Result | Handling |\n|---|---|---|---|\n| R01 | `opencode/glm-5.3-flash-free` | Provider `FreeUsageLimitError`, HTTP 429; session `ses_eb4dd9325ffe9oXr3xiZMQ1NxO`; no review. | Saved raw JSON; switched to another currently listed free model. |\n| R02 | `opencode/mimo-v2.6-flash-free` | Provider `FreeUsageLimitError`, HTTP 429; session `ses_eb4dd3dadffeNgowqsWxUAfsee`; no review. | Saved raw JSON; switched to `opencode/beam-free`. |\n| R03 | `opencode/beam-free` | See `review/opencode_v2_semantic_R03/` and final status recorded in this report after CLI completion. | Same R05 exact SHA and read-only review prompt; no DOCX modification. |\n\n## Antigravity evidence coverage manifest\n\nThe preserved base plus this appendix inventories `{len(records)}` Antigravity prompt/response/execution text artifacts under `quality-review`. Each non-empty artifact body is either already embedded verbatim in R02 or reproduced verbatim below; empty files have explicit empty-state/hash records.\n\n| Repository path | Bytes | SHA-256 | Inclusion in this report |\n|---|---:|---|---|\n''' + ''.join(f'| `{rel}` | {size} | `{sha}` | {status} |\n' for rel,sha,size,status in records)

appendix = '\n\n## Full raw Antigravity artifacts missing from the prior R02 report\n\nThe following file bodies are copied verbatim from the local evidence files. The enclosing code-fence length is selected to avoid altering any inner text.\n'
for p, rel, content, sha, size in missing:
    lang = 'json' if p.suffix.lower()=='.json' else ('text' if p.suffix.lower() in {'.txt','.raw'} else 'markdown')
    max_run = max((len(x) for x in re.findall(r'`+', content)), default=0)
    fence = '`' * max(4, max_run + 1)
    appendix += f'\n### `{rel}`\n\n- Bytes: {size}\n- SHA-256: `{sha}`\n- Raw content follows.\n\n{fence}{lang}\n{content}'
    if not content.endswith('\n'):
        appendix += '\n'
    appendix += fence + '\n'

# Also attach the exact R04 scoped-invocation wrapper, which establishes the CLI route and settings restoration.
wrapper = PKG/'evidence'/'antigravity_0058_R04_scoped_invoke.ps1'
if wrapper.exists():
    b = wrapper.read_bytes(); content = b.decode('utf-8-sig', errors='replace')
    sha = hashlib.sha256(b).hexdigest().upper(); max_run=max((len(x) for x in re.findall(r'`+', content)), default=0); fence='`'*max(4,max_run+1)
    appendix += f'\n### `{wrapper.relative_to(REPO).as_posix()}` — scoped invocation wrapper\n\n- Bytes: {len(b)}\n- SHA-256: `{sha}`\n\n{fence}powershell\n{content}' + ('' if content.endswith('\n') else '\n') + fence + '\n'

footer = '''\n\n## Current disposition\n\n`0058_R05.docx` remains a CANDIDATE SAMPLE/SYNTHETIC artifact. The three known pagination defects from R04 have been repaired and all 32 pages were visually inspected locally. Independent exact-SHA semantic review is the remaining acceptance evidence; a free-model quota or encoding problem is recorded as a reviewer-route issue and does not turn a candidate into PASS. No true association records, approvals, signatures or third-party evidence were invented. Continue with the exact candidate and only repair a reviewer finding that is tied to the reviewed SHA.\n'''

OUT.write_text(clean + update + appendix + footer, encoding='utf-8', newline='\n')
out_bytes=OUT.read_bytes()
print(f'WROTE={OUT}')
print(f'BASE_BYTES={len(raw)} BASE_SHA256={base_sha} SANITIZED_BELL_COUNT={bell_count}')
print(f'INVENTORY={len(files)} EMBEDDED_IN_BASE={sum(1 for r in records if "already present" in r[3])} APPENDED={len(missing)}')
print(f'OUT_BYTES={len(out_bytes)} OUT_SHA256={hashlib.sha256(out_bytes).hexdigest().upper()}')