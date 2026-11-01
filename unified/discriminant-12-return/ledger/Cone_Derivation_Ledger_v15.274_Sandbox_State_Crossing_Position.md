# Ledger v15.274 — Sandbox addendum to v15.272: position on the mass hyperbola is the opposite-sign parabola crossing

**Kind:** Sandbox addendum; exact identities + worked example.
**Origin:** Jeremy (2026-11-01): "and its position on that
hyperbola is the intersection of 2 opposite sign acceleration
parabolas."
**Producer:** `state_crossing.py` (clean exit).
**Payload:** `payloads/state_crossing_v15_274/` —
STATE_CROSSING.md, state_crossing.py, state_crossing_output.txt.

## Result
A crossing (n, k) read as E = AM = (n+k)/2, p = offset =
(n−k)/2, m = GM = √(nk) satisfies E² − p² = nk = m² identically
(the v14.550 diameter–secant identity): every crossing lies on
the boost hyperbola labelled by its own GM (v15.234 §B), and its
position along the hyperbola is the pair's ratio,
ψ = ½ ln(n/k) from the seat. The two opposite-sign parabolas
meeting at the crossing (v15.235) carry the light-cone components
u = E + pc, v = E − pc as labels, with uv = (mc²)² fixed; a boost
is the product-preserving split (u, v) → (λu, v/λ).

For the electron (v15.272): at rest the labels are equal,
u = v = 0.51100 MeV — the diagonal crossing of its own hyperbola,
the opposed pair in exact balance; boosted, the pair splits at
fixed product (E = 1 MeV: (1.85958, 0.14042), ψ = 1.2917 =
arccosh(E/m); E = 5 MeV: (9.97382, 0.02618), ψ = 2.9714). Rest
is balance; motion is imbalance at fixed product. A state's full
address: one hyperbola (mass from the product), one crossing on
it (position from the ratio).

**Seams.** The electron's labels are continuous (the parabola
families foliate continuously; the integer mesh samples them),
and on the integer mesh the seat crossing exists only for square
labels (present at N = 36; absent at N = 12, 60, where every
factor pair is sampled except exactly at rest). The continuum
pair always has its seat.

## Scope
Addendum to v15.272, binding v15.234 §B (level hyperbolas),
v15.235 (opposite-sign pairs), and v15.270 (mass shell). Exact
kinematics/dictionary; no gate, classification, or selector
statement changes.
