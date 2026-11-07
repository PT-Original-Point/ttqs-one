$ErrorActionPreference='Stop'
$root='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01'
$docx=Join-Path $root 'candidate\0063_R01.docx'
$outDir=Join-Path $root 'evidence\render_R03'
$pdf=Join-Path $outDir '0063_R01_R03_word.pdf'
$log=Join-Path $outDir 'render_R03_phases.log'
$receiptPath=Join-Path $outDir 'render_R03_receipt.json'
$expectedSha=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
if($expectedSha -ne '4e2d56c9ce46b8acdb2d8b3288ed6083a054c4bb2955edf2127a4f16c058792d'){throw 'Candidate SHA changed; refusing render.'}
if(Test-Path -LiteralPath $pdf){throw 'Refusing to overwrite an existing PDF.'}
function Write-Phase([string]$phase){$line=('{0}|{1}' -f [DateTimeOffset]::Now.ToString('o'),$phase)+[Environment]::NewLine; [IO.File]::AppendAllText($log,$line,[Text.UTF8Encoding]::new($false))}
$priorIds=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$word=$null;$document=$null;$wordPid=$null;$owned=$false;$failure=$null;$started=[DateTimeOffset]::Now
try{
 Write-Phase 'START'
 $word=New-Object -ComObject Word.Application
 $newIds=@()
 for($i=0;$i -lt 20;$i++){ $newIds=@(Get-Process WINWORD -ErrorAction SilentlyContinue | Where-Object {$priorIds -notcontains $_.Id} | ForEach-Object Id); if($newIds.Count -eq 1){break}; if($newIds.Count -gt 1){throw ('More than one new Word process appeared: '+($newIds -join ','))}; Start-Sleep -Seconds 1 }
 if($newIds.Count -ne 1){throw 'Word did not create one isolated automation process.'}
 $wordPid=[int]$newIds[0];$owned=$true
 $word.Visible=$false;$word.DisplayAlerts=0;$word.ScreenUpdating=$false
 Write-Phase ('WORD_READY|PID='+$wordPid)
 $document=$word.Documents.Open($docx,$false,$true,$false)
 Write-Phase 'DOCX_OPENED_READ_ONLY'
 Write-Phase 'EXPORT_START'
 $document.ExportAsFixedFormat($pdf,17)
 Write-Phase 'EXPORT_RETURNED'
 if(-not(Test-Path -LiteralPath $pdf)){throw 'Word returned without producing a PDF.'}
 $pdfInfo=Get-Item -LiteralPath $pdf
 if($pdfInfo.Length -le 0){throw 'Word produced an empty PDF.'}
 $after=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
 $pdfSha=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
 $result=[ordered]@{project_id='TTQS_ONE';doc_id='0063';candidate_revision='R01';render_run='R03';candidate_sha256_before=$expectedSha;candidate_sha256_after=$after;docx_unchanged=($after -eq $expectedSha);renderer='Microsoft Word COM ExportAsFixedFormat';word_pid=$wordPid;started_local=$started.ToString('o');completed_local=[DateTimeOffset]::Now.ToString('o');pdf_path='evidence/render_R03/0063_R01_R03_word.pdf';pdf_bytes=$pdfInfo.Length;pdf_sha256=$pdfSha;status='WORD_RENDER_COMPLETE';visual_inspection='PENDING'}
 [IO.File]::WriteAllText($receiptPath,($result|ConvertTo-Json -Depth 6),[Text.UTF8Encoding]::new($false))
 Write-Phase ('RECEIPT_WRITTEN|PDF_BYTES='+$pdfInfo.Length)
}
catch{$failure=$_.Exception.ToString();Write-Phase ('ERROR|'+$failure.Replace([Environment]::NewLine,' '));[IO.File]::WriteAllText((Join-Path $outDir 'render_R03_error.txt'),$failure,[Text.UTF8Encoding]::new($false));throw}
finally{
 if($document -ne $null){try{$document.Close(0)}catch{}}
 if($word -ne $null -and $owned){try{$word.Quit(0)}catch{}}
 if($document -ne $null){try{[void][Runtime.InteropServices.Marshal]::ReleaseComObject($document)}catch{}}
 if($word -ne $null){try{[void][Runtime.InteropServices.Marshal]::ReleaseComObject($word)}catch{}}
 [GC]::Collect();[GC]::WaitForPendingFinalizers()
 if($owned -and $wordPid){try{Wait-Process -Id $wordPid -Timeout 30 -ErrorAction SilentlyContinue}catch{}}
 Write-Phase 'CLEANUP_COMPLETE'
}