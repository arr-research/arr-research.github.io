# Reuse this one cell 28 times. Set index and exact corresponding frozen base64 text.
# Preserve each emitted receipt; clear pasted data after success to avoid a huge notebook DOM.
CHUNK_INDEX = None
CHUNK_BASE64 = ''
require(platform.node()==OWNED_RUNTIME_NODE, 'Owned validation runtime changed')
require(ROOT==Path('/content/ui-validation348E') and ROOT.is_dir() and not ROOT.is_symlink(), 'Exact existing input root')
parts_manifest=json.loads((ROOT/'INPUT-CHUNKS348E.json').read_bytes())
require(type(CHUNK_INDEX) is int and 0<=CHUNK_INDEX<len(parts_manifest['parts']), 'Set one exact chunk index')
entry=parts_manifest['parts'][CHUNK_INDEX]
require(entry['index']==CHUNK_INDEX and entry['name']==f'part-{CHUNK_INDEX:03d}.bin', 'Exact chunk filename')
require(isinstance(CHUNK_BASE64,str) and 0<len(CHUNK_BASE64)<=262144, 'One bounded base64 chunk required')
part=base64.b64decode(CHUNK_BASE64,validate=True)
require(len(part)==entry['bytes'] and digest(part)==entry['sha256'], 'Part bytes/hash before any write')
parts_root=ROOT/'input-parts'
require(parts_root.is_dir() and not parts_root.is_symlink(), 'Exact chunk directory')
dest=parts_root/entry['name']
require(not dest.exists() and not dest.is_symlink(), 'No chunk overwrite or silent retry')
with dest.open('xb') as stream: stream.write(part);stream.flush();os.fsync(stream.fileno())
require(dest.read_bytes()==part, 'Exact chunk disk readback')
receipt={'index':CHUNK_INDEX,'bytes':len(part),'sha256':digest(part),'hostname':platform.node(),
         'observed_at':datetime.now(timezone.utc).isoformat(),'method':'strict-base64-chunk-exclusive-write-readback'}
with (ROOT/'transport-receipts'/f'part-{CHUNK_INDEX:03d}.json').open('x',encoding='utf-8') as stream:
    json.dump(receipt,stream,indent=2);stream.write('\n')
print(json.dumps(receipt))
