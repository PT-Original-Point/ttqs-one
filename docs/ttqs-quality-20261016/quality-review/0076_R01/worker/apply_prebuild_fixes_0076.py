from __future__ import annotations
import hashlib,json,shutil
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BODY=ROOT/"candidate/0076_R01_body.md"
WORKER=ROOT/"worker"
TEMP_HELPER=Path(r"C:\Users\J\AppData\Local\Temp\opencode\validate_tables0076.py")
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    raw=BODY.read_bytes()
    original=WORKER/"opencode_original_0076_R01_body.md"
    if original.exists(): raise FileExistsError(original)
    original.write_bytes(raw)
    text=raw.decode("utf-8-sig")
    old_title="# 志工服務溝通與紀錄交接實務｜考試暨實作評量紀錄（含試題、逐筆作答、實作評分與勾稽）"
    new_title="# 志工服務溝通與紀錄交接實務考試暨實作評量紀錄"
    if text.count(old_title)!=1: raise ValueError(f"expected one title; found {text.count(old_title)}")
    text=text.replace(old_title,new_title,1)
    typo="勾選 084 複合影像"
    if text.count(typo)!=1: raise ValueError(f"expected one located typo; found {text.count(typo)}")
    text=text.replace(typo,"勾選 084 複合佐證",1)
    notice="> **SAMPLE/SYNTHETIC 示範；非本會實際辦訓、施測、評分、交接、結案或核准。本文件不得被理解為本會已辦理考試或實作評量、已有學員、已有成績或已達成任何等級。**\n\n"
    if not text.startswith(notice+new_title): raise ValueError("leading notice/title layout changed unexpectedly")
    text=text[len(notice):]
    text=text.replace(new_title+"\n\n## 第 1 節",new_title+"\n\n"+notice+"## 第 1 節",1)
    BODY.write_text(text,encoding="utf-8")
    copied=None
    if TEMP_HELPER.is_file():
        dest=WORKER/"worker_created_validate_tables0076.py"
        shutil.copyfile(TEMP_HELPER,dest)
        copied={"source":str(TEMP_HELPER),"evidence_copy":str(dest.relative_to(ROOT)),"sha256":sha(dest),"bytes":dest.stat().st_size}
    receipt={"schema":"TTQS_ONE_0076_PREBUILD_EDIT_RECEIPT.v1","original_worker_body_path":str(original.relative_to(ROOT)),"original_sha256":sha(original),"revised_body_path":str(BODY.relative_to(ROOT)),"revised_body_sha256":sha(BODY),"changes":[{"locator":"document title","reason":"Apply document title style cleanly and remove punctuation per document title standard","before":old_title,"after":new_title},{"locator":"section 1.2 table","reason":"Correct obvious generated typo without changing scope","before":typo,"after":"勾選 084 複合佐證"},{"locator":"opening callout","reason":"Place the status statement after the title so the first heading can use Word Title style","before":"Callout preceded the title","after":"Title followed by callout"}],"worker_temporary_helper":copied,"writer_body_sha256_before":sha(original),"status":"TARGETED_PREBUILD_EDIT_ONLY"}
    (ROOT/"evidence/body_editorial_correction_R01.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(receipt,ensure_ascii=False))
if __name__=="__main__": main()
