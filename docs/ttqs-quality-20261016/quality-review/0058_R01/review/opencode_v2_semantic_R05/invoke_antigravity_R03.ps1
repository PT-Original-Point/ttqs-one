$ErrorActionPreference = 'Stop'
$reviewDir = (Resolve-Path $PSScriptRoot).Path
$root = (Resolve-Path (Join-Path $reviewDir '..\..')).Path
$cli = 'C:\Users\J\AppData\Local\agy\bin\agy.exe'
$settings = 'C:\Users\J\.gemini\antigravity-cli\settings.json'
$candidate = Join-Path $root 'candidate\0058_R08.docx'
$promptPath = Join-Path $reviewDir 'antigravity_review_prompt_R01.md'
$stdoutPath = Join-Path $reviewDir 'antigravity_gemini38_0058_R08_semantic_R03_stdout.json'
$stderrPath = Join-Path $reviewDir 'antigravity_gemini38_0058_R08_semantic_R03_stderr.txt'
$exitPath = Join-Path $reviewDir 'antigravity_gemini38_0058_R08_semantic_R03_exit_code.txt'
$outputPath = Join-Path $reviewDir 'antigravity_gemini38_0058_R08_semantic_R03_response.md'
$qaBefore = (Get-FileHash -LiteralPath $candidate -Algorithm SHA256).Hash
$settingsBefore = (Get-FileHash -LiteralPath $settings -Algorithm SHA256).Hash
$start = [System.Diagnostics.ProcessStartInfo]::new()
$start.FileName = $cli
$start.WorkingDirectory = 'E:\TTQS'
$start.UseShellExecute = $false
$start.CreateNoWindow = $true
$start.RedirectStandardOutput = $true
$start.RedirectStandardError = $true
$packetDir = $reviewDir.Replace('\','/')
$args = @('--model','gemini-3.8-flash-high','--effort','high','--mode','plan','--sandbox','--add-dir',$packetDir,'--output-format','json','--print-timeout','20m')
foreach ($arg in $args) { [void]$start.ArgumentList.Add($arg) }
$prompt = Get-Content -LiteralPath $promptPath -Raw
[void]$start.ArgumentList.Add('--prompt')
[void]$start.ArgumentList.Add($prompt)
$proc = [System.Diagnostics.Process]::new()
$proc.StartInfo = $start
$started = [DateTime]::UtcNow.ToString('o')
if (-not $proc.Start()) { throw 'Antigravity CLI process did not start' }
$stdoutTask = $proc.StandardOutput.ReadToEndAsync()
$stderrTask = $proc.StandardError.ReadToEndAsync()
$finished = $proc.WaitForExit(1220000)
if (-not $finished) { $proc.Kill(); $proc.WaitForExit() }
$stdout = $stdoutTask.GetAwaiter().GetResult()
$stderr = $stderrTask.GetAwaiter().GetResult()
$exitCode = if ($finished) { $proc.ExitCode } else { 124 }
[IO.File]::WriteAllText($stdoutPath,$stdout,[Text.UTF8Encoding]::new($false))
[IO.File]::WriteAllText($stderrPath,$stderr,[Text.UTF8Encoding]::new($false))
[IO.File]::WriteAllText($exitPath,[string]$exitCode,[Text.UTF8Encoding]::new($false))
$sha = { param($p) (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash }
$session = $null
if ($stdout -match '"conversation_id"\s*:\s*"([^"]+)"') { $session = $Matches[1] }
elseif ($stdout -match '"conversationId"\s*:\s*"([^"]+)"') { $session = $Matches[1] }
elseif ($stdout -match '"conversation_id"\s*:\s*\{[^}]*"id"\s*:\s*"([^"]+)"') { $session = $Matches[1] }
$receipt = [ordered]@{
  cli=$cli; model='gemini-3.8-flash-high'; effort='high'; mode='plan'; sandbox=$true; computer_use=$false
  project_path='E:\TTQS'; packet_path=$reviewDir; conversation_id=$session
  candidate_sha256_before=$qaBefore; candidate_sha256_after=& $sha $candidate; candidate_unchanged=($qaBefore -eq (& $sha $candidate))
  settings_sha256_before=$settingsBefore; settings_sha256_after=& $sha $settings; settings_unchanged=($settingsBefore -eq (& $sha $settings))
  read_only_allow_rule_present=((Get-Content -LiteralPath $settings -Raw | ConvertFrom-Json).permissions.allow -contains "read_file($packetDir)")
  prompt_sha256=& $sha $promptPath; stdout_bytes=[Text.Encoding]::UTF8.GetByteCount($stdout); stdout_sha256=& $sha $stdoutPath
  stderr_bytes=[Text.Encoding]::UTF8.GetByteCount($stderr); stderr_sha256=& $sha $stderrPath
  exit_code=$exitCode; process_id=$proc.Id; started_utc=$started; finished_utc=[DateTime]::UtcNow.ToString('o')
}
$receiptPath = Join-Path $reviewDir 'antigravity_gemini38_0058_R08_semantic_R03_route_receipt.json'
$receipt | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $receiptPath -Encoding utf8
if ($stdout.Trim().Length -gt 0) { [IO.File]::WriteAllText($outputPath,$stdout,[Text.UTF8Encoding]::new($false)) }
[pscustomobject]@{PID=$proc.Id;ExitCode=$exitCode;Conversation=$session;Model=$receipt.model;CandidateUnchanged=$receipt.candidate_unchanged;SettingsUnchanged=$receipt.settings_unchanged;StdoutBytes=$receipt.stdout_bytes;StderrBytes=$receipt.stderr_bytes;Receipt=$receiptPath} | Format-List
