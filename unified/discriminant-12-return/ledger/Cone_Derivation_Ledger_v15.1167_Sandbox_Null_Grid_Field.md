# Cone Derivation Ledger v15.1167 — Sandbox: a lattice field on the cone's null grid — massless sector exact, Dirac doubler-free, box-scheme massive propagator tracks J0

**Deposit type:** Sandbox build, independently checkable
(producer re-executed from the staged payload copy;
11 checks ALL PASS). Origin: Jeremy's correction on the
Craig mapping (the counting lattice is only one lattice
on the cone; spacetime lands on it too) and his call
2026-11-18: "Go bigger: build a lattice field on the
null grid." Grid: u = T + X, v = T - X on ℤ² — the
integer pair plane, the cone's spacetime (v15.1042);
operator ΔuΔv with one-sided differences.

**The massless scalar is exact on this grid.** ΔuΔv φ = 0
has precisely the continuum solution space φ = f(u) +
g(v) (both directions verified exactly), and the
retarded propagator marched by recursion is exactly the
quadrant indicator θ(u)θ(v) — in (u,v) normalization it
is the continuum propagator, not an approximation. The
null factorization leaves no lattice artifacts in the
massless sector, unlike any Cartesian spacetime lattice.

**The massive scalar makes the scheme a real choice**
(μ² = m²/4). Forward scheme: dispersion near the shell
(Re q = 0.01948 vs 0.02000 at p = 0.5) but complex —
Im q = -0.00518 phase drift per step, accumulating in
the propagator (deviation from J0(m√(uv)): 0.035 at
(10,10), 0.126 max by n = 40; filed as a defect). Box
scheme (mass on the cell average): REAL dispersion
tan(p/2)tan(q/2) = μ²/4 exactly, propagator tracking J0
to max deviation 0.00194 on the diagonal — the grid's
working massive discretization. Centered scheme: real
dispersion but doubler lines at p = π, q = π.

**The massless Dirac operator has no doublers.**
One-sided differences split by chirality (Δv ψ_R =
-(m/2)ψ_L, Δu ψ_L = +(m/2)ψ_R); the symbol
(e^{ip}-1)(e^{iq}-1) vanishes at m = 0 exactly on the
two chiral lines p = 0, q = 0 (Brillouin-zone scan;
value 4.0 at (π,π)). Price stated: the one-sided
operator is not anti-Hermitian — the standard
light-front evasion of Nielsen-Ninomiya, verified here
on this grid, not claimed as new.

**Sectors and refinement.** The crossed propagator is
the same recursion marched in (u, -v): propagator
support IS the sector decomposition (future/past T
cone, two X-cone quadrants). An eternal worldline
source gives φ = g·min(u,v) exactly — constant field
strength, the 1+1 linear potential in null form. Under
refinement the coarse ΔuΔv is the sum of the four fine
ones (telescoping, exact): the massless solution space
is refinement-invariant; the massive box propagator
converges (deviation ~1×10⁻⁵ at (4,4), smaller at half
spacing). Grid-to-grid consistency — the shape of
Craig's construction — holds here as an exact property
of the factorized free field.

**Scope filed in the note:** 1+1 free fields (scalar +
Dirac) plus one sourced solution. No gauge fields, no
interacting dynamics, no fermion measure, no 3+1, no
continuum-limit theorem. Craig's measure question is
still not posable; the arena it would need now has
filed field content with two exactness properties a
Cartesian arena lacks. Corridor species:
dictionary/transport; no selector; no door touched.

**Payload:** `payloads/null_grid_field_v15_1167/` — Null_Grid_Field.md `b9188e7816de330001b78a83db935b6dca8b27293b8ac333c8eb743e25a20fdd`, null_grid_field.py `5b9c68cfaf150ee71545244a0fc2ca57b277f043fd10a0e961d41385b4000046`.
