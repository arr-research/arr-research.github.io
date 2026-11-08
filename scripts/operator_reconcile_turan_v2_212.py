# SPDX-License-Identifier: AGPL-3.0-or-later
"""Host-only successor reconciliation after actual native/public verification.

Default is read-only. Does not create scope, grants, cases, receipts, permissions
or a publication record. Requires the native case already marked published.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import stat
import urllib.request

PID = 'ARR-2026-72G1SSCNNG8YDVC2'
RECORD = 'arr:record:e2807396-56b0-479b-b60b-3229e1a6e6c8'
DIGEST = '9656985cce8bfb46e961acf9e4e6efbc8ee8114c5259ccf0d27e4f33ea1843f6'
RELEASE = 'https://github.com/arr-research/arr-research.github.io/releases/tag/' + PID + '-v2'
OLD = {'record_id': RECORD,
       'version_id': 'arr:version:85887c0e-1e00-489b-97f0-8b6e6a721191',
       'version': 'v1',
       'canonical_sha256': 'b6307a215b321c380f1f76b117e6cb6c660239c176b0b25c45fe2fe5a3c59d50',
       'authors': ['Lluis Eriksson']}
NEW = {'record_id': RECORD,
       'version_id': 'arr:version:bd6d0362-c5cc-4ef6-a35d-87ae6fd4aa51',
       'version': 'v2', 'canonical_sha256': DIGEST,
       'authors': ['Lluis Eriksson']}


def public(url, limit):
    req = urllib.request.Request(url, headers={'User-Agent': 'AIRR-exact-release-integrity'})
    with urllib.request.urlopen(req, timeout=30) as response:
        raw = response.read(limit + 1)
    if len(raw) > limit:
        raise ValueError('Oversized public artifact')
    return raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    if os.name != 'posix':
        raise ValueError('Existing AIRR Linux host only')
    base = ('https://raw.githubusercontent.com/arr-research/arr-research.github.io/'
            '0e6e9b5f0ff5de29140aee864070ad39d980c7d5/papers/2026/07/72/' + PID)
    meta = json.loads(public(base + '/versions/v2/metadata.json', 100000))
    if (meta['id'] != PID or meta['authors'] != [{'name': 'Lluis Eriksson',
                                                'affiliation': 'Independent researcher'}]
            or any(meta[k] != NEW[k] for k in ('record_id', 'version_id', 'version'))
            or meta['integrity']['canonical_sha256'] != DIGEST
            or meta['supersedes_version_id'] != OLD['version_id']):
        raise ValueError('Immutable published identity/author/predecessor mismatch')
    pdf = public('https://airr.science/papers/' + PID + '/versions/v2/' + PID + '-v2.pdf', 1000000)
    if len(pdf) != 303006 or hashlib.sha256(pdf).hexdigest() != DIGEST:
        raise ValueError('Exact public AIRR PDF mismatch')
    path = Path('/srv/airr-private/historical-revisions/catalogue.json').resolve()
    raw = path.read_bytes()
    data = json.loads(raw)
    if data.get(PID) not in (OLD, NEW):
        raise ValueError('Unexpected existing entry; do not overwrite')
    db = sqlite3.connect('/srv/airr-private/instance/intake.sqlite3', timeout=15)
    try:
        db.execute('BEGIN IMMEDIATE')
        case = db.execute('SELECT sha256,public_release_url,public_released_at '
                          'FROM submissions WHERE id=?', ('SUB-D0F755BA33E8A205',)).fetchone()
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
                  'creates_permission_or_publication': False}
        if not args.apply:
            print(json.dumps(result))
            return
        if path.read_bytes() != raw:
            raise ValueError('Concurrent catalogue change')
        backup = Path('/srv/airr-private/tep-catalogue-before212-turan-v2.json')
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
        tmp = path.with_name('catalogue.212-turan-v2.tmp')
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
        result.update(status='reconciled_verified_public_v2', mutated=True,
                      new_sha256=hashlib.sha256(new).hexdigest(), backup=str(backup))
        print(json.dumps(result))
    finally:
        db.rollback()
        db.close()


if __name__ == '__main__':
    main()
