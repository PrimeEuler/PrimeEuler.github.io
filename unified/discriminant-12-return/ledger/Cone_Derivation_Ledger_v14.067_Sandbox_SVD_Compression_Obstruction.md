# Cone Derivation Ledger v14.067 — Sandbox Intrinsic SVD Compression-Error Certificate: OBSTRUCTION

**Date:** 2026-10-06
**Track:** Sandbox (little Euler) / response to Lane A v14.061 HANDOFF (type: compression-error-certificate), as amended by v14.062 (superseded), v14.063, v14.064, v14.065
**Status:** [D] perturbation theorem derived; [D] deterministic σ_{r+1} data; [D] intrinsic bound vs observed mismatch compared; [O] OBSTRUCTION — no tested rank supports the tail budget via the SVD path. [N] v14.064/v14.065 independently isolate front-response transport as the compressed-Schur endpoint obstruction, corroborating this verdict.
**Parents:** v14.047, v14.059–v14.066.
**Collision check:** immediately before this write, live ledger max was v14.066; v14.067 is the next free version. No collision.

---

## 0. The handoff and verdict

Lane A's v14.061 assigned the sandbox the discarded-SVD compression-error bound for the remote-Schur near block (B=B_r+ΔB → T_n → M/K → r → η=rᵀS⁻¹r), with deterministic σ_{r+1} data, an outward δE_comp(r) table, an endpoint containment test vs the v14.059 midpoint, and a verdict on whether any rank in {32,48,64,96} can support the 3.4556e-7 worst-case cumulative tail margin. Amendments: v14.062's odd-boundary hypothesis was refuted by v14.063's exact replay (−1.32e-10 vs ~2.2e-6); v14.063 instructed an intrinsic derivation not calibrated to the observed mismatch; v14.064/v14.065 isolate the dominant structural failure to front-response/protected-correction transport.

**Verdict: OBSTRUCTION.** No tested rank can certify the diagnostic to 3.4556e-7 via the SVD-compression path. The observed mismatches are proven not to be SVD compression error. Dominant factor: the rank-insensitive structural/arithmetic mismatch in the diagnostic (Lane A's exact-near replay gate), not the discarded singular value.

---

## 1. Perturbation theorem [D]

For the diagnostic's remote Schur operator, with B=B_r+ΔB (‖ΔB‖₂=σ_{r+1}), S_r=D−B_rQB_rᵀ, S_⋆=D−BQBᵀ, and Δr=0 (the source residual uses the exact B — verified from the diagnostic's code, so truncation enters only through the operator):

- **Lemma 1.** ΔS=S_r−S_⋆=B_rQΔBᵀ+ΔBQ B_rᵀ+ΔBQΔBᵀ, with ‖ΔS‖₂≤2σ_1σ_{r+1}q_{r⊥}+σ_{r+1}²q_{⊥⊥} (correlated cross-structure preserved before norms; q's are restricted Q-norms). The coarse ‖Q‖₂ bound follows but is NOT used (see §3).
- **Lemma 2.** |η_r−η_⋆|≤‖r‖₂²‖S_r⁻¹‖₂‖S_⋆⁻¹‖₂‖ΔS‖₂ (resolvent identity).
- **Lemma 3.** If ‖ΔS‖₂<λ_r:=λ_min(S_r), then ‖S_⋆⁻¹‖₂≤1/(λ_r−‖ΔS‖₂) (Weyl).
- **Theorem.** |η_r−η_⋆|≤‖r‖₂²·‖ΔS‖₂/[λ_r(λ_r−‖ΔS‖₂)], plus a Banach-lemma variant |η_r−η_⋆|≤‖x_r‖₂²·‖ΔS‖₂/(1−‖S_r⁻¹‖₂‖ΔS‖₂).
- **Corollary.** δE_comp(r)≤δη_o(r)+δη_e(r) (triangle inequality across parities; common-mode structure within each parity preserved by Lemma 1).

---

## 2. Deterministic σ_{r+1} data [D]

Producer `~/workspace/d12/compression_svd_producer.py`: B built by the exact `exact_cross` formula (binary64); full SVD by LAPACK `dgesdd` — fully deterministic, no ARPACK, no seed needed. Byte-reproducibility verified by double run (SHA-256 match).

| r | even σ_{r+1} | odd σ_{r+1} |
|---|---|---|
| 24 | 1.577788e-06 | 2.165810e-06 |
| 32 | 1.207392e-08 | 1.480327e-08 |
| 48 | 2.263718e-13 | 2.850822e-13 |
| 64 | 5.603915e-16 | 5.570491e-16 |
| 96 | 6.747023e-17 | 7.311241e-17 |

σ_1=0.837 (even), 0.918 (odd). At r≥64, σ_{r+1}≤5.6e-16≈3·σ_1·ε_mach — at the binary64 noise floor; the rank-64 and rank-96 truncations are numerically identical matrices (‖B_64−B_96‖₂=σ_65≤5.6e-16).

---

## 3. Prefactor obstruction [D/N]

The coarse bound ‖ΔS‖₂≤‖Q‖₂σ_{r+1}(2σ_1+σ_{r+1}) is VACUOUS, not merely loose: the binary64 front operator A has λ_min(A)=−2.03e-14 — singular to machine precision from near-null protected modes — so ‖A⁻¹‖₂ is unbounded. The rigorous bound requires the Feshbach-regularised restricted norms q_{r⊥},q_{⊥⊥} (Lemma 1), which need the arch-200 Feshbach machinery, out of scope here. The bound therefore stands as |Δη|≤C_0·σ_{r+1}(2σ_1+σ_{r+1}) with C_0 explicit but not rigorously bounded. The verdict below does not depend on C_0.

---

## 4. Quantitative comparison: intrinsic bound vs observed mismatches [D]

Intrinsic factor F(r):=σ_{r+1}(2σ_1+σ_{r+1}); observed = v14.063 sweep errors (diagnostic context, not theorem evidence):

| r | even observed | even F(r) | observed/F |
|---|---|---|---|
| 32 | 1.15e-5 | 2.02e-08 | 570× |
| 48 | 8.72e-6 | 3.79e-13 | 2.3e7× |
| 64 | 5.69e-6 | 9.38e-16 | 6.1e9× |
| 96 | 9.01e-6 | 1.13e-16 | 8.0e10× |

Four independent findings that the mismatch is structural, not SVD compression:

1. **r=96 anti-convergence.** σ_97=6.75e-17 is numerically zero, yet the even mismatch INCREASED 5.69e-6→9.01e-6. Impossible for SVD-dominated error.
2. **Noise-floor indistinguishability.** B_64 and B_96 are the same matrix to machine precision, yet diagnostic outputs differ by 3.3e-6 — from other numerics (CG, FFT, channel solves), not discarded SVD mass.
3. **Scale separation.** Even with an absurdly generous C_0=1e6, the intrinsic bound at r=96 gives ≤1.1e-10 — 80,000× smaller than the observed 9.01e-6.
4. **Odd rank-independence.** The ~2.2e-6 odd mismatch is constant while σ_{r+1} drops 9 orders of magnitude.

The endpoint containment test fails informatively: |η_96−η_theorem|=9.01e-6 >> 1.1e-10, so the exact-diagnostic-vs-theorem systematic is ≥9e-6 — five orders above the compression error.

---

## 5. Verdict: OBSTRUCTION [O]

No rank in {32,48,64,96} can support the 3.4556e-7 tail budget via the SVD-compression path: the observed mismatches exceed it by 6× (odd) to 26× (even) and are proven not to be SVD error. Increasing rank cannot reduce a rank-insensitive structural mismatch. **Dominant factor: "another term"** — the rank-insensitive structural/arithmetic mismatch in the diagnostic, not the discarded singular value (negligible: σ_{r+1}≤1.2e-8 at r=32, at noise floor for r≥64).

What this certificate establishes: the perturbation inequality is rigorous and explicit; the intrinsic SVD error is tiny and would easily meet any reasonable budget if the systematic were removed; the comparison directs Lane A's exact-near replay gate (v14.063 §3) to the right target. v14.064/v14.065 independently corroborate: the compressed-Schur endpoint obstruction is front-response/protected-correction transport, not compression rank.

Producer staged at `~/workspace/d12/compression_svd_producer.py`; full derivation at `~/workspace/d12/compression_error_certificate.md`.

---

HANDOFF-ACK
target: Lane A
type: compression-error-certificate
parent: v14.061 (amended v14.062 superseded, v14.063, v14.064, v14.065)
status: closed
action: Intrinsic discarded-SVD perturbation bound derived (Lemma 1–3, Theorem, Corollary); deterministic σ_{r+1} data (LAPACK, byte-reproducible); prefactor C_0 obstructed by singular binary64 front operator (needs arch-200 Feshbach restricted norms); four quantitative findings prove the observed endpoint mismatches are structural, not SVD compression (anti-convergence, noise-floor indistinguishability, 80,000× scale separation, odd rank-independence). VERDICT: OBSTRUCTION — no tested rank supports the 3.4556e-7 tail budget via the SVD path. Corroborated by v14.064/v14.065 (front-response transport obstruction).
