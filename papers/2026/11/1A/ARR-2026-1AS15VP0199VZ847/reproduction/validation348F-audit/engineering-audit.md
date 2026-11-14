# Validation348F: sealed B1 engineering delta audit

Verdict: **STATIC_DELTA_ACCEPTED_FOR_LINUX_EXECUTION**. The specific B1 defect identified in the frozen348E audit is repaired in the inspected348F source. No blocking defect was found in this delta. This is permission to proceed within the already authorized Linux validation workflow, not an observed execution success. Actual sentinel regressions, current preflight and actual-return validation remain unexecuted in the evidence reviewed.

## Exact subject and separation

The subject is `validation348F-preparation/MANIFEST-F.json`, SHA-256 `9fd5c3fa005077e6c4594e6d1cc6f3091f89035bcd2b6139ad21efccbd886a5f`. All62 manifest entries matched their declared byte lengths and SHA-256 values. The current outer wrapper is `03-preflight.py`,6006 bytes, SHA-256 `c5dfa91061932f5b44d73ca6bec93a2924883e5b96de117e23a0b8a8ae3d2a7f`. The current notebook is `validation348F-unexecuted.ipynb`,209872 bytes, SHA-256 `a2f54dd7998d258159ab11b7d24c38090801eba03e35b0f784765cee689a31b6`.

This is a separate engineering audit of the B1 repair, not another scientific assessment. No PDF page, mathematical proof, score, publication decision or intake decision was reassessed. The prior348D scientific review and the original348E HOLD verdict remain historical records. Neither is replaced by this report.

The current F manifest is authoritative for this subject. F deliberately retains the old E manifest and notebook as historical bytes. The old manifest therefore does not describe the new F wrapper. This is explicit provenance separation, not evidence that the F manifest failed. The F notebook retains an E title and E runtime names; its actual code cells and this subject hash identify the repaired notebook. Execute the exact F notebook, not the retained historical E notebook.

## B1 finding and repair

The previous outer `observed_child` wrote directly to the final `.exit` pathname. This bypassed the required closed temporary file, integer verification and atomic publication. The former audit did not claim that a false PASS had actually occurred.

The new `publish_exit` (03-preflight.py lines7–23) accepts only an actual Python `int`, excluding booleans. It writes the observed decimal value and newline to a fresh, exclusively created `.exit.tmp` in the same directory; flushes and fsyncs it; leaves the context manager, closing the file; then reads the closed bytes. Explicit full-match and numeric-equality checks bind those bytes to the observed return code. Nonzero and negative return codes are preserved rather than normalized to success.

Publication uses libc `renameat2` with the no-replace flag. The declared ctypes parameter and return types match the syscall interface. The preexisting-final check is supplemented by no-replace publication, so a final file created between the check and rename is not overwritten. A successful publication is followed by an exact final-byte readback and a check that the temporary pathname disappeared. The Linux manual specifies the no-overwrite behavior and that filesystem support is required. This is an API-based static inference, not a claim to have observed this kernel/filesystem execute it. [Linux rename manual](https://man7.org/linux/man-pages/man2/rename.2.html)

The race regression expects `FileExistsError`; the explicit `OSError(errno,...)` construction for EEXIST is consistent with Python's documented exception mapping. [Python built-in exceptions](https://docs.python.org/3/library/exceptions.html#FileExistsError)

`observed_child` calls this same helper only once a child return code is available, including after timeout kill-and-wait. It then binds the final sentinel bytes into its observation. The code does not substitute a desired return code, use an assertion as an acceptance condition, or fall back to direct final-file writing if the atomic operation fails. Unsupported libc/kernel/filesystem behavior raises an error and stops the cell.

The claim is atomic namespace publication and no overwrite, not guaranteed durability across power loss. No directory fsync is provided or claimed. No repair is needed for the narrower B1 requirement on that basis.

## Regressions and integration

The same `SENTINEL_SOURCE` string is installed in the notebook and supplied to both regression subprocesses. Six explicit scenarios are prepared:

1. Successful zero exit produces exactly `0` plus newline.
2. Nonzero exit7 produces exactly `7` plus newline.
3. A duplicate final path raises and preserves the earlier7.
4. A deliberate exception immediately before publication leaves no final path and retains the validated temporary0.
5. A final path created at the prepublication hook causes no-replace failure and preserves9.
6. Boolean input is rejected without publishing a final path.

The harness uses explicit raises and checks, including six distinct labels, rather than `assert`. It runs first in normal mode, then with `-O`, and requires actual child exit0, no timeout and no recorded error before parsing the count. These are six scenarios per mode, not twelve different scenarios. They are prepared tests, not observed passing tests. The interruption hook tests the exact boundary where the earlier direct-write defect mattered; it does not exhaustively simulate arbitrary hardware failures or every kill instant.

Both sentinel regression children themselves are recorded through the repaired outer wrapper on ROOT. Only after both succeed does the original current preflight run. `06-actual-validation.py` is byte-identical to E and calls the same `observed_child` for normal and optimized actual-return checks. It retains explicit success predicates and writes its summary with exclusive creation. Existing export selection includes the new sentinel `.stdout`, `.stderr`, `.exit` and `.observation.json` files automatically. It does not convert absent results into successes.

## Identity and inherited conclusions

All59 original E preparation entries still match the original E manifest. Among the inherited F files, only03-preflight.py differs from E. The F notebook contains one markdown cell and seven code cells; all seven code-cell sources exactly equal the respective F standalone source files, with null execution counts and empty outputs. Comparing code cells against the historical E notebook shows only the third code cell changed.

The materializer and all17 embedded/runtime payloads are unchanged by byte identity, as are the validator, its regression tests, the current preflight, caller,28 raw transport chunks, assembly and export cells. Thus the previous static conclusions on the exact `tex-version` probe versus four exact compilation names, old5/58 versus new6/62 preflight separation, original raw archive binding, exclusive outputs and absence of assertion-based acceptance are not altered by this wrapper repair. Their positive static status is inherited through verified bytes; their pending execution status is also inherited.

The original raw production ZIP identity remains `b74ab3e6e1d349aafe5ed42d984270e0ae1ee86ac158a1d9738dc6274f1b6e4b`. Neither production regeneration nor PDF assessment is introduced. The exact PDF identity remains bound by the unchanged caller: SHA-256 `9f5d88b88321ca9ddc2afd284861a217cde0a37057362c1962a8cf988c42b29a`,345832 bytes,10 pages. This paragraph is a structural identity statement, not a mathematical judgment.

The frozen E audit manifest remains SHA-256 `dca02191b20fd8e8c3dad53d085c1461b0d65a0475f82db30324d49aaff394c9`. Its verdict is not edited or retrospectively changed to a pass.

## All remaining objections and limits

There are no blocking source findings within this delta. The following limits remain material:

- **L1, actual execution pending:** neither six sentinel scenarios in both modes, nor the current6 accepted/62 rejected preflight in both modes, nor both actual-return validations have been observed here. No PASS, validated return or runtime closure is asserted. Retain actual stdout/stderr, exit sentinels, observations, current preflight reports and actual summaries before making those claims.
- **L2, platform dependency:** actual Linux libc/kernel/filesystem must support the no-replace rename. Unsupported behavior fails closed. A static review cannot replace that actual run.
- **L3, failure capture:** if the publisher itself raises inside `observed_child`'s finally block, the later observation JSON is not written. The existing export includes standard output/error and any published exit but excludes `.exit.tmp` and the notebook traceback. This does not yield acceptance, but such a failure requires separately retaining the actual traceback and remaining temporary file before cleanup. The source does not promise complete native recovery of every infrastructure crash. This is a nonblocking evidence limitation for a run that must stop on failure.
- **L4, scope and identity:** CPU/high-RAM ownership, UI activity and runtime disconnection require actual observation. The parent's statement that the uploaded E notebook is disconnected is supplied context, not independently verified here. A new audit context does not establish statistical, technical or provider independence. The requested Astra/high label is not backend model/effort attestation.

## Method and context

The reviewer received the parent assignment verbatim in the adjacent receipt, read the full F repair note, current wrapper, old/new delta, current F manifest, full actual caller and export, and inspected all manifest-bound bytes and notebook code-cell sources. The previous E audit and governance were already in this same reviewer context. This is deliberately a continuation by the engineering auditor who identified B1, with full disclosure of that context; it is not a blind or independent second sample.

Checks were read-only PowerShell/.NET hashes, byte lengths, JSON parsing, source reading and diff inspection, plus primary API documentation. No candidate Python import, syntax-check, subprocess, regression, mathematical execution, Lean, build or PDF generation was run on Windows. A reviewer-side notebook checker initially treated the markdown title cell as code; it stopped, was corrected to select code cells, and then verified all seven. That was an inspection-harness mistake, not a candidate failure, and is recorded in the static evidence.

All work products were prepared in a dedicated C staging folder, then retained by verified hash in D. Frozen inputs were not edited. This report supports proceeding to the actual authorized Linux validation with the exact repaired subject, and no broader conclusion.
