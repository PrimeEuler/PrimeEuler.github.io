# Duck test, the rest: shaping, acoustics, and the Suzuki side

*Sandbox (little Euler), 2026-10-19. Continuation of
`runs/20261019-duck-test/` (v14.628), which tested the rotor
sector only and found identity. Same criterion: a rhyme is
identity iff forced — same equations, no free parameter in the
map. Producer: `shaping.py`.*

## 1. Shaping sector — NOT forced (analogy by design)

Question: is the model's void profile r² = 2|X| + 1 the
equilibrium of the ferrofluid in the coil field, or an imposed
shape? In the clean regime (static, zero-g, no spin) the
Rosensweig condition makes the interface a level set of |B|
(any monotone saturation law gives the same level sets).
Level set through the design throat (0, 1), units of the V4
design:

- **Single center loop** (a = 6.5): deviations from the
  parabola −12.7% (X = 0.5), +3.5% (X = 1), **+64% (X = 2)**;
  beyond |X| ≈ 2–3 the level set through the throat **ceases
  to exist** — the axial field falls too fast to hold the
  surface; the physical void opens up. A single coil makes a
  short fat pinch, not the long paraboloid.
- **Totient ring set** (a = 6; turns 50/106/115/92 — turns set
  by the on-axis amplitude criterion, not by profile fitting):
  tracks within −15%…+3% to |X| = 2, +16% at |X| = 3, then
  runs away: **+46% (X = 4), +53% (X = 5)** — the level set
  bulges toward the outer wires.

Verdict: the physical equilibrium is a |B| level set of the
coil field, a different curve from the circle's parabola
(tens of percent at the mouths; non-existent at length for a
single coil). Holding r² = 2|X| + 1 exactly is an inverse
problem (choose the winding to make a level set be the
parabola) — design, not discovery. Gravity and spin perturb
further (device thread). **The shaping rhyme is engineered
approximation, now quantified.**

## 2. Acoustic sector — split verdict

- **Wave level: forced.** The focuser selects its center by
  interference: the transducer caps are sections of
  core-centered spheres (station distances exactly 3, 4, 6;
  sagitta exactly 1 — verified in the focuser thread), so the
  drive arrives in phase at the core; the center antinode is
  selection by phase-coherent addition — the same mechanism
  as the overlay's exact collapse to 12πδ₀. Superposition has
  no free parameters; the integer station distances make the
  phasing exact at commensurate wavelengths.
- **Ray level: false.** Rays from the focus reflect off a
  paraboloid axis-parallel (collimation — the searchlight
  direction); they do not return to the center. The trap is a
  wave/Bjerknes trap, not a ray retroreflector. (Consistent
  with the sphere-optics ray trace: source at the focus exits
  collimated, 0.00° deviation.)

## 3. Suzuki/channel side — no device duck

The channels 𝒜_χ are pure spectral mathematics; no device
counterpart exists to test a correspondence against. The only
structural bridge: the focuser's Helmholtz problem separates
in parabolic coordinates — the same PDE family as the
parabolic dipole (α note) and the bouncer's Airy asymptotics.
A shared skeleton, not an identity of spectra. Recorded as a
boundary, not a result.

## Summary of the whole duck

- Rotor sector: **identity** (v14.628).
- Acoustic selection: **identity at the wave level**; ray
  version false.
- Shaping profile: **analogy by design**, deviations
  quantified (§1).
- Suzuki side: untestable — no counterpart.

The duck is real in its skeleton (couplings, selection) and
cosmetic in its silhouette (the fluid profile). Both halves
are now on record with numbers.
