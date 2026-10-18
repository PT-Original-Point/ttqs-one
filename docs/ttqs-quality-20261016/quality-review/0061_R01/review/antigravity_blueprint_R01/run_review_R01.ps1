$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$packetPath = Join-Path $here 'review_packet_R01.md'
$promptPath = Join-Path $here 'antigravity_prompt_R01.md'
$expectedPacketSha = 'BA85566CD15D6CD8C12F59A61D204146513F8C7869DCF25E2F505B801863283E'
$expectedCandidateSha = '8BD571FEA48D9B401A9416BD991AD4FC52AA566E3550DC0EFB362344C9E5A4B7'
$expectedSourceSha = '8423FBC5F73B603AF3E5FD74F524AE33AD850465ADD466CABFB2FB5DEFC1CC41'
$packetSha = (Get-FileHash -LiteralPath $packetPath -Algorithm SHA256).Hash.ToUpperInvariant()
if ($packetSha -ne $expectedPacketSha) { throw "Review packet SHA mismatch: $packetSha" }
$repo = 'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016'
$candidate = Join-Path $repo 'docs\ttqs-quality-20261016\quality-review\0061_R01\inputs\0061_UNIQUE_BLUEPRINT_R02.md'
$candidateSha = (Get-FileHash -LiteralPath $candidate -Algorithm SHA256).Hash.ToUpperInvariant()
if ($candidateSha -ne $expectedCandidateSha) { throw "Blueprint SHA mismatch: $candidateSha" }
$sourcePacket = Join-Path $repo 'docs\ttqs-quality-20261016\quality-review\0061_R01\inputs\0061_BLUEPRINT_WRITER_PACKET_R01.md'
$sourceSha = (Get-FileHash -LiteralPath $sourcePacket -Algorithm SHA256).Hash.ToUpperInvariant()
if ($sourceSha -ne $expectedSourceSha) { throw "Source packet SHA mismatch: $sourceSha" }
$promptText = [IO.File]::ReadAllText($promptPath, [Text.Encoding]::UTF8)
$packetText = [IO.File]::ReadAllText($packetPath, [Text.Encoding]::UTF8)
$fullPrompt = $promptText + "`r`n`r`n" + $packetText
$inputObject = @{ event = 'user'; message = @{ content = $fullPrompt } }
$inputLine = ConvertTo-Json -InputObject $inputObject -Compress -Depth 8
$agy = Join-Path $env:LOCALAPPDATA 'agy\bin\agy.exe'
$stdoutPath = Join-Path $here 'stdout_R01.jsonl'
$stderrPath = Join-Path $here 'stderr_R01.txt'
$responsePath = Join-Path $here 'response_R01.txt'
$receiptPath = Join-Path $here 'invocation_receipt_R01.json'
$psi = [Diagnostics.ProcessStartInfo]::new()
$psi.FileName = $agy
$psi.Arguments = '--input-format stream-json --output-format stream-json --model gemini-3.8-flash-high --effort high --mode plan --sandbox --print-timeout 15m'
$psi.WorkingDirectory = $repo
$psi.UseShellExecute = $false
$psi.CreateNoWindow = $true
$psi.RedirectStandardInput = $true
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$psi.StandardInputEncoding = [Text.UTF8Encoding]::new($false)
$psi.StandardOutputEncoding = [Text.UTF8Encoding]::new($false)
$psi.StandardErrorEncoding = [Text.UTF8Encoding]::new($false)
$proc = [Diagnostics.Process]::new()
$proc.StartInfo = $psi
$started = [DateTimeOffset]::Now
if (-not $proc.Start()) { throw 'Antigravity process did not start.' }
$stdoutTask = $proc.StandardOutput.ReadToEndAsync()
$stderrTask = $proc.StandardError.ReadToEndAsync()
$proc.StandardInput.WriteLine($inputLine)
$proc.StandardInput.Close()
if (-not $proc.WaitForExit(900000)) { $proc.Kill($true); $proc.WaitForExit(); $exitCode = 124 } else { $exitCode = $proc.ExitCode }
$ended = [DateTimeOffset]::Now
$stdout = $stdoutTask.GetAwaiter().GetResult()
$stderr = $stderrTask.GetAwaiter().GetResult()
$utf8 = [Text.UTF8Encoding]::new($false)
[IO.File]::WriteAllText($stdoutPath, $stdout, $utf8)
[IO.File]::WriteAllText($stderrPath, $stderr, $utf8)
$events = @()
foreach ($line in ($stdout -split "`r?`n")) { if (-not [string]::IsNullOrWhiteSpace($line)) { try { $events += ($line | ConvertFrom-Json -Depth 40) } catch {} } }
$finalEvent = $events | Where-Object { $_.event -eq 'result' } | Select-Object -Last 1
$result = if ($finalEvent) { $finalEvent.result } else { $null }
$response = if ($result -and $null -ne $result.response) { [string]$result.response } else { '' }
[IO.File]::WriteAllText($responsePath, $response, $utf8)
$stdoutBytes = [IO.File]::ReadAllBytes($stdoutPath)
$stderrBytes = [IO.File]::ReadAllBytes($stderrPath)
$responseBytes = [IO.File]::ReadAllBytes($responsePath)
$receipt = [ordered]@{
  Started = $started.ToString('o'); Ended = $ended.ToString('o'); DurationSeconds = [Math]::Round(($ended - $started).TotalSeconds, 3)
  ExitCode = $exitCode; CliVersion = '1.4.1'; ModelRequested = 'gemini-3.8-flash-high'; ModelIdentityAttestation = 'UNKNOWN; CLI response envelope may not attest runtime model.'
  Effort = 'high'; Mode = 'plan'; Sandbox = $true; ComputerUse = $false; FileAccess = $false; ToolUseRequested = $false
  CandidateBlueprintSHA256 = $candidateSha; SourcePacketSHA256 = $sourceSha; ReviewPacketSHA256 = $packetSha
  PromptSHA256 = (Get-FileHash -LiteralPath $promptPath -Algorithm SHA256).Hash.ToUpperInvariant(); InputCharacters = $fullPrompt.Length
  Stdout = $stdoutPath; StdoutBytes = $stdoutBytes.Length; StdoutSHA256 = (Get-FileHash -LiteralPath $stdoutPath -Algorithm SHA256).Hash.ToUpperInvariant()
  Stderr = $stderrPath; StderrBytes = $stderrBytes.Length; StderrSHA256 = (Get-FileHash -LiteralPath $stderrPath -Algorithm SHA256).Hash.ToUpperInvariant()
  Response = $responsePath; ResponseBytes = $responseBytes.Length; ResponseSHA256 = (Get-FileHash -LiteralPath $responsePath -Algorithm SHA256).Hash.ToUpperInvariant()
  ConversationId = if ($result) { $result.conversation_id } else { $null }; Status = if ($result) { $result.status } else { 'NO_RESULT_EVENT' }
  Error = if ($result) { $result.error } else { $null }; Usage = if ($result) { $result.usage } else { $null }; ProviderCost = 'UNKNOWN; not returned by CLI receipt.'
}
$receipt | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $receiptPath -Encoding utf8
Write-Output "EXIT=$exitCode"
Write-Output "STATUS=$($receipt.Status)"
Write-Output "RESPONSE_BYTES=$($receipt.ResponseBytes)"
Write-Output "CONVERSATION=$($receipt.ConversationId)"
Write-Output "STDOUT_SHA=$($receipt.StdoutSHA256)"
Write-Output "STDERR_SHA=$($receipt.StderrSHA256)"
Write-Output "RESPONSE_SHA=$($receipt.ResponseSHA256)"
if ($exitCode -ne 0 -or $receipt.Status -ne 'SUCCESS' -or $receipt.ResponseBytes -eq 0) { exit 1 }
