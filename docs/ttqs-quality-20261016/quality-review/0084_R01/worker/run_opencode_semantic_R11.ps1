$ErrorActionPreference = 'Stop'
$base = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$docx = Join-Path $base 'candidate/0084_R11.docx'
$packet = Join-Path $base 'review/semantic_review_packet_R11.md'
$promptFile = Join-Path $base 'review/semantic_review_prompt_R11.md'
$reviewDir = Join-Path $base 'review'
$stdout = Join-Path $reviewDir 'opencode_semantic_R11_stdout.jsonl'
$stderr = Join-Path $reviewDir 'opencode_semantic_R11_stderr.txt'
$exitFile = Join-Path $reviewDir 'opencode_semantic_R11_exit.txt'
$requestFile = Join-Path $reviewDir 'opencode_semantic_R11_request.json'
$resultFile = Join-Path $reviewDir 'opencode_semantic_R11_result.json'
$exe = 'C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe'
$expectedDocx = 'cf4376b3287db4f3a900fe7a39012e7dc6a49b419e586371b1eb1e0190a245d8'
$expectedPacket = 'f07a00034887ef956eb6b398f5e40bbe9ef9dc9088a8284b3f842dab58baee55'
$model = 'opencode/mimo-v2.6-flash-free'

function Get-Sha256([string]$Path) {
  return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

if (-not (Test-Path -LiteralPath $exe)) { throw "OpenCode CLI not found: $exe" }
$actualDocx = Get-Sha256 $docx
$actualPacket = Get-Sha256 $packet
if ($actualDocx -ne $expectedDocx -or $actualPacket -ne $expectedPacket) {
  throw "Exact-SHA inputs changed; no review dispatched. DOCX=$actualDocx packet=$actualPacket"
}
$cliVersion = (& $exe --version 2>&1 | Select-Object -First 1).ToString()
$started = [DateTimeOffset]::Now.ToString('o')
$request = [ordered]@{
  route = 'OpenCode CLI v2'
  cli_version = $cliVersion
  model = $model
  candidate_docx_sha256 = $actualDocx
  review_packet_sha256 = $actualPacket
  prompt_sha256 = Get-Sha256 $promptFile
  started_at_local = $started
  operation = 'one bounded independent semantic review; no write authorization; no retry on service/account failure'
}
$request | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $requestFile -Encoding utf8
$prompt = Get-Content -LiteralPath $promptFile -Raw -Encoding utf8
& $exe run --model $model --format json --title 'TTQS 0084 R11 exact-SHA semantic review' --file $packet $prompt 1> $stdout 2> $stderr
$code = $LASTEXITCODE
Set-Content -LiteralPath $exitFile -Value $code -Encoding ascii
$afterDocx = Get-Sha256 $docx
$afterPacket = Get-Sha256 $packet
$result = [ordered]@{
  route = 'OpenCode CLI v2'
  cli_version = $cliVersion
  model = $model
  candidate_docx_sha256_before = $actualDocx
  candidate_docx_sha256_after = $afterDocx
  candidate_unchanged_during_review = ($actualDocx -eq $afterDocx)
  review_packet_sha256_before = $actualPacket
  review_packet_sha256_after = $afterPacket
  packet_unchanged_during_review = ($actualPacket -eq $afterPacket)
  started_at_local = $started
  finished_at_local = [DateTimeOffset]::Now.ToString('o')
  exit_code = $code
  stdout_bytes = (Get-Item -LiteralPath $stdout -ErrorAction SilentlyContinue).Length
  stderr_bytes = (Get-Item -LiteralPath $stderr -ErrorAction SilentlyContinue).Length
  attempt_count = 1
  retry_count = 0
  verdict = 'PENDING_PARSE'
}
$result | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $resultFile -Encoding utf8
Get-Content -LiteralPath $resultFile -Raw -Encoding utf8
if ($code -ne 0) { exit $code }
