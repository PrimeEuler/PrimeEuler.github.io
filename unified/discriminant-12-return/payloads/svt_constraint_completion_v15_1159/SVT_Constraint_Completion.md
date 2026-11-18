# The nonlinear K4 corner, part 2 — the SVT constraint completion for v15.1085's mode

Sandbox note (little Euler), 2026-11-18; item 3 of
Jeremy's 2026-11-18 tasking, second half. Producer:
`svt_constraint_completion.py` (sympy, exact; all
checks PASS). v15.1085 filed the full initial SVT
stress of the compact Maxwell packet and Gate 911's
limitation: the TT-only Weyl jet of v15.1083 "cannot
simply be called the full electric tidal field," with
the scalar/vector ADM constraints left to solve. This
note solves them on the initial slice for the filed
longitudinal mode (q ∥ z), in one stated gauge, and
computes what the completion changes.

## Setup (conventions stated once)

Sources as filed (v15.1085 Gate 909, conformal
orthonormal, η = 0): T00 = R, T0i = 0,
Tij = diag(P, −P, R), P/R = (b²−a²)/(b²+a²), TT part
diag(P, −P, 0). Longitudinal (conformal-Newtonian)
gauge, signature (−,+,+,+), G = κT, conformal densities
as filed (physical stresses ∝ a⁻⁴; constraint sources
enter with a⁻², matching v15.1083's scaling). The
linearized constraint equations are standard GR —
imported, not cone-derived; component signs follow
these conventions, the structural results do not
depend on them.

## The solve

- **SVT split** (verified): Tij = (R/3)I +
  diag(−R/3, −R/3, 2R/3) + diag(P, −P, 0) — isotropic,
  scalar STF with S_L = 2R/3 (the filed value; nonzero
  even at P = 0), TT. The scalar anisotropic-stress
  amplitude is Π^S = (3/2)S_L = R.
- **Momentum constraint at η = 0:** T0i = 0 forces
  Ψ′ + ℋΦ = 0, which removes the ℋ terms from the
  Hamiltonian constraint, leaving the Poisson form
  **Ψ(q,0) = −κa₀⁻²R/(2q²)** — forced by the energy
  density R, not by the anisotropy P.
- **Traceless ij equation:** Φ − Ψ = −κa₀⁻²Π^S/q²
  = −κa₀⁻²R/q², so **Φ = 3Ψ** and
  **Φ + Ψ = −2κa₀⁻²R/q²**.
- **Vector sector:** the transverse momentum
  constraint is homogeneous with zero source for this
  data at η = 0 (v15.1085: vector momentum and
  anisotropy vanish on the initial slice for this
  orientation), so the vector potential and vector
  Weyl vanish at η = 0 for this data — initial slice
  and this orientation only, per the filed caveat.
- **Ward jet re-verified** (Gate 910's algebra):
  R′(0) = 0, S_z′(0) = −iqR, R″(0) = −q²R — the
  completed initial data is consistent with the
  source's own conservation jet.

## The completed initial tidal field

Scalar electric Weyl for the mode,
E^S_ij = −(1/2a₀²)(∂i∂j − δij∇²/3)(Φ+Ψ):

    E^S = (κR/(3a₀⁴)) · diag(1, 1, −2),

traceless, q-independent at η = 0 (the constraints'
1/q² is cancelled by the tidal operator's q²), and
proportional to R. Combined with v15.1083's TT jet
W₊(q,0) = κP/(2a₀⁴) (xx component):

- at a:b = 1:2 (P = 3R/5): completed E_xx
  = (19/30)·κR/a₀⁴ against the TT-only (3/10)·κR/a₀⁴ —
  the scalar sector more than doubles the xx tide;
- at a = b (P = 0): the TT jet vanishes identically,
  while the completed field is
  (κR/(3a₀⁴))·diag(1, 1, −2) ≠ 0 — the scalar sector
  carries the *entire* initial tide. Gate 911's warning
  is quantitatively maximal at the symmetric point:
  the TT-only answer there is zero, and the true
  initial tide is set by the energy density.

## Scope

This is an initial-slice constraint solve for one
filed Fourier mode, with homogeneous scalar/vector
data set to zero by the stated gauge choice — the
uniqueness inputs Gate 911 listed (gauge, boundary
conditions, solid zero modes) are fixed by that
choice, not derived. No time evolution of the scalar
sector, no position-space detector reconstruction.
And the comparator point stands: the completed field
is standard Einstein gravity sourced by the standard
Maxwell stress — no cone-specific operator appears.
The completion corrects the record's tidal
bookkeeping (the TT-only jet is now explicitly a
sector of the answer, with the scalar sector computed
beside it); it is not new physics and selects nothing.

Flags: SVT_completion = DONE (initial slice, filed
mode, stated gauge); scalar_tide ∝ R, survives at
P = 0; vector = 0 at η = 0 (this data/orientation);
cone_specific_content = NONE; G_derived = false.
