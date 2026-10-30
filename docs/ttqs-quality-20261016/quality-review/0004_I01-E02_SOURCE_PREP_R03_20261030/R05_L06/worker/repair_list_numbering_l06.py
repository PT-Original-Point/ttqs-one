from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from lxml import etree

ROOT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0004_I01-E02_SOURCE_PREP_R03_20261030")
SOURCE = ROOT / "docx" / "0004_I01-E02_R05_L05.docx"
OUTPUT = ROOT / "docx" / "0004_I01-E02_R05_L06.docx"
RECEIPT = ROOT / "qa" / "NUMBERING_REPAIR_RECEIPT_R05_L06.json"
EXPECTED_SOURCE_SHA256 = "be55d8f06dd0179cf043cfd4c48ba76bbdb8c110de109a111d8c58dc91b48f85"
NS_URI = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": NS_URI}
W = f"{{{NS_URI}}}"
GROUPS = [
    ("6.2 對帳等式驗證結果", 4),
    ("8.1 缺漏值與更正歷程管制", 2),
    ("8.2 拒答與撤回程序", 2),
    ("8.3 去識別化與最小存取權限", 2),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def paragraph_text(p) -> str:
    return "".join(t.text or "" for t in p.findall(".//w:t", NS)).strip()


def paragraph_style(p) -> str | None:
    ppr = p.find("w:pPr", NS)
    style = ppr.find("w:pStyle", NS) if ppr is not None else None
    return style.get(W + "val") if style is not None else None


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(SOURCE)
    if OUTPUT.exists() or RECEIPT.exists():
        raise FileExistsError("Refusing to overwrite an existing L06 candidate or receipt")
    source_sha = sha256(SOURCE)
    if source_sha != EXPECTED_SOURCE_SHA256:
        raise ValueError(f"Source SHA mismatch: {source_sha}")

    with zipfile.ZipFile(SOURCE, "r") as zin:
        bad = zin.testzip()
        if bad:
            raise ValueError(f"Source package integrity failure: {bad}")
        document = etree.fromstring(zin.read("word/document.xml"))
        numbering = etree.fromstring(zin.read("word/numbering.xml"))
        body = document.find("w:body", NS)
        paragraphs = body.findall("w:p", NS)

        style_root = etree.fromstring(zin.read("word/styles.xml"))
        list_number_style = next(
            (s for s in style_root.findall("w:style", NS) if s.get(W + "styleId") == "ListNumber"),
            None,
        )
        if list_number_style is None:
            raise ValueError("ListNumber style is missing")
        style_num = list_number_style.find("w:pPr/w:numPr/w:numId", NS)
        if style_num is None:
            raise ValueError("ListNumber style does not reference an expected numbering instance")
        style_num_id = style_num.get(W + "val")
        base_num = next((n for n in numbering.findall("w:num", NS) if n.get(W + "numId") == style_num_id), None)
        if base_num is None:
            raise ValueError(f"Style numId {style_num_id} is missing from numbering.xml")
        abstract_ref = base_num.find("w:abstractNumId", NS)
        if abstract_ref is None:
            raise ValueError("Base numbering instance has no abstractNumId")
        abstract_num_id = abstract_ref.get(W + "val")

        max_num_id = max(int(n.get(W + "numId")) for n in numbering.findall("w:num", NS))
        assignments = []
        for offset, (heading_prefix, expected_count) in enumerate(GROUPS, start=1):
            heading_index = next(
                (i for i, p in enumerate(paragraphs) if paragraph_text(p).startswith(heading_prefix)),
                None,
            )
            if heading_index is None:
                raise ValueError(f"Heading not found: {heading_prefix}")
            group = []
            for p in paragraphs[heading_index + 1 :]:
                style = paragraph_style(p)
                if style in {"Heading1", "Heading2", "Heading3", "Heading4"}:
                    break
                if style == "ListNumber":
                    group.append(p)
            if len(group) != expected_count:
                raise ValueError(f"{heading_prefix}: expected {expected_count} numbered paragraphs, found {len(group)}")

            new_num_id = str(max_num_id + offset)
            new_num = etree.SubElement(numbering, W + "num")
            new_num.set(W + "numId", new_num_id)
            abstract = etree.SubElement(new_num, W + "abstractNumId")
            abstract.set(W + "val", abstract_num_id)
            override = etree.SubElement(new_num, W + "lvlOverride")
            override.set(W + "ilvl", "0")
            start = etree.SubElement(override, W + "startOverride")
            start.set(W + "val", "1")

            texts = []
            for p in group:
                ppr = p.find("w:pPr", NS)
                if ppr is None:
                    ppr = etree.Element(W + "pPr")
                    p.insert(0, ppr)
                if ppr.find("w:numPr", NS) is not None:
                    raise ValueError(f"Unexpected direct numPr in {heading_prefix}; refusing to overwrite")
                numpr = etree.SubElement(ppr, W + "numPr")
                ilvl = etree.SubElement(numpr, W + "ilvl")
                ilvl.set(W + "val", "0")
                numid = etree.SubElement(numpr, W + "numId")
                numid.set(W + "val", new_num_id)
                texts.append(paragraph_text(p))
            assignments.append({
                "section": heading_prefix,
                "paragraph_count": len(group),
                "num_id": int(new_num_id),
                "start_value": 1,
                "paragraph_text_sha256": [hashlib.sha256(t.encode("utf-8")).hexdigest() for t in texts],
            })

        with zipfile.ZipFile(OUTPUT, "w") as zout:
            for info in zin.infolist():
                if info.filename == "word/document.xml":
                    data = etree.tostring(document, xml_declaration=True, encoding="UTF-8", standalone=True)
                elif info.filename == "word/numbering.xml":
                    data = etree.tostring(numbering, xml_declaration=True, encoding="UTF-8", standalone=True)
                else:
                    data = zin.read(info.filename)
                zout.writestr(info, data)

    with zipfile.ZipFile(OUTPUT, "r") as zout:
        bad = zout.testzip()
        if bad:
            raise ValueError(f"Output package integrity failure: {bad}")
        doc_after = etree.fromstring(zout.read("word/document.xml"))
        numbering_after = etree.fromstring(zout.read("word/numbering.xml"))
        current_nums = {n.get(W + "numId") for n in numbering_after.findall("w:num", NS)}
        for item in assignments:
            if str(item["num_id"]) not in current_nums:
                raise ValueError(f"Missing restarted numbering definition {item['num_id']}")
        # Content XML text must remain byte-for-byte identical at the text-node level.
        before_root = etree.fromstring(zipfile.ZipFile(SOURCE).read("word/document.xml"))
        before_text = [t.text for t in before_root.findall(".//w:t", NS)]
        after_text = [t.text for t in doc_after.findall(".//w:t", NS)]
        if before_text != after_text:
            raise ValueError("Text nodes changed during list-numbering-only repair")

    receipt = {
        "status": "REPAIR_APPLIED_CONTENT_UNCHANGED",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "official_checkbox_project_serial": "002",
        "source_docx": SOURCE.name,
        "source_docx_sha256": source_sha,
        "candidate_docx": OUTPUT.name,
        "candidate_docx_sha256": sha256(OUTPUT),
        "source_manuscript_sha256": sha256(ROOT / "worker" / "0004_WRITER_MANUSCRIPT_CANDIDATE_R05.md"),
        "change_scope": "Restart independent Word list numbering in four specified sections; preserve all document text nodes and all other package members.",
        "changed_package_parts": ["word/document.xml", "word/numbering.xml"],
        "base_style_num_id": int(style_num_id),
        "abstract_num_id": int(abstract_num_id),
        "groups": assignments,
        "verification": {
            "source_and_output_zip_integrity": "PASS",
            "document_text_nodes_unchanged": "PASS",
            "four_independent_groups_restart_at_1": "PASS",
            "native_word_open_export_and_visual_check": "PENDING",
            "independent_semantic_review_exact_sha": "PENDING",
            "formal_acceptance": "UNKNOWN",
        },
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"candidate": str(OUTPUT), "sha256": receipt["candidate_docx_sha256"], "receipt": str(RECEIPT), "groups": assignments}, ensure_ascii=False))


if __name__ == "__main__":
    main()
