import hashlib,json,os,pathlib,subprocess,sys,tempfile,uuid
root=pathlib.Path(sys.argv[1]); repo=pathlib.Path(sys.argv[2]); mp=root/'qa_R01/0120_R01_github_bundle_manifest.json'; branch='work/ttqs-one-document-quality-contract-20261016'; remote='origin'; first='17b511110e0096d7e44c33c37c90ceaf2ca42d03'
def run(args,env=None,check=True):
 p=subprocess.run(['git',*args],cwd=repo,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if check and p.returncode: raise RuntimeError(f'git {args[0]} failed rc={p.returncode}: {p.stderr.decode("utf-8","replace")[-1200:]}')
 return p
sha=lambda b:hashlib.sha256(b).hexdigest()
m=json.loads(mp.read_text(encoding='utf-8')); root_remote=m['remote_root']; m['initial_sync_attempt_commit']=first; m['readback_receipt_path']=f'{root_remote}/evidence/GITHUB_RAW_BYTE_READBACK_R01.json'; m['git_blob_mode']='--no-filters (preserve exact local bytes)'
files=m['files']; sync_script=root/'qa_R01/sync_github_0120_R01.py'; sync_remote=f'{root_remote}/evidence/reproducibility/sync_github_0120_R01.py'
for x in files:
 if x['path']==sync_remote:
  x['sha256']=sha(sync_script.read_bytes());x['bytes']=sync_script.stat().st_size
repair_local=root/'qa_R01/repair_rawbyte_sync_0120_R01.py';repair_remote=f'{root_remote}/evidence/reproducibility/repair_rawbyte_sync_0120_R01.py'
if not any(x['path']==repair_remote for x in files):files.append({'path':repair_remote,'local_path':str(repair_local),'sha256':sha(repair_local.read_bytes()),'bytes':repair_local.stat().st_size})
m['manifest_remote_path']=f'{root_remote}/evidence/0120_R01_github_bundle_manifest.json';mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
payload=list(files)+[{'path':m['manifest_remote_path'],'local_path':str(mp),'sha256':sha(mp.read_bytes()),'bytes':mp.stat().st_size}]
for x in payload:
 b=pathlib.Path(x['local_path']).read_bytes()
 if sha(b)!=x['sha256'] or len(b)!=x['bytes']:raise RuntimeError('local byte/hash mismatch '+x['path'])
head=run(['ls-remote',remote,f'refs/heads/{branch}']).stdout.decode().split()[0]
if head!=first:raise RuntimeError(f'branch changed since first attempt: {head}; expected {first}; abort')
run(['fetch','--quiet',remote,branch]);fetched=run(['rev-parse','FETCH_HEAD']).stdout.decode().strip()
if fetched!=head:raise RuntimeError('fetched head mismatch')
if run(['merge-base','--is-ancestor',first,head],check=False).returncode:raise RuntimeError('first attempt not ancestor; abort')
# Isolated index, only this unique 0120 subtree is amended; no worktree/index mutation.
idx=pathlib.Path(tempfile.gettempdir())/f'ttqs0120raw-{uuid.uuid4().hex}.index';env=os.environ.copy();env['GIT_INDEX_FILE']=str(idx)
try:
 run(['read-tree',head],env)
 for x in payload:
  if not x['path'].startswith(root_remote+'/'):raise RuntimeError('path escaped unique bundle root')
  p=pathlib.Path(x['local_path']);blob=run(['hash-object','--no-filters','-w','--',str(p)],env).stdout.decode().strip()
  run(['update-index','--add','--cacheinfo',f'100644,{blob},{x["path"]}'],env)
 tree=run(['write-tree'],env).stdout.decode().strip();env.update(GIT_AUTHOR_NAME='Codex Desktop',GIT_AUTHOR_EMAIL='codex@localhost.invalid',GIT_COMMITTER_NAME='Codex Desktop',GIT_COMMITTER_EMAIL='codex@localhost.invalid')
 commit=run(['commit-tree',tree,'-p',head,'-m','Preserve exact bytes for 0120 R01 GitHub bundle'],env).stdout.decode().strip()
finally:
 try:idx.unlink(missing_ok=True)
 except OSError:pass
run(['push',remote,f'{commit}:refs/heads/{branch}']);run(['fetch','--quiet',remote,branch]);fh=run(['rev-parse','FETCH_HEAD']).stdout.decode().strip()
if fh!=commit:raise RuntimeError('repair commit HEAD readback mismatch')
tree_bytes=run(['ls-tree','-r','-z',commit]).stdout;entries={}
for rec in tree_bytes.split(b'\0'):
 if rec:
  meta,path=rec.split(b'\t',1);entries[path]=meta.decode('ascii').split(' ')[2]
verified=[]
for x in payload:
 path=x['path'].encode('utf-8')
 if path not in entries:raise RuntimeError('exact UTF-8 path missing '+repr(x['path']))
 data=run(['cat-file','blob',entries[path]]).stdout;h=sha(data)
 if h!=x['sha256'] or len(data)!=x['bytes']:raise RuntimeError(f'raw byte mismatch {x["path"]}: {h} != {x["sha256"]}; {len(data)} != {x["bytes"]}')
 verified.append({'path':x['path'],'sha256':h,'bytes':len(data),'blob':entries[path]})
print(json.dumps({'status':'EXACT_RAW_BYTE_REPAIR_VERIFIED','initial_attempt_commit':first,'corrected_commit':commit,'final_path_count':len(verified),'docx_sha256':next(x['sha256'] for x in payload if x['path'].endswith('.docx')),'verified':verified},ensure_ascii=False))
