$ErrorActionPreference = "Stop"
$base = "E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0059_R01"
$docx = Join-Path $base "0059_R03.docx"
$render = Join-Path $base "evidence\render_final_0263017F"
$pdf = Join-Path $render "0059_R03.pdf"
New-Item -ItemType Directory -Force -Path $render | Out-Null
$word = $null
$doc = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.AutomationSecurity = 3
    $doc = $word.Documents.Open($docx, $false, $true, $false)
    $doc.ExportAsFixedFormat($pdf, 17)
    $doc.Close(0)
    $doc = $null
    $version = $word.Version
    $word.Quit(0)
    $word = $null
    $item = Get-Item -LiteralPath $pdf
    $hash = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash
    [pscustomobject]@{Status="EXPORTED";WordVersion=$version;PDF=$pdf;Bytes=$item.Length;SHA256=$hash}
}
finally {
    if ($doc) { try { $doc.Close(0) } catch {} }
    if ($word) { try { $word.Quit(0) } catch {} }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
