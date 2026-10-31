$ErrorActionPreference = 'Stop'
$base = Join-Path $PSScriptRoot '..'
$docx = [IO.Path]::GetFullPath((Join-Path $base 'candidate/0084_R11.docx'))
$out = [IO.Path]::GetFullPath((Join-Path $base 'evidence/render_R11_final'))
New-Item -ItemType Directory -Force -Path $out | Out-Null
$pdf = Join-Path $out '0084_R11.pdf'
$statusPath = Join-Path $out 'render_status.json'
$sw = [Diagnostics.Stopwatch]::StartNew()
$word = $null
$doc = $null
$status = [ordered]@{
  engine = 'Microsoft Word COM'
  word_instance = 'reused existing ROT instance; not created'
  docx = $docx
  pdf = $pdf
  opened = $false
  fields_updated = $false
  saved = $false
  exported = $false
  closed = $false
  exit_code = 1
}
try {
  $native = @'
using System;
using System.Runtime.InteropServices;
public static class RotProbe {
  [DllImport("oleaut32.dll", PreserveSig=true)]
  public static extern int GetActiveObject(ref Guid rclsid, IntPtr pvReserved, out IntPtr ppunk);
}
'@
  if (-not ('RotProbe' -as [type])) { Add-Type -TypeDefinition $native }
  $clsid = (Get-ItemProperty -LiteralPath 'Registry::HKEY_CLASSES_ROOT\Word.Application\CLSID').'(default)'
  $guid = [guid]$clsid
  [IntPtr]$punk = [IntPtr]::Zero
  $hr = [RotProbe]::GetActiveObject([ref]$guid, [IntPtr]::Zero, [ref]$punk)
  if ($hr -ne 0) { throw "No existing Word ROT instance; HRESULT=$hr" }
  $word = [Runtime.InteropServices.Marshal]::GetObjectForIUnknown($punk)
  if ($word.Documents.Count -ne 0) { throw "Existing Word instance has $($word.Documents.Count) open document(s); render deferred to avoid interference." }
  $word.Visible = $false
  $word.DisplayAlerts = 0
  $word.AutomationSecurity = 3
  $doc = $word.Documents.Open($docx, $false, $false, $false)
  $status.opened = $true
  [void]$doc.Fields.Update()
  if ($doc.TablesOfContents.Count -gt 0) { [void]$doc.TablesOfContents.Item(1).Update() }
  $status.fields_updated = $true
  $doc.Repaginate()
  $status.pages = [int]$doc.ComputeStatistics(2)
  $doc.Save()
  $status.saved = $true
  $doc.ExportAsFixedFormat($pdf, 17)
  $status.exported = Test-Path -LiteralPath $pdf
  $doc.Close(0)
  $status.closed = $true
  $status.exit_code = 0
} catch {
  $status.error = $_.Exception.ToString()
} finally {
  if ($doc) { try { $doc.Close(0) } catch {} }
  # This script borrowed an existing idle Word COM instance; leave its process alive.
  if ($doc) { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($doc) }
  if ($word) { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($word) }
  [GC]::Collect()
  [GC]::WaitForPendingFinalizers()
  $sw.Stop()
  $status.elapsed_seconds = [math]::Round($sw.Elapsed.TotalSeconds, 2)
  $status.finished_at = (Get-Date).ToString('o')
  $status | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $statusPath -Encoding utf8
}
Get-Content -LiteralPath $statusPath -Raw
if ($status.exit_code -ne 0) { exit 1 }

