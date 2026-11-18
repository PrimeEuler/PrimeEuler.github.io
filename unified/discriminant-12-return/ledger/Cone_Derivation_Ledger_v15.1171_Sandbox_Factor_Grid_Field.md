# Cone Derivation Ledger v15.1171 — Sandbox: a lattice field on the k=4 factor grid — (1,3) signature, pair-plane exactness survives, full 4D exactness dies quantified

**Deposit type:** Sandbox build, independently checkable
(producer re-executed from the staged payload copy;
6 checks ALL PASS). Origin: Jeremy's extension call
after the null-grid field (v15.1167), "factors, then
tilt on top" — part 1, factors (tilt is the companion
deposit). Arena: the record's k-factor Hessian metric
(v14.953-955): ds² = P[(Σ d ln x_i)² - Σ(d ln x_i)²],
which in log-factor coordinates y_i = ln x_i is
ds² = 2P·Σ_{i<j} dy_i dy_j — the constant form A
(0 diagonal, 1 off-diagonal) times conformal factor 2P.
Grid: ℤ⁴ in y; operator L = Σ_{i<j} Δ_iΔ_j, the k=4
lift of ΔuΔv. The field is the conformal
representative's (light cones are conformally
invariant); the physical metric's minimally coupled
field is a different object, stated in the note.

**Signature and filed arithmetic.** A's eigenvalues
at k=4 are exactly {3, -1, -1, -1} — (1,3). The
record's FLRW form verifies: τ = 2√(3/4)√P gives
a(τ) = τ/√3 and R = -6/τ² = -2/P, the filed K4 values.

**Pair-plane exactness survives.** Any 1+1 massless
solution on a factor pair plane (φ = f(y₁) + g(y₂),
constant in the other factors) solves the k=4 lattice
equation EXACTLY. The v15.1167 exactness is demoted
from global to planar, not lost.

**Full 4D exactness dies, quantified.** The continuum
cone momentum p* = (1, 1, -1/2, 0) (on the cone in
exact rational arithmetic, three active coordinates)
has lattice symbol 0.6849 ≠ 0; on the cone the symbol
vanishes only cubically as p → 0 (scaling ratio
7.98 ≈ 8). Generic 4D waves are lattice-approximate,
as on any spacetime lattice; the pair planes are the
exception.

**Causality and energy.** In orthonormal coordinates
(s₀ = Σy/2, form 3ds₀² - |dz|²) the cone speed is √3;
a compact pulse's axis front at the 10⁻³ level runs
at net speed 1.833 (within 6%; threshold spread
1.500-2.000 filed as dispersive precursors). Discrete
energy positive and bounded throughout (ratio 1.40) —
no ghost, per v14.955's signature-vs-ghost point.
And the grid's diagonal is log-time: along
(n,n,n,n), τ = √3·e^{2n} — equal diagonal steps
multiply proper time by e².

**Scope:** conformal-representative free scalar on
the factor grid; exactness planar only; no minimal-
coupling corrections, interactions, mass, or measure.
Corridor species: dictionary/transport; no selector.

**Payload:** `payloads/factor_grid_field_v15_1171/` — Factor_Grid_Field.md `4695b7ebcbf793bebd94900a0569846e10f22233e6dfc191970d142b373f04ef`, factor_grid_field.py `b100da6e536b3095447a5ef7511a251e87c772b996da47ec55a5af0b974a6cb5`.
