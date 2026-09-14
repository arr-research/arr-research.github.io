import importlib.util,sys
from pathlib import Path
s=importlib.util.spec_from_file_location('checked_validator',sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);m.CERTIFICATE=Path(sys.argv[2]);m.main()
