# Review response

This record documents the repairs made before deposit.

## P0/P1 issues

No P0 or P1 issue remained in the final audit.

## Closed P2 issue: asymptotic maximization

An earlier proof sketch expanded only on bounded K/s and did not explicitly
exclude maximizers with K<s or K/s tending to infinity. The final Proposition
2.4 now:

- bounds the K<s range by s^d/d! plus lower-order terms;
- observes that the limiting function has positive derivative at zero and
  hence a strictly larger maximum;
- excludes K/s tending to infinity because the normalized expression becomes
  negative while K=s stays positive;
- applies uniform binomial expansion on the remaining bounded range; and
- obtains the matching lower estimate by rounding the continuous maximizer.

The referee rechecked this repair and found the asymptotic proof sufficient.

## Closed P2 issue: genericity incidences

The final proof now states the numerical dimension comparisons explicitly:

- singular plane sections impose three first-jet conditions over a
  two-dimensional base;
- singular hypersurfaces off the plane impose four first-jet conditions over
  a three-dimensional base.

It also states that the closure of each incidence image is proper. The referee
checked these two additions against the exact final source hash and found no
regression.

## Attribution and claim control

- Sharpness in the ordinary plane multiple-point class is attributed to the
  classical literature.
- The manuscript makes no exhaustive priority claim for the universal
  generator count.
- The recent Ma–Zuo preprint is described as unconsolidated and is not used.
- No positive-characteristic, higher-dimensional sharpness, or optimal-degree
  claim is made.

## Reproducibility boundary

The replays certify only finite fixtures. Universal theorems rest on the
written proofs. No human peer review, ARR screening, formal verification, or
independent reproduction is claimed.
