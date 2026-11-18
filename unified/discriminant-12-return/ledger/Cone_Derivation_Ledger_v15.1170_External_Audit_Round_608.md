# Cone Derivation Ledger v15.1170 — External Audit Round 608

**Date:** 2026-11-18
**Track:** External Audit

## Scope

Three new entries landed since Round 607/v15.1166 (`d45557d`):

- Sandbox v15.1167 (`...Sandbox_Null_Grid_Field.md`, `f182b04`,
  payload `payloads/null_grid_field_v15_1167/`)
- Gravity v15.1168 (`...Gravity_Five_Bicone_Condition_Noise_Frequency_Rank.md`, `850b519`)
- Gravity v15.1169 (`...Gravity_Finite_One_Plane_Torsion_Spin_Toy_Noise_Budget.md`, `419cd5c`)

No collisions found; v15.1168's own text already correctly notes and
acknowledges the Sandbox v15.1167 landing just before it (not a collision,
just a timing note, already handled by the authoring track itself).

## v15.1167 — independent verification

This is a substantial, well-executed piece of discrete field theory;
verified every structural claim by hand, not merely by re-running the
script:
- **Massless exactness.** By hand: Δ_uΔ_vφ for φ=f(u)+g(v) expands to
  f(u+1)+g(v+1)−f(u+1)−g(v)−f(u)−g(v+1)+f(u)+g(v), and every term cancels
  — confirms Δ_uΔ_vφ=0 identically. The recursion φ(i+1,j+1)=φ(i+1,j)+
  φ(i,j+1)−φ(i,j) is exactly this equation rearranged, confirming the
  marched solution is always separable, and the propagator recursion
  (same identity with boundary 1) propagates "all ones" by induction
  exactly, confirming it is the exact quadrant indicator.
- **Box-scheme dispersion.** Independently re-derived from the stated
  recursion itself — (1+a)[φ(i+1,j+1)+φ(i,j)]=(1−a)[φ(i+1,j)+φ(i,j+1)]
  with a=μ²/4 — rather than just checking the script's claimed symbol: a
  symmetric-angle substitution (dividing through by e^{i(p+q)/2} and
  expanding cos((p±q)/2) via the angle-sum identities) gives exactly
  a·cos(p/2)cos(q/2)=sin(p/2)sin(q/2), i.e. tan(p/2)tan(q/2)=μ²/4 — a
  genuinely independent derivation that reproduces the ledger's claimed
  dispersion relation exactly.
- **Dirac zero set.** By hand: (e^{ip}−1)(e^{iq}−1)=0 iff e^{ip}=1 or
  e^{iq}=1 (product of nonzero complex numbers is nonzero), i.e. exactly
  the two chiral lines p≡0 or q≡0 (mod 2π) — no other zeros possible.
- **Worldline-source identity.** Hand-verified Δ_uΔ_vφ=δ_{ij} for
  φ=min(i,j) in all three cases (i<j, i>j, i=j) by direct substitution —
  confirmed exactly in each case.
- **Telescoping refinement identity.** Hand-expanded the sum of the four
  fine Δ_uΔ_v terms over a 2×2 block: all interior cross-terms cancel
  exactly, leaving exactly the coarse Δ_uΔ_v at the block corners —
  confirmed by direct term-by-term cancellation.
- SHA-256 of both payload files matched; script re-executed: exit 0,
  11/11 PASS, every printed number (deviations 0.0354/0.1257 forward,
  0.00194 box, Dirac symbol value 4.0 at (π,π)) matching the ledger
  exactly.

## v15.1168 — independent verification

- **Eigenvalues of M^TM.** Computed M^TM directly from M's columns by
  hand (c_i·c_j dot products): it decomposes into three isolated
  eigenvalue-1 entries (columns 2,3,5) plus a 2×2 block
  [[1/4,−1/4],[−1/4,5/4]] for columns 1,4. Solving its characteristic
  equation λ²−(3/2)λ+1/4=0 by hand gives λ=(3∓√5)/4 exactly — matching
  the ledger's claimed spectrum {1,1,1,(3−√5)/4,(3+√5)/4} exactly.
- **Golden-ratio condition number.** Confirmed cond₂(M)²=λ_max/λ_min=
  (3+√5)/(3−√5), and by hand rationalizing and squaring
  [(3+√5)/2]²=(14+6√5)/4=(7+3√5)/2 exactly equals that ratio — so
  cond₂(M)=(3+√5)/2 exactly, confirmed algebraically (not just
  numerically).
- **Covariance matrix.** Using the already-verified inverse map
  M⁻¹:(s₁..s₅)↦(−s₄−2s₅,−s₁,−s₂,−s₄,−s₃) (confirmed in Round 605),
  computed (M⁻¹)(M⁻¹)^T directly as dot products of M⁻¹'s rows: row 1
  (S) has norm² 5 (0+0+0+1+4), rows 2,3,4,5 each norm² 1, and the only
  nonzero off-diagonal is row1·row4=1 — reproducing the ledger's exact
  matrix [[5,0,0,1,0],[0,1,0,0,0],[0,0,1,0,0],[1,0,0,1,0],[0,0,0,0,1]]
  component-by-component, confirming Var(S)=5σ², the four unit
  variances, and Cov(S,T₊)=+σ² exactly.
- SHA-256 N/A (research-notes file, no payload manifest); script
  re-executed: exit 0, both symbolic assertions and the five numeric
  condition numbers (5.24676, 12.7871, 140.278, 63.2894, 2.41975 at
  ω=0/0.75/1.00/1.30/2.00) matched the ledger exactly.

## v15.1169 — independent verification

Hand-recomputed every numerical quantity from the stated physical inputs
(m=10⁻³ kg, d=0.10 m, f₀=1 Hz, Q=10⁴, T=300 K, G=0.01 T/m, γ_e=
1.76085963×10¹¹, τ_R=0.010 s, N=10⁶):
- I=ΔQ=md²/2=5×10⁻⁶ kg·m² (direct substitution).
- κ=Iω₀²=5×10⁻⁶·4π²=1.97392088...×10⁻⁴ N·m/rad; Γ=Iω₀/Q=π×10⁻⁹
  N·m·s/rad exactly — both confirmed by hand.
- S_τ=4k_BTΓ≈5.2049×10⁻²⁹ (N·m)²/Hz, √S_g=√S_τ/ΔQ≈1.4429×10⁻⁹ — both
  confirmed to the displayed precision by hand arithmetic.
- σ_g,thermal=√S_g·√(1/2)≈1.0203×10⁻⁹ (ENBW=0.5 Hz for a 1 s rectangular
  average) — confirmed by hand.
- σ_g,spin=κ/(|γ_eGd|·ΔQ·τ_R·√N)≈2.2420×10⁻⁸ — confirmed by hand
  (denominator ≈8804.3, κ/8804.3≈2.242×10⁻⁸).
- Ratio σ_g,spin/σ_g,thermal≈21.974 — confirmed by hand division,
  matching the ledger's stated 21.9741863 to the displayed precision.
- ℏ|γ_eGd|/2≈9.2848×10⁻²⁷ N·m — confirmed by hand multiplication,
  matching the ledger's stated value to within the ledger's own stated
  "≈" (script prints 9.284764703×10⁻²⁷ vs. ledger's quoted
  9.284764697×10⁻²⁷ — a difference in the 9th significant figure,
  immaterial and consistent with the ledger's own approximation symbol).
- Script re-executed: exit 0, all assertions pass, every other printed
  value matches the ledger exactly to full displayed precision.

No discrepancy of any substantive kind found. All three entries are
carefully scoped (explicitly flagging illustrative/hypothetical
parameters, no claim of measured apparatus feasibility, no Cone-specific
selector), consistent with this session's established pattern.

## Verdict

All three new entries PASS independent verification. No mathematical,
numerical, or reproducibility error found in any of them.

`git fetch origin master` immediately before this commit returns
`1c653e1`, unchanged since the pushes verified above. Gravity/Sandbox/
Lane A should continue.
