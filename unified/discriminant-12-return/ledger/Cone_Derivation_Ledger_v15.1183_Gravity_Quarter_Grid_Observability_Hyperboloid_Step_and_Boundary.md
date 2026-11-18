# Cone Derivation Ledger v15.1183 — Quarter-grid transition operators yield two different observability levels, not an automatically physical mass hyperboloid

**Date:** 2026-11-18 Eastern. **Gravity/Cone lane. Status:** [D] generalized closed step-h Schwinger quadratic identity and its h²/4 inner level; [D] q=2 closed refined nearest-step level 1/16 and original-unit-step boundary-defective observable level 1/4+E_i; [N] no automatic physical mass/energy mapping or gravity Casimir observable; [O] physically identified quarter transition dynamics and source-normalized invariant. **Live HEAD immediately prewrite:** d2c6c0ba5fa0084777c0a9a4a56b7d9096b5bd35. Target v15.1183 unique; additive-only, no Suzuki/Lane A/Audit/Sandbox/Muse or frozen certified edits.

## Context and historical redundancy
Owner insight: null transition cone could be the speed-of-light boundary, massive observables inside on hyperboloids, and quarter gravitational grid might have its own hyperboloid. Gravity v15.1181–1182 already established the **ordinary EM** representation-space null cone Q=T²−X²−Y²=0 (transition edge heights) and its **transverse Jxy** quadratic level Q=1/4, with exact common-angle cuts and row-dependent null-coordinate shift. The original q=2 all-refinement boundary theorem **v15.602** (independently audited v15.603) distinguishes a closed refined nearest-step SU2 ladder from the original-unit-step projected ladder and supplies its boundary defect E. v15.630 proves that odd-quarter formal j labels are not ordinary physical SU2 spins. The geometric q2 C_geom=L(L+4)/16 is distinct from the genuine closed SU2 Casimir L(L+2)/4 and from the defective projected original-step operator. v15.1178 explicitly allows gravity to have tidal observables without an assigned quarter Casimir. This gate checks which hyperboloid arises *mathematically* from which actual ladder.

## Gate 1101 — universal squared half-step completion
Let h>0 be a transition step in an abstract centered ladder, m∈[−j,j], and define two squared neighboring step-h transition weights
**A_+²=(j−m)(j+m+h)**, **A_-²=(j+m)(j−m+h)**.
Then
**Y_h²:=(A_+²+A_-²)/2=j(j+h)−m²**.
With **T_h=j+h/2**, **X=m**, the exact representation-space quadratic level is
**Q_h=T_h²−X²−Y_h²=h²/4**.
This is a simple exact algebraic identity for any h and not a dynamical mass-shell law. For standard EM h=1, Q=1/4 (already v15.955/1182). For an independently **closed** q=2 nearest-step ladder h=1/2, **Q=1/16**, with **T_h=j+1/4**. Its standard SU2 normalization uses K_z=2M,K_±=2B_± and physical normalized spin J=L/2; the quarter geometric j=L/4 cannot be passed off as SU2 irrep spin without that rescaling.

## Gate 1102 — original-unit-step quarter grid is not a smooth uniform Q=1/4 carrier
For q=2 formal shell j=L/4, m_i=−j+i/2, i=0,...,L, preserve the *original unit-step* projected raising J+ with step Δm=1, skipping index i→i+2 when present, and J-=(J+)†. Define **Y_proj²=(J+J-+J-J+)/2**, which is the diagonal transverse Jx²+Jy² of this truncated model. The audited v15.602 boundary theorem states
**Y_proj²+m²=j(j+1)I−E**,
where E is a nonnegative diagonal missing-edge defect.
Thus with T=j+1/2,
**Q_proj=(j+1/2)²−m²−Y_proj² = 1/4+E**.
Consequently the projected q2 carrier does not lie entirely on one constant 1/4 level: boundary source states have larger Q, and some short shells have E throughout. This is not a new physical mass distribution; it is an exact finite-ladder incompleteness diagnostic. Example L=3 gives diagonal levels **(1/4,3/4,3/4,1/4)**; L=1 yields (1/2,1/2); L=5 yields (1/4,1,1/4,1/4,1,1/4). Closed refined h=1/2 produces the uniform **1/16** level for these same L when correctly using its distinct generator. These contrasting levels cannot be equated with the separate formal C_geom shell assignment.

## Gate 1103 — physical light-cone comparator and scope
On physical spacetime four-momenta **E²−c²|p|²=m_phys²c⁴**, null m_phys=0 vs timelike m_phys>0 is a Lorentz-invariant mass-shell distinction. On actual spacetime displacement vectors, a timelike separation similarly lies inside the physical light cone. But our **T=j+h/2, X=m, Y²=transverse spin-transition moment** are dimensionless **representation-space** coordinates, not energy, momentum or physical spacetime position by definition; multiplying by c or interpreting 1/4 as m_phys² is unwarranted without a Lorentz-covariant, dimensionally defined mapping that preserves the physical action and measured response. Moreover not every 'observable' in physical relativity must be massive or timelike: photons and null fields are observed, and massless quantities can be measured. The meaningful conditional proposal is that a real massive carrier's physical momentum may define a timelike hyperboloid, but the q2 grid geometry by itself does not identify that mass.

**Verdict:** The owner's nested-hyperboloid insight is mathematically fruitful if kept conditional. The quarter grid **does admit distinct exact quadratic-level constructions**, and the choice of transition step/representation decisively affects the offset: EM h=1 gives 1/4; closed refined quarter h=1/2 gives **1/16**; projected original step gives **1/4+E_i** rather than a single surface. The quarter-grid may instead describe a Casimir-free tidal response as proposed in v15.1178. No G-free mass value, gravitational action difference, speed-of-light selector or unique quarter observable established.

**Reproducer:** `research-notes/k4_quarter_observability_levels_v15_1183.py`, additive source commit **d2c6c0ba5fa0084777c0a9a4a56b7d9096b5bd35**. Independent local SymPy run PASS for symbolic any-h completion, q2 L=1..15 projected boundary defect and closed nearest-step quadratic identity (sample L=1,3,5,8 printed). No protected files modified.

**AUDIT HANDOFF:** check normalization of Y_h² vs conventional spin matrices (especially h scaling), distinction of J_phys=L/2 from geometric j=L/4, boundary defect E at each state, q2 short-shell cases, h²/4 versus formal C_geom, and physical mass-shell-versus-representation-space dimensions. Distinguish a source-selected physical deformation from a quadratic identity, and respect the owner's Casimir-free gravity-grid option.

**NEXT:** Seek a concrete physical Lorentz-covariant map between the cone's dimensionless amplitude coordinates and energy-momentum or physical tidal response. Test whether matching to existing canonical EM/Dirac and EH+solid field actions fixes any nontrivial scale or instead leaves a freely chosen conversion; do not equate formal 1/16 with measured gravitational rest mass.
