param([Parameter(Mandatory=$true)][ValidatePattern('^[a-f0-9]{64}$')][string]$ApprovedManifestSha256)
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$source='f4d66763d3fe3eccfc9e5eafba37d17dbe519f6b'
. (Join-Path $PSScriptRoot 'capture_cli_atomic.ps1')
$manifest=Join-Path $PSScriptRoot 'RUNNER-HASHES.json'
if((Get-FileHash -LiteralPath $manifest).Hash.ToLowerInvariant() -cne $ApprovedManifestSha256){throw 'Parent exact runner gate pin required'}
foreach($entry in (Get-Content -LiteralPath $manifest -Raw|ConvertFrom-Json)){
 $file=Join-Path $PSScriptRoot $entry.path
 if((Get-Item -LiteralPath $file).Length -ne $entry.bytes -or (Get-FileHash -LiteralPath $file).Hash.ToLowerInvariant() -cne $entry.sha256){throw ('Frozen runner input differs: '+$entry.path)}
}
$authority=Get-Content -LiteralPath (Join-Path $PSScriptRoot 'parent-authority-relay.json') -Raw|ConvertFrom-Json
if($authority.source -cne $source -or $authority.runner_manifest_sha256 -cne $ApprovedManifestSha256 -or $authority.manuscript_tex_sha256 -cne '440e5c1f4e99d8f188923c2a467e76f008c3a7a1fbfd7670610ae7ea2a1b9486' -or $authority.parent_full_mathematical_report_read -ne $true -or $authority.parent_full_engineering_report_read -ne $true){throw 'Both actual parent gates must be read and relayed before allocation'}
if($authority.mathematical_accepted -ne $true -or $authority.engineering_accepted -ne $true){throw 'Actual accepted source gates required'}
foreach($kind in @('mathematical','engineering')){
 $pathField=$kind+'_report_path';$hashField=$kind+'_report_sha256'
 $reportPath=[string]$authority.$pathField;$reportHash=[string]$authority.$hashField
 if(-not[regex]::IsMatch($reportHash,'\A[a-f0-9]{64}\z') -or (Get-FileHash -LiteralPath $reportPath).Hash.ToLowerInvariant() -cne $reportHash){throw 'Original full report hash binding differs'}
}
$out='D:\Datos\the-eriksson-programme\autonomia\evidencia-294\production-b\attempt-b'
if(Test-Path -LiteralPath $out){throw 'Preserve previous attempt; no blind retry'}
New-Item -ItemType Directory -Path $out|Out-Null
$prefix='export GOOGLE_APPLICATION_CREDENTIALS=/mnt/c/Users/lluis/AppData/Roaming/gcloud/application_default_credentials.json; exec /home/lluis/.local/bin/colab --auth adc --config /home/lluis/.config/colab-cli/tep294-build-b-sessions.json'
$session='tep294-build-b-own-cpu'
$remote='/content/tep294-build-b-results.zip'
$local='/mnt/d/Datos/the-eriksson-programme/autonomia/evidencia-294/production-b/attempt-b/tep294-build-b-results.zip'
$script='/mnt/c/Trabajo/the-eriksson-programme/prefix-rank290-20261113/_tmp/production294-b/build294.py'
$attempted=$false;$exits=[ordered]@{};$caught=$null
[IO.File]::WriteAllText((Join-Path $out 'runtime-open-requested.txt'),[DateTime]::UtcNow.ToString('o')+"`n")
try{
 $attempted=$true
 $exits.allocation=Invoke-CapturedWsl -Name 'allocation' -ShellCommand ($prefix+' new -s '+$session+' --high-mem') -OutputDirectory $out
 if($exits.allocation -ne 0){throw 'Actual allocation failed; preserve output and stop own session if any'}
 $exits.execution=Invoke-CapturedWsl -Name 'execution' -ShellCommand ($prefix+' exec -s '+$session+' -f '+$script+' --timeout 3600') -OutputDirectory $out
 $exits.download=Invoke-CapturedWsl -Name 'download' -ShellCommand ($prefix+' download -s '+$session+' '+$remote+' '+$local) -OutputDirectory $out
}catch{$caught=$_.Exception.ToString();[IO.File]::WriteAllText((Join-Path $out 'outer-failure.txt'),$caught+"`n")}
finally{
 if($attempted){$exits.release=Invoke-CapturedWsl -Name 'release' -ShellCommand ($prefix+' stop -s '+$session) -OutputDirectory $out}
 [IO.File]::WriteAllText((Join-Path $out 'runtime-release-finished.txt'),[DateTime]::UtcNow.ToString('o')+"`n")
 [ordered]@{actual_cli_exits=$exits;failure=$caught;status='Actual transport capture only; require returned inner logs/hash gate, stop readback and all-page review';source=$source;native_submit=$false}|ConvertTo-Json -Depth 8|Set-Content -LiteralPath (Join-Path $out 'outer-report.json') -Encoding utf8NoBOM
}
$exits|ConvertTo-Json
if($null -ne $caught -or $exits.Count -ne 4 -or @($exits.Values|Where-Object{$_ -ne 0}).Count -ne 0){throw 'Incomplete/nonzero actual lifecycle; preserve evidence'}
