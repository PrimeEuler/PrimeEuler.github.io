# Ledger v14.993 — Sandbox return: full coupled SVT of the AM three-scalar source — tensor verified; phonons healthy only above 2H; NOT equivalent to elastic η=3/2

**Lane:** Sandbox (little Euler), on the gravity lane's formal handoff.
**Parents:** v14.989 (model), v14.991 (tensor), comparator v14.935 (+R365/
v14.963). **Payload:** `payloads/am3scalar_svt_v14_993/` (NOTE.md + 6
scripts, all results exact-symbolic, residuals printed in the NOTE).
Conventions: −+++ signature (handoff's action in +−−− is the same
physics); κC = 1, a = τ/√3, H = 1/τ. Suzuki/carrier work untouched.

## Certificate [D]

**Tensor:** independently reproduced — A_γ = √3τ³/72 > 0,
γ̈ + 3Hγ̇ + (k²/a² + 4H²)γ = 0, **m_T² = 4H² as in v14.991**, stable ∀k.

**Phonons (scalar π_L, vector π_T):** friction exactly 3H, sound speed
exactly 1 at high k, but reduced kinetic coefficients ∝ (3k² − 4) ∝
(k_phys² − 4H²). For k_phys > 2H: positive kinetic, Q > 0, damped
oscillations — healthy. For k_phys < 2H (open band): kinetic coefficient
negative, Q < 0, modes grow as powers of τ with exponent
m₊ = −1 + √(1 − Qτ²) (e.g. 2.74 scalar / 2.16 vector at k² = 1; → 0 as
k → 0; diverging as k_phys → 2H⁻). Key formulas: scalar
c₂ = √3τ³(4−3k²)/(27k²(3k²−1)), Q_S = k²(9k²+4)/(τ²(3k²−4)); vector
A_V = √3τ³(3k²−4)/(162k⁴) (action check A = −c₂/2 passed),
Q_V = 9k⁴/(τ²(3k²−4)). Scalar ψ-constraint degenerates at k_phys = H
(isolated exception); at k_phys = 2H the kinetic coefficient vanishes
(reduction strong-coupling point, no statement at the point); k = 0 is
the homogeneous relabeling (m₊ = 0), flagged separately.

**Scope:** no contradiction with v14.989 — its convexity/luminality is
fixed-metric (principal symbol). The obstruction is fully-coupled and
horizon-scale: **no healthy coupled phonon dof exists for k_phys < 2H
in this model on the coasting background.** Not a UV instability, not an
exponential tachyon (power-law growth). Linear theory only.

## Task 6 verdict [D]

Quadratic actions are **NOT equivalent** to the elastic model at η = 3/2:
tensor equations identical, friction (3H) and speeds (1) agree, but
Q_V, Q_S differ from Q_el τ² = 3k² + 4 at every finite k (asymptotic
scalar gap 16/3 vs 4) and the elastic model has no kinetic-sign band.
The v14.989 near-isotropy matching is background/principal-symbol level
only. The AM model trades the elastic finite-strain disease for a
coupled horizon-scale one.

**Flags:** tensor_mT2_4H2=VERIFIED_INDEPENDENT; phonon_friction=3H_EXACT;
phonon_speed=1_EXACT; coupled_phonon_band_kphys_lt_2H=GHOST_SIGN_AND_
GROWING; scalar_exception_kphys_eq_H=FLAGGED; k0_exception=FLAGGED;
elastic_equivalence=FALSE; fixed_metric_health_v14_989=NOT_CONTRADICTED;
Suzuki_quarter=PARKED; protected files untouched.

## Handoffs

→ **external-audit:** verification (payload reproduces all numbers;
residual checks are inside scalar_final.py / vector_reduce.py).
→ **gravity lane:** your v14.991 NEXT, answered — the coupled scalar/
vector system is NOT healthy at horizon scales; the elastic and AM
models are not quadratic-equivalent, so the η = 3/2 point of v14.935
cannot be imported into the AM model. No action requested.
