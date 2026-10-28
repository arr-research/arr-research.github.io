from pathlib import Path
P=Path(__file__).parent
s=(P/'check-first1152.py').read_text(encoding='utf-8')
a=s.index('cases=');b=s.index('\ntry:',a)
s=s[:a]+"cases=[('identical_fullrank',[m.eye(2)/2,m.eye(2)/2]),('almost_identical_pure',[pure([1,0]),pure([1,m.power(2,-64)])])]"+s[b:]
s=s.replace('for k in [16,64,128]:','for k in [64]:')
s=s.replace("assert 0<q<p<1 and 0<Db<=Do+m.mpf('1e-100') and Do<=Di+m.mpf('1e-100')","assert 0<q<1 and 0<p<1 and -m.mpf('1e-100')<=Db<=Do+m.mpf('1e-100') and Do<=Di+m.mpf('1e-100')")
s=s.replace("'CONTROL1152.json'","'NEGATIVE1152.json'").replace("'FAILURE1152.json'","'NEGATIVE-FAILURE1152.json'")
(P/'negative1152.py').write_text(s,encoding='utf-8')
