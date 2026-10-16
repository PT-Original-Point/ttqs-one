from pathlib import Path
from hashlib import sha256
import json, sys
root=Path(sys.argv[1])
excluded={'artifact_manifest.json','PROGRESS.json'}
files=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name not in excluded:
        data=p.read_bytes()
        files.append({'path':p.relative_to(root).as_posix(),'bytes':len(data),'sha256':sha256(data).hexdigest()})
progress_path=root/'PROGRESS.json'
progress=json.loads(progress_path.read_text(encoding='utf-8-sig'))
manifest={'project_id':'TTQS_ONE','doc_id':'0036','requirement_id':'I07-E04','official_checkbox_serial':'036','revision':'R09','status':'CANDIDATE_ONLY_NOT_PROMOTED','candidate_sha256':progress['candidate_sha256'],'file_count':len(files),'files':files,'manifest_note':'PROGRESS.json and artifact_manifest.json are excluded to prevent a circular digest; the Git commit binds both.'}
manifest_path=root/'artifact_manifest.json'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
progress['artifact_manifest_sha256']=sha256(manifest_path.read_bytes()).hexdigest()
progress_path.write_text(json.dumps(progress,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'file_count':len(files),'artifact_manifest_sha256':progress['artifact_manifest_sha256'],'candidate_sha256':progress['candidate_sha256']},indent=2))
