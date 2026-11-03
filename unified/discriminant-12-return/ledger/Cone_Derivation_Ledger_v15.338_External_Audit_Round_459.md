# Cone Derivation Ledger v15.338 — External Audit Round 459: distinct-shift orthogonality shortcut correctly closed

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's closure of the "distinct shifts imply orthogonality" shortcut independently re-derived by hand and confirmed numerically on a discretized circle.
**Parents:** v15.334 (Round 458), v15.335, v15.336, v15.337.

---

## Fresh pre-write check

Live `origin/master` was `4cedadb` (v15.337) both at the start of this round and immediately before this write; no further commits landed in between. `v15.338` is the next free ledger number; no collisions (one Lane A commit after Round 458).

## Verification

Two independent claims, both checked.

**Pairwise distinctness of the ten signed shifts.** Hand-verified the Lindemann–Weierstrass/unique-factorization argument: a coincidence `ε log q − δ log r = 2k` exponentiates to `q^ε/r^δ = e^{2k}`, a rational number on the left; for `k≠0` this contradicts the transcendence of `e^{2k}` (since `e` itself is transcendental, `e^n` algebraic for nonzero integer `n` would force `e` algebraic as a root of `y^n=e^n`); for `k=0`, `q^ε=r^δ` forces `q=r,ε=δ` (same sign) or `qr=1` (opposite sign, impossible for `q,r≥2`). Confirmed correct and consistent with the identical technique already verified in v15.323/Round 455.

**Distinct translations are not orthogonal.** Hand-derived the shift-operator identities `U_αU_β=U_{α+β}` and `U_α^*=U_{-α}` directly from the definition `(U_αf)(x)=f(x+α)`, giving `U_α^*U_β=U_{β-α}`, which is itself a unitary and therefore has operator norm exactly `1` regardless of how different `α,β` are. Independently confirmed this numerically: built explicit unitary translation matrices on a 2000-point discretization of the circle `ℝ/2ℤ` for two distinct irrational shifts (`log 3` and `−log 5`), verified each is unitary to machine precision (`‖U_α^*U_α−I‖≈3.3×10⁻¹⁴`), and computed the singular values of the cross-product `U_α^*U_β` — both the largest and smallest singular value came back `1.0000000000000016`/`0.9999999999999979`, confirming the cross-product is itself exactly unitary, not merely bounded, for arbitrarily distinct shifts.

## Scope check

The entry correctly draws only the narrow conclusion that this specific shortcut (discarding cross-frequency Gram terms just because the underlying shifts differ) fails, and explicitly does not claim anything about the actual coefficient-weighted products `T_q^*T_r`, which still need to be evaluated rather than assumed small. `FULL_K_TRANSFER` remains INCONCLUSIVE; no numerical probe or bound is promoted.

## Summary

A clean, quick, and useful negative result: a tempting simplification (distinct logarithmic frequencies ⟹ negligible cross-terms) is definitively false for pure translation operators, confirmed both analytically and by direct numerical construction. This correctly forces the next step to actually evaluate the coefficient-weighted cross-frequency products rather than hoping they vanish for free. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-459
parent: v15.338
status: closed
action: none — v15.337's distinctness and non-orthogonality claims independently confirmed by hand and numerical construction; no correction needed.
deliverable: independent confirmation of the ten-shift distinctness proof and the exact-unitary cross-product claim, including a direct numerical verification on a discretized circle.
