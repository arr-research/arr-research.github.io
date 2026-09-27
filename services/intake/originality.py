"""Exact-version originality evidence; similarity is a review aid, never a verdict."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import urlsplit

from flask import abort, g, redirect, render_template, request, url_for

POLICY = 'AIRR-ORIGINALITY-1.0'
SCHEMA = '''
CREATE TABLE IF NOT EXISTS originality_scans (
 id INTEGER PRIMARY KEY, submission_id TEXT NOT NULL REFERENCES submissions(id),
 manuscript_sha256 TEXT NOT NULL, result_json TEXT NOT NULL,
 created_by INTEGER NOT NULL REFERENCES users(id), created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS originality_reviews (
 id INTEGER PRIMARY KEY, submission_id TEXT NOT NULL REFERENCES submissions(id),
 manuscript_sha256 TEXT NOT NULL, scan_id INTEGER NOT NULL REFERENCES originality_scans(id),
 outcome TEXT NOT NULL CHECK(outcome IN ('clear','concerns')),
 evidence_json TEXT NOT NULL, signed_by INTEGER NOT NULL REFERENCES users(id), signed_at TEXT NOT NULL
);
'''


def migrate(db):
    db.executescript(SCHEMA)
    columns = {r[1] for r in db.execute('PRAGMA table_info(submissions)')}
    for name, definition in [('originality_required', 'INTEGER NOT NULL DEFAULT 0'),
                             ('publication_mode', "TEXT NOT NULL DEFAULT 'standard'"),
                             ('source_disclosure', "TEXT NOT NULL DEFAULT ''")]:
        if name not in columns:
            db.execute(f'ALTER TABLE submissions ADD COLUMN {name} {definition}')
    db.commit()


def latest(db, row):
    return db.execute('SELECT * FROM originality_reviews WHERE submission_id=? AND manuscript_sha256=? ORDER BY id DESC LIMIT 1',
                      (row['id'], row['sha256'])).fetchone()


def ready(db, row):
    if not row['originality_required']:
        return True
    review = latest(db, row)
    scan = db.execute('SELECT id FROM originality_scans WHERE submission_id=? AND manuscript_sha256=? ORDER BY id DESC LIMIT 1',
                      (row['id'], row['sha256'])).fetchone()
    return bool(review and scan and review['outcome'] == 'clear' and review['scan_id'] == scan['id'])


def require_ready(db, row):
    if not ready(db, row):
        abort(409, 'Originality, attribution and rights review of this exact PDF must be completed before release or acceptance.')


def extract_text(pdf):
    """No network or shell; bounded extraction, fail closed on missing tools/OCR."""
    # Extracted private text belongs on the encrypted quarantine volume too.
    with tempfile.TemporaryDirectory(prefix='airr-text-', dir=Path(pdf).parent) as temporary:
        target = Path(temporary) / 'text.txt'
        try:
            result = subprocess.run(['pdftotext', '-f', '1', '-l', '201', '-enc', 'UTF-8', str(pdf), str(target)],
                                    capture_output=True, timeout=20, check=False)
            if result.returncode or not target.exists() or target.stat().st_size > 2_000_000:
                raise ValueError('Text extraction failed or exceeded the size limit; manual/OCR evidence is needed.')
            value = target.read_text(encoding='utf-8')
            if value.count('\f') > 200:
                raise ValueError('The 200-page checking limit was exceeded; no complete check is claimed.')
        except (OSError, subprocess.TimeoutExpired) as error:
            raise ValueError('PDF text extraction is unavailable; originality review remains pending.') from error
    if len(re.findall(r'\w+', value)) < 40:
        raise ValueError('Insufficient extractable text. Supply an accessible PDF or arrange an evidenced manual review.')
    return value


def shingles(text):
    words = re.findall(r'\w+', text.casefold())
    return {' '.join(words[i:i + 7]) for i in range(max(0, len(words) - 6))}


def compare_text(text, corpus):
    source = shingles(text)
    matches, indexed = [], []
    for path in sorted(Path(corpus).glob('**/paper.txt')):
        if path.is_symlink() or path.stat().st_size > 2_000_000:
            continue
        raw = path.read_bytes()
        indexed.append((str(path.relative_to(corpus)), hashlib.sha256(raw).hexdigest()))
        shared = source & shingles(raw.decode('utf-8', errors='replace'))
        if shared:
            matches.append({'record': str(path.parent.relative_to(corpus)).replace('\\', '/'),
                            'shared_seven_word_sequences': len(shared),
                            'candidate_sequence_overlap': round(len(shared) / max(1, len(source)), 4)})
    if not indexed:
        raise ValueError('The local public comparison corpus is missing; no clear result may be recorded.')
    return {'public_texts_checked': len(indexed),
            'corpus_sha256': hashlib.sha256(json.dumps(indexed).encode()).hexdigest(),
            'candidate_sequences': len(source),
            'matching_public_texts': len(matches), 'matches_truncated': len(matches) > 30,
            'matches': sorted(matches, key=lambda x: -x['shared_seven_word_sequences'])[:30],
            'scope': 'Extractable text versus AIRR public paper.txt files only. Formulas, images, translations and outside sources require editorial checks. Overlap is not a plagiarism verdict.'}


def public_summary(db, row):
    review = latest(db, row)
    if not review or not ready(db, row):
        return None
    return {'policy': POLICY, 'manuscript_sha256': row['sha256'], 'checked_at': review['signed_at'],
            'outcome': 'no_unresolved_concerns_in_checked_sources',
            'limitations': 'Documented checks of specified sources, not a guarantee of global originality.'}


def install(app, a):
    app.config.setdefault('ORIGINALITY_CORPUS', str(Path(__file__).resolve().parents[2] / 'papers'))

    def case(case_id):
        row = a.get_db().execute('SELECT * FROM submissions WHERE id=?', (case_id,)).fetchone()
        if not row:
            abort(404)
        if row['scan_status'] != 'clean' or row['status'] in {'removed', 'withdrawn', 'superseded', 'legal_hold'}:
            abort(409, 'Use a clean, current manuscript.')
        return row

    @app.context_processor
    def context():
        def state(row):
            db = a.get_db()
            scan = db.execute('SELECT * FROM originality_scans WHERE submission_id=? AND manuscript_sha256=? ORDER BY id DESC LIMIT 1',
                              (row['id'], row['sha256'])).fetchone()
            agent_request = db.execute('SELECT publication_requested,requested_license FROM independent_submissions WHERE submission_id=?', (row['id'],)).fetchone()
            return {'required': bool(row['originality_required']), 'ready': ready(db, row), 'agent_request': agent_request,
                    'scan': scan, 'review': latest(db, row)}
        return {'originality_state': state}

    @app.post('/admin/submission/<submission_id>/originality-scan')
    @a.editor_required
    def originality_scan(submission_id):
        a.require_csrf()
        a.enforce_rate('originality-scan', 5, 3600, submission_id)
        row = case(submission_id)
        pdf = Path(app.config['QUARANTINE']) / row['stored_name']
        if not pdf.is_file():
            abort(409, 'The private PDF is no longer retained; do not reuse earlier evidence for another artifact.')
        if hashlib.sha256(pdf.read_bytes()).hexdigest() != row['sha256']:
            abort(409, 'Stored manuscript integrity mismatch.')
        try:
            result = compare_text(extract_text(pdf), Path(app.config['ORIGINALITY_CORPUS']))
        except ValueError as error:
            abort(409, str(error))
        db = a.get_db()
        result['other_private_exact_duplicates'] = db.execute('SELECT COUNT(*) FROM submissions WHERE sha256=? AND id<>?',
                                                             (row['sha256'], row['id'])).fetchone()[0]
        result['policy'] = POLICY
        db.execute('INSERT INTO originality_scans(submission_id,manuscript_sha256,result_json,created_by,created_at) VALUES(?,?,?,?,?)',
                   (submission_id, row['sha256'], json.dumps(result), g.user['id'], a.iso()))
        db.commit()
        a.audit('originality_local_check', submission_id, sha256=row['sha256'])
        return redirect(url_for('submission_detail', submission_id=submission_id))

    @app.post('/admin/submission/<submission_id>/originality-review')
    @a.editor_required
    def originality_review(submission_id):
        a.require_csrf()
        row = case(submission_id)
        db = a.get_db()
        scan = db.execute('SELECT * FROM originality_scans WHERE submission_id=? AND manuscript_sha256=? ORDER BY id DESC LIMIT 1',
                          (submission_id, row['sha256'])).fetchone()
        if not scan or str(scan['id']) != request.form.get('scan_id') or request.form.get('sha256') != row['sha256']:
            abort(409, 'Review the latest local check of the exact PDF.')
        outcome = request.form.get('outcome')
        evidence = {key: request.form.get(key, '').strip() for key in
                    ('search_scope', 'sources_checked', 'match_adjudication', 'attribution_basis', 'rights_basis', 'privacy_check')}
        if outcome not in {'clear', 'concerns'} or any(not 40 <= len(value) <= 8000 for value in evidence.values()) or request.form.get('signed') != 'on':
            abort(400, 'Document the searches, public sources, matches, attribution, rights and PDF identity check, then sign the review.')
        # At least one source was actually identified and checked; do not require an external
        # manuscript upload or treat a numerical similarity score as automatic clearance.
        links = re.findall(r'https?://[^\s<>]+', evidence['sources_checked'])
        if not any(urlsplit(link).hostname for link in links):
            abort(400, 'Include the public source URLs checked and the result of each check.')
        db.execute('INSERT INTO originality_reviews(submission_id,manuscript_sha256,scan_id,outcome,evidence_json,signed_by,signed_at) VALUES(?,?,?,?,?,?,?)',
                   (submission_id, row['sha256'], scan['id'], outcome, json.dumps(evidence), g.user['id'], a.iso()))
        db.commit()
        a.audit('originality_review_signed', submission_id, outcome=outcome, sha256=row['sha256'])
        return redirect(url_for('submission_detail', submission_id=submission_id))
