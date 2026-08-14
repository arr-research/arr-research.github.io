$ErrorActionPreference = 'Stop'

$replayRoot = $PSScriptRoot
Set-Location $replayRoot

$commands = @(
    'verify_radial_phase_coefficients.py',
    'verify_global_phase.py',
    'verify_contact_asymptotics.py',
    'make_complete_phase_figure.py'
)

foreach ($scriptPath in $commands) {
    Write-Host "RUN $scriptPath"
    & python $scriptPath
    if ($LASTEXITCODE -ne 0) {
        throw "Replay failed: $scriptPath"
    }
}

$manifestPath = Join-Path $replayRoot 'REPLAY_ARTIFACTS.sha256'
foreach ($line in Get-Content -LiteralPath $manifestPath) {
    if ($line -notmatch '^([0-9a-f]{64})  (.+)$') {
        throw "Malformed manifest line: $line"
    }
    $expected = $matches[1]
    $artifact = Join-Path $replayRoot $matches[2]
    $actual = (Get-FileHash -LiteralPath $artifact -Algorithm SHA256).Hash.ToLower()
    if ($actual -ne $expected) {
        throw "Hash mismatch: $artifact"
    }
}

Write-Host 'PASS: all bounded replays and artifact hashes verified.'
