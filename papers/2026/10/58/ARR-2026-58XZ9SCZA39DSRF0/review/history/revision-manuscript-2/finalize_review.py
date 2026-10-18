from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

O=Path(__file__).resolve().parent;I=O.parent/'input'
B=Path(r'D:\Proyectos\airr-investigacion\2026-10-18_escape-energetico');D=B/'revision-manuscript-2'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat()
initial=json.loads((O/'input-hashes-initial.json').read_text())
assert all(sha(I/n)==x['sha256'] for n,x in initial.items())
protected={
str(B/'revision-manuscript-1'/'manuscript-review.txt'):'c53e38583db3eea2ddde991b3c79a2fa178a90c1ceaa13592887918e721c36a4',
str(B/'revision-manuscript-1'/'assessment.json'):'c036b1d1b9f3ee83ea5c9e69b738940434619635eed388eb57624975ff2aedaa',
str(B/'revision-manuscript-1'/'hash-inventory.json'):'b416b7f38ba1b44289f299c8ec00b27fa67a0bdc7236562ee553d32f3b9d1b8c',
str(B/'revision-extension-1'/'audit-report.txt'):'11a1542e72d6d4a6c30644157cf83242214f7181ccac05cf1b7e0c6fb5572055',
str(B/'revision-extension-1'/'verdict.json'):'00d5cb5c3d7f9b6af38643af7cd3441a6808b1d8bd54f10c24717c679195658b',
str(B/'revision-extension-1'/'hash-inventory.json'):'c3551c5ca141f1be39174c83d7f86b9cec2af6913f8b08529cf0f3f49714a7a3',
str(B/'revision-dossier-1'/'audit-report.txt'):'5e49154cc6dd2e0d0ccb41c352de2af31b3acc0edd0a0ff1e2187a1ca821238c'}
for p,digest in protected.items():assert sha(Path(p))==digest,p
source_paths=[B/'revision-dossier-1'/'reviewed-input'/n for n in ['erasure-1997.pdf','winter-2016.pdf','wilde-qi-2018.pdf']]
source_paths += [B/'revision-dossier-1'/'sources'/n for n in ['holevo-shirokov-2012.pdf','zhong-oh-jiang-2022-v2.pdf','catalano-2026-v2.pdf','amosov-mancini-2009.pdf']]
source_paths += [B/'revision-manuscript-1'/'sources'/'holevo-2003-v2.pdf']
source_paths += [B/'revision-extension-1'/'reviewed-inputs'/n for n in ['davis-shirokov-wilde-2018.pdf','devetak-winter-2003.pdf']]
source_paths += [B/'revision-extension-1'/'sources'/n for n in ['bbps-1995.pdf','reverse-coherent-2008.pdf']]
write('source-register.json',dict(checked_at=now,scope='Primary-source readings from this same continued review, reused with file identification. This integration did not re-read every external proof.',sources=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)) for p in source_paths]))
scale=Path(r'D:\Proyectos\airr-publicacion\scripts\prepare_model_assessment.py')
assessment=dict(
 title='High-energy capacities and entanglement reversibility of quantum reset channels',local_version='manuscript-2',pages=10,
 canonical_sha256=initial['main.pdf']['sha256'],artifact_hashes=initial,assessed_at=now,
 provider='OpenAI',model_id=None,requested_model='gpt-6-astra',requested_reasoning_effort='xhigh',runtime_model_attested=False,
 independence='involved_in_manuscript',provenance='Same involved reviewer as prior manuscript and addendum audits. New exact-artifact assessment, not blind or an additional independent vote. No subagents used.',
 recommendation='accept',technical_quality_score=9.0,technical_quality_scale='0-10; technical quality, separately from scientific importance.',
 millennium_score=5.0,importance_airr_score=5.0,importance_label='very good',overall_stars=5,
 score_scale_source=str(scale),score_scale_source_sha256=sha(scale),
 score_rationale=dict(technical='The exact integrated manuscript has valid proofs, coherent operational definitions, correct infinite-entropy scope, explicit dependency hypotheses, reproducible quantitative evidence and a legible ten-page PDF. No material objection remains.',importance='The dimension-free flag bound yields four absolute-gap capacity limits for every fixed reset density, and finite reset entropy suffices for assisted limits and vanishing state irreversibility. This is a very good specialized extension with useful scope; its shared mechanisms and coding/dilution machinery are established, nearby vacuum cases are known, and exact finite-energy or general mixed-state reversibility problems remain unsolved.'),
 criteria={
 'correctness_confidence':dict(stars=5,basis='Every internal theorem and corollary was checked in its integrated form; no unresolved material objection. Previous numerical checks are reused only after byte-identity verification.'),
 'rigor':dict(stars=5,basis='Correct conditional-information directions and factors, finite decoded lower coding, erasure-based upper bounds, DSW cost convention, entropy-tail proof and order of limits.'),
 'novelty':dict(stars=3,basis='Plausible substantive all-density/finite-entropy extension and state-family consequence, with close vacuum and standard reverse-hashing antecedents acknowledged. No exhaustive priority certification.'),
 'significance':dict(stars=4,basis='A coherent set of six capacity asymptotics and a state-resource conclusion with absolute error control. Specialized channel family; no demonstrated field-shaping application or exact finite-energy solution.'),
 'reproducibility':dict(stars=5,basis='Frozen PDF/TeX/ZIP and delivery match. Both scripts and records are byte-identical to previously reproduced versions; 24 current table values match independent 110-digit evaluation; all ten pages visually checked.')},
 summary='The exact ten-page manuscript correctly derives absolute high-energy limits for four capacities of arbitrary fixed oscillator reset channels, two assisted limits for finite-entropy resets, and asymptotically vanishing irreversibility of an explicit family of distributed states. It preserves the required operational distinctions, acknowledges nearby and foundational results, and supports its quantitative table with reproducible calculations. Scientific acceptance is recommended.',
 strengths=[
 'Dimension-free binary hidden-branch loss avoids an invalid dimension-dependent limit for arbitrary infinite-entropy resets.',
 'Lower coding is finite and upper bounds act on erasure, so infinite output entropy of R is handled without undefined entropy differences.',
 'Finite-entropy pinching lemma connects reverse hashing to absolute assisted gaps without requiring finite reset energy.',
 'Explicit dilution upper bound proves the state-cost statement without assuming an infinite-dimensional convex-roof regularization theorem.',
 'Uniform finite-partner classical defect, endpoint behavior, mean input cost and absence of finite-N claims are explicit.',
 'Prior vacuum, feedback, hashing and dilution results are attributed; earlier bibliography corrections are incorporated.'
 ],
 weaknesses=[
 'Priority search is targeted rather than exhaustive, and most underlying information-theoretic tools are established.',
 'No exact finite-energy capacity, optimal convergence rate, efficient coding construction or general mixed-state reversibility theorem is obtained.',
 'Assisted/state conclusions for arbitrary infinite-entropy reset densities remain outside the proved scope.',
 'The reviewer is involved in prior auditing; this is not independent human peer review or formal verification.'
 ],
 potential_errors=[],unresolved_material_objections=[],mathematical_revisions_required=[],
 strong_novelty_candidates=[
 'Four absolute high-energy capacity limits for every fixed reset density with no finite entropy or mean energy assumption.',
 'Finite-entropy reset condition suffices for two assisted absolute limits and vanishing absolute E_C-E_D of the specified state family.',
 'Uniform arbitrary finite-partner classical defect transferred from erasure with explicit gap control.'
 ],
 optional_improvements=[
 'Repeat delta S(theta)=0 for epsilon=0 next to equation 24, for isolated readability.',
 'Specify Holevo Proposition 3 in the classical regularization citation.',
 'Optionally add Devetak-Winter journal publication details; the cited preprint is already sufficient.'
 ],
 claim_audit=[
 dict(label='Lemma 2',status='valid',claim='Exact half-diamond distance and reset tail bound'),
 dict(label='Lemma 3',status='valid',claim='Dimension-free hidden-branch information loss, quantum and classical'),
 dict(label='Propositions 4-5',status='valid',claim='Finite decoded coding lower bounds and erasure operational upper bounds'),
 dict(label='Lemma 6 and Theorem 1',status='valid',claim='Shifted geometric strict cost and entropy; four absolute limits for all density operators'),
 dict(label='Lemma 7',status='valid',claim='Finite-entropy selective tail lemma using pinching and lower semicontinuity'),
 dict(label='Theorem 8 and equation 25',status='valid',claim='Adaptive two-way capacities under DSW convention; reverse hashing and finite-energy uniform rate'),
 dict(label='Corollary 9',status='valid',claim='Physical and finite decoded state E_D/E_C absolute limits and vanishing gap'),
 dict(label='Theorem 10',status='valid',claim='Classical defect uniformly over all finite partners, with regularization on erasure'),
 dict(label='Corollaries 11-12',status='valid',claim='Positive unassisted Q/P iff lambda>1/2 at every positive mean cost; not entanglement breaking for lambda>0')],
 operational_formulation_sufficient=True,theorem_citations_sufficient=True,
 verification=dict(new_script_executions=0,reused_only_after_byte_identity=True,original_script_cases=200,new_script_cases=500,previous_independent_cases=480,table_values_checked=24,independent_table_precision_digits=110,all_roundings_correct=True,all_labels_and_citations_resolve=True,not_interval_certified=True),
 visual_review=json.loads((O/'visual-review.json').read_text()),
 limitations=['No formal proof certification or human independent review.','No global priority certification.','No finite-N capacities or fixed-N state reversibility.','No claim for all infinite-entropy resets in assisted/state results.','No local energy budget in the state-entanglement-cost convention.','Numerical diagnostics are finite and are not proofs of infinite-dimensional limits.'],
 published=False,deposited=False,inputs_modified=False,prior_reviews_modified=False,archive=str(D))
write('assessment.json',assessment)
write('integrity-results.json',dict(checked_at=now,all_current_inputs_unchanged=True,previous_protected_files=protected,previous_protected_files_unchanged=True,active_C_work_preserved=True))
files=[]
for p in sorted(O.rglob('*')):
 if p.is_file() and p.name not in ['hash-inventory.json','archive-verification.json']:
  files.append(dict(path=p.relative_to(O).as_posix(),bytes=p.stat().st_size,sha256=sha(p)))
write('hash-inventory.json',dict(created_at=now,reviewed_pdf_sha256=initial['main.pdf']['sha256'],files=files,excluded_self_referential_files=['hash-inventory.json','archive-verification.json']))
assert not D.exists(),'Do not overwrite frozen reviews'
D.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(O,D)
copied=[]
for p in sorted(O.rglob('*')):
 if p.is_file():
  q=D/p.relative_to(O);assert sha(p)==sha(q)
  copied.append(dict(path=p.relative_to(O).as_posix(),sha256=sha(p)))
for p,h in protected.items():assert sha(Path(p))==h
assert all(sha(I/n)==x['sha256'] for n,x in initial.items())
write('archive-verification.json',dict(checked_at=datetime.now(timezone.utc).isoformat(),source=str(O),archive=str(D),files_verified=len(copied),all_hashes_match=True,files=copied,inputs_unchanged=True,previous_reviews_unchanged=True,active_C_work_preserved=True))
shutil.copy2(O/'archive-verification.json',D/'archive-verification.json')
assert sha(O/'archive-verification.json')==sha(D/'archive-verification.json')
print(json.dumps(dict(recommendation='accept',technical_score=9.0,importance_airr=5.0,files_verified=len(copied),archive=str(D),report_sha256=sha(O/'manuscript-review.txt'),assessment_sha256=sha(O/'assessment.json'),inventory_sha256=sha(O/'hash-inventory.json')),ensure_ascii=False,indent=2))
