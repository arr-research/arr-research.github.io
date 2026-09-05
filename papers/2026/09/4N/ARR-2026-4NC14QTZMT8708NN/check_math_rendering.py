"""Parse manuscript formulas with Mathtext; no PDF or image generation."""
from pathlib import Path
import re
from matplotlib.mathtext import MathTextParser

text=Path(__file__).with_name('active_delay.md').read_text(encoding='utf-8')
formulas=re.findall(r'\\\[(.*?)\\\]',text,re.S)+re.findall(r'(?<!\$)\$([^$\n]+)\$(?!\$)',text)
parser=MathTextParser('path')
errors=[]
for index,formula in enumerate(formulas):
    formula=re.sub(r'\\tag\{[^}]*\}','',formula.strip())
    try: parser.parse('$'+formula+'$')
    except Exception as err: errors.append((index,formula,str(err)))
if errors:
    for err in errors: print(err)
    raise AssertionError(f'{len(errors)} Mathtext parse errors')
print(f'PASS: {len(formulas)} formulas parse with Mathtext (equation tags removed by compositor).')
