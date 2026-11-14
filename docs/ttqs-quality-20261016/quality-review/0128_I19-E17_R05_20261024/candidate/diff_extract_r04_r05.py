from pathlib import Path
import difflib,hashlib,json
base=Path(r"E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0128_I19-E17_SOURCE_PREP_R01_20261024\candidate")
a=(base/"0128_I19-E17_R04_EXTRACTED_TEXT.txt").read_text(encoding="utf-8").splitlines()
b=(base/"0128_I19-E17_R05_EXTRACTED_TEXT.txt").read_text(encoding="utf-8").splitlines()
d=list(difflib.unified_diff(a,b,fromfile="R04",tofile="R05",lineterm=""))
print(json.dumps({"changed_lines":d,"diff_count":len(d),"r04_sha":hashlib.sha256((base/"0128_I19-E17_R04_EXTRACTED_TEXT.txt").read_bytes()).hexdigest(),"r05_sha":hashlib.sha256((base/"0128_I19-E17_R05_EXTRACTED_TEXT.txt").read_bytes()).hexdigest()},ensure_ascii=False))