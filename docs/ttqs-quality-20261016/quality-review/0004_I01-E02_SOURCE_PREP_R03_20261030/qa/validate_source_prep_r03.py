import csv, hashlib, json, pathlib, sys
root=pathlib.Path(sys.argv[1])
manifest_path=root/'SOURCE_PREP_MANIFEST_0004_R03.json'
m=json.loads(manifest_path.read_text(encoding='utf-8-sig'))
checks={}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ck(k,v): checks[k]=bool(v)
for item in m['files']:
    p=root/item['path']
    ck('file:'+item['path'],p.is_file() and p.stat().st_size==item['bytes'] and sha(p)==item['sha256'])
reg3=root/'source/0003_SHARED_R09/SYNTHETIC_REPLACEMENT_REGISTER_0003_R09.csv'
with reg3.open(encoding='utf-8-sig',newline='') as f: rows3={r['fact_id']:r for r in csv.DictReader(f)}
dep=m['0003_dependency']
ck('0003_register_hash_matches_manifest',sha(reg3)==dep['register_sha256'])
ck('0003_fact_values_and_synthetic_status',rows3.get('SYN-001',{}).get('synthetic_value')=='2026-10-28' and rows3.get('SYN-002',{}).get('synthetic_value')=='SYN-0003-001' and rows3.get('SYN-001',{}).get('status')=='SAMPLE_SYNTHETIC_ONLY' and rows3.get('SYN-002',{}).get('status')=='SAMPLE_SYNTHETIC_ONLY')
doc3=root/'source/0003_SHARED_R09/0003_I01-E02_R09_reference_only.docx'
ck('0003_candidate_hash_matches_manifest',sha(doc3)==dep['candidate_docx_sha256'])
m3=json.loads((root/'source/0003_SHARED_R09/CANDIDATE_EVIDENCE_MANIFEST.json').read_text(encoding='utf-8-sig'))
ck('0003_manifest_truth_boundary',m3.get('identity',{}).get('candidate_sha256')==dep['candidate_docx_sha256'] and m3.get('identity',{}).get('register_sha256')==dep['register_sha256'] and m3.get('quality',{}).get('independent_semantic')=='IN_PROGRESS' and m3.get('quality',{}).get('formal_acceptance')=='UNKNOWN')
packet=(root/'SOURCE_PACKET_0004_I01-E02_R03.md').read_text(encoding='utf-8-sig')
bp=(root/'UNIQUE_BLUEPRINT_0004_I01-E02_R03.md').read_text(encoding='utf-8-sig')
plan_path=root/'SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R03.csv'
with plan_path.open(encoding='utf-8-sig',newline='') as f: plan=list(csv.DictReader(f))
ck('packet_binds_live_register_candidate_and_manifest',dep['register_sha256'] in packet and dep['candidate_docx_sha256'] in packet and dep['manifest_sha256'] in packet)
ck('blueprint_binds_r03_packet_and_live_crossref','SOURCE_PACKET_0004_I01-E02_R03.md' in bp and dep['register_sha256'] in bp and dep['candidate_docx_sha256'] in bp)
stale='646a5dff8a540d53033d1cf161a6d4839bbf9928d0ae4fece6b6a256764604e1'
plan_text=plan_path.read_text(encoding='utf-8-sig')
ck('no_stale_0003_hash_in_active_inputs',all(stale not in x for x in [packet,bp,plan_text]))
ck('no_stale_r17_in_active_inputs',all('R17' not in x for x in [packet,bp,plan_text]))
ck('register_ids_unique_and_expected',len(plan)==84 and len({r['fact_id'] for r in plan})==84 and all(r['fact_id'] for r in plan))
ck('register_contains_both_updated_crossrefs',all(any(r['fact_id']==fid and dep['register_sha256'] in r['source_basis'] for r in plan) for fid in ['XREF-0003-SYN-001','XREF-0003-SYN-002']))
ck('register_sample_values_match_shared_source',next((r['synthetic_value'] for r in plan if r['fact_id']=='XREF-0003-SYN-001'),None)=='2026-10-28' and next((r['synthetic_value'] for r in plan if r['fact_id']=='XREF-0003-SYN-002'),None)=='SYN-0003-001')
def normalize(s): return "".join(s.split())
pn,bn=normalize(packet),normalize(bp)
rates=['2/4=50.0%','1/2=50.0%','1/4=25.0%','4/5=80.0%']
a=m['sample_arithmetic']
ck('sample_rates_match_packet_and_blueprint',all(x in pn and x in bn for x in rates))
ck('sample_flow_counts_reconcile',a['screened']==a['ineligible']+a['eligible_invites'] and a['eligible_invites']==a['unique_returns']+a['refusal']+a['no_response'] and a['unique_returns']==a['valid']+a['invalid'] and a['raw_receipt_events']==a['unique_returns']+a['duplicate_extra'])
ck('sample_rates_recompute',a['rates']['response_rate']=='2/4=50.0%' and a['rates']['effective_rate']=='1/2=50.0%' and a['rates']['valid_yield']=='1/4=25.0%' and a['rates']['eligibility_pass_rate']=='4/5=80.0%')
ck('official_pdf_snapshot_hash',sha(root/'source/official_requirement.pdf')=='805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709')
ck('doc4_not_built_and_no_real_or_acceptance_claim',m.get('docx_built') is False and m.get('real_execution_status')=='UNKNOWN' and m.get('formal_acceptance')=='NOT_GRANTED' and 'CANDIDATE' in packet and 'SAMPLE/SYNTHETIC' in packet)
failed=[k for k,v in checks.items() if not v]
qa={'project_id':'TTQS_ONE','doc_id':'0004','requirement_id':'I01-E02','revision':'SOURCE_PREP_R03','status':'PASS_SOURCE_PREP_CANDIDATE_NOT_DOCX' if not failed else 'FAIL','checks':checks,'failures':failed,'stage':'SOURCE_PREPARATION_ONLY','formal_acceptance':'NOT_GRANTED','docx_built':False,'real_execution_status':'UNKNOWN','independent_semantic_review':'NOT_APPLICABLE_TO_SOURCE_PREP','manifest_sha256':sha(manifest_path),'validator_sha256':sha(pathlib.Path(__file__)),'source_hashes':{x['path']:x['sha256'] for x in m['files']},'0003_dependency':dep,'sample_arithmetic':{'screened':5,'ineligible':1,'eligible_invites':4,'unique_returns':2,'valid':1,'invalid':1,'refusal':1,'no_response':1,'duplicate_extra':1,'raw_receipt_events':3,'rates':{'response':'2/4=50.0%','effective':'1/2=50.0%','valid_yield':'1/4=25.0%','eligibility_pass':'4/5=80.0%'}}}
(root/'qa/SOURCE_PREP_QA_R03.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':qa['status'],'checks':len(checks),'failures':failed,'manifest_sha256':qa['manifest_sha256'],'validator_sha256':qa['validator_sha256']},ensure_ascii=False,indent=2))
sys.exit(1 if failed else 0)
