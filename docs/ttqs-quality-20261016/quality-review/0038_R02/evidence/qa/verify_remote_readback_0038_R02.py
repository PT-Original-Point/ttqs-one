from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PACKAGE = Path(__file__).resolve().parents[2]
BRANCH = "work/ttqs-one-document-quality-contract-20261016"
REMOTE_REF = f"refs/remotes/origin/{BRANCH}"
MANIFEST = PACKAGE / "evidence" / "manifest.json"
PROGRESS = PACKAGE / "PROGRESS.json"
READBACK_REL = "docs/ttqs-quality-20261016/quality-review/0038_R02/evidence/qa/remote_readback_R02.json"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


TEXT_SUFFIXES = {".md", ".json", ".jsonl", ".csv", ".py", ".txt", ".ps1"}


def canonical_local_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    return data.replace(b"\r\n", b"\n") if path.suffix.lower() in TEXT_SUFFIXES else data


manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
remote_head = git("rev-parse", REMOTE_REF).decode().strip()
local_head = git("rev-parse", "HEAD").decode().strip()
if remote_head != local_head:
    raise SystemExit(f"branch readback is not current: local={local_head}; remote={remote_head}")
manifest_rel = MANIFEST.relative_to(ROOT).as_posix()
remote_manifest = git("show", f"{REMOTE_REF}:{manifest_rel}")
if remote_manifest != canonical_local_bytes(MANIFEST):
    raise SystemExit("remote manifest bytes do not match the canonical local manifest")
manifest_sha = sha256(remote_manifest)

checks = []
prefix = "docs/ttqs-quality-20261016/quality-review/0038_R02/"
for artifact in manifest["artifacts"]:
    path = prefix + artifact["path"]
    remote_bytes = git("show", f"{REMOTE_REF}:{path}")
    actual_sha = sha256(remote_bytes)
    local_bytes = canonical_local_bytes(PACKAGE / artifact["path"])
    local_canonical_matches = remote_bytes == local_bytes
    ok = actual_sha == artifact["sha256"] and len(remote_bytes) == artifact["bytes"] and local_canonical_matches
    checks.append({"path": artifact["path"], "sha256": actual_sha, "bytes": len(remote_bytes), "local_canonical_matches": local_canonical_matches, "status": "PASS" if ok else "FAIL"})

candidate = next(x for x in checks if x["path"] == "candidate/0038_R02.docx")
pdf = next(x for x in checks if x["path"] == "evidence/render/0038_R02.pdf")
ok = all(x["status"] == "PASS" for x in checks)
result = {
    "project": "TTQS_ONE",
    "document_id": "0038",
    "candidate": "0038_R02",
    "branch": BRANCH,
    "remote_commit": remote_head,
    "local_commit": local_head,
    "manifest_path": manifest_rel,
    "manifest_sha256": manifest_sha,
    "candidate_sha256": candidate["sha256"],
    "pdf_sha256": pdf["sha256"],
    "artifact_count": len(checks),
    "verified_artifact_count": sum(x["status"] == "PASS" for x in checks),
    "status": "PASS" if ok else "FAIL",
    "method": "Fresh git fetch from GitHub followed by git-show readback of each manifested remote blob and local SHA-256/byte-length comparison",
    "checks": checks,
}
out = PACKAGE / "evidence" / "qa" / "remote_readback_R02.json"
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
receipt_sha = sha256(canonical_local_bytes(out))
progress = json.loads(PROGRESS.read_text(encoding="utf-8"))
progress["remote"] = {
    "status": "PASS_EXACT_READBACK" if ok else "FAIL_EXACT_READBACK",
    "github_path": "docs/ttqs-quality-20261016/quality-review/0038_R02/",
    "verified_readback": ok,
    "verified_commit": remote_head,
    "manifest_sha256": manifest_sha,
    "candidate_sha256": candidate["sha256"],
    "pdf_sha256": pdf["sha256"],
    "artifact_count": len(checks),
    "verified_artifact_count": sum(x["status"] == "PASS" for x in checks),
    "readback_receipt": "evidence/qa/remote_readback_R02.json",
    "readback_receipt_sha256": receipt_sha,
    "verified_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "method": "Fresh GitHub branch fetch; canonical manifest verification; exact remote Git blob SHA-256 and byte-length comparison for every manifested artifact",
}
PROGRESS.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("remote_commit", "manifest_sha256", "candidate_sha256", "pdf_sha256", "artifact_count", "verified_artifact_count", "status")}, ensure_ascii=False))
if not ok:
    raise SystemExit(1)
