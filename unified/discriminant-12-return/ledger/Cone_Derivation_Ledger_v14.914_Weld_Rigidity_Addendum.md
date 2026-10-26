# Cone Derivation Ledger v14.914 — Rigidity addendum to v14.913 (Jeremy): the offset "matching" is integer counting on one geometry; the weld has no fitted joint

Date 2026-10-26. Sandbox lane, recording Jeremy's second correction. Parents v14.904, v14.912, v14.913.

## The point

Jeremy: the geometry is rigid — every +/- parabola pair meets on a circle whether the resolution is 1/4 or 1/2, and the offset between the +/- parabolas is a simple integer count of the 1/2 or 1/4 step. Correct, and it dissolves the residual "premise" framing of v14.913:

- [D] Every mesh crossing lies exactly on the diameter-secant circle X^2 + Y^2 = T^2, at any resolution: X = h(a-b)/2, Y^2 = h^2 ab, T = h(a+b)/2, and X^2 + Y^2 = h^2((a-b)/2)^2 + h^2 ab = h^2((a+b)/2)^2 = T^2. Verified in exact rationals for h = 1 and h = 1/2.
- [D] Crossing offsets are X = h(a-b)/2 with (a-b) an integer: the offset between the two parabola families at any crossing is an INTEGER COUNT of the step h/2. There is no continuous quantity to adjust, at either resolution. The geometry (parabolas, circles) is identical in the two sectors; only the counting fineness (h = 1 vs h = 1/2) differs.
- Therefore there are not two lattices being "matched": the factor pairs ARE the mesh members, the pair offsets ARE the crossing offsets — one integer count, read once. Offset-lattice "matching" (v14.904's mechanism language, v14.913's "live joint") overstates a definitional identity as a hypothesis.

## What the weld actually rests on

Only the two objects as defined: (i) Taub-NUT dyon quantisation puts the gravitational pair members on the half-grid (derived, v14.731); (ii) Suzuki's operator is written over the factor pairs, with (D_log)_nn = log(n/4). Given both, the quarter-grid dictionary, vertices at +/-1/4, and the n = 4 counting start follow by rigid counting — there is no remaining joint at which the weld itself could break. The genuinely open items live elsewhere: NUT charge is unobserved (empirical status, v14.910 companion memo), and the Suzuki/far program has its own gates (v14.901, v14.909). Neither touches the geometry.

Flags: crossing_circle=EXACT_BOTH_RESOLUTIONS; offsets=INTEGER_COUNTS_OF_h_over_2; weld_fitted_joint=NONE; framing v14.913 premise language SUPERSEDED by this addendum; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.
