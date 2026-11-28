from pathlib import Path
import hashlib, json

root = Path(__file__).resolve().parent
source = root / "source"
blob_ids = {
    "SOURCE_PACKET_0136_I19-E26_R01.md": "6145ea6f27beb6950aefe95a92292bbb0b49838b",
    "UNIQUE_BLUEPRINT_0136_I19-E26_R01.md": "13fbafe5b0a8fbe3c83053a7be0dc7cf9c885743",
    "OFFICIAL_SOURCE_P8_P9_TEXT.txt": "a0eb83ae4e8fe7c9389f727ba023e1ed3521709d",
    "OFFICIAL_SOURCE_P8_P9_EXTRACT.pdf": "10cfe4c0d53b027c3d0eeefcfe50d144587c998e",
    "PROJECT_157_INDEX150_AND_NEIGHBORS.md": "40f5f357ac0b88b29536aef6f6463df21b7c3c1e",
    "official_129_to_142_crosswalk.csv": "1ac4a8419088d947947031b758e29c35a3606514",
}
files = []
for name, blob in blob_ids.items():
    data = (source / name).read_bytes()
    files.append({"path": name, "git_blob_oid_at_source_commit": blob,
                  "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
manifest = {
    "project_id": "TTQS_ONE",
    "doc_id": "0136",
    "official_requirement_id": "I19-E26",
    "project_157_index": 150,
    "official_printed_checkbox_serial": "UNKNOWN",
    "source_commit": "a19293ffae3096c5f7306d851b1fc1659ee8e82e",
    "files": files,
    "note": "Git blob OIDs are Git SHA-1 object identifiers; the independent SHA-256 values identify the exact local source bytes."
}
(root / "SOURCE_MATERIAL_MANIFEST_0136_R02.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(manifest, ensure_ascii=False))
