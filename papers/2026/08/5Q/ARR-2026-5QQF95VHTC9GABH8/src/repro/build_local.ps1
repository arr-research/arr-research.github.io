[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $PSScriptRoot).Path
$build = Join-Path $root 'build'
$pdfOut = Join-Path $root 'output\pdf'
$paperPdf = Join-Path $build 'paper.pdf'
$finalPdf = Join-Path $pdfOut 'Sharp_Onset_Unbounded_Norm_Optimal_Selfcommutator_Rank.pdf'

New-Item -ItemType Directory -Force -Path $build, $pdfOut | Out-Null

Push-Location $root
try {
    & pdflatex -interaction=nonstopmode -halt-on-error "-output-directory=$build" 'paper.tex'
    if ($LASTEXITCODE -ne 0) { throw "First pdflatex pass failed: $LASTEXITCODE" }
    & bibtex (Join-Path $build 'paper')
    if ($LASTEXITCODE -ne 0) { throw "BibTeX failed: $LASTEXITCODE" }
    & pdflatex -interaction=nonstopmode -halt-on-error "-output-directory=$build" 'paper.tex'
    if ($LASTEXITCODE -ne 0) { throw "Second pdflatex pass failed: $LASTEXITCODE" }
    & pdflatex -interaction=nonstopmode -halt-on-error "-output-directory=$build" 'paper.tex'
    if ($LASTEXITCODE -ne 0) { throw "Final pdflatex pass failed: $LASTEXITCODE" }
} finally {
    Pop-Location
}

$bad = Select-String -LiteralPath (Join-Path $build 'paper.log') -Pattern @(
    'LaTeX Warning:',
    'Package .* Warning:',
    'Overfull',
    'Underfull',
    'Missing character:',
    'undefined references',
    'multiply defined'
)
if ($bad) {
    $bad | ForEach-Object { Write-Error $_.Line }
    throw 'LaTeX log contains warnings.'
}

$bibBad = Select-String -LiteralPath (Join-Path $build 'paper.blg') -Pattern @('Warning--','error message')
if ($bibBad) {
    $bibBad | ForEach-Object { Write-Error $_.Line }
    throw 'BibTeX log contains warnings.'
}

Copy-Item -LiteralPath $paperPdf -Destination $finalPdf -Force
& pdftotext -layout $finalPdf (Join-Path $pdfOut 'paper.txt')
if ($LASTEXITCODE -ne 0) { throw "pdftotext failed: $LASTEXITCODE" }

$hash = (Get-FileHash -LiteralPath $finalPdf -Algorithm SHA256).Hash
$size = (Get-Item -LiteralPath $finalPdf).Length
$pages = (& pdfinfo $finalPdf | Select-String '^Pages:\s+(\d+)$').Matches.Groups[1].Value
Write-Host "PASS: $pages pages, $size bytes, SHA256 $hash"
