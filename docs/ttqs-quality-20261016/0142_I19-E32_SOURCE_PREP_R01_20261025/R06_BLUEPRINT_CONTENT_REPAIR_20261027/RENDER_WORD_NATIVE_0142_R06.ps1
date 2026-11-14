$ErrorActionPreference = 'Stop'
function HashFile([string]$path) {
  $sha=[System.Security.Cryptography.SHA256]::Create()
  try { return ([BitConverter]::ToString($sha.ComputeHash([IO.File]::ReadAllBytes($path)))).Replace('-','').ToLowerInvariant() }
  finally { $sha.Dispose() }
}
$docPath='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025\R06_BLUEPRINT_CONTENT_REPAIR_20261027\0142_I19-E32_R06_BLUEPRINT_REPAIR_CANDIDATE.docx'
$pdfPath='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025\R06_BLUEPRINT_CONTENT_REPAIR_20261027\0142_I19-E32_R06_WordNative.pdf'
$receiptPath='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025\R06_BLUEPRINT_CONTENT_REPAIR_20261027\WORD_NATIVE_RENDER_RECEIPT_0142_R06.json'
$ownerPath='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0142_I19-E32_SOURCE_PREP_R01_20261025\R06_BLUEPRINT_CONTENT_REPAIR_20261027\0142_WORD_OWNER_R06.json'
[IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($pdfPath))|Out-Null
$beforeHash=HashFile $docPath
$beforeIds=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$app=$null;$doc=$null;$owned=$false;$appPid=$null;$result='NOT_STARTED';$message=$null
$started=(Get-Date).ToString('o')
try {
  $app=New-Object -ComObject Word.Application
  $app.Visible=$false;$app.DisplayAlerts=0;$app.AutomationSecurity=3
  Start-Sleep -Seconds 2
  $afterProcs=@(Get-Process WINWORD -ErrorAction SilentlyContinue)
  $newProcs=@($afterProcs | Where-Object {$beforeIds -notcontains $_.Id})
  if($newProcs.Count -ne 1) {
    $result='SKIPPED_WORD_OWNERSHIP_NOT_UNAMBIGUOUS'
    $message="COM created $($newProcs.Count) new WINWORD processes; document was not opened; existing Word processes untouched."
  } else {
    $appPid=[int]$newProcs[0].Id;$owned=$true
    $owner=[ordered]@{worker_pid=$PID;winword_pid=$appPid;created=(Get-Date).ToString('o');candidate_sha256=$beforeHash}
    [IO.File]::WriteAllText($ownerPath,($owner|ConvertTo-Json -Depth 3),[Text.UTF8Encoding]::new($false))
    $missing=[System.Type]::Missing
    $openArgs=[object[]]@($docPath,[object]$false,[object]$true,[object]$false,$missing,$missing,[object]$false,$missing,$missing,$missing,$missing,[object]$false,[object]$false,$missing,[object]$false,$missing)
    $documents=$app.Documents
    $doc=$documents.GetType().InvokeMember('Open',[System.Reflection.BindingFlags]::InvokeMethod,$null,$documents,$openArgs)
    $pages=$doc.ComputeStatistics(2)
    $version=$app.Version
    $doc.ExportAsFixedFormat($pdfPath,17,$false,0,0,1,1,0,$false,$true,0,$true,$true,$false)
    $doc.Close(0);$doc=$null
    $result='PDF_EXPORTED_BY_OWNED_WORD_INSTANCE'
  }
} catch {
  $result='ERROR';$message=$_.Exception.ToString()
} finally {
  if($doc){try{$doc.Close(0)}catch{}}
  if($app -and $owned){try{$app.Quit(0)}catch{}}
  if($app){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)}
  [GC]::Collect();[GC]::WaitForPendingFinalizers()
}
$afterHash=HashFile $docPath
$pdfExists=Test-Path -LiteralPath $pdfPath
$pdfSha=if($pdfExists){HashFile $pdfPath}else{$null}
$pdfBytes=if($pdfExists){(Get-Item -LiteralPath $pdfPath).Length}else{0}
$pdfPages=$null
if($pdfExists){
  $py='C:\Users\J\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
  $pdfPages=& $py -c 'import sys; from pypdf import PdfReader; print(len(PdfReader(sys.argv[1]).pages))' $pdfPath
  if($LASTEXITCODE -ne 0){$pdfPages='UNKNOWN'}
}
$r=[ordered]@{schema='ttqs-one-0142-word-native-render-r06-v1';doc_id='0142';requirement_id='I19-E32';renderer='Microsoft Word COM ExportAsFixedFormat';started_local=$started;finished_local=(Get-Date).ToString('o');result=$result;message=$message;candidate_path=$docPath;candidate_sha256_before=$beforeHash;candidate_sha256_after=$afterHash;candidate_unchanged=($beforeHash -eq $afterHash);winword_pid=$appPid;winword_pid_was_new=$owned;before_winword_count=$beforeIds.Count;pdf_path=$(if($pdfExists){$pdfPath}else{$null});pdf_sha256=$pdfSha;pdf_bytes=$pdfBytes;pdf_pages=$pdfPages;visible_window=$false;read_only=$true;scope='Existing candidate opened read-only; only the single new Word PID was used; all pre-existing Word processes untouched.'}
[IO.File]::WriteAllText($receiptPath,($r|ConvertTo-Json -Depth 5),[Text.UTF8Encoding]::new($false))
$r|ConvertTo-Json -Depth 5
