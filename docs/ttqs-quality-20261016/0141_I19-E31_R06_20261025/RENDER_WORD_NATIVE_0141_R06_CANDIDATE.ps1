param()
$ErrorActionPreference = 'Stop'
$docx = 'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0141_I19-E31_SOURCE_PREP_R01_20261025\0141_I19-E31_R06_CANDIDATE.docx'
$pdf = 'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0141_I19-E31_SOURCE_PREP_R01_20261025\0141_I19-E31_R06_WORD_RENDER_CANDIDATE.pdf'
$before = (Get-FileHash -Algorithm SHA256 -LiteralPath $docx).Hash.ToLower()
$word = $null; $doc = $null
try {
  $word = New-Object -ComObject Word.Application
  $word.Visible = $false
  $word.DisplayAlerts = 0
  $word.AutomationSecurity = 3
  $doc = $word.Documents.Open($docx, $false, $true, $false)
  $pages = $doc.ComputeStatistics(2)
  $version = $word.Version
  $doc.ExportAsFixedFormat($pdf,17,$false,0,0,1,1,0,$true,$true,1,$true,$true,$false)
  $doc.Close(0); $doc = $null
  $saveChanges=0; $word.Quit([ref]$saveChanges); $word = $null
  $after = (Get-FileHash -Algorithm SHA256 -LiteralPath $docx).Hash.ToLower()
  if ($before -ne $after) { throw 'DOCX_CHANGED_DURING_READ_ONLY_RENDER' }
  $pdfHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $pdf).Hash.ToLower()
  [pscustomobject]@{ renderer='Microsoft Word COM'; word_version=$version; docx_sha256_before=$before; docx_sha256_after=$after; pdf_path=$pdf; pdf_sha256=$pdfHash; pdf_bytes=(Get-Item -LiteralPath $pdf).Length; word_reported_pages=$pages; visible_window=$false; read_only=$true; result='PASS' } | ConvertTo-Json -Depth 4
} finally {
  if ($doc) { try {$doc.Close(0)} catch {} }
  if ($word) { try {$saveChanges=0; $word.Quit([ref]$saveChanges)} catch {} }
  if ($doc) {[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}
  if ($word) {[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}
  [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}

