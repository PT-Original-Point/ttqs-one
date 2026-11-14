$ErrorActionPreference='Stop'
$docx='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0062_R01\candidate\0062_R04.docx'
$pdf='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0062_R01\evidence\render_R04_range\0062_R04_saveas.pdf'
$log='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0062_R01\evidence\render_R04_saveas_trace.log'
Set-Content -LiteralPath $log -Value "START $(Get-Date -Format o)" -Encoding utf8
$word=$null;$doc=$null
try {
 $word=New-Object -ComObject Word.Application;$word.Visible=$false;$word.DisplayAlerts=0
 Add-Content -LiteralPath $log -Value "WORD_CREATED $(Get-Date -Format o)"
 $doc=$word.Documents.Open($docx,$false,$true,$false)
 Add-Content -LiteralPath $log -Value "DOC_OPENED PAGES=$($doc.ComputeStatistics(2)) SAVEAS_BEGIN $(Get-Date -Format o)"
 $doc.SaveAs2($pdf,17,$false)
 Add-Content -LiteralPath $log -Value "SAVEAS_DONE $(Get-Date -Format o) bytes=$((Get-Item -LiteralPath $pdf).Length)"
 $doc.Close(0);$doc=$null;$word.Quit();$word=$null
 Add-Content -LiteralPath $log -Value "CLOSED $(Get-Date -Format o)"
} catch {Add-Content -LiteralPath $log -Value "ERROR=$($_.Exception.ToString()) $(Get-Date -Format o)";throw}
finally {if($doc -ne $null){try{$doc.Close(0)}catch{}};if($word -ne $null){try{$word.Quit()}catch{}}}