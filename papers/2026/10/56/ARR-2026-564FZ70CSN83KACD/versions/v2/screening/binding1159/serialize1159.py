"""Serialization only of the immutable 1148 judgment and corrective continuation 1156.
Writes exclusively in the designated 1159 C: dossier; does not import a report into AIRR.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json
import shutil
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
REPO = Path(r'C:\Trabajo\airr-publicacion\reviewed-publications-20261026')
PAPER = REPO / 'papers/2026/10/56/ARR-2026-564FZ70CSN83KACD/versions/v2'
CBASE = Path(r'C:\Trabajo\airr')
DBASE = Path(r'D:\Proyectos\airr-investigacion')
SOURCES = {'1148': '2026-10-28_support1148-review', '1156': '2026-10-28_support1156-delta'}
EXPECTED = {
    '1148/REVIEW1148.txt': 'bda1b7625f92a44f7dd23eeac524929b4f485d518e977a015276b3f6ef2493f8',
    '1148/verdict1148.json': 'a00ba996be7defcd9230f34fb0398fd9673cbf521907a8a3c28a39911aba5c1c',
    '1156/DELTA1156.txt': '1b5dbe0aa81552187232d0fe7ab544ec0fecc0a819ec509be89b79a1a439ce0d',
    '1156/DELTA1156.json': '1bbed28e2e969e375440f5d2759a4b68d80efc70f567e75925923f47d3203d46',
}
PDF_SHA = '5cf3e9a66c6d86063d68b92bb0494bb5186a73506da60935819ff9d0265be361'
IDS = {'paper_id': 'ARR-2026-564FZ70CSN83KACD', 'version': 'v2',
       'version_id': 'arr:version:12e58b0b-3848-46ef-8dd1-656797e934f5'}

def utc():
    return datetime.now(timezone.utc).isoformat()

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def write(name, data):
    target = ROOT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def inventory(root):
    return [{'path': p.relative_to(root).as_posix(), 'bytes': p.stat().st_size, 'sha256': digest(p)}
            for p in sorted(root.rglob('*')) if p.is_file()]

def source_check():
    result = {}
    for number, name in SOURCES.items():
        c, d = CBASE / name, DBASE / name
        ic, id_ = inventory(c), inventory(d)
        assert ic == id_, f'Original C/D mismatch: {number}'
        manifest = read(d / f'MANIFEST{number}.json')
        table = {r['path']: r for r in ic}
        for row in manifest['files']:
            assert table[row['path']] == row, f'Original manifest mismatch: {number}/{row["path"]}'
        assert len(ic) == manifest['payload_count'] + 2
        assert set(table) == {r['path'] for r in manifest['files']} | {f'MANIFEST{number}.json', f'CLOSURE{number}.json'}
        result[number] = {'C': str(c), 'D': str(d), 'C_D_identical': True,
                          'file_count': len(ic), 'manifest_payload_count': manifest['payload_count'],
                          'files': ic}
    for key, expected in EXPECTED.items():
        number, filename = key.split('/')
        assert digest(DBASE / SOURCES[number] / filename) == expected, key
    return result

def metadata_check(metadata):
    assert metadata['id'] == IDS['paper_id']
    assert metadata['version'] == IDS['version']
    assert metadata['version_id'] == IDS['version_id']
    assert metadata['record_id'] == 'arr:record:a623fe70-3335-40e6-a637-b365287b12bd'
    assert metadata['source_of_truth'] == 'paper.pdf'
    assert metadata['integrity']['canonical_sha256'] == PDF_SHA
    assert metadata['integrity']['canonical_bytes'] == 422006
    assert (PAPER / 'paper.pdf').stat().st_size == 422006
    assert digest(PAPER / 'paper.pdf') == PDF_SHA

def main():
    assert not (ROOT / 'model-response.json').exists(), 'Do not overwrite an existing response or restart a judgment.'
    started = utc()
    initial = source_check()
    write('SOURCE-INTEGRITY-INITIAL1159.json', {'at': started, 'sources': initial, 'scope': 'Byte integrity only; no rerun of scientific checks.'})
    selected = {
        '1148': ['REVIEW1148.txt', 'verdict1148.json', 'INCIDENTS1148.json', 'PROVENANCE1148.json',
                 'READINGS1148.json', 'PRIOR-READINGS1128.json', 'REPRODUCTION1148.json', 'VALIDATION1148.json',
                 'OWN-FAILURE-INITIAL1148.json', 'OWN-FAILURE1148.json', 'OWN-DIAGNOSIS1148.json', 'OWN1148.json',
                 'MANIFEST1148.json', 'CLOSURE1148.json'],
        '1156': ['DELTA1156.txt', 'DELTA1156.json', 'INCIDENTS1156.json', 'PROVENANCE1156.json',
                 'VALIDATION1156.json', 'OBSERVED-DELTA1156.diff', 'MANIFEST1156.json', 'CLOSURE1156.json']
    }
    copied = []
    for number, names in selected.items():
        folder = ROOT / f'source{number}'
        folder.mkdir(exist_ok=True)
        for name in names:
            source = DBASE / SOURCES[number] / name
            target = folder / name
            shutil.copyfile(source, target)
            assert digest(source) == digest(target)
            copied.append({'source': str(source), 'copy': target.relative_to(ROOT).as_posix(), 'sha256': digest(target)})
    schema = ROOT / 'schema-snapshot'
    schema.mkdir(exist_ok=True)
    schema_receipt = []
    for name in ['assessmentlib.py', 'arrlib.py', 'ratinglib.py', 'prepare_model_assessment.py']:
        source, target = REPO / 'scripts' / name, schema / name
        shutil.copyfile(source, target)
        schema_receipt.append({'source': str(source), 'copy': target.relative_to(ROOT).as_posix(), 'sha256': digest(target)})
    sys.path.insert(0, str(schema))
    from assessmentlib import normalize_model_response, validate_assessment, source_hash
    from arrlib import Paper
    shutil.copyfile(PAPER / 'metadata.json', ROOT / 'metadata-initial1159.json')
    meta = read(ROOT / 'metadata-initial1159.json')
    metadata_check(meta)
    v = read(ROOT / 'source1148/verdict1148.json')
    delta = read(ROOT / 'source1156/DELTA1156.json')
    assert delta['same_judgment_applies_to_corrected_PDF'] is True
    assert delta['O1_resolution']['status'] == 'resolved'
    assert delta['corrected_artifact']['pdf_sha256'] == PDF_SHA
    assert delta['remaining_objections_unchanged'] == v['objections'][1:]
    assert v['recommendation']['value'] == 'minor_revision'
    assert v['scientific_importance_airr_0_10'] == 7.0
    assert v['overall_millennium_0_10'] == 6.7
    assert v['technical_quality_0_10'] == 8.8
    assert all(c['stars'] == 4 for c in v['criteria_1_5'].values())
    assert datetime.fromisoformat(v['assessed_at']) == datetime.fromisoformat(delta['source_review']['original_assessed_at'])
    now = utc()
    summary = (
        'Serialization only of the same judgment 1148 (2026-10-27T23:48:25Z UTC), '
        'with its limited corrective continuation 1156 (2026-10-27T23:55:15Z UTC). '
        'The full review concerned PDF 203d...; 1156 verified the sole O1 wording correction and binds that judgment to this exact v2 PDF. '
        'No new full review, scientific reading, controls, grading or additional vote occurred in 1159. '
        'Original minor_revision is preserved: O1 is resolved; accept serializes the already documented recommendation to publish within declared scope, not editorial acceptance. '
        'O2–O5 remain reservations. Importance 7.0/10, global Millennium 6.7/10 (7 stars), technical quality 8.8/10 and all five criteria 4/5 are unchanged, distinct judgments, not an average or correctness probability. '
        'OpenAI Codex participated in the project; shared context from 952 through 1128/1137/1148/1156 and shared filesystem, prior-score exposure and possible bias persist. '
        'GPT-6 Astra xhigh was requested only; effective identity, effort, isolation and independence are unattested; no fresh/blind or human review is claimed. '
        'The PDF §8 phrase about a still-required full assessment is historical: evidence is full 1148 plus limited delta 1156. '
        'assessed_at dates this serialization; ARR-ASSESS-1.0 is only the later format. Full original reports and all objections accompany the binding.'
    )
    criteria = copy.deepcopy(v['criteria_1_5'])
    for key, item in criteria.items():
        item['basis'] = 'Original 1148 basis, unchanged: ' + item['basis']
        if key == 'correctness_confidence':
            item['basis'] += ' Historical O1 is resolved by 1156; this is not a rerating.'
    weaknesses = [
        'O1 — historical minor scalar-domain error, p.6: ' + v['objections'][0]['statement'] + ' Evidence: ' +
        v['objections'][0]['evidence'] + ' It did not refute the states, fixed scaling or Theorem 6.1. '
        'Resolution recorded in 1156: the same sentence now says "only for n>=3" before "inactive eigenvalue". '
        'The original objection and original minor_revision remain in the source report; no formulas, controls or Section 6 changed.'
    ]
    for objection in v['objections'][1:]:
        weaknesses.append(
            f"{objection['id']} — {objection['severity']}; pp." + ','.join(map(str, objection['pages'])) +
            f". {objection['status']}. {objection['statement']} Evidence: {objection['evidence']} " +
            f"Preserve: {objection['requested_resolution']}"
        )
    potential_errors = [
        'Original 1148 uncertainty, unchanged: ' + v['potential_errors_or_uncertainties'][1],
        'Original 1148 uncertainty, unchanged: ' + v['potential_errors_or_uncertainties'][2],
        'Historical I1–I2: the first TeX read preceded the initial 312-file integrity completion (subsequently all passed). Truncated display was recovered; failed README.md lookup was corrected to README.txt. No input was changed or review restarted.',
        'Historical I3: the own equality-case checker had a chained-tolerance bug; Do-Di=7.784e-259 at 260 digits versus intended tolerance 1e-210. Split comparisons retained the same cases, parameters and tolerance. Initial failures, diagnosis, initial and repaired code remain in 1148; no scientific checker was rerun in 1159.',
        'Historical I4: replacement-channel Do=-4.7039e-262 was a numerical residual; exact value zero. It remains visible, not presented as physical negative divergence.',
        'Historical I5: first 1134 flagged protocol failure; 1136 Unicode/float-stochasticity/script-reconstruction, negative residual, selector and scale falsifiers; and 1126 malformed-output narrative correction remain preserved. No adverse case is removed by this projection.',
        'Historical I6/O4: previous scores were exposed and original narratives accessible; shared involved context, dependent code and reports give no fresh/blind, isolated, human, independent-library or statistically independent review guarantee. No runtime model or effort evidence is supplied.',
        'Original reproduction limits: 12 bounded checkers plus stated own exact/high-precision checks, not every archived script/platform; inherited integer libraries and diagnostics are not independent interval implementation or universal numerical proof. Full source packet authentication does not mean every historical line was read.',
        'O2/O3/O5 remain: directed partial primary reading, Lee–Makur 2024 full text uninspected, priority open; fixed-n/adaptive-effect/exact-support/rare-event/conditioning and quantum-input-denominator limitations; remote current-supplement access not validated by 1148 or 1159. No capacity, robust experiment or optimal cost claim follows.',
        'Binding limitation: 1156 was a limited O1 delta check, not a second full assessment of the corrected PDF. This serialization adds no scientific evidence. The historical §8 assessment-pending sentence is contextualized, not silently edited. Working-paper status and model-identification gates are not converted into editorial acceptance.'
    ]
    response = {
        **IDS, 'canonical_sha256': PDF_SHA, 'provider': 'OpenAI', 'model_id': 'unknown',
        'assessed_at': now, 'prompt_version': 'ARR-ASSESS-1.0', 'independence': 'involved_in_manuscript',
        'recommendation': 'accept', 'millennium_score': 6.7, 'overall_stars': 7,
        'criteria': criteria, 'summary': summary,
        'strengths': ['Original 1148 finding, unchanged: ' + s for s in v['strengths']],
        'weaknesses': weaknesses, 'potential_errors': potential_errors,
        'strong_novelty_candidates': [
            'Original 1148 candidate, unchanged: complete support criterion for every finite classical channel (n>=2), with the distinctions and known upper/tools attribution in the full report. Worldwide priority is not certified.',
            'Original 1148 candidate, unchanged: channel-independent faithful separable preparation and an adaptive binary measured positive-limit realization, uniform over zero-Doeblin channels only at fixed n. No uniformity in n, fixed measurement, robust experiment or optimal resource claim.'
        ],
        'unresolved_material_objections': []
    }
    write('model-response.json', response)
    normalized = normalize_model_response(response)
    errors = validate_assessment(normalized, [Paper(PAPER, meta)])
    # The normalization-only UUID is deliberately not saved or registered.
    structured_hash = source_hash(response)
    validation = {
        'at': utc(), 'operation': 'read-only official format validation; no scientific review',
        'actual_metadata_path': str(PAPER / 'metadata.json'),
        'metadata_snapshot_sha256': digest(ROOT / 'metadata-initial1159.json'),
        'actual_pdf_bytes': (PAPER / 'paper.pdf').stat().st_size, 'actual_pdf_sha256': digest(PAPER / 'paper.pdf'),
        'real_ids': IDS, 'schema_files': schema_receipt,
        'method': 'normalize_model_response then validate_assessment against Paper(actual version path, actual metadata). Official helper copied byte-for-byte; Python bytecode writes disabled.',
        'normalization_uuid': 'ephemeral in memory only; not persisted, imported, registered or used as an invented assessment identifier',
        'errors': errors, 'passed': not errors,
        'response_file_sha256': digest(ROOT / 'model-response.json'),
        'response_structured_sha256': structured_hash,
        'string_lengths': {'summary': len(summary), 'weaknesses': list(map(len, weaknesses)), 'potential_errors': list(map(len, potential_errors))},
        'new_scientific_execution_count': 0, 'native_repository_mutations': False,
        'scientific_scores_preserved': True, 'all_original_objections_preserved': True
    }
    write('VALIDATION-INITIAL1159.json', validation)
    if errors:
        raise ValueError('Preserved initial format validation failed: ' + repr(errors))
    mappings = {
        'paper_id/version/version_id/canonical_sha256': 'Copied from actual existing v2 metadata; PDF bytes independently hashed, matching delta 1156. No v1 IDs or earlier-PDF hash substituted.',
        'provider/model_id': 'OpenAI is the provided service identity; unknown preserves absence of attested effective runtime identity. Requested Astra is not an observed model identifier.',
        'independence': 'involved_in_manuscript records actual prior project participation. It is not a claim that statistical independence/isolation was measured.',
        'assessed_at': 'Serialization timestamp only. Original assessment timestamp and limited delta timestamp retained below and in summary; no additional judgment or vote.',
        'prompt_version': 'ARR-ASSESS-1.0 names the subsequent output format, not the prompt or protocol used to produce the historical full review.',
        'millennium_score/overall_stars': 'Original global 6.7 and its existing whole-star display 7; no averaging of criteria, no regrading.',
        'criteria': 'All original stars 4/5 and basis strings retained. Historical basis is labeled; correctness note only records the already completed O1 delta resolution. No new basis or rating.',
        'importance/technical_quality': 'Original separate 7.0/10 and 8.8/10 in summary and this binding because native model-response schema has no separate scalar fields for them.',
        'recommendation': 'accept maps the position already documented in 1156 after sole O1 minor correction was fulfilled. Original 1148 minor_revision remains intact. This is a scientific recommendation within declared scope, not Accepted status, editorial decision, new recommendation or additional vote.',
        'strengths/strong_novelty_candidates': 'Projection of original 1148 findings only; known prior tools/upper, open priority and resource/operational limits retained.',
        'weaknesses': 'O1 original claim and adverse example remain, with only its already documented 1156 correction. O2–O5 statements, evidence, status and requested limitations are retained as reservations; full objects and full original report accompany this projection.',
        'potential_errors': 'Preserves original uncertainty and I1–I6 adverse/procedural history, bounded reproduction, incomplete bibliographic reading, runtime/context and scope limits. No newly executed scientific checks claimed.',
        'unresolved_material_objections': 'Original empty material-objection list remains empty; retained moderate reservations are not silently relabeled as resolved.',
        'operator-controlled fields': 'No assessment_id, source_response_sha256, runtime_provenance, review_context, intake_source or fictitious case ID in model response. Operator may assign real registration fields later.'
    }
    binding = {
        'format': '1159 serialization and binding of one existing judgment, not a scientific reevaluation',
        'serialized_at': now, 'operation': 'format_and_real_version_binding_only',
        'new_full_review': False, 'new_scientific_readings': False, 'new_scientific_controls': False,
        'regrade': False, 'additional_vote': False, 'new_scientific_recommendation': False,
        'input_review': {'path': str(DBASE / SOURCES['1148']), 'assessed_at_as_original': v['assessed_at'],
                         'assessed_at_UTC_same_instant': delta['source_review']['original_assessed_at'],
                         'report_sha256': EXPECTED['1148/REVIEW1148.txt'], 'verdict_sha256': EXPECTED['1148/verdict1148.json'],
                         'original_pdf': v['artifact'], 'original_recommendation': v['recommendation']},
        'corrective_continuation': {'path': str(DBASE / SOURCES['1156']), 'checked_at': delta['checked_at'],
                                    'report_sha256': EXPECTED['1156/DELTA1156.txt'], 'json_sha256': EXPECTED['1156/DELTA1156.json'],
                                    'scope': delta['scope'], 'same_judgment_applies_to_corrected_PDF': True,
                                    'scientific_position_after_condition_satisfied': delta['scientific_position_after_condition_satisfied']},
        'actual_public_binding': {**IDS, 'record_id': meta['record_id'], 'canonical_sha256': PDF_SHA,
                                  'pdf_bytes': 422006, 'pages': delta['corrected_artifact']['pages'],
                                  'page_count_source': 'existing verified delta 1156; no new PDF reading/rendering',
                                  'metadata_path': str(PAPER / 'metadata.json'), 'metadata_snapshot': 'metadata-initial1159.json',
                                  'metadata_snapshot_sha256': digest(ROOT / 'metadata-initial1159.json'),
                                  'status_observed': meta['status'], 'source_of_truth': meta['source_of_truth']},
        'original_separate_judgments_unchanged': {
            'scientific_importance_airr_0_10': 7.0, 'overall_millennium_0_10': 6.7,
            'technical_quality_0_10': 8.8, 'overall_stars': 7,
            'definitions': v['definitions'], 'original_bases_unchanged': v['bases'],
            'all_criteria_original_unchanged': v['criteria_1_5'], 'averaged': False,
            'correctness_probability': None, 'historical_O1_basis_annotation': 'The original minor flaw is now resolved by 1156; no score recomputation.'},
        'original_O1_visible': v['objections'][0], 'O1_resolution_already_documented': delta['O1_resolution'],
        'O2_to_O5_unchanged_in_full': v['objections'][1:],
        'original_uncertainties': v['potential_errors_or_uncertainties'], 'original_limits': v['limits'],
        'requested_configuration': v['requested_configuration'], 'observed_configuration': v['observed_configuration'],
        'original_context': v['context'], 'additional_context_reused': ['1148', '1156'],
        'field_mapping': mappings,
        'historical_section8_notice': {
            'source': 'Parent clarification received during 1159; no new scientific or PDF reading',
            'phrase': 'The present exact PDF still requires a full assessment',
            'explanation': 'Historical pre-1148 wording. Actual evidence chain is full 1148 on PDF 203d0c2f... plus limited corrective continuation 1156 on PDF 5cf3e9a6.... Not a second complete or independent review of 1155.',
            'PDF_modified': False},
        'parent_reported_publication_context': {
            'submission': 'SUB-6FE1A863DE23202D', 'author_revision': 2,
            'scanner_clean_server_hash_and_permissions': 'reported by parent; not independently checked against server in this formatting task',
            'permission_UTC': '2026-10-28T00:00:22Z', 'founder_disclosure_UTC': '2026-10-28T00:00:43Z',
            'two_identified_model_gates': 'not satisfied according to assignment; this unknown-runtime involved judgment does not certify gates',
            'new_publication_by_this_task': False, 'editorial_acceptance': False},
        'copied_source_files': copied, 'schema_snapshot': schema_receipt,
        'original_dossier_inventory_receipt': 'SOURCE-INTEGRITY-INITIAL1159.json',
        'copy_scope': 'Selected original reports, original verdicts/provenance/readings/adverses copied byte-for-byte. Complete original 435-file 1148 and 59-file 1156 C/D dossiers remain intact and inventoried; this subset is not relabeled a complete copy.',
        'model_response': {'path': 'model-response.json', 'file_sha256': digest(ROOT / 'model-response.json'),
                           'structured_sha256': structured_hash, 'hash_distinction': 'File hash covers exact UTF-8 bytes; structured hash uses official canonical JSON.'},
        'native_registration_or_case_id_created': False,
        'scientific_audit1157_or_other_candidate_read': False,
        'originals_modified': False, 'Git_or_root_state_mutated': False, 'publication_performed': False
    }
    write('BINDING1159.json', binding)
    write('PROVENANCE1159.json', {
        'started_at': started, 'serialized_at': now, 'purpose': 'Faithful formatting and real v2 binding of same 1148 plus 1156 judgment',
        'requested_configuration_only': v['requested_configuration'], 'observed_configuration': v['observed_configuration'],
        'runtime_attestation': None, 'native_provider': 'OpenAI', 'native_model_id': 'unknown',
        'context': v['context'], 'current_continuation': ['1148', '1156', '1159'],
        'filesystem': 'shared; own work in C:, identical preservation in D:',
        'science_read_or_recomputed_this_task': False, 'new_agents_models_chats': False,
        'other_chats_read_or_messaged': False, 'format_validation_only': True,
        'source_inventory': 'SOURCE-INTEGRITY-INITIAL1159.json', 'original_source_hashes': EXPECTED,
        'metadata_and_schema_only_for_binding': True,
        'publication_or_registration': False, 'full_report_and_objections_must_remain_visible': True
    })
    write('INCIDENTS1159.json', {
        'at': utc(), 'new_scientific_incidents': [],
        'format_or_display_incidents': [{'id': 'S1', 'kind': 'read-only console truncation',
          'detail': 'An initial full metadata/combined output exceeded display context. Relevant actual IDs, status, source_of_truth, integrity hash and PDF hash recovered by bounded projection. No files were altered by these reads.'}],
        'historical_incidents_1148': read(ROOT / 'source1148/INCIDENTS1148.json'),
        'historical_incidents_1156': read(ROOT / 'source1156/INCIDENTS1156.json'),
        'no_adverse_removed': True, 'no_review_restart_or_resampling': True,
        'parent_section8_clarification': binding['historical_section8_notice']
    })
    (ROOT / 'BINDING1159.txt').write_text(
        '1159 — Serialización del mismo juicio 1148 + continuación correctiva 1156\n\n'
        'Este expediente no es una nueva evaluación, nueva nota ni voto adicional. El informe completo 1148 se conserva íntegro; '
        'su objeto fue el PDF 203d0c2f... . El cierre 1156 verificó únicamente la corrección O1 y justificó aplicar el mismo juicio al PDF corregido 5cf3e9a6... .\n\n'
        'La respuesta ARR-ASSESS-1.0 se vincula a ARR-2026-564FZ70CSN83KACD v2 y al version_id real de metadata.json. '
        'El PDF depositado local se ha cotejado por tamaño y SHA-256. No se ha vuelto a leer científicamente ni se han ejecutado controles científicos.\n\n'
        'Se mantienen importancia 7.0, valoración global Millennium 6.7 (presentación entera 7), calidad técnica 8.8 y cinco criterios 4/5. '
        'Son juicios distintos, no un promedio ni una probabilidad de corrección. Las bases originales permanecen completas en BINDING1159.json.\n\n'
        'La recomendación original minor_revision permanece en 1148. La única condición O1 se cumplió al insertar «only for n>=3» '
        'en la frase sobre el modo inactivo; accept codifica la recomendación científica ya documentada en 1156 de publicar dentro del alcance declarado. '
        'No significa Accepted ni decisión editorial. O1 original y su ejemplo adverso siguen visibles; O2–O5 permanecen íntegramente como reservas.\n\n'
        'La frase de §8 sobre evaluación todavía pendiente es histórica: la cadena es revisión completa 1148 más delta limitado 1156, '
        'sin nueva revisión completa independiente del PDF corregido. Se conserva el PDF sin editar.\n\n'
        'provider=OpenAI, model_id=unknown, independence=involved_in_manuscript. Astra xhigh fue configuración solicitada, no atestada. '
        'Contexto y filesystem compartidos, participación previa, exposición a notas y posible sesgo están declarados; '
        'identidad/esfuerzo/aislamiento/independencia efectivos siguen sin atestación.\n\n'
        'assessed_at fecha la serialización; las fechas originales de 1148 y 1156 se conservan. No se crea ni registra assessment ID/case ID. '
        'La comprobación oficial de esquema usa copias exactas del validador y el registro v2 real en modo lectura. '
        'El UUID que el normalizador oficial genera para validar solo existe transitoriamente en memoria y no se guarda.\n\n'
        'Los informes completos, veredictos, incidencias, lecturas y adversos seleccionados están copiados con los mismos bytes; '
        'los expedientes completos originales se verifican antes y después, permanecen inmutables y se referencian mediante inventarios. '
        'Esta carpeta es un encuadernado, no una copia integral de los 494 archivos de origen.\n', encoding='utf-8')
    print(json.dumps({'stage': 'serialization_written', 'validation_errors': errors, 'summary_chars': len(summary),
                      'response_file_sha256': digest(ROOT / 'model-response.json'), 'structured_sha256': structured_hash,
                      'binding_sha256': digest(ROOT / 'BINDING1159.json'), 'source_counts': {k: x['file_count'] for k,x in initial.items()}}, indent=2))

if __name__ == '__main__':
    main()
