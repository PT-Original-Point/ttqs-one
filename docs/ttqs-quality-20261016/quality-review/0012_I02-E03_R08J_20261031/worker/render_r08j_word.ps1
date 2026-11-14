$ErrorActionPreference='Stop'
$docx='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\candidate\0012_I02-E03_R08J.docx'
$pdf='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\qa\R08J_SCOPED_LABEL_CLARIFICATION_20261031\render\0012_I02-E03_R08J_WORD.pdf'
$receipt='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0012_I02-E03_LUNA_TEXT_DRAFT_R01_20261029\qa\R08J_SCOPED_LABEL_CLARIFICATION_20261031\render\WORD_RENDER_RECEIPT_R08J.json'
$before=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$docHashBefore=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower()
$app=$null; $doc=$null; $export='NOT_STARTED'; $err=$null
try {
  $app=New-Object -ComObject Word.Application
  $app.Visible=$false
  $app.DisplayAlerts=0
  $doc=$app.Documents.Open($docx,$false,$true)
  $doc.ExportAsFixedFormat($pdf,17)
  $export='EXPORTED'
} catch { $err=$_.Exception.Message; $export='FAILED' }
finally {
  if($doc){ try{$doc.Close(0)}catch{}; [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($doc) }
  if($app){ try{$app.Quit(0)}catch{}; [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($app) }
  [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}
Start-Sleep -Seconds 2
$after=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$created=@($after | Where-Object { $_ -notin $before })
$exists=Test-Path -LiteralPath $pdf
$pdfHash=if($exists){(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()}else{$null}
$docHashAfter=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower()
$result=[ordered]@{observed_at_local=(Get-Date).ToString('o');renderer='Microsoft Word COM';export_status=$export;candidate_sha256_before=$docHashBefore;candidate_sha256_after=$docHashAfter;candidate_unchanged=($docHashBefore -eq $docHashAfter);pdf_path=$pdf;pdf_exists=$exists;pdf_sha256=$pdfHash;preexisting_winword_pids=$before;new_winword_pids=$created;new_pids_alive_after_quit=@($created|Where-Object{$_ -in $after});error=$err}
$result | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $receipt -Encoding utf8
$result | ConvertTo-Json -Depth 5
if($export -ne 'EXPORTED' -or -not $exists -or -not $result.candidate_unchanged){exit 1}

