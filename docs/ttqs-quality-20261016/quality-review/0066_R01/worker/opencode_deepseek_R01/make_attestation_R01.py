from pathlib import Path
import json,hashlib
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0066_R01')
exp=root/'worker'/'opencode_deepseek_R01'/'session_export_R01.json';raw=root/'worker'/'opencode_deepseek_R01'/'stdout_R01.jsonl';j=json.loads(exp.read_text(encoding='utf-8-sig'));i=j['info'];h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'session_id':i['id'],'provider_id':i['model']['providerID'],'model_id':i['model']['id'],'outcome':i['outcome'],'cost_usd':i['cost'],'tokens':i['tokens'],'raw_jsonl_sha256':h(raw),'sanitized_session_export_sha256':h(exp),'final_body_sha256':h(root/'inputs'/'0066_BODY_R01_HUMAN_READY.md'),'attestation_note':'Model and outcome verified from OpenCode v2 session export; output is production provenance, not evidence of association activity.'}
(root/'worker'/'opencode_deepseek_R01'/'writer_attestation_R01.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
