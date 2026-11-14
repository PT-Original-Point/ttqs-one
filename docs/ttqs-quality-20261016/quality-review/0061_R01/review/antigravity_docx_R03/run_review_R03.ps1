$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repo = 'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016'
$lane = Join-Path $repo 'docs\ttqs-quality-20261016\quality-review\0061_R01'
$docx = Join-Path $lane 'candidate\0061_R03.docx'
$blueprint = Join-Path $lane 'inputs\0061_UNIQUE_BLUEPRINT_R02.md'
$sourcePacket = Join-Path $lane 'inputs\0061_BLUEPRINT_WRITER_PACKET_R01.md'
$packetPath = Join-Path $here 'review_packet_R03.md'
$promptPath = Join-Path $here 'antigravity_prompt_R03.md'
$expectedCandidateSha = '3D4FE20F7FB825E470ED5DFD71FCAF0F5BB8052DC7A63EF51EE08E2A11668C9C'
$expectedBlueprintSha = 'C58903927FA257DD43322BE1B25F25547CE282F964D0C435DA49623A6049CABB'
$expectedSourceSha = '8423FBC5F73B603AF3E5FD74F524AE33AD850465ADD466CABFB2FB5DEFC1CC41'
$expectedPacketSha = '0BE0E00B0EE806EA3C13AFEFDD9B03D13996E4395A972A0544AE6FEDCFC33978'
$sha = { param($p) (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.ToUpperInvariant() }
$actualCandidateSha = & $sha $docx
if ($actualCandidateSha -ne $expectedCandidateSha) { throw 'Candidate DOCX exact SHA mismatch.' }
$actualBlueprintSha = & $sha $blueprint
if ($actualBlueprintSha -ne $expectedBlueprintSha) { throw 'Blueprint exact SHA mismatch.' }
$actualSourceSha = & $sha $sourcePacket
if ($actualSourceSha -ne $expectedSourceSha) { throw 'Source packet exact SHA mismatch.' }
$actualPacketSha = & $sha $packetPath
if ($actualPacketSha -ne $expectedPacketSha) { throw 'Review packet exact SHA mismatch.' }
$promptText = [IO.File]::ReadAllText($promptPath,[Text.Encoding]::UTF8)
$packetText = [IO.File]::ReadAllText($packetPath,[Text.Encoding]::UTF8)
if ($promptText -match '\$packetSha|\$candidateSha|\$blueprintSha|\$sourceSha') { throw 'Unresolved variable placeholder in prompt.' }
foreach ($h in @($expectedCandidateSha,$expectedBlueprintSha,$expectedSourceSha,$expectedPacketSha)) { if (-not $promptText.Contains($h)) { throw "Prompt missing exact hash $h" } }
$fullPrompt = $promptText + "`r`n`r`n" + $packetText
$inputObject = @{ event='user'; message=@{content=$fullPrompt} }
$inputLine = ConvertTo-Json -InputObject $inputObject -Compress -Depth 8
$agy = Join-Path $env:LOCALAPPDATA 'agy\bin\agy.exe'
if (-not (Test-Path -LiteralPath $agy)) { throw "Antigravity CLI not found at $agy" }
$stdoutPath = Join-Path $here 'stdout_R03.jsonl'
$stderrPath = Join-Path $here 'stderr_R03.txt'
$responsePath = Join-Path $here 'response_R03.txt'
$receiptPath = Join-Path $here 'invocation_receipt_R03.json'
$psi = [Diagnostics.ProcessStartInfo]::new()
$psi.FileName = $agy
$psi.Arguments = '--input-format stream-json --output-format stream-json --model gemini-3.8-flash-high --effort high --mode plan --sandbox --print-timeout 15m'
$psi.WorkingDirectory = $repo
$psi.UseShellExecute = $false; $psi.CreateNoWindow = $true
$psi.RedirectStandardInput = $true; $psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true
$psi.StandardInputEncoding = [Text.UTF8Encoding]::new($false)
$psi.StandardOutputEncoding = [Text.UTF8Encoding]::new($false)
$psi.StandardErrorEncoding = [Text.UTF8Encoding]::new($false)
$proc = [Diagnostics.Process]::new(); $proc.StartInfo = $psi
$started = [DateTimeOffset]::Now
if (-not $proc.Start()) { throw 'Antigravity process did not start.' }
$stdoutTask = $proc.StandardOutput.ReadToEndAsync(); $stderrTask = $proc.StandardError.ReadToEndAsync()
$proc.StandardInput.WriteLine($inputLine); $proc.StandardInput.Close()
if (-not $proc.WaitForExit(900000)) { $proc.Kill($true); $proc.WaitForExit(); $exitCode=124 } else { $exitCode=$proc.ExitCode }
$ended = [DateTimeOffset]::Now
$stdout=$stdoutTask.GetAwaiter().GetResult(); $stderr=$stderrTask.GetAwaiter().GetResult()
$utf8=[Text.UTF8Encoding]::new($false)
[IO.File]::WriteAllText($stdoutPath,$stdout,$utf8); [IO.File]::WriteAllText($stderrPath,$stderr,$utf8)
$events=@(); foreach($line in ($stdout -split "`r?`n")) { if(-not [string]::IsNullOrWhiteSpace($line)) { try{$events+=($line|ConvertFrom-Json -Depth 40)}catch{} } }
$finalEvent=$events|Where-Object{$_.event -eq 'result'}|Select-Object -Last 1
$result=if($finalEvent){$finalEvent.result}else{$null}
$response=if($result -and $null -ne $result.response){[string]$result.response}else{''}
[IO.File]::WriteAllText($responsePath,$response,$utf8)
$receipt=[ordered]@{
  Started=$started.ToString('o'); Ended=$ended.ToString('o'); DurationSeconds=[Math]::Round(($ended-$started).TotalSeconds,3)
  ExitCode=$exitCode; CliVersion='1.4.1'; ModelRequested='gemini-3.8-flash-high'; ModelIdentityAttestation='UNKNOWN; CLI response envelope may not attest runtime model.'
  Effort='high'; Mode='plan'; Sandbox=$true; ComputerUse=$false; FileAccess=$false; ToolUseRequested=$false
  CandidateDocxSHA256=$expectedCandidateSha; BlueprintSHA256=$expectedBlueprintSha; SourcePacketSHA256=$expectedSourceSha; ReviewPacketSHA256=$expectedPacketSha
  PromptSHA256=& $sha $promptPath; InputCharacters=$fullPrompt.Length; InputLineBytes=[Text.Encoding]::UTF8.GetByteCount($inputLine)
  Stdout=$stdoutPath; StdoutBytes=[Text.Encoding]::UTF8.GetByteCount($stdout); StdoutSHA256=& $sha $stdoutPath
  Stderr=$stderrPath; StderrBytes=[Text.Encoding]::UTF8.GetByteCount($stderr); StderrSHA256=& $sha $stderrPath
  Response=$responsePath; ResponseBytes=[Text.Encoding]::UTF8.GetByteCount($response); ResponseSHA256=& $sha $responsePath
  ConversationId=if($result){$result.conversation_id}else{$null}; Status=if($result){$result.status}else{'NO_RESULT_EVENT'}; Error=if($result){$result.error}else{$null}; Usage=if($result){$result.usage}else{$null}
  ProviderCost='UNKNOWN; not returned by CLI receipt.'
}
$receipt|ConvertTo-Json -Depth 12|Set-Content -LiteralPath $receiptPath -Encoding utf8
Write-Output "EXIT=$exitCode"; Write-Output "STATUS=$($receipt.Status)"; Write-Output "MODEL=$($receipt.ModelRequested)"; Write-Output "RESPONSE_BYTES=$($receipt.ResponseBytes)"; Write-Output "CONVERSATION=$($receipt.ConversationId)"; Write-Output "DOCX_SHA=$expectedCandidateSha"; Write-Output "PACKET_SHA=$expectedPacketSha"; Write-Output "RESPONSE_SHA=$($receipt.ResponseSHA256)"; Write-Output "STDOUT_SHA=$($receipt.StdoutSHA256)"; Write-Output "STDERR_SHA=$($receipt.StderrSHA256)"
if ($exitCode -ne 0 -or $receipt.Status -ne 'SUCCESS' -or $receipt.ResponseBytes -eq 0) { exit 1 }

