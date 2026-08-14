$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $here "verify_semiclassical_frontier.py")
python (Join-Path $here "verify_semiclassical_coherent_rdf.py")
