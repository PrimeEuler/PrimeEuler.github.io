# Cone Derivation Ledger v15.1053 — Confocal unit-parabola secant compactification and exact T-cone / X-cone circle-coordinate transport

**Date:** 2026-11-16 Eastern. **Gravity / Cone lane.** **Owner intuition:** diameter divided in half-steps supplies vertices of a family of confocal square-root parabolas. A parallel displaced secant intersects those parabolas at signed v_k=(n−k²)/(2k). On the n+1 diameter circle the original rungs are spaced in steps of one rather than half. Is there an exact map from a secant to a circle on the other signed cone, replacing a forced sign-reflection picture with a geometric translation? **Status:** [D] projective secant-to-circle compactification, exact same coordinates on both cones and Pell Möbius action; [D] sample-label preservation but failure of equal spacing under the compactification; [N] no rigid rotation, time-independent physical sector-changing Hamiltonian, or new gravitational kinetic law; [O] action/phase and quarter-boundary physical operator matching.

**Ledger redundancy / process:** v13.691 §6–7 already established the secant divisor identity v_k=(n−k²)/(2k)=−X_k and real hyperbolic-to-circle map normalized by T; v13.179 derived discriminant-12 Pell boost as rapidity shift and proved it moves continuous unit-row/parabola foliation but not integer-labeled row; v15.008 Sandbox AM–GM diameter multi-step ladder and its chord heights, which depend on cumulative pairs, not on arbitrary secant projective images; v15.235 proved both opposite-opening parabola families are confocal at the apex, with each lattice intersection a row/column pair; v15.595 tied the differences of neighboring square heights to ladder/current responses and kept its force interpretation conditional; v15.1042 Sandbox signed T/X cones; v15.1050 V4 sqrt(1,5,7,11) unit-parabola mirror; v15.1052 smooth null hinge and rank-two open-boundary T obstruction. External Audit Round 587/v15.1051 independently checked v15.1049–1050. **Immediately before this ledger write live HEAD** 8c59a04c72b4e137503438cee9c97e75dd5bb459 (canonical script); path verified absent, additive only, no existing Audit/Sandbox/Muse/Suzuki/certified content modified.

## Gate 853 — reconstruct the secant family with original half-step labels

Let u=k>0, v=n/k>0, n>0. The Paper-A cone coordinates are **T=(u+v)/2=(k²+n)/(2k), X=(u−v)/2=(k²−n)/(2k), Y=sqrt(uv)=sqrt n**. Fixed n means Y=sqrt n, a secant/height slice. Each fixed k corresponds to the confocal original-unit parabola **Y²=k(2T−k)** in (T,Y), or **Y²=k(k−2X)** in (X,Y) for the appropriate row orientation. Its vertex in (X,Y) is X=k/2 for the displayed Y²=k(k−2X); the mirror column family has opposite vertex, and both have focus (0,0). The old divisor secant coordinate **v_k=(n−k²)/(2k)=−X** is exactly v13.691, not a newly introduced function. Choosing k on an integer, half-integer, or quarter-refined mesh gives a family of intersection labels; the continuous formulas hold at every positive real k.

## Gate 854 — radial circle compactification transports secant intersections from one cone onto fixed-radius action-circle slices

For any chosen A>0, project the cone point (T,X,Y) to the T-cone circle T=A by scaling all three cone coordinates by A/T. Its planar circle coordinates are

**x_A=A X/T=A(k²−n)/(k²+n)**,
**y_A=A Y/T=2A k sqrt n/(k²+n)**,

and exactly **x_A²+y_A²=A²**. This is the rational stereographic compactification of the parameter q=k/sqrt n>0, with x_A/A=(q²−1)/(q²+1), y_A/A=2q/(q²+1). One may express its angular coordinate with tan(θ/2)=sqrt(n)/k (θ∈(0,π) measured from the +x radius), up to orientation conventions.

Now apply the discrete signed-pair reflection **(u,v)→(u,−v)**. The resulting X-cone has **(T_X,X_X,R_X)=(X,T,Y)** and **X_X²−T_X²=R_X²=n**. Project it radially to the X-cone constant-axis slice **X_X=A**: its transverse circle coordinates are

**(A T_X/X_X, A R_X/X_X)=(x_A,y_A)**.

Thus both cones have EXACTLY THE SAME normalized secant-circle coordinates for a given positive k,n,A, with the longitudinal-axis label exchanged. This geometric correspondence uses the discrete sign reflection, not a dynamical path through the null hinge; it does not circumvent the rank-two vs full-rank obstruction of v15.1052. It is, however, an explicit *projective transport dictionary* between cone circle sections, not merely a numerical coincidence.

## Gate 855 — distinguish labeled half-step spacing from actual equal circle spacing and the n+1 chord ladder

The projective circle coordinate is nonlinear in k. Derivatives:

**dx_A/dk=4A n k/(k²+n)²**, **dy_A/dk=2A sqrt(n)(n−k²)/(k²+n)²**.

Equally spaced k labels therefore DO NOT map to equal circle angles or equal horizontal chord-foot positions; θ'(k)=−2sqrt n/(k²+n). The original diameter m=n+1 *cumulative pair ladder* of v15.008, in contrast, has actual fixed-circle chord foot abscissae **x_j=j−(n+1)/2**, j=1,..,n (step one), and chord heights **y_j=sqrt[j(n+1−j)]**, satisfying x_j²+y_j²=[(n+1)/2]². Treating those as the same sampled k-grid is generally false.

Explicit counterexample n=11, A=(11+1)/2=6: for k=1 the compactified secant gives (x,y)=(−5,sqrt11), agreeing with the j=1 diameter-12 ladder endpoint; k=11 gives (+5,sqrt11) agreeing with j=11. However for k=2 the secant compactification gives **x_A=−14/5=−2.8**, while the j=2 diameter-ladder foot is **x_j=−4**. The height values differ correspondingly. The projective transport therefore preserves secant *labels and order*, not the equally spaced diameter ladder's actual Euclidean coordinates. This scope distinction is essential when extending to EM half-grid or gravity quarter-grid sampling.

## Gate 856 — Pell return becomes an exact Möbius action on each circle; neither a rigid translation nor sector crossing

Under the real discriminant-12 boost, **u→λu, v→λ^−1v**, λ=2+sqrt3>0. For fixed n, this is k→λk, and the log parameter **s=log(k/sqrt n)** shifts **s→s+logλ** (v13.179). In the normalized circle variable **q_c=x_A/A=(k²−n)/(k²+n)**, Pell acts by the exact fractional-linear map

**q_c'=[λ²(1+q_c)−(1−q_c)]/[λ²(1+q_c)+(1−q_c)].**

This is the circle compactification's conjugate of a *rapidity translation*, not a rigid Euclidean circle rotation. Under the same boost the signed X-cone construction acts with the identical q_c update: the same projective dictionary commutes with the boost on the two continuous circle sections. But λ is irrational and the k-step mesh generally does not map into itself. Also positive reciprocal rescaling preserves sign uv; the map cannot independently produce physical T→X transition.

For n>0, every finite k>0 has y_A>0; the null hinge y_A=0 occurs only at k→0 or k→∞. In this projective picture those are boundary limits, and merely identifying those circle endpoints with a physical change of Cone sector would be incorrect.

## Gate 857 — strong positive geometric result / physical open gate

**Exact test script:** `research-notes/k4_secant_circle_T_X_cone_mobius_v15_1053.py`, additive commit **8c59a04c72b4e137503438cee9c97e75dd5bb459**. Executed an equivalent Python/SymPy local script: exact circle identity and reflection transport, exact Pell Möbius map, n=11 diameter-12 counterexample and hinge limits; all PASS. External independent Audit pending.

**Positive:** one confocal-parabola secant family carries a canonical projective circle coordinate on both T and X cone sheets. The same k/sqrt n and signed parabola intersections yield a single shared parameter; Pell scaling becomes a Möbius action in this parameter. This is a precise mathematical bridge between continuous cone foliations and circle sections, with the mirror symmetry v13.691 and signed-X completion v15.1042.

**Negative:** projective transport is not Euclidean translation, equal-arc sampling, an identification of the n+1 integer diameter ladder with the n-shell k-step sample, a physical action circle frequency, or an inter-sector Hilbert operator. It does not derive the missing physical rank-two boundary projector, its amplitude sqrt[(L+1)/4], or a GR-distinguishable G-free observable.

**NEXT / HANDOFF Audit, Muse, Sandbox:** independently verify the orientation of row/column parabola formulas and their focus at the apex, the exact stereographic map, n=11 k=2 mismatch, Pell fractional-linear conjugacy, and the commutative T/X signed reflection. To test whether the user's 'translation' idea can go beyond a geometric dictionary, seek an action-preserving symplectic lift on physically specified canonical secant variables and independently calculate its boundary projector matrix elements against open q2 T†T=2E. Do not infer physical acceleration from the shape of a parabola without a time law or active source.
