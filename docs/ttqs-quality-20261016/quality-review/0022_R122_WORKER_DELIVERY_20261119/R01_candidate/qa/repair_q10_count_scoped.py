from pathlib import Path
from docx import Document
import hashlib, json, shutil, datetime
root = Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORKTREES\R122_DELIVERY_20261118B\docs\ttqs-quality-20261016\quality-review\0022_R122_WORKER_DELIVERY_20261119\R01_candidate')
docx = root / '0022_I04-E01_R01.docx'
qa = root / 'qa'
backup = qa / '0022_I04-E01_R01_PRE_Q10_COUNT_FIX.docx'
receipt = qa / 'q10_count_scoped_repair_receipt.json'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest().upper()
assert docx.is_file(), docx
before_sha = sha(docx)
assert before_sha == 'BA3650445179F50FCE75E5F9EEFDFAAD813DC6978B40D80BEE201FA3CD2A8C3D', before_sha
assert not backup.exists(), f'backup exists; refusing overwrite: {backup}'
doc = Document(str(docx))
assert len(doc.tables) > 9
assert doc.tables[6].rows[2].cells[1].text.strip() == '0', doc.tables[6].rows[2].cells[1].text
assert doc.tables[9].rows[2].cells[4].text.strip() == '1', doc.tables[9].rows[2].cells[4].text
cell = doc.tables[9].rows[2].cells[4]
paragraphs = cell.paragraphs
assert len(paragraphs) == 1 and len(paragraphs[0].runs) == 2, (len(paragraphs), [len(p.runs) for p in paragraphs])
assert [r.text for r in paragraphs[0].runs] == ['', '1'], [r.text for r in paragraphs[0].runs]
run = paragraphs[0].runs[1]
assert run.text == '1', repr(run.text)
shutil.copy2(docx, backup)
backup_sha = sha(backup)
run.text = '0'
doc.save(str(docx))
new_sha = sha(docx)
check = Document(str(docx))
assert check.tables[9].rows[2].cells[4].text.strip() == '0'
assert check.tables[6].rows[2].cells[1].text.strip() == '0'
# Verify all table cell text changes are limited to the authorized cell.
orig = Document(str(backup))
changes=[]
assert len(orig.tables)==len(check.tables)
for ti,(a,b) in enumerate(zip(orig.tables,check.tables)):
    assert len(a.rows)==len(b.rows)
    for ri,(ar,br) in enumerate(zip(a.rows,b.rows)):
        assert len(ar.cells)==len(br.cells)
        for ci,(ac,bc) in enumerate(zip(ar.cells,br.cells)):
            if ac.text != bc.text:
                changes.append({'table':ti,'row':ri,'cell':ci,'before':ac.text,'after':bc.text})
assert changes == [{'table':9,'row':2,'cell':4,'before':'1','after':'0'}], changes
# Confirm unchanged synthetic source totals still add to 6 and displayed distribution agrees.
register = check.tables[6]
counts = [int(register.rows[i].cells[1].text.strip()) for i in range(1,7)]
assert counts == [2,0,1,1,1,1], counts
assert sum(counts)==6
row = check.tables[9].rows[2]
assert row.cells[4].text.strip() == '0'
obj={
 'schema':'TTQS_ONE_SCOPED_QA_REPAIR_V1','doc_id':'0022','requirement_id':'I04-E01',
 'work_id':'TTQS_ONE_0022_I04-E01_R01_Q10_COUNT_SCOPED_REPAIR_20261119',
 'observed_at_local':datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
 'before_candidate_sha256':before_sha,'backup_path':str(backup),'backup_sha256':backup_sha,
 'after_candidate_sha256':new_sha,'edit_scope':'table[9].row[2].cell[4]: 1 -> 0',
 'supporting_exact_source':'table[6].row[2].cell[1] == 0; synthetic register counts [2,0,1,1,1,1], sum 6',
 'text_change_diff':changes,'deterministic_result':'PASS','semantic_visual_recheck_required':True}
receipt.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(obj,ensure_ascii=True,indent=2))

