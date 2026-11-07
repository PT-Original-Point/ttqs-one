$ErrorActionPreference='Stop'
$base='E:\TTQS\_r09_opencode_0108_text_only_20261022_R01';$docx=Join-Path $base 'candidate\0108_I18-E16_candidate_R01-C08.docx';$dir=Join-Path $base 'render\R01-C08';$pdf=Join-Path $dir '0108_R01-C08_Word_export.pdf';$receipt=Join-Path $base 'evidence\word_export_R01-C08.json'
New-Item -ItemType Directory -Force -Path $dir|Out-Null
if(Test-Path -LiteralPath $pdf){throw 'Refusing to overwrite an existing C08 PDF'}
Add-Type -Namespace Native -Name WordWindowPid -MemberDefinition '[DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint processId);'
$start=(Get-Date).ToString('o');$before=@(Get-Process WINWORD -ErrorAction SilentlyContinue|ForEach-Object Id);$word=$null;$doc=$null;$ownedPid=$null;$windowPid=$null;$stage='COM_CREATE';$err=$null;$ver=$null;$pages=$null
try{
 $word=New-Object -ComObject Word.Application;Start-Sleep -Seconds 2
 $after=@(Get-Process WINWORD -ErrorAction SilentlyContinue|ForEach-Object Id);$delta=@($after|Where-Object{$_ -notin $before})
 if($delta.Count -ne 1){$stage='OWNERSHIP_AMBIGUOUS';throw "Refusing: preexisting=$($before -join ','); new=$($delta -join ',')"}
 $ownedPid=[int]$delta[0];$ver=$word.Version;$word.Visible=$false;$word.DisplayAlerts=0
 $stage='OPEN_READ_ONLY';$doc=$word.Documents.Open($docx,$false,$true,$false)
 $h=[IntPtr]([int64]$doc.ActiveWindow.Hwnd);[uint32]$wpid=0;$null=[Native.WordWindowPid]::GetWindowThreadProcessId($h,[ref]$wpid);$windowPid=[int]$wpid
 if($h -eq [IntPtr]::Zero -or $windowPid -ne $ownedPid){$stage='OWNERSHIP_WINDOW_MISMATCH';throw "C08 document window does not map to owned PID $ownedPid (window PID $windowPid)"}
 $stage='REPAGINATE';$doc.Repaginate();$pages=$doc.ComputeStatistics(2)
 $stage='EXPORT_PDF';$doc.ExportAsFixedFormat($pdf,17)
 $stage='CLOSE';$doc.Close(0);$doc=$null
 $stage='QUIT_OWNED_WORD';$word.Quit();$word=$null
}catch{$err=$_.Exception.Message}finally{if($doc){try{$doc.Close(0)}catch{}};if($word -and $ownedPid){try{$word.Quit()}catch{}}}
$docxHash=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant();$pdfHash=$null;$pdfBytes=0;if(Test-Path -LiteralPath $pdf){$pdfHash=(Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant();$pdfBytes=(Get-Item -LiteralPath $pdf).Length};$remaining=if($ownedPid){Get-Process -Id $ownedPid -ErrorAction SilentlyContinue}else{$null}
$r=[ordered]@{doc_id='0108';requirement='I18-E16';candidate='R01-C08';candidate_sha256=$docxHash;pdf_path='render/R01-C08/0108_R01-C08_Word_export.pdf';pdf_sha256=$pdfHash;pdf_bytes=$pdfBytes;word_version=$ver;preexisting_word_pids=$before;owned_pid=$ownedPid;document_window_pid=$windowPid;owned_pid_exited=($null -eq $remaining);page_count=$pages;read_only=$true;stage=$stage;started_at=$start;finished_at=(Get-Date).ToString('o');error=$err;status=$(if($pdfHash){'PDF_EXPORTED'}else{'FAILED'})}
$r|ConvertTo-Json -Depth 6|Set-Content -LiteralPath $receipt -Encoding utf8;$r|ConvertTo-Json -Compress
if(-not $pdfHash){exit 1}
