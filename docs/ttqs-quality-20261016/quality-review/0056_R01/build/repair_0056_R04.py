from __future__ import annotations
import hashlib
import json
import re
import zipfile
from pathlib import Path
from lxml import etree

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / "0056_R03.docx"
OUTPUT = BASE / "0056_R04.docx"
RECEIPT = BASE / "build" / "build_receipt_R04.json"
EXPECTED_SOURCE_SHA256 = "1960c37ee335d0af4872d2c41100a26c3f0c38a4475ec2e185993708c3028f3d"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = "{" + W_NS + "}"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

HEADER_LABELS = {
    "義務編號obligation_id": "義務編號",
    "檢查編號check_id": "檢查編號",
    "索取編號req_id": "索取編號",
    "證據編號evidence_id": "證據編號",
    "決策編號decision_id": "決策編號",
    "sample_fact_id": "示範資料編號",
    "例外編號exception_id": "例外編號",
    "來源 obligation/check": "來源義務／檢查編號",
    "判定決策代號": "判定決策",
}
EXPECTED_HEADER_COUNTS = {
    "義務編號obligation_id": 5,
    "檢查編號check_id": 1,
    "索取編號req_id": 1,
    "證據編號evidence_id": 1,
    "決策編號decision_id": 1,
    "sample_fact_id": 1,
    "例外編號exception_id": 1,
    "來源 obligation/check": 1,
    "判定決策代號": 1,
}

LITERAL_REPLACEMENTS = {
    "HOLD 原因": "暫停原因",
    "D1 APPLY_INSPECTION_ONLY": "僅走設備安檢路徑",
    "D2 APPLY_INSURANCE_ONLY": "僅走場地投保證明路徑",
    "D3 APPLY_BOTH": "設備安檢與場地投保證明兩路皆適用",
    "D4 NOT_APPLICABLE_WITH_BASIS": "兩路均有來源依據並判定不適用",
    "D5 HOLD_UNKNOWN": "適用性未明，暫停判定",
    "NOT_APPLICABLE_SUPPORTED": "有來源佐證的不適用",
    "NOT_APPLICABLE_WITH_BASIS": "有來源依據的不適用",
    "UNKNOWN_APPLICABILITY": "適用性未知",
    "APPLICABLE_CONFIRMED": "已依來源確認適用",
    "APPLICABLE_CANDIDATE": "可能適用，待核實來源",
    "REQUEST_DRAFTED_NOT_SENT": "索取稿已擬，尚未寄出",
    "RECEIVED_VERIFIED_REAL": "已收到並核驗真實正本",
    "RECEIVED_UNVERIFIED": "已收到、尚待核實",
    "MISMATCH_OR_UNVERIFIABLE": "不符或無法核實",
    "EXPIRED_OR_OUT_OF_PERIOD": "已逾期或不涵蓋使用期間",
    "EVIDENCE_MISSING": "尚未取得證據",
    "HOLD_UNKNOWN": "適用性未知，暫停判定",
    "PENDING_REAL_SOURCE": "待取得真實來源",
    "sample_fact_id": "示範資料編號",
    "fact-level": "逐筆示範資料",
    "tag-out": "掛牌停用",
    "NOT SENT": "尚未寄出",
    "(both)": "（兩路皆辦）",
}
WORD_REPLACEMENTS = {
    "PROPOSED": "提案待授權",
    "CANDIDATE": "候選待核",
    "UNKNOWN": "未知",
    "VERIFIED": "已核實",
    "REAL": "真實來源",
    "PASS": "通過",
    "HOLD": "暫停",
}
RULES = dict(LITERAL_REPLACEMENTS)
RULES.update(WORD_REPLACEMENTS)
PATTERN_PARTS = [re.escape(x) for x in sorted(LITERAL_REPLACEMENTS, key=len, reverse=True)]
PATTERN_PARTS.extend(r"\b" + re.escape(x) + r"\b" for x in sorted(WORD_REPLACEMENTS, key=len, reverse=True))
TOKEN_PATTERN = re.compile("(?:" + "|".join(PATTERN_PARTS) + ")")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def set_cell_text_nodes(cell: etree._Element, label: str) -> None:
    nodes = list(cell.iter(W + "t"))
    if not nodes:
        raise RuntimeError(f"Target header cell has no text node: {label}")
    nodes[0].text = label
    for node in nodes[1:]:
        node.text = ""


def apply_paragraph_replacements(paragraph: etree._Element, counts: dict[str, int]) -> None:
    nodes = list(paragraph.iter(W + "t"))
    if not nodes:
        return
    original_parts = [node.text or "" for node in nodes]
    original = "".join(original_parts)
    if not original:
        return
    bounds = []
    pos = 0
    for part in original_parts:
        bounds.append((pos, pos + len(part)))
        pos += len(part)
    chunks: list[list[str]] = [[] for _ in nodes]

    def distribute_unchanged(start: int, end: int) -> None:
        if start >= end:
            return
        for index, (left, right) in enumerate(bounds):
            lo, hi = max(start, left), min(end, right)
            if lo < hi:
                chunks[index].append(original[lo:hi])

    def put_replacement(start: int, value: str) -> None:
        for index, (left, right) in enumerate(bounds):
            if left <= start < right:
                chunks[index].append(value)
                return
        for index, (left, right) in enumerate(bounds):
            if left >= start and right > left:
                chunks[index].append(value)
                return
        chunks[-1].append(value)

    cursor = 0
    for match in TOKEN_PATTERN.finditer(original):
        distribute_unchanged(cursor, match.start())
        key = match.group(0)
        put_replacement(match.start(), RULES[key])
        counts[key] += 1
        cursor = match.end()
    distribute_unchanged(cursor, len(original))
    for node, parts in zip(nodes, chunks):
        value = "".join(parts)
        node.text = value
        if value[:1].isspace() or value[-1:].isspace():
            node.set(XML_SPACE, "preserve")
        elif XML_SPACE in node.attrib:
            del node.attrib[XML_SPACE]


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(SOURCE)
    if OUTPUT.exists() or RECEIPT.exists():
        raise FileExistsError("R04 output or receipt already exists; refusing overwrite")
    source_bytes = SOURCE.read_bytes()
    source_sha = sha256(source_bytes)
    if source_sha != EXPECTED_SOURCE_SHA256:
        raise RuntimeError(f"Unexpected R03 SHA: {source_sha}")

    with zipfile.ZipFile(SOURCE, "r") as zin:
        infos = zin.infolist()
        package = {info.filename: zin.read(info.filename) for info in infos}
        archive_comment = zin.comment
    original_package = dict(package)
    original_xml = package.get("word/document.xml")
    if original_xml is None:
        raise RuntimeError("Missing word/document.xml")

    # Keep the complete source namespace map. ElementTree drops declarations
    # used only by mc:Ignorable (for example w14/wp14), which makes Word reject
    # the otherwise well-formed package.
    root = etree.fromstring(original_xml)
    original_nsmap = dict(root.nsmap)
    ignorable = root.get("{http://schemas.openxmlformats.org/markup-compatibility/2006}Ignorable", "")
    missing_ignorable = sorted(prefix for prefix in ignorable.split() if prefix not in original_nsmap)
    if missing_ignorable:
        raise RuntimeError(f"Source has unresolved mc:Ignorable prefixes: {missing_ignorable}")

    header_counts = {key: 0 for key in HEADER_LABELS}
    for table in root.iter(W + "tbl"):
        first_row = table.find(W + "tr")
        if first_row is None:
            continue
        for cell in first_row.findall(W + "tc"):
            nodes = list(cell.iter(W + "t"))
            joined = "".join(node.text or "" for node in nodes)
            if joined in HEADER_LABELS:
                header_counts[joined] += 1
                set_cell_text_nodes(cell, HEADER_LABELS[joined])
    if header_counts != EXPECTED_HEADER_COUNTS:
        raise RuntimeError(f"Unexpected schema-header counts: {header_counts}")

    replacement_counts = {key: 0 for key in RULES}
    for paragraph in root.iter(W + "p"):
        apply_paragraph_replacements(paragraph, replacement_counts)

    final_text = "".join(node.text or "" for node in root.iter(W + "t"))
    forbidden = sorted(set(re.findall(r"\b[a-z][a-z0-9]*_[a-z0-9_]+\b", final_text)))
    long_status_keys = sorted(set(re.findall(r"\b[A-Z][A-Z0-9]+_[A-Z0-9_]+\b", final_text)))
    if forbidden or long_status_keys or "fact-level" in final_text or "obligation/check" in final_text:
        raise RuntimeError(f"Human-facing control strings remain: snake={forbidden}, status={long_status_keys}")

    package["word/document.xml"] = etree.tostring(
        root, encoding="UTF-8", xml_declaration=True, standalone=True, pretty_print=False
    )
    serialized_root = etree.fromstring(package["word/document.xml"])
    if dict(serialized_root.nsmap) != original_nsmap:
        raise RuntimeError("Namespace declarations changed during XML serialization")
    try:
        with zipfile.ZipFile(OUTPUT, "w") as zout:
            zout.comment = archive_comment
            for info in infos:
                zout.writestr(info, package[info.filename])
        with zipfile.ZipFile(OUTPUT, "r") as zout:
            bad = zout.testzip()
            output_package = {info.filename: zout.read(info.filename) for info in zout.infolist()}
            output_order = [info.filename for info in zout.infolist()]
        changed = [name for name in original_package if original_package[name] != output_package.get(name)]
        if bad or changed != ["word/document.xml"] or output_order != [info.filename for info in infos]:
            raise RuntimeError(f"Package verification failed: bad={bad}, changed={changed}")
    except Exception:
        OUTPUT.unlink(missing_ok=True)
        raise

    out_sha = sha256(OUTPUT.read_bytes())
    receipt = {
        "project_id": "TTQS_ONE",
        "doc_id": "0056",
        "revision": "R04",
        "official_requirement_id": "I12-E04",
        "official_checkbox_serial": "059",
        "status": "CANDIDATE_BUILD_ONLY_QA_PENDING",
        "predecessor": "0056_R03.docx",
        "predecessor_sha256": source_sha,
        "candidate": "0056_R04.docx",
        "candidate_sha256": out_sha,
        "candidate_bytes": OUTPUT.stat().st_size,
        "changed_package_members": changed,
        "xml_namespace_map_preserved": True,
        "mc_ignorable_prefixes_preserved": ignorable.split(),
        "unchanged_package_members": len(infos) - len(changed),
        "header_humanization_counts": header_counts,
        "text_replacement_counts": replacement_counts,
        "forbidden_snake_case_keys_remaining": forbidden,
        "long_machine_status_keys_remaining": long_status_keys,
        "all_examples_remain_SAMPLE_SYNTHETIC": True,
        "human_acceptance": "NOT_GRANTED",
        "technical_visual_semantic_qa": "PENDING",
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
