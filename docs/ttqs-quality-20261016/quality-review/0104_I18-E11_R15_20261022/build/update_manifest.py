from pathlib import Path
import hashlib,json
pkg=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022')
files=[]
for p in sorted(pkg.rglob('*')):
 if p.is_file() and p.name!='SHA256SUMS.json':
  b=p.read_bytes(); files.append({'path':p.relative_to(pkg).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
manifest={
 'package':'0104_I18-E11_R15_20261022 (R15 historical; R16 current)',
 'current_candidate_docx_sha256':hashlib.sha256((pkg/'candidate/R16/0104__證照獲取率_分析報告_R16.docx').read_bytes()).hexdigest(),
 'candidate_state':'CANDIDATE_NOT_FORMALLY_ACCEPTED',
 'file_count':len(files),
 'files':files
}
(pkg/'SHA256SUMS.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('manifest_count',len(files),'current_candidate_sha',manifest['current_candidate_docx_sha256'])
