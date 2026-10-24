from pathlib import Path
import subprocess, hashlib, json, sys
root=Path(r'E:\TTQS\_github_sync_0064')
review=root/'docs/ttqs-quality-20261016/quality-review/0067_R01/review'
exe=Path(r'C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe')
packet=review/'semantic_review_packet_R03.md'
args=[str(exe),'run','--model','opencode/beam-free','--format','json','--title','TTQS ONE 0067 R03 independent semantic review','--file',str(packet),'Review this attached, source-bound packet independently. Verify the exact DOCX SHA against the actual file in the stated workspace, inspect the DOCX-derived body, evaluate every required question and use the required response format. This is a READ-ONLY semantic review: do not modify, rebuild, commit, push, or use Computer Use. Do not trust any claimed PASS; report only checks you actually performed.']
p=subprocess.run(args,cwd=str(root),capture_output=True)
(review/'opencode_semantic_R03_stdout.jsonl').write_bytes(p.stdout)
(review/'opencode_semantic_R03_stderr.txt').write_bytes(p.stderr)
(review/'opencode_semantic_R03_exit.txt').write_text(str(p.returncode)+'\n',encoding='ascii')
print(json.dumps({'exit_code':p.returncode,'stdout_bytes':len(p.stdout),'stderr_bytes':len(p.stderr),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest(),'stdout_path':str(review/'opencode_semantic_R03_stdout.jsonl'),'stderr_path':str(review/'opencode_semantic_R03_stderr.txt')},ensure_ascii=False))
if p.returncode: sys.exit(p.returncode)
