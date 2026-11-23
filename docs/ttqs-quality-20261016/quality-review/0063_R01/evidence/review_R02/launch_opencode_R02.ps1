$ErrorActionPreference = 'Stop'
$repo = 'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016'
$exe = 'C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe'
$model = 'opencode/deepseek-v4.1-flash-free'
$relPacket = 'docs/ttqs-quality-20261016/quality-review/0063_R01/evidence/review_R02/0063_R02_SEMANTIC_REVIEW_PACKET.md'
$relDocx = 'docs/ttqs-quality-20261016/quality-review/0063_R01/candidate/0063_R02.docx'
$docSha = (Get-FileHash -LiteralPath (Join-Path $repo $relDocx) -Algorithm SHA256).Hash.ToLower()
$expected = 'b1e8210b57d00813596d343403526787f065da51afcf5df4434868f0c96279f5'
if ($docSha -ne $expected) { throw "Candidate SHA mismatch: $docSha" }
$models = @(& $exe models)
if ($LASTEXITCODE -ne 0 -or $models -notcontains $model) { throw 'Report-priority model is not available from this OpenCode CLI.' }
$active = @(Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'opencode-cli.exe' -and $_.CommandLine -match '\brun\b' -and $_.CommandLine -match '0063' })
if ($active.Count -gt 0) { throw "Existing 0063 run found; refusing duplicate dispatch. PIDs=$($active.ProcessId -join ',')" }
$prompt = "Independent semantic review only. Review the complete packet at $relPacket and the DOCX at $relDocx. Bind the verdict to exact DOCX SHA-256 $expected, official requirement I14-E04 / checkbox 068, and Unique Blueprint SHA-256 9c5e91155a18ccb5aae2a21f7bba40f35d8c483b973436873f08e2fde925dd34. Use the official mapping, unique Blueprint, cross-document facts, complete extracted body, and synthetic replacement register in the packet. Do not use provisional R01 output as a verdict. Return one complete standalone Markdown report with overall PASS, PARTIAL, or FAIL; concrete body/table locators; official-purpose and correct genre; negative-neighbor separation; operational usability for a small volunteer association; SAMPLE/REAL boundary; arithmetic/date consistency; and hard rejection conditions. State that visual review is outside this semantic verdict. Do not edit or rebuild any file. Finish with the explicit terminal verdict."
$outDir = Join-Path $repo 'docs/ttqs-quality-20261016/quality-review/0063_R01/evidence/review_R02'
$requestPath = Join-Path $outDir 'opencode_R02_request.txt'
$stdout = Join-Path $outDir 'opencode_R02_stdout.jsonl'
$stderr = Join-Path $outDir 'opencode_R02_stderr.txt'
$receiptPath = Join-Path $outDir 'opencode_R02_launch_receipt.json'
[IO.File]::WriteAllText($requestPath,$prompt,[Text.UTF8Encoding]::new($false))
$quoted = '"' + $prompt.Replace('"','\"') + '"'
$args = "run --model $model --format json $quoted"
$proc = Start-Process -FilePath $exe -ArgumentList $args -WorkingDirectory $repo -RedirectStandardOutput $stdout -RedirectStandardError $stderr -PassThru -WindowStyle Hidden
$receipt = [ordered]@{project_id='TTQS_ONE';doc_id='0063';candidate_revision='R02';candidate_sha256=$docSha;official_requirement_id='I14-E04';official_checkbox_sequence='068';unique_blueprint_sha256='9c5e91155a18ccb5aae2a21f7bba40f35d8c483b973436873f08e2fde925dd34';cli_version='opencode v2.0.29';model=$model;model_source='2026-10-18 OpenCode free model monitoring report, first-priority isolated test';packet_path=$relPacket;packet_sha256=(Get-FileHash -LiteralPath (Join-Path $repo $relPacket) -Algorithm SHA256).Hash.ToLower();request_path='opencode_R02_request.txt';request_sha256=(Get-FileHash -LiteralPath $requestPath -Algorithm SHA256).Hash.ToLower();pid=$proc.Id;started_local=(Get-Date).ToString('o');stdout_path='opencode_R02_stdout.jsonl';stderr_path='opencode_R02_stderr.txt';status='RUNNING';provider_billing='UNKNOWN';visual_review_separate=$true}
[IO.File]::WriteAllText($receiptPath,($receipt | ConvertTo-Json -Depth 5),[Text.UTF8Encoding]::new($false))
$receipt | ConvertTo-Json -Depth 5