# Tilt on top: cutting-plane sections of the gridded cone

Sandbox note (little Euler), 2026-11-18. Origin:
Jeremy's extension call after v15.1167 — "factors,
then tilt on top," part 2 (part 1, the k=4 factor
grid, is the companion deposit). Producer:
`tilt_sections.py`, 5 checks (6 with T1b), ALL PASS.

Setup: the cone surface from the pair grid,
(u,v) ↦ (T, X, Y) = ((u+v)/2, (u−v)/2, √(uv)) with
T² = X² + Y² — the 45° cone. A cutting plane tilted
by γ in the (T, Y) plane: T cos γ + Y sin γ = c.
γ = 0 cuts a circle. This is the tilt the e(t) line
(v15.1110–1160) made a dynamical coordinate in the
continuum; here it is put on the grid.

## The tilt–eccentricity relation is exact

Substituting the plane parametrization
T = c cos γ − s sin γ, Y = c sin γ + s cos γ into the
cone equation gives, symbolically and identically,
c²cos 2γ − X² − cos 2γ·s² − 2c sin 2γ·s = 0 — an
ellipse with semi-axes a_X = c/√(cos 2γ) and
a_s = c/cos 2γ, hence

  e² = 1 − cos 2γ,   e = √2 sin γ,

0 at γ = 0 (circle), 1 at γ = 45° (the parabola —
the plane parallel to a cone generator). Numeric
section extents reproduce e at 10°, 20°, 30° to
12 decimals. The e of the e(t) deposits is therefore
√2 sin γ in this parametrization: tilt and
eccentricity are one degree of freedom, now with its
grid-side formula filed.

## What the field does on tilted sections

For two filed fields of v15.1167 — the
worldline-sourced φ = min(u,v) and the massless wave
φ = sin(2πu/12) + cos(2πv/12) — the section Dirichlet
energy per unit X-extent was computed on lattice
points in a thin shell of the tilted plane, at nine
tilts γ = 0°…40°:

- min(u,v): E falls 1.9718 → 1.2667; fit
  E ≈ E₀ − 0.8814·e².
- wave: E falls 0.5490 → 0.4754; fit
  E ≈ E₀ − 0.1088·e².

Both fields' section energies DECREASE with tilt and
both carry a genuine e² term. Filed as a contrast,
not a contradiction: the continuum Maxwell U_B(e)
of v15.1110 had NO e² term (pure quartic, restoring)
— but that was the self-consistent field energy of a
sourced configuration, where this is the restriction
functional of two fixed lattice fields. Different
functionals, different tilt response; anyone quoting
one for the other is mixing objects. What the grid
adds is that tilt response is computable section by
section from the field itself, with no actuator
postulated.

## Tilt is a continuum modulus over the grid, not a grid symmetry

At k=4 the cone form A (0 diagonal, 1 off-diagonal)
is preserved by exactly 48 of the 384 signed
permutations of the factors — the permutations S₄
times the overall sign. Independent sign flips break
the pair form (a flipped pair term changes sign), a
fact the build's first draft got wrong by assuming
all 384; the enumeration is the correction, filed
here. And a continuous tilt — a boost mixing s₀ and
z₁ at θ = 0.1 — moves the lattice point (1,0,0,0) to
y₁ = 1.074582 ∉ ℤ⁴: boosts do not preserve the factor
grid at any angle. So the tilt family lives over the
grid the way the e(t) actuator lived over the
continuum ellipse: as an external continuous
parameter whose sections the grid samples, never as
a symmetry the grid possesses. A lattice field theory
that wants tilt dynamics must supply it as the e(t)
line did — a collective coordinate with its own
inertia — not extract it from grid symmetries.

## Scope

Sections and restriction energies on the k=2 cone;
symmetry/boost statements at k=4. Not built: tilted
hyperplane sections of the factor grid with evolved
fields (the boost-breaking makes tilted evolution an
interpolation scheme, not an exact one — the honest
reason it is not in this deposit), tilt dynamics
proper (an M(e) for the lattice field), interactions.
Corridor species: dictionary/transport; the tilt
degree of freedom is real, filed, and — like ρ and
the doors' residues — supplied, not selected.

Flags: e = sqrt(2) sin(gamma) EXACT; section_energy =
DECREASES with tilt, e^2 coefficients -0.8814 /
-0.1088 (contrast v15.1110's quartic U_B, different
functional); grid_symmetries = 48 of 384;
continuous_tilt = NOT a grid symmetry (witness
y1 = 1.074582).
