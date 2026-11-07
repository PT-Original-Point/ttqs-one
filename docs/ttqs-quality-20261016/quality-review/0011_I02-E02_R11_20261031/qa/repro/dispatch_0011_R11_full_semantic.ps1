$ErrorActionPreference='Stop'
$base='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0011_I02-E02_LUNA_TEXT_DRAFT_R01_20261029'
$dir=Join-Path $base 'qa\W1_SEMANTIC_REVIEW_R11_FULL_20261031'
$docx=Join-Path $base 'candidate\0011_I02-E02_R11.docx'
$input=Join-Path $dir 'REVIEW_INPUT_R11_FULL.md'
$binding=Join-Path $dir 'REVIEW_INPUT_BINDING_R11.json'
$exe='C:\Users\J\AppData\Roaming\npm\node_modules\@opencode\cli\bin\opencode.exe'
$work='TTQS-0011-W1-SEMANTIC-R11-FULL-20261031-01'
$receipt=Join-Path $dir 'DISPATCH_TERMINAL_R11.json'
$stdout=Join-Path $dir 'RAW_STDOUT_R11.jsonl'
$stderr=Join-Path $dir 'RAW_STDERR_R11.txt'
function Get-Sha($p){(Get-FileHash -Algorithm SHA256 -LiteralPath $p).Hash.ToLowerInvariant()}
if(!(Test-Path $docx) -or !(Test-Path $input) -or !(Test-Path $binding)){throw 'INPUT_MISSING'}
if((Get-Sha $docx) -ne 'cce86967e17b6ff2a5af5bec7e37e0d6f850b069ad3845a8d04ebb1065b37f3d'){throw 'CANDIDATE_SHA_CHANGED'}
if((Get-Sha $input) -ne 'f143be37de95398f9f4d1dd6573c3135cb93e8c10857dd1db4dab8ebe37017e1'){throw 'REVIEW_INPUT_SHA_CHANGED'}
$existing=Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'opencode.exe' -and $_.CommandLine -match '\brun\b' -and $_.CommandLine -match 'TTQS-0011-I02-E02-R11-FULL-SEMANTIC' }
if($existing){throw 'DUPLICATE_WORK_ID_PROCESS_EXISTS'}
$started=Get-Date
$args='run --model opencode/glm-5.3-flash-free --format json --title TTQS-0011-I02-E02-R11-FULL-SEMANTIC --file "'+$input+'" "Review the complete attached packet independently. Return the requested JSON verdict only. Do not use tools or edit files."'
$psi=New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName=$exe;$psi.Arguments=$args;$psi.WorkingDirectory=$dir;$psi.UseShellExecute=$false;$psi.CreateNoWindow=$true;$psi.WindowStyle=[System.Diagnostics.ProcessWindowStyle]::Hidden;$psi.RedirectStandardOutput=$true;$psi.RedirectStandardError=$true
$p=[System.Diagnostics.Process]::Start($psi)
$initial=[ordered]@{schema='ttqs-one-cli-worker-dispatch-v1';work_id=$work;worker='W1 OpenCode v2 CLI';doc_id='0011';requirement_id='I02-E02';stage='READY_INDEPENDENT_SEMANTIC';status='RUNNING';started_at_local=$started.ToString('o');pid=$p.Id;process_created_hidden=$true;process_window='HIDDEN_CREATE_NO_WINDOW';requested_model='opencode/glm-5.3-flash-free';actual_model='UNKNOWN';model_identity_status='UNKNOWN_UNLESS_SESSION_METADATA_PROVES';candidate_sha256_before=(Get-Sha $docx);candidate_sha256_after=$null;candidate_unchanged=$null;review_input_path=$input;review_input_sha256=(Get-Sha $input);review_binding_sha256=(Get-Sha $binding);review_scope='Full R11 candidate body and tables in document order against official I02-E02 source, current unique Blueprint row, crosswalk, and negative neighbors; semantic/usability only; no file writes.';stdout_path=$stdout;stderr_path=$stderr;stdout_sha256=$null;stderr_sha256=$null;exit_code=$null;timed_out=$false;reviewer_verdict='NOT_ADJUDICATED';formal_acceptance='NOT_GRANTED'}
$tmp=$receipt+'.tmp';$initial|ConvertTo-Json -Depth 8|Set-Content -LiteralPath $tmp -Encoding UTF8;Move-Item -LiteralPath $tmp -Destination $receipt -Force
$taskOut=$p.StandardOutput.ReadToEndAsync();$taskErr=$p.StandardError.ReadToEndAsync()
$completed=$p.WaitForExit(600000)
if(!$completed){$initial.status='TIMEOUT_UNRESOLVED_PROCESS';$initial.timed_out=$true;$initial.timeout_limit_seconds=600;$initial.pid=$p.Id;$initial.candidate_sha256_after=(Get-Sha $docx);$initial.candidate_unchanged=($initial.candidate_sha256_before -eq $initial.candidate_sha256_after);$tmp=$receipt+'.tmp';$initial|ConvertTo-Json -Depth 8|Set-Content -LiteralPath $tmp -Encoding UTF8;Move-Item -LiteralPath $tmp -Destination $receipt -Force;Write-Output ($initial|ConvertTo-Json -Depth 6 -Compress);exit 124}
$outText=$taskOut.Result;$errText=$taskErr.Result
[IO.File]::WriteAllText($stdout,$outText,[Text.UTF8Encoding]::new($false));[IO.File]::WriteAllText($stderr,$errText,[Text.UTF8Encoding]::new($false))
$initial.finished_at_local=(Get-Date).ToString('o');$initial.duration_seconds=[math]::Round(((Get-Date)-$started).TotalSeconds,3);$initial.exit_code=$p.ExitCode;$initial.candidate_sha256_after=(Get-Sha $docx);$initial.candidate_unchanged=($initial.candidate_sha256_before -eq $initial.candidate_sha256_after);$initial.stdout_bytes=[Text.Encoding]::UTF8.GetByteCount($outText);$initial.stderr_bytes=[Text.Encoding]::UTF8.GetByteCount($errText);$initial.stdout_sha256=(Get-Sha $stdout);$initial.stderr_sha256=(Get-Sha $stderr);$initial.status=if($p.ExitCode -eq 0 -and $outText.Trim()){'COMPLETED_RAW_RESPONSE'}elseif($p.ExitCode -eq 0){'COMPLETED_EMPTY'}else{'FAILED_EXIT'}
try{$events=@($outText -split "`r?`n"|Where-Object{$_.Trim()}|ForEach-Object{try{$_|ConvertFrom-Json}catch{$null}}|Where-Object{$_});$initial.session_ids=@($events|ForEach-Object{if($_.sessionID){$_.sessionID}elseif($_.session_id){$_.session_id}}|Where-Object{$_}|Select-Object -Unique);$initial.usage_metadata=@($events|ForEach-Object{if($_.part.tokens){$_.part.tokens}elseif($_.tokens){$_.tokens}}|Where-Object{$_})}catch{$initial.session_parse_status='UNKNOWN'}
$tmp=$receipt+'.tmp';$initial|ConvertTo-Json -Depth 8|Set-Content -LiteralPath $tmp -Encoding UTF8;Move-Item -LiteralPath $tmp -Destination $receipt -Force
Write-Output ($initial|ConvertTo-Json -Depth 6 -Compress)
if($p.ExitCode -ne 0){exit $p.ExitCode}

