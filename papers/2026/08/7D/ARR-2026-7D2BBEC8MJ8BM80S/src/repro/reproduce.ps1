$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$bundle = Join-Path $scriptRoot 'lean-2d-yang-mills.bundle'
$buildRoot = Join-Path $scriptRoot '_build'
$mainRoot = Join-Path $buildRoot 'main'
$diskRoot = Join-Path $buildRoot 'disk'
$mainCommit = '05c4ec316cb9aa295416670a2578b1c2e77e1c36'
$diskCommit = '6dbb8cebc18ab2d65b6ae24af5216347c476df3f'

if (-not (Test-Path -LiteralPath $bundle)) {
  throw "Missing bundled Git history: $bundle"
}
if (Test-Path -LiteralPath $buildRoot) {
  throw "Refusing to overwrite existing build directory: $buildRoot"
}

python -m pip install -r (Join-Path $scriptRoot 'requirements.txt')
if ($LASTEXITCODE -ne 0) { throw 'Python dependency installation failed' }
python (Join-Path $scriptRoot 'replay.py')
if ($LASTEXITCODE -ne 0) { throw 'Numerical replay failed' }

New-Item -ItemType Directory -Path $buildRoot | Out-Null
git init $mainRoot
if ($LASTEXITCODE -ne 0) { throw 'git init failed for main checkout' }
git -C $mainRoot fetch $bundle refs/remotes/origin/main
if ($LASTEXITCODE -ne 0) { throw 'git fetch failed for main checkout' }
git -C $mainRoot checkout --detach FETCH_HEAD
if ($LASTEXITCODE -ne 0) { throw 'git checkout failed for main commit' }
if ((git -C $mainRoot rev-parse HEAD).Trim() -ne $mainCommit) {
  throw 'Bundled main commit does not match the pinned hash'
}
Copy-Item -LiteralPath (Join-Path $scriptRoot 'SU2ClassTransferGap.lean') `
  -Destination (Join-Path $mainRoot 'Lean2dYangMills\SU2ClassTransferGap.lean')
Copy-Item -LiteralPath (Join-Path $scriptRoot 'AuditClassTransferGap.lean') `
  -Destination (Join-Path $mainRoot 'AuditClassTransferGap.lean')
Push-Location $mainRoot
lake exe cache get
if ($LASTEXITCODE -ne 0) { throw 'Mathlib cache retrieval failed' }
lake build Lean2dYangMills.SU2ClassTransferGap
if ($LASTEXITCODE -ne 0) { throw 'Gap module build failed' }
lake env lean '.\AuditClassTransferGap.lean'
if ($LASTEXITCODE -ne 0) { throw 'Axiom audit failed' }
Pop-Location

git init $diskRoot
if ($LASTEXITCODE -ne 0) { throw 'git init failed for disk checkout' }
git -C $diskRoot fetch $bundle refs/remotes/origin/agent/su2-boundary-conditioned-bridge
if ($LASTEXITCODE -ne 0) { throw 'git fetch failed for disk checkout' }
git -C $diskRoot checkout --detach FETCH_HEAD
if ($LASTEXITCODE -ne 0) { throw 'git checkout failed for disk commit' }
if ((git -C $diskRoot rev-parse HEAD).Trim() -ne $diskCommit) {
  throw 'Bundled disk commit does not match the pinned hash'
}
Push-Location $diskRoot
lake exe cache get
if ($LASTEXITCODE -ne 0) { throw 'Disk checkout cache retrieval failed' }
lake build Lean2dYangMills
if ($LASTEXITCODE -ne 0) { throw 'Disk endpoint build failed' }
Pop-Location

Write-Output 'FULL REPRODUCTION: PASS'
