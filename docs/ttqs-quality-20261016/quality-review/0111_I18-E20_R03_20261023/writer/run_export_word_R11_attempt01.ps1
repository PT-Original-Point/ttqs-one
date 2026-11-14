$ErrorActionPreference='Stop'
$base='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0111_I18-E20_SOURCE_PREP_20261023'
$script=Join-Path $base 'writer\export_word_0111_R03_R11_attempt01.ps1'
$owner=Join-Path $base 'evidence\word_export_owner_0111_R03_R11_attempt01.json'
$receipt=Join-Path $base 'evidence\word_export_receipt_0111_R03_R11_attempt01.json'
$stdout=Join-Path $base 'writer\export_word_0111_R03_R11_attempt01.stdout.txt'
$stderr=Join-Path $base 'writer\export_word_0111_R03_R11_attempt01.stderr.txt'
$runnerReceipt=Join-Path $base 'evidence\word_export_runner_0111_R03_R11_attempt01.json'
$timeoutReceipt=Join-Path $base 'evidence\word_export_timeout_0111_R03_R11_attempt01.json'
foreach($p in @($stdout,$stderr,$runnerReceipt,$timeoutReceipt)){if(Test-Path -LiteralPath $p){throw "Refuse to overwrite attempt evidence: $p"}}
$baseline=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | ForEach-Object {[int]$_.ProcessId})
$start=Get-Date
$argLine='-NoProfile -STA -ExecutionPolicy Bypass -File "'+$script+'"'
$proc=Start-Process -FilePath (Join-Path $PSHOME 'powershell.exe') -ArgumentList $argLine -WindowStyle Hidden -PassThru -WorkingDirectory $base -RedirectStandardOutput $stdout -RedirectStandardError $stderr
$childPid=$proc.Id
$childStart=(Get-Process -Id $childPid).StartTime.ToString('o')
$deadline=$start.AddSeconds(150)
$lastNotice=0
while((Get-Date) -lt $deadline){
  $proc.Refresh()
  if($proc.HasExited){break}
  $elapsed=[int]((Get-Date)-$start).TotalSeconds
  if($elapsed -ge ($lastNotice+25)){
    $lastNotice=$elapsed
    $wordState='owner-marker-pending'
    if(Test-Path -LiteralPath $owner){try{$o=Get-Content -LiteralPath $owner -Raw|ConvertFrom-Json;$wordState="word-pid=$($o.word_pid)"}catch{$wordState='owner-marker-invalid'}}
    Write-Output "R11_WORD_EXPORT_RUNNING elapsed=${elapsed}s worker_pid=$childPid $wordState"
  }
  Start-Sleep -Seconds 5
}
$proc.Refresh()
$timedOut=(-not $proc.HasExited)
$stoppedWord=$false
$wordDisposition='none'
if($timedOut){
  if(Test-Path -LiteralPath $owner){
    try{
      $o=Get-Content -LiteralPath $owner -Raw|ConvertFrom-Json
      $wpid=[int]$o.word_pid
      $live=Get-CimInstance Win32_Process -Filter "ProcessId=$wpid"
      $created=if($live){([datetime]$live.CreationDate).ToString('o')}else{$null}
      $matches=($live -and $wpid -notin $baseline -and $live.ExecutablePath -eq $o.word_path -and $live.CommandLine -match '/Automation\s+-Embedding' -and $created -eq $o.word_creation_time)
      if($matches){Stop-Process -Id $wpid -Force; $stoppedWord=$true; $wordDisposition="stopped-owned-word-pid-$wpid"}else{$wordDisposition='owner-marker-did-not-match-live-process; left-untouched'}
    }catch{$wordDisposition="owner-check-error:$($_.Exception.Message)"}
  }else{$wordDisposition='no-owner-marker; no WINWORD process terminated'}
  $sameChild=Get-Process -Id $childPid -ErrorAction SilentlyContinue
  if($sameChild -and $sameChild.StartTime.ToString('o') -eq $childStart){Stop-Process -Id $childPid -Force}
  [ordered]@{status='TIMEOUT_150S';worker_pid=$childPid;worker_started_at=$childStart;started_at=$start.ToString('o');finished_at=(Get-Date).ToString('o');baseline_word_pids=$baseline;owned_word_disposition=$wordDisposition;owned_word_stopped=$stoppedWord;receipt_exists=(Test-Path -LiteralPath $receipt);stdout_path=$stdout;stderr_path=$stderr;limit_seconds=150}|ConvertTo-Json -Depth 5|Set-Content -LiteralPath $timeoutReceipt -Encoding UTF8
  Write-Output "R11_WORD_EXPORT_TIMEOUT worker_pid=$childPid owned_word=$wordDisposition"
}else{
  $exitCode=$proc.ExitCode
  $status='WORKER_EXITED_WITHOUT_EXPORT_RECEIPT'
  if(Test-Path -LiteralPath $receipt){try{$rr=Get-Content -LiteralPath $receipt -Raw|ConvertFrom-Json;$status=[string]$rr.status}catch{$status='EXPORT_RECEIPT_INVALID'}}
  [ordered]@{status=$status;worker_pid=$childPid;worker_started_at=$childStart;worker_exit_code=$exitCode;started_at=$start.ToString('o');finished_at=(Get-Date).ToString('o');baseline_word_pids=$baseline;receipt_exists=(Test-Path -LiteralPath $receipt);stdout_path=$stdout;stderr_path=$stderr;limit_seconds=150}|ConvertTo-Json -Depth 5|Set-Content -LiteralPath $runnerReceipt -Encoding UTF8
  Write-Output "R11_WORD_EXPORT_RESULT status=$status exit=$exitCode worker_pid=$childPid receipt=$((Test-Path -LiteralPath $receipt))"
  if($exitCode -ne 0){exit [int]$exitCode}
}
