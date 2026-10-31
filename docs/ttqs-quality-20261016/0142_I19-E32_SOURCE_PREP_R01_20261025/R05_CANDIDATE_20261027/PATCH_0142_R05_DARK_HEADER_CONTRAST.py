from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import hashlib,json
root=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025")
src=root/"0142_I19-E32_R04_TABLE3_FLOW_CANDIDATE.docx";out=root/"0142_I19-E32_R05_HEADER_CONTRAST_CANDIDATE.docx";receipt=root/"R05_HEADER_CONTRAST_PATCH_RECEIPT.json"
ns={"w":"http://schemas.openxmlformats.org/wordprocessingml/2006/main"};W="{"+ns['w']+"}"
def sha(b):return hashlib.sha256(b).hexdigest()
rawsrc=src.read_bytes()
if sha(rawsrc)!="e43ab1564e19d9cf024a57bebaf0bd8cf898fa364155800a404409d69fa5181c":raise SystemExit("R04_BASE_SHA_MISMATCH")
if out.exists():raise SystemExit("OUTPUT_ALREADY_EXISTS")
with ZipFile(src,"r") as zin:
 if zin.testzip():raise SystemExit("SOURCE_ZIP_CORRUPT")
 names=zin.namelist();raw=zin.read("word/document.xml");x=etree.fromstring(raw);tables=x.xpath("//w:tbl",namespaces=ns)
 targets=[(4,0),(5,1)]
 for ti,ci in targets:
  cell=tables[ti].xpath("./w:tr[1]/w:tc",namespaces=ns)[ci]
  shd=cell.find(W+"tcPr").find(W+"shd")
  if shd is None or shd.get(W+"fill")!="203955":raise SystemExit(f"TARGET_HEADER_FILL_UNEXPECTED:{ti+1}:{ci}")
  runs=cell.xpath("./w:p/w:r",namespaces=ns)
  if len(runs)!=1:raise SystemExit(f"TARGET_RUN_COUNT_UNEXPECTED:{ti+1}:{ci}")
  rpr=runs[0].find(W+"rPr")
  if rpr is None: rpr=etree.Element(W+"rPr");runs[0].insert(0,rpr)
  if rpr.find(W+"color") is not None or rpr.find(W+"b") is not None:raise SystemExit("TARGET_ALREADY_HAS_DIRECT_COLOR_OR_BOLD")
  bold=etree.Element(W+"b")
  color=etree.Element(W+"color");color.set(W+"val","FFFFFF")
  # CT_RPr order: bold, ... color, ... size. Existing size is preserved.
  rpr.insert(0,bold)
  sz=rpr.find(W+"sz")
  if sz is None:rpr.append(color)
  else:rpr.insert(rpr.index(sz),color)
 text_before="".join(x.xpath("//w:t/text()",namespaces=ns))
 newxml=etree.tostring(x,xml_declaration=True,encoding="UTF-8",standalone=True)
 with ZipFile(out,"w") as zout:
  for info in zin.infolist():zout.writestr(info,newxml if info.filename=="word/document.xml" else zin.read(info.filename))
with ZipFile(out,"r") as z:
 if z.testzip():raise SystemExit("OUTPUT_ZIP_CORRUPT")
 y=etree.fromstring(z.read("word/document.xml"));ts=y.xpath("//w:tbl",namespaces=ns)
 for ti,ci in targets:
  cell=ts[ti].xpath("./w:tr[1]/w:tc",namespaces=ns)[ci];r=cell.xpath("./w:p/w:r",namespaces=ns)[0];rpr=r.find(W+"rPr")
  if rpr.find(W+"color").get(W+"val")!="FFFFFF" or rpr.find(W+"b") is None:raise SystemExit("HEADER_STYLE_READBACK_FAIL")
 text_after="".join(y.xpath("//w:t/text()",namespaces=ns))
 if text_after!=text_before:raise SystemExit("VISIBLE_TEXT_CHANGED")
 obj={"schema":"ttqs-one-0142-r05-header-contrast-patch-v1","doc_id":"0142","requirement_id":"I19-E32","candidate_state":"CANDIDATE","base_candidate_sha256":sha(rawsrc),"candidate_sha256":sha(out.read_bytes()),"changed_package_parts":["word/document.xml"],"headers_corrected":[{"table_index_one_based":5,"cell_index_zero_based":0,"dark_fill":"203955","font_color":"FFFFFF","bold":True},{"table_index_one_based":6,"cell_index_zero_based":1,"dark_fill":"203955","font_color":"FFFFFF","bold":True}],"visible_text_unchanged":True,"visible_text_sha256":sha(text_before.encode("utf-8")),"source_sample_values_and_formulas_unchanged":True,"package_integrity":"PASS","formal_acceptance":"NOT_GRANTED","real_evidence":"UNKNOWN/HOLD"}
receipt.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps(obj,ensure_ascii=False))
