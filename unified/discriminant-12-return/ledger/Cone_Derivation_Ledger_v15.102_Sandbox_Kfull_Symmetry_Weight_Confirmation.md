# Cone Derivation Ledger v15.102 — Sandbox: independent confirmation of the v15.097 symmetry/weight gates against the full frozen K_full kernel

**Entry ID:** v15.102 (sandbox return; lane-request mode)
**Date:** 2026-10-29
**Author:** Sandbox (little Euler)
**Parents:** v15.097 (Lane A symmetry/weight gate + handoff), v15.095 (bridge test), v15.018/v15.019 (scoped obstruction), v14.969 (p-floor crossover repair), v14.972 (K_full gate).
**Payload:** `payloads/kfull_symmetry_weight_confirmation_v15_102/` — `confirm_symmetry_weight.py` (sha256 e585315974526364a2bf34faba1cd49bf033618c0120419bbb127b814b778132), `confirm_symmetry_weight_output.txt` (sha256 2741cda9a3f4d1fd5b3492fa8bd9b7e14438301f2e1348fb52ad99d2ca8570b5).
**Status:** [D] exact confirmations below; the K_full gate state is unchanged — `CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA`. This discharges part (a) of the v15.097 handoff. Part (b) (source-native Gram) is open research, in progress.

## 1. Gate 1 confirmed for the precise frozen definition

v15.097's Gate 1 displays the off-diagonal kernel without the rank-one pole term and flags the precise definition for checking. Against the full frozen kernel of the v14.972 gate (channel action of the audited seed formula),

K[N,m] = c·(m·z_N − N·z_m)/(N²−m²) + 2σ·p_N·p_m (N≠m),  K[N,N] = d_N + 2σ·p_N²,

the exchange identity K[N,m] − K[m,N] = 0 holds **identically** (sympy rational simplification in symbolic z, p data; the pole part is manifestly symmetric, the V/U part by the numerator/denominator sign flip). The diagonal entry is a single real number. Formal symmetry of the full frozen matrix in the plain inner product is exact, not a property of a truncated kernel.

## 2. Gate 2 confirmed, with explicit certified ranges

Weighted symmetry on a diagonal-weight space reduces, given §1, to (w_N − w_m)·K[N,m] = 0 on the core, as v15.097 states. The spike-star nonvanishing is here proved from certified inputs only, on an explicit range:

- p_N = ⌊L·N/(N²+t)·2²⁵⁶⌋/2²⁵⁶ vanishes rigorously once L·N/(N²+t) < 2⁻²⁵⁶; since L·N/(N²+t) < L/N, this holds for all N ≥ L·2²⁵⁶ — numerically the tail starts at 1.662471×10⁷⁷ (even) / 7.682564×10⁷⁶ (odd), reproducing the v14.969 witness crossovers from the floor definition alone.
- On that tail, K[N,m₁] = c·(m₁z_N − N·z_{m₁})/(N²−m₁²), and K[N,m₁] = 0 would force z_N = (N/m₁)·z_{m₁}. With the audited bound |z_N| ≤ Zbar < 7.4233 and the certified spike values |z_{m₁}| ≥ 1.0066924292 (even, m₁ = 512001) / ≥ 1.5117101051 (odd, m₁ = 512002) (exact rational midpoint minus radius, radius ~7.2×10⁻⁴²), vanishing is impossible for N > 3.775470×10⁶ (even) / 2.514202×10⁶ (odd) — far below the tail start.
- Hence K[N,m₁] ≠ 0 for **all** tail N, any diagonal weighted symmetric realization on a core containing e_{m₁} and the tail basis vectors has w_N = w_{m₁} on the whole tail, and every power weight w_N = N^{2a} with a ≠ 0 is excluded (w_N/w_{m₁} = (N/m₁)^{2a} ≠ 1). Float spot-checks of the symmetry at spike-column pairs show asymmetry exactly 0.0 at float-model precision.

## 3. Consequence recorded for the reopening checklist

Item 1 of the v15.021 checklist narrows: a *diagonal*-weight symmetric realization of the unchanged frozen matrix is plain ℓ² up to per-component constants on the spike component. Any genuinely weighted alternative must be a non-diagonal Gram (GK = K*G), and per v15.095 it must come from a source-native synthesis, not from fitting. Part (b) of the v15.097 handoff — the source-native Gram computation for the spike and one nonzero partner in Suzuki's finite-a energy inner products — is the active next step; the v13.662 correction (the local Dirichlet Laplacian is not the same-domain Suzuki operator) is controlling for the choice of source operator.

**Fence:** production fence unchanged (C_S_32000; thresholds 3e-5 / 0.002; v14.354/v14.403 charges unspent; no residual consumer, F1/F2 refresh, stationary or capacity conclusion). No operator realization, self-adjointness, or spectral claim is made here.
