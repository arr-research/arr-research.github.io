# SPDX-License-Identifier: AGPL-3.0-or-later
"""Host-only exact v1 reconciliation; official release AND AIRR mirror required.

Default is read-only. Does not create scope, grants, cases, receipts, permissions
or a publication record. Requires the native case already marked published.
Requires immutable metadata, exact public release-tag asset membership and bytes,
plus exact AIRR mirror bytes. Existing helpers remain unchanged. No authority
is created; both public witnesses and an already-published exact native case must exist.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import stat
import re
import subprocess
import urllib.request

PID = 'ARR-2026-4T35VQ6MZB8F99F4'
RECORD = 'arr:record:9a197773-53eb-43d2-9791-9c2d49ea5b17'
DIGEST = 'fbd2b9784d11740cef74c85f870dff27e4b97158210388cf3ae355eb4ffcbcf3'
PDF_BYTES = 370582
CASE = 'SUB-670D054094713B92'
TAG = PID + '-v1'
ASSET_NAME = TAG + '.pdf'
RELEASE = 'https://github.com/arr-research/arr-research.github.io/releases/tag/' + TAG
RELEASE_API = 'https://api.github.com/repos/arr-research/arr-research.github.io/releases/tags/' + TAG
MIRROR_PDF = 'https://airr.science/papers/' + PID + '/' + ASSET_NAME
NEW = {'record_id': RECORD,
       'version_id': 'arr:version:d0091425-03c9-47ee-8e38-b46da15c789c',
       'version': 'v1', 'canonical_sha256': DIGEST,
       'authors': ['Lluis Eriksson']}
APP_CONFIG_SHA256 = '7db0f6910059aa77eb6adceef0760d3d5a2128a571828af2b6bcb2df7f3977ce'


def verify_live_service():
    """Check the running immutable factory and its actual configuration inputs.

    Never print the environment: it includes private service credentials.
    Require the same physical files, not just matching source defaults.
    """
    pid = subprocess.check_output(
        ['systemctl', 'show', 'airr-intake.service', '--property=MainPID', '--value'],
        text=True, timeout=10).strip()
    if not pid.isdecimal() or int(pid) <= 1:
        raise ValueError('Running intake service required')
    proc = Path('/proc') / pid
    cwd = (proc / 'cwd').resolve(strict=True)
    if cwd != Path('/opt/airr-intake/current').resolve(strict=True):
        raise ValueError('Running release differs from current release')
    command = (proc / 'cmdline').read_bytes()
    if b'gunicorn' not in command or b'services.intake.app:create_app()' not in command:
        raise ValueError('Unexpected running service command')
    env = dict(item.decode().split('=', 1) for item in
               (proc / 'environ').read_bytes().split(b'\0') if b'=' in item)
    # This pinned factory defines DATABASE as ARR_INTAKE_INSTANCE/intake.sqlite3
    # and the catalogue/author directly from these environment variables.
    # Do not call create_app here: startup chmod/mkdir are not read-only checks.
    if hashlib.sha256((cwd / 'services/intake/app.py').read_bytes()).hexdigest() != APP_CONFIG_SHA256:
        raise ValueError('Unreviewed live configuration factory; reconcile before use')
    if (not (Path(env['ARR_INTAKE_INSTANCE']) / 'intake.sqlite3').samefile(
                '/srv/airr-private/instance/intake.sqlite3')
            or not Path(env['AIRR_HISTORICAL_REVISION_CATALOGUE']).samefile(
                '/srv/airr-private/historical-revisions/catalogue.json')
            or env['AIRR_HISTORICAL_OPERATOR_AUTHOR'] != 'Lluis Eriksson'):
        raise ValueError('Live database/catalogue/sole-author configuration mismatch')
    return pid


def public(url, limit, accept=None):
    headers = {'User-Agent': 'AIRR-exact-release-integrity'}
    if accept:
        headers['Accept'] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        if response.status != 200 or not response.url.startswith('https://'):
            raise ValueError('Public HTTPS200 required')
        raw = response.read(limit + 1)
    if len(raw) > limit:
        raise ValueError('Oversized public artifact')
    return raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--case', required=True, help='Actual exact native published case')
    parser.add_argument('--metadata-commit', required=True, help='Full immutable public metadata commit')
    parser.add_argument('--asset-id', required=True, type=int,
                        help='Actual PDF asset ID belonging to the published v1 tag')
    args = parser.parse_args()
    if args.case != CASE:
        raise ValueError('Exact actual native case ID required')
    if not re.fullmatch(r'[a-f0-9]{40}', args.metadata_commit):
        raise ValueError('Full immutable publication commit required')
    if args.asset_id <= 0:
        raise ValueError('Actual positive release asset ID required')
    if os.name != 'posix':
        raise ValueError('Existing AIRR Linux host only')
    service_pid = verify_live_service()
    base = ('https://raw.githubusercontent.com/arr-research/arr-research.github.io/'
            + args.metadata_commit + '/papers/2026/11/4T/' + PID)
    metadata_raw = public(base + '/metadata.json', 100000)
    meta = json.loads(metadata_raw)
    if (meta['id'] != PID or meta['authors'] != [{'name': 'Lluis Eriksson',
                                                'affiliation': 'Independent researcher'}]
            or any(meta[k] != NEW[k] for k in ('record_id', 'version_id', 'version'))
            or meta.get('status') != 'working_paper'
            or meta['integrity']['canonical_sha256'] != DIGEST
            or meta.get('supersedes_version_id') is not None):
        raise ValueError('Immutable published identity/author/predecessor mismatch')
    release = json.loads(public(RELEASE_API, 1000000, 'application/vnd.github+json'))
    if (release.get('tag_name') != TAG or release.get('html_url') != RELEASE
            or release.get('draft') is not False or not release.get('published_at')
            or not isinstance(release.get('assets'), list)):
        raise ValueError('Actual public v1 release identity required')
    matching = [asset for asset in release['assets']
                if asset.get('id') == args.asset_id or asset.get('name') == ASSET_NAME]
    if (len(matching) != 1 or matching[0].get('id') != args.asset_id
            or matching[0].get('name') != ASSET_NAME
            or matching[0].get('size') != PDF_BYTES
            or matching[0].get('state') != 'uploaded'
            or matching[0].get('browser_download_url') !=
            'https://github.com/arr-research/arr-research.github.io/releases/download/' + TAG + '/' + ASSET_NAME):
        raise ValueError('Exact PDF asset ID/name/size must belong to actual v1 release')
    pdf = public('https://api.github.com/repos/arr-research/arr-research.github.io/'
                 'releases/assets/' + str(args.asset_id), 1000000, 'application/octet-stream')
    if len(pdf) != PDF_BYTES or hashlib.sha256(pdf).hexdigest() != DIGEST:
        raise ValueError('Exact authoritative official-release PDF mismatch')
    mirror_pdf = public(MIRROR_PDF, 1000000)
    if len(mirror_pdf) != PDF_BYTES or hashlib.sha256(mirror_pdf).hexdigest() != DIGEST:
        raise ValueError('Exact public AIRR mirror PDF mismatch')
    path = Path('/srv/airr-private/historical-revisions/catalogue.json').resolve()
    db = sqlite3.connect('/srv/airr-private/instance/intake.sqlite3', timeout=15)
    try:
        db.execute('BEGIN IMMEDIATE')
        # Mandatory shared writer protocol; see docs/CATALOGUE-WRITER-PROTOCOL.md.
        # No grant issuer or supported catalogue writer may cross this lock.
        raw = path.read_bytes()
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError('Catalogue must be an object')
        if PID in data and data[PID] != NEW:
            raise ValueError('Unexpected existing entry; do not overwrite')
        case = db.execute('SELECT sha256,public_release_url,public_released_at '
                          'FROM submissions WHERE id=?', (args.case,)).fetchone()
        if not case or case[0] != DIGEST or case[1] != RELEASE or not case[2]:
            raise ValueError('Native exact case must already be marked published')
        active = db.execute("SELECT count(*) FROM historical_revision_grants h JOIN "
                            "agent_grants g ON h.grant_id=g.id WHERE g.state='approved' "
                            "AND g.uses=0 AND julianday(g.expires_at)>julianday('now')").fetchone()[0]
        if active:
            raise ValueError('Live unused historical grant; reconcile before changing catalogue')
        if data.get(PID) == NEW:
            print(json.dumps({'status': 'already_reconciled', 'mutated': False,
                              'active_unused_grants': active, 'unrelated_entries_preserved': len(data)-1,
                              'official_release_verified': True, 'AIRR_mirror_verified': True}))
            return
        result = {'status': 'verified_absent_public_predecessor', 'mutated': False,
                  'active_unused_grants': active, 'unrelated_entries_preserved': len(data),
                  'old_sha256': hashlib.sha256(raw).hexdigest(), 'entry': NEW,
                  'creates_permission_or_publication': False,
                  'public_witness': 'official_GitHub_release_exact_asset_' + str(args.asset_id),
                  'official_release_tag': TAG, 'release_asset_name': ASSET_NAME,
                  'metadata_commit': args.metadata_commit,
                  'metadata_sha256': hashlib.sha256(metadata_raw).hexdigest(),
                  'AIRR_mirror_verified': True, 'AIRR_mirror_url': MIRROR_PDF}
        if not args.apply:
            print(json.dumps(result))
            return
        if path.read_bytes() != raw:
            raise ValueError('Concurrent catalogue change')
        if verify_live_service() != service_pid:
            raise ValueError('Service restarted during preparation; inspect before retry')
        backup = Path('/srv/airr-private/tep-catalogue-before354-v1-two-witnesses.json')
        with backup.open('xb') as stream:
            os.chmod(backup, 0o600)
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        previous = dict(data)
        data[PID] = NEW
        if any(data[k] != value for k, value in previous.items() if k != PID):
            raise ValueError('Unrelated entry changed')
        new = (json.dumps(data, sort_keys=True, indent=2) + '\n').encode()
        tmp = path.with_name('catalogue.354-v1-two-witnesses.tmp')
        mode = path.stat()
        with tmp.open('xb') as stream:
            stream.write(new)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(tmp, stat.S_IMODE(mode.st_mode))
        os.chown(tmp, mode.st_uid, mode.st_gid)
        os.replace(tmp, path)
        if path.read_bytes() != new:
            raise ValueError('Catalogue readback mismatch')
        db.commit()
        result.update(status='reconciled_verified_public_v1', mutated=True,
                      new_sha256=hashlib.sha256(new).hexdigest(), backup=str(backup))
        print(json.dumps(result))
    finally:
        db.rollback()
        db.close()


if __name__ == '__main__':
    main()
