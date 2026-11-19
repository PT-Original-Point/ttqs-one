$ErrorActionPreference='Stop'
$base='E:\PT-Original-Point\ttqs-one\docs\ttqs-quality-20261016\quality-review\0105_I18-E13_R01_20261022'
$docx=(Get-ChildItem -LiteralPath (Join-Path $base 'candidate') -Filter '*_R04.docx' | Select-Object -First 1 -ExpandProperty FullName)
$pdf=Join-Path $base 'visual\0105_R04\0105_R04_word_saveas.pdf'
$temp=Join-Path $base 'visual\0105_R04\0105_R04_word_saveas_source.docx'
$receiptPath=Join-Path $base 'evidence\word_saveas_receipt_0105_R04.json'
$phasePath=Join-Path $base 'evidence\word_saveas_phase_R04.txt'
$expected='17f7d680cbb992db93a6f67df84415500050953eecf426b477f675810177b4cb'
Set-Content -LiteralPath $phasePath -Value ('START '+(Get-Date).ToString('o')) -Encoding UTF8
function Phase([string]$v){Add-Content -LiteralPath $phasePath -Value ((Get-Date).ToString('o')+' '+$v) -Encoding UTF8}
$before=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|Select-Object -ExpandProperty ProcessId|Sort-Object)
$word=$null;$doc=$null;$newPid=$null;$started=(Get-Date).ToString('o')
try{
 $srcSha=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower();if($srcSha -ne $expected){throw 'source candidate SHA mismatch'}
 Copy-Item -LiteralPath $docx -Destination $temp -Force
 $copySha=(Get-FileHash -LiteralPath $temp -Algorithm SHA256).Hash.ToLower();if($copySha -ne $expected){throw 'temporary source copy SHA mismatch'};Phase 'SOURCE_COPY_VERIFIED'
 $word=New-Object -ComObject Word.Application;Phase 'COM_CREATED';$word.Visible=$false;$word.DisplayAlerts=0
 for($i=0;$i -lt 40 -and -not $newPid;$i++){Start-Sleep -Milliseconds 250;$now=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|Select-Object -ExpandProperty ProcessId|Sort-Object);$delta=@($now|Where-Object {$_ -notin $before});if($delta.Count -eq 1){$newPid=[int]$delta[0]}elseif($delta.Count -gt 1){throw "Ambiguous new Word process list: $($delta -join ',')"}}
 if(-not $newPid){throw 'No unique new WINWORD PID'};Phase ('WORD_PID '+$newPid)
 $doc=$word.Documents.Open($temp,$false,$false,$false);Phase ('DOC_OPENED PAGES='+$doc.ComputeStatistics(2))
 $doc.SaveAs2($pdf,17);Phase 'SAVEAS2_RETURNED'
 $doc.Close(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc);$doc=$null
 $word.Quit(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word);$word=$null
 for($i=0;$i -lt 80;$i++){if(-not(Get-Process -Id $newPid -ErrorAction SilentlyContinue)){break};Start-Sleep -Milliseconds 250}
 $after=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|Select-Object -ExpandProperty ProcessId|Sort-Object);$exited=-not[bool](Get-Process -Id $newPid -ErrorAction SilentlyContinue);$baseline=@($after|Where-Object {$_ -in $before}).Count -eq $before.Count;$unexpected=@($after|Where-Object {$_ -notin $before});$pdfSha=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLower()
 $result=[pscustomobject]@{status=if($exited -and $baseline -and $unexpected.Count -eq 0 -and (Get-Item $pdf).Length -gt 0 -and $srcSha -eq $expected){'PASS'}else{'FAIL'};doc_id='0105';revision='R04';method='Microsoft Word COM SaveAs2 WdFormatPDF 17, from byte-identical temporary DOCX copy';source_docx_sha256=$srcSha;temporary_docx_sha256=$copySha;pdf_path=$pdf;pdf_sha256=$pdfSha;pdf_bytes=(Get-Item $pdf).Length;new_word_pid=$newPid;new_word_pid_exited=$exited;preexisting_word_pids_unchanged=$baseline;preexisting_count=$before.Count;unexpected_new_word_pids=$unexpected;started_at=$started;verified_at=(Get-Date).ToString('o');error=$null}
}catch{
 $err=$_.Exception.Message;Phase ('ERROR '+$err+' STACK '+$_.ScriptStackTrace)
 $result=[pscustomobject]@{status='FAIL';doc_id='0105';revision='R04';source_docx_path=$docx;source_docx_sha256=if(Test-Path -LiteralPath $docx){(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLower()}else{$null};temporary_path=$temp;pdf_path=$pdf;new_word_pid=$newPid;preexisting_pids=$before;started_at=$started;verified_at=(Get-Date).ToString('o');error=$err;error_stack=$_.ScriptStackTrace;position=$_.InvocationInfo.PositionMessage}
 if($newPid -and $word){try{if($doc){$doc.Close(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}}catch{};try{$word.Quit(0);[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}catch{}}
}
$result|ConvertTo-Json -Depth 5|Set-Content -LiteralPath $receiptPath -Encoding UTF8
$result|ConvertTo-Json -Depth 5
if($result.status -ne 'PASS'){exit 1}