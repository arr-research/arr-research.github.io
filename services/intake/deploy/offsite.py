#!/usr/bin/python3
"""Copy only a completed age snapshot to B2; verify the downloaded bytes.

No plaintext manuscripts, decryption keys, broad sync or remote deletion.
The bucket lifecycle is configured separately by its owner.
"""
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path('/srv/airr-private')
SNAPSHOTS = Path('/var/backups/airr')
CONFIG = Path('/etc/airr-intake/offsite.json')
STATE = Path('/var/lib/airr-offsite/status.json')
RCLONE_CONFIG = ROOT / 'secrets/b2-rclone.conf'
NAME = re.compile(r'airr-(\d{8}T\d{6}Z)\.tar\.gz\.age')


def utcnow():
    return datetime.now(timezone.utc)


def checksum(path):
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def latest_snapshot(directory, max_bytes):
    candidates = sorted(p for p in directory.glob('airr-*.tar.gz.age') if NAME.fullmatch(p.name))
    if not candidates:
        raise RuntimeError('No completed encrypted snapshot is available.')
    snapshot = candidates[-1]
    sidecar = snapshot.with_suffix(snapshot.suffix + '.sha256')
    for path in (snapshot, sidecar):
        if path.is_symlink() or not path.is_file() or path.resolve().parent != directory.resolve():
            raise RuntimeError('Snapshot or checksum path is unsafe or incomplete.')
    created = datetime.strptime(NAME.fullmatch(snapshot.name)[1], '%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc)
    age = utcnow() - created
    if age < timedelta(minutes=-5) or age > timedelta(hours=30):
        raise RuntimeError('The latest snapshot is stale or has an invalid timestamp.')
    size = snapshot.stat().st_size
    if size <= 0 or size > max_bytes:
        raise RuntimeError('Snapshot exceeds the configured transfer limit; review account caps.')
    with snapshot.open('rb') as handle:
        if handle.read(22) != b'age-encryption.org/v1\n':
            # The header is 22 bytes, including its trailing newline.
            raise RuntimeError('Only binary age-encrypted snapshots may leave the server.')
    parts = sidecar.read_text().strip().split()
    if len(parts) != 2 or not re.fullmatch(r'[a-f0-9]{64}', parts[0]) or parts[1] != snapshot.name:
        raise RuntimeError('Snapshot checksum record is invalid.')
    if checksum(snapshot) != parts[0]:
        raise RuntimeError('The local encrypted snapshot failed its integrity check.')
    return snapshot, sidecar, parts[0], size, created


def remote_for(settings):
    if settings.get('enabled') is not True:
        raise RuntimeError('Offsite transfer is not enabled.')
    bucket = settings.get('bucket', '')
    if not re.fullmatch(r'airr-intake-backups-eu-[a-z0-9-]+', bucket):
        raise RuntimeError('Unexpected offsite bucket.')
    if settings.get('prefix') != 'intake/' or settings.get('region') != 'eu-central-003':
        raise RuntimeError('Unexpected offsite prefix or region.')
    limit = settings.get('max_snapshot_bytes')
    if type(limit) is not int or not 1 <= limit <= 500_000_000:
        raise RuntimeError('An explicit transfer limit of at most 500 MB is required.')
    return 'airrb2:' + bucket + '/intake/', limit


def rclone(*args):
    command = ['/usr/bin/rclone', '--config', str(RCLONE_CONFIG),
        '--contimeout', '20s', '--timeout', '60s', '--retries', '2', '--low-level-retries', '2',
        '--transfers', '1', '--checkers', '1', '--bwlimit', '8M', '--log-level', 'ERROR', *args]
    result = subprocess.run(command, capture_output=True, text=True, timeout=600)
    if result.returncode:
        # Do not echo provider responses or auth headers into the journal.
        raise RuntimeError('B2 operation failed; check connectivity, credentials and account caps.')
    return result.stdout


def downloaded_checksum(remote):
    # Stream a full download into a hash without retaining another archive.
    command = ['/usr/bin/rclone', '--config', str(RCLONE_CONFIG), '--contimeout', '20s',
        '--timeout', '60s', '--retries', '1', '--low-level-retries', '1',
        '--bwlimit', '8M', '--log-level', 'ERROR', 'cat', remote]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    digest = hashlib.sha256()
    try:
        for chunk in iter(lambda: process.stdout.read(1024 * 1024), b''):
            digest.update(chunk)
        process.stdout.close()
        if process.wait(timeout=90):
            raise RuntimeError('The B2 verification download failed.')
    except BaseException:
        process.kill()
        process.wait()
        raise
    return digest.hexdigest()


def transfer(settings):
    remote, limit = remote_for(settings)
    snapshot, sidecar, expected, size, created = latest_snapshot(SNAPSHOTS, limit)
    target = remote + snapshot.name
    rclone('copyto', str(snapshot), target, '--immutable', '--checksum')
    info = json.loads(rclone('lsjson', target, '--stat'))
    if info.get('IsDir') or info.get('Size') != size:
        raise RuntimeError('The uploaded snapshot has an unexpected size.')
    if downloaded_checksum(target) != expected:
        raise RuntimeError('Downloaded B2 bytes differ from the verified local snapshot.')
    rclone('copyto', str(sidecar), target + '.sha256', '--immutable', '--checksum')
    return {'ok': True, 'verified_at': utcnow().isoformat(), 'snapshot_at': created.isoformat(),
        'snapshot': snapshot.name, 'sha256': expected, 'bytes': size, 'bucket': settings['bucket'],
        'region': settings['region'], 'download_verified': True}


def save_status(value):
    STATE.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    pending = STATE.with_suffix('.pending')
    pending.write_text(json.dumps(value, indent=2))
    pending.replace(STATE)


def main():
    os.umask(0o077)
    try:
        if os.geteuid() != 0 or not os.path.ismount(ROOT):
            raise RuntimeError('The encrypted volume must be mounted for offsite transfer.')
        if RCLONE_CONFIG.is_symlink() or RCLONE_CONFIG.stat().st_mode & 0o077:
            raise RuntimeError('The B2 credential file is not private.')
        settings = json.loads(CONFIG.read_text())
        status = transfer(settings)
    except Exception as error:
        # Messages from our own RuntimeErrors are deliberately credential-free.
        status = {'ok':False, 'attempted_at':utcnow().isoformat(),
            'error': str(error) if type(error) is RuntimeError else type(error).__name__}
        save_status(status)
        print(json.dumps(status))
        return 1
    save_status(status)
    print(json.dumps(status))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
