from pathlib import Path
import json,hashlib,shutil,datetime
P=Path(__file__).resolve().parent
D=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_support1156-delta')
OLD=Path(r'C:\Trabajo\airr\2026-10-28_support1148-review');OLDD=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_support1148-review')
CIN=Path(r'C:\Trabajo\airr\2026-10-28_support1155');DIN=Path(r'D:\Proyectos\airr-investigacion\2026-10-28_support1155')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def put(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def inv(root):return {q.relative_to(root).as_posix():dict(bytes=q.stat().st_size,sha256=sha(q)) for q in sorted(root.rglob('*')) if q.is_file()}
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
v=read(P/'source1148/verdict1148.json');val=read(P/'VALIDATION1156.json');initial=read(P/'INPUT-INITIAL1156.json')
assert val['all_automated_passed'] and val['PDF_text_changed_pages']==[6]
assert len([r for r in val['pixel_comparison'] if r['identical_pixels']])==14
assert (P/'OBSERVED-DELTA1156.diff').read_text(encoding='utf-8')==(P/'input/CHANGE1155.diff').read_text(encoding='utf-8')
oldinv=inv(OLD);assert oldinv==inv(OLDD) and len(oldinv)==435
for r in read(OLD/'MANIFEST1148.json')['files']:assert oldinv[r['path']]==dict(bytes=r['bytes'],sha256=r['sha256'])
assert sha(OLD/'REVIEW1148.txt')==v['report']['sha256']=='bda1b7625f92a44f7dd23eeac524929b4f485d518e977a015276b3f6ef2493f8'
assert sha(OLD/'verdict1148.json')=='a00ba996be7defcd9230f34fb0398fd9673cbf521907a8a3c28a39911aba5c1c'
assert inv(CIN)==inv(DIN)==inv(P/'input')==initial['files']
put('INPUT-FINAL1156.json',dict(utc=utc(),all_passed=True,current24files_C_D_and_own_copy_exact=True,previous435files_C_D_and_manifest_pass=True,previous_report_sha256=sha(OLD/'REVIEW1148.txt'),previous_verdict_sha256=sha(OLD/'verdict1148.json'),current_files=inv(CIN),previous_manifest_sha256=sha(OLD/'MANIFEST1148.json')))
o1=next(o for o in v['objections'] if o['id']=='O1')
delta=dict(format='Limited corrective continuation1156 of review1148; not native ARR registration',checked_at=utc(),operation='O1correction_and_exactPDFbinding_only',new_full_scientific_review=False,additional_vote=False,regrade=False,source_review=dict(report='source1148/REVIEW1148.txt',report_sha256=sha(P/'source1148/REVIEW1148.txt'),verdict='source1148/verdict1148.json',verdict_sha256=sha(P/'source1148/verdict1148.json'),original_assessed_at=v['assessed_at'],original_PDF_sha256=v['artifact']['pdf_sha256'],original_recommendation=v['recommendation']),corrected_artifact=dict(title=v['artifact']['title'],author=v['artifact']['author'],pdf_sha256=val['new_pdf_sha256'],bytes=422006,pages=15,main_tex_sha256=sha(P/'input/main.tex'),general_section_sha256=sha(P/'input/sections/general-support.tex'),manifest_sha256=sha(P/'input/MANIFEST1155.json')),O1_original=o1,O1_resolution=dict(status='resolved',exact_change=val['semantic_source_changes'],basis='Explicit only-for-n>=3 qualification removes nonexistent n2mode. For n>=3,n²-3n+1>=1 and alpha,epsilon>0 imply displayed positivity.',main_theorems_or_controls_changed=False),remaining_objections_unchanged=[o for o in v['objections'] if o['id']!='O1'],unresolved_material_objections=[],same_judgment_applies_to_corrected_PDF=True,application_basis='Complete1148inspection of exact203dPDF plus verified unique scientific delta and14unchangedpixelpages; this is not a new complete inspection of1155.',scores_from_original_unchanged={k:v[k] for k in ['scientific_importance_airr_0_10','overall_millennium_0_10','technical_quality_0_10','overall_whole_star_display']},score_definitions=v['definitions'],score_bases=v['bases'],criteria_from_original_unchanged=v['criteria_1_5'],score_recalculation=False,scientific_position_after_condition_satisfied='Recommend publication within declared scope; original sole minor correction satisfied. Not editorial acceptance or a new independent recommendation/vote.',requested_configuration=v['requested_configuration'],observed_configuration=v['observed_configuration'],context=v['context'],scope=dict(page6_visually_inspected=True,source_delta_verified=True,all15page_text_and_pixel_comparison=True,all15pages_scientifically_rereviewed=False,section6_byte_identical=True,new_bibliographic_search=False,new_scientific_control_campaign=False,CQ1152_read_or_evaluated=False,own_original_compile=False),incidents_and_adverses='Original1148dossier and copied report/verdict/incidents/OWNoutput retained unchanged; no adverse deletion.',report_sha256=sha(P/'DELTA1156.txt'),native_ID_generated=False,publication=False,editorial_acceptance=False)
put('DELTA1156.json',delta)
put('INCIDENTS1156.json',dict(utc=utc(),execution_errors=[],format_observation=dict(detail='main.tex converted398CRLFtoLF in supplied corrected source; normalized content differs only by authorized qualification.',source_line_endings=val['source_line_endings'],scientific_effect='none'),no_prior_incidents_erased=True,prior_incidents=dict(path='source1148/INCIDENTS1148.json',sha256=sha(P/'source1148/INCIDENTS1148.json')),no_restart_or_resampling=True))
put('PROVENANCE1156.json',dict(utc=utc(),operation='same-review corrective continuation',requested_configuration=v['requested_configuration'],observed_configuration=v['observed_configuration'],shared_context=v['context'],sources_C_D=[str(CIN),str(DIN),str(OLD),str(OLDD)],visual_inspection='Newpage6 viewed directly after ownrender;14otherpages compared pixelwise to authenticated1148renders. No fresh full scientific review claimed.',readings=['FREEZE1155.json','CHANGE1155.diff','ownsource/textdelta','changedpage6','originalO1andunchangedO2–O5 in1148report/verdict'],no_new_scientific_sources_or_models=True,no_native_ID_or_editorial_decision=True))
for q in P.glob('*.json'):read(q)
assert delta['scores_from_original_unchanged']==dict(scientific_importance_airr_0_10=7.0,overall_millennium_0_10=6.7,technical_quality_0_10=8.8,overall_whole_star_display=7)
assert all(c['stars']==4 for c in delta['criteria_from_original_unchanged'].values())
assert not D.exists() and not (P/'MANIFEST1156.json').exists() and not (P/'CLOSURE1156.json').exists()
payload=inv(P)
put('MANIFEST1156.json',dict(utc=utc(),payload_count=len(payload),scope='All delta dossier payloads, including copied immutable inputs and prior reports; excludes self and closure.',files=[dict(path=k,**r) for k,r in payload.items()],original_report_sha256=sha(OLD/'REVIEW1148.txt'),original_verdict_sha256=sha(OLD/'verdict1148.json'),corrected_PDF_sha256=val['new_pdf_sha256']))
shutil.copytree(P,D);assert inv(P)==inv(D)
put('CLOSURE1156.json',dict(utc=utc(),terminal=True,operation='limited_same1148review_O1continuation',C=str(P),D=str(D),payload_files=len(payload),total_files=len(payload)+2,C_D_byte_identical=True,report_sha256=sha(P/'DELTA1156.txt'),delta_json_sha256=sha(P/'DELTA1156.json'),manifest_sha256=sha(P/'MANIFEST1156.json'),new_input24_C_D_unchanged=True,old_review435_C_D_unchanged=True,O1_resolved=True,other_reservations_preserved=True,no_new_review_vote_or_score=True,no_editorial_acceptance_or_publication=True))
shutil.copy2(P/'CLOSURE1156.json',D/'CLOSURE1156.json')
ci=inv(P);assert ci==inv(D) and len(ci)==len(payload)+2
assert {k:r for k,r in ci.items() if k not in ['MANIFEST1156.json','CLOSURE1156.json']}==payload
assert inv(CIN)==inv(DIN)==initial['files'] and inv(OLD)==inv(OLDD)==oldinv
print(json.dumps(dict(terminal=True,C_D_identical_files=len(ci),payloads=len(payload),O1='resolved',report_sha256=sha(P/'DELTA1156.txt'),delta_json_sha256=sha(P/'DELTA1156.json'),manifest_sha256=sha(P/'MANIFEST1156.json'),closure_sha256=sha(P/'CLOSURE1156.json'))))
