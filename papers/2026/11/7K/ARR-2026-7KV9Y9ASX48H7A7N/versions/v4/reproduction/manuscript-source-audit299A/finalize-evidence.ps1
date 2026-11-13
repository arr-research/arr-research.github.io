$ErrorActionPreference='Stop'
$repoRoot='C:\Trabajo\the-eriksson-programme\prefix-rank290-20261113'
$auditRoot='D:\Datos\the-eriksson-programme\autonomia\evidencia-299\manuscript-source-audit299A'
$sha='6f9b27f59e3b105a872c773ed4d38d027536655b'
$utf8=New-Object System.Text.UTF8Encoding($false);$lf=[string][char]10
$pi=New-Object System.Diagnostics.ProcessStartInfo
$pi.FileName='gh.exe';$pi.Arguments='pr view 245 --repo lluiseriksson/THE-ERIKSSON-PROGRAMME --json body,headRefOid,url,title,baseRefOid,files,state'
$pi.WorkingDirectory=$repoRoot;$pi.UseShellExecute=$false;$pi.RedirectStandardOutput=$true;$pi.CreateNoWindow=$true
$p=New-Object System.Diagnostics.Process;$p.StartInfo=$pi;[void]$p.Start()
$stream=[IO.File]::Create("$auditRoot\pr245-final-body-capture.json")
try{$p.StandardOutput.BaseStream.CopyTo($stream)}finally{$stream.Dispose()}
$p.WaitForExit();if($p.ExitCode -ne 0){throw 'Final PR capture failed'}
$pr=Get-Content -LiteralPath "$auditRoot\pr245-final-body-capture.json" -Raw|ConvertFrom-Json
$body=($pr.body -replace "\r\n?",$lf).TrimEnd([char]10)+$lf
[IO.File]::WriteAllText("$auditRoot\pr245-final-body-normalized.txt",$body,$utf8)
$bodyHash=(Get-FileHash -LiteralPath "$auditRoot\pr245-final-body-normalized.txt" -Algorithm SHA256).Hash.ToLower()
$initial=Get-Content -LiteralPath "$auditRoot\pr245-snapshot.json" -Raw|ConvertFrom-Json
$head=(& git -C $repoRoot rev-parse HEAD);$branch=(& git -C $repoRoot branch --show-current)
if($pr.headRefOid -ne $sha -or $head -ne $sha -or $bodyHash -ne $initial.normalized_sha256){throw 'Frozen referent changed'}
$inputs=Get-Content -LiteralPath "$auditRoot\input-manifest.json" -Raw|ConvertFrom-Json
$stability=@()
foreach($item in $inputs.subjects){$actual=(Get-FileHash -LiteralPath (Join-Path $repoRoot $item.path) -Algorithm SHA256).Hash.ToLower();$stability+=[pscustomobject]@{path=$item.path;current_checkout_sha256=$actual;matches_captured_checkout=($actual -eq $item.checkout_sha256)}}
$bad=@($stability|Where-Object {-not $_.matches_captured_checkout})
if($bad.Count -ne 0){throw 'Source checkout changed'}
$final=[ordered]@{checked_utc=[DateTime]::UtcNow.ToString('o');commit=$sha;local_head=$head;branch=$branch;pr_head=$pr.headRefOid;pr_url=$pr.url;body_capture_method=$initial.method;body_normalization=$initial.normalization;normalized_body_bytes=(Get-Item "$auditRoot\pr245-final-body-normalized.txt").Length;normalized_body_sha256=$bodyHash;initial_body_match=($bodyHash -eq $initial.normalized_sha256);status=@(& git -C $repoRoot status --short);subjects_rechecked=$stability.Count;source_changes=$bad;verdict='ACCEPT';scope='Mathematical source integration and package only; no PDF assessment or numerical score';new_pdf_score=$null;backend_and_isolation_verified=$false}
[IO.File]::WriteAllText("$auditRoot\pr245-final-snapshot.json",($final|ConvertTo-Json -Depth 8)+$lf,$utf8)
[IO.File]::WriteAllText("$auditRoot\source-stability.json",($stability|ConvertTo-Json -Depth 6)+$lf,$utf8)
$records=@()
foreach($file in Get-ChildItem -LiteralPath $auditRoot -Recurse -File|Sort-Object FullName){
 if($file.FullName -in @("$auditRoot\raw-hashmanifest.json","$auditRoot\raw-hashmanifest.sha256")){continue}
 $records+=[pscustomobject]@{path=$file.FullName.Substring($auditRoot.Length+1).Replace('\','/');absolute_path=$file.FullName;bytes=$file.Length;raw_sha256=(Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLower()}
}
$output=[ordered]@{frozen_commit=$sha;verdict='ACCEPT';representation='Exact stored raw bytes, no normalization. PR normalization is limited to the expressly named normalized-body files. Separate Git and checkout subjects retained.';exclusions='This raw manifest and its detached digest are excluded to avoid circular hashing.';file_count=$records.Count;files=$records}
[IO.File]::WriteAllText("$auditRoot\raw-hashmanifest.json",($output|ConvertTo-Json -Depth 8)+$lf,$utf8)
$manifestHash=(Get-FileHash -LiteralPath "$auditRoot\raw-hashmanifest.json" -Algorithm SHA256).Hash.ToLower()
[IO.File]::WriteAllText("$auditRoot\raw-hashmanifest.sha256",$manifestHash+'  raw-hashmanifest.json'+$lf,$utf8)
$final|ConvertTo-Json -Depth 6
[pscustomobject]@{output_files=$records.Count;raw_manifest_sha256=$manifestHash;full_report_sha256=(Get-FileHash -LiteralPath "$auditRoot\full-report.md").Hash.ToLower();input_manifest_sha256=(Get-FileHash -LiteralPath "$auditRoot\input-manifest.json").Hash.ToLower();context_sha256=(Get-FileHash -LiteralPath "$auditRoot\context-and-scope.txt").Hash.ToLower();gate_table_sha256=(Get-FileHash -LiteralPath "$auditRoot\judge-table.md").Hash.ToLower()}|ConvertTo-Json
