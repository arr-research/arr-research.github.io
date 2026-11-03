"""Explicit installation of one restricted editorial public key. Root only."""
import argparse
import hashlib
import os
from pathlib import Path
import re
import urllib.request


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--commit', required=True)
    p.add_argument('--sha256', required=True)
    p.add_argument('--public-key', required=True)
    p.add_argument('--activate', action='store_true')
    a = p.parse_args()
    if os.getuid() != 0:
        raise SystemExit('Root console required.')
    if not re.fullmatch('[a-f0-9]{40}', a.commit) or not re.fullmatch('[a-f0-9]{64}', a.sha256):
        raise SystemExit('Pinned commit and script digest required.')
    if not re.fullmatch(r'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5[A-Za-z0-9+/]{48}', a.public_key):
        raise SystemExit('An exact Ed25519 public key is required.')
    for path in [Path('/opt/airr-intake/current').resolve(), Path('/opt/airr-intake/venv'), Path('/etc/airr-intake/intake.env')]:
        stat = path.stat()
        if stat.st_uid or stat.st_mode & 0o022:
            raise SystemExit('Application, runtime and config must be administrator-owned and not writable by other users.')
    root = Path('/usr/local/lib/airr-delegated')
    launcher = Path('/usr/local/sbin/airr-editorial-ssh')
    authorized = Path('/root/.ssh/authorized_keys')
    old = authorized.read_bytes()
    if a.public_key.encode().split()[1] in old or b'airr-editorial-20260914' in old:
        raise SystemExit('A key already exists. Inspect or explicitly revoke it; do not duplicate or replace.')
    url = f'https://raw.githubusercontent.com/arr-research/arr-research.github.io/{a.commit}/services/intake/deploy/editorial_ssh.py'
    raw = urllib.request.urlopen(url, timeout=30).read(100001)
    if len(raw) > 100000 or hashlib.sha256(raw).hexdigest() != a.sha256:
        raise SystemExit('Pinned bridge digest mismatch.')
    compile(raw, 'editorial_ssh.py', 'exec')
    if not a.activate:
        print('Preflight passed. No server files or access permissions changed.')
        return
    root.mkdir(mode=0o755, parents=True, exist_ok=True)
    if root.stat().st_uid or root.stat().st_mode & 0o022:
        raise SystemExit('Bridge directory is not protected.')
    bridge = root/'editorial_ssh.py'
    bridge.write_bytes(raw); bridge.chmod(0o644)
    envfile = root/'editorial-env'
    envfile.write_text('#!/bin/sh\nset -eu\nset -a\n. /etc/airr-intake/intake.env\nset +a\ncd /opt/airr-intake/current\nexec /opt/airr-intake/venv/bin/python -I /usr/local/lib/airr-delegated/editorial_ssh.py\n')
    envfile.chmod(0o700)
    launcher.write_text('#!/bin/sh\nexec /usr/bin/env -i PATH=/usr/bin:/bin SSH_ORIGINAL_COMMAND="$SSH_ORIGINAL_COMMAND" /bin/sh /usr/local/lib/airr-delegated/editorial-env\n')
    launcher.chmod(0o700)
    entry = f'restrict,expiry-time="20261213235959Z",command="/usr/local/sbin/airr-editorial-ssh" {a.public_key} airr-editorial-20260914\n'.encode()
    # Preserve all existing keys; this uniquely labelled key can be revoked alone.
    temp = authorized.with_name('authorized_keys.airr-pending')
    with temp.open('xb') as f:
        f.write(old + (b'\n' if old and not old.endswith(b'\n') else b'') + entry)
    temp.chmod(0o600)
    os.replace(temp, authorized)
    print('Restricted editorial key installed; expires 2026-12-13 23:59:59 UTC. Live verification is still required.')


if __name__ == '__main__':
    main()
