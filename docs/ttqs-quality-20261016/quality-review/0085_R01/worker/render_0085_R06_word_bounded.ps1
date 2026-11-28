$ErrorActionPreference = 'Stop'
$root = 'E:\TTQS\_github_sync_0064\docs\ttqs-quality-20261016\quality-review\0085_R01'
$docx = Join-Path $root 'candidate\0085_R06.docx'
$pdf = Join-Path $root 'evidence\render_R06\0085_R06_word_render.pdf'
$log = Join-Path $root 'evidence\render_R06\word_render_events.jsonl'
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $pdf) | Out-Null
function Event([string]$name) {
    [ordered]@{ at_local=(Get-Date).ToString('o'); event=$name } |
        ConvertTo-Json -Compress | Add-Content -LiteralPath $log -Encoding utf8
}
$word = $null
$doc = $null
try {
    Event 'START'
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    Event 'WORD_CREATED'
    $doc = $word.Documents.Open($docx, $false, $true, $false)
    Event 'DOCX_OPENED_READ_ONLY'
    $doc.ExportAsFixedFormat($pdf, 17)
    Event 'PDF_EXPORT_RETURNED'
    $doc.Close(0)
    $doc = $null
    $word.Quit(0)
    $word = $null
    Event 'WORD_CLOSED'
    [pscustomobject]@{status='RENDERED';pdf=$pdf;bytes=(Get-Item -LiteralPath $pdf).Length} | ConvertTo-Json -Compress
}
finally {
    if ($doc -ne $null) { try { $doc.Close(0) } catch {} }
    if ($word -ne $null) { try { $word.Quit(0) } catch {} }
    if ($doc -ne $null) { [void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc) }
    if ($word -ne $null) { [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word) }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
