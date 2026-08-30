# Exact replay

Requirements: Python 3.10 or later; standard library only.

```text
python -I verify_extremal_tax.py --max-d 20 --output verification.recheck.json
```

The committed `verification.json` is the output from the frozen manuscript run.
The script writes atomically, uses explicit checks, and refuses optimized Python.
It is a finite algebra/index audit rather than a formal proof of the universal
theorem or of the imported Horn inequalities.
