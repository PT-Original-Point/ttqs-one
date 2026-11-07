$ErrorActionPreference='Stop'
$root='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0058_R01'
$docPath=Join-Path $root 'candidate\0058_R08.docx'
$outDir=Join-Path $root 'evidence\render_R08'
New-Item -ItemType Directory -Path $outDir -Force | Out-Null
$pdfPath=Join-Path $outDir '0058_R08.pdf'
if(Test-Path -LiteralPath $pdfPath){throw 'Refusing to overwrite existing R07 PDF.'}
$existing=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
$word=$null; $doc=$null; $owned=$false; $wordPid=0; $started=[DateTime]::UtcNow.ToString('o')
try {
  $word=New-Object -ComObject Word.Application
  $deadline=[DateTime]::UtcNow.AddSeconds(8); $fresh=@()
  do { Start-Sleep -Milliseconds 200; $fresh=@(Get-Process WINWORD -ErrorAction SilentlyContinue | Where-Object {$existing -notcontains $_.Id}) } while($fresh.Count -eq 0 -and [DateTime]::UtcNow -lt $deadline)
  if($fresh.Count -ne 1){[void][Runtime.InteropServices.Marshal]::ReleaseComObject($word);$word=$null;throw "Expected one newly owned Word process, detected $($fresh.Count); did not use or quit any pre-existing instance."}
  $wordPid=$fresh[0].Id; $owned=$true
  $word.Visible=$false; $word.DisplayAlerts=0; $word.AutomationSecurity=3; $word.Options.UpdateLinksAtOpen=$false
  $doc=$word.Documents.Open($docPath,$false,$true,$false)
  $doc.ExportAsFixedFormat($pdfPath,17)
  $doc.Close(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc); $doc=$null
  $word.Quit(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word); $word=$null
  $finished=[DateTime]::UtcNow.ToString('o')
  $receipt=[ordered]@{renderer='Microsoft Word COM';candidate_path=$docPath;candidate_sha256=(Get-FileHash -LiteralPath $docPath -Algorithm SHA256).Hash;pdf_path=$pdfPath;pdf_sha256=(Get-FileHash -LiteralPath $pdfPath -Algorithm SHA256).Hash;pdf_bytes=(Get-Item -LiteralPath $pdfPath).Length;owned_word_pid=$wordPid;attached_to_preexisting_instance=$false;started_utc=$started;finished_utc=$finished;display_alerts_disabled=$true;macros_disabled=$true;read_only_open=$true}
  $json=$receipt|ConvertTo-Json -Depth 5
  [IO.File]::WriteAllText((Join-Path $outDir 'word_export_receipt.json'),$json,(New-Object System.Text.UTF8Encoding -ArgumentList $false))
  $receipt|ConvertTo-Json -Depth 5
} finally {
  if($doc -ne $null){try{$doc.Close(0)}catch{};try{[void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc)}catch{}}
  if($word -ne $null){if($owned){try{$word.Quit(0)}catch{}};try{[void][Runtime.InteropServices.Marshal]::ReleaseComObject($word)}catch{}}
}