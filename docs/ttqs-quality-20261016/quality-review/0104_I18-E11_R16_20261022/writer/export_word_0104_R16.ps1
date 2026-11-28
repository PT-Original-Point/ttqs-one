$ErrorActionPreference = 'Stop'
$base = 'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0104_I18-E11_SOURCE_PREP_20261022'
$docx = Join-Path $base 'candidate\0104__證照獲取率_分析報告_R16.docx'
$pdf = Join-Path $base 'visual\0104_R16\0104_R16_word_native.pdf'
$receiptPath = Join-Path $base 'evidence\word_export_receipt_0104_R16.json'
$expectedDocxSha = '9a074b207e7a57f1448cf96868f3cc3f30a72834a021f9b04392909ea3183d7b'
New-Item -ItemType Directory -Path (Split-Path -Parent $pdf) -Force | Out-Null
$before = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
$word = $null
$doc = $null
$newPid = $null
$errorText = $null
$started = (Get-Date).ToString('o')
try {
    if ((Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower() -ne $expectedDocxSha) { throw 'DOCX SHA changed before native Word export' }
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $newPid = $null
    for ($i = 0; $i -lt 40 -and -not $newPid; $i++) {
        Start-Sleep -Milliseconds 250
        $now = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
        $delta = @($now | Where-Object { $_ -notin $before })
        if ($delta.Count -eq 1) { $newPid = [int]$delta[0] }
        elseif ($delta.Count -gt 1) { throw "Ambiguous new Word processes: $($delta -join ',')" }
    }
    if (-not $newPid) { throw 'No unique new WINWORD process; refused to open or close an ambiguous instance' }
    $doc = $word.Documents.Open($docx, $false, $true, $false)
    $doc.ExportAsFixedFormat($pdf, 17)
    $doc.Close(0)
    [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)
    $doc = $null
    $word.Quit(0)
    [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)
    $word = $null
    for ($i = 0; $i -lt 80; $i++) {
        if (-not (Get-Process -Id $newPid -ErrorAction SilentlyContinue)) { break }
        Start-Sleep -Milliseconds 250
    }
    $after = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
    $pdfSha = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()
    $docxSha = (Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower()
    $unexpected = @($after | Where-Object { $_ -notin $before })
    $exited = -not [bool](Get-Process -Id $newPid -ErrorAction SilentlyContinue)
    $unchanged = (@($after | Where-Object { $_ -in $before }).Count -eq $before.Count)
    $result = [pscustomobject]@{
        status = if ($docxSha -eq $expectedDocxSha -and $exited -and $unchanged -and $unexpected.Count -eq 0) { 'PASS' } else { 'FAIL' }
        docx_path = $docx; pdf_path = $pdf; docx_sha256 = $docxSha; pdf_sha256 = $pdfSha
        new_word_pid = $newPid; new_word_pid_exited = $exited; preexisting_word_pids_unchanged = $unchanged
        preexisting_count = $before.Count; unexpected_new_word_pids = $unexpected
        pid_binding_method = 'unique new WINWORD.EXE process difference; no dependence on COM Hwnd'
        started_at = $started; verified_at = (Get-Date).ToString('o'); error = $null
    }
} catch {
    $errorText = $_.Exception.Message
    $result = [pscustomobject]@{
        status = 'FAIL'; docx_path = $docx; pdf_path = $pdf; new_word_pid = $newPid
        preexisting_pids = $before; started_at = $started; verified_at = (Get-Date).ToString('o'); error = $errorText
    }
    if ($newPid -and $word) {
        try { if ($doc) { $doc.Close(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc) } } catch {}
        try { $word.Quit(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) } catch {}
    }
}
$result | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $receiptPath -Encoding utf8
$result | ConvertTo-Json -Depth 5
if ($result.status -ne 'PASS') { exit 1 }

