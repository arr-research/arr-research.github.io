# Reproducibility package

Install the declared Python dependencies from the record root:

```text
python -m pip install -r src/replay/requirements.txt
```

Run both bounded deterministic checks:

```text
powershell -ExecutionPolicy Bypass -File src/replay/replay_all.ps1
```

Regenerate the figure with:

```text
python src/manuscript/generate_semiclassical_figure.py
```

The frozen JSON files record the audited author run. Platform and library
differences may alter final floating-point digits or line endings; acceptance
is based on the analytic tolerances implemented by the scripts, not byte
identity with the frozen JSON. These programs diagnose constants and code
paths. They do not formally certify the analytic theorems.
