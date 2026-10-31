#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""AIRR agent deposits without a browser file picker. Python 3.10+, no packages.

Permission is approved in the author's workspace. This client never approves
terms, widens a grant, uses editor access, or publishes a manuscript.
"""
import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

ORIGIN = 'https://submit.airr.science'
MAX_PDF = 25 * 1024 * 1024
FIELDS = {'title', 'authors', 'abstract', 'primary_subject', 'secondary_subjects',
          'specific_topic', 'sha256', 'ai_disclosure', 'operator_conflict', 'rights_confirmed'}


class ClientError(Exception):
    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def call(method, path, token=None, data=None, headers=None):
    if not re.fullmatch(r'/api/v1/[A-Za-z0-9/_-]+', path):
        raise ClientError('Invalid API path.')
    request_headers = {'Accept': 'application/json', **(headers or {})}
    if token:
        request_headers['Authorization'] = 'Bearer ' + token
    if isinstance(data, dict):
        data = json.dumps(data).encode('utf-8')
        request_headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(ORIGIN + path, data=data, headers=request_headers, method=method)
    # Never send a bearer token to a redirect, proxy supplied by the environment,
    # another origin, or an endpoint with certificate verification disabled.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(req, timeout=120) as response:
            raw = response.read(1024 * 1024 + 1)
            if len(raw) > 1024 * 1024:
                raise ClientError('Unexpected oversized response. Keep the same job to reconcile.')
            return json.loads(raw)
    except urllib.error.HTTPError as error:
        retry = error.headers.get('Retry-After', '')
        guidance = {
            401: 'Credential not recognized. Run authorize --replace-unusable; owner approval is still required.',
            403: 'Permission is inactive or its terms changed. Inspect status before replacing it.',
            409: 'Conflict: keep the same job and inspect its metadata or receipt; do not create another case.',
            413: 'PDF/request exceeds the 25 MiB PDF limit.',
            429: 'Rate limited. Wait for the server limit; do not change accounts or keys.',
            503: 'Intake is unavailable. Keep this job and retry later.',
        }.get(error.code, 'Request rejected. Check the documented metadata and exact PDF.')
        if retry:
            guidance += ' Retry-After: ' + retry[:100]
        raise ClientError(f'AIRR HTTP {error.code}. {guidance}', error.code) from None
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        raise ClientError('Response uncertain. Preserve this job and its idempotency key; do not start a new deposit.') from None


def atomic_json(path, value, private=True):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(value, ensure_ascii=False, indent=2).encode('utf-8') + b'\n'
    atomic_bytes(path, raw, private)


def atomic_bytes(path, raw, private=True):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.' + secrets.token_hex(8) + '.tmp')
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600 if private else 0o644)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def dpapi(raw, decrypt=False):
    from ctypes import wintypes

    class Blob(ctypes.Structure):
        _fields_ = [('size', wintypes.DWORD), ('data', ctypes.POINTER(ctypes.c_ubyte))]

    buffer = ctypes.create_string_buffer(raw)
    source = Blob(len(raw), ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ubyte)))
    dest = Blob()
    crypt = ctypes.WinDLL('crypt32', use_last_error=True)
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    fn = crypt.CryptUnprotectData if decrypt else crypt.CryptProtectData
    fn.argtypes = [ctypes.POINTER(Blob), ctypes.c_void_p, ctypes.c_void_p,
                   ctypes.c_void_p, ctypes.c_void_p, wintypes.DWORD, ctypes.POINTER(Blob)]
    fn.restype = wintypes.BOOL
    kernel.LocalFree.argtypes = [ctypes.c_void_p]
    if not fn(ctypes.byref(source), None, None, None, None, 1, ctypes.byref(dest)):
        raise ClientError('Windows credential protection failed; no token was printed.')
    try:
        return ctypes.string_at(dest.data, dest.size)
    finally:
        kernel.LocalFree(dest.data)


def credential_path():
    if os.name == 'nt':
        return Path(os.environ['LOCALAPPDATA']) / 'AIRR/delegated-access/airr.dpapi'
    return Path.home() / '.local/state/airr/credential.json'


def load_credential(path):
    path = Path(path)
    if os.name != 'nt' and path.stat().st_mode & 0o077:
        raise ClientError('Credential permissions must be owner-only (chmod 600).')
    raw = path.read_bytes()
    value = json.loads(dpapi(raw, True) if os.name == 'nt' else raw)
    if not re.fullmatch(r'[A-Za-z0-9_-]{43}', value.get('agent_token', '')):
        raise ClientError('Invalid local credential. Preserve it and inspect before replacing.')
    return value


def save_credential(path, value):
    raw = json.dumps(value).encode()
    atomic_bytes(path, dpapi(raw) if os.name == 'nt' else raw)


def authorize(path, replace=False, name='AIRR research assistant', version='user-declared agent',
              purpose='Deposit exact manuscripts authorized by the responsible author and recover their receipts.'):
    path = Path(path)
    if path.exists():
        previous = load_credential(path)
        try:
            state = call('GET', '/api/v1/agent-authorization', previous['agent_token'])
        except ClientError as error:
            if error.status != 401 or not replace:
                raise
            state = {'state': 'unrecognized'}
        if state['state'] in ('pending', 'approved') and state.get('uploads_remaining', 1) > 0:
            return {'request_id': previous['request_id'], 'state': state['state'],
                    'authorization_url': previous['authorization_url'], 'reused': True}
        if not replace:
            raise ClientError('Inactive credential preserved. Run authorize --replace-unusable to request owner approval again.')
        # Retain the old protected credential and its request ID. Never revoke it,
        # delete receipts, or infer approval of the replacement.
        backup = path.with_name(path.name + '.previous-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S') + '-' + secrets.token_hex(4))
        atomic_bytes(backup, path.read_bytes())
    value = call('POST', '/api/v1/agent-requests', data={
        'agent_name': name, 'agent_version': version, 'purpose': purpose})
    url = value.get('authorization_url', '')
    if (not re.fullmatch(re.escape(ORIGIN) + r'/agents/authorize/[A-Za-z0-9_-]{43}', url)
            or not re.fullmatch(r'[A-Za-z0-9_-]{43}', value.get('agent_token', ''))
            or not re.fullmatch(r'AGT-[A-F0-9]{24}', value.get('request_id', ''))):
        raise ClientError('Unexpected authorization response. No credential replaced or token printed.')
    save_credential(path, value)
    return {k: value[k] for k in ('request_id', 'state', 'authorization_url', 'expires_at')}


def exact_pdf(path):
    with Path(path).open('rb') as stream:
        raw = stream.read(MAX_PDF + 1)
    if not raw.startswith(b'%PDF-') or len(raw) > MAX_PDF:
        raise ClientError('Choose an actual PDF no larger than 25 MiB.')
    return raw, hashlib.sha256(raw).hexdigest()


def prepare(pdf, metadata_path, job_path):
    job_path = Path(job_path)
    if job_path.exists():
        raise ClientError('Job already exists. Reuse it for retries; do not replace its idempotency key.')
    raw, digest = exact_pdf(pdf)
    metadata = json.loads(Path(metadata_path).read_text(encoding='utf-8-sig'))
    if not isinstance(metadata, dict) or set(metadata) not in (FIELDS, FIELDS - {'sha256'}):
        raise ClientError('Metadata fields must match agent-submissions.md; sha256 may be omitted during preparation.')
    if metadata.get('sha256', digest) != digest:
        raise ClientError('Metadata SHA-256 differs from the actual PDF.')
    metadata['sha256'] = digest
    if metadata['rights_confirmed'] is not True or type(metadata['operator_conflict']) is not bool:
        raise ClientError('Supply true authority for this exact manuscript and an explicit conflict declaration.')
    for field, low, high in [('title', 1, 500), ('authors', 0, 1000), ('abstract', 80, 5000), ('ai_disclosure', 20, 2000)]:
        val = metadata[field]
        if not isinstance(val, str) or not low <= len(val.strip()) <= high or '\x00' in val or '\r' in val:
            raise ClientError(f'{field} must have {low}–{high} characters, without NUL or CR.')
    if (not isinstance(metadata['primary_subject'], str) or not metadata['primary_subject']
            or not isinstance(metadata['specific_topic'], str)
            or not isinstance(metadata['secondary_subjects'], list)
            or len(metadata['secondary_subjects']) > 2
            or any(not isinstance(x, str) for x in metadata['secondary_subjects'])):
        raise ClientError('Use subject IDs from the live subject catalogue and at most two secondary subjects.')
    job = {'pdf': str(Path(pdf).resolve()), 'metadata': metadata,
           'idempotency_key': 'airr-' + secrets.token_hex(24)}
    atomic_json(job_path, job)
    return {'job': str(job_path.resolve()), 'sha256': digest, 'size_bytes': len(raw),
            'idempotency_key': job['idempotency_key'], 'sent': False}


def submit(job_path, credential):
    job_path = Path(job_path)
    job = json.loads(job_path.read_text(encoding='utf-8-sig'))
    raw, digest = exact_pdf(job['pdf'])
    if digest != job['metadata']['sha256'] or not re.fullmatch(r'[A-Za-z0-9._:-]{8,80}', job['idempotency_key']):
        raise ClientError('PDF changed or job key is invalid. Do not send altered bytes under this job.')
    receipt_path = job_path.with_name(job_path.name + '.receipt.json')
    if receipt_path.exists():
        result = json.loads(receipt_path.read_text(encoding='utf-8'))
        if result.get('sha256') != digest or result.get('size_bytes') != len(raw):
            raise ClientError('Saved receipt does not match this exact PDF.')
        return result
    permission = load_credential(credential)
    if job.get('grant_id') and job['grant_id'] != permission['request_id']:
        raise ClientError('This job was attempted under a different grant. Reconcile the old case in the owner workspace before any new deposit.')
    token = permission['agent_token']
    state = call('GET', '/api/v1/agent-authorization', token)
    if state['state'] != 'approved' or not state.get('intake_open'):
        raise ClientError('An active owner-approved permission and open intake are required. No PDF sent.')
    job['grant_id'] = permission['request_id']
    atomic_json(job_path, job)
    boundary = 'airr-' + secrets.token_hex(24)
    body = (f'--{boundary}\r\nContent-Disposition: form-data; name="metadata"\r\nContent-Type: application/json\r\n\r\n'.encode()
            + json.dumps(job['metadata'], ensure_ascii=False).encode('utf-8')
            + f'\r\n--{boundary}\r\nContent-Disposition: form-data; name="manuscript"; filename="manuscript.pdf"\r\nContent-Type: application/pdf\r\n\r\n'.encode()
            + raw + f'\r\n--{boundary}--\r\n'.encode())
    result = call('POST', '/api/v1/submissions', token, body, {
        'Content-Type': 'multipart/form-data; boundary=' + boundary,
        'Idempotency-Key': job['idempotency_key']})
    if (result.get('sha256') != digest or result.get('size_bytes') != len(raw)
            or not re.fullmatch(r'SUB-[A-F0-9]{16}', result.get('registration_number', ''))):
        raise ClientError('Response does not match the exact PDF. Preserve this job and reconcile before proceeding.')
    atomic_json(receipt_path, result)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--credential', type=Path, default=credential_path(), help='Protected local credential; never a token on the command line')
    sub = parser.add_subparsers(dest='command', required=True)
    auth = sub.add_parser('authorize', help='Request/reuse permission; print the owner approval URL, never the token')
    auth.add_argument('--replace-unusable', action='store_true')
    auth.add_argument('--agent-name', default='AIRR research assistant')
    auth.add_argument('--agent-version', required=True, help='Actual declared client/model; do not invent verified provenance')
    sub.add_parser('status', help='Check at most once per minute')
    prep = sub.add_parser('prepare', help='Freeze exact PDF, metadata and retry key locally; sends nothing')
    prep.add_argument('--pdf', required=True, type=Path)
    prep.add_argument('--metadata', required=True, type=Path)
    prep.add_argument('--job', required=True, type=Path)
    send = sub.add_parser('submit', help='Upload once or recover the same receipt; no publication')
    send.add_argument('--job', required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == 'prepare':
            result = prepare(args.pdf, args.metadata, args.job)
        elif args.command == 'authorize':
            result = authorize(args.credential, args.replace_unusable, args.agent_name, args.agent_version)
        elif args.command == 'status':
            result = call('GET', '/api/v1/agent-authorization', load_credential(args.credential)['agent_token'])
        else:
            result = submit(args.job, args.credential)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ClientError, OSError, ValueError, KeyError) as error:
        print(str(error) if isinstance(error, ClientError) else 'Invalid or unreadable local job/credential; no secret was printed.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
