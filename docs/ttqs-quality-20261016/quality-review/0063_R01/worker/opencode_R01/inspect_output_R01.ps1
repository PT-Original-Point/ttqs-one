$ErrorActionPreference='Stop'
$p='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01\worker\opencode_R01\worker_output_R01.md'
$c=Get-Content -LiteralPath $p -Encoding UTF8
'HEADINGS:'; $c | Where-Object {$_ -match '^#{1,4} '}
'TABLES:'
for($i=0;$i -lt $c.Count;$i++){
 if($c[$i] -match '^\|'){
  $rows=@(); while($i -lt $c.Count -and $c[$i] -match '^\|'){ $rows+=,$c[$i]; $i++ }
  $counts=@($rows | ForEach-Object {([regex]::Matches($_,'(?<!\\)\|')).Count-1} | Select-Object -Unique)
  "rows=$($rows.Count) cols=$($counts -join ',') first=$($rows[0])"
 }
}
'KEY_FACTS:'; $c | Select-String -Pattern '5/8|6/8|8/8|62\.5|75\.0|100\.0|12\.5|068|0061|速度|效能|簽|核准|部門|理監事|2026-10-|2026-11-' | Select-Object -First 120 | ForEach-Object {$_.Line}
