from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

OUT=Path(__file__).resolve().parent
INPUT=OUT.parent/'input'
ARCHIVE=Path(r'D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico\revision-manuscript-1')
PREVIOUS=ARCHIVE.parent/'revision-dossier-1'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,value): (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
initial=json.loads((OUT/'input-integrity-initial.json').read_text())['inputs']
actual={p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in INPUT.iterdir()}
assert actual==initial
manifest=json.loads((INPUT/'artifact-manifest.json').read_text())
assert all(actual[x['name']]==dict(bytes=x['bytes'],sha256=x['sha256']) for x in manifest['artifacts'])
sm=json.loads((OUT/'supplement-frozen'/'manifest.json').read_text())
assert all(sha(OUT/'supplement-frozen'/x['path'])==x['sha256'] and (OUT/'supplement-frozen'/x['path']).stat().st_size==x['bytes'] for x in sm['entries'])

protected={
str(PREVIOUS/'audit-report.txt'):'5e49154cc6dd2e0d0ccb41c352de2af31b3acc0edd0a0ff1e2187a1ca821238c',
str(PREVIOUS/'verdict.json'):'ba45becc730e5818a297c2631a736a407ace8803a903bd43a9a9d239fa6444a3',
str(PREVIOUS/'hash-inventory.json'):'e13a48dad4a4275e4ee37c9cca6e7a114c60fee851787dfe3738dc3c59b37981',
str(PREVIOUS/'archive-verification.json'):'be03a05569bed5e873fb82a6657182c36610707a47fe858ade6153b19f04bafa',
r'D:\Proyectos\airr-investigacion\2026-10-17_canales-termicos\revision-manuscript-3\manuscript-review.txt':'a6d1f899ac8c46f30d40791fd624173aae2b88b4c37c9559af0bd09a9a1b85c4',
r'D:\Proyectos\airr-investigacion\2026-10-17_canales-termicos\revision-manuscript-3\assessment.json':'3577120df2374e60abab9bf903d99e30056714007837039fd8feafd5fe5d9865',
r'D:\Proyectos\airr-investigacion\2026-10-18_reinicio-termico\revision-parcial-1\audit-report.txt':'286a243f6df2faf87d83771657b80d0d9be5de192a3bfb2bedfb9b29c51cad60'
}
for path,digest in protected.items(): assert sha(Path(path))==digest,path
sources=[]
for p in sorted((PREVIOUS/'sources').glob('*.pdf')):
 sources.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,status='Reused primary-source reading from dossier audit; not newly downloaded'))
for n in ['erasure-1997.pdf','winter-2016.pdf','wilde-qi-2018.pdf']:
 p=PREVIOUS/'reviewed-input'/n
 assert p.exists(),p
 sources.append(dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size,status='Reused primary-source reading from dossier audit'))
write('source-register.json',dict(generated_at=now,reused_sources=sources,new_source=json.loads((OUT/'new-source.json').read_text()),bibliographic_checks=[
 dict(reference=4,url='https://epubs.siam.org/doi/10.1137/S0040585X97980415',finding='English edition 48(2), 243-255 (2004); manuscript pages 359-374 belong to Russian edition. Correct published title: Entanglement-Assisted Capacities of Constrained Quantum Channels.'),
 dict(reference=5,url='https://www.mathnet.ru/eng/ppi2099',author_confirmation='https://homepage.mi-ras.ru/~msh/list_e.html',finding='Journal title: On classical capacities of infinite-dimensional quantum channels. Preprint title in manuscript is genuine. DOI 10.1134/S003294601301002X; same journal year and pages.')]))

reproduction=json.loads((OUT/'reproduction-results.json').read_text())
assessment={
 'title':manifest['title'],'local_version':'manuscript-1','canonical_sha256':actual['main.pdf']['sha256'],
 'artifact_hashes':actual,'assessed_at':now,'provider':'OpenAI','model_id':None,
 'requested_model':'gpt-6-astra','requested_reasoning_effort':'xhigh','runtime_model_attested':False,
 'independence':'involved_in_manuscript','provenance':'Same involved reviewer as the candidate/dossier audit and earlier research line. Continued full-manuscript review, not blind or an additional independent vote. No subagents used.',
 'recommendation':'accept','recommendation_detail':'Scientific content accepted; two nonblocking bibliographic copyedits are recorded. No publication authorization is implied.',
 'technical_quality_score':9.0,'technical_quality_scale':'0-10; rigor, completeness, operational precision and reproducibility, separately from impact.',
 'millennium_score':4.0,'importance_airr_score':4.0,'importance_label':'strong','overall_stars':4,
 'score_scale_source':r'D:\Proyectos\airr-publicacion\scripts\prepare_model_assessment.py',
 'score_scale_source_sha256':sha(Path(r'D:\Proyectos\airr-publicacion\scripts\prepare_model_assessment.py')),
 'score_rationale':{'technical':'Correct exact finite-dimensional reduction, explicit entropy and energy control, full-environment operational definitions, valid regularization and uniform partner argument. Reproduction and visual inspection passed; minor bibliographic defects remain.',
 'importance':'Useful uniform extension to arbitrary finite-energy reset states with coherences and an arbitrary finite-dimensional classical partner. The four asymptotics share one reduction and use established coding/continuity machinery; the vacuum mechanism is already close in Catalano et al. No exact finite-energy capacities, Gaussian thermal-loss result or field-changing application is established.'},
 'criteria':{
 'correctness_confidence':{'stars':5,'basis':'No unresolved material objection after checking every stated proof, boundary regimes and applicable coding hypotheses; numerical checks support identities but are not proofs.'},
 'rigor':{'stars':5,'basis':'Finite reference dimension, exact diamond factor, cost slack, limit order, security environment and finite-entropy requirements are explicit.'},
 'novelty':{'stars':3,'basis':'Plausible new uniform arbitrary-reset extension and partner transfer; close vacuum antecedents acknowledged. No exhaustive priority certification.'},
 'significance':{'stars':3,'basis':'Strong specialized asymptotic result with quantitative bounds. Does not determine finite-energy capacities or settle general additivity.'},
 'reproducibility':{'stars':5,'basis':'Frozen PDF/TeX/ZIP verified; supplement reproduces exactly except timestamp; independent 90-digit table check and seven-page visual inspection pass.'}},
 'summary':'The exact seven-page manuscript establishes absolute high-energy erasure-capacity asymptotics for four operational capacities of unflagged oscillator reset channels with arbitrary finite-energy reset states, uniformly for bounded reset energy, plus a uniform classical additivity-defect bound. The scientific claims are supported. Correct the Holevo journal pagination/title and distinguish the Holevo-Shirokov journal title from its arXiv title.',
 'strengths':[
 'Exact half-diamond distance equals (1-lambda) Tr(Pi tau), valid for coherent resets and arbitrary references.',
 'Shifted truncated geometric inputs preserve Gibbs entropy up to absolute o(1), with explicit finite-energy bounds.',
 'Operational definitions and source hypotheses exclude confusion with public-discussion key capacity, peak input cost and Gaussian attenuation.',
 'Direct survival-pattern proof gives a partner bound uniform over all finite-dimensional partners after regularization.',
 'Nearby vacuum results are explicitly attributed and no finite-energy equality Q=P is claimed.'
 ],
 'weaknesses':[
 'Two minor bibliography metadata issues; source identities and required results are nevertheless identifiable.',
 'Current quantitative construction is not asserted optimal or efficiently implementable.',
 'Novelty evidence is limited to the primary sources inspected; impact beyond this specialized channel family is unestablished.',
 'This reviewer participated in prior auditing; no blind or independent additional assessment is present.'
 ],
 'potential_errors':[
 {'id':'E1','severity':'minor_editorial','location':'p.7 reference [4]','finding':'English journal citation uses Russian-edition pages 359-374.','correction':'A. S. Holevo, Entanglement-Assisted Capacities of Constrained Quantum Channels, Theory Probab. Appl. 48(2), 243-255 (2004), DOI 10.1137/S0040585X97980415.','main_claim_affected':False},
 {'id':'E2','severity':'minor_editorial','location':'p.7 reference [5]','finding':'Preprint title is combined with journal metadata.','correction':'Use journal title On classical capacities of infinite-dimensional quantum channels, Problems Inform. Transmission 49(1), 15-31 (2013), DOI 10.1134/S003294601301002X, or explicitly label the preprint-title variant.','main_claim_affected':False}],
 'strong_novelty_candidates':['Uniform absolute four-capacity asymptotics for arbitrary bounded-energy reset states, including number-basis coherences.','Explicit transfer to vanishing classical additivity defect uniformly over every finite-dimensional partner.'],
 'unresolved_material_objections':[],
 'mathematical_revisions_required':[],
 'optional_improvements':['Specify [4, Proposition 3] at the classical regularization step.','Pin version-specific arXiv links, particularly Catalano v2.'],
 'operational_formulation_sufficient':True,
 'theorem_citations_sufficient':True,
 'citation_metadata_corrections_required':['E1','E2'],
 'claim_audit':[
 {'claim':'Lemma 2 exact diamond distance and Markov bound','status':'valid'},
 {'claim':'Proposition 3 finite-cost achievable bounds','status':'valid'},
 {'claim':'Proposition 4 energy-constrained erasure upper bounds','status':'valid'},
 {'claim':'Lemma 5 shifted geometric entropy and strict cost','status':'valid'},
 {'claim':'Theorem 1 absolute asymptotics and bounded-reset-energy uniformity','status':'valid'},
 {'claim':'Thermal-tail O_M(log N/N) refinement','status':'valid; c fixed as a function of M with c ln(1+1/M)>2'},
 {'claim':'Theorem 6 uniform arbitrary finite partner defect','status':'valid'},
 {'claim':'Corollary 7 positivity for every N>0 iff lambda>1/2','status':'valid under stated block-mean cost'},
 {'claim':'Corollary 8 non-entanglement-breaking for every lambda>0 and any density tau','status':'valid; only trace class needed'}],
 'reproduction':{'all_fields_identical_except_generated_at':True,'random_cases':200,'summary':reproduction['summary'],'table_rows_checked':6,'table_values_checked':18,'table_precision_digits':90,'all_upward_rounding_correct':True,'certified_interval_arithmetic':False},
 'visual_review':{'pages':7,'pages_inspected':[1,2,3,4,5,6,7],'render_dpi':100,'status':'pass','observations':'All formulas and references legible; no clipping, overlap or unresolved citations observed. Original PDF not recompiled or edited.'},
 'limitations':['No formal proof certification.','No human peer review or additional independent reviewer.','No exhaustive literature/priority certification.','No finite-N capacity solution, optimal convergence rate, efficient code or two-way capacity.','No claim for reset energy growing with N, Gaussian thermal loss, memory or input-dependent reset.'],
 'published':False,'deposited':False,'inputs_modified':False,
 'durable_archive':str(ARCHIVE)
}
write('assessment.json',assessment)
write('visual-review.json',assessment['visual_review'])
write('integrity-results.json',dict(checked_at=now,inputs_unchanged=True,artifact_manifest_valid=True,supplement_manifest_valid=True,protected_previous_files=protected,protected_previous_files_unchanged=True))
files=[]
for p in sorted(OUT.rglob('*')):
 if p.is_file() and p.name not in ['hash-inventory.json','archive-verification.json']:
  files.append(dict(path=p.relative_to(OUT).as_posix(),bytes=p.stat().st_size,sha256=sha(p)))
write('hash-inventory.json',dict(created_at=now,root=str(OUT),reviewed_pdf_sha256=actual['main.pdf']['sha256'],files=files,excluded_self_referential_files=['hash-inventory.json','archive-verification.json']))
assert not ARCHIVE.exists(), 'Archive already exists; do not overwrite frozen reviews'
ARCHIVE.parent.mkdir(parents=True,exist_ok=True)
shutil.copytree(OUT,ARCHIVE)
verified=[]
for p in sorted(OUT.rglob('*')):
 if p.is_file():
  q=ARCHIVE/p.relative_to(OUT)
  assert q.is_file() and sha(p)==sha(q),str(q)
  verified.append(dict(path=p.relative_to(OUT).as_posix(),sha256=sha(p)))
for path,digest in protected.items(): assert sha(Path(path))==digest,path
assert actual=={p.name:dict(bytes=p.stat().st_size,sha256=sha(p)) for p in INPUT.iterdir()}
verification=dict(checked_at=datetime.now(timezone.utc).isoformat(),source=str(OUT),archive=str(ARCHIVE),files_verified=len(verified),all_files_match=True,files=verified,inputs_unchanged=True,previous_protected_files_unchanged=True,active_C_workspace_preserved=True)
write('archive-verification.json',verification)
shutil.copy2(OUT/'archive-verification.json',ARCHIVE/'archive-verification.json')
assert sha(OUT/'archive-verification.json')==sha(ARCHIVE/'archive-verification.json')
print(json.dumps(dict(recommendation=assessment['recommendation'],technical_score=9.0,importance_airr=4.0,verified_files=len(verified),archive=str(ARCHIVE),report_sha256=sha(OUT/'manuscript-review.txt'),assessment_sha256=sha(OUT/'assessment.json'),inventory_sha256=sha(OUT/'hash-inventory.json'),archive_verification_sha256=sha(OUT/'archive-verification.json')),ensure_ascii=False,indent=2))
