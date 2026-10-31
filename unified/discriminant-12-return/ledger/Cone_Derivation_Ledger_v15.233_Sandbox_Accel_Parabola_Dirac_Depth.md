# Ledger v15.233 — Sandbox addendum to v15.230 §3: the acceleration parabola vs the Dirac depth; crossing range

**Kind:** Sandbox addendum; exact algebra + numeric check,
catalog discipline as in v15.230 §3 (no derivation claimed).
**Origin:** Jeremy (2026-10-31): "every parabola crosses a
hyperbola — what does the acceleration parabola (9.8 m/s²) look
like compared to the Dirac depth?"
**Producer:** `accel_parabola.py` (clean exit).
**Payload:** `payloads/accel_parabola_v15_233/` — ACCEL_PARABOLA.md,
accel_parabola.py, accel_parabola_output.txt.

## Depth comparison (negative)
Log-depth below the Planck acceleration a_P = 5.5607e51 m/s²: the
1 g parabola sits at ln(a_P/g) = 116.865 = 2.5792 × psi_D
(45.310004305, v14.621); excess 71.555, factor 1.19e31. No lock —
consistent with v15.230 §3's depth check. The acceleration at the
Dirac depth itself, a_P e^{−psi} = 1.1675e32 m/s², has Rindler
length c²/a = l_P e^{psi} = 7.698e-16 m (0.915× proton charge
radius; 3.66× proton reduced Compton): recorded as fermi
neighbourhood, NOT an identity — psi was constructed from
proton/electron data, so a fermi-scale output is partly built-in.
Geometric reading only: psi_D is the depth at which the
acceleration parabola's bend radius shrinks from a light-year to
a proton.

## Crossing range (exact)
In edge-pinned units u = gt/c, xi = gx/c² (parabola xi = u²/2,
edge xi = u):
- Parabola × null edge: crosses at u = 2 exactly (t = 1.9374 yr,
  x = 1.9374 ly) — the Galilean trajectory exits the cone there.
- Parabola × its own Rindler hyperbola xi = sqrt(1+u²) − 1:
  tangent at the vertex (difference u⁴/8 − u⁶/16 + …), strictly
  outside thereafter — NEVER crosses. The relativistic curve bends
  toward the edge and stays inside; its Galilean shadow leaves.
- Parabola × interval hyperbolas u² − xi² = sigma²: two crossings
  iff sigma < 1 (u² = 2 −/+ 2 sqrt(1−sigma²)); one grazing
  crossing at sigma = 1 (u = sqrt(2), xi = 1); none for sigma > 1.
Hence Jeremy's sentence in its exact form: every parabola crosses
every hyperbola INSIDE its own Rindler scale — twice — grazes the
one at its scale, and is blind to the rest. The crossing geometry
is scale-free; only the reach (set by c²/g) changes.

## Scope
Addendum to the v15.230 catalog; no gate, classification, or
selector statement changes.
