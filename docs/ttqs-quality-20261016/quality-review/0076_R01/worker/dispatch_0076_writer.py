from __future__ import annotations
import json, subprocess
from pathlib import Path

repo=Path(__file__).resolve().parents[5]
package=repo/"docs/ttqs-quality-20261016/quality-review/0076_R01"
worker=package/"worker"
cli=Path(r"C:\Users\J\AppData\Roaming\ai.opencode.desktop\cli\2.0.29-x64\opencode-cli.exe")
if not cli.is_file(): raise FileNotFoundError(cli)
attach=[
 worker/"WRITE_PROMPT_0076_R01.md",
 package/"inputs/UNIQUE_BLUEPRINT_0076_R01.md",
 package/"inputs/SOURCE_PACKET_0076_R01.md",
 package/"inputs/SYNTHETIC_ASSESSMENT_DATA_0076_R01.csv",
 package/"inputs/SYNTHETIC_ITEM_ANALYSIS_0076_R01.csv",
 package/"inputs/SYNTHETIC_CALCULATION_CHECK_0076_R01.json",
]
for p in attach:
 if not p.is_file(): raise FileNotFoundError(p)
argv=[str(cli),"run","--format","json","--model","opencode/deepseek-v4.1-flash-free","--title","TTQS ONE 0076 R01 source-bound writer"]
for p in attach: argv += ["--file",str(p)]
argv += ["Write the two assigned files now. Read every attached source, obey the scope, and return a concise completion summary with exact paths and byte counts."]
receipt={"tool":"OpenCode CLI v2","version":"2.0.29","model":"opencode/deepseek-v4.1-flash-free","cwd":str(repo),"argv":argv,"attachments":[str(p.relative_to(repo)) for p in attach],"computer_use":False,"auto_approval_flag":False}
(worker/"opencode_writer_R01_dispatch.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
run=subprocess.run(argv,cwd=str(repo),capture_output=True)
(worker/"opencode_writer_R01_stdout.jsonl").write_bytes(run.stdout)
(worker/"opencode_writer_R01_stderr.txt").write_bytes(run.stderr)
(worker/"opencode_writer_R01_exit.txt").write_text(str(run.returncode)+"\n",encoding="ascii")
print(json.dumps({"exit_code":run.returncode,"stdout_bytes":len(run.stdout),"stderr_bytes":len(run.stderr),"dispatch":str(worker/"opencode_writer_R01_dispatch.json")},ensure_ascii=False))
raise SystemExit(run.returncode)
