$ErrorActionPreference='Stop'
$base=Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$docx=Join-Path $base 'candidate\0083_R03.docx'
$pdf=Join-Path $base 'evidence\R03_page1_probe.pdf'
$log=Join-Path $base 'evidence\R03_page1_probe.log'
Set-Content -LiteralPath $log -Value (Get-Date -Format o) -Encoding utf8
$word=$null; $doc=$null
try {
  Add-Content $log 'OPEN'
  $word=New-Object -ComObject Word.Application; $word.Visible=$false; $word.DisplayAlerts=0; $word.ScreenUpdating=$false
  $doc=$word.Documents.Open($docx,$false,$true,$false)
  Add-Content $log 'OPENED'
  $doc.ExportAsFixedFormat($pdf,17,$false,0,3,1,1,0,$true,$true,1,$true,$true,$false)
  Add-Content $log 'EXPORTED'
} catch { Add-Content $log ('ERROR '+$_.Exception.ToString()); throw }
finally { if($doc){try{$doc.Close(0)|Out-Null}catch{}}; if($word){try{$word.Quit(0)|Out-Null}catch{}}; [GC]::Collect(); [GC]::WaitForPendingFinalizers() }
