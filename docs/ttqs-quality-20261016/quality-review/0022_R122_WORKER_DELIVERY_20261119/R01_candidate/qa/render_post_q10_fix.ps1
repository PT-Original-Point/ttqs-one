$ErrorActionPreference = 'Stop'
$docx = 'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORKTREES\R122_DELIVERY_20261118B\docs\ttqs-quality-20261016\quality-review\0022_R122_WORKER_DELIVERY_20261119\R01_candidate\0022_I04-E01_R01.docx'
$pdf = 'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORKTREES\R122_DELIVERY_20261118B\docs\ttqs-quality-20261016\quality-review\0022_R122_WORKER_DELIVERY_20261119\R01_candidate\0022_I04-E01_R01_POST_Q10_FIX.pdf'
$word = $null; $doc = $null
try {
  $word = New-Object -ComObject Word.Application
  $word.Visible = $false
  $word.DisplayAlerts = 0
  $doc = $word.Documents.Open($docx, $false, $true)
  $doc.ExportAsFixedFormat($pdf, 17)
  $doc.Close($false); $doc = $null
  $word.Quit(); $word = $null
  $f = Get-Item -LiteralPath $pdf
  $h = Get-FileHash -Algorithm SHA256 -LiteralPath $pdf
  [pscustomobject]@{result='PASS';pdf=$pdf;bytes=$f.Length;sha256=$h.Hash;word_visible=$false} | ConvertTo-Json -Compress
} finally {
  if ($doc -ne $null) { try { $doc.Close($false) } catch {} }
  if ($word -ne $null) { try { $word.Quit() } catch {} }
}
