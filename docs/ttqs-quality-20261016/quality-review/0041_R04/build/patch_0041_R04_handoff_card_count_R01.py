from pathlib import Path
import hashlib, os, tempfile, zipfile
from lxml import etree

R04 = Path(__file__).resolve().parents[1]
R03 = R04.parent / "0041_R03"
SOURCE = R03 / "candidate" / "0041_R03.docx"
TARGET = R04 / "candidate" / "0041_R04.docx"
EXPECTED_SOURCE_SHA = "1BC0337C0328C68A8644CABF3E07D5080E9C2A9D98B19B8881A6DB05196CBA43".lower()
actual_source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
if actual_source_sha != EXPECTED_SOURCE_SHA:
    raise SystemExit(f"R03 SHA mismatch: {actual_source_sha}")
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
with zipfile.ZipFile(SOURCE, "r") as zin:
    entries = [(info, zin.read(info.filename)) for info in zin.infolist()]
xml_name = "word/document.xml"
tree = etree.fromstring(next(data for info, data in entries if info.filename == xml_name))
revision_hits = []
card_hits = []
for node in tree.findall(".//w:t", NS):
    if node.text and "文檔識別：0041 R03" in node.text:
        revision_hits.append(node)
    if node.text == "三欄交接卡演練及同儕回饋。":
        card_hits.append(node)
if len(revision_hits) != 1 or len(card_hits) != 1:
    raise SystemExit(f"Expected one revision and one card mismatch; found {len(revision_hits)}, {len(card_hits)}")
revision_hits[0].text = revision_hits[0].text.replace("文檔識別：0041 R03", "文檔識別：0041 R04", 1)
card_hits[0].text = "四欄交接卡演練及同儕回饋。"
new_xml = etree.tostring(tree, xml_declaration=True, encoding="UTF-8", standalone=True)
fd, temp_name = tempfile.mkstemp(dir=str(TARGET.parent), suffix=".tmp")
os.close(fd)
try:
    with zipfile.ZipFile(temp_name, "w") as zout:
        for info, data in entries:
            zout.writestr(info, new_xml if info.filename == xml_name else data)
    os.replace(temp_name, TARGET)
finally:
    if os.path.exists(temp_name):
        os.remove(temp_name)
with zipfile.ZipFile(TARGET) as check:
    if check.testzip() is not None:
        raise SystemExit("R04 DOCX ZIP integrity failed")
print({"source_sha256": actual_source_sha, "candidate": str(TARGET), "candidate_sha256": hashlib.sha256(TARGET.read_bytes()).hexdigest(), "revision_marker_changed": True, "card_column_count_fixed": True, "only_document_xml_modified": True})
