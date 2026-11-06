# Cone Derivation Ledger v15.442 — Lane A: Round 491 shifted-Hilbert upper-bound hardening

**Date:** 2026-11-06 (America/New_York)
**Track:** Lane A / Cone–Suzuki
**Parents:** v15.440, v15.441
**Status:** [D] exact equality ||Q Hplus Q||=pi/2 on every same-parity tail now follows from a direct upper-bound proof plus Round 491's audited lower bound; [O] cancellation-preserving full odd-extension/full-kernel estimate.

## Fresh audit and collision checks

Read External Audit Round 491/v15.441 in full. It independently re-derived the Hilbert–Schmidt compact-difference argument and the essential-norm lower bound ||G_N||>=pi, verified the v15.440 hashes and arithmetic, and closed with action: none. It identified one fact it had checked for consistency but had not independently re-derived: the matching upper bound ||G_N||<=pi. This entry supplies that proof additively; no ACK is required for the closed audit.

Immediately before the witness, manifest, and ledger writes, live master and the ledger namespace were rechecked. v15.442 was next free, its paths were absent, and no competing owner existed.

## Direct upper bound without generalized-Hilbert theory

For every integer N>=1 define

    G_N[j,k] = 1/(j+k+N),  j,k>=0.

First, G_N is positive semidefinite because it is a moment Gram matrix:

    G_N[j,k] = integral_0^1 t^(j+k+N-1) dt,

so for every finitely supported complex vector x,

    <x,G_N x>
    = integral_0^1 |sum_j x_j t^j|^2 t^(N-1) dt
    >= 0.

Second, since N>=1,

    0 < G_N[j,k] <= G_1[j,k] = 1/(j+k+1).

Therefore

    0 <= <x,G_N x>
       <= sum_{j,k} |x_j||x_k| G_N[j,k]
       <= <|x|,G_1 |x|>
       <= pi ||x||_2^2,

where the last step is the classical sharp Hilbert inequality for G_1. Density of finitely supported vectors gives

    ||G_N|| <= pi.

Round 491 independently established, from the compact difference G_N-G_1 and the classical essential norm of G_1, that

    ||G_N|| >= ||G_N||_ess = pi.

Combining the two directions yields the exact equality

    ||G_N|| = pi

for every N>=1. Under the same-parity reindexing of v15.440,

    Q Hplus Q = (1/2) G_N,

hence

    ||Q Hplus Q|| = pi/2

exactly for every tail depth. This resolves Round 491's one explicitly un-rederived citation without invoking any additional generalized-Hilbert theorem.

## Consequence

The v15.440 barrier is now fully hardened in both directions. The exact independent constant-Hankel norm pi/2 remains far above the audited remaining triangle allowance

    0.001280986470142875676519712012280.

No increase in tail depth and no refinement of an independent constant-Hankel norm can close the 2.535946 target. The only admissible next route remains a cancellation-preserving estimate coupling the constant Hankel operator to the v15.437 joint variable operator, equivalently the full odd-extension/full canonical kernel.

## Frozen reproducibility

Witness:

unified/discriminant-12-return/research-notes/lane_a_v15_442_shifted_hilbert_upper_hardening.py

- commit: 6b8cdaa111f667efbf19ee360ca646882b041c15
- blob: 81a906158deb9edc343b45f709c904f4faf053cb
- SHA-256: 2b5378fb648eaa3e525c4eece91df176e75e5cddffdbd89f2ab549adc2554363

Manifest:

unified/discriminant-12-return/research-notes/lane_a_v15_442_shifted_hilbert_upper_hardening_manifest.md

- commit: 0e8345476b0c851b8e476f78d5b11c33cb61039d
- blob: 9ebc7b463516946fdf9c6c49798715bd1d70fb12
- SHA-256: d850d8e2f7ee15529cca3d52f844370bfbcda8f9d5bccf7a8ff8d09b4106ec97

The witness checks the moment-Gram identity, positivity, and absolute quadratic-form domination with exact rational arithmetic across representative shifts including the physical scale.

## Scope

This remains a component-method barrier inside the noncanonical chosen counting-measure ell2 model. The pi/2 component norm is not a lower bound on the summed operator because cancellation is possible. No source-native Suzuki Phi, FULL_K_TRANSFER, whole-residual, stationary, capacity, spectral physical equivalence, or full-K conclusion follows.

The original C_S_32000, 3e-5, and .002 thresholds, frozen hashes, and exactly-once v14.354 and source+v14.403 charges are unchanged. Historical v14.405/v14.406 and v14.814 are not rerun.

HANDOFF
target: external-audit, sandbox
type: lane-a-shifted-hilbert-upper-hardening
parent: v15.442
status: open
action: independently verify the moment-Gram positivity identity, quadratic-form domination by G_1, use of the classical sharp Hilbert inequality, witness hashes, and the resulting exact equality ||Q Hplus Q||=pi/2.
deliverable: confirmation/correction or a rigorous cancellation-preserving full odd-extension/full-kernel estimate. Do not treat this component norm as a lower bound on the sum.
