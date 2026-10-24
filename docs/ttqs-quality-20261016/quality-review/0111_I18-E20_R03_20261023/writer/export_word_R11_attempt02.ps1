$ErrorActionPreference = 'Stop'
$base = 'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0111_I18-E20_SOURCE_PREP_20261023'
$docx = Join-Path $base 'candidate\0111_I18-E20_特殊績效及社會面成果證據登錄表_R03.docx'
$visual = Join-Path $base 'visual\0111_R03'
$pdf = Join-Path $visual '0111_R03_word_native.pdf'
$evidence = Join-Path $base 'evidence'
$ownerPath = Join-Path $evidence 'word_export_owner_0111_R03_R11_attempt02.json'
$receiptPath = Join-Path $evidence 'word_export_receipt_0111_R03_R11_attempt02.json'
$expectedDocxSha = 'f427ed898a79393a91d6d8fadcde960a8126e90697325aa94c1b764b8b537a50'
$started = (Get-Date).ToString('o')
$before = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | ForEach-Object { [int]$_.ProcessId })
$word = $null; $doc = $null; $newPid = $null; $pidCreation = $null
try {
  if ((Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower() -ne $expectedDocxSha) { throw 'Candidate SHA changed before export' }
  if (Test-Path -LiteralPath $pdf) { throw 'Refuse to overwrite existing PDF' }
  if (Test-Path -LiteralPath $ownerPath -or Test-Path -LiteralPath $receiptPath) { throw 'Attempt evidence path already exists; refuse overwrite' }
  New-Item -ItemType Directory -Path $visual -Force | Out-Null
  $word = New-Object -ComObject Word.Application
  for ($i=0; $i -lt 40 -and -not $newPid; $i++) {
    Start-Sleep -Milliseconds 250
    $now = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | ForEach-Object { [int]$_.ProcessId })
    $delta = @($now | Where-Object { $_ -notin $before })
    if ($delta.Count -eq 1) { $newPid = [int]$delta[0] }
    elseif ($delta.Count -gt 1) { throw "Ambiguous new Word PIDs: $($delta -join ',')" }
  }
  if (-not $newPid) { throw 'Word COM returned without one uniquely attributable new WINWORD process' }
  $procInfo = Get-CimInstance Win32_Process -Filter "ProcessId=$newPid"
  if (-not $procInfo -or -not $procInfo.ExecutablePath.EndsWith('WINWORD.EXE',[StringComparison]::OrdinalIgnoreCase) -or $procInfo.CommandLine -notmatch '/Automation\s+-Embedding') { throw 'Unique process did not match hidden Word automation identity' }
  $pidCreation = ([datetime]$procInfo.CreationDate).ToString('o')
  [ordered]@{doc_id='0111';revision='R03';candidate_sha256=$expectedDocxSha;word_pid=$newPid;word_creation_time=$pidCreation;word_path=$procInfo.ExecutablePath;word_command_line=$procInfo.CommandLine;exporter_pid=$PID;started_at=$started;ownership_method='unique WINWORD PID absent from baseline; exact creation time/path/Automation command'} | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $ownerPath -Encoding UTF8
  $word.Visible = $false
  $word.DisplayAlerts = 0
  $word.AutomationSecurity = 3
  $documentCountBefore = [int]$word.Documents.Count
  if ($documentCountBefore -ne 0) { throw "Fresh Word instance already has $documentCountBefore open documents" }
  $doc = $word.Documents.Open($docx,$false,$true,$false)
  $null = $doc.Fields.Update()
  $doc.ExportAsFixedFormat($pdf,17,$false,0,0,1,999,0,$true,$false,0,$true,$false,$false)
  $doc.Close(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc); $doc=$null
  $version = [string]$word.Version
  $word.Quit(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word); $word=$null
  for ($i=0; $i -lt 80 -and (Get-Process -Id $newPid -ErrorAction SilentlyContinue); $i++) { Start-Sleep -Milliseconds 250 }
  if (-not (Test-Path -LiteralPath $pdf) -or (Get-Item -LiteralPath $pdf).Length -le 0) { throw 'Word returned without a nonempty PDF' }
  $docxShaAfter = (Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower()
  $pdfSha = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()
  $alive = [bool](Get-Process -Id $newPid -ErrorAction SilentlyContinue)
  $after = @(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | ForEach-Object { [int]$_.ProcessId })
  $preexistingUnchanged = (@($before | Where-Object { $_ -in $after }).Count -eq $before.Count)
  $unexpected = @($after | Where-Object { $_ -notin $before })
  $status = if ($docxShaAfter -eq $expectedDocxSha -and -not $alive -and $preexistingUnchanged -and $unexpected.Count -eq 0) { 'PDF_EXPORTED_PENDING_PAGE_COUNT_RENDER_AND_VISUAL_INSPECTION' } else { 'EXPORT_RESULT_NEEDS_INVESTIGATION' }
  [ordered]@{doc_id='0111';official_requirement_id='I18-E20';revision='R03';status=$status;docx_path=$docx;docx_sha256=$docxShaAfter;pdf_path=$pdf;pdf_sha256=$pdfSha;pdf_bytes=(Get-Item -LiteralPath $pdf).Length;word_version=$version;word_pid=$newPid;word_creation_time=$pidCreation;word_exited=(-not $alive);preexisting_word_pids_unchanged=$preexistingUnchanged;unexpected_new_word_pids=$unexpected;read_only=$true;fresh_instance_document_count_before_open=$documentCountBefore;export_method='Microsoft Word COM ExportAsFixedFormat; R08c verified 14-argument flags';started_at=$started;verified_at=(Get-Date).ToString('o')} | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
} catch {
  $msg = $_.Exception.Message
  if ($doc) { try { $doc.Close(0) } catch {} }
  if ($word) { try { $word.Quit(0) } catch {} }
  if ($doc) { try { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc) } catch {} }
  if ($word) { try { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) } catch {} }
  [ordered]@{doc_id='0111';official_requirement_id='I18-E20';revision='R03';status='EXPORT_FAILED';docx_sha256=(if (Test-Path -LiteralPath $docx) {(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower()} else {$null});pdf_path=$pdf;word_pid=$newPid;word_creation_time=$pidCreation;error=$msg;started_at=$started;verified_at=(Get-Date).ToString('o')} | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $receiptPath -Encoding UTF8
  exit 1
}
