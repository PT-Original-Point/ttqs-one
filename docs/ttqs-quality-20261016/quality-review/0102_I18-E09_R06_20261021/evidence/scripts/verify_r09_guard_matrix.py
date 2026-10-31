import csv, hashlib, json, platform, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[2]
e=json.loads((root/"evidence/r09_guard_test_matrix_T01_T14_20261021.json").read_text(encoding="utf-8"))
o=json.loads((root/"evidence/r09_os_worker_panel_scheduler_reconciliation_20261021.json").read_text(encoding="utf-8"))
r=json.loads((root/"evidence/github_readback_receipt_0102_R06_R09.json").read_text(encoding="utf-8"))
w=json.loads((root/"writer/opencode_writer_execution_receipt_0102_R01_PUBLIC.json").read_text(encoding="utf-8"))
v=json.loads((root/"evidence/visual_qa_receipt_0102_R06_R09.json").read_text(encoding="utf-8"))
t=json.loads((root/"evidence/technical_qa_receipt_0102_R06.json").read_text(encoding="utf-8"))
s=json.loads((root/"review/semantic_review_status_0102_R06.json").read_text(encoding="utf-8"))
items={x["id"]:x for x in e["tests"]}
assert set(items)=={f"T{i:02d}" for i in range(1,15)}
assert items["T01"]["result"]=="PASS_GUARD" and o["worker_lane"]["opencode_service_is_not_writer"]
assert items["T02"]["result"]=="UNKNOWN_RETAINED" and o["worker_lane"]["winword_embedding_instances_owner_unknown"]==19
assert items["T03"]["result"]=="UNKNOWN" and o["panel"]["alignment"]=="UNKNOWN"
assert items["T04"]["result"]=="PASS_GUARD" and o["panel"]["live_http_port_8765"]=="CONNECTION_REFUSED"
assert items["T05"]["result"]=="FAIL_RECOVERY" and o["goal"]["status"]=="PAUSED" and "INTERVAL=2" in o["scheduler"]["rrule"]
assert items["T06"]["result"]=="PASS_GUARD" and (root/"source/SOURCE_PACKET_0102_I18-E09_R01.md").is_file() and (root/"source/UNIQUE_BLUEPRINT_0102_I18-E09_R01.md").is_file()
assert items["T07"]["result"]=="PASS_GUARD" and (root/"candidate"/next(x.name for x in (root/"candidate").glob("*R06.docx"))).is_file()
simulated_complete=lambda exit_code,artifact_present: exit_code==0 and artifact_present
assert items["T08"]["result"]=="PASS_SIMULATED" and not simulated_complete(0,False)
assert items["T09"]["result"]=="PASS_GUARD" and w["cli_exit_code"]==1 and (root/"writer/opencode_writer_manuscript_0102_R01_raw.md").is_file()
assert items["T10"]["result"]=="PASS_GUARD" and s["independent_semantic_review"]=="PENDING"
assert items["T11"]["result"]=="UNKNOWN" and o["worker_lane"]["antigravity_provider_model_fallback_billing"]=="UNKNOWN"
assert items["T12"]["result"]=="PARTIAL" and v["pdf_page_count"]==53 and t["docx_sha256"]==v["docx_sha256"]
assert items["T13"]["result"]=="PASS_GUARD" and r["all_git_blobs_match"] and r["docx_sha256_local"]==r["docx_sha256_remote"] and r["pdf_sha256_local"]==r["pdf_sha256_remote"]
assert items["T14"]["result"]=="UNKNOWN_RETAINED" and not o["worker_lane"]["new_worker_dispatch_this_turn"]
result={
    "schema":"ttqs-one-r09-guard-test-run-v1",
    "run_id":"0102-R06-R09-20261021-final-local-run",
    "executed_at_utc":datetime.now(timezone.utc).isoformat(),
    "execution_location":"Windows local workspace E:\\TTQS detached publish worktree",
    "python_executable":sys.executable,
    "python_version":platform.python_version(),
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "tests":14,
    "assertions_passed":14,
    "operational_overall":"PARTIAL_NOT_AUTONOMOUS_RESUME_PASS",
    "simulated_cases":1,
    "live_scheduler_trigger_tested":False,
    "provider_billing_tested":False,
    "test_results":[{"id":f"T{i:02d}","result":items[f"T{i:02d}"]["result"]} for i in range(1,15)],
    "limitations":[
        "This is a local assertion-based guard matrix run, not a live two-hour scheduler trigger.",
        "Goal remains PAUSED; this harness does not resume or mutate Goal state.",
        "The 19 WINWORD embedding process owners remain UNKNOWN and were retained.",
        "Independent semantic review for 0102 exact SHA remains PENDING.",
        "Antigravity provider/model identity and current billing/quota remain UNKNOWN."
    ]
}
out=root/"evidence/r09_guard_test_run_receipt_20261021.json"
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"receipt":str(out),"tests":14,"assertions_passed":14,"operational_overall":result["operational_overall"],"receipt_sha256":hashlib.sha256(out.read_bytes()).hexdigest()},ensure_ascii=False,indent=2))
