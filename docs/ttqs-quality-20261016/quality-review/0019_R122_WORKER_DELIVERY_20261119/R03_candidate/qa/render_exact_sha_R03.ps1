param([string]$DocPath,[string]$ExpectedSha,[string]$OutputDir,[string]$PopplerExe)
$ErrorActionPreference='Stop'
$started=(Get-Date).ToString('o')
$before=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object {$_.Id})
$actual=(Get-FileHash -LiteralPath $DocPath -Algorithm SHA256).Hash
if($actual -ne $ExpectedSha){throw "Candidate SHA changed before render: $actual"}
New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
$pdf=Join-Path $OutputDir "0019_R03_${ExpectedSha}.pdf"
$app=$null;$doc=$null;$owned=$false;$wordPid=0;$pages=0
try {
  $app=New-Object -ComObject Word.Application
  $app.Visible=$false
  $app.DisplayAlerts=0
  $newPids=@()
  for($i=0;$i -lt 20;$i++){
    $now=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object {$_.Id})
    $newPids=@($now | Where-Object {$_ -notin $before})
    if($newPids.Count -gt 0){break}
    Start-Sleep -Milliseconds 500
  }
  if($newPids.Count -ne 1){throw "Expected exactly one newly spawned Word PID, observed $($newPids.Count); aborted before opening candidate"}
  $wordPid=[int]$newPids[0]
  $owned=$true
  $doc=$app.Documents.Open($DocPath,$false,$true,$false)
  $pages=$doc.ComputeStatistics(2)
  $doc.ExportAsFixedFormat($pdf,17)
  $doc.Close($false);$doc=$null
} finally {
  if($doc){try{$doc.Close($false)}catch{}}
  if($owned -and $app){try{$app.Quit()}catch{}}
  if($doc){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}
  if($app){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)}
  [GC]::Collect();[GC]::WaitForPendingFinalizers()
}
$after=(Get-FileHash -LiteralPath $DocPath -Algorithm SHA256).Hash
if($after -ne $ExpectedSha){throw "Candidate SHA changed during read-only render: $after"}
if(-not(Test-Path -LiteralPath $pdf)){throw 'Word produced no PDF'}
$prefix=Join-Path $OutputDir 'page'
$ppm=Start-Process -FilePath $PopplerExe -ArgumentList @('-png','-r','100',"`"$pdf`"","`"$prefix`"") -WindowStyle Hidden -PassThru -Wait
if($ppm.ExitCode -ne 0){throw "pdftoppm exit $($ppm.ExitCode)"}
$pngs=@(Get-ChildItem -LiteralPath $OutputDir -File -Filter 'page-*.png' | Sort-Object Name)
$receipt=[ordered]@{schema='TTQS_ONE_EXACT_SHA_RENDER_0019_R03_V1';candidate_docx_sha256=$ExpectedSha;candidate_sha_before=$actual;candidate_sha_after=$after;candidate_path=$DocPath;word_pid=$wordPid;word_pid_owned=$owned;word_pages=$pages;pdf_path=$pdf;pdf_sha256=(Get-FileHash $pdf -Algorithm SHA256).Hash;pdf_bytes=(Get-Item $pdf).Length;render_png_pages=$pngs.Count;pngs=@(foreach($f in $pngs){[ordered]@{file=$f.Name;sha256=(Get-FileHash $f.FullName -Algorithm SHA256).Hash;bytes=$f.Length}});pdftoppm_exit_code=$ppm.ExitCode;started_at=$started;finished_at=(Get-Date).ToString('o');render_input_binding='EXACT_DOCX_SHA_CHECKED_BEFORE_AND_AFTER_WORD_READONLY_EXPORT'}
$rp=Join-Path $OutputDir 'RENDER_RECEIPT.json'
[IO.File]::WriteAllText($rp,($receipt|ConvertTo-Json -Depth 6),[Text.UTF8Encoding]::new($false))
$receipt | ConvertTo-Json -Depth 3