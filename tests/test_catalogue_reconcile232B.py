# SPDX-License-Identifier: AGPL-3.0-or-later
"""Actual v15 helper, isolated SQLite/files/public transport; Linux normal and -O.
Synthetic PDF is ONLY a fixture, never an actual publication witness.
Thirteen top-level methods with explicit subcases; no host path/network allowed.
"""
from contextlib import contextmanager, ExitStack, redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sqlite3
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
CONNECT = sqlite3.connect
READ = Path.read_bytes
OPEN = Path.open
REPLACE = __import__('os').replace
HELPER = ROOT / 'scripts/operator_reconcile_rectangular_v15_232B.py'


class Fixture:
    def __init__(self, root):
        spec = importlib.util.spec_from_file_location('actual_v15_fixture', HELPER)
        self.h = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.h)
        self.root = root
        self.catalogue = root / 'catalogue.json'
        self.database = root / 'intake.sqlite3'
        self.backup = root / 'tep-catalogue-before232B-v15-two-witnesses.json'
        self.tmp = root / 'catalogue.232B-v15-two-witnesses.tmp'
        self.pdf = b'F' * self.h.PDF_BYTES
        self.digest = hashlib.sha256(self.pdf).hexdigest()
        self.new = {**self.h.NEW, 'canonical_sha256': self.digest}
        self.others = {'unrelated-' + str(i): {'sentinel': i} for i in range(93)}
        self.write_catalogue(self.h.OLD)
        self.before = READ(self.catalogue)
        self.metadata = {**self.new, 'id': self.h.PID, 'status': 'working_paper',
                         'authors': [{'name': 'Lluis Eriksson', 'affiliation': 'Independent researcher'}],
                         'integrity': {'canonical_sha256': self.digest},
                         'supersedes_version_id': self.h.OLD['version_id']}
        self.asset_id = 123456789  # Synthetic API fixture identity, not real asset.
        self.asset = {'id': self.asset_id, 'name': self.h.ASSET_NAME,
                      'size': self.h.PDF_BYTES, 'state': 'uploaded',
                      'browser_download_url': 'https://github.com/arr-research/arr-research.github.io/releases/download/'
                      + self.h.TAG + '/' + self.h.ASSET_NAME}
        self.release = {'tag_name': self.h.TAG, 'html_url': self.h.RELEASE,
                        'draft': False, 'published_at': 'fixture-published-time', 'assets': [self.asset]}
        self.asset_bytes = self.mirror_bytes = self.pdf
        self.requests, self.sql, self.connections = [], [], []
        self.args = ['helper', '--case', self.h.CASE, '--metadata-commit', 'a' * 40,
                     '--asset-id', str(self.asset_id)]
        db = CONNECT(self.database)
        db.executescript('CREATE TABLE submissions(id,sha256,public_release_url,public_released_at);'
                         'CREATE TABLE agent_grants(id,state,uses,expires_at);'
                         'CREATE TABLE historical_revision_grants(grant_id);')
        db.execute('INSERT INTO submissions VALUES(?,?,?,?)',
                   (self.h.CASE, self.digest, self.h.RELEASE, 'fixture-published-time'))
        db.commit()
        db.close()
        self.initial_rows = self.rows()

    def write_catalogue(self, entry):
        self.catalogue.write_text(json.dumps({self.h.PID: entry, **self.others}))

    def rows(self):
        db = CONNECT(self.database)
        try:
            return {name: db.execute('SELECT * FROM ' + name).fetchall()
                    for name in ('submissions', 'agent_grants', 'historical_revision_grants')}
        finally:
            db.close()

    def change_db(self, sql, values=()):
        db = CONNECT(self.database)
        try:
            db.execute(sql, values)
            db.commit()
        finally:
            db.close()

    def host_path(self, value):
        allowed = {'/srv/airr-private/historical-revisions/catalogue.json': self.catalogue,
                   '/srv/airr-private/tep-catalogue-before232B-v15-two-witnesses.json': self.backup}
        if str(value) not in allowed:
            raise AssertionError('Unexpected host path: ' + str(value))
        return allowed[str(value)]

    def connect(self, value, **kwargs):
        if value != '/srv/airr-private/instance/intake.sqlite3':
            raise AssertionError('Unexpected database')
        db = CONNECT(self.database, **kwargs)
        db.set_trace_callback(self.sql.append)
        self.connections.append(db)
        return db

    def public(self, url, limit, accept=None):
        self.requests.append((url, limit, accept))
        if url.endswith('/versions/v15/metadata.json'):
            return json.dumps(self.metadata).encode()
        if url == self.h.RELEASE_API:
            return json.dumps(self.release).encode()
        if url.endswith('/releases/assets/' + str(self.asset_id)):
            return self.asset_bytes
        if url == self.h.MIRROR_PDF:
            return self.mirror_bytes
        raise AssertionError('Unexpected network destination: ' + url)

    def run(self, apply=False, extras=()):
        with ExitStack() as stack:
            stack.enter_context(patch.object(self.h, 'DIGEST', self.digest))
            stack.enter_context(patch.object(self.h, 'NEW', self.new))
            stack.enter_context(patch.object(self.h, 'Path', side_effect=self.host_path))
            stack.enter_context(patch.object(self.h.sqlite3, 'connect', side_effect=self.connect))
            stack.enter_context(patch.object(self.h, 'public', side_effect=self.public))
            stack.enter_context(patch.object(self.h.urllib.request, 'urlopen', side_effect=AssertionError('Real network forbidden')))
            stack.enter_context(patch.object(sys, 'argv', self.args + (['--apply'] if apply else []) + list(extras)))
            output = stack.enter_context(redirect_stdout(io.StringIO()))
            self.h.main()
        return json.loads(output.getvalue())


class CatalogueReconcile232BTests(unittest.TestCase):
    @contextmanager
    def fixture(self):
        with tempfile.TemporaryDirectory() as name:
            yield Fixture(Path(name))

    def unchanged(self, f, before=None):
        self.assertEqual(READ(f.catalogue), f.before if before is None else before)
        self.assertFalse(f.backup.exists())
        self.assertFalse(f.tmp.exists())
        self.assertEqual(f.rows(), f.initial_rows)

    def no_authority_writes(self, f, expected=None):
        self.assertEqual(f.rows(), f.initial_rows if expected is None else expected)
        self.assertFalse(any(s.lstrip().upper().startswith(('INSERT', 'UPDATE', 'DELETE', 'REPLACE', 'CREATE', 'DROP'))
                             for s in f.sql), f.sql)

    def test_01_default_readonly_has_both_witnesses_and_no_mutation(self):
        with self.fixture() as f:
            out = f.run()
            self.assertFalse(out['mutated'])
            self.assertFalse(out['creates_permission_or_publication'])
            self.assertEqual(out['unrelated_entries_preserved'], 93)
            self.assertEqual(out['active_unused_grants'], 0)
            self.assertTrue(out['AIRR_mirror_verified'])
            self.assertEqual(out['metadata_sha256'], hashlib.sha256(json.dumps(f.metadata).encode()).hexdigest())
            self.assertEqual(len(f.requests), 4)
            self.unchanged(f)
            self.no_authority_writes(f)

    def test_02_apply_preserves_93_entries_backup_permissions_and_readback(self):
        with self.fixture() as f:
            mode = f.catalogue.stat()
            out = f.run(apply=True)
            self.assertTrue(out['mutated'])
            self.assertEqual(json.loads(READ(f.catalogue)), {f.h.PID: f.new, **f.others})
            self.assertEqual(READ(f.backup), f.before)
            self.assertEqual(stat.S_IMODE(f.backup.stat().st_mode), 0o600)
            self.assertEqual(stat.S_IMODE(f.catalogue.stat().st_mode), stat.S_IMODE(mode.st_mode))
            self.assertEqual((f.catalogue.stat().st_uid, f.catalogue.stat().st_gid), (mode.st_uid, mode.st_gid))
            self.assertFalse(f.tmp.exists())
            self.assertEqual(out['new_sha256'], hashlib.sha256(READ(f.catalogue)).hexdigest())
            self.no_authority_writes(f)

    def test_03_already_new_is_checked_noop_even_with_apply_and_existing_backup(self):
        for apply in (False, True):
            with self.subTest(apply=apply), self.fixture() as f:
                f.write_catalogue(f.new)
                before = READ(f.catalogue)
                f.backup.write_bytes(b'original-private-backup-sentinel')
                out = f.run(apply=apply)
                self.assertEqual(out['status'], 'already_reconciled')
                self.assertFalse(out['mutated'])
                self.assertEqual(out['active_unused_grants'], 0)
                self.assertEqual(len(f.requests), 4)
                self.assertEqual(READ(f.catalogue), before)
                self.assertEqual(READ(f.backup), b'original-private-backup-sentinel')
                self.assertFalse(f.tmp.exists())
                self.no_authority_writes(f)

    def test_04_exact_native_case_and_actual_published_binding_required(self):
        cases = ['argv', 'missing', 'hash', 'release', 'time']
        for case in cases:
            with self.subTest(case=case), self.fixture() as f:
                if case == 'argv':
                    f.args[2] = 'SUB-AAAAAAAAAAAAAAAA'
                elif case == 'missing':
                    f.change_db('DELETE FROM submissions')
                else:
                    column, value = {'hash': ('sha256', '0' * 64), 'release': ('public_release_url', 'https://wrong.test/'),
                                     'time': ('public_released_at', None)}[case]
                    f.change_db('UPDATE submissions SET ' + column + '=?', (value,))
                f.initial_rows = f.rows()
                with self.assertRaisesRegex(ValueError, 'native case|Native exact case'):
                    f.run(apply=True)
                self.unchanged(f)
                self.no_authority_writes(f)

    def test_05_metadata_author_identity_predecessor_status_and_cli_guards(self):
        for field in ('id', 'authors', 'record_id', 'version_id', 'version', 'status', 'integrity', 'supersedes_version_id',
                      'commit', 'asset-zero', 'asset-missing'):
            with self.subTest(field=field), self.fixture() as f:
                if field == 'commit':
                    f.args[4] = 'main'
                elif field == 'asset-zero':
                    f.args[6] = '0'
                elif field == 'asset-missing':
                    f.args = f.args[:5]
                else:
                    f.metadata[field] = {'authors': [{'name': 'Other author'}], 'integrity': {'canonical_sha256': '0' * 64}}.get(field, 'WRONG')
                with redirect_stdout(io.StringIO()), patch('sys.stderr', new_callable=io.StringIO):
                    with self.assertRaises((ValueError, SystemExit)):
                        f.run(apply=True)
                self.unchanged(f)

    def test_06_release_tag_unique_asset_membership_id_name_size_and_state(self):
        for change in ('tag', 'url', 'draft', 'unpublished', 'absent', 'wrong-id', 'wrong-name', 'wrong-size',
                       'wrong-state', 'wrong-browser', 'split-id-name', 'duplicate'):
            with self.subTest(change=change), self.fixture() as f:
                if change in ('tag', 'url', 'draft', 'unpublished'):
                    key, value = {'tag': ('tag_name', f.h.PID + '-v14'), 'url': ('html_url', 'https://wrong.test/'),
                                  'draft': ('draft', True), 'unpublished': ('published_at', None)}[change]
                    f.release[key] = value
                elif change == 'absent':
                    f.release['assets'] = []
                elif change == 'split-id-name':
                    f.release['assets'] = [{**f.asset, 'name': 'other.pdf'}, {**f.asset, 'id': f.asset_id + 1}]
                elif change == 'duplicate':
                    f.release['assets'].append(dict(f.asset))
                else:
                    key, value = {'wrong-id': ('id', f.asset_id + 1), 'wrong-name': ('name', 'other.pdf'),
                                  'wrong-size': ('size', f.h.PDF_BYTES + 1), 'wrong-state': ('state', 'new'),
                                  'wrong-browser': ('browser_download_url', f.asset['browser_download_url'].replace('-v15/', '-v14/'))}[change]
                    f.asset[key] = value
                with self.assertRaisesRegex(ValueError, 'release identity|must belong'):
                    f.run(apply=True)
                self.unchanged(f)
                self.assertFalse(any('/releases/assets/' in item[0] for item in f.requests))

    def test_07_independent_pdf_bytes_and_real_public_transport_guards(self):
        for source in ('asset', 'mirror'):
            for defect in ('size', 'hash'):
                with self.subTest(source=source, defect=defect), self.fixture() as f:
                    value = f.pdf[:-1] if defect == 'size' else b'X' * len(f.pdf)
                    setattr(f, source + '_bytes', value)
                    with self.assertRaisesRegex(ValueError, 'PDF mismatch'):
                        f.run(apply=True)
                    self.unchanged(f)
        for status, url, body, expected in [(404, 'https://example.test/', b'', 'HTTPS200'),
                                             (200, 'http://example.test/', b'', 'HTTPS200'),
                                             (200, 'https://example.test/', b'12345', 'Oversized')]:
            with self.subTest(status=status, url=url), self.fixture() as f:
                response = type('Response', (), {'status': status, 'url': url,
                           '__enter__': lambda this: this, '__exit__': lambda *args: False,
                           'read': lambda this, size: body[:size]})()
                with patch.object(f.h.urllib.request, 'urlopen', return_value=response):
                    with self.assertRaisesRegex(ValueError, expected):
                        f.h.public('https://example.test/', 4)
                self.unchanged(f)

    def test_08_catalogue_exact_predecessor_count_and_valid_json(self):
        for defect in ('entry', 'missing', 'count-low', 'count-high', 'json'):
            with self.subTest(defect=defect), self.fixture() as f:
                data = json.loads(f.before)
                if defect == 'entry':
                    data[f.h.PID]['canonical_sha256'] = '0' * 64
                elif defect == 'missing':
                    del data[f.h.PID]
                    data['replacement'] = {}
                elif defect == 'count-low':
                    del data['unrelated-0']
                elif defect == 'count-high':
                    data['extra'] = {}
                if defect == 'json':
                    f.catalogue.write_bytes(b'{not-json')
                else:
                    f.catalogue.write_text(json.dumps(data))
                before = READ(f.catalogue)
                with self.assertRaises(ValueError):
                    f.run(apply=True)
                self.unchanged(f, before)

    def test_09_global_unused_grants_also_block_already_new_noop(self):
        for already in (False, True):
            for state, uses, expires, blocks in [('approved', 0, '2999-01-01', True),
                                                  ('approved', 0, '2000-01-01', False),
                                                  ('approved', 1, '2999-01-01', False),
                                                  ('revoked', 0, '2999-01-01', False)]:
                with self.subTest(already=already, state=state, uses=uses, expires=expires), self.fixture() as f:
                    if already:
                        f.write_catalogue(f.new)
                    before = READ(f.catalogue)
                    # Unrelated grant, deliberately no PID filtering column.
                    f.change_db('INSERT INTO agent_grants VALUES(?,?,?,?)', ('unrelated-grant', state, uses, expires))
                    f.change_db('INSERT INTO historical_revision_grants VALUES(?)', ('unrelated-grant',))
                    f.initial_rows = f.rows()
                    if blocks:
                        with self.assertRaisesRegex(ValueError, 'Live unused historical grant'):
                            f.run(apply=True)
                    else:
                        out = f.run()  # Readonly, including OLD; no rewrite in this control.
                        self.assertFalse(out['mutated'])
                    self.unchanged(f, before)
                    self.no_authority_writes(f)

    def test_10_real_sqlite_writer_excluded_at_snapshot_and_final_compare(self):
        with self.fixture() as f:
            observations = []

            def compete(stage):
                other = CONNECT(f.database, timeout=0)
                try:
                    with self.assertRaisesRegex(sqlite3.OperationalError, 'locked'):
                        other.execute('BEGIN IMMEDIATE')
                    observations.append(stage)
                finally:
                    other.rollback()
                    other.close()

            def read(path):
                raw = READ(path)
                if path == f.catalogue and not observations:
                    self.assertTrue(f.connections[0].in_transaction)
                    compete('snapshot')
                return raw

            def opened(path, *args, **kwargs):
                if path == f.backup:
                    compete('after_final_compare')
                return OPEN(path, *args, **kwargs)

            with patch.object(Path, 'read_bytes', read), patch.object(Path, 'open', opened):
                f.run(apply=True)
            self.assertEqual(observations, ['snapshot', 'after_final_compare'])
            other = CONNECT(f.database, timeout=0)
            try:
                other.execute('BEGIN IMMEDIATE')
            finally:
                other.rollback()
                other.close()
            self.assertEqual(json.loads(READ(f.catalogue)), {f.h.PID: f.new, **f.others})
            self.no_authority_writes(f)

    def test_11_out_of_contract_content_change_before_final_compare_aborts(self):
        with self.fixture() as f:
            reads = []
            changed = json.dumps({**json.loads(f.before), 'unrelated-0': {'changed': 'outside protocol'}}).encode()

            def read(path):
                if path == f.catalogue:
                    reads.append(True)
                    if len(reads) == 2:
                        path.write_bytes(changed)
                return READ(path)

            with patch.object(Path, 'read_bytes', read):
                with self.assertRaisesRegex(ValueError, 'Concurrent catalogue change'):
                    f.run(apply=True)
            self.assertEqual(READ(f.catalogue), changed)
            self.assertFalse(f.backup.exists())
            self.assertFalse(f.tmp.exists())
            self.no_authority_writes(f)

    def test_12_exclusive_backup_and_temp_reject_existing_files_and_links(self):
        for kind in ('backup-file', 'backup-link', 'temp-file', 'temp-link'):
            with self.subTest(kind=kind), self.fixture() as f:
                target = f.root / 'do-not-overwrite'
                target.write_bytes(b'sentinel')
                chosen = f.backup if kind.startswith('backup') else f.tmp
                if kind.endswith('link'):
                    chosen.symlink_to(target)
                else:
                    chosen.write_bytes(b'sentinel')
                with self.assertRaises(FileExistsError):
                    f.run(apply=True)
                self.assertEqual(READ(f.catalogue), f.before)
                self.assertEqual(READ(chosen), b'sentinel')
                self.assertEqual(READ(target), b'sentinel')
                if kind.startswith('temp'):
                    self.assertEqual(READ(f.backup), f.before)
                self.no_authority_writes(f)

    def test_13_atomic_replace_failure_and_postreplace_readback_failure_are_honest(self):
        for stage in ('replace', 'readback'):
            with self.subTest(stage=stage), self.fixture() as f:
                def replace(source, target):
                    raise OSError('fixture replace refused')

                def read(path):
                    raw = READ(path)
                    if path == f.catalogue and json.loads(raw).get(f.h.PID) == f.new:
                        return raw + b'corrupt-readback'
                    return raw

                with ExitStack() as stack:
                    if stage == 'replace':
                        stack.enter_context(patch.object(f.h.os, 'replace', side_effect=replace))
                    else:
                        stack.enter_context(patch.object(Path, 'read_bytes', read))
                    with self.assertRaisesRegex((ValueError, OSError), 'readback mismatch|replace refused'):
                        f.run(apply=True)
                self.assertEqual(READ(f.backup), f.before)
                if stage == 'replace':
                    self.assertEqual(READ(f.catalogue), f.before)
                    self.assertTrue(f.tmp.exists())
                else:
                    self.assertEqual(json.loads(READ(f.catalogue)), {f.h.PID: f.new, **f.others})
                    self.assertFalse(f.tmp.exists())
                self.no_authority_writes(f)
                # DB rollback is not filesystem restore. Lock must still release.
                other = CONNECT(f.database, timeout=0)
                try:
                    other.execute('BEGIN IMMEDIATE')
                finally:
                    other.rollback()
                    other.close()


if __name__ == '__main__':
    unittest.main()
