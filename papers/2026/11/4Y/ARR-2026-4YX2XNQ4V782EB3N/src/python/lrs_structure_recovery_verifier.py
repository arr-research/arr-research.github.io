"""Exact finite-field GF(p^m) Overbeck Frobenius-shift, shortening, and LRS structure recovery verifier.

Zero floating-point arithmetic, zero '/' division operator, zero '**' operator (AST-enforced).
All field operations are exact polynomial arithmetic over F_p[x]/(f(x)) with integer coefficients.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from typing import Any


def int_pow(base: int, exp: int) -> int:
    if exp < 0:
        raise ValueError("Negative exponent forbidden in integer arithmetic")
    res = 1
    b = base
    e = exp
    while e > 0:
        if e & 1:
            res = res * b
        b = b * b
        e = e >> 1
    return res


def mod_inv_prime(a: int, p: int) -> int:
    a_mod = a % p
    if a_mod == 0:
        raise ZeroDivisionError("Zero has no multiplicative inverse mod p")
    return pow(a_mod, p - 2, p)


def poly_trim(poly: list[int], p: int) -> list[int]:
    out = [c % p for c in poly]
    while out and out[-1] == 0:
        out.pop()
    return out


def poly_mod_fp(a: list[int], b: list[int], p: int) -> list[int]:
    rem = poly_trim(a, p)
    div = poly_trim(b, p)
    if not div:
        raise ZeroDivisionError("Polynomial division by zero")
    inv_lead = mod_inv_prime(div[-1], p)
    deg_b = len(div) - 1
    while len(rem) - 1 >= deg_b and rem:
        fac = (rem[-1] * inv_lead) % p
        off = len(rem) - len(div)
        for i, coeff in enumerate(div):
            rem[off + i] = (rem[off + i] - fac * coeff) % p
        rem = poly_trim(rem, p)
    return rem


def poly_gcd_fp(a: list[int], b: list[int], p: int) -> list[int]:
    x = poly_trim(a, p)
    y = poly_trim(b, p)
    while y:
        x, y = y, poly_mod_fp(x, y, p)
    if x:
        inv_lead = mod_inv_prime(x[-1], p)
        x = [(c * inv_lead) % p for c in x]
    return x


def poly_mul_mod_fp(a: list[int], b: list[int], mod: list[int], p: int) -> list[int]:
    if not a or not b:
        return []
    res = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                res[i + j] = (res[i + j] + x * y) % p
    return poly_mod_fp(res, mod, p)


def is_irreducible_fp(p: int, mod: tuple[int, ...]) -> bool:
    """Rabin irreducibility test over F_p using exact polynomial GCD (zero floats)."""
    if p < 2 or len(mod) < 2 or mod[-1] % p == 0:
        return False
    m = len(mod) - 1
    mod_list = [c % p for c in mod]

    def pow_x(exp: int) -> list[int]:
        res = [1]
        base = [0, 1]
        e = exp
        while e > 0:
            if e & 1:
                res = poly_mul_mod_fp(res, base, mod_list, p)
            base = poly_mul_mod_fp(base, base, mod_list, p)
            e = e >> 1
        return res

    if pow_x(int_pow(p, m)) != [0, 1]:
        return False
    for d in range(1, (m // 2) + 1):
        xp = pow_x(int_pow(p, d))
        if len(xp) < 2:
            xp = xp + [0] * (2 - len(xp))
        xp[1] = (xp[1] - 1) % p
        xp = poly_trim(xp, p)
        g = poly_gcd_fp(mod_list, xp, p)
        if len(g) > 1:
            return False
    return True


class GFpm:
    """Exact finite field F_{p^m} = F_p[x]/(mod(x)) with zero floating-point arithmetic."""

    def __init__(self, p: int, mod: tuple[int, ...]) -> None:
        if not is_irreducible_fp(p, mod):
            raise ValueError(f"Modulus {mod} is not irreducible over F_{p}")
        self.p = p
        self.mod = tuple(c % p for c in mod)
        self.m = len(mod) - 1
        self.order = int_pow(p, self.m)

    def zero(self) -> tuple[int, ...]:
        return (0,) * self.m

    def one(self) -> tuple[int, ...]:
        return (1,) + (0,) * (self.m - 1)

    def gen(self) -> tuple[int, ...]:
        if self.m == 1:
            return (1,)
        return (0, 1) + (0,) * (self.m - 2)

    def scalar(self, c: int) -> tuple[int, ...]:
        return (c % self.p,) + (0,) * (self.m - 1)

    def is_zero(self, a: tuple[int, ...]) -> bool:
        return not any(a)

    def add(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def sub(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((x - y) % self.p for x, y in zip(a, b))

    def mul(self, a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        res = [0] * (2 * self.m - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    res[i + j] = (res[i + j] + x * y) % self.p
        for i in range(len(res) - 1, self.m - 1, -1):
            c = res[i]
            if c:
                for j in range(self.m + 1):
                    res[i - self.m + j] = (res[i - self.m + j] - c * self.mod[j]) % self.p
        return tuple(res[: self.m])

    def pow(self, a: tuple[int, ...], exp: int) -> tuple[int, ...]:
        if exp < 0:
            raise ValueError("Negative exponent forbidden")
        res = self.one()
        base = a
        e = exp
        while e > 0:
            if e & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            e = e >> 1
        return res

    def inv(self, a: tuple[int, ...]) -> tuple[int, ...]:
        if self.is_zero(a):
            raise ZeroDivisionError("Zero is not invertible in GF(p^m)")
        return self.pow(a, self.order - 2)

    def frob(self, a: tuple[int, ...], times: int = 1) -> tuple[int, ...]:
        cur = a
        for _ in range(times):
            cur = self.pow(cur, self.p)
        return cur

    def truncated_norm(self, a: tuple[int, ...], i: int) -> tuple[int, ...]:
        """Exact truncated skew norm N_i(a) = prod_{j=0}^{i-1} sigma^j(a)."""
        if i < 0:
            raise ValueError("Negative norm index forbidden")
        res = self.one()
        cur = a
        for _ in range(i):
            res = self.mul(res, cur)
            cur = self.frob(cur)
        return res


def matrix_rank_gf(F: GFpm, mat: list[list[tuple[int, ...]]]) -> int:
    if not mat or not mat[0]:
        return 0
    M = [list(row) for row in mat]
    rows = len(M)
    cols = len(M[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if not F.is_zero(M[i][c]):
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv_p = F.inv(M[r][c])
        M[r] = [F.mul(v, inv_p) for v in M[r]]
        for i in range(rows):
            if i != r and not F.is_zero(M[i][c]):
                fac = M[i][c]
                M[i] = [F.sub(M[i][j], F.mul(fac, M[r][j])) for j in range(cols)]
        r += 1
    return r


def matrix_mul_gf(
    F: GFpm, A: list[list[tuple[int, ...]]], B: list[list[tuple[int, ...]]]
) -> list[list[tuple[int, ...]]]:
    rows = len(A)
    inner = len(A[0])
    cols = len(B[0])
    if len(B) != inner:
        raise ValueError("Matrix dimension mismatch")
    out: list[list[tuple[int, ...]]] = []
    for i in range(rows):
        row: list[tuple[int, ...]] = []
        for j in range(cols):
            acc = F.zero()
            for t in range(inner):
                if not F.is_zero(A[i][t]) and not F.is_zero(B[t][j]):
                    acc = F.add(acc, F.mul(A[i][t], B[t][j]))
            row.append(acc)
        out.append(row)
    return out


def standard_basis_gf(F: GFpm, count: int) -> list[tuple[int, ...]]:
    if count < 1 or count > F.m:
        raise ValueError(f"Basis count {count} out of range 1..{F.m}")
    return [tuple(1 if i == j else 0 for j in range(F.m)) for i in range(count)]


def find_distinct_conjugacy_anchors(F: GFpm, ell: int) -> list[tuple[int, ...]]:
    """Find ell elements in F_{p^m}^* with pairwise distinct full norms N_m(a) in F_p^*."""
    if ell < 1 or ell > F.p - 1:
        raise ValueError(f"Cannot have {ell} distinct conjugacy classes over F_{F.p} (max {F.p - 1})")
    anchors: list[tuple[int, ...]] = [F.one()]
    seen_norms: set[int] = {1}
    if ell == 1:
        return anchors
    gen = F.gen()
    cur = gen
    for _ in range(1, F.order):
        nm = F.truncated_norm(cur, F.m)
        if any(nm[1:]):
            raise RuntimeError("Full norm must lie in base field F_p")
        if nm[0] not in seen_norms:
            seen_norms.add(nm[0])
            anchors.append(cur)
            if len(anchors) == ell:
                return anchors
        cur = F.mul(cur, gen)
    raise RuntimeError("Failed to locate required conjugacy anchors")


def lrs_generator_matrix(
    F: GFpm,
    anchors: list[tuple[int, ...]],
    blocks: list[list[tuple[int, ...]]],
    k: int,
) -> list[list[tuple[int, ...]]]:
    """Build exact k x n Linearized Reed-Solomon generator matrix G_{i,(r,j)} = N_i(a_r) sigma^i(beta_{r,j})."""
    if len(anchors) != len(blocks) or not anchors:
        raise ValueError("anchors and blocks must be non-empty of equal length")
    n = sum(len(b) for b in blocks)
    if k < 1 or k > n:
        raise ValueError(f"Invalid dimension k={k} for length n={n}")
    # Verify pairwise distinct conjugacy classes via full norms N_m(a_r)
    norms = [F.truncated_norm(a, F.m) for a in anchors]
    if len(set(norms)) != len(norms):
        raise ValueError("Anchors must represent distinct Frobenius conjugacy classes (distinct N_m)")
    rows: list[list[tuple[int, ...]]] = []
    for i in range(k):
        row: list[tuple[int, ...]] = []
        for a, betas in zip(anchors, blocks):
            na = F.truncated_norm(a, i)
            for b in betas:
                row.append(F.mul(na, F.frob(b, i)))
        rows.append(row)
    return rows


def frobenius_sum_dim(F: GFpm, G: list[list[tuple[int, ...]]], t: int) -> int:
    """Compute exact dim(Lambda_t(C)) = dim(C + C^[1] + ... + C^[t]) over F_{p^m}."""
    if t < 0:
        raise ValueError("Frobenius shift order t must be >= 0")
    stacked: list[list[tuple[int, ...]]] = []
    cur = G
    for _ in range(t + 1):
        stacked.extend(cur)
        cur = [[F.frob(v) for v in row] for row in cur]
    return matrix_rank_gf(F, stacked)


def overbeck_lrs_upper_bound(n: int, ell: int, k: int, t: int) -> int:
    """Exact theoretical Overbeck-LRS upper bound on dim(Lambda_t(C)) for ell-block LRS."""
    if t < ell:
        return min(n, (t + 1) * k)
    if k < ell:
        return min(n, (t + 1) * k)
    return min(n, ell * k + ell * (t - ell + 1))


def overbeck_lrs_defect(n: int, ell: int, k: int, t: int) -> int:
    """Exact rank defect min(n, (t+1)k) - overbeck_lrs_upper_bound(n, ell, k, t)."""
    return min(n, (t + 1) * k) - overbeck_lrs_upper_bound(n, ell, k, t)


def shorten_generator_matrix(
    F: GFpm, G: list[list[tuple[int, ...]]], drop_cols: list[int]
) -> list[list[tuple[int, ...]]]:
    """Exact shortening of code C = rowspace(G) at drop_cols over F_{p^m}."""
    k = len(G)
    n = len(G[0])
    drop_set = set(drop_cols)
    if any(c < 0 or c >= n for c in drop_set):
        raise ValueError("drop_cols index out of range")
    sub = [[G[r][c] for r in range(k)] for c in sorted(drop_set)]
    M = [list(row) for row in sub]
    rows = len(M)
    pivs: list[int] = []
    r = 0
    for c in range(k):
        piv = None
        for i in range(r, rows):
            if not F.is_zero(M[i][c]):
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv_p = F.inv(M[r][c])
        M[r] = [F.mul(v, inv_p) for v in M[r]]
        for i in range(rows):
            if i != r and not F.is_zero(M[i][c]):
                fac = M[i][c]
                M[i] = [F.sub(M[i][j], F.mul(fac, M[r][j])) for j in range(k)]
        pivs.append(c)
        r += 1
    free = [c for c in range(k) if c not in pivs]
    keep = [j for j in range(n) if j not in drop_set]
    out: list[list[tuple[int, ...]]] = []
    for fc in free:
        u = [F.zero()] * k
        u[fc] = F.one()
        for row_idx, pc in enumerate(pivs):
            u[pc] = F.sub(F.zero(), M[row_idx][fc])
        vec: list[tuple[int, ...]] = []
        for j in keep:
            acc = F.zero()
            for i in range(k):
                if not F.is_zero(u[i]):
                    acc = F.add(acc, F.mul(u[i], G[i][j]))
            vec.append(acc)
        out.append(vec)
    return out


def build_basefield_block_isometry(F: GFpm, block_sizes: list[int]) -> list[list[tuple[int, ...]]]:
    """Construct a deterministic invertible block-diagonal F_p-linear isometry P in GL_{n_1}(F_p) x ... x GL_{n_ell}(F_p)."""
    n = sum(block_sizes)
    P = [[F.zero() for _ in range(n)] for _ in range(n)]
    offset = 0
    for sz in block_sizes:
        # Upper-triangular unipotent + cyclic shift over F_p (det = +-1, invertible, fixed by sigma!)
        for i in range(sz):
            P[offset + i][offset + ((i + 1) % sz)] = F.one()
            if i + 2 < sz:
                P[offset + i][offset + ((i + 2) % sz)] = F.scalar(1)
        # Ensure invertibility by using clean invertible companion/triangular block: I + superdiagonal
        for i in range(sz):
            for j in range(sz):
                P[offset + i][offset + j] = F.zero()
        for i in range(sz):
            P[offset + i][offset + i] = F.one()
            if i + 1 < sz:
                P[offset + i][offset + i + 1] = F.one()
        if sz >= 2:
            P[offset + sz - 1][offset] = F.scalar(F.p - 1) if F.p > 2 else F.zero()
        offset += sz
    if matrix_rank_gf(F, P) != n:
        # Fallback pure upper unitriangular (always det = 1!)
        P = [[F.zero() for _ in range(n)] for _ in range(n)]
        offset = 0
        for sz in block_sizes:
            for i in range(sz):
                P[offset + i][offset + i] = F.one()
                if i + 1 < sz:
                    P[offset + i][offset + i + 1] = F.one()
            offset += sz
    return P


def build_extension_scrambler(F: GFpm, k: int) -> list[list[tuple[int, ...]]]:
    """Deterministic invertible S in GL_k(F_{p^m}) with non-basefield extension entries."""
    S = [[F.zero() for _ in range(k)] for _ in range(k)]
    gen = F.gen()
    for i in range(k):
        S[i][i] = F.one()
        for j in range(i + 1, k):
            S[i][j] = F.pow(gen, i + j + 1)
    assert matrix_rank_gf(F, S) == k
    return S


def lrs_overbeck_cert(
    p: int,
    mod: tuple[int, ...],
    ell: int,
    block_sizes: list[int],
    k: int,
    max_t: int,
    scramble: bool = True,
) -> dict[str, Any]:
    """Generate an exact finite-field certificate of Overbeck-LRS Frobenius-shift rank profile."""
    F = GFpm(p, mod)
    anchors = find_distinct_conjugacy_anchors(F, ell)
    blocks = [standard_basis_gf(F, sz) for sz in block_sizes]
    n = sum(block_sizes)
    G = lrs_generator_matrix(F, anchors, blocks, k)
    rank_G = matrix_rank_gf(F, G)
    if rank_G != k:
        raise RuntimeError(f"LRS generator matrix rank {rank_G} != {k}")

    profile = [frobenius_sum_dim(F, G, t) for t in range(max_t + 1)]
    bounds = [overbeck_lrs_upper_bound(n, ell, k, t) for t in range(max_t + 1)]
    random_expected = [min(n, (t + 1) * k) for t in range(max_t + 1)]
    defects = [random_expected[t] - profile[t] for t in range(max_t + 1)]
    for t in range(max_t + 1):
        if profile[t] > bounds[t]:
            raise RuntimeError(f"Observed dim {profile[t]} exceeds bound {bounds[t]} at t={t}")

    scramble_invariant = True
    if scramble:
        S = build_extension_scrambler(F, k)
        P = build_basefield_block_isometry(F, block_sizes)
        # Verify sigma(P) == P entrywise
        for r_idx in range(n):
            for c_idx in range(n):
                if F.frob(P[r_idx][c_idx]) != P[r_idx][c_idx]:
                    raise RuntimeError("Base-field isometry P not fixed by Frobenius")
        G_pub = matrix_mul_gf(F, matrix_mul_gf(F, S, G), P)
        pub_profile = [frobenius_sum_dim(F, G_pub, t) for t in range(max_t + 1)]
        scramble_invariant = pub_profile == profile
        if not scramble_invariant:
            raise RuntimeError("Scrambling broke Frobenius-shift rank invariance!")

    d_sr_singleton = n - k + 1
    rate_q = Fraction(k, n)
    return {
        "field": f"GF({p}^{F.m})",
        "p": p,
        "m": F.m,
        "modulus_coeffs_asc": list(mod),
        "ell": ell,
        "block_sizes": block_sizes,
        "n": n,
        "k": k,
        "rate_exact": [rate_q.numerator, rate_q.denominator],
        "singleton_sum_rank_distance": d_sr_singleton,
        "anchor_full_norms": [F.truncated_norm(a, F.m)[0] for a in anchors],
        "lambda_t_dims": profile,
        "theoretical_upper_bounds": bounds,
        "random_code_dims": random_expected,
        "overbeck_defects": defects,
        "distinguished_from_random": any(d > 0 for d in defects),
        "public_key_scramble_invariant": scramble_invariant,
    }


def lrs_shortening_collapse_cert(
    p: int,
    mod: tuple[int, ...],
    ell: int,
    block_sizes: list[int],
    k: int,
    drop_cols: list[int],
) -> dict[str, Any]:
    """Certify shortening-induced block collapse triggering single-step t=1 Overbeck distinguisher."""
    F = GFpm(p, mod)
    anchors = find_distinct_conjugacy_anchors(F, ell)
    blocks = [standard_basis_gf(F, sz) for sz in block_sizes]
    n = sum(block_sizes)
    G = lrs_generator_matrix(F, anchors, blocks, k)
    dim_orig_t1 = frobenius_sum_dim(F, G, 1)

    G_sh = shorten_generator_matrix(F, G, drop_cols)
    n_sh = n - len(set(drop_cols))
    k_sh = matrix_rank_gf(F, G_sh)
    dim_sh_t1 = frobenius_sum_dim(F, G_sh, 1)
    rand_sh_t1 = min(n_sh, 2 * k_sh)
    defect_sh_t1 = rand_sh_t1 - dim_sh_t1

    # Compute residual block sizes
    drop_set = set(drop_cols)
    rem_blocks: list[int] = []
    off = 0
    for sz in block_sizes:
        rem_blocks.append(sum(1 for idx in range(off, off + sz) if idx not in drop_set))
        off += sz
    max_blk = max(rem_blocks)
    delta_other = sum(rem_blocks) - max_blk
    collapse_bound = min(n_sh, min(max_blk, k_sh + 1) + delta_other)
    if dim_sh_t1 > collapse_bound:
        raise RuntimeError(f"Shortened dim {dim_sh_t1} exceeded collapse bound {collapse_bound}")

    return {
        "field": f"GF({p}^{F.m})",
        "p": p,
        "m": F.m,
        "ell": ell,
        "orig_n": n,
        "orig_k": k,
        "orig_lambda1_dim": dim_orig_t1,
        "shortened_cols_count": len(drop_set),
        "shortened_n": n_sh,
        "shortened_k": k_sh,
        "residual_block_sizes": rem_blocks,
        "delta_other_blocks": delta_other,
        "shortened_lambda1_dim": dim_sh_t1,
        "collapse_upper_bound": collapse_bound,
        "random_lambda1_dim": rand_sh_t1,
        "t1_overbeck_defect": defect_sh_t1,
        "single_step_distinguished": defect_sh_t1 > 0,
    }


def norm_cocycle_and_shift_cert(p: int, mod: tuple[int, ...], i: int, j: int) -> dict[str, Any]:
    """Certify exact skew-norm cocycle N_{i+j}(a) = N_i(a)*sigma^i(N_j(a)) and Frobenius shift identity."""
    F = GFpm(p, mod)
    a = F.gen()
    lhs = F.truncated_norm(a, i + j)
    rhs = F.mul(F.truncated_norm(a, i), F.frob(F.truncated_norm(a, j), i))
    if lhs != rhs:
        raise RuntimeError("Norm cocycle identity failed")
    # Shift identity: sigma(N_i(a)) * a == N_{i+1}(a)
    shift_lhs = F.mul(F.frob(F.truncated_norm(a, i)), a)
    shift_rhs = F.truncated_norm(a, i + 1)
    if shift_lhs != shift_rhs:
        raise RuntimeError("Norm Frobenius shift identity failed")
    # Also verify sigma^m(a) == a
    frob_m_id = F.frob(a, F.m) == a
    if not frob_m_id:
        raise RuntimeError("Frobenius order m identity failed")
    return {
        "field": f"GF({p}^{F.m})",
        "i": i,
        "j": j,
        "anchor_poly": list(a),
        "N_i_plus_j": list(lhs),
        "cocycle_exact": lhs == rhs,
        "shift_identity_exact": shift_lhs == shift_rhs,
        "frob_order_m_exact": frob_m_id,
    }


def canonical_json_sha256(payload: dict[str, Any]) -> str:
    raw = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()
