# Cone Derivation Ledger v13.973 — Sandbox Xi Scalar Spectral-Tail Rate

**Date:** 2026-10-03
**Track:** Sandbox (our Lane B)
**Status:** [N] numerical tail-rate for the v13.965 spectral-shift sum; [I] implication for the a→∞ certification.

---

## 1. What was computed [N]

Ran the v13.965 reproducer (`research-notes/xi_scalar_spectral_shift_check.py`)
to M = 60 intervals (vs. M = 19 in the ledger entry). Target:
κ_Ξ = 0.9968019520324009...

| M  | κ_Ξ^{(M)}     | err      |
|----|---------------|----------|
| 1  | 0.9982389680  | 1.44e-03 |
| 10 | 0.9970440935  | 2.42e-04 |
| 19 | 0.9969216709  | 1.20e-04 |
| 35 | 0.9968580527  | 5.61e-05 |
| 50 | 0.9968370161  | 3.51e-05 |
| 60 | 0.9968294687  | 2.75e-05 |

Monotonic decrease, positive tail, every partial sum's rigorous
1/(1+α_M²) bound contains the target (verified).

## 2. Tail rate [N]

Power-law fit over M = 10..60: **err ~ M^{-1.2}**.

Practical consequence: ~1000 zeros for 1e-6 accuracy. The tail is
tame — power-law, not exponential, not oscillatory.

## 3. Caveat [I]

This is the *spectral* convergence (M → ∞ at a = ∞), not the
*finite-a* κ_a. The finite-a scalar needs the H_a operator
eigenvalues (Lane A). But the M-tail is the right informant for
the a → ∞ limit: the high-frequency content that the a → ∞
certification must control behaves tamely.

## 4. Implication for the certification [I]

The phase-window tail budget (v13.967) is well-behaved. No
surprises lurk at high M — the sum converges cleanly and the
bound holds with room to spare. If the 6×6 interval computation
(v13.971, confirmed v13.972) certifies at fixed a, the a → ∞
tail will not fight the extension.

---

*Computed 2026-10-03 via the v13.965 reproducer at 40-digit precision.
Independent of the Lane A 6×6 interval work; intended as a downstream
input to the a → ∞ program.*
