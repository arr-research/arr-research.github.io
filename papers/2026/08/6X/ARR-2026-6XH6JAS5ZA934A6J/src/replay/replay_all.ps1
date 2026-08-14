$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $here 'verify_coherent_orbit_rdf.py')
python (Join-Path $here 'verify_slater_cartan_series.py')
Write-Output 'ARR coherent-orbit replay: PASS'
