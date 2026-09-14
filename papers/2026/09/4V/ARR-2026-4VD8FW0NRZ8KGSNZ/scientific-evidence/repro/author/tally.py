import re, glob, collections
rows = []
for f in glob.glob('s3b_seed3?.txt'):
    for ln in open(f):
        m = re.match(r"start \d+: gamma = ([\d.]+) active = (\[.*\])", ln)
        if m: rows.append((round(float(m.group(1)), 7), m.group(2)))
c = collections.Counter(rows)
print(f"{len(rows)} local optima tallied")
for (g, a), n in sorted(c.items(), key=lambda kv: -kv[0][0])[:25]:
    print(f"  {n:3d} x  gamma = {g:.7f}  active = {a}")
