# Exact reproduction protocol

This directory accompanies manuscript version 0.6,
`Cellulation-Independent Boundary Gauge Averaging and Sharp Class-Sector Gaps
in Two-Dimensional Yang--Mills`.

The release archive contains the PDF, its LaTeX source, this reproduction
directory, the exact Git history bundle for the two cited repository commits,
the pinned Lake manifest/toolchain, Python requirements, and `MANIFEST.sha256`.
No manual root-import edit is required.

## Numerical replay

```powershell
python -m pip install -r requirements.txt
python replay.py
```

Expected terminal line: `REPLAY: PASS`.

## New Lean endpoint

Run the self-contained driver from this directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\reproduce.ps1
```

The driver clones from the included Git bundle, checks out the full hashes
`05c4ec316cb9aa295416670a2578b1c2e77e1c36` and
`6dbb8cebc18ab2d65b6ae24af5216347c476df3f` in separate directories, copies
the companion module into the correct namespace, and invokes Lean directly.
It does not mutate a user's existing clone.

Observed in the manuscript build environment:

```text
Build completed successfully (2817 jobs).
The four new endpoints depend only on:
  [propext, Classical.choice, Quot.sound]
Boundary-conditioned branch build completed successfully (3097 jobs).
```

## Fixed-boundary physical disk endpoint

```powershell
git fetch origin agent/su2-boundary-conditioned-bridge
git checkout 6dbb8cebc18ab2d65b6ae24af5216347c476df3f
lake exe cache get
lake build Lean2dYangMills
```

The endpoint used by the paper is
`SU2BoundaryDiskCellulation.conditionedEdgeModelAmplitude_eq_heatKernel`.
The branch provenance identifies mathematical snapshot
`a1fbea97cbe673d383dbb4bc5e2a2fb70dbf190a`.

## Integrity

From the release root, verify every preserved file with:

```powershell
Get-Content MANIFEST.sha256 | ForEach-Object {
  $hash, $path = $_ -split '  ', 2
  if ((Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLower() -ne $hash) {
    throw "Hash mismatch: $path"
  }
}
```
