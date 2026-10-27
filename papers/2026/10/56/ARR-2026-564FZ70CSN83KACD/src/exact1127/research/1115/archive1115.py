"""Terminal immutable archive protocol, adapted from own archive1100 lineage."""
from pathlib import Path
import ast, datetime, hashlib, json, shutil

C = Path(r'C:\Trabajo\airr\2026-10-27_fixed1115-audit').resolve()
D = Path(r'D:\Proyectos\airr-investigacion\2026-10-27_fixed1115-audit').resolve()
assert str(C) == r'C:\Trabajo\airr\2026-10-27_fixed1115-audit'
assert str(D) == r'D:\Proyectos\airr-investigacion\2026-10-27_fixed1115-audit'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def inventory(root):
    assert not any(p.is_symlink() or p.is_junction() for p in root.rglob('*'))
    return {p.relative_to(root).as_posix(): (p.stat().st_size, sha(p))
            for p in root.rglob('*') if p.is_file()}

def check_inputs():
    receipt = json.loads((C/'INPUT_FINAL1115.json').read_text(encoding='utf-8'))
    count = 0
    for package in receipt['packages']:
        a, b = Path(package['C']), Path(package['D'])
        mf = 'MANIFEST'+package['id']+'.json'
        assert sha(a/mf) == sha(b/mf) == package['manifest_sha256']
        for row in package['files']:
            assert sha(a/row['path']) == sha(b/row['path']) == row['sha256']
            assert (a/row['path']).stat().st_size == (b/row['path']).stat().st_size == row['bytes']
        expected = sorted([mf]+[row['path'] for row in package['files']])
        assert sorted(p.name for p in a.iterdir()) == sorted(p.name for p in b.iterdir()) == expected
        count += len(expected)
    assert count == 19
    return count

check_inputs()
assert not D.exists(), 'Refuse overwrite existing archive'
for p in C.rglob('*.json'):
    json.loads(p.read_text(encoding='utf-8-sig'))
for p in C.rglob('*.py'):
    ast.parse(p.read_text(encoding='utf-8-sig'), filename=str(p))
excluded = ['MANIFEST1115.json', 'SHA256SUMS1115.txt', 'CLOSURE1115.json']
assert not any((C/name).exists() for name in excluded), 'Refuse reseal existing audit'
files = [dict(path=k, bytes=v[0], sha256=v[1]) for k,v in sorted(inventory(C).items())]
manifest = {
    'task': '1115',
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'payloads': len(files), 'files': files, 'excluded_metadata': excluded,
    'reason': 'Manifest cannot hash itself. SHA256SUMS covers payloads and manifest. Closure is checked identically on C/D after writing.',
    'input_final_verification': 'INPUT_FINAL1115.json',
    'configuration': 'Requested GPT-6 Astra xhigh; effective identity/effort/independence unattested; shared context/filesystem'
}
(C/'MANIFEST1115.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
inv = inventory(C)
(C/'SHA256SUMS1115.txt').write_text(''.join(v[1]+'  '+k+'\n' for k,v in sorted(inv.items())), encoding='utf-8')
D.mkdir()
for p in C.rglob('*'):
    if p.is_file():
        dest = D/p.relative_to(C)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(p, dest)
before = inventory(C)
assert before == inventory(D)
closure = {
    'task': '1115', 'C': str(C), 'D': str(D),
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'preclosure_files': len(before), 'final_files_including_this_receipt': len(before)+1,
    'all_preclosure_inventory_and_bytes_identical': True,
    'manifest_sha256': sha(C/'MANIFEST1115.json'),
    'report_sha256': sha(C/'AUDIT1115.txt'),
    'verdict_sha256': sha(C/'verdict1115.json'),
    'sha256sums_sha256': sha(C/'SHA256SUMS1115.txt'),
    'input_packages_unchanged_verified_again': True, 'input_files_including_manifests': 19,
    'terminal_protocol': 'Identical closure bytes are written, then full recursive inventory/hash equality, manifest payload integrity and original input C/D integrity are asserted before TERMINAL_VERIFIED is printed.'
}
raw = (json.dumps(closure, indent=2, ensure_ascii=False)+'\n').encode('utf-8')
(C/'CLOSURE1115.json').write_bytes(raw)
(D/'CLOSURE1115.json').write_bytes(raw)
final = inventory(C)
assert final == inventory(D)
assert len(final) == len(before)+1
for row in files:
    assert final[row['path']] == (row['bytes'], row['sha256'])
check_inputs()
print(json.dumps({
    'status': 'TERMINAL_VERIFIED', 'files': len(final),
    'bytes': sum(v[0] for v in final.values()), 'manifest_payloads': len(files),
    'AUDIT1115_sha256': sha(C/'AUDIT1115.txt'),
    'verdict1115_sha256': sha(C/'verdict1115.json'),
    'MANIFEST1115_sha256': sha(C/'MANIFEST1115.json'),
    'SHA256SUMS1115_sha256': sha(C/'SHA256SUMS1115.txt'),
    'CLOSURE1115_sha256': sha(C/'CLOSURE1115.json'),
    'C_D_identical': True, 'inputs_unchanged': True
}, indent=2))
