# SPDX-License-Identifier: AGPL-3.0-or-later
"""Offline regression checks for the actual helper and supported writer inventory.

All acceptance checks use unittest methods, which remain active under python -O.
No host path, network, native service or real permission is used.
"""
import ast
from contextlib import ExitStack, redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
WRITERS = {
    'operator_reconcile_turan212.py', 'operator_reconcile_turan_v2_212.py',
    'operator_reconcile_perron_v2_213.py', 'operator_reconcile_parity_v2_215.py',
    'operator_register_parity_predecessor215.py',
    'operator_reconcile_integrated_v11_217.py',
    'operator_reconcile_integrated_v12_221.py',
    'operator_reconcile_integrated_v13_223.py',
    'operator_reconcile_matrix_v14_226C.py',
    'operator_reconcile_matrix_v14_official_release_226C.py',
}


class CatalogueWriterProtocolTests(unittest.TestCase):
    def test_all_supported_writers_retain_same_lock_across_compare_and_replace(self):
        found = set()
        for path in (ROOT / 'scripts').glob('*.py'):
            source = path.read_text(encoding='utf-8')
            if '/srv/airr-private/historical-revisions/catalogue.json' not in source or 'os.replace(' not in source:
                continue
            found.add(path.name)
            with self.subTest(writer=path.name):
                tree = ast.parse(source)
                calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
                begins = [node.lineno for node in calls if node.args and
                          isinstance(node.args[0], ast.Constant) and
                          node.args[0].value == 'BEGIN IMMEDIATE']
                replaces = [node.lineno for node in calls if isinstance(node.func, ast.Attribute)
                            and isinstance(node.func.value, ast.Name)
                            and node.func.value.id == 'os' and node.func.attr == 'replace']
                commits = [node.lineno for node in calls if isinstance(node.func, ast.Attribute)
                           and node.func.attr == 'commit']
                self.assertEqual(len(begins), 1)
                self.assertEqual(len(replaces), 1)
                self.assertTrue(any(isinstance(node, ast.Constant) and
                                    node.value == '/srv/airr-private/instance/intake.sqlite3'
                                    for node in ast.walk(tree)))
                self.assertLess(begins[0], replaces[0])
                self.assertTrue(commits)
                self.assertTrue(all(line >= replaces[0] for line in commits))
                comparisons = [node for node in ast.walk(tree) if isinstance(node, ast.If)
                               and begins[0] < node.lineno < replaces[0]
                               and any(isinstance(child, ast.Call)
                                       and isinstance(child.func, ast.Attribute)
                                       and child.func.attr == 'read_bytes'
                                       for child in ast.walk(node.test))]
                self.assertTrue(comparisons, 'Missing final in-lock file comparison')
                self.assertTrue(any(isinstance(node, ast.Call)
                                    and isinstance(node.func, ast.Attribute)
                                    and node.func.attr == 'rollback'
                                    and node.lineno >= replaces[0] for node in calls))
        self.assertEqual(found, WRITERS, 'Review any newly added private catalogue writer')

    def test_actual_helper_snapshot_and_compare_replace_window_exclude_writer(self):
        spec = importlib.util.spec_from_file_location(
            'official_release_race_fixture',
            ROOT / 'scripts/operator_reconcile_matrix_v14_official_release_226C.py')
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        connect = sqlite3.connect
        read_bytes = Path.read_bytes
        open_path = Path.open
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            catalogue = root / 'catalogue.json'
            database = root / 'intake.sqlite3'
            backup = root / 'tep-catalogue-before226C-official-release-v14.json'
            pdf = b'P' * 419361  # Synthetic bytes; never a publication witness.
            digest = hashlib.sha256(pdf).hexdigest()
            new = {**helper.NEW, 'canonical_sha256': digest}
            unrelated = {'unrelated-' + str(i): {'sentinel': i} for i in range(93)}
            catalogue.write_text(json.dumps({helper.PID: helper.OLD, **unrelated}))
            before = read_bytes(catalogue)
            db = connect(database)
            db.executescript('CREATE TABLE submissions(id,sha256,public_release_url,public_released_at);'
                             'CREATE TABLE agent_grants(id,state,uses,expires_at);'
                             'CREATE TABLE historical_revision_grants(grant_id);')
            db.execute('INSERT INTO submissions VALUES(?,?,?,?)',
                       ('SUB-AAAAAAAAAAAAAAAA', digest, helper.RELEASE, 'fixture-recorded-time'))
            db.commit()
            db.close()
            connections, observations = [], []

            def private_path(value):
                value = str(value)
                if value == '/srv/airr-private/historical-revisions/catalogue.json':
                    return catalogue
                if value == '/srv/airr-private/tep-catalogue-before226C-official-release-v14.json':
                    return backup
                raise ValueError('Unexpected host path in isolated fixture: ' + value)

            def connection(value, **kwargs):
                self.assertEqual(value, '/srv/airr-private/instance/intake.sqlite3')
                actual = connect(database, **kwargs)
                connections.append(actual)
                return actual

            def compete(stage):
                other = connect(database, timeout=0)
                try:
                    try:
                        other.execute('BEGIN IMMEDIATE')
                    except sqlite3.OperationalError as error:
                        if 'locked' not in str(error).lower():
                            raise
                        observations.append((stage, 'blocked'))
                    else:
                        observations.append((stage, 'unlocked'))
                finally:
                    other.rollback()
                    other.close()

            def observed_read(path):
                raw = read_bytes(path)
                if path == catalogue and not observations:
                    self.assertTrue(connections, 'Snapshot was read before DB connection')
                    self.assertTrue(connections[0].in_transaction)
                    compete('initial_snapshot')
                return raw

            def observed_open(path, *args, **kwargs):
                if path == backup:
                    # After the final comparison, before replacement: a second
                    # supported writer must still fail to acquire the DB lock.
                    compete('after_final_compare')
                return open_path(path, *args, **kwargs)

            metadata = {**new, 'id': helper.PID,
                        'authors': [{'name': 'Lluis Eriksson', 'affiliation': 'Independent researcher'}],
                        'integrity': {'canonical_sha256': digest},
                        'supersedes_version_id': helper.OLD['version_id']}
            with ExitStack() as stack:
                stack.enter_context(patch.object(helper, 'DIGEST', digest))
                stack.enter_context(patch.object(helper, 'NEW', new))
                stack.enter_context(patch.object(helper, 'Path', side_effect=private_path))
                stack.enter_context(patch.object(helper.sqlite3, 'connect', side_effect=connection))
                stack.enter_context(patch.object(helper, 'public', side_effect=lambda url, *args:
                                                json.dumps(metadata).encode() if url.endswith('metadata.json') else pdf))
                stack.enter_context(patch.object(helper.os, 'chown'))
                stack.enter_context(patch.object(Path, 'read_bytes', observed_read))
                stack.enter_context(patch.object(Path, 'open', observed_open))
                stack.enter_context(patch('sys.argv', ['helper', '--apply', '--case',
                                                     'SUB-AAAAAAAAAAAAAAAA', '--metadata-commit', 'a' * 40]))
                output = stack.enter_context(redirect_stdout(io.StringIO()))
                helper.main()
            self.assertEqual(observations, [('initial_snapshot', 'blocked'),
                                            ('after_final_compare', 'blocked')])
            after = json.loads(read_bytes(catalogue))
            self.assertEqual(after, {helper.PID: new, **unrelated})
            self.assertEqual(read_bytes(backup), before)
            self.assertEqual(backup.stat().st_mode & 0o777, 0o600)
            result = json.loads(output.getvalue())
            self.assertTrue(result['mutated'])
            self.assertFalse(result['AIRR_mirror_verified'])
            self.assertEqual(result['original_mirror_gate'], 'pending_unchanged')
            # Lock is actually released after completion, so a subsequent
            # cooperating writer can read/preserve the installed successor.
            other = connect(database, timeout=0)
            try:
                other.execute('BEGIN IMMEDIATE')
                self.assertEqual(json.loads(read_bytes(catalogue))[helper.PID], new)
            finally:
                other.rollback()
                other.close()
