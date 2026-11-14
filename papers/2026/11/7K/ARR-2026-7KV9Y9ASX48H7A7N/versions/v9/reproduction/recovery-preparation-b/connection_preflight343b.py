"""One connection/readiness probe; no source clone, build, tests or mutation."""
import os,json,sys
from pathlib import Path
root=Path('/content/tep343-build-a')
archive=Path('/content/tep343-build-a-results.zip')
if os.name!='posix' or not Path('/content').is_dir() or Path.cwd().resolve()!=Path('/content'):
    raise RuntimeError('Owned Colab /content readiness required')
if root.exists() or root.is_symlink() or archive.exists() or archive.is_symlink():
    raise RuntimeError('Fresh runtime required; unchanged builder root/archive already present')
print(json.dumps({'kind':'TEP343B_CONNECTION_PREFLIGHT','source':'28640cd82e5b2ae9a6da8c78ca772bc41134c0c6','cwd':str(Path.cwd().resolve()),'os_name':os.name,'builder_root_absent':True,'builder_archive_absent':True,'python_version':sys.version,'scope':'Point-in-time connection and unused builder paths only; no guarantee of subsequent connection or build success'}))
