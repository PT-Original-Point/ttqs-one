$ErrorActionPreference = "Stop"
$base = "E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0059_R01"
$review = Join-Path $base "review\antigravity_semantic_R03"
$agy = "C:\Users\J\AppData\Local\agy\bin\agy.exe"
$packet = Join-Path $review "review_packet_R01.md"
$promptFile = Join-Path $review "antigravity_prompt_R01.md"
$stdout = Join-Path $review "stdout_R01.json"
$stderr = Join-Path $review "stderr_R01.txt"
$receipt = Join-Path $review "invocation_receipt_R01.json"
if (-not (Test-Path -LiteralPath $agy)) { throw "Antigravity CLI not found: $agy" }
if (-not (Test-Path -LiteralPath $packet)) { throw "Review packet not found: $packet" }
if ((Get-FileHash -LiteralPath $base\0059_R03.docx -Algorithm SHA256).Hash -ne "0263017F16D81B1121BB97410DE9895B43B7A42F75632BF71A82B86426FBC2B0") { throw "Candidate SHA changed before review." }
$prompt = "Read the complete review packet at E:/TTQS/_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016/docs/ttqs-quality-20261016/quality-review/0059_R01/review/antigravity_semantic_R03/review_packet_R01.md. Follow antigravity_prompt_R01.md instructions contained in the same directory. Perform a read-only semantic review. Do not use Computer Use or external tools, do not edit files, and review the exact DOCX SHA stated in the packet. Return only the required structured JSON verdict and concrete section/table locators."
$started = Get-Date
$clock = [System.Diagnostics.Stopwatch]::StartNew()
& $agy --model gemini-3.8-flash-high --effort high --mode plan --sandbox --output-format json --print-timeout 0s --print $prompt 1> $stdout 2> $stderr
$exitCode = $LASTEXITCODE
$clock.Stop()
$ended = Get-Date
$hash = { param($p) (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash }
$receiptObject = [ordered]@{
    Started = $started.ToString("o")
    Ended = $ended.ToString("o")
    DurationSeconds = [math]::Round($clock.Elapsed.TotalSeconds,3)
    ExitCode = $exitCode
    ModelRequested = "gemini-3.8-flash-high"
    Effort = "high"
    Mode = "plan"
    Sandbox = $true
    ComputerUse = $false
    CandidateSHA256 = & $hash (Join-Path $base "0059_R03.docx")
    Packet = $packet
    PacketSHA256 = & $hash $packet
    PromptFile = $promptFile
    PromptSHA256 = & $hash $promptFile
    Output = $stdout
    OutputBytes = (Get-Item -LiteralPath $stdout).Length
    OutputSHA256 = & $hash $stdout
    Stderr = $stderr
    StderrBytes = (Get-Item -LiteralPath $stderr).Length
    StderrSHA256 = & $hash $stderr
    ModelIdentityAttestation = "UNKNOWN; CLI model slug records requested model only."
    ProviderCost = "UNKNOWN; not returned by CLI receipt."
}
$receiptObject | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $receipt -Encoding utf8
if ($exitCode -ne 0) { throw "Antigravity CLI exit code $exitCode. Raw stdout and stderr are preserved." }
[pscustomobject]$receiptObject | Format-List
