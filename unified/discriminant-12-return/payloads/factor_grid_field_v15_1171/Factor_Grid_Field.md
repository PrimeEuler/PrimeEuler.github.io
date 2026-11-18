# A lattice field on the k=4 factor grid

Sandbox note (little Euler), 2026-11-18. Origin:
Jeremy's extension call after the null-grid field
(v15.1167): "factors, then tilt on top" — part 1,
factors. Producer: `factor_grid_field.py`, 6 checks,
ALL PASS.

The arena is the record's own k-factor Hessian
geometry (v14.953–955): for positive x_i with
P = Πx_i, the pullback of the affine Hessian of P is
ds² = P[(Σ d ln x_i)² − Σ(d ln x_i)²], inertia
(1, k−1). In log-factor coordinates y_i = ln x_i this
is ds² = 2P·Σ_{i<j} dy_i dy_j — a constant form A
(0 diagonal, 1 off-diagonal) times the conformal
factor 2P. The field built here is the conformal
representative's field on the grid ℤ⁴ in y (light
cones are conformally invariant; the physical
metric's minimally coupled scalar differs by the
conformal factor and is not what is built — stated
plainly). The grid operator is the k=4 lift of
v15.1167's ΔuΔv: L = Σ_{i<j} Δ_iΔ_j, one-sided
differences in each log-factor.

## What the checks found

**Signature and filed arithmetic (F1, F2).** A's
eigenvalues at k=4 are exactly {3, −1, −1, −1} —
(1,3). The record's FLRW form checks arithmetically:
τ = 2√((k−1)/k)√P gives a(τ) = τ/√3 at k=4, and
R = −6/τ² = −2/P, the filed K4 values.

**Pair-plane exactness survives (F3).** Any 1+1
massless solution living on a factor pair plane
(φ = f(y₁) + g(y₂), constant in y₃, y₄) solves the
k=4 lattice equation EXACTLY — every other pair term
contains a difference in a direction the field
doesn't vary. The v15.1167 miracle is not lost in
4D; it is demoted from global to planar: the field
is exact on every coordinate pair plane.

**Full 4D exactness dies, quantified (F4).** The
continuum cone momentum p* = (1, 1, −1/2, 0) —
exactly on the cone, Σ_{i<j} p_i p_j = 0 in rational
arithmetic, with three active coordinates — has
lattice symbol |Σ_{i<j}(e^{ip_i}−1)(e^{ip_j}−1)| =
0.6849 ≠ 0. On the cone the symbol vanishes only
cubically as p → 0 (measured scaling ratio 7.98 ≈ 8
between ε = 0.2 and ε = 0.1): the lattice cone agrees
with the metric cone to second order and no better.
Generic 4D waves are lattice-approximate, exactly as
on any spacetime lattice; the pair planes are the
exception, not the rule.

**Causality and energy in orthonormal coordinates
(F5).** With s₀ = Σy/2 the form is 3ds₀² − |dz|², so
the wave equation is φ_{s₀s₀} = 3∇²_z φ, cone speed
√3. A compact smooth pulse evolved by leapfrog has
its axis front (absolute threshold 10⁻³) at net speed
1.833 — within 6% of √3; the threshold spread
(1.500 at 10⁻², 2.000 at 10⁻⁴) is the standard
dispersive-precursor structure, filed rather than
averaged away. The discrete energy is positive
throughout and bounded (max/min ratio 1.40 over the
run): no ghost, in line with v14.955's point that the
Hessian metric's negative spatial components are
spacetime signature, not a matter ghost.

**The grid's diagonal is log-time (F6).** Along
y = (n,n,n,n), P = e^{4n} and τ = √3·e^{2n}: equal
diagonal grid steps multiply proper time by e². The
factor grid's natural time is logarithmic in the
physical τ — the grid is uniform in ln τ, which is
why the conformal representative is the grid's native
field.

## Scope

Conformal-representative free scalar on ℤ⁴ in
log-factor coordinates. Exactness: planar only.
Not built: the physical metric's minimally coupled
field (conformal-factor corrections), interactions,
the massive box scheme at k=4, any measure. The
3+1 arena the Craig question would need now has a
filed field on it, with the same honesty shape as
the 1+1 build: exact where the structure factorizes,
approximate where it doesn't, numbers filed either
way. Corridor species: dictionary/transport; no
selector; no door touched.

Flags: signature = (1,3) EXACT; pair_planes = EXACT;
full_4D = APPROXIMATE (symbol 0.6849 at p*, cubic
on-cone vanishing); cone_speed = sqrt(3), front
1.833 at 1e-3; energy = POSITIVE, bounded;
diagonal = LOG tau.
