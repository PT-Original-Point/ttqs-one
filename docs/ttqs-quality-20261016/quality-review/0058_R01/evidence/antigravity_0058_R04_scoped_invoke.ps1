$ErrorActionPreference = 'Stop'
$AgExe = 'C:\Users\J\AppData\Local\agy\bin\agy.exe'
$SettingsPath = 'C:\Users\J\.gemini\antigravity-cli\settings.json'
$SettingsBackupPath = 'C:\Users\J\.gemini\antigravity-cli\settings.json.ttqs-one-0058-r04.bak'
$PackageRoot = 'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\quality-review\0058_R01'
$WorkerRoot = Join-Path $PackageRoot 'worker\antigravity'
$PromptPath = Join-Path $PackageRoot 'inputs\0058_ANTIGRAVITY_REPAIR_PROMPT_R03.md'
$ReceiptRoot = Join-Path $PackageRoot 'evidence\antigravity_0058_R04'
$Model = 'gemini-3.8-flash-high'
$ConversationId = '8f678926-388c-4322-8cf7-df548f38f60c'
$ReadFiles = @(
    $PromptPath,
    'E:\TTQS\_TTQS_ONE_REVIEW_SYNC_0036_R08_20261016\docs\ttqs-quality-20261016\01_HUMAN_MISSION_AND_ACCEPTANCE.md',
    (Join-Path $WorkerRoot '0058_UNIQUE_BLUEPRINT_R02.md'),
    (Join-Path $WorkerRoot '0058_CONTENT_R02.json'),
    (Join-Path $WorkerRoot '0058_SYNTHETIC_REPLACEMENT_REGISTER_R02.csv'),
    (Join-Path $WorkerRoot '0058_build_R02.py')
)
$WriteFiles = @(
    (Join-Path $WorkerRoot '0058_UNIQUE_BLUEPRINT_R03.md'),
    (Join-Path $WorkerRoot '0058_CONTENT_R03.json'),
    (Join-Path $WorkerRoot '0058_SYNTHETIC_REPLACEMENT_REGISTER_R03.csv'),
    (Join-Path $WorkerRoot '0058_build_R03.py')
)
New-Item -ItemType Directory -Force -Path $ReceiptRoot | Out-Null
$StdoutPath = Join-Path $ReceiptRoot 'stdout.json'
$StderrPath = Join-Path $ReceiptRoot 'stderr.txt'
$ExitPath = Join-Path $ReceiptRoot 'exit_code.txt'
$MetaPath = Join-Path $ReceiptRoot 'execution.json'
$PromptText = [System.IO.File]::ReadAllText($PromptPath, [System.Text.Encoding]::UTF8)
$OriginalSettings = [System.IO.File]::ReadAllBytes($SettingsPath)
$OriginalSettingsSha = [Convert]::ToHexString([System.Security.Cryptography.SHA256]::HashData($OriginalSettings))
if (Test-Path -LiteralPath $SettingsBackupPath) { throw "Refusing to overwrite existing settings backup: $SettingsBackupPath" }
[System.IO.File]::WriteAllBytes($SettingsBackupPath, $OriginalSettings)
$Start = [DateTimeOffset]::Now
$ExitCode = $null
try {
    $Settings = [System.Text.Encoding]::UTF8.GetString($OriginalSettings) | ConvertFrom-Json -AsHashtable
    $Allow = @($Settings.permissions.allow)
    foreach ($Path in $ReadFiles) { $Allow += "read_file($($Path.Replace('\','/')))" }
    foreach ($Path in $WriteFiles) { $Allow += "write_file($($Path.Replace('\','/')))" }
    $Settings.permissions.allow = @($Allow | Select-Object -Unique)
    $TempSettings = [System.Text.Encoding]::UTF8.GetBytes(($Settings | ConvertTo-Json -Depth 20))
    [System.IO.File]::WriteAllBytes($SettingsPath, $TempSettings)
    $Args = @('--conversation', $ConversationId, '--model', $Model, '--effort', 'high', '--mode', 'auto', '--sandbox', '--disable-slash-commands', '--print-timeout', '0', '--output-format', 'json', '--print', $PromptText)
    & $AgExe @Args 1> $StdoutPath 2> $StderrPath
    $ExitCode = $LASTEXITCODE
    [System.IO.File]::WriteAllText($ExitPath, [string]$ExitCode + "`n", [System.Text.Encoding]::UTF8)
}
finally {
    [System.IO.File]::WriteAllBytes($SettingsPath, $OriginalSettings)
    $RestoredBytes = [System.IO.File]::ReadAllBytes($SettingsPath)
    $RestoredSha = [Convert]::ToHexString([System.Security.Cryptography.SHA256]::HashData($RestoredBytes))
    $End = [DateTimeOffset]::Now
    $Meta = [ordered]@{
        model_requested = $Model
        conversation_id = $ConversationId
        computer_use = 'forbidden_not_used'
        permission_bypass = 'not_used'
        cli = $AgExe
        invocation_mode = 'auto_sandbox_scoped_file_permissions'
        start_local = $Start.ToString('o')
        end_local = $End.ToString('o')
        elapsed_seconds = [Math]::Round(($End - $Start).TotalSeconds, 3)
        exit_code = $ExitCode
        settings_sha256_before = $OriginalSettingsSha
        settings_sha256_after_restore = $RestoredSha
        settings_restored_match = ($OriginalSettingsSha -eq $RestoredSha)
        temporary_read_file_paths = $ReadFiles
        temporary_write_file_paths = $WriteFiles
        raw_stdout = $StdoutPath
        raw_stderr = $StderrPath
        exit_receipt = $ExitPath
    }
    [System.IO.File]::WriteAllText($MetaPath, ($Meta | ConvertTo-Json -Depth 10), [System.Text.Encoding]::UTF8)
}
if (-not $Meta.settings_restored_match) { throw 'Antigravity settings restore hash mismatch.' }
Write-Output "EXIT_CODE=$ExitCode"
Write-Output "MODEL=$Model"
Write-Output "CONVERSATION_ID=$ConversationId"
Write-Output "SETTINGS_RESTORED_SHA256=$($Meta.settings_sha256_after_restore)"
Write-Output "RECEIPT_ROOT=$ReceiptRoot"
