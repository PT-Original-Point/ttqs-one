$ErrorActionPreference='Stop'
$qa='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\qa\R08E_REPORT_TABLE_START_20261031'
$docx='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\candidate\0012_I02-E03_R08E.docx'
$pdf=Join-Path $qa '0012_I02-E03_R08E_WORD_RENDER.pdf'; $receipt=Join-Path $qa 'WORD_RENDER_RECEIPT_R08E.json'
$before=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$app=$null;$doc=$null;$status='NOT_STARTED';$errorText=$null;$candidateHash=(Get-FileHash $docx -Algorithm SHA256).Hash.ToLower()
try {
 $app=New-Object -ComObject Word.Application;$app.Visible=$false;$app.DisplayAlerts=0
 $doc=$app.Documents.Open($docx,$false,$true);$doc.ExportAsFixedFormat($pdf,17);$status='EXPORTED'
 $pdfHash=(Get-FileHash $pdf -Algorithm SHA256).Hash.ToLower();$pdfBytes=(Get-Item $pdf).Length
 $pre=[ordered]@{receipt_id='0012-I02-E03-R08E-WORD-RENDER';observed_at_local=(Get-Date).ToString('o');renderer='Microsoft Word COM';candidate_sha256=$candidateHash;pdf_path=$pdf;pdf_sha256=$pdfHash;pdf_bytes=$pdfBytes;export_status=$status;semantic_status='PENDING';visual_status='PENDING';cleanup_status='IN_PROGRESS'}
 $pre|ConvertTo-Json -Depth 5|Set-Content -LiteralPath $receipt -Encoding utf8
} catch {$errorText=$_.Exception.Message;$status='FAILED'}
finally {
 if($doc){try{$doc.Close(0)}catch{};try{[void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($doc)}catch{}}
 if($app){try{$app.Quit(0)}catch{};try{[void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($app)}catch{}}
}
Start-Sleep -Seconds 2
$after=@(Get-Process WINWORD -ErrorAction SilentlyContinue|ForEach-Object Id);$created=@($after|Where-Object{$_ -notin $before});$remaining=@($created|Where-Object{$_ -in $after})
if(Test-Path $receipt){$o=Get-Content $receipt -Raw|ConvertFrom-Json;$o|Add-Member NoteProperty preexisting_winword_pids $before -Force;$o|Add-Member NoteProperty new_winword_pids $created -Force;$o|Add-Member NoteProperty new_winword_pids_alive_after_quit $remaining -Force;$o|Add-Member NoteProperty cleanup_status $(if($remaining.Count -eq 0){'NEW_PROCESSES_CLOSED; PREEXISTING_PIDS_PRESERVED'}else{'NEW_PROCESS_STILL_ALIVE'}) -Force;$o|Add-Member NoteProperty error $errorText -Force;$o|ConvertTo-Json -Depth 6|Set-Content -LiteralPath $receipt -Encoding utf8;$o|ConvertTo-Json -Depth 6}
else { [ordered]@{export_status=$status;error=$errorText;pdf_exists=(Test-Path $pdf);new_winword_pids=$created;remaining=$remaining}|ConvertTo-Json -Depth 4 }
if($status -ne 'EXPORTED' -or -not (Test-Path $pdf)){exit 1}