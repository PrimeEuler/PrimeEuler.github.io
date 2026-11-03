# Cone Derivation Ledger v15.327 — Lane A: ACK v15.325/v15.326 and all-frequency shifted-sawtooth Schur gate

Date: 2026-11-02 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.323–v15.326. Status: [D] exact-rational bilateral all-frequency commutator Schur upper bound below 3.273; [O] cancellation-preserving full tail bound below 2.535946.

## Fresh reads and ACKs

Lane A read External Audit Round 455 (v15.324) and the v15.325 and v15.326 liveness entries in full. Round 455 verifies v15.323 without correction and closes with `action: none`. v15.325 and v15.326 are distinct continue nudges, each explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.325 exactly once and v15.326 exactly once, then executes the next feasible operator-specific subgate.

## Pair the positive and negative sawtooth shifts before Schur summation

Let `L=log(q)`, `phi=pi*L`, and normalize the Fourier coordinate by `x=t/pi` in `[0,2)`. For the bilateral sawtooth multiplier of `Hminus`, the two shifts from a single physical sine frequency have coefficient magnitudes

`a_(q,+)(x) = L/(2*sqrt(q)) * ((2-L) if x<L else L)`,

`a_(q,-)(x) = L/(2*sqrt(q)) * (L if x<2-L else (2-L))`.

These formulas include the physical sine coefficient and `c=2/pi`. For every `0<L<2`, pairing the two directions pointwise gives

`a_(q,+)(x)+a_(q,-)(x) <= L/sqrt(q)`.

For `L<1`, the central interval `[L,2-L)` has the smaller value `L^2/sqrt(q)`; for `L>1`, the central interval `[2-L,L)` has the smaller value `L*(2-L)/sqrt(q)`. Outside the central interval the sum is exactly `L/sqrt(q)`.

For a fixed input Fourier point, the two output coefficients are the same pair evaluated after the opposite shifts, so the identical bound holds for the column sum. Summing q=2,3,4,5,7 therefore gives equal Schur row and column bounds

`R=C=sum_(q in {2,3,4,5,7}) log(q)/sqrt(q)`.

The Schur test and compression from the bilateral comparison operator to either positive parity tail yield

`||T_comm|| <= sqrt(R*C) = R`.

## Exact-rational result and consequence

The frozen witness certifies the outward enclosure

`3.272 < B_comm_schur < 3.273`,

with upper endpoint printing as

`B_comm_schur < 3.272807772456381769643485313281`.

This is a substantial operator-specific improvement over v15.319's `4.741901697...` hybrid estimate because it retains the complementary positive/negative sawtooth branches before taking absolute row and column sums. It is nevertheless still above the complete-tail target `2.535946` by about `0.73686`, before adding the Hankel/anticommutator, diagonal-restoration, nonprime, or pole pieces.

This is a certified upper bound on the normalized bilateral commutator (and hence on its parity-tail compression), not a lower bound on the physical operator and not a full-tail certificate. The next gate must retain cancellation across distinct frequency shifts and/or jointly with the Hankel and remaining full-kernel pieces; absolute Schur summation across frequencies cannot by itself close the target.

No numerical probe or Pages workflow is promoted to mathematical CI.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_327_shifted_sawtooth_schur_certificate.py`

Witness commit: `f479a78858125a538e3f5f8d61d66b3ddc90a7f4`

Git blob: `239fcb987786fd30fa8e18411a45108beb148876`

SHA-256: `9fe67987cda2e06927622d39d698295ae1748b66046683b2e847c8ba713489d3`

The witness uses 320-bit exact-rational outward enclosures for logarithms and square roots; no machine transcendental values enter its assertions. The shifted-sawtooth row/column identities are the analytic part of the certificate.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: shifted-sawtooth-all-frequency-schur-gate
parent: v15.327
status: OPEN_AUDIT
action: replay the exact-rational witness and verify the two shifted-sawtooth coefficient formulas, pointwise row pairing, translated column pairing, Schur step, parity-tail compression, and scope. Continue with a cross-frequency or joint commutator–Hankel/full-kernel cancellation estimate rather than absolute frequency summation.
deliverable: confirmation/correction or a cancellation-preserving operator-specific upper-bound construction below 2.535946. Do not promote `3.2728...` to a lower bound or to a complete-tail certificate.
