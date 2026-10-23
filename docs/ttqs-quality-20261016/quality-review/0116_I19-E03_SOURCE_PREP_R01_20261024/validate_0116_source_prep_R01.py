import csv, json, hashlib
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / "source"
EVIDENCE = BASE / "evidence"
DATA = SRC / "SYNTHETIC_DATASET_0116_R01.csv"
REG = SRC / "SYNTHETIC_REPLACEMENT_REGISTER_0116_R01.csv"
PACKET = SRC / "SOURCE_PACKET_0116_I19-E03_R01.md"
BLUEPRINT = SRC / "UNIQUE_BLUEPRINT_0116_I19-E03_R01.md"
OUT = EVIDENCE / "source_prep_validation_R01.json"
MANIFEST = EVIDENCE / "source_manifest_0116_R01.json"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

with DATA.open("r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
with REG.open("r", encoding="utf-8-sig", newline="") as f:
    register = list(csv.DictReader(f))
assert len(rows) == 8, f"expected 8 rows, got {len(rows)}"
assert len({r["case_id"] for r in rows}) == 8
assert all(r["cohort_id"] == "SYN-0116-COHORT-01" for r in rows)
assert all(r["data_origin"] == "SAMPLE_SYNTHETIC_ONLY" for r in rows)
assert all(r["consent_status"] == "SAMPLE_ONLY_NOT_REAL_CONSENT" for r in rows)
assert all(r["evidence_class"] in {"SELF_REPORT_ONLY", "UNKNOWN"} for r in rows)
responded = [r for r in rows if r["response_status"] == "RESPONDED"]
no_response = [r for r in rows if r["response_status"] == "NO_RESPONSE"]
assert len(responded) == 6 and len(no_response) == 2
employed = [r for r in responded if r["followup_status"] in {"EMPLOYED", "SELF_EMPLOYED"}]
assert len(employed) == 4
assert all(r["evidence_index"] == "NONE_PROVIDED" for r in employed)
assert all(r["followup_status"] == "UNKNOWN" and r["evidence_class"] == "UNKNOWN" for r in no_response)
assert all(r["response_date"] == "2026-09-28" for r in responded)
assert all(r["response_date"] == "" for r in no_response)
assert all(r["followup_due_date"] == "2026-09-28" for r in rows)
assert len(register) == 8
for p in (PACKET, BLUEPRINT):
    t = p.read_text(encoding="utf-8-sig")
    assert "SAMPLE" in t and "UNKNOWN" in t and "I19-E03" in t and "127" in t
bt = BLUEPRINT.read_text(encoding="utf-8-sig")
assert "6/8=75.0%" in bt and "4/6=66.7%" in bt and "0/4=0%" in bt
assert "Q12" in bt and "REJECTED" in bt and "HOLD_PRIVACY_POLICY" in bt
assert "2026-06-30" in bt and "2026-09-28" in bt
receipt = {
  "project_id": "TTQS_ONE",
  "doc_id": "0116",
  "requirement_id": "I19-E03",
  "source_prep": "R01",
  "status": "PASS_SOURCE_PREP_VALIDATION_ONLY",
  "synthetic_rows": len(rows),
  "responded": len(responded),
  "nonresponse_unknown": len(no_response),
  "self_report_employed": len(employed),
  "response_rate": {"numerator": 6, "denominator": 8, "percent": 75.0},
  "respondent_self_report_ratio": {"numerator": 4, "denominator": 6, "percent": 66.7},
  "documentary_evidence_provided_in_synthetic_case": {"numerator": 0, "denominator": 4, "percent": 0.0},
  "real_evidence": "UNKNOWN_NOT_PROVIDED",
  "official_printed_checkbox_serial": "UNKNOWN_NOT_ASSERTED",
  "dataset_sha256": sha(DATA),
  "register_sha256": sha(REG),
  "packet_sha256": sha(PACKET),
  "blueprint_sha256": sha(BLUEPRINT),
  "assertions": [
    "eight unique synthetic IDs",
    "6/8 response rate",
    "4/6 respondents self-report employed/self-employed",
    "0/4 sample claims have evidence provided",
    "two nonresponders remain UNKNOWN",
    "consent flags are explicitly synthetic"
  ]
}
source_manifest = {
  "project_id": "TTQS_ONE",
  "doc_id": "0116",
  "requirement_id": "I19-E03",
  "source_prep": "R01",
  "source_commit": "7573bc1525e1fb40d36f72c2e8833ebf100374f6",
  "branch": "work/ttqs-one-document-quality-contract-20261016",
  "sources": {
    "official_pdf": {
      "path": "送審資料/評核依據/TTQS查核佐證文件資料表-訓練機構版 (3).pdf",
      "git_blob_sha1": "9c7621decdad585b743bf2b3d949ee5518b7bee0",
      "local_sha256": "805386b77df045b396fabafed7a47d12491c25a0b5744edd9a04876caee34709",
      "bytes": 303044,
      "pages": [7,8]
    },
    "mission": {"path":"docs/ttqs-quality-20261016/01_HUMAN_MISSION_AND_ACCEPTANCE.md","git_blob_sha1":"538bedb9d87e8465f43151933b4a5c1bfa4bbc4e"},
    "writing_manual": {"path":"docs/ttqs-quality-20261016/02_GENRE_WRITING_MANUAL.md","git_blob_sha1":"4ff863d9f534b6359fc1c7c1685bd8cce02da886"},
    "blueprints_157": {"path":"docs/ttqs-quality-20261016/03_157_CHECKBOX_BLUEPRINTS.md","git_blob_sha1":"8c2bbe7ca9dcbb03088a48934b9e57e7147ede63"},
    "official_129_to_142_crosswalk": {"path":"docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/official_129_to_142_crosswalk.csv","git_blob_sha1":"1ac4a8419088d947947031b758e29c35a3606514","row":"I19-E03,1,0,0116,學員訓後就業狀況追蹤調查表"},
    "blueprint_seed_142": {"path":"docs/ttqs-quality-20261016/quality-review/0098_R08_20261021/inputs/blueprint_seed_142.csv","git_blob_sha1":"f20ac9ae37700eb03a93b8da4407e7bf4788b602","row":"0116,I19-E03,0116__學員訓後就業狀況追蹤調查表.docx"},
    "local_129_mapping_copy": {"sha256":"bc2e70b087cc2d6904de454f967d811223f1c87257a3dae7c1dae3aee1dad45d"},
    "local_142_checklist_copy": {"sha256":"166eb3cd3d8026206e88f06cb083aa162d2ddd464d53883a3ce5ac411adcea6a"}
  },
  "outputs": {}
}
for p in (PACKET, BLUEPRINT, DATA, REG):
  source_manifest["outputs"][p.name] = {"sha256":sha(p),"bytes":p.stat().st_size}
EVIDENCE.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
MANIFEST.write_text(json.dumps(source_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))
print("MANIFEST", sha(MANIFEST))