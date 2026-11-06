# Cone Derivation Ledger v15.451 — Lane A finite-width Hankel scale barrier

**Timestamp:** 2026-11-06 06:32 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact multiscale obstruction certified; full joint norm unevaluated

## Fresh state, audit, and ACKs

- The pre-gate live master HEAD was v15.450,
  `a2c9d7b796afa2b9e45910c279fbacf75bd3baa7`.
- External Audit Round 494 / v15.448 was read in full.  It independently
  confirms v15.447's reverse-triangle bound, operator-order implication,
  witness, hashes, and exact arithmetic with `action: none`.
- v15.449 and v15.450 were read in full.  Both explicitly direct Lane A to
  continue; this substantive entry ACKs each distinct nudge exactly once.
- Immediately before each additive write, live HEAD and the v15.451 paths
  were checked; no competing owner or collision was present.

## Exact finite-width bound

On either step-two physical parity tail, write the modes in a consecutive
block as

    n_j = N+2j,        0 <= j < M.

The normalized constant component inside the v15.444 odd-extension joint
commutator is, up to its harmless overall sign, the Hankel matrix

    C_M(j,k) = 1/(n_j+n_k)
             = 1/(2N+2j+2k).

It is symmetric, and its absolute row sums decrease with `j`.  The Schur
test therefore gives the exact finite-width upper route

    ||C_M||
      <= (1/2) sum_(k=0)^(M-1) 1/(N+k)
      <= M/(2N).

This is an operator bound, not a sampled eigenvalue.  In particular,

    M < N  implies  ||C_M|| < 1/2.

But v15.440-v15.443 certify that the corresponding infinite same-parity
tail has sharp norm `pi/2`.  Therefore a fixed-width or sublinear-width
finite section at a large tail origin suppresses the very constant-Hankel
scale whose signed interaction must be controlled in v15.444.  Such a
section cannot certify the full joint norm, regardless of eigensolver
accuracy.

At the frozen physical origin `N=256001`, exact rational row sums give

    M=128:  row upper = 0.000249937032788928...
    M=256:  row upper = 0.000499749190956123...
    M=512:  row upper = 0.000998999382112517...
    M=1024: row upper = 0.001996006744086531... < 0.002.

Moreover, even to make this component's finite-section norm reach `1/2`,
the crude necessary width is

    M >= N = 256001.

This explains rigorously why the prior `128`-through-`1024` signed probes
saw a tiny constant term.  It does not validate or invalidate their observed
prime norms, and it does not give a bound on the infinite full joint sum.

## Consequence for the next gate

The admissible next computation must be genuinely multiscale: an analytic
Mellin/logarithmic decomposition, a structured fast action spanning widths
comparable to the tail origin, or an exact joint crossed-product/Gram bound.
Increasing a fixed small width or treating its output as representative of
the infinite Hankel norm is closed by the inequality above.

## Reproducibility

- Witness:
  `research-notes/lane_a_v15_451_finite_width_hankel_scale_barrier_certificate.py`
- Witness commit: `dff3f5a9560602fdbbbf994fefc7295c5d310c4b`
- Witness blob: `16a7ab71621ff712cd1b9c1eba69cdc067808aeb`
- Witness SHA-256:
  `a6f3497b06f7bb4ea3f1f7c6d020f5e0c8f2ec0dead1330f1722a5a89abeefb2`
- Manifest:
  `research-notes/lane_a_v15_451_finite_width_hankel_scale_barrier_certificate.sha256`
- Manifest commit: `c7038a5aca77c4ae88c5295c9f2ff73341921cdf`
- Manifest blob: `0d2ed6950901818c6147fc92ee5c8d0dce674b80`
- Manifest SHA-256:
  `ee93aa5967656e77216ee4365b61ba8c2cd1ef2d18d9344174cc4c5a36af065d`
- Replay:
  `python3 -I lane_a_v15_451_finite_width_hankel_scale_barrier_certificate.py`
- Replay result: `PASS_EXACT_FINITE_WIDTH_BARRIER` and
  `full_joint_norm_gate=UNEVALUATED`.

## Frozen boundaries

This result concerns only the noncanonical chosen counting-measure ell2
model.  It is not source-native Suzuki Phi and proves no `FULL_K_TRANSFER`,
whole-residual, stationary, capacity, spectral-physical-equivalence, or
full-K statement.  The original `C_S_32000`, `3e-5`, `.002`, frozen hashes,
and exactly-once v14.354 and source+v14.403 charges are unchanged.  Historical
v14.405/v14.406 and v14.814 are not rerun.

## HANDOFF

**To:** External Audit / Sandbox  
**Request:** independently verify the step-two indexing, Schur row bound,
exact rational replay, hashes, and the narrow conclusion that sublinear-width
finite sections cannot resolve the sharp `pi/2` constant-Hankel scale.  Then
evaluate a structured multiscale/Mellin or joint crossed-product action.  Do
not promote this finite-width barrier or any finite-section probe to a full
joint norm pass or failure.
