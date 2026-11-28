#!/usr/bin/env python
"""Bounded deterministic QA for the existing 0032/I06-E03 R03 DOCX; based on the R01 QA method.

Writes only QA_RECEIPT_0032_I06-E03_R03_INDEPENDENT.json beside this script.
"""
import sys
sys.dont_write_bytecode = True
import hashlib
import json
import re
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from zipfile import ZipFile

from docx import Document
from docx.oxml.ns import qn
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table
import docx

SCRIPT = Path(__file__).resolve()
QA_DIR = SCRIPT.parent
CANDIDATE_DIR = QA_DIR.parents[1]
PREP_DIR = CANDIDATE_DIR.parent
DOCX_PATH = CANDIDATE_DIR / "0032_I06-E03_R03_LAYOUT_FLOW_REPAIR.docx"
R01_PATH = CANDIDATE_DIR / "0032_I06-E03_R01.docx"
REPAIR_RECEIPT_PATH = CANDIDATE_DIR / "qa" / "scoped_repair_r03" / "SCOPED_REPAIR_RECEIPT_R03.json"
R01_QA_SCRIPT_PATH = CANDIDATE_DIR / "qa" / "static_qa_r01_independent" / "qa_0032_i06_e03_r01_static.py"
R01_QA_RECEIPT_PATH = CANDIDATE_DIR / "qa" / "static_qa_r01_independent" / "QA_RECEIPT_0032_I06-E03_R01_INDEPENDENT.json"
R03_EXPECTED_SHA256 = "C0A0FB1FB346EAC6EEF2B7DE209E455185CF76CF4563C62FBCB96FCC2A9C546B"
R03_REPAIR_INDICES = [7, 60, 66, 72, 78, 87, 93, 99, 105]
BUILD_PATH = CANDIDATE_DIR / "BUILD_RECEIPT_0032_I06-E03_R01.json"
INPUT_PATH = CANDIDATE_DIR / "BUILDER_INPUT_0032_I06-E03_R01.json"
BUILDER_PATH = CANDIDATE_DIR / "build_0032_I06-E03_R01.py"
SOURCE_PATH = PREP_DIR / "SOURCE_PACKET_0032_I06-E03_R01.md"
BLUEPRINT_PATH = PREP_DIR / "UNIQUE_BLUEPRINT_0032_I06-E03_R01.md"
SOURCE_RECEIPT_PATH = PREP_DIR / "SHA_RECEIPT_0032_I06-E03_R01.json"
OUTPUT_PATH = QA_DIR / "QA_RECEIPT_0032_I06-E03_R03_INDEPENDENT.json"

checks = []
errors = []

def add_check(name, status, evidence):
    checks.append({"name": name, "status": status, "evidence": evidence})

def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()

def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))

def norm(value):
    return re.sub(r"\s+", "", str(value)).replace("，", ",").replace("；", ";")

def sha_text(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()

def repair_body_text(document):
    parts = []
    table_index = 0
    for element in document.element.body.iterchildren():
        if isinstance(element, CT_P):
            paragraph = Paragraph(element, document)
            if paragraph.text.strip():
                parts.append(paragraph.text)
        elif isinstance(element, CT_Tbl):
            table_index += 1
            table = Table(element, document)
            parts.append(f"\n[TABLE {table_index}]")
            for row in table.rows:
                parts.append(" | ".join(" / ".join(p.text.strip() for p in cell.paragraphs if p.text.strip()) for cell in row.cells))
            parts.append(f"[/TABLE {table_index}]\n")
    return "\n".join(parts).strip() + "\n"

def repair_body_sha(document):
    return hashlib.sha256(repair_body_text(document).encode("utf-8")).hexdigest().upper()

def repair_table_sha(document):
    rows = []
    for table in document.tables:
        for row in table.rows:
            rows.append(tuple(cell.text for cell in row.cells))
    payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()

def check(name, ok, evidence):
    add_check(name, "PASS" if ok else "FAIL", evidence)

def number(value):
    m = re.search(r"-?\d+(?:\.\d+)?", str(value).replace(",", "").strip())
    if not m:
        raise ValueError("not numeric: " + repr(value))
    return Decimal(m.group(0))

def size_from_rpr(rpr):
    if rpr is None:
        return None
    for tag in ("w:sz", "w:szCs"):
        el = rpr.find(qn(tag))
        if el is not None and el.get(qn("w:val")):
            try:
                return Decimal(el.get(qn("w:val"))) / Decimal(2)
            except InvalidOperation:
                return None
    return None

def style_size(style_id, style_map):
    seen = set()
    cur = style_id
    while cur and cur not in seen:
        seen.add(cur)
        el = style_map.get(cur)
        if el is None:
            break
        size = size_from_rpr(el.find(qn("w:rPr")))
        if size is not None:
            return size
        based = el.find(qn("w:basedOn"))
        cur = based.get(qn("w:val")) if based is not None else None
    return None

def effective_size(run, paragraph, style_map, default_size, default_char_style):
    rpr = run._r.find(qn("w:rPr"))
    size = size_from_rpr(rpr)
    if size is not None:
        return size
    rstyle = rpr.find(qn("w:rStyle")) if rpr is not None else None
    if rstyle is not None:
        size = style_size(rstyle.get(qn("w:val")), style_map)
        if size is not None:
            return size
    ppr = paragraph._p.find(qn("w:pPr"))
    size = size_from_rpr(ppr.find(qn("w:rPr")) if ppr is not None else None)
    if size is not None:
        return size
    try:
        pstyle = paragraph.style.style_id if paragraph.style else None
    except Exception:
        pstyle = None
    size = style_size(pstyle, style_map)
    if size is not None:
        return size
    if default_char_style:
        size = style_size(default_char_style, style_map)
        if size is not None:
            return size
    return default_size

def cell_paragraphs(cell):
    yield from cell.paragraphs
    for nested in cell.tables:
        for row in nested.rows:
            for subcell in row.cells:
                yield from cell_paragraphs(subcell)

def vertical_merge_continuation(cell):
    tcpr = cell._tc.find(qn("w:tcPr"))
    vm = tcpr.find(qn("w:vMerge")) if tcpr is not None else None
    return vm is not None and (vm.get(qn("w:val")) is None or vm.get(qn("w:val")) == "continue")

def expand_id_spec(value):
    m = re.fullmatch(r"(SYN-[A-Z]+-)(\d{2})(?:\s*(?:至|~|～|–|-|—)\s*(?:SYN-[A-Z]+-)?(\d{2}))?", str(value).strip())
    if not m:
        return set(), False
    prefix, first, last = m.groups()
    lo, hi = int(first), int(last) if last else int(first)
    if hi < lo or hi - lo > 999:
        return set(), False
    return {f"{prefix}{n:02d}" for n in range(lo, hi + 1)}, True

receipt = {
    "schema": "ttqs-0032-independent-static-qa/2",
    "created_at_local": datetime.now().astimezone().isoformat(timespec="seconds"),
    "scope": {
        "project_id": "TTQS_ONE", "doc_id": "0032", "requirement_id": "I06-E03",
        "qa_type": "deterministic_static_only", "docx_mutated": False,
        "semantic_review": "NOT_PERFORMED_PER_USER",
        "word_visual_render": "NOT_PERFORMED_PER_USER",
        "github_or_shared_state_touched": False,
    },
    "paths": {
        "candidate_docx": str(DOCX_PATH), "r01_baseline_docx": str(R01_PATH),
        "repair_receipt": str(REPAIR_RECEIPT_PATH), "r01_qa_script": str(R01_QA_SCRIPT_PATH),
        "r01_qa_receipt": str(R01_QA_RECEIPT_PATH), "build_receipt": str(BUILD_PATH),
        "builder_input": str(INPUT_PATH), "source_sha_receipt": str(SOURCE_RECEIPT_PATH),
        "qa_script": str(SCRIPT), "qa_receipt": str(OUTPUT_PATH),
    },
    "checks": checks, "errors": errors,
}

start_sha = None
try:
    start_sha = sha256(DOCX_PATH)
    receipt["candidate"] = {"sha256_at_start": start_sha, "bytes": DOCX_PATH.stat().st_size, "expected_sha256": R03_EXPECTED_SHA256}
    check("candidate_current_sha", start_sha == R03_EXPECTED_SHA256, {"sha256": start_sha, "expected_sha256": R03_EXPECTED_SHA256, "bytes": DOCX_PATH.stat().st_size})
except Exception as e:
    add_check("candidate_current_sha", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})
    errors.append({"stage": "candidate_hash", "error": f"{type(e).__name__}: {e}"})

build = inp = source_receipt = repair = None
input_spec = {}
try:
    repair = read_json(REPAIR_RECEIPT_PATH)
    repair_sha = sha256(REPAIR_RECEIPT_PATH)
    r01_actual_sha = sha256(R01_PATH)
    repair_indices = repair.get("paragraph_indices_zero_based", [])
    repair_changes = repair.get("run_changes", [])
    repair_binding_ok = (
        repair.get("schema") == "TTQS_ONE_0032_SCOPED_PAGEFLOW_REPAIR_R03"
        and repair.get("doc_id") == "0032"
        and repair.get("requirement_id") == "I06-E03"
        and Path(repair.get("input_candidate", "")).resolve() == R01_PATH.resolve()
        and str(repair.get("input_candidate_sha256", "")).upper() == r01_actual_sha
        and Path(repair.get("output_candidate", "")).resolve() == DOCX_PATH.resolve()
        and str(repair.get("output_candidate_sha256", "")).upper() == start_sha == R03_EXPECTED_SHA256
        and repair_indices == R03_REPAIR_INDICES
        and repair.get("run_change_count") == 9
        and len(repair_changes) == 9
        and repair.get("body_text_identical") is True
        and repair.get("table_text_identical") is True
        and repair.get("body_text_sha256_before") == repair.get("body_text_sha256_after")
        and repair.get("table_text_sha256_before") == repair.get("table_text_sha256_after")
    )
    receipt["repair_receipt_sha256"] = repair_sha
    check("r03_repair_receipt_binding", repair_binding_ok, {
        "repair_receipt_sha256": repair_sha,
        "input_candidate_sha256_actual": r01_actual_sha,
        "input_candidate_sha256_receipt": repair.get("input_candidate_sha256"),
        "output_candidate_sha256_actual": start_sha,
        "output_candidate_sha256_receipt": repair.get("output_candidate_sha256"),
        "expected_r03_sha256": R03_EXPECTED_SHA256,
        "paragraph_indices_zero_based": repair_indices,
        "run_change_count": repair.get("run_change_count"),
        "body_text_identical_claim": repair.get("body_text_identical"),
        "table_text_identical_claim": repair.get("table_text_identical"),
    })
    try:
        pageflow_doc = Document(str(DOCX_PATH))
        targets = [
            "四 對外訓練服務執行能力鏈",
            "五 訓練主管規劃與執行能力",
            "七 評核題項與證據判讀續",
            "八 加權計分與基準判定",
        ]
        children = list(pageflow_doc.element.body.iterchildren())
        findings = []
        for heading in targets:
            found = None
            for idx, element in enumerate(children):
                if isinstance(element, CT_P) and Paragraph(element, pageflow_doc).text.strip() == heading:
                    found = idx
                    break
            prev = children[found - 1] if found is not None and found > 0 else None
            page_break_before = False
            if prev is not None and isinstance(prev, CT_P):
                prev_p = Paragraph(prev, pageflow_doc)
                page_break_before = (not prev_p.text.strip() and
                    (bool(prev.xpath('.//w:br[@w:type="page"]')) or
                     bool(prev.xpath('./w:pPr/w:pageBreakBefore'))))
            heading_p = children[found] if found is not None else None
            own_page_break_before = bool(heading_p is not None and heading_p.xpath('./w:pPr/w:pageBreakBefore'))
            findings.append({"heading": heading, "found": found is not None,
                             "preceding_blank_page_break": page_break_before,
                             "heading_page_break_before": own_page_break_before})
        removed = repair.get("removed_page_breaks", [])
        pageflow_ok = (repair.get("removed_page_break_count") == 4
                       and len(removed) == 4
                       and all(x.get("page_break_paragraph_removed") is True for x in removed)
                       and all(x["found"] and not x["preceding_blank_page_break"] and not x["heading_page_break_before"] for x in findings))
        check("four_sparse_section_page_breaks_removed", pageflow_ok,
              {"receipt_removed_headings": [x.get("heading") for x in removed], "target_checks": findings,
               "receipt_removed_count": repair.get("removed_page_break_count")})
    except Exception as e:
        errors.append({"stage": "pageflow_repair_validation", "error": f"{type(e).__name__}: {e}"})
        add_check("four_sparse_section_page_breaks_removed", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})
except Exception as e:
    repair = None
    errors.append({"stage": "r03_repair_receipt", "error": f"{type(e).__name__}: {e}"})
    add_check("r03_repair_receipt_binding", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

try:
    r01_qa = read_json(R01_QA_RECEIPT_PATH)
    r01_actual_sha = sha256(R01_PATH)
    r01_receipt_sha = sha256(R01_QA_RECEIPT_PATH)
    r01_candidate_sha = str(r01_qa.get("candidate", {}).get("sha256_at_start", "")).upper()
    r01_scope = r01_qa.get("scope", {})
    r01_receipt_ok = (r01_candidate_sha == r01_actual_sha
                      and r01_scope.get("docx_mutated") is False
                      and r01_scope.get("qa_type") == "deterministic_static_only")
    receipt["r01_qa_receipt_sha256"] = r01_receipt_sha
    receipt["r01_qa_script_sha256"] = sha256(R01_QA_SCRIPT_PATH)
    check("r01_qa_receipt_binds_baseline", r01_receipt_ok, {
        "r01_docx_sha256_actual": r01_actual_sha,
        "r01_receipt_candidate_sha256": r01_candidate_sha,
        "r01_qa_receipt_sha256": r01_receipt_sha,
        "r01_qa_script_sha256": receipt["r01_qa_script_sha256"],
        "r01_summary": r01_qa.get("summary"),
        "docx_mutated": r01_scope.get("docx_mutated"),
        "qa_type": r01_scope.get("qa_type"),
    })
except Exception as e:
    errors.append({"stage": "r01_qa_baseline", "error": f"{type(e).__name__}: {e}"})
    add_check("r01_qa_receipt_binds_baseline", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

try:
    build = read_json(BUILD_PATH)
    inp = read_json(INPUT_PATH)
    source_receipt = read_json(SOURCE_RECEIPT_PATH)
    receipt["receipt_hashes"] = {
        "build_receipt_sha256": sha256(BUILD_PATH),
        "builder_input_sha256": sha256(INPUT_PATH),
        "source_sha_receipt_sha256": sha256(SOURCE_RECEIPT_PATH),
        "r03_repair_receipt_sha256": sha256(REPAIR_RECEIPT_PATH),
        "source_packet_sha256": sha256(SOURCE_PATH),
        "blueprint_sha256": sha256(BLUEPRINT_PATH),
        "builder_script_sha256": sha256(BUILDER_PATH),
    }
    expected_doc = str(build.get("output", {}).get("sha256", "")).upper()
    expected_bytes = build.get("output", {}).get("bytes")
    expected_input = str(build.get("builder_input", {}).get("sha256", "")).upper()
    expected_builder = str(build.get("builder_script", {}).get("sha256", "")).upper()
    r01_actual_sha = sha256(R01_PATH)
    check("r01_baseline_matches_build_receipt",
          bool(r01_actual_sha == expected_doc and R01_PATH.stat().st_size == expected_bytes),
          {"r01_actual_sha256": r01_actual_sha, "build_receipt_sha256": expected_doc,
           "r01_actual_bytes": R01_PATH.stat().st_size, "build_receipt_bytes": expected_bytes})
    check("builder_input_matches_build_receipt", sha256(INPUT_PATH) == expected_input,
          {"actual_sha256": sha256(INPUT_PATH), "receipt_sha256": expected_input})
    check("builder_script_matches_build_receipt", sha256(BUILDER_PATH) == expected_builder,
          {"actual_sha256": sha256(BUILDER_PATH), "receipt_sha256": expected_builder})
    check("build_receipt_identity", build.get("doc_id") == "0032" and build.get("requirement_id") == "I06-E03",
          {"doc_id": build.get("doc_id"), "requirement_id": build.get("requirement_id"), "status": build.get("status")})

    files = {
        "SOURCE_PACKET_0032_I06-E03_R01.md": SOURCE_PATH,
        "UNIQUE_BLUEPRINT_0032_I06-E03_R01.md": BLUEPRINT_PATH,
        "SHA_RECEIPT_0032_I06-E03_R01.json": SOURCE_RECEIPT_PATH,
    }
    input_bindings = inp.get("verified_sources", {})
    build_bindings = build.get("inputs", {})
    source_outputs = {o.get("name"): o for o in source_receipt.get("outputs", [])}
    binding_results = {}
    for name, path in files.items():
        actual = sha256(path)
        a = str(input_bindings.get(name, {}).get("sha256", "")).upper()
        b = str(build_bindings.get(name, {}).get("sha256", "")).upper()
        c = actual if name.startswith("SHA_RECEIPT_") else str(source_outputs.get(name, {}).get("sha256", "")).upper()
        binding_results[name] = {
            "actual_sha256": actual, "builder_input_expected_sha256": a,
            "build_receipt_expected_sha256": b, "source_receipt_expected_sha256": c,
            "pass": actual == a == b == c,
        }
    check("source_blueprint_and_sha_receipt_bindings", all(x["pass"] for x in binding_results.values()), binding_results)
    embedded = json.loads(inp.get("source_sha_receipt", "{}"))
    check("embedded_source_receipt_matches_parent_receipt", embedded == source_receipt,
          {"objects_equal": embedded == source_receipt, "embedded_schema": embedded.get("schema"),
           "parent_schema": source_receipt.get("schema")})
    embedded_texts = {}
    for key, path in (("source_packet_text", SOURCE_PATH), ("unique_blueprint_text", BLUEPRINT_PATH)):
        expected_text = path.read_text(encoding="utf-8-sig")
        actual_text = inp.get(key)
        embedded_texts[key] = {
            "text_equal": isinstance(actual_text, str) and actual_text == expected_text,
            "embedded_text_sha256": sha_text(actual_text) if isinstance(actual_text, str) else None,
            "file_text_sha256": sha_text(expected_text),
        }
    check("embedded_source_text_matches_input_files", all(x["text_equal"] for x in embedded_texts.values()), embedded_texts)
    input_spec = inp.get("content_spec", {})
except Exception as e:
    errors.append({"stage": "receipt_bindings", "error": f"{type(e).__name__}: {e}"})
    add_check("receipt_bindings", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

try:
    with ZipFile(DOCX_PATH, "r") as zf:
        bad_member = zf.testzip()
        zip_members = len(zf.namelist())
    check("docx_zip_crc", bad_member is None, {"bad_member": bad_member, "zip_members": zip_members})
except Exception as e:
    errors.append({"stage": "zip_crc", "error": f"{type(e).__name__}: {e}"})
    add_check("docx_zip_crc", "FAIL", {"error": f"{type(e).__name__}: {e}"})

doc = None
try:
    doc = Document(str(DOCX_PATH))
    check("python_docx_openability", True, {"python_docx_version": docx.__version__,
          "tables": len(doc.tables), "body_paragraphs": len(doc.paragraphs)})
except Exception as e:
    errors.append({"stage": "docx_openability", "error": f"{type(e).__name__}: {e}"})
    add_check("python_docx_openability", "FAIL", {"error": f"{type(e).__name__}: {e}"})

doc_r01 = None
try:
    doc_r01 = Document(str(R01_PATH))
    add_check("r01_baseline_openability", "PASS", {"tables": len(doc_r01.tables), "body_paragraphs": len(doc_r01.paragraphs)})
except Exception as e:
    errors.append({"stage": "r01_baseline_openability", "error": f"{type(e).__name__}: {e}"})
    add_check("r01_baseline_openability", "FAIL", {"error": f"{type(e).__name__}: {e}"})

if doc is not None and doc_r01 is not None:
    try:
        r03_body_sha = repair_body_sha(doc)
        r01_body_sha = repair_body_sha(doc_r01)
        r03_table_sha = repair_table_sha(doc)
        r01_table_sha = repair_table_sha(doc_r01)
        body_receipt_match = (repair is not None
                              and r03_body_sha == r01_body_sha
                              and r03_body_sha == repair.get("body_text_sha256_before")
                              and r03_body_sha == repair.get("body_text_sha256_after"))
        table_receipt_match = (repair is not None
                               and r03_table_sha == r01_table_sha
                               and r03_table_sha == repair.get("table_text_sha256_before")
                               and r03_table_sha == repair.get("table_text_sha256_after"))
        check("body_table_text_hashes_match_r01", body_receipt_match and table_receipt_match, {
            "body_extraction": "R03 patch script algorithm: document body XML paragraphs/tables in order; blank paragraphs omitted; UTF-8 SHA-256",
            "table_extraction": "R03 patch script algorithm: JSON compact UTF-8 list of row cell text tuples",
            "r01_body_text_sha256": r01_body_sha,
            "r03_body_text_sha256": r03_body_sha,
            "repair_body_sha256_before": repair.get("body_text_sha256_before") if repair else None,
            "repair_body_sha256_after": repair.get("body_text_sha256_after") if repair else None,
            "r01_table_text_sha256": r01_table_sha,
            "r03_table_text_sha256": r03_table_sha,
            "repair_table_sha256_before": repair.get("table_text_sha256_before") if repair else None,
            "repair_table_sha256_after": repair.get("table_text_sha256_after") if repair else None,
        })
    except Exception as e:
        errors.append({"stage": "body_table_text_hashes", "error": f"{type(e).__name__}: {e}"})
        add_check("body_table_text_hashes_match_r01", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

    try:
        changes = repair.get("run_changes", []) if repair else []
        r01_nonempty = [(i, p) for i, p in enumerate(doc_r01.paragraphs) if p.text.strip()]
        r03_nonempty = [(i, p) for i, p in enumerate(doc.paragraphs) if p.text.strip()]
        text_sequences_match = [p.text for _, p in r01_nonempty] == [p.text for _, p in r03_nonempty]
        targets = []
        for change in changes:
            pi = int(change["paragraph_index"])
            ri = int(change["run_index"])
            ordinal = sum(1 for p in doc_r01.paragraphs[:pi + 1] if p.text.strip()) - 1
            if ordinal < 0 or ordinal >= len(r01_nonempty) or ordinal >= len(r03_nonempty):
                raise IndexError(f"font repair paragraph ordinal out of range: {ordinal}")
            r01_i, r01_p = r01_nonempty[ordinal]
            r03_i, r03_p = r03_nonempty[ordinal]
            r01_run = r01_p.runs[ri]
            r03_run = r03_p.runs[ri]
            old_pt = Decimal(str(r01_run.font.size.pt)) if r01_run.font.size is not None else None
            new_pt = Decimal(str(r03_run.font.size.pt)) if r03_run.font.size is not None else None
            prefix = str(change.get("text_prefix", ""))
            targets.append({"r01_paragraph_index": r01_i, "r03_paragraph_index": r03_i,
                            "run_index": ri, "receipt_old_size_pt": change.get("old_size_pt"),
                            "r01_direct_size_pt": str(old_pt) if old_pt is not None else None,
                            "r03_direct_size_pt": str(new_pt) if new_pt is not None else None,
                            "receipt_text_prefix_matches": bool(prefix and r03_run.text.startswith(prefix)),
                            "pass": old_pt == Decimal("10.0") and new_pt == Decimal("10.5")
                                   and Decimal(str(change.get("old_size_pt"))) == Decimal("10.0")
                                   and bool(prefix and r03_run.text.startswith(prefix))})
        target_ok = (text_sequences_match and repair is not None
                     and repair.get("run_change_count") == 9
                     and len(changes) == 9 and all(item["pass"] for item in targets))
        check("nine_font_repair_targets", target_ok, {
            "nonempty_paragraph_text_sequences_match": text_sequences_match,
            "expected_run_change_count": 9,
            "receipt_run_change_count": repair.get("run_change_count") if repair else None,
            "actual_target_runs": targets,
        })
    except Exception as e:
        errors.append({"stage": "nine_font_repair_targets", "error": f"{type(e).__name__}: {e}"})
        add_check("nine_font_repair_targets", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

if doc is not None:
    # Table cells and repeated header rows.
    empty_cells, headers, cell_ids = [], [], set()
    for ti, table in enumerate(doc.tables, 1):
        marked = []
        for ri, row in enumerate(table.rows, 1):
            trpr = row._tr.find(qn("w:trPr"))
            if trpr is not None and trpr.find(qn("w:tblHeader")) is not None:
                marked.append(ri)
            for ci, cell in enumerate(row.cells, 1):
                cid = id(cell._tc)
                if cid in cell_ids or vertical_merge_continuation(cell):
                    continue
                cell_ids.add(cid)
                if not cell.text.strip():
                    empty_cells.append({"table": ti, "row": ri, "cell": ci})
        trpr = table.rows[0]._tr.find(qn("w:trPr")) if table.rows else None
        first_marked = trpr is not None and trpr.find(qn("w:tblHeader")) is not None
        first_text = any(c.text.strip() for c in table.rows[0].cells) if table.rows else False
        headers.append({"table": ti, "rows": len(table.rows), "columns": len(table.columns),
                        "repeat_header_rows": marked, "first_row_marked": first_marked,
                        "first_row_nonempty": first_text})
    check("table_cells_nonempty", not empty_cells,
          {"table_count": len(doc.tables), "unique_nonmerged_cells_checked": len(cell_ids),
           "empty_cell_count": len(empty_cells), "empty_cells": empty_cells[:50]})
    header_ok = bool(doc.tables) and all(h["first_row_marked"] and h["first_row_nonempty"] for h in headers)
    check("table_header_rows", header_ok,
          {"tables_with_repeating_first_header": sum(h["first_row_marked"] for h in headers),
           "table_count": len(doc.tables),
           "tables_without_valid_header": [h["table"] for h in headers if not (h["first_row_marked"] and h["first_row_nonempty"])]})

    text_blocks = [(f"body_paragraph_{i+1}", p.text) for i, p in enumerate(doc.paragraphs)]
    for ti, table in enumerate(doc.tables, 1):
        for ri, row in enumerate(table.rows, 1):
            for ci, cell in enumerate(row.cells, 1):
                text_blocks.append((f"table_{ti}_row_{ri}_cell_{ci}", cell.text))
    patterns = [
        ("Chinese_placeholder", re.compile(r"待填|待核|待補|待確認|請填")),
        ("English_placeholder", re.compile(r"\b(?:TODO|TBD|Lorem\s+ipsum)\b", re.I)),
        ("blank_placeholder", re.compile(r"_{3,}|\[\s*(?:name|date|insert|fill|tbd|todo)[^\]]*\]", re.I)),
    ]
    hits, allowed_real_replacement_hits, unexpected_hits = [], [], []
    for loc, text in text_blocks:
        for label, pattern in patterns:
            for m in pattern.finditer(text):
                hit = {"kind": label, "location": loc, "match": m.group(0),
                       "context": text[max(0, m.start()-50):m.end()+50]}
                hits.append(hit)
                explicit_real_area = (
                    label == "blank_placeholder"
                    and "實際評核紀錄" in text
                    and "REAL SOURCE" in text
                    and "UNKNOWN" in text
                    and "SAMPLE/SYNTHETIC" in text
                )
                (allowed_real_replacement_hits if explicit_real_area else unexpected_hits).append(hit)
    check("placeholder_terms", not unexpected_hits,
          {"total_hits": len(hits), "allowed_explicit_real_replacement_hits": len(allowed_real_replacement_hits),
           "allowed_real_replacement_locations": sorted({h["location"] for h in allowed_real_replacement_hits}),
           "unexpected_hit_count": len(unexpected_hits), "unexpected_hits": unexpected_hits[:50],
           "patterns": [name for name, _ in patterns],
           "exception_rule": "underscores allowed only in a line explicitly labeled 實際評核紀錄 and REAL SOURCE/UNKNOWN/SAMPLE-SYNTHETIC"})

    # Effective body/table font sizes from run formatting, styles, and document defaults.
    style_map, default_char_style = {}, None
    for style in doc.styles:
        el = style.element
        sid = el.get(qn("w:styleId"))
        if sid:
            style_map[sid] = el
        if el.get(qn("w:type")) == "character" and el.get(qn("w:default")) in ("1", "true", "on"):
            default_char_style = sid
    root = doc.styles.element
    defaults = root.find(qn("w:docDefaults"))
    rpd = defaults.find(qn("w:rPrDefault")) if defaults is not None else None
    default_rpr = rpd.find(qn("w:rPr")) if rpd is not None else None
    default_size = size_from_rpr(default_rpr)
    body_paras, table_paras, seen = [], [], set()
    for p in doc.paragraphs:
        if id(p._p) not in seen:
            seen.add(id(p._p)); body_paras.append(p)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell_paragraphs(cell):
                    if id(p._p) not in seen:
                        seen.add(id(p._p)); table_paras.append(p)
    def measure(paras):
        sizes, unresolved = [], []
        for pi, p in enumerate(paras, 1):
            for ri, run in enumerate(p.runs, 1):
                if not run.text.strip():
                    continue
                size = effective_size(run, p, style_map, default_size, default_char_style)
                if size is None:
                    unresolved.append({"paragraph": pi, "run": ri, "text_sample": run.text[:80]})
                else:
                    sizes.append(size)
        return sizes, unresolved
    body_sizes, body_unknown = measure(body_paras)
    table_sizes, table_unknown = measure(table_paras)
    def below_floor(paras, floor, limit=30):
        out = []
        for pi, p in enumerate(paras, 1):
            for ri, run in enumerate(p.runs, 1):
                if not run.text.strip():
                    continue
                size = effective_size(run, p, style_map, default_size, default_char_style)
                if size is not None and size < floor:
                    out.append({"paragraph": pi, "run": ri, "size_pt": str(size),
                                "text_sample": run.text[:80]})
                    if len(out) >= limit:
                        return out
        return out
    body_below = below_floor(body_paras, Decimal("10.5"))
    table_below = below_floor(table_paras, Decimal("9.5"))
    font_evidence = {
        "body_min_pt": str(min(body_sizes)) if body_sizes else None, "body_floor_pt": "10.5",
        "body_text_runs_measured": len(body_sizes), "body_unresolved_runs": body_unknown[:20],
        "body_below_floor_count_at_least": len(body_below), "body_below_floor": body_below,
        "table_min_pt": str(min(table_sizes)) if table_sizes else None, "table_floor_pt": "9.5",
        "table_text_runs_measured": len(table_sizes), "table_unresolved_runs": table_unknown[:20],
        "table_below_floor_count_at_least": len(table_below), "table_below_floor": table_below,
        "document_default_run_size_pt": str(default_size) if default_size is not None else None,
    }
    if not body_sizes or not table_sizes or body_unknown or table_unknown:
        add_check("body_and_table_font_minima", "UNKNOWN", font_evidence)
    else:
        check("body_and_table_font_minima",
              min(body_sizes) >= Decimal("10.5") and min(table_sizes) >= Decimal("9.5"),
              font_evidence)

    # Synthetic ID register and REAL replacement instructions.
    spec_facts = input_spec.get("facts", []) if isinstance(input_spec, dict) else []
    if len(doc.tables) <= 19:
        add_check("synthetic_id_register_completeness", "UNKNOWN", {"reason": "table index 19 absent"})
        add_check("real_replacement_guidance", "UNKNOWN", {"reason": "table index 19 absent"})
    else:
        reg = doc.tables[19]  # zero-based index 19; physical Word table 20
        registered, reg_rows, malformed, replacement_gaps = set(), [], [], []
        for ri, row in enumerate(reg.rows[1:], 2):
            vals = [c.text.strip() for c in row.cells]
            if len(vals) < 3 or not all(vals[:3]):
                malformed.append({"row": ri, "cells": vals})
                continue
            expanded, valid = expand_id_spec(vals[0])
            if not valid:
                malformed.append({"row": ri, "id_spec": vals[0]})
            registered.update(expanded)
            reg_rows.append({"row": ri, "id_spec": vals[0], "example": vals[1], "replacement": vals[2]})
            if not re.search(r"以|替換|重算|核定|證據|來源|UNKNOWN|原件|政策|使用|維持|不沿用|重新", vals[2], re.I):
                replacement_gaps.append({"row": ri, "id_spec": vals[0], "replacement": vals[2]})
        candidate_ids = set()
        for _, text in text_blocks:
            candidate_ids.update(re.findall(r"SYN-[A-Z]+-\d{2}", text))
        input_ids, bad_input = set(), []
        for fi, fact in enumerate(spec_facts, 1):
            if not isinstance(fact, list) or len(fact) < 3:
                bad_input.append({"index": fi, "value": str(fact)[:120]})
                continue
            expanded, valid = expand_id_spec(fact[0])
            if not valid:
                bad_input.append({"index": fi, "id_spec": fact[0]})
            input_ids.update(expanded)
        unregistered = sorted(candidate_ids - registered)
        missing_input = sorted(input_ids - registered)
        unused_registered = sorted(registered - candidate_ids)
        check("synthetic_id_register_completeness",
              not (malformed or bad_input or unregistered or missing_input),
              {"register_data_rows": len(reg_rows), "register_expanded_id_count": len(registered),
               "candidate_unique_synthetic_ids": len(candidate_ids), "builder_input_fact_specs": len(spec_facts),
               "builder_input_expanded_id_count": len(input_ids), "unregistered_candidate_ids": unregistered,
               "builder_input_ids_missing_from_register": missing_input, "unused_registered_ids": unused_registered,
               "malformed_register_rows": malformed, "malformed_builder_input_facts": bad_input})
        expected = {}
        for fact in spec_facts:
            if isinstance(fact, list) and len(fact) >= 3:
                expected[str(fact[0]).strip()] = (str(fact[1]).strip(), str(fact[2]).strip())
        replacement_parity, example_differences = [], []
        for row in reg_rows:
            pair = expected.get(row["id_spec"])
            if pair is None:
                replacement_parity.append({"id_spec": row["id_spec"], "reason": "no exact builder-input fact row"})
            else:
                if norm(row["replacement"]) != norm(pair[1]):
                    replacement_parity.append({"id_spec": row["id_spec"], "replacement_matches": False})
                if norm(row["example"]) != norm(pair[0]):
                    example_differences.append(row["id_spec"])
        check("real_replacement_guidance",
              len(reg_rows) == len(spec_facts) and not replacement_gaps and not replacement_parity,
              {"rows_with_nonempty_replacement_guidance": sum(bool(r["replacement"]) for r in reg_rows),
               "register_rows": len(reg_rows), "builder_input_fact_rows": len(spec_facts),
               "rows_missing_guidance": replacement_gaps, "replacement_parity_mismatches": replacement_parity,
               "example_text_differences_not_used_as_replacement_failures": example_differences,
               "third_party_identity_credentials_originals": build.get("synthetic_controls", {}).get("third_party_identity_credentials_and_originals") if build else None,
               "candidate_explicit_UNKNOWN_present": "UNKNOWN" in "\n".join(t for _, t in text_blocks)})

    # Score formula and table index 12 (physical Word table 13).
    actual_levels = {}
    try:
        items = input_spec.get("items", [])
        table = doc.tables[12]
        rows = table.rows[1:]
        row_results, weights, total = [], [], Decimal("0")
        rows_ok = len(rows) == len(items) == 8
        for row, item in zip(rows, items):
            cells = [c.text.strip() for c in row.cells]
            qid = str(item[0])
            weight, level, stated = number(cells[1]), number(cells[2]), number(cells[3])
            expected_weight, expected_level = Decimal(str(item[2])), Decimal(str(item[-1]))
            expected_critical = bool(item[3])
            calculated = (weight * level / Decimal(4)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            row_ok = (cells[0].split()[0] == qid and weight == expected_weight and level == expected_level
                      and stated == calculated and ((cells[4] == "是") == expected_critical))
            rows_ok = rows_ok and row_ok
            weights.append(weight); total += calculated; actual_levels[qid] = level
            row_results.append({"qid": qid, "weight": str(weight), "level": str(level),
                                "stated_weighted": str(stated), "calculated_weighted": str(calculated), "pass": row_ok})
        formula_doc = "\n".join(t for _, t in text_blocks)
        formula_present = "權重×級別÷4" in norm(formula_doc)
        weight_sum = sum(weights, Decimal("0"))
        total = total.quantize(Decimal("0.01"))
        check("scoring_formula_and_table_12",
              rows_ok and formula_present and weight_sum == Decimal("100") and total == Decimal("61.25"),
              {"table_index_0based": 12, "physical_word_table_number": 13,
               "builder_formula": input_spec.get("rules", {}).get("formula"), "formula_present": formula_present,
               "weights_sum": str(weight_sum), "calculated_total": str(total), "rows": row_results})
    except Exception as e:
        errors.append({"stage": "scoring_formula", "error": f"{type(e).__name__}: {e}"})
        add_check("scoring_formula_and_table_12", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

    # Threshold/total table index 13 (physical Word table 14).
    try:
        table = doc.tables[13]
        rows = [[c.text.strip() for c in r.cells] for r in table.rows]
        total_row = next((r for r in rows[1:] if r and "總分" in r[0]), None)
        key_row = next((r for r in rows[1:] if r and "關鍵題" in r[0]), None)
        role_row = next((r for r in rows[1:] if r and "關鍵角色" in r[0]), None)
        threshold_text = str(input_spec.get("rules", {}).get("threshold", ""))
        m = re.search(r"(?:至少|>=?\s*)(\d+(?:\.\d+)?)\s*/\s*100", threshold_text)
        threshold = Decimal(m.group(1)) if m else Decimal("75")
        critical_ids = [str(x[0]) for x in input_spec.get("items", []) if bool(x[3])]
        ok = bool(total_row and key_row and role_row)
        if total_row:
            ok = ok and re.search(rf"{re.escape(str(threshold))}\s*/\s*100", total_row[1]) is not None
            ok = ok and "61.25" in total_row[2] and "未達" in total_row[2]
        failed_critical = sorted(q for q in critical_ids if actual_levels.get(q) != Decimal("3"))
        if key_row:
            ok = ok and all(q in key_row[1] for q in critical_ids) and "3級" in key_row[1] and "未達" in key_row[2]
            ok = ok and all(q in key_row[2] for q in failed_critical)
        if role_row:
            ok = ok and "3/5" in norm(role_row[2]) and "2/5" in norm(role_row[2]) and "未達" in role_row[2]
        check("threshold_and_total_table_13", ok,
              {"table_index_0based": 13, "physical_word_table_number": 14,
               "builder_threshold": threshold_text, "expected_total_threshold": str(threshold),
               "total_row": total_row, "critical_question_row": key_row, "critical_questions": critical_ids,
               "critical_questions_below_level_3": failed_critical, "role_coverage_row": role_row})
    except Exception as e:
        errors.append({"stage": "threshold_total", "error": f"{type(e).__name__}: {e}"})
        add_check("threshold_and_total_table_13", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

    # Capacity ratio in table index 9 (physical Word table 10).
    try:
        case = input_spec.get("case", {})
        learners, seats = Decimal(str(case["learners"])), Decimal(str(case["seats"]))
        pct = (learners / seats * Decimal(100)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        rows = [[c.text.strip() for c in r.cells] for r in doc.tables[9].rows]
        capacity_row = next((r for r in rows[1:] if r and "容量利用" in r[0]), None)
        pct_string = format(pct, "f").rstrip("0").rstrip(".")
        ratio = bool(capacity_row and re.search(
            rf"(?<!\d){int(learners)}\s*名.*?(?:÷|/)\s*{int(seats)}\s*席\s*=\s*{re.escape(pct_string)}%",
            capacity_row[1]))
        check("capacity_12_of_16_equals_75_percent", ratio,
              {"table_index_0based": 9, "physical_word_table_number": 10, "learners": str(learners),
               "seats": str(seats), "calculated_percent": str(pct), "candidate_row": capacity_row})
    except Exception as e:
        errors.append({"stage": "capacity_ratio", "error": f"{type(e).__name__}: {e}"})
        add_check("capacity_12_of_16_equals_75_percent", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

    # Reassessment table index 16 (physical Word table 17).
    try:
        reeval = input_spec.get("reeval", {})
        rows = [[c.text.strip() for c in r.cells] for r in doc.tables[16].rows]
        rowmap = {r[0]: r[1:] for r in rows[1:] if len(r) >= 2}
        expected_scores = [int(x) for x in reeval.get("scores", [])]
        score_text = rowmap.get("八題級別", [""])[0]
        candidate_scores = [int(x) for x in re.findall(r"\d+", score_text)]
        total_text = rowmap.get("加權總分", [""])[0]
        date_text = rowmap.get("日期", [""])[0]
        coverage_text = rowmap.get("主責／備援", [""])[0]
        readiness_text = rowmap.get("目標追蹤", [""])[0]
        followup_text = rowmap.get("訓後追蹤", [""])[0]
        third_party = rowmap.get("第三方原件", [""])[0]
        expected_total = int(reeval.get("total", 0))
        computed_total = sum((Decimal(str(item[2])) * Decimal(str(score)) / Decimal(4)
                              for item, score in zip(input_spec.get("items", []), expected_scores)),
                             Decimal("0")).quantize(Decimal("0.01"))
        ok = (len(candidate_scores) == 8 and candidate_scores == expected_scores
              and str(reeval.get("date", "")) in date_text
              and re.search(rf"{expected_total}\s*/\s*100", total_text) is not None
              and computed_total == Decimal(expected_total)
              and coverage_text.count("5/5=100%") == 2
              and norm(reeval.get("readiness", "")) in norm(readiness_text)
              and norm(reeval.get("followup", "")) in norm(followup_text)
              and "UNKNOWN" in third_party)
        check("reassessment_values_table_16", ok,
              {"table_index_0based": 16, "physical_word_table_number": 17, "builder_input": reeval,
               "candidate_date": date_text, "candidate_scores": candidate_scores, "candidate_total": total_text,
               "calculated_total_from_weights": str(computed_total), "candidate_coverage": coverage_text,
               "candidate_readiness": readiness_text, "candidate_followup": followup_text,
               "third_party_original_status": third_party})
    except Exception as e:
        errors.append({"stage": "reassessment", "error": f"{type(e).__name__}: {e}"})
        add_check("reassessment_values_table_16", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

try:
    end_sha = sha256(DOCX_PATH)
    receipt.setdefault("candidate", {})["sha256_at_end"] = end_sha
    check("candidate_stable_during_qa", bool(start_sha and end_sha == start_sha),
          {"sha256_at_start": start_sha, "sha256_at_end": end_sha})
except Exception as e:
    errors.append({"stage": "candidate_end_hash", "error": f"{type(e).__name__}: {e}"})
    add_check("candidate_stable_during_qa", "UNKNOWN", {"error": f"{type(e).__name__}: {e}"})

try:
    receipt["qa_script_sha256"] = sha256(SCRIPT)
except Exception as e:
    receipt["qa_script_sha256"] = None
    errors.append({"stage": "script_hash", "error": f"{type(e).__name__}: {e}"})

failures = [c for c in checks if c["status"] == "FAIL"]
unknowns = [c for c in checks if c["status"] == "UNKNOWN"]
receipt["summary"] = {
    "status": "FAIL" if failures else ("PASS_WITH_UNKNOWN" if unknowns else "PASS"),
    "check_count": len(checks),
    "pass_count": sum(c["status"] == "PASS" for c in checks),
    "failure_count": len(failures),
    "unknown_count": len(unknowns),
    "failures": [c["name"] for c in failures],
    "unknowns": [{"name": c["name"], "evidence": c["evidence"]} for c in unknowns],
    "errors": errors,
}
OUTPUT_PATH.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"receipt": str(OUTPUT_PATH), "status": receipt["summary"]["status"],
                  "pass_count": receipt["summary"]["pass_count"],
                  "failure_count": receipt["summary"]["failure_count"],
                  "unknown_count": receipt["summary"]["unknown_count"],
                  "candidate_sha256": receipt.get("candidate", {}).get("sha256_at_start"),
                  "script_sha256": receipt.get("qa_script_sha256")}, ensure_ascii=True))
