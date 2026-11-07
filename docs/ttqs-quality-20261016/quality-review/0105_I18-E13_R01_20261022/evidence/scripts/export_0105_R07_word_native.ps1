$ErrorActionPreference = 'Stop'
$base = 'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022'
$candidateDir = Join-Path $base 'candidate'
$candidateFiles = @(Get-ChildItem -LiteralPath $candidateDir -File | Where-Object { $_.Name -like '*R07.docx' })
if ($candidateFiles.Count -ne 1) { throw "expected one R07 candidate; found $($candidateFiles.Count)" }
$docx = $candidateFiles[0].FullName
$pdf = Join-Path $base 'visual\0105_R07\word_native\0105_I18-E13_R07.pdf'
$log = Join-Path $base 'evidence\word_export_receipt_0105_R07.json'
if (-not (Test-Path -LiteralPath $docx)) { throw 'candidate DOCX missing' }
if (Test-Path -LiteralPath $pdf) { throw 'refusing to overwrite existing PDF' }
New-Item -ItemType Directory -Path (Split-Path -Parent $pdf) -Force | Out-Null
$before = @(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$word = $null; $doc = $null; $ownedPid = $null; $version = $null; $pages = $null; $failure = $null
$started = (Get-Date).ToString('o')
try {
  $word = New-Object -ComObject Word.Application
  $version = $word.Version
  $afterStart = @(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
  $newIds = @($afterStart | Where-Object { $_ -notin $before })
  if ($newIds.Count -ne 1) { throw "Word ownership is ambiguous; preexisting=$($before -join ','); new=$($newIds -join ',')" }
  $ownedPid = [int]$newIds[0]
  $word.Visible = $false
  $word.DisplayAlerts = 0
  $doc = $word.Documents.Open($docx, $false, $true, $false)
  $pages = $doc.ComputeStatistics(2)
  $doc.ExportAsFixedFormat($pdf, 17)
  $doc.Close(0); $doc = $null
  $word.Quit(); $word = $null
} catch {
  $failure = $_.Exception.Message
  throw
} finally {
  if ($doc) { try { $doc.Close(0) } catch {} }
  if ($word) { try { $word.Quit() } catch {} }
  if ($doc) { try { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc) } catch {} }
  if ($word) { try { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) } catch {} }
}
$exited = $null
if ($ownedPid) {
  try { $p = Get-Process -Id $ownedPid -ErrorAction Stop; $exited = $p.WaitForExit(10000) } catch { $exited = $true }
}
$after = @(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$preserved = @($before | Where-Object { $_ -in $after })
if (-not (Test-Path -LiteralPath $pdf)) { throw 'Word did not create PDF' }
$pdfHash = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
$docxHash = (Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
$r = [ordered]@{ doc_id='0105'; official_requirement_id='I18-E13'; candidate=$docx; candidate_sha256=$docxHash; pdf=$pdf; pdf_sha256=$pdfHash; page_count=$pages; word_version=$version; created_word_pid=$ownedPid; created_process_exited=$exited; preexisting_word_pids=$before; preexisting_word_pids_still_alive=$preserved; mode='Microsoft Word COM; R07 opened read-only; PDF export'; started_at=$started; finished_at=(Get-Date).ToString('o'); export_error=$failure; verdict=if($failure){'FAIL'}else{'PASS'} }
$r | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $log -Encoding UTF8
$r | ConvertTo-Json -Compress
