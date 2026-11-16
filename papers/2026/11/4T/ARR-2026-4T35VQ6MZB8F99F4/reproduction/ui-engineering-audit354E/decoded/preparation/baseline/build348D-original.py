"""UNEXECUTED Linux-only PDF production348; no mathematical test or assessment.
Adapted from the actual successful343 recovery builder. Source bytes stay frozen.
"""
import os, sys, json, hashlib, subprocess, traceback, zipfile, re, shutil
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone

SOURCE = 'a27c28cbfd506b7ad06aeebb8b141df89d6a0cba'
BRANCH = 'codex/tep-stationary347b-20261114'
PAPER = 'papers/stationary-doob347'
TEX_SHA = '0a851ffb2e6b6a7c4a491266f6fdd2e22dcd4efc3c234cc5a57b86719f63319d'
SUPPORT_SHA = 'c273a2ada5308dacddcf6b28d615aa2e9721fa89f0e0c8fd6f48ac97738b127b'
EXTRA = {
    'MANIFEST.json': 'ddc04b04064d9a5ddadf56a64552748e9ae86afc224d68eeaef81a72221672ec',
    'retention.json': 'e24fb7055130ab2d30ca86fce6b0b24f4b6db951f03d6aeb0a7b1811bd353952',
    '.gitattributes': '7be1a69c06d7d7f7b45b226f4c770ea16e40d836adde81f017c7e07f216d3f46',
}
ROOT = Path('/content/tep348D-build-a')
OUT = ROOT / 'evidence'
ARCHIVE = Path('/content/tep348D-build-a-results.zip')
STATUS = 'TWO_FRESH_MATCHING_PDFS_RENDERED_PENDING_ALL_PAGE_VISUAL_AND_FIRST_EXACT_PDF_ASSESSMENT'
# Reproducibility metadata only: no visible text, mathematics or source edit.
TEX_ARG = (r'\pdfinfoomitdate=1\pdftrailerid{}'
           r'\ifdefined\pdfsuppressptexinfo\pdfsuppressptexinfo=15\fi'
           r'\input{manuscript347.tex}')
MARKERS = ('Stationary marginals and bottleneck restrictions for Boolean Doob kernels',
           'The model and the theorem map', 'Quantitative rigidity of the smoothed potential',
           'An admissible failure of uniform convergence',
           'The imported weighting theorem and its exact role',
           'Actual cut capacities above the rare-mass threshold',
           'Small supports without a marginal matching assumption',
           'Classical scaling and the unresolved comparison',
           'Model assessments and review context')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def utc():
    return datetime.now(timezone.utc).isoformat()

def put(path, value):
    with path.open('xb') as stream:
        stream.write((json.dumps(value, indent=2) + '\n').encode('utf-8'))

def safe_relative(name):
    require(isinstance(name, str) and name and '\\' not in name, 'Input name')
    require(not PurePosixPath(name).is_absolute() and
            all(p not in ('', '.', '..') for p in name.split('/')), 'Input traversal')
    return name

require(os.name == 'posix' and Path('/content').resolve() == Path('/content')
        and Path('/content').is_dir(), 'Own Colab Linux only')
require(not ROOT.exists() and not ROOT.is_symlink() and
        not ARCHIVE.exists() and not ARCHIVE.is_symlink(), 'Fresh preserved attempt required')
OUT.mkdir(parents=True)
commands, clones, cleanup, builds = [], [], [], []
status = 'FAILED_PRESERVED'
report = {'source': SOURCE, 'tex_raw_sha256': TEX_SHA, 'support_raw_sha256': SUPPORT_SHA,
          'started_at': utc(), 'python_version': sys.version, 'math_tests': False,
          'formal_verification': False, 'new_assessment': None,
          'billing_units': None, 'billing_seconds': None, 'tex_argument': TEX_ARG}

def atomic_exit(path, actual):
    require(type(actual) is int and not path.exists(), 'New actual exit required')
    temporary = path.with_name(path.name + '.tmp')
    with temporary.open('x', encoding='ascii', newline='\n') as stream:
        stream.write(str(actual) + '\n'); stream.flush(); os.fsync(stream.fileno())
    raw = temporary.read_bytes()
    require(re.fullmatch(rb'-?[0-9]+\n', raw) is not None and int(raw) == actual,
            'Closed real integer exit')
    os.replace(temporary, path)
    require(path.read_bytes() == raw, 'Exit readback differs')

def run(name, argv, cwd=None, timeout=600, env=None):
    started, timed_out = utc(), False
    with (OUT / (name + '.stdout')).open('xb') as stdout, (OUT / (name + '.stderr')).open('xb') as stderr:
        child = subprocess.Popen(argv, cwd=cwd or ROOT, stdout=stdout, stderr=stderr, env=env)
        try:
            actual = child.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True; child.kill(); actual = child.wait()
        stdout.flush(); os.fsync(stdout.fileno()); stderr.flush(); os.fsync(stderr.fileno())
    atomic_exit(OUT / (name + '.exit'), actual)
    commands.append({'name': name, 'argv': argv, 'actual_exit': actual, 'timed_out': timed_out,
                     'started_at': started, 'finished_at': utc()})
    require(actual == 0 and not timed_out, 'Child failed ' + name)
    return (OUT / (name + '.stdout')).read_text(errors='replace')

try:
    run('apt-update', ['apt-get', '-qq', 'update'])
    run('apt-install', ['apt-get', 'install', '-y', '-qq', 'texlive-latex-base',
                       'texlive-latex-recommended', 'lmodern', 'poppler-utils', 'python3-pil'], timeout=1200)
    run('tex-version', ['pdflatex', '--version'])
    run('poppler-version', ['pdftoppm', '-v'])
    run('git-version', ['git', '--version'])
    for mode in ('a', 'b'):
        clone = ROOT / ('clone-' + mode); clones.append(clone)
        run('clone-' + mode, ['git', 'clone', '--filter=blob:none', '--depth', '1', '--no-checkout',
                             '--branch', BRANCH, 'https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.git',
                             str(clone)], timeout=900)
        actual = run('head-' + mode, ['git', 'rev-parse', 'HEAD'], clone).strip()
        require(actual == SOURCE, 'Frozen branch HEAD changed; no fallback source')
        run('sparse-init-' + mode, ['git', 'sparse-checkout', 'init', '--cone'], clone)
        run('sparse-set-' + mode, ['git', 'sparse-checkout', 'set', PAPER], clone)
        run('checkout-' + mode, ['git', 'checkout', '--detach', SOURCE], clone, timeout=900)
        paper = clone / PAPER
        for name, digest in EXTRA.items():
            require(sha((paper / name).read_bytes()) == digest, 'Pinned extra differs ' + name)
        declared = json.loads((paper / 'MANIFEST.json').read_bytes())['payloads']
        require(len(declared) == 41, 'Exact frozen payload count')
        inventory = {}
        for row in declared:
            name = safe_relative(row['path'])
            require(name not in inventory, 'Repeated source input')
            path = paper / name
            require(path.resolve().is_relative_to(paper.resolve()) and path.is_file()
                    and not path.is_symlink(), 'Unsafe source input')
            raw = path.read_bytes()
            require(len(raw) == row['bytes'] and sha(raw) == row['sha256'], 'Frozen payload differs ' + name)
            inventory[name] = {'path': name, 'bytes': len(raw), 'sha256': sha(raw)}
        for name in EXTRA:
            require(name not in inventory, 'Extra/payload collision')
            raw = (paper / name).read_bytes()
            inventory[name] = {'path': name, 'bytes': len(raw), 'sha256': sha(raw)}
        require(len(inventory) == 44 and sha((paper / 'manuscript347.tex').read_bytes()) == TEX_SHA
                and sha((paper / 'support346-section.tex').read_bytes()) == SUPPORT_SHA, 'Active source identity')
        if mode == 'a':
            names = run('source-files-a', ['git', 'ls-files', '--', PAPER], clone).splitlines()
            require(set(names) == {PAPER + '/' + name for name in inventory}, 'Exact tracked source universe')
            for name in inventory:
                dest = OUT / 'source-capture' / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes((paper / name).read_bytes())
        epoch = run('epoch-' + mode, ['git', 'show', '-s', '--format=%ct', SOURCE], clone).strip()
        require(re.fullmatch(r'[0-9]+', epoch) is not None, 'Actual source epoch missing')
        env = dict(os.environ, SOURCE_DATE_EPOCH=epoch, FORCE_SOURCE_DATE='1', TZ='UTC', LC_ALL='C.UTF-8')
        for passno in (1, 2):
            name = 'tex-' + mode + '-pass' + str(passno)
            def native_paths():
                return [paper / 'manuscript347.tex', paper / 'support346-section.tex'] + sorted(paper.glob('production348*'))
            prior = {p.name: {'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())}
                     for p in native_paths() if p.is_file() and not p.is_symlink()}
            try:
                run(name, ['pdflatex', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
                           '-file-line-error', '-jobname=production348', TEX_ARG], paper, env=env)
            finally:
                dest = OUT / 'native-tex' / name; dest.mkdir(parents=True, exist_ok=False)
                saved = []
                for path in native_paths():
                    require(not path.is_symlink(), 'Unexpected native symlink')
                    if path.is_file():
                        raw = path.read_bytes(); (dest / path.name).write_bytes(raw)
                        saved.append({'path': path.name, 'bytes': len(raw), 'sha256': sha(raw)})
                observed = [c for c in commands if c['name'] == name]
                put(dest / 'retention.json', {'attempt': name, 'actual_child_result': observed[-1] if observed else None,
                                            'files_before_attempt': prior, 'files_saved_after_attempt': saved,
                                            'meaning': 'Presence may be preexisting output; actual exit/log determines success.'})
        raw = (paper / 'production348.pdf').read_bytes()
        require(raw.startswith(b'%PDF-'), 'No actual PDF')
        (OUT / ('clone-' + mode + '.pdf')).write_bytes(raw)
        log = (paper / 'production348.log').read_bytes(); (OUT / ('clone-' + mode + '-latex.log')).write_bytes(log)
        require(b'There were undefined references' not in log and b'Citation `' not in log,
                'Unresolved final-pass references/citations')
        diff = run('tracked-diff-' + mode, ['git', 'diff', '--exit-code', SOURCE, '--', PAPER], clone)
        require(not diff.strip(), 'Tracked source changed during build')
        builds.append({'mode': mode, 'source': actual, 'epoch': epoch, 'pdf_bytes': len(raw),
                       'pdf_sha256': sha(raw), 'input_files_verified': 44,
                       'overfull_lines': [line for line in log.decode(errors='replace').splitlines() if 'Overfull' in line]})
    require(builds[0]['pdf_sha256'] == builds[1]['pdf_sha256'] and
            builds[0]['pdf_bytes'] == builds[1]['pdf_bytes'], 'Fresh-clone PDFs differ; preserve both')
    report['builds'] = builds
    pdf = OUT / 'manuscript347.pdf'; pdf.write_bytes((OUT / 'clone-a.pdf').read_bytes())
    put(OUT / 'source-binding348.json', {'source': SOURCE, 'paper': PAPER, 'active_tex_sha256': TEX_SHA,
                                       'support_tex_sha256': SUPPORT_SHA, 'pdf_sha256': sha(pdf.read_bytes()),
                                       'tex_argument': TEX_ARG, 'input_files': list(inventory.values())})
    info = run('pdfinfo', ['pdfinfo', str(pdf)]); report['pdfinfo'] = info
    match = re.search(r'(?m)^Pages:\s+(\d+)\s*$', info)
    require(match is not None, 'Actual page count missing')
    count = int(match.group(1)); require(1 <= count <= 60, 'Unexpected page count')
    run('extract', ['pdftotext', '-layout', str(pdf), str(OUT / 'manuscript347.txt')])
    text = (OUT / 'manuscript347.txt').read_text(); normal = ' '.join(text.split())
    for marker in MARKERS:
        require(marker in normal, 'Actual PDF missing content marker ' + marker)
    require(len(text) > 15000 and '??' not in text and '[SLOT]' not in text, 'Incomplete extraction/reference')
    run('render', ['pdftoppm', '-r', '110', '-png', str(pdf), str(OUT / 'page')], timeout=900)
    pages = sorted(OUT.glob('page-*.png'), key=lambda p: int(p.stem.split('-')[-1]))
    require(len(pages) == count and [int(p.stem.split('-')[-1]) for p in pages] == list(range(1, count+1)), 'All pages required')
    from PIL import Image, ImageDraw, __version__ as pillow_version
    report['pillow_version'] = pillow_version
    for offset in range(0, count, 4):
        sheet = Image.new('RGB', (1040, 1480), '#dddddd')
        for j, path in enumerate(pages[offset:offset+4]):
            with Image.open(path) as im:
                im = im.convert('RGB'); im.thumbnail((500, 700))
                sheet.paste(im, ((j % 2)*520+(520-im.width)//2, (j // 2)*740+5))
            ImageDraw.Draw(sheet).text(((j % 2)*520+10, (j // 2)*740+714), path.name, fill='black')
        sheet.save(OUT / ('contact-' + str(offset//4+1).zfill(2) + '.jpg'), quality=93)
    report['pages'] = count; status = STATUS
except Exception:
    (OUT / 'failure.txt').write_text(traceback.format_exc(), encoding='utf-8')
finally:
    for clone in clones:
        try:
            require(clone.parent == ROOT and clone.name in ('clone-a', 'clone-b')
                    and not clone.is_symlink() and clone.resolve().parent == ROOT.resolve(), 'Disposable clone boundary')
            if clone.exists(): shutil.rmtree(clone)
            cleanup.append({'path': str(clone), 'removed': not clone.exists()})
        except Exception as exc:
            cleanup.append({'path': str(clone), 'removed': False, 'error': str(exc)})
    debts = [c for c in cleanup if not c['removed']]
    if debts:
        status = 'FAILED_PRESERVED'
        lines = ['CLEANUP-PENDING: ' + c['path'] for c in debts]
        (OUT / 'cleanup-pending.txt').write_text('\n'.join(lines)+'\n', encoding='utf-8')
        for line in lines: print(line)
    report.update(status=status, commands=commands, cleanup=cleanup, builds=builds, finished_at=utc())
    put(OUT / 'report.json', report)
    files = [p for p in sorted(OUT.rglob('*')) if p.is_file()]
    put(OUT / 'manifest.json', [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
                                'sha256': sha(p.read_bytes())} for p in files])
    with zipfile.ZipFile(ARCHIVE, 'x', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(OUT.rglob('*')):
            if path.is_file(): archive.write(path, path.relative_to(ROOT).as_posix())
print(json.dumps({'status': status, 'archive': str(ARCHIVE), 'archive_bytes': ARCHIVE.stat().st_size,
                  'archive_sha256': sha(ARCHIVE.read_bytes())}))
if status == 'FAILED_PRESERVED':
    raise RuntimeError('Production failed; retain all evidence, no blind retry')
