$ErrorActionPreference='Stop'
$audit='D:\Datos\the-eriksson-programme\autonomia\evidencia-314\production-a-source-audit'
$repo='C:\Trabajo\the-eriksson-programme\cutoff306-20261113'
$source='b72cfbcb74275ff7f80b6c262cb003c5cc6ea8eb'
$paper='papers/marginal-transfer/'
$utf8=[Text.UTF8Encoding]::new($false)
function Write-Json($name,$obj){[IO.File]::WriteAllText((Join-Path $audit $name),($obj|ConvertTo-Json -Depth 12)+"`n",$utf8)}
$info=[Diagnostics.ProcessStartInfo]::new('git');$info.UseShellExecute=$false;$info.RedirectStandardInput=$true;$info.RedirectStandardOutput=$true;$info.RedirectStandardError=$true;$info.CreateNoWindow=$true
foreach($arg in @('-C',$repo,'cat-file','--batch')){$info.ArgumentList.Add($arg)}
$p=[Diagnostics.Process]::new();$p.StartInfo=$info;if(-not $p.Start()){throw 'cat-file failed'}
$stream=$p.StandardOutput.BaseStream
function Read-Blob([string]$spec){
 $p.StandardInput.WriteLine($spec);$p.StandardInput.Flush();$header=[Text.StringBuilder]::new()
 while(($b=$stream.ReadByte()) -ne 10){if($b -lt 0){throw 'EOF header'};[void]$header.Append([char]$b)}
 $h=$header.ToString();if($h -notmatch '^([a-f0-9]{40}) blob ([0-9]+)$'){throw ('Unexpected blob '+$h)}
 $size=[int]$Matches[2];$data=[byte[]]::new($size);$pos=0
 while($pos -lt $size){$n=$stream.Read($data,$pos,$size-$pos);if($n -le 0){throw 'EOF blob'};$pos+=$n}
 if($stream.ReadByte() -ne 10){throw 'Missing separator'}
 return ,$data
}
$tree=@(& git -C $repo ls-tree -r $source -- 'papers/marginal-transfer');if($LASTEXITCODE -ne 0){throw 'tree failed'}
[IO.File]::WriteAllText((Join-Path $audit 'source-paper-tree.txt'),($tree -join "`n")+"`n",$utf8)
$types=@{};foreach($line in $tree){if($line -match '^(\d+) (\S+) ([a-f0-9]+)\t(.+)$'){$types[$Matches[4]]=$Matches[1]+' '+$Matches[2]}}
foreach($name in @('manuscript314A.tex','SOURCE-INPUTS314.json','PACKAGE-BOUNDARY314.json','judges314.txt')){[IO.File]::WriteAllBytes((Join-Path $audit ('subjects\'+$name)),(Read-Blob ($source+':'+$paper+$name)))}
foreach($name in @('CLAUDE.md','docs/OPERATIONAL-GOVERNANCE-CHARTER.md')){[IO.File]::WriteAllBytes((Join-Path $audit ('subjects\'+[IO.Path]::GetFileName($name))),(Read-Blob ($source+':'+$name)))}
$inventory=Get-Content -LiteralPath (Join-Path $audit 'subjects\SOURCE-INPUTS314.json') -Raw|ConvertFrom-Json
$zip=[IO.Compression.ZipFile]::Open((Join-Path $audit 'source-input-capture.zip'),[IO.Compression.ZipArchiveMode]::Create)
$rows=@();$seen=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
try{
 foreach($row in $inventory.files){
  $name=[string]$row.path
  $safe= -not [IO.Path]::IsPathRooted($name) -and $name -notmatch '(^|/)\.\.(/|$)' -and $name -notmatch '\\'
  if(-not $safe -or -not $seen.Add($name)){throw ('Unsafe/duplicate '+$name)}
  $raw=Read-Blob ($source+':'+$paper+$name)
  $hash=[Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($raw)).ToLowerInvariant()
  $ok=$raw.Length -eq $row.bytes -and $hash -ceq $row.raw_sha256 -and $types[$paper+$name] -eq '100644 blob'
  $rows += [ordered]@{path=$name;bytes=$raw.Length;raw_sha256=$hash;git_type=$types[$paper+$name];matches=$ok}
  if(-not $ok){throw ('Mismatch '+$name)}
  $entry=$zip.CreateEntry($name,[IO.Compression.CompressionLevel]::Fastest);$output=$entry.Open();try{$output.Write($raw,0,$raw.Length)}finally{$output.Dispose()}
 }
}finally{$zip.Dispose();$p.StandardInput.Close();$p.WaitForExit();$p.Dispose()}
Write-Json 'source-input-verification.json' ([ordered]@{representation='Raw Git blob bytes at exact source; no text normalization';source=$source;count=$rows.Count;all_match=(@($rows|Where-Object{-not $_.matches}).Count -eq 0);files=$rows})
$old=Get-Content -LiteralPath 'D:\Datos\the-eriksson-programme\autonomia\evidencia-311\production-a-source-audit\subjects\SOURCE-INPUTS311.json' -Raw|ConvertFrom-Json
$newByPath=@{};foreach($row in $inventory.files){$newByPath[$row.path]=$row}
$inherited=@();foreach($row in $old.files){$new=$newByPath[$row.path];$inherited+=[ordered]@{path=$row.path;unchanged=($null -ne $new -and $new.bytes -eq $row.bytes -and $new.raw_sha256 -ceq $row.raw_sha256)}}
Write-Json 'inherited311-bindings.json' ([ordered]@{count=$inherited.Count;unchanged=@($inherited|Where-Object{$_.unchanged}).Count;entries=$inherited})
[ordered]@{count=$rows.Count;all_match=(@($rows|Where-Object{-not $_.matches}).Count -eq 0);inherited311=$inherited.Count;inherited_unchanged=@($inherited|Where-Object{$_.unchanged}).Count;tex_bytes=(Get-Item -LiteralPath (Join-Path $audit 'subjects\manuscript314A.tex')).Length;tex_raw_sha256=(Get-FileHash -LiteralPath (Join-Path $audit 'subjects\manuscript314A.tex')).Hash.ToLowerInvariant()}|ConvertTo-Json