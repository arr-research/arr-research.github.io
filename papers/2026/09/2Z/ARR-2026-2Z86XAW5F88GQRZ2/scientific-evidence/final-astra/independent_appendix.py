from pathlib import Path
import re,datetime
print('UTC',datetime.datetime.now(datetime.timezone.utc).isoformat())
root=Path(r'C:/Users/lluis/Documents/Codex/2026-09-11/airr-continuidad')
s=(root/'outputs/fable-c2c3-20260914/papers/A3_inertia_m3/candidate-2/paper.md').read_text(encoding='utf8').split('## Appendix A.')[1]
n=0
for line in s.splitlines():
 if not line.startswith('| $('):continue
 cells=line.split('|');formtxt=cells[1].strip();mt=re.fullmatch(r'\$\(([-0-9,;]+)\)\$',formtxt)
 if not mt:continue
 left,right=mt[1].split(';');alpha=list(map(int,left.split(',')));beta=list(map(int,right.split(',')));layers=re.findall(r'\\\{(.*?)\\\}',cells[-2]);levels={}
 for t,layer in enumerate(layers):
  terms=re.findall(r'([ab])_(\d+)',layer);assert 1<=len(terms)<=3
  for term in terms:assert term not in levels;levels[term]=t
 assert len(levels)==len(alpha)+3
 t3=levels['b','3'];actual=[levels['a',str(j)]-t3 for j in range(1,len(alpha)+1)]+[t3-levels['b',str(j)] for j in [1,2]]
 assert actual==alpha+beta,(formtxt,actual);n+=1
assert n==90
print('PASS independent parsing and cost reconstruction of',n,'Appendix A rows')
