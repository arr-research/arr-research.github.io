"""Adapt retained PDF production texts; never compile or allocate locally."""
from pathlib import Path
import sys,re,json,hashlib,shutil
W=Path(__file__).resolve().parents[1]; E=Path(r'D:\Datos\the-eriksson-programme\autonomia\evidencia-284')
old=Path(r'D:\Datos\the-eriksson-programme\autonomia\evidencia-274\production-b')
source,tex=sys.argv[1:]
if re.fullmatch('[0-9a-f]{40}',source) is None or re.fullmatch('[0-9a-f]{64}',tex) is None:raise ValueError('Exact pins required')
P=W/'_tmp/production284-a'; P.mkdir(exist_ok=False)
map_items=[('bec9892206b0e9d82bc96ed247895d68d9c25e48',source),('fc4d23951bca6bad51ffd2af70a95d439a01eb4202015ff9098878c6bc9c912c',tex),('codex/tep-paper274-20261112','codex/tep-solenoidal275-20261112'),('papers/flat-coarse-rank/research-consolidation/paper274','papers/checkerboard-response'),('coverage_coexactness274','manuscript284B'),('tep274-build-b','tep284-build-a'),('evidencia-274/production-b','evidencia-284/production-a'),('build274.py','build284.py'),('attempt-b','attempt-a')]
for src,dst in [('build274.py','build284.py'),('capture_cli_atomic.ps1','capture_cli_atomic.ps1'),('run_owned_after_gate.ps1','run_owned_after_gate.ps1'),('readback_after_stop.ps1','readback_after_stop.ps1')]:
    text=(old/src).read_text(encoding='utf-8-sig')
    for a,b in map_items:text=text.replace(a,b)
    if src=='build274.py':
        lines=text.splitlines()
        for i,line in enumerate(lines):
            if line.startswith('    for token in (SOURCE,'):
                lines[i]="    for token in (SOURCE,'Model assessments and review context','Complete spectrum on the actual coexact domain','The exact shifted cancellation criterion','Logarithmic response persists on useful low data'):"
        text='\n'.join(lines)+'\n'
    if src=='run_owned_after_gate.ps1':
        text=text.replace("$out=Join-Path $PSScriptRoot 'attempt-a'","$out='D:\\Datos\\the-eriksson-programme\\autonomia\\evidencia-284\\production-a\\attempt-a'")
        text=text.replace("$script='/mnt/d/Datos/the-eriksson-programme/autonomia/evidencia-284/production-a/build284.py'","$script='/mnt/c/Trabajo/the-eriksson-programme/solenoidal-layers275-20261112/_tmp/production284-a/build284.py'")
    if src=='readback_after_stop.ps1':
        # Point the separate readback at the same retained D attempt.
        text=text.replace("$out=Join-Path $PSScriptRoot 'attempt-a'","$out='D:\\Datos\\the-eriksson-programme\\autonomia\\evidencia-284\\production-a\\attempt-a'")
    (P/dst).write_text(text,encoding='utf-8',newline='\n')
files=[{'path':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(P.iterdir()) if p.is_file()]
(P/'RUNNER-HASHES.json').write_text(json.dumps(files,indent=2)+'\n',encoding='utf-8',newline='\n')
shutil.copytree(P,E/'production-a');shutil.copy2(__file__,E/'prepare_production284.py')
print(json.dumps({'source':source,'tex_sha256':tex,'manifest_sha256':hashlib.sha256((P/'RUNNER-HASHES.json').read_bytes()).hexdigest(),'operative_files':len(files),'runtime_allocated':False}))
