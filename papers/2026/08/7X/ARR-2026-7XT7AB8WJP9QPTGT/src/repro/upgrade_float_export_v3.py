"""Upgrade certified component caches to the centred-binary64 export format.

The mathematical Arb balls are unchanged.  For every exported matrix entry we
add one ulp of the stored midpoint to its radius, then round the addition
outwards.  This encloses the displacement between the high-precision Arb
centre and the binary64 centre stored in the NPZ file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np

CANONICAL_PREDECESSORS = {
    "third-window-thirteen-block":
        "c5cff9fba1684a5822e1544a2a96f91aa843d9b0074e239df6e81a51875ecad4",
    "third-window-near-tail-bands":
        "c6ad7afe1a0094b1404a240967e04f165a7ce7ce86dacc88872fed69a3b72d66",
}


def upgrade(source: Path, target: Path) -> None:
    source_digest = hashlib.sha256(source.read_bytes()).hexdigest()
    with np.load(source, allow_pickle=False) as payload:
        arrays = {name: np.array(payload[name], copy=True) for name in payload.files}
    metadata = json.loads(str(arrays["metadata"].item()))
    if int(metadata.get("float_export_version", 1)) >= 2:
        raise ValueError("cache already uses centred-binary64 export radii")
    architecture = metadata.get("architecture")
    allowed = {
        "third-window-thirteen-block": {"format": 1},
        "third-window-near-tail-bands": {"format": 2, "accumulator_version": 2},
    }
    if architecture not in allowed or any(
        metadata.get(key) != value for key, value in allowed[architecture].items()
    ):
        raise ValueError("source cache schema is not an allowlisted v3 predecessor")
    if source_digest != CANONICAL_PREDECESSORS[architecture]:
        raise ValueError("source cache hash is not the canonical predecessor")
    metadata["format"] = 3
    metadata["accumulator_version"] = 2
    metadata["float_export_version"] = 2
    arrays["metadata"] = np.array(json.dumps(metadata, sort_keys=True))

    upgraded = 0
    radius_names = [name for name in arrays if name.endswith("_radius")]
    if not radius_names:
        raise ValueError("source cache contains no exported radius arrays")
    for radius_name in radius_names:
        midpoint_name = radius_name.removesuffix("_radius") + "_midpoint"
        if midpoint_name not in arrays:
            raise KeyError(f"missing midpoint partner for {radius_name}")
        midpoint = np.asarray(arrays[midpoint_name], dtype=float)
        radius = np.asarray(arrays[radius_name], dtype=float)
        if (
            midpoint.shape != radius.shape
            or midpoint.shape != (78, 78)
            or not np.isfinite(midpoint).all()
            or not np.isfinite(radius).all()
            or np.any(radius < 0)
        ):
            raise ValueError(f"malformed exported pair {midpoint_name}/{radius_name}")
        ulp = np.abs(np.spacing(midpoint))
        intrinsic_upper = np.nextafter(radius, np.inf)
        arrays[radius_name] = np.nextafter(intrinsic_upper + ulp, np.inf)
        upgraded += radius.size

    if architecture == "third-window-near-tail-bands":
        for radius_name in radius_names:
            stem = radius_name.removesuffix("_radius")
            if not stem.startswith("band_"):
                continue
            midpoint = arrays[stem + "_midpoint"]
            radius = arrays[radius_name]
            if float(np.trace(midpoint - radius)) <= 0:
                raise ValueError(f"explicit band {stem} has nonpositive lower trace")
    else:
        half_width = Fraction(str(metadata["half_width"]))
        maximum_power = int(metadata["maximum_smooth_power"])
        ratio = 2 * half_width / 3
        h_tail = Fraction(2, 3) * ratio ** (maximum_power + 1) / (1 - ratio)
        first_even = maximum_power + 1
        if first_even % 2:
            first_even += 1
        first_term = Fraction(2) * half_width**first_even / math.factorial(first_even)
        next_ratio = half_width**2 / ((first_even + 1) * (first_even + 2))
        exact_smooth = 2 * half_width * (h_tail + first_term / (1 - next_ratio))
        arrays["smooth_remainder"] = np.array(
            np.nextafter(float(exact_smooth), np.inf)
        )

    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    with temporary.open("wb") as stream:
        np.savez_compressed(stream, **arrays)
    temporary.replace(target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"UPGRADED {upgraded} radii -> {target}")
    print(f"SHA256 {digest}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    args = parser.parse_args()
    upgrade(args.source, args.target)


if __name__ == "__main__":
    main()
