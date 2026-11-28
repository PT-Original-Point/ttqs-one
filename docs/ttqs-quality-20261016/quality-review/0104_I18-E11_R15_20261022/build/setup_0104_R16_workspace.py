from pathlib import Path
import shutil
pkg=Path(r'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022')
rt=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0104_I18-E11_SOURCE_PREP_20261022')
(rt/'candidate').mkdir(parents=True,exist_ok=True);(rt/'evidence').mkdir(parents=True,exist_ok=True);(rt/'visual'/'0104_R16'/'pages').mkdir(parents=True,exist_ok=True);(rt/'writer').mkdir(parents=True,exist_ok=True)
shutil.copy2(pkg/'writer/opencode_writer_manuscript_0104_R16_patched.md',rt/'writer/opencode_writer_manuscript_0104_R16_patched.md')
files=['build_0104_docx_R15.py','qa_0104_R15.py','render_0104_R15_pdf_pages.py','export_word_0104_R15.ps1']
for name in files:
 text=(pkg/'build'/name).read_text(encoding='utf-8-sig')
 text=text.replace('R15','R16')
 target=name.replace('R15','R16')
 out_pkg=pkg/'build'/target;out_pkg.write_text(text,encoding='utf-8')
 out_rt=rt/'writer'/target;out_rt.write_text(text,encoding='utf-8')
 print('script',out_pkg.name)
print('R16 source manuscript copied to runtime')
