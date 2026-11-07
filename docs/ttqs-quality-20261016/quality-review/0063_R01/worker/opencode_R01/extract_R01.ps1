param()
$ErrorActionPreference='Stop'
$work='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01\worker\opencode_R01'
$raw=Get-Content -LiteralPath (Join-Path $work 'stdout_R01.jsonl') -Encoding UTF8
$events=@($raw | ForEach-Object { $_ | ConvertFrom-Json })
$text=($events | Where-Object {$_.type -eq 'text'} | ForEach-Object {$_.part.text}) -join ''
if([string]::IsNullOrWhiteSpace($text)){throw 'OpenCode returned no text event'}
$out=Join-Path $work 'worker_output_R01.md'
[System.IO.File]::WriteAllText($out,$text,[System.Text.UTF8Encoding]::new($false))
$finish=$events | Where-Object {$_.type -eq 'step_finish'} | Select-Object -Last 1
$receiptPath=Join-Path $work 'invocation_receipt_R01.json'
$receipt=Get-Content -LiteralPath $receiptPath -Raw -Encoding UTF8 | ConvertFrom-Json -AsHashtable
$receipt.provider_usage=[ordered]@{source='OpenCode CLI step_finish JSON event';reported_cost=$finish.part.cost;input_tokens=$finish.part.tokens.input;output_tokens=$finish.part.tokens.output;reasoning_tokens=$finish.part.tokens.reasoning;cache_read_tokens=$finish.part.tokens.cache.read;cache_write_tokens=$finish.part.tokens.cache.write}
$receipt.result_path=$out
$receipt.result_sha256=(Get-FileHash -LiteralPath $out -Algorithm SHA256).Hash.ToLowerInvariant()
$receipt.result_chars=$text.Length
[System.IO.File]::WriteAllText($receiptPath,($receipt|ConvertTo-Json -Depth 10),[System.Text.UTF8Encoding]::new($false))
"TEXT_CHARS=$($text.Length) RESULT_SHA=$($receipt.result_sha256) COST=$($finish.part.cost) INPUT=$($finish.part.tokens.input) OUTPUT=$($finish.part.tokens.output) REASONING=$($finish.part.tokens.reasoning) EVENTS=$($events.Count)"
"---FIRST---"; Get-Content -LiteralPath $out -Encoding UTF8 -TotalCount 30
"---LAST---"; Get-Content -LiteralPath $out -Encoding UTF8 -Tail 30
