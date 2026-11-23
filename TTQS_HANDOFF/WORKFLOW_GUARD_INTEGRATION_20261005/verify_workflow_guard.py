from pathlib import Path
import importlib.util,json,hashlib
root=Path(__file__).resolve().parents[2];spec=importlib.util.spec_from_file_location('guard',root/'MASTER/workflow_guard.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
cases=[]
def check(name,condition):assert condition,name;cases.append({'case':name,'pass':True})
p=root/'WORK/CONTENT_PAYLOADS/WF_ANTIGRAVITY_BUILD_0013_INLINE_20261005/content.json'
check('Real 0013 prompt leak blocked',not g.body_preflight(json.loads(p.read_text(encoding='utf-8-sig')))['allowed'])
p=root/'MASTER/CONTENT_AUDIT_0013/operational_proposal_R01.json'
check('Repaired 0013 passes cheap screen only',g.body_preflight(json.loads(p.read_text(encoding='utf-8-sig')))['allowed'])
p=root/'WORK/CONTENT_PAYLOADS/WF_MASTER_DIRECT_AG_0013_PATCH_20261005_1158/merged_content.json'
check('Real short repair instruction and engineering leak blocked',not g.body_preflight(json.loads(p.read_text(encoding='utf-8-sig')))['allowed'])
w=root/'WORK/REVIEWS/codex_cross_review_0054_R13_20261005_104829';raw=(w/'codex_review_raw.txt').read_text(encoding='utf-8-sig');sha='87e230fa4822ac0e2ab29d853a2d267493b872ad2c781abf0700824812e453c0';obj=g.extract_final_review(raw,sha,w.name)
check('Real transcript yields actual FAIL not template',obj['verdict']=='FAIL' and len(obj['defects'])==5)
for name,raw,expected in [('Prompt template rejected',json.dumps({'work_id':'a','reviewed_sha256':'b','verdict':'PASS|FAIL'}),'b'),('Wrong SHA rejected',json.dumps({'work_id':'a','reviewed_sha256':'c','verdict':'PASS'}),'b')]:
 try:g.extract_final_review(raw,expected,'a');rejected=False
 except ValueError:rejected=True
 check(name,rejected)
for verdict in ['FAIL_REPAIRABLE','FAIL_SYSTEMIC']:
 value={'work_id':'cross','reviewed_sha256':'sha','verdict':verdict}
 check('Existing cross-review failure verdict preserved '+verdict,g.extract_final_review(json.dumps(value),'sha','cross')['verdict']==verdict)
check('Source missing blocked',not g.packet_preflight(100,False)['allowed'])
check('Slot busy blocked',not g.packet_preflight(100,True,True)['allowed'])
check('Large packet compacted before model',not g.packet_preflight(32769,True)['allowed'])
check('Small valid packet admitted without reserve',g.packet_preflight(17601,True)['allowed'])
a=g.review_fingerprint('sha','contract','source',{'rule':'basic'})
check('Identical evidence fingerprint stable',a==g.review_fingerprint('sha','contract','source',{'rule':'basic'}))
check('Fact repair permits meaningful same-body review',a!=g.review_fingerprint('sha','contract','source',{'rule':'repaired'}))
err={'type':'provider.quota','status':429,'response':{'body':'{"error":{"type":"FreeUsageLimitError"}}'}};r=g.provider_event(err)
check('Quota refusal stops automatic retries without asserting ban',r['automatic_retry_allowed'] is False and r['permanent_ban_proven'] is False and r['status_observed']==429)
template={'work_id':'old','reviewed_sha256':'wrong','verdict':'PASS'}
final={'work_id':'new','reviewed_sha256':'sha-new','verdict':'FAIL_REPAIRABLE','defects':[{'body_locator':'P1'}]}
raw=json.dumps(template)+'\n'+json.dumps(final)+'\ntokens used\n1'
parsed=g.extract_final_review(raw,'sha-new','new')
check('Final transcript object wins over earlier template and token trailer',parsed==final)
body_result=g.provider_event({'type':'document_text','message':'line 429'})
check('Body text 429 never classifies provider quota',body_result['classification']!='PROVIDER_USAGE_REJECTED')
supervisor_spec=importlib.util.spec_from_file_location('supervisor_integration',root/'AUTOMATION/supervisor_core.py')
supervisor=importlib.util.module_from_spec(supervisor_spec);supervisor_spec.loader.exec_module(supervisor)
loaded=supervisor.workflow_guard(root)
check('Supervisor loads workflow guard at dispatch runtime',Path(loaded.__file__).resolve()==(root/'MASTER/workflow_guard.py').resolve())
queue=supervisor.load_json(root/'CONTROL'/'BUILD_QUEUE.json',{})
item=next(x for x in queue.get('items',[]) if str(x.get('deliverable_id','')).zfill(4)=='0013')
payload_path=root/'WORK'/'CONTENT_PAYLOADS'/'WF_ANTIGRAVITY_BUILD_0013_INLINE_20261005'/'content.json'
checked_payload,validation_error=supervisor.validate_content_payload(root,item,payload_path)
check('Live payload-validation entrypoint blocks actual prompt leak',checked_payload is None and str(validation_error).startswith('CONTENT_PROMPT_LEAK:'))
check('Supervisor respects Master-only Antigravity dispatch policy',supervisor.antigravity_direct_dispatch_only(root))
check('Production auto-dispatch defers Antigravity to Master',supervisor.antigravity_auto_dispatch_deferred(root,True,False))
check('Existing payload salvage remains allowed under Master-only dispatch',not supervisor.antigravity_auto_dispatch_deferred(root,True,True))
out=Path(__file__).with_name('guard_verification.json');out.write_text(json.dumps({'passed':len(cases),'cases':cases,'real_artifact_fixtures_used':True,'live_model_calls':0,'integration_with_supervisor':'PASS','supervisor_sha256':hashlib.sha256((root/'AUTOMATION/supervisor_core.py').read_bytes()).hexdigest(),'workflow_guard_sha256':hashlib.sha256((root/'MASTER/workflow_guard.py').read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'passed':len(cases),'live_model_calls':0,'integration_with_supervisor':'PASS'}))
