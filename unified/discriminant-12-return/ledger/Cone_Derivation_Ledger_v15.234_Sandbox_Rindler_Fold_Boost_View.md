# Ledger v15.234 — Sandbox addendum to v15.233: the parabola in the Rindler frame; the grid's view of boost hyperbolas

**Kind:** Sandbox addendum; exact algebra + numeric scans.
**Origin:** Jeremy (2026-10-31): "what are these parabolas in the
Rindler frame?" and "how does this parabolic acceleration grid
see our boost hyperbolas?"
**Producers:** `rindler_parabola.py`, `boost_grid.py` (clean
exits).
**Payload:** `payloads/rindler_boost_v15_234/` — RINDLER_BOOST.md,
rindler_parabola.py, rindler_parabola_output.txt, boost_grid.py,
boost_grid_output.txt.

## A. The parabola in its own Rindler frame (exact)
With X = x + c²/g and X = ρ cosh η, ct = ρ sinh η, the Galilean
parabola x = (1/2)gt² becomes ρ² = (c²/g)² + ((1/2)gt²)² — the t²
terms of X² − c²t² cancel identically, the algebraic form of
v15.233's parabola–hyperbola tangency. ρ departs monotonically;
Rindler time folds: η_max = ln(1+√2) = 0.881374 at u = gt/c = √2,
ρ = √2 c²/g, then η decreases to 0 as ρ → ∞ (the parabola runs
backward in Rindler time on its outer branch — its
superluminality, translated). The fold point IS v15.233's σ = 1
grazing crossing seen from the accelerated frame; the inertial
edge crossing (u = 2) sits on the returning branch at
η = (1/2) ln 5, equal to the outbound u = 1 point's η.
Family: a parabola of acceleration a in the frame of g dips in ρ
first iff a < g, exits the wedge through the horizon before
folding iff a < g/2, folds exactly on the horizon at a = g/2
(η → ∞), and folds inside for a > g/2 with η_max decreasing in
a/g (1.1462 at 3/4; 0.8814 at 1; 0.5493 at 2; 0.3695 at 4); a = g
is marginal (ρ flat to fourth order at departure).

## B. The grid's view of the boost hyperbolas (exact)
In pair coordinates (X = (u−v)/2, T = (u+v)/2, Y = √(uv)), the
boost hyperbola uv = s² is seen by the parabolic grid as:
(1) completely resolved — every row and every column meets it
exactly once (v = s²/u); (2) read as the AM/GM split — GM = s is
its label, AM = GM cosh ψ and offset = GM sinh ψ along it, so
γ = AM/GM = cosh ψ (v14.621) is the grid's reading of a boost,
with AM minimized at the diagonal vertex (ψ = 0, the hyperbola's
seat); (3) discretely sampled ONLY at factor pairs — the lattice
points on uv = N are exactly (d, N/d), all carrying ladder
amplitude √N = GM, so a boost moves a crossing continuously
along its hyperbola and meets the grid exactly at divisor pairs
(boost composition = multiplication in the table); (4) lifted,
it is the LEVEL curve Y = GM — the mesh parabolas climb, the
boost hyperbolas run level, and every mesh crossing is a triple
intersection of a row, a column, and one level hyperbola. The
Rindler frame's ρ = const lines are these hyperbolas: the
accelerated observer's rulers are the grid's level sets.

## Scope
Addendum to v15.233; kinematics and grid-reading only. No gate,
classification, or selector statement changes.
