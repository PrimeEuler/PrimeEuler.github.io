# The TN trajectory cone — verification note

**Question.** The MIC trajectory lies on the Poincaré cone
(v15.229). Does a Taub–NUT geodesic do the same — and where does
the quarter sit in the opening?

**Answer [D]: yes, verbatim, with the paired charge.** Along true
TN geodesics (Hamilton flow of H = ½ g^μνp_μp_ν from the record's
inverse metric, sympy-derived; m = 1, ε = 0.92, RK4 in proper time),
the charge vector of the record (J = p_θ φ̂ − (Π/sinθ) θ̂ − s n̂,
Π = k + s cosθ, **s = 2lε**) is conserved as a vector, and
J·n̂ = −s holds identically. The trajectory is therefore confined
to the cone cos α = s/|J| about −Ĵ, exactly as in MIC.

**Numbers** (`tn_cone_test.py`, `tn_cone_output.txt`; 8 cases,
s ∈ {0, 1/2, 1, 3/2} × j ∈ {1/2, 3/2}): worst |ΔJ| ≤ 8.3e-13,
identity ≤ 6.7e-16, angle constancy ≤ 4.4e-16, constraint drift
≤ 7.3e-9. Openings agree with the MIC table at equal (s, |J|) to
all printed digits — 60.0000° at (1/2, j=1/2), 75.5225° at
(1/2, j=3/2), 62.6883° at (1, j=3/2), 52.2388° at (3/2, j=3/2),
90° at s = 0 — plus 30.0000° at (3/2, j=1/2) (|J| = √3). The
TN−MIC difference is purely radial (v14.731/tn_sector.py), now
verified in trajectory space, not only in the HJ equation.

**Where the quarter is.** The cone sees the PAIRED charge s = 2lε.
The parabolic seats sit at k/2 ± εl — the seat offset εl is HALF
the cone's s. So at trajectory level the gravitational sector
repeats the pair pattern of the whole dyon thread: what a single
trajectory measures is the doubled (pair) charge, and the quarter
lives one level down, in the seat split and the pair product
(k/4)² of v14.731. The cone does not see the quarter directly; it
sees the pair whose product is quartered.

**Scope.** Verification in the record's own conventions; no new
physics, no gate moved. The EM cone (v15.229) and the TN cone are
one theorem in two radial sectors.
