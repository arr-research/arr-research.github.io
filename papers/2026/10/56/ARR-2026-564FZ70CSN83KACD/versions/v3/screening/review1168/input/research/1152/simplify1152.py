from pathlib import Path
P=Path(__file__).parent
s=(P/'exact1152.py').read_text(encoding='utf-8-sig').replace('Y,params=T.gauss_jordan_solve(Z)','T=T.applyfunc(s.simplify);Z=Z.applyfunc(s.simplify);S=S.applyfunc(s.simplify)\n Y,params=T.gauss_jordan_solve(Z)').replace('assert T*Y==Z','assert (T*Y-Z).applyfunc(s.simplify)==s.zeros(n*d,d)')
(P/'exact1152.py').write_text(s,encoding='utf-8')
