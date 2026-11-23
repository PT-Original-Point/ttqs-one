#!/usr/bin/env python3
import hashlib, json, re
from pathlib import Path

base=Path(__file__).resolve().parents[1]
raw=base/'review'/'opencode_semantic_R02_stdout.jsonl'
body=base/'candidate'/'0083_R02_body.md'
events=[json.loads(x) for x in raw.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
texts=[e['part']['text'] for e in events if e.get('type')=='text' and isinstance(e.get('part',{}).get('text'),str)]
if not texts: raise SystemExit('No reviewer text found')
review=texts[-1].strip()+'\n'
out=base/'review'/'independent_semantic_review_R02.md'; out.write_text(review,encoding='utf-8')
sha=hashlib.sha256(body.read_bytes()).hexdigest()
m=re.search(r'(?is)\bverdict\s*[:：* ]+\s*(PASS|PARTIAL|FAIL)\b',review)
receipt={'schema':'ttqs-0083-independent-semantic-review-v2','reviewer_route':'OpenCode v2 CLI separate from writer session','model':'opencode/deepseek-v4.1-flash-free','session_id':next((e.get('sessionID') for e in events if e.get('sessionID')),None),'exit_code':int((base/'review'/'opencode_semantic_R02_exit.txt').read_text().strip()),'body_path':str(body),'body_sha256':sha,'reviewed_sha_echoed':sha in review,'prompt_sha256':hashlib.sha256((base/'review'/'semantic_review_prompt_R02.md').read_bytes()).hexdigest(),'raw_stdout_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'stderr_sha256':hashlib.sha256((base/'review'/'opencode_semantic_R02_stderr.txt').read_bytes()).hexdigest(),'review_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'reported_verdict':m.group(1).upper() if m else 'UNPARSED','acceptance':'INDEPENDENT_TEXT_REVIEW_ONLY_NOT_FORMAL_ACCEPTANCE'}
(base/'evidence'/'semantic_review_receipt_R02.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=True))
