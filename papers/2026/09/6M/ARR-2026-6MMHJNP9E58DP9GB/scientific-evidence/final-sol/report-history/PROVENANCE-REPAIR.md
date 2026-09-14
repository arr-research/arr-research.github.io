# B4 final-sol provenance repair

- Recorded at: `2026-09-14T17:49:50Z`
- Scope: provenance reconstruction only; no scientific reassessment.
- Final report was not modified during this repair.

## Preserved byte versions

- `PREASSESSMENT.prior-04faa6c5.recovered.json`
  - SHA-256: `04faa6c59fccca33ce8cf996e984a8ae7686944b895349498aba03ea62a3de8f`
  - Recovery method: copied the current report and reversed the single recorded post-freeze `apply_patch`. The resulting SHA-256 exactly equals the runtime-captured pre-change hash, establishing byte-for-byte recovery.
- `PREASSESSMENT.current-c1f7eacf.json`
  - SHA-256: `c1f7eacfec03391f4e39c4c46e59e94b51041cf02af15633da22a4f525e64622`
  - This is a byte copy of the current `candidate-2/final-sol/PREASSESSMENT.json`.

## Exact change

Only `actual_logs` entry 2, field `utc`, changed:

```diff
-      "utc": "2026-09-14T17:30:03Z",
+      "utc": "2026-09-14T17:29:44Z",
```

The command and result fields, scientific assessment, recommendation, score, criteria, objections, sources, and disclosure are identical.

## Reason and chronology

After announcing the B4 report as frozen and complete, the reviewer checked the filesystem timestamp of `work/sol-preassessment/B4_two_planes_fold/paper-from-pdf.txt`, observed `LastWriteTimeUtc = 2026-09-14 17:29:44`, and patched the report's extraction-log UTC from the initially entered `17:30:03Z` to `17:29:44Z`. The correction was factually motivated but procedurally invalid because it occurred after the freeze notification. The exact inverse patch reproduces the prior runtime-captured hash, so the earlier bytes are recovered rather than inferred from scientific content.
