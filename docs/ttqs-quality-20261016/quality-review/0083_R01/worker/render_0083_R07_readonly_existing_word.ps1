$ErrorActionPreference = 'Stop'
$base = Join-Path $PSScriptRoot '..'
$docx = [IO.Path]::GetFullPath((Join-Path $base 'candidate/0083_R07.docx'))
$out = [IO.Path]::GetFullPath((Join-Path $base 'evidence/render_R07_final'))
New-Item -ItemType Directory -Force -Path $out | Out-Null
$pdf = Join-Path $out '0083_R07.pdf'
$statusPath = Join-Path $out 'render_status.json'
$sw = [Diagnostics.Stopwatch]::StartNew()
$word = $null
$doc = $null
$status = [ordered]@{
  engine = 'Microsoft Word COM'
  word_instance = 'reused existing ROT instance; not created'
  open_mode = 'ReadOnly; no DOCX save'
  docx = $docx
  pdf = $pdf
  opened = $false
  fields_updated_in_memory = $false
  saved = $false
  exported = $false
  closed = $false
  candidate_sha_before = (Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
  exit_code = 1
}
try {
  $native = @'
using System;
using System.Runtime.InteropServices;
public static class RotProbe0083 {
  [DllImport("oleaut32.dll", PreserveSig=true)]
  public static extern int GetActiveObject(ref Guid rclsid, IntPtr pvReserved, out IntPtr ppunk);
}
'@
  if (-not ('RotProbe0083' -as [type])) { Add-Type -TypeDefinition $native }
  $clsid = (Get-ItemProperty -LiteralPath 'Registry::HKEY_CLASSES_ROOT\Word.Application\CLSID').'(default)'
  $guid = [guid]$clsid
  [IntPtr]$punk = [IntPtr]::Zero
  $hr = [RotProbe0083]::GetActiveObject([ref]$guid, [IntPtr]::Zero, [ref]$punk)
  if ($hr -ne 0) { throw "No existing Word ROT instance; HRESULT=$hr" }
  $word = [Runtime.InteropServices.Marshal]::GetObjectForIUnknown($punk)
  if ($word.Documents.Count -ne 0) { throw "Existing Word instance has $($word.Documents.Count) open document(s); render deferred to avoid interference." }
  $word.Visible = $false
  $word.DisplayAlerts = 0
  $word.AutomationSecurity = 3
  $doc = $word.Documents.Open($docx, $false, $true, $false)
  $status.opened = $true
  [void]$doc.Fields.Update()
  if ($doc.TablesOfContents.Count -gt 0) { [void]$doc.TablesOfContents.Item(1).Update() }
  $status.fields_updated_in_memory = $true
  $doc.Repaginate()
  $status.pages = [int]$doc.ComputeStatistics(2)
  $doc.ExportAsFixedFormat($pdf, 17)
  $status.exported = Test-Path -LiteralPath $pdf
  $doc.Close(0)
  $status.closed = $true
  $status.exit_code = 0
} catch {
  $status.error = $_.Exception.ToString()
} finally {
  if ($doc) { try { $doc.Close(0) } catch {} }
  # Borrowed existing idle Word instance is left running; no process is created or stopped.
  if ($doc) { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc) }
  if ($word) { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) }
  [GC]::Collect()
  [GC]::WaitForPendingFinalizers()
  $status.candidate_sha_after = (Get-FileHash -LiteralPath $docx -Algorithm SHA256).Hash.ToLowerInvariant()
  $status.candidate_sha_unchanged = ($status.candidate_sha_before -eq $status.candidate_sha_after)
  $sw.Stop()
  $status.elapsed_seconds = [math]::Round($sw.Elapsed.TotalSeconds, 2)
  $status.finished_at = (Get-Date).ToString('o')
  $status | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $statusPath -Encoding utf8
}
Get-Content -LiteralPath $statusPath -Raw -Encoding utf8
if ($status.exit_code -ne 0 -or -not $status.candidate_sha_unchanged) { exit 1 }
