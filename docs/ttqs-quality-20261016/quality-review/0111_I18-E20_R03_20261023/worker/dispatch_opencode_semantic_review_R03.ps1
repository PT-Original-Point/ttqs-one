$ErrorActionPreference = 'Stop'
$root = 'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0111_I18-E20_SOURCE_PREP_20261023'
$review = Join-Path $root 'review'
$candidate = Join-Path $root 'candidate\0111_I18-E20_特殊績效及社會面成果證據登錄表_R03.docx'
$packet = Join-Path $review 'semantic_review_packet_0111_R03.md'
$exe = 'C:\Users\J\AppData\Roaming\ai.opencode.desktop\cli\2.0.32-x64\opencode-cli.exe'
$model = 'opencode/mimo-v2.6-flash-free'
$expectedDocx = 'f427ed898a79393a91d6d8fadcde960a8126e90697325aa94c1b764b8b537a50'
$expectedPacket = 'fa2582e9d1d43f6c31932b92988a346436c54046afb124a0725faccb2ec55033'
$stdout = Join-Path $review 'opencode_semantic_review_0111_R03_stdout.jsonl'
$stderr = Join-Path $review 'opencode_semantic_review_0111_R03_stderr.txt'
$dispatchPath = Join-Path $review 'opencode_semantic_review_0111_R03_dispatch.json'
$resultPath = Join-Path $review 'opencode_semantic_review_0111_R03_process_result.json'
$jsonEncoding = [System.Text.UTF8Encoding]::new($false)

if (-not (Test-Path -LiteralPath $exe)) { throw 'OpenCode v2 CLI missing.' }
$docSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $candidate).Hash.ToLower()
$packetSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $packet).Hash.ToLower()
if ($docSha -ne $expectedDocx) { throw "Refusing review: DOCX SHA changed: $docSha" }
if ($packetSha -ne $expectedPacket) { throw "Refusing review: packet SHA changed: $packetSha" }
$active = @(Get-CimInstance Win32_Process | Where-Object {
    $_.CommandLine -match 'opencode-cli\.exe.*run' -and $_.CommandLine -match 'semantic_review_0111_R03'
})
if ($active.Count -gt 0) { throw 'A live 0111 exact-scope reviewer process already exists.' }

$args = @('run','--model',$model,'--agent','plan','--format','json','--file',$packet,'REVIEW_EXACT_SHA_0111_I18-E20_R03_READ_ONLY_NO_FALLBACK')
$started = (Get-Date).ToString('o')
$proc = Start-Process -FilePath $exe -ArgumentList $args -WorkingDirectory $root -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
$dispatch = [ordered]@{
    project_id = 'TTQS_ONE'; work_id = 'TTQS-0111-I18-E20-INDEPENDENT-SEMANTIC-REVIEW-R03-20261023'
    doc_id = '0111'; requirement_id = 'I18-E20'; official_checkbox_serial = 'UNKNOWN_NOT_ASSERTED'
    worker = 'OpenCode v2 CLI'; cli_path = $exe; cli_version = '2.0.32'; pid = $proc.Id
    requested_model = $model; actual_model = 'UNKNOWN_PENDING_NATIVE_OUTPUT_READBACK'; provider_billing = 'UNKNOWN_PENDING_NATIVE_OUTPUT_READBACK'
    candidate_sha256 = $docSha; review_packet_sha256 = $packetSha; started_at_local = $started
    window_style = 'Hidden'; agent = 'plan'; computer_use = $false; file_edit_or_write = 'NOT_REQUESTED'; fallback = 'PROHIBITED'
    stdout_path = $stdout; stderr_path = $stderr; status = 'DISPATCHED_BOUNDED_SINGLE_ATTEMPT'
}
[IO.File]::WriteAllText($dispatchPath,($dispatch | ConvertTo-Json -Depth 5),$jsonEncoding)
Write-Output ('DISPATCH_PID=' + $proc.Id)
Write-Output ('REQUESTED_MODEL=' + $model)
Write-Output ('CANDIDATE_SHA=' + $docSha)
Write-Output ('PACKET_SHA=' + $packetSha)
Write-Output 'WINDOW_STYLE=Hidden'

$done = $proc.WaitForExit(480000)
$proc.Refresh()
$result = [ordered]@{
    work_id = $dispatch.work_id; doc_id = '0111'; pid = $proc.Id; started_at_local = $started
    finished_at_local = (Get-Date).ToString('o'); exit_code = if ($done) { $proc.ExitCode } else { $null }
    timed_out = (-not $done); requested_model = $model; actual_model = 'UNKNOWN_PENDING_NATIVE_OUTPUT_READBACK'
    stdout_bytes = if (Test-Path -LiteralPath $stdout) { (Get-Item -LiteralPath $stdout).Length } else { 0 }
    stderr_bytes = if (Test-Path -LiteralPath $stderr) { (Get-Item -LiteralPath $stderr).Length } else { 0 }
    state = if ($done) { 'EXITED' } else { 'STILL_RUNNING' }
}
[IO.File]::WriteAllText($resultPath,($result | ConvertTo-Json -Depth 5),$jsonEncoding)
Write-Output ($result | ConvertTo-Json -Compress)
