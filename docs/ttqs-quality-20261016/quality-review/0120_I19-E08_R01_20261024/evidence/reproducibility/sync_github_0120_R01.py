import hashlib, json, os, pathlib, subprocess, sys, tempfile, uuid, datetime
root=pathlib.Path(sys.argv[1]); repo=pathlib.Path(sys.argv[2]); manifest_path=root/'qa_R01/0120_R01_github_bundle_manifest.json'; branch='work/ttqs-one-document-quality-contract-20261016'; remote='origin'; repo_full='PT-Original-Point/ttqs-one'
def run(args, env=None, check=True):
    p=subprocess.run(args,cwd=repo,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if check and p.returncode: raise RuntimeError(f'command failed rc={p.returncode}: {args[1:]}\n{p.stderr.decode("utf-8", "replace")[-1800:]}')
    return p
sha=lambda b: hashlib.sha256(b).hexdigest()
m=json.loads(manifest_path.read_text(encoding='utf-8'))
script_rel='evidence/reproducibility/sync_github_0120_R01.py'; remote_root=m['remote_root']; script_remote=f'{remote_root}/{script_rel}'
script_local=root/'qa_R01/sync_github_0120_R01.py'; script_bytes=script_local.read_bytes(); script_sha=sha(script_bytes)
if not any(x['path']==script_remote for x in m['files']):
    m['files'].append({'path':script_remote,'local_path':str(script_local),'sha256':script_sha,'bytes':len(script_bytes)})
m['manifest_remote_path']=f'{remote_root}/evidence/0120_R01_github_bundle_manifest.json'
m['worker_outputs_adopted']=False
m['independent_semantic_review']='PENDING'
manifest_path.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest_remote=m['manifest_remote_path']
files=list(m['files'])+[{'path':manifest_remote,'local_path':str(manifest_path),'sha256':sha(manifest_path.read_bytes()),'bytes':manifest_path.stat().st_size}]
# Reconcile every input byte before touching the remote.
for x in files:
    data=pathlib.Path(x['local_path']).read_bytes()
    actual=sha(data)
    if actual!=x['sha256'] or len(data)!=x['bytes']:
        raise RuntimeError(f'local manifest mismatch: {x["path"]}: {actual} expected {x["sha256"]}')
# Fail closed if likely secrets appear in text receipts/source/raw worker outputs.
import re
secret=re.compile(rb'(?i)(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AIza[0-9A-Za-z_-]{30,}|-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----|Bearer\s+[A-Za-z0-9._-]{24,})')
for x in files:
    p=pathlib.Path(x['local_path'])
    if p.suffix.lower() in {'.md','.json','.csv','.txt','.jsonl','.py'} and secret.search(p.read_bytes()):
        raise RuntimeError(f'possible credential pattern; excluded pending inspection: {x["path"]}')
# Fresh ref read, fetch, then check expected parent.
ls=run(['git','ls-remote',remote,f'refs/heads/{branch}']).stdout.decode().strip().split()
if not ls: raise RuntimeError('remote branch missing')
head=ls[0]
if head!=m['expected_sync_parent']:
    raise RuntimeError(f'branch advanced: expected {m["expected_sync_parent"]}, observed {head}; no push performed')
run(['git','fetch','--quiet',remote,branch])
fetched=run(['git','rev-parse','FETCH_HEAD']).stdout.decode().strip()
if fetched!=head: raise RuntimeError(f'FETCH_HEAD mismatch: {fetched} != {head}')
# Use a disposable index. Existing worktree/index/untracked files remain untouched.
def build_commit(parent, payload, msg):
    idx=pathlib.Path(tempfile.gettempdir())/f'ttqs0120-{uuid.uuid4().hex}.index'
    env=os.environ.copy(); env['GIT_INDEX_FILE']=str(idx)
    try:
        run(['git','read-tree',parent],env)
        for x in payload:
            p=pathlib.Path(x['local_path']); data=p.read_bytes(); blob=run(['git','hash-object','-w','--',str(p)],env).stdout.decode().strip()
            remote_path=x['path']
            exists=run(['git','cat-file','-e',f'{parent}:{remote_path}'],env,check=False)
            if exists.returncode==0:
                old=run(['git','cat-file','blob',f'{parent}:{remote_path}'],env).stdout
                if sha(old)!=sha(data): raise RuntimeError(f'refusing to overwrite different existing path: {remote_path}')
            run(['git','update-index','--add','--cacheinfo',f'100644,{blob},{remote_path}'],env)
        tree=run(['git','write-tree'],env).stdout.decode().strip()
        env['GIT_AUTHOR_NAME']='Codex Desktop'; env['GIT_AUTHOR_EMAIL']='codex@localhost.invalid'; env['GIT_COMMITTER_NAME']='Codex Desktop'; env['GIT_COMMITTER_EMAIL']='codex@localhost.invalid'
        commit=run(['git','commit-tree',tree,'-p',parent,'-m',msg],env).stdout.decode().strip()
        return commit
    finally:
        try: idx.unlink(missing_ok=True)
        except OSError: pass
first=build_commit(head,files,'Add 0120 I19-E08 R01 candidate and QA evidence')
run(['git','push',remote,f'{first}:refs/heads/{branch}'])
run(['git','fetch','--quiet',remote,branch])
head1=run(['git','rev-parse','FETCH_HEAD']).stdout.decode().strip()
if head1!=first: raise RuntimeError(f'first push readback HEAD mismatch {head1} != {first}')
verified=[]
for x in files:
    data=run(['git','cat-file','blob',f'{first}:{x["path"]}']).stdout
    actual=sha(data)
    if actual!=x['sha256'] or len(data)!=x['bytes']:
        raise RuntimeError(f'first readback mismatch: {x["path"]} {actual} expected {x["sha256"]}')
    verified.append({'path':x['path'],'sha256':actual,'bytes':len(data),'status':'VERIFIED_RAW_BYTES'})
receipt={'project_id':'TTQS_ONE','doc_id':'0120','requirement_id':'I19-E08','candidate_state':'CANDIDATE','formal_acceptance':'NOT_GRANTED','independent_semantic_review':'PENDING','branch':branch,'pr':92,'parent_before_sync':head,'first_sync_commit':first,'verified_at_local':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(),'files_verified':len(verified),'docx_sha256':next(x['sha256'] for x in files if x['path'].endswith('.docx')),'docx_remote_path':next(x['path'] for x in files if x['path'].endswith('.docx')),'worker_prose_adopted':False,'records':verified}
receipt_path=root/'qa_R01/GITHUB_RAW_BYTE_READBACK_R01.json'; receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
receipt_entry={'path':f'{remote_root}/evidence/GITHUB_RAW_BYTE_READBACK_R01.json','local_path':str(receipt_path),'sha256':sha(receipt_path.read_bytes()),'bytes':receipt_path.stat().st_size}
second=build_commit(first,[receipt_entry],'Record 0120 R01 exact GitHub raw-byte readback')
run(['git','push',remote,f'{second}:refs/heads/{branch}'])
run(['git','fetch','--quiet',remote,branch])
finalhead=run(['git','rev-parse','FETCH_HEAD']).stdout.decode().strip()
if finalhead!=second: raise RuntimeError(f'final push readback HEAD mismatch {finalhead} != {second}')
# Verify final commit inherits all payload bytes and the readback receipt itself.
final_records=[]
for x in files+[receipt_entry]:
    data=run(['git','cat-file','blob',f'{second}:{x["path"]}']).stdout
    actual=sha(data)
    if actual!=x['sha256'] or len(data)!=x['bytes']:
        raise RuntimeError(f'final readback mismatch: {x["path"]} {actual} expected {x["sha256"]}')
    final_records.append({'path':x['path'],'sha256':actual,'bytes':len(data)})
# Validate DOCX again from the final remote commit.
docx=next(x for x in files if x['path'].endswith('.docx'))
assert next(x for x in final_records if x['path']==docx['path'])['sha256']==docx['sha256']
print(json.dumps({'status':'SYNC_AND_READBACK_VERIFIED','branch':branch,'pr':92,'parent_before_sync':head,'first_sync_commit':first,'final_head':second,'manifest_files':len(m['files']),'readback_receipt_remote':receipt_entry['path'],'readback_receipt_sha256':receipt_entry['sha256'],'docx_sha256':docx['sha256'],'docx_remote_path':docx['path'],'verified_final_paths':len(final_records),'final_records':final_records},ensure_ascii=False))
