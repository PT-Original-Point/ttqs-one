$ErrorActionPreference = 'Stop'
$root = 'E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0103_I18-E10_R01_20261022'
$docx = Join-Path $root 'candidate\0103__I18-E10__感謝函取得與真偽查核工作紀錄_R03.docx'
$pdf = Join-Path $root 'render\0103_R03_word_native.pdf'
$receiptPath = Join-Path $root 'evidence\word_export_0103_R03_isolated.json'
$expectedDocxSha = '7b95524d9e0c0010ebd45938dad25afe2432e2d6f0c83bba4cafbf7d180375e2'
New-Item -ItemType Directory -Path (Split-Path -Parent $pdf) -Force | Out-Null
$before = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
$word = $null; $doc = $null; $newPid = $null; $started = (Get-Date).ToString('o'); $err = $null
try {
 if ((Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower() -ne $expectedDocxSha) { throw '0103 R03 candidate SHA changed before export' }
 $word = New-Object -ComObject Word.Application
 $word.Visible = $false; $word.DisplayAlerts = 0
 for ($i=0; $i -lt 40 -and -not $newPid; $i++) {
  Start-Sleep -Milliseconds 250
  $now = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
  $delta = @($now | Where-Object { $_ -notin $before })
  if ($delta.Count -eq 1) { $newPid = [int]$delta[0] }
  elseif ($delta.Count -gt 1) { throw "Ambiguous new Word processes: $($delta -join ',')" }
 }
 if (-not $newPid) { throw 'No unique new WINWORD PID appeared; do not attach to or close a pre-existing Word process' }
 $doc = $word.Documents.Open($docx, $false, $true, $false)
 $doc.ExportAsFixedFormat($pdf, 17)
 $doc.Close(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc); $doc=$null
 $word.Quit(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word); $word=$null
 for ($i=0; $i -lt 80; $i++) { if (-not (Get-Process -Id $newPid -ErrorAction SilentlyContinue)) { break }; Start-Sleep -Milliseconds 250 }
 $after = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId | Sort-Object)
 $survivingBaseline = @($before | Where-Object { $_ -in $after })
 $unexpected = @($after | Where-Object { $_ -notin $before })
 $exited = -not [bool](Get-Process -Id $newPid -ErrorAction SilentlyContinue)
 $docxSha = (Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower()
 $pdfSha = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()
 $pdfBytes = (Get-Item -LiteralPath $pdf).Length
 $result = [pscustomobject]@{status=if($docxSha -eq $expectedDocxSha -and $exited -and $survivingBaseline.Count -eq $before.Count -and $unexpected.Count -eq 0 -and $pdfBytes -gt 0){'PASS'}else{'FAIL'};docx_sha256=$docxSha;pdf_sha256=$pdfSha;pdf_bytes=$pdfBytes;docx_path=$docx;pdf_path=$pdf;new_word_pid=$newPid;new_pid_exited=$exited;baseline_word_count=$before.Count;baseline_pids_preserved=($survivingBaseline.Count -eq $before.Count);unexpected_new_word_pids=$unexpected;method='Word COM Dispatch using unique new WINWORD PID delta; no Hwnd access; read-only open; native ExportAsFixedFormat';started_at=$started;verified_at=(Get-Date).ToString('o');error=$null}
} catch {
 $err=$_.Exception.Message
 if ($newPid -and $word) { try { if($doc){$doc.Close(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)} } catch {}; try {$word.Quit(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)} catch {} }
 $result=[pscustomobject]@{status='FAIL';docx_sha256=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower();docx_path=$docx;pdf_path=$pdf;new_word_pid=$newPid;baseline_word_pids=$before;method='Word COM Dispatch using unique new WINWORD PID delta; no Hwnd access; read-only open';started_at=$started;verified_at=(Get-Date).ToString('o');error=$err}
}
$result | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $receiptPath -Encoding utf8
$result | ConvertTo-Json -Depth 6
if ($result.status -ne 'PASS') { exit 1 }
