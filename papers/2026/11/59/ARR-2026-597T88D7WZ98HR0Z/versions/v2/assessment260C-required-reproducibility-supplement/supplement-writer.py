import ast,json,hashlib,os,re,shutil,urllib.request
from pathlib import Path
from datetime import datetime,timezone
A=Path(r'D:\Datos\the-eriksson-programme\autonomia\evidencia-260')
F=A/'assessment260C-first-round';D=A/'assessment260C-required-reproducibility-supplement'
O=A/'production-c/attempt-c';R=O/'returned';E=R/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if D.exists():raise RuntimeError('Preserve existing supplement; no duplicate write')
original_before={p.relative_to(F).as_posix():sha(p) for p in F.rglob('*') if p.is_file()}
if sha(F/'scientific-review.txt')!='e598f628b78db894cc04af1b2148d45d9e262a26cb2f29cddb7f8e90d7b8ec55' or sha(F/'response-native.json')!='70ae74208f198811c3dcf44c4b3ebf9830c61965b1b03782b5449ccb66ade69f':raise RuntimeError('Original first round changed')
original=json.loads((F/'response-native.json').read_bytes())
if original['millennium_score']!=5.0 or original['overall_stars']!=5 or original['criteria']['clarity']['stars']!=4 or original['recommendation']!='major_revision' or len(original['unresolved_material_objections'])!=2:raise RuntimeError('Original immutable findings differ')
pdf=E/'checkerboard_observations260.pdf';pd=sha(pdf)
if pdf.stat().st_size!=397040 or pd!='f9d3a44e4811a28ec11af3577a4218dad1cb2b3bc0482e2528f5ff80ffdc3892':raise RuntimeError('Subject differs')
z=O/'tep260-build-c-results.zip'
if z.stat().st_size!=11154836 or sha(z)!='6bfa6a96638612868b07bb42ad1c9d77232d2cc67506bdc03456df920b314a7b':raise RuntimeError('Reproduction archive differs')
members=json.loads((E/'manifest.json').read_bytes());n=0
for row in members:
    p=R/row['path']
    if not p.resolve().is_relative_to(R.resolve()) or p.stat().st_size!=row['bytes'] or sha(p)!=row['sha256']:raise RuntimeError('Changed reproduction evidence member')
    n+=1
if n!=337:raise RuntimeError('Unexpected manifest count')
inputs=json.loads((E/'source-capture/SOURCE-INPUTS.json').read_bytes())['files']
for row in inputs:
    p=E/'source-capture'/row['path']
    if p.stat().st_size!=row['bytes'] or sha(p)!=row['raw_sha256']:raise RuntimeError('Changed source input')
if len(inputs)!=201:raise RuntimeError('Actual input count differs')
report=json.loads((E/'report.json').read_bytes())
if report['source']!='fb3ba8d2c0ae52d4a2e909b0fb2df02b2f953bc4' or len(report['builds'])!=2:raise RuntimeError('Source/clone evidence differs')
for b in report['builds']:
    if b['source']!=report['source'] or b['pdf_sha256']!=pd or b['pdf_bytes']!=397040 or b['input_files_verified']!=201:raise RuntimeError('Clone binding differs')
for name in ['clone-a.pdf','clone-b.pdf','checkerboard_observations260.pdf']:
    if (E/name).read_bytes()!=pdf.read_bytes():raise RuntimeError('Actual PDF byte mismatch')
for c in report['commands']:
    raw=(E/(c['name']+'.exit')).read_bytes()
    if raw!=b'0\n' or c['actual_exit']!=0 or c['timed_out']:raise RuntimeError('Nonzero actual command')
    if not(E/(c['name']+'.stdout')).is_file() or not(E/(c['name']+'.stderr')).is_file():raise RuntimeError('Missing complete command log')
if len(report['commands'])!=27 or not all(c['removed'] for c in report['cleanup']):raise RuntimeError('Command count or cleanup differs')
for m in ['allocation','execution','download','release','backend-readback']:
    if (O/(m+'.exit')).read_bytes()!=b'0\n':raise RuntimeError('Nonzero actual lifecycle')
if 'No active sessions found on server.' not in (O/'backend-readback.log').read_text(encoding='utf-8'):raise RuntimeError('No captured own inactivity')
for suffix in ['a','b']:
    if (E/f'head-{suffix}.stdout').read_text(encoding='utf-8').strip()!=report['source'] or (E/f'epoch-{suffix}.stdout').read_text(encoding='utf-8').strip()!='1794419533':raise RuntimeError('Actual head/epoch differs')
engineering=A/'production-c-returned-audit/full-report.txt'
engineering_text=engineering.read_text(encoding='utf-8-sig')
if 'ACCEPT_RETURNED_C_ENGINEERING_REPRODUCTION_WITH_LIMITS_NO_SCIENTIFIC_GRADE' not in engineering_text:raise RuntimeError('Actual engineering report differs')
contract_url='https://raw.githubusercontent.com/arr-research/arr-research.github.io/main/scripts/assessmentlib.py'
with urllib.request.urlopen(contract_url,timeout=30) as response:contract_raw=response.read(100000)
contract_text=contract_raw.decode('utf-8');match=re.search(r'^CRITERIA\s*=\s*(\([^\n]+\))',contract_text,re.M)
if match is None or ast.literal_eval(match.group(1))!=('correctness_confidence','rigor','novelty','significance','reproducibility'):raise RuntimeError('Live required criterion contract differs')
now=datetime.now(timezone.utc).isoformat()
supplement=r'''REQUIRED REPRODUCIBILITY CRITERION SUPPLEMENT260C

NEW CRITERION ONLY: reproducibility4/5.

This is a narrowly bounded missing-dimension supplement, NOT a second scientific
or importance sample and NOT a grade-improvement review. The parent explicitly
reported that its first protocol mistakenly requested clarity instead of the
reproducibility dimension required by AIRR's actual assessment data contract.
I read the actual public CRITERIA declaration and its criterion-validation
section. They require correctness_confidence,rigor,novelty,significance and
reproducibility, with integer criterion stars1--5. I do not rename clarity as
reproducibility, change that schema or infer a reproducibility number from a
clarity number. This task supplies a fresh judgment of ONLY the missing axis.

The original first report, response, importance5.00/10, overall5/10, five
original criterion findings INCLUDING clarity4/5, major_revision recommendation
and the two open material objections remain unchanged. The new criterion also
happens to be4/5, but its basis is the actual reproduction evidence below,
not equality with or substitution for clarity. Clarity remains an additional
diagnostic in the immutable original round. I do not reevaluate mathematics,
novelty, significance, importance, overall stars or the original objections.

EXACT SUBJECT AND EVIDENCE

PDF397040bytes,14pages, SHA256(raw bytes)
f9d3a44e4811a28ec11af3577a4218dad1cb2b3bc0482e2528f5ff80ffdc3892.
Exact sourcefb3ba8d2c0ae52d4a2e909b0fb2df02b2f953bc4;
TeX SHA256(raw bytes)
9c24b70685a5a7ae9301555170fa84acafd9f17524734775b1e9bca7cce822d9.
Actual production ZIP11154836bytes, SHA256(raw bytes)
6bfa6a96638612868b07bb42ad1c9d77232d2cc67506bdc03456df920b314a7b.

I read the COMPLETE production-c-returned-audit/full-report.txt, actual inner
report, complete frozen Linux build260.py, actual clone HEAD/epoch outputs,
clone path logs, tool-version outputs, APT warning and captured allocation,
release and backend readback logs. I checked the actual returned file bytes
against all337 raw manifest entries, separately verified all201 source-input
length/hash bindings, and checked all27 command records against their actual
zero-exit sentinel and full stdout/stderr file presence. I did not run a build,
compiler, Colab CLI, mathematical program or any live-runtime operation.
This is a bounded file/artifact-fidelity reading, not201 scientific rereadings
or another assessment of the theorems. The full immutable result ZIP is retained
in this supplement so that every original inner source/log/PDF/PNG remains
available; selected direct evidence and complete outer logs are also captured.

The actual clone-a.pdf,clone-b.pdf and selected final PDF agree byte-for-byte.
The two clone logs identify separate fresh directories under the own production
root. Both actual HEAD outputs equal the exact source above, both epochs are
1794419533, and both build records verify201 inputs. The recipe checks a fresh
root/archive and pinned source/TeX/input bytes before compilation, uses the same
source epoch and date-suppression/UTC settings, and preserves both actual TeX
passes. The returned engineering report verifies the four native attempt
retention records, complete ZIP membership and tracked source capture. My
supplement checks its binding and actual core file/command evidence; it is not
a new execution by an independent operator.

All27 recorded inner commands have actual zero exits and no timeout. Both full
stdout/stderr files are present for every command. Source clone/epoch outputs
and the reported tool versions are retained. There are five actual zero outer
exits: allocation,execution,download,release and backend-readback. The captured
stop names the own session, and the separate backend log explicitly says no
active sessions were found. The inner report records removal of both own
disposable clones. These are observed returned lifecycle artifacts; I did not
inspect or stop any live runtime or another chat's session. Billing units are
not exposed by the packet, and I infer no quota/charge figure from timestamps.

Observed tool context includes pdfTeX1.40.25/TeX Live2023, Poppler24.02.0,
Git2.43.0, Python3.13.18 and reported Pillow11.3.0. APT's actual update returned
zero but warned about an unavailable configured r2u source index. This warning
and package-install output are retained rather than called warning-free.

JUDGMENT AND LIMITATIONS

Reproducibility4/5 is justified by unusually complete source/hash/command/native
artifact capture and the observed two-fresh-clone byte match of the exact PDF.
The manuscript supplies an immutable source referent, its201 declared inputs
are captured, the production recipe and tool versions are retained, failures
and warnings remain visible, and the output can be traced to real child exits
rather than acceptance inferred from file existence. This supports strong
within-environment terminal reproduction and artifact traceability.

I withhold5/5 because the evidence shows two clones in ONE owned Linux execution
environment and shared toolchain, not a genuinely independent external operator
or a second platform/runtime reproducing the result. The package installation
uses repository package resolution rather than a fully version-locked container
or environment image; future tool/package changes may alter raw PDF bytes. The
frozen script also guards a named branch HEAD against its exact source pin;
if that branch advances, an operator must preserve or fetch the exact archived
source referent rather than blindly rerun against changed HEAD. These are
reproduction-portability limits, not a claim that the observed build failed.
No new build was executed to test another environment. Raw matching PDF bytes
do not formally verify the mathematical arguments, novelty or physical claims.

ACTUAL CONTEXT AND IMMUTABILITY

This is the same involved child session that completed the first exact260C
assessment, now assigned a separate required-criterion task after that round
finished. The parent construction/conversation and original report are visible.
It is not blind, human or independently established review. Actually exposed
identity is Codex/OpenAI; exact served backend/model version/reasoning effort
is unavailable and is not inferred from a task name or another reviewer.
No outside model service was used and no inbound parent message arrived during
this bounded task. The actual assignment and read scopes are retained. The
full inherited conversation is not exportable through a provided tool, so no
full-chat export or independent provider context is fabricated.

Only this NEW supplement directory is written. The original first-round
directory was read for binding and remains byte-for-byte unchanged. The
original scientific report and original numerical response retain hashes
e598f628b78db894cc04af1b2148d45d9e262a26cb2f29cddb7f8e90d7b8ec55
and70ae74208f198811c3dcf44c4b3ebf9830c61965b1b03782b5449ccb66ade69f.
No source, branch, scientific score, material objection, state, permission,
native receipt, publication or automation is modified by this task. No new
runtime or clone exists and there is no new cleanup debt.

The supplement records criterion reproducibility4/5 with its own evidence and
limitations. Any later native projection must transparently retain both the
original complete first report and this required missing-criterion supplement;
it must not pretend the first protocol requested or assessed this dimension.
'''
basis='Two fresh same-SHA clones produced byte-identical397040-byte PDFs;201 frozen inputs,27 actual zero-exit commands,337 raw-manifest members and complete source/tool/log capture support strong within-environment reproduction. Independent external/cross-platform reproduction and a fully version-locked environment remain unestablished.'
assignment=r'''First round COMPLETE and immutable: do not change or resample any original report,5.00importance/5overall, five originalcriteria includingclarity, recommendation or twoopenmaterialobjections. New narrowly bounded REQUIRED-CRITERION SUPPLEMENT only: I mistakenly specifiedclarity in the frozen protocol, while AIRR's actually inspected scripts/assessmentlib.py CRITERIA requires correctness_confidence,rigor,novelty,significance,REPRODUCIBILITY exactly. We must not rename clarity as reproducibility, invent a number, change schema to suit our output, or repeat a review to improve5.00. Please assess ONLY missing reproducibility0/1--5 dimension for SAME exact f9d3... PDF from actual source/reproduction evidence (evidencia-260/production-c/attempt-c/returned, actual201inputmanifest/27commands and completeproduction-c-returned-audit/full-report.txt). Read actual evidence needed, give genuine stars+basis+limitations; no targetscore. Do NOT re-review importance/overall/maths/novelty or change originalsixfindings/objections. Do not modify originalfirst-rounddirectory at all. Retaincompleteunabridged supplement, actualassignment/context and exactevidencecaptures/rawmanifest in evidencia-260/assessment260C-required-reproducibility-supplement. Explicitly record this is a required data-contract dimension missing dueparentprotocol choice, not a second scientific/importance sample or gradeimprovement; originalclarity4/5 remains preserved as an additional diagnostic. Existing firstreview staysunchanged. No actualexecution/runtime, state/source/permissions/publication. No inboundmessages whilethisboundedtask runs; returnactualnewcriterionjudgment andhashpaths. If this cannot honestly be assessed, sayso without inventing stars.
'''
ctx={'recorded_at':now,'task':'/root/exact260c_first_pdf_assessment','task_kind':'Required missing reproducibility criterion only, after completed immutable first round','reason':'Parent protocol requested clarity instead of actual required reproducibility dimension; no target score or schema change','new_criterion':{'name':'reproducibility','stars':4,'basis':basis},'original_first_round_changed':False,'importance_or_overall_or_scientific_reassessment':False,'original_clarity_4_preserved_as_additional_diagnostic':True,'original_report_sha256_raw':sha(F/'scientific-review.txt'),'original_response_sha256_raw':sha(F/'response-native.json'),'PDF_sha256_raw':pd,'exact_source':report['source'],'identity_actually_exposed':'Codex/OpenAI; exact served backend/model version and reasoning effort unavailable','inherited_context_visible':True,'blind':False,'independence_established':False,'inbound_parent_messages_during_bounded_task':False,'external_model_service_called':False,'production_or_compilation_executed':False,'runtime_allocated_or_inspected':False,'mathematical_program_run':False,'scope_of_local_operations':'File reads, byte hashes/binding comparisons, public contract-source retrieval and retention writes only','actual_returned_file_manifest_entries_verified':337,'actual_source_input_entries_verified':201,'actual_inner_commands_checked':27,'actual_outer_zero_exits_checked':5,'all201_inputs_scientifically_reread':False,'complete_returned_engineering_report_read':str(engineering),'engineering_report_sha256_raw':sha(engineering),'contract_source':{'url':contract_url,'retrieved_at':now,'sha256_raw':hashlib.sha256(contract_raw).hexdigest(),'read_scope':'CRITERIA declaration and criteria validation section; full raw source retained, not executed'},'full_inherited_context_export_limit':'Actual assignment retained; full inherited conversation not tool-exportable and not claimed captured','cleanup_pending':False}
result={'criterion':'reproducibility','stars':4,'basis':basis,'scale':'integer1--5 as actual native contract','subject_pdf_sha256':pd,'source_commit':report['source'],'supplement_kind':'required missing data-contract dimension, not a second scientific/importance sample','original_scientific_report_sha256':sha(F/'scientific-review.txt'),'original_numerical_response_sha256':sha(F/'response-native.json'),'original_findings_unchanged':True,'original_clarity_preserved_as_additional_diagnostic':True,'new_importance_or_overall_or_recommendation':None,'new_material_objection_judgment':None,'independence_established':False,'limitations':['Two clones share one Linux runtime/toolchain; not independent external/cross-platform reproduction.','Package repository resolution is not a fully version-locked environment image.','Exact branch-HEAD guard requires the immutable source referent to be preserved/fetched if branch moves.','Matching PDF/source artifacts do not formally verify mathematics, novelty or physical claims.']}
D.mkdir(); C=D/'capture';C.mkdir()
def put(name,v):
    raw=(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode('utf-8') if not isinstance(v,str) else v.encode('utf-8')
    with (D/name).open('xb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
    if (D/name).read_bytes()!=raw:raise RuntimeError('Supplement readback differs')
put('reproducibility-supplement.txt',supplement);put('criterion-response.json',result);put('review-context.json',ctx);put('assignment.txt',assignment)
(C/'assessmentlib.py').write_bytes(contract_raw)
captures={'exact260C.pdf':pdf,'production-c-results.zip':z,'returned-engineering-full-report.txt':engineering,'build260.py':A/'production-c/build260.py','inner-report.json':E/'report.json','inner-manifest.json':E/'manifest.json','SOURCE-INPUTS.json':E/'source-capture/SOURCE-INPUTS.json','source-files-a.stdout':E/'source-files-a.stdout','head-a.stdout':E/'head-a.stdout','head-b.stdout':E/'head-b.stdout','epoch-a.stdout':E/'epoch-a.stdout','epoch-b.stdout':E/'epoch-b.stdout','clone-a.stderr':E/'clone-a.stderr','clone-b.stderr':E/'clone-b.stderr','tex-version.stdout':E/'tex-version.stdout','poppler-version.stderr':E/'poppler-version.stderr','git-version.stdout':E/'git-version.stdout','apt-update.stderr':E/'apt-update.stderr','tracked-diff-a.stdout':E/'tracked-diff-a.stdout','tracked-diff-b.stdout':E/'tracked-diff-b.stdout'}
for mode in ['allocation','execution','download','release','backend-readback']:
    for suffix in ['.exit','.log','.stderr.log']:captures[mode+suffix]=O/(mode+suffix)
for name,src in captures.items():
    shutil.copyfile(src,C/name)
    if (C/name).read_bytes()!=src.read_bytes():raise RuntimeError('Capture differs')
shutil.copyfile(__file__,D/'supplement-writer.py')
original_after={p.relative_to(F).as_posix():sha(p) for p in F.rglob('*') if p.is_file()}
if original_before!=original_after:raise RuntimeError('Original first-round directory changed during supplement')
put('original-round-immutability-check.json',{'all_original_file_hashes_unchanged':True,'original_file_count':len(original_before),'files':original_before,'scope':'File-byte identity only, no scientific regrading'})
files=[{'path':p.relative_to(D).as_posix(),'bytes':p.stat().st_size,'sha256_raw':sha(p),'representation':'Exact retained raw bytes; no newline normalization'} for p in sorted(D.rglob('*')) if p.is_file()]
put('supplement-hashes.json',{'files':files,'file_count':len(files),'self_exclusion':True,'original_first_round_untouched':True})
print(json.dumps({'new_criterion':'reproducibility','stars':4,'report':str(D/'reproducibility-supplement.txt'),'report_sha256_raw':sha(D/'reproducibility-supplement.txt'),'response_sha256_raw':sha(D/'criterion-response.json'),'manifest_sha256_raw':sha(D/'supplement-hashes.json'),'manifested_files':len(files),'original_first_round_files_unchanged':len(original_before),'importance_overall_recommendation_or_objections_reassessed':False}))
