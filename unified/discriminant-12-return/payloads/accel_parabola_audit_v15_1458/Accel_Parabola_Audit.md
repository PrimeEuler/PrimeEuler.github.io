# Audit: mass and acceleration in the parabola complex — no selector in the trajectories, one pointer at the quantum seam

Sandbox note (little Euler), 2026-11-25. Origin:
Jeremy's direction — gravity accelerates mass, so
the acceleration/transition parabolas should hold a
selector, or at least a pointer — plus his proposal
that every mass hyperboloid has its own G
acceleration paraboloid. Producer:
`accel_parabola_audit.py`, 5 checks, ALL PASS.
Method: census of the filed objects built from
acceleration parabolas and transition parabolas,
each marked for what it carries (m, a, ħ) and
whether its inputs are independent.

## The census

| object | m | a | ħ | verdict |
|---|---|---|---|---|
| EM acceleration parabola, a = qE/m (v15.1082) | yes (as q/m) | yes | no | reads the charge-to-mass ratio |
| G acceleration parabola, a = g | **no** | field only | no | mass-blind — universality (A1) |
| Tangency/osculation gap (v15.233, v15.864) | no (scale c²/g) | yes | no | pure field geometry |
| Larmor readout q² = 6πε₀c³P/a² (v15.1082) | no | yes | no | EM-side; sign(q) in the opening direction |
| Quantum fence a* = mc³/ħ (v15.1082) | yes | yes | yes | a* is DEFINED from m — inputs not independent |
| Seat clock τ_C = ħ/(mc²); KMS period 2πρτ_C | yes | via ρ | yes | reads ρ^{+1} (A3) |
| **Quantum bouncer** (v15.469; Airy, v15.869) | **yes** | **yes** | **yes** | **independent inputs, rigid values** |
| Transition parabolas, J₊ amplitudes √(r(D−r)) | no | no | no | pure ladder combinatorics (A5) |
| Tidal channel β₂ = 2GM_sI²/(ħ²R³) (v14.630) | source M_s | reads g | yes | pointer-shaped, but G IMPORTED |
| Gradiometer → spin transfer (v15.1128–1162) | no | via carriers | yes | gravity enters through positions only |
| Seated balance (2026-10-20) | yes | yes | no | measures G; does not derive it |
| Sciama apex B = Ω/2 (v15.1164) | cosmic inventory | no | no | one empirical joint — the mass-side pointer |

## Findings

**1. No selector lives in any gravitational
trajectory or transition.** The classical G
parabola is mass-blind by construction (A1:
∂a_G/∂m = 0 against ∂a_EM/∂m ≠ 0 — the one-tag
seat of v15.1088 restated as a derivative), the
tangency gap's scale c²/g carries the field alone,
and the transition amplitudes are SU(2)
combinatorics exactly (A5: √(r(D−r)) reproduces
j(j+1) − m(m+1) for j = ½…5 in rational arithmetic).
Mass appears in shapes, fences and clocks — never
in gravitational dynamics. This is the equivalence
principle audited across the whole complex, not
assumed at one point.

**2. The pointer is the quantum bouncer, and it is
unique.** It is the only object in the census
carrying m, a and ħ with independent inputs and
rigid values: E_n = (ħ²ma²/2)^{1/3}|a_n|, Airy
zeros. Verified numerically here (finite-difference
spectrum against the Airy prediction: max deviation
0.62% at grid resolution; m^{1/3} scaling 1.2553 vs
2^{1/3} = 1.2599; a^{2/3} scaling 1.5848 vs 1.5874).
Mass re-enters the acceleration complex exactly
where the classical parabola is quantized — the
phase, not the path.

**3. The pointer pair, re-derived (A3).** With
a = a*/ρ: the bouncer reads E_n/(mc²) ∝ ρ^{−2/3}
while the seat clock reads ρ^{+1}. Two filed
objects, opposite ρ-powers, one shared unknown.
A second, independent computation of either — the
same spectrum read in the seat-curvature language
rather than the spacetime one — would read ρ off
their ratio. Nothing in the record supplies that
second computation (v15.1163's reopening condition,
unchanged); the audit's contribution is showing
the acceleration-parabola route terminates at the
same pair, so the pointer is route-independent:
Jeremy's trajectory-first path and the ρ census
meet at the bouncer.

**4. Jeremy's per-mass G acceleration paraboloid —
verified, with its embedding caveat.** Every mass
hyperboloid E² − p² = m² carries its osculating
paraboloid at the seat, E = m + p²/(2m): gap series
−p⁴/(8m³) + p⁶/(16m⁵) − 5p⁸/(128m⁷) — v15.233's
tangency coefficients (1/8, 1/16, 5/128) exactly
(A4). The paraboloid's shape carries the mass
(seat at m, curvature 1/m at the seat, focal length
m/2 from p² = 2m(E − m)); the dynamics on it under
uniform g carries none. Caveat filed: in this
momentum embedding the focus sits at E = 3m/2,
different for each mass — the confocality at 0
belongs to the cone's (X, Y) mesh parabolas
(v15.235), a different embedding; the two
paraboloid families must not be merged. So each
mass does have its own G paraboloid, and it is one
more instance of the audit's main line: m in the
shape, never in the fall.

## Verdict

Selector: NONE in the acceleration/transition
parabola complex — and the census is the proof
shape: every gravitational entry is either
mass-blind, combinatoric, definition-fed (a*), or
G-imported (β₂). Pointer: TWO, one on each side —
the quantum bouncer (acceleration side: m, a, ħ
with independent inputs, ρ^{−2/3} against the seat
clock's ρ^{+1}) and the Sciama apex (mass side:
one empirical identification joint, v15.1164). A
selector, if the frame ever grows one in this
complex, must close one of those two joints; the
audit found no third place for it to live.

Flags: selector = NONE (census-complete over filed
objects); pointer = BOUNCER + APEX; paraboloid =
PER-MASS, shape carries m, dynamics does not;
rho_status = POSTULATE (unchanged, v15.1163).
