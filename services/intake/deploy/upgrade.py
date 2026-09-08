"""Upgrade a closed intake from a pinned AIRR Git commit, preserving private data.

Run as root on the existing configured Netcup host. No credentials are created,
printed or changed. This command never opens intake or publishes the public site.
"""
import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import tarfile
import time
import urllib.error
import urllib.request


MONITOR = 'airr-intake-monitor'
BACKGROUND = ['airr-intake-' + name for name in ('mail', 'maintenance', 'backup', 'offsite')]


def run(*command):
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL)


def unit_state(unit):
    return subprocess.check_output(
        ['systemctl', 'show', unit, '--property=ActiveState', '--value'], text=True).strip()


def wait_for_idle(units, timeout=60):
    deadline = time.monotonic() + timeout
    while True:
        # Type=oneshot is "activating" while its program runs, not "active".
        # Unknown/transitional states must not let us replace a live worker.
        pending = [unit for unit in units if unit_state(unit) not in {'inactive', 'failed'}]
        if not pending:
            return
        if time.monotonic() >= deadline:
            raise RuntimeError('Background operation still running: ' + ', '.join(pending))
        time.sleep(1)


def pause_background(timers):
    # Let any in-flight health check finish against the still-running service.
    # Stopping only its timer neither stops nor waits for that oneshot process.
    if MONITOR + '.timer' in timers:
        run('systemctl', 'stop', MONITOR + '.timer')
    wait_for_idle([MONITOR + '.service'])
    workers = [timer for timer in timers if timer != MONITOR + '.timer']
    if workers:
        run('systemctl', 'stop', *workers)
    wait_for_idle([unit + '.service' for unit in BACKGROUND])


def resume_background(timers):
    workers = [timer for timer in timers if timer != MONITOR + '.timer']
    try:
        if workers:
            run('systemctl', 'start', *workers)
    finally:
        # Resume monitoring last, even if restarting a worker failed: a real
        # failure must still alert. No alert suppression or grace period is used.
        if MONITOR + '.timer' in timers:
            run('systemctl', 'start', MONITOR + '.timer')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('commit', help='Full pinned Git commit identifier')
    args = parser.parse_args()
    if not re.fullmatch('[0-9a-f]{40}', args.commit):
        parser.error('Supply the full commit identifier')
    os.umask(0o077)
    assert os.geteuid() == 0
    assert os.path.ismount('/srv/airr-private')
    current = Path('/opt/airr-intake/current')
    previous = current.resolve()
    release = Path('/opt/airr-intake/releases') / args.commit
    assert previous != release and not release.exists()
    values = {key.strip(): value for line in Path('/etc/airr-intake/intake.env').read_text().splitlines()
              if '=' in line and not line.lstrip().startswith('#') for key, value in [line.split('=', 1)]}
    assert values.get('ARR_INTAKE_OPEN', '0').strip().strip('"\'') == '0', 'Pause intake before upgrading'
    url = 'https://codeload.github.com/arr-research/arr-research.github.io/tar.gz/' + args.commit
    with urllib.request.urlopen(url, timeout=90) as response:
        archive = response.read(128 * 1024 * 1024 + 1)
    assert len(archive) <= 128 * 1024 * 1024, 'Source archive exceeds deployment limit'
    archive_hash = hashlib.sha256(archive).hexdigest()
    release.mkdir(mode=0o755)
    release.chmod(0o755)
    exact = {'scripts/__init__.py', 'scripts/subjectlib.py', 'scripts/donationlib.py',
             'site/donations.json', 'site/subjects.js',
             'registry/euroscivoc.json', 'registry/subject-extensions.json'}
    with tarfile.open(fileobj=io.BytesIO(archive)) as source:
        for member in source.getmembers():
            parts = member.name.split('/', 1)
            if len(parts) != 2:
                continue
            relative = parts[1]
            if not (relative.startswith('services/intake/') or relative in exact):
                continue
            target = release / relative
            assert target.resolve().is_relative_to(release)
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True, mode=0o755)
            elif member.isfile():
                assert member.size <= 16 * 1024 * 1024
                target.parent.mkdir(parents=True, exist_ok=True, mode=0o755)
                with source.extractfile(member) as stream, target.open('wb') as output:
                    shutil.copyfileobj(stream, output)
                target.chmod(0o644)
            else:
                raise RuntimeError('Source archive contains an unsupported link')
    for filename in ('app.py', 'accounts.py', 'agents.py', 'workflow.py', 'pageviews.py'):
        assert (release / 'services/intake' / filename).is_file()
    # The public-path allowlist is generated, not part of Git. Preserve the last
    # verified manifest; the collector's existing refresh mechanism updates it.
    manifest = previous / 'site/analytics-pages.json'
    if manifest.is_file():
        shutil.copyfile(manifest, release / 'site/analytics-pages.json')
        (release / 'site/analytics-pages.json').chmod(0o644)
    # umask applies to intermediate mkdir parents too; source is public code.
    for path in release.rglob('*'):
        if path.is_dir():
            path.chmod(0o755)
    database = Path('/srv/airr-private/instance/intake.sqlite3')
    rollback = Path('/srv/airr-private') / ('rollback-' + args.commit[:12])
    rollback.mkdir(mode=0o700)
    (rollback / 'previous-release.txt').write_text(str(previous) + '\n')
    def switch(path):
        temporary = current.with_name('current-next')
        assert not temporary.exists() and not temporary.is_symlink()
        temporary.symlink_to(path)
        temporary.replace(current)

    def snapshot(source, target):
        with sqlite3.connect(source) as src, sqlite3.connect(target) as dst:
            src.backup(dst)

    def counts():
        with sqlite3.connect(database) as db:
            assert db.execute('PRAGMA integrity_check').fetchone()[0] == 'ok'
            return {table: db.execute('SELECT COUNT(*) FROM ' + table).fetchone()[0]
                    for table in ('users', 'submissions', 'recovery_codes', 'mail_outbox')}

    def status(path):
        try:
            with urllib.request.urlopen('http://127.0.0.1:8000' + path, timeout=10) as response:
                return response.status
        except urllib.error.HTTPError as error:
            return error.code

    timers = [unit + '.timer' for unit in [MONITOR, *BACKGROUND]
              if unit_state(unit + '.timer') == 'active']
    saved = False
    try:
        assert status('/submit') == 503, 'Public reception must be paused'
        pause_background(timers)
        run('systemctl', 'stop', 'airr-intake.service')
        before = counts()
        snapshot(database, rollback / 'intake.sqlite3')
        saved = True
        switch(release)
        pre = subprocess.check_output(['systemctl', 'show', 'airr-intake.service', '-p', 'ExecStartPre'], text=True)
        assert 'init-db' in pre
        run('systemctl', 'start', 'airr-intake.service')
        for _ in range(30):
            try:
                if status('/readyz') == 200:
                    break
            except OSError:
                pass
            time.sleep(1)
        assert status('/readyz') == 200 and counts() == before
        with sqlite3.connect(database) as live, sqlite3.connect(rollback / 'intake.sqlite3') as old:
            for table in ('users', 'recovery_codes'):
                assert live.execute('SELECT * FROM ' + table + ' ORDER BY rowid').fetchall() == old.execute('SELECT * FROM ' + table + ' ORDER BY rowid').fetchall(), 'Existing credentials changed'
        for path, expected in {'/login':200, '/account/login':200, '/account/recover':200,
                               '/account/register':503, '/submit':503, '/agents':200}.items():
            assert status(path) == expected, path
        with sqlite3.connect(database) as db:
            assert db.execute("SELECT 1 FROM sqlite_master WHERE name='private_accounts'").fetchone()
            assert 'owner_user_id' in {row[1] for row in db.execute('PRAGMA table_info(agent_grants)')}
        proof = {'commit':args.commit, 'previous_commit':previous.name, 'source_archive_sha256':archive_hash,
                 'preserved_counts':before, 'migration_verified':True, 'readiness':200,
                 'public_intake_closed':True, 'rollback':str(rollback)}
        (rollback / 'deployment.json').write_text(json.dumps(proof, indent=2) + '\n')
        print(json.dumps(proof))
    except Exception:
        if saved:
            run('systemctl', 'stop', 'airr-intake.service')
            switch(previous)
            # Intake stayed closed throughout; do not apply this rollback
            # procedure to a live intake with newly received manuscripts.
            snapshot(rollback / 'intake.sqlite3', database)
        run('systemctl', 'start', 'airr-intake.service')
        raise
    finally:
        resume_background(timers)


if __name__ == '__main__':
    main()
