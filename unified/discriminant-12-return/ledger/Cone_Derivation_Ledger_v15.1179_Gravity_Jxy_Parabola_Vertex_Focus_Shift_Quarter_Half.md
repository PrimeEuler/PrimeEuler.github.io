# Cone Derivation Ledger v15.1179 — Jxy transverse observable traces a shifted, nonconfocal parabola between half/quarter acceleration vertices

**Date:** 2026-11-18 Eastern. **Gravity/Cone lane. Status:** [D] exact parabolic locus of the fixed-state-row Jxy transverse observable in legacy parabola X,Y coordinates when the common null-circle diameter D varies; [D] analytic vertex and focus displacement relative to original ±1/2 and interleaved ±1/4 confocal acceleration parabola families; [D] exact harmonic-mean formula and physical-domain restriction; [N] no third physical field, new quantum state, source law, additional gravitational Casimir or fixed G-free coupling follows from the translated locus; [O] physically motivated way a dynamical response might sample a distinct focus, if any, rather than purely translating a representation. **Immediately pre-ledger live HEAD:** ce4d581377d86f5cd1f09248129af1e55abd0cf5. Target v15.1179 unused, additive-only; protect Suzuki/Lane A, Audit, Sandbox, Muse and audited historical files.

## Prior ledger, user subtlety and coordinate conventions
Owner asks to trace **the Jxy Casimir-related observable itself as a parabola** and compare its vertex offsets to the two source acceleration families with vertices ±1/2 (integer EM fixed-factor rows) and ±1/4 (half-integer rows of the q=2 interlay). This is related to but **distinct from** the already verified v15.932 midpoint squared-height surplus and v15.955/v15.1176 EM Jxy transverse operator state-center identity. The old v15.924 exact family is P_r: Y²=r²+2rX, *all rows confocal at X_focus=0* (with horizontal right-opening parabola Y²=4p(X−Xv), p=r/2, Xv=−r/2). Integer r=k produces original EM row vertices Xv=−k/2; half-integer K=k+1/2 produces quarter-grid interlay vertices Xv=−k/2−1/4. The mirror half uses X→−X and symmetric positive vertices. Circle diameter D=n+1 is the Schwinger state-shell parameter; rotating a diagram does not turn a coefficient plot into an independent field.

## Gate 1092 — third locus at fixed k varying D: exact Jxy squared-height parabola
Fix the EM magnetic-state index k≥0 and vary the containing integer diameter D≥k+1. Put K=k+1/2, X_mid=D/2−K and f_D(K)=K(D−K). From the exact transverse EM observable v15.955,
**<k|Jx²+Jy²|k>=f_D(K)−1/4**.
Eliminate D via D=2(X+K) to obtain the whole analytic locus
**Y²_{Jxy}=K²+2KX−1/4 = (2k+1)X+k(k+1)**.
Thus it is an ordinary translated *right-opening parabola* (in the X,Y plane), with **exactly the same coefficient 2K=2k+1** as the quarter-interlay P_K but the squared ordinate decreased by 1/4 **at fixed X**. Equivalently, **Y²_Jxy=[P_k(X)+P_{k+1}(X)]/2−1/2**. This fixed-X comparison must not be confused with the pre-existing fixed-D midpoint identity **f_D(K)=[f_D(k)+f_D(k+1)]/2+1/4**, which samples the two EM edges at **different X** on the same circle. Both identities hold; the midpoint Jxy squared value is the arithmetic mean of the two *circle-intersection* edge squares, while at the same X the Jxy squared row is the *average of two row parabolas minus 1/2*. The apparent 1/4 versus 1/2 is no contradiction: different slices.

## Gate 1093 — exact three-vertex comparison and nonconfocal Jxy focus
The original rows bracketing K have Xv,EM,left=−k/2 and Xv,EM,right=−(k+1)/2. The interleaved **quarter-grid** parabola P_K has Xv,quarter=−K/2=−(2k+1)/4, exactly centered between those two original vertices. But setting Y²_Jxy=0 gives the **translated transverse observable parabola's vertex**
**Xv,Jxy=−K/2+1/(8K)=−k(k+1)/(2k+1)**,
hence
**Xv,Jxy−Xv,quarter=+1/[4(2k+1)]**.
Its signed differences from the two EM vertices are
**Xv,Jxy−(−k/2)=−k/[2(2k+1)]**,
**Xv,Jxy−(−(k+1)/2)=+(k+1)/[2(2k+1)]**.
Therefore for k≥1 the Jxy vertex lies **strictly between** the left-hand (less-negative) EM row vertex and the quarter-grid interleaved vertex, rather than coinciding with either; at k=0 it coincides with degenerate original P_0 vertex X=0. A neat exact reinterpretation is
**Xv,Jxy=−[H(k,k+1)]/2**, where H=2k(k+1)/(2k+1) is the *harmonic mean of adjacent factors* (for k>0, and formally 0 at k=0).

Because the parabola coefficient is unchanged, its focal parameter remains p=K/2. Thus its geometric focus is
**Xfocus,Jxy=Xv,Jxy+p=1/(8K)=1/[4(2k+1)]**,
whereas both original integer EM and quarter-interleaved acceleration families retain **Xfocus=0**. The transverse Jxy locus is therefore **not confocal** with the two original fixed-factor acceleration families, although it is a mere rightward translation of P_K. This is a new and precise way to describe the existing quarter-midpoint identity; it is not evidence a physical lens/force field has changed its focus.

Examples (legacy X axis, leftward negative orientation):
k=0: original EM vertex 0, Jxy 0, interlay quarter −1/4, next EM −1/2;
k=1: EM −1/2, Jxy −2/3, quarter −3/4, next EM −1;
k=2: EM −1, Jxy −6/5, quarter −5/4, next EM −3/2;
k=3: EM −3/2, Jxy −12/7, quarter −7/4, next EM −2.
As k increases the focus shift 1/[4(2k+1)] decays toward zero. A physical scale u rescales *all* X coordinates/focal distances by u and *all* squared-Y ordinates by u²; neither the 1/4 numerical vertical squared shift nor the focus displacement is an SI length without a supplied u.

## Gate 1094 — the extrapolated vertex is generally outside actual Schwinger state domain
This is an **essential restriction**. At fixed k the full Schwinger state |D−1−k,k> is available only for D≥k+1 (with integer D). Thus the smallest actual circle-intersection state-center coordinate is **Xmin,physical=(k+1)/2−(k+1/2)=−k/2** and its physical Jxy² is **k/2**. For k≥1, the translated parabola's zero-height vertex is at **−k(k+1)/(2k+1)<−k/2**, *outside the sampled physical domain*. Only k=0 reaches Xv,Jxy=0 at the actual spin-0 D=1 state. Thus the Jxy parabola and its focus are legitimate **analytic continuations of the state moment across D**, not additional measured zero-transition points or new foci visited by a physical oscillator. Identifying them as sources, charges, or gravitational acceleration centers would require a separate physical model.

## Reproducer, Audit and next discriminant
Canonical additive Python/SymPy source `research-notes/k4_Jxy_three_vertex_parabolas_v15_1179.py`, SHA **ce4d581377d86f5cd1f09248129af1e55abd0cf5**. Source algebra locally executed successfully: exact Jxy row equation, Xv, focus, harmonic mean, EM/quarter relative offsets, both fixed-X and fixed-D averaging identities, D≥k+1 lowest boundary, k=0..8 vertex order. **AUDIT HANDOFF:** independently verify both coordinate-slicing conventions, 1/4 vertical squared shift versus +1/[4(2k+1)] horizontal focal/vertex displacement, relation to harmonic mean, right-opening focus p=K/2 and actual state domain caveat, scale u factors and no new gravitational Casimir/source claim. **NEXT:** ask whether this translated Jxy curve corresponds to a *physically selected* dynamic susceptibility or merely an equivalent EM operator representation; map the zero-height vertex to actual field geometry only if the acceleration field equations source such a focal shift. Under frozen Einstein–Hilbert+same-solid no such quarter-specific physical focus has yet been derived. Preserve the owner's possible Casimir-free quarter gravitational-grid hypothesis.
