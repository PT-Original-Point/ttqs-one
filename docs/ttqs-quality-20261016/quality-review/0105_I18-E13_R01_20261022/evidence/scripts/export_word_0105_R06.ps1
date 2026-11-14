$ErrorActionPreference='Stop'
$docx='E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022\candidate\0105_I18-E13_績效改善調查與課後行動計畫追蹤套件_R06.docx'
$pdf='E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022\visual\0105_R06\0105_R06_Word_native.pdf'
$receiptPath='E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022\evidence\word_export_receipt_0105_R06.json'
$pdfDir=Split-Path -Parent $pdf
New-Item -ItemType Directory -Path $pdfDir -Force | Out-Null
if(Test-Path -LiteralPath $pdf){throw 'R06 Word PDF already exists; refusing to overwrite.'}
$beforeHash=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
$beforePids=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object {$_.Id})
$started=(Get-Date).ToString('o')
$word=$null; $doc=$null; $wordVersion=$null; $pages=$null; $exportError=$null; $newPids=@()
try {
  $word=New-Object -ComObject Word.Application
  $word.Visible=$false; $word.DisplayAlerts=0
  $wordVersion=$word.Version
  $newPids=@(Get-Process WINWORD -ErrorAction SilentlyContinue | Where-Object {$beforePids -notcontains $_.Id} | ForEach-Object {$_.Id})
  $doc=$word.Documents.Open($docx,$false,$true,$false)
  $pages=$doc.ComputeStatistics(2)
  $doc.ExportAsFixedFormat($pdf,17,$false,0)
  $doc.Close(0); $doc=$null
  $word.Quit(); $word=$null
} catch {
  $exportError=$_.Exception.Message
  throw
} finally {
  if($doc){try{$doc.Close(0)}catch{}}
  if($word){try{$word.Quit()}catch{}}
}
$afterHash=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
if($afterHash -ne $beforeHash){throw "Candidate changed during read-only Word export: before=$beforeHash after=$afterHash"}
$pdfHash=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
$pdfBytes=(Get-Item -LiteralPath $pdf).Length
$record=[ordered]@{receipt_id='TTQS-0105-WORD-EXPORT-R06';doc_id='0105';requirement_id='I18-E13';candidate=$docx;candidate_sha256=$beforeHash;candidate_sha256_after=$afterHash;pdf=$pdf;pdf_sha256=$pdfHash;pdf_bytes=$pdfBytes;page_count_word=$pages;word_version=$wordVersion;word_pid_new=$newPids;mode='Microsoft Word COM; read-only open; ExportAsFixedFormat PDF';started_at=$started;finished_at=(Get-Date).ToString('o');export_error=$exportError;verdict='PASS'}
$record|ConvertTo-Json -Depth 5|Set-Content -LiteralPath $receiptPath -Encoding UTF8
$record|ConvertTo-Json -Depth 5 -Compress
