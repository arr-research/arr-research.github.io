from pathlib import Path
P=Path(__file__).parent
s=(P/'exact1152.py').read_text(encoding='utf-8-sig')
s=s.replace('R=(S-Z.H*T.pinv()*Z).applyfunc(s.simplify)','Y,params=T.gauss_jordan_solve(Z)\n Y=Y.subs({x:0 for x in params})\n assert T*Y==Z\n R=(S-Z.H*Y).applyfunc(s.simplify)')
s=s.replace('exact rational complex SymPy Moore-Penrose quadratic identity; no interval claim','exact rational complex SymPy linear solve T Y=Z and quadratic residual; no interval claim')
(P/'exact1152.py').write_text(s,encoding='utf-8')
