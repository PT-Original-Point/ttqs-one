import collections,json,pathlib
p=pathlib.Path(__file__).with_name("RAW_STDOUT_W2_R10.jsonl")
evs=[json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
print("EVENT_COUNTS",collections.Counter(e.get("event","?") for e in evs))
steps=[e.get("step_update",{}) for e in evs if e.get("event")=="step_update"]
print("STEP_KEYS",collections.Counter(k for s in steps for k in s.keys()))
for s in steps[:4]:
    print("STEP_SAMPLE",json.dumps({k:(v if isinstance(v,(str,int,float,bool,type(None))) else type(v).__name__) for k,v in s.items()},ensure_ascii=False))
tool=[]
for e in evs:
    raw=json.dumps(e,ensure_ascii=False).lower()
    if any(x in raw for x in ('tool_call','toolcall','tool_use','tooluse','command_status','call_mcp_tool','read_file','write_file')):
        tool.append(e)
print("TOOL_MENTIONED_EVENT_COUNT",len(tool))
print("TOOL_EVENT_NAMES",collections.Counter(e.get("event","?") for e in tool))
print("TOOL_EXAMPLES",json.dumps([{k:v for k,v in e.items() if k!="step_update"}|{"step_update_keys":list(e.get("step_update",{}).keys())} for e in tool[:8]],ensure_ascii=False)[:3000])