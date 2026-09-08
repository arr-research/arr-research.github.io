"""One private PDF receiving path for browser and delegated-agent submissions."""
import hashlib
import json
import os
from pathlib import Path
import secrets
import shutil

from flask import abort


def receive(app, a, upload, data, reserve=None):
    if shutil.disk_usage(app.config['QUARANTINE']).free < a.MAX_PDF_BYTES * 4:
        abort(503, 'Private storage is temporarily full; no manuscript was registered.')
    original = Path((upload.filename or 'manuscript.pdf').replace('\\', '/')).name[:200]
    case_id = 'SUB-' + secrets.token_hex(8).upper()
    stored = secrets.token_hex(24) + '.pdf'
    target = Path(app.config['QUARANTINE']) / stored
    fingerprint = hashlib.sha256()
    size = 0
    committed = False
    db = a.get_db()
    try:
        with os.fdopen(os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), 'wb') as handle:
            first = upload.stream.read(5)
            if first != b'%PDF-':
                raise ValueError('Only a PDF beginning with the PDF signature is accepted.')
            handle.write(first)
            fingerprint.update(first)
            size = len(first)
            while chunk := upload.stream.read(1024 * 1024):
                size += len(chunk)
                if size > a.MAX_PDF_BYTES:
                    abort(413, 'The manuscript exceeds 25 MiB.')
                handle.write(chunk)
                fingerprint.update(chunk)
        checksum = fingerprint.hexdigest()
        if data.get('expected_sha256') and data['expected_sha256'] != checksum:
            raise ValueError('The PDF does not match the declared SHA-256.')
        submitter = db.execute("SELECT * FROM users WHERE id=? AND active=1 AND role='depositor'", (data.get('user_id'),)).fetchone()
        if not submitter:
            abort(403, 'A private workspace must own this submission.')
        conflict = int(data['email'] == app.config['OPERATOR_EMAIL'] or bool(data.get('operator_conflict')))
        db.execute('BEGIN IMMEDIATE')
        db.execute('''INSERT INTO submissions(
            id,user_id,title,authors,abstract,original_filename,stored_name,sha256,size_bytes,
            scan_status,scan_detail,status,operator_conflict,ai_review_opt_in,terms_version,
            privacy_version,created_at,updated_at,classification_json,submission_channel,agent_provenance_json)
            VALUES(?,?,?,?,?,?,?,?,?,'pending','Awaiting approved scanner.','quarantined',?,1,?,?,?,?,?,?,?)''',
            (case_id,submitter['id'],data['title'][:500],data['authors'][:1000],data['abstract'][:5000],
             original,stored,checksum,size,conflict,a.TERMS_VERSION,a.PRIVACY_VERSION,a.iso(),a.iso(),
             json.dumps(data['classification'],ensure_ascii=False),data.get('channel','human'),
             json.dumps(data.get('agent_provenance',{}),ensure_ascii=False)))
        if reserve:
            reserve(db, case_id)
        db.commit()
        committed = True
    finally:
        if not committed:
            db.rollback()
            target.unlink(missing_ok=True)
    a.audit('submission_received', case_id, sha256=checksum, size_bytes=size, channel=data.get('channel','human'))
    row = db.execute('SELECT * FROM submissions WHERE id=?', (case_id,)).fetchone()
    scan_status, _ = a.scan_submission(row)
    a.notify_operator(case_id, data['title'], data['email'], scan_status)
    app.extensions['editorial']['received'](case_id)
    return db.execute('SELECT * FROM submissions WHERE id=?', (case_id,)).fetchone()
