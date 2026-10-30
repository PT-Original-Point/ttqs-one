param([string]$DocxPath,[string]$PdfPath,[string]$ReceiptPath,[string]$ProgressPath,[string]$ExpectedSha)
$ErrorActionPreference='Stop'
Import-Module Microsoft.PowerShell.Utility -ErrorAction Stop
Import-Module Microsoft.PowerShell.Management -ErrorAction Stop
function Sha([string]$p){$a=[Security.Cryptography.SHA256]::Create();$f=[IO.File]::OpenRead($p);try{return ([BitConverter]::ToString($a.ComputeHash($f))).Replace('-','').ToLowerInvariant()}finally{$f.Dispose();$a.Dispose()}}
function Mark([string]$phase,[string]$detail=$null){[IO.File]::WriteAllText($ProgressPath,([ordered]@{phase=$phase;at=(Get-Date).ToString('o');runner_pid=$PID;owned_word_pid=$ownedWordPid;detail=$detail}|ConvertTo-Json -Depth 4),[Text.UTF8Encoding]::new($false))}
$resolved=(Resolve-Path -LiteralPath $DocxPath).Path
$beforeHash=Sha $resolved
if($beforeHash -ne $ExpectedSha){throw "Candidate SHA mismatch: $beforeHash"}
$before=@(Get-Process WINWORD -ErrorAction SilentlyContinue|ForEach-Object {[int]$_.Id})
$app=$null;$doc=$null;$ownedWordPid=$null;$pdfSha=$null;$pages=$null;$err=$null;$status='NOT_STARTED';$started=(Get-Date).ToString('o')
try {
 Mark 'STARTING_WORD_COM'
 $app=New-Object -ComObject Word.Application
 $appPid=$null
 for($i=0;$i -lt 25 -and -not $appPid;$i++){$now=@(Get-Process WINWORD -ErrorAction SilentlyContinue|ForEach-Object {[int]$_.Id});$delta=@($now|Where-Object {$_ -notin $before});if($delta.Count -eq 1){$appPid=[int]$delta[0]}elseif($delta.Count -gt 1){throw "Multiple new Word processes appeared; refused to guess ownership: $($delta -join ',')"}else{Start-Sleep -Milliseconds 400}}
 if(-not $appPid){throw 'No uniquely new Word PID identified; refused to change visibility or quit a pre-existing instance'}
 $ownedWordPid=[int]$appPid
 Mark 'OWNED_NEW_WORD_PID' "PID=$ownedWordPid"
 $app.Visible=$false;$app.DisplayAlerts=0;$app.ScreenUpdating=$false
 $doc=$app.Documents.Open($resolved,$false,$true,$false)
 Mark 'DOCUMENT_OPENED_READ_ONLY'
 $doc.Repaginate();$pages=$doc.ComputeStatistics(2)
 $doc.ExportAsFixedFormat($PdfPath,17,$false,0,0,1,1,0,$true,$false,0,$true,$true,$false)
 if(!(Test-Path -LiteralPath $PdfPath) -or (Get-Item -LiteralPath $PdfPath).Length -lt 1000){throw 'Word PDF export missing or undersized'}
 $pdfSha=Sha $PdfPath;$status='EXPORTED'
 Mark 'PDF_EXPORTED' "pages=$pages;pdf_sha256=$pdfSha"
} catch { $err=$_.Exception.ToString();$status='FAILED';Mark 'FAILED' $err }
finally {
 try{if($doc){$doc.Close(0)}}catch{if(!$err){$err=$_.Exception.ToString()}}
 try{if($doc){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}}catch{}
 if($app -and $ownedWordPid -and $ownedWordPid -notin $before){try{$saveChanges=0;$originalFormat=0;$routeDocument=0;$app.Quit([ref]$saveChanges,[ref]$originalFormat,[ref]$routeDocument)}catch{if(!$err){$err=$_.Exception.ToString()}}}
 try{if($app){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)}}catch{}
 $doc=$null;$app=$null;[GC]::Collect();[GC]::WaitForPendingFinalizers()
}
$afterHash=Sha $resolved
$after=@(Get-Process WINWORD -ErrorAction SilentlyContinue|ForEach-Object {[int]$_.Id})
$alive=@($ownedWordPid|Where-Object {$_ -and $_ -in $after})
$result=[ordered]@{project_id='TTQS_ONE';doc_id='0007';requirement_id='I01-E04';candidate_path=$resolved;candidate_sha256_before=$beforeHash;candidate_sha256_after=$afterHash;candidate_unchanged=($beforeHash -eq $afterHash);renderer='Microsoft Word COM hidden, read-only; export fixed format PDF';owned_word_pid=$ownedWordPid;preexisting_word_pids=$before;owned_word_pid_alive_after_quit=$alive;page_count_word=$pages;pdf_path=$PdfPath;pdf_sha256=$pdfSha;pdf_bytes=$(if(Test-Path $PdfPath){(Get-Item $PdfPath).Length}else{$null});export_status=$status;error=$err;started_at=$started;finished_at=(Get-Date).ToString('o')}
[IO.File]::WriteAllText($ReceiptPath,($result|ConvertTo-Json -Depth 6),[Text.UTF8Encoding]::new($false));Mark 'COMPLETE' $status
if($status -ne 'EXPORTED' -or $beforeHash -ne $afterHash){exit 1}
