from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "docs" / "ttqs-quality-20261016" / "quality-review" / "0084_R01"
BRANCH = "work/ttqs-one-document-quality-contract-20261016"
REF = f"origin/{BRANCH}"
PATHS = [
    "candidate/0084_R10.docx",
    "candidate/0084_R11.docx",
    "candidate/0084_R10_body.md",
    "inputs/SOURCE_PACKET_0084_R01.md",
    "inputs/UNIQUE_BLUEPRINT_0084_R03.md",
    "evidence/synthetic_replacement_register_R10.csv",
    "evidence/build_receipt_R11_final.json",
    "evidence/format_R11_appendixE.json",
    "evidence/technical_review_R11.json",
    "evidence/visual_review_R11.json",
    "evidence/render_R11_final/0084_R11.pdf",
    "evidence/render_R11_final/visual_input_manifest.json",
    "evidence/render_R11_final/contact_sheet_01.png",
    "evidence/render_R11_final/contact_sheet_02.png",
    "evidence/render_R11_final/contact_sheet_03.png",
    "evidence/render_R11_final/contact_sheet_04.png",
    "review/independent_semantic_review_R09.md",
    "review/semantic_review_packet_R11.md",
    "review/semantic_review_prompt_R11.md",
    "review/opencode_semantic_R11_request.json",
]
OUT = BASE / "evidence" / "remote_readback_R11.json"
TEXT_EXTENSIONS = {".md", ".json", ".csv", ".py", ".ps1", ".txt"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


head = subprocess.run(
    ["git", "rev-parse", REF], cwd=ROOT, check=True, capture_output=True, text=True
).stdout.strip()
results = []
for relative in PATHS:
    local_path = BASE / relative
    # SOURCE_PACKET is tracked and is part of the same directory; all paths are relative to BASE.
    local_bytes = local_path.read_bytes()
    remote = subprocess.run(
        ["git", "show", f"{REF}:docs/ttqs-quality-20261016/quality-review/0084_R01/{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    local_hash, remote_hash = sha256(local_bytes), sha256(remote)
    is_text = local_path.suffix.lower() in TEXT_EXTENSIONS
    if is_text:
        local_canonical = local_bytes.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        remote_canonical = remote.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        content_match = local_canonical == remote_canonical
    else:
        local_canonical, remote_canonical = local_bytes, remote
        content_match = local_bytes == remote
    local_blob = subprocess.run(
        ["git", "hash-object", f"--path={relative}", str(local_path)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    remote_blob = subprocess.run(
        ["git", "rev-parse", f"{REF}:docs/ttqs-quality-20261016/quality-review/0084_R01/{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    results.append({
        "path": relative.replace("\\", "/"),
        "local_sha256": local_hash,
        "remote_sha256": remote_hash,
        "line_ending_normalized_sha256_local": sha256(local_canonical),
        "line_ending_normalized_sha256_remote": sha256(remote_canonical),
        "text_line_endings_differ": is_text and local_hash != remote_hash and content_match,
        "local_git_blob_oid": local_blob,
        "remote_git_blob_oid": remote_blob,
        "git_blob_oid_match": local_blob == remote_blob,
        "content_match_after_expected_checkout_normalization": content_match,
        "match": content_match and local_blob == remote_blob,
    })

receipt = {
    "schema": "TTQS_ONE_0084_REMOTE_READBACK.v1",
    "branch": BRANCH,
    "remote_head": head,
    "checked_paths": len(results),
    "all_readbacks_match": all(item["match"] for item in results),
    "results": results,
}
OUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
if not receipt["all_readbacks_match"]:
    raise SystemExit(1)
