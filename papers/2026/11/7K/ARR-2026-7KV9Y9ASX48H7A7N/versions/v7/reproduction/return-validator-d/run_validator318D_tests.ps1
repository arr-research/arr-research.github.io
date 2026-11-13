$ErrorActionPreference='Stop'
Set-StrictMode -Version Latest
$helper=Join-Path $PSScriptRoot 'production318-b\capture_cli_atomic.ps1'
if((Get-FileHash -LiteralPath $helper).Hash.ToLowerInvariant() -cne '4fe3fc65796ee55dc5db5bc52c924b5401b72699f56eac8dc73ceb2c53da2b7b'){throw 'Capture helper drift'}
. $helper
$script=Join-Path $PSScriptRoot 'run_validator318D_tests_colab.py'
if((Get-FileHash -LiteralPath $script).Hash.ToLowerInvariant() -cne 'e38553fe1a90551861e3f878f7fe3bd5ade87ebe00a15da37518ad8295e1a447'){throw 'Frozen harness drift'}
$out='D:\Datos\the-eriksson-programme\autonomia\evidencia-318\return-validator-d\test-attempt-a'
if(Test-Path -LiteralPath $out){throw 'Preserve prior test attempt'}
New-Item -ItemType Directory -Path $out|Out-Null
$prefix='export GOOGLE_APPLICATION_CREDENTIALS=/mnt/c/Users/lluis/AppData/Roaming/gcloud/application_default_credentials.json; exec /home/lluis/.local/bin/colab --auth adc --config /home/lluis/.config/colab-cli/tep318-validator-d-tests-sessions.json'
$session='tep318-validator-d-tests-own-cpu'
$exits=[ordered]@{};$failure=$null;$attempted=$false
[IO.File]::WriteAllText((Join-Path $out 'runtime-open-requested.txt'),[DateTime]::UtcNow.ToString('o')+"`n")
try{
 $attempted=$true
 $exits.allocation=Invoke-CapturedWsl -Name 'allocation' -ShellCommand ($prefix+' new -s '+$session+' --high-mem') -OutputDirectory $out
 if($exits.allocation -ne 0){throw 'Allocation failed'}
 $exits.execution=Invoke-CapturedWsl -Name 'execution' -ShellCommand ($prefix+' exec -s '+$session+' -f /mnt/c/Trabajo/the-eriksson-programme/prefix-rank290-20261113/_tmp/run_validator318D_tests_colab.py --timeout 180') -OutputDirectory $out
 $exits.download=Invoke-CapturedWsl -Name 'download' -ShellCommand ($prefix+' download -s '+$session+' /content/tep318-validator-d-tests.zip /mnt/d/Datos/the-eriksson-programme/autonomia/evidencia-318/return-validator-d/test-attempt-a/tep318-validator-d-tests.zip') -OutputDirectory $out
}catch{$failure=$_.Exception.ToString()}
finally{
 if($attempted){$exits.release=Invoke-CapturedWsl -Name 'release' -ShellCommand ($prefix+' stop -s '+$session) -OutputDirectory $out}
 [IO.File]::WriteAllText((Join-Path $out 'runtime-release-finished.txt'),[DateTime]::UtcNow.ToString('o')+"`n")
 [ordered]@{actual_cli_exits=$exits;failure=$failure;scope='Actual test transport only, requires raw child logs and separate backend readback'}|ConvertTo-Json -Depth 8|Set-Content -LiteralPath (Join-Path $out 'outer-report.json') -Encoding utf8NoBOM
}
if($null -ne $failure -or $exits.Count -ne 4 -or @($exits.Values|Where-Object{$_ -ne 0}).Count -ne 0){throw 'Actual test lifecycle failed; preserve'}
$readback=Invoke-CapturedWsl -Name 'backend-readback' -ShellCommand ($prefix+' sessions') -OutputDirectory $out
if($readback -ne 0){throw 'Actual backend query failed'}
$exits|ConvertTo-Json
