# Reproducing the canonical document

The canonical artifact is paper.pdf (12 pages,290841 bytes), SHA256
9f94b0619b37b052aaecfcdfafdc190e0965f950c31d52ef4f9932706d212538.
This is partial document-production reproduction, not executable mathematical
verification, independent peer review or independent-environment replication.

The complete original production archive and closed actual exits/logs are
under production/. The full returned archive preserves all original pages,
logs, raw manifest and both byte-identical clone PDFs. Parent all-page QA is
an involved observation; this base fabricator did not perform another visual
review. Two page6 overfull warnings3.07271pt/22.96838pt remain visible in the
original report and logs; text was fully visible. No claim of warning-free
or flawless typography is made. The own runtime was stopped and literal
backend inactivity captured separately. Billing units remain unknown.

Frozen-source and the exact Git tar archive retain research source
4d55ce32f54983977aac175f89e80e9cd0b64278, manuscript284B.tex and all85 input
source bindings. Ancestor A/B defects, corrections, full source/engineering
reports, original contexts and raw manifests are retained unchanged.

The preserved original owned-runtime runner intentionally checks that its
research branch HEAD equals the frozen SHA. It may refuse after the branch
advances; it is not an unconditional future one-click replay. Do not weaken
its actual historical gate or fabricate a new approval relay. For detached
document replay, extract the exact source tar (or obtain a detached checkout
at the SHA), verify its hashes, use Linux and the retained tool versions,
and work in papers/checkerboard-response. No network service/permission call
is needed merely to compile those already licensed source bytes.

Original environment: pdfTeX1.40.25 TeXLive2023/Debian; Poppler24.02.0;
Git2.43.0; Python3.13.18. Set SOURCE_DATE_EPOCH=1794500580,
FORCE_SOURCE_DATE=1, TZ=UTC and LC_ALL=C.UTF-8. Run the original document
command twice, with jobname manuscript284B:

    pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
      -jobname=manuscript284B \
      '\def\SourceCommit{4d55ce32f54983977aac175f89e80e9cd0b64278}\input{manuscript284B.tex}'

The identical SourceCommit injection, source epoch and source/tool versions
are necessary to compare bytes. Future environments may produce different
PDF bytes; such differences must be reported, not recast as verification.
The original run used two fresh clones in the SAME owned runtime,27 actual
zero-exit children, and no mathematical executable tests. Full source proofs
remain analytical. Any later exact-PDF assessment is a separate hash-bound
artifact and is not supplied by production success.
