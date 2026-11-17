# The curl and the action circle — B circulates, and the charge on the seat's circle is the Zitterbewegung loop

Sandbox note (little Euler), 2026-11-17; fourth in the
charge-at-the-seat run (v15.1082, v15.1084, v15.1086,
cross-reference v15.1088). Producer: `zb_circle.py`
(sympy, exact; all checks PASS, exit 0). Jeremy: "an
accelerating charge creates curl which seems like the
action circle."

## A. The curl is literal

The slid seat's magnetic field (v15.1084) is **purely
azimuthal** around the motion axis — verified: no radial
component (B·ρ̂ = 0), no axial component (B_x = 0), and
(B·φ̂)² = |B|²ρ², i.e. all of B is the circulating part.
Its field lines are circles about the trajectory and
∮ B·dl = 2πρ B_φ ≠ 0 around any loop encircling the axis.
The boost's shadow of E is a circulation, not a fan.

## B. The charge on the seat's own circle

The seat's action data (v15.864) define one distinguished
circulation: the Dirac electron's Zitterbewegung circle,

    r = ħ/(2mc),   ω = 2mc²/ħ,   v = ωr = c (verified).

Its invariants land exactly on the seat's filed numbers:

- **circuit action** ∮ p dx = (mc)(2πr) = **πħ** — the
  phase-space Compton-ellipse action of v15.864, exactly;
- **period** τ_ZB = π·τ_C — the ZB circuit is the πħ
  object, *not* the ħ object (the seat cycle
  E_rest·τ_C = ħ stays a separate, smaller datum);
- **circulation angular momentum** L = mvr = **ħ/2**.

And the circulating charge is a current loop,
I = qω/2π, with moment

    μ = Iπr² = qħ/(4m) = μ_B/2.

The loop gives **g = 1**; the electron's is g = 2. The
missing half is standard Dirac structure (imported): the
Gordon decomposition splits the Dirac current into a
convection part — this loop — and a polarization part
proportional to the **curl of the spin density**. So
"the charge creates curl" has two floors, each worth
g = 1: the circulation of the charge, and the curl of
its spin density. This check gates the first; the second
is imported Dirac theory, not re-derived.

## Scope

Zitterbewegung is a mathematical feature of the Dirac
equation — interference between the +E and −E sectors
(in this run's language: the seat and its crossed
partner; a pure one-sector state does not circulate) —
not a literal classical orbit. The gated content is the
azimuthal purity of B and the scale coincidences
(πħ, ħ/2, π τ_C) with the seat's action data: dictionary
level, corridor species, as throughout this run. Nothing
selects a coupling; Doors I–III untouched.
