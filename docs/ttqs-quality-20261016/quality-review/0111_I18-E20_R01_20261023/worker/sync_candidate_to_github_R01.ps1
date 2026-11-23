$ErrorActionPreference = 'Stop'
$repo = 'E:\TTQS\_github_sync_0064'
$branch = 'work/ttqs-one-document-quality-contract-20261016'
$root = 'E:\TTQS\TTQS_ONE_CODEX_RUNTIME\WORK\QUALITY_REBUILD_20261016\0111_I18-E20_SOURCE_PREP_20261023'
$manifestPath = Join-Path $root 'evidence\github_package_manifest_0111_R01.json'
$readbackPath = Join-Path $root 'evidence\github_raw_readback_receipt_0111_R01.json'
$prefix = 'docs/ttqs-quality-20261016/quality-review/0111_I18-E20_R01_20261023'
$expectedHead = '71ef5a70232950508ac443c39f632ff95705f862'
$encoding = [System.Text.UTF8Encoding]::new($false)

function Invoke-Git([string[]]$Arguments) {
    $out = & git -C $repo @Arguments 2>&1
    if ($LASTEXITCODE -ne 0) { throw ("git " + ($Arguments -join ' ') + " failed: " + ($out -join "`n")) }
    return ($out -join "`n").Trim()
}

function Get-RawBlobEvidence([string]$blobSha, [string]$label) {
    $tmp = Join-Path $env:TEMP ('ttqs_0111_remote_' + [guid]::NewGuid().ToString('N') + '.bin')
    $psi = [Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = 'git'
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.CreateNoWindow = $true
    foreach ($arg in @('-C',$repo,'cat-file','blob',$blobSha)) { [void]$psi.ArgumentList.Add($arg) }
    $proc = [Diagnostics.Process]::Start($psi)
    $fs = [IO.File]::Create($tmp)
    $proc.StandardOutput.BaseStream.CopyTo($fs)
    $fs.Dispose()
    $proc.WaitForExit()
    $err = $proc.StandardError.ReadToEnd()
    if ($proc.ExitCode -ne 0) { Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue; throw "remote blob read failed for $label : $err" }
    $sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $tmp).Hash.ToLower()
    $bytes = (Get-Item -LiteralPath $tmp).Length
    Remove-Item -LiteralPath $tmp -Force
    return [pscustomobject]@{ sha256 = $sha; bytes = $bytes }
}

function New-CommitWithFiles([string]$parent, [object[]]$files, [string]$message) {
    $tree = Invoke-Git @('rev-parse',("{0}^{{tree}}" -f $parent))
    $indexPath = Join-Path $env:TEMP ('ttqs_0111_index_' + [guid]::NewGuid().ToString('N'))
    $env:GIT_INDEX_FILE = $indexPath
    try {
        [void](Invoke-Git @('read-tree',$tree))
        foreach ($file in $files) {
            $blob = Invoke-Git @('hash-object','-w','--no-filters','--',$file.local_path)
            [void](Invoke-Git @('update-index','--add','--cacheinfo',("100644,{0},{1}" -f $blob,$file.remote_path)))
        }
        $newTree = Invoke-Git @('write-tree')
        $commit = Invoke-Git @('commit-tree',$newTree,'-p',$parent,'-m',$message)
        return $commit
    } finally {
        Remove-Item Env:GIT_INDEX_FILE -ErrorAction SilentlyContinue
        Remove-Item -LiteralPath $indexPath -Force -ErrorAction SilentlyContinue
    }
}

$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding utf8 | ConvertFrom-Json
if ($manifest.candidate_sha256 -ne '31fc783e6021a6f19ae2fa316a0b8bb28b0cf058508da46bcb312ea7787090fd') { throw 'Candidate manifest is not bound to expected DOCX SHA.' }
$items = [System.Collections.Generic.List[object]]::new()
foreach ($entry in $manifest.files) {
    $local = [string]$entry.local_path
    $relative = [string]$entry.remote_relative_path
    if (-not (Test-Path -LiteralPath $local -PathType Leaf)) { throw "Missing local file: $local" }
    $sha = (Get-FileHash -Algorithm SHA256 -LiteralPath $local).Hash.ToLower()
    $length = (Get-Item -LiteralPath $local).Length
    if ($sha -ne [string]$entry.sha256 -or $length -ne [int64]$entry.bytes) { throw "Package input changed after manifest: $local" }
    $items.Add([pscustomobject]@{ local_path=$local; remote_path="$prefix/$relative"; sha256=$sha; bytes=$length })
}
$items.Add([pscustomobject]@{ local_path=$manifestPath; remote_path="$prefix/evidence/github_package_manifest_R01.json"; sha256=(Get-FileHash -Algorithm SHA256 -LiteralPath $manifestPath).Hash.ToLower(); bytes=(Get-Item -LiteralPath $manifestPath).Length })

[void](Invoke-Git @('fetch','--no-tags','origin',$branch))
$head = Invoke-Git @('rev-parse','FETCH_HEAD')
if ($head -ne $expectedHead) { throw "Remote HEAD changed after verified preflight. expected=$expectedHead actual=$head; no push made." }
$existing = Invoke-Git @('ls-tree','-r','--name-only',$head,'--',$prefix)
if (-not [string]::IsNullOrWhiteSpace($existing)) { throw "Remote target prefix already exists; refusing overwrite: $($existing.Split("`n")[0])" }

$packageCommit = New-CommitWithFiles $head $items.ToArray() 'TTQS ONE add 0111 I18-E20 R01 candidate and QA evidence'
$push = & git -C $repo push origin ($packageCommit + ':refs/heads/' + $branch) 2>&1
if ($LASTEXITCODE -ne 0) { throw ("Non-forced push rejected; no retry performed. " + ($push -join "`n")) }
[void](Invoke-Git @('fetch','--no-tags','origin',$branch))
$afterPackageHead = Invoke-Git @('rev-parse','FETCH_HEAD')
[void](Invoke-Git @('merge-base','--is-ancestor',$packageCommit,$afterPackageHead))

$checks = [System.Collections.Generic.List[object]]::new()
foreach ($item in $items) {
    $remoteBlob = Invoke-Git @('rev-parse',("{0}:{1}" -f $afterPackageHead,$item.remote_path))
    $remote = Get-RawBlobEvidence $remoteBlob $item.remote_path
    if ($remote.sha256 -ne $item.sha256 -or $remote.bytes -ne $item.bytes) { throw "Raw-byte readback mismatch: $($item.remote_path)" }
    $checks.Add([pscustomobject]@{ path=$item.remote_path; local_sha256=$item.sha256; remote_raw_sha256=$remote.sha256; bytes=$item.bytes; match=$true })
}

$receipt = [ordered]@{
    project_id = 'TTQS_ONE'; doc_id = '0111'; requirement_id = 'I18-E20'
    source_branch = $branch; remote_head_before = $head; package_commit = $packageCommit
    remote_head_after_package = $afterPackageHead; package_file_count = $checks.Count
    candidate_sha256 = $manifest.candidate_sha256; package_manifest_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $manifestPath).Hash.ToLower()
    files = $checks; all_raw_bytes_match = $true; formal_acceptance = 'NOT_GRANTED'
    readback_time_local = (Get-Date).ToString('o')
}
[IO.File]::WriteAllText($readbackPath,($receipt | ConvertTo-Json -Depth 8),$encoding)
$receiptSha = (Get-FileHash -Algorithm SHA256 -LiteralPath $readbackPath).Hash.ToLower()
$receiptItem = [pscustomobject]@{ local_path=$readbackPath; remote_path="$prefix/evidence/github_raw_readback_receipt_R01.json"; sha256=$receiptSha; bytes=(Get-Item -LiteralPath $readbackPath).Length }
$receiptCommit = New-CommitWithFiles $afterPackageHead @($receiptItem) 'TTQS ONE record 0111 exact GitHub raw-byte readback'
$push2 = & git -C $repo push origin ($receiptCommit + ':refs/heads/' + $branch) 2>&1
if ($LASTEXITCODE -ne 0) { throw ("Readback receipt non-forced push rejected; no retry performed. " + ($push2 -join "`n")) }
[void](Invoke-Git @('fetch','--no-tags','origin',$branch))
$finalHead = Invoke-Git @('rev-parse','FETCH_HEAD')
[void](Invoke-Git @('merge-base','--is-ancestor',$receiptCommit,$finalHead))

$finalChecks = [System.Collections.Generic.List[object]]::new()
foreach ($item in $items) {
    $remoteBlob = Invoke-Git @('rev-parse',("{0}:{1}" -f $finalHead,$item.remote_path))
    $remote = Get-RawBlobEvidence $remoteBlob $item.remote_path
    if ($remote.sha256 -ne $item.sha256 -or $remote.bytes -ne $item.bytes) { throw "Final raw-byte readback mismatch: $($item.remote_path)" }
    $finalChecks.Add([pscustomobject]@{ path=$item.remote_path; sha256=$remote.sha256; bytes=$remote.bytes; match=$true })
}
$remoteReceiptBlob = Invoke-Git @('rev-parse',("{0}:{1}" -f $finalHead,$receiptItem.remote_path))
$remoteReceipt = Get-RawBlobEvidence $remoteReceiptBlob $receiptItem.remote_path
if ($remoteReceipt.sha256 -ne $receiptSha -or $remoteReceipt.bytes -ne $receiptItem.bytes) { throw 'Readback receipt itself failed final raw-byte verification.' }

$final = [ordered]@{
    project_id = 'TTQS_ONE'; doc_id = '0111'; candidate_sha256 = $manifest.candidate_sha256
    package_commit = $packageCommit; readback_receipt_commit = $receiptCommit; final_remote_head = $finalHead
    package_files_verified = $finalChecks.Count; readback_receipt_sha256 = $remoteReceipt.sha256
    all_package_raw_bytes_match = $true; readback_receipt_raw_bytes_match = $true
    final_verified_at_local = (Get-Date).ToString('o')
}
Write-Output ($final | ConvertTo-Json -Compress)
