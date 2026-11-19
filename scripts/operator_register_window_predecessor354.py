# SPDX-License-Identifier: AGPL-3.0-or-later
"""Host-only exact v1 or v2 reconciliation; official release AND AIRR mirror required.

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
from urllib.parse import urlsplit

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
V2_CASE = 'SUB-973BC089595D6A26'
V2 = {**NEW, 'version': 'v2',
      'version_id': 'arr:version:c6363401-35d3-4d12-ac51-6210cd61d288',
      'canonical_sha256': 'd617dc40ae813e50894dede5ea8f73c113f20e7d52b218c74ee9cc3656bae014'}
SHELL_CASE = 'SUB-15AB00123A598331'
SHELL_ID = 'ARR-2026-2B2W1WQ7DF9N5VW7'
SHELL_COMMIT = 'f4bbc6f50afef4337b76175312c84284891a2fef'
SHELL_PDF_ASSET = 762639932
SHELL_V1 = {'record_id': 'arr:record:4b1703cb-9daf-4d4b-be1c-825c4243ecbb',
            'version_id': 'arr:version:2523e2c1-9b71-4986-be81-931bf48e2ea4',
            'version': 'v1',
            'canonical_sha256': '32dc8014a45b981f7adff96cb8a6946923a8c093bf7ab8375d55347032d56bcd',
            'authors': ['Lluis Eriksson']}
# Pins from the immutable first releases and their original intake receipts.
PINNED_V1 = {
    'SUB-ACCEA0EE2952069D': {
        'paper': 'ARR-2026-2FDKAKD7CC9G4BNQ', 'commit': 'c0094bed56c7daa7e53e8d9091d0f3161d3d7784',
        'asset': 768718565, 'bytes': 243849,
        'entry': {'record_id': 'arr:record:4f6cd536-9d8c-4c08-bade-2c4386d1315a',
                  'version_id': 'arr:version:90163fc0-6fd6-46db-aa53-6bdf377600c9',
                  'canonical_sha256': '6705413f1da5f3bc8fdf325d2c6e2ed2fc0ce1b920827b885c8eba170b2fcb61',
                  'version': 'v1', 'authors': ['Lluis Eriksson']},
    },
    'SUB-89DC4655B42EC065': {
        'paper': 'ARR-2026-54GRS2WX6182EVEB', 'commit': '4b74a6d7b726c83cae36d23ffd5f64e1da33b2ca',
        'asset': 766435224, 'bytes': 295919,
        'entry': {'record_id': 'arr:record:a486322e-74c1-409d-b72c-97a4ac7fe9c5',
                  'version_id': 'arr:version:13fea17f-561a-46c6-92ea-81c47c8b815e',
                  'canonical_sha256': '834b1c5312f6060514c0c1465564138534e3574707f6db41f044a46e50c2fd41',
                  'version': 'v1', 'authors': ['Lluis Eriksson']},
    },
    'SUB-48EF3BDD79BBA4B0': {
        'paper': 'ARR-2026-2SH3CGGBHG9Q5BYN', 'commit': 'f5b5519265af1a600ad8b69b599c4d205704d205',
        'asset': 766198128, 'bytes': 438313,
        'entry': {'record_id': 'arr:record:5988d908-2e30-4dca-bf54-0a2eb715db2d',
                  'version_id': 'arr:version:0a812b4d-a488-4467-9cb7-6c1a0438ea66',
                  'canonical_sha256': '382c71a1e7c1a07cbd78520dd9bf135d4cdbb3c0c2ed08841e23796850febcec',
                  'version': 'v1', 'authors': ['Lluis Eriksson']},
    },
    'SUB-E8772979C782BC39': {
        'paper': 'ARR-2026-56MSF5D1YA8QDAXM', 'commit': 'b4e16557daf300d006501b9f2367e2a9e19a37f7',
        'asset': 766053026, 'bytes': 288851,
        'entry': {'record_id': 'arr:record:a6a65e56-87ca-45da-aed2-30a41cf46ee0',
                  'version_id': 'arr:version:d970fce2-faf5-451b-abff-ce4a5cbc68ac',
                  'canonical_sha256': '8d020090d405db8f5db806b0ac7f61561325cb9ceb585972a1bd5a3e0b6ce828',
                  'version': 'v1', 'authors': ['Lluis Eriksson']},
    },
}
APP_CONFIG_SHA256 = '7db0f6910059aa77eb6adceef0760d3d5a2128a571828af2b6bcb2df7f3977ce'
ISSUER_SOURCE_SHA256 = {
    'services/intake/programme_delegations.py': '459a854d2a19745ac5a9783c3ea023d3383727e49d7b797d45b4afb833d8d815',
    'services/intake/historical_revisions.py': '26c3ddf0abe9ad847ac8667917e809c4e573a86181b71e0e2d601b0b880d780b',
}


def mount_points(raw):
    points = set()
    for line in raw.splitlines():
        fields = line.split()
        if len(fields) < 10 or '-' not in fields:
            raise ValueError('Invalid mount namespace evidence')
        points.add(re.sub(r'\\([0-7]{3})', lambda m: chr(int(m[1], 8)), fields[4]))
    if not points:
        raise ValueError('Missing mount namespace evidence')
    return points


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
    if any(hashlib.sha256((cwd / name).read_bytes()).hexdigest() != digest
           for name, digest in ISSUER_SOURCE_SHA256.items()):
        raise ValueError('Unreviewed live grant issuers; reconcile deployment before use')
    instance = Path(env['ARR_INTAKE_INSTANCE'])
    catalogue = Path(env['AIRR_HISTORICAL_REVISION_CATALOGUE'])
    if not instance.is_absolute() or not catalogue.is_absolute():
        raise ValueError('Absolute live configuration paths required')
    own_mounts = mount_points(Path('/proc/self/mountinfo').read_text())
    service_mounts = mount_points((proc / 'mountinfo').read_text())
    for configured, canonical in (
            (instance / 'intake.sqlite3', Path('/srv/airr-private/instance/intake.sqlite3')),
            (catalogue, Path('/srv/airr-private/historical-revisions/catalogue.json'))):
        service_path = proc / 'root' / str(configured).lstrip('/')
        if (configured.resolve(strict=True) != canonical.resolve(strict=True)
                or not configured.samefile(canonical)
                or not service_path.samefile(canonical)
                or not service_path.parent.samefile(canonical.parent)):
            raise ValueError('Live canonical path or mount mismatch')
        # A file bind mount can retain an old catalogue inode after replace or
        # give SQLite a different journal/WAL directory despite matching inodes.
        names = {str(configured), str(canonical), str(canonical.resolve(strict=True))}
        if canonical.name == 'intake.sqlite3':
            names |= {name + suffix for name in tuple(names) for suffix in ('-journal', '-wal', '-shm')}
        if names & (own_mounts | service_mounts):
            raise ValueError('Individual database/catalogue/sidecar mount is unsupported')
    if env['AIRR_HISTORICAL_OPERATOR_AUTHOR'] != 'Lluis Eriksson':
        raise ValueError('Live database/catalogue/sole-author configuration mismatch')
    # Field22 is starttime; comm may contain spaces and closing parentheses.
    starttime = (proc / 'stat').read_text().rsplit(')', 1)[1].split()[19]
    return (pid, starttime, catalogue, proc / 'root' / str(catalogue).lstrip('/'))


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result


def public(url, limit, accept=None):
    headers = {'User-Agent': 'AIRR-exact-release-integrity'}
    if accept:
        headers['Accept'] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        if response.status != 200 or not response.url.startswith('https://'):
            raise ValueError('Public HTTPS200 required')
        requested, final = urlsplit(url), urlsplit(response.url)
        allowed = {requested.hostname}
        if requested.hostname == 'api.github.com' and accept == 'application/octet-stream':
            allowed.update({'release-assets.githubusercontent.com', 'objects.githubusercontent.com'})
        if (requested.hostname not in {'airr.science', 'api.github.com', 'raw.githubusercontent.com'}
                or final.hostname not in allowed or final.username or final.password
                or final.port not in (None, 443)):
            raise ValueError('Public witness redirect origin mismatch')
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
    paper_id, record_id, shard, backup_key = PID, RECORD, '4T', '354'
    if args.case in PINNED_V1:
        expected = PINNED_V1[args.case]
        if args.metadata_commit != expected['commit'] or args.asset_id != expected['asset']:
            raise ValueError('Expected the immutable v1 metadata and PDF asset')
        paper_id, target, predecessor = expected['paper'], expected['entry'], None
        record_id = target['record_id']
        shard = paper_id.split('-')[-1][:2]
        backup_key = paper_id.lower()
        tag = paper_id + '-v1'
        asset_name, pdf_bytes = tag + '.pdf', expected['bytes']
        release_url = RELEASE.removesuffix(TAG) + tag
        release_api = RELEASE_API.removesuffix(TAG) + tag
        mirror = 'https://airr.science/papers/' + paper_id + '/versions/v1/' + asset_name
        metadata_path = '/metadata.json'
    elif args.case == SHELL_CASE:
        target, predecessor = SHELL_V1, None
        paper_id, record_id, shard, backup_key = SHELL_ID, target['record_id'], '2B', 'shell-trap'
        tag = paper_id + '-v1'
        asset_name, pdf_bytes = tag + '.pdf', 311003
        release_url = RELEASE.removesuffix(TAG) + tag
        release_api = RELEASE_API.removesuffix(TAG) + tag
        mirror = 'https://airr.science/papers/' + paper_id + '/versions/v1/' + asset_name
        metadata_path = '/metadata.json'
        if args.metadata_commit != SHELL_COMMIT or args.asset_id != SHELL_PDF_ASSET:
            raise ValueError('Published shell v1 metadata commit and PDF asset required')
    elif args.case == V2_CASE:
        target, predecessor = V2, NEW
        tag = PID + '-v2'
        asset_name = tag + '.pdf'
        pdf_bytes = 398180
        mirror = 'https://airr.science/papers/' + PID + '/versions/v2/' + asset_name
        release_url = RELEASE.removesuffix(TAG) + tag
        release_api = RELEASE_API.removesuffix(TAG) + tag
        metadata_path = '/versions/v2/metadata.json'
    elif args.case == CASE:
        target, predecessor = NEW, None
        tag, asset_name, pdf_bytes = TAG, ASSET_NAME, PDF_BYTES
        mirror, release_url, release_api = MIRROR_PDF, RELEASE, RELEASE_API
        metadata_path = '/metadata.json'
    else:
        raise ValueError('Exact actual native case ID required')
    if not re.fullmatch(r'[a-f0-9]{40}', args.metadata_commit):
        raise ValueError('Full immutable publication commit required')
    if args.asset_id <= 0:
        raise ValueError('Actual positive release asset ID required')
    if os.name != 'posix':
        raise ValueError('Existing AIRR Linux host only')
    service_pid = verify_live_service()
    base = ('https://raw.githubusercontent.com/arr-research/arr-research.github.io/'
            + args.metadata_commit + '/papers/2026/11/' + shard + '/' + paper_id)
    metadata_raw = public(base + metadata_path, 100000)
    meta = json.loads(metadata_raw, object_pairs_hook=unique_object)
    if (meta['id'] != paper_id or meta['authors'] != [{'name': 'Lluis Eriksson',
                                                'affiliation': 'Independent researcher'}]
            or any(meta[k] != target[k] for k in ('record_id', 'version_id', 'version'))
            or meta.get('status') != 'working_paper'
            or meta['integrity']['canonical_sha256'] != target['canonical_sha256']
            or meta.get('supersedes_version_id') != (predecessor['version_id'] if predecessor else None)):
        raise ValueError('Immutable published identity/author/predecessor mismatch')
    release = json.loads(public(release_api, 1000000, 'application/vnd.github+json'),
                         object_pairs_hook=unique_object)
    if (release.get('tag_name') != tag or release.get('html_url') != release_url
            or release.get('draft') is not False or not release.get('published_at')
            or not isinstance(release.get('assets'), list)):
        raise ValueError('Actual public release identity required')
    matching = [asset for asset in release['assets']
                if asset.get('id') == args.asset_id or asset.get('name') == asset_name]
    if (len(matching) != 1 or matching[0].get('id') != args.asset_id
            or matching[0].get('name') != asset_name
            or matching[0].get('size') != pdf_bytes
            or matching[0].get('state') != 'uploaded'
            or matching[0].get('browser_download_url') !=
            'https://github.com/arr-research/arr-research.github.io/releases/download/' + tag + '/' + asset_name):
        raise ValueError('Exact PDF asset ID/name/size must belong to actual published release')
    pdf = public('https://api.github.com/repos/arr-research/arr-research.github.io/'
                 'releases/assets/' + str(args.asset_id), 1000000, 'application/octet-stream')
    if len(pdf) != pdf_bytes or hashlib.sha256(pdf).hexdigest() != target['canonical_sha256']:
        raise ValueError('Exact authoritative official-release PDF mismatch')
    mirror_pdf = public(mirror, 1000000)
    if len(mirror_pdf) != pdf_bytes or hashlib.sha256(mirror_pdf).hexdigest() != target['canonical_sha256']:
        raise ValueError('Exact public AIRR mirror PDF mismatch')
    path = Path('/srv/airr-private/historical-revisions/catalogue.json').resolve()
    database = Path('/srv/airr-private/instance/intake.sqlite3')
    db = sqlite3.connect(database.as_uri() + '?mode=rw', uri=True, timeout=15)
    try:
        db.execute('BEGIN IMMEDIATE')
        # Mandatory shared writer protocol; see docs/CATALOGUE-WRITER-PROTOCOL.md.
        # No grant issuer or supported catalogue writer may cross this lock.
        raw = path.read_bytes()
        data = json.loads(raw, object_pairs_hook=unique_object)
        if not isinstance(data, dict):
            raise ValueError('Catalogue must be an object')
        expected_parent = (data.get(paper_id) == predecessor if predecessor else paper_id not in data)
        if data.get(paper_id) != target and not expected_parent:
            raise ValueError('Unexpected existing entry; do not overwrite')
        case = db.execute('SELECT sha256,public_release_url,public_released_at '
                          'FROM submissions WHERE id=?', (args.case,)).fetchone()
        if not case or case[0] != target['canonical_sha256'] or case[1] != release_url or not case[2]:
            raise ValueError('Native exact case must already be marked published')
        if predecessor:
            row = db.execute('SELECT version_id,binding_json FROM historical_revisions WHERE submission_id=?',
                             (args.case,)).fetchone()
            if not row or row[0] != target['version_id']:
                raise ValueError('Native revision identity mismatch')
            binding = json.loads(row[1], object_pairs_hook=unique_object)
            expected = {'paper_id': paper_id, 'record_id': record_id, 'version': target['version'],
                        'version_id': row[0], 'sha256': target['canonical_sha256'],
                        'parent_sha256': predecessor['canonical_sha256'],
                        'supersedes_version_id': predecessor['version_id']}
            if any(binding.get(k) != v for k, v in expected.items()):
                raise ValueError('Native historical revision binding mismatch')
        active = db.execute("SELECT count(*) FROM historical_revision_grants h JOIN "
                            "agent_grants g ON h.grant_id=g.id WHERE g.state='approved' "
                            "AND g.uses=0 AND julianday(g.expires_at)>julianday('now')").fetchone()[0]
        if active:
            raise ValueError('Live unused historical grant; reconcile before changing catalogue')
        if data.get(paper_id) == target:
            print(json.dumps({'status': 'already_reconciled', 'mutated': False,
                              'active_unused_grants': active, 'unrelated_entries_preserved': len(data)-1,
                              'official_release_verified': True, 'AIRR_mirror_verified': True}))
            return
        result = {'status': 'verified_public_successor' if predecessor else 'verified_absent_public_predecessor', 'mutated': False,
                  'active_unused_grants': active, 'unrelated_entries_preserved': len(data) - int(paper_id in data),
                  'old_sha256': hashlib.sha256(raw).hexdigest(), 'entry': target,
                  'creates_permission_or_publication': False,
                  'public_witness': 'official_GitHub_release_exact_asset_' + str(args.asset_id),
                  'official_release_tag': tag, 'release_asset_name': asset_name,
                  'metadata_commit': args.metadata_commit,
                  'metadata_sha256': hashlib.sha256(metadata_raw).hexdigest(),
                  'AIRR_mirror_verified': True, 'AIRR_mirror_url': mirror}
        if not args.apply:
            print(json.dumps(result))
            return
        if path.read_bytes() != raw:
            raise ValueError('Concurrent catalogue change')
        if verify_live_service() != service_pid:
            raise ValueError('Service restarted during preparation; inspect before retry')
        backup = Path('/srv/airr-private/tep-catalogue-before' + backup_key + '-' + target['version'] + '-two-witnesses.json')
        with os.fdopen(os.open(backup, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), 'wb') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        previous = dict(data)
        data[paper_id] = target
        if any(data[k] != value for k, value in previous.items() if k != paper_id):
            raise ValueError('Unrelated entry changed')
        new = (json.dumps(data, sort_keys=True, indent=2) + '\n').encode()
        tmp = path.with_name('catalogue.' + backup_key + '-' + target['version'] + '-two-witnesses.tmp')
        mode = path.stat()
        with os.fdopen(os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), 'wb') as stream:
            stream.write(new)
            stream.flush()
            os.fchown(stream.fileno(), mode.st_uid, mode.st_gid)
            os.fchmod(stream.fileno(), stat.S_IMODE(mode.st_mode))
            os.fsync(stream.fileno())
        os.replace(tmp, path)
        if (path.read_bytes() != new or service_pid[2].read_bytes() != new
                or service_pid[3].read_bytes() != new):
            raise ValueError('Catalogue readback mismatch')
        db.commit()
        result.update(status='reconciled_verified_public_' + target['version'], mutated=True,
                      new_sha256=hashlib.sha256(new).hexdigest(), backup=str(backup))
        print(json.dumps(result))
    finally:
        db.rollback()
        db.close()


if __name__ == '__main__':
    main()
