# AM–GM multi-split diameter, the (n+k)/(n−k) ladder, and the means as conics (Sandbox)

Origin: Jeremy's question — the AM side was only ever divided once; the
single GM was then squared/cubed for higher dimensions. Does dividing
the diameter into multiple sections, each with its GM, still work?
All results [D], machine-verified (payload scripts). Signature objects:
diameter D, sections s_1..s_m, cumulative S_i, boundary height
h_i = sqrt(S_i (D − S_i)), offset X_i = S_i − D/2.

## Multi-split: works, with cumulative pairs [D]

Every boundary is an honest pair-crossing (S_i | D − S_i) with
X_i² + h_i² = (D/2)² and the SAME center AM = D/2 for all boundaries —
the multi-split diameter is a set of crossings on one T-slice.
Generalized GM²: **sum_i h_i² = sum_{j<l} (l−j) s_j s_l** (symbolic,
m = 2, 3, 4), the separation-weighted pair-product sum; equal sections:
sum h_i² = s²(m−1)m(m+1)/6 = s² C(m+1, 3). m = 3 product:
h_1²h_2² = ac(a+b)(b+c). Symmetric divisions pair up equal GMs
(Jeremy's examples: D = 10, divisions at ±4 = sections (1, 8, 1), pair
(1|9), GM = 3, the 3-4-5 rung, ladder 3² = 9, 3³ = 27; equal thirds:
boundaries at ±5/3, GM = 10√2/3).

**Negatives [D]:** the local GM of adjacent sections is NOT a chord
height ((1,2,3): √(2·3) = √6 vs actual height 3 — the boundary sees
the cumulative pair (3|3)); subdividing a section starts a smaller
circle (different T-slice). The m-factor GM (prod s_i)^{1/m} is not a
chord height nor any monomial in (h_i, D) (exponent fit predicts 3.79
vs actual 2.71 on a held-out triple). The circle carries cumulative
pairs, not the sections' own GM.

## The ladder (Jeremy's construction) [D]

Stepping across the circle with (n+k)/(n−k) steps (= sec φ = coth ψ of
the split) gives an (n+1)-dimensional AM–GM object: the diameter plus
one GM height per step. Diameter-12 rungs: GMs √11, √20, √27, √32,
√35, 6, … (the antinode amplitudes, Y² + X² = 36), step ratios
6/5, 3/2, 2, 3, 6, ∞, 6, …, center rung ratio divergent, GM = A = 6.

Ladder aggregates on diameter m (unit sections; verified m = 10, 12):
- **prod G = (m−1)!** (the ladder volume; left/right parts each
  telescope to (m−1)!)
- sum G² = (m−1)m(m+1)/6 (tetrahedral)
- sum Q² = (m−1)m(2m−1)/6 (square-pyramidal)
- sum H = (m²−1)/3
- prod H = ((m−1)!)²/A^{m−1}, A = m/2 (via H = G²/A per rung)
- **prod Q does not collapse** (m = 12: prod Q² = 1606635342973440000):
  n²+k² has roots off the ladder (n = 6 ± 6i for m = 12), so no
  left/right telescoping — a Γ-type value, not a factorial.
- A = m/2 at every rung in every dimension (the invariant center);
  ladder-level chain H̄ ≤ Ḡ ≤ A ≤ Q_rms (m = 12: 4.33 ≤ 5.01 ≤ 6 ≤ √46).

Per rung on the circle [D]: A = radius; G = half-chord;
Q² = A² + X² (Q = segment from split foot to top of circle);
H = G²/A (AH = G² exact; H is the derived third proportional, NOT
itself a chord height on the same circle).

## The means as conics [D]

Chord = 2G is the opening between the ± branches of the row/column
parabolas at a crossing. Row walk (pair (u, 2T−u), u fixed, T grows):
- A = T — the diagonal line
- G² = 2uT − u² — the parabola (the mesh row parabola)
- H = 2u − u²/T — hyperbola, saturating at 2u (H = Y²/T)
- Q² = 2T² − 2uT + u² — hyperbola branch, ~ √2·T
Growth regimes: saturating / √T / linear / √2-linear.
Offset walk (fixed diameter 2A, pair (A±X)): A = const (line),
G² = A² − X² (circle), H = A − X²/A (downward parabola),
Q² = A² + X² (hyperbola) — the four means are the four conic types,
with G and H exchanging the parabola role between the two walks.

## Scoped assessments (asked and answered in-session)

**Gravity:** no selector contact (34! and 35! bracket the Dirac ratio
2.27e39 by ×7.7 / ×4.6 — no hit, no mechanism). The volumes are
grid-dependent (diameter 12 on the gravity grid h = 1/2: volume
23!/2²³ ≈ 3.08e15 ≠ 11!), so they fail the weld's grid-invariance
test; no action/current (charge question untouched); Pantheon shape
untouched. Only overlap: W₂'s N³/6 shares the tetrahedral pair-sum
skeleton with sum G² — counting skeleton, not mechanism.
**Suzuki:** the ladder GMs are the semicircle-envelope samples (the
J1/dictionary ground of v14.593); log prod G = sum ln n is the Γ/log
currency of (D_log) and the archimedean factors. No contact with the
far/K_full spectral gates; the physical quarter weld remains PARKED
(v14.916) — the ladder ran on unit sections and produces
products/sums, while the Suzuki side consumes logs/transforms.

**Payload:** multisplit.py, ladder.py, means_conics.py, this NOTE.
