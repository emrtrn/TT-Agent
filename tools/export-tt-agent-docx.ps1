[CmdletBinding(DefaultParameterSetName = 'File')]
param(
  [Parameter(Mandatory = $true, Position = 0, ParameterSetName = 'File')]
  [string]$InputPath,
  [Parameter(Mandatory = $true, ParameterSetName = 'Unit')]
  [string]$Unit,
  [Parameter(Mandatory = $true, ParameterSetName = 'All')]
  [switch]$All,
  [ValidateSet('7', '8')]
  [string]$Grade = '8',
  [string]$OutputRoot
)

$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$projectRoot = Split-Path -Parent $PSScriptRoot
$python = Get-Command python -ErrorAction Stop
$exporter = Join-Path $PSScriptRoot 'export-tt-agent-docx.py'
if (-not $OutputRoot) { $OutputRoot = Join-Path $projectRoot 'docs/docx' }
$pythonArgs = @($exporter, '--grade', $Grade, '--output-root', $OutputRoot)
switch ($PSCmdlet.ParameterSetName) {
  'File' { $pythonArgs += (Resolve-Path -LiteralPath $InputPath).Path }
  'Unit' { $pythonArgs += @('--unit', $Unit) }
  'All' { $pythonArgs += '--all' }
}
Push-Location $projectRoot
try {
  & $python.Source @pythonArgs
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
finally { Pop-Location }
