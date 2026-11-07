from pathlib import Path
import hashlib,json
root=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0066_R01');p=root/'inputs'/'0066_BODY_R01_HUMAN_READY.md';s=p.read_text(encoding='utf-8')
line='**追溯說明**：上表將官方文字逐句對應到本報告章節，確保結案報告不遺漏任一官方要素。所有對應內容在本文中皆有填妥內容，但均標示為合成示例。\n'
if s.count(line)!=1:raise SystemExit('orphan trace paragraph not found exactly once')
p.write_text(s.replace(line,''),encoding='utf-8')
mf=root/'evidence'/'source_manifest_R01.json';m=json.loads(mf.read_text(encoding='utf-8'));m['body_sha256']=hashlib.sha256(p.read_bytes()).hexdigest();m['body_layout_source_sha256']=m['body_sha256'];m['layout_fix']='Removed a two-line trace paragraph orphaned from its table on the preceding page; trace remains explicit in the crosswalk table.';mf.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(m['body_sha256'])
