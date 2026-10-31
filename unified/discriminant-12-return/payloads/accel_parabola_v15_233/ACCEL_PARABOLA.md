# The acceleration parabola vs the Dirac depth; crossing range

Producer: `accel_parabola.py` / `accel_parabola_output.txt`.

**Depth comparison.** Log-depth below the Planck acceleration
a_P = 5.5607e51 m/s²: the 1 g parabola sits at ln(a_P/g) = 116.865
= 2.5792 × the Dirac depth ψ_D = 45.310004305 (v14.621) — excess
71.555 (factor 1.19e31), no lock. The acceleration AT the Dirac
depth, a_P e^{−ψ} = 1.1675e32 m/s², has Rindler length
c²/a = ℓ_P e^ψ = 7.698e-16 m (0.915× the proton charge radius,
3.66× its reduced Compton wavelength): fermi neighbourhood,
flagged as partly built-in — ψ was constructed from proton/
electron data, so a fermi-scale output is not an identity.

**Crossings** (edge-pinned units u = gt/c, ξ = gx/c²; parabola
ξ = u²/2, edge ξ = u), exact algebra + numeric check:
- Parabola × null edge: u = 2 exactly (t = 1.9374 yr,
  x = 1.9374 ly) — the Galilean trajectory exits the cone there.
- Parabola × its own Rindler hyperbola ξ = √(1+u²) − 1: tangent
  at the vertex (difference u⁴/8 − u⁶/16 + …), strictly outside
  thereafter, NEVER crosses. The relativistic curve bends toward
  the edge and stays inside; its Galilean shadow leaves.
- Parabola × interval hyperbolas u² − ξ² = σ²: two crossings iff
  σ < 1 (u² = 2 ± 2√(1−σ²)); one grazing crossing at σ = 1
  (u = √2, ξ = 1); none for σ > 1.
So "every parabola crosses a hyperbola" holds exactly inside the
parabola's own Rindler scale: the crossing range is set by the
parabola's null metric c²/g — a light-year at 1 g, a fermi at the
Dirac depth. The crossing geometry is scale-free; only the reach
changes.
