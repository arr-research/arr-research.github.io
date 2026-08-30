[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$build = Join-Path $root 'build'
$log = Join-Path $build 'scientific_replay.log'
New-Item -ItemType Directory -Force -Path $build | Out-Null

& python (Join-Path $root 'run_replay.py') 2>&1 | Tee-Object -FilePath $log
if ($LASTEXITCODE -ne 0) {
    throw "Scientific replay failed: $LASTEXITCODE"
}

if (-not (Select-String -LiteralPath $log -SimpleMatch 'PASS: both independent exact replay routes completed.')) {
    throw 'Replay completion marker missing.'
}
