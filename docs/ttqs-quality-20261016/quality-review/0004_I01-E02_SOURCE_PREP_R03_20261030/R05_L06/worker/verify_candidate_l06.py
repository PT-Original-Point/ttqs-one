from __future__ import annotations

import csv
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from docx import Document
from lxml import etree
from pypdf import PdfReader

ROOT = Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0004_I01-E02_SOURCE_PREP_R03_20261030")
SOURCE = ROOT / "docx" / "0004_I01-E02_R05_L05.docx"
DOCX = ROOT / "docx" / "0004_I01-E02_R05_L06.docx"
PDF = ROOT / "render" / "0004_I01-E02_R05_L06_WordNative.pdf"
REGISTER = ROOT / "SYNTHETIC_REPLACEMENT_REGISTER_PLAN_0004_R05.csv"
PREVIOUS_QA = ROOT / "qa" / "TECHNICAL_QA_R05_L05.json"
RECEIPT = ROOT / "qa" / "TECHNICAL_QA_R05_L06.json"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{" + NS["w"] + "}"


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    old_sha = sha(SOURCE)
    docx_sha = sha(DOCX)
    pdf_sha = sha(PDF)
    with PREVIOUS_QA.open(encoding="utf-8") as f:
        old_qa = json.load(f)
    assert old_qa["docx_sha256"] == old_sha

    with zipfile.ZipFile(SOURCE) as old_zip, zipfile.ZipFile(DOCX) as new_zip:
        assert old_zip.testzip() is None and new_zip.testzip() is None
        old_doc_xml = etree.fromstring(old_zip.read("word/document.xml"))
        new_doc_xml = etree.fromstring(new_zip.read("word/document.xml"))
        old_text = [x.text for x in old_doc_xml.findall(".//w:t", NS)]
        new_text = [x.text for x in new_doc_xml.findall(".//w:t", NS)]
        assert old_text == new_text, "Document text nodes changed"
        old_run_props = [etree.tostring(x) for x in old_doc_xml.findall(".//w:rPr", NS)]
        new_run_props = [etree.tostring(x) for x in new_doc_xml.findall(".//w:rPr", NS)]
        assert old_run_props == new_run_props, "Text run formatting changed"
        for part in old_zip.namelist():
            if part not in {"word/document.xml", "word/numbering.xml"}:
                assert old_zip.read(part) == new_zip.read(part), f"Unexpected package part changed: {part}"
        numbering = etree.fromstring(new_zip.read("word/numbering.xml"))
        nums = {n.get(W + "numId"): n for n in numbering.findall("w:num", NS)}
        paragraphs = new_doc_xml.findall(".//w:body/w:p", NS)
        groups = [
            ("6.2 對帳等式驗證結果", ["篩選流向平衡式：", "邀請流向平衡式：", "有效判定平衡式：", "收件事件平衡式："]),
            ("8.1 缺漏值與更正歷程管制", ["缺漏欄位判定：", "更正軌跡留存（擬議流程）："]),
            ("8.2 拒答與撤回程序", ["拒絕受訪：", "同意撤回："]),
            ("8.3 去識別化與最小存取權限", ["全面去識別化：", "最小存取限制："]),
        ]
        group_results = []
        for heading, expected_labels in groups:
            hidx = next(i for i, p in enumerate(paragraphs) if "".join(p.xpath(".//w:t/text()", namespaces=NS)).startswith(heading))
            got = []
            for p in paragraphs[hidx + 1 :]:
                st = p.find("w:pPr/w:pStyle", NS)
                style = st.get(W + "val") if st is not None else None
                if style in {"Heading1", "Heading2", "Heading3", "Heading4"}:
                    break
                if style == "ListNumber":
                    got.append(p)
            assert len(got) == len(expected_labels), f"Wrong list count under {heading}"
            assigned = []
            for p, label in zip(got, expected_labels):
                text = "".join(p.xpath(".//w:t/text()", namespaces=NS))
                assert text.startswith(label), f"Unexpected list item under {heading}: {text[:50]}"
                numpr = p.find("w:pPr/w:numPr", NS)
                assert numpr is not None, f"Missing direct restart under {heading}"
                num_id = numpr.find("w:numId", NS).get(W + "val")
                num_def = nums[num_id]
                start = num_def.find("w:lvlOverride/w:startOverride", NS)
                assert start is not None and start.get(W + "val") == "1"
                assigned.append(int(num_id))
            assert len(set(assigned)) == 1, f"List items split across numbering definitions under {heading}"
            group_results.append({"section": heading, "item_count": len(got), "num_id": assigned[0], "start_value": 1})

    d = Document(str(DOCX))
    all_docx_text = "\n".join([p.text for p in d.paragraphs] + [c.text for t in d.tables for row in t.rows for c in row.cells])
    with REGISTER.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    fact_ids = sorted({row["fact_id"].strip() for row in rows if row.get("fact_id", "").strip()})
    missing = [fid for fid in fact_ids if fid not in all_docx_text]
    assert len(fact_ids) == 104 and not missing

    pdf = PdfReader(str(PDF))
    assert len(pdf.pages) == 21
    page_text = [p.extract_text() or "" for p in pdf.pages]
    expected_markers = {
        13: ["1. 篩選流向平衡式：", "2. 邀請流向平衡式："],
        14: ["3. 有效判定平衡式：", "4. 收件事件平衡式："],
        15: ["1. 缺漏欄位判定：", "2. 更正軌跡留存（擬議流程）："],
        16: ["1. 拒絕受訪：", "2. 同意撤回：", "1. 全面去識別化：", "2. 最小存取限制："],
    }
    marker_results = {}
    for page, markers in expected_markers.items():
        text = page_text[page - 1]
        for marker in markers:
            assert marker in text, f"Expected numbering marker missing on page {page}: {marker}"
        marker_results[str(page)] = markers

    receipt = {
        "receipt_id": "TECHNICAL_QA_R05_L06",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "doc_id": "0004",
        "requirement_id": "I01-E02",
        "official_checkbox_project_serial": "002",
        "source_l05_docx_sha256": old_sha,
        "docx_sha256": docx_sha,
        "docx_bytes": DOCX.stat().st_size,
        "pdf_sha256": pdf_sha,
        "source_manuscript_sha256": sha(ROOT / "worker" / "0004_WRITER_MANUSCRIPT_CANDIDATE_R05.md"),
        "synthetic_register_sha256": sha(REGISTER),
        "python_docx_reopen": "PASS",
        "zip_integrity": "PASS",
        "paragraph_count": len(d.paragraphs),
        "table_count": len(d.tables),
        "register_fact_id_count": len(fact_ids),
        "register_fact_id_unique_count": len(fact_ids),
        "missing_fact_ids_in_docx": missing,
        "body_explicit_font_min_pt": old_qa["body_explicit_font_min_pt"],
        "body_below_10_5_count": old_qa["body_below_10_5_count"],
        "table_explicit_font_min_pt": old_qa["table_explicit_font_min_pt"],
        "table_below_9_5_count": old_qa["table_below_9_5_count"],
        "font_scope_inheritance": "PASS: all w:rPr nodes and all document text nodes match L05; only paragraph numbering properties and numbering.xml changed",
        "numbering_restart_groups": group_results,
        "pdf_visible_numbering_markers": marker_results,
        "pdf_pages": len(pdf.pages),
        "word_native_export": "PASS; Word opened candidate read-only and exported PDF; process PID capture was unavailable due a PowerShell reserved-variable collision; no new WINWORD PID remained after close",
        "visual_full_document_review": "PENDING",
        "independent_semantic_review_exact_sha": "PENDING",
        "status": "PASS_TECHNICAL_CANDIDATE_ONLY",
        "formal_acceptance": "UNKNOWN",
        "real_execution": "UNKNOWN",
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"docx_sha256": docx_sha, "pdf_sha256": pdf_sha, "pages": len(pdf.pages), "tables": len(d.tables), "fact_ids": len(fact_ids), "groups": group_results, "status": receipt["status"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
