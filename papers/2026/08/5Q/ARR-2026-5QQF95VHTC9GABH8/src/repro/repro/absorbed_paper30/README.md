# Paper 30: exact rank--norm phase transitions

This package contains the manuscript, exact Horn certificates, independent
Littlewood--Richardson replay, priority audit, and visual QA for a single
merged paper that supersedes the unpublished isolated Paper 29 witness.

## Main results

- On the dimension-eight family
  `lambda_t=(4-3t,t,t,t,-1,-1,-1,-1)`, the unrestricted cost is
  `10-7t` on `[0,1/2]` and `9-5t` on `[1/2,1]`.
- The rank-at-most-four cost is `10-6t`, so the exact gap is
  `min(t,1-t)` and the optimal rank is five for `0<t<1`.
- The dimension-nine two-valued spectrum `(5,5,5,5,-4,-4,-4,-4,-4)`
  has unrestricted cost `29` at minimum rank six and rank-five cost `30`.

No dimensional-minimality, all-spectrum classification, universal excess-one,
formal proof-assistant, peer-review, or absolute-priority claim is made.

## Replay and build

```powershell
.\run_scientific_replay.ps1
.\build_local.ps1
python .\package_release.py
python .\package_release.py --check
```

All scientific replay code uses exact `fractions.Fraction` arithmetic.  The
independent dimension-eight route directly enumerates nonzero
Littlewood--Richardson tableaux and does not import the recursive-Horn route.

