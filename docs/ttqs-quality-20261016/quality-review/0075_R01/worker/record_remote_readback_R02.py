from pathlib import Path
import hashlib,json,subprocess,datetime
root=Path(r'E:\TTQS\_github_sync_0064'); rel='docs/ttqs-quality-20261016/quality-review/0075_R01'; base=root/rel
ref='origin/work/ttqs-one-document-quality-contract-20261016'
run=lambda *a:subprocess.run(a,cwd=root,capture_output=True,check=True).stdout
commit=run('git','rev-parse',ref).decode().strip(); local_head=run('git','rev-parse','HEAD').decode().strip()
remote_manifest=run('git','show',f'{ref}:{rel}/evidence/package_manifest_R02.json')
manifest=json.loads(remote_manifest)
local_manifest=(base/'evidence/package_manifest_R02.json').read_bytes()
if remote_manifest!=local_manifest: raise SystemExit('Manifest remote bytes differ from local')
sha=lambda b:hashlib.sha256(b).hexdigest()
results=[]
for entry in manifest['files']:
 data=run('git','show',f"{ref}:{rel}/{entry['path']}")
 got=sha(data); ok=got==entry['sha256'] and len(data)==entry['bytes']
 results.append((entry['path'],ok,got,entry['sha256'],len(data),entry['bytes']))
failed=[x for x in results if not x[1]]
if failed: raise SystemExit(json.dumps({'remote_commit':commit,'failures':failed[:8]},ensure_ascii=False))
readback={
 'schema':'TTQS_ONE_0075_R02_REMOTE_READBACK.v1','repository':'PT-Original-Point/ttqs-one','branch':'work/ttqs-one-document-quality-contract-20261016',
 'readback_commit':commit,'local_head_at_readback':local_head,'manifest_sha256':sha(remote_manifest),'manifest_entries_verified':len(results),'manifest_entries_mismatched':0,
 'manifest_and_all_package_files_exact':True,'candidate_sha256':manifest['candidate_sha256'],'candidate_remote_sha256':sha(run('git','show',f'{ref}:{rel}/candidate/0075_R02.docx')),
 'verified_at_local':datetime.datetime.now().astimezone().isoformat(),'method':'git fetch from origin followed by byte-for-byte git object readback and SHA-256/length comparison for every manifest path plus manifest blob.'
}
(base/'evidence/remote_readback_R02.json').write_text(json.dumps(readback,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Update project-facing status and P8 from pending to verified after the actual readback.
sp=base/'evidence/candidate_status_R02.json'; status=json.loads(sp.read_text(encoding='utf-8')); status['remote_sync']='VERIFIED'; status['remote_commit_first_readback']=commit; status['remote_readback_entries_verified']=len(results); status['remote_readback_mismatches']=0; sp.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p8p=base/'evidence/R04_P8_STATUS_0075_R02.json'; p8=json.loads(p8p.read_text(encoding='utf-8')); p8['sync_state']='VERIFIED'; p8['remote_commit_readback']=commit; p8['remote_paths_verified']=len(results); p8['remote_mismatches']=0; p8['next_action']='Commit the readback receipt and final status to the same PR branch; then verify the finalized remote package and select the next READY document.'; p8p.write_text(json.dumps(p8,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Refresh the manifest to include the readback receipt and updated status files.
manifest_path=base/'evidence/package_manifest_R02.json'; entries=[]
for p in sorted(base.rglob('*')):
 if p.is_file() and p!=manifest_path: entries.append({'path':p.relative_to(base).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())})
manifest.update({'source_head_before_sync':local_head,'first_sync_commit_readback':commit,'file_count_excluding_manifest':len(entries),'total_bytes_excluding_manifest':sum(x['bytes'] for x in entries),'files':entries})
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'first_sync_commit':commit,'local_head':local_head,'first_readback_entries_verified':len(results),'mismatches':0,'candidate_sha256':readback['candidate_sha256'],'remote_readback_receipt_sha256':sha((base/'evidence/remote_readback_R02.json').read_bytes()),'updated_manifest_entries':len(entries),'status':'VERIFIED_FIRST_SYNC_AWAIT_FINAL_STATUS_COMMIT'},ensure_ascii=False,indent=2))
