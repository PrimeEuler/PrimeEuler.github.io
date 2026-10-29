# Phase-cancellation / parabolic-ladder lattice test — RESULTS

Sandbox, 2026-10-29. Jeremy's idea: EM created the 1/4 lattice; gravity is
the residue of a phase cancellation. Producer: `ladder_test.py` (exact
rationals + sympy; run log `output.txt`, clean exit). NOT ledgered.

Levels kept separate throughout (ħ = 1): **P** pair product (EM eg ∈ ½ℤ;
TN εl ∈ ¼ℤ), **S** HJ twist (s_EM = eg; s_TN = 2εl — both ∈ ½ℤ),
**R** parabolic seat roots r± = (k ∓ s)/2.

## Part 0 — the ladder is s-blind [D]
MIC parabolic separation holds with **symbolic** s (residual exactly 0), and
TN − MIC is purely radial at s = 2εl. So the parabolic ladder operator
accepts any twist; it creates no lattice. Whatever quantizes s is imported
from fiber single-valuedness (Dirac for EM, Misner for TN).

## Part 1 — EM pairs DO generate a coordinate quarter lattice [D]
For two EM half-lattice variables A = p/2, B = q/2, the pair coordinates
C = (A+B)/2, X = (A−B)/2 lie in ¼ℤ on a checkerboard: 4C ≡ 4X (mod 2)
(exhaustive, 0 violations). Same parity (p,q) → C,X ∈ ½ℤ; opposite parity →
C,X both odd quarters. Example: A = 1/2, B = 0 → C = X = 1/4.

## Part 2 — cancellation condition [D]
Grouping by centre mod 1: X carries odd quarters **iff C itself is an odd
quarter mod 1** (C ≡ 1/4, 3/4 → X ∈ {1/4, 3/4}; C ≡ 0, 1/2 → X ∈ {0, 1/2}).
Exact cancellation C = 0 forces X = A ∈ ½ℤ — **complete cancellation kills
the odd quarters**. So an EM origin for quarter offsets requires the
"cancelled" common mode to leave an odd-quarter holonomy behind; bare
cancellation does not select it.

## Part 3 — no twist-level route to the dyon quarter [D]
½ℤ is a group: s1 ± s2 stays in ½ℤ. The only combination reaching ¼ℤ is the
offset coordinate (s1−s2)/2 — but fed into the seats as a twist it produces
root offsets in **⅛ℤ**, an eighth lattice that is not in the record
(falsified combination rule). And at minimal twist the seats cannot
distinguish the sectors at all: EM (s = 1/2) and TN (εl = 1/4, s = 2εl = 1/2)
give **identical seat charges** for k = 0..4. The quarter is invisible in the
twist and in the seats; it lives in the factorisation s = 2εl
(state ε × coupling l).

## Part 4 — the benchmark [D]
The dyon quarter is the Misner fiber spectrum ε_n·l = n/4. EM has no time
fiber and no ε. Its quarter (Parts 1–2) is a **coordinate** quarter
(centre/offset of a pair) — the same kind of quarter as the mesh/weld
coordinates. Identifying the coordinate quarter with the fiber-product
quarter is exactly the weld's node = state premise (v14.904), not a
consequence of EM phase algebra.

## Verdict
- **Mesh/coordinate quarter: EM-generable, conditionally** — opposite-parity
  EM pair + an odd-quarter centre holonomy. [D algebra; the holonomy's origin
  is open]
- **Dyon product quarter: NOT EM-generable** by phase combination. It needs
  the Misner fiber factorisation. [D, within the tested combination rules]
- "Gravity as phase-cancellation residue" survives only as an origin story
  for the *coordinate* quarter, and only if something fixes the centre at an
  odd quarter. It does not derive the fiber quarter, the dynamics, or κ —
  consistent with the v15.069 classification (κ empirical, product derived,
  split state/empirical).
