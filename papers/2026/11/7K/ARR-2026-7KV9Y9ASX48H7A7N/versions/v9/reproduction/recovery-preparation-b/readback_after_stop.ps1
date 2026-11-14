Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$helper=Join-Path $PSScriptRoot 'capture_cli_atomic.ps1'
if((Get-FileHash -LiteralPath $helper).Hash.ToLowerInvariant() -cne '4fe3fc65796ee55dc5db5bc52c924b5401b72699f56eac8dc73ceb2c53da2b7b'){throw 'Capture helper drift'}
. $helper
$out='D:\Datos\the-eriksson-programme\autonomia\evidencia-343\production-a\attempt-b'
if(-not(Test-Path -LiteralPath (Join-Path $out 'runtime-open-requested.txt'))){throw 'No recorded B allocation request; inspect ownership before query'}
$command='export GOOGLE_APPLICATION_CREDENTIALS=/mnt/c/Users/lluis/AppData/Roaming/gcloud/application_default_credentials.json; exec /usr/bin/timeout --signal=TERM --kill-after=15s 180s /home/lluis/.local/bin/colab --auth adc --config /home/lluis/.config/colab-cli/tep343-build-b-sessions.json sessions'
# Optional recovery-only query; never overwrite the wrapper's backend-readback logs.
$code=Invoke-CapturedWsl -Name 'backend-readback-recovery' -ShellCommand $command -OutputDirectory $out
if($code -ne 0){throw 'Recovery backend query nonzero; actual stop/readback still requires operator action'}
Get-Content -LiteralPath (Join-Path $out 'backend-readback-recovery.log')
Get-Content -LiteralPath (Join-Path $out 'backend-readback-recovery.stderr.log')
# Query zero alone never proves inactivity. No stop/allocation/retry is performed here.
