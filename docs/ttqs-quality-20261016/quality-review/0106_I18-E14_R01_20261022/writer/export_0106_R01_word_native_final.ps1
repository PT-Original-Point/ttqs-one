$ErrorActionPreference='Stop'
$docx='E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0106_I18-E14_R01_20261022\candidate\0106_I18-E14_R01.docx'
$pdf='E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0106_I18-E14_R01_20261022\visual\0106_R01\full_render_204bc47e1d70\0106-I18-E14-R01.pdf'
$log='E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0106_I18-E14_R01_20261022\evidence\word_export_receipt_0106_R01_204bc47e1d70.json'
$word=$null; $doc=$null; $wordPid=$null; $version=$null; $pages=$null; $exportError=$null; $start=(Get-Date).ToString('o')
try {
  $word=New-Object -ComObject Word.Application
  $wordPid=(Get-Process WINWORD | Sort-Object StartTime -Descending | Select-Object -First 1).Id
  $version=$word.Version; $word.Visible=$false; $word.DisplayAlerts=0
  $doc=$word.Documents.Open($docx,$false,$true,$false)
  $pages=$doc.ComputeStatistics(2)
  $doc.ExportAsFixedFormat($pdf,17,$false,0)
  $doc.Close(0); $doc=$null
  $word.Quit(); $word=$null
} catch { $exportError=$_.Exception.Message; throw }
finally {
  if($doc){try{$doc.Close(0)}catch{}}
  if($word){try{$word.Quit()}catch{}}
}
$hash=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
$receipt=[ordered]@{doc_id='0106';requirement_id='I18-E14';candidate=$docx;candidate_sha256=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant();pdf=$pdf;pdf_sha256=$hash;page_count=$pages;word_version=$version;word_pid=$wordPid;mode='Microsoft Word COM; DOCX opened read-only; PDF export';started_at=$start;finished_at=(Get-Date).ToString('o');export_error=$exportError;verdict='PASS'}
$receipt|ConvertTo-Json -Depth 5|Set-Content -LiteralPath $log -Encoding UTF8
$receipt|ConvertTo-Json -Compress