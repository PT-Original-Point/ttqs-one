import json, pathlib
p=pathlib.Path(__file__).with_name("RAW_STDOUT_W2_R10.jsonl")
events=[json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
print("FIRST_KEYS",list(events[0].keys()))
print("FIRST",json.dumps(events[0],ensure_ascii=False)[:1000])
print("LAST_KEYS",list(events[-1].keys()))
print("LAST",json.dumps(events[-1],ensure_ascii=False,indent=2)[:15000])