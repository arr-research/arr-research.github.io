# SPDX-License-Identifier: AGPL-3.0-or-later
"""Host-only authoritative official-release reconciliation; AIRR mirror remains pending.

Default is read-only. Does not create scope, grants, cases, receipts, permissions
or a publication record. Requires the native case already marked published.
Uses WORKFLOW.md official GitHub publication and ARCHITECTURE.md authoritative
release store. This is not a PASS for the separately retained AIRR mirror gate.
Original operator_reconcile_matrix_v14_226C.py is preserved unchanged.
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
DIGEST = '28cb2a7502e05cd8588aa6294f07a7eca5e0e452cce1bf5e4f09e9ec3c89e1a6'
RELEASE = 'https://github.com/arr-research/arr-research.github.io/releases/tag/' + PID + '-v14'
OLD = {'record_id': RECORD,
       'version_id': 'arr:version:be398c87-1bbf-4831-b06e-e4b1f2fa1e53',
       'version': 'v13',
       'canonical_sha256': 'c99f59936f7ac58dc4af25443d3a3a17932d6b1651542285feb65d6781f3814e',
       'authors': ['Lluis Eriksson']}
NEW = {'record_id': RECORD,
       'version_id': 'arr:version:ccd9fd43-ebe6-45a4-a6e0-21c5a0b572fb',
       'version': 'v14', 'canonical_sha256': DIGEST,
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
    args = parser.parse_args()
    if not re.fullmatch(r'SUB-[A-F0-9]{16}', args.case):
        raise ValueError('Exact actual native case ID required')
    if not re.fullmatch(r'[a-f0-9]{40}', args.metadata_commit):
        raise ValueError('Full immutable publication commit required')
    if os.name != 'posix':
        raise ValueError('Existing AIRR Linux host only')
    base = ('https://raw.githubusercontent.com/arr-research/arr-research.github.io/'
            + args.metadata_commit + '/papers/2026/08/7E/' + PID)
    meta = json.loads(public(base + '/versions/v14/metadata.json', 100000))
    if (meta['id'] != PID or meta['authors'] != [{'name': 'Lluis Eriksson',
                                                'affiliation': 'Independent researcher'}]
            or any(meta[k] != NEW[k] for k in ('record_id', 'version_id', 'version'))
            or meta['integrity']['canonical_sha256'] != DIGEST
            or meta['supersedes_version_id'] != OLD['version_id']):
        raise ValueError('Immutable published identity/author/predecessor mismatch')
    pdf = public('https://api.github.com/repos/arr-research/arr-research.github.io/'
                 'releases/assets/732763589', 1000000, 'application/octet-stream')
    if len(pdf) != 419361 or hashlib.sha256(pdf).hexdigest() != DIGEST:
        raise ValueError('Exact authoritative official-release PDF mismatch')
    path = Path('/srv/airr-private/historical-revisions/catalogue.json').resolve()
    db = sqlite3.connect('/srv/airr-private/instance/intake.sqlite3', timeout=15)
    try:
        db.execute('BEGIN IMMEDIATE')
        # Mandatory shared writer protocol; see docs/CATALOGUE-WRITER-PROTOCOL.md.
        # No grant issuer or supported catalogue writer may cross this lock.
        raw = path.read_bytes()
        data = json.loads(raw)
        if data.get(PID) not in (OLD, NEW):
            raise ValueError('Unexpected existing entry; do not overwrite')
        case = db.execute('SELECT sha256,public_release_url,public_released_at '
                          'FROM submissions WHERE id=?', (args.case,)).fetchone()
        if not case or case[0] != DIGEST or case[1] != RELEASE or not case[2]:
            raise ValueError('Native exact case must already be marked published')
        if data[PID] == NEW:
            print(json.dumps({'status': 'already_reconciled', 'mutated': False}))
            return
        active = db.execute("SELECT count(*) FROM historical_revision_grants h JOIN "
                            "agent_grants g ON h.grant_id=g.id WHERE g.state='approved' "
                            "AND g.uses=0 AND julianday(g.expires_at)>julianday('now')").fetchone()[0]
        if active:
            raise ValueError('Live unused historical grant; reconcile before changing catalogue')
        result = {'status': 'verified_public_successor', 'mutated': False,
                  'active_unused_grants': active, 'unrelated_entries_preserved': len(data)-1,
                  'old_sha256': hashlib.sha256(raw).hexdigest(), 'entry': NEW,
                  'creates_permission_or_publication': False,
                  'public_witness': 'official_GitHub_release_exact_asset_732763589',
                  'AIRR_mirror_verified': False, 'original_mirror_gate': 'pending_unchanged'}
        if not args.apply:
            print(json.dumps(result))
            return
        if path.read_bytes() != raw:
            raise ValueError('Concurrent catalogue change')
        backup = Path('/srv/airr-private/tep-catalogue-before226C-official-release-v14.json')
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
        tmp = path.with_name('catalogue.226C-official-release-v14.tmp')
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
        result.update(status='reconciled_verified_public_v14', mutated=True,
                      new_sha256=hashlib.sha256(new).hexdigest(), backup=str(backup))
        print(json.dumps(result))
    finally:
        db.rollback()
        db.close()


if __name__ == '__main__':
    main()
