from pathlib import Path
import json,hashlib,re
pkg=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022')
src_path=pkg/'writer/opencode_writer_manuscript_0104_R15_patched.md'; resp_path=pkg/'writer/opencode_writer_R16_response.md'; packet_path=pkg/'writer/TASK_PACKET_0104_R16_BOUNDED_REPAIR.md'
src=src_path.read_text(encoding='utf-8-sig'); obj=json.loads(resp_path.read_text(encoding='utf-8-sig'))
assert obj['work_id']=='TTQS-0104-I18-E11-R16-BOUNDED-REPAIR-20261022'
assert obj['input_candidate_sha256']=='9bbb96da74ba9da845ab0e063421d04f035e79496209a02de1f04b0c98ec7eb8'
assert obj['checks']['changed_math'] is False and obj['checks']['changed_real_claims'] is False and obj['checks']['introduced_i18_e12_claim'] is False
assert set(obj['checks']['addressed_findings'])=={f'RF-{i}' for i in range(1,11)}
cur=src; applied=[]
for p in obj['patches']:
 if 'find_exactly' in p:
  a=p['find_exactly'];n=cur.count(a)
  if n!=p.get('expected_matches',1):raise SystemExit(f"exact replacement mismatch {p['finding']}: {n} {a[:100]!r}")
  cur=cur.replace(a,p['replace_with'],1)
 else:
  a=p['insert_after_exactly'];n=cur.count(a)
  if n!=p.get('expected_matches',1):raise SystemExit(f"exact insertion mismatch {p['finding']}: {n} {a[:100]!r}")
  cur=cur.replace(a,a+'\n'+'\n'.join(p.get('insert_rows',[])),1)
 applied.append(p['finding'])
# Deterministic correction: the worker claimed the F-GP locators were synchronized, but its JSON had no such replacement. Align all five exact keys with the new T-13 row IDs.
locator_targets={
'F-GP-01':('row 1','D-1'),'F-GP-02':('row 2','D-3'),'F-GP-03':('row 3','D-2'),'F-GP-04':('row 4','M-1'),'F-GP-05':('row 5','M-2')}
for key,(old,new) in locator_targets.items():
 pat=re.compile(r'(\| '+re.escape(key)+r' \|[^\n]*\| )§12/T-13 '+re.escape(old)+r'( \|)')
 cur,n=pat.subn(lambda m:m.group(1)+'§12/T-13 '+new+m.group(2),cur,count=1)
 if n!=1:raise SystemExit(f'locator correction failed for {key}: {n}')
# Clarify tie handling for positive-margin monitoring rows as well as deficit rows.
old='差距相同時，先以「是否直接影響對外佐證」優先，再依四段乘法鏈順序（申請→到考→通過→簽發查證）決定。達標之正差距不佔缺口次序，另列 M 列並依正差距由小到大排序（M-1→M-2）；'
new='D 列同差距時，先以「是否直接影響對外佐證」優先，再依四段乘法鏈順序（申請→到考→通過→簽發查證）決定。達標之正差距不佔缺口次序，另列 M 列並依正差距由小到大排序（M-1→M-2）；M 列同正差距時亦依四段乘法鏈順序排列。'
if cur.count(old)!=1:raise SystemExit('T-13 tie-rule anchor mismatch')
cur=cur.replace(old,new,1)
old_version='| 版本 | R15（SAMPLE／SYNTHETIC 候選工作版） |';new_version='| 版本 | R16（SAMPLE／SYNTHETIC 候選工作版） |'
if cur.count(old_version)!=1:raise SystemExit('version anchor mismatch')
cur=cur.replace(old_version,new_version,1)
# Invariant checks: 121 existing fact rows plus exactly three new keys.
key_rows=re.findall(r'^\| (F-[A-Z0-9-]+) \|',cur,re.M)
if len(key_rows)!=124 or len(set(key_rows))!=124:raise SystemExit(f'register fact-row count/uniqueness failed rows={len(key_rows)} unique={len(set(key_rows))}')
for k in ('F-CHAIN-A','F-CHAIN-B','F-RET-01','F-GP-01','F-GP-02','F-GP-03','F-GP-04','F-GP-05'):
 if f'| {k} |' not in cur:raise SystemExit(f'missing key {k}')
# Confirm version and no stale locator labels remain.
for bad in ('§12/T-13 row 1','§12/T-13 row 2','§12/T-13 row 3','§12/T-13 row 4','§12/T-13 row 5'):
 if bad in cur:raise SystemExit('stale locator remains: '+bad)
assert 'F-SR-07 | SRC-C1 SAMPLE 未成班控制紀錄' in cur
assert 'I18-E12' not in cur
out=pkg/'writer/opencode_writer_manuscript_0104_R16_patched.md';out.write_text(cur,encoding='utf-8')
receipt={'receipt_id':'TTQS-0104-R15-TO-R16-PATCH-APPLICATION','work_id':obj['work_id'],'input_candidate_sha256':obj['input_candidate_sha256'],'input_manuscript_sha256':hashlib.sha256(src_path.read_bytes()).hexdigest(),'worker_response_sha256':hashlib.sha256(resp_path.read_bytes()).hexdigest(),'worker_patch_count':len(obj['patches']),'worker_findings_claimed':obj['checks']['addressed_findings'],'worker_patch_anchor_validation':'ALL 19 exact anchors matched exactly once','deterministic_codex_corrections':['F-GP-01..05 locators changed to D-1,D-3,D-2,M-1,M-2; the worker narrative claimed this but its patch array omitted these edits.','T-13 tie rule extended to M-row ties.','Version row changed R15 to R16.'],'register_row_count_input':121,'register_row_count_output':124,'new_keys':['F-CHAIN-A','F-CHAIN-B','F-RET-01'],'unique_register_keys':len(set(key_rows)),'output_path':str(out),'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'output_bytes':out.stat().st_size,'source_values_changed_by_deterministic_patch':False,'formal_acceptance':'NOT_GRANTED'}
(pkg/'writer/opencode_patch_application_receipt_R16.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('worker_patch_count',len(obj['patches']),'manual_corrections',len(receipt['deterministic_codex_corrections']),'register_rows',len(key_rows),'sha256',receipt['output_sha256'])
