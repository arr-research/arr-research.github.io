$ErrorActionPreference='Stop'
$repoRoot='C:\Trabajo\the-eriksson-programme\prefix-rank290-20261113'
$auditRoot='D:\Datos\the-eriksson-programme\autonomia\evidencia-299\manuscript-source-audit299A'
$sha='6f9b27f59e3b105a872c773ed4d38d027536655b'
$utf8=New-Object System.Text.UTF8Encoding($false)
$lf=[string][char]10
function Capture-Raw([string]$exe,[string]$arguments,[string]$destination) {
 $pi=New-Object System.Diagnostics.ProcessStartInfo
 $pi.FileName=$exe; $pi.Arguments=$arguments; $pi.WorkingDirectory=$repoRoot
 $pi.UseShellExecute=$false; $pi.RedirectStandardOutput=$true; $pi.CreateNoWindow=$true
 $p=New-Object System.Diagnostics.Process; $p.StartInfo=$pi
 [void]$p.Start(); $stream=[IO.File]::Create($destination)
 try {$p.StandardOutput.BaseStream.CopyTo($stream)} finally {$stream.Dispose()}
 $p.WaitForExit(); if($p.ExitCode -ne 0){throw "capture failed: $exe $arguments"}
}
Capture-Raw 'gh.exe' 'pr view 245 --repo lluiseriksson/THE-ERIKSSON-PROGRAMME --json body,headRefOid,url,title,baseRefOid,files,state' "$auditRoot\pr245-body-capture.json"
$pr=Get-Content -LiteralPath "$auditRoot\pr245-body-capture.json" -Raw | ConvertFrom-Json
if($pr.headRefOid -ne $sha){throw 'PR head mismatch'}
$body=($pr.body -replace "\r\n?",$lf).TrimEnd([char]10)+$lf
[IO.File]::WriteAllText("$auditRoot\pr245-body-normalized.txt",$body,$utf8)
$snapshot=[ordered]@{captured_utc=[DateTime]::UtcNow.ToString('o');commit=$sha;pr=$pr.url;title=$pr.title;head=$pr.headRefOid;base=$pr.baseRefOid;method='gh pr view 245 --repo lluiseriksson/THE-ERIKSSON-PROGRAMME --json body,headRefOid,url,title,baseRefOid,files,state; stdout raw bytes';normalization='Decode JSON UTF-8, extract entire body; CRLF/CR to LF; remove trailing LF characters; append exactly one LF; UTF-8 without BOM';normalized_bytes=(Get-Item "$auditRoot\pr245-body-normalized.txt").Length;normalized_sha256=(Get-FileHash "$auditRoot\pr245-body-normalized.txt" -Algorithm SHA256).Hash.ToLower();head_local=(& git -C $repoRoot rev-parse HEAD);branch=(& git -C $repoRoot branch --show-current);status=@(& git -C $repoRoot status --short)}
[IO.File]::WriteAllText("$auditRoot\pr245-snapshot.json",($snapshot|ConvertTo-Json -Depth 8)+$lf,$utf8)
$manifest=Get-Content -LiteralPath "$repoRoot\papers\marginal-transfer\SOURCE-INPUTS299.json" -Raw|ConvertFrom-Json
$tree=@{}; & git -C $repoRoot ls-tree -r $sha | ForEach-Object {if($_ -match '^\d+ blob ([0-9a-f]+)\t(.+)$'){$tree[$Matches[2]]=$Matches[1]}}
$subjects=@()
foreach($f in $manifest.files){$subjects+= [pscustomobject]@{path='papers/marginal-transfer/'+$f.path;declared_bytes=$f.bytes;declared_sha256=$f.raw_sha256;kind='declared-source-input'}}
$extra=@('papers/marginal-transfer/SOURCE-INPUTS299.json','papers/marginal-transfer/manuscript299A.tex','papers/marginal-transfer/manuscript298A.tex','papers/marginal-transfer/critical299-section.tex','papers/marginal-transfer/PACKAGE-BOUNDARY299.txt','research/critical299/critical299A.txt','research/critical299/judges299.txt','research/critical298/critical298A.txt','CLAUDE.md','docs/OPERATIONAL-GOVERNANCE-CHARTER.md','.gitattributes')
foreach($path in $extra){if($path -notin $subjects.path){$subjects+=[pscustomobject]@{path=$path;declared_bytes=$null;declared_sha256=$null;kind='additional-audit-subject'}}}
$rows=@()
foreach($subject in $subjects){
 $path=$subject.path; if(-not $tree.ContainsKey($path)){throw "untracked subject $path"}
 $source=Join-Path $repoRoot $path
 $gitTarget=Join-Path "$auditRoot\subjects\git-blob" $path
 $checkoutTarget=Join-Path "$auditRoot\subjects\checkout" $path
 [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($gitTarget))
 [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($checkoutTarget))
 Capture-Raw 'git.exe' ('cat-file blob '+$tree[$path]) $gitTarget
 [IO.File]::Copy($source,$checkoutTarget,$false)
 $gitHash=(Get-FileHash -LiteralPath $gitTarget -Algorithm SHA256).Hash.ToLower()
 $checkoutHash=(Get-FileHash -LiteralPath $checkoutTarget -Algorithm SHA256).Hash.ToLower()
 $gitSize=(Get-Item -LiteralPath $gitTarget).Length; $checkoutSize=(Get-Item -LiteralPath $checkoutTarget).Length
 $ok=$true;if($subject.kind -eq 'declared-source-input'){$ok=($gitHash -eq $subject.declared_sha256 -and $checkoutHash -eq $subject.declared_sha256 -and $gitSize -eq $subject.declared_bytes -and $checkoutSize -eq $subject.declared_bytes)}
 $rows+=[pscustomobject]@{path=$path;kind=$subject.kind;git_blob=$tree[$path];declared_bytes=$subject.declared_bytes;declared_sha256=$subject.declared_sha256;git_bytes=$gitSize;git_sha256=$gitHash;checkout_bytes=$checkoutSize;checkout_sha256=$checkoutHash;declared_match=$ok;git_copy=$gitTarget;checkout_copy=$checkoutTarget}
}
$result=[ordered]@{commit=$sha;declared_count=@($manifest.files).Count;declared_unique_count=@($manifest.files.path|Sort-Object -Unique).Count;subjects_count=$rows.Count;failures=@($rows|Where-Object {-not $_.declared_match});subjects=$rows}
[IO.File]::WriteAllText("$auditRoot\input-manifest.json",($result|ConvertTo-Json -Depth 8)+$lf,$utf8)
$changes=@(& git -C $repoRoot diff --name-status $pr.baseRefOid $sha)
[IO.File]::WriteAllText("$auditRoot\changed-paths.txt",($changes -join $lf)+$lf,$utf8)
$ws=@(& git -C $repoRoot -c core.whitespace=cr-at-eol diff --check $pr.baseRefOid $sha 2>&1)
$wsExit=$LASTEXITCODE
[IO.File]::WriteAllText("$auditRoot\whitespace-observation.txt",("exit=$wsExit"+$lf+($ws -join $lf)+$lf),$utf8)
$text=[IO.File]::ReadAllText("$repoRoot\papers\marginal-transfer\manuscript299A.tex")
$labels=@([regex]::Matches($text,'\\label\{([^}]+)\}')|ForEach-Object {$_.Groups[1].Value})
$refs=@([regex]::Matches($text,'\\(?:ref|eqref)\{([^}]+)\}')|ForEach-Object {$_.Groups[1].Value})
$bibs=@([regex]::Matches($text,'\\bibitem\{([^}]+)\}')|ForEach-Object {$_.Groups[1].Value})
$cites=@([regex]::Matches($text,'\\cite(?:\[[^\]]*\])?\{([^}]+)\}')|ForEach-Object {$_.Groups[1].Value.Split(',')})
$static=[ordered]@{manuscript_lines=([IO.File]::ReadAllLines("$repoRoot\papers\marginal-transfer\manuscript299A.tex")).Count;labels=$labels.Count;duplicate_labels=@($labels|Group-Object|Where-Object Count -gt 1|Select-Object Name,Count);undefined_references=@($refs|Where-Object {$_ -notin $labels}|Sort-Object -Unique);bibliography_keys=$bibs;undefined_citations=@($cites|Where-Object {$_ -notin $bibs}|Sort-Object -Unique);section_literal_in_manuscript=$text.Contains([IO.File]::ReadAllText("$repoRoot\papers\marginal-transfer\critical299-section.tex").TrimEnd([char]10,[char]13));changed_files=$changes.Count;added_files=@($changes|Where-Object {$_ -match '^A\s'}).Count;evidence299_added=@($changes|Where-Object {$_ -match '^A\s+papers/marginal-transfer/evidence299/'}).Count;pr_files=@($pr.files).Count;whitespace_exit=$wsExit}
[IO.File]::WriteAllText("$auditRoot\static-observations.json",($static|ConvertTo-Json -Depth 8)+$lf,$utf8)
$snapshot|ConvertTo-Json -Depth 6
$result|Select-Object commit,declared_count,declared_unique_count,subjects_count,failures|ConvertTo-Json -Depth 5
$static|ConvertTo-Json -Depth 8
