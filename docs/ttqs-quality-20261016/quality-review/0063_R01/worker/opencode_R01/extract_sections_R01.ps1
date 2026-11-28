$ErrorActionPreference='Stop'
$work='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01\worker\opencode_R01'
$text=Get-Content -LiteralPath (Join-Path $work 'worker_output_R01.md') -Raw -Encoding UTF8
$parts=[regex]::Split($text,'(?m)^# HUMAN_FACING_MANUSCRIPT\s*\r?$',2)
if($parts.Count -ne 2){throw 'Missing HUMAN_FACING_MANUSCRIPT marker'}
$bp=$parts[0].Trim()
$body=$parts[1].Trim()
$body=[regex]::Replace($body,'(?s)\r?\n---\r?\n## Unique Blueprint\s*\r?\n.*$','').Trim()
if(-not $body.StartsWith('# 查詢服務與持續改善作業指引暨合成演練')){throw 'Human-facing title missing'}
$root=Split-Path (Split-Path $work -Parent) -Parent
[System.IO.File]::WriteAllText((Join-Path $root 'inputs\0063_UNIQUE_BLUEPRINT_R01.md'),$bp,[System.Text.UTF8Encoding]::new($false))
[System.IO.File]::WriteAllText((Join-Path $root 'inputs\0063_MANUSCRIPT_SOURCE_R01.md'),$body,[System.Text.UTF8Encoding]::new($false))
"BLUEPRINT_CHARS=$($bp.Length) MANUSCRIPT_CHARS=$($body.Length) BODY_LINES=$(@($body -split '\r?\n').Count)"
"BODY HEADINGS:"; $body -split '\r?\n' | Where-Object {$_ -match '^#{1,3} '}
"CHECKS:"; foreach($s in @('SYN-0063-QI-2026-01','SYN-0060-2026-A01','F-0061-2026-0001','TT-2026-SYN60A-DO-ATT-RST-S3-006-V01','62.5%','75.0%','100.0%','+12.5','2026-11-25','實際協會的人員派任','沒有專職品管')){"$s="+$body.Contains($s)}
