$ErrorActionPreference='Stop'
function Get-Sha256($path){$alg=[Security.Cryptography.SHA256]::Create();$fs=[IO.File]::OpenRead($path);try{([BitConverter]::ToString($alg.ComputeHash($fs))).Replace('-','').ToLowerInvariant()}finally{$fs.Dispose();$alg.Dispose()}}
$stage='E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0127_I19-E16_SOURCE_PREP_R01_20261024\codex_fallback_R02_visual_repair'
$docx=(Get-ChildItem -LiteralPath $stage -Filter '*R02_CODEX_CANDIDATE.docx' -File|Select-Object -First 1).FullName
$pdf=Join-Path $stage '0127_R02_word_native.pdf';$out=Join-Path $stage 'word_native_render_0127_R02.json'
$expected='abba46bcdd0919c4511df025cd90d65cd302fe3f9f59c86d0fa8b7efe2015285'
$before=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|Select-Object -ExpandProperty ProcessId|Sort-Object)
$word=$null;$doc=$null;$newPid=$null;$started=(Get-Date).ToString('o');$err=$null;$pages=$null
try{
 $actual=(Get-Sha256 $docx);if($actual -ne $expected){throw "candidate SHA mismatch: $actual"}
 $word=New-Object -ComObject Word.Application;$word.Visible=$false;$word.DisplayAlerts=0
 Start-Sleep -Milliseconds 400
 $now=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|Select-Object -ExpandProperty ProcessId|Sort-Object);$delta=@($now|Where-Object{$_ -notin $before})
 if($delta.Count -ne 1){throw "expected one unique new WINWORD PID, found $($delta.Count)"};$newPid=[int]$delta[0]
 $doc=$word.Documents.Open($docx,$false,$true,$false);$pages=$doc.ComputeStatistics(2);$doc.ExportAsFixedFormat($pdf,17)
 if(!(Test-Path -LiteralPath $pdf) -or (Get-Item -LiteralPath $pdf).Length -le 0){throw 'Word export returned without a non-empty PDF'}
}catch{$err=$_.Exception.ToString()}
finally{
 try{if($doc){$doc.Close(0)}}catch{if(-not $err){$err=$_.Exception.ToString()}}
 try{if($doc){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc)}}catch{};$doc=$null
 if($word -and $newPid -and $newPid -notin $before){try{$save=0;$fmt=0;$route=0;$word.Quit([ref]$save,[ref]$fmt,[ref]$route)}catch{if(-not $err){$err=$_.Exception.ToString()}}}
 try{if($word){[void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word)}}catch{};$word=$null
}
if($newPid){Start-Sleep -Milliseconds 500}
$after=@(Get-CimInstance Win32_Process -Filter "Name='WINWORD.EXE'"|Select-Object -ExpandProperty ProcessId|Sort-Object);$unexpected=@($after|Where-Object{$_ -notin $before})
$docSha=(Get-Sha256 $docx);$pdfSha=$null;$bytes=0;if(Test-Path -LiteralPath $pdf){$pdfSha=(Get-Sha256 $pdf);$bytes=(Get-Item -LiteralPath $pdf).Length}
$ok=($docSha -eq $expected -and $bytes -gt 0 -and $unexpected.Count -eq 0 -and $after.Count -eq $before.Count -and -not $err)
$r=[pscustomobject]@{status=if($ok){'PASS_WORD_NATIVE_EXPORT'}elseif($err){'BLOCKED_OR_FAIL'}else{'FAIL'};docx_sha256=$docSha;expected_sha256=$expected;pdf_sha256=$pdfSha;pdf_bytes=$bytes;page_count=$pages;new_owned_word_pid=$newPid;baseline_word_pid_count=$before.Count;baseline_word_pids_preserved=(@($before|Where-Object{$_ -in $after}).Count -eq $before.Count);unexpected_new_word_pids=$unexpected;method='Microsoft Word COM, hidden, read-only open, ExportAsFixedFormat PDF, close only opened document, quit only unique new process';started_at=$started;finished_at=(Get-Date).ToString('o');error=$err}
[IO.File]::WriteAllText($out,($r|ConvertTo-Json -Depth 6),[Text.UTF8Encoding]::new($false));$r|ConvertTo-Json -Depth 6