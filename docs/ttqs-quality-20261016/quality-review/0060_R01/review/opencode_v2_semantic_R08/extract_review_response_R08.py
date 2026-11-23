from __future__ import annotations

import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
RUN = BASE / "review/opencode_v2_semantic_R08/attempt01_mimo_v2_6_flash_free/stdout_R08_attempt01.jsonl"
OUT = BASE / "review/opencode_v2_semantic_R08/independent_review_response_R08.md"

events: list[str] = []
for line in RUN.read_text(encoding="utf-8").splitlines():
    if line.strip():
        event = json.loads(line)
        if event.get("type") == "text":
            text = event.get("part", {}).get("text", "")
            if text:
                events.append(text)
if not events:
    raise SystemExit("No model text events found; preserve raw stdout and do not fabricate a response")
OUT.write_text("\n\n".join(events).rstrip() + "\n", encoding="utf-8", newline="\n")
raw = OUT.read_bytes()
print(json.dumps({"output": str(OUT), "text_events": len(events), "characters": sum(map(len, events)), "sha256": hashlib.sha256(raw).hexdigest().upper(), "bytes": len(raw)}, ensure_ascii=False))
