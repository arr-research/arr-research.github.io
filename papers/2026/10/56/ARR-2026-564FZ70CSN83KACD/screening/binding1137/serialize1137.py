from pathlib import Path
import json,hashlib,shutil,datetime,sys
P=Path(__file__).resolve().parent
SRC=Path(r'C:\Trabajo\airr\2026-10-27_simplex1128-review')
SRCD=Path(r'D:\Proyectos\airr-investigacion\2026-10-27_simplex1128-review')
REPO=Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026')
PAPER=REPO/'papers/2026/10/56/ARR-2026-564FZ70CSN83KACD'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def inv(root):return {p.relative_to(root).as_posix():dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(root.rglob('*')) if p.is_file()}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert sha(SRC/'REVIEW1128.txt')=='213033661031a8ea1f9b5c278d1faaadf9e267ae5abe59a2509a130a17ae152d'
assert sha(SRC/'verdict1128.json')=='c7c7aa0fae70ed8d8d436507358a64911d74fcd79ae9e89a6e53a5de97741f65'
sourceinv=inv(SRC);assert sourceinv==inv(SRCD) and len(sourceinv)==325
m=read(SRC/'MANIFEST1128.json')
assert len(m['files'])==323
for row in m['files']:assert sourceinv[row['path']]==dict(bytes=row['bytes'],sha256=row['sha256'])
v=read(SRC/'verdict1128.json');report=(SRC/'REVIEW1128.txt').read_text(encoding='utf-8')
inc=read(SRC/'INCIDENTS1128.json')
meta=read(PAPER/'metadata.json')
assert meta['id']=='ARR-2026-564FZ70CSN83KACD' and meta['version']=='v1'
assert meta['version_id']=='arr:version:1f7b63ee-4ad0-44c1-b391-53e775cbaedb'
assert meta['record_id']=='arr:record:a623fe70-3335-40e6-a637-b365287b12bd'
assert v['scientific_importance_airr_0_10']==6.5 and v['overall_millennium_0_10']==6.3 and v['technical_quality_0_10']==8.8
for d in ['source1128','schema-snapshot','validation-fixture']:(P/d).mkdir(exist_ok=True)
source_files=['REVIEW1128.txt','verdict1128.json','PROVENANCE1128.json','READINGS1128.json','INCIDENTS1128.json','REPRODUCTION1128.json','MANIFEST1128.json','CLOSURE1128.json','OWN1128.json','OWN-FAILURE-INITIAL1128.json','OWN-FAILURE-SECOND1128.json','CURATION-RECEIPT1128.json','HISTORY-CHECK1128.json']
for n in source_files:shutil.copy2(SRC/n,P/'source1128'/n)
for n in ['assessmentlib.py','arrlib.py','ratinglib.py','prepare_model_assessment.py']:
    shutil.copy2(REPO/'scripts'/n,P/'schema-snapshot'/n)
shutil.copy2(PAPER/'metadata.json',P/'metadata-initial1137.json')
shutil.copy2(SRC/'input/manuscript.pdf',P/'validation-fixture/paper.pdf')
assert sha(P/'validation-fixture/paper.pdf')==v['artifact']['pdf_sha256']

cmap={'correctness_confidence':'correctness_confidence','rigor':'rigor_and_completeness','novelty':'novelty_relative_to_checked_sources','significance':'significance_if_claims_hold','reproducibility':'reproducibility_or_independent_inspectability'}
summary=(
 'Serialization of the SAME completed review1128, dated '+v['assessed_at']+'; no new scientific review, regrade or additional vote. '
 'Exact PDF: Quantum reference activation of classical symmetric channels. Scientific recommendation: publish within its declared scope; accept below is not an editorial decision. '
 'No confirmed material mathematical error was found. Distinct unchanged judgments: scientific importance AIRR6.5/10 (mathematical/physical consequence); global Millennium6.3/10 (overall research contribution); technical quality8.8/10 (rigor and evidence, not probability). Criteria are not averaged. '
 'The exact complete coefficient, binary-input barrier and fixed-dimensional binary readout with positive limiting relative entropy are substantive but specialized; methods and classical benchmark are prior, priority remains open and operational costs matter. '
 'Codex participated substantially. Context952/998/1006/1010/1031/1042/1048/1084 and filesystem were reused; this is not fresh, blind, human or independently isolated review. Effective model identity, effort and statistical independence are unattested. GPT-6 Astra xhigh was requested only, not observed. '
 'Full unchanged report213033661031a8ea1f9b5c278d1faaadf9e267ae5abe59a2509a130a17ae152d and verdictc7c7aa0fae70ed8d8d436507358a64911d74fcd79ae9e89a6e53a5de97741f65 remain authoritative.')
weak=[]
for o in v['objections']:
    weak.append(o['id']+' ['+o['severity']+'; PDF pp'+','.join(map(str,o['pages']))+']: '+o['statement']+' Status: '+o['status']+'. '+o['basis'])
potential=list(v['potential_errors_or_uncertainties'])
potential += [i['id']+' [preserved incident, not a newly detected theorem error]: '+i['description']+' Status: '+i['status']+'.' for i in inc['incidents']]
potential.append('Verification scope from1128 is unchanged: seven bounded replays passed; all200research files were not read line by line; additional eleven2048-bit1115 cases were authenticated/read but not all rerun. Own100-digit checks are numerical, not interval certificates; the inherited interval library is not an independent implementation. No formal proof, independent expert guarantee or remote supplement publication validation was claimed.')
potential.append('Adverse cases remain part of the same report and dossier: three nonseparating1096/1099 Umegaki pairs; small dimensional cases; n=3,k=3,4 below1/2; deterioration when n=k; changed regularizer; reversed Bernoulli orientation; replacing the effect by its limit gives zero divergence; polynomial delta changes the limiting retention. They are not excluded by selecting favorable finite certificates.')
response=dict(paper_id=meta['id'],version=meta['version'],version_id=meta['version_id'],canonical_sha256=v['artifact']['pdf_sha256'],provider='OpenAI',model_id='unknown',assessed_at=now,prompt_version='ARR-ASSESS-1.0',independence='involved_in_manuscript',recommendation='accept',millennium_score=v['overall_millennium_0_10'],overall_stars=v['overall_whole_star_display'],criteria={k:dict(stars=v['criteria_1_5'][s]['rating_1_5'],basis=v['criteria_1_5'][s]['basis']) for k,s in cmap.items()},summary=summary,strengths=v['strengths'],weaknesses=weak,potential_errors=potential,strong_novelty_candidates=[
 'Same1128 novelty candidate, priority open: exact complete coefficients for the classical symmetric family with arbitrary finite common quantum reference upper and faithful simplex sharpness for the named quantities; not a claim of all-Petz equality.',
 'Same1128 novelty candidate: contrast with every binary-input classical subchannel, whose quantum-reference amplification is absent. Classical formula and classical binary-support reduction are prior.',
 'Same1128 novelty candidate: fixed-dimensional separable CQ exclusion construction and binary readout retaining relative entropy with positive limit. States, common marginal and effect vary with k; conditioning and rare-event costs are essential.'],unresolved_material_objections=v['unresolved_material_objections'])
assert len(summary)<=1600,len(summary)
assert all(len(x)<=800 for field in ['strengths','weaknesses','potential_errors','strong_novelty_candidates'] for x in response[field])
assert len(potential)<=12
assert not any(x in response for x in ['assessment_id','source_response_sha256','runtime_provenance','review_context','intake_source'])
put('model-response.json',response)
sys.dont_write_bytecode=True
sys.path.insert(0,str(P/'schema-snapshot'))
from assessmentlib import normalize_model_response,validate_assessment,source_hash
from arrlib import Paper
# Official normalizer creates an ephemeral operator envelope in memory only.
# Its assessment UUID is discarded, never emitted or presented as a registered assessment.
normalized=normalize_model_response(response)
fixture_metadata=dict(meta)
fixture_metadata['source_of_truth']='paper.pdf'
fixture_metadata['integrity']={'algorithm':'sha256','canonical_sha256':v['artifact']['pdf_sha256']}
put('validation-fixture/metadata.json',fixture_metadata)
fixture_errors=validate_assessment(normalized,[Paper(P/'validation-fixture',fixture_metadata)])
assert not fixture_errors,fixture_errors
real_errors=validate_assessment(normalized,[Paper(PAPER,meta)])
real_pdf=PAPER/'paper.pdf'
observed_pdf_hash=sha(real_pdf) if real_pdf.is_file() else None
put('validation-initial1137.json',dict(utc=now,schema_and_offline_exact_PDF_pass=not fixture_errors,fixture_errors=fixture_errors,fixture_explanation='Read-only actual generated IDs plus exact reviewed PDF copied locally. Explicit source_of_truth/hash supplied in an isolated validation fixture only; not a claim that repository metadata is populated.',actual_registry_errors=real_errors,actual_repository_PDF_exists=real_pdf.is_file(),actual_repository_PDF_sha256=observed_pdf_hash,actual_metadata_sha256=sha(P/'metadata-initial1137.json'),normalized_assessment_UUID='ephemeral official-validator envelope, not saved or registered',structured_response_sha256=source_hash(response),model_response_file_sha256=sha(P/'model-response.json'),publication=False,repository_mutated=False))
mapping={
 'paper_id/version/version_id':'Read verbatim from actual newly generated metadata.json; no IDs inferred from old versions.',
 'canonical_sha256':'Exact1127 PDF SHA from immutable1128; canonical_sha256 means reviewed PDF here.',
 'provider/model_id':'OpenAI is the observed environment provider. model_id is literal unknown because effective runtime identity is not attested; requested Astra is only disclosed in prose.',
 'assessed_at':'Serialization timestamp, not a claim of a new scientific assessment. Original1128 assessed_at is retained in summary, full original verdict and this binding.',
 'prompt_version':'ARR-ASSESS-1.0 is the subsequent serialization format; does not assert this prompt was the original1128 request.',
 'independence':'involved_in_manuscript records participation; it does NOT assert independence. Shared context, prior exposure and possible bias remain explicit.',
 'recommendation':'recommend_publication_with_declared_scope -> accept. Same scientific recommendation with O1–O5; no editorial acceptance, admission or publication.',
 'millennium_score/overall_stars':'6.3 and6 unchanged. Scientific importance6.5 and technical8.8 are distinct and preserved in summary/binding/original verdict because schema has no separate numeric fields for them.',
 'criteria':'Only key aliases change; all five stars4 and original bases copied verbatim. No averaging.',
 'summary':'Concise faithful representation with provenance and all three score meanings; full source report and verdict preserved by SHA.',
 'strengths':'Original verdict list unchanged.',
 'weaknesses':'All five original objections expanded with original IDs, severity, pages, status and bases; no suppressed reservation.',
 'potential_errors':'Original uncertainties plus preserved I1–I6 incidents, verification scope and adverse-case inventory from report; incidents are not relabeled as theorem errors.',
 'strong_novelty_candidates':'Same1128 candidates, without priority certification or new scientific search.',
 'unresolved_material_objections':'Original empty array retained; this does not erase O1–O5 reservations.',
 'omitted_operator_fields':'No assessment_id, runtime_provenance, review_context, intake_source or source_response_sha256 in model response; no operator evidence fabricated.'}
put('BINDING1137.json',dict(utc=now,task='1137',operation='serialization_of_same_terminal_1128_judgment',new_scientific_review=False,additional_vote=False,regrade=False,scientific_sources_browsed=False,candidate1134_inspected=False,original_scientific_assessed_at=v['assessed_at'],serialization_at=now,prompt_version_role='subsequent format only',submission_id='SUB-FAEA3B94D5EE9309',record_id=meta['record_id'],paper_id=meta['id'],version=meta['version'],version_id=meta['version_id'],DOI=None,exact_pdf=v['artifact'],requested_configuration=v['requested_configuration'],observed_configuration=v['observed_configuration'],context=v['context'],scores={k:v[k] for k in ['scientific_importance_airr_0_10','overall_millennium_0_10','technical_quality_0_10','overall_whole_star_display']},score_definitions=v['definitions'],score_bases=v['bases'],mapping=mapping,criterion_key_mapping=cmap,objections=v['objections'],unresolved_material_objections=v['unresolved_material_objections'],original_incidents=inc,source_review=dict(C=str(SRC),D=str(SRCD),total_files=325,all_hashes_C_D_verified=True,files={n:sourceinv[n] for n in source_files},full_source_inventory=sourceinv),schema_files={q.name:dict(bytes=q.stat().st_size,sha256=sha(q)) for q in (P/'schema-snapshot').glob('*.py')},model_response_raw_sha256=sha(P/'model-response.json'),model_response_structured_sha256=source_hash(response),source_report_sha256=sha(SRC/'REVIEW1128.txt'),source_verdict_sha256=sha(SRC/'verdict1128.json'),initial_registry_state=dict(metadata_sha256=sha(P/'metadata-initial1137.json'),PDF_sha256=observed_pdf_hash,validation_errors=real_errors),validation_limit='Offline schema/exact-PDF fixture validation is separate from actual registry readiness; see final validation receipt.',full_public_context_requirement='Publish unchanged full1128 report and each objection alongside this projection; retain earlier reports as history for other PDFs, not extra votes.',no_editorial_decision=True,no_publication=True))
assert inv(SRC)==sourceinv and inv(SRCD)==sourceinv
print(json.dumps(dict(serialized=True,summary_chars=len(summary),schema_pass=True,initial_real_registry_errors=real_errors,model_response_sha256=sha(P/'model-response.json'),original_sources_unchanged=True)))
