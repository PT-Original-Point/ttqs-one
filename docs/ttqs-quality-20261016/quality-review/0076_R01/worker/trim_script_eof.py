from pathlib import Path
paths=[
Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01\worker\apply_prebuild_fixes_0076.py'),
Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01\worker\dispatch_0076_writer.py'),
Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01\worker\make_0076_builder.py'),
Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01\worker\prepare_0076_packet.py'),
Path(r'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0076_R01\worker\verify_0076_R01.py')]
for p in paths:
 t=p.read_text(encoding='utf-8-sig')
 p.write_text(t.rstrip()+'\n',encoding='utf-8')
 print(p.name)
