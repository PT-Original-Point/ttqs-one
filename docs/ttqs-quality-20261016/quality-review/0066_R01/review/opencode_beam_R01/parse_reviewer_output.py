import json,sys,re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
p=Path(sys.argv[1]);ev=[json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
texts=[]
for x in ev:
 if x.get('type')=='text':
  part=x.get('part') or {};s=part.get('text') or ''
  if s:texts.append(s)
out='\n\n'.join(texts)
dest=p.parent/'independent_semantic_review_R01.md';dest.write_text(out+'\n',encoding='utf-8')
print('SESSION='+str(next((x.get('sessionID') for x in ev if x.get('sessionID')),'')))
print('TEXT_EVENTS='+str(len(texts)))
print('RESULT_SHA256='+__import__('hashlib').sha256(dest.read_bytes()).hexdigest())
print(out[-8500:])
