from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import hashlib,json
root=Path(r"docs/ttqs-quality-20261016/quality-review/0035_I07-E03_SOURCE_PREP_R01_20261118")
src=root/"candidate/0035_I07-E03_R02_SCOPED_REPAIR.docx"; out=root/"candidate/0035_I07-E03_R02_TW_CHAR_FIX.docx"; qa=root/"candidate/qa/text_patch_r03"
needle="记录方法版本變更".encode("utf-8"); replacement="記錄方法版本變更".encode("utf-8")
with ZipFile(src) as zin: parts=[(i,zin.read(i.filename)) for i in zin.infolist()]
found=0; patched=[]
for info,data in parts:
 if info.filename=="word/document.xml":
  found=data.count(needle)
  if found!=1: raise SystemExit(f"expected exactly one targeted string; got {found}")
  data=data.replace(needle,replacement); ET.fromstring(data)
 patched.append((info,data))
with ZipFile(out,"w") as zout:
 for info,data in patched: zout.writestr(info,data)
with ZipFile(out) as z:
 if z.testzip(): raise SystemExit("ZIP CRC failed")
 ET.fromstring(z.read("word/document.xml"))
 if needle in z.read("word/document.xml") or replacement not in z.read("word/document.xml"): raise SystemExit("text verification failed")
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest().upper()
r={"work_id":"0035-I07-E03-TW-CHAR-FIX-R02","stage":"SCOPED_DETERMINISTIC_TEXT_REPAIR","status":"PASS","parent_candidate":"0035_I07-E03_R02_SCOPED_REPAIR.docx","parent_sha256":sha(src),"candidate":"0035_I07-E03_R02_TW_CHAR_FIX.docx","candidate_sha256":sha(out),"bytes":out.stat().st_size,"part":"word/document.xml","replacement_count":found,"from":"记录方法版本變更","to":"記錄方法版本變更","xml_parse":"PASS","zip_test":"PASS","other_content":"UNCHANGED_AT_XML_PART_LEVEL","formal_acceptance":"NOT_CLAIMED"}
(qa/"PATCH_RECEIPT_R03.json").write_text(json.dumps(r,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(r,ensure_ascii=False))
