param(
    [string]$DocxPath = (Join-Path $PSScriptRoot '..\candidate\0088_R07.docx'),
    [string]$PdfPath = (Join-Path $PSScriptRoot '..\evidence\render_R07_final3\0088_R07.pdf'),
    [string]$ReceiptPath = (Join-Path $PSScriptRoot '..\evidence\render_receipt_R07_final3.json'),
    [string]$ExpectedSha = '83ff96699e8c3e01852524047c822f912323207b2c22eb7e6fdb2cc561a5b5dc'
)
$ErrorActionPreference = 'Stop'
$started = (Get-Date).ToString('o')
$word = $null
$doc = $null
$status = 'FAIL'
$errorText = $null
$pageCount = $null
try {
    $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $DocxPath).Hash.ToLowerInvariant()
    if ($actual -ne $ExpectedSha) { throw "Candidate changed before render: $actual" }
    $null = New-Item -ItemType Directory -Path (Split-Path -Parent $PdfPath) -Force
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.AutomationSecurity = 3
    $doc = $word.Documents.Open($DocxPath, $false, $true, $false)
    $pageCount = $doc.ComputeStatistics(2)
    $doc.ExportAsFixedFormat($PdfPath, 17)
    $status = 'PASS'
} catch {
    $errorText = $_.Exception.ToString()
} finally {
    if ($null -ne $doc) { try { $doc.Close(0) } catch {}; [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc) }
    if ($null -ne $word) { try { $word.Quit(0) } catch {}; [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) }
    [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}
$record = [ordered]@{
    project_id = 'TTQS_ONE'
    doc_id = '0088'
    requirement_id = 'I17D-E02'
    revision = 'R07'
    docx_sha256 = $ExpectedSha
    render_engine = 'Microsoft Word COM read-only export; macros disabled'
    started_at = $started
    completed_at = (Get-Date).ToString('o')
    status = $status
    page_count = $pageCount
    pdf_path = $PdfPath
    pdf_sha256 = if (Test-Path -LiteralPath $PdfPath) { (Get-FileHash -Algorithm SHA256 -LiteralPath $PdfPath).Hash.ToLowerInvariant() } else { $null }
    visual_review = 'PENDING'
    formal_acceptance = 'NOT_GRANTED'
    error = $errorText
}
$record | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $ReceiptPath -Encoding utf8
if ($status -ne 'PASS') { exit 1 }
$record | ConvertTo-Json -Compress -Depth 6



