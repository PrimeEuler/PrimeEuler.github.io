# The flip: gravity creates the grid, a phase offset creates EM

Sandbox addendum, 2026-10-29. Producer `flip_test.py` (exact rationals,
clean run). NOT ledgered.

## Result [D, lattice level]
Start from gravity's quarter checkerboard (C, X ∈ ¼ℤ, 4C ≡ 4X mod 2;
1,089 points in the test window). A staggered phase offset — a second
channel translated by half a period, carrying the sign character
χ = (−1)^{4C} — interferes as (1+χ)/2 and leaves **exactly** the EM
sublattice: 545 survivors, all with C, X ∈ ½ℤ; the 544 cancelled points are
exactly the odd quarters. (Same partition as the EM-first test's
same/opposite-parity split, read from the other end.) Ladder reading: if U
steps one quarter rung, the EM ladder is U²; the phase offset is the
ℤ₄ → ℤ₂ grading character of the gravity ladder. Quotient (¼ℤ)/(½ℤ) ≅ ℤ₂.

## Assessment
- This direction is the record's native one: q_G = ¼ is derived (Misner /
  Killing triad, v14.731), and EM's half-lattice as the even sublattice is
  already §4 of that entry. The flip adds a *selection mechanism*:
  EM = quarter grid + parity phase lock.
- Precedent: Kaluza–Klein — a phase (fiber momentum) on a gravitational
  fiber appears in 4D as EM charge. The grid version avoids KK's radius
  problem: the fiber here is the universal mesh, not one TN solution's l
  (l is a charge; a charge-dependent e would be fatal).
- Debts, mirroring the EM-first direction: (1) a projector selects, it does
  not create — a dynamics that locks the relative phase (a potential with
  the offset as its minimum) is owed; (2) EM's dynamics and the value of e
  are not supplied — α stays empirical/selector class (v15.069); (3) the
  odd-quarter sector must be somewhere: the flip predicts gravity-only
  rungs (P1's h = 1/2 at every k is the standing falsifiable form).
- Net: gravity-first is the more economical direction (one derived lattice
  + one ℤ₂ projection, no imported holonomy), but "creates EM" currently
  means "assigns EM its lattice address," not a derivation of Maxwell
  theory or of e.

## Test 2 — operator level (`flip_operator_test.py`, clean run)

Finite gravity ladder: 24 quarter sites on a ring, U = quarter step,
H_EM = U² + U⁻², H_grav = U + U⁻¹, grading χ = (−1)ⁿ, P = (1+χ)/2.

- [χ, H_EM] = 0 exactly; {χ, U} = 0 exactly; PUP = 0. EM dynamics preserves
  the phase-offset sectors; every gravity step flips sector.
- U² has exactly two orbits (evens, odds), 12 sites each; each sector's
  H_EM spectrum equals the half-lattice ring's **exactly** (max deviation
  0.00e+00), and the full spectrum is two identical copies. The odd copy
  sits at positions 1/4, 3/4, 5/4, … — the EM lattice translated by ¼ rung
  = half an EM period = a π phase offset in EM's own phase variable.
- No EM-internal observable distinguishes the copies (same moral as
  v14.770: grid offset is spectrally invisible). Only U — the gravity
  step — sees the offset.
- A χ-potential −λχ rigidly splits the copies by 2λ and does nothing else.
  That term *is* the phase lock: a staggered rung potential. Nothing in
  MIC/TN currently generates it. Open concrete question: does the bicone's
  two-sheet alternation supply a staggered sign on quarter rungs?

**Priority verdict:** the two directions are one operator fact (U vs U²
orbits). The lattice cannot decide which created which; the record can —
U has a derivation (Misner period 8πl), the EM-side U² dynamics has none
yet. Gravity-first remains the economical reading; "phase offset creates
EM" is operator-true as *sector selection*, with the χ-lock as its named
debt.

## Correction (2026-10-29, Jeremy: "the casimirs are different")
Test 2's sentence "No EM-internal observable distinguishes the copies"
is **superseded** — it was an artifact of the translation-invariant ring
toy. On the cone, the Casimir j(j+1) is EM-internal and separates the
sectors completely (even diagonals: C ≡ 0, 3/4 mod 1; odd diagonals:
C ≡ 5/16, 13/16 mod 1). See CASIMIR.md. The grading algebra of Test 2
stands; the invisibility moral does not.
