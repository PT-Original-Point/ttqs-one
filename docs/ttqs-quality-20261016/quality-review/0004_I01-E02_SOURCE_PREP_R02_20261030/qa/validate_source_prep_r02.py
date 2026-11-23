from pathlib import Path

import csv,json,hashlib,collections,datetime

base=Path(__file__).resolve().parents[1]

rt=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME')

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def checkfile(p,expected): return p.is_file() and sha(p)==expected

manifest_path=base/'SOURCE_PREP_MANIFEST_0004_R02.json'

m=json.loads(manifest_path.read_text(encoding='utf-8'))

qa={

 'project_id':'TTQS_ONE','doc_id':'0004','requirement_id':'I01-E02','revision':'SOURCE_PREP_R02',

 'status':'PASS_SOURCE_PREP_CANDIDATE_NOT_DOCX','checks':{},'failures':[],

 'stage':'SOURCE_PREPARATION_ONLY','formal_acceptance':'NOT_GRANTED','docx_built':False,

 'real_execution_status':'UNKNOWN','independent_semantic_review':'NOT_APPLICABLE_TO_SOURCE_PREP'

}

def ck(name,ok,details=None):

 qa['checks'][name]=bool(ok)

 if not ok: qa['failures'].append(name)

 if details is not None: qa.setdefault('details',{})[name]=details

packet=base/'SOURCE_PACKET_0004_I01-E02_R02.md'

blueprint=base/'UNIQUE_BLUEPRINT_0004_I01-E02_R02.md'

plan=base/'SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R02.csv'

current=rt/'CONTROL'/'BLUEPRINT_CURRENT.jsonl'

rowcopy=base/'source'/'BLUEPRINT_CURRENT_ROW_0004.jsonl'

reg3=rt/'WORK'/'QUALITY_REBUILD_20261016'/'0003_I01-E02_R17_20261030'/'source'/'SYNTHETIC_REPLACEMENT_REGISTER_0003_R17.csv'

pkt3=rt/'WORK'/'QUALITY_REBUILD_20261016'/'0003_I01-E02_R17_20261030'/'source'/'SOURCE_PACKET_0003_I01-E02_R17.md'

doc3=rt/'WORK'/'QUALITY_REBUILD_20261016'/'0003_I01-E02_R17_20261030'/'candidate'/'0003_I01-E02_R17.docx'

manifest3=rt/'WORK'/'QUALITY_REBUILD_20261016'/'0003_I01-E02_R17_20261030'/'qa'/'CANDIDATE_EVIDENCE_MANIFEST_R17.json'

semantic3=rt/'WORK'/'QUALITY_REBUILD_20261016'/'0003_I01-E02_R17_20261030'/'qa'/'SEMANTIC_REVIEW_R17_METADATA_CLEAN.json'

oldm_path=rt/'WORK'/'QUALITY_REBUILD_20261016'/'0004_I01-E02_SOURCE_PREP_R01_20261029'/'SOURCE_PREP_MANIFEST_0004_R01.json'

# Current official requirement, project crosswalk and Blueprint source hashes.

official=rt/'INPUTS'/'R04'/'06_OFFICIAL_SOURCES'/'TTQS查核佐證文件資料表-訓練機構版 (2).pdf'

crosswalk=rt/'CONTROL'/'TTQS_ONE_129_REQUIREMENT_TO_142_DELIVERABLE_CROSSWALK_R01.csv'

ck('official_requirement_hash_matches',sha(official)==m['source_checks']['official_pdf_r04']['sha256'],sha(official))

ck('crosswalk_hash_matches',sha(crosswalk)==m['source_checks']['crosswalk']['sha256'],sha(crosswalk))
ck('packaged_official_pdf_matches',sha(base/'source'/'official_requirement.pdf')==m['source_checks']['official_pdf_r04']['sha256'])
ck('packaged_crosswalk_matches',sha(base/'source'/'crosswalk_129_to_142.csv')==m['source_checks']['crosswalk']['sha256'])
ck('packaged_source_reconciliation_matches',sha(base/'source'/'requirement_source_reconciliation.csv')==m['source_checks']['requirement_source_reconciliation']['sha256'])

ck('blueprint_current_file_hash_matches',sha(current)==m['source_checks']['blueprint_current']['sha256'],sha(current))

rows=[json.loads(line) for line in current.read_text(encoding='utf-8-sig').splitlines() if line.strip()]

row=next((x for x in rows if str(x.get('deliverable_id'))=='0004'),None)

copyrow=json.loads(rowcopy.read_text(encoding='utf-8-sig'))

canonical=lambda x: json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')

raw=json.dumps(row,ensure_ascii=False,separators=(',',':')).encode('utf-8') if row is not None else b''

ck('current_0004_blueprint_row_found',row is not None)

ck('exported_row_equals_current_row',row==copyrow)

ck('blueprint_raw_row_sha_matches_manifest',hashlib.sha256(raw).hexdigest()==m['blueprint_current_row']['raw_json_without_line_ending_sha256'])

ck('blueprint_canonical_row_sha_matches_manifest',hashlib.sha256(canonical(row)).hexdigest()==m['blueprint_current_row']['canonical_json_sha256'])

ck('source_packet_identity_correct',all(x in packet.read_text(encoding='utf-8') for x in ['doc_id=0004','requirement_id=I01-E02','157 項次 `002`']))

bs=blueprint.read_text(encoding='utf-8')

ck('unique_blueprint_revision_and_packet_link_correct','Unique Blueprint R02' in bs and 'SOURCE_PACKET_0004_I01-E02_R02.md' in bs and 'R01.md' not in bs)

# Rebind the explicitly shared synthetic reference to the current 0003 evidence.

dep=m['0003_dependency']

ck('0003_candidate_sha_current',sha(doc3)==dep['candidate_docx_sha256'])

ck('0003_register_sha_current',sha(reg3)==dep['register_sha256'])

ck('0003_source_packet_sha_current',sha(pkt3)==dep['source_packet_sha256'])

ck('0003_manifest_sha_current',sha(manifest3)==dep['candidate_evidence_manifest_sha256'])

ck('0003_semantic_receipt_sha_current',sha(semantic3)==dep['semantic_review_receipt_sha256'])

with reg3.open(encoding='utf-8-sig',newline='') as f: r3=list(csv.DictReader(f))

valmap={r.get('fact_id'):r.get('synthetic_value') for r in r3}

ck('shared_sample_date_matches',valmap.get('SYN-001')==dep['verified_current_values']['SYN-001']=='2026-10-28')

ck('shared_response_code_matches',valmap.get('SYN-002')==dep['verified_current_values']['SYN-002']=='SYN-0003-001')

# Detect stale 0003 dependency hash from preserved R01 source-prep evidence.

oldm=json.loads(oldm_path.read_text(encoding='utf-8'))

oldhash=oldm.get('0003_dependency',{}).get('register_sha256') or oldm.get('source_checks',{}).get('replacement_register',{}).get('sha256')

texts=[packet.read_text(encoding='utf-8'),blueprint.read_text(encoding='utf-8'),plan.read_text(encoding='utf-8-sig'),manifest_path.read_text(encoding='utf-8')]

ck('old_0003_hash_absent_from_r02_sources',bool(oldhash) and all(oldhash not in t for t in texts),oldhash)

with plan.open(encoding='utf-8-sig',newline='') as f: facts=list(csv.DictReader(f))

counts=collections.Counter(r.get('status','') for r in facts)

allowed={'SAMPLE_SYNTHETIC_ONLY','PROPOSED_RULE_NOT_REAL_POLICY','UNKNOWN_REAL_SOURCE','SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE'}

ck('register_fact_count_84',len(facts)==84)

ck('register_fact_ids_unique_and_nonempty',len({r.get('fact_id','') for r in facts})==84 and all(r.get('fact_id') for r in facts))

ck('register_status_taxonomy_complete',set(counts).issubset(allowed) and set(counts)==allowed,dict(counts))

proposed=[r for r in facts if r['status']=='PROPOSED_RULE_NOT_REAL_POLICY']

unknown=[r for r in facts if r['status']=='UNKNOWN_REAL_SOURCE']

shared=[r for r in facts if r['status']=='SHARED_SAMPLE_REFERENCE_NOT_ACCEPTANCE']

sample=[r for r in facts if r['status']=='SAMPLE_SYNTHETIC_ONLY']

ck('proposed_rules_explicitly_not_real_policy',len(proposed)==2 and all(r['value_type']=='proposed rule' and ('confirm' in r['source_basis'].lower() or 'sample-only' in r['source_basis'].lower()) for r in proposed))

ck('unknown_real_sources_remain_unknown',len(unknown)==6 and all(r['value_type'].startswith('unknown') and (r['synthetic_value']=='UNKNOWN' or 'No retention period specified' in r['synthetic_value']) for r in unknown))

ck('shared_sample_references_not_acceptance',len(shared)==2 and all(r['value_type']=='shared synthetic reference' for r in shared))

ck('synthetic_facts_have_fact_ids',len(sample)==74 and all(r['fact_id'] and r['synthetic_value'] for r in sample))

# Ensure the changed R02 files exactly match the source-prep manifest.

for name in ['SOURCE_PACKET_0004_I01-E02_R02.md', 'UNIQUE_BLUEPRINT_0004_I01-E02_R02.md', 'SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R02.csv', 'source/BLUEPRINT_CURRENT_ROW_0004.jsonl', 'source/official_evidence_table_p1.png', 'source/official_requirement.pdf', 'source/crosswalk_129_to_142.csv', 'source/requirement_source_reconciliation.csv']:

 f=base/name

 entry=next((x for x in m['outputs'] if x['path']==name),None)

 ck('manifest_output:'+name,f.is_file() and entry is not None and f.stat().st_size==entry['bytes'] and sha(f)==entry['sha256'])
ck('manifest_output_paths_unique',len([x['path'] for x in m['outputs']])==len(set(x['path'] for x in m['outputs'])))

# Recompute all flow equations and displayed rates from the recorded integers.

a=m['sample_arithmetic']['counts']; rates=m['sample_arithmetic']['rates']

checks={

 'screening':a['screened']==a['ineligible']+a['eligible_invites'],

 'invites':a['eligible_invites']==a['unique_returns']+a['refusal']+a['no_response'],

 'returns':a['unique_returns']==a['valid']+a['invalid'],

 'receipt_events':a['raw_receipt_events']==a['unique_returns']+a['duplicate_extra']}

for key,val in checks.items(): ck('arithmetic_'+key,val,a)

expected={'response_rate':f"{a['unique_returns']}/{a['eligible_invites']}=50.0%",'effective_rate':f"{a['valid']}/{a['unique_returns']}=50.0%",'valid_yield':f"{a['valid']}/{a['eligible_invites']}=25.0%",'eligibility_pass_rate':f"{a['eligible_invites']}/{a['screened']}=80.0%"}

ck('displayed_rates_match_recomputed_values',rates==expected,rates)

ck('no_docx_built',m['docx_built'] is False)

ck('no_shared_control_github_or_current_mutation',m['shared_control_mutated'] is False and m['github_mutated'] is False and m['current_mutated'] is False)

ck('real_claims_not_made_and_acceptance_not_granted',m['real_claims_made'] is False and m['independent_acceptance']=='NOT_PERFORMED')

# Finalize the manifest as source-prep only, without claiming Word or acceptance.

script_path=Path(__file__)

m['status']='SOURCE_PREP_R02_VERIFIED_READY_FOR_BOUNDED_WRITER' if not qa['failures'] else 'SOURCE_PREP_R02_VALIDATION_FAILED'

m['source_prep_validation']={'validator':'qa/validate_source_prep_r02.py','validator_sha256':sha(script_path),'result':qa['status'] if not qa['failures'] else 'FAIL','check_count':len(qa['checks'])}

manifest_path.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

qa['failures']=[]

# Re-evaluate after manifest status update; source snapshot output list intentionally excludes manifest and QA to avoid cycles.

for name in ['SOURCE_PACKET_0004_I01-E02_R02.md', 'UNIQUE_BLUEPRINT_0004_I01-E02_R02.md', 'SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R02.csv', 'source/BLUEPRINT_CURRENT_ROW_0004.jsonl', 'source/official_evidence_table_p1.png', 'source/official_requirement.pdf', 'source/crosswalk_129_to_142.csv', 'source/requirement_source_reconciliation.csv']:

 f=base/name; entry=next((x for x in m['outputs'] if x['path']==name),None)

 if not (f.is_file() and entry and f.stat().st_size==entry['bytes'] and sha(f)==entry['sha256']): qa['failures'].append('manifest_output:'+name)

qa['status']='PASS_SOURCE_PREP_CANDIDATE_NOT_DOCX' if not qa['failures'] else 'FAIL_SOURCE_PREP'

qa['manifest_sha256']=sha(manifest_path)

qa['validator_sha256']=sha(script_path)

qa['source_hashes']={'source_packet_sha256':sha(packet),'unique_blueprint_sha256':sha(blueprint),'register_plan_sha256':sha(plan),'0003_candidate_sha256':sha(doc3),'0003_register_sha256':sha(reg3),'official_requirement_sha256':sha(official),'blueprint_current_sha256':sha(current)}

qa['docx_built']=False; qa['formal_acceptance']='NOT_GRANTED'; qa['real_execution_status']='UNKNOWN'; qa['independent_semantic_review']='NOT_APPLICABLE_TO_SOURCE_PREP'

qa_path=base/'SOURCE_PREP_QA_R02.json'

qa_path.write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

print(json.dumps({'status':qa['status'],'check_count':len(qa['checks']),'failures':qa['failures'],'manifest_sha256':qa['manifest_sha256'],'qa_sha256':sha(qa_path),'validator_sha256':qa['validator_sha256']},ensure_ascii=False,indent=2))

if qa['failures']: raise SystemExit(1)

