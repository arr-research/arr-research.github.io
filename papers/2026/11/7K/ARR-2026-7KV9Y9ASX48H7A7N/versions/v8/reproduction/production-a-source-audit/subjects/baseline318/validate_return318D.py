"""Raw return validator. No claim of independent execution or scientific validity."""
from pathlib import Path, PurePosixPath
import json, hashlib, re, zipfile

SOURCE = 'd7e35107e2826d7a9342bdce30b50a3a725ec3dc'
TEX = '1ea3598636d490e6d3d542557301c61dbd6219b2927ed98357de7b248f30d2fd'
STATUS = 'TWO_FRESH_MATCHING_PDFS_RENDERED_PENDING_ALL_PAGE_VISUAL_AND_FIRST_EXACT_PDF_ASSESSMENT'
COMMANDS = ['apt-update','apt-install','tex-version','poppler-version','git-version']
for mode in ('a','b'):
    COMMANDS += ['clone-'+mode,'head-'+mode,'sparse-init-'+mode,'sparse-set-'+mode,'checkout-'+mode]
    if mode == 'a': COMMANDS += ['source-files-a']
    COMMANDS += ['epoch-'+mode,'tex-'+mode+'-pass1','tex-'+mode+'-pass2','tracked-diff-'+mode]
COMMANDS += ['pdfinfo','extract','render']

def require(ok, message):
    if not ok: raise ValueError(message)

def digest(raw): return hashlib.sha256(raw).hexdigest()

def check_zero(raw): require(raw == b'0\n', 'Exact single-line zero sentinel required')

def fresh(paths):
    require(len(paths)==len(set(map(str, paths))), 'Repeated destination')
    for path in paths:
        require(not path.exists() and not path.is_symlink(), 'Existing destination: '+str(path))
        for parent in path.parents:
            require(not parent.is_symlink(), 'Symlink parent')

def safe_names(names):
    seen=set()
    for name in names:
        require(isinstance(name,str) and name and '\\' not in name, 'Invalid archive path')
        parts=name.split('/')
        require(not PurePosixPath(name).is_absolute(), 'Absolute path')
        for part in parts:
            require(part not in ('','.','..') and part==part.rstrip(' .'), 'Aliased path')
            require(not re.search(r'[\x00-\x1f<>:"|?*]', part), 'Windows unsafe name')
            require(part.split('.')[0].upper() not in {'CON','PRN','AUX','NUL',*[f'COM{i}' for i in range(1,10)],*[f'LPT{i}' for i in range(1,10)]}, 'Reserved name')
        folded=name.casefold()
        require(folded not in seen, 'Duplicate/case alias')
        seen.add(folded)
    for name in seen:
        parts=name.split('/')
        require(not any('/'.join(parts[:i]) in seen for i in range(1,len(parts))), 'File/directory collision')

def check_outer(outer):
    require(outer['source']==SOURCE and outer['failure'] is None, 'Outer source/failure')
    exits=outer['actual_cli_exits']
    require(set(exits)=={'allocation','execution','download','release'}, 'Outer exit names')
    require(all(type(x) is int and x==0 for x in exits.values()), 'Outer actual exits')

def check_report(report):
    require(report['source']==SOURCE and report['tex_raw_sha256']==TEX and report['status']==STATUS, 'Report subject/status')
    builds=report['builds']
    require(len(builds)==2 and [x['mode'] for x in builds]==['a','b'], 'Two unique builds required')
    for b in builds:
        require(b['source']==SOURCE and type(b['input_files_verified']) is int and b['input_files_verified']==1045, 'Build inputs/source')
        require(type(b['pdf_bytes']) is int and b['pdf_bytes']>0 and re.fullmatch('[0-9a-f]{64}',b['pdf_sha256']) is not None, 'Build PDF')
        require(isinstance(b['epoch'],str) and re.fullmatch('[0-9]+',b['epoch']) is not None, 'Build epoch')
    require(all(builds[0][k]==builds[1][k] for k in ('epoch','pdf_bytes','pdf_sha256')), 'Different builds')
    require([x['name'] for x in report['commands']]==COMMANDS, 'Exact native command sequence')
    for c in report['commands']:
        require(type(c['actual_exit']) is int and c['actual_exit']==0 and c['timed_out'] is False, 'Native exit/timeout')
        require(isinstance(c['argv'],list) and c['argv'] and all(isinstance(x,str) for x in c['argv']), 'Native argv')
    cleanup=report['cleanup']
    require(len(cleanup)==2 and [c['path'] for c in cleanup]==['/content/tep318-build-b/clone-a','/content/tep318-build-b/clone-b'], 'Exact cleanup paths')
    require(all(c['removed'] is True and 'error' not in c for c in cleanup), 'Cleanup failure')
    require(type(report['pages']) is int and 1<=report['pages']<=60, 'Page count')

def check_manifest(rows, names):
    require(isinstance(rows,list) and rows, 'Empty manifest')
    paths=[r['path'] for r in rows]
    safe_names(paths)
    require(set(paths)==set(names)-{'evidence/manifest.json'}, 'Manifest coverage')
    for row in rows:
        require(type(row['bytes']) is int and row['bytes']>=0 and re.fullmatch('[0-9a-f]{64}',row['sha256']) is not None, 'Manifest types')

def validate(archive, attempt, source_manifest, destinations):
    fresh(destinations)
    outer=json.loads((attempt/'outer-report.json').read_bytes());check_outer(outer)
    for name in ('allocation','execution','download','release'):
        check_zero((attempt/(name+'.exit')).read_bytes())
        require((attempt/(name+'.log')).is_file(), 'Missing outer log')
    announcements=[]
    for line in (attempt/'execution.log').read_text(encoding='utf-8-sig').splitlines():
        if line.startswith('{'):
            value=json.loads(line)
            if 'archive_sha256' in value: announcements.append(value)
    require(len(announcements)==1, 'Actual archive announcement')
    ann=announcements[0]
    require(ann['archive']=='/content/tep318-build-b-results.zip' and ann['status']==STATUS, 'Remote archive identity')
    require(archive.stat().st_size==ann['archive_bytes'] and digest(archive.read_bytes())==ann['archive_sha256'], 'Transport archive bytes')
    expected=json.loads(source_manifest.read_bytes())['files']
    safe_names([r['path'] for r in expected]);require(len(expected)==1045, 'Frozen input inventory')
    with zipfile.ZipFile(archive) as z:
        infos=z.infolist();names=[i.filename for i in infos];safe_names(names)
        require(0<len(names)<5000 and sum(i.file_size for i in infos)<512_000_000, 'Archive bounds')
        require(all(not i.is_dir() and (i.external_attr>>16)&0o170000 != 0o120000 for i in infos), 'Archive regular files')
        require('evidence/manifest.json' in names, 'No manifest')
        rows=json.loads(z.read('evidence/manifest.json'));check_manifest(rows,names)
        for row in rows:
            raw=z.read(row['path'])
            require(len(raw)==row['bytes'] and digest(raw)==row['sha256'], 'Raw member mismatch '+row['path'])
        r=json.loads(z.read('evidence/report.json'));check_report(r)
        captured={n.removeprefix('evidence/source-capture/') for n in names if n.startswith('evidence/source-capture/')}
        require(captured=={x['path'] for x in expected}|{'SOURCE-INPUTS318.json'}, 'Exact captured source inventory')
        require(z.read('evidence/source-capture/SOURCE-INPUTS318.json')==source_manifest.read_bytes(), 'Pinned manifest differs')
        for row in expected:
            raw=z.read('evidence/source-capture/'+row['path'])
            require(len(raw)==row['bytes'] and digest(raw)==row['raw_sha256'], 'Captured source differs')
        require(digest(z.read('evidence/source-capture/manuscript318A.tex'))==TEX, 'Captured TeX')
        for c in r['commands']:
            require(z.read('evidence/'+c['name']+'.exit')==b'0\n', 'Actual native exit')
            for ext in ('.stdout','.stderr'): require('evidence/'+c['name']+ext in names, 'Missing native log')
        for mode in ('a','b'):
            require(z.read('evidence/head-'+mode+'.stdout').decode().strip()==SOURCE, 'Actual source head')
            require(z.read('evidence/epoch-'+mode+'.stdout').decode().strip()==r['builds'][0]['epoch'], 'Actual source epoch')
            require(not z.read('evidence/tracked-diff-'+mode+'.stdout').strip(), 'Tracked source changed')
        pdf=z.read('evidence/manuscript318A.pdf')
        require(pdf.startswith(b'%PDF-') and len(pdf)==r['builds'][0]['pdf_bytes'] and digest(pdf)==r['builds'][0]['pdf_sha256'], 'Canonical PDF')
        require(all(z.read('evidence/clone-'+m+'.pdf')==pdf for m in ('a','b')), 'Actual PDFs differ')
        info=z.read('evidence/pdfinfo.stdout').decode();match=re.search(r'(?m)^Pages:\s+(\d+)\s*$',info)
        require(match is not None and int(match.group(1))==r['pages'] and info==r['pdfinfo'], 'Actual pdfinfo')
        pages={n for n in names if re.fullmatch(r'evidence/page-[0-9]+\.png',n)}
        require(len(pages)==r['pages'] and {int(n.split('-')[-1].split('.')[0]) for n in pages}==set(range(1,r['pages']+1)), 'Page inventory')
        contacts={n for n in names if re.fullmatch(r'evidence/contact-[0-9]+\.jpg',n)}
        require(contacts=={f'evidence/contact-{i:02d}.jpg' for i in range(1,(r['pages']+3)//4+1)}, 'Contact inventory')
        require(all(z.read(n).startswith(b'\x89PNG\r\n\x1a\n') for n in pages), 'Actual PNG headers')
        require(SOURCE in z.read('evidence/manuscript318A.txt').decode(), 'PDF source marker')
        require('evidence/failure.txt' not in names and 'evidence/cleanup-pending.txt' not in names, 'Recorded failure/debt')
        universe={'evidence/'+n for n in ('report.json','manifest.json','manuscript318A.pdf','manuscript318A.txt','clone-a.pdf','clone-b.pdf','clone-a-latex.log','clone-b-latex.log')}
        universe |= {'evidence/'+c+ext for c in COMMANDS for ext in ('.exit','.stdout','.stderr')}
        universe |= {'evidence/source-capture/'+n for n in captured} | pages | contacts
        for mode in ('a','b'):
            for passno in (1,2):
                name=f'tex-{mode}-pass{passno}';prefix='evidence/native-tex/'+name+'/'
                retention=json.loads(z.read(prefix+'retention.json'))
                require(retention['attempt']==name and retention['actual_child_result']==next(c for c in r['commands'] if c['name']==name), 'Native retention child binding')
                saved=retention['files_saved_after_attempt'];safe_names([x['path'] for x in saved])
                require({x['path'] for x in saved}=={'manuscript318A'+ext for ext in ('.tex','.pdf','.log','.aux','.out')}, 'Native retained inventory')
                for item in saved:
                    raw=z.read(prefix+item['path'])
                    require(len(raw)==item['bytes'] and digest(raw)==item['sha256'], 'Native retained bytes')
                require(digest(z.read(prefix+'manuscript318A.tex'))==TEX, 'Native TeX')
                if passno==2: require(z.read(prefix+'manuscript318A.pdf')==pdf, 'Final native PDF')
                universe |= {prefix+x['path'] for x in saved} | {prefix+'retention.json'}
        require(set(names)==universe, 'Unexpected/missing archive artifact')
    return {'source':SOURCE,'PDF_sha256':digest(pdf),'PDF_bytes':len(pdf),'pages':r['pages'],'archive_sha256':digest(archive.read_bytes()),'raw_members_verified':len(rows),'source_input_members_verified':1045,'scope':'Exact raw declared inventories, bindings and exits checked; parent must read native logs/argv/retention, verify runtime inactivity, inspect all pages and assess exact PDF. Not independent proof of execution or mathematics.'}
