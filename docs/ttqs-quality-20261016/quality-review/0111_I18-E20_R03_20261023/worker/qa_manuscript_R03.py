from pathlib import Path
import hashlib,json,re,datetime
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0111_I18-E20_SOURCE_PREP_20261023')
p=root/'manuscript'/'0111_I18-E20_特殊績效及社會面成果證據登錄表_R03.md'
s=p.read_text(encoding='utf-8')
checks=[]
def add(name,ok,detail): checks.append({'check':name,'pass':bool(ok),'detail':detail})
def table(n):
    cap=re.search(rf'(?m)^\*\*表 {n} ',s)
    if not cap: return None,None
    lines=s[cap.start():].splitlines()
    hi=next((i for i,x in enumerate(lines) if x.startswith('| ')),None)
    if hi is None or hi+1>=len(lines): return None,None
    cells=lambda line:[x.strip() for x in line.strip().strip('|').split('|')]
    headers=cells(lines[hi]); rows=[]
    for line in lines[hi+2:]:
        if not line.startswith('|'): break
        row=cells(line)
        if len(row)!=len(headers): return headers,('MALFORMED_ROW',len(row),line)
        rows.append(dict(zip(headers,row)))
    return headers,rows
sha=lambda b: hashlib.sha256(b).hexdigest()
add('doc_requirement_binding','0111／I18-E20' in s and '提出目標客戶及學員對訓練達特殊績效之說明（社會面、其他）。' in s,'Official text and exact doc/requirement pair present; serial remains unasserted in source receipt.')
nums=[int(x) for x in re.findall(r'(?m)^\*\*表 (\d+)(?:\s|[-（])',s)]
add('numbered_tables_1_to_16',nums==list(range(1,17)),str(nums))
old_refs=re.findall(r'表\s*\d+\s*-\s*\d+',s)
add('no_stale_subtable_references',not old_refs,','.join(old_refs))
refnums=[int(x) for x in re.findall(r'表\s*(\d+)',s)]
add('table_references_resolve',all(1<=x<=16 for x in refnums),f'{len(refnums)} table references; all within captions 1–16')
for n in range(1,17):
    h,rows=table(n); add(f'table_{n}_nonempty',bool(h) and isinstance(rows,list) and len(rows)>0,f'headers={len(h) if h else 0}; rows={len(rows) if isinstance(rows,list) else rows}')
for n,prefix in [(7,'TC'),(8,'L')]:
    h,rows=table(n)
    ok=isinstance(rows,list) and len(rows)==8 and '示範同意（非實際文件）' in h and all(r.get('示範同意（非實際文件）')=='SAMPLE假設同意：是' for r in rows)
    add(f'table_{n}_{prefix}_rows_and_consent',ok,f'rows={len(rows) if isinstance(rows,list) else rows}; consent column present and SAMPLE-only')
h7,r7=table(7); h8,r8=table(8)
if isinstance(r7,list):
    t0=sum(int(r['T0']) for r in r7);t1=sum(int(r['T1']) for r in r7)
else:t0=t1=None
if isinstance(r8,list): learner=sum(int(r['正向']) for r in r8)
else: learner=None
add('TC_arithmetic_3_of_8_to_6_of_8',t0==3 and t1==6 and len(r7)==8,f'T0={t0}/8; T1={t1}/8; delta={(t1-t0) if t0 is not None else None}/8=37.5pp')
add('learner_arithmetic_6_of_8',learner==6 and len(r8)==8,f'{learner}/8=75.0%')
add('displayed_math_and_claim_boundary','3/8' in s and '6/8' in s and '37.5 個百分點' in s and '0/2＝0.0%' in s and '不能推論訓練造成改變' in s,'Expected rates, original acquisition denominator, and non-causal limit present.')
h14,r14=table(14)
keys=[r.get('鍵','') for r in r14] if isinstance(r14,list) else []
expected=[f'SYN-0111-{i:03}' for i in range(1,54)]
add('replacement_register_53_keys',keys==expected,f'rows={len(keys)}; sequential={keys==expected}')
add('replacement_register_has_locations_and_replacement',isinstance(r14,list) and all(r.get('定位（章／表／欄）') and r.get('真實替換證據（最低）') and r.get('責任') for r in r14),'Every registered synthetic key has locator, real replacement evidence and role.')
add('consent_nonreal_boundary','16/16 SAMPLE 假設同意；不是實際同意文件' in s and '沒有同意書' in s and 'REAL同意' in s,'Synthetic consent values are explicitly not real consents.')
add('D4_no_fabricated_file','D4 同意／原件控制：只以表 7–8' in s and '本件沒有同意書、原件檔或真實來源路徑' in s,'D4 is modeled as an unprovided source, not an asserted file.')
add('E3_not_misrepresented','尚須符合本列全部條件；本示範未取得' in s and 'REAL＝E0／HOLD' in s,'E3 is unmet; real evidence remains E0/HOLD.')
add('neighbor_rejection','0110（I18-E19）' in s and '0112（I18-E21）' in s,'Distinct adjacent requirement IDs and boundaries included.')
add('SAMPLE_only_overall','SAMPLE / SYNTHETIC — NOT ASSOCIATION REAL PERFORMANCE' in s and '正式驗收：未授予（HOLD）' in s,'Sample/real and formal acceptance boundary preserved.')
add('font_floor',('10.5pt' in s and '9.5pt' in s),'Both explicit font minima are present for the subsequent DOCX build.')
add('no_control_characters',not any(ord(c)<32 and c not in '\r\n\t' for c in s),'No disallowed control chars in manuscript.')
receipt={'work_id':'TTQS-0111-I18-E20-MANUSCRIPT-QA-R03-20261023','doc_id':'0111','requirement_id':'I18-E20','official_checkbox_serial':'UNKNOWN_NOT_ASSERTED','manuscript_sha256':sha(p.read_bytes()),'manuscript_bytes':p.stat().st_size,'checks':checks,'deterministic_result':'PASS' if all(x['pass'] for x in checks) else 'FAIL','scope':'Deterministic manuscript structure, mapping, sample arithmetic, consent/REAL boundaries, registration completeness, and cross-reference checks only. Not an independent semantic review and not DOCX visual QA.','observed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
out=root/'evidence'/'manuscript_qa_0111_R03.json';out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'result':receipt['deterministic_result'],'failed':[x for x in checks if not x['pass']],'receipt':str(out),'manuscript_sha256':receipt['manuscript_sha256']},ensure_ascii=False))