$ErrorActionPreference='Stop'
$folder='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\EXTERNAL_WORK\TTQS_ONE_0036_I07-E04_VISUAL_REPAIR_R03_20261118'
$html=Join-Path $folder 'CANDIDATE_HTML_0036_R03.html'
$docx=Join-Path $folder 'CANDIDATE_0036_I07-E04_R03.docx'
$pdf=Join-Path $folder 'CANDIDATE_0036_I07-E04_R03.pdf'
$before=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$word=$null; $doc=$null; $pidWord=$null; $result='FAILED'
try {
  $word=New-Object -ComObject Word.Application
  $word.Visible=$false
  $word.DisplayAlerts=0
  $after=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
  $new=@($after | Where-Object { $before -notcontains $_ })
  if($new.Count -eq 1){$pidWord=[int]$new[0]}
  $doc=$word.Documents.Open($html,$false,$true,$false)
  $doc.SaveAs2($docx,16)
  $doc.ExportAsFixedFormat($pdf,17)
  $result='DOCX_AND_PDF_EXPORTED'
} finally {
  if($doc){try{$doc.Close(0)}catch{}}
  if($word){try{$word.Quit()}catch{}}
  if($doc){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}
  if($word){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}
  [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}
$presentAfter=$false
if($pidWord){try{Wait-Process -Id $pidWord -Timeout 10 -ErrorAction Stop;$presentAfter=$true}catch{$presentAfter=$false}}
$docxHash=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash
$pdfHash=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash
$receipt=[ordered]@{schema='TTQS_ONE_0036_WORD_COM_BUILD_R03';doc_id='0036';requirement_id='I07-E04';html_sha256=(Get-FileHash -LiteralPath $html -Algorithm SHA256).Hash;docx_path=$docx;docx_sha256=$docxHash;docx_bytes=(Get-Item -LiteralPath $docx).Length;pdf_path=$pdf;pdf_sha256=$pdfHash;pdf_bytes=(Get-Item -LiteralPath $pdf).Length;word_pid=$pidWord;word_pid_was_new=($pidWord -and ($before -notcontains $pidWord));word_pid_present_after_quit=$presentAfter;result=$result}
$receipt | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $folder 'WORD_COM_BUILD_RECEIPT_R03.json') -Encoding utf8
$receipt | ConvertTo-Json -Compress
