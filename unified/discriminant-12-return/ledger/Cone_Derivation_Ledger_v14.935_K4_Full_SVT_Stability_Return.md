# Ledger v14.935 — K4 Full SVT Stability Return (Sandbox → v14.928 handoff)

**Gate:** Sandbox return on the v14.928 handoff: full SVT decomposition of the
frozen k4 solid action, lapse/shift eliminated by constraints, verdict on
whether any η in the local window (3/8, 3/2] survives full stability.
**Parents:** v14.924 (fluid completion), v14.925 (elastic J), v14.927 (local
phonons), v14.928 (coupled tensor gate + this handoff). Parallel lane work
v14.932/933 (sector decay computations) is complementary; nothing here
modifies Lane A / Suzuki / far-production files.
**Payload:** `payloads/k4_full_svt_v14_935/` (NOTE.md + run_all.sh + 7 scripts).

## Frozen setup

S = ∫√−g [R/(2κ) − C b^(2/3) (1 + ηJ)], signature (+,−,−,−),
B^IJ = −g^{μν}∂_μφ^I∂_νφ^J, b = √(det B), J = tr(B²)/(trB)² − 1/3;
background φ^I = z^I, a(τ) = τ/√3 at κC = 1, ρ = C/a², p = −ρ/3, H = 1/τ,
κρ = 3H². No cosmology fitting was performed or needed.

## Method [D]

ADM density N√h [R⁽³⁾ + K_ijK^ij − K²]/(2κ); for h = diag(A, A, B)(z),
R⁽³⁾ = −2A''/(AB) + A'B'/(AB²) + A'²/(2A²B) derived from the Christoffels and
limit-verified (conformal / warped / pure-gauge). Machinery calibrated exactly:
background density −3aȧ²/κ; TT kinetic a³tr(γ̇²)/(8κ); TT gradient in Fourier
average. Solid expanded from B^IJ directly. Gauges: scalar E = 0, vector
F_i = 0. Φ and shifts eliminated by their own equations. Eigen-analysis by
exact state-space reduction of the τ-dependent frozen Euler–Lagrange system.

## Validation

Tensor sector of v14.928 independently reproduced. Flat limits of both matter
sectors reproduce v14.927 exactly. η = 0 reproduces v14.924 (ω² = −k_phys²/3,
high k). Scalar kinetic matrix is rank 1 on-shell (K_ψψ = K_ψP = 0 identically
under κC = 1, ȧ² = κC/3) — one propagating scalar dof, ψ auxiliary, matching
the GR + solid count. Friction is exactly 3H at every sample point (oscillatory
Re λ = −3H/2). Window edge sharp: ω₀² changes sign between η = 0.374 and
0.376 at k_phys/H = 100; η = 3/8 gives ω₀² = H² at k_phys/H = 1000.

## Results [D]

With k_phys = k/a and the common gap m² = (8η/3)H² = (8/9)κρη:

- Tensor: ω² = m² + k_phys² (v14.928, verified here).
- Vector (each transverse polarization): ω² = m² + (2η/3) k_phys².
  Kinetic coefficient positive for all k > 0; potential pure gradient — the
  k → 0 gap enters through the dressed kinetic term.
- Scalar (one dof): ω² = m² + (−1/3 + 8η/9) k_phys².
  Reduced kinetic coefficient positive at every sampled k > 0 (no ghost).
  Low-k modes overdamped for η < 27/32, underdamped (Re λ = −3H/2) above.
  At η = 3/8: ω² = H² at all k, λ = (−3 ± √5)H/2, stable marginal point.

The shared k → 0 gap is the homogeneous-shear identity: at zero momentum all
three sectors are the same elastic deformation, and three independent
computations land on m².

## Verdict [D]

**Every η in (3/8, 3/2] survives full coupled SVT stability** — no ghosts, no
gradient instability, no tachyon in any sector; sound speeds subluminal on
the window (c_T² = 2η/3 ≤ 1, c_L² = −1/3 + 8η/9 ≤ 1, equality at η = 3/2).
Metric coupling and constraint elimination do not narrow the local window of
v14.925/927.

## Negatives / scope

η ≤ 3/8 fails in exactly one place: the scalar gradient coefficient
c_L² < 0 (growing mode λ₊ ≈ |c_L|k_phys − 3H/2 at high k); no other sector
or regime fails there. η > 3/2 is linearly stable but superluminal in both
sound speeds (recorded, not pursued). Linear theory on the exact background
only; nonlinear stability and backreaction untouched; the k = 0 scalar is
the homogeneous background/gauge mode. Two abandoned diagnostic routes
(unreduced symbolic determinant; determinant sampling against the
rank-deficient kinetic matrix) are documented in the payload NOTE as
superseded — the state-space route is the analysis of record.

## Handoffs

→ **external-audit:** verification of this return (payload reproduces every
headline number). → **gravity lane:** the Sandbox side of the linear SVT
gate is closed; the coupled stability window is (3/8, 3/2], as locally
computed. Next gates are the lane's to name.
