# SPDX-License-Identifier: AGPL-3.0-or-later
"""Colab/CI only: real-field controls for the exact Working paper producer.

No normalizer is called here, so normal/-O runs cannot manufacture extra report
IDs. The public input inventory is refreshed for the edited field in each control:
the semantic guard, not merely a stale file digest, must reject the mutation.
"""
import hashlib
import json
from pathlib import Path
import shutil
import stat
import sys
import tempfile
import unittest
import warnings
import zipfile
import io
import gzip

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import finalize_rectangular_v15_232B as producer


class Publication232BTests(unittest.TestCase):
    def test_positive_exact_candidate_keeps_all_material_entries(self):
        meta, bound, checks = producer.check_candidate()
        self.assertGreaterEqual(len(checks), 170)
        self.assertEqual(bound['recommendation'], 'major_revision')
        self.assertEqual(len(bound['unresolved_material_objections']), 3)
        self.assertFalse(meta['screening']['human_signoff'])

    def reject_changed_field(self, relative, change, expected):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            path = target / relative
            value = json.loads(path.read_text())
            change(value)
            path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
            inventory_path = target / 'PACKAGE-INPUTS232B.json'
            inventory = json.loads(inventory_path.read_text())
            entries = [item for item in inventory['files'] if item['path'] == relative]
            self.assertEqual(len(entries), 1)
            entries[0]['bytes'] = path.stat().st_size
            entries[0]['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
            inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n')
            self.refresh_fixture_manifest(target)
            with self.assertRaisesRegex(ValueError, expected):
                producer.check_candidate(target)

    def refresh_fixture_manifest(self, target):
        manifest = target / 'MANIFEST.sha256'
        if manifest.exists():
            files = sorted(path for path in target.rglob('*') if path.is_file() and path != manifest)
            manifest.write_text(''.join(hashlib.sha256(path.read_bytes()).hexdigest() + '  '
                                        + path.relative_to(target).as_posix() + '\n' for path in files))

    def list_fixture_file(self, target, relative):
        path = target / relative
        inventory_path = target / 'PACKAGE-INPUTS232B.json'
        inventory = json.loads(inventory_path.read_text())
        inventory['files'].append(dict(path=relative, bytes=path.stat().st_size,
                                       sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        inventory_path.write_text(json.dumps(inventory, indent=2) + '\n')
        self.refresh_fixture_manifest(target)

    def reject_added_archive(self, members, expected):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            with warnings.catch_warnings(), zipfile.ZipFile(target / 'extra-appendix.zip', 'w') as archive:
                warnings.simplefilter('ignore', UserWarning)  # Deliberate duplicate member control.
                for name, raw in members:
                    archive.writestr(name, raw)
            self.list_fixture_file(target, 'extra-appendix.zip')
            with self.assertRaisesRegex(ValueError, expected):
                producer.check_candidate(target)

    def test_grade_inflation_is_rejected_even_with_updated_input_digest(self):
        self.reject_changed_field('bound-model-response232B.json',
                                  lambda value: value.update(millennium_score=9.0),
                                  'Only actual version_id')

    def test_dropping_material_entry_is_rejected(self):
        self.reject_changed_field('bound-model-response232B.json',
                                  lambda value: value['unresolved_material_objections'].pop(),
                                  'Only actual version_id')

    def test_false_human_signoff_is_rejected(self):
        self.reject_changed_field('metadata.json',
                                  lambda value: value['screening'].update(human_signoff=True),
                                  'No false screening pass')

    def test_different_native_license_is_rejected(self):
        self.reject_changed_field('NATIVE-AUTHORITY-EVIDENCE.json',
                                  lambda value: value['working_permission'].update(license='CC0-1.0'),
                                  'Actual exact Working permission')

    def test_private_bearer_key_cannot_enter_public_projection(self):
        self.reject_changed_field('NATIVE-AUTHORITY-EVIDENCE.json',
                                  lambda value: value.update(agent_token='SYNTHETIC-NEGATIVE-CONTROL'),
                                  'Only non-secret')

    def test_wrong_actual_version_binding_is_rejected(self):
        self.reject_changed_field('bound-model-response232B.json',
                                  lambda value: value.update(version_id='arr:version:00000000-0000-4000-8000-000000000000'),
                                  'Only actual version_id')

    def test_unlisted_private_json_is_not_swept_into_public_manifest(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            (target / 'native-grant232B.json').write_text(json.dumps({'agent_token': 'SYNTHETIC-NEGATIVE-CONTROL'}))
            with self.assertRaisesRegex(ValueError, 'Exact public file-set closure'):
                producer.check_candidate(target)

    def test_listed_extra_archive_private_payload_is_rejected(self):
        self.reject_added_archive([('results.json', b'{"access_token":"SYNTHETIC-NEGATIVE-CONTROL"}')],
                                  'Private credential/operational JSON key')

    def test_duplicate_inventory_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            path = target / 'PACKAGE-INPUTS232B.json'
            value = json.loads(path.read_text())
            value['files'].append(dict(value['files'][0]))
            path.write_text(json.dumps(value))
            with self.assertRaisesRegex(ValueError, 'Duplicate public inventory path'):
                producer.check_candidate(target)

    def test_noncanonical_inventory_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            path = target / 'PACKAGE-INPUTS232B.json'
            value = json.loads(path.read_text())
            value['files'][0]['path'] = './' + value['files'][0]['path']
            path.write_text(json.dumps(value))
            with self.assertRaisesRegex(ValueError, 'Noncanonical public relative path'):
                producer.check_candidate(target)

    def test_in_record_file_symlink_is_rejected_before_resolve(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            (target / 'scalar-rings.tex').unlink()
            (target / 'scalar-rings.tex').symlink_to(target / 'source-b/scalar-rings.tex')
            with self.assertRaisesRegex(ValueError, 'Symlink'):
                producer.check_candidate(target)

    def test_symlink_directory_component_is_rejected_before_resolve(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            shutil.rmtree(target / 'source-b')  # Own Linux temporary fixture only.
            (target / 'source-b').symlink_to(target, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'Symlink'):
                producer.check_candidate(target)

    def test_archive_traversal_member_is_rejected(self):
        self.reject_added_archive([('../outside.json', b'{}')], 'Noncanonical public relative path')

    def test_duplicate_archive_member_is_rejected(self):
        self.reject_added_archive([('public.json', b'{}'), ('public.json', b'{}')],
                                  'Duplicate archive member path')

    def test_archive_symlink_member_is_rejected(self):
        link = zipfile.ZipInfo('link.txt')
        link.create_system = 3
        link.external_attr = (stat.S_IFLNK | 0o777) << 16
        self.reject_added_archive([(link, b'public.json')], 'Archive symlink/nonregular')

    def test_listed_private_json_outside_authority_projection_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            (target / 'extra-results.json').write_text('{"password":"SYNTHETIC-NEGATIVE-CONTROL"}')
            self.list_fixture_file(target, 'extra-results.json')
            with self.assertRaisesRegex(ValueError, 'Private credential/operational JSON key'):
                producer.check_candidate(target)

    def test_oversize_sparse_public_file_is_rejected_before_read(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            with (target / 'oversize-proof.bin').open('wb') as stream:
                stream.truncate(32 * 1024 * 1024 + 1)
            self.list_fixture_file(target, 'oversize-proof.bin')
            with self.assertRaisesRegex(ValueError, 'bounded size'):
                producer.check_candidate(target)

    def test_json_depth_bound_is_enforced(self):
        value = {}
        for _ in range(45):
            value = {'public': value}
        self.reject_added_archive([('nested.json', json.dumps(value).encode())], 'JSON depth/node bound')

    def test_archive_depth_bound_is_enforced(self):
        raw, name = b'{}', 'public.json'
        for _ in range(6):
            output = io.BytesIO()
            with zipfile.ZipFile(output, 'w') as archive:
                archive.writestr(name, raw)
            raw, name = output.getvalue(), 'layer.zip'
        self.reject_added_archive([(name, raw)], 'archive nesting depth bound')

    def test_partial_generated_state_is_not_publishable(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'v15'
            shutil.copytree(producer.RECORD, target)
            (target / 'MANIFEST.sha256').unlink(missing_ok=True)
            (target / 'NORMALIZATION-RECEIPT232B.json').write_text('{}')
            with self.assertRaisesRegex(ValueError, 'Partial generated normalization state'):
                producer.check_candidate(target)

    def test_unsupported_nested_container_cannot_hide_private_json(self):
        hidden = gzip.compress(b'{"access_token":"SYNTHETIC-NEGATIVE-CONTROL"}')
        self.reject_added_archive([('opaque.bin', hidden)], 'Unsupported archive/container')

    def test_encoded_json_cannot_hide_private_keys(self):
        hidden = '{"access_token":"SYNTHETIC-NEGATIVE-CONTROL"}'.encode('utf-16')
        self.reject_added_archive([('opaque.txt', hidden)], 'Unsupported encoded text/JSON')

    def test_json_string_encoded_object_cannot_hide_private_keys(self):
        hidden = json.dumps({'log': json.dumps({'agent_token': 'SYNTHETIC-NEGATIVE-CONTROL'})}).encode()
        self.reject_added_archive([('results.json', hidden)], 'Private credential/operational JSON key')
