from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from copy import deepcopy
from pathlib import Path
from xml.etree import ElementTree as ET

from docx import Document

ROOT = Path(__file__).resolve().parents[1]
R05 = ROOT / "candidate" / "0057_R05.docx"
R06 = ROOT / "candidate" / "0057_R06.docx"
CSV_R05 = ROOT / "sidecar" / "0057_R05_SYNTHETIC_REPLACEMENT_REGISTER.csv"
JSON_R05 = ROOT / "sidecar" / "0057_R05_SYNTHETIC_REPLACEMENT_REGISTER.json"
CSV_R06 = ROOT / "sidecar" / "0057_R06_SYNTHETIC_REPLACEMENT_REGISTER.csv"
JSON_R06 = ROOT / "sidecar" / "0057_R06_SYNTHETIC_REPLACEMENT_REGISTER.json"
RECEIPT = ROOT / "build" / "0057_R06_build_receipt.md"
EXPECTED_R05 = "FCA14E2AE661D0C8BF207531FD2FA28D130176FFE8C6D1B9BE17A7052AAEEF52"
OLD_T1 = "非回覆／聯繫三次仍無法接觸、明確表示不參與留在 C，不從分母剔除；只在分子 D 計入有主波次追蹤資料者。"
NEW_T1 = "經三次聯繫仍無法接觸者，或明確表示不參與者，均保留於 C 的分母中，不從分母剔除；只有取得主波次追蹤資料者才列入有效追蹤數 D。"
OLD_MAPPING = "3 次嘗試後仍未接觸 → 聯繫三次仍無法接觸；明確表示不參與 → 明確表示不參與"
NEW_MAPPING = "三次嘗試後仍未接觸者列為失聯；明確表示不參與者列為拒訪，兩者均留在分母 C，且不列入 D"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def paragraphs(doc):
    yield from doc.paragraphs
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                yield from cell.paragraphs


def replace_paragraph_text(paragraph, old: str, new: str) -> None:
    old_text = paragraph.text
    new_text = old_text.replace(old, new)
    if new_text == old_text:
        raise RuntimeError("Target text was not present in the selected paragraph")
    old_runs = list(paragraph.runs)
    first_rpr = deepcopy(old_runs[0]._r.rPr) if old_runs and old_runs[0]._r.rPr is not None else None
    for run in old_runs:
        run._element.getparent().remove(run._element)
    run = paragraph.add_run(new_text)
    if first_rpr is not None:
        run._element.insert(0, first_rpr)


def text_blocks(doc):
    return [p.text for p in paragraphs(doc)]


def main() -> None:
    if sha256(R05) != EXPECTED_R05:
        raise RuntimeError(f"R05 exact SHA mismatch: {sha256(R05)}")
    if R06.exists() or CSV_R06.exists() or JSON_R06.exists() or RECEIPT.exists():
        raise RuntimeError("R06 output already exists; refusing to overwrite")
    if not CSV_R05.exists() or not JSON_R05.exists():
        raise RuntimeError("R05 sidecar source is missing")

    doc = Document(R05)
    before_blocks = text_blocks(doc)
    t1_matches = [p for p in paragraphs(doc) if p.text.count(OLD_T1)]
    mapping_matches = [p for p in paragraphs(doc) if p.text.count(OLD_MAPPING)]
    if len(t1_matches) != 1 or sum(p.text.count(OLD_T1) for p in t1_matches) != 1:
        raise RuntimeError(f"Expected one T1 phrase occurrence; found {sum(p.text.count(OLD_T1) for p in t1_matches)}")
    if sum(p.text.count(OLD_MAPPING) for p in mapping_matches) != 2:
        raise RuntimeError(f"Expected two duplicated mapping occurrences; found {sum(p.text.count(OLD_MAPPING) for p in mapping_matches)}")

    for p in t1_matches:
        replace_paragraph_text(p, OLD_T1, NEW_T1)
    for p in mapping_matches:
        replace_paragraph_text(p, OLD_MAPPING, NEW_MAPPING)

    R06.parent.mkdir(parents=True, exist_ok=True)
    doc.save(R06)
    shutil.copyfile(CSV_R05, CSV_R06)
    shutil.copyfile(JSON_R05, JSON_R06)

    check = Document(R06)
    after_blocks = text_blocks(check)
    expected_blocks = [b.replace(OLD_T1, NEW_T1).replace(OLD_MAPPING, NEW_MAPPING) for b in before_blocks]
    if after_blocks != expected_blocks:
        raise RuntimeError("R05→R06 text delta exceeded the three authorized phrase repairs")
    all_text = "\n".join(after_blocks)
    if OLD_T1 in all_text or OLD_MAPPING in all_text:
        raise RuntimeError("A duplicated source phrase remains")
    if all_text.count(NEW_T1) != 1 or all_text.count(NEW_MAPPING) != 2:
        raise RuntimeError("Expected corrected phrase occurrence count does not match")
    if len(check.tables) != len(Document(R05).tables) or len(check.tables) < 22 or len(check.inline_shapes) != 2:
        raise RuntimeError("Table/image inventory changed unexpectedly")
    if len(check.sections) != 5 or any(s.footer.is_linked_to_previous for s in check.sections):
        raise RuntimeError("R05 section/footer structure changed unexpectedly")
    if sha256(CSV_R05) != sha256(CSV_R06) or sha256(JSON_R05) != sha256(JSON_R06):
        raise RuntimeError("R06 register sidecars are not byte-identical to R05")
    with zipfile.ZipFile(R06) as zf:
        bad_member = zf.testzip()
        if bad_member is not None:
            raise RuntimeError(f"DOCX package integrity failure: {bad_member}")
        footers = [n for n in zf.namelist() if n.startswith("word/footer") and n.endswith(".xml")]
        if len(footers) != 5:
            raise RuntimeError(f"Expected five independent footer parts; found {len(footers)}")
        for name in footers:
            root = ET.fromstring(zf.read(name))
            page_fields = 0
            for field in root.findall(".//w:fldSimple", NS):
                if (field.get(f"{{{NS['w']}}}instr") or "").strip().upper() == "PAGE":
                    page_fields += 1
            for instr in root.findall(".//w:instrText", NS):
                if (instr.text or "").strip().upper() == "PAGE":
                    page_fields += 1
            if page_fields != 1:
                raise RuntimeError(f"Expected one PAGE field in {name}; found {page_fields}")

    r05_sha = sha256(R05)
    r06_sha = sha256(R06)
    csv_sha = sha256(CSV_R06)
    json_sha = sha256(JSON_R06)
    script_sha = sha256(Path(__file__))
    receipt = (
        "# 0057 R06 bounded phrase repair receipt\n\n"
        "## Identity\n"
        "- Document: DOCX 0057; official requirement I13-E01; checkbox 061\n"
        "- Source candidate: `candidate/0057_R05.docx`\n"
        f"- Source SHA-256: `{r05_sha}`\n"
        "- Output candidate: `candidate/0057_R06.docx`\n"
        f"- Output SHA-256: `{r06_sha}`\n"
        "- Source Blueprint: `inputs/0057_UNIQUE_BLUEPRINT_R09.md`\n"
        "- Blueprint SHA-256: `A6602B5B37250F03914A075CBAD909D469C9AAE71383BEAD85006DF334899E02`\n"
        "- Bounded patcher: `build/build_0057_R06.py`\n"
        f"- Bounded patcher SHA-256: `{script_sha}`\n\n"
        "## Changes and checks\n"
        "- Corrected one T1 sentence and two instances of the duplicated contact/refusal mapping. No numbers, dates, decisions, survey results, or evidence facts were changed.\n"
        "- Ordered paragraph/cell text comparison confirms the only text changes are the three specified phrase repairs.\n"
        "- DOCX package integrity, 22-table inventory, two inline charts, five independent sections, and exactly one PAGE field per section passed this deterministic check.\n"
        f"- R06 CSV SHA-256: `{csv_sha}`; byte-identical to R05.\n"
        f"- R06 JSON SHA-256: `{json_sha}`; byte-identical to R05.\n\n"
        "## Limits\n"
        "This receipt records a deterministic bounded patch only. It is not independent technical QA, semantic acceptance, visual approval, or formal association acceptance. Render and review the exact R06 SHA before any semantic review.\n"
    )
    RECEIPT.write_text(receipt, encoding="utf-8", newline="\n")
    print(json.dumps({
        "source_sha256": r05_sha,
        "candidate_sha256": r06_sha,
        "builder_sha256": script_sha,
        "sidecar_csv_sha256": csv_sha,
        "sidecar_json_sha256": json_sha,
        "t1_replacements": 1,
        "mapping_replacements": 2,
        "tables": len(check.tables),
        "sections": len(check.sections),
        "inline_shapes": len(check.inline_shapes),
        "status": "BUILDER_BOUNDED_PATCH_COMPLETE_NOT_ACCEPTED",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
