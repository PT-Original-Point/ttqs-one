$ErrorActionPreference = 'Stop'
$base = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$docx = Join-Path $base 'candidate\0083_R03.docx'
$pdf = Join-Path $base 'evidence\0083_R03_word_render.pdf'
$receipt = Join-Path $base 'evidence\word_render_receipt_R03.json'
$before = @(Get-Process WINWORD -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)
$word = $null
$doc = $null
$fieldsUpdated = $false
$tocCount = 0
$errorText = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.ScreenUpdating = $false
    $word.Options.UpdateLinksAtOpen = $false
    $doc = $word.Documents.Open($docx, $false, $true, $false)
    $fieldsUpdated = ([int]$doc.Fields.Update()) -ge 0
    $tocCount = [int]$doc.TablesOfContents.Count
    for ($i=1; $i -le $tocCount; $i++) { $doc.TablesOfContents.Item($i).Update() | Out-Null }
    $doc.ExportAsFixedFormat($pdf, 17, $false, 0, 0, 1, 1, 0, $true, $true, 1, $true, $true, $false)
} catch {
    $errorText = $_.Exception.ToString()
} finally {
    if ($doc -ne $null) { try { $doc.Close(0) | Out-Null } catch {} }
    if ($word -ne $null) { try { $word.Quit(0) | Out-Null } catch {} }
    if ($doc -ne $null) { try { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc) } catch {} }
    if ($word -ne $null) { try { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) } catch {} }
    [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}
$after = @(Get-Process WINWORD -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)
$newPids = @($after | Where-Object { $_ -notin $before })
$stillNew = @($newPids | Where-Object { $_ -in $after })
$receiptObject = [ordered]@{
    schema = 'ttqs-0083-word-render-v1'
    renderer = 'Microsoft Word COM headless PDF export plus bundled Poppler rasterization'
    visible = $false
    docx_sha256 = (Get-FileHash -Algorithm SHA256 $docx).Hash.ToLower()
    body_sha256 = (Get-FileHash -Algorithm SHA256 (Join-Path $base 'candidate\0083_R03_body.md')).Hash.ToLower()
    fields_updated_in_memory = $fieldsUpdated
    table_of_contents_count = $tocCount
    pdf_path = $pdf
    pdf_exists = (Test-Path $pdf)
    pdf_sha256 = if (Test-Path $pdf) { (Get-FileHash -Algorithm SHA256 $pdf).Hash.ToLower() } else { $null }
    pdf_bytes = if (Test-Path $pdf) { (Get-Item $pdf).Length } else { 0 }
    preexisting_word_pids = $before
    new_word_pids = $newPids
    newly_started_word_processes_remaining = $stillNew
    error = $errorText
    result = if ($errorText -eq $null -and (Test-Path $pdf) -and $stillNew.Count -eq 0) { 'PASS_WORD_PDF_EXPORTED_AND_OWN_PROCESS_CLOSED' } else { 'FAIL' }
}
$receiptObject | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 $receipt
$receiptObject | ConvertTo-Json -Depth 8
if ($receiptObject.result -eq 'FAIL') { exit 1 }
