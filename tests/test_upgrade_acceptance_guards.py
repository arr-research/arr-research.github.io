"""Offline upgrade guard regressions; unittest checks survive Python -O.

Use only after overlaying the candidate into a disposable Colab checkout.
Every absolute host path, privileged operation and HTTP request is replaced.
SQLite snapshots and symlink replacement operate only in a TemporaryDirectory.
"""
import ast
from contextlib import ExitStack, redirect_stdout
import io
from pathlib import Path
import sqlite3
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from services.intake.deploy import upgrade


class FixtureArchive:
    def __init__(self, members):
        self.members = members

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def getmembers(self):
        return self.members

    def extractfile(self, member):
        if member.size > 16 * 1024 * 1024 or '..' in member.name.split('/'):
            raise RuntimeError('Unsafe fixture member reached extraction')
        return io.BytesIO(b'# synthetic public source\n')


def member(relative, size=26):
    return SimpleNamespace(name='archive-root/' + relative, size=size,
                           isdir=lambda: False, isfile=lambda: True)


class UpgradeAcceptanceGuardTests(unittest.TestCase):
    def scenario(self, *, uid=0, mounted=True, current_is_release=False,
                 release_exists=False, intake='0', archive_size=1, members=None,
                 submit_status=503, ready_status=200, migration='init-db',
                 mutate_credentials=False, missing_schema=None, stale_switch=False,
                 accept=False, expected_message=None):
        with tempfile.TemporaryDirectory() as folder, ExitStack() as stack:
            root = Path(folder)
            releases = root / 'releases'
            releases.mkdir()
            commit = 'a' * 40
            release = releases / commit
            previous = releases / ('b' * 40)
            previous.mkdir()
            current = root / 'current'
            current.symlink_to(release if current_is_release else previous)
            if release_exists:
                release.mkdir()
            if stale_switch:
                (root / 'current-next').write_text('preserve this existing path')
            env = root / 'intake.env'
            env.write_text('ARR_INTAKE_OPEN=' + intake + '\n')
            private = root / 'private'
            (private / 'instance').mkdir(parents=True)
            database = private / 'instance/intake.sqlite3'
            with sqlite3.connect(database) as db:
                for table in ('users', 'submissions', 'recovery_codes', 'mail_outbox'):
                    db.execute('CREATE TABLE ' + table + '(value)')
                    db.execute('INSERT INTO ' + table + ' VALUES(?)', ('preserve original',))
                for table in ('private_accounts', 'paper_keys', 'paper_drafts'):
                    if table != missing_schema:
                        db.execute('CREATE TABLE ' + table + '(value)')
                db.execute('CREATE TABLE agent_grants(' +
                           ('unrelated' if missing_schema == 'owner_user_id' else 'owner_user_id') + ')')
            mapping = {
                '/opt/airr-intake/current': current,
                '/opt/airr-intake/releases': releases,
                '/etc/airr-intake/intake.env': env,
                '/srv/airr-private': private,
                '/srv/airr-private/instance/intake.sqlite3': database,
            }

            def safe_path(value):
                if str(value) not in mapping:
                    raise RuntimeError('Unexpected production path: ' + str(value))
                return mapping[str(value)]

            required = ['services/intake/' + filename for filename in
                        ('app.py', 'accounts.py', 'agents.py', 'workflow.py',
                         'pageviews.py', 'independent_agents.py', 'originality.py')]
            contents = [member(path) for path in required + ['papers/fixture/paper.txt']]
            if members is not None:
                contents = members
            calls = []
            changed = False

            def command(*args):
                nonlocal changed
                calls.append(args)
                if (mutate_credentials and not changed and
                        args == ('systemctl', 'start', 'airr-intake.service') and
                        current.resolve() == release):
                    with sqlite3.connect(database) as db:
                        db.execute("UPDATE users SET value='changed credential fixture'")
                    changed = True

            def response(url, **kwargs):
                if url.startswith('https://codeload.github.com/'):
                    return io.BytesIO(b'x' * archive_size)
                if not url.startswith('http://127.0.0.1:8000/'):
                    raise RuntimeError('Unexpected HTTP target: ' + url)
                path = url.removeprefix('http://127.0.0.1:8000')
                code = {'/submit': submit_status, '/readyz': ready_status,
                        '/account/register': 503, '/paper/new': 503}.get(path, 200)
                return FixtureResponse(code)

            stack.enter_context(patch.object(upgrade, 'Path', side_effect=safe_path))
            stack.enter_context(patch.object(upgrade.os, 'geteuid', return_value=uid, create=True))
            stack.enter_context(patch.object(upgrade.os.path, 'ismount', return_value=mounted))
            stack.enter_context(patch.object(upgrade.os, 'umask'))
            stack.enter_context(patch.object(upgrade, 'MAX_SOURCE_BYTES', 32))
            stack.enter_context(patch.object(upgrade.urllib.request, 'urlopen', side_effect=response))
            stack.enter_context(patch.object(upgrade.tarfile, 'open', return_value=FixtureArchive(contents)))
            stack.enter_context(patch.object(upgrade, 'run', side_effect=command))
            stack.enter_context(patch.object(upgrade, 'unit_state', return_value='inactive'))
            stack.enter_context(patch.object(upgrade.subprocess, 'check_output', return_value=migration))
            stack.enter_context(patch.object(upgrade.time, 'sleep'))
            stack.enter_context(patch('sys.argv', ['upgrade', commit]))
            stack.enter_context(redirect_stdout(io.StringIO()))
            error = None
            try:
                upgrade.main()
            except Exception as caught:
                error = caught
            proof = private / ('rollback-' + commit[:12]) / 'deployment.json'
            if accept:
                self.assertIsNone(error, repr(error))
                self.assertTrue(proof.is_file())
                self.assertEqual(current.resolve(), release)
            else:
                self.assertIsInstance(error, AssertionError, repr(error))
                if expected_message is not None:
                    self.assertEqual(str(error), expected_message)
                self.assertFalse(proof.exists(), 'Rejected deployment emitted acceptance proof')
                if mutate_credentials:
                    self.assertTrue(changed, 'Credential mutation did not reach the comparison')
                    with sqlite3.connect(database) as db:
                        self.assertEqual(db.execute('SELECT value FROM users').fetchone()[0],
                                         'preserve original', 'Fixture snapshot rollback was not restored')
            return calls

    def test_no_optimization_sensitive_assert_nodes_remain(self):
        tree = ast.parse(Path(upgrade.__file__).read_text())
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))

    def test_nonroot_rejected(self):
        self.assertEqual(self.scenario(uid=1000, expected_message=''), [])

    def test_unmounted_private_volume_rejected(self):
        self.assertEqual(self.scenario(mounted=False, expected_message=''), [])

    def test_current_or_existing_release_rejected(self):
        for value in ({'current_is_release': True}, {'release_exists': True}):
            with self.subTest(value=value):
                self.assertEqual(self.scenario(**value), [])

    def test_open_intake_rejected_with_original_message(self):
        self.assertEqual(self.scenario(intake='1', expected_message='Pause intake before upgrading'), [])

    def test_archive_limit_rejected_with_original_message(self):
        self.assertEqual(self.scenario(archive_size=33,
                         expected_message='Source archive exceeds deployment limit'), [])

    def test_archive_path_escape_rejected_before_extraction(self):
        self.assertEqual(self.scenario(members=[member('services/intake/../../../escape')]), [])

    def test_archive_member_size_rejected_before_extraction(self):
        self.assertEqual(self.scenario(members=[member('services/intake/app.py', 16 * 1024 * 1024 + 1)]), [])

    def test_required_source_files_rejected(self):
        self.assertEqual(self.scenario(members=[]), [])

    def test_originality_corpus_rejected_with_original_message(self):
        members = [member('services/intake/' + name) for name in
                   ('app.py', 'accounts.py', 'agents.py', 'workflow.py',
                    'pageviews.py', 'independent_agents.py', 'originality.py')]
        self.assertEqual(self.scenario(members=members,
                         expected_message='Public originality corpus must accompany this release'), [])

    def test_http_reception_must_be_paused(self):
        self.scenario(submit_status=200, expected_message='Public reception must be paused')

    def test_migration_hook_and_ready_state_rejected(self):
        for value in ({'migration': 'no migration command'}, {'ready_status': 503}):
            with self.subTest(value=value):
                self.scenario(**value)

    def test_existing_credentials_verified_against_actual_fixture_snapshot(self):
        self.scenario(mutate_credentials=True, expected_message='Existing credentials changed')

    def test_missing_migrated_schema_rejected(self):
        for name in ('private_accounts', 'paper_keys', 'paper_drafts', 'owner_user_id'):
            with self.subTest(table=name):
                self.scenario(missing_schema=name)

    def test_stale_switch_path_is_never_overwritten(self):
        self.scenario(stale_switch=True)

    def test_valid_synthetic_closed_upgrade_still_accepted(self):
        self.scenario(accept=True)


class FixtureResponse:
    def __init__(self, status):
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False
