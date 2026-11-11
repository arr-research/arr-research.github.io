# SPDX-License-Identifier: AGPL-3.0-or-later
"""Bounded, fail-closed public file-set/JSON/ZIP checks; no execution/extraction.

This rejects operational artifacts and common credential-bearing fields/patterns.
It is not a universal PII, steganography or rights certificate. Archive/text source
may mention credential paths as provenance; credential files/values are forbidden.
"""
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

INVENTORY = 'PACKAGE-INPUTS232B.json'
MANIFEST = 'MANIFEST.sha256'
RECEIPT = 'NORMALIZATION-RECEIPT232B.json'
GENERATED = {MANIFEST, RECEIPT}
MAX_FILES = 4096
MAX_FILE_BYTES = 32 * 1024 * 1024
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_TOTAL_BYTES = 256 * 1024 * 1024
MAX_ARCHIVE_MEMBERS = 1024
MAX_ARCHIVE_DEPTH = 4
MAX_JSON_DEPTH = 40
MAX_JSON_NODES = 1000000
FORBIDDEN_KEYS = {'agenttoken', 'controllertoken', 'accesstoken', 'refreshtoken',
                  'idtoken', 'clientsecret', 'privatekey', 'password', 'passwordhash',
                  'totpsecret', 'recoverycodes', 'recoveryhash', 'owneruserid',
                  'setuptoken', 'idempotencykey', 'token', 'credentials'}
BEARER = re.compile(rb'\bBearer[ \t]+[A-Za-z0-9._~+/-]{16,}={0,2}', re.IGNORECASE)
PRIVATE_KEY = re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
TEXT_CREDENTIAL_KEY = re.compile(
    rb'(?<!\\)"(?:agent[_ -]*token|controller[_ -]*token|access[_ -]*token|refresh[_ -]*token|'
    rb'id[_ -]*token|client[_ -]*secret|private[_ -]*key|password(?:[_ -]*hash)?|'
    rb'totp[_ -]*secret|recovery[_ -]*(?:codes|hash)|setup[_ -]*token|idempotency[_ -]*key|credentials|token)"\s*:',
    re.IGNORECASE)
JSON_START = re.compile(r'[\[{](?=\s*(?:"|\{|\[|\]|\}|-|[0-9]|true\b|false\b|null\b))')
MAX_EMBEDDED_ATTEMPTS = 20000
MAX_EMBEDDED_SCAN_BYTES = 512 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical_relative(name):
    require(isinstance(name, str) and bool(name) and name == name.strip()
            and '\\' not in name and ':' not in name and not name.startswith('/')
            and all(ord(character) >= 32 and ord(character) != 127 for character in name),
            'Noncanonical public relative path')
    parsed = PurePosixPath(name)
    require(bool(parsed.parts) and parsed.as_posix() == name
            and not any(part in {'.', '..', ''} or part.endswith((' ', '.')) for part in parsed.parts),
            'Noncanonical public relative path')
    return name


def reject_operational_name(name):
    lower = PurePosixPath(name).name.casefold()
    operational = lower.lstrip('.')
    safe_native = {'native-authority-evidence.json', 'native-release-gates232b.json'}
    require(not (operational.startswith(('native-', 'native_')) and lower.endswith('.json') and lower not in safe_native)
            and not re.match(r'^job(?:[0-9._-]|$)', operational)
            and not re.match(r'^binding[0-9]', operational)
            and lower not in {'.env', 'application_default_credentials.json'} and not lower.startswith('.env.')
            and 'credential' not in lower
            and not lower.endswith(('.dpapi', '.pem', '.key', '.p12', '.pfx', '.kdbx', '.sqlite', '.sqlite3', '.db')),
            'Private operational filename is forbidden: ' + name)


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, 'Duplicate JSON key is not a canonical public object')
        value[key] = item
    return value


def load_bounded_json(path, *, max_bytes=MAX_JSON_BYTES):
    require(path.stat().st_size <= max_bytes, 'Public JSON exceeds bounded size')
    try:
        return json.loads(path.read_text(encoding='utf-8-sig'), object_pairs_hook=unique_object)
    except (UnicodeError, json.JSONDecodeError, RecursionError) as error:
        raise ValueError('Malformed or excessively nested public JSON') from error


def lexical_files(record):
    # Check each lexical component BEFORE resolve can erase a symlink identity.
    record = Path(record)
    require(record.is_absolute() and '..' not in record.parts, 'Canonical absolute public record root required')
    component = Path(record.anchor)
    for part in record.parts[1:]:
        component = component / part
        require(not component.is_symlink(), 'Symlink path component is forbidden')
    require(record.is_dir(), 'Public record directory required')
    result = {}
    for directory, dirs, files in os.walk(record, followlinks=False):
        parent = Path(directory)
        for name in dirs:
            child = parent / name
            mode = child.lstat().st_mode
            require(not stat.S_ISLNK(mode) and stat.S_ISDIR(mode), 'Symlink/non-directory public path component')
        for name in files:
            child = parent / name
            mode = child.lstat().st_mode
            require(not stat.S_ISLNK(mode) and stat.S_ISREG(mode), 'Symlink/nonregular public file')
            relative = canonical_relative(child.relative_to(record).as_posix())
            require(relative.casefold() not in {item.casefold() for item in result}, 'Duplicate case-folded public path')
            require(child.stat().st_size <= MAX_FILE_BYTES, 'Public file exceeds bounded size')
            result[relative] = child
            require(len(result) <= MAX_FILES, 'Public file count exceeds bounded limit')
    return result


def exact_inventory(record, *, generating_manifest=False):
    actual = lexical_files(record)
    require(INVENTORY in actual, 'Exact public input inventory required')
    inventory = load_bounded_json(actual[INVENTORY])
    require(isinstance(inventory, dict) and isinstance(inventory.get('files'), list), 'Public inventory envelope')
    expected, folded = set(), set()
    for item in inventory['files']:
        require(isinstance(item, dict) and set(item) == {'path', 'bytes', 'sha256'}, 'Canonical inventory entry fields')
        name = canonical_relative(item['path'])
        require(name.casefold() not in {item.casefold() for item in GENERATED | {INVENTORY}},
                'Generated/self path must not be an input entry')
        require(name not in expected and name.casefold() not in folded, 'Duplicate public inventory path')
        require(type(item['bytes']) is int and 0 <= item['bytes'] <= MAX_FILE_BYTES
                and isinstance(item['sha256'], str) and re.fullmatch('[a-f0-9]{64}', item['sha256']),
                'Canonical inventory byte/hash fields')
        expected.add(name)
        folded.add(name.casefold())
    generated = set(actual) & GENERATED
    require(generated in (set(), GENERATED) or (generating_manifest and generated == {RECEIPT}),
            'Partial generated normalization state; never publish it')
    require(set(actual) == expected | {INVENTORY} | generated, 'Exact public file-set closure: unlisted or missing file')
    return inventory, actual


class PrivacyBudget:
    def __init__(self):
        self.bytes = 0
        self.files = 0
        self.json_nodes = 0
        self.embedded_attempts = 0
        self.embedded_scan_bytes = 0

    def inspect_text_json(self, raw):
        # Ordinary CLI logs are not declared JSON. Parse recognizable bounded
        # JSON values within them, including a report followed by CLI lines.
        # Raw credential syntax is checked independently, even in malformed text.
        require(not TEXT_CREDENTIAL_KEY.search(raw), 'Private credential/operational JSON key in text')
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeError:
            return  # Non-text binaries still passed filename/value/container checks.
        decoder = json.JSONDecoder(object_pairs_hook=unique_object)
        position = 0
        while True:
            match = JSON_START.search(text, position)
            if match is None:
                return
            start = match.start()
            window = text[start:start + MAX_JSON_BYTES]
            self.embedded_attempts += 1
            self.embedded_scan_bytes += len(window.encode('utf-8'))
            require(self.embedded_attempts <= MAX_EMBEDDED_ATTEMPTS
                    and self.embedded_scan_bytes <= MAX_EMBEDDED_SCAN_BYTES,
                    'Embedded public JSON attempt/scan bound')
            try:
                value, end = decoder.raw_decode(window)
            except json.JSONDecodeError:
                position = start + 1
                continue  # E.g. mathematical [0,n] or ordinary [colab] prose.
            except RecursionError as error:
                raise ValueError('Embedded public JSON nesting bound') from error
            self.inspect_json(value)
            position = start + end

    def inspect_json(self, value, depth=0):
        self.json_nodes += 1
        require(depth <= MAX_JSON_DEPTH and self.json_nodes <= MAX_JSON_NODES, 'Public JSON depth/node bound')
        if isinstance(value, dict):
            for key, item in value.items():
                normalized = re.sub('[^a-z0-9]', '', key.casefold())
                require(normalized not in FORBIDDEN_KEYS, 'Private credential/operational JSON key')
                self.inspect_json(item, depth + 1)
        elif isinstance(value, list):
            for item in value:
                self.inspect_json(item, depth + 1)
        elif isinstance(value, str):
            encoded = value.encode('utf-8')
            require(not BEARER.search(encoded) and not PRIVATE_KEY.search(encoded), 'Private credential value pattern')
            # Logs may carry another JSON object encoded as a JSON string. Inspect
            # recognizable valid encodings too; ordinary mathematical prose is
            # not interpreted as code or required to be syntactically JSON.
            if value.lstrip().startswith(('{', '[', '"')):
                require(len(encoded) <= MAX_JSON_BYTES, 'Encoded public JSON exceeds bounded size')
                try:
                    nested = json.loads(value, object_pairs_hook=unique_object)
                except json.JSONDecodeError:
                    return
                except RecursionError as error:
                    raise ValueError('Encoded public JSON nesting bound') from error
                self.inspect_json(nested, depth + 1)

    def inspect(self, raw, name, depth=0):
        self.files += 1
        self.bytes += len(raw)
        require(self.files <= MAX_FILES and self.bytes <= MAX_TOTAL_BYTES and len(raw) <= MAX_FILE_BYTES,
                'Public recursive payload resource bound')
        reject_operational_name(name)
        require(not BEARER.search(raw) and not PRIVATE_KEY.search(raw), 'Private credential value pattern')
        require(not name.casefold().endswith(('.tar', '.tgz', '.tar.gz', '.gz', '.bz2', '.xz', '.7z', '.rar', '.zst'))
                and not raw.startswith((b'\x1f\x8b', b'BZh', b'\xfd7zXZ\x00', b'7z\xbc\xaf\x27\x1c', b'Rar!', b'\x28\xb5\x2f\xfd'))
                and raw[257:262] != b'ustar', 'Unsupported archive/container must not bypass ZIP inspection')
        require(not raw.startswith((b'\xff\xfe', b'\xfe\xff', b'\x00\x00\xfe\xff',
                                    b'\x00{', b'\x00[', b'{\x00', b'[\x00', b'\x00\x00\x00{', b'\x00\x00\x00[')),
                'Unsupported encoded text/JSON must not bypass privacy inspection')
        archive_like = name.casefold().endswith('.zip') or raw.startswith(b'PK') or zipfile.is_zipfile(io.BytesIO(raw))
        if archive_like:
            require(depth < MAX_ARCHIVE_DEPTH, 'Public archive nesting depth bound')
            try:
                with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                    members = archive.infolist()
                    require(len(members) <= MAX_ARCHIVE_MEMBERS, 'Public archive member count bound')
                    names = set()
                    for member in members:
                        require(member.orig_filename == member.filename, 'Truncated/noncanonical archive member name')
                        member_name = member.filename[:-1] if member.is_dir() else member.filename
                        member_name = canonical_relative(member_name)
                        require(member_name.casefold() not in names, 'Duplicate archive member path')
                        names.add(member_name.casefold())
                        mode = member.external_attr >> 16
                        kind = stat.S_IFMT(mode)
                        require(not stat.S_ISLNK(mode)
                                and kind in ({0, stat.S_IFDIR} if member.is_dir() else {0, stat.S_IFREG}),
                                'Archive symlink/nonregular member is forbidden')
                        require(not member.flag_bits & 1 and member.compress_type in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED},
                                'Encrypted/unsupported public archive member')
                        require(member.file_size <= MAX_FILE_BYTES
                                and member.file_size <= max(1, member.compress_size) * 1000,
                                'Public archive member size/ratio bound')
                        reject_operational_name(member_name)
                        if member.is_dir():
                            require(member.file_size == 0, 'Archive directory has unexpected data')
                            continue
                        with archive.open(member) as stream:
                            data = stream.read(MAX_FILE_BYTES + 1)
                        require(len(data) == member.file_size, 'Archive member size/readback mismatch')
                        self.inspect(data, member_name, depth + 1)
            except (zipfile.BadZipFile, RuntimeError, NotImplementedError, OSError) as error:
                raise ValueError('Malformed/unsupported public archive') from error
        elif name.casefold().endswith('.json'):
            require(len(raw) <= MAX_JSON_BYTES, 'Public JSON exceeds bounded size')
            try:
                value = json.loads(raw.decode('utf-8-sig'), object_pairs_hook=unique_object)
            except (UnicodeError, json.JSONDecodeError, RecursionError) as error:
                raise ValueError('Malformed or excessively nested public JSON') from error
            self.inspect_json(value)
        else:
            self.inspect_text_json(raw)


def scan_files(actual):
    budget = PrivacyBudget()
    for name, path in sorted(actual.items()):
        budget.inspect(path.read_bytes(), name)
    return dict(inspected_file_instances=budget.files, inspected_bytes=budget.bytes, json_nodes=budget.json_nodes)
