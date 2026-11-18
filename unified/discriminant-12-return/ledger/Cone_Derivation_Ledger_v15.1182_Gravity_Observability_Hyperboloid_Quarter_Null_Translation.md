# Cone Derivation Ledger v15.1182 — The transverse Jxy 'cone of observability' is a quadratic hyperboloid and a row-dependent null translation

**Date:** 2026-11-18 Eastern. **Lane:** Gravity/Cone. **Status:** [D] exact inner future timelike quadratic level Q=1/4 carrying the EM transverse Jxy state moments; [D] same-angle fixed-row sections are null-direction translations of Q=0 with shift dependent on K; [D] exact reproduction of the nonconfocal focus from v15.1179/1181; [N] not one global rigid T-axis translation, physical spacetime mass shell or newly sourced gravitational response; [O] action-derived identification of an observable source/response. **Immediately prewrite live HEAD:** b955d79883c9a01036fc4165d0e9d52d7d78ebe9. v15.1182 unique/collision-free; additive-only, no Suzuki/Lane A, Audit, Sandbox, Muse or certified changes.

## Owner intuition and parent ledger
Owner suggests the Jxy transverse observability surface is a cone offset by 1/2²=1/4 along T from the null transition cone. This is closely supported geometrically, with an essential distinction. The archived EM operator identity at v15.955/1176 is `<Jx²+Jy²>=j(j+1)-m²`; its transition-circle coordinate is T=j+1/2 and its magnetic coordinate X=m. v15.1179 shows a translated nonconfocal Jxy row parabola; v15.1181 shows original acceleration parabolas and Jxy parabolas are all 45-degree cuts, respectively of Q=0 and Q=1/4, where Q=T²-X²-Y². The source-scale and physical Hilbert-space caveats remain. Current live HEAD after v15.1181, no collision. Independent Audit of this gate pending.

## Gate 1098 — two quadratic surfaces have the same T-axis
In representation-space coordinates T=j+1/2, X=m and Y²=<Jx²+Jy²>=j(j+1)-m²,
**Q=T²-X²-Y²=(j+1/2)²-j(j+1)=1/4**.
The transition edge amplitude locus lies instead on **Q=0**. The future positive-T level Q=1/4 is a **two-dimensional sheet of the two-sheet hyperboloid**, T=+sqrt(X²+Y²+1/4), with asymptotic null cone Q=0. At fixed T its circular radius is **R_Jxy=sqrt(T²−1/4)**, compared with **R_null=T**. The radial deficit is not constant: **T−sqrt(T²−1/4)=(1/4)/(T+sqrt(T²−1/4))**, tending to ~1/(8T). The geometry is nested inside the future cone and approaches it asymptotically; it is legitimate to call it the 'observability hyperboloid' or 'cone of observability' as project terminology, but it is not literally a second null cone. Only the sampled discrete Schwinger states lie on this continuous Q=1/4 surface.

A rigid T translation of the null cone by a constant a would give **(T−a)²−X²−Y²=0**, i.e. **Q=2aT−a²**, not constant 1/4 as T varies. A T-shift a(T) can be chosen on a fixed cross-section, but then it depends on T and does not give a single global translated cone.

## Gate 1099 — exact fixed-row null-direction displacement
Define light-cone coordinates **U=T−X** and **V=T+X**, so **Q=UV−Y²**. On the original row-parabola cut **U=K>0**, the two surfaces obey:
- Null edge geometry: **V_null=Y²/K**.
- Jxy level mu=1/4: **V_Jxy=(Y²+1/4)/K=V_null+1/(4K)**.

Therefore for each fixed K, the Jxy section is obtained from the null section at the **same Y and same U** through a *null-direction translation*
**ΔV=mu/K**, equivalently **ΔT=ΔX=mu/(2K)**.
For mu=1/4 this gives **ΔT=ΔX=1/(8K)**. The shift direction (ΔT,ΔX,ΔY)=(δ,δ,0) is null in the (T,X,Y) quadratic form. Since δ depends on K, this is NOT a single global isometry translation of the entire cone and NOT a rigid translation solely along T.

The fixed-row parabolic equation is then **Y²=K²+2KX−mu**, with vertex **Xv=−K/2+mu/(2K)** and focal parameter K/2, yielding its translated focus
**Xfocus=mu/(2K)**.
At the EM state-center index K=k+1/2 and mu=1/4 this is **Xfocus=1/[4(2k+1)]**, exactly v15.1179's offset. This gives a coordinate interpretation of that focus displacement: it is the X-component of the **fixed-U null shift** between two quadratic levels. The original 1/2 and 1/4 vertex acceleration parabolas both have mu=0 and focus X=0.

## Gate 1100 — what this does and does not select
The quadratic level mu=1/4 follows from **standard SU2 transverse Casimir completion**; no second genuine gravitational SU2 Casimir is needed. The geometry is a useful single ambient construction for the null J± *edge coefficients* and offset Jxy *state moments*, at a common null-cut angle but different Q level. Critically, edges and states belong to the same standard EM carrier; the section-by-section map is not a physical state transition or a universal new gravity connection. The continuous Q=mu ambient surface is representation-space geometry; it must NOT be read as the relativistic spacetime mass shell Q=m²c² or as a gravitational scale. On actual EM states D and k are discrete, the analytical parabola vertex is usually outside the physical state domain (v15.1179). The gravity quarter-grid may continue to organize a Casimir-free tidal/response geometry as suggested v15.1178; no action fixes a physical global EM↔gravity map from this identity.

## Reproducer, Audit and next
Executable additive source `research-notes/k4_observability_hyperboloid_null_shift_v15_1182.py`, commit **b955d79883c9a01036fc4165d0e9d52d7d78ebe9**, tested locally with exact SymPy identities for Q=UV−Y², fixed-U shift preserving the cut, Q-level conversion, focus, failure of constant T-axis translation, and EM j=0,1/2,1,3/2,2 sections; all PASS. **AUDIT HANDOFF:** verify direction/sign of ΔV for fixed Y and the distinction of translating surface *points* versus writing Y²(X); verify Q=1/4 sheet type, radial asymptotics and physical domain; no conflation with the gravitational quarter formal Casimir or Minkowski physical spacetime mass shell. **NEXT:** test whether an actually sourced Cone/elastic response can change the quadratic offset mu(T,X) independently of the standard SU2 identity, and whether it yields a nonzero dimensionless residual against matched GR+same-solid. If no action supplies such a term, keep this as a geometric correspondence.
