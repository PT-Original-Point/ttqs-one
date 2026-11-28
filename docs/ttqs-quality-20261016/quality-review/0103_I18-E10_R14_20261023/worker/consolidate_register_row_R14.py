from pathlib import Path
import hashlib,json
p=Path(r'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\TEMP\R11_0103_R04')
s=(p/'manuscript_R06.md').read_text(encoding='utf-8')
old='| S-06 | 案例一／Form A | 目的 | `SAMPLE-PURPOSE-01` | 真實用途與閱覽層級 | 隱私權責 | 目的經核定 | SAMPLE_ONLY |'
new='| S-06 | 案例一、二／Form A | 合法目的 | `SAMPLE-PURPOSE-01`（案例一）、`SAMPLE-PURPOSE-02`（案例二） | 真實用途與閱覽層級 | 隱私權責 | 兩案目的及揭露範圍均經權責核定 | SAMPLE_ONLY |'
row='| S-39 | 案例二／Form A | 合法目的 | `SAMPLE-PURPOSE-02`（真偽查核演練） | 真實用途與閱覽層級 | 隱私權責 | 目的及揭露範圍經權責核定 | SAMPLE_ONLY |\n'
if s.count(old)!=1 or s.count(row)!=1: raise SystemExit('Expected S-06/S-39 rows not unique')
s=s.replace(old,new,1).replace(row,'',1)
dst=p/'manuscript_R07.md'; dst.write_text(s,encoding='utf-8',newline='\n')
print(json.dumps({'manuscript_sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'rows_replaced':2},ensure_ascii=True))
