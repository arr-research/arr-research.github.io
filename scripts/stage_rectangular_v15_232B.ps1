# Exact public scholarly copy/metadata editing only. No Python, tests or service calls.
$ErrorActionPreference='Stop'
$W='C:\Trabajo\airr-publicacion\tep-turan-v2-207-20261108'
$E='D:\Datos\the-eriksson-programme\autonomia\evidencia-232'
$D='D:\Entregas\the-eriksson-programme\2026-11-10_manuscript232'
$O=Join-Path $E 'public-v15-preparation'
$PID232='ARR-2026-7EPM3V3DP796BBRR'
$VID='arr:version:ec7f4fe6-6e9a-4618-bfbe-dcda3daa8fbe'
$PDF='5595e89c1bcbec1d9b1ae35053a76e6a962f67b45d5d1ac483e5b7a60c9b9be0'
$SOURCE='f83ee8a84b3ecc27470ed8a92ea61eb627d86445'
$INITIAL='8458953bee142a8d99a6839fef11d1fb004e79681a7ef7df72063ef4479a2d07'
$REL='papers/2026/08/7E/'+$PID232+'/versions/v15'
$DEST=Join-Path $W $REL
function Require($condition,[string]$message){if(-not $condition){throw $message}}
function Load([string]$path){Get-Content -LiteralPath $path -Raw|ConvertFrom-Json -AsHashtable}
function SHA([string]$path){(Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()}
function Put([string]$relative,$value){$path=Join-Path $DEST $relative;New-Item -ItemType Directory -Force -Path (Split-Path $path)|Out-Null;[System.IO.File]::WriteAllText($path,($value|ConvertTo-Json -Depth 70)+"`n",[System.Text.UTF8Encoding]::new($false))}
function Copy-Scholarly([string]$source,[string]$relative){$target=Join-Path $DEST $relative;New-Item -ItemType Directory -Force -Path (Split-Path $target)|Out-Null;Copy-Item -LiteralPath $source -Destination $target}
function Copy-ScholarlyTree([string]$source,[string]$relative){Get-ChildItem -LiteralPath $source -Recurse -File|ForEach-Object{Copy-Scholarly $_.FullName ($relative+'/'+$_.FullName.Substring($source.Length+1).Replace('\','/'))}}
function Text([string]$relative,[string]$value){$target=Join-Path $DEST $relative;New-Item -ItemType Directory -Force -Path (Split-Path $target)|Out-Null;[System.IO.File]::WriteAllText($target,$value,[System.Text.UTF8Encoding]::new($false))}
Require (-not(Test-Path -LiteralPath $DEST)) 'Existing v15 must be reconciled, never overwritten.'
$job=Load (Join-Path $E 'job232B.json')
$receipt=Load (Join-Path $E 'native-receipt232B.json')
$readback=Load (Join-Path $E 'native-receipt-https-readback232B.json')
$permission=Load (Join-Path $E 'native-working-permission232B.json')
$verified=Load (Join-Path $E 'native-intake232B-verified.json')
$binding=Load (Join-Path $E 'binding232B.json')
$decision=Load (Join-Path $E 'delegated-working-deposit-decision232B.json')
$review=Load (Join-Path $E 'assessment232B-protocol-clarification/response-native.json')
$original=Load (Join-Path $E 'assessment232B-codex/response.json')
$parent=Load (Join-Path $W 'papers/2026/08/7E/ARR-2026-7EPM3V3DP796BBRR/versions/v14/metadata.json')
Require ((SHA $job.pdf) -eq  $PDF  -and  (Get-Item -LiteralPath $job.pdf).Length -eq 505936) 'Exact assessed PDF gate.'
foreach($r in @($receipt,$readback)){
 Require ($r.registration_number -eq 'SUB-370C455C4D32B2FB'  -and  $r.sha256 -eq $PDF  -and  $r.size_bytes -eq 505936  -and  $r.status -eq 'eligible'  -and  $r.scan_status -eq 'clean'  -and  $r.published -eq $false) 'Actual clean receipt and separate readback required.'
 Require ($r.historical_revision.version_id -eq $VID  -and  $r.historical_revision.version -eq 'v15'  -and  $r.historical_revision.paper_id -eq $PID232  -and  $r.historical_revision.sha256 -eq $PDF  -and  $r.historical_revision.supersedes_version_id -eq $parent.version_id  -and  $r.historical_revision.parent_sha256 -eq $parent.integrity.canonical_sha256) 'Actual linked native binding gate.'
}
Require ($binding.version_id -eq $VID  -and  $verified.native_binding.version_id -eq $VID  -and  $verified.case -eq $receipt.registration_number  -and  $verified.grant -eq 'AGT-509C4BB2772680E386978FB7'  -and  $verified.separate_authenticated_HTTPS_readback -eq $true) 'Verified binding and actual grant record required.'
Require ($permission.submission_id -eq $receipt.registration_number  -and  $permission.sha256 -eq $PDF  -and  $permission.publication_permission_recorded -eq $true  -and  $permission.license -eq 'CC-BY-4.0'  -and  $permission.metadata_license -eq 'CC0-1.0'  -and  $permission.public_status -eq 'working_paper'  -and  $permission.published -eq $false  -and  $permission.initial_instruction_sha256 -eq $INITIAL) 'Actual exact licensed Working permission gate.'
Require ($review.recommendation -eq 'major_revision'  -and  $review.millennium_score -eq 4.1  -and  $review.overall_stars -eq 4  -and  $review.canonical_sha256 -eq $PDF  -and  $review.independence -eq 'unknown'  -and  $review.unresolved_material_objections.Count -eq 3) 'Exact adverse first assessment required.'
$criteria=@('correctness_confidence','rigor','novelty','significance','reproducibility');$stars=@(4,4,3,3,4)
for($i=0;$i -lt 5;$i++){Require ($review.criteria[$criteria[$i]].stars -eq $stars[$i]) 'Criterion stars changed.'}
for($i=0;$i -lt 3;$i++){Require ($review.unresolved_material_objections[$i] -ceq $original.unresolved_material_objections[$i]  -and  $review.unresolved_material_objections[$i] -ceq $decision.objections[$i].text  -and  $decision.objections[$i].status -eq 'OPEN_UNCHANGED') 'Original material entry/status changed.'}
Require ($original.recommendation -eq 'minor_revision'  -and  $decision.exact_pdf_sha256 -eq $PDF  -and  $decision.decision -eq 'working_deposit'  -and  $decision.human_signoff -eq $false  -and  $decision.editorial_acceptance -eq $false  -and  $decision.authority.initial_actual_authority_sha256_raw -eq $INITIAL) 'Truthful existing delegated disposition gate.'
$frozen=@{'assessment232B-codex/scientific-review.txt'='9619c2a5b971bdeca22c7654587229bd1ade8cb44b1b355cf1a7aecbbcdb50e9';'assessment232B-codex/response.json'='e05cc1bb5dea2cf3a43713b2d380d9afa3920c8e4ee3d350b95f4eb492c53e4f';'assessment232B-protocol-clarification/response-native.json'='12d5d04f87bca41ebcdec874bab4002e0672c716dab1f5bb90e61a4029254eea';'author-response232B/author-response232B.txt'='86aa0588974f9e26940aa44fc0aa222c83c35214a41f31ca40481190d7146c06'}
foreach($key in $frozen.Keys){Require ((SHA (Join-Path $E $key)) -eq $frozen[$key]) ('Frozen original changed: '+$key)}
$archives=@{'rectangular_matrix232B-assessed-package.zip'='c874aa8bdb3d846ae50f9047e1e2ae155a423fac1b1340935fd6ecc4190baa6e';'attempt-b/tep232B-review.zip'='f9ffa131859c97a8ab578ac7616d731d843ad3986171da372dcff7b1edfd48ae';'attempt-a/tep232A-review.zip'='cb90267e04861514afd2186d1df7fbc26f265245b6998658530462a2de964242'}
foreach($key in $archives.Keys){Require ((SHA (Join-Path $D $key)) -eq $archives[$key]) ('Frozen companion archive changed: '+$key)}
$sourceProof=Load (Join-Path $E 'source232B-verified.json')
foreach($s in $sourceProof.source_files){if($s.file){Require ((SHA (Join-Path $E ('source-b/'+$s.file))) -eq $s.sha256) ('Exact sourceB changed: '+$s.file)}}
New-Item -ItemType Directory -Path $DEST|Out-Null
Copy-Scholarly $job.pdf 'paper.pdf'
Copy-Scholarly (Join-Path $D 'exact232B/rectangular_matrix.txt') 'paper.txt'
Copy-ScholarlyTree (Join-Path $E 'source-b') 'source-b'
Get-ChildItem (Join-Path $E 'source-b') -File -Filter '*.tex'|ForEach-Object{Copy-Scholarly $_.FullName $_.Name}
Copy-Scholarly (Join-Path $E 'source-b/rectangular_matrix.tex') 'paper.tex'
foreach($folder in @('assessment232B-codex','assessment232B-protocol-clarification','author-response232B','source-audit','source-audit-b','visual-QA232B')){Copy-ScholarlyTree (Join-Path $E $folder) $folder}
Copy-ScholarlyTree (Join-Path $D 'inputs') 'source-inputs'
foreach($file in @('AUTHORING-REPORT.txt','AUTHORING-SCOPE.txt','CHANGE-MAP.json','PENDING-GATES.json','README.txt','SOURCE-INPUTS.json','SOURCE-MANIFEST.json','STRUCTURAL-CHECK.json')){Copy-Scholarly (Join-Path $E ('author/'+$file)) ('authoring-history/'+$file)}
foreach($file in @('source232B-prepared.json','source232B-verified.json','production232A-failure-verified.json','render232B-verified.json','assessed-package232B-verified.json')){Copy-Scholarly (Join-Path $E $file) ('production-history/'+$file)}
Copy-Scholarly (Join-Path $D 'exact232B/report.json') 'production-history/render232B-report.json'
foreach($file in @('render232B.py','run232B.sh')){Copy-Scholarly (Join-Path $E $file) $file}
Copy-Scholarly (Join-Path $D 'rectangular_matrix232B-assessed-package.zip') 'rectangular_matrix232B-assessed-package.zip'
Copy-Scholarly (Join-Path $D 'attempt-b/tep232B-review.zip') 'tep232B-review.zip'
Copy-Scholarly (Join-Path $D 'attempt-a/tep232A-review.zip') 'tep232A-review.zip'
$privateNames=@('native-intake232B-verified.json','native-receipt232B.json','native-receipt-https-readback232B.json','native-working-permission232B.json','native-grant232B.json','binding232B.json','delegated-working-deposit-decision232B.json','intake232B.py')
$privateHashes=@($privateNames|ForEach-Object{[ordered]@{file=$_;sha256_raw_file=SHA (Join-Path $E $_)}})
Put 'NATIVE-AUTHORITY-EVIDENCE.json' ([ordered]@{registration_number=$receipt.registration_number;grant_id=$verified.grant;canonical_sha256=$PDF;canonical_bytes=505936;received_at=$receipt.received_at;status='eligible';scan_status='clean';published_at_intake=$false;separate_authenticated_HTTPS_readback=$true;verified_at=$verified.checked_at;binding=[ordered]@{paper_id=$PID232;record_id=$binding.record_id;version='v15';version_id=$VID;supersedes_version_id=$parent.version_id;parent_sha256=$parent.integrity.canonical_sha256;sha256=$PDF};working_permission=[ordered]@{recorded=$true;license='CC-BY-4.0';metadata_license='CC0-1.0';public_status='working_paper';initial_instruction_sha256=$INITIAL};original_private_evidence=$privateHashes;projection='Checked non-secret fields only. Raw grants/tokens/jobs/receipts/authority records remain private. No publication or acceptance created by this projection.'})
Put 'DELEGATED-WORKING-DISPOSITION.json' ([ordered]@{recorded_at=$decision.recorded_at;exact_pdf_sha256=$PDF;source_sha=$SOURCE;decision='working_deposit';signed_by='Codex (delegated Working-paper handling; owner instruction retained)';human_signoff=$false;human_response_simulated=$false;editorial_acceptance=$false;independence_claim=$false;initial_instruction_sha256=$INITIAL;minimum_threshold_reason=$decision.minimum_threshold_reason;conflicts=@('author_is_founder_editor','Codex assisted preparation; no independent human editorial adjudication claimed');objections=$decision.objections;native_format_recommendation='major_revision';score_unchanged=4.1;overall_stars_unchanged=4;criteria_unchanged=$stars;original_private_record_sha256=SHA (Join-Path $E 'delegated-working-deposit-decision232B.json');projection_note='Truthful correctly encoded public role projection. Original private record bytes, including any legacy mojibake, are unchanged; no original owner quote or private authority path is republished.'})
$bound=Load (Join-Path $E 'assessment232B-protocol-clarification/response-native.json');Require (-not $bound.ContainsKey('version_id')) 'Original already includes unexpected version binding.';$bound.version_id=$VID
Put 'bound-model-response232B.json' $bound
Put 'assessment-binding232B.json' ([ordered]@{original_response_raw_sha256=SHA (Join-Path $E 'assessment232B-codex/response.json');native_clarification_response_raw_sha256=SHA (Join-Path $E 'assessment232B-protocol-clarification/response-native.json');bound_response_raw_sha256=SHA (Join-Path $DEST 'bound-model-response232B.json');actual_version_id=$VID;actual_native_case=$receipt.registration_number;native_evidence_projection='NATIVE-AUTHORITY-EVIDENCE.json';projection='Only actual verified version_id added to complete model-authored clarified response. No scientific, categorical, criterion, timestamp or score field changed. Native normalizer still pending in sanctioned Linux environment.'})
$code=@(@{spdx='AGPL-3.0-only';path='render232B.py'},@{spdx='AGPL-3.0-only';path='run232B.sh'})
$meta=Load (Join-Path $W 'papers/2026/08/7E/ARR-2026-7EPM3V3DP796BBRR/versions/v14/metadata.json')
$meta.version_id=$VID;$meta.version='v15';$meta.title=$job.metadata.title;$meta.abstract=$job.metadata.abstract;$meta.date='2026-11-11';$meta.status='working_paper';$meta.source_of_truth='paper.pdf';$meta.supersedes_version_id=$parent.version_id;$meta.Remove('release_url')
$meta.integrity=@{algorithm='sha256';manifest='MANIFEST.sha256';canonical_sha256=$PDF;canonical_bytes=505936}
$meta.licenses=@{manuscript='CC-BY-4.0';metadata='CC0-1.0';code=$code;data=@()}
$meta.deposit.terms_version='ARR-DEPOSIT-2.1'
$meta.ai_assistance=@{used=$true;statement=($job.metadata.ai_disclosure+' Future234-240 results are absent from these exact bytes and receive no transferred4.10 score. Actual native receipt/permission now recorded; full original reports and one-round context remain unchanged.');systems=@('Codex/OpenAI; based on GPT-6, exact served backend/effort unknown')}
$meta.screening=@{protocol='ARR-SCREEN-1.0';status='fail';critical_objections_unresolved=3;human_signoff=$false;evaluators=@(@{provider=$review.provider;model_id=$review.model_id;outcome='concerns';report='assessment232B-protocol-clarification/response-native.json';involved_in_creation=$true})}
$meta.verification=@{protocol='ERIKSSON-EXACT-ARTIFACT-20261031';bibliography='partial';source_integrity='pass';reproducibility='partial';lean4='not_assessed';report='VERIFICATION.md'}
$meta.editorial=@{decision='working_deposit';signed_by='Codex (delegated Working-paper handling; owner instruction retained)';conflicts=@('author_is_founder_editor','authoring_and_handling_AI_involvement');statement='Delegated Working-paper disposition under retained actual owner instructions, with exact native clean receipt and Working permission; no fresh human reply, human signoff or editorial acceptance. First exact232B score4.10/10,4 stars,criteria4/4/3/3/4; native major_revision and all three material entries OPEN. Original conditional minor opinion, complete reports/clarification/author response preserved. Priority/usefulness/conditioning unresolved. See DELEGATED-WORKING-DISPOSITION.json.'}
$meta.revision=@{change_size='major';summary='Integrated finite observation-class successor: sharp actual coexact common-rank bounds, component-adapted block-diagonal escape and fixed-basis growing-channel coupled lower/matching-mode upper, retaining full scalar/matrix/weak-endpoint proofs. No PDF change after first assessment; all material objections remain open.'}
$meta.keywords=@('Finite matrix gradients','Observation classes','Coexact common-partition rank','Component-adapted rectangles','Coupled channel-separable observations','Critical weak endpoints')
Put 'metadata.json' $meta
Put 'LICENSES.json' (@{manuscript=@{spdx='CC-BY-4.0';notice='Copyright 2026 Lluis Eriksson. Actual native exact-v15 Working-paper permission. Original source/code notices inside all archives remain unchanged; no blanket third-party relicensing.'};metadata=@{spdx='CC0-1.0'};code=$code;data=@()})
Copy-Scholarly (Join-Path $W 'LICENSE') 'LICENSES/AIRR-AGPL-3.0.txt'
Put 'PROVENANCE.json' ([ordered]@{schema_version='1.0';record_id=$binding.record_id;version_id=$VID;source_of_truth='paper.pdf';pdf_source_commit=$SOURCE;canonical_source=@{pages=30;media_type='application/pdf';bytes=505936;sha256=$PDF};supersedes_version_id=$parent.version_id;revision=$meta.revision;native_evidence='NATIVE-AUTHORITY-EVIDENCE.json';working_deposit='DELEGATED-WORKING-DISPOSITION.json';assessment_binding='assessment-binding232B.json';source_files='source-b/';original_assessed_archive_includes_completed_author_response=$true;original_assessed_archive_sha256=$archives['rectangular_matrix232B-assessed-package.zip'];history='Failed sourceA/render and correctedB differential audit preserved. Source/date-specific earlier pending statements retain their historical referents. No future234-240 content or score transfer.';verification_notes='Document-tool exits and visual QA are not mathematical execution, formal certification or two-fresh-clone scientific replay. Scientific source/PDF judgments are qualified AI readings. Native normalizer and public validation run separately in Linux.'})
$reportFiles=@()
foreach($folder in @('assessment232B-codex','assessment232B-protocol-clarification','author-response232B')){foreach($p in Get-ChildItem (Join-Path $DEST $folder) -File){$reportFiles+=@{label=($folder+'/'+$p.Name);path=($folder+'/'+$p.Name);sha256=SHA $p.FullName}}}
Put 'MODEL-REVIEW-CONTEXT.json' ([ordered]@{schema_version='1.0';version_id=$VID;canonical_sha256=$PDF;provider=$review.provider;ui_label=$review.model_id;backend_identity=$null;recorded_at=$review.assessed_at;score=4.1;scale='Scientific importance0-10; native rounded overall stars1-10; five criteria1-5';recommendation='major_revision';summary='Same first exact232B round: original conditional specialist minor_revision opinion and conservative major_revision protocol clarification retained in full; score4.10 and all three material entries remain OPEN. Not acceptance.';context='No blind, score-blind, human or demonstrated independent review. Predecessor3.25 score visible inside PDF. Exact backend/effort unknown. The public screening involvement flag conservatively discloses that Codex was used in manuscript creation; the original model independence field remains unknown and no backend identity is inferred.';report_files=$reportFiles})
$history=@()
foreach($r in @('versions/v6/MODEL-REVIEW-CONTEXT.json','versions/v14/MODEL-REVIEW-CONTEXT.json')){$path=Join-Path $W ('papers/2026/08/7E/'+$PID232+'/'+$r);$history+=@{public_repository_path=('papers/2026/08/7E/'+$PID232+'/'+$r);sha256=SHA $path;purpose='Different exact predecessor PDF only; no score or quorum transfer.'}}
$h154='papers/2026/08/7E/'+$PID232+'/versions/v6/model-assessment154'
foreach($p in Get-ChildItem (Join-Path $W $h154) -File){$history+=@{public_repository_path=($h154+'/'+$p.Name);sha256=SHA $p.FullName;purpose='Complete original informe154 already public; preserve original v6 PDF binding and objections.'}}
Put 'HISTORICAL-REVIEW-LINKS.json' $history
Text 'CITATION.cff' ("cff-version: 1.2.0`nmessage: 'Cite exact v15 and full adverse review context.'`ntitle: '"+$meta.title+"'`nauthors:`n  - family-names: Eriksson`n    given-names: Lluis`nversion: 'v15'`nlicense: CC-BY-4.0`nurl: 'https://airr.science/papers/"+$PID232+"/versions/v15/'`n")
Text 'paper.md' ("# "+$meta.title+"`n`nWorking paper — not admitted to the AIRR accepted collection.`n`n"+$meta.abstract+"`n`nThe canonical artifact is the unchanged 30-page PDF; paper.txt is the existing full text extraction. Read REVIEW-STATUS.md and all original reports. The Markdown is a structured catalogue summary, not a replacement mathematical transcription. Complete mathematical TeX is in source-b/.`n")
Text 'REVIEW-STATUS.md' @'
# Exact232B review and release preparation

Working paper — not admitted to the AIRR accepted collection.

First and only exact-PDF numerical assessment: scientific importance4.10/10,
four native overall stars; criteria4/4/3/3/4. The original conditional specialist
minor_revision opinion and full report are unchanged. Same-round protocol
clarification requires major_revision; ALL THREE material entries remain OPEN.
Historical priority, practical usefulness, conditioning and efficient implementation
remain unestablished. No favorable grade was requested or repeated for improvement.

The full completed author response is already included in the unchanged original
97-subject assessed ZIP, as well as separately alongside the reports. The earlier
author-policy preparation's contrary chronology statement was false and is not
repeated here. SourceA failed on undefined mathscr; exactly two typography controls
were corrected inB, separately audited before rendering and this assessment.

Named author Lluis Eriksson; Codex/OpenAI assisted drafting and delegated handling.
Exact backend/effort unknown. Same provider/account context, predecessor-score
exposure inside the PDF, and unverified isolation prevent blind, independent or
human-review claims. A public evaluator involvement flag conservatively discloses
use of Codex in authorship; original assessment independence remains unknown.

Native exact-hash linked receipt and Working permission are recorded in a safe
projection. The delegated disposition is not a new human reply/signature, editorial
acceptance, independent minimum-quality review or release. Metadata date11November
is not a release timestamp. Actual production was10November; PDF metadata9November
is fixed SOURCE_DATE_EPOCH. No publication time is invented. Future234-240 results
are absent from the PDF and inherit no4.10 score. Earlier dated pending/no-PDF
source notes and all predecessor reports retain their original exact referents.

Full first report, clarification and response are linked by MODEL-REVIEW-CONTEXT.
HISTORICAL-REVIEW-LINKS identifies original v6 informe154 and v14 context with hashes.
Those different-artifact scores do not enter this version's aggregate or quorum.
'@
Text 'VERIFICATION.md' @'
# Scope of verification for exact232B

Canonical PDF SHA2565595e89c1bcbec1d9b1ae35053a76e6a962f67b45d5d1ac483e5b7a60c9b9be0,
505936bytes,30pages; produced sourcef83ee8a84b3ecc27470ed8a92ea61eb627d86445.
Source-b is exact; the same ten TeX files also appear at the root and paper.tex is
an unchanged root alias, with its nine exact inputs available beside it. To inspect
the source use source-b/rectangular_matrix.tex with its nine inputs, or the root.
The convenience root alias is not a separately flattened proof.

Full analytical source auditA, correctedB differential audit, original failed render
A, successful originalB document archive, original assessed archive and all30-page
visual-QA records are supplied. The assessed archive already includes all three
completed author-response files. Historical pending headings are dated evidence.
Existing original render records report all10document-tool exits0,81 payload hashes
and separately inactive runtime backend; assessed archive verification reports97.
This is not an all-size scientific test, mathematical computation, Lean/formal
proof, practical algorithm or two-fresh-clone scientific replay. Bibliography was
selectively checked; priority and exact classical equivalence remain unresolved.

Actual native libraries will normalize the one bound response and validate/build
the public package in a separately owned Linux runtime after the source gate.
Those results must be bound to exact code/payload and real exits, never inferred
from this preparation. No score, objection, old failure criterion or native state
is changed by these files. All three material objections remain open.

Rights: actual exact-v15 native Working permission covers manuscriptCC-BY-4.0 and
metadataCC0-1.0. Repository-produced render code retains AGPL-3.0 scope; original
notices in captured inputs/archives prevail, no blanket third-party relicensing.
Primary bibliography URLs in the manuscript identify acknowledged classical work.
Historical report154 remains at its original public v6 path with exact hashes.
'@
# Reproduce the separately prepared scholarly addenda from the retained frozen set.
foreach($entry in (Load (Join-Path $O 'addenda-hashes.json'))){
 $source=Join-Path $O ('addenda/'+$entry.path)
 Require ((SHA $source) -eq $entry.sha256) ('Frozen public addendum changed: '+$entry.path)
 Copy-Scholarly $source $entry.path
}
$bindingNote=Load (Join-Path $DEST 'assessment-binding232B.json')
$bindingNote.binding_prepared_at=Get-Date -Format o
$bindingNote.normalizer_status_at_binding_preparation='Not executed at this editing-stage freeze; later actual result belongs to NORMALIZATION-RECEIPT232B.json.'
Put 'assessment-binding232B.json' $bindingNote
$rows=@(Get-ChildItem -LiteralPath $DEST -File -Recurse|Sort-Object FullName|ForEach-Object{[ordered]@{path=$_.FullName.Substring($DEST.Length+1).Replace('\','/');bytes=$_.Length;sha256=SHA $_.FullName}})
Put 'PACKAGE-INPUTS232B.json' ([ordered]@{canonical_sha256=$PDF;source_commit=$SOURCE;native_version_id=$VID;files=$rows;note='Editing/copy/hash-stage identity, not native normalizer or build result; self and later MANIFEST excluded.'})
$attrs=Join-Path $W '.gitattributes';[System.IO.File]::AppendAllText($attrs,"`n# Preserve exact v15 PDF, original reports and archived source bytes.`n"+$REL+"/** -text whitespace=cr-at-eol,-blank-at-eof`n",[System.Text.UTF8Encoding]::new($false))
Copy-Item -LiteralPath $PSCommandPath -Destination (Join-Path $O 'stage_public232B.ps1')
[ordered]@{prepared_at=(Get-Date -Format o);branch='codex/tep232b-linked-working-v15-20261111';base='aa3fac26d52df621679fa0d8be71483afc3c82a1';public_relative_path=$REL;canonical_sha256=$PDF;source_commit=$SOURCE;native_case=$receipt.registration_number;native_version_id=$VID;file_count=$rows.Count;normalizer_executed=$false;tests_build_render=$false;registry_mutated=$false;release_or_merge=$false}|ConvertTo-Json -Depth 6|Set-Content (Join-Path $O 'editing-stage.json') -Encoding utf8NoBOM
Write-Output ('Staged exact scholarly v15 files: '+$rows.Count+'. Native normalizer/validators/build remain unexecuted.')
