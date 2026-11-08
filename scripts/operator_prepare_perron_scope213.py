# SPDX-License-Identifier: AGPL-3.0-or-later
"""Prepare private machine mapping of the actual retained programme instruction.

Read-only SQLite access; never issues scope/grants/cases/permissions. The native
extend-programme-papers command must separately validate and record this evidence.
No owner response, timestamp, licence or original instruction is rewritten.
"""
import hashlib
import json
import os
from pathlib import Path
import sqlite3

PROGRAMME = 'PRG-376B2C03C74C234C0C3F2A42'
INITIAL = '8458953bee142a8d99a6839fef11d1fb004e79681a7ef7df72063ef4479a2d07'
PAPER = 'ARR-2026-1A608PTGTC9XX9JZ'
SUFFIX = (' Machine mapping213 of the actual originally authorized sole-author '
          'programme to the existing Perron record omitted from its machine list; '
          'no new human reply, date, terms, licence, quota, grant or acceptance.')


def derive(initial):
    if (initial.get('programme') != 'THE ERIKSSON PROGRAMME'
            or initial.get('author') != 'Lluis Eriksson'
            or initial.get('rights_confirmed') is not True
            or initial.get('operator_authorship_confirmed') is not True):
        raise ValueError('Unexpected original programme authority')
    evidence = {key: initial[key] for key in
                ('author_instruction', 'recorded_at', 'rights_confirmed',
                 'operator_authorship_confirmed')}
    evidence.update(programme_id=PROGRAMME, initial_instruction_sha256=INITIAL,
                    paper_ids=[PAPER],
                    source_reference=initial['source_reference'] + SUFFIX)
    return (json.dumps(evidence, ensure_ascii=False, indent=2) + '\n').encode()


def main():
    if os.name != 'posix':
        raise ValueError('Existing authenticated AIRR Linux host only')
    uri = 'file:/srv/airr-private/instance/intake.sqlite3?mode=ro'
    with sqlite3.connect(uri, uri=True) as db:
        row = db.execute('SELECT evidence_json,evidence_sha256 FROM '
                         'programme_delegations WHERE id=?', (PROGRAMME,)).fetchone()
    if row is None or row[1] != INITIAL:
        raise ValueError('Original authority hash mismatch')
    catalogue = json.loads(Path('/srv/airr-private/historical-revisions/catalogue.json').read_bytes())
    expected = {'record_id': 'arr:record:2a30116d-434c-4f7a-997c-48ad16211b9d',
                'version_id': 'arr:version:b818e296-b5ce-49d4-9d9b-a11b873bab4f',
                'version': 'v1',
                'canonical_sha256': 'e8063013965ea1699718d08f2bce1646e73f0dd2b970a518bb9e6339c68d78a0',
                'authors': ['Lluis Eriksson']}
    if catalogue.get(PAPER) != expected:
        raise ValueError('Verify the actual existing sole-author Perron v1 catalogue binding')
    raw = derive(json.loads(row[0]))
    path = Path('/srv/airr-private/tep-scope213-derived.json')
    if path.exists():
        if path.read_bytes() != raw:
            raise ValueError('Preserve differing existing evidence; do not overwrite')
    else:
        with path.open('xb') as stream:
            os.chmod(path, 0o600)
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
    print(json.dumps({'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(),
                      'original_instruction_sha256': INITIAL,
                      'original_instruction_unchanged': True,
                      'new_human_response': False, 'scope_recorded': False,
                      'grant_created': False, 'published': False}))


if __name__ == '__main__':
    main()
