# Full coupled SVT certificate: Einstein + three canonical label scalars (Sandbox return)

**Handoff:** gravity v14.989 (model) + v14.991 (tensor only); **comparator:**
Sandbox v14.935 (elastic model, incl. R365/v14.963 corrections).
**Action:** S = ∫√−g [R/(2κ) − (C/3)Σ_I (∂φ^I)²] (signature −+++; the handoff's
+(C/3)(∂φ)² in +−−− — same physics). Background a(τ) = τ/√3, φ^I = z^I, κC = 1,
H = 1/τ, ä = 0. ρ = C/a², p = −C/(3a²) reproduced. Method: quadratic ADM action
per sector (lapse/shift retained), exact elimination of all auxiliaries,
state-space-free reduction; scalar reduction verified by exact residuals
(EL_Φ and EL_B of the *original* action vanish identically on the reconstruction;
the scalar π̈ coefficient was also derived by hand and matches).

## Tensor (γ) — v14.991 VERIFIED, stable at all k

A_γ = √3 τ³/72 > 0; γ̈ + (3/τ)γ̇ + (k²/a² + 4H²)γ = 0.
**m_T² = 4H² independently reproduced.** No ghost, no tachyon; damped
oscillations, indices as in v14.991. [D]

## Phonon sectors — healthy only above k_phys = 2H

Both label phonons have friction exactly 3H and unit sound speed
(Ω²/(k²/a²) → 1), but their *reduced kinetic coefficients are proportional
to (3k² − 4) ∝ (k_phys² − 4H²)*:

**Vector (π_T, ×2):** V eliminated exactly (V = 4√3 τ ṗ_T/(9k³), residual 0;
action check A = −c₂/2 passed). A_V = √3 τ³(3k²−4)/(162k⁴);
Q_V = 9k⁴/(τ²(3k²−4)); Ω²_V = 3(12k⁴−3k²+4)/(4τ²(3k²−4)).

**Scalar (π_L):** ψ slaved by the constraint
√3τ[(k²−1/3)ψ + π/9 − τπ̇/(9k²)] = 0 (residuals 0).
c₂ = √3τ³(4−3k²)/(27k²(3k²−1)); Q_S = k²(9k²+4)/(τ²(3k²−4));
Ω²_S = (36k⁴+7k²+12)/(4τ²(3k²−4)).

**Regimes** (k_phys² = 3k²/τ²; mode exponents m from m² + 2m + Qτ² = 0):

- k_phys > 2H: kinetic > 0, Q > 0 — damped oscillations. Healthy.
- k_phys < 2H (open band): kinetic coefficient NEGATIVE in both sectors
  (scalar: for H < k_phys < 2H; vector: for all k_phys < 2H), Q < 0, and
  the modes GROW as powers of τ: m₊ = −1 + √(1−Qτ²) ∈ (0, ∞), e.g.
  m₊ ≈ 2.74 (scalar) / 2.16 (vector) at k² = 1, → 0 as k → 0, and
  diverging as k_phys → 2H⁻.
- k_phys = 2H exactly: kinetic coefficient = 0 — the reduction degenerates
  (strong-coupling point of the phonon variable); no statement at the point.
- Scalar exception k_phys = H (k² = 1/3): the ψ-constraint loses ψ
  (coefficient k² − 1/3); the reduced form changes there — isolated momentum,
  excluded from the band statements.
- k = 0: homogeneous relabeling; m₊ = 0 (frozen). Excluded separately.

## Scope and interpretation

This does NOT contradict v14.989: the material principal symbol is luminal
and the energy is rank-one convex — on a FIXED metric. The failure is in
the FULLY COUPLED reduction: at horizon scales the phonon's kinetic term
is overwhelmed by its coupling to the metric potentials, the phonon
ceases to be a healthy propagating dof, and long-wavelength label
perturbations grow as powers of τ. It is not a UV/gradient instability
(high k is exactly canonical) and not an exponential tachyon (growth is
power-law, H-scale). Whether read as a true ghost band or as breakdown of
the phonon variable where mixing is order-one, the classical certificate
is: **no healthy coupled phonon exists for k_phys < 2H in this model.**

## Task 6 — NOT equivalent to the elastic model at η = 3/2

The elastic comparator (v14.935) has, at η = 3/2, friction 3H and the SAME
Q in all sectors: Q_el τ² = 3k² + 4, with positive kinetic coefficient at
every k. Here: tensor Q agrees exactly (3k² + 4)/τ², but
Q_V τ² = 9k⁴/(3k²−4) and Q_S τ² = k²(9k²+4)/(3k²−4) differ at every finite
k (asymptotic gap constants: vector 4 ✓, scalar 16/3 ≠ 4), and the kinetic
sign structure differs (band above vs none). The v14.989 matching
(A_B/G_B expansion = elastic η = 3/2 at quadratic order about isotropy) is
a background-stress/principal-symbol statement; **the fully coupled
quadratic actions are not equivalent.** The AM three-scalar model trades
the elastic model's finite-strain disease for a coupled horizon-scale one.

## Method notes / failures disclosed

- A first substitution chain (eliminating ψ inside the action after Φ, B
  had reintroduced ψ̇ through their solutions) produced spurious results
  (zero friction, negative high-k Ω²); it was caught by cross-checks
  (friction must be 3H; high-k speed must be 1) and replaced by the
  {E1, E1′, E2} equation-level reduction with exact residuals. The payload
  contains only the corrected chain.
- An independent Christoffel-route cross-check of the scalar sector was
  attempted and abandoned after a 47-minute runtime (recorded in
  scalar_direct.py); the certificate rests on the ADM action, exact
  residuals, the hand-derived π̈ coefficient, the vector action/equation
  agreement (A = −c₂/2), and the tensor match to v14.991.
- Stability statements are for the linear coupled system on the coasting
  background; nothing here certifies the nonlinear theory.

**Payload scripts:** scalar_adm.py + scalar_final.py (scalar),
vector_adm.py + vector_reduce.py (vector), tensor_adm.py (tensor),
scan.py (mode table). All symbolic results exact; scan is numerical
evaluation of the exact formulas.
