param([string]$DocxPath,[string]$PdfPath,[string]$ReceiptPath,[string]$ExpectedSha)
$ErrorActionPreference='Stop'
$started=(Get-Date).ToString('o')
$word=$null; $doc=$null; $status='FAIL'; $errorText=$null
try {
  $actual=(Get-FileHash -Algorithm SHA256 -LiteralPath $DocxPath).Hash.ToLower()
  if($actual -ne $ExpectedSha){ throw "candidate SHA changed: $actual" }
  $word=New-Object -ComObject Word.Application
  $word.Visible=$false
  $word.DisplayAlerts=0
  $word.AutomationSecurity=3
  $doc=$word.Documents.Open($DocxPath,$false,$true,$false)
  $doc.ExportAsFixedFormat($PdfPath,17)
  $status='PASS'
} catch { $errorText=$_.Exception.ToString() }
finally {
  if($null -ne $doc){ try{$doc.Close(0)}catch{}; [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc) }
  if($null -ne $word){ try{$word.Quit(0)}catch{}; [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) }
  [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}
$record=[ordered]@{document_id='0069';revision='R02';candidate_sha256=$ExpectedSha;renderer='Microsoft Word COM read-only export; macros disabled';started_at=$started;completed_at=(Get-Date).ToString('o');status=$status;pdf_path=$PdfPath;pdf_exists=(Test-Path -LiteralPath $PdfPath);error=$errorText}
$record | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $ReceiptPath -Encoding utf8
if($status -ne 'PASS'){exit 1}
