# Exact replay

Run from the paper directory with:

```powershell
python .\repro\run_all_replays.py
```

The replay uses only the Python standard library and exact integer/rational
arithmetic. It regenerates `results.json` in a temporary directory and requires
byte-for-byte equality with the committed file.

It certifies:

- truncated local Macaulay quotient stabilization for the fixtures
  `(d,s)=(2,4),(3,3),(4,2)`, giving `mu=s^d` and `tau=s^d-1`;
- the Euler and initial Hessian terms for `x^5+y^5+x^3*y^3`;
- 36 fat-point/Milnor floor arithmetic cases;
- 22 defect-one formula cases; and
- 60 support/absorption arithmetic cases.

It does **not** mechanize analytic coordinates, finite contact determinacy,
incidence arguments, projective smoothness, or bibliographic priority.
