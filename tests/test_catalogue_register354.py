# SPDX-License-Identifier: AGPL-3.0-or-later
"""Actual v1 registration helper, isolated SQLite/files/public transport.
Synthetic PDF is ONLY a fixture, never an actual publication witness.
Derived from the existing 232B field-regression corpus; no host/network allowed.
"""
from contextlib import contextmanager, ExitStack, redirect_stdout
import hashlib
import importlib.util
import io
import json
import os
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
OS_OPEN = os.open
REPLACE = __import__('os').replace
HELPER = ROOT / 'scripts/operator_register_window_predecessor354.py'


class Fixture:
    def __init__(self, root):
        spec = importlib.util.spec_from_file_location('actual_v1_fixture', HELPER)
        self.h = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.h)
        self.root = root
        self.catalogue = root / 'catalogue.json'
        self.database = root / 'intake.sqlite3'
        self.backup = root / 'tep-catalogue-before354-v1-two-witnesses.json'
        self.tmp = root / 'catalogue.354-v1-two-witnesses.tmp'
        self.pdf = b'F' * self.h.PDF_BYTES
        self.digest = hashlib.sha256(self.pdf).hexdigest()
        self.new = {**self.h.NEW, 'canonical_sha256': self.digest}
        self.others = {'unrelated-' + str(i): {'sentinel': i} for i in range(93)}
        self.write_catalogue(None)
        self.before = READ(self.catalogue)
        self.metadata = {**self.new, 'id': self.h.PID, 'status': 'working_paper',
                         'authors': [{'name': 'Lluis Eriksson', 'affiliation': 'Independent researcher'}],
                         'integrity': {'canonical_sha256': self.digest},
                         'supersedes_version_id': None}
        self.asset_id = 123456789  # Synthetic API fixture identity, not real asset.
        self.asset = {'id': self.asset_id, 'name': self.h.ASSET_NAME,
                      'size': self.h.PDF_BYTES, 'state': 'uploaded',
                      'browser_download_url': 'https://github.com/arr-research/arr-research.github.io/releases/download/'
                      + self.h.TAG + '/' + self.h.ASSET_NAME}
        self.release = {'tag_name': self.h.TAG, 'html_url': self.h.RELEASE,
                        'draft': False, 'published_at': 'fixture-published-time', 'assets': [self.asset]}
        self.asset_bytes = self.mirror_bytes = self.pdf
        self.requests, self.sql, self.connections = [], [], []
        self.live_service = lambda: ('1234', '1000', self.catalogue, self.catalogue)
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
        self.catalogue.write_text(json.dumps({**({self.h.PID: entry} if entry is not None else {}), **self.others}))

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
                   '/srv/airr-private/instance/intake.sqlite3': self.database,
                   '/srv/airr-private/tep-catalogue-before354-v1-two-witnesses.json': self.backup}
        if str(value) not in allowed:
            raise AssertionError('Unexpected host path: ' + str(value))
        return allowed[str(value)]

    def connect(self, value, **kwargs):
        if value != self.database.as_uri() + '?mode=rw' or kwargs.get('uri') is not True:
            raise AssertionError('Unexpected database')
        db = CONNECT(value, **kwargs)
        db.set_trace_callback(self.sql.append)
        self.connections.append(db)
        return db

    def public(self, url, limit, accept=None):
        self.requests.append((url, limit, accept))
        if url.endswith('/metadata.json'):
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
            stack.enter_context(patch.object(self.h, 'verify_live_service', side_effect=self.live_service))
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


class CatalogueReconcile354Tests(unittest.TestCase):
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

    def test_v2_requires_exact_v1_and_native_revision(self):
        with self.fixture() as f:
            h = f.h
            parent = f.new
            f.pdf = b'G' * 398180
            v2 = {**h.V2, 'canonical_sha256': hashlib.sha256(f.pdf).hexdigest()}
            tag = h.PID + '-v2'
            name = tag + '.pdf'
            release = h.RELEASE.removesuffix(h.TAG) + tag
            mirror = 'https://airr.science/papers/' + h.PID + '/versions/v2/' + name
            api = h.RELEASE_API.removesuffix(h.TAG) + tag
            metadata = {**f.metadata, **v2, 'authors': f.metadata['authors'],
                        'integrity': {'canonical_sha256': v2['canonical_sha256']},
                        'supersedes_version_id': parent['version_id']}
            asset = {**f.asset, 'name': name, 'size': len(f.pdf),
                     'browser_download_url': f.asset['browser_download_url'].replace(h.TAG, tag)}
            endpoints = {api: json.dumps({**f.release, 'tag_name': tag, 'html_url': release,
                                          'assets': [asset]}).encode(), mirror: f.pdf,
                         'https://api.github.com/repos/arr-research/arr-research.github.io/releases/assets/'
                         + str(f.asset_id): f.pdf,
                         'https://raw.githubusercontent.com/arr-research/arr-research.github.io/'
                         + 'a' * 40 + '/papers/2026/11/4T/' + h.PID + '/versions/v2/metadata.json':
                         json.dumps(metadata).encode()}
            f.public = lambda url, *args: endpoints[url]
            f.args[2] = h.V2_CASE
            f.change_db('UPDATE submissions SET id=?,sha256=?,public_release_url=?',
                        (h.V2_CASE, v2['canonical_sha256'], release))
            f.change_db('CREATE TABLE historical_revisions(submission_id,version_id,binding_json)')
            binding = {'paper_id': h.PID, 'record_id': h.RECORD, 'version': 'v2',
                       'version_id': v2['version_id'], 'sha256': v2['canonical_sha256'],
                       'parent_sha256': parent['canonical_sha256'], 'supersedes_version_id': parent['version_id']}
            paths = f.host_path
            backup = f.root / 'v2-backup.json'
            f.host_path = lambda value: backup if str(value).endswith('before354-v2-two-witnesses.json') else paths(value)
            with patch.object(h, 'V2', v2):
                with self.assertRaisesRegex(ValueError, 'Unexpected existing entry'):
                    f.run(apply=True)
                f.write_catalogue(parent)
                old = READ(f.catalogue)
                with self.assertRaisesRegex(ValueError, 'Native revision identity'):
                    f.run(apply=True)
                f.change_db('INSERT INTO historical_revisions VALUES(?,?,?)',
                            (h.V2_CASE, v2['version_id'], json.dumps({**binding, 'parent_sha256': '0' * 64})))
                with self.assertRaisesRegex(ValueError, 'binding mismatch'):
                    f.run(apply=True)
                self.assertEqual(READ(f.catalogue), old)
                self.assertFalse(backup.exists())
                f.change_db('UPDATE historical_revisions SET binding_json=?', (json.dumps(binding),))
                self.assertFalse(f.run()['mutated'])
                self.assertTrue(f.run(apply=True)['mutated'])
                self.assertEqual(READ(backup), old)
                self.assertEqual(json.loads(READ(f.catalogue)), {**f.others, h.PID: v2})
                self.assertFalse(f.run(apply=True)['mutated'])

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
                                  'wrong-browser': ('browser_download_url', f.asset['browser_download_url'].replace('-v1/', '-v14/'))}[change]
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
        for status, url, body, expected in [(404, 'https://airr.science/', b'', 'HTTPS200'),
                                             (200, 'http://example.test/', b'', 'HTTPS200'),
                                             (200, 'https://airr.science/', b'12345', 'Oversized')]:
            with self.subTest(status=status, url=url), self.fixture() as f:
                response = type('Response', (), {'status': status, 'url': url,
                           '__enter__': lambda this: this, '__exit__': lambda *args: False,
                           'read': lambda this, size: body[:size]})()
                with patch.object(f.h.urllib.request, 'urlopen', return_value=response):
                    with self.assertRaisesRegex(ValueError, expected):
                        f.h.public(f.h.MIRROR_PDF, 4)
                self.unchanged(f)

    def test_08_conflicting_catalogue_entry_and_invalid_json_refused(self):
        for defect in ('entry', 'json', 'array'):
            with self.subTest(defect=defect), self.fixture() as f:
                if defect == 'entry':
                    f.write_catalogue({**f.new, 'canonical_sha256': '0' * 64})
                elif defect == 'array':
                    f.catalogue.write_bytes(b'[]')
                else:
                    f.catalogue.write_bytes(b'{not-json')
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
                elif path == f.catalogue and json.loads(raw).get(f.h.PID) == f.new and 'readback' not in observations:
                    compete('readback')
                return raw

            def opened(path, *args, **kwargs):
                if path == f.backup:
                    compete('after_final_compare')
                return OS_OPEN(path, *args, **kwargs)

            with patch.object(Path, 'read_bytes', read), patch.object(f.h.os, 'open', opened):
                f.run(apply=True)
            self.assertEqual(observations, ['snapshot', 'after_final_compare', 'readback'])
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

    def test_14_service_failure_or_restart_never_mutates_catalogue(self):
        for stage in ('first-check', 'restart'):
            with self.subTest(stage=stage), self.fixture() as f:
                if stage == 'first-check':
                    def fail():
                        raise ValueError('fixture live config mismatch')
                    f.live_service = fail
                else:
                    replies = iter([('1234', '1000', f.catalogue, f.catalogue),
                                    ('1234', '2000', f.catalogue, f.catalogue)])
                    f.live_service = lambda: next(replies)
                with self.assertRaisesRegex(ValueError, 'config mismatch|Service restarted'):
                    f.run(apply=True)
                self.unchanged(f)
                self.no_authority_writes(f)

    def test_15_configuration_factory_pin_matches_reviewed_LF_source(self):
        with self.fixture() as f:
            source = READ(ROOT / 'services/intake/app.py')
            self.assertNotIn(b'\r', source)  # Linux CI uses the Git LF representation.
            self.assertEqual(hashlib.sha256(source).hexdigest(), f.h.APP_CONFIG_SHA256)
            for name, digest in f.h.ISSUER_SOURCE_SHA256.items():
                self.assertEqual(hashlib.sha256(READ(ROOT / name)).hexdigest(), digest)

    def test_16_live_guard_reads_process_config_without_importing_factory(self):
        for defect in ('none', 'pid', 'command', 'factory', 'database', 'catalogue', 'author', 'release',
                       'relative-db', 'relative-catalogue', 'hardlink-db', 'hardlink-catalogue', 'mount', 'issuers',
                       'parent', 'file-mount', 'own-file-mount', 'sidecar-mount'):
            with self.subTest(defect=defect), self.fixture() as f:
                release = f.root / 'release'
                (release / 'services/intake').mkdir(parents=True)
                app_bytes = b'fixture-not-executed-factory'
                (release / 'services/intake/app.py').write_bytes(app_bytes)
                issuer_bytes = b'fixture-not-executed-grant-issuer'
                (release / 'services/intake/programme_delegations.py').write_bytes(issuer_bytes)
                (release / 'services/intake/historical_revisions.py').write_bytes(issuer_bytes)
                proc = f.root / 'proc'
                (proc / '1234').mkdir(parents=True)
                (proc / '1234/cwd').symlink_to(release, target_is_directory=True)
                (proc / '1234/stat').write_text('1234 (gunicorn worker) ' + ' '.join(['0'] * 19 + ['1000']))
                mounted = proc / '1234/root' / str(f.root).lstrip('/')
                mounted.parent.mkdir(parents=True)
                if defect in ('parent', 'mount'):
                    mounted.mkdir()
                    (mounted / 'intake.sqlite3').symlink_to(f.database)
                    (mounted / 'catalogue.json').symlink_to(f.database if defect == 'mount' else f.catalogue)
                else:
                    mounted.symlink_to(f.root, target_is_directory=True)
                baseline_mount = '1 0 0:1 / / rw - ext4 /dev/root rw\n'
                own_mountinfo = f.root / 'own-mountinfo'
                own_mountinfo.write_text(baseline_mount)
                (proc / '1234/mountinfo').write_text(baseline_mount)
                if defect in ('file-mount', 'own-file-mount', 'sidecar-mount'):
                    target = str(f.catalogue) if defect != 'sidecar-mount' else str(f.database) + '-wal'
                    extra = '2 1 0:1 / ' + target + ' rw - ext4 /dev/root rw\n'
                    chosen = own_mountinfo if defect == 'own-file-mount' else proc / '1234/mountinfo'
                    chosen.write_text(baseline_mount + extra)
                command = b'gunicorn\0services.intake.app:create_app()\0'
                (proc / '1234/cmdline').write_bytes(b'wrong' if defect == 'command' else command)
                env = {'ARR_INTAKE_INSTANCE': str(f.root),
                       'AIRR_HISTORICAL_REVISION_CATALOGUE': str(f.catalogue),
                       'AIRR_HISTORICAL_OPERATOR_AUTHOR': 'Lluis Eriksson',
                       'ARR_SESSION_SECRET': 'fixture-secret-must-not-be-printed'}
                if defect == 'database':
                    env['ARR_INTAKE_INSTANCE'] = str(release)
                if defect == 'catalogue':
                    env['AIRR_HISTORICAL_REVISION_CATALOGUE'] = str(f.database)
                if defect == 'author':
                    env['AIRR_HISTORICAL_OPERATOR_AUTHOR'] = 'Other author'
                if defect == 'relative-db':
                    env['ARR_INTAKE_INSTANCE'] = '.'
                if defect == 'relative-catalogue':
                    env['AIRR_HISTORICAL_REVISION_CATALOGUE'] = 'catalogue.json'
                if defect == 'hardlink-db':
                    alternate = f.root / 'alternate'
                    alternate.mkdir()
                    os.link(f.database, alternate / 'intake.sqlite3')
                    env['ARR_INTAKE_INSTANCE'] = str(alternate)
                if defect == 'hardlink-catalogue':
                    alternate = f.root / 'catalogue-alias.json'
                    os.link(f.catalogue, alternate)
                    env['AIRR_HISTORICAL_REVISION_CATALOGUE'] = str(alternate)
                (proc / '1234/environ').write_bytes(b'\0'.join(
                    (k+'='+v).encode() for k, v in env.items()))
                paths = {'/proc': proc, '/opt/airr-intake/current': release,
                         '/proc/self/mountinfo': own_mountinfo,
                         '/srv/airr-private/instance/intake.sqlite3': f.database,
                         '/srv/airr-private/historical-revisions/catalogue.json': f.catalogue}
                if defect == 'release':
                    paths['/opt/airr-intake/current'] = f.root
                samefile = Path.samefile

                def mapped_path(value):
                    return paths.get(str(value), Path(value))

                def mapped_samefile(path, other):
                    actual = {'/srv/airr-private/instance/intake.sqlite3': f.database,
                              '/srv/airr-private/historical-revisions/catalogue.json': f.catalogue}
                    return samefile(path, actual.get(str(other), other))

                with ExitStack() as stack:
                    stack.enter_context(patch.object(f.h, 'Path', side_effect=mapped_path))
                    stack.enter_context(patch.object(Path, 'samefile', mapped_samefile))
                    stack.enter_context(patch.object(f.h, 'APP_CONFIG_SHA256',
                        '0'*64 if defect == 'factory' else hashlib.sha256(app_bytes).hexdigest()))
                    stack.enter_context(patch.object(f.h, 'ISSUER_SOURCE_SHA256', {
                        name: ('0'*64 if defect == 'issuers' else hashlib.sha256(issuer_bytes).hexdigest())
                        for name in f.h.ISSUER_SOURCE_SHA256}))
                    stack.enter_context(patch.object(f.h.subprocess, 'check_output',
                        return_value='0\n' if defect == 'pid' else '1234\n'))
                    output = stack.enter_context(redirect_stdout(io.StringIO()))
                    if defect == 'none':
                        self.assertEqual(f.h.verify_live_service(),
                                         ('1234', '1000', f.catalogue, mounted / 'catalogue.json'))
                    else:
                        with self.assertRaises((ValueError, FileNotFoundError)):
                            f.h.verify_live_service()
                    self.assertEqual(output.getvalue(), '')
                self.unchanged(f)


    def test_17_private_files_are_created_0600_even_with_permissive_umask(self):
        with self.fixture() as f:
            observed = []
            def opened(path, flags, mode=0o777, **kwargs):
                fd = OS_OPEN(path, flags, mode, **kwargs)
                if path in (f.backup, f.tmp):
                    observed.append(path)
                    self.assertEqual(stat.S_IMODE(os.fstat(fd).st_mode), 0o600)
                    self.assertEqual(os.fstat(fd).st_size, 0)
                    self.assertTrue(flags & os.O_EXCL)
                return fd
            previous_umask = os.umask(0)
            try:
                with patch.object(f.h.os, 'open', opened):
                    f.run(apply=True)
            finally:
                os.umask(previous_umask)
            self.assertEqual(observed, [f.backup, f.tmp])

    def test_18_duplicate_json_keys_refused_without_losing_original_bytes(self):
        for kind in ('paper', 'unrelated', 'nested'):
            with self.subTest(kind=kind), self.fixture() as f:
                if kind == 'paper':
                    raw = ('{"' + f.h.PID + '":{"wrong":true},"' + f.h.PID + '":' + json.dumps(f.new) + '}').encode()
                elif kind == 'unrelated':
                    raw = b'{"other":{"a":1},"other":{"a":2}}'
                else:
                    raw = b'{"other":{"a":1,"a":2}}'
                f.catalogue.write_bytes(raw)
                with self.assertRaisesRegex(ValueError, 'Duplicate JSON key'):
                    f.run(apply=True)
                self.unchanged(f, raw)

    def test_19_transport_preserves_distinct_public_witness_origins(self):
        for requested, final, accept, succeeds in (
                ('https://airr.science/a.pdf', 'https://airr.science/a.pdf', None, True),
                ('https://airr.science/a.pdf', 'https://release-assets.githubusercontent.com/a.pdf', None, False),
                ('https://raw.githubusercontent.com/a', 'https://api.github.com/a', None, False),
                ('https://api.github.com/a', 'https://release-assets.githubusercontent.com/a', 'application/vnd.github+json', False),
                ('https://api.github.com/a', 'https://release-assets.githubusercontent.com/a', 'application/octet-stream', True),
                ('https://api.github.com/a', 'https://objects.githubusercontent.com/a', 'application/octet-stream', True),
                ('https://airr.science/a.pdf', 'https://airr.science.evil.test/a.pdf', None, False),
                ('https://airr.science/a.pdf', 'https://user@airr.science/a.pdf', None, False),
                ('https://airr.science/a.pdf', 'https://airr.science:444/a.pdf', None, False)):
            with self.subTest(requested=requested, final=final), self.fixture() as f:
                # Even correct bytes cannot turn the official asset into a mirror witness.
                response = type('Response', (), {'status': 200, 'url': final,
                           '__enter__': lambda this: this, '__exit__': lambda *args: False,
                           'read': lambda this, size: f.pdf[:size]})()
                with patch.object(f.h.urllib.request, 'urlopen', return_value=response):
                    if succeeds:
                        self.assertEqual(f.h.public(requested, len(f.pdf), accept), f.pdf)
                    else:
                        with self.assertRaisesRegex(ValueError, 'redirect origin mismatch'):
                            f.h.public(requested, len(f.pdf), accept)
                self.unchanged(f)

    def test_20_missing_database_is_not_created(self):
        with self.fixture() as f:
            f.database.unlink()
            with self.assertRaises(sqlite3.OperationalError):
                f.run(apply=True)
            self.assertFalse(f.database.exists())
            self.assertEqual(READ(f.catalogue), f.before)
            self.assertFalse(f.backup.exists())
            self.assertFalse(f.tmp.exists())

    def test_21_identity_constants_match_existing_public_metadata(self):
        with self.fixture() as f:
            meta = json.loads(READ(ROOT / 'papers/2026/11/4T/ARR-2026-4T35VQ6MZB8F99F4/metadata.json'))
            self.assertEqual(f.h.PID, meta['id'])
            self.assertEqual(f.h.DIGEST, meta['integrity']['canonical_sha256'])
            self.assertEqual(f.h.NEW['canonical_sha256'], meta['integrity']['canonical_sha256'])
            for key in ('record_id', 'version_id', 'version'):
                self.assertEqual(f.h.NEW[key], meta[key])
            self.assertEqual(f.h.NEW['authors'], [a['name'] for a in meta['authors']])

    def test_22_mountinfo_escaping_and_invalid_evidence(self):
        with self.fixture() as f:
            self.assertEqual(f.h.mount_points(r'1 0 0:1 / /with\040space\134slash rw - ext4 /dev/root rw'),
                             {'/with space\\slash'})
            for raw in ('', 'invalid', '1 0 0:1 / / rw ext4 /dev/root rw'):
                with self.assertRaises(ValueError):
                    f.h.mount_points(raw)

    def test_23_service_view_readback_failure_is_not_reported_as_success(self):
        with self.fixture() as f:
            stale = f.root / 'service-stale.json'
            stale.write_bytes(f.before)
            f.live_service = lambda: ('1234', '1000', f.catalogue, stale)
            with self.assertRaisesRegex(ValueError, 'Catalogue readback mismatch'):
                f.run(apply=True)
            self.assertEqual(json.loads(READ(f.catalogue)), {f.h.PID: f.new, **f.others})
            self.assertEqual(READ(stale), f.before)
            self.assertEqual(READ(f.backup), f.before)
            self.no_authority_writes(f)


if __name__ == '__main__':
    unittest.main()
