$ErrorActionPreference='Stop'
$root='docs\ttqs-quality-20261016\quality-review\0063_R01'
$dir=Join-Path $root 'evidence\review_R01'
$packet=Join-Path $dir '0063_R01_SEMANTIC_REVIEW_PACKET.md'
$docx=Join-Path $root 'candidate\0063_R01.docx'
$exe='C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe'
$out=Join-Path $dir 'opencode_reviewer_stdout_R01.jsonl'
$err=Join-Path $dir 'opencode_reviewer_stderr_R01.txt'
$receiptPath=Join-Path $dir 'opencode_reviewer_receipt_R01.json'
$request='Review the complete attached exact-candidate packet as an independent semantic reviewer. Follow its checklist, give an overall PASS/PARTIAL/FAIL, locate all findings, and do not edit files. Keep the report concise and evidence-based. State visual review was not performed.'
[IO.File]::WriteAllText((Join-Path $dir 'opencode_reviewer_request_R01.txt'),$request,[Text.UTF8Encoding]::new($false))
$before=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
$packetHash=(Get-FileHash -LiteralPath $packet -Algorithm SHA256).Hash.ToLowerInvariant()
$version=(& $exe --version | Out-String).Trim()
$started=[DateTimeOffset]::Now
$psi=[Diagnostics.ProcessStartInfo]::new(); $psi.FileName=$exe; $psi.UseShellExecute=$false; $psi.RedirectStandardOutput=$true; $psi.RedirectStandardError=$true; $psi.StandardOutputEncoding=[Text.UTF8Encoding]::new($false); $psi.StandardErrorEncoding=[Text.UTF8Encoding]::new($false)
$packetQ='"'+$packet+'"'; $titleQ='"0063 Independent Semantic Review R01"'; $requestQ='"'+$request.Replace('"','\"')+'"'
$psi.Arguments='run --model opencode/nemotron-3.5-lightning-free --file '+$packetQ+' --title '+$titleQ+' --format json '+$requestQ
$p=[Diagnostics.Process]::new(); $p.StartInfo=$psi
if(-not $p.Start()){throw 'OpenCode reviewer process did not start'}
$outTask=$p.StandardOutput.ReadToEndAsync(); $errTask=$p.StandardError.ReadToEndAsync(); $finished=$p.WaitForExit(900000)
if(-not $finished){try{$p.Kill($true)}catch{}; $p.WaitForExit()}
$outText=$outTask.GetAwaiter().GetResult(); $errText=$errTask.GetAwaiter().GetResult()
[IO.File]::WriteAllText($out,$outText,[Text.UTF8Encoding]::new($false)); [IO.File]::WriteAllText($err,$errText,[Text.UTF8Encoding]::new($false))
$after=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant(); $packetAfter=(Get-FileHash -LiteralPath $packet -Algorithm SHA256).Hash.ToLowerInvariant(); $finishedAt=[DateTimeOffset]::Now
$receipt=[ordered]@{project_id='TTQS_ONE';doc_id='0063';requirement_id='I14-E04';official_checkbox_sequence='068';candidate_revision='R01';route='OpenCode v2 CLI independent reviewer';cli_version=$version;model_requested='opencode/nemotron-3.5-lightning-free';runtime_model_identity='NOT_ATTESTED';requested_free_label='visible in opencode models at dispatch';packet_path='quality-review/0063_R01/evidence/review_R01/0063_R01_SEMANTIC_REVIEW_PACKET.md';packet_sha256=$packetHash;docx_sha256_before=$before;docx_sha256_after=$after;packet_sha256_after=$packetAfter;invocation_args=@('run','--model','opencode/nemotron-3.5-lightning-free','--file','<review packet>','--title','0063 Independent Semantic Review R01','--format','json','<request saved>');started_local=$started.ToString('o');completed_local=$finishedAt.ToString('o');elapsed_seconds=[math]::Round(($finishedAt-$started).TotalSeconds,3);timed_out=(-not $finished);process_exit_code=$p.ExitCode;stdout_path='evidence/review_R01/opencode_reviewer_stdout_R01.jsonl';stdout_sha256=(Get-FileHash -LiteralPath $out -Algorithm SHA256).Hash.ToLowerInvariant();stderr_path='evidence/review_R01/opencode_reviewer_stderr_R01.txt';stderr_sha256=(Get-FileHash -LiteralPath $err -Algorithm SHA256).Hash.ToLowerInvariant();stdout_chars=$outText.Length;stderr_chars=$errText.Length;visual_review='NOT_IN_REVIEW_PACKET';docx_changed_by_review=$false;status=if((-not $finished) -or $p.ExitCode -ne 0 -or $outText.Length -eq 0){'INCOMPLETE'}else{'RETURNED_PENDING_PARSE'} }
[IO.File]::WriteAllText($receiptPath,($receipt|ConvertTo-Json -Depth 8),[Text.UTF8Encoding]::new($false))
Get-Content -LiteralPath $receiptPath -Raw
