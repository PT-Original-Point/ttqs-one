from __future__ import annotations
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TEMPLATE=ROOT.parent/"0075_R01/worker/build_0075_R02_docx.py"
OUT=ROOT/"worker/build_0076_R01_docx.py"
REPLACES=[
("0075_R01_body.md","0076_R01_body.md"),
("UNIQUE_BLUEPRINT_0075_R01.md","UNIQUE_BLUEPRINT_0076_R01.md"),
("SYNTHETIC_REPLACEMENT_REGISTER_0075_R01.csv","SYNTHETIC_REPLACEMENT_REGISTER_0076_R01.csv"),
("SOURCE_PACKET_0075_R01.md","SOURCE_PACKET_0076_R01.md"),
("0075_R02.docx","0076_R01.docx"),
("build_receipt_R02.json","build_receipt_R01.json"),
("TTQS ONE  |  DOCX 0075  |  I17A-E03  |  官方勾選 082","TTQS ONE  |  DOCX 0076  |  I17B-E01  |  官方勾選 084"),
("課程改善行動方案 0075 I17A-E03","考試暨實作評量紀錄 0076 I17B-E01"),
("TTQS_ONE_0075_R02_BUILD_RECEIPT.v1","TTQS_ONE_0076_R01_BUILD_RECEIPT.v1"),
('"document_id": "0075"','"document_id": "0076"'),
('"requirement_id": "I17A-E03"','"requirement_id": "I17B-E01"'),
('"official_checkbox_serial": "082"','"official_checkbox_serial": "084"'),
("0075, I17A-E03, checkbox 082, SAMPLE, SYNTHETIC","0076, I17B-E01, checkbox 084, SAMPLE, SYNTHETIC"),
]
def main():
    if not TEMPLATE.is_file(): raise FileNotFoundError(TEMPLATE)
    text=TEMPLATE.read_text(encoding="utf-8")
    counts={}
    for old,new in REPLACES:
        n=text.count(old)
        if n<1: raise ValueError(f"template marker absent: {old}")
        counts[old]=n
        text=text.replace(old,new)
    OUT.write_text(text,encoding="utf-8")
    print("BUILDER_CREATED",str(OUT.relative_to(ROOT)),"REPLACEMENTS",counts)
if __name__=="__main__": main()
