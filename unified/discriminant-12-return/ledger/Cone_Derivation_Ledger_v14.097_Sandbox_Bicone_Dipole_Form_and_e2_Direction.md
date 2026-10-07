# Cone Derivation Ledger v14.097 — Sandbox: Bicone Dipole Form (Partial) and e²-from-Transitions Direction

**Date:** 2026-10-06
**Track:** Sandbox (exploratory, Jeremy-directed)
**Status:** Partial triumph with precise obstruction. Nothing published.
**Source report:** `workspace/d12/explorations/bicone-dipole/REPORT.md` (sandbox-only)

---

## 1. Task

Derive the hydrogen dipole radial matrix element ⟨R₁₀|r|R₂₁⟩ = 768/(243√6)·a₀ ≈ 1.290266·a₀
from the bicone/SO(4,2) algebra — no Schrödinger wavefunctions, no radial integrals.
(Target value confirmed by independent numerical integration; used only as answer-check.)

## 2. Derived [D]: bicone funds the dipole's angular structure

States (bicone: cone1=(a₁,a₂), cone2=(b₁,b₂), N_a=N_b=n−1):
- |1s⟩ = |0,0,0,0⟩ (vacuum, j=0)
- |2p,m⟩ = triplet from |j=1/2⟩⊗|j=1/2⟩:
  m=+1: a₁†b₁†|0⟩, m=0: (a₁†b₂†+a₂†b₁†)/√2|0⟩, m=−1: a₂†b₂†|0⟩

By explicit ladder algebra (aᵢ|1⟩=|0⟩, machine-verified, no integrals):
- M[i,j,m] = ⟨1s|aᵢbⱼ|2p,m⟩ exhibits the exact Wigner–Eckhart vector
  selection rule δ_{q,−m} with algebraic value +1 — emerging from computation.
- Via SO(3) Wigner–Eckhart: **|⟨R₁₀|r|R₂₁⟩| = √3·|C|**, where C is the dipole
  length constant. The √3 and δ_{q,−m} pattern are bicone output.

## 3. Obstruction [D]: scale not in su(2)⊕su(2)

The ab-type (and a†b†-type) bilinears FAIL to form proper SO(3) vector
operators under L=J^a+J^b (L_z eigenvalues correct, [L_±,·] ladder relations
fail for every σ-pairing tried; machine-verified). Reason: Schwinger
lowering/raising ops are dual/conjugate spinors, not proper SU(2) tensors.

Hence r_q is not in the bicone's su(2)⊕su(2) enveloping algebra in simple
bilinear form. It lives in the larger SO(4,2) (Barut: dipole-as-generator),
whose Lie-algebraic normalization fixes C. That construction is not done here.

**Checkable prediction (not derivation):** the target 768/(243√6)·a₀ requires
|C|/a₀ = 256/(243√2) ≈ 0.7449. This is the number the Barut SO(4,2) vector-generator
construction must produce.

## 4. e²-from-transitions direction (proof-of-concept)

Parent thread established: e² follows from (measured A₂₁, ω) + geometric dipole via
A = ω³e²|⟨r⟩|²/3πε₀ℏc³. Using Lyman-α (A₂₁=6.265×10⁸ s⁻¹, E=10.2 eV) and the
STANDARD-QM radial element (not yet the cone's), obtained e²=2.569×10⁻³⁸ C²
vs known 2.567×10⁻³⁸ (0.07%), α≈1/136.94.

This validates the METHOD. The genuine cone-program result requires the bicone/SO(4,2)
to supply |C| algebraically (see §3 obstruction). When |C|/a₀≈0.7449 is derived
(not just predicted), e² becomes (cone geometry + one spectral line) with no
Schrödinger input.

## 5. Calibration

- [D, new]: bicone vector pattern (δ_{q,−m}, +1); |⟨R₁₀|r|R₂₁⟩|=√3|C|; ab-type
  tensor failure (obstruction).
- [S]: target 768/(243√6)·a₀ (Gordon); Barut–Kleinert SO(4,2) dipole (cited);
  SO(3) Wigner–Eckhart factors.
- [O]: |C|/a₀=256/(243√2) from explicit Barut SO(4,2) vector generator in
  bicone oscillators; full r_q with correct [L_i,r_j].

## 6. Verdict

Partial triumph with precise obstruction. The bicone derives the dipole's form
(√3, δ_{q,−m}) purely algebraically; the scale |C| awaits SO(4,2). The e²
determination is method-validated but scale-blocked pending |C|.

---
*Sandbox exploratory. Per-item Jeremy authorization 2026-10-06 ("right when it lands").
Candidate for a new standalone arXiv note (not in Papers A/B/C).*
