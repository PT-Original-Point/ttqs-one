import json
import sys
from pathlib import Path

sys.stdout.reconfigure(errors="backslashreplace")
p = Path(__file__).with_name("opencode_longcat_R01_stdout.jsonl")
for number, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
    try:
        event = json.loads(line)
    except Exception as exc:
        print(f"{number}: INVALID_JSON {exc}")
        continue
    typ = event.get("type")
    part = event.get("part") or {}
    if typ == "error":
        print(f"{number}: ERROR {json.dumps(event.get('error'), ensure_ascii=False)[:800]}")
    elif typ == "tool_use":
        state = part.get("state") or {}
        print(f"{number}: TOOL {part.get('tool')} status={state.get('status')} title={state.get('title')} input={json.dumps(state.get('input'), ensure_ascii=False)[:300]} output={str(state.get('output'))[:700]}")
    elif typ == "text" or part.get("type") == "text":
        print(f"{number}: TEXT {str(part.get('text') or event.get('text') or '')[:1200]}")
    elif typ == "step_finish":
        print(f"{number}: FINISH reason={part.get('reason')} cost={part.get('cost')} tokens={json.dumps(part.get('tokens'), ensure_ascii=False)}")
    elif typ in ("message_end", "turn_end", "step_start"):
        continue
    else:
        print(f"{number}: TYPE {typ} part_type={part.get('type')} keys={','.join(part.keys())}")
