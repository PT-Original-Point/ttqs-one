from pathlib import Path
from datetime import datetime
from copy import deepcopy
from zipfile import ZipFile
import hashlib, json, re, subprocess, sys, shutil
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml.ns import qn

REPO = Path(r'E:\PT-Original-Point\ttqs-one')
R01 = REPO / 'docs/ttqs-quality-20261016/quality-review/0107_I18-E15_R01_20261022'
R02 = REPO / 'docs/ttqs-quality-20261016/quality-review/0107_I18-E15_R02_20261022'
R01_DOCX = R01 / 'candidate/0107_I18-E15_R01_sample_certificate_pass_rate_evidence.docx'
R01_MD = R01 / 'source/manuscript_0107_R01_final.md'
R01_BLUEPRINT = R01 / 'source/unique_blueprint_0107_R01.md'
R02_DOCX = R02 / 'candidate/0107_I18-E15_R02_sample_certificate_pass_rate_evidence.docx'
R02_MD = R02 / 'source/manuscript_0107_R02_targeted_cutoff_repair.md'
OLD_SHA = '748ac062b33c1da0db75aa882905c4d0e8c624b0ab50189b7b37146bc6968651'
SOURCE_COMMIT = '2080a1eb89c6b3ea73a99f73f4bb7d9324cdeeba'
OLD_ID = 'TTQS-0107-I18-E15-SAMPLE-WRITER-R01-20261022-02'
NEW_ID = 'TTQS-0107-I18-E15-SAMPLE-WRITER-R02-20261022-01'
CUTOFF = '2026-07-29'


def sha_bytes(data): return hashlib.sha256(data).hexdigest()
def sha_file(path): return sha_bytes(path.read_bytes())
def write_json(path, data): path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
def md_cells(line): return [c.strip() for c in line.strip().strip('|').split('|')]
def md_line(cells): return '| ' + ' | '.join(cells) + ' |'

if not R01_DOCX.is_file() or not R01_MD.is_file() or not R01_BLUEPRINT.is_file():
    raise SystemExit('Required exact R01 candidate/source missing; no R02 generated.')
if sha_file(R01_DOCX) != OLD_SHA:
    raise SystemExit('R01 candidate SHA changed; refuse to patch stale bytes.')
if R02_DOCX.exists():
    raise SystemExit('R02 candidate already exists; refusing overwrite.')
R02.mkdir(parents=True, exist_ok=True)
for part in ('candidate', 'source', 'evidence/scripts', 'review', 'render'):
    (R02 / part).mkdir(parents=True, exist_ok=True)

original = R01_MD.read_text(encoding='utf-8')
lines = original.splitlines()
# Patch exactly one metrics table, following the Blueprint 5.D cutoff-date requirement.
starts = [i for i, line in enumerate(lines) if line.startswith('| 指標名稱 |')]
if len(starts) != 1:
    raise SystemExit(f'Expected exactly one metrics table header, found {len(starts)}.')
start = starts[0]
end = start
while end < len(lines) and lines[end].startswith('|'):
    end += 1
block = lines[start:end]
if len(block) != 6:
    raise SystemExit(f'Expected header, separator and four metric rows; got {len(block)} lines.')
header = md_cells(block[0])
separator = md_cells(block[1])
if len(header) != 6 or len(separator) != 6 or header[4] != '計算結果':
    raise SystemExit('Metrics table structure differs from the reviewed R01 source.')
header.append('觀察窗截止日<br>`cutoff_date`')
separator.append(':---:')
patched = [md_line(header), md_line(separator)]
row_labels = []
for line in block[2:]:
    row = md_cells(line)
    if len(row) != 6:
        raise SystemExit('Unexpected metrics row width; refusing broad transformation.')
    row_labels.append(re.sub(r'<br>.*', '', row[0]).strip('* '))
    row.append(f'`{CUTOFF}`')
    patched.append(md_line(row))
if len(row_labels) != 4 or not all(('指標 ' + key) in row_labels[index] for index, key in enumerate(('A：', 'B：', 'C：'))):
    raise SystemExit(f'Metric row identity mismatch: {row_labels}')
lines[start:end] = patched
new_md_text = '\n'.join(lines) + '\n'
if original.count(OLD_ID) != 1:
    raise SystemExit('Expected one visible R01 work ID in source; found a mismatch.')
new_md_text = new_md_text.replace('R01／`' + OLD_ID + '`', 'R02／`' + NEW_ID + '`', 1)
R02_MD.write_text(new_md_text, encoding='utf-8', newline='\n')
shutil.copy2(R01_BLUEPRINT, R02 / 'source/unique_blueprint_0107_R02.md')
for name in ('writer_input_0107_R01_current_source_snapshot.md', 'writer_input_0107_R01_original.md'):
    src = R01 / 'source' / name
    if src.exists(): shutil.copy2(src, R02 / 'source' / name)

# Targeted Word repair: insert one explicit cutoff-date column before calculation results.
shutil.copy2(R01_DOCX, R02_DOCX)
doc = Document(R02_DOCX)
metric_tables = [t for t in doc.tables if t.rows and t.rows[0].cells[0].text.strip() == '指標名稱']
if len(metric_tables) != 1:
    raise SystemExit(f'Expected one matching DOCX metrics table, found {len(metric_tables)}.')
table = metric_tables[0]
if len(table.columns) != 6 or len(table.rows) != 5:
    raise SystemExit(f'Unexpected DOCX metrics table shape: {len(table.rows)}x{len(table.columns)}.')
# Append the seventh column and keep all original metric columns in their exact order.
table.add_column(Cm(2.5))
widths = (2.8, 4.3, 3.8, 4.3, 2.1, 5.7, 2.5)
if abs(sum(widths) - 25.5) > 0.001:
    raise SystemExit('Landscape table width allocation error.')
for i, width in enumerate(widths):
    table.columns[i].width = Cm(width)
for row_index, row in enumerate(table.rows):
    date_cell = row.cells[6]
    source_cell = row.cells[0] if row_index == 0 else row.cells[3]
    date_tcpr = date_cell._tc.get_or_add_tcPr()
    source_tcpr = source_cell._tc.get_or_add_tcPr()
    for tag in ('w:shd', 'w:tcMar', 'w:tcBorders'):
        old = date_tcpr.find(qn(tag))
        if old is not None: date_tcpr.remove(old)
        src = source_tcpr.find(qn(tag))
        if src is not None: date_tcpr.append(deepcopy(src))
    date_cell.width = Cm(widths[6])
    date_cell.text = '觀察窗截止日\ncutoff_date' if row_index == 0 else CUTOFF
    date_cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    for p in date_cell.paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        for run in p.runs:
            run.font.name = 'Microsoft JhengHei'
            run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'), 'Microsoft JhengHei')
            run.font.size = Pt(9.5)
            if row_index == 0:
                run.bold = True
                run.font.color.rgb = RGBColor.from_string('FFFFFF')
            else:
                run.font.color.rgb = RGBColor.from_string('233746')

# Version metadata only; leave the R01 historical candidate and its receipts untouched.
work_id_hits = 0
for t in doc.tables:
    for row in t.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                for run in p.runs:
                    if OLD_ID in run.text:
                        run.text = run.text.replace(OLD_ID, NEW_ID)
                        work_id_hits += 1
                    if 'R01／' in run.text and '版本號' not in run.text:
                        # Change only the metadata run containing the old work ID's version prefix.
                        if 'SAMPLE-WRITER' in ''.join(r.text for r in p.runs):
                            run.text = run.text.replace('R01／', 'R02／')
if work_id_hits != 1:
    raise SystemExit(f'Expected one R01 work-ID run, updated {work_id_hits}.')
new_id_seen = any(NEW_ID in cell.text for t in doc.tables for row in t.rows for cell in row.cells)
if not new_id_seen:
    raise SystemExit('R02 work ID not present after targeted metadata patch.')
doc.core_properties.subject = '0107 / I18-E15 / R02 targeted observation cutoff date repair; SAMPLE-SYNTHETIC'
doc.save(R02_DOCX)

# Preserve provenance conflict without altering original raw receipts.
receipt_dir = R01 / 'review'
writer_receipts = {}
for fname in ('antigravity_writer_attempt02_dispatch_receipt.json', 'antigravity_revision_dispatch_receipt.json'):
    d = json.loads((receipt_dir / fname).read_text(encoding='utf-8'))
    writer_receipts[fname] = {k: d.get(k) for k in ('work_id', 'worker', 'requested_model', 'actual_model', 'conversation_id', 'result_status') if k in d}

# Deterministic verification: exact localized change plus existing arithmetic and sample controls.
base_doc = Document(R01_DOCX)
final_doc = Document(R02_DOCX)
with ZipFile(R02_DOCX) as z:
    zip_bad = z.testzip()
base_tables = base_doc.tables
final_tables = final_doc.tables
base_metrics = next(i for i,t in enumerate(base_tables) if t.rows and t.rows[0].cells[0].text.strip() == '指標名稱')
final_metrics = next(i for i,t in enumerate(final_tables) if t.rows and t.rows[0].cells[0].text.strip() == '指標名稱')
non_target_tables_equal = True
for ti, (bt, ft) in enumerate(zip(base_tables, final_tables)):
    if ti != base_metrics:
        b = [[c.text for c in row.cells] for row in bt.rows]
        f = [[c.text.replace('R02／' + NEW_ID, 'R01／' + OLD_ID) for c in row.cells] for row in ft.rows]
        if b != f: non_target_tables_equal = False
btab, ftab = base_tables[base_metrics], final_tables[final_metrics]
base_rows = [[c.text for c in row.cells] for row in btab.rows]
final_rows = [[c.text for c in row.cells] for row in ftab.rows]
normalized_final_rows = [r[:-1] for r in final_rows]
metrics_other_cells_unchanged = base_rows == normalized_final_rows
all_cutoff_cells = len(final_rows) == 5 and [r[6].strip() for r in final_rows[1:]] == [CUTOFF]*4
all_paragraphs_unchanged = [p.text for p in base_doc.paragraphs] == [p.text for p in final_doc.paragraphs]
text = '\n'.join([p.text for p in final_doc.paragraphs] + [c.text for t in final_doc.tables for row in t.rows for c in row.cells])
source = new_md_text
people = sorted(set(re.findall(r'\bSYN-P\d{2}\b', source)))
attempt_rows = re.findall(r'(?m)^\|\s*\d+\s*\|\s*`?SYN-P\d{2}`?\s*\|\s*\d+\s*\|', source)
body_small = [(p.style.name, r.font.size.pt) for p in final_doc.paragraphs if not (p.style and p.style.name.startswith('Heading')) for r in p.runs if r.text.strip() and r.font.size and r.font.size.pt < 10.5]
table_small = [(ti, r.font.size.pt) for ti,t in enumerate(final_doc.tables) for row in t.rows for c in row.cells for p in c.paragraphs for r in p.runs if r.text.strip() and r.font.size and r.font.size.pt < 9.5]
checks = {
 'docx_zip_integrity': zip_bad is None,
 'official_binding_doc_0107_i18_e15': '0107' in text and 'I18-E15' in text and '第 7 頁' in text,
 'sample_synthetic_and_real_boundary': 'SAMPLE' in text and 'SYNTHETIC' in text and 'UNKNOWN' in text and 'NOT_GRANTED' in text,
 'eight_synthetic_people': len(people) == 8,
 'seven_attempts': len(attempt_rows) == 7,
 'math_4_6_66_7': '4/6' in text and '66.7%' in text,
 'math_5_6_83_3': '5/6' in text and '83.3%' in text,
 'math_5_8_62_5': '5/8' in text and '62.5%' in text,
 'explicit_blueprint_cutoff_column_and_four_rows': len(ftab.columns) == 7 and all_cutoff_cells,
 'other_metric_cells_unchanged': metrics_other_cells_unchanged,
 'all_non_target_tables_unchanged': non_target_tables_equal,
 'all_body_paragraphs_unchanged': all_paragraphs_unchanged,
 'body_min_font_10_5pt': not body_small,
 'table_min_font_9_5pt': not table_small,
 'no_formal_acceptance_or_real_outcome_claim': 'NOT_GRANTED' in text and '非原始點協會' in text,
}
if not all(checks.values()):
    failed = [k for k,v in checks.items() if not v]
    raise SystemExit('R02 deterministic QA failed: ' + ', '.join(failed))

# Capture current native renderer lane evidence without launching Word or another renderer.
ps_cmd = "Get-CimInstance Win32_Process | Where-Object { $_.ProcessId -in @(66060,70808,15600) } | Select-Object ProcessId,ParentProcessId,Name,CommandLine | ConvertTo-Json -Compress"
try:
    pr = subprocess.run(['powershell.exe','-NoProfile','-Command',ps_cmd],capture_output=True,text=True,timeout=15)
    process_snapshot = pr.stdout.strip() if pr.returncode == 0 else 'UNKNOWN_POWERSHELL_QUERY_FAILED'
except Exception as e:
    process_snapshot = 'UNKNOWN_' + type(e).__name__

review_raw = receipt_dir / 'opencode_semantic_review_0107_R01_raw_response.txt'
review_sha = sha_file(review_raw) if review_raw.exists() else 'UNKNOWN'
old_id_conflict = {
 'dispatch_work_id': writer_receipts.get('antigravity_writer_attempt02_dispatch_receipt.json', {}).get('work_id'),
 'revision_work_id': writer_receipts.get('antigravity_revision_dispatch_receipt.json', {}).get('work_id'),
 'shared_conversation_id': writer_receipts.get('antigravity_revision_dispatch_receipt.json', {}).get('conversation_id'),
 'resolution': 'Preserve both immutable raw receipts; do not assert which suffix owns both calls. R02 receives a fresh unique work ID.'
}
write_json(R02/'evidence/repair_receipt_0107_R01_to_R02.json', {
 'doc_id':'0107','requirement_id':'I18-E15','requirement_page':7,'internal_blueprint_index':116,
 'source_commit':SOURCE_COMMIT,'blueprint_blob':'8c2bbe7ca9dcbb03088a48934b9e57e7147ede63','crosswalk_blob':'ee3fc17e4e0e89a5b5d404c6f0ca7bd92a1a4f9b',
 'official_pdf_sha256':'805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709',
 'base_candidate_sha256':OLD_SHA,'new_candidate_sha256':sha_file(R02_DOCX),'base_source_sha256':sha_file(R01_MD),'new_source_sha256':sha_file(R02_MD),
 'review_finding_addressed':'Blueprint 5.D requires a cutoff date in the three-metric recomputation table; R01 had the 90-day window in the cohort card and narrative but no explicit cutoff-date column in the table.',
 'localized_change':'Added an explicit 觀察窗截止日 / cutoff_date final column to the metrics table and populated 2026-07-29 for metrics A, B, C and the attempt-count reference row. Updated visible candidate version/work ID to R02.',
 'date_basis':'SAMPLE cohort completion 2026-04-30; 90-day observation window is 2026-05-01 through 2026-07-29 inclusive, as stated in the existing cohort card and attempt table.',
 'no_change':'No results, numerator/denominator sets, formulas, synthetic records, other tables, body paragraphs, or REAL evidence claims changed.',
 'technical_comparison':{'metrics_non_date_cells_unchanged':metrics_other_cells_unchanged,'all_other_tables_unchanged':non_target_tables_equal,'all_paragraphs_unchanged':all_paragraphs_unchanged},
 'antigravity_work_id_reconciliation':old_id_conflict,
 'r01_independent_review':{'verdict':'PASS_TEXT_SEMANTIC_ONLY','candidate_sha256':OLD_SHA,'review_raw_response_sha256':review_sha,'scope':'text-only; no binary/page visual inspection; two LOW findings, one corrected here; one receipt-ID inconsistency is preserved as provenance.'},
 'visual_state':'BLOCKED_RENDERER_LANE_ONLY; no extra WINWORD process launched. Current process snapshot: '+process_snapshot,
 'formal_acceptance':'NOT_GRANTED','created_at_local':datetime.now().astimezone().isoformat(timespec='seconds')
})
write_json(R02/'evidence/technical_qa_receipt_0107_R02.json', {
 'doc_id':'0107','requirement_id':'I18-E15','candidate_sha256':sha_file(R02_DOCX),'candidate_bytes':R02_DOCX.stat().st_size,
 'source_manuscript_sha256':sha_file(R02_MD),'source_commit':SOURCE_COMMIT,'checks':checks,
 'synthetic_people_ids':people,'exam_attempt_rows':len(attempt_rows),'metrics_rows_with_cutoff_date':4,'cutoff_date':'2026-07-29',
 'formulae':{'first_pass':'4/6=66.7%','pass_by_cutoff_exam_takers':'5/6=83.3%','pass_by_cutoff_full_cohort':'5/8=62.5%'},
 'visual_render':'BLOCKED_RENDERER_LANE_ONLY; not attempted to avoid competing with the active 0102 Word COM export. Packaged LibreOffice renderer previously failed because soffice.exe unavailable.',
 'active_process_snapshot':process_snapshot,'independent_semantic_review':'PENDING_R02_EXACT_SHA_DELTA_REVIEW','formal_acceptance':'NOT_GRANTED',
 'checked_at_local':datetime.now().astimezone().isoformat(timespec='seconds')
})
write_json(R02/'evidence/docx_build_receipt_0107_R02.json', {
 'doc_id':'0107','requirement_id':'I18-E15','official_pdf_page':7,'internal_blueprint_index':116,'source_commit':SOURCE_COMMIT,
 'source_blobs':{'157_blueprints':'8c2bbe7ca9dcbb03088a48934b9e57e7147ede63','checkbox_crosswalk':'ee3fc17e4e0e89a5b5d404c6f0ca7bd92a1a4f9b','official_pdf_raw_sha256':'805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709'},
 'base_candidate_sha256':OLD_SHA,'candidate_path':str(R02_DOCX.relative_to(REPO)).replace('\\','/'),'candidate_sha256':sha_file(R02_DOCX),'candidate_bytes':R02_DOCX.stat().st_size,
 'authoring':'Deterministic narrow python-docx OOXML patch of R01; no substantive content regeneration.',
 'change_scope':['appended one explicit observation cutoff date column to metric recomputation table while preserving all original columns','updated visible version/work ID to R02'],
 'unchanged_scope':['all other table cell content','all body paragraphs','all formulas and synthetic rows','SAMPLE/REAL boundary'],
 'state':'CANDIDATE_NOT_FORMALLY_ACCEPTED','built_at_local':datetime.now().astimezone().isoformat(timespec='seconds')
})

# Extract a text snapshot and bounded delta-review packet bound to the exact R02 SHA.
text_snapshot = '\n'.join([p.text for p in final_doc.paragraphs] + ['\n'.join(c.text for c in row.cells) for t in final_doc.tables for row in t.rows]) + '\n'
snapshot_path = R02/'review/candidate_text_0107_R02.txt'
snapshot_path.write_text(text_snapshot, encoding='utf-8', newline='\n')
packet = f'''# 0107 / I18-E15 exact-SHA delta review request

Review type: independent semantic delta review. Do not claim binary/page visual inspection; do not claim formal acceptance.

## Artifact binding
- R02 candidate: `{str(R02_DOCX.relative_to(REPO)).replace(chr(92), '/')}`
- DOCX SHA-256: `{sha_file(R02_DOCX)}`
- Extracted text snapshot SHA-256: `{sha_file(snapshot_path)}`
- Prior exact-SHA candidate R01: `{OLD_SHA}`
- Prior independent response SHA-256: `{review_sha}` (raw response retained under the R01 review directory)
- Requirement: DOCX 0107 = I18-E15, official source PDF p.7; internal Blueprint index 116.

## Inherited review and exact delta
R01 received `PASS_TEXT_SEMANTIC_ONLY`; the reviewer explicitly did not inspect DOCX binary or rendered pages. R01's only content finding was that the three-metric recomputation table omitted the explicit cutoff-date field required by Unique Blueprint §5.D. R02 adds the column `觀察窗截止日 / cutoff_date` as the seventh/final metrics-table column, populated `2026-07-29` for indicators A/B/C and the 7-attempt reference row. This date is already established by the SAMPLE cohort card: completion date 2026-04-30; inclusive 90-day observation window 2026-05-01 through 2026-07-29.

The visible version/work ID changes to R02. Separate provenance evidence documents that the R01 Antigravity dispatch receipt used suffix `...-03`, while the targeted revision receipt and manuscript used `...-02`; both receipts are preserved, and no source receipt was rewritten.

Deterministic comparison confirms all non-date metric cells, all other table cells, and all body paragraphs are unchanged from R01. Please review the complete extracted text snapshot as the exact R02 content, verify the changed locus against Blueprint §5.D, independently recompute any related logic, and return PASS / PARTIAL / FAIL with text locators. Inherited R01 verdict is reusable only for unchanged content. Page layout remains separately pending.

## Exact R02 text snapshot follows

{text_snapshot}
'''
packet_path=R02/'review/independent_semantic_delta_review_packet_0107_R02.md'
packet_path.write_text(packet,encoding='utf-8',newline='\n')
write_json(R02/'evidence/packet_manifest_0107_R02.json',{
 'doc_id':'0107','requirement_id':'I18-E15','candidate_sha256':sha_file(R02_DOCX),
 'text_snapshot_path':str(snapshot_path.relative_to(REPO)).replace('\\','/'),'text_snapshot_sha256':sha_file(snapshot_path),
 'review_packet_path':str(packet_path.relative_to(REPO)).replace('\\','/'),'review_packet_sha256':sha_file(packet_path),
 'prior_review_response_sha256':review_sha,'review_scope':'semantic delta exact R02 SHA; inherited semantic verdict for unchanged content only; visual QA separate.'
})
readme = f'''# DOCX 0107 — I18-E15 — R02 candidate

- Official purpose: high certificate pass-rate evidence with traceable source records (official source PDF p.7; unique Blueprint internal index 116).
- Candidate SHA-256: `{sha_file(R02_DOCX)}`.
- R02 repairs the explicit cutoff-date column required by Blueprint §5.D. The SAMPLE cutoff is 2026-07-29; all values remain SYNTHETIC.
- Technical/data comparison: `evidence/technical_qa_receipt_0107_R02.json`.
- R01 prior exact-SHA semantic response and raw dispatch evidence are retained in the sibling R01 package; R02 delta packet is under `review/`.
- Visual inspection: pending; no second Word process was started while 0102 COM export was active, and the bundled LibreOffice renderer lacks `soffice.exe`.
- State: CANDIDATE, not formally accepted. REAL evidence remains UNKNOWN; association approval NOT_GRANTED.
'''
(R02/'README.md').write_text(readme,encoding='utf-8',newline='\n')
# Keep the reproducible patcher as an audit artifact.
script_dst=R02/'evidence/scripts/patch_0107_R02_cutoff_column.py'
script_dst.write_bytes(Path(__file__).read_bytes())
print(json.dumps({'candidate':str(R02_DOCX),'sha256':sha_file(R02_DOCX),'bytes':R02_DOCX.stat().st_size,'source_sha256':sha_file(R02_MD),'qa':checks,'technical_qa':'PASS' if all(checks.values()) else 'FAIL','text_snapshot_sha256':sha_file(snapshot_path),'review_packet_sha256':sha_file(packet_path),'work_id_reconciliation':old_id_conflict,'status':'CANDIDATE_NOT_FORMALLY_ACCEPTED'},ensure_ascii=False,indent=2))