"""Light exact fixtures for the canonical tester-compression memo.

This script proves no general theorem.  It checks, with SymPy exact arithmetic,
the nonuniform four-oracle fixture, a singular-safe compression toy model, and
the weighted-Gram identity used in the equality statement.  Any failed check
raises and the process exits nonzero.
"""

from itertools import combinations

from sympy import I, Matrix, Rational, eye, simplify, sqrt, zeros


def tr(a: Matrix):
    return sum(a[j, j] for j in range(a.rows))


def projector(v: Matrix) -> Matrix:
    return v * v.conjugate().T


def check_rank_one_projector(rho: Matrix) -> None:
    assert rho == rho.conjugate().T
    assert rho * rho == rho
    assert tr(rho) == 1


def diagonal_unitary_fixture() -> None:
    inv_sqrt2 = 1 / sqrt(2)
    phi0 = Matrix([1, 1]) * inv_sqrt2
    phipi = Matrix([1, -1]) * inv_sqrt2
    phiplus = Matrix([1, I]) * inv_sqrt2
    phiminus = Matrix([1, -I]) * inv_sqrt2
    states = [projector(v) for v in (phi0, phipi, phiplus, phiminus)]
    for rho in states:
        check_rank_one_projector(rho)

    effects = [states[0], states[1], zeros(2), zeros(2)]
    assert sum(effects, zeros(2)) == eye(2)

    priors = [Rational(7, 10), Rational(1, 10),
              Rational(1, 10), Rational(1, 10)]
    success = sum(p * tr(m * rho)
                  for p, m, rho in zip(priors, effects, states))
    assert success == Rational(4, 5)

    feature_matrix = Matrix.hstack(phi0, phipi, phiplus, phiminus)
    dimension = feature_matrix.rank()
    assert dimension == 2
    top_dimension_priors = sum(sorted(priors, reverse=True)[:dimension])
    assert top_dimension_priors == Rational(4, 5)
    assert min(1, max(priors) * dimension) == 1

    # Strict-gap equality: the two guessed vectors are orthonormal.
    gram_guessed = Matrix.hstack(phi0, phipi).conjugate().T * Matrix.hstack(
        phi0, phipi
    )
    assert gram_guessed == eye(2)


def canonical_compression_fixture() -> None:
    # Genuine Moore--Penrose branch: W has a one-dimensional kernel.  The
    # canonical POVM sums to the support projector, not the ambient identity.
    W = Matrix.diag(1, 2, 0)
    sqrtW = Matrix.diag(1, sqrt(2), 0)
    invsqrtW = Matrix.diag(1, 1 / sqrt(2), 0)
    supportW = Matrix.diag(1, 1, 0)
    J1 = Matrix.diag(1, 0, 0)
    J2 = Matrix.diag(0, Rational(1, 2), 0)
    assert W.det() == 0
    assert invsqrtW * W * invsqrtW == supportW
    assert tr(W * J1) == tr(W * J2) == 1

    M1, M2 = Matrix.diag(1, 0, 0), Matrix.diag(0, 1, 0)
    assert M1 + M2 == supportW
    T1, T2 = sqrtW * M1 * sqrtW, sqrtW * M2 * sqrtW
    assert T1 + T2 == W
    assert invsqrtW * T1 * invsqrtW == M1
    assert invsqrtW * T2 * invsqrtW == M2

    rho1, rho2 = sqrtW * J1 * sqrtW, sqrtW * J2 * sqrtW
    assert tr(rho1) == tr(rho2) == 1
    for T, J, M, rho in ((T1, J1, M1, rho1), (T2, J2, M2, rho2)):
        assert tr(T * J) == tr(M * rho) == 1


def subspace_sum_dimension(subspaces: list[Matrix], subset: tuple[int, ...]) -> int:
    if not subset:
        return 0
    return Matrix.hstack(*(subspaces[i] for i in subset)).rank()


def rado_rank(subspaces: list[Matrix], subset: tuple[int, ...]) -> int:
    """Exact Rado rank from the min formula, for finite regression fixtures."""
    best = len(subset)
    for size in range(len(subset) + 1):
        for chosen in combinations(subset, size):
            candidate = len(subset) - len(chosen) + subspace_sum_dimension(
                subspaces, chosen
            )
            best = min(best, candidate)
    return best


def mixed_subspace_greedy_fixture() -> None:
    # Three genuinely rank-two supports share one two-dimensional flat; a
    # fourth rank-two support is disjoint.  The induced label matroid is
    # U_{2,3} direct-sum U_{1,1} even though none of the hypotheses is rank one.
    e1, e2, e3, e4 = (eye(4).col(i) for i in range(4))
    flat = Matrix.hstack(e1, e2)
    transverse = Matrix.hstack(e3, e4)
    subspaces = [flat, flat, flat, transverse]
    assert all(space.rank() == 2 for space in subspaces)
    assert rado_rank(subspaces, (0, 1, 2)) == 2
    assert rado_rank(subspaces, (0, 1, 2, 3)) == 3

    priors = [Rational(3, 10), Rational(3, 10),
              Rational(3, 10), Rational(1, 10)]
    chosen: tuple[int, ...] = ()
    value = Rational(0)
    for i in sorted(range(4), key=lambda j: priors[j], reverse=True):
        trial = chosen + (i,)
        if rado_rank(subspaces, trial) > len(chosen):
            chosen = trial
            value += priors[i]
    assert len(chosen) == 3
    assert value == Rational(7, 10)


def spectral_tail_robustness_fixture() -> None:
    # Full-rank noise destroys the exact support matroid, but a positive
    # low-rank core retains the beta + weighted-tail certificate.
    eta = Rational(1, 10)
    e1, e2, e3, e4 = (eye(4).col(i) for i in range(4))
    flat = Matrix.hstack(e1, e2)
    transverse = Matrix.hstack(e3, e4)
    supports = [flat, flat, flat, transverse]
    projectors = [space * space.conjugate().T for space in supports]
    cores = [(1 - eta) * P / 2 for P in projectors]
    residuals = [eta * eye(4) / 4 for _ in supports]
    states = [L + R for L, R in zip(cores, residuals)]
    assert all(rho.rank() == 4 and tr(rho) == 1 for rho in states)
    assert all(L.rank() == 2 and R.rank() == 4
               for L, R in zip(cores, residuals))
    assert all(tr(R) == eta for R in residuals)

    priors = [Rational(3, 10), Rational(3, 10),
              Rational(3, 10), Rational(1, 10)]
    chosen: tuple[int, ...] = ()
    beta = Rational(0)
    for i in range(4):
        trial = chosen + (i,)
        if rado_rank(supports, trial) > len(chosen):
            chosen = trial
            beta += priors[i]
    assert beta == Rational(7, 10)
    robust_bound = beta + eta
    assert robust_bound == Rational(4, 5) < 1


def weighted_gram_fixture() -> None:
    # Three trine states form a scalable frame in dimension two with c_i=2/3.
    # A real exact realization avoids floating-point roots of unity.
    v1 = Matrix([1, 0])
    v2 = Matrix([-Rational(1, 2), sqrt(3) / 2])
    v3 = Matrix([-Rational(1, 2), -sqrt(3) / 2])
    F = Matrix.hstack(v1, v2, v3)
    C = Rational(2, 3) * eye(3)
    K = F.conjugate().T * F
    assert F * C * F.conjugate().T == eye(2)
    assert K * C * K == K


def strict_matroid_unitary_fixture() -> None:
    # Normalized vectorizations of I, Z, diag(1,i), X, Y in the orthonormal
    # Pauli-Choi coordinates (I,Z,X,Y)/sqrt(2).
    u1 = Matrix([1, 0, 0, 0])
    u2 = Matrix([0, 1, 0, 0])
    u3 = Matrix([(1 + I) / 2, (1 - I) / 2, 0, 0])
    u4 = Matrix([0, 0, 1, 0])
    u5 = Matrix([0, 0, 0, 1])
    vectors = [u1, u2, u3, u4, u5]
    for v in vectors:
        assert simplify((v.conjugate().T * v)[0]) == 1
    assert u3 == (1 + I) * u1 / 2 + (1 - I) * u2 / 2
    assert Matrix.hstack(*vectors).rank() == 4
    assert Matrix.hstack(u1, u2, u3).rank() == 2
    assert Matrix.hstack(u1, u2, u4, u5).rank() == 4

    priors = [Rational(3, 10), Rational(1, 4), Rational(1, 5),
              Rational(3, 20), Rational(1, 10)]
    top_four = sum(sorted(priors, reverse=True)[:4])
    greedy_basis_mass = priors[0] + priors[1] + priors[3] + priors[4]
    assert top_four == Rational(9, 10)
    assert greedy_basis_mass == Rational(4, 5)

    # Project onto I, Z, X, Y and never guess the dependent phase label.
    effects = [projector(u1), projector(u2), zeros(4),
               projector(u4), projector(u5)]
    assert sum(effects, zeros(4)) == eye(4)
    success = sum(p * tr(m * projector(v))
                  for p, m, v in zip(priors, effects, vectors))
    assert success == greedy_basis_mass

    # Exhaust the 32 subsets: the correct-label vector lies in the vector
    # matroid independence polytope, and its weighted cap is exactly 4/5.
    correct = [tr(m * projector(v)) for m, v in zip(effects, vectors)]
    best_independent_mass = Rational(0)
    for size in range(6):
        for subset in combinations(range(5), size):
            rank = (Matrix.hstack(*(vectors[j] for j in subset)).rank()
                    if subset else 0)
            assert sum(correct[j] for j in subset) <= rank
            if rank == size:
                best_independent_mass = max(
                    best_independent_mass, sum(priors[j] for j in subset)
                )
    assert best_independent_mass == Rational(4, 5)
    # Every prior drop is strict here; the exact equality audit requires each
    # prefix success to equal its vector-matroid rank.
    for j in range(1, 6):
        assert sum(correct[:j]) == Matrix.hstack(*vectors[:j]).rank()


def mixed_support_scope_fixture() -> None:
    # Three identical full-rank qubit states: the support Rado matroid is the
    # uniform matroid U_{2,3}, while geometry/spectra make the actual optimum
    # only p_max.  This certifies validity but also non-sharpness of supports.
    rho = eye(2) / 2
    priors = [Rational(1, 2), Rational(3, 10), Rational(1, 5)]

    def support_sum_dimension(subset):
        return 0 if not subset else 2

    def rado_rank(subset):
        subset = tuple(subset)
        candidates = []
        for size in range(len(subset) + 1):
            for positions in combinations(range(len(subset)), size):
                chosen = tuple(subset[j] for j in positions)
                candidates.append(len(subset) - len(chosen)
                                  + support_sum_dimension(chosen))
        return min(candidates)

    assert [rado_rank(range(j)) for j in range(1, 4)] == [1, 2, 2]
    rado_cap = sum(sorted(priors, reverse=True)[:2])
    assert rado_cap == Rational(4, 5)

    # For identical states, any POVM obeys sum_i Tr(M_i rho)=1; weighting by
    # priors is at most p_max.  Guessing label 1 always attains that value.
    always_first = [eye(2), zeros(2), zeros(2)]
    actual = sum(p * tr(m * rho) for p, m in zip(priors, always_first))
    assert actual == max(priors) == Rational(1, 2)
    assert actual < rado_cap
    correct = [tr(m * rho) for m in always_first]
    assert sum(correct[:2]) < rado_rank(range(2))


def trine_phase_coloop_fixture() -> None:
    # Computational Choi coordinates: |00>, |11>, |01>, |10>.
    omega = -Rational(1, 2) + I * sqrt(3) / 2
    phases = [Matrix([1, omega**j, 0, 0]) / sqrt(2) for j in range(3)]
    x_state = Matrix([0, 0, 1, 1]) / sqrt(2)
    y_state = Matrix([0, 0, -I, I]) / sqrt(2)
    phase_effects = [Rational(2, 3) * projector(v) for v in phases]
    x_effect = projector(x_state) + projector(y_state)
    effects = phase_effects + [x_effect]
    assert simplify(sum(effects, zeros(4))) == eye(4)

    # Choose one exact point in the open chamber: a=3/10, b=1/10.
    a, b = Rational(3, 10), Rational(1, 10)
    assert 3 * a + b == 1 and 0 < b < a
    states = [projector(v) for v in phases] + [projector(x_state)]
    correct = [simplify(tr(m * rho)) for m, rho in zip(effects, states)]
    assert correct == [Rational(2, 3)] * 3 + [1]
    success = sum(p * s for p, s in zip([a, a, a, b], correct))
    matroid_beta = 2 * a + b
    top_dimension = 3 * a
    assert success == matroid_beta == Rational(7, 10)
    assert top_dimension - matroid_beta == a - b == Rational(1, 5)
    assert all(m != zeros(4) for m in effects)


if __name__ == "__main__":
    diagonal_unitary_fixture()
    canonical_compression_fixture()
    weighted_gram_fixture()
    strict_matroid_unitary_fixture()
    mixed_subspace_greedy_fixture()
    spectral_tail_robustness_fixture()
    mixed_support_scope_fixture()
    trine_phase_coloop_fixture()
    print("PASS: singular compression, mixed Rado, spectral-tail, prior-profile, and Gram fixtures")
