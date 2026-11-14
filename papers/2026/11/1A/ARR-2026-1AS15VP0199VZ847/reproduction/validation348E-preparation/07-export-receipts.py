# Run also after an earlier failure. Does not turn missing results into successes.
import zipfile, io
require(platform.node()==OWNED_RUNTIME_NODE, 'Owned validation runtime changed')
selected=[]
for directory in (ROOT,ROOT/'preflight',ROOT/'transport-receipts'):
    if directory.is_dir():
        for path in sorted(directory.iterdir()):
            if path.is_file() and not path.is_symlink() and path.suffix in ('.json','.stdout','.stderr','.exit'):
                selected.append(path)
for mode in ('normal','optimized'):
    for name in ('result.json','validation-failure.txt'):
        path=ROOT/('actual-'+mode)/name
        if path.is_file() and not path.is_symlink():selected.append(path)
names=[p.relative_to(ROOT).as_posix() for p in selected]
require(len(names)==len(set(names)), 'Unique export paths')
require(sum(p.stat().st_size for p in selected)<2*1024*1024,'Bounded receipts only; no original production ZIP copies')
rows=[{'path':name,'bytes':path.stat().st_size,'sha256':digest(path.read_bytes())} for path,name in zip(selected,names)]
manifest=json.dumps({'scope':'Actual available validation348E receipts, including failures; no implied success or runtime closure','files':rows},indent=2).encode()+b'\n'
output=ROOT/'validation348E-receipts.zip'
with output.open('xb') as sink:
    with zipfile.ZipFile(sink,'w',compression=zipfile.ZIP_DEFLATED) as archive:
        for path,name in zip(selected,names):archive.writestr(name,path.read_bytes())
        archive.writestr('EXPORT-MANIFEST.json',manifest)
raw=output.read_bytes()
with zipfile.ZipFile(io.BytesIO(raw)) as archive:
    require(set(archive.namelist())==set(names)|{'EXPORT-MANIFEST.json'},'Export exact inventory readback')
    for row in rows:require(digest(archive.read(row['path']))==row['sha256'],'Export raw member readback')
print(json.dumps({'filename':output.name,'bytes':len(raw),'sha256':digest(raw),'method':'rendered-base64-actual-receipt-archive',
                  'download_success_claim':False,'runtime_closed_claim':False,'data_base64':base64.b64encode(raw).decode('ascii')}))
