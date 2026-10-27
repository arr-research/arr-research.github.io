"""Format the closed review958 once; no manuscript parsing or scientific review."""
import sys
sys.dont_write_bytecode = True
import copy
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(r'C:\Trabajo\airr\2026-10-27_sharp967-binding')
DEST = Path(r'D:\Proyectos\airr-investigacion\2026-10-27_sharp967-binding')
OLD_C = Path(r'C:\Trabajo\airr\2026-10-27_sharp958-review')
OLD_D = Path(r'D:\Proyectos\airr-investigacion\2026-10-27_sharp958-review')
REPO = Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026')
PAPER = REPO / 'papers/2026/10/0J/ARR-2026-0JN84GQ1MD8FW9WR'
INPUT = Path(r'C:\Trabajo\airr\2026-10-27_sharp957-input')
PDF_HASH = '5542d2507f1dea4bf09ffa69353a3643e211ea92eb07de4c4d75fb463c363d10'
EXPECTED = {
    'REVIEW958.txt': '1111a2c566797acefd994b5ecc4f565c526bb9bff7d9477328dacb9c74423c07',
    'verdict958.json': 'e967a424fdc2d7a1921835a2e43313be96ae77c1d98652cf607727871b2aae65',
    'MANIFEST958.sha256': '9063c90786b4a7d10a3c8f7992e19be6683a3c6815d2becfeacdffd124620270',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_json(name, value):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def inventory(root):
    return {p.relative_to(root).as_posix(): {'bytes': p.stat().st_size, 'sha256': sha(p)}
            for p in sorted(root.rglob('*')) if p.is_file()}

def verify_original(root):
    for name, digest in EXPECTED.items():
        assert sha(root / name) == digest, (root, name)
    entries = 0
    for line in (root / 'MANIFEST958.sha256').read_text(encoding='utf-8').splitlines():
        digest, relative = line.split('  ', 1)
        assert sha(root / relative) == digest, (root, relative)
        entries += 1
    assert entries == 46
    return inventory(root)

def finding(item):
    prefix = f"{item['id']} (pp. {', '.join(map(str, item['pages']))})"
    extra = '; '.join(str(item[k]) for k in ('location', 'status') if k in item)
    return prefix + (f' [{extra}]' if extra else '') + ': ' + item['text']

assert not (OUT / 'model-response.json').exists(), 'Do not overwrite an earlier serialization.'
before_c = verify_original(OLD_C)
before_d = verify_original(OLD_D)
assert before_c == before_d and len(before_c) == 48
for path in (INPUT / 'manuscript.pdf', PAPER / 'paper.pdf'):
    assert path.stat().st_size == 289572 and sha(path) == PDF_HASH
assert sha(INPUT / 'INPUT957.json') == '544bfcc12da120b32004613b94a5fb819aed74c449227b7e839a96e3d541aaeb'

metadata_raw = (PAPER / 'metadata.json').read_bytes()
metadata = json.loads(metadata_raw)
assert metadata['version_id'] == 'arr:version:b9419be9-9f6f-4b44-a158-5b44755620b7'
assert metadata['integrity']['canonical_sha256'] == PDF_HASH
assert metadata['deposit']['submission_id'] == 'SUB-835C8FD66D10163D'
assert metadata['source_of_truth'] == 'paper.pdf'
verdict = json.loads((OLD_D / 'verdict958.json').read_text(encoding='utf-8'))
receipt958 = json.loads((OLD_D / 'DELIVERY958.json').read_text(encoding='utf-8'))
assert (verdict['scientific_importance_airr_0_10'], verdict['millennium_score'],
        verdict['technical_quality_0_10'], verdict['recommendation_original']) == (4.0, 4.5, 8.5, 'minor_revision')
o1, = verdict['unresolved_material_objections']
assert o1['id'] == 'O1' and o1['severity'] == 'revision_required_not_fatal'
assert verdict['unresolved_material_correctness_objections'] == []
timestamp = datetime.now(timezone.utc).isoformat()

sys.path.insert(0, str(REPO / 'scripts'))
import assessmentlib
from arrlib import Paper

o1_text = (f"O1 (pp. {', '.join(map(str, o1['pages']))}); etiqueta original: "
           f"unresolved_material_objections; type: {o1['type']}; severity: {o1['severity']}. "
           f"{o1['text']} Fuente: {o1['source']}. "
           "Sigue pendiente; revisión bibliográfica menor no bloqueante según la aclaración de formato967.")
summary = (
    'Serialización posterior del mismo informe958 sobre el PDF exacto, sin nueva evaluación ni voto. '
    'Millennium_score global: 4.5/10; importancia científica AIRR: 4.0/10; calidad técnica: 8.5/10, '
    'juicios distintos y sin promedio automático. Recomendación ORIGINAL: minor_revision. '
    'Coeficiente exacto y testigo separable constituyen el núcleo; aplicaciones correctas de alcance especializado. '
    'No se halló error matemático sustantivo en la revisión original. '
    'O1 sigue pendiente en weaknesses con texto, severidad y etiqueta originales; se aclara como revisión '
    'bibliográfica menor no bloqueante. La lista nativa vacía no significa que O1 se haya resuelto. '
    'assessed_at fecha esta serialización y prompt_version sólo su formato posterior ARR-ASSESS-1.0. '
    'Se solicitó GPT-6 Astra xhigh; model_id e independencia unknown, sin atestación de identidad/esfuerzo efectivos, '
    'aislamiento o ceguera técnica. Contexto nuevo declarado y filesystem compartido; participación previa de '
    'Codex declarada en p. 8. Contaminación incidental por un resultado secundario sobre otro paper y fallo '
    'numérico propio diagnosticado se conservan en original958 y BINDING967. Búsqueda original no exhaustiva; '
    'sin nueva búsqueda ni lectura científica. No es decisión editorial ni Accepted, ni completa el gate de dos modelos.'
)
response = {
    'paper_id': metadata['id'], 'version': metadata['version'], 'version_id': metadata['version_id'],
    'canonical_sha256': PDF_HASH, 'provider': 'OpenAI', 'model_id': 'unknown',
    'assessed_at': timestamp, 'prompt_version': assessmentlib.PROMPT_VERSION,
    'independence': 'unknown', 'recommendation': verdict['recommendation_original'],
    'millennium_score': verdict['millennium_score'],
    'overall_stars': assessmentlib.expected_stars(verdict['millennium_score']),
    'criteria': copy.deepcopy(verdict['criteria']), 'summary': summary,
    'strengths': [finding(x) for x in verdict['strengths']],
    'weaknesses': [finding(x) for x in verdict['weaknesses']] + [o1_text],
    'potential_errors': [finding(x) for x in verdict['potential_errors']],
    'strong_novelty_candidates': [finding(x) for x in verdict['strong_novelty_candidates']],
    'unresolved_material_objections': [],
}
write_json('model-response.json', response)

paper = Paper(PAPER, metadata)
normalized = assessmentlib.normalize_model_response(response)
errors = assessmentlib.validate_assessment(normalized, [paper])
literal = copy.deepcopy(response)
literal['unresolved_material_objections'] = [o1_text]
literal_errors = assessmentlib.validate_assessment(assessmentlib.normalize_model_response(literal), [paper])
write_json('controls/VALIDATION967.json', {
    'recorded_at': timestamp,
    'method': 'assessmentlib.normalize_model_response then validate_assessment, in memory, actual selected metadata',
    'normalized_uuid': 'ephemeral validation only; discarded; not registered or delivered as a second assessment',
    'faithful_projection_errors': errors,
    'literal_list_copy_expected_errors': literal_errors,
    'literal_list_copy_status': 'incompatible, retained as diagnostic; no recommendation change',
    'summary_characters': len(summary), 'o1_weakness_characters': len(o1_text),
    'source_response_sha256': assessmentlib.source_hash(response),
    'raw_json_sha256': sha(OUT / 'model-response.json'),
    'source_response_hash_definition': 'SHA256 of sorted compact UTF-8 canonical JSON as implemented by assessmentlib; distinct from raw-file hash',
    'registry_read': False, 'registry_written': False, 'manuscript_parsed_or_reevaluated': False,
})
assert not errors, errors
assert literal_errors == ['recommendation: unresolved material objections require major_revision or reject'], literal_errors

(OUT / 'original958').mkdir(parents=True, exist_ok=True)
for name in (*EXPECTED, 'DELIVERY958.json'):
    shutil.copyfile(OLD_D / name, OUT / 'original958' / name)
(OUT / 'evidence').mkdir(parents=True, exist_ok=True)
(OUT / 'evidence/metadata-at-binding967.json').write_bytes(metadata_raw)

notice = (
    'Esta es una representación posterior del único informe958 ya cerrado, no otra evaluación o voto. '
    'Su recomendación ORIGINAL sigue siendo minor_revision. En el original, O1 aparece en '
    'unresolved_material_objections con severity revision_required_not_fatal y type prior_art_comparison. '
    'El autor de esta misma revisión aclara que era una revisión bibliográfica menor pendiente y no bloqueante, '
    'coherente con la recomendación y la ausencia de objeciones materiales de corrección. '
    'El contrato ARR-ASSESS-1.0 exige major_revision o reject cuando su lista de objeciones materiales no está vacía; '
    'para esta proyección esa lista se interpreta como objeciones bloqueantes. O1 se conserva íntegramente en '
    'weaknesses, incluida su etiqueta original y severidad: no se borra, resuelve, minimiza su prioridad provisional '
    'ni se reescribe el informe original. Texto original exacto de O1: ' + o1['text'] +
    ' Fuente original: ' + o1['source'] + '. '
    'La aclaración concierne a la compatibilidad del formato; no aplica una evaluación científica nueva. '
    'assessed_at es la fecha de serialización, no una nueva fecha de examen del manuscrito; prompt_version '
    'describe únicamente este formato posterior, no el prompt usado para el informe958. '
    'No se ha atestado modelo efectivo, esfuerzo efectivo, independencia, aislamiento o ceguera técnica.'
)
binding = {
    'schema': 'local-review-format-binding-967-v1', 'binding_id': 'binding967', 'serialized_at': timestamp,
    'scope': 'format_and_provenance_of_same_closed_review958_only',
    'new_scientific_assessment': False, 'new_vote': False, 'reassessment': False,
    'output_protocol': 'ARR-ASSESS-1.0',
    'protocol_is_posterior_serialization_only': True,
    'assessed_at_semantics': 'serialization timestamp, not another scientific assessment',
    'local_manuscript_id': 'sharp957', 'original_review_id': 'review958',
    'submission_id': metadata['deposit']['submission_id'], 'paper_id': metadata['id'],
    'record_id': metadata['record_id'], 'version': metadata['version'], 'version_id': metadata['version_id'],
    'canonical_pdf': {'sha256': PDF_HASH, 'bytes': 289572, 'pages_from_original_review': 9,
                      'input_path': str(INPUT / 'manuscript.pdf'), 'deposit_path': str(PAPER / 'paper.pdf'),
                      'hash_only_checked_during_binding': True, 'content_not_reread': True},
    'deposit_context': {
        'basis': 'parent assignment and selected metadata; no additional authorization attestation',
        'licenses_as_observed': metadata['licenses'],
        'exact_pdf_public_release_sha256': metadata['deposit']['public_release_sha256'],
        'founder_conflict_as_observed': metadata['editorial']['conflicts'],
        'status_at_binding': metadata['status'], 'editorial_decision_at_binding': metadata['editorial']['decision'],
    },
    'original958': {
        'review_date': verdict['review_date'], 'original_receipt_time': receipt958['utc'],
        'source_C': str(OLD_C), 'source_D': str(OLD_D),
        'files': {name: before_d[name] for name in (*EXPECTED, 'DELIVERY958.json')},
        'copied_original_files_are_byte_identical': True,
        'full_original_manifest_verified_entries': 46,
        'full_original_C_D_files_compared': 48,
        'full_original_controls_readings_incidents_remain_preserved_at_source_paths': True,
        'original_public_identifiers_remain_null': True,
        'public_identifiers_in_this_projection_read_from_current_metadata_only': True,
        'original_files_modified': False,
    },
    'unchanged_judgment': {
        key: copy.deepcopy(verdict[key]) for key in (
            'scientific_importance_airr_0_10', 'scientific_importance_basis', 'millennium_score',
            'millennium_score_basis', 'technical_quality_0_10', 'technical_quality_basis',
            'criteria', 'recommendation', 'recommendation_original', 'recommendation_basis', 'rubric')
    },
    'format_mapping': {
        'millennium_score_source': 'original millennium_score = 4.5, not scientific importance = 4.0',
        'technical_quality': 'original 8.5 remains distinct; no substitution into global score',
        'overall_stars': {'value': response['overall_stars'], 'basis': 'contract display rounding of 4.5; not another judgment or mean'},
        'criteria': 'all five stars and basis strings unchanged',
        'findings': 'original IDs, pages and text retained; location/status rendered as text where present',
        'o1': {
            'original_field_label': 'unresolved_material_objections',
            'original_object_unchanged': copy.deepcopy(o1),
            'original_scientific_status': 'still_pending',
            'format_interpretation': 'nonblocking_minor_bibliographic_revision',
            'destination_field': 'weaknesses', 'destination_index': 4,
            'destination_text_exact': o1_text,
            'native_unresolved_material_objections': [],
            'empty_native_list_means': 'no blocking objection under this serialization contract; not absence or resolution of original O1',
            'recommendation_original_preserved': True,
            'faithfulness_basis': 'original severity revision_required_not_fatal; original minor_revision; original absence of unresolved material correctness objections; no direct coverage of Theorem 2 found in original review',
        },
        'provenance_notice': notice,
    },
    'configuration_and_limits': {
        'provider_label': 'OpenAI', 'provider_label_basis': 'observed Codex product/assignment; no independent backend attestation',
        'model_id': 'unknown', 'independence': 'unknown',
        'requested_model': 'GPT-6 Astra', 'requested_reasoning_effort': 'xhigh',
        'observed_original_provenance_exact': copy.deepcopy(verdict['provenance_and_configuration']),
        'observed_original_verification_limits_exact': copy.deepcopy(verdict['verification_summary']),
        'runtime_provenance_field_omitted': 'no admissible operator/platform attestation supplied',
        'review_context_field_omitted': 'no verified isolation/memory controls evidence supplied',
        'configuration_is_not_attested': True,
        'binding_activity': 'same review author format clarification only; no PDF content reread, web search, new tests of scientific claims, subagents, publication or registry mutation',
    },
    'validation': {
        'file': 'controls/VALIDATION967.json', 'schema_errors': errors,
        'literal_unresolved_list_incompatibility_retained': literal_errors,
        'model_response_sha256': sha(OUT / 'model-response.json'),
        'model_response_canonical_source_hash': assessmentlib.source_hash(response),
        'assessmentlib_sha256': sha(REPO / 'scripts/assessmentlib.py'),
        'arrlib_sha256': sha(REPO / 'scripts/arrlib.py'),
        'ratinglib_sha256': sha(REPO / 'scripts/ratinglib.py'),
        'metadata_snapshot_sha256': hashlib.sha256(metadata_raw).hexdigest(),
        'snapshot_file': 'evidence/metadata-at-binding967.json',
        'normalization_only_in_memory': True,
        'public_assessment_id_assigned': False,
    },
    'admission_and_publication_limits': {
        'not_accepted': True, 'native_two_distinct_models_gate_completed': False,
        'no_second_model_or_independence_attestation_created': True,
        'no_registry_or_repository_modified_by_this_task': True,
        'no_publication_performed': True,
        'must_not_count_original_and_projection_as_two_reviews_or_votes': True,
    },
    'copy_C': str(OUT), 'copy_D': str(DEST),
}
write_json('BINDING967.json', binding)

after_c = verify_original(OLD_C)
after_d = verify_original(OLD_D)
assert before_c == after_c == before_d == after_d
for path in (INPUT / 'manuscript.pdf', PAPER / 'paper.pdf'):
    assert sha(path) == PDF_HASH and path.stat().st_size == 289572
for name in (*EXPECTED, 'DELIVERY958.json'):
    assert sha(OUT / 'original958' / name) == before_d[name]['sha256']
write_json('controls/INTEGRITY967.json', {
    'checked_at': datetime.now(timezone.utc).isoformat(),
    'original_review_files_before_and_after': after_d,
    'original_C_and_D_unchanged_and_equal': True,
    'reviewed_and_deposited_pdf_hashes_equal': PDF_HASH,
    'input_manifest_sha256': sha(INPUT / 'INPUT957.json'),
    'selected_metadata_snapshot_sha256': hashlib.sha256(metadata_raw).hexdigest(),
    'selected_metadata_current_sha256': sha(PAPER / 'metadata.json'),
    'metadata_changed_concurrently': metadata_raw != (PAPER / 'metadata.json').read_bytes(),
    'scope': 'Hash/byte integrity only. No scientific manuscript rereading or re-evaluation.',
})

payloads = inventory(OUT)
manifest = ''.join(f"{entry['sha256']}  {relative}\n" for relative, entry in sorted(payloads.items()))
(OUT / 'MANIFEST967.sha256').write_text(manifest, encoding='utf-8')
assert not DEST.exists(), 'Do not overwrite an existing preserved binding.'
DEST.mkdir(parents=True)
for path in sorted(OUT.rglob('*')):
    if path.is_file():
        target = DEST / path.relative_to(OUT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
assert inventory(OUT) == inventory(DEST)
delivery = {
    'closed_at': datetime.now(timezone.utc).isoformat(), 'binding_id': 'binding967',
    'original_review_id': 'review958', 'new_scientific_assessment': False,
    'paper_id': metadata['id'], 'version_id': metadata['version_id'], 'canonical_pdf_sha256': PDF_HASH,
    'scientific_importance_airr_0_10': 4.0, 'millennium_score': 4.5, 'technical_quality_0_10': 8.5,
    'recommendation_original': 'minor_revision',
    'model_response_sha256': sha(OUT / 'model-response.json'),
    'model_response_canonical_source_hash': assessmentlib.source_hash(response),
    'binding_sha256': sha(OUT / 'BINDING967.json'),
    'manifest_sha256': sha(OUT / 'MANIFEST967.sha256'),
    'original_report_sha256': EXPECTED['REVIEW958.txt'],
    'original_verdict_sha256': EXPECTED['verdict958.json'],
    'original_manifest_sha256': EXPECTED['MANIFEST958.sha256'],
    'manifest_entries': len(payloads), 'manifest_excludes': ['MANIFEST967.sha256', 'DELIVERY967.json'],
    'copy_C': str(OUT), 'copy_D': str(DEST),
    'copy_comparison': 'Every path, byte size and SHA256 identical; final receipt identically copied and checked.',
    'total_files_each_copy': len(payloads) + 2,
    'C_retained': 'Explicit request for matching C/D copies; no artifact exists only in C.',
    'schema_validation_errors': [],
}
write_json('DELIVERY967.json', delivery)
shutil.copyfile(OUT / 'DELIVERY967.json', DEST / 'DELIVERY967.json')
assert inventory(OUT) == inventory(DEST)
print(json.dumps(delivery, ensure_ascii=False, indent=2))
