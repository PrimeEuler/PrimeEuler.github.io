# The gravity tangency circle, in the weld dictionary

*Sandbox note (little Euler), 2026-11-13. Jeremy: the EM
ħ unit circle has its transition parabola at 1/2 — does
the 1/4 gravity parabola have a different circle?
Built in the weld dictionary (v14.904) on the
diameter–secant machine of v14.620, extending the
tangency chain of v15.864. Producer: `gravity_circle.py`
(symbolic in h and j; exact rational cross-checks).*

## The machine, per sector [D]

A sector has step h (weld: EM h = 1, vertices ±1/2,
diagonal log n; G h = 1/2, vertices ±1/4 = ±q, diagonal
log(n/4); matching h = 2q). Its transition
(consecutive-node) split at level j is
(n, k) = ((j+1)h, jh), with

AM = h(j + ½),  GM = h√(j(j+1)),  offset = h/2,

and AM² − offset² = GM² identically — the pair point
(offset, GM) lies on the secant circle of radius AM.

## The answer: a different circle, the same quantum [D]

- **Radius.** The figure is h-similar: at every level
  the G circle has exactly half the EM radius
  ((j+½)/2 vs j+½), and the tangency circle of
  v15.864 (radius = the state's GM) halves with it.
  In the common plane it is a genuinely different
  circle; the transition point's angular position on
  it, offset/AM = 1/(2j+1), is sector-independent —
  same shape, half size.
- **The dictionary is one-parameter.** q = h/2 and the
  diagonal's constant is c = 1/h² (EM log(n/1), G
  log(n/4) — the weld's values, recovered); the G
  sector's unit node sits at n = c = 4, EM's at n = 1.
- **The spectral correction differs.** offset² = h²/4:
  EM's is ¼ (the universal quarter of the
  Casimir/Langer/Maslov/bouncer record); gravity's is
  **1/16**. Cross-check against the lanes' record: the
  quarter grid's Casimir residues are exactly
  {5/16, 13/16} (v15.544 §4, recomputed here), and
  the vertex value decomposes as q(1+q) = q + q² =
  1/4 + 1/16 at q = 1/4, against EM's (1/2)(3/2) = 3/4.
  The sixteenths in the quarter sector's spectral data
  are the G circle's offset² showing through.
- **The quantum does not halve.** Per v14.620, ħ
  appears in none of the machine's formulas: it is the
  exchange rate (action per radian) named when the
  lattice is read as action. The weld rescales the
  lattice, not the rate: the G state's tangency circle
  has half the radius and twice the Compton period,
  and the cycle action is ħ again — the second and
  third candidate outcomes of the question (different
  radius at fixed ħ; same construction) hold jointly,
  and the half-quantum outcome is excluded by the
  dictionary itself.

Scope: this is the weld dictionary exhibited as a
construction, uniform in j — the shape prediction P1
(h = 1/2 at every k) asserts. It is not evidence for
P1, and it touches neither G's value nor the ψ
selector: the two sectors share one action quantum and
differ in step, radius, and correction.
