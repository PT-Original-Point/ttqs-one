from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PACKAGE = Path(__file__).resolve().parents[2]
BRANCH = "work/ttqs-one-document-quality-contract-20261016"
REMOTE_REF = f"refs/remotes/origin/{BRANCH}"
MANIFEST = PACKAGE / "evidence" / "manifest.json"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
remote_head = git("rev-parse", REMOTE_REF).decode().strip()
local_head = git("rev-parse", "HEAD").decode().strip()
if remote_head != local_head:
    raise SystemExit(f"branch readback is not current: local={local_head}; remote={remote_head}")

checks = []
prefix = "docs/ttqs-quality-20261016/quality-review/0038_R02/"
for artifact in manifest["artifacts"]:
    path = prefix + artifact["path"]
    remote_bytes = git("show", f"{REMOTE_REF}:{path}")
    actual_sha = sha256(remote_bytes)
    ok = actual_sha == artifact["sha256"] and len(remote_bytes) == artifact["bytes"]
    checks.append({"path": artifact["path"], "sha256": actual_sha, "bytes": len(remote_bytes), "status": "PASS" if ok else "FAIL"})

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
    "manifest_sha256": sha256(MANIFEST.read_bytes()),
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
print(json.dumps({k: result[k] for k in ("remote_commit", "manifest_sha256", "candidate_sha256", "pdf_sha256", "artifact_count", "verified_artifact_count", "status")}, ensure_ascii=False))
