# Cone Derivation Ledger v15.689 — Gravity lane: seeded cavity spatial parity versus Cone sector parity

**Date:** 2026-11-11 US Eastern. **Parents:** v15.626–628 q=2 Casimir grading and odd-rung algebra; v15.676 standard parametric-pump gate; v15.680 finite-cavity seeded resonance; v15.686–688 temporal-selector and physical-length audits. **Status:** [D] exact abstract chi-odd EM→EM matrix-element no-go; [D] exact centered-cavity spatial-reflection selection rules for standing versus traveling seeded drives; [N] no derived intertwiner identifying Cone chi with cavity reflection parity; [C] a nonzero chi-mediated seeded response requires a chi-even effective interaction, two chi-odd factors/compensator, or a different physical sector assignment. **Immediately prewrite live HEAD:** 69d3a6552fd3872a768fe6354450e6c4877bdf2f. Collision searches found no v15.689 ledger entry or prior seeded-cavity chi result. Frozen Suzuki/far-tail objects untouched.

## Gate 241 — exact sector-parity theorem: a single chi-odd operator cannot connect ordinary EM states to ordinary EM states

For the q=2 Cone carrier,

**chi=(-1)^L**, with **P_EM=(1+chi)/2** and **P_G=(1-chi)/2**.

Let W be a minimal quarter-rung interaction satisfying

**{chi,W}=0**, equivalently **chi W chi=-W**.

Then exactly

**P_EM W P_EM=0**, **P_G W P_G=0**.

Therefore if both the initial and final physical states are assigned to the ordinary EM sector chi=+1, every matrix element of a single chi-odd interaction vanishes:

**<f_EM|W|i_EM>=0.**

This is not model-specific; it follows only from the grading.

Consequently, the proposal “use the q=2 odd quarter rung directly as the seeded EM cavity interaction” has an immediate obstruction. A nonzero EM→EM seeded conversion requires at least one of:

1. a **chi-even effective interaction**;
2. a product of **two chi-odd factors**, since odd×odd is chi-even;
3. an auxiliary chi-odd compensator like the formal construction of v15.628;
4. a physical state assignment in which the relevant cavity mode is not purely P_EM;
5. abandonment of the identification of the driving gravitational operator with the minimal chi-odd quarter rung.

The actual v15.602 q=2 cross-shell witness remains chi-even, but v15.627 already showed that it preserves rather than exchanges the EM/odd-quarter sectors, so it is not the missing gravity rung either.

## Gate 242 — ordinary cavity reflection parity gives real seeded zero/nonzero selection rules

Now separate the above internal sector grading from ordinary spatial reflection.

Take a centered 1D PEC cavity

**z in [-pi/2,pi/2]**

with normalized opposite-parity modes

**f_even=sqrt(2/pi) cos z,**

**f_odd=sqrt(2/pi) sin 2z.**

For the seeded fixed-wall Maxwell comparator of v15.680, the spatial source is proportional to

**S(z)=partial_z b(z).**

If the prescribed standing metric drive is reflection-even,

**b_even=cos(Kz),**

then

**S_even=-K sin(Kz)**

is reflection-odd. Therefore the exact overlap with every reflection-even cavity mode vanishes. In particular,

**integral f_even S_even dz = 0.**

The reflection-odd mode is generically allowed.

Conversely, for the reflection-odd standing drive

**b_odd=sin(Kz),**

the source

**S_odd=K cos(Kz)**

is reflection-even, and

**integral f_odd S_odd dz = 0**

while the even mode is generically allowed.

These are genuine physical symmetry zeros of the ideal centered cavity. They require no Newton G, no K4 Hubble scale and no quarter-grid frequency dictionary.

## Gate 243 — a traveling seeded drive generically destroys the exact reflection zero

For

**b_trav=e^(iKz)=cos(Kz)+i sin(Kz),**

the source contains both reflection parities:

**partial_z b_trav = iK cos(Kz)-K sin(Kz).**

Therefore a generic traveling drive has nonzero overlap with both the even and odd cavity mode classes. The exact standing-wave selection rule is recovered only when the physical drive is prepared in a definite reflection parity or when geometry/source placement enforces it.

Thus ordinary cavity parity is useful experimentally, but it is a statement about detector geometry and source symmetry, not by itself a Cone q=2 prediction.

## Gate 244 — why Cone chi is not yet the cavity parity operator

The q=2 Cone grading and centered-cavity reflection are both Z2 involutions, but abstract isomorphism of two Z2 labels is not a physical identification.

A physical claim needs an intertwiner I satisfying, for example,

**I chi = P_reflection I**

on the realized field-state space, together with a field operator whose transformation law under chi is derived from the dynamics.

No current ledger entry supplies such an intertwiner. In fact the present sector dictionary cuts the other way: the EM half-grid is the **entire chi=+ sector**, whereas a real EM cavity contains both reflection-even and reflection-odd Maxwell modes. Therefore identifying

**chi = spatial reflection parity**

would immediately conflict with the current statement that ordinary EM modes all live in P_EM, unless the sector interpretation is refined.

This is the key negative result: the exact q=2 parity cannot simply be relabeled as cavity mode parity.

## Verdict

The quarter-grid parity remains mathematically real and potentially useful, but the seeded cavity does **not** yet turn it into a new physical selection rule.

**[D]** Ordinary centered-cavity reflection gives exact zero/nonzero seeded overlaps for standing drives.

**[D]** Cone chi-odd quarter-rung operators have exact zero ordinary-EM→ordinary-EM matrix elements.

**[N]** No derived physical intertwiner identifies the Cone sector parity with cavity reflection parity.

**[C]** A viable Cone seeded-cavity mechanism would need a chi-even composite interaction, plausibly odd×odd, with both odd factors independently sourced. This is structurally similar to the compensator logic of v15.628, but no physical compensator has yet been identified.

So the best surviving Cone-specific cavity route is no longer “quarter frequency pumps half frequency” and not “chi directly equals spatial parity.” It is:

**find a physically derived second chi-odd ingredient such that the seeded effective Maxwell interaction is chi-even and acts within the EM sector, while its matrix elements are fixed by the existing geometry rather than an arbitrary coupling.**

**Reproducibility:** research-notes/seeded_cavity_chi_vs_spatial_parity_v15_689.py, additive commit 69d3a6552fd3872a768fe6354450e6c4877bdf2f. The script verifies the projector theorem, that the product of two chi-odd operators is chi-even, exact centered-cavity parity zeros, and generic nonzero traveling-wave overlaps. No figures and no protected Suzuki modifications.

**HANDOFF:** external audit/gravity/sandbox should verify the sector-parity theorem, the centered-cavity overlap zeros and the distinction between internal chi grading and spatial reflection. In particular, check that assigning all ordinary EM modes to chi=+ is indeed inconsistent with identifying chi directly with ordinary reflection parity.

**NEXT:** inspect the strongest existing candidates for the required second chi-odd factor: the static magnetic seed/background, charge-monopole/dyon operator, and the v15.628 auxiliary charge compensator. Determine their transformation under the q=2 grading from previously derived operators, not by declaration. If none is independently chi-odd, close the Cone-specific seeded-cavity parity branch as representation-theoretic only.
