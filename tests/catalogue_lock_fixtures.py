# SPDX-License-Identifier: AGPL-3.0-or-later
"""Deterministic two-connection interleaving, without timing-based sleeps."""
import hashlib
import json
import sqlite3
from unittest.mock import patch

from services.intake import historical_revisions


def contend_during_grant_snapshot(test, issue):
    original = historical_revisions.catalogue
    observed = []

    def snapshot(app):
        # Capture the old snapshot first: on the rejected code a writer can
        # commit here, before the issuer acquires its later SQLite lock.
        captured = original(app)
        other = sqlite3.connect(app.config['DATABASE'], timeout=0)
        try:
            try:
                other.execute('BEGIN IMMEDIATE')
            except sqlite3.OperationalError as error:
                if 'locked' not in str(error).lower():
                    raise
                observed.append('blocked')
            else:
                active = other.execute("SELECT count(*) FROM historical_revision_grants h "
                                       "JOIN agent_grants g ON h.grant_id=g.id "
                                       "WHERE g.state='approved' AND g.uses=0 "
                                       "AND julianday(g.expires_at)>julianday('now')").fetchone()[0]
                if active:
                    observed.append('active_grant')
                else:
                    entries = json.loads(test.catalog.read_bytes())
                    entries['unrelated-concurrent-entry'] = {'witness': 'preserve me'}
                    test.catalog.write_text(json.dumps(entries))
                    other.commit()
                    observed.append('changed_before_grant')
        finally:
            other.rollback()
            other.close()
        return captured

    with patch.object(historical_revisions, 'catalogue', side_effect=snapshot):
        result = issue()
    test.assertEqual(observed, ['blocked'], 'Catalogue read crossed its grant writer lock')
    with test.app.app_context():
        from services.intake.app import get_db
        rows = get_db().execute('SELECT catalogue_sha256 FROM historical_revision_grants').fetchall()
        test.assertEqual(len(rows), 1)
        test.assertEqual(rows[0][0], hashlib.sha256(test.catalog.read_bytes()).hexdigest(),
                         'Fresh grant was bound to a stale catalogue')
    return result
