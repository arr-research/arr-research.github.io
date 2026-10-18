from pathlib import Path
import hashlib, json, shutil, zipfile, re
from pypdf import PdfReader

root = Path(__file__).resolve().parent
inp = root.parent / 'input'
def info(p):
    return {'name': p.name, 'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
manifest = json.loads((inp/'artifact-manifest.json').read_text(encoding='utf-8'))
for rec in manifest['artifacts']:
    assert info(inp/rec['name']) == rec
for name in ('reviewed-inputs', 'supplement', 'visual', 'reproduction'):
    (root/name).mkdir(exist_ok=True)
for p in inp.iterdir():
    if p.is_file(): shutil.copy2(p, root/'reviewed-inputs'/p.name)
with zipfile.ZipFile(inp/'supplement.zip') as z:
    for name in z.namelist():
        q = (root/'supplement'/name).resolve()
        assert q.is_relative_to((root/'supplement').resolve())
    z.extractall(root/'supplement')
reader = PdfReader(inp/'main.pdf')
assert len(reader.pages) == 13
(root/'main-extracted.txt').write_text('\n\n'.join(f'PAGE {i+1}\n{p.extract_text()}' for i,p in enumerate(reader.pages)),encoding='utf-8')
tex = (inp/'main.tex').read_text(encoding='utf-8')
cited = set(k.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', tex) for k in group.split(','))
items = set(re.findall(r'\\bibitem\{([^}]+)\}', tex))
records = [info(p) | {'relative': p.relative_to(root/'supplement').as_posix()} for p in (root/'supplement').rglob('*') if p.is_file()]
out = {'input_files':[info(p) for p in inp.iterdir() if p.is_file()], 'manifest_match':True,'pdf_pages':len(reader.pages),'supplement':records,'citations_missing':sorted(cited-items),'bibliography_uncited':sorted(items-cited)}
(root/'input-check.json').write_text(json.dumps(out, indent=2),encoding='utf-8')
print(json.dumps(out, indent=2))
