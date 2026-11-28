param([Parameter(Mandatory=$true)][string]$DocxPath,[Parameter(Mandatory=$true)][string]$PdfPath,[Parameter(Mandatory=$true)][string]$ReceiptPath)
$ErrorActionPreference='Stop'
$before=@(Get-CimInstance Win32_Process | Where-Object Name -eq 'WINWORD.EXE' | Select-Object -ExpandProperty ProcessId)
$word=$null;$doc=$null;$result=[ordered]@{route='Microsoft Word COM native export';input_docx=(Resolve-Path -LiteralPath $DocxPath).Path;input_docx_sha256=(Get-FileHash -LiteralPath $DocxPath -Algorithm SHA256).Hash.ToLowerInvariant();pdf_path=$PdfPath;opened=$false;page_count=$null;paragraph_count=$null;table_count=$null;exported=$false;pdf_sha256=$null;pdf_bytes=$null;new_word_process_ids=@();error=$null}
try{
  $word=New-Object -ComObject Word.Application
  $word.Visible=$false;$word.DisplayAlerts=0
  $doc=$word.Documents.Open($result.input_docx,$false,$true,$false)
  $doc.Repaginate();$result.opened=$true;$result.page_count=$doc.ComputeStatistics(2);$result.paragraph_count=$doc.Paragraphs.Count;$result.table_count=$doc.Tables.Count
  $doc.ExportAsFixedFormat($PdfPath,17,$false,0,0,1,$result.page_count,0,$true,$false,0,$true,$true,$false)
  if(!(Test-Path -LiteralPath $PdfPath) -or (Get-Item -LiteralPath $PdfPath).Length -lt 1000){throw 'Word did not produce a non-empty PDF.'}
  $result.exported=$true;$result.pdf_sha256=(Get-FileHash -LiteralPath $PdfPath -Algorithm SHA256).Hash.ToLowerInvariant();$result.pdf_bytes=(Get-Item -LiteralPath $PdfPath).Length
}catch{$result.error=$_.Exception.Message}
finally{
  if($doc -ne $null){try{$doc.Close(0)}catch{}}
  if($word -ne $null){try{$word.Quit(0)}catch{}}
  if($doc -ne $null){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}
  if($word -ne $null){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}
  [GC]::Collect();[GC]::WaitForPendingFinalizers()
}
$after=@(Get-CimInstance Win32_Process | Where-Object Name -eq 'WINWORD.EXE' | Select-Object -ExpandProperty ProcessId)
$result.new_word_process_ids=@($after|Where-Object{$before -notcontains $_})
$json=$result|ConvertTo-Json -Depth 5
Set-Content -LiteralPath $ReceiptPath -Value $json -Encoding UTF8
Write-Output $json
if(!$result.exported){exit 1}