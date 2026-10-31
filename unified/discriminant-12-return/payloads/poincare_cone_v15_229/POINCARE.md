# The Poincaré cone in our MIC producer — verification note

**Claim [D].** In the charge–monopole (MIC) system on record
(v14.731ff: J = L_mech − s·n̂, s = eg; angular unification v14.735),
the trajectory of the charge lies on a cone — the Poincaré cone —
whose opening is fixed by the charge product s and the total
angular momentum |J| alone:

    J = r × v − s·r̂   (conserved),     J·r̂ = −s   (identity),
    cos α = s/|J|,     |J|² = L² + s².

**Why it is exact.** J·r̂ = −s is an algebraic identity at every
instant: the mechanical part r × v is perpendicular to r̂, so only
the −s·r̂ term contributes. The dynamical content is conservation
of J: with a = −κr̂/r² + s(v × r̂)/r² (Coulomb + monopole Lorentz
force), dJ/dt = 0 follows in three lines (the monopole term's
contribution to d(r × v)/dt is exactly cancelled by d(−s·r̂)/dt).
Since J is a fixed vector and J·r̂ never changes, r̂ keeps a
constant angle to J forever: the motion is confined to the cone
with apex at the monopole and axis −Ĵ. Energy, eccentricity, and
radial range do not enter the opening.

**Producer.** `poincare_test.py` (RK4, dt = 1e-3, 60 000 steps per
orbit, tilted transverse velocity so J is not axis-aligned).
Checks per orbit: |ΔJ| (conservation), |J·r̂ + s| (identity),
|cos α − s/|J|| (angle constancy), |ΔE| (integrator control).
Runs: an s-scan at fixed shell j = 3/2 (s = 0, ±1/2, 1, 3/2) and a
shell scan at the Dirac unit s = 1/2 (j = 1/2, 1, 3/2, 5/2, two
eccentricities each). Full numbers: `poincare_output.txt`.

**Cone-native closed form.** At s = 1/2 with shell angular momentum
L² = j(j+1): |J|² = j(j+1) + 1/4 = (j + 1/2)², so |J| = R — the
ladder radius itself — and cos α = 1/(2j + 1): j = 1/2 → α = 60°,
j = 1 → arccos(1/3) ≈ 70.53°, j = 3/2 → arccos(1/4) ≈ 75.52°,
j = 5/2 → arccos(1/6) ≈ 80.41°. The s = 0 control degenerates to
α = 90° (the orbital plane), as it must.

**Results** (clean exit, ALL CHECKS PASS; 13 orbits). Worst-case
residuals over all runs: conservation |ΔJ| ≤ 6.5e-14; identity
|J·r̂ + s| ≤ 8.9e-16 (machine precision, as an identity must be);
cone-angle constancy |Δcos α| ≤ 3.3e-16; energy drift ≤ 9.1e-15.
Measured openings match the closed form at every point: s-scan at
j = 3/2 gives α = 90.0000° (s = 0 control, the orbital plane),
75.5225° (s = 1/2), 62.6883° (s = 1), 52.2388° (s = 3/2), and
104.4775° at s = −1/2 — the cone flips side with the sign of the
charge product. Shell scan at s = 1/2: |J| − (j + 1/2) = 0 to
2.2e-16 at j = 1/2, 1, 3/2, 5/2, both eccentricities.

**Scope.** A standard result (Poincaré 1896) — now verified inside
this project's own MIC conventions rather than quoted, upgrading
v15.228 §5(iii) from citation to in-house [D]. It says the cone of
the project is, in the monopole sector, literally a trajectory:
acceleration by the monopole field draws it, and the charge product
sets its opening. No new physics, no change to any gate; the
node = state premise is not involved.
