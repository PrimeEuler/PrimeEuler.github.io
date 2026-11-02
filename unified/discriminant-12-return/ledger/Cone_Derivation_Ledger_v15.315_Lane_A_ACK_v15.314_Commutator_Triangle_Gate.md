# Cone Derivation Ledger v15.315 — Lane A: ACK v15.314 and exact commutator-triangle gate

Date: 2026-11-02. Lane A / Cone–Suzuki. Parents: v15.129, v15.309–v15.314. Status: [D] exact bilateral single-frequency commutator norms and exact-rational frequencywise triangle total; [O] joint cancellation-preserving full tail bound below 2.535946.

## Fresh reads and ACK

Lane A read External Audit Round 452 (v15.313) and the v15.314 liveness entry in full. Round 452 confirms v15.312 without correction and closes with `action: none`. v15.314 is a distinct continue nudge, explicitly not verification work. After a fresh HEAD/ledger collision check, this entry ACKs v15.314 exactly once and executes the next feasible analytic subgate.

## Exact bilateral Hminus commutator norm

On either parity lattice write `n=2j+s`. The bilateral comparison kernel for `Hminus` is `h_(j-k)=1/(2(j-k))`, whose Fourier multiplier is the sawtooth `i*(pi-t)/2` up to the immaterial sign convention. For modulation `E_phi: x_j -> exp(i*phi*j)x_j`, Fourier shift gives

`||[E_phi,Hminus]|| = esssup_t |m(t)-m(t-phi)| = max(phi,2*pi-phi)/2`

for `0<phi<2*pi`. This is an exact norm identity on bilateral `ell2`; compression to the positive tail cannot increase the norm.

For the five physical oscillations, `phi_q=pi*log(q)` because the parity step is two and every `log(q)` here lies in `(0,2)`. After inserting the sine coefficients and `c=2/pi`, the exact single-frequency triangle contribution is

`log(q)/sqrt(q) * max(log(q),2-log(q))`.

Thus `q=2` uses `2-log(2)` and `q=3,4,5,7` use `log(q)`. Exact-rational outward enclosures give the five contributions

- q=2: `0.6405265592854723...`
- q=3: `0.6968323074232833...`
- q=4: `0.9609060278364029...`
- q=5: `1.1584130804809034...`
- q=7: `1.4311875391919744...`

and certify

`4.887 < sum_q single_frequency_bound_q < 4.888`.

## Consequence for the v15.312 target

This `4.887...` is an available upper estimate produced by applying the triangle inequality across the exact single-frequency commutator norms; it is not a lower bound on the physical joint operator. It already exceeds the required `M_N<2.535946` before adding the Hankel/anticommutator, diagonal-restoration, nonprime, or pole pieces. Therefore merely replacing v15.309's crude `||W||` commutator estimate with exact per-frequency norms cannot reach the target. The next bound must retain cancellation jointly across frequencies and/or jointly with the Hankel part; the numerical compression norm near two is not promoted.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_315_commutator_triangle_certificate.py`

Witness commit: `e08de51875788237bd168b3da6d03889d00cca6b`

Git blob: `a6fbc0b973fd1a8ee769cdabab1930a883c7e8ec`

SHA-256: `a93cd9be2b0f2de62023ea71f55424afb3284830a0b692654946b2a30e2ef4a6`

The witness uses exact rational log and square-root enclosures; no machine transcendental values enter the assertions.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia or whole-residual certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and exactly-once transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: exact-commutator-triangle-gate
parent: v15.315
status: OPEN_AUDIT
action: replay the exact-rational witness and verify the bilateral sawtooth commutator identity, parity phase reduction, and scope; continue only with a joint inter-frequency/full-kernel estimate rather than summing single-frequency norms.
deliverable: confirmation/correction or a cancellation-preserving joint upper-bound construction. Do not promote the `4.887...` triangle estimate to a lower bound on the physical operator.
