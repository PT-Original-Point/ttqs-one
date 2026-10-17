import json
from pathlib import Path
from hashlib import sha256

here = Path(__file__).resolve().parent
raw = here / "opencode_longcat_R01_stdout.jsonl"
events = [json.loads(line) for line in raw.read_text(encoding="utf-8").splitlines() if line.strip()]
texts = []
for event in events:
    part = event.get("part") or {}
    if part.get("type") == "text" and isinstance(part.get("text"), str):
        texts.append(part["text"])
    elif event.get("type") == "text" and isinstance(event.get("text"), str):
        texts.append(event["text"])
if not texts:
    raise SystemExit("No final text response found in raw OpenCode JSONL")
response = "\n\n".join(texts)
out = here / "opencode_longcat_R01_independent_review.md"
out.write_text(response.rstrip() + "\n", encoding="utf-8")
print(f"events={len(events)} text_parts={len(texts)} response_chars={len(response)} response_sha256={sha256(out.read_bytes()).hexdigest().upper()} output={out}")
