# SPDX-License-Identifier: AGPL-3.0-or-later
"""Host-only exact v15 reconciliation; official release AND AIRR mirror required.

Default is read-only. Does not create scope, grants, cases, receipts, permissions
or a publication record. Requires the native case already marked published.
Requires immutable metadata, exact public release-tag asset membership and bytes,
plus exact AIRR mirror bytes. Existing v14 helpers remain unchanged. No authority
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
import urllib.request

PID = 'ARR-2026-7EPM3V3DP796BBRR'
RECORD = 'arr:record:eeb507b1-b6c7-4996-bc62-a4e7c416be00'
DIGEST = '5595e89c1bcbec1d9b1ae35053a76e6a962f67b45d5d1ac483e5b7a60c9b9be0'
PDF_BYTES = 505936
CASE = 'SUB-370C455C4D32B2FB'
TAG = PID + '-v15'
ASSET_NAME = TAG + '.pdf'
RELEASE = 'https://github.com/arr-research/arr-research.github.io/releases/tag/' + TAG
RELEASE_API = 'https://api.github.com/repos/arr-research/arr-research.github.io/releases/tags/' + TAG
MIRROR_PDF = 'https://airr.science/papers/' + PID + '/versions/v15/' + ASSET_NAME
OLD = {'record_id': RECORD,
       'version_id': 'arr:version:ccd9fd43-ebe6-45a4-a6e0-21c5a0b572fb',
       'version': 'v14',
       'canonical_sha256': '28cb2a7502e05cd8588aa6294f07a7eca5e0e452cce1bf5e4f09e9ec3c89e1a6',
       'authors': ['Lluis Eriksson']}
NEW = {'record_id': RECORD,
       'version_id': 'arr:version:ec7f4fe6-6e9a-4618-bfbe-dcda3daa8fbe',
       'version': 'v15', 'canonical_sha256': DIGEST,
       'authors': ['Lluis Eriksson']}


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
                        help='Actual PDF asset ID belonging to the published v15 tag')
    args = parser.parse_args()
    if args.case != CASE:
        raise ValueError('Exact actual native case ID required')
    if not re.fullmatch(r'[a-f0-9]{40}', args.metadata_commit):
        raise ValueError('Full immutable publication commit required')
    if args.asset_id <= 0:
        raise ValueError('Actual positive release asset ID required')
    if os.name != 'posix':
        raise ValueError('Existing AIRR Linux host only')
    base = ('https://raw.githubusercontent.com/arr-research/arr-research.github.io/'
            + args.metadata_commit + '/papers/2026/08/7E/' + PID)
    metadata_raw = public(base + '/versions/v15/metadata.json', 100000)
    meta = json.loads(metadata_raw)
    if (meta['id'] != PID or meta['authors'] != [{'name': 'Lluis Eriksson',
                                                'affiliation': 'Independent researcher'}]
            or any(meta[k] != NEW[k] for k in ('record_id', 'version_id', 'version'))
            or meta.get('status') != 'working_paper'
            or meta['integrity']['canonical_sha256'] != DIGEST
            or meta['supersedes_version_id'] != OLD['version_id']):
        raise ValueError('Immutable published identity/author/predecessor mismatch')
    release = json.loads(public(RELEASE_API, 1000000, 'application/vnd.github+json'))
    if (release.get('tag_name') != TAG or release.get('html_url') != RELEASE
            or release.get('draft') is not False or not release.get('published_at')
            or not isinstance(release.get('assets'), list)):
        raise ValueError('Actual public v15 release identity required')
    matching = [asset for asset in release['assets']
                if asset.get('id') == args.asset_id or asset.get('name') == ASSET_NAME]
    if (len(matching) != 1 or matching[0].get('id') != args.asset_id
            or matching[0].get('name') != ASSET_NAME
            or matching[0].get('size') != PDF_BYTES
            or matching[0].get('state') != 'uploaded'
            or matching[0].get('browser_download_url') !=
            'https://github.com/arr-research/arr-research.github.io/releases/download/' + TAG + '/' + ASSET_NAME):
        raise ValueError('Exact PDF asset ID/name/size must belong to actual v15 release')
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
        if len(data) != 94:
            raise ValueError('Exactly93 unrelated catalogue entries must be preserved')
        if data.get(PID) not in (OLD, NEW):
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
        if data[PID] == NEW:
            print(json.dumps({'status': 'already_reconciled', 'mutated': False,
                              'active_unused_grants': active, 'unrelated_entries_preserved': 93,
                              'official_release_verified': True, 'AIRR_mirror_verified': True}))
            return
        result = {'status': 'verified_public_successor', 'mutated': False,
                  'active_unused_grants': active, 'unrelated_entries_preserved': len(data)-1,
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
        backup = Path('/srv/airr-private/tep-catalogue-before232B-v15-two-witnesses.json')
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
        tmp = path.with_name('catalogue.232B-v15-two-witnesses.tmp')
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
        result.update(status='reconciled_verified_public_v15', mutated=True,
                      new_sha256=hashlib.sha256(new).hexdigest(), backup=str(backup))
        print(json.dumps(result))
    finally:
        db.rollback()
        db.close()


if __name__ == '__main__':
    main()
