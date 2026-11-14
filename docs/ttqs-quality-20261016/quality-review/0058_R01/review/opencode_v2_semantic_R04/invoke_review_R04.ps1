$ErrorActionPreference = 'Stop'
$reviewDir = (Resolve-Path (Join-Path $PSScriptRoot '.')).Path
$inputsDir = Join-Path $reviewDir 'inputs'
$cli = 'C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe'
$promptPath = Join-Path $reviewDir 'review_prompt_R04.md'
$stdoutPath = Join-Path $reviewDir 'stdout_R04.jsonl'
$stderrPath = Join-Path $reviewDir 'stderr_R04.txt'
$exitPath = Join-Path $reviewDir 'exit_code_R04.txt'
$inputFiles = Get-ChildItem $inputsDir -Recurse -File | Where-Object { $_.Name -ne 'manifest.json' } | Sort-Object FullName
$start = [System.Diagnostics.ProcessStartInfo]::new()
$start.FileName = $cli
$start.WorkingDirectory = $reviewDir
$start.UseShellExecute = $false
$start.CreateNoWindow = $true
$start.RedirectStandardOutput = $true
$start.RedirectStandardError = $true
foreach ($arg in @('run','--model','opencode/beam-free','--format','json','--title','TTQS ONE 0058 R06 Independent Review')) { [void]$start.ArgumentList.Add($arg) }
foreach ($file in $inputFiles) { [void]$start.ArgumentList.Add('--file'); [void]$start.ArgumentList.Add($file.FullName) }
$prompt = Get-Content $promptPath -Raw
[void]$start.ArgumentList.Add($prompt)
$proc = [System.Diagnostics.Process]::new()
$proc.StartInfo = $start
if (-not $proc.Start()) { throw 'OpenCode process did not start' }
$stdoutTask = $proc.StandardOutput.ReadToEndAsync()
$stderrTask = $proc.StandardError.ReadToEndAsync()
$proc.WaitForExit()
$stdout = $stdoutTask.GetAwaiter().GetResult()
$stderr = $stderrTask.GetAwaiter().GetResult()
[IO.File]::WriteAllText($stdoutPath,$stdout,[Text.UTF8Encoding]::new($false))
[IO.File]::WriteAllText($stderrPath,$stderr,[Text.UTF8Encoding]::new($false))
[IO.File]::WriteAllText($exitPath,[string]$proc.ExitCode,[Text.UTF8Encoding]::new($false))
$sha = { param($p) (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash }
$manifest = [ordered]@{
  cli=$cli; cli_version=((& $cli --version 2>&1 | Out-String).Trim()); model='opencode/beam-free'; session_id=$null
  candidate_sha256='B7F8806A204EB6CB9C1F9FA2F84B016B6F1EAFB56FF43E5C7C02E2499CE13B07'
  prompt_sha256=& $sha $promptPath; attached_files=@($inputFiles | ForEach-Object { [ordered]@{path=$_.FullName.Substring($reviewDir.Length+1).Replace('\','/');bytes=$_.Length;sha256=& $sha $_.FullName} })
  stdout_bytes=[Text.Encoding]::UTF8.GetByteCount($stdout); stdout_sha256=& $sha $stdoutPath
  stderr_bytes=[Text.Encoding]::UTF8.GetByteCount($stderr); stderr_sha256=& $sha $stderrPath; exit_code=$proc.ExitCode
  completed_at=(Get-Date).ToString('o'); no_computer_use=$true; candidate_mutation_check='PENDING'
}
if ($stdout -match '"sessionID"\s*:\s*"([^"]+)"') { $manifest.session_id=$Matches[1] }
$invocationPath=Join-Path $reviewDir 'invocation_receipt_R04.json'
$manifest | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $invocationPath -Encoding utf8
[pscustomobject]@{PID=$proc.Id;ExitCode=$proc.ExitCode;Session=$manifest.session_id;StdoutBytes=$manifest.stdout_bytes;StderrBytes=$manifest.stderr_bytes;StdoutSha=$manifest.stdout_sha256;Invocation=$invocationPath} | Format-List
