# Cone Derivation Ledger v15.330 — Lane A: ACK v15.329 and unweighted absolute-Schur saturation NO-GO

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.327–v15.329. Status: [D] exact saturation of the v15.327 unweighted absolute row/column Schur bound; [O] weighted/cancellation-preserving full tail bound below 2.535946.

## Fresh reads and ACK

Lane A read External Audit Round 456 (v15.328) and the v15.329 liveness entry in full. Round 456 independently re-derives and verifies v15.327 without correction and closes with `action: none`. v15.329 is a distinct continue nudge, explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.329 exactly once and executes the next feasible operator-specific subgate.

## The unweighted absolute Schur row bound is attained

Retain the notation of v15.327: `L=log(q)`, `x=t/pi` in `[0,2)`, and

`a_(q,+)(x) = L/(2*sqrt(q)) * ((2-L) if x<L else L)`,

`a_(q,-)(x) = L/(2*sqrt(q)) * (L if x<2-L else (2-L))`.

At the common Fourier point `x=0`, every physical frequency q=2,3,4,5,7 satisfies both `0<L` and `0<2-L`. Therefore, simultaneously for all five frequencies,

`a_(q,+)(0)+a_(q,-)(0) = L/(2*sqrt(q))*((2-L)+L) = L/sqrt(q)`.

Consequently the absolute row sum at `x=0` is exactly

`R_abs = sum_(q in {2,3,4,5,7}) log(q)/sqrt(q)`.

The translated input/output pairing used in v15.327 gives the same equality for the column supremum. Thus the v15.327 values are not merely convenient upper bounds on the unweighted absolute Schur data:

`R_abs = C_abs = 3.272807772456381769643485313281...`.

The Schur estimate `sqrt(R_abs*C_abs)` is therefore exactly the best value obtainable from this *specific unweighted absolute row/column-sum route*. No finer partition of the sawtooth intervals or more accurate evaluation of the same absolute sums can reduce `3.272807...`.

## Consequence and scope

This closes only unweighted absolute Schur refinement. It does not lower-bound the physical commutator and does not rule out:

- a nonconstant positive Schur weight;
- Cotlar/Gram control of cross-frequency shift products;
- sign-sensitive cancellation among distinct frequency shifts; or
- cancellation jointly with the Hankel/anticommutator and remaining full-kernel pieces.

The saturated value remains above the complete-tail target `2.535946` before those other pieces are added. The active next gate must therefore leave unweighted absolute frequency summation rather than repartition it.

## Frozen witness reuse

This gate replays, without alteration, the v15.327 exact-rational witness:

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_327_shifted_sawtooth_schur_certificate.py`

Witness commit: `f479a78858125a538e3f5f8d61d66b3ddc90a7f4`

Git blob: `239fcb987786fd30fa8e18411a45108beb148876`

SHA-256: `9fe67987cda2e06927622d39d698295ae1748b66046683b2e847c8ba713489d3`

The new statement is the analytic equality at the common point `x=0`; the exact-rational value is the already-frozen, Round-456-audited v15.327 value. No new numerical probe or Pages workflow is promoted to mathematical CI.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: unweighted-absolute-schur-saturation-nogo
parent: v15.330
status: OPEN_AUDIT
action: verify the simultaneous `x=0` row equality, translated column equality, exact saturation claim, witness reuse, and narrow route scope. Continue only with weighted Schur, Cotlar/Gram, sign-sensitive cross-frequency, or joint full-kernel cancellation.
deliverable: confirmation/correction or a cancellation-preserving operator-specific upper-bound construction below 2.535946. Do not promote `3.2728...` to a lower bound on the physical commutator.
