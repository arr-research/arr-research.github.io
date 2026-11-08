# SPDX-License-Identifier: AGPL-3.0-or-later
"""Reconcile one absent, already public predecessor. Default read-only.

Creates no authority, grant, receipt, licence, acceptance or publication record.
The separate native programme extension still enforces real owner authority.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import stat
import urllib.request

PID = 'ARR-2026-5HRC3PS9HZ9WDAA5'
PIN = '2061bfa2f33704b707d58289af4a449f43aa25c5'
ENTRY = {'record_id': 'arr:record:b1c3076c-a63f-4f1a-a517-f539fae928fb',
         'version_id': 'arr:version:913ff5f2-f32f-416e-8aeb-33fe7ab2c8d9',
         'version': 'v1',
         'canonical_sha256': 'dc3b243efcb6f161516b48a7f17bd0e79092b59d17476f3cf8f3f40a7bd9ba4b',
         'authors': ['Lluis Eriksson']}


def fetch(url, limit):
    req = urllib.request.Request(url, headers={'User-Agent': 'AIRR-public-predecessor-integrity'})
    with urllib.request.urlopen(req, timeout=45) as r:
        data = r.read(limit+1)
    if len(data) > limit:
        raise ValueError('Oversized artifact')
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--apply', action='store_true')
    args = p.parse_args()
    if os.name != 'posix':
        raise ValueError('Existing authenticated AIRR Linux host only')
    root = 'https://raw.githubusercontent.com/arr-research/arr-research.github.io/'
    meta = json.loads(fetch(root+PIN+'/papers/2026/07/5H/'+PID+'/metadata.json', 100000))
    if (meta['id'] != PID or meta['authors'] != [{'name': 'Lluis Eriksson',
                                                'affiliation': 'Independent researcher'}]
            or any(meta[k] != ENTRY[k] for k in ('record_id', 'version_id', 'version'))
            or meta['integrity']['canonical_sha256'] != ENTRY['canonical_sha256']):
        raise ValueError('Immutable public predecessor binding mismatch')
    url = 'https://airr.science/papers/'+PID+'/versions/v1/'+PID+'-v1.pdf'
    raw_pdf = fetch(url, 1000000)
    if len(raw_pdf) != 284127 or hashlib.sha256(raw_pdf).hexdigest() != ENTRY['canonical_sha256']:
        raise ValueError('Exact public predecessor PDF mismatch')
    path = Path('/srv/airr-private/historical-revisions/catalogue.json').resolve()
    raw = path.read_bytes()
    data = json.loads(raw)
    if PID in data:
        if data[PID] != ENTRY:
            raise ValueError('Preserve unexpected existing entry')
        print(json.dumps({'status': 'already_reconciled', 'mutated': False}))
        return
    db = sqlite3.connect('/srv/airr-private/instance/intake.sqlite3', timeout=15)
    try:
        db.execute('BEGIN IMMEDIATE')
        active = db.execute("SELECT count(*) FROM historical_revision_grants h JOIN "
                            "agent_grants g ON h.grant_id=g.id WHERE g.state='approved' "
                            "AND g.uses=0 AND julianday(g.expires_at)>julianday('now')").fetchone()[0]
        if active:
            raise ValueError('Live unused historical grant; do not mutate catalogue')
        result = {'status': 'verified_absent_public_predecessor', 'mutated': False,
                  'entry': ENTRY, 'public_pdf_bytes': len(raw_pdf),
                  'active_unused_grants': active, 'unrelated_entries_preserved': len(data),
                  'old_sha256': hashlib.sha256(raw).hexdigest(),
                  'creates_scope_grant_permission_or_publication': False}
        if not args.apply:
            print(json.dumps(result))
            return
        if path.read_bytes() != raw:
            raise ValueError('Concurrent catalogue change')
        backup = Path('/srv/airr-private/tep-catalogue-before215-parity-v1.json')
        with backup.open('xb') as f:
            os.chmod(backup, 0o600)
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
        old = dict(data)
        data[PID] = ENTRY
        if any(data[k] != value for k, value in old.items()):
            raise ValueError('Unrelated catalogue entry changed')
        new = (json.dumps(data, sort_keys=True, indent=2)+'\n').encode()
        tmp = path.with_name('catalogue.215-parity-v1.tmp')
        mode = path.stat()
        with tmp.open('xb') as f:
            f.write(new)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(tmp, stat.S_IMODE(mode.st_mode))
        os.chown(tmp, mode.st_uid, mode.st_gid)
        os.replace(tmp, path)
        if path.read_bytes() != new:
            raise ValueError('Catalogue readback mismatch')
        db.commit()
        result.update(status='reconciled_verified_public_predecessor', mutated=True,
                      backup=str(backup), new_sha256=hashlib.sha256(new).hexdigest())
        print(json.dumps(result))
    finally:
        db.rollback()
        db.close()


if __name__ == '__main__':
    main()
