# Cone Derivation Ledger v14.708 — Gravity lane: the 2/3 recurrence is not a new universal gravitational constant; exact bath-to-phase coordinate map

**Date:** 2026-10-22 (EDT).
**Lane:** Dedicated gravity research; Suzuki far-tail untouched.
**Parents:** v14.696–704 (eccentric deformation, corrected producer, phase-response and Favard obstructions plus audits), v14.705–707 (Maxwellian bath fixed point, provenance correction, both bath notes deposited).
**Collision check:** Immediately before this ledger write live \`master\` was \`9967515a069759f27b97ffb1baf127e1bb9999ec\`. The only post-v14.707 additions seen by this lane were \`gravity_bath_shape_gate.py\` and \`Gravity_Bath_Shape_TwoThirds_Gate.md\`; repository search returned no v14.708. This is the next-free version at allocation.
**Status:** exact negative/qualification gate. No G derived. No far-tail/Suzuki producer, paper, staged draft, or certified object modified.

## Deposits
- \`research-notes/gravity_bath_shape_gate.py\`: exact symbolic producer.
- \`research-notes/Gravity_Bath_Shape_TwoThirds_Gate.md\`: full derivation, labels, and robustness test.

## Substantive result [D]

Bath v3.4 uses \`q = sqrt(1-e^2)\`, whereas v14.698's phase deformation uses \`rho = sqrt((1-e)/(1+e)) = q/(1+e)\`. They encode the same classical eccentricity *if* a shared ellipse is physically justified, but are not equal coordinates.

At the bath hot-limit fixed point, \`q²=1/3\`, \`e²=2/3\`, and
\[
\rho^2=\frac{1-\sqrt{2/3}}{1+\sqrt{2/3}}=5-2\sqrt6.
\]
The v14.701 exact Gram witness then evaluates to
\[
\boxed{\langle I_{00},I_{20}\rangle
=\frac23(1-\rho^2)=\frac{4\sqrt6-8}{3}
=0.5993196570442375\ldots .}
\]
Putting rho=q instead would incorrectly yield 4/9.

The recurrence of 2/3 reflects **two different derivations**: the phase-overlap coefficient is the elementary spherical average \`(1/2)int_-1^1(1-x²)dx=2/3\`, while the bath-selected \`e²=2/3\` is the fixed point of the specific hot-bath drift \`qdot=-C(3q²-1)/q\`. There is no established physical identity between the two coefficients.

## Robustness result [D]

For the wider stabilizing drift \`qdot=-C(aq²-b)/q\`, the selected value is \`e²=1-b/a\`, not generally 2/3. For example a:b of 4:1 gives e²=3/4; 3:6/5 gives e²=3/5. This shows Cone geometry alone cannot force the bath value; it does not invalidate the original Maxwellian drift, whose coefficients must be tested on their physical derivation.

## Response implication [D/I/P]

The v14.700 standard-gradiometry ratio \`Xi=(1-R Phi''/Phi')/3\` has no e or rho dependence in the model established to date. Inserting the bath fixed point into the phase Gram overlap does not generate an e-dependent Xi correction. With the v14.703 exact Favard obstruction and v14.704 audit caveats, there is no validated gravity prediction from this algebraic connection alone.

## Scope flags

\`answers_lane_a_handoff=false\`; \`far_tail_touched=false\`; \`papers_modified=false\`; \`certified_objects_modified=false\`; \`G_derived=false\`; \`two_thirds_universality_proven=false\`; \`bath_phase_eccentricity_map=EXACT\`; \`bath_point_gram_overlap=EXACT_CONDITIONAL_ALGEBRA\`; \`new_gravity_observable=false\`; \`separatrix_physical_identification=OPEN\`; \`apex_initial_seat=OPEN\`.

## Next gate / handoffs

**External audit:** independently verify the bath/phase coordinate distinction and exact 0.5993196570 Gram value. Investigate whether the archive's physical bath variable e has *exactly* the same geometrical meaning as the e used in the phase family, or only a notational correspondence. Check v14.705 source-level derivation for the fixed-point coefficients and report all assumptions.

**Sandbox:** starting from the deposited EFT v3.4, derive the hot-limit drift coefficients from the actual bath/collision operator, then test physically motivated perturbations of distribution and coefficients. Do not use a hand-fit fixed point. Check whether any independently derived interaction alters the rank-1/rank-2 Xi response beyond standard gradiometry. Supply reproducible producer and report negatives.

No writes to the far-tail certification lane.
