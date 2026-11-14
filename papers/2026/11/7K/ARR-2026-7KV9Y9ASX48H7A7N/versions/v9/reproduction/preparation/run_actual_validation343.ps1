param([Parameter(Mandatory=$true)][ValidatePattern('^[a-f0-9]{64}$')][string]$ExpectedBundleSha256,[Parameter(Mandatory=$true)][ValidatePattern('^[a-f0-9]{64}$')][string]$ExpectedScriptSha256)
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$helper=Join-Path $PSScriptRoot 'capture_cli_atomic.ps1'
if((Get-FileHash -LiteralPath $helper).Hash.ToLowerInvariant() -cne '4fe3fc65796ee55dc5db5bc52c924b5401b72699f56eac8dc73ceb2c53da2b7b'){throw 'Helper drift'}
. $helper
$e='D:\Datos\the-eriksson-programme\autonomia\evidencia-343'
$bundle=Join-Path $e 'actual-return-inputs343.zip'
$script=Join-Path $PSScriptRoot 'validate343_actual_colab.py'
if((Get-FileHash -LiteralPath $bundle).Hash.ToLowerInvariant() -cne $ExpectedBundleSha256 -or (Get-FileHash -LiteralPath $script).Hash.ToLowerInvariant() -cne $ExpectedScriptSha256){throw 'Actual input/script pin mismatch'}
$out=Join-Path $e 'actual-return-validation-attempt-a'
if(Test-Path -LiteralPath $out){throw 'Preserve prior validation attempt'}
New-Item -ItemType Directory -Path $out|Out-Null
$prefix='export GOOGLE_APPLICATION_CREDENTIALS=/mnt/c/Users/lluis/AppData/Roaming/gcloud/application_default_credentials.json; exec /home/lluis/.local/bin/colab --auth adc --config /home/lluis/.config/colab-cli/tep343-actual-return-a-sessions.json'
$session='tep343-actual-return-a-own-cpu'
$exits=[ordered]@{};$failure=$null;$attempted=$false
[IO.File]::WriteAllText((Join-Path $out 'runtime-open-requested.txt'),[DateTime]::UtcNow.ToString('o')+"`n")
try{
 $attempted=$true
 $exits.allocation=Invoke-CapturedWsl -Name 'allocation' -ShellCommand ($prefix+' new -s '+$session+' --high-mem') -OutputDirectory $out
 if($exits.allocation -ne 0){throw 'Allocation failed'}
 $exits.upload=Invoke-CapturedWsl -Name 'upload' -ShellCommand ($prefix+' upload -s '+$session+' /mnt/d/Datos/the-eriksson-programme/autonomia/evidencia-343/actual-return-inputs343.zip /content/tep343-actual-return-inputs.zip') -OutputDirectory $out
 if($exits.upload -ne 0){throw 'Upload failed'}
 $exits.execution=Invoke-CapturedWsl -Name 'execution' -ShellCommand ($prefix+' exec -s '+$session+' -f /mnt/c/Trabajo/the-eriksson-programme/prefix-rank290-20261113/_tmp/production343-a/validate343_actual_colab.py --timeout 180') -OutputDirectory $out
}catch{$failure=$_.Exception.ToString()}
finally{
 if($attempted){try{$exits.release=Invoke-CapturedWsl -Name 'release' -ShellCommand ($prefix+' stop -s '+$session) -OutputDirectory $out}catch{$failure=[string]$failure+' STOP_CAPTURE: '+$_.Exception.ToString()}}
 [IO.File]::WriteAllText((Join-Path $out 'runtime-release-finished.txt'),[DateTime]::UtcNow.ToString('o')+"`n")
 [ordered]@{actual_cli_exits=$exits;failure=$failure;input_bundle_sha256=$ExpectedBundleSha256;script_sha256=$ExpectedScriptSha256;scope='Actual remote raw validation transport; requires full logs, exact bundle/result binding and separate backend inspection'}|ConvertTo-Json -Depth 8|Set-Content -LiteralPath (Join-Path $out 'outer-report.json') -Encoding utf8NoBOM
}
if($attempted){$query=Invoke-CapturedWsl -Name 'backend-readback' -ShellCommand ($prefix+' sessions') -OutputDirectory $out;if($query -ne 0){throw 'Actual backend readback failed'}}
if($null -ne $failure -or $exits.Count -ne 4 -or @($exits.Values|Where-Object{$_ -ne 0}).Count -ne 0){throw 'Actual validation lifecycle failed; preserve'}
$exits|ConvertTo-Json
