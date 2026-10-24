$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$cli = 'C:\Users\J\AppData\Roaming\ai.opencode.desktop\cli\2.1.4-x64\opencode-cli.exe'
$inputFile = Join-Path $root 'REVIEW_INPUT_0136_R01_EXACT_SHA.md'
$stdoutFile = Join-Path $root 'REVIEWER_OPENCODE_DEEPSEEK_R01_STDOUT.jsonl'
$stderrFile = Join-Path $root 'REVIEWER_OPENCODE_DEEPSEEK_R01_STDERR.txt'
$receiptFile = Join-Path $root 'REVIEWER_OPENCODE_DEEPSEEK_R01_RECEIPT.json'
$prompt = @'
Perform an independent, read-only semantic review of the exact DOCX candidate identified in the attached review packet. The packet binds the target to DOCX SHA-256 a9bd0fb528a1e22865fa5e07df44b314d48c1fd826a08149ecdd1d5915048b39. The review target is DOCX 0136, official requirement I19-E26, project index 150; the printed checkbox serial is UNKNOWN. Compare the official requirement and the Unique Blueprint with the candidate body. Do not edit, call tools, claim association approval, or infer real evidence. Treat all SAMPLE/SYNTHETIC examples as demonstrations. Assess document type, operational usefulness, completeness of workflows/forms, rejection/hold rules, source and role verification, crosswalk separation from 0135/I19-E25 and 0137/I19-E27 and nearby I19-E22/E23, consistency, and any unsupported claims. Do not assess page layout; layout is reviewed separately against this exact SHA. Return an explicit PASS, PARTIAL, or FAIL for semantic content only, with findings tied to section headings, table labels, and quoted short anchors; explain any material defect and concrete minimal correction. If no material semantic defect is found, say so but do not grant formal acceptance. If the input is insufficient, use UNKNOWN. Review only the supplied attachment; no model fallback or other route is authorized.
'@
$args = @('run', '--model', 'opencode/deepseek-v4.1-flash-free', '--format', 'json', '--file', $inputFile, $prompt)
$quoted = foreach ($arg in $args) { '"' + $arg.Replace('"', '\"') + '"' }
$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = $cli
$psi.Arguments = $quoted -join ' '
$psi.UseShellExecute = $false
$psi.CreateNoWindow = $true
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$proc = New-Object System.Diagnostics.Process
$proc.StartInfo = $psi
$started = [DateTimeOffset]::Now
if (-not $proc.Start()) { throw 'OpenCode reviewer process did not start.' }
$pidValue = $proc.Id
$stdoutTask = $proc.StandardOutput.ReadToEndAsync()
$stderrTask = $proc.StandardError.ReadToEndAsync()
$finished = $proc.WaitForExit(180000)
if (-not $finished) {
    $proc.Kill()
    $proc.WaitForExit()
}
$ended = [DateTimeOffset]::Now
$stdout = $stdoutTask.Result
$stderr = $stderrTask.Result
[IO.File]::WriteAllText($stdoutFile, $stdout, [Text.UTF8Encoding]::new($false))
[IO.File]::WriteAllText($stderrFile, $stderr, [Text.UTF8Encoding]::new($false))
$sha = (Get-FileHash -LiteralPath $inputFile -Algorithm SHA256).Hash.ToLowerInvariant()
$receipt = [ordered]@{
    work_id = 'TTQS-0136-SEMANTIC-REVIEW-20261025-R01'
    project_id = 'TTQS_ONE'
    doc_id = '0136'
    official_requirement_id = 'I19-E26'
    target_docx_sha256 = 'a9bd0fb528a1e22865fa5e07df44b314d48c1fd826a08149ecdd1d5915048b39'
    reviewer = 'OpenCode CLI v2'
    cli_version = '2.1.4'
    requested_model = 'opencode/deepseek-v4.1-flash-free'
    model_fallback = $false
    input_path = $inputFile
    input_sha256 = $sha
    pid = $pidValue
    create_no_window = $true
    tools_authorized = $false
    started_at = $started.ToString('o')
    ended_at = $ended.ToString('o')
    duration_seconds = [math]::Round(($ended - $started).TotalSeconds, 3)
    timed_out = (-not $finished)
    exit_code = if ($finished) { $proc.ExitCode } else { $null }
    stdout_sha256 = (Get-FileHash -LiteralPath $stdoutFile -Algorithm SHA256).Hash.ToLowerInvariant()
    stdout_bytes = (Get-Item -LiteralPath $stdoutFile).Length
    stderr_sha256 = (Get-FileHash -LiteralPath $stderrFile -Algorithm SHA256).Hash.ToLowerInvariant()
    stderr_bytes = (Get-Item -LiteralPath $stderrFile).Length
    disposition = 'REVIEW_PENDING_PARSE'
}
$receipt | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $receiptFile -Encoding utf8
Get-Content -LiteralPath $receiptFile -Raw
