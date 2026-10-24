$ErrorActionPreference='Stop'
$repo='E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016'
$root=Join-Path $repo 'docs\ttqs-quality-20261016\quality-review\0063_R01'
$dir=Join-Path $root 'evidence\review_R01'
$docx=Join-Path $root 'candidate\0063_R01.docx'
$packet=Join-Path $dir '0063_R01_SEMANTIC_REVIEW_PACKET.md'
$exe='C:\Users\J\AppData\Local\Programs\@opencode-aidesktop\resources\opencode-cli.exe'
$session='ses_eb24a07aeffeXb5vPLg3Hs2KQG'
$out=Join-Path $dir 'opencode_resume_R02_stdout.jsonl'
$err=Join-Path $dir 'opencode_resume_R02_stderr.txt'
$receiptPath=Join-Path $dir 'opencode_resume_R02_launch_receipt.json'
$requestPath=Join-Path $dir 'opencode_resume_R02_request.txt'
if(Test-Path $out){throw 'Refusing to overwrite reviewer stdout.'}
if(Test-Path $err){throw 'Refusing to overwrite reviewer stderr.'}
if(Test-Path $receiptPath){throw 'Refusing to overwrite launch receipt.'}
$docxSha=(Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
$packetSha=(Get-FileHash -LiteralPath $packet -Algorithm SHA256).Hash.ToLowerInvariant()
if($docxSha -ne '4e2d56c9ce46b8acdb2d8b3288ed6083a054c4bb2955edf2127a4f16c058792d'){throw 'Candidate SHA changed; refusing to resume.'}
if($packetSha -ne 'bd1850baa2383d357bfc30641cfd0777eb2e4d83e1a92d4155f361fa6e4f07fe'){throw 'Review packet SHA changed; refusing to resume.'}
$version=(& $exe --version | Out-String).Trim()
$request='Continue from the current state in this exact existing session. Do not reread the full packet or repeat completed checks; use gathered evidence and only targeted reads if required. Finish the independent semantic review of DOCX 0063 R01 bound to SHA-256 4e2d56c9ce46b8acdb2d8b3288ed6083a054c4bb2955edf2127a4f16c058792d and Blueprint SHA 9c5e91155a18ccb5aae2a21f7bba40f35d8c483b973436873f08e2fde925dd34, official requirement I14-E04 / checkbox 068. Return PASS, PARTIAL, or FAIL with concrete body locators; cover title-blind genre, negative neighbors, staff usability, SAMPLE/REAL boundary, arithmetic, dates, cross-document facts, and remaining defects. Visual review was not performed. Do not edit files. If any required criterion is unresolved, return PARTIAL.'
[IO.File]::WriteAllText($requestPath,$request,[Text.UTF8Encoding]::new($false))
$argumentLine='run --session '+$session+' --model opencode/nemotron-3.5-lightning-free --format json "'+$request.Replace('"','\"')+'"'
$started=[DateTimeOffset]::Now
$p=Start-Process -FilePath $exe -ArgumentList $argumentLine -WorkingDirectory $repo -WindowStyle Hidden -PassThru -RedirectStandardOutput $out -RedirectStandardError $err
$scriptSha=(Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLowerInvariant()
$receipt=[ordered]@{project_id='TTQS_ONE';doc_id='0063';review_revision='R01';attempt='resume_R02';route='OpenCode v2 CLI';cli_version=$version;requested_model='opencode/nemotron-3.5-lightning-free';runtime_model_identity='NOT_ATTESTED';session_id=$session;candidate_sha256=$docxSha;review_packet_sha256=$packetSha;request_sha256=(Get-FileHash -LiteralPath $requestPath -Algorithm SHA256).Hash.ToLowerInvariant();runner_script_sha256=$scriptSha;started_local=$started.ToString('o');process_id=$p.Id;stdout_path='evidence/review_R01/opencode_resume_R02_stdout.jsonl';stderr_path='evidence/review_R01/opencode_resume_R02_stderr.txt';provider_billing='UNKNOWN';status='RUNNING_SAME_EXISTING_SESSION';visual_review='NOT_PERFORMED'}
[IO.File]::WriteAllText($receiptPath,($receipt|ConvertTo-Json -Depth 8),[Text.UTF8Encoding]::new($false))
Get-Content -LiteralPath $receiptPath -Raw