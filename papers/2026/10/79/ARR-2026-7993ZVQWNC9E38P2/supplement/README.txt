SUPPLEMENT: Rank-two obstructions to Lorentzian graph partition functions
Lluis Eriksson, author research draft, 17 October 2026.

Status at package creation: author-side exact checks; no completed separate Astra assessment,
no importance grade, no submission or publication of this draft.
The general conjecture is not claimed solved and priority is not certified.

Requirements: Python 3, SymPy, NetworkX. NumPy is needed only to rerun
the exploratory source_lorentzian_rank2_probe.py and
profile_hierarchy_screen.py searches. Exact certificate
verification uses the preserved source-lorentzian-rank2-probe.json input.

Run the following scripts from a COPY of this supplement directory:
  python -B verify_degree_kernel.py
  python -B verify_regular_obstruction.py
  python -B verify_parametric_obstruction.py
  python -B verify_conditioning_hierarchy.py
  python -B verify_normalized_target.py
  python -B certify_source_witnesses.py
They regenerate their corresponding JSON result files in that directory.
These finite checks corroborate the manuscript proofs; they do not prove
the conjecture for arbitrary graphs, certify novelty, or constitute peer review.

verify_degree_kernel.py checks the original nonnegative target t=0,1,...,Delta.
verify_parametric_obstruction.py separately checks the strictly positive target
t=1,2,...,Delta+1 used in the manuscript. The former also checks all 806
minimum-degree compression certificates in the connected atlas at orders 3-7.

verify_regular_obstruction.py checks the original s=0 regular identity.
verify_parametric_obstruction.py checks the extension at five rational values
on 18 regular graphs, including the explicit 12-vertex/7-triangle graph.
Its parameter-list checks are not claimed exhaustive over all real parameters.
The determinant identity is also checked symbolically.

verify_conditioning_hierarchy.py checks the general conditioned-set identity
at h=1,2,3 on six source graphs, with 26 rational parameter comparisons.
It checks exact rational elimination for the eight-vertex cubic edge-swap
example, including the strictly positive target t=(1/100,1,2,3).
The hierarchy is not claimed sufficient for every connected nonclique.
The same file includes 24 normalized-target identity checks, with irregular
and disconnected sources as well as regular graphs.

verify_normalized_target.py checks the edge-wedge-triangle Hessian identity
on 144 graphs at two rational parameters (288 exact comparisons), including
irregular and disconnected graphs. It verifies the determinant symbolically
and the fixed positive matrix Kstar has eigenvalues 3,-1/2,0. The universal
triangle-free statement follows from the written counting proof, not merely
from the bounded graph census.

certify_source_witnesses.py recomputes all 137 selected integer Hessians from
the graph edge sets, target matrices and derivative multi-indices. The input
search is floating-point; its accepted certificates are checked exactly.
Each negative determinant and positive trace establishes inertia (2,1,0).
The four clique controls are classified as complete graphs; absence of a
detected witness for them is not used as a proof of Lorentzianity.

All scripts and results originate in the same authoring workflow. They have
not been evaluated by an independent human referee or a formal proof assistant.
The manifest protects file identity, not mathematical correctness.


ADDITION: NEIGHBOURHOOD GAP AND DIAMOND-FREE CHARACTERIZATION
The enlarged manuscript includes an exact profile-basis version of the
conditioned-set identity, the sufficient condition b(G)>c(G), and the
fixed four-state nonnegative target Kdiamond for connected diamond-free
sources. Positive perturbations may depend on the source graph.

Run these additional checks in this order, from a COPY of the supplement:
  python -B certify_profile_hierarchy.py
  python -B audit_profile_certificates.py
  python -B verify_neighbourhood_gap.py
  python -B verify_fixed_diamond.py
The archived profile-hierarchy-screen.json is input to the first script.
It contains a numeric parameter search, not mathematical certificates.
The certifier reconstructs every accepted matrix in exact arithmetic and
checks all 989 identities by direct partition-coefficient enumeration.
The characteristic-polynomial audit independently counts positive,
negative and zero roots of the stored real symmetric integer matrices.
Here independence means a separate algorithm, not a separate reviewer.
It also checks complete coverage of all 989 connected noncliques of
orders 3--7 in the NetworkX atlas. Five clique controls are excluded.

The gap verifier checks the boundary compression and positive continuations
on 634 graphs. The fixed-diamond verifier checks 255 diamond-free graphs:
88 triangle-free and 167 with triangles. It compares exact partition
Hessians for the common nonnegative target (or its three-state principal
target) and strictly positive rational perturbations. Both sets have 255
exact comparisons. The fixed target has one zero entry, rank two and
inertia (1,1,2). No common strictly positive perturbation for all source
orders is asserted.

All four scripts were rerun from the assembled supplement. Their JSON
outputs matched the original files byte for byte. This tests packaging
and reproducibility; it is not external peer review, a proof-assistant
verification, or a claim that finite tests prove the general conjecture.
The manuscript contains the general combinatorial proofs separately.


ADDITION: FIXED TARGETS FOR CLIQUE SEPARATORS AND SCOPE LIMITS
The expanded manuscript includes the two-branch proposition, the fixed
five-spin theorem for K_s joined to any number of disjoint nonempty cliques,
and the precise limitation of one four-spin derivative. Its profile identity
now explicitly allows rectangular evaluation matrices.

Run from a copy of this supplement:
  python -B verify_two_clique_extension.py
  python -B verify_fixed_five_cluster.py
  python -B verify_four_spin_restriction.py
  python -B probe_fixed_diamond_scope.py
  python -B probe_larger_fixed_target.py
  python -B probe_three_spin_targets.py

The first script checks symbolic determinants, 64 direct boundary identities
and 46 direct positive identities. The fixed-five script checks 64 direct
boundary identities and 27 direct positive identities with r=2,3,4,5,6;
the output also records a rational positive continuation for every case.
The four-spin restriction script checks its determinant symbolically and
six direct Hessians. Failure of that specified derivative is NOT proof that
the fixed four-spin target has a Lorentzian partition polynomial.

The fixed-diamond scope script records direct exact Hessian certificates for
all 989 connected noncliques of orders 3--7. The larger search checks 64
selected seeded graphs up to order ten; this is not an exhaustive census.
The three-spin script checks three particular principal targets and stops
at the first exact Lorentzian counterexample for each. It tests every
quadratic derivative and the full support exchange condition. It does not
assert that all three-spin targets fail or that four states are necessary.

These scripts load selected helper function definitions from
certify_profile_hierarchy.py; the larger probe also reads the function
definitions in probe_fixed_diamond_scope.py. All dependencies are included.
The fixed-five and four-spin restriction scripts were run from this assembled
supplement after adding the r=5,6 cases and the symbolic restriction test.
Other new files preserve the already-run preceding research checks, with
only obsolete draft-location metadata updated. Original outputs are in
the round-two/round-three research archives. Runtime fields can vary on replay.

The newly located primary Zeng research note is credited in the introduction
and pinned by commit and content hash in prior-art-audit.json. No code from
that repository was executed. None of these checks is a separate model
review, proof-assistant verification, or worldwide priority certificate.

ADDITION: COMPLETE MULTIPARTITE SOURCES
Run python -B verify_multipartite_extension.py from the supplement directory.
It symbolically checks two determinants, reconstructs profile kernels for
36 complete multipartite sources, and compares every boundary Hessian with
direct coefficient enumeration. It also checks 17 positive identities.
Largest parts run from 2 through 6. These checks corroborate the general
counting proof; they do not supply its arbitrary-order scope. The script
loads only function definitions from certify_profile_hierarchy.py.
The Choudhury--Khare distance-matrix blowup polynomial is credited and
distinguished in the manuscript and prior-art-audit.json.

ADDITION: MAXIMUM DEGREE, TRUE TWINS AND LIMITS OF THE ZERO-PARAMETER TEST
Run python -B verify_maximum_degree_twins.py for the new theorem checks:
817 eligible atlas graphs plus four larger cases; 821 exact compression
certificates and 819 direct positive Hessian identities. The two largest
cases (15 and 16 vertices) do not use direct partition enumeration.
Run python -B probe_zero_parameter_kernels.py for the exact finite search
using the binomial local-type formula. It tests 989 atlas noncliques and
12 selected clique blowups; nine blowups have PSD T_h at every h.
Run python -B verify_blowup_layer.py for the explicit C5[K2] limitation,
including exact matrices and rational congruence blocks at all eight h,
and three direct positive full-hierarchy identities. Its symbolic C5[K_s]
output is exploratory; no all-s theorem follows from it or is claimed.
All three scripts load local helper definitions; all dependencies are
included. zero-parameter-local-formula.txt explains the binomial count.
The original round-six research archive preserves the pre-integration
outputs. The supplement's blowup-layer verifier adds direct checks of the
displayed coefficient polynomial, reversal symmetry and pivot table.
None of these author-side computations supplies an external review,
worldwide priority certificate, or numerical quality/importance score.
