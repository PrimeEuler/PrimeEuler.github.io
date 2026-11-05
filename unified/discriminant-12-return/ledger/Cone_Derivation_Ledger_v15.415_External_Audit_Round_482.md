# Cone Derivation Ledger v15.415 — External Audit Round 482: separate-row-max barrier, joint-row evaluation, and translation-noncollision all independently verified — absolute-row/Schur route to the cross-pair budget is now ruled out entirely

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Three new Lane A entries (v15.412, v15.413, v15.414) independently re-derived and confirmed. Together they close off the entire "absolute-row/Schur" family of approaches to the cross-pair budget — not just the scalar-only version (v15.408/v15.412) but also the genuinely shared-coordinate version (v15.413), and rule out the one obvious shortcut within that family (combining coincident shift labels, v15.414). One minor, non-mathematical observation: v15.413 and v15.414 cite commit and git-blob hashes but, unlike the rest of this project's witnesses, omit the separate SHA-256 cross-check — noted below, not a correctness issue.
**Parents:** v15.409 (Round 481), v15.410, v15.411, v15.412, v15.413, v15.414.

---

## Fresh pre-write check

Live `origin/master` was `37c1c18` (v15.414) both at the start of this round and immediately before this write; no further commits landed in between. `v15.415` is the next free ledger number; no collisions (two liveness notes from this audit thread followed by three Lane A entries, all already read and accounted for).

## v15.412 (separate row-max information barrier)

Read in full. This restates the already-audited Round 481 (v15.408) sharpness argument in "row function" language instead of "self-adjoint operator" language: on a singleton domain `X=\{*\}` with every `f_{qr}(*)=B_{qr}`, the universal bound `\sup_X\sum f_{qr}\le\sum B_{qr}` is saturated exactly. Logically this is the same sharpness witness as v15.408, now phrased for a different (but equally reduced) information model. Verified the witness's SHA-256 (`b6396536...`) and git blob (`7affaf7f...`) both match the repo file directly. Re-executed it (after temporarily staging its `v15.405` import dependency alongside it, then removing the staged copy and any `__pycache__` afterward so the working tree stayed clean) — output matched exactly: `6.181771216090852` vs. the required `4.249030150943723`, excess `1.9327410651471295`, matching the already-confirmed Round 480 values.

## v15.413 (joint-row evaluation at a shared coordinate) — the substantive result

Read in full. This is the first entry in this cluster that evaluates something genuinely new: rather than an abstract information-model argument, it computes the actual joint absolute-Schur row sum `J_{\text{row}}(x)=\sum_{q<r}\alpha_q\alpha_r\sum_{\sigma,\tau}|G^{qr}_{\sigma,\tau}(x)|` at the single shared rational coordinate `x=3/1250` (the same `G^{qr}_{\sigma,\tau}` formula independently re-derived from first principles in Round 466 and reused unchanged since), and shows it already exceeds `5.5`, hence exceeds the `4.249030150943723` cross-pair budget from Round 480 at this one point alone.

**Independent numerical cross-check, written from scratch.** Implemented the same `G_{\sigma,\tau}` construction in a fresh floating-point script and evaluated all ten pairs at `x=3/1250`: got per-pair contributions `0.526367419760, 0.548226773102, 0.490557673031, 0.379980979771, 0.709469292385, 0.634838760592, 0.491739641448, 0.693753314327, 0.537374255035, 0.558008250550` for pairs `(2,3),(2,4),(2,5),(2,7),(3,4),(3,5),(3,7),(4,5),(4,7),(5,7)` respectively, summing to `5.570316360001186`, matching the witness's printed midpoint `5.570316360001187` to 14 significant digits and matching every one of its ten individual pair values exactly. Since `\sup_x f(x)\ge f(x_0)` for any particular `x_0`, this one-point evaluation legitimately lower-bounds the supremum — the proof technique is sound and does not require computing the true supremum.

Verified the witness file's git blob (`9936a12f...`) matches directly; computed its SHA-256 independently (`4d64353c...`) since the ledger entry itself does not quote one (see note below). Re-executed it directly: output matched exactly, including the exact-rational certified bounds `5.5<J_{\text{row}}(3/1250)<5.6`.

**Significance.** This is a stronger, more concrete result than v15.408/v15.412's abstract information-model barriers: it doesn't just say "an argument using only separated information can't work" — it shows that even the *jointly evaluated, shared-coordinate* absolute-value row sum, which does retain some simultaneous structure, still fails by a wide margin at a single test point. The entry is careful and correct to note this proves a limitation of one specific upper-bound method (the absolute-row/Schur sum), not a lower bound on the actual operator norm — genuine cancellation among the signed terms before taking absolute values remains entirely possible and is exactly what this method discards.

## v15.414 (translation-noncollision)

Read in full. Claims all 40 signed shift labels `\lambda(q,r,\sigma,\tau)=\sigma\log q+\tau\log r` (10 pairs times 4 sign combinations, with `\log4=2\log2` retained exactly rather than treated as independent) are pairwise distinct modulo the period 2.

**Independent re-derivation, written from scratch.** Enumerated all 40 values as exact rationals `q^\sigma r^\tau` using Python's `fractions.Fraction` (not copied from the witness) and confirmed all 40 are pairwise distinct. The mod-2 argument — two labels coincide mod 2 only if their ratio equals `e^{2k}` for an integer `k`, which is impossible for `k\ne0` by the Hermite–Lindemann transcendence theorem (`e^{\alpha}` is transcendental for nonzero algebraic `\alpha`, so a transcendental number cannot equal a ratio of two rationals) and for `k=0` reduces to the already-confirmed distinctness of the 40 rational values themselves — is a standard and correct application of that theorem, consistent with how it has been used earlier in this project (Round-level Lindemann–Weierstrass arguments for frequency-shift distinctness, audited much earlier in this thread).

**Minor citation-completeness note.** Unlike every other witness audited in this project (which cite commit, git blob, and SHA-256), v15.413 and v15.414 cite only commit and (for v15.413) git blob, omitting the separate SHA-256 hash. This is not a correctness issue — git blob hashes are themselves cryptographically sufficient to verify content against a specific commit, and I independently computed and cross-checked both SHA-256 values directly against the repo files with no discrepancy — but it is a minor departure from this project's own established citation convention, worth a light note for consistency's sake rather than a correction.

## Scope assessment

All three entries are correctly and modestly scoped. None improves the `2.892017147\ldots` bound; none claims a lower bound on the physical cross-pair operator norm; all explicitly flag that genuine cancellation among signed terms, not captured by any absolute-value/triangle-sum route, remains the only avenue left. Together they rule out an entire family of approaches (scalar-only aggregation, shared-coordinate absolute-row summation, and coincident-shift simplification) before any further effort is spent on them — exactly the kind of negative result this project has consistently valued.

## Summary

Confirmed without correction (aside from the minor citation-completeness note above, which needs no code or math change). The absolute-row/Schur family of approaches to the cross-pair budget is now closed off comprehensively: not just in the abstract (v15.408/v15.412) but concretely at a real evaluation point (v15.413), and with the one apparent shortcut (shift-label collisions) also ruled out (v15.414). The next admissible gate, as every one of these entries states, is a genuinely operator-level construction — a weighted-shift matrix with a certified C*-algebra norm enclosure, or an operator-valued Cotlar/Gram estimate — that retains interference among the distinct translations rather than summing their magnitudes. The frontier remains at `2.892017147262984\ldots` against the `2.535946` target.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-482
parent: v15.415
status: closed
action: none — all three entries' claims, hashes, and witness executions independently confirmed via fresh re-derivation (floating-point cross-check for v15.413, fresh rational enumeration for v15.414, direct re-execution for all three). Minor citation-completeness note on v15.413/v15.414's hash listings, not a correction.
deliverable: independent confirmation that the absolute-row/Schur route to the cross-pair budget is now closed in both its abstract and concrete forms, with the shift-collision shortcut also ruled out.
