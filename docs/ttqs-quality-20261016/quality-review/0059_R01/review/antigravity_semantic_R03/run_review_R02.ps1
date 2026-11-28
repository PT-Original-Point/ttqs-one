$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$repo = (Resolve-Path (Join-Path $here '..\..\..\..\..\..')).Path
$packetPath = Join-Path $here 'review_packet_R01.md'
$promptPath = Join-Path $here 'antigravity_prompt_R02.md'
$expectedPacketSha = '936E3011C867A422CC1313AE0137A1C8D2C793AC1DB5523858D85D43DD5F4587'
$expectedDocxSha = '0263017F16D81B1121BB97410DE9895B43B7A42F75632BF71A82B86426FBC2B0'
$packetSha = (Get-FileHash -LiteralPath $packetPath -Algorithm SHA256).Hash.ToUpperInvariant()
$docxPath = Join-Path $repo 'docs\ttqs-quality-20261016\quality-review\0059_R01\0059_R03.docx'
$docxSha = (Get-FileHash -LiteralPath $docxPath -Algorithm SHA256).Hash.ToUpperInvariant()
if ($packetSha -ne $expectedPacketSha) { throw "Packet SHA mismatch: $packetSha" }
if ($docxSha -ne $expectedDocxSha) { throw "DOCX SHA mismatch: $docxSha" }

$promptText = [IO.File]::ReadAllText($promptPath, [Text.Encoding]::UTF8)
$packetText = [IO.File]::ReadAllText($packetPath, [Text.Encoding]::UTF8)
$fullPrompt = $promptText + $packetText
$inputObject = @{ event = 'user'; message = @{ content = $fullPrompt } }
$inputLine = ConvertTo-Json -InputObject $inputObject -Compress -Depth 8

$agy = Join-Path $env:LOCALAPPDATA 'agy\bin\agy.exe'
$stdoutPath = Join-Path $here 'stdout_R02.jsonl'
$stderrPath = Join-Path $here 'stderr_R02.txt'
$responsePath = Join-Path $here 'response_R02.txt'
$receiptPath = Join-Path $here 'invocation_receipt_R02.json'
$psi = [Diagnostics.ProcessStartInfo]::new()
$psi.FileName = $agy
$psi.Arguments = '--input-format stream-json --output-format stream-json --model gemini-3.8-flash-high --effort high --mode plan --sandbox --print-timeout 0'
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
if (-not $proc.WaitForExit(900000)) {
    $proc.Kill($true)
    $proc.WaitForExit()
    $exitCode = 124
} else {
    $exitCode = $proc.ExitCode
}
$ended = [DateTimeOffset]::Now
$stdout = $stdoutTask.GetAwaiter().GetResult()
$stderr = $stderrTask.GetAwaiter().GetResult()
$utf8NoBom = [Text.UTF8Encoding]::new($false)
[IO.File]::WriteAllText($stdoutPath, $stdout, $utf8NoBom)
[IO.File]::WriteAllText($stderrPath, $stderr, $utf8NoBom)

$events = @()
foreach ($line in ($stdout -split "`r?`n")) {
    if (-not [string]::IsNullOrWhiteSpace($line)) {
        try { $events += ($line | ConvertFrom-Json -Depth 30) } catch { }
    }
}
$finalEvent = $events | Where-Object { $_.event -eq 'result' } | Select-Object -Last 1
$result = if ($finalEvent) { $finalEvent.result } else { $null }
$response = if ($result -and $null -ne $result.response) { [string]$result.response } else { '' }
[IO.File]::WriteAllText($responsePath, $response, $utf8NoBom)

$stdoutBytes = [IO.File]::ReadAllBytes($stdoutPath)
$stderrBytes = [IO.File]::ReadAllBytes($stderrPath)
$responseBytes = [IO.File]::ReadAllBytes($responsePath)
$receipt = [ordered]@{
    Started = $started.ToString('o')
    Ended = $ended.ToString('o')
    DurationSeconds = [Math]::Round(($ended - $started).TotalSeconds, 3)
    ExitCode = $exitCode
    ModelRequested = 'gemini-3.8-flash-high'
    ModelIdentityAttestation = 'UNKNOWN; CLI model slug records requested model only.'
    Effort = 'high'
    Mode = 'plan'
    Sandbox = $true
    ComputerUse = $false
    InputTransport = 'Antigravity CLI stream-json stdin; complete review packet embedded in user message; no file/tool access requested.'
    CandidateSHA256 = $docxSha
    PacketSHA256 = $packetSha
    PromptFile = $promptPath
    PromptFileSHA256 = (Get-FileHash -LiteralPath $promptPath -Algorithm SHA256).Hash.ToUpperInvariant()
    InputCharacters = $fullPrompt.Length
    Output = $stdoutPath
    OutputBytes = $stdoutBytes.Length
    OutputSHA256 = (Get-FileHash -LiteralPath $stdoutPath -Algorithm SHA256).Hash.ToUpperInvariant()
    Stderr = $stderrPath
    StderrBytes = $stderrBytes.Length
    StderrSHA256 = (Get-FileHash -LiteralPath $stderrPath -Algorithm SHA256).Hash.ToUpperInvariant()
    Response = $responsePath
    ResponseBytes = $responseBytes.Length
    ResponseSHA256 = (Get-FileHash -LiteralPath $responsePath -Algorithm SHA256).Hash.ToUpperInvariant()
    ConversationId = if ($result) { $result.conversation_id } else { $null }
    Status = if ($result) { $result.status } else { 'NO_RESULT_EVENT' }
    Error = if ($result) { $result.error } else { $null }
    Usage = if ($result) { $result.usage } else { $null }
    ProviderCost = 'UNKNOWN; not returned by CLI receipt.'
}
$receipt | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $receiptPath -Encoding utf8
Write-Output "EXIT=$exitCode"
Write-Output "STATUS=$($receipt.Status)"
Write-Output "RESPONSE_BYTES=$($receipt.ResponseBytes)"
Write-Output "CONVERSATION=$($receipt.ConversationId)"
Write-Output "STDOUT_SHA=$($receipt.OutputSHA256)"
Write-Output "STDERR_SHA=$($receipt.StderrSHA256)"
Write-Output "RESPONSE_SHA=$($receipt.ResponseSHA256)"
if ($exitCode -ne 0 -or $receipt.Status -ne 'SUCCESS' -or $receipt.ResponseBytes -eq 0) { exit 1 }
