$ErrorActionPreference='Stop'
$docx='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01\candidate\0063_R01.docx'
$outDir='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0063_R01\evidence\render_R02'
$pdf=Join-Path $outDir '0063_R02_word.pdf'
$expectedSha=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
$priorIds=@(Get-Process WINWORD -ErrorAction SilentlyContinue | ForEach-Object Id)
if(Test-Path -LiteralPath $pdf){throw 'Refusing to overwrite existing Word-rendered PDF'}
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$word=$null; $document=$null; $wordPid=$null; $owned=$false
try {
    $word=New-Object -ComObject Word.Application
    $newIds=@()
    for($attempt=0;$attempt -lt 20;$attempt++){
        $newIds=@(Get-Process WINWORD -ErrorAction SilentlyContinue | Where-Object {$priorIds -notcontains $_.Id} | ForEach-Object Id)
        if($newIds.Count -eq 1){break}
        if($newIds.Count -gt 1){throw "More than one new Word process appeared; refusing to select an owner: $($newIds -join ',')"}
        Start-Sleep -Seconds 1
    }
    if($newIds.Count -ne 1){throw 'Word did not create a new isolated automation process; no document opened'}
    $wordPid=[int]$newIds[0]
    $owned=$true
    $word.Visible=$false
    $word.DisplayAlerts=0
    $document=$word.Documents.Open($docx,$false,$true,$false)
    $document.ExportAsFixedFormat($pdf,17)
    $document.Close(0); $document=$null
    if(-not (Test-Path -LiteralPath $pdf)){throw 'Word returned without producing PDF'}
    $pdfInfo=Get-Item -LiteralPath $pdf
    $pdfSha=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
    "WORD_PID=$wordPid"
    "PDF=$pdf"
    "PDF_BYTES=$($pdfInfo.Length)"
    "PDF_SHA256=$pdfSha"
    "DOCX_SHA_BEFORE=$expectedSha"
    "DOCX_SHA_AFTER=$((Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant())"
}
finally {
    if($document -ne $null){try{$document.Close(0)}catch{}}
    if($word -ne $null -and $owned){try{$word.Quit(0)}catch{}}
    if($document -ne $null){try{[void][Runtime.InteropServices.Marshal]::ReleaseComObject($document)}catch{}}
    if($word -ne $null){try{[void][Runtime.InteropServices.Marshal]::ReleaseComObject($word)}catch{}}
    [GC]::Collect(); [GC]::WaitForPendingFinalizers()
    if($owned -and $wordPid){try{Wait-Process -Id $wordPid -Timeout 30 -ErrorAction SilentlyContinue}catch{}}
}
