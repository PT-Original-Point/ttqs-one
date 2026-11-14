$ErrorActionPreference='Stop'
$docx='E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0086_R01\candidate\0086_R03.docx'
$pdf='E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0086_R01\evidence\render_R03_v3\0086_R03.pdf'
$word=$null;$doc=$null
try{$word=New-Object -ComObject Word.Application;$word.Visible=$false;$word.DisplayAlerts=0;$doc=$word.Documents.Open($docx,$false,$true,$false);$doc.ExportAsFixedFormat($pdf,17);[pscustomobject]@{Result='EXPORTED';Pages=$doc.ComputeStatistics(2)}|ConvertTo-Json -Compress}
finally{if($doc -ne $null){$doc.Close(0);[void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc)};if($word -ne $null){$word.Quit();[void][Runtime.InteropServices.Marshal]::ReleaseComObject($word)};[GC]::Collect();[GC]::WaitForPendingFinalizers()}
