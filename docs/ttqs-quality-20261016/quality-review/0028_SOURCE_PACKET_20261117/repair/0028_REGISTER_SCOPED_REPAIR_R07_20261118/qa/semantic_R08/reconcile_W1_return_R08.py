from pathlib import Path
import json
from hashlib import sha256
qa=Path(r'E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0028_SOURCE_PACKET_20261117\repair\0028_REGISTER_SCOPED_REPAIR_R07_20261118\qa\semantic_R08')
events=[json.loads(x) for x in (qa/'W1_STDOUT_R08.jsonl').read_text(encoding='utf-8-sig').splitlines() if x.strip()]
text=next(e['part']['text'] for e in events if e.get('type')=='text')
review=json.loads(text);finish=next(e for e in events if e.get('type')=='step_finish');part=finish['part']
if review['candidate_docx_sha256']!='1EB4E9D26F761B57885AF7DC304BB76324AD85C7513FC858C82AF199D5273F70' or review['decision']!='PASS':raise SystemExit('RETURN_BINDING_OR_DECISION_MISMATCH')
sha=lambda b:sha256(b).hexdigest().upper()
original=json.loads((qa/'W1_REVIEW_RETURN_R08.json').read_text(encoding='utf-8-sig'))
result=dict(original)
result.update({'cost_usd':part.get('cost'),'token_usage':part.get('tokens'),'provider_terminal_reason':part.get('reason'),'review_json_sha256':sha(text.encode('utf-8')),'reconciles_prior_receipt':'W1_REVIEW_RETURN_R08.json','reconciliation_note':'Corrected token/cost extraction to read OpenCode JSON step_finish.part; initial return receipt recorded null because it looked at the wrong JSON level.'})
out=qa/'W1_REVIEW_RETURN_R08_RECONCILED.json'
if out.exists():raise SystemExit('RECONCILED_RETURN_ALREADY_EXISTS')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'decision':result['decision'],'served_model':result['served_model'],'cost_usd':result['cost_usd'],'token_usage':result['token_usage'],'stdout_sha256':result['stdout_sha256'],'review_json_sha256':result['review_json_sha256'],'receipt':str(out)},ensure_ascii=False))

