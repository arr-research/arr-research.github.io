# Corrected accumulator audit

The initially registered `[12,16)` artifact was identically zero because
`arb_mat +=` was applied to a loop variable rather than through the
`full_bands` list.  That preliminary certificate was rejected before release.

The producer now assigns through the list, uses cache format 3, encloses the
binary64 centre conversion in every radius, exports scalar upper bounds
outward, rejects malformed caches and every explicit nonempty band with
nonpositive lower trace, and has focused regression fixtures. A corrected
512-bit replay generated nonzero degreewise
Grams for degrees 12 through 23.  The corresponding interval Schur
adjudication closes both parity sectors with 78 positive and zero unresolved
directions.  The paper and release hashes refer only to these corrected
objects; the zero-band artifact is not included as evidence.
