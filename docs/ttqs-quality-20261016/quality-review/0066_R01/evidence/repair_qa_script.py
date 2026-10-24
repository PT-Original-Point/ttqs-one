from pathlib import Path
p=Path(r'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0066_R01\evidence\technical_qa_R01.py')
s=p.read_text(encoding='utf-8')
s=s.replace("),\\n 'rendered_page_count_matches_pdf'", "),\n 'rendered_page_count_matches_pdf'")
s=s.replace("True,\\n  'render_count_matches_pdf'", "True,\n  'render_count_matches_pdf'")
p.write_text(s,encoding='utf-8')
print('fixed literal newlines',s.count('\\\\n'))
