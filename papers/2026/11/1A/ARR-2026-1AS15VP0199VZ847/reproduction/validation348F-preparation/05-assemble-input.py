require(platform.node()==OWNED_RUNTIME_NODE, 'Owned validation runtime changed')
parts_manifest=json.loads((ROOT/'INPUT-CHUNKS348E.json').read_bytes())
require(parts_manifest['input_name']=='ui-return348D.zip' and len(parts_manifest['parts'])==28, 'Frozen input identity')
pieces=[]
for index,entry in enumerate(parts_manifest['parts']):
    require(entry['index']==index and entry['name']==f'part-{index:03d}.bin','Exact sequential input chunks')
    path=ROOT/'input-parts'/entry['name']
    require(path.is_file() and not path.is_symlink(), 'Required regular chunk')
    raw=path.read_bytes()
    require(len(raw)==entry['bytes'] and digest(raw)==entry['sha256'], 'Actual chunk identity')
    receipt=json.loads((ROOT/'transport-receipts'/f'part-{index:03d}.json').read_bytes())
    require(receipt['hostname']==OWNED_RUNTIME_NODE and receipt['index']==index and receipt['sha256']==digest(raw) and receipt['bytes']==len(raw),'Actual chunk receipt binding')
    pieces.append(raw)
bundle=b''.join(pieces)
require(len(bundle)==parts_manifest['bytes']==5429697 and digest(bundle)==parts_manifest['sha256']=='b74ab3e6e1d349aafe5ed42d984270e0ae1ee86ac158a1d9738dc6274f1b6e4b', 'Exact original bundle before exclusive write')
dest=ROOT/'ui-return348D.zip'
require(not dest.exists() and not dest.is_symlink(),'Original input destination must be absent')
with dest.open('xb') as stream: stream.write(bundle);stream.flush();os.fsync(stream.fileno())
require(dest.read_bytes()==bundle,'Exact original bundle disk readback')
receipt={'bytes':len(bundle),'sha256':digest(bundle),'hostname':platform.node(),'parts':28,
         'observed_at':datetime.now(timezone.utc).isoformat(),'method':'verified-chunk-assembly-exclusive-write-readback'}
with (ROOT/'transport-receipts'/'assembled.json').open('x',encoding='utf-8') as stream:
    json.dump(receipt,stream,indent=2);stream.write('\n')
print(json.dumps(receipt))
