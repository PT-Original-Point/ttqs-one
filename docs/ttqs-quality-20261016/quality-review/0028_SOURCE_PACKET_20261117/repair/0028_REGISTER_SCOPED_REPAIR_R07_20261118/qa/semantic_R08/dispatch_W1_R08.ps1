$ErrorActionPreference='Stop'
$qa=(Resolve-Path 'qa\semantic_R08').Path
$packet=(Resolve-Path 'qa\semantic_R08\W1_REVIEW_PACKET_R08.md').Path
$manifest=Join-Path $qa 'W1_DISPATCH_R08.json'
$stdout=Join-Path $qa 'W1_STDOUT_R08.jsonl'
$stderr=Join-Path $qa 'W1_STDERR_R08.txt'
if((Test-Path $manifest)-or(Test-Path $stdout)-or(Test-Path $stderr)){throw 'W1_R08_DISPATCH_ARTIFACT_EXISTS_REFUSE_DUPLICATE'}
$exe='C:\Users\J\AppData\Roaming\npm\node_modules\@opencode\cli\bin\opencode.exe'
if(-not(Test-Path $exe)){throw 'OPENCODE_CLI_EXECUTABLE_MISSING'}
$sha=(Get-FileHash -LiteralPath $packet -Algorithm SHA256).Hash
$active=@(Get-CimInstance Win32_Process -Filter "Name='opencode.exe'" | Where-Object {$_.CommandLine -and ($_.CommandLine -match 'W1_REVIEW_PACKET_R08|TTQS_ONE_0028_I05-E02_W1_SEMANTIC_REVIEW_R08')})
if($active.Count){throw 'SAME_SCOPE_OPENCODE_REVIEW_ALREADY_ACTIVE'}
$tempRoot=Join-Path $env:TEMP 'TTQS_ONE_0028_R08_W1_REVIEW'
New-Item -ItemType Directory -Force -Path $tempRoot|Out-Null
$message='Perform the bounded independent review from the attached packet. Return exactly the specified JSON object. Do not edit, create, or delete files. Do not broaden scope.'
$args=@('run','--model','opencode/nemotron-3.5-lightning-free','--format','json','--file',('"'+$packet+'"'),('"'+$message+'"'))
$argline=$args -join ' '
$started=Get-Date
$proc=Start-Process -FilePath $exe -ArgumentList $argline -WorkingDirectory $tempRoot -WindowStyle Hidden -RedirectStandardOutput $stdout -RedirectStandardError $stderr -PassThru
$manifestData=[ordered]@{
 schema='TTQS_ONE_0028_W1_DISPATCH_R08'
 work_id='TTQS_ONE_0028_I05-E02_W1_SEMANTIC_REVIEW_R08_20261118'
 route='W1_OpenCode_v2_CLI'
 cli_version='opencode v2.3.0'
 executable=$exe
 requested_model='opencode/nemotron-3.5-lightning-free'
 served_model='UNKNOWN_UNTIL_PROVIDER_OR_RESPONSE_METADATA'
 process_id=$proc.Id
 process_start_time=$started.ToString('o')
 working_directory=$tempRoot
 packet_path=$packet
 packet_sha256=$sha
 candidate_sha256='1EB4E9D26F761B57885AF7DC304BB76324AD85C7513FC858C82AF199D5273F70'
 extracted_text_sha256='B999DF1D0A681825C4CD57D7E6220F21E32CC7660EF5FF6983EE3FD8D6474D79'
 stdout_path=$stdout
 stderr_path=$stderr
 status='RUNNING'
 timeout_seconds=900
 automatic_retry=false
 no_file_modification_requested=true
}
$manifestData|ConvertTo-Json -Depth 8|Set-Content -LiteralPath $manifest -Encoding utf8
[pscustomobject]@{work_id=$manifestData.work_id;pid=$proc.Id;route=$manifestData.requested_model;packet_sha256=$sha;status=$manifestData.status;manifest=$manifest}|ConvertTo-Json -Compress
