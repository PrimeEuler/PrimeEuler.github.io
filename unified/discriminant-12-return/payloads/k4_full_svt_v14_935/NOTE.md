# k4 solid — full coupled SVT stability (v14.928 Sandbox handoff return)

**Gate.** v14.928 (gravity lane) handed Sandbox the full SVT problem for the frozen
action: gauge-fixed quadratic scalar + vector actions with lapse/shift eliminated
by their constraints, kinetic-matrix principal minors, high-k/low-k eigenfrequencies,
ghost/instability intervals, and an explicit verdict on the local window
eta in (3/8, 3/2]. No cosmology fitting. This note is the return.

**Frozen setup (parents v14.924/925/927/928, unchanged).**
S = ∫√−g [ R/(2κ) − C b^{2/3} (1 + ηJ) ], signature (+,−,−,−),
B^IJ = −g^{μν}∂_μφ^I∂_νφ^J, b = √(det B), J = tr(B²)/(trB)² − 1/3.
Background φ^I = z^I, a(τ) = τ/√3 at κC = 1, ρ = C/a², p = −ρ/3, H = 1/τ,
κρ = 3H², ä = 0. Cross-check constants: μ(η) = 4ρη/9; local speeds (v14.927)
c_T² = 2η/3, c_L² = −1/3 + 8η/9; tensor mass (v14.928) m_T² = (8/9)κρη = (8η/3)H².

## Method

ADM (N, N^i, h_ij) with the bulk density N√h [ R⁽³⁾ + K_ijK^ij − K² ] / (2κ).
For h = diag(A, A, B)(z): R⁽³⁾ = −2A''/(AB) + A'B'/(AB²) + A'²/(2A²B), derived from
the Christoffels and verified in the conformal, warped-product, and pure-gauge
limits. Machinery calibrated exactly on: the background density −3aȧ²/κ (whose
background equation is ȧ² = κC/3, v14.924), the TT kinetic coefficient
a³tr(γ̇²)/(8κ), and the TT gradient coefficient in Fourier average.
Solid expanded directly from B^IJ (sympy series in a bookkeeping ε, fields scaled
once at construction). Scalar gauge E = 0; vector gauge F_i = 0. Lapse Φ and
shifts eliminated by their own (derivative-free in the fields) Euler–Lagrange
equations. Eigen-analysis by exact state-space reduction of the frozen
Euler–Lagrange system (τ-dependence of all coefficients retained before
freezing at τ0; H = 1/τ0), not by determinant fitting.

## Validation web

1. Tensor sector of v14.928 reproduced independently (J = (1/9)trγ² + O(γ³),
   det B unperturbed at TT order, m_T² = (8η/3)H², η = 3/4 → 2H²).
2. Flat/no-metric limits of both matter sectors reproduce v14.927 exactly:
   L_T = (ρ/3)[ḟ² − (2η/3)f′²], L_L = (ρ/3)[ḟ² − (−1/3 + 8η/9)f′²] (a = 1 frame).
3. η = 0 reduces to v14.924's barotropic fluid: scalar ω₀² = −(1/3)k_phys²
   at high k (gradient instability), as required.
4. Scalar kinetic matrix is rank 1 on-shell (K_ψψ = K_ψP = 0 identically once
   κC = 1 and ȧ² = κC/3 are imposed; det K₂ = 0): exactly one propagating
   scalar dof, ψ purely auxiliary — the GR + solid dof count.
5. Friction comes out exactly 3H (B21 = 3·A22 at every sample point;
   oscillatory eigenvalues have Re λ = −3H/2).
6. The k → 0 gap of all three sectors coincides with the tensor mass (below) —
   homogeneous scalar/vector perturbations are homogeneous shears, so this is
   a physical identity, and three independent computations land on it.
7. Window boundary is sharp numerically: at k_phys/H = 100, ω₀² < 0 for
   η = 0.374 and > 0 for η = 0.376; at η = 3/8, ω₀² = H² at k_phys/H = 1000
   (gradient term identically zero).

## Results [D] (on the frozen background; k_phys = k/a)

Dispersion relations are exact in the adiabatic (frozen-coefficient) sense, with
the τ-dependence shown through H(τ) = 1/τ and k_phys(τ) = k/a(τ):

- Tensor: ω_T² = m_T² + k_phys²,  m_T² = (8η/3) H².  (v14.928, verified.)
- Vector (per transverse polarization):
  ω_V² = (8η/3) H² + (2η/3) k_phys².
  Kinetic coefficient after shift elimination is positive for every k > 0;
  the potential is pure gradient — the k → 0 gap enters through the
  k²-vanishing of the dressed kinetic term, not through a mass term.
- Scalar (single propagating dof; ψ slaved algebraically, ψ = α(k,τ)·P):
  ω_S² = (8η/3) H² + (−1/3 + 8η/9) k_phys²,
  with reduced kinetic coefficient A22(k) > 0 at every sampled k > 0
  (A22 ∝ k² with a positive constraint-dressing factor; no ghost).
  Low-k scalar modes are overdamped (pure decay) for η < 27/32 and
  underdamped with Re λ = −3H/2 for η > 27/32. At η = 3/8 exactly:
  ω_S² = H² at all k, λ = (−3 ± √5)H/2 — stable marginal point.

## Verdict

**The window survives.** Every η ∈ (3/8, 3/2] is ghost-free, gradient-stable,
and tachyon-free in all three sectors of the full coupled SVT system on the
k4 background. Both sound speeds are subluminal on the window
(c_T² = 2η/3 ≤ 1, c_L² = −1/3 + 8η/9 ≤ 1, equality at η = 3/2); the tensor
sector is luminal with positive mass². The local window of v14.925/927 is
therefore not narrowed by metric coupling, constraint elimination, or the
low-k sector.

**Negatives / scope.**
- η ≤ 3/8 fails, and the full analysis isolates the failure to exactly one
  place: the scalar gradient coefficient c_L² < 0 (high-k growing mode
  λ₊ ≈ |c_L| k_phys − 3H/2). No other sector or regime fails there.
- η > 3/2 (outside the asked window) remains linearly stable but both sound
  speeds exceed 1; recorded, not pursued.
- Linear theory on the exact background only. Nonlinear stability, backreaction,
  and any cosmology fitting are out of scope and untouched. The k = 0 scalar
  is the homogeneous background/gauge mode (constraint degenerates there);
  all statements are for k > 0 with the k → 0 limits as shown.
- Two superseded diagnostic routes (symbolic determinant of the unreduced
  system; determinant sampling fits against the rank-deficient kinetic matrix)
  produced spurious branches and were abandoned for the state-space route;
  they remain in the sandbox run directory, not in the payload.

## Reproducer

`run_all.sh` executes the payload chain in order:
tensor_check.py (tensor verification) → matter_sector.py (solid scalar) →
eh_scalar.py (EH scalar via ADM) → assemble.py (Fourier map, E = 0 gauge,
constraint elimination, kinetic matrix) → vector_sector.py (vector sector +
shift elimination) → scalar_statespace.py (scalar eigenvalues) →
final_checks.py (vector closed-form check to 6 digits; scalar boundary
sharpness). All headline numbers above are printed by the chain.

**Handoff:** → external-audit (verification of this return);
→ gravity lane (linear SVT gate closed on the Sandbox side; the window
(3/8, 3/2] stands as the coupled stability window).
