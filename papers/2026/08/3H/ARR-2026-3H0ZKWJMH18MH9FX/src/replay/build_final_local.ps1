$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$paperRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$paperSourceDir = Join-Path $paperRoot "paper"
$paperBuildDir = Join-Path $paperRoot "output\build"
New-Item -ItemType Directory -Force -Path $paperBuildDir | Out-Null

$pdflatexCommand = Get-Command pdflatex -ErrorAction SilentlyContinue
$bibtexCommand = Get-Command bibtex -ErrorAction SilentlyContinue
if (-not $pdflatexCommand -or -not $bibtexCommand) {
    $miktexBin = Join-Path $env:LOCALAPPDATA "Programs\MiKTeX\miktex\bin\x64"
    $pdflatexPath = Join-Path $miktexBin "pdflatex.exe"
    $bibtexPath = Join-Path $miktexBin "bibtex.exe"
    if (-not (Test-Path -LiteralPath $pdflatexPath) -or
        -not (Test-Path -LiteralPath $bibtexPath)) {
        throw "MiKTeX pdflatex/bibtex not found. Install MiKTeX or add it to PATH."
    }
} else {
    $pdflatexPath = $pdflatexCommand.Source
    $bibtexPath = $bibtexCommand.Source
}

$pythonCandidates = @()
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCommand) { $pythonCandidates += $pythonCommand.Source }
$pythonCandidates += Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$pythonPath = $null
foreach ($candidate in $pythonCandidates | Select-Object -Unique) {
    if (-not (Test-Path -LiteralPath $candidate)) { continue }
    & $candidate -c "import numpy, pypdf"
    if ($LASTEXITCODE -eq 0) {
        $pythonPath = $candidate
        break
    }
}
if (-not $pythonPath) {
    throw "Python with NumPy and pypdf not found. Install requirements.txt first."
}

Push-Location $paperSourceDir
try {
    & $pdflatexPath --output-directory=../output/build --interaction=nonstopmode --halt-on-error exterior_list_decoders.tex
    if ($LASTEXITCODE -ne 0) { throw "First pdflatex pass failed." }

    $env:BIBINPUTS = ".;$paperSourceDir"
    & $bibtexPath ../output/build/exterior_list_decoders
    if ($LASTEXITCODE -ne 0) { throw "BibTeX pass failed." }

    & $pdflatexPath --output-directory=../output/build --interaction=nonstopmode --halt-on-error exterior_list_decoders.tex
    if ($LASTEXITCODE -ne 0) { throw "Second pdflatex pass failed." }
    & $pdflatexPath --output-directory=../output/build --interaction=nonstopmode --halt-on-error exterior_list_decoders.tex
    if ($LASTEXITCODE -ne 0) { throw "Final pdflatex pass failed." }
} finally {
    Pop-Location
}

Push-Location $paperRoot
try {
    & $pythonPath verify_full_spark_list_threshold.py --check results/full_spark_list_threshold_certificate.json
    if ($LASTEXITCODE -ne 0) { throw "Scientific replay failed." }
    & $pythonPath package_release.py
    if ($LASTEXITCODE -ne 0) { throw "Release build failed." }
    & $pythonPath package_release.py --check
    if ($LASTEXITCODE -ne 0) { throw "Release verification failed." }
} finally {
    Pop-Location
}

Write-Output "PASS: final PDF and deterministic release rebuilt and verified."
