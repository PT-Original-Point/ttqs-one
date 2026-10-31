from pathlib import Path
from zipfile import ZipFile
root=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0132_I19-E21_SOURCE_PREP_R01_20261024')
out=root/'review'/'W2_EXACT_SHA_20261026'/'embedded_media'
out.mkdir(parents=True,exist_ok=True)
p=root/'candidate'/'0132_I19-E21_CANDIDATE_R01.docx'
with ZipFile(p) as z:
 for n in z.namelist():
  if n.startswith('word/media/'):
   target=out/Path(n).name
   target.write_bytes(z.read(n))
   print(f'{target} {target.stat().st_size}')