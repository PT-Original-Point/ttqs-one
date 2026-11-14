$ErrorActionPreference='Stop'
$pkg='E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0104_I18-E11_R15_20261022'
$exe='C:\Users\J\AppData\Roaming\ai.opencode.desktop\cli\2.0.32-x64\opencode-cli.exe'
$packet=Join-Path $pkg 'writer\TASK_PACKET_0104_R16_BOUNDED_REPAIR.md'
$out=Join-Path $pkg 'writer\opencode_writer_R16_stdout.jsonl'
$err=Join-Path $pkg 'writer\opencode_writer_R16_stderr.txt'
$receipt=Join-Path $pkg 'writer\opencode_writer_dispatch_R16.json'
$arglist=@('run','--model','opencode/deepseek-v4.1-flash-free','--agent','plan','--format','json','--title','TTQS 0104 R16 bounded patch writer','--file',$packet,'Return only the exact JSON patch plan required by the attached bounded task packet. Do not call tools and do not edit files.')
$quote={ param($s) '"'+($s -replace '"','\"')+'"' }
$psi=New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName=$exe
$psi.Arguments=(($arglist | ForEach-Object { & $quote $_ }) -join ' ')
$psi.WorkingDirectory=$pkg
$psi.UseShellExecute=$false
$psi.CreateNoWindow=$true
$psi.RedirectStandardOutput=$true
$psi.RedirectStandardError=$true
$proc=New-Object System.Diagnostics.Process
$proc.StartInfo=$psi
$start=Get-Date
$proc.Start() | Out-Null
$pid=$proc.Id
$fsOut=[System.IO.File]::Open($out,[System.IO.FileMode]::Create,[System.IO.FileAccess]::Write,[System.IO.FileShare]::Read)
$fsErr=[System.IO.File]::Open($err,[System.IO.FileMode]::Create,[System.IO.FileAccess]::Write,[System.IO.FileShare]::Read)
$tOut=$proc.StandardOutput.BaseStream.CopyToAsync($fsOut)
$tErr=$proc.StandardError.BaseStream.CopyToAsync($fsErr)
$proc.WaitForExit()
[System.Threading.Tasks.Task]::WaitAll(@($tOut,$tErr))
$fsOut.Dispose();$fsErr.Dispose()
$end=Get-Date
$sha=[System.Security.Cryptography.SHA256]::Create()
$hashOut=([BitConverter]::ToString($sha.ComputeHash([System.IO.File]::ReadAllBytes($out)))).Replace('-','').ToLowerInvariant()
$hashErr=([BitConverter]::ToString($sha.ComputeHash([System.IO.File]::ReadAllBytes($err)))).Replace('-','').ToLowerInvariant()
$packetHash=(Get-FileHash -LiteralPath $packet -Algorithm SHA256).Hash.ToLowerInvariant()
$cliVersion=& $exe --version
$raw=[System.IO.File]::ReadAllText($out,[System.Text.Encoding]::UTF8)
$session='UNKNOWN'
if($raw -match '"sessionID":"([^"]+)"'){$session=$Matches[1]}
$obj=[ordered]@{work_id='TTQS-0104-I18-E11-R16-BOUNDED-REPAIR-20261022';doc_id='0104';requirement_id='I18-E11';candidate_input_sha256='9bbb96da74ba9da845ab0e063421d04f035e79496209a02de1f04b0c98ec7eb8';packet_path=$packet;packet_sha256=$packetHash;requested_model='opencode/deepseek-v4.1-flash-free';actual_serving_model='UNKNOWN';cli_version=$cliVersion;pid=$pid;session_id=$session;started_at_tpe=$start.ToString('o');ended_at_tpe=$end.ToString('o');elapsed_seconds=[math]::Round(($end-$start).TotalSeconds,3);exit_code=$proc.ExitCode;stdout_path=$out;stdout_bytes=(Get-Item $out).Length;stdout_sha256=$hashOut;stderr_path=$err;stderr_bytes=(Get-Item $err).Length;stderr_sha256=$hashErr;permission_auto_approve=$false;result='RAW_OUTPUT_CAPTURED_PENDING_REVIEW'}
$obj | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $receipt -Encoding utf8
"PID=$pid SESSION=$session EXIT=$($proc.ExitCode) SECONDS=$([math]::Round(($end-$start).TotalSeconds,1)) STDOUT=$((Get-Item $out).Length) STDERR=$((Get-Item $err).Length)"
