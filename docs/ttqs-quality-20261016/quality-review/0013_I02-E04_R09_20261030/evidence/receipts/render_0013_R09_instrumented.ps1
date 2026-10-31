$ErrorActionPreference='Stop'
$manifest=Join-Path $PSHOME 'Modules\Microsoft.PowerShell.Utility\Microsoft.PowerShell.Utility.psd1'; if(Test-Path $manifest){Import-Module $manifest -Force -ErrorAction Stop}
$runtime='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0013_I02-E04_LUNA_TEXT_DRAFT_R01_20261029'; $qa=Join-Path $runtime 'qa'; $stage=Join-Path $qa 'render_R09_instrumented'; New-Item -ItemType Directory -Path $stage -Force|Out-Null
$docx=Join-Path $runtime 'candidate\0013_I02-E04_R09.docx'; $pdf=Join-Path $stage '0013_I02-E04_R09_WORD_NATIVE.pdf'; $log=Join-Path $stage 'progress.jsonl'; $expected='dd5ff6cc55c649952872e03a77e77f844375df3db9a86f2bf664aefe1554df3f'
function Mark([string]$phase,[hashtable]$details=@{}){ $o=[ordered]@{at=(Get-Date).ToString('o');phase=$phase}; foreach($k in $details.Keys){$o[$k]=$details[$k]}; ($o|ConvertTo-Json -Compress -Depth 5)|Add-Content -LiteralPath $log -Encoding utf8 }
$before=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|Select-Object -ExpandProperty ProcessId|Sort-Object); $word=$null;$doc=$null;$newPid=$null
try{
 Mark 'START' @{candidate_sha=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower();baseline_word_count=$before.Count}
 if((Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower() -ne $expected){throw 'R09 candidate SHA mismatch'}
 Mark 'COM_CREATE_BEGIN' @{}
 $word=New-Object -ComObject Word.Application; $word.Visible=$false; $word.DisplayAlerts=0
 Mark 'COM_CREATED' @{}
 for($i=0;$i -lt 40 -and -not $newPid;$i++){Start-Sleep -Milliseconds 250;$now=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|Select-Object -ExpandProperty ProcessId|Sort-Object);$delta=@($now|Where-Object{$_ -notin $before});if($delta.Count -eq 1){$newPid=[int]$delta[0]}elseif($delta.Count -gt 1){throw "Ambiguous new Word PIDs: $($delta -join ',')"}}
 if(-not $newPid){throw 'No unique new Word PID'}; Mark 'WORD_PID_IDENTIFIED' @{word_pid=$newPid}
 Mark 'DOCUMENT_OPEN_BEGIN' @{word_pid=$newPid}
 $doc=$word.Documents.Open($docx,$false,$true,$false)
 Mark 'DOCUMENT_OPENED' @{word_pid=$newPid;page_count=$doc.ComputeStatistics(2)}
 Mark 'PDF_EXPORT_BEGIN' @{word_pid=$newPid;pdf=$pdf}
 $doc.ExportAsFixedFormat($pdf,17)
 Mark 'PDF_EXPORT_DONE' @{pdf_bytes=(Get-Item $pdf).Length;pdf_sha256=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()}
 $doc.Close(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc);$doc=$null
 $word.Quit(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word);$word=$null
 Mark 'COM_CLOSED' @{word_pid=$newPid}
}catch{ Mark 'ERROR' @{message=$_.Exception.ToString();word_pid=$newPid} ; if($doc){try{$doc.Close(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}catch{}}; if($word){try{$word.Quit(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}catch{}}; exit 1 }
