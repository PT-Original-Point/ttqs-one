import json
from pathlib import Path
p=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01\review\opencode_semantic_R01_stdout.jsonl')
out=Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01\review\independent_semantic_review_R01.md')
parts=[]
for line in p.read_text(encoding='utf-8-sig').splitlines():
 try: o=json.loads(line)
 except: continue
 if o.get('type')=='text':
  txt=(o.get('part') or {}).get('text')
  if txt: parts.append(txt)
out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('text events',len(parts),'output bytes',out.stat().st_size)
