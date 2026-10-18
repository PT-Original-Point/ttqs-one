import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

base = Path(r"E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0059_R01")
out = base / "review" / "opencode_deepseek_blueprint_R02"
source = base / "worker" / "opencode" / "0059_UNIQUE_BLUEPRINT_R01_DRAFT.md"
body = base / "worker" / "opencode" / "0059_DOCUMENT_BODY_R03_FINAL.md"
docx = base / "0059_R03.docx"
patch_path = out / "model_patch_response_R02.json"
target = base / "worker" / "opencode" / "0059_UNIQUE_BLUEPRINT_R02.md"

def sha(b):
    return hashlib.sha256(b).hexdigest().upper()

source_bytes = source.read_bytes()
bom = source_bytes.startswith(b"\xef\xbb\xbf")
text = source_bytes.decode("utf-8-sig")
before_docx = sha(docx.read_bytes())
patch = json.loads(patch_path.read_text(encoding="utf-8-sig"))
assert patch["candidate_docx_sha256"].upper() == before_docx
changes = []
for item in patch["replacements"]:
    old = item["search_exact"]
    new = item["replace_with"]
    count = text.count(old)
    expected = int(item["expected_occurrences"])
    assert count == expected, {"search": old, "expected": expected, "actual": count}
    text = text.replace(old, new)
    changes.append({
        "body_locator": item["body_locator"],
        "expected_occurrences": expected,
        "applied_occurrences": count,
        "reason": item["reason"],
        "search_sha256": sha(old.encode("utf-8")),
        "replacement_sha256": sha(new.encode("utf-8")),
    })
new_bytes = (b"\xef\xbb\xbf" if bom else b"") + text.encode("utf-8")
target.write_bytes(new_bytes)

assert not re.search(r"機制有用性指數\s*4\.2／5", text)
assert "結訓後第 6 週" not in text
assert "結訓後第 6 週（113 年 8 月），或參與機制後 2 週內" not in text
assert "完成獨立查證 12 件" not in text
assert "證照查證完成率" not in text
assert "11 年 12 月 15 日" not in text
assert "113 年 12 月 15 日" in text
assert "情境內合成流程比對 12 件（非外部查證）" in text
assert "209÷51" in text
after_docx = sha(docx.read_bytes())
assert before_docx == after_docx

receipt = {
    "project_id": "TTQS_ONE",
    "doc_id": "0059",
    "requirement_id": "I13-E03",
    "official_checkbox_serial": "063",
    "candidate_docx_sha256_before": before_docx,
    "candidate_docx_sha256_after": after_docx,
    "source_blueprint_r01_path": str(source),
    "source_blueprint_r01_sha256": sha(source_bytes),
    "body_r03_sha256": sha(body.read_bytes()),
    "model_patch_response_sha256": sha(patch_path.read_bytes()),
    "blueprint_r02_path": str(target),
    "blueprint_r02_sha256": sha(new_bytes),
    "replacement_count": len(changes),
    "replacements": changes,
    "unresolved_items_from_writer": patch.get("unresolved", []),
    "docx_modified": False,
    "status": "PATCH_APPLIED_AWAITING_INDEPENDENT_BLUEPRINT_REVIEW",
    "created_at_local": datetime.now().astimezone().isoformat(timespec="seconds"),
}
(out / "blueprint_patch_receipt_R02.json").write_text(
    json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({
    "blueprint_r01_sha256": receipt["source_blueprint_r01_sha256"],
    "blueprint_r02_sha256": receipt["blueprint_r02_sha256"],
    "candidate_docx_sha256": after_docx,
    "replacements_applied": len(changes),
    "status": receipt["status"],
}, ensure_ascii=False))

