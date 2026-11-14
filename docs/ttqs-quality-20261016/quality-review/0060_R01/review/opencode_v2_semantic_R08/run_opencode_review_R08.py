from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
REVIEW = BASE / "review/opencode_v2_semantic_R08"
PACKET = REVIEW / "review_packet_R08.md"
DOCX = BASE / "candidate/0060_R08.docx"
PDF = BASE / "evidence/render_R08/0060_R08_Word_export.pdf"
REGISTER = BASE / "sidecar/0060_R08_SYNTHETIC_REPLACEMENT_REGISTER.csv"
REPO = BASE.parents[3]
OFFICIAL = REPO / "docs/ttqs-quality-20261016/quality-review/0058_R01/review/opencode_v2_semantic_R05/inputs/official/official_evidence_table_source.pdf"
MAPPING = REPO / "docs/ttqs-quality-20261016/quality-review/0036_R13/inputs/mapping/checkbox_mapping_compact.json"
EXE = Path(r"C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe")
MODEL = "opencode/mimo-v2.6-flash-free"
EXPECTED = "92962DF774A7A16546829D8968DC274394FC1EFCC12421C1A355F45127E9B5C3"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    for path in (PACKET, DOCX, PDF, REGISTER, OFFICIAL, MAPPING, EXE):
        if not path.is_file():
            raise SystemExit(f"Missing required file: {path}")
    before = sha(DOCX)
    if before != EXPECTED:
        raise SystemExit(f"R08 candidate SHA mismatch before dispatch: {before}")
    version = subprocess.run([str(EXE), "--version"], capture_output=True, text=True, timeout=20)
    started = datetime.now().astimezone()
    args = [str(EXE), "run", "--model", MODEL, "--format", "json",
            "--file", str(PACKET), "--file", str(DOCX), "--file", str(PDF),
            "--file", str(OFFICIAL), "--file", str(MAPPING), "--file", str(REGISTER),
            "Perform a fresh, full independent exact-SHA review of the attached DOCX 0060 R08. Follow every review instruction and return an explicit PASS, PARTIAL, or FAIL with precise locators. Do not use Computer Use."]
    run = subprocess.run(args, cwd=str(REVIEW), capture_output=True, timeout=1800)
    ended = datetime.now().astimezone()
    attempt = REVIEW / "attempt01_mimo_v2_6_flash_free"
    attempt.mkdir(parents=True, exist_ok=True)
    out, err, code = attempt / "stdout_R08_attempt01.jsonl", attempt / "stderr_R08_attempt01.txt", attempt / "exit_code_R08_attempt01.txt"
    out.write_bytes(run.stdout)
    err.write_bytes(run.stderr)
    code.write_text(str(run.returncode) + "\n", encoding="ascii")
    after = sha(DOCX)
    metadata = {
        "project_id": "TTQS_ONE", "doc_id": "0060", "requirement_id": "I14-E01", "official_checkbox": "065",
        "model_requested": MODEL, "model_attestation": "Requested model recorded by CLI; provider-side runtime identity not independently attested.",
        "cli_executable": str(EXE), "cli_version_stdout": version.stdout.strip(),
        "cli_version_stderr": version.stderr.strip(), "cli_version_exit": version.returncode,
        "argv": args, "packet_sha256": sha(PACKET), "docx_sha256_before": before,
        "pdf_sha256_before": sha(PDF), "official_pdf_sha256": sha(OFFICIAL),
        "mapping_sha256": sha(MAPPING), "register_sha256": sha(REGISTER), "docx_sha256_after": after,
        "start_time_local": started.isoformat(), "end_time_local": ended.isoformat(),
        "duration_seconds": round((ended-started).total_seconds(), 3), "exit_code": run.returncode,
        "stdout_bytes": len(run.stdout), "stdout_sha256": sha(out), "stderr_bytes": len(run.stderr),
        "stderr_sha256": sha(err), "status": "COMPLETED" if run.returncode == 0 else "FAILED",
        "candidate_unchanged": before == after, "computer_use_used": False,
    }
    (attempt / "run_R08_attempt01.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))
    if run.returncode:
        raise SystemExit(run.returncode)


if __name__ == "__main__":
    main()
