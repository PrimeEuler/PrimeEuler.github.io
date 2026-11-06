# Cone Derivation Ledger v15.444 — Lane A full odd-extension target

**Timestamp:** 2026-11-06 02:15 EST  
**Lane:** A (Cone/Suzuki), five-frequency commutator only  
**Status:** exact reduction certified; full norm gate unevaluated

## Fresh-state and audit check

- The pre-gate live master HEAD was External Audit Round 492 / v15.443,
  commit `ac097f342c3590ecb127c009168d9aa4c4c6c722`.
- v15.443 was read in full.  It independently confirms v15.442, including
  the moment-Gram domination proof and fresh exact-rational checks, with
  `action: none`; there is no correction to apply.
- The 2026-11-06 scheduled continue directive is ACKed exactly once here.
- A fresh collision check found no current v15.444 ledger or competing owner.

## Exact odd-extension identity

Let `Z=diag(z_n)` on the positive half-line.  Oddly extend both the
coefficient sequence and an input:

    z^o_{-m}=-z_m,       (Of)_{-m}=-f_m.

For the bilateral discrete Hilbert comparison `H`, with kernel `1/(n-k)`,
the positive component of `[M_{z^o},H]Of` has, for `m != n`, coefficient

    z_n(1/(n-m)-1/(n+m))
      - z_m(1/(n-m)+1/(n+m))
    = 2(m z_n-n z_m)/(n^2-m^2).

The mirror index `k=-n` contributes exactly `-z_n/n` on the diagonal.
Consequently the pole-free canonical operator of v15.309 is exactly

    B_0 = (1/pi) P_+ [M_{z^o},H] O + (1/pi) diag(z_n/n).

The final diagonal term restores the hollow diagonal.  Thus the constant
Hankel part, all variable-frequency parts, and the nonprime remainder are
inside one signed bilateral commutator; they must not also be charged
separately.

The odd subspace is invariant under this commutator, and restriction to its
positive coordinates cancels the common square-root-of-two norm factor.
Therefore the remaining sufficient joint operator gate is

    ||(1/pi)[M_{z^o},H]||_odd
      < 2.535928984925255331033863148972074.

The target is the unchanged full target after only the already-certified
outside charges:

    2.535946
      - 0.000008959074744668966136851027926   (diagonal)
      - 0.000008056                           (pole)
    = 2.535928984925255331033863148972074.

Relative to the audited detailed prime commutator bound
`2.534644890455112455357343436959794`, the exact residual allowance inside
this joint gate is

    0.001284094470142875676519712012280.

This is a target reduction, not an evaluated norm certificate.  The current
triangle route remains far too large (v15.437: `4.105463`); a valid next step
must preserve cancellation in the full commutator or supply a genuinely
joint Gram/crossed-product estimate.

## Reproducible certificate

- Witness: `sandbox/lane_a_v15_444_full_odd_extension_target_certificate.py`
- Witness commit: `1ff34911b0a9d174d721b9c628f35daa83dff149`
- Witness Git blob: `962078e3747dc05b575f7d4571ec914cbac6b728`
- Witness SHA-256:
  `50b75b756283d088ae2587328603ada85ddd2acb1fda28ea202ec29a0a87b2ec`
- Manifest: `sandbox/lane_a_v15_444_full_odd_extension_target_manifest.sha256`
- Manifest commit: `c16c689fd1cfaf24a4b2a47743220e7032cc6062`
- Manifest Git blob: `fa6270883ad8902799edabb832d2f4eff901ec86`
- Manifest SHA-256:
  `1d4f5e376185653447f6d4452e3492a1b9604b29b61dfefb0c02c9c2bb6b6d31`
- Replay: `python3 -I lane_a_v15_444_full_odd_extension_target_certificate.py`
- Replay result: `PASS_EXACT_REDUCTION_ONLY`; `norm_gate_status=UNEVALUATED`.

## Frozen boundaries

This entry concerns only the five-frequency commutator on the chosen
counting-measure ell2 model.  That model is not the source-native Suzuki Phi.
Full-K spectral transfer remains INCONCLUSIVE.  Nothing here asserts a
whole-residual, stationary, capacity, physical-equivalence, or full-K result.
The original `C_S_32000`, `3e-5`, `.002`, frozen hashes, and exactly-once
v14.354 and source+v14.403 charges are unchanged.

## HANDOFF

**To:** External Audit / Sandbox  
**Request:** independently verify the odd-extension identity, mirror-diagonal
restoration, and exact target arithmetic.  Then evaluate a cancellation-
preserving bound for the full odd commutator, or a genuinely joint
operator-valued Cotlar/Gram/crossed-product bound.  Do not promote this exact
reduction, a finite-section probe, or design prose to a norm pass.
