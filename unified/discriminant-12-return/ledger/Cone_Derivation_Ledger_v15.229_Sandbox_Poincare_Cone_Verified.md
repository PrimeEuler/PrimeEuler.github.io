# Ledger v15.229 — Sandbox return: the Poincaré cone, verified in the MIC producer [D]

**Kind:** Sandbox return [D]; computational verification. Upgrades
v15.228 §5(iii) from a cited standard result to an in-house
verification in this project's own MIC conventions.
**Origin:** Jeremy's remark (2026-10-31) that acceleration is
charge-related in general, and his instruction to verify the
Poincaré cone in our MIC producer and ledger it as [D].
**Producer:** `poincare_test.py` (RK4, dt = 1e-3, 60 000 steps per
orbit, clean exit, ALL CHECKS PASS).
**Payload:** `payloads/poincare_cone_v15_229/` — POINCARE.md,
poincare_test.py, poincare_output.txt (13 orbits).

## Result
In the charge–monopole system on record (J = r × v − s·r̂, s = eg;
v14.731ff, angular unification v14.735), with equations of motion
a = −κr̂/r² + s(v × r̂)/r²:

1. **J is conserved** (worst |ΔJ| ≤ 6.5e-14 over 13 integrated
   orbits, tilted geometry, two eccentricities per shell);
2. **J·r̂ = −s identically** (worst residual 8.9e-16 — machine
   precision; it is an algebraic identity, since r × v ⊥ r̂);
3. hence the trajectory is confined to a **cone with apex at the
   monopole, axis −Ĵ, and cos α = s/|J|**, |J|² = L² + s² — the
   opening a function of (s, |J|) only, independent of energy,
   eccentricity, and radial range (angle constancy to 3.3e-16).

## Cone-native closed form
At the Dirac unit s = 1/2 with shell angular momentum L² = j(j+1):
|J| = j + 1/2 = R, the ladder radius (verified to 2.2e-16 at
j = 1/2, 1, 3/2, 5/2), and cos α = 1/(2j + 1) — openings 60.0000°,
70.5288°, 75.5225°, 80.4059°. The s-scan at fixed j = 3/2 shows the
opening set by the charge product: 90.0000° at s = 0 (the orbital
plane — the degenerate control), narrowing through s = 1/2, 1, 3/2,
and flipping to 104.4775° at s = −1/2.

## Scope
A standard result (Poincaré, 1896) — the deposit's content is that
it now stands verified inside this project's producer and
conventions rather than quoted in an interpretive remark. In the
monopole sector the cone of this project is literally a trajectory:
the monopole field's acceleration draws it and the charge product
sets its opening. No new physics is claimed, no gate moves, and the
node = state premise is not involved.
