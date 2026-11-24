# Cone Derivation Ledger v15.1405 — Current conservation alone cannot turn geometric 3:1 null-affine spacing into a uniquely weighted physical flux

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [EXACT NEGATIVE] there are multiple smooth divergence-free ambient null-coordinate currents which assign different nonnegative **illustrative integrated null-line weights** to the identical, Lorentz-covariant geometric three-sheet intersection of v15.1404; [POSITIVE conditional] if the current is further constrained to a purely null-flow component with zero transverse transport and uniform affine density, the 3:1 geometric spacing becomes a 3:1 density-integral weighting; [OPEN] derivation of a specific physical current, the null-line measure from a covariant action/canonical structure, physical state preparation, full Maxwell/quarter intersector coupling and independent G-free observable. **Immediately preledger HEAD:** 83645a66ffd5cabedf8afab11ec1304bd9417f67. Additive, certified archives untouched.

## Gate 1335 — a physical transport density is an extra law, not a geometric distance

The v15.1404 null-affine triple lies on U=U0,Y=Y0 with V values (after translating V by V_null=Y0²/U0) `V_null=0,V_q2=h,V_EM=4h`, where `h=1/(16U0)>0`. It has exact affine lengths h and 3h and Lorentz-covariant ratio 3, with no rapidity or bulk-volume cutoff. A physical transition amplitude or probability nonetheless needs a **specified current and measure**. Merely assigning a uniform weight to every affine V interval is not implied by the Einstein, Maxwell, K4 or unselected continuous H² action.

On flat null-coordinate ambient representation space `(U,V,Y)`, consider the family of vector fields

`J^U=−d U,quad J^V=c+d V,quad J^Y=0`, with c>0,d≥0.

Its ambient divergence is identically **`∂U J^U+∂V J^V+∂Y J^Y=−d+d=0`**. Thus it obeys the same geometric current-conservation condition for every d (note that for d>0 it also carries U-directed transport; it is not a unidirectional purely-null flux along the selected V generator). If, as one *illustrative proposed readout*, we weight the two intervals by integrating the component J^V with affine measure dV along the selected null line, we obtain

`W_inner=∫_0^h(c+dV)dV=c h+(d/2)h²`,

`W_outer=∫_h^(4h)(c+dV)dV=3ch+(15d/2)h²`,

and the general ratio

`W_outer/W_inner=(3c+(15/2)dh)/(c+(1/2)dh)`.

For d=0, uniform affine density yields the **geometric 3:1**. For d*h=c, another strictly conserved ambient current yields **7:1**, and as d increases this weighting approaches 15:1. This shows *conservation alone does not force 3:1 even on the exact 3:1 null-affine triple*. The 7 here is **not** the physically same construction as v15.1401's 7:1 rapidity-regularized volume; their numerical equality for this illustrative density choice is not a law or independent confirmation.

**Crucial precise scope:** `∫J^V dV` on a null line is an **illustrative candidate line weighting**, NOT automatically the conserved 2D flux through a physical detector hypersurface. True flux requires specifying the oriented surface element, observer/detector and field action. The example is a counterexample to deducing *any uniform affine weighting* from divergence-freedom alone, not a proposed new electromagnetic probability density. If one *adds* the strong assumptions J^U=J^Y=0 and no Y-dependence, then ∇·J=0 forces ∂VJ^V=0, selecting constant V density and hence 3:1. Those assumptions about permitted transport are precisely the missing physical selector.

## Gate 1336 — exact numerical and symbolic certification

Locally executed exact SymPy script `/mnt/data/cone_gate/k4_null_flux_measure_selector_v15_1405.py` passed all conservation, integration and ratios. Additive equivalent `research-notes/k4_null_flux_measure_selector_v15_1405.py`, commit **83645a66ffd5cabedf8afab11ec1304bd9417f67**; precise committed-byte independent Audit replay pending.

**AUDIT:** verify the exact conserved current and its coordinate divergence in flat null coordinates, the ratio after shift V−V_null, all integrated weights, and explicitly enforce the distinction between the proposed null-line weighting and true physical hypersurface flux. Check that any future scalar-current candidate is a bona fide Noether/symplectic current for a stated action and satisfies positivity/unitarity and true detector normalization. Independently replay the two earlier bridge scripts v15.1403 and v15.1404, including the corrected historical Dirac-force hierarchy and covariance of the collinear null triple.

**NEXT:** seek an action that *forces* J^U=J^Y=0 or another prescribed distribution, rather than choose it; simultaneously derive a representation-to-physical-spacetime map that determines a measurable source, detector and dimensions. Compare candidate intersector operator against v15.1397's conditional low-rank tensor obstruction and v15.1398's quarter-radius/coupling degeneracy. Without such a selector, the 3:1 null-affine ratio and the ln2 matched-U boost shift are exact mathematics but NOT gravitational predictions or derived G.
