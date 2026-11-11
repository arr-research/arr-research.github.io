# SPDX-License-Identifier: AGPL-3.0-or-later
"""Colab/Linux only: normalize one actual bound report and validate public v15.

No network, deployment, release, native service or credential operation. This is
not a review or grade. --normalize modifies only disposable checkout registries,
the pending first-repository timestamp and the record's normalization/manifest.
Do not use before the separate exact-source gate. Normal/-O use explicit checks.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

from arrlib import ROOT, Paper, parse_exact_timestamp, validate_paper
from assessmentlib import normalize_model_response, source_hash, validate_assessment
from public_payload_privacy import exact_inventory, load_bounded_json, scan_files, MANIFEST, RECEIPT

PID = 'ARR-2026-7EPM3V3DP796BBRR'
VID = 'arr:version:ec7f4fe6-6e9a-4618-bfbe-dcda3daa8fbe'
PDF = '5595e89c1bcbec1d9b1ae35053a76e6a962f67b45d5d1ac483e5b7a60c9b9be0'
SOURCE = 'f83ee8a84b3ecc27470ed8a92ea61eb627d86445'
INITIAL = '8458953bee142a8d99a6839fef11d1fb004e79681a7ef7df72063ef4479a2d07'
REL = Path('papers/2026/08/7E') / PID / 'versions/v15'
RECORD = ROOT / REL
CRITERIA = ('correctness_confidence', 'rigor', 'novelty', 'significance', 'reproducibility')
FROZEN = {
    'paper.pdf': PDF,
    'assessment232B-codex/response.json': 'e05cc1bb5dea2cf3a43713b2d380d9afa3920c8e4ee3d350b95f4eb492c53e4f',
    'assessment232B-codex/scientific-review.txt': '9619c2a5b971bdeca22c7654587229bd1ade8cb44b1b355cf1a7aecbbcdb50e9',
    'assessment232B-protocol-clarification/response-native.json': '12d5d04f87bca41ebcdec874bab4002e0672c716dab1f5bb90e61a4029254eea',
    'author-response232B/author-response232B.txt': '86aa0588974f9e26940aa44fc0aa222c83c35214a41f31ca40481190d7146c06',
    'rectangular_matrix232B-assessed-package.zip': 'c874aa8bdb3d846ae50f9047e1e2ae155a423fac1b1340935fd6ecc4190baa6e',
    'tep232B-review.zip': 'f9ffa131859c97a8ab578ac7616d731d843ad3986171da372dcff7b1edfd48ae',
    'tep232A-review.zip': 'cb90267e04861514afd2186d1df7fbc26f265245b6998658530462a2de964242',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path, *, max_bytes=2 * 1024 * 1024):
    return load_bounded_json(path, max_bytes=max_bytes)


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def check_candidate(record=RECORD):
    inputs, actual_files = exact_inventory(record)
    checks = []

    def check(condition, message):
        require(condition, message)
        checks.append(message)

    for relative, digest in FROZEN.items():
        check(sha(record / relative) == digest, 'Frozen original bytes: ' + relative)
    check((record / 'paper.pdf').stat().st_size == 505936, 'Exact PDF size')
    native = load(record / 'assessment232B-protocol-clarification/response-native.json')
    original = load(record / 'assessment232B-codex/response.json')
    bound = load(record / 'bound-model-response232B.json')
    binding = load(record / 'assessment-binding232B.json')
    meta = load(record / 'metadata.json')
    authority = load(record / 'NATIVE-AUTHORITY-EVIDENCE.json')
    decision = load(record / 'DELEGATED-WORKING-DISPOSITION.json')
    expected = dict(native, version_id=VID)
    check(bound == expected, 'Only actual version_id may be added; no scientific fields changed')
    check(native['recommendation'] == 'major_revision' and original['recommendation'] == 'minor_revision',
          'Original minor opinion and actual major clarification retained')
    check(native['millennium_score'] == 4.1 and native['overall_stars'] == 4
          and [native['criteria'][key]['stars'] for key in CRITERIA] == [4, 4, 3, 3, 4],
          'Exact unchanged importance and all five criteria')
    material = native['unresolved_material_objections']
    check(len(material) == 3 and material == original['unresolved_material_objections'],
          'All three original material objections remain open')
    check(all(native[key] == original[key] for key in native if key not in {'recommendation', 'summary'}),
          'Clarification preserves every other original field')
    check(binding['actual_version_id'] == VID and binding['bound_response_raw_sha256'] == sha(record / 'bound-model-response232B.json')
          and binding['native_clarification_response_raw_sha256'] == FROZEN['assessment232B-protocol-clarification/response-native.json']
          and binding['original_response_raw_sha256'] == FROZEN['assessment232B-codex/response.json'],
          'Actual-only projection hash bindings')
    check(meta['version_id'] == VID and meta['id'] == PID and meta['version'] == 'v15'
          and meta['integrity']['canonical_sha256'] == PDF and meta['integrity']['canonical_bytes'] == 505936,
          'Exact public record identity')
    check(meta['status'] == 'working_paper' and meta['editorial']['decision'] == 'working_deposit'
          and meta['editorial']['signed_by'] == decision['signed_by'], 'Delegated Working-paper identity only')
    check(meta['screening']['status'] == 'fail' and meta['screening']['critical_objections_unresolved'] == 3
          and meta['screening']['human_signoff'] is False
          and len(meta['screening']['evaluators']) == 1
          and meta['screening']['evaluators'][0]['outcome'] == 'concerns',
          'No false screening pass, zero objections or human signoff')
    check(decision['exact_pdf_sha256'] == PDF and decision['source_sha'] == SOURCE
          and decision['decision'] == 'working_deposit' and decision['human_signoff'] is False
          and decision['editorial_acceptance'] is False and decision['human_response_simulated'] is False
          and decision['initial_instruction_sha256'] == INITIAL
          and [item['text'] for item in decision['objections']] == material
          and all(item['status'] == 'OPEN_UNCHANGED' for item in decision['objections']),
          'Actual delegated disposition preserves all open objections')
    permission = authority['working_permission']
    check(authority['registration_number'] == 'SUB-370C455C4D32B2FB'
          and authority['grant_id'] == 'AGT-509C4BB2772680E386978FB7'
          and authority['canonical_sha256'] == PDF and authority['canonical_bytes'] == 505936
          and authority['status'] == 'eligible' and authority['scan_status'] == 'clean'
          and authority['separate_authenticated_HTTPS_readback'] is True
          and authority['published_at_intake'] is False and authority['binding']['version_id'] == VID,
          'Checked actual native receipt/readback projection')
    check(permission['recorded'] is True and permission['license'] == 'CC-BY-4.0'
          and permission['metadata_license'] == 'CC0-1.0' and permission['public_status'] == 'working_paper'
          and permission['initial_instruction_sha256'] == INITIAL, 'Actual exact Working permission projection')
    gates = load(record / 'NATIVE-RELEASE-GATES232B.json')
    check(gates['case'] == authority['registration_number'] and gates['sha256'] == PDF
          and gates['originality_required'] == 0 and gates['submission_channel'] == 'agent'
          and gates['originality_ready'] is True and gates['distribution_ready'] is True
          and gates['permission_hash_matches'] is True and gates['mutation_performed'] is False
          and gates['not_novelty_clearance'] is True,
          'Actual read-only native route checks; no fabricated novelty clearance')
    forbidden = {'agent_token', 'controller_token', 'idempotency_key', 'owner_user_id', 'initial_actual_authority_path'}

    def no_private_keys(value):
        if isinstance(value, dict):
            return not forbidden.intersection(value) and all(no_private_keys(item) for item in value.values())
        if isinstance(value, list):
            return all(no_private_keys(item) for item in value)
        return True

    check(no_private_keys(authority) and no_private_keys(decision), 'Only non-secret native/decision projections')
    check(inputs['source_commit'] == SOURCE and inputs['canonical_sha256'] == PDF
          and inputs['native_version_id'] == VID and len(inputs['files']) >= 148, 'Complete fixed public input inventory')
    privacy = scan_files(actual_files)
    check(privacy['inspected_file_instances'] >= len(actual_files), 'Bounded recursive JSON/archive privacy completed')
    for item in inputs['files']:
        path = actual_files[item['path']]
        check(path.stat().st_size == item['bytes'] and sha(path) == item['sha256'],
              'Exact public input: ' + item['path'])
    if RECEIPT in actual_files:
        receipt = load(actual_files[RECEIPT])
        check(set(receipt) == {'actual_library', 'library_sha256', 'bound_response_raw_sha256', 'assessment_id',
                              'source_response_sha256', 'exact_pdf_sha256', 'actual_version_id', 'recommendation',
                              'all_three_material_objections_open', 'rescore', 'publication', 'note'}
              and receipt['actual_library'] == 'scripts/assessmentlib.py:normalize_model_response'
              and receipt['library_sha256'] == sha(ROOT / 'scripts/assessmentlib.py')
              and receipt['bound_response_raw_sha256'] == sha(record / 'bound-model-response232B.json')
              and receipt['source_response_sha256'] == source_hash(bound)
              and bool(re.fullmatch(r'arr:assessment:[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}', receipt['assessment_id']))
              and receipt['exact_pdf_sha256'] == PDF and receipt['actual_version_id'] == VID
              and receipt['recommendation'] == 'major_revision'
              and receipt['all_three_material_objections_open'] is True
              and receipt['rescore'] is False and receipt['publication'] is False,
              'Exact generated normalization receipt; no partial or fabricated state')
        from public_payload_privacy import canonical_relative
        recorded = {}
        for line in actual_files[MANIFEST].read_text(encoding='utf-8').splitlines():
            match = re.fullmatch(r'([a-f0-9]{64})  (.+)', line)
            check(match is not None, 'Canonical generated manifest line')
            name = canonical_relative(match[2])
            check(name not in recorded, 'Unique generated manifest entry')
            recorded[name] = match[1]
        check(set(recorded) == set(actual_files) - {MANIFEST}, 'Generated manifest exact file-set closure')
        check(all(recorded[name] == sha(actual_files[name]) for name in recorded), 'Generated manifest exact byte hashes')
    check(len(checks) >= 170, 'Explicit completed acceptance-check count')
    return meta, bound, checks


def manifest(record):
    # Never sweep arbitrary rglob extras into a public manifest. Recheck the exact
    # inventory and privacy after the receipt write and before generating it.
    _, actual = exact_inventory(record, generating_manifest=True)
    scan_files(actual)
    paths = [actual[name] for name in sorted(actual) if name != MANIFEST]
    (record / 'MANIFEST.sha256').write_text(''.join(sha(path) + '  ' + path.relative_to(record).as_posix() + '\n'
                                                   for path in paths), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--normalize', action='store_true')
    parser.add_argument('--deposit-commit')
    parser.add_argument('--deposit-recorded-at')
    args = parser.parse_args()
    require(sys.platform.startswith('linux'), 'Sanctioned owned Linux runtime only')
    meta, bound, checks = check_candidate()
    registry_path = ROOT / 'registry/model-assessments.json'
    # Existing repository-wide registries are distinct from bounded per-record
    # JSON; they are already about 2 MiB and grow by one preserved report.
    registry = load(registry_path, max_bytes=16 * 1024 * 1024)
    matches = [item for item in registry['assessments'] if item.get('version_id') == VID
               or (item.get('paper_id') == PID and item.get('version') == 'v15')]
    require(len(matches) <= 1, 'Duplicate v15 assessments must not be appended')
    if args.normalize:
        require(re.fullmatch('[a-f0-9]{40}', args.deposit_commit or ''), 'Actual first repository commit required')
        parse_exact_timestamp(args.deposit_recorded_at)
        # Preflight the timestamp before any append. The actual first-commit/time
        # is separately Git-attested by the owned runner/caller, not this parser.
        dates_path = ROOT / 'registry/record-timestamps.json'
        dates = load(dates_path, max_bytes=16 * 1024 * 1024)
        expected = dict(id=PID, version='v15', deposit_recorded_at=args.deposit_recorded_at,
                        deposit_timestamp_basis='first_repository_commit', deposit_commit=args.deposit_commit,
                        publication_state='pending')
        found = [item for item in dates['records'] if item['id'] == PID and item['version'] == 'v15']
        require(not found or found == [expected], 'Existing timestamp must not be fabricated or overwritten')
        if matches:
            existing = matches[0]
            reconstructed = {key: value for key, value in existing.items()
                             if key not in {'assessment_id', 'source_response_sha256'}}
            require(reconstructed == bound and existing['source_response_sha256'] == source_hash(bound),
                    'Existing normalized report differs; do not mutate or append')
            require(not validate_assessment(existing, [Paper(RECORD, meta)]), 'Existing normalized report is invalid')
        if not matches:
            normalized = normalize_model_response(bound)  # Native normalizer ONCE.
            errors = validate_assessment(normalized, [Paper(RECORD, meta)])
            require(not errors, 'Native assessment validation: ' + '; '.join(errors))
            registry['assessments'].append(normalized)
            write(registry_path, registry)
            matches = [normalized]
        # These are sequential filesystem writes, NOT one transaction. A failed
        # run/partial generated pair is retained and must never be published.
        if not found:
            dates['records'].append(expected)
            write(dates_path, dates)
        write(RECORD / 'NORMALIZATION-RECEIPT232B.json', dict(
            actual_library='scripts/assessmentlib.py:normalize_model_response',
            library_sha256=sha(ROOT / 'scripts/assessmentlib.py'),
            bound_response_raw_sha256=sha(RECORD / 'bound-model-response232B.json'),
            assessment_id=matches[0]['assessment_id'], source_response_sha256=matches[0]['source_response_sha256'],
            exact_pdf_sha256=PDF, actual_version_id=VID, recommendation='major_revision',
            all_three_material_objections_open=True, rescore=False, publication=False,
            note='Normalization/binding only. No new reviewer identity, verified isolation, grade or acceptance.'))
        manifest(RECORD)
        meta, bound, checks = check_candidate()
    require(len(matches) == 1, 'One genuine native-normalized v15 report required')
    report = matches[0]
    require(report['source_response_sha256'] == source_hash(bound), 'Native structured source-response hash')
    reconstructed = {key: value for key, value in report.items()
                     if key not in {'assessment_id', 'source_response_sha256'}}
    require(reconstructed == bound, 'Normalization may add only native assessment ID/source hash')
    errors = validate_assessment(report, [Paper(RECORD, meta)]) + validate_paper(Paper(RECORD, meta))
    require(not errors, 'Native paper/report validation: ' + '; '.join(errors))
    print(json.dumps(dict(status='exact_v15_native_normalization_and_validation_complete',
                          checks=len(checks), assessment_id=report['assessment_id'], recommendation='major_revision',
                          material_entries_open=3, score=4.1, overall_stars=4, publication=False)))


if __name__ == '__main__':
    main()
