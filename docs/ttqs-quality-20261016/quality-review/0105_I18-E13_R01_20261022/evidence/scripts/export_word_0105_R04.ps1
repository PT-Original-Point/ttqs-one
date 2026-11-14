$ErrorActionPreference = 'Stop'
$base = 'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022'
$docx = Join-Path $base 'candidate\0105_I18-E13_績效改善調查與課後行動計畫追蹤套件_R04.docx'
$pdf = Join-Path $base 'visual\0105_R04\0105_R04_word_native.pdf'
$receiptPath = Join-Path $base 'evidence\word_export_receipt_0105_R04.json'
$expectedDocxSha = '17f7d680cbb992db93a6f67df84415500050953eecf426b477f675810177b4cb'
New-Item -ItemType Directory -Path (Split-Path -Parent $pdf) -Force | Out-Null
$before = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
$word = $null; $doc = $null; $newPid = $null; $started=(Get-Date).ToString('o')
$phasePath=Join-Path $base 'evidence\word_export_phase_R04.txt'
Set-Content -LiteralPath $phasePath -Value ('START '+(Get-Date).ToString('o')) -Encoding UTF8
function Add-Phase([string]$v){Add-Content -LiteralPath $phasePath -Value ((Get-Date).ToString('o')+' '+$v) -Encoding UTF8}
try {
    $docxShaBefore=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower()
    if ($docxShaBefore -ne $expectedDocxSha) { throw 'DOCX SHA changed before native Word export' }; Add-Phase 'DOCX_HASH_VERIFIED'
    $word = New-Object -ComObject Word.Application
    Add-Phase 'COM_CREATED'; $word.Visible = $false; $word.DisplayAlerts = 0
    for ($i=0; $i -lt 40 -and -not $newPid; $i++) {
        Start-Sleep -Milliseconds 250
        $now=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
        $delta=@($now | Where-Object { $_ -notin $before })
        if ($delta.Count -eq 1) { $newPid=[int]$delta[0] }
        elseif ($delta.Count -gt 1) { throw "Ambiguous new Word processes: $($delta -join ',')" }
    }
    if (-not $newPid) { throw 'No unique new WINWORD process; refused to open or close an ambiguous instance' }; Add-Phase ('NEW_WORD_PID '+$newPid)
    $doc=$word.Documents.Open($docx,$false,$true,$false); Add-Phase ('DOC_OPENED PAGES='+$doc.ComputeStatistics(2))
    $doc.ExportAsFixedFormat($pdf,17); Add-Phase 'PDF_EXPORTED'
    $doc.Close(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc); $doc=$null
    $word.Quit(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word); $word=$null
    for ($i=0;$i -lt 80;$i++) { if (-not (Get-Process -Id $newPid -ErrorAction SilentlyContinue)) { break }; Start-Sleep -Milliseconds 250 }
    $after=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
    $exited=-not [bool](Get-Process -Id $newPid -ErrorAction SilentlyContinue)
    $unchanged=(@($after | Where-Object { $_ -in $before }).Count -eq $before.Count)
    $unexpected=@($after | Where-Object { $_ -notin $before })
    $pdfSha=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()
    $result=[pscustomobject]@{status=if($exited -and $unchanged -and $unexpected.Count -eq 0 -and (Get-Item $pdf).Length -gt 0 -and $docxShaBefore -eq $expectedDocxSha){'PASS'}else{'FAIL'};doc_id='0105';revision='R04';docx_sha256=$docxShaBefore;pdf_path=$pdf;pdf_sha256=$pdfSha;pdf_bytes=(Get-Item $pdf).Length;new_word_pid=$newPid;new_word_pid_exited=$exited;preexisting_word_pids_unchanged=$unchanged;preexisting_count=$before.Count;unexpected_new_word_pids=$unexpected;started_at=$started;verified_at=(Get-Date).ToString('o');error=$null}
} catch {
    $err=$_.Exception.Message
    Add-Phase ('ERROR '+$err+' STACK '+$_.ScriptStackTrace)
    $result=[pscustomobject]@{status='FAIL';doc_id='0105';revision='R04';docx_path=$docx;pdf_path=$pdf;new_word_pid=$newPid;preexisting_pids=$before;started_at=$started;verified_at=(Get-Date).ToString('o');error=$err;error_stack=$_.ScriptStackTrace;position=$_.InvocationInfo.PositionMessage}
    if ($newPid -and $word) { try { if($doc){$doc.Close(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)} } catch {}; try {$word.Quit(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)} catch {} }
}
$result | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $receiptPath -Encoding utf8
$result | ConvertTo-Json -Depth 5
if ($result.status -ne 'PASS') { exit 1 }
