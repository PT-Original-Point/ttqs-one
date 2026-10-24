param()
$ErrorActionPreference = 'Stop'
$base = 'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01'
$exe = 'C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe'
$packet = Join-Path $base 'inputs\0063_WRITER_PACKET_R01.md'
$work = Join-Path $base 'worker\opencode_R01'
$out = Join-Path $work 'stdout_R01.jsonl'
$err = Join-Path $work 'stderr_R01.txt'
$request = 'Follow the attached TTQS ONE 0063 Writer Packet exactly. Return the complete UNIQUE_BLUEPRINT and HUMAN_FACING_MANUSCRIPT sections, with the final two section headings specified in the packet. Do not summarize.'
[System.IO.File]::WriteAllText((Join-Path $work 'request_R01.txt'), $request, [System.Text.UTF8Encoding]::new($false))
$packetHash = (Get-FileHash -LiteralPath $packet -Algorithm SHA256).Hash.ToLowerInvariant()
$version = (& $exe --version | Out-String).Trim()
$started = [DateTimeOffset]::Now
$psi = [System.Diagnostics.ProcessStartInfo]::new()
$psi.FileName = $exe
$psi.UseShellExecute = $false
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$psi.StandardOutputEncoding = [System.Text.UTF8Encoding]::new($false)
$psi.StandardErrorEncoding = [System.Text.UTF8Encoding]::new($false)
foreach($arg in @('run','--model','opencode/deepseek-v4.1-flash-free','--file',$packet,'--title','0063 Writer R01','--format','json',$request)){ [void]$psi.ArgumentList.Add($arg) }
$p = [System.Diagnostics.Process]::new()
$p.StartInfo = $psi
if(-not $p.Start()){ throw 'OpenCode process did not start' }
$taskOut = $p.StandardOutput.ReadToEndAsync()
$taskErr = $p.StandardError.ReadToEndAsync()
$finished = $p.WaitForExit(900000)
if(-not $finished){ try{$p.Kill($true)}catch{}; $p.WaitForExit() }
$stdoutText = $taskOut.GetAwaiter().GetResult()
$stderrText = $taskErr.GetAwaiter().GetResult()
[System.IO.File]::WriteAllText($out, $stdoutText, [System.Text.UTF8Encoding]::new($false))
[System.IO.File]::WriteAllText($err, $stderrText, [System.Text.UTF8Encoding]::new($false))
$completed = [DateTimeOffset]::Now
$receipt = [ordered]@{
 project_id='TTQS_ONE'; doc_id='0063'; requirement_id='I14-E04'; official_checkbox_sequence='068'
 route='OpenCode v2 CLI'; cli_version=$version; model_requested='opencode/deepseek-v4.1-flash-free'; runtime_model_identity='NOT_ATTESTED'
 packet_path=$packet; packet_sha256=$packetHash; invocation_args=@('run','--model','opencode/deepseek-v4.1-flash-free','--file',$packet,'--title','0063 Writer R01','--format','json','<request saved in request_R01.txt>')
 started_local=$started.ToString('o'); completed_local=$completed.ToString('o'); elapsed_seconds=[math]::Round(($completed-$started).TotalSeconds,3)
 timed_out=(-not $finished); process_exit_code=$p.ExitCode; stdout_path=$out; stdout_sha256=(Get-FileHash -LiteralPath $out -Algorithm SHA256).Hash.ToLowerInvariant()
 stderr_path=$err; stderr_sha256=(Get-FileHash -LiteralPath $err -Algorithm SHA256).Hash.ToLowerInvariant()
 stdout_chars=$stdoutText.Length; stderr_chars=$stderrText.Length; provider_usage='UNKNOWN_UNTIL_PARSED'
}
$receiptPath=Join-Path $work 'invocation_receipt_R01.json'
[System.IO.File]::WriteAllText($receiptPath, ($receipt | ConvertTo-Json -Depth 8), [System.Text.UTF8Encoding]::new($false))
Get-Content -LiteralPath $receiptPath -Raw
