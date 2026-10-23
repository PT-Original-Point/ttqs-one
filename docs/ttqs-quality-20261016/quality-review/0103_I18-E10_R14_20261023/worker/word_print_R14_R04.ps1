$ErrorActionPreference='Stop'
$d='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\TEMP\R11_0103_R04'
$docx=Join-Path $d '0103__I18-E10__感謝函取得與真偽查核工作紀錄_R14.docx'
$pdf=Join-Path $d '0103_R14_word_print_to_pdf_R04.pdf'
$receipt=Join-Path $d 'word_print_0103_R14_R04.json'
$phase=Join-Path $d 'word_print_R14_R04_phase.txt'
$expected='4548a0fba48bb59c08389a6ec13edb1ffe61b58f6e3df3b302c5c4fa7cb39cb0'
function mark($s){[IO.File]::WriteAllText($phase,([DateTimeOffset]::Now.ToString('o')+'|'+$s))}
$baseline=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId)
$word=$null;$doc=$null;$status='FAIL';$err=$null;$started=[DateTimeOffset]::Now.ToString('o');$pidNew=$null;$pages=$null
try{
 mark 'start'
 $word=New-Object -ComObject Word.Application
 $word.Visible=$false;$word.DisplayAlerts=0;$word.ActivePrinter='Microsoft Print to PDF'
 $now=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId)
 $created=@($now | Where-Object {$_ -notin $baseline})
 if($created.Count -ne 1){throw "expected one new Word PID; got $($created.Count)"}
 $pidNew=[int]$created[0]
 $doc=$word.Documents.Open($docx,$false,$true,$false)
 $pages=[int]$doc.ComputeStatistics(2)
 mark "opened_pages=$pages;printer=$($word.ActivePrinter)"
 mark 'print_begin_by_value'
 $null=$doc.PrintOut([bool]$false,[bool]$false,[int]0,[string]$pdf,[int]1,[int]$pages,[int]0,[int]1,[string]'',[int]0,[bool]$true,[bool]$false,[string]'',[string]'',[bool]$false,[int]0,[int]0,[int]0,[int]0)
 mark 'print_return'
 $deadline=(Get-Date).AddSeconds(20)
 while(!(Test-Path -LiteralPath $pdf) -and (Get-Date) -lt $deadline){Start-Sleep -Milliseconds 500}
 if(!(Test-Path -LiteralPath $pdf)){throw 'PrintOut returned but PDF was not produced in 20 seconds'}
 if((Get-Item -LiteralPath $pdf).Length -lt 1000){throw 'PDF output too small'}
 $status='PASS'
}catch{$err=$_.Exception.ToString()}
finally{try{if($doc){$doc.Close(0)}}catch{};try{if($word){$word.Quit()}}catch{};try{if($doc){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}}catch{};try{if($word){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}}catch{}}
$after=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'" | Select-Object -ExpandProperty ProcessId);$survivors=@($baseline|Where-Object{$_ -in $after});$exists=Test-Path $pdf;$bytes=if($exists){(Get-Item $pdf).Length}else{0};$result=[ordered]@{status=$status;doc_id='0103';candidate_sha256=$expected;method='Word COM Document.PrintOut by-value positional args; Microsoft Print to PDF; hidden read-only';page_count=$pages;new_word_pid=$pidNew;baseline_word_pid_count=$baseline.Count;baseline_word_pids_preserved=($survivors.Count -eq $baseline.Count);pdf_exists=$exists;pdf_bytes=$bytes;started_at=$started;finished_at=[DateTimeOffset]::Now.ToString('o');error=$err};$result|ConvertTo-Json -Depth 5|Set-Content -LiteralPath $receipt -Encoding UTF8;mark "finished=$status";$result|ConvertTo-Json -Depth 5;if($status -ne 'PASS'){exit 1}
