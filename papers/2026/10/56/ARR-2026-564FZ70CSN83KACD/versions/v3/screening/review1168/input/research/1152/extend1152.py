from pathlib import Path
P=Path(__file__).parent
s=(P/'check1152.py').read_text(encoding='utf-8-sig')
(P/'check-first1152.py').write_text(s,encoding='utf-8')
(P/'CONTROL-FIRST1152.json').write_bytes((P/'CONTROL1152.json').read_bytes())
s=s.replace("rows=[]\ncases=", "rows=[]\ndef plane(xs):return (m.eye(len(xs))-pure(xs))/2\ncases=")
s=s.replace("for name,ts in cases:", "cases.append(('three_noncommuting_ranktwo',[plane([1,0,0]),plane([1,1,0]),plane([1,1,1])]))\n for name,ts in cases:")
(P/'check1152.py').write_text(s,encoding='utf-8')
