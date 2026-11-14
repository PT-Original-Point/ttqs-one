from pathlib import Path
import subprocess,json,hashlib,datetime,os,sys
repo=Path(r'E:\PT-Original-Point\ttqs-one'); pkg=repo/'docs/ttqs-quality-20261016/quality-review/0104_I18-E11_R15_20261022'
ref='refs/remotes/origin/pr-92-head'; expected=sys.argv[1]
env=os.environ.copy();env.update({'GIT_CONFIG_COUNT':'1','GIT_CONFIG_KEY_0':'safe.directory','GIT_CONFIG_VALUE_0':'E:/PT-Original-Point/ttqs-one'})
head=subprocess.check_output(['C:\\Program Files\\Git\\cmd\\git.exe','-C',str(repo),'rev-parse',ref],env=env,text=True).strip()
if head!=expected: raise SystemExit(f'HEAD mismatch expected {expected} got {head}')
m=json.loads((pkg/'SHA256SUMS.json').read_text(encoding='utf-8'))
miss=[]
for f in m['files']:
 path='docs/ttqs-quality-20261016/quality-review/0104_I18-E11_R15_20261022/'+f['path']
 cp=subprocess.run(['C:\\Program Files\\Git\\cmd\\git.exe','-C',str(repo),'show',f'{ref}:{path}'],env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if cp.returncode:
  miss.append({'path':f['path'],'error':cp.stderr.decode('utf-8','replace')});continue
 h=hashlib.sha256(cp.stdout).hexdigest()
 if h!=f['sha256'] or len(cp.stdout)!=f['bytes']:miss.append({'path':f['path'],'expected_sha256':f['sha256'],'remote_sha256':h,'expected_bytes':f['bytes'],'remote_bytes':len(cp.stdout)})
candidate=next(f for f in m['files'] if f['path']=='candidate/0104__證照獲取率_分析報告_R15.docx')
receipt={'receipt_id':'TTQS-0104-R15-REMOTE-READBACK-COMMIT3','checked_at_tpe':datetime.datetime.now().astimezone().isoformat(),'repository':'PT-Original-Point/ttqs-one','pull_request':92,'branch':'work/ttqs-one-document-quality-contract-20261016','checked_commit':head,'manifest_count':m['file_count'],'raw_git_blob_sha256_mismatches':len(miss),'mismatches':miss,'candidate_path':'docs/ttqs-quality-20261016/quality-review/0104_I18-E11_R15_20261022/candidate/0104__證照獲取率_分析報告_R15.docx','candidate_sha256_expected':candidate['sha256'],'candidate_remote_sha256':hashlib.sha256(subprocess.check_output(['C:\\Program Files\\Git\\cmd\\git.exe','-C',str(repo),'show',f"{ref}:docs/ttqs-quality-20261016/quality-review/0104_I18-E11_R15_20261022/candidate/0104__證照獲取率_分析報告_R15.docx"],env=env)).hexdigest(),'formal_acceptance':'NOT_GRANTED','semantic_review':'PARTIAL, exact-SHA; zero blocking defects; ten residual findings'}
if receipt['candidate_remote_sha256']!=candidate['sha256']:raise SystemExit('candidate SHA mismatch')
out=pkg/'evidence/github_remote_readback_commit3.json';out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('checked_commit',head,'manifest_count',m['file_count'],'mismatches',len(miss),'candidate_sha',receipt['candidate_remote_sha256'])
if miss:raise SystemExit(2)
