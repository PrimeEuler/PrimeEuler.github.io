# Cone Derivation Ledger v15.323 — Lane A: ACK v15.321/v15.322 and q=3,5,7 multiplier-sup route NO-GO

Date: 2026-11-02 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.319–v15.322. Status: [D] exact q=3,5,7 physical-multiplier sup norm and generic commutator-route comparison; [O] cancellation-preserving full tail bound below 2.535946.

## Fresh reads and ACKs

Lane A read External Audit Round 454 (v15.320) and the v15.321 and v15.322 liveness entries in full. Round 454 verifies v15.319 without correction and closes with `action: none`. v15.321 and v15.322 are distinct continue nudges, each explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.321 exactly once and v15.322 exactly once, then executes the next feasible analytic subgate.

## Exact q=3,5,7 multiplier supremum

On either parity lattice the q=3,5,7 physical multiplier has the form

`Z_357(j) = sum_(q in {3,5,7}) 2*log(q)/sqrt(q) * sin(pi*log(q)*j + delta_q)`,

where the fixed phases `delta_q` depend on the parity sector but not on `j`.

The four numbers

`1, log(3)/2, log(5)/2, log(7)/2`

are rationally independent. Indeed, clearing denominators in a rational relation and exponentiating would give `exp(m_0)` equal to a nonzero rational number made from powers of 3, 5, and 7. Lindemann–Weierstrass excludes this when the nonzero integer `m_0` is algebraic; when `m_0=0`, unique factorization forces all remaining coefficients to vanish.

Kronecker density therefore makes the phase triple dense in the three-torus. Each sine can approach its maximizing sign simultaneously, for either fixed parity phase. Hence

`||Z_357||_infinity = sum_(q in {3,5,7}) 2*log(q)/sqrt(q)`.

The frozen exact-rational witness certifies

`4.179 < ||Z_357||_infinity < 4.180`,

with outward endpoints printing as `4.179063040324325406515981740085...`.

## Consequence: generic lumped-multiplier route is worse

Using only `c=2/pi`, `||Hminus||<=pi/2`, and the generic commutator inequality gives

`||(c/2)[Z_357,Hminus]|| <= c*||Z_357||*||Hminus|| <= ||Z_357||`.

Thus the best exact sup norm available to this *specific generic inequality route* is about `4.1791`. It is already worse than v15.315's audited exact frequencywise q=3,5,7 commutator sum `3.286432927...`, and it exceeds the complete-tail target `2.535946` before q=2,4 or any Hankel, diagonal-restoration, nonprime, or pole contribution is added.

This does not lower-bound the physical joint commutator and does not rule out a sharper operator-specific cancellation argument. It closes only the proposal “lump q=3,5,7 into one physical multiplier, take its sup norm, then apply the generic commutator inequality.” The remaining gate must use the shifted-sawtooth operator structure and/or joint commutator–Hankel/full-kernel cancellation, not multiplier sup norm alone.

No numerical probe or Pages workflow is promoted to mathematical CI.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_323_q357_multiplier_supnorm_nogo.py`

Witness commit: `ed4aec617307de544c985bbfa43924a8189f8830`

Git blob: `2e491a923606dca6eb4f4883e2aae88d9ac412ae`

SHA-256: `9127014e8bdbe6357c564f7b9b3c4833f027890b6c6dd7c4790699ab2bd8d8ed`

The witness uses 320-bit exact-rational outward enclosures for logarithms and square roots; no machine transcendental values enter its assertions. The equality with the multiplier supremum uses the analytic rational-independence/Kronecker argument above.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q357-multiplier-sup-route-nogo
parent: v15.323
status: OPEN_AUDIT
action: replay the exact-rational witness and verify the rational-independence/Kronecker argument and the narrow route scope. Continue with an operator-specific shifted-sawtooth or joint commutator–Hankel/full-kernel cancellation bound; do not reuse generic multiplier sup norm as if it improved v15.315.
deliverable: confirmation/correction or a cancellation-preserving operator-specific upper-bound construction. Do not promote `4.179...` to a lower bound on the physical commutator.
