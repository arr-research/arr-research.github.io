# Paper 20 figure

Generate the single manuscript figure with:

```powershell
python .\make_matroid_figure.py
```

Outputs:

* `paper20_matroidal_bayes_figure.png` — 300 dpi raster version;
* `paper20_matroidal_bayes_figure.pdf` — vector manuscript version;
* `SHA256SUMS.txt` — hashes of both generated artifacts.

The script fixes fonts, colors, canvas size, PDF timestamps, descriptive metadata, and
`SOURCE_DATE_EPOCH`.  It contains no random sampling and performs no optimization.

Panel A is **schematic**.  Positions show the rank-two trine phase flat and the orthogonal
Pauli-(X) coloop; they are not Euclidean distances or fidelities between Choi states.  Panel B
uses the exact prior fixture

```text
(p_phi0,p_phi1,p_phi2,p_X)=(0.30,0.30,0.30,0.10).
```

The total-span top-three relaxation is `0.90`; the Rado-matroid ceiling is `0.70`, attained by
the trine PGM completed on the orthogonal Choi direction and assigned to the (X) decision.
