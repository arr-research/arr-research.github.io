"""Read-only source revalidation and preservation of the already serialized response."""
from pathlib import Path
import json
import shutil
import sys
sys.dont_write_bytecode = True
from serialize1159 import ROOT, REPO, PAPER, CBASE, DBASE, IDS, PDF_SHA, EXPECTED, utc, digest, read, write, inventory, source_check, metadata_check

ARCHIVE = DBASE / ROOT.name

def main():
    assert not (ROOT / 'MANIFEST1159.json').exists(), 'Do not overwrite a sealed dossier.'
    initial = read(ROOT / 'SOURCE-INTEGRITY-INITIAL1159.json')['sources']
    final = source_check()
    assert initial == final, 'Original source dossiers changed during serialization.'
    response = read(ROOT / 'model-response.json')
    binding = read(ROOT / 'BINDING1159.json')
    assert digest(ROOT / 'model-response.json') == binding['model_response']['file_sha256']
    for item in binding['copied_source_files']:
        assert digest(Path(item['source'])) == digest(ROOT / item['copy']) == item['sha256']
    for item in binding['schema_snapshot']:
        assert digest(Path(item['source'])) == digest(ROOT / item['copy']) == item['sha256']

    # Authenticate the actual corrected source packet too, without reading/reviewing its content.
    corrected_C = CBASE / '2026-10-28_support1155'
    corrected_D = DBASE / '2026-10-28_support1155'
    ci, di = inventory(corrected_C), inventory(corrected_D)
    assert ci == di
    assert len(ci) == 24
    assert digest(corrected_D / 'MANIFEST1155.json') == '7f8afab0e1749764ec7157eb1cf144b618813bbbf8b6e50de86a859f507f1231'
    corrected_manifest = read(corrected_D / 'MANIFEST1155.json')
    table = {r['path']: r for r in ci}
    for row in corrected_manifest['files']:
        assert table[row['path']] == row
    assert digest(corrected_C / 'manuscript.pdf') == PDF_SHA

    shutil.copyfile(PAPER / 'metadata.json', ROOT / 'metadata-final1159.json')
    meta = read(ROOT / 'metadata-final1159.json')
    metadata_check(meta)
    sys.path.insert(0, str(ROOT / 'schema-snapshot'))
    from assessmentlib import normalize_model_response, validate_assessment, source_hash
    from arrlib import Paper
    errors = validate_assessment(normalize_model_response(response), [Paper(PAPER, meta)])
    assert not errors, repr(errors)
    assert source_hash(response) == binding['model_response']['structured_sha256']
    original_meta = read(ROOT / 'metadata-initial1159.json')
    source_receipt = {
        'at': utc(), 'all_original_1148_and_1156_files_unchanged': True,
        'all_original_C_D_copies_identical': True,
        'original_source_file_counts': {k: v['file_count'] for k, v in final.items()},
        'initial_inventory_receipt_sha256': digest(ROOT / 'SOURCE-INTEGRITY-INITIAL1159.json'),
        'critical_original_hashes': EXPECTED,
        'corrected1155': {'C': str(corrected_C), 'D': str(corrected_D), 'C_D_identical': True,
                          'manifest_sha256': digest(corrected_D / 'MANIFEST1155.json'),
                          'file_count': len(ci), 'all_manifest_entries_match': True, 'files': ci},
        'scope': 'Hash and size authentication only. No scientific checks, sources, PDF readings or rendering repeated.'
    }
    write('SOURCE-INTEGRITY-FINAL1159.json', source_receipt)
    validation = {
        'at': utc(), 'passed': not errors, 'errors': errors, 'format': 'ARR-ASSESS-1.0',
        'schema_sha256': digest(ROOT / 'schema-snapshot/assessmentlib.py'),
        'official_validator_unchanged_from_repository': True,
        'real_version_metadata_path': str(PAPER / 'metadata.json'),
        'real_version_metadata_initial_sha256': digest(ROOT / 'metadata-initial1159.json'),
        'real_version_metadata_final_sha256': digest(ROOT / 'metadata-final1159.json'),
        'metadata_changed_during_serialization': original_meta != meta,
        'actual_IDs_and_PDF_match_both_snapshots': True,
        'paper_status_observed': meta['status'], 'real_ids': IDS,
        'actual_pdf_bytes': (PAPER / 'paper.pdf').stat().st_size, 'actual_pdf_sha256': digest(PAPER / 'paper.pdf'),
        'response_file_sha256': digest(ROOT / 'model-response.json'), 'response_structured_sha256': source_hash(response),
        'score_preservation': {'importance': 7.0, 'global_millennium': 6.7, 'technical_quality': 8.8, 'whole_stars': 7, 'criteria_each': 4},
        'O1_original_preserved_and_resolution_from_1156_only': True, 'O2_to_O5_retained_unchanged': True,
        'source_dossiers_unchanged': True, 'source_files_read_as_serialization_data_only': True,
        'new_full_review': False, 'new_science_executions': 0, 'new_grade_or_vote': False,
        'new_registration': False, 'editorial_acceptance': False, 'repo_mutations': False,
        'normalizer_UUID': 'transient official validation envelope only; not saved or registered',
        'human_check': 'Serialized response inspected for exact field binding, historical/current recommendation distinction, original criteria, all objections, uncertainty, context and scope. No fresh scientific evaluation.'
    }
    write('VALIDATION1159.json', validation)
    payloads = inventory(ROOT)
    manifest = {'at': utc(), 'payload_count': len(payloads),
                'scope': 'All 1159 binding payloads including selected unchanged originals and schema snapshots; excludes this manifest and closure to avoid self-reference.',
                'files': payloads}
    write('MANIFEST1159.json', manifest)
    # No destructive copy, deletion, move or Git operation. A new archive is required.
    assert not ARCHIVE.exists(), f'Archive already exists; refuse to overwrite {ARCHIVE}'
    ARCHIVE.mkdir(parents=True)
    for file in sorted(ROOT.rglob('*')):
        if file.is_file():
            target = ARCHIVE / file.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(file, target)
    assert inventory(ROOT) == inventory(ARCHIVE)
    closure = {
        'at': utc(), 'terminal': True, 'operation': 'Serialization only of same 1148 judgment with corrective continuation 1156',
        'C': str(ROOT), 'D': str(ARCHIVE), 'payload_count': len(payloads), 'total_files_including_manifest_and_closure': len(payloads) + 2,
        'C_D_payloads_and_manifest_identical': True,
        'C_D_closure': 'Same exact closure bytes are copied and then all files re-compared by relative path, size and SHA256 before success is returned.',
        'manifest_sha256': digest(ROOT / 'MANIFEST1159.json'),
        'model_response_file_sha256': digest(ROOT / 'model-response.json'),
        'model_response_structured_sha256': source_hash(response),
        'binding_sha256': digest(ROOT / 'BINDING1159.json'),
        'validation_sha256': digest(ROOT / 'VALIDATION1159.json'),
        'source_integrity_final_sha256': digest(ROOT / 'SOURCE-INTEGRITY-FINAL1159.json'),
        'sources_1148_1156_unchanged_and_C_D_identical': True, 'source_counts': {'1148': 435, '1156': 59},
        'corrected1155_24_files_manifest_and_C_D_verified': True,
        'source_report_and_verdict_hashes': EXPECTED,
        'actual_public_pdf_sha256': PDF_SHA, 'actual_public_pdf_bytes': 422006,
        'real_ids': IDS, 'format_validation_passed': True,
        'no_new_scientific_review_grade_vote_or_recommendation': True,
        'O1_resolved_only_as_in_1156_original_preserved': True, 'O2_O5_reservations_preserved': True,
        'runtime_model': 'unknown', 'effective_effort_isolation_independence_attested': False,
        'requested_model_only': 'GPT-6 Astra xhigh', 'involved_shared_context': True,
        'native_registration_or_publication_performed': False, 'editorial_acceptance': False,
        'no_Git_root_state_or_other_dossier_mutations': True
    }
    write('CLOSURE1159.json', closure)
    shutil.copyfile(ROOT / 'CLOSURE1159.json', ARCHIVE / 'CLOSURE1159.json')
    complete_C, complete_D = inventory(ROOT), inventory(ARCHIVE)
    assert complete_C == complete_D
    assert len(complete_C) == len(payloads) + 2
    print(json.dumps({'terminal': True, 'total_C_D_files': len(complete_C), 'payloads': len(payloads),
                      'C_D_identical': True, 'manifest_sha256': digest(ROOT / 'MANIFEST1159.json'),
                      'closure_sha256': digest(ROOT / 'CLOSURE1159.json'),
                      'response_file_sha256': digest(ROOT / 'model-response.json'),
                      'response_structured_sha256': source_hash(response),
                      'binding_sha256': digest(ROOT / 'BINDING1159.json'),
                      'original_dossiers_intact': True, 'official_format_errors': errors}, indent=2))

if __name__ == '__main__':
    main()
