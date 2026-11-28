#!/usr/bin/env python3
"""Independent, read-only deterministic QA for TTQS 0035/I07-E03 R02 TW char fix.

Reads only the named candidate, source packet, Blueprint, scoped repair, and build
receipt. It never writes to those inputs. Output is one JSON report on stdout.
"""
from __future__ import annotations
import hashlib
import json
import math
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

BASE = Path(r"E:\tqrepo\docs\ttqs-quality-20261016\quality-review\0035_I07-E03_SOURCE_PREP_R01_20261118")
CANDIDATE = BASE / "candidate" / "0035_I07-E03_R02_TW_CHAR_FIX.docx"
SOURCE = BASE / "SOURCE_PACKET_0035_I07-E03_R01.md"
BLUEPRINT = BASE / "UNIQUE_BLUEPRINT_0035_I07-E03_R01.md"
REPAIR = BASE / "candidate" / "qa" / "scoped_repair_r02_worker" / "0035_I07-E03_R02_SCOPED_REPAIR.md"
BUILD_RECEIPT = BASE / "candidate" / "qa" / "static_qa_r03_carver" / "BUILD_RECEIPT_0035_I07-E03_R03.json"
EXPECTED_CANDIDATE_SHA = "0E5AB81615BA45D0A1D8008203C8696F24A3B98ADA65B99A261DC9D0DF13FF99"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{" + NS["w"] + "}"
FACT_RE = re.compile(r"SYN-0035-(\d{4})\b")
FINDING_RE = re.compile(r"SYN-0035-(F\d{2})\b")
ID_TOKEN_RE = re.compile(r"SYN-0035-[A-Z0-9]+(?:-[A-Z0-9]+)*")
PLACEHOLDER_RE = re.compile(r"待填|待核|待補|待確認|TODO|TBD|\[\s*\]|〔\s*〕|_{3,}|＿{2,}", re.I)


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def text_of(el: ET.Element) -> str:
    out = []
    for node in el.iter():
        if node.tag == W + "t":
            out.append(node.text or "")
        elif node.tag == W + "tab":
            out.append("\t")
        elif node.tag in (W + "br", W + "cr"):
            out.append("\n")
    return "".join(out)


def compact(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def check(status: str, evidence, note=""):
    return {"status": status, "evidence": evidence, **({"note": note} if note else {})}


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def extract_table(table_el: ET.Element, idx: int):
    rows = []
    for ri, row in enumerate(table_el.findall("./w:tr", NS), 1):
        cells = []
        for ci, cell in enumerate(row.findall("./w:tc", NS), 1):
            cells.append({"column": ci, "text": text_of(cell), "normalized": compact(text_of(cell))})
        rows.append({"row": ri, "cells": cells})
    return {"table": idx, "rows": rows, "row_count": len(rows), "column_counts": [len(r["cells"]) for r in rows]}


def get_cell_size(run: ET.Element):
    sz = run.find("./w:rPr/w:sz", NS)
    if sz is None:
        return None
    try:
        return int(sz.attrib.get(W + "val")) / 2.0
    except (TypeError, ValueError):
        return None


def numeric_cell(s: str):
    t = compact(s).replace("−", "-").replace(",", "")
    if re.fullmatch(r"[-+]?\d+(?:\.\d+)?", t):
        try:
            return float(t)
        except ValueError:
            return None
    return None


def matrix_from_table(table: dict):
    # Expected crosstab shape: first column category, next two cells counts, last total.
    candidate_rows = []
    for row in table["rows"]:
        vals = [numeric_cell(c["text"]) for c in row["cells"]]
        if len(vals) >= 4 and vals[1] is not None and vals[2] is not None and vals[3] is not None:
            label = " ".join(c["text"] for c in row["cells"][:1])
            if re.search(r"達成|未達成|未达成|達標|未達標", label):
                candidate_rows.append({"label": compact(label), "values": vals[1:4]})
    if len(candidate_rows) < 2:
        return {"status": "UNKNOWN", "candidate_rows": candidate_rows, "reason": "Could not deterministically identify two category rows with count/count/total cells."}
    data = candidate_rows[:2]
    m = [[int(x) for x in r["values"][:2]] for r in data]
    row_totals = [sum(r) for r in m]
    col_totals = [sum(m[i][j] for i in range(2)) for j in range(2)]
    n = sum(row_totals)
    if n <= 0:
        return {"status": "FAIL", "matrix": m, "reason": "Nonpositive sample size."}
    po = (m[0][0] + m[1][1]) / n
    pe = sum(row_totals[i] * col_totals[i] for i in range(2)) / (n * n)
    kappa = None if math.isclose(pe, 1.0) else (po - pe) / (1.0 - pe)
    totals_rows = [r for r in table["rows"] if any(re.search(r"合計|總計|总计", c["text"]) for c in r["cells"])]
    observed_totals = []
    for r in totals_rows:
        observed_totals.append([numeric_cell(c["text"]) for c in r["cells"]])
    row_cells_match = all(int(r["values"][2]) == row_totals[i] for i, r in enumerate(data))
    total_candidates = []
    for values in observed_totals:
        numeric = [int(v) for v in values if v is not None]
        if len(numeric) >= 3:
            total_candidates.append(numeric[-3:])
    totals_row = total_candidates[-1] if total_candidates else None
    totals_row_matches = totals_row == [col_totals[0], col_totals[1], n]
    return {"status": "PASS", "category_rows": data, "matrix": m, "row_totals": row_totals,
            "row_cells_match_recalculation": row_cells_match,
            "column_totals": col_totals, "n": n, "observed_final_totals": totals_row,
            "final_totals_row_matches_recalculation": totals_row_matches,
            "p_o": po, "p_e": pe, "kappa": kappa,
            "observed_total_rows": observed_totals}


def main() -> int:
    input_paths = {"candidate": CANDIDATE, "source_packet": SOURCE, "blueprint": BLUEPRINT,
                   "scoped_repair": REPAIR, "build_receipt": BUILD_RECEIPT}
    missing = [str(p) for p in input_paths.values() if not p.is_file()]
    report = {
        "report_type": "TTQS_ONE_INDEPENDENT_STATIC_QA",
        "work_id": "TTQS_ONE_0035_I07-E03_STATIC_QA_R02_CARVER",
        "scope": "0035/I07-E03 R02 deterministic static checks only; no edit, Word COM, render, visual review, or semantic acceptance",
        "inputs": {}, "checks": {}, "evidence": {},
        "limitations": ["No Word COM or rendering; physical page boundaries and page-by-page SAMPLE marking are UNKNOWN.",
                        "No semantic/source-alignment acceptance; this is deterministic static QA only.",
                        "Font gate reads explicit w:sz on text-bearing runs; inherited style behavior is not used to infer a missing direct size."],
    }
    if missing:
        report["checks"]["input_files_present"] = check("FAIL", {"missing": missing})
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 2

    for name, path in input_paths.items():
        report["inputs"][name] = {"path": str(path), "sha256": sha(path), "bytes": path.stat().st_size}
    script_path = Path(__file__).resolve()
    report["inputs"]["qa_script"] = {"path": str(script_path), "sha256": sha(script_path), "bytes": script_path.stat().st_size}
    report["inputs"]["expected_candidate_sha256"] = EXPECTED_CANDIDATE_SHA
    try:
        build = json.loads(read_utf8(BUILD_RECEIPT))
    except Exception as exc:
        report["checks"]["build_receipt_parse"] = check("FAIL", {"error": repr(exc)})
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 2

    report["evidence"]["build_receipt_claims"] = {
        "work_id": build.get("work_id"), "doc_id": build.get("doc_id"),
        "requirement_id": build.get("requirement_id"), "revision": build.get("revision"),
        "status": build.get("status"),
        "inputs": build.get("inputs"), "outputs": build.get("outputs"),
        "content_claims": {k: build.get("content", {}).get(k) for k in
                            ("paragraph_count", "output_paragraph_count", "table_count", "table_row_counts_including_header", "total_table_rows_including_header", "FACT_FINDING_ID_checks", "calculations")},
        "font_claims": build.get("OOXML_font_checks"),
    }
    # Recompute and bind every named input to the builder's receipt.
    binding_specs = [
        ("scoped_repair", "sole_body_source"),
        ("source_packet", "source_packet_metadata_only"),
        ("blueprint", "blueprint_metadata_only"),
    ]
    bindings = {}
    for local_name, receipt_key in binding_specs:
        claim = build.get("inputs", {}).get(receipt_key, {})
        actual = report["inputs"][local_name]
        bindings[local_name] = {"receipt_path": claim.get("path"), "receipt_sha256": claim.get("sha256"),
                                "actual_path": actual["path"], "actual_sha256": actual["sha256"],
                                "path_matches": str(Path(claim.get("path", ""))).casefold() == str(input_paths[local_name]).casefold(),
                                "sha_matches": claim.get("sha256", "").upper() == actual["sha256"],
                                "bytes_matches": claim.get("bytes") == actual["bytes"]}
    out_claim = build.get("outputs", {}).get("docx", {})
    candidate_actual = report["inputs"]["candidate"]
    bindings["candidate_output"] = {"receipt_path": out_claim.get("path"), "receipt_sha256": out_claim.get("sha256"),
                                    "actual_path": candidate_actual["path"], "actual_sha256": candidate_actual["sha256"],
                                    "path_matches": str(Path(out_claim.get("path", ""))).casefold() == str(CANDIDATE).casefold(),
                                    "sha_matches": out_claim.get("sha256", "").upper() == candidate_actual["sha256"],
                                    "expected_sha_matches": candidate_actual["sha256"] == EXPECTED_CANDIDATE_SHA,
                                    "bytes_matches": out_claim.get("bytes") == candidate_actual["bytes"]}
    report["evidence"]["receipt_bindings"] = bindings
    binding_good = all(v.get("path_matches") and v.get("sha_matches") and v.get("bytes_matches", True)
                       for v in bindings.values()) and bindings["candidate_output"].get("expected_sha_matches")
    report["checks"]["input_output_sha_binding"] = check("PASS" if binding_good else "FAIL", bindings)
    report["checks"]["build_receipt_parse"] = check("PASS", {"receipt_type": build.get("receipt_type"), "status": build.get("status")})

    # Cross-file identity is a deterministic metadata check, not a semantic review.
    source_text, blueprint_text, repair_text = map(read_utf8, (SOURCE, BLUEPRINT, REPAIR))
    identities = {"source_packet": source_text, "blueprint": blueprint_text, "scoped_repair": repair_text}
    metadata = {}
    for name, content in identities.items():
        metadata[name] = {
            "doc_id_0035_present": bool(re.search(r"(?<!\d)0035(?!\d)", content)),
            "requirement_I07_E03_present": bool(re.search(r"I07\s*[-–]\s*E03", content, re.I)),
            "content_sha256": report["inputs"][name]["sha256"],
        }
    metadata["build_receipt"] = {"doc_id": build.get("doc_id"), "requirement_id": build.get("requirement_id"), "revision": build.get("revision")}
    report["evidence"]["identity_metadata"] = metadata
    identity_ok = all(metadata[n]["doc_id_0035_present"] and metadata[n]["requirement_I07_E03_present"] for n in identities)
    identity_ok = identity_ok and build.get("doc_id") == "0035" and build.get("requirement_id") == "I07-E03" and build.get("revision") == "R02"
    report["checks"]["document_requirement_identity"] = check("PASS" if identity_ok else "FAIL", metadata)

    zip_evidence = {"testzip_bad_member": None, "required_members": {}, "xml_parse_errors": []}
    doc_root = None
    try:
        with zipfile.ZipFile(CANDIDATE, "r") as zf:
            bad = zf.testzip()
            zip_evidence["testzip_bad_member"] = bad
            names = set(zf.namelist())
            required = ["[Content_Types].xml", "word/document.xml", "word/_rels/document.xml.rels", "word/styles.xml"]
            zip_evidence["required_members"] = {n: n in names for n in required}
            for n in sorted(names):
                if n.endswith((".xml", ".rels")) or n == "[Content_Types].xml":
                    try:
                        ET.fromstring(zf.read(n))
                    except Exception as exc:
                        zip_evidence["xml_parse_errors"].append({"member": n, "error": str(exc)})
            doc_root = ET.fromstring(zf.read("word/document.xml"))
    except Exception as exc:
        zip_evidence["open_error"] = repr(exc)
    zip_ok = zip_evidence["testzip_bad_member"] is None and all(zip_evidence["required_members"].values()) and not zip_evidence["xml_parse_errors"] and doc_root is not None
    report["evidence"]["docx_zip_ooxml"] = zip_evidence
    report["checks"]["docx_zip_and_ooxml_openability"] = check("PASS" if zip_ok else "FAIL", zip_evidence)
    if not zip_ok:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1

    body = doc_root.find("./w:body", NS)
    if body is None:
        report["checks"]["document_body"] = check("FAIL", {"reason": "word/document.xml has no w:body"})
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1
    direct_children = list(body)
    body_paras = [x for x in direct_children if x.tag == W + "p"]
    table_els = [x for x in direct_children if x.tag == W + "tbl"]
    table_data = [extract_table(t, i) for i, t in enumerate(table_els, 1)]
    row_counts = [t["row_count"] for t in table_data]
    para_records = [{"paragraph": i, "text": text_of(p)} for i, p in enumerate(body_paras, 1)]
    raw_body_text = text_of(body)
    # Rebuild scan text from the independently enumerated top-level paragraphs and
    # every top-level table cell. This preserves all ledger rows and avoids relying
    # on a single flattened XML traversal for ID coverage.
    all_body_text = "\n".join([p["text"] for p in para_records] +
                              [c["text"] for t in table_data for r in t["rows"] for c in r["cells"]])
    empty_paras = [p["paragraph"] for p in para_records if not compact(p["text"])]
    empty_cells = []
    irregular_rows = []
    for t in table_data:
        widths = t["column_counts"]
        if widths and len(set(widths)) > 1:
            irregular_rows.append({"table": t["table"], "column_counts": widths})
        for row in t["rows"]:
            for cell in row["cells"]:
                if not cell["normalized"]:
                    empty_cells.append({"table": t["table"], "row": row["row"], "column": cell["column"]})
    build_content = build.get("content", {})
    table_shape_matches = len(table_data) == build_content.get("table_count") and row_counts == build_content.get("table_row_counts_including_header")
    report["evidence"]["structure"] = {
        "top_level_paragraph_count": len(body_paras), "all_document_paragraph_count": len(doc_root.findall(".//w:p", NS)),
        "table_count": len(table_data), "table_row_counts": row_counts, "total_rows": sum(row_counts),
        "table_cell_counts_by_row": [{"table": t["table"], "column_counts": t["column_counts"]} for t in table_data],
        "empty_top_level_paragraphs": empty_paras, "empty_table_cells": empty_cells,
        "irregular_row_widths": irregular_rows, "matches_build_receipt_table_counts": table_shape_matches,
        "flattened_xml_text_length": len(raw_body_text), "paragraph_cell_scan_text_length": len(all_body_text),
        "flattened_vs_enumerated_id_token_difference": {
            "flattened_only": sorted(set(ID_TOKEN_RE.findall(raw_body_text)) - set(ID_TOKEN_RE.findall(all_body_text))),
            "enumerated_only": sorted(set(ID_TOKEN_RE.findall(all_body_text)) - set(ID_TOKEN_RE.findall(raw_body_text)))},
        "tables_text": [{"table": t["table"], "text": " | ".join(" / ".join(c["text"] for c in row["cells"]) for row in t["rows"])} for t in table_data],
    }
    report["checks"]["table_structure_receipt_consistency"] = check("PASS" if table_shape_matches else "FAIL", {"actual_tables": len(table_data), "actual_rows": row_counts, "receipt_tables": build_content.get("table_count"), "receipt_rows": build_content.get("table_row_counts_including_header")})
    report["checks"]["empty_table_cells"] = check("PASS" if not empty_cells else "FAIL", {"count": len(empty_cells), "locations": empty_cells})
    report["checks"]["irregular_table_row_widths"] = check("PASS" if not irregular_rows else "UNKNOWN", {"tables": irregular_rows}, "Unequal cell counts can be intentional for OOXML merged cells; reported for inspection." if irregular_rows else "")

    # Explicit run sizes by body paragraph versus table content.
    body_runs, table_runs = [], []
    for child in direct_children:
        is_table = child.tag == W + "tbl"
        for run in child.iter(W + "r"):
            rtext = text_of(run)
            if not rtext:
                continue
            entry = {"text": compact(rtext)[:120], "size_pt": get_cell_size(run)}
            (table_runs if is_table else body_runs).append(entry)
    def size_summary(runs, minimum):
        missing_sizes = [i for i, x in enumerate(runs, 1) if x["size_pt"] is None]
        numeric = [x["size_pt"] for x in runs if x["size_pt"] is not None]
        violations = [{"run": i, **x} for i, x in enumerate(runs, 1) if x["size_pt"] is not None and x["size_pt"] < minimum]
        status = "UNKNOWN" if missing_sizes else ("FAIL" if violations or (not numeric and runs) else "PASS")
        return {"status": status, "minimum_required_pt": minimum, "observed_minimum_pt": min(numeric) if numeric else None,
                "text_run_count": len(runs), "missing_direct_size_count": len(missing_sizes), "missing_direct_size_run_indexes": missing_sizes,
                "below_threshold": violations}
    body_size = size_summary(body_runs, 10.5)
    table_size = size_summary(table_runs, 9.5)
    report["evidence"]["font_sizes"] = {"body": body_size, "tables": table_size,
                                        "method": "direct w:rPr/w:sz on nonempty text runs in word/document.xml"}
    font_status = "FAIL" if "FAIL" in (body_size["status"], table_size["status"]) else ("UNKNOWN" if "UNKNOWN" in (body_size["status"], table_size["status"]) else "PASS")
    report["checks"]["font_size_floor"] = check(font_status, report["evidence"]["font_sizes"])

    # Independent ID extraction and ledger/replacement-guide integrity.
    all_tokens = ID_TOKEN_RE.findall(all_body_text)
    fact_occurrences = FACT_RE.findall(all_body_text)
    finding_occurrences = FINDING_RE.findall(all_body_text)
    malformed_ids = sorted(set(t for t in all_tokens if not FACT_RE.fullmatch(t) and not FINDING_RE.fullmatch(t)))
    register_tables = {"fact": [], "finding": []}
    for t in table_data:
        first = [c["normalized"].casefold() for c in (t["rows"][0]["cells"] if t["rows"] else [])]
        joined = " ".join(first)
        has_replacement_guide = bool(re.search(r"替換|replacement", joined, re.I))
        if re.search(r"fact[_\s-]?id", joined) and has_replacement_guide:
            register_tables["fact"].append(t)
        if re.search(r"finding[_\s-]?id", joined) and has_replacement_guide:
            register_tables["finding"].append(t)
    def register_extract(kind):
        rex = FACT_RE if kind == "fact" else FINDING_RE
        found, duplicate, rows_without_guide = [], [], []
        row_details = []
        for t in register_tables[kind]:
            headers = [c["normalized"] for c in (t["rows"][0]["cells"] if t["rows"] else [])]
            guide_idx = next((i for i, h in enumerate(headers) if re.search(r"替換|replacement|real", h, re.I)), None)
            for row in t["rows"][1:]:
                cells = row["cells"]
                first_cell = cells[0]["normalized"] if cells else ""
                m = rex.search(first_cell)
                if not m:
                    continue
                ident = m.group(0)
                if ident in found:
                    duplicate.append({"id": ident, "table": t["table"], "row": row["row"]})
                found.append(ident)
                guide = cells[guide_idx]["normalized"] if guide_idx is not None and guide_idx < len(cells) else ""
                if not guide:
                    rows_without_guide.append({"id": ident, "table": t["table"], "row": row["row"], "guide_column": guide_idx + 1 if guide_idx is not None else None})
                row_details.append({"id": ident, "table": t["table"], "row": row["row"], "replacement_guidance": guide})
        return {"table_indexes": [t["table"] for t in register_tables[kind]], "ids": found,
                "unique_count": len(set(found)), "row_count": len(found), "duplicate_rows": duplicate,
                "rows_missing_replacement_guidance": rows_without_guide, "rows": row_details}
    facts_reg = register_extract("fact")
    findings_reg = register_extract("finding")
    body_fact_ids = sorted(set("SYN-0035-" + x for x in fact_occurrences))
    body_finding_ids = sorted(set("SYN-0035-" + x for x in finding_occurrences))
    expected_facts = [f"SYN-0035-{i:04d}" for i in range(1, 78)]
    expected_findings = [f"SYN-0035-F{i:02d}" for i in range(1, 6)]
    fact_missing_register = sorted(set(body_fact_ids) - set(facts_reg["ids"]))
    fact_unreferenced = sorted(set(facts_reg["ids"]) - set(body_fact_ids))
    finding_missing_register = sorted(set(body_finding_ids) - set(findings_reg["ids"]))
    finding_unreferenced = sorted(set(findings_reg["ids"]) - set(body_finding_ids))
    id_evidence = {"fact_occurrences": len(fact_occurrences), "fact_unique_in_body": len(body_fact_ids), "fact_ids_in_body": body_fact_ids,
                   "fact_register": facts_reg, "fact_missing_register": fact_missing_register, "fact_registered_not_used": fact_unreferenced,
                   "fact_missing_expected_sequence": sorted(set(expected_facts) - set(body_fact_ids)),
                   "finding_occurrences": len(finding_occurrences), "finding_unique_in_body": len(body_finding_ids), "finding_ids_in_body": body_finding_ids,
                   "finding_register": findings_reg, "finding_missing_register": finding_missing_register, "finding_registered_not_used": finding_unreferenced,
                   "finding_missing_expected_sequence": sorted(set(expected_findings) - set(body_finding_ids)),
                   "malformed_tokens": malformed_ids,
                   "build_receipt_claims": build_content.get("FACT_FINDING_ID_checks")}
    report["evidence"]["synthetic_ids_and_registers"] = id_evidence
    ids_ok = (set(body_fact_ids) == set(facts_reg["ids"]) == set(expected_facts) and
              set(body_finding_ids) == set(findings_reg["ids"]) == set(expected_findings) and
              not facts_reg["duplicate_rows"] and not findings_reg["duplicate_rows"] and
              not facts_reg["rows_missing_replacement_guidance"] and not findings_reg["rows_missing_replacement_guidance"] and not malformed_ids)
    report["checks"]["fact_finding_id_register_and_replacement_completeness"] = check("PASS" if ids_ok else "FAIL", {
        "facts_body_unique": len(body_fact_ids), "facts_registered_rows": facts_reg["row_count"], "facts_missing_registration": fact_missing_register,
        "findings_body_unique": len(body_finding_ids), "findings_registered_rows": findings_reg["row_count"], "findings_missing_registration": finding_missing_register,
        "duplicate_register_rows": facts_reg["duplicate_rows"] + findings_reg["duplicate_rows"],
        "rows_missing_replacement_guidance": facts_reg["rows_missing_replacement_guidance"] + findings_reg["rows_missing_replacement_guidance"],
        "malformed_tokens": malformed_ids})

    # SAMPLE/REAL/UNKNOWN boundary evidence. Page-by-page status is deliberately UNKNOWN without rendering.
    table_boundary = []
    for t in table_data:
        ttext = " ".join(c["text"] for row in t["rows"] for c in row["cells"])
        has_ids = bool(ID_TOKEN_RE.search(ttext))
        sample = bool(re.search(r"SAMPLE|SYNTHETIC|合成|樣本", ttext, re.I))
        table_boundary.append({"table": t["table"], "contains_synthetic_id": has_ids, "has_sample_marker": sample,
                              "sample_marker_evidence": sorted(set(re.findall(r"SAMPLE|SYNTHETIC|合成|樣本", ttext, re.I)))})
    boundary_counts = {label: len(re.findall(label, all_body_text, re.I)) for label in (r"SAMPLE", r"SYNTHETIC", r"REAL", r"UNKNOWN")}
    id_tables_unmarked = [x["table"] for x in table_boundary if x["contains_synthetic_id"] and not x["has_sample_marker"]]
    boundary_ok = boundary_counts["SAMPLE"] + boundary_counts["SYNTHETIC"] > 0 and boundary_counts["REAL"] > 0 and boundary_counts["UNKNOWN"] > 0 and not id_tables_unmarked
    report["evidence"]["truth_boundaries"] = {"body_marker_occurrences": boundary_counts, "tables": table_boundary,
                                              "synthetic_id_tables_without_sample_marker": id_tables_unmarked,
                                              "all_fact_and_finding_ids_are_SYN": all(x.startswith("SYN-0035-") for x in body_fact_ids + body_finding_ids),
                                              "page_by_page_marker_check": "UNKNOWN_NOT_RENDERED"}
    report["checks"]["SAMPLE_REAL_UNKNOWN_boundary_marking"] = check("PASS" if boundary_ok else "FAIL", report["evidence"]["truth_boundaries"])

    # Literal placeholders and blank cells, with exact structural locators.
    placeholder_hits = []
    for p in para_records:
        for m in PLACEHOLDER_RE.finditer(p["text"]):
            context = p["text"][max(0, m.start()-70):min(len(p["text"]), m.end()+70)]
            placeholder_hits.append({"location": f"body paragraph {p['paragraph']}", "token": m.group(0), "context": context})
    for t in table_data:
        for row in t["rows"]:
            for cell in row["cells"]:
                for m in PLACEHOLDER_RE.finditer(cell["text"]):
                    context = cell["text"][max(0, m.start()-70):min(len(cell["text"]), m.end()+70)]
                    placeholder_hits.append({"location": f"table {t['table']} row {row['row']} column {cell['column']}", "token": m.group(0), "context": context})
    # Clear pending tokens inside content fields are deterministic fails; policy/negative examples are reported for manual semantic distinction.
    literal_placeholder_hits = []
    mention_only_hits = []
    for hit in placeholder_hits:
        ctx = hit["context"]
        protective = bool(re.search(r"不得|不可|禁止|避免|不得出現|不可使用|不得填|禁止填|例如|示例|placeholder|占位|負向|負面", ctx, re.I))
        if protective:
            mention_only_hits.append(hit)
        else:
            literal_placeholder_hits.append(hit)
    report["evidence"]["empty_and_placeholder_content"] = {"empty_top_level_paragraph_count": len(empty_paras),
                                                            "empty_table_cell_count": len(empty_cells),
                                                            "placeholder_occurrence_count": len(placeholder_hits),
                                                            "literal_placeholder_candidates": literal_placeholder_hits,
                                                            "policy_or_example_mentions": mention_only_hits}
    report["checks"]["pending_placeholder_scan"] = check("FAIL" if literal_placeholder_hits else ("UNKNOWN" if mention_only_hits else "PASS"), report["evidence"]["empty_and_placeholder_content"],
                                                           "Textual policy/example mentions need semantic interpretation." if mention_only_hits and not literal_placeholder_hits else "")

    # Independent extraction and recomputation of the two crosstabs; compare to build receipt claims.
    matrices = {}
    for label, index in (("version_A", 14), ("version_B", 16)):
        t = table_data[index - 1] if len(table_data) >= index else None
        matrices[label] = {"table_index_1_based": index, "table_rows": t["rows"] if t else None,
                           "computed": matrix_from_table(t) if t else {"status": "UNKNOWN", "reason": "Table index not present."}}
    computed_a = matrices["version_A"]["computed"]
    computed_b = matrices["version_B"]["computed"]
    math_status = "UNKNOWN"
    delta = None
    matrix_compare = {}
    displayed_result_tokens_present = {"kappa_A_-0.20": bool(re.search(r"[−-]0\.20", all_body_text)),
                                       "kappa_B_0.60": bool(re.search(r"(?<!\d)0\.60", all_body_text)),
                                       "delta_0.80": bool(re.search(r"(?<!\d)0\.80", all_body_text))}
    if computed_a.get("status") == computed_b.get("status") == "PASS":
        delta = computed_b.get("kappa") - computed_a.get("kappa")
        claimed = build.get("calculations", {}).get("corrected_synthetic_kappa_matrices", {})
        for key, comp in (("version_A", computed_a), ("version_B", computed_b)):
            claim = claimed.get(key, {})
            matrix_compare[key] = {"matrix_matches_receipt": comp.get("matrix") == claim.get("matrix"),
                                   "n_matches_receipt": comp.get("n") == claim.get("n"),
                                   "kappa_matches_receipt_rounded_6dp": round(comp.get("kappa", 0), 6) == round(float(claim.get("kappa", 999)), 6),
                                   "receipt_claim": claim}
        matrix_compare["delta_matches_receipt_rounded_6dp"] = round(delta, 6) == round(float(claimed.get("kappa_delta_B_minus_A", 999)), 6)
        all_matrix_gates = all(comp.get("row_cells_match_recalculation") and comp.get("final_totals_row_matches_recalculation") for comp in (computed_a, computed_b))
        all_display_values = all(displayed_result_tokens_present.values())
        math_status = "PASS" if all_matrix_gates and all_display_values and all(v.get("matrix_matches_receipt", True) and v.get("n_matches_receipt", True) and v.get("kappa_matches_receipt_rounded_6dp", True) for v in matrix_compare.values() if isinstance(v, dict)) and matrix_compare.get("delta_matches_receipt_rounded_6dp") else "FAIL"
    report["evidence"]["independent_math"] = {"matrices": matrices, "delta_B_minus_A": delta, "receipt_comparison": matrix_compare,
                                               "displayed_result_tokens_present": displayed_result_tokens_present}
    report["checks"]["kappa_matrix_and_arithmetic_recalculation"] = check(math_status, report["evidence"]["independent_math"])

    # Check source packet/Blueprint/repair metadata claims as directly stated in build receipt.
    receipt_claim_ok = build.get("status") == "CANDIDATE_BUILD_COMPLETE_DETERMINISTIC_CHECKS_ONLY" and build.get("outputs", {}).get("docx", {}).get("sha256", "").upper() == candidate_actual["sha256"]
    report["checks"]["builder_receipt_output_claim"] = check("PASS" if receipt_claim_ok else "FAIL", {"claimed_status": build.get("status"), "claimed_candidate_sha256": out_claim.get("sha256"), "actual_candidate_sha256": candidate_actual["sha256"]})

    statuses = [v["status"] for v in report["checks"].values()]
    overall = "FAIL" if "FAIL" in statuses else ("UNKNOWN" if "UNKNOWN" in statuses else "PASS")
    report["overall_static_gate"] = overall
    report["exit_code"] = 1 if overall == "FAIL" else (3 if overall == "UNKNOWN" else 0)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report["exit_code"]


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(json.dumps({"report_type": "TTQS_ONE_INDEPENDENT_STATIC_QA", "work_id": "TTQS_ONE_0035_I07-E03_STATIC_QA_R02_CARVER",
                          "overall_static_gate": "FAIL", "exit_code": 2, "fatal_error": repr(exc),
                          "limitations": ["Input inspection aborted on an unhandled deterministic-check error."]}, ensure_ascii=False, indent=2))
        sys.exit(2)
