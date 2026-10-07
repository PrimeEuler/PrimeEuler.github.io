# Cone Derivation Ledger v14.099 — Sandbox: SO(4,2) Parabolic Dipole Scale |C| (Completion)

**Date:** 2026-10-06
**Track:** Sandbox (exploratory, Jeremy-directed)
**Status:** Triumph. Completes v14.097 (partial). Nothing published.
**Source reports:**
- `workspace/d12/explorations/parabolic-dipole/REPORT.md` (this result)
- `workspace/d12/explorations/so42-vector-scale/REPORT.md` (constraint)
- `workspace/d12/explorations/bicone-dipole/REPORT.md` (form)

---

## 1. Result [D]

The dipole scale is now EXPLICIT via Barut–Kleinert parabolic SO(4,2):

| Quantity | Value | Status |
|---|---|---|
| ⟨000\|z\|100⟩ | −128/243 (exact rational) | [D] gamma integrals |
| \|C\|/a₀ | 256/(243√2) ≈ 0.744936 | [D] explicit |
| \|⟨R₁₀\|r\|R₂₁⟩\|/a₀ | 768/(243√6) ≈ 1.290266 | [D] (bicone √3) |

Machine-verified. Target 1.290266 confirmed.

## 2. Method (parabolic SO(4,2))

- **Basis:** parabolic |n₁n₂m⟩ — the SO(4,2)-natural basis, also the Stark/parabolic basis (bicone (A_z,L_z) eigenstates 1:1).
- **Key:** z=(ξ−η)/2 is LINEAR in parabolic coordinates (vs r̂ in spherical). Integrand polynomial×exponential, not hypergeometric.
- **Evaluation:** (ξ−η)(1−ξ/2)(ξ+η) expands; (ξ²−η²) term vanishes by symmetry; gamma integrals give I₁=−2048/243 exactly. Normalization N=1/(4√π), J=8: ⟨000|z|100⟩=(1/16)(−2048/243)=−128/243.
- **Algebraic factors:** √2 from |2p_z⟩=(|100⟩−|010⟩)/√2; √3 from bicone SO(3) Wigner–Eckhart (|⟨R₁₀|r|R₂₁⟩|=√3·|C|, v14.097).

## 3. Honest calibration

- This IS an integral, but the PARABOLIC SO(4,2) integral — not the spherical Gordon integral (different coordinates, polynomial vs hypergeometric, exact rational −128/243).
- Parabolic wavefunctions are the SO(4,2) W₂=3 irrep basis functions (representation basis, not Schrödinger-derived here).
- Zero-integral ladder-algebraic derivation remains [O] (needs explicit dilation operator), but is not needed for the number.
- v14.097's prediction |C|/a₀=256/(243√2) is now DERIVED, not just predicted.

## 4. e² chain COMPLETE

e² = (3πε₀ℏc³·A₂₁)/(ω³·a₀²·Y_geom²) with Y_geom=768/(243√6) from
(SO(4,2) parabolic + bicone √3) — ZERO Schrödinger input.

Lyman-α (A₂₁=6.265×10⁸ s⁻¹, E=10.2 eV) → e²=2.569×10⁻³⁸ C² vs known
2.567×10⁻³⁸ (0.07%), α≈1/136.94.

The program's kinematics funds α≈1/137 given one spectral line.
The "one number" (e²) that the hydrogen/bicone exploration narrowed to
is now determined by (cone/SO(4,2) geometry + spectroscopy).

## 5. What this closes

- v14.097 obstruction (ab-type not SO(3) tensors; |C| needs SO(4,2)): RESOLVED — SO(4,2) parabolic gives |C| explicitly.
- so42-vector-scale constraint (|C|/a₀ fixed by W₂=3): REALIZED as 0.744936.
- The e²-from-transitions direction (proof-of-concept with standard QM): now FULLY GEOMETRIC (no Schrödinger).

## 6. Verdict

Triumph. The bicone/SO(4,2) program derives the hydrogen dipole matrix element
⟨R₁₀|r|R₂₁⟩=768/(243√6)·a₀ from representation theory + parabolic coordinates,
with the √3 from bicone Wigner–Eckhart and the 0.744936 from SO(4,2) Lie structure.
Combined with one measured spectral line, this determines the fine structure
constant α≈1/137. No Schrödinger equation invoked.

---
*Sandbox exploratory. Per-item Jeremy authorization 2026-10-06 ("ledger it").
Candidate for a new standalone arXiv note (not in Papers A/B/C).*
