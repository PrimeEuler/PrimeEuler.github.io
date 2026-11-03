# Cone Derivation Ledger v15.352 — External Audit Round 463: generic adjoint-pair NO-GO and sharpness obstruction independently verified

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's generic adjoint-pairing estimate for the q=3,5 cross block (v15.351) independently re-derived and confirmed, including the scalar sharpness example showing sign information alone cannot beat the factor-2 loss; witness re-executed.
**Parents:** v15.348 (Round 462), v15.349, v15.350, v15.351.

---

## Fresh pre-write check

Live `origin/master` was `443275b` (v15.351) both at the start of this round and immediately before this write; no further commits landed in between. `v15.352` is the next free ledger number; no collisions (two liveness notes from this audit thread followed by one Lane A entry, all already read and accounted for).

## Verification

Read v15.349 and v15.350 (my own prior liveness notes) and v15.351 (Lane A's generic adjoint-pair NO-GO) in full.

Confirmed the universal estimate by hand: for any bounded `A_j`, `||s_j(A_j+A_j^*)|| = ||A_j+A_j^*|| <= ||A_j||+||A_j^*|| = 2||A_j||` since `||A_j^*||=||A_j||` always, so summing over `j` gives `||sum_j s_j(A_j+A_j^*)|| <= 2 sum_j ||A_j||` regardless of the specific signs `s_j` — this is forced by the triangle inequality alone.

Confirmed the sharpness example independently: taking `A_j = s_j a_j I` on a one-dimensional space, `A_j` is already self-adjoint (real scalar), so `A_j+A_j^*=2s_ja_jI`, and `s_j(A_j+A_j^*) = 2 s_j^2 a_j I = 2a_jI` since `s_j^2=1` for any sign. Summing gives `2(sum_j a_j)I`, with norm exactly `2 sum_j a_j` — matching the generic bound with equality, *independent of which signs appear*. This is the key structural point: because `s_j^2=1` always, no choice of signs can ever help at this information level (branch norms + signs + adjoint pairing alone); genuine cancellation requires the actual sawtooth coefficient functions, not scalar sign bookkeeping. Verified this numerically with the witness's own test case (`signs=(+1,-1,-1,+1)`, `magnitudes=(1/7,2/7,3/7,4/7)`): by hand, the signed sum evaluates to `20/7`, and `2*sum(magnitudes)=2*(10/7)=20/7` — exact equality, confirming the forcing argument is not a coincidence of this particular sign pattern.

Checked the numeric consequence: since `C_35 = b_3b_5\log(5) \approx 0.734762998873283335...` (independently confirmed in Round 461), `2C_35 \approx 1.469525997746566670...`, which lies strictly inside the claimed `(1.468, 1.470)` window.

Verified the witness file's SHA-256 (`513d4664...`) and git blob (`131720e3...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed

```
q35_generic_adjoint_pair_lower 1.469525997746566670087986494764
q35_generic_adjoint_pair_upper 1.469525997746566670087986494764
sharp_scalar_example 20/7 20/7
certified 1.468 < 2*C_q35 < 1.470; generic A+A* pairing is sharp
```

matching the ledger's claimed values and my independent hand computation (`20/7 = 20/7`) exactly.

## Scope check

The entry is correctly scoped: it proves only that the specific information set {individual branch norms, signs, adjoint pairing} cannot force any improvement over `2 sum_j ||A_j||`, via a genuine sharpness example rather than an unproven assertion. It explicitly states the physical sawtooth coefficient functions may still cancel and must be evaluated jointly, not replaced by their norms. `FULL_K_TRANSFER` remains INCONCLUSIVE; no finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed.

## Summary

Confirmed without correction. This is a clean, honest negative result: Lane A correctly diagnoses that merely knowing the branch norms and the `+,-,-,+` sign pattern (from v15.347) is not enough to beat the trivial factor-2 adjoint-pairing bound, because any sign pattern is absorbed by `s_j^2=1` in the sharpness construction. This rules out an entire class of attempted shortcuts and correctly redirects effort toward evaluating the actual translated sawtooth multipliers jointly. The frontier remains at 3.273 (Round 456) against the 2.535946 target. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-463
parent: v15.352
status: closed
action: none — v15.351's universal estimate, sharpness example, and numeric enclosure independently confirmed by hand derivation and witness re-execution; no correction needed.
deliverable: independent confirmation of the generic adjoint-pairing bound, its scalar sharpness example (with the `s_j^2=1` forcing argument made explicit), the `2C_35` numeric enclosure, and the correctly narrow scope.
