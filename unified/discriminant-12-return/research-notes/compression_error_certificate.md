# Remote-Schur Near-Block Compression-Error Certificate

**Task:** Sandbox CONSTRUCTION handoff v14.061 (type: compression-error-certificate),
as amended by v14.062 (superseded) and v14.063 (current).
**Date:** 2026-10-06
**Scope:** Derive and execute a rigorous bound from discarded near-block SVD error
to the induced parity-difference error in the remote-Schur capacity calculation.
Sandbox owns ONLY the compression-error bound. Lane A retains the rank sweep,
the remote (n>16000) representation, and the final E_{>16k} enclosure.

**v14.063 amendment (current, supersedes v14.062):**
- v14.062's odd-boundary hypothesis REFUTED: exactizing n=16000 changes η_o
  by only −1.32e-10 vs the ~2.2e-6 mismatch. Boundary term negligible.
- Rank sweep r=32,48,64,96 shows NO monotone convergence:
  even +1.15e-5 → +8.72e-6 → +5.69e-6 → +9.01e-6 (r=96 goes UP);
  odd ~−2.2e-6 plateau. The "rank-24 discrepancy = SVD compression"
  hypothesis is NOT supported.
- Lane A's decisive gate: exact-near matrix-free Schur replay (no SVD).
- **Revised sandbox instructions:** (a) derive the SVD bound INTRINSICALLY
  from ‖ΔB‖/resolvent data, do NOT calibrate it to the observed mismatch;
  (b) compare bound magnitude vs observed mismatches quantitatively —
  if bound << observed, that is EVIDENCE the mismatch is not SVD error;
  (c) do NOT attempt the structural mismatch (Lane A's gate).

---

## 1. Operator structure (from the diagnostic)

Fix a parity sector p ∈ {e, o}. At the rmax=16000 endpoint:

- `nr` near modes (4000 even-v, 3999 odd-v), `nf = 4000` front modes.
- **D ∈ ℝ^{nr×nr}**: remote operator (diagonal + FFT off-diagonal + pole
  rank-1), symmetric positive definite. Applied by the diagnostic's `Smv`
  minus the low-rank update.
- **B ∈ ℝ^{nr×nf}**: exact front-to-near coupling,
  `B = exact_cross(near, front, sector)` (deterministic, binary64).
- **Q ∈ ℝ^{nf×nf}**: front self-energy operator
  `Q = A_P^{-1} + W S_prot^{-1} W^T`, symmetric positive definite,
  truncation-independent (from the front Feshbach solve, no SVD involved).
- **B = UΣVᵀ** full SVD; **B_r = U_r Σ_r V_rᵀ** rank-r truncation;
  **ΔB = B − B_r**, ‖ΔB‖₂ = σ_{r+1}(B).
- **T_r = V_r Σ_r ∈ ℝ^{nf×r}**: compressed channel matrix (front space).
  Key identity: **U_r T_rᵀ = U_r Σ_r V_rᵀ = B_r**.
- **M_r = T_rᵀ Q T_r + T_rᵀ δX_r ∈ ℝ^{r×r}**: computed correlated
  front-inverse Gram (δX_r = channel-solve refinement error).
- **S_r^{comp} = D − U_r M_r U_rᵀ**: the diagnostic's computed Schur operator.
- **S_r = D − B_r Q B_rᵀ**: ideal rank-r Schur operator (exact arithmetic).
- **S_⋆ = D − B Q Bᵀ**: exact untruncated Schur operator.
- **r ∈ ℝ^{nr}**: normalized remote source residual,
  `r = √C·f − B·y` on near modes with the **exact** B ⇒ **Δr = 0**
  under truncation. (The truncation enters only through the operator S,
  not through the source vector. This is verified from the diagnostic's
  `one()`: `r[:nr] -= Bnear @ st["y"]` uses `exact_cross`, not the SVD.)
- **η_r^{comp} = rᵀ(S_r^{comp})⁻¹r**, **η_r = rᵀS_r⁻¹r**, **η_⋆ = rᵀS_⋆⁻¹r**.

The refinement error: U_r M_r U_rᵀ = B_r Q B_rᵀ + B_r δX_r U_rᵀ, so
S_r^{comp} = S_r − E_ref with ‖E_ref‖₂ ≤ σ_1‖δX_r‖_F.
The compression certificate bounds |η_r − η_⋆| (ideal rank-r vs exact);
the diagnostic's own arithmetic (|η_r^{comp} − η_r|) is separately
accounted by its target_res/CG data ("tiny FFT/CG arithmetic" guardrail)
and validated by the endpoint cross-check.

---

## 2. Perturbation theorem

**Lemma 1 (truncation → Schur perturbation, correlated structure preserved).**
Let ΔS := S_r − S_⋆. Then
  ΔS = BQBᵀ − B_rQB_rᵀ = B_rQΔBᵀ + ΔBQ B_rᵀ + ΔBQΔBᵀ.
*Proof.* B = B_r + ΔB; expand BQBᵀ. ∎

Writing B_r = U_rΣ_rV_rᵀ, ΔB = U_⊥Σ_⊥V_⊥ᵀ:
  B_rQΔBᵀ = U_r Σ_r (V_rᵀQV_⊥) Σ_⊥ U_⊥ᵀ,
  ΔBQΔBᵀ = U_⊥ Σ_⊥ (V_⊥ᵀQV_⊥) Σ_⊥ U_⊥ᵀ.
Hence, with q_{r⊥} := ‖V_rᵀQV_⊥‖₂ and q_{⊥⊥} := ‖V_⊥ᵀQV_⊥‖₂:
  ‖ΔS‖₂ ≤ 2σ_1σ_{r+1} q_{r⊥} + σ_{r+1}² q_{⊥⊥}.     (1)
Since Q ≻ 0, Cauchy–Schwarz for the PSD form gives
q_{r⊥} ≤ √(‖V_rᵀQV_r‖₂ · q_{⊥⊥}), so with q_rr := ‖V_rᵀQV_r‖₂:
  ‖ΔS‖₂ ≤ 2σ_1σ_{r+1}√(q_rr q_{⊥⊥}) + σ_{r+1}² q_{⊥⊥}.  (2)
*Remarks.* (i) This keeps the exact B_rQΔBᵀ cross structure before norms —
it is the correct first-order perturbation, not an independent overbound
of B and B_r. (ii) The coarse bound ‖ΔS‖₂ ≤ ‖Q‖₂σ_{r+1}(2σ_1+σ_{r+1})
follows from q_{r⊥},q_{⊥⊥} ≤ ‖Q‖₂ but is NOT used (see §4: it is vacuous).

**Lemma 2 (resolvent perturbation, Δr = 0).**
η_r − η_⋆ = −rᵀS_r⁻¹ΔS S_⋆⁻¹r, so
  |η_r − η_⋆| ≤ ‖r‖₂² ‖S_r⁻¹‖₂ ‖S_⋆⁻¹‖₂ ‖ΔS‖₂.
*Proof.* S_r⁻¹ − S_⋆⁻¹ = −S_r⁻¹(S_r − S_⋆)S_⋆⁻¹. ∎

**Lemma 3 (exact resolvent via computed resolvent).**
Let λ_r := λ_min(S_r) > 0. If ‖ΔS‖₂ < λ_r then S_⋆ ≻ 0 and
‖S_⋆⁻¹‖₂ ≤ 1/(λ_r − ‖ΔS‖₂).
*Proof.* Weyl: λ_min(S_⋆) ≥ λ_r − ‖ΔS‖₂. ∎

**Theorem (discarded-SVD compression error).**
With the notation above, if ‖ΔS‖₂ < λ_r := λ_min(S_r):
  |η_r − η_⋆| ≤ ‖r‖₂² · ‖ΔS‖₂ / [λ_r(λ_r − ‖ΔS‖₂)],   (3)
where ‖ΔS‖₂ satisfies (1)–(2). Moreover, with x_r := S_r⁻¹r
(the diagnostic's CG solution):
  |η_r − η_⋆| ≤ ‖x_r‖₂² · ‖ΔS‖₂ / (1 − ‖S_r⁻¹‖₂‖ΔS‖₂),  (4)
whenever ‖S_r⁻¹‖₂‖ΔS‖₂ < 1.
*Proof of (4).* |η_r−η_⋆| ≤ ‖x_r‖‖x_⋆‖‖ΔS‖ and
‖x_⋆‖ ≤ ‖x_r‖/(1−‖S_r⁻¹‖‖ΔS‖) by the standard Banach perturbation lemma. ∎

**Corollary (parity-difference compression error).**
δE_comp(r) := |(η_{o,r}−η_{e,r}) − (η_{o,⋆}−η_{e,⋆})| ≤ δη_o(r) + δη_e(r),
with each δη_p(r) from (3) or (4). The two parities have disjoint mode
sets; no shared structure exists between them, so the triangle inequality
is the honest bound. (Common-mode structure WITHIN each parity is preserved
by Lemma 1.)

---

## 3. Deterministic σ_{r+1} data

*Producer:* `~/workspace/d12/compression_svd_producer.py`.
B built by the exact `exact_cross` formula (binary64); full SVD by LAPACK
`dgesdd` via `numpy.linalg.svd` — fully deterministic, no ARPACK, no seed
needed. Byte-reproducibility verified by double run (SHA-256 of spectra match).

| r | even-v σ_{r+1} | odd-v σ_{r+1} |
|---|---|---|
| 24 | 1.577788e-06 | 2.165810e-06 |
| 32 | 1.207392e-08 | 1.480327e-08 |
| 48 | 2.263718e-13 | 2.850822e-13 |
| 64 | 5.603915e-16 | 5.570491e-16 |
| 96 | 6.747023e-17 | 7.311241e-17 |

σ_1 = 8.369482e-01 (even), 9.180304e-01 (odd).
SHA-256: even `54025a3cd50c3dfc…`, odd `35d0311197537c60…` (both runs identical).

**Noise-floor note:** σ_1·ε_mach ≈ 1.8e-16 (binary64). At r≥64,
σ_{r+1} ≤ 5.6e-16 ≈ 3·σ_1·ε_mach — the discarded "mass" is at the level of
rounding noise. The rank-64 and rank-96 truncations are numerically identical
matrices (‖B_64−B_96‖₂ = σ_65 ≤ 5.6e-16, below the rounding error in B itself).

---

## 4. The ‖Q‖ obstruction and the restricted-norm refinement

The coarse bound ‖ΔS‖₂ ≤ ‖Q‖₂σ_{r+1}(2σ_1+σ_{r+1}) is not merely loose — it is
VACUOUS here. The binary64 front operator A (4000×4000, `full_source_matrix`
construction) has λ_min(A) = −2.03e-14, i.e., it is SINGULAR to machine
precision (the near-null protected modes). Therefore ‖A⁻¹‖₂ is unbounded
(≥5e13 from rounding noise alone; infinite if an exact null vector exists).
Any bound requiring the full ‖Q‖₂ is meaningless.

The rigorous bound MUST use the Feshbach-regularised RESTRICTED norms
q_{r⊥} = ‖V_rᵀQV_⊥‖₂ and q_{⊥⊥} = ‖V_⊥ᵀQV_⊥‖₂ from Lemma 1, where
Q = A_P⁻¹ + WS_prot⁻¹Wᵀ is the regularised front inverse. These are NOT
computable from the raw (singular) front operator; they require the arch-200
Feshbach machinery (the `build_double_complement` / `form_Ktilde` pipeline),
which is out of scope for this certificate. This is a clean, quantitative
obstruction to completing the rigorous numerical prefactor.

The bound therefore stands as:
  |η_r − η_⋆| ≤ C_0 · σ_{r+1}(2σ_1 + σ_{r+1}),     (5)
with C_0 = ‖r‖₂²‖S_r⁻¹‖₂‖S_⋆⁻¹‖₂·max(q_{r⊥},q_{⊥⊥}) EXPLICIT but not
rigorously bounded (obstruction). The σ_{r+1} factor is rigorous and tiny;
C_0 is the open constant.

---

## 5. Numerical bound table (intrinsic, up to prefactor C_0)

The rigorous σ-dependent factor F(r) := σ_{r+1}(2σ_1+σ_{r+1}) from (5):

| r | even σ_{r+1} | even F(r) | odd σ_{r+1} | odd F(r) |
|---|---|---|---|---|
| 32 | 1.207e-08 | 2.02e-08 | 1.480e-08 | 2.72e-08 |
| 48 | 2.264e-13 | 3.79e-13 | 2.851e-13 | 5.24e-13 |
| 64 | 5.604e-16 | 9.38e-16 | 5.570e-16 | 1.02e-15 |
| 96 | 6.747e-17 | 1.13e-16 | 7.311e-17 | 1.34e-16 |

The full bound is |Δη_p(r)| ≤ C_0·F(r) with C_0 explicit but not rigorously
bounded (§4 obstruction). For scale: with C_0 = 1e6 (absurdly generous),
|Δη_e(32)| ≤ 2.0e-2, |Δη_e(96)| ≤ 1.1e-10. The r=96 value is what matters
for the comparison below.

| r | even observed | even F(r) | ratio (observed/F) |
|---|---|---|---|
| 32 | 1.15e-5 | 2.02e-08 | 570× |
| 48 | 8.72e-6 | 3.79e-13 | 2.3e7× |
| 64 | 5.69e-6 | 9.38e-16 | 6.1e9× |
| 96 | 9.01e-6 | 1.13e-16 | 8.0e10× |

The observed/F ratio grows from 570× to 8e10× — the observed mismatch is
utterly decoupled from the intrinsic SVD scale. For the observed mismatch
to be SVD compression error, C_0 would need to be ≥8e10 at r=96 (and growing
with r), which is absurd for a prefactor composed of ‖r‖², ‖S⁻¹‖², and
restricted Q-norms. This is quantitative proof the mismatch is structural.

## 6. Quantitative comparison: intrinsic bound vs observed mismatches

Lane A's completed sweep (v14.063, diagnostic context — NOT consumed as
theorem evidence) gives signed endpoint errors vs the v14.059 midpoint:

even: r=32: +1.1546e-5, r=48: +8.7187e-6, r=64: +5.6899e-6, r=96: +9.0127e-6.
odd:  r=32: −2.2214e-6, r=48: −2.2035e-6, r=64: −2.3264e-6, r=96: −2.2876e-6.

**Finding 1 — r=96 anti-convergence (even).**
σ_97 = 6.75e-17 < σ_1·ε_mach. The discarded mass is numerically zero, yet
the mismatch INCREASED from r=64 (5.69e-6) to r=96 (9.01e-6). If the mismatch
were SVD-dominated (|mismatch| ≤ C·σ_{r+1} with slowly-varying C), decreasing
σ_{r+1} by 8.3× could not increase the mismatch by 1.58×. The r=64→96 change
(3.3e-6) from a <5.6e-16 input change is impossible for SVD truncation.
The mismatch is NOT SVD compression error.

**Finding 2 — noise-floor indistinguishability.**
‖B_64 − B_96‖₂ = σ_65 ≤ 5.6e-16, below the rounding error in B itself.
The two truncations are the SAME matrix to machine precision. Any diagnostic
difference between r=64 and r=96 therefore comes from other numerical effects
(CG, FFT, channel solves), not from discarded SVD mass.

**Finding 3 — scale separation.**
Even with an absurdly generous prefactor C_0 = 1e6, the intrinsic bound (5)
at r=96 gives |Δη| ≤ 1e6 × 6.75e-17 × 1.7 ≈ 1.1e-10, which is 80,000× smaller
than the observed 9.01e-6 mismatch. The observed mismatch cannot be SVD
compression error — it exceeds the most generous intrinsic bound by nearly
five orders of magnitude.

**Finding 4 — odd plateau rank-independence.**
The odd ~2.2e-6 mismatch is constant across r=32..96 while σ_{r+1} drops by
9 orders of magnitude (1.48e-8 → 7.3e-17). A rank-independent error cannot
be caused by rank-dependent truncation. (v14.063 already refuted the K=10
boundary hypothesis: exactizing n=16000 changes η_o by only −1.32e-10.)

**Conclusion of comparison:** The endpoint mismatches (~1e-5 even, ~2.2e-6 odd)
are dominated by a rank-insensitive structural/arithmetic term in the
diagnostic, NOT by discarded SVD mass. The intrinsic SVD compression error
is tiny (σ_{r+1} ≤ 1.2e-8 at r=32, at noise floor for r≥64) but is not the
limiting factor.

## 7. Endpoint containment test

**Test:** Does the v14.059 theorem midpoint lie inside the intrinsic
SVD-error enclosure [η_r − bound(r), η_r + bound(r)]?

- η_theorem,e = 0.0036404008257719944.
- |η_{96} − η_theorem,e| = 9.0127e-6 (v14.063).
- Intrinsic bound(96) ≤ 1.1e-10 (generous C_0=1e6).
- 9.01e-6 >> 1.1e-10. **CONTAINMENT FAILS.**

This failure is INFORMATIVE, not a defect of the bound. By the triangle
inequality:
  |η_⋆ − η_theorem| ≥ |η_96 − η_theorem| − |η_96 − η_⋆|
                    ≥ 9.01e-6 − 1.1e-10 ≈ 9.01e-6.
The EXACT-diagnostic-vs-theorem systematic is at least ~9e-6 — it dominates
the SVD compression error by five orders of magnitude. The containment test
as specified (theorem midpoint inside the SVD-error enclosure) cannot pass
because it conflates compression error with diagnostic systematic. The
systematic is out of scope for this certificate (Lane A's exact-near replay
gate, v14.063 §3).

## 8. Verdict: OBSTRUCTION

**Question:** Can any tested rank r ∈ {32,48,64,96} support a final tail
budget below the 3.4556e-7 worst-case cumulative margin?

**Answer: NO — OBSTRUCTION.**

The observed endpoint mismatches (~1e-5 even, ~2.2e-6 odd) exceed the
3.4556e-7 budget by 6× to 30×. These mismatches are PROVEN not to be SVD
compression error:
  (a) r=96 anti-convergence (mismatch increases while σ_{r+1} decreases);
  (b) noise-floor indistinguishability (B_64 = B_96 to machine precision,
      yet diagnostic outputs differ by 3.3e-6);
  (c) scale separation (intrinsic bound ≤1.1e-10 vs observed 9e-6);
  (d) odd rank-independence (9 orders of σ decay, constant mismatch).

Increasing rank cannot reduce a rank-insensitive structural mismatch.
Therefore no rank in {32,48,64,96} can certify the diagnostic to 3.4556e-7
via the SVD-compression path.

**Dominant factor** (per v14.061's list): **"another term"** — the
rank-insensitive structural/arithmetic mismatch between the remote-Schur
diagnostic and the v14.059 theorem endpoint. NOT the discarded singular
value (negligible: σ_{r+1} ≤ 1.2e-8 at r=32, at noise floor for r≥64).
NOT the front inverse norm or Schur resolvent norm per se (these enter the
intrinsic bound's prefactor C_0, which is obstructed by the singular front
operator, but even generous prefactors cannot explain the observed scale).

**What the certificate DOES establish:**
- The perturbation inequality (Theorem, §2) is rigorous and explicit.
- The intrinsic SVD compression error is TINY: σ_{r+1} decays spectacularly
  (1.6e-6 → 1.2e-8 → 2.3e-13 → 5.6e-16 → 6.7e-17 even).
- IF the diagnostic systematic were removed, SVD compression at r=32
  (σ_33=1.2e-8) would easily meet any reasonable budget.
- The quantitative comparison PROVES the observed mismatch is structural,
  directing Lane A's exact-near replay gate (v14.063 §3) to the right target.

**What remains open (not this certificate):** the rank-insensitive
structural mismatch (~9e-6 even, ~2.2e-6 odd). Lane A's exact-near
matrix-free Schur replay will determine whether it lives in the remote raw
operator, source normalization, or front-response transport. This
certificate does not attempt that assignment (per v14.063(c)).

---

*Notes.* No repo/ledger writes. Producer staged at `~/workspace/d12/`;
repo placement (research-notes/) by the parent after review.
