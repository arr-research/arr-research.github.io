# Repeat this cell once per actual chunk. Never reuse an index or invent data.
CHUNK_INDEX=None
CHUNK_BASE64=''
need(type(CHUNK_INDEX) is int and 0<=CHUNK_INDEX<len(plan['parts']),'Select an actual planned chunk')
need(isinstance(CHUNK_BASE64,str) and 0<len(CHUNK_BASE64)<4_000_000,'Bounded actual encoded bytes')
encoded=CHUNK_BASE64.encode('ascii')
path=BASE/plan['parts'][CHUNK_INDEX]['path']
publish_bytes(path,encoded,len(encoded),digest(encoded))
print(json.dumps(dict(encoded_chunk_saved=CHUNK_INDEX,encoded_bytes=len(encoded),raw_chunk_validation='pending existing materialize354A.py')))
