$ErrorActionPreference='Stop'
function Get-FileSha256 {
  param([Parameter(Mandatory=$true)][string]$Path)
  $stream=[System.IO.File]::OpenRead($Path)
  $sha=[System.Security.Cryptography.SHA256]::Create()
  try { return ([BitConverter]::ToString($sha.ComputeHash($stream))).Replace('-','').ToLowerInvariant() }
  finally { $sha.Dispose(); $stream.Dispose() }
}
$base='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0111_I18-E20_SOURCE_PREP_20261023'
$docx=Join-Path $base 'candidate\0111_I18-E20_特殊績效及社會面成果證據登錄表_R03.docx'
$visual=Join-Path $base 'visual\0111_R03'
$pdf=Join-Path $visual '0111_R03_word_native.pdf'
$evidence=Join-Path $base 'evidence'
$ownerPath=Join-Path $evidence 'word_export_owner_0111_R03_R11_attempt04.json'
$receiptPath=Join-Path $evidence 'word_export_receipt_0111_R03_R11_attempt04.json'
$expectedDocxSha='f427ed898a79393a91d6d8fadcde960a8126e90697325aa94c1b764b8b537a50'
$started=(Get-Date).ToString('o')
$step='preflight'
$before=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | ForEach-Object {[int]$_.ProcessId})
$word=$null; $doc=$null; $newPid=$null; $pidCreation=$null; $owned=$false
try {
  if((Get-FileSha256 -Path $docx) -ne $expectedDocxSha){throw 'Candidate SHA changed before Word export'}
  if(Test-Path -LiteralPath $pdf){throw 'Refuse to overwrite an existing R03 PDF'}
  if((Test-Path -LiteralPath $ownerPath) -or (Test-Path -LiteralPath $receiptPath)){throw 'Attempt03 evidence exists; refuse overwrite'}
  New-Item -ItemType Directory -Path $visual -Force | Out-Null
  $step='word_com_activation'
  $word=New-Object -ComObject Word.Application
  $step='capture_new_word_pid'
  for($i=0;$i -lt 40 -and -not $newPid;$i++){
    Start-Sleep -Milliseconds 250
    $now=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | ForEach-Object {[int]$_.ProcessId})
    $delta=@($now | Where-Object {$_ -notin $before})
    if($delta.Count -eq 1){$newPid=[int]$delta[0]}
    elseif($delta.Count -gt 1){throw "Ambiguous new WINWORD PIDs: $($delta -join ',')"}
  }
  if(-not $newPid){throw 'Word COM activation created no unique new WINWORD process'}
  $step='verify_word_process_identity'
  $procInfo=Get-CimInstance Win32_Process -Filter "ProcessId=$newPid"
  if(-not $procInfo -or -not $procInfo.ExecutablePath.EndsWith('WINWORD.EXE',[StringComparison]::OrdinalIgnoreCase) -or $procInfo.CommandLine -notmatch '/Automation\s+-Embedding'){throw 'New process did not match WINWORD /Automation -Embedding identity; do not quit an unverified instance'}
  $owned=$true
  $pidCreation=([datetime]$procInfo.CreationDate).ToString('o')
  $step='write_owner_marker'
  [ordered]@{doc_id='0111';requirement='I18-E20';revision='R03';candidate_sha256=$expectedDocxSha;word_pid=$newPid;word_creation_time=$pidCreation;word_path=$procInfo.ExecutablePath;word_command_line=$procInfo.CommandLine;exporter_pid=$PID;started_at=$started;ownership_method='new PID absent from baseline plus exact executable, automation command and creation time'} | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $ownerPath -Encoding UTF8
  $step='configure_hidden_readonly_word'
  $word.Visible=$false
  $word.DisplayAlerts=0
  $word.AutomationSecurity=3
  $documentCountBefore=[int]$word.Documents.Count
  if($documentCountBefore -ne 0){throw "Fresh Word instance already has $documentCountBefore open documents"}
  $step='open_candidate_readonly'
  $doc=$word.Documents.Open($docx,$false,$true,$false)
  $step='update_fields'
  $null=$doc.Fields.Update()
  $step='word_export_pdf'
  $doc.ExportAsFixedFormat($pdf,17,$false,0,0,1,999,0,$true,$false,0,$true,$false,$false)
  $step='close_document_and_word'
  $doc.Close(0)
  [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc);$doc=$null
  $version=[string]$word.Version
  $word.Quit(0)
  [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word);$word=$null
  for($i=0;$i -lt 80 -and (Get-Process -Id $newPid -ErrorAction SilentlyContinue);$i++){Start-Sleep -Milliseconds 250}
  if(-not(Test-Path -LiteralPath $pdf) -or (Get-Item -LiteralPath $pdf).Length -le 0){throw 'Word returned without a nonempty PDF'}
  $docxShaAfter=(Get-FileSha256 -Path $docx)
  $pdfSha=(Get-FileSha256 -Path $pdf)
  $alive=[bool](Get-Process -Id $newPid -ErrorAction SilentlyContinue)
  $after=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | ForEach-Object {[int]$_.ProcessId})
  $preexistingUnchanged=(@($before | Where-Object {$_ -in $after}).Count -eq $before.Count)
  $unexpected=@($after | Where-Object {$_ -notin $before})
  $status=if($docxShaAfter -eq $expectedDocxSha -and -not $alive -and $preexistingUnchanged -and $unexpected.Count -eq 0){'PDF_EXPORTED_PENDING_PAGE_RENDER_AND_VISUAL_INSPECTION'}else{'EXPORT_RESULT_NEEDS_INVESTIGATION'}
  [ordered]@{doc_id='0111';official_requirement_id='I18-E20';revision='R03';status=$status;docx_path=$docx;docx_sha256=$docxShaAfter;pdf_path=$pdf;pdf_sha256=$pdfSha;pdf_bytes=(Get-Item -LiteralPath $pdf).Length;word_version=$version;word_pid=$newPid;word_creation_time=$pidCreation;word_exited=(-not $alive);preexisting_word_pids_unchanged=$preexistingUnchanged;unexpected_new_word_pids=$unexpected;read_only=$true;fresh_instance_document_count_before_open=$documentCountBefore;export_method='Microsoft Word COM ExportAsFixedFormat; 14-argument flags already verified on 0102 R08c';started_at=$started;verified_at=(Get-Date).ToString('o')} | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
}catch{
  $err=$_
  $msg=[string]$err.Exception.Message
  $line=$err.InvocationInfo.ScriptLineNumber
  $position=[string]$err.InvocationInfo.PositionMessage
  $docxShaOnFail=$null
  if(Test-Path -LiteralPath $docx){$docxShaOnFail=(Get-FileSha256 -Path $docx)}
  $quitAttempted=$false
  if($doc){try{$doc.Close(0)}catch{}}
  if($owned -and $word){$quitAttempted=$true;try{$word.Quit(0)}catch{}}
  if($doc){try{[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}catch{}}
  if($word){try{[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}catch{}}
  [ordered]@{doc_id='0111';official_requirement_id='I18-E20';revision='R03';status='EXPORT_FAILED';failed_step=$step;docx_sha256=$docxShaOnFail;pdf_path=$pdf;word_pid=$newPid;word_creation_time=$pidCreation;error=$msg;error_id=[string]$err.FullyQualifiedErrorId;script_line=$line;position=$position;word_quit_attempted=$quitAttempted;started_at=$started;verified_at=(Get-Date).ToString('o')} | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
  exit 1
}