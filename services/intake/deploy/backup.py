#!/usr/bin/python3
"""Consistent SQLite snapshot plus exact immutable files, encrypted to an offline age key.

Requires a mounted private volume. Never writes an unencrypted archive outside it.
The output must also be copied to independent storage and verified there.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import tarfile
import tempfile
from datetime import datetime, timezone, timedelta

ROOT = Path('/srv/airr-private')
DEST = Path('/var/backups/airr')


def main():
    if os.geteuid() != 0 or not os.path.ismount(ROOT):
        raise RuntimeError('The encrypted volume must be mounted; backup aborted.')
    recipient = Path('/etc/airr-intake/backup-recipient.txt').read_text().strip()
    if not recipient.startswith('age1'):
        raise RuntimeError('Missing offline recovery recipient')
    DEST.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.umask(0o077)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    output = DEST / ('airr-' + stamp + '.tar.gz.age')
    pending = output.with_suffix('.partial')
    if output.exists() or pending.exists():
        raise RuntimeError('Snapshot already exists; refusing replacement.')
    with tempfile.TemporaryDirectory(prefix='backup-', dir=ROOT) as work:
        stage = Path(work)
        (stage / 'instance' / 'quarantine').mkdir(parents=True)
        source = sqlite3.connect(ROOT / 'instance' / 'intake.sqlite3')
        snapshot = sqlite3.connect(stage / 'instance' / 'intake.sqlite3')
        source.backup(snapshot)
        source.close()
        if snapshot.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise RuntimeError('Database integrity check failed')
        manifest = {'created_at': stamp, 'files': {}}
        for stored, expected in snapshot.execute("SELECT stored_name,sha256 FROM submissions WHERE stored_name NOT LIKE 'deleted-%'"):
            path = ROOT / 'instance' / 'quarantine' / stored
            if path.parent != ROOT / 'instance' / 'quarantine' or not path.is_file():
                # Infected bytes are deliberately removed immediately.
                state = snapshot.execute('SELECT scan_status FROM submissions WHERE stored_name=?', (stored,)).fetchone()[0]
                if state == 'infected':
                    continue
                raise RuntimeError('A referenced manuscript disappeared; retry after the retention job finishes.')
            destination = stage / 'instance' / 'quarantine' / stored
            # Manuscript files are immutable. A hard link pins the exact inode
            # across retention deletion without doubling private-volume usage.
            os.link(path, destination)
            with destination.open('rb') as handle:
                actual = hashlib.file_digest(handle, 'sha256').hexdigest()
            if actual != expected:
                raise RuntimeError('A manuscript does not match the recorded fingerprint.')
            manifest['files'][stored] = actual
        snapshot.close()
        shutil.copytree(ROOT / 'secrets', stage / 'secrets')
        (stage / 'manifest.json').write_text(json.dumps(manifest, indent=2))
        # The only plaintext tar stream is a pipe between gzip and age.
        with pending.open('xb') as encrypted:
            process = subprocess.Popen(['/usr/bin/age', '-r', recipient], stdin=subprocess.PIPE, stdout=encrypted)
            try:
                with tarfile.open(fileobj=process.stdin, mode='w|gz') as archive:
                    for name in ('instance', 'secrets', 'manifest.json'):
                        archive.add(stage / name, arcname=name)
                process.stdin.close()
                if process.wait(timeout=300) != 0:
                    raise RuntimeError('Encryption failed')
            except Exception:
                process.kill()
                process.wait()
                pending.unlink(missing_ok=True)
                raise
        pending.rename(output)
    with output.open('rb') as handle:
        checksum = hashlib.file_digest(handle, 'sha256').hexdigest()
    output.with_suffix(output.suffix + '.sha256').write_text(checksum + '  ' + output.name + '\n')
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    snapshots = sorted(DEST.glob('airr-*.tar.gz.age'))
    keep = set(snapshots[-3:])
    for old in snapshots:
        if old == output or old.is_symlink() or not old.is_file():
            continue
        try:
            created = datetime.strptime(old.name, 'airr-%Y%m%dT%H%M%SZ.tar.gz.age').replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        if created < cutoff or old not in keep:
            old.unlink()
            old.with_suffix(old.suffix + '.sha256').unlink(missing_ok=True)
    print(json.dumps({'snapshot': str(output), 'sha256': checksum, 'verified_manuscripts': len(manifest['files'])}))


if __name__ == '__main__':
    main()
