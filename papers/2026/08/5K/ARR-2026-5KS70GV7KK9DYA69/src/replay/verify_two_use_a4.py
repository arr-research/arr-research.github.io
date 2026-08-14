"""Fail-closed light verifier for TWO_USE_A4_AUDIT.md.

No SDP and no random sampling are used.  The script reconstructs all 24
quaternion echoes at q=1/2, checks the exact spectral formula, and checks the
closed Bell and optimized-parallel fixtures.
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np


TOL = 2.0e-11
VERTICES = np.asarray(
    [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], dtype=float
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def q_of_t(t: float) -> float:
    u = t * t
    return (u - 1.0) * (u**3 + 13.0 * u**2 + 35.0 * u + 79.0) / (u + 3.0) ** 4


def bisect_q(target: float, lo: float, hi: float) -> float:
    flo = q_of_t(lo) - target
    fhi = q_of_t(hi) - target
    require(math.isfinite(flo) and math.isfinite(fhi), "non-finite bracket")
    require(flo < 0.0 < fhi, "invalid monotone q bracket")
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if q_of_t(mid) < target:
            lo = mid
        else:
            hi = mid
    root = 0.5 * (lo + hi)
    require(abs(q_of_t(root) - target) < 5.0e-15, "q root did not close")
    return root


def qmul(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    a, u = left[0], left[1:]
    b, v = right[0], right[1:]
    return np.r_[a * b - u @ v, a * v + b * u + np.cross(u, v)]


def word(order: tuple[int, ...], sign: int, c: float, x: float) -> np.ndarray:
    out = np.asarray([1.0, 0.0, 0.0, 0.0])
    for label in order:
        out = qmul(np.r_[c, sign * x * VERTICES[label]], out)
    return out


def parity(order: tuple[int, ...]) -> int:
    return sum(
        order[i] > order[j]
        for i in range(4)
        for j in range(i + 1, 4)
    ) % 2


def echoes(t: float) -> tuple[list[tuple[int, ...]], np.ndarray]:
    x = 1.0 / math.sqrt(t * t + 3.0)
    c = t * x
    orders = list(itertools.permutations(range(4)))
    values = []
    for order in orders:
        values.append(qmul(word(order, +1, c, x), word(order, -1, c, x)))
    out = np.asarray(values)
    require(np.max(np.abs(np.linalg.norm(out, axis=1) - 1.0)) < TOL, "non-unit echo")
    require(np.ptp(out[:, 0]) < TOL, "trace coordinate depends on order")
    return orders, out


def symmetric_square_row(quaternion: np.ndarray) -> np.ndarray:
    q = quaternion[0]
    v = quaternion[1:]
    w = np.r_[q, -1j * v]
    return np.asarray(
        [
            w[0] ** 2,
            math.sqrt(2.0) * w[0] * w[1],
            math.sqrt(2.0) * w[0] * w[2],
            math.sqrt(2.0) * w[0] * w[3],
            w[1] ** 2,
            w[2] ** 2,
            w[3] ** 2,
            math.sqrt(2.0) * w[1] * w[2],
            math.sqrt(2.0) * w[1] * w[3],
            math.sqrt(2.0) * w[2] * w[3],
        ],
        dtype=complex,
    )


def e_plus(t: float) -> float:
    return (
        32768.0
        * (t - 1.0) ** 8
        * (t + 1.0) ** 2
        * (t**5 - t**4 + 8.0 * t**3 - 8.0 * t**2 + 15.0 * t + 1.0) ** 2
        / (t * t + 3.0) ** 16
    )


def e_minus(t: float) -> float:
    return (
        32768.0
        * (t - 1.0) ** 2
        * (t + 1.0) ** 8
        * (t**5 + t**4 + 8.0 * t**3 + 8.0 * t**2 + 15.0 * t - 1.0) ** 2
        / (t * t + 3.0) ** 16
    )


def seed_energy(v: np.ndarray) -> float:
    return 2.0 * sum(v[i] ** 2 * v[j] ** 2 for i in range(3) for j in range(i + 1, 3))


def main() -> None:
    t = bisect_q(0.5, 1.0, 2.0)
    orders, values = echoes(t)
    q = float(values[0, 0])
    r2 = 1.0 - q * q
    require(abs(q - 0.5) < TOL, "wrong q=1/2 fixture")

    ep, em = e_plus(t), e_minus(t)
    for p, expected in ((0, ep), (1, em)):
        index = next(i for i, order in enumerate(orders) if parity(order) == p)
        require(
            abs(seed_energy(values[index, 1:]) - expected) < TOL,
            f"parity-{p} energy formula failed",
        )

    rows = np.asarray([symmetric_square_row(value) for value in values])
    frame = rows.conj().T @ rows / 24.0
    eig = np.linalg.eigvalsh(frame)
    total = 2.0 * r2 * r2 / 3.0
    dp, dm = total - ep, total - em
    expected_eig = np.sort(
        np.asarray(
            [
                0.0,
                q**4 + r2**2 / 3.0,
                *([(dp + dm) / 4.0] * 2),
                *([2.0 * q * q * r2 / 3.0] * 3),
                *([(ep + em) / 6.0] * 3),
            ]
        )
    )
    require(np.max(np.abs(eig - expected_eig)) < TOL, "two-copy spectrum failed")
    require(np.sum(eig > TOL) == 9, "generic rank is not nine")
    require(abs(np.sum(eig) - 1.0) < TOL, "frame trace is not one")

    target_e = 2.0 * r2 * r2 / 5.0
    require(min(ep, em) < target_e < max(ep, em), "q=1/2 clamp is not interior")
    ec = min(max(target_e, min(ep, em)), max(ep, em))
    dc = total - ec
    h_mix = math.sqrt(2.0 * dc) + math.sqrt(3.0 * ec)
    p_bell = (
        math.sqrt(q**4 + r2**2 / 3.0)
        + math.sqrt(6.0) * abs(q) * math.sqrt(r2)
        + h_mix
    ) ** 2 / 24.0
    p_bell_exact = (2.0 + 3.0 * math.sqrt(2.0) + math.sqrt(30.0)) ** 2 / 384.0
    require(abs(p_bell - p_bell_exact) < TOL, "Bell x Bell fixture failed")

    h = (4.0 * q * q - 1.0) ** 2 / 9.0
    k = math.sqrt(8.0) * abs(q) * math.sqrt(r2) + 2.0 * h_mix / math.sqrt(3.0)
    require(h * k * k <= (1.0 - h) ** 2, "wrong optimized-input branch")
    p_parallel = (1.0 + k * k / (1.0 - h)) / 24.0
    a_star = 1.0 - k * k / ((1.0 - h) * (k * k + 1.0 - h))
    require(abs(p_parallel - (5.0 + math.sqrt(15.0)) / 24.0) < TOL, "parallel fixture failed")
    require(abs(a_star - (5.0 - math.sqrt(15.0)) / 10.0) < TOL, "a_star fixture failed")
    require(p_bell < p_parallel < 3.0 / 8.0, "strict hierarchy failed")

    # No real q^2 can make the generic rank-nine frame tight.
    require((-4.0) ** 2 - 4.0 * 6.0 * 1.0 < 0.0, "tightness discriminant check failed")
    print("PASS two-use A4 audit")
    print(f"t={t:.16g}  P_Bell2={p_bell:.15g}  P_parallel={p_parallel:.15g}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # fail closed with a nonzero status
        print(f"FAIL: {exc}", file=sys.stderr)
        raise

