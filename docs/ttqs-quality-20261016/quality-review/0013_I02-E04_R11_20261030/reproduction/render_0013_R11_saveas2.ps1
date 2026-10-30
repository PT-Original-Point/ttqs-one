$ErrorActionPreference='Stop'
$manifest=Join-Path $PSHOME 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1'; if(Test-Path $manifest){Import-Module $manifest -Force -ErrorAction Stop}
$docx='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029\candidate\0013_I02-E04_R11.docx'
$pdf='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029\qa\render_R11_saveas2_trial\0013_I02-E04_R11_WORD_SAVEAS2.pdf'
$log='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029\qa\render_R11_saveas2_trial\progress.jsonl'
$expected='c6570ac11ac06e889628937069c4d66944e4a59e287f8df3cbcd3fa468f5dc95'
function M($p,$d=@{}){$o=[ordered]@{at=(Get-Date).ToString('o');phase=$p};foreach($k in $d.Keys){$o[$k]=$d[$k]};($o|ConvertTo-Json -Compress -Depth 4)|Add-Content -LiteralPath $log -Encoding utf8}
$baseline=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|% ProcessId);$word=$null;$doc=$null;$wpid=$null
try{
$sha=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower();M 'START' @{candidate_sha=$sha;baseline_word_count=$baseline.Count}
if($sha -ne $expected){throw 'Candidate SHA mismatch'}
if(Test-Path -LiteralPath $pdf){throw 'Target PDF already exists; refusing overwrite'}
$word=New-Object -ComObject Word.Application;$word.Visible=$false;$word.DisplayAlerts=0;$word.ScreenUpdating=$false;M 'COM_CREATED' @{}
for($i=0;$i -lt 80 -and -not $wpid;$i++){Start-Sleep -Milliseconds 250;$now=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|% ProcessId);$delta=@($now|?{$_ -notin $baseline});if($delta.Count -eq 1){$wpid=[int]$delta[0]}elseif($delta.Count -gt 1){throw ('Ambiguous new Word PID '+($delta -join ','))}}
if(-not $wpid){throw 'No unique new Word PID'}
M 'WORD_PID' @{word_pid=$wpid}
$doc=$word.Documents.Open($docx,$false,$true,$false);M 'OPENED' @{word_pid=$wpid;page_count=$doc.ComputeStatistics(2)}
M 'SAVEAS2_BEGIN' @{word_pid=$wpid;pdf=$pdf}
$doc.SaveAs2($pdf,17);M 'SAVEAS2_DONE' @{pdf_bytes=(Get-Item $pdf).Length;pdf_sha256=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()}
$doc.Close(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc);$doc=$null;$word.Quit(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word);$word=$null;M 'CLOSED' @{word_pid=$wpid}
}catch{M 'ERROR' @{message=$_.Exception.ToString();word_pid=$wpid};if($doc){try{$doc.Close(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}catch{}};if($word){try{$word.Quit(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}catch{}};exit 1}

