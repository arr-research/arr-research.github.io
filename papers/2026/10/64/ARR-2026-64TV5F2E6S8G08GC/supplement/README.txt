REPRODUCIBLE SUPPLEMENT: UNIFORM TEN-SPIN CYCLE CLIQUE BLOWUPS

Python 3.12+ and SymPy 1.14.0. No network, credentials or other project
directories are required. Run: python -B verify_all.py
Run in a writable copy. The driver works in a temporary child directory,
reconstructs the symbolic matrices and all sign/tail/exception certificates,
and checks every stored exact field. Only timing fields are excluded from
comparisons. Successful checks print PASS and return zero. A failure raises
an exception. Full computations may take several minutes.

odd_cycle_ground_kernels.py supplies the classified occupation formulas.
Its standalone entry point delegates to verify_all.py; it no longer reads
the unbundled legacy cycle-ground-classification-checks.json file.
derive_initial_odd_block.py reconstructs the two symbolic matrices and their
leading determinants; its historical status string says signs not yet proved.
prove_odd_initial_large.py supplies those sign proofs and all 836 positive
coefficients. certify_initial_odd_small.py covers s=2,...,19, real infinite
k tails, all 42 exceptional integers, and k=2 separately. exact_inertia.py
is included locally; no external manuscript dependency remains.

check_compression.py and previous_own_odd.py are original code written by
Astra during the disclosed source audit. They reproduce three compression
cases and the positive seven-state witness using all 4335 occupations.
Their source provenance is recorded, not presented as an independent new
review of this paper. The previous_own_odd.py command-line audit entry point
belongs to an earlier audit and is NOT invoked by this driver; its functions
used by check_compression.py are self-contained.

Trials that fail are retained: ell=-255/256 for the seven-state target,
smaller initial blocks in s=4,s=7, and compression before the limiting
inertia stabilizes. The infinite theorem is supported by exact polynomial
certificates and the manuscript's combinatorial proof, not extrapolation.

Licenses: authored code Apache-2.0 (2026 Lluis Eriksson); manuscript and
text CC BY 4.0; generated certificate data and metadata CC0. Third-party
libraries and primary papers are cited, not bundled or relicensed.
No formal verification, optimal target size, global priority or manuscript
score is asserted by this package. A later assessment has its own PDF hash.
