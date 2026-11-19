$ErrorActionPreference = 'Stop'
$reviewDir = (Resolve-Path $PSScriptRoot).Path
$root = (Resolve-Path (Join-Path $reviewDir '..\..')).Path
$cli = 'C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe'
$session = 'ses_eb4c69a00ffecdiCvGl5LzE5aU'
$candidate = Join-Path $root 'candidate\0058_R08.docx'
$promptPath = Join-Path $reviewDir 'review_prompt_R05.md'
$stdoutPath = Join-Path $reviewDir 'opencode_longcat_R01_stdout.jsonl'
$stderrPath = Join-Path $reviewDir 'opencode_longcat_R01_stderr.txt'
$exitPath = Join-Path $reviewDir 'opencode_longcat_R01_exit_code.txt'
$qaBefore = (Get-FileHash -LiteralPath $candidate -Algorithm SHA256).Hash
$relativeFiles = @(
  'inputs\candidate\0058_R08.docx',
  'inputs\candidate\0058_R06_source.docx',
  'inputs\blueprint\0058_UNIQUE_BLUEPRINT_R06.md',
  'inputs\content\0058_CONTENT_R08.json',
  'inputs\register\0058_SYNTHETIC_REPLACEMENT_REGISTER_R08.csv',
  'inputs\official\official_checkbox_page4_excerpt.txt',
  'inputs\official\official_evidence_table_fulltext.txt',
  'inputs\official\official_evidence_table_source.pdf',
  'inputs\contracts\01_HUMAN_MISSION_AND_ACCEPTANCE.md',
  'inputs\contracts\03_157_CHECKBOX_BLUEPRINTS.md',
  'inputs\previous_review\independent_review_R04.md',
  'evidence\patch_0058_layout_R08.json',
  'evidence\technical_qa_0058_R08.json',
  'evidence\visual_review_0058_R08.md',
  'inputs\render\0058_R08.pdf',
  'inputs\render\render_manifest_R08.json'
)
$inputFiles = @($relativeFiles | ForEach-Object { (Resolve-Path (Join-Path $reviewDir $_)).Path })
$start = [System.Diagnostics.ProcessStartInfo]::new()
$start.FileName = $cli
$start.WorkingDirectory = $reviewDir
$start.UseShellExecute = $false
$start.CreateNoWindow = $true
$start.RedirectStandardOutput = $true
$start.RedirectStandardError = $true
foreach ($arg in @('run','--model','opencode/longcat-2.5-preview-free','--format','json','--session',$session)) { [void]$start.ArgumentList.Add($arg) }
foreach ($file in $inputFiles) { [void]$start.ArgumentList.Add('--file'); [void]$start.ArgumentList.Add($file) }
$prompt = Get-Content -LiteralPath $promptPath -Raw
[void]$start.ArgumentList.Add($prompt)
$proc = [System.Diagnostics.Process]::new()
$proc.StartInfo = $start
$started = [DateTime]::UtcNow.ToString('o')
if (-not $proc.Start()) { throw 'OpenCode process did not start' }
$stdoutTask = $proc.StandardOutput.ReadToEndAsync()
$stderrTask = $proc.StandardError.ReadToEndAsync()
$completed = $proc.WaitForExit(1200000)
if (-not $completed) { $proc.Kill(); $proc.WaitForExit() }
$stdout = $stdoutTask.GetAwaiter().GetResult()
$stderr = $stderrTask.GetAwaiter().GetResult()
$exitCode = if ($completed) { $proc.ExitCode } else { 124 }
[IO.File]::WriteAllText($stdoutPath,$stdout,[Text.UTF8Encoding]::new($false))
[IO.File]::WriteAllText($stderrPath,$stderr,[Text.UTF8Encoding]::new($false))
[IO.File]::WriteAllText($exitPath,[string]$exitCode,[Text.UTF8Encoding]::new($false))
$sha = { param($p) (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash }
$receipt = [ordered]@{
  cli=$cli; cli_version=((& $cli --version 2>&1 | Out-String).Trim()); model='opencode/longcat-2.5-preview-free'; session_id=$session
  candidate_sha256_before=$qaBefore; candidate_sha256_after=& $sha $candidate; candidate_unchanged=($qaBefore -eq (& $sha $candidate))
  prompt_sha256=& $sha $promptPath
  attached_files=@($inputFiles | ForEach-Object { [ordered]@{path=$_.Substring($reviewDir.Length+1).Replace('\','/');bytes=(Get-Item $_).Length;sha256=& $sha $_} })
  stdout_bytes=[Text.Encoding]::UTF8.GetByteCount($stdout); stdout_sha256=& $sha $stdoutPath
  stderr_bytes=[Text.Encoding]::UTF8.GetByteCount($stderr); stderr_sha256=& $sha $stderrPath
  exit_code=$exitCode; process_id=$proc.Id; started_utc=$started; finished_utc=[DateTime]::UtcNow.ToString('o')
  no_computer_use=$true; session_reused=$true; timeout_seconds=1200
}
$receiptPath = Join-Path $reviewDir 'opencode_longcat_R01_invocation_receipt.json'
$receipt | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $receiptPath -Encoding utf8
[pscustomobject]@{PID=$proc.Id;ExitCode=$exitCode;Session=$session;CandidateUnchanged=$receipt.candidate_unchanged;StdoutBytes=$receipt.stdout_bytes;StderrBytes=$receipt.stderr_bytes;StdoutSha=$receipt.stdout_sha256;Receipt=$receiptPath} | Format-List
