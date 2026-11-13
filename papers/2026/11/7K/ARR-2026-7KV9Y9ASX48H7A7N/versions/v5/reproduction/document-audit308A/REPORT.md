# DELTA308 bounded source/document audit

Verdict: ACCEPT for L1-L3 on the exact referents below. No blocking objection was found. L4 and L5 are PENDING / NOT EXECUTED BY THIS AUDIT and are not accepted or waived. No score is assigned and no308 PDF quality claim is made.

## Frozen referents

Candidate source:8ac81a6f3f70aa552cc957d45abaf3f0fab90e65.
Registered judges:5a9fb36a4d4f9213d6a92b3702ce05e76726c2cc.
Base307:3edb8d656e511d3f81c147f54451fb57a84e5c38.
PR255:https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME/pull/255.
Actual capture command: gh pr view 255 --repo lluiseriksson/THE-ERIKSSON-PROGRAMME --json body,headRefOid.
Normalization: JSON-decode body; CRLF/CR to LF; remove all terminal LF; append exactly one LF; UTF-8 without BOM.
Observed body:932 bytes; SHA25611699d481580fbe81463ab62a926abf244f713875beb8e62726be9788a4a4c63.
Observed PR head matches the candidate.
manuscript308A.tex:73400 raw bytes; SHA256a58b4d312a5e8af6bd238d340b646332d4a62cf9ff423e6f09a9db67c4a5d5bb.
The registered judges bytes are unchanged and their commit is an ancestor of the candidate.

The scope is a separate involved document delta audit with retained300-307 context, including exposure to the historical299 assessment and its rating. No claim of a fresh blind context, known served backend, provider independence or human review is made.

## L1 — exact bounded change and mathematical preservation: ACCEPT

The complete textual diff contains exactly the three declared changes:
1. The first nonrendering identity comment changes DOCUMENT307 to DOCUMENT308.
2. The existing theorem title changes from “Finite cutoff below one” to “Finite cutoff with tail budget below one”.
3. The weighted-moment assumption sup_L E[r_L^s psi(r_L)] <= C < infinity moves from inline math into an unnumbered display. The surrounding phrase is line-broken to continue “with a nonnegative nondecreasing function ...”; the expression and quantifiers are unchanged.

An explicit three-substitution text transformation of the entire307 source equals the entire308 source exactly. This is stronger than checking selected diff lines. All19 proof environments are exactly text-identical; no line-ending normalization was needed for their comparison. Theorems retain their statements, constants, hypotheses, labels and order. No new equation number is introduced by the display, and no new mathematical conclusion is claimed.

The display still states a uniform weighted moment bound under the same uniform Boolean measure. Monotonicity of psi and its divergence at infinity remain the hypotheses yielding H(K)<=C/psi(K) when psi(K)>0. The text still distinguishes this weighted condition from an arbitrary Young function or Luxemburg norm. No premise was added, weakened, moved into a conclusion or lost.

The title clarification addresses the minor editorial ambiguity recorded in the full307 audit: “below one” now unmistakably describes tau, not the cutoff K>=1. It does not change the sufficient constant or the separate K<1 corollary. The normalized gap, same-family K>=1 endpoint, finite-prefix floor, strict budget slack in stable spikes, fixed-rho scope and distinction from physical/local/continuum claims remain unchanged.

Static reference checking still finds41 labels and49 ref/eqref uses, with no duplicate or unresolved label.17 citation uses resolve to11 bibliography entries. These are source checks, not TeX compilation or layout inspection. The source marker remains pending for actual pinned production. Moving the expression into display is an appropriate source-level repair attempt, but only new rendered output can establish that no margin or pagination defect remains.

## L2 — complete historical evidence, bytes and boundaries: ACCEPT

All727 SOURCE-INPUTS308 entries passed raw byte length and SHA256 verification and raw Git blob identity against the frozen tree. The inventory itself was separately bound as the728th archive member, rather than incorrectly self-hashed. The only tracked paper path outside the727-entry list is SOURCE-INPUTS308.json itself. The completed audit snapshot archive was read back and all728 member lengths/hashes matched.

Every one of the588 SOURCE-INPUTS307 entries remains byte-identical. Thus307 source, earlier source proofs, full historical299 assessment and all seven objections/author response, prior complete audits and nested exclusion disclosures remain unchanged. The308 change does not overwrite the historical307 rendering, source or analytical report.

All110 copied files from the two original307 audit directories match their D originals: the full document audit and the full production static engineering audit, including their reports, contexts, assignments, original manifests and supporting subjects. Their original manifests were retained unchanged. Complete raw reports, not only parent acceptance summaries, were considered. Their conditional or pending gates are not retroactively rewritten by later production.

All22 direct production307 evidence files match their original retained attempt files, including the original archive, canonical PDF, page16 image, raw transport logs/exits and runtime readback. The original production archive SHA256 is b078c2952867a56091a8ad452d788004348d4686d0e516a731cc8fbde11b2171. Its729 manifested raw members were individually rehashed and all matched. No failed layout output was regenerated or overwritten.

Inside that archive, clone-a.pdf, clone-b.pdf and the canonical manuscript307A.pdf each have478529 bytes and SHA256a4f73a3cd260051f602390500ca8edcf58766faeb30d9141b7b11fe316062ef7. Retained PDF metadata reports22 pages and all22 page PNGs are present. The27 recorded native commands have matching retained zero exit sentinels and no recorded timeout. These are checks of historical evidence, not a new build or an assertion that process logs mathematically prove truth.

Both final clone logs retain the same adverse line: an overfull hbox of13.91057pt at the weighted-moment paragraph. The parent record places the visible overflow on page16 and states all22 pages were inspected. This auditor verifies the record, log and exact image preservation, but does not impersonate the parent's all-page visual observation. Historical307 is therefore retained as a matching production result with a failed layout requirement, not as accepted final presentation.

The original outer return record reports actual allocation/execution/download/release exit0. The preserved release output states session termination; the separate later readback states no active sessions. The earlier parent-return-validation JSON still has visual review false and backend readback pending, whereas the later visual-finding record states completed inspection and inactive readback. This is a preserved sequence of records, not a contradiction requiring history to be erased. This audit queries no live runtime and certifies no present-time global runtime state.

No numerical307 assessment was initiated according to the supplied assignment and retained parent finding; the prepared packet remained unused. The audit does not inspect or invoke another chat to establish this and does not claim an independent platform-wide negative proof. No score appears to transfer to308.

No new third-party fulltext or credential payload was identified. Existing nested public-subset manifests still explicitly exclude private primary PDFs and unrelated local-index files; no new omission from the two complete307 audit copies requires pretending a file is bundled. Public hashes do not confer redistribution permission. The PDFs retained here are the user's manuscript307 and its native compilation outputs, not third-party references. The new text/log package and historical production-archive text were screened for high-confidence private-key/token payload patterns with no hits, without outputting any matched value. This check is limited and is not a comprehensive security certification.

## L3 — freeze, distinct audit and integration boundaries: ACCEPT

The source head and normalized PR body match their assigned identities. Judges308 are unchanged from registration and precede the candidate. No inbound guidance was solicited or incorporated during this review. No candidate, PR, branch, service or other chat was modified. No mathematical, TeX, Lean, numerical or runtime execution occurred.

The complete307 mathematical context is retained and its source preserved; this narrow review does not multiply scientific review counts or claim a fresh theorem. The engineering307 report was read in full, including its limits on timeouts, catastrophic failure retention, dependency locking, same-user filesystem assumptions, actual authority relays and owned-runtime shutdown. That read does not itself accept a new308 runner.

Required repository checks and unchanged normal merge remain separate. PR254 must be integrated before PR255. This verdict does not certify CI, perform a merge or authorize an unreviewed changed source.307 has no PDF rating, and historical299 ratings apply only to their original artifact. Working-paper publication remains distinct from editorial acceptance and human peer review.

## L4 — new runner, paired production and all-page layout: PENDING

The new exact-pinned308 runner requires its own separate engineering audit without guard relaxation. The parent's actual full report reads and exact hash-bound relay must precede allocation. Two fresh exact-SHA clones must produce matching308 PDFs with complete actual exits, logs and preserved outputs. The owned runtime must be released and separately read back. Every final308 page requires visual inspection and absence of remaining margin or legibility defects.

None of these new308 production outcomes was performed or accepted here. The unchanged proofs and plausible display repair do not establish that the new PDF fits, retains its page count or needs no further visual correction. Historical307's defect remains intact as adverse evidence.

## L5 — exact-PDF assessment and publication: PENDING

Only after final visual clearance may the first numerical assessment of the exact308 PDF be requested, retaining its full report, objections and actual context. No inherited grade or resampling to improve a score is permitted. Actual linked native permission, quota, receipt, licences, audited release and public readback remain separate required facts. This source delta audit supplies none of those facts and opens no new scientific route.

## Final disposition

ACCEPT L1-L3 only, bound to source8ac81a6f3f70aa552cc957d45abaf3f0fab90e65 and normalized932-byte PR255 body SHA25611699d481580fbe81463ab62a926abf244f713875beb8e62726be9788a4a4c63. L4-L5 remain pending and are not waived. No blocking source/document objection was found; no new score or PDF acceptance is supplied. Earlier scientific limitations and historical objections remain exactly preserved.
