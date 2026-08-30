[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$build = Join-Path $root 'build'
New-Item -ItemType Directory -Force -Path $build | Out-Null

$frontierLog = Join-Path $build 'rank_gap_frontier_replay.json'
& python (Join-Path $root 'verify_rank_gap_frontier.py') 2>&1 |
    Tee-Object -FilePath $frontierLog -Encoding utf8
if ($LASTEXITCODE -ne 0) { throw "Frontier replay failed: $LASTEXITCODE" }
if (-not (Select-String -LiteralPath $frontierLog -SimpleMatch '"status": "PASS"')) {
    throw 'Frontier PASS marker missing.'
}

$independentLog = Join-Path $build 'independent_d8_replay.log'
& python (Join-Path $root 'run_parametric_family_replay.py') 2>&1 |
    Tee-Object -FilePath $independentLog -Encoding utf8
if ($LASTEXITCODE -ne 0) { throw "Independent replay failed: $LASTEXITCODE" }
if (-not (Select-String -LiteralPath $independentLog -SimpleMatch 'PASS: recursive-Horn and direct-LR routes agree')) {
    throw 'Independent replay completion marker missing.'
}

Write-Host 'PASS: complete Paper 30 scientific replay.'

