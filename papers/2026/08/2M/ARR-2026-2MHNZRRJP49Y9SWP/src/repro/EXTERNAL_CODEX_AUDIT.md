# External Codex audit — version 0.6

## Status

This was a separate read-only Codex task, not human peer review, formal
verification, independent reproduction, or a priority certification.

## Score on the requested scale

The scale assigns `10.00` to a correct unconditional solution of a Millennium
Prize Problem.

| Dimension | Score |
|---|---:|
| Apparent correctness | 9.20 |
| Rigor | 8.55 |
| Novelty | 6.35 |
| Depth | 6.15 |
| Generality | 8.85 |
| Reproducibility | 7.50 |
| Potential impact | 6.00 |
| **Global** | **6.60 / 10.00** |

Uncertainty interval: `[5.65, 7.40]`.

## Mathematical verdict

The audit found no fatal error in the chain

```text
absorption on X
  => (I_Y)_m = (I_Y^(2))_m
  => (I_Y)_m = 0
  => h_Z(m) >= h^0(P^d,O(m)).
```

It separately validated the adapted finite projection, transfer of first
jets, one-degree fattening argument, Bertini construction, restriction
isomorphism, local identity `y=-f/G in m_p^2`, and the `r_1`/Gauss refinement.

The initial verdict was “publish after mandatory minor revision.” The
requested revisions were:

- state the Jacobian criterion at the étale step;
- use irreducibility of the Grassmannian for the finite intersection of open
  center conditions;
- describe Wang only as an analogous adapted-projection construction;
- distinguish the support from the scheme structure of the Bertini base
  scheme;
- justify integralness of a smooth projective hypersurface;
- display the hypersurface exact sequence and cohomology vanishings;
- correct the Wang and Lee–Phillips bibliography.

All were applied. The referee then rechecked the final source, 9-page PDF and
clean build log and confirmed:

> No new defect prevents publication. The conditions of the verdict remain
> satisfied: PUBLISH.

The main remaining scientific uncertainty is specialist priority review.
