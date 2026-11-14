# Cone Derivation Ledger v15.943 — Hyperbola-interleaved quarter Casimir offsets reconstruct the global n+1 endpoint diameter

**Date:** 2026-11-13 Eastern. **Lane:** Gravity; exact AM–GM factor geometry. **Question:** Does the relative offset of the EM 1/2-vertex and quarter 1/4-vertex parabolas along the SAME hyperbola, with row intersection X=(n−k²)/(2k), encode the global n+1 diameter and mediate the distinct quarter-shell Casimir offsets?

**Prewrite HEAD:** f4651c8be8d9ae29ec64893db80670bfe962d358 (standalone reproducer). Target v15.943 checked absent. Additive-only. Latest independent Audit available is Round 575 v15.939, which confirmed Gravity v15.930–938; v15.940–942 remain unaudited. Parent/collision review: v15.932 already proves **fixed-diameter** midpoint GM² surplus +1/4 and interleaved vertices; v14.767 already proves normalized u-grid diameter and power transport; v15.625 the all-q Casimir classes; v15.942 the absence of a physical Taub–NUT Casimir identification; `Gravity_Shifted_Divisor_Hyperbola_Seats.md` already defines a DIFFERENT shifted divisor lattice. The **new gate** is the hyperbola X-coordinate midpoint curvature, n reconstruction and precise distinction between fixed-xy and fixed-(x+y) slices.

**Status:** [D] exact elementary identities and finite-row verification; [R] geometric refinement/circle structure previously known; [C] proposed Casimir *geometric midpoint* bridge, not an operator intertwiner; [O] physical quarter-grid selector, gravitational source/coupling or new measured response.

## Gate 714 — retain user's exact row-intersection X=(n−k²)/(2k)

Take factor pair (a,b)=(n/k,k), so product **ab=n** and, as in the legacy diameter/secant representation,

**X_n(k)=(a−b)/2=(n−k²)/(2k)**,
**Y_n(k)=sqrt(ab)=sqrt(n)**,
**R_n(k)=(a+b)/2=(n+k²)/(2k)**.

Then **R_n(k)²−X_n(k)²=n** for every real k>0, and mirror/inversion sends k→n/k, changing X to −X and preserving R. The fixed-product hyperbola Y²=n intersects acceleration/deceleration mirror parabolas **P_k^±: Y²=k²±2kX** at ±X_n(k). Integer factor rows k=1,2,... carry half-integer vertex offsets X_v=∓k/2; half-integer k+1/2 rows have exactly interleaved quarter offsets ∓k/2∓1/4.

Careful **global diameter** statement: the diameter associated to a general hyperbola factor pair is **D_n(k)=a+b=n/k+k**, not identically n+1. However

**D_n(k)−(n+1)=(k−1)(k−n)/k**,

so the original *n+1* diameter is reached exactly at the distinguished factor-pair endpoints k=1 or k=n (for n≥1), i.e. the pair (n,1) and mirror. This is the same n+1 singled out in the existing fixed-diameter transition circle, but one must not claim that every point of the product hyperbola lies on that same circle. For k>0 non-endpoint rows usually have different D_n(k).

## Gate 715 — fixed-product EM/quarter interleave encodes n by a local nonlinear offset

Compare neighboring **EM rows** k,k+1 with their quarter-vertex **interlay row** k+1/2 at fixed product n. Define **ΔX_n(k)=X_n(k+1/2)−[X_n(k)+X_n(k+1)]/2**. Direct exact simplification yields

**ΔX_n(k)=−n/[4k(k+1)(2k+1)]**.

Even though the underlying *vertex positions* are exactly equally spaced (zero vertex midpoint defect), the *hyperbola intersection X positions* have nonzero curvature due to the reciprocal n/k factor. Rearrangement recovers the same global dimensionless product, and hence the original endpoint n+1 diameter, from every local midpoint comparison:

**n=−4k(k+1)(2k+1) ΔX_n(k)**,
**n+1=1−4k(k+1)(2k+1) ΔX_n(k)**.

The radius R_n(k) has **the same** interpolation defect as X_n(k), since R_n(k)−X_n(k)=k is affine in k. For grid scale u, physical offsets scale to uΔX; the dimensionless reconstruction must divide by u and so does not independently select the physical EM/gravity scale. In particular this is a recovery of the already present global input n from local, *normalized* geometry, not a field-generated prediction or a new independent invariant.

Example n=12: k=1 has X(1)=11/2, X(3/2)=13/4, X(2)=2, midpoint defect −1/2 and reconstructed n+1=13. At k=2, X(2)=2, X(5/2)=23/20, X(3)=1/2, midpoint defect −1/10 and reconstructed **the same 13**. This is exact and works for any real k>0 for which those rows are defined, not only positive-integer divisors of n; half-integer row intersections do not automatically correspond to integer divisor contacts.

## Gate 716 — the separate formal Casimir midpoint defect and an exact scale factor

Compare the **original-unit-step geometric shell function** C(j)=j(j+1) at neighboring EM half-step spins j and j+1/2 with the odd-quarter geometric midpoint j+1/4:

**ΔC(j)=C(j+1/4)−[C(j)+C(j+1/2)]/2=−1/16**.

This holds for every j, and for j=k/2 specifically compares even shell labels L=2k,2k+2 with odd-quarter L=2k+1 in the *formal* q2 shell tower. It is not the **physical** monopole/EM angular Casimir on an independent gravitational carrier; it is a discrete second-difference of the common polynomial C(j) sampled on disjoint shell classes. The two geometric midpoint offsets obey the exact algebraic link

**ΔX_n(k)=[4n/(k(k+1)(2k+1))] ΔC.**

Thus the fixed n product and the row-dependent reciprocal hyperbola geometry amplify the universal Casimir-polynomial midpoint defect. This is an exact **scalar-geometry** relation, not an operator equality, intertwiner, energy shift or new spin/graviton spectrum. In particular the odd-quarter C(j) values remain spectrally different from EM, as v15.625/630 prove.

## Gate 717 — distinguish the two kinds of global slice: n fixed vs D=n+1 fixed

Previous **v15.932** holds the diameter **D=n+1** fixed, and sweeps factor rows k through the circle with **Y_D(k)²=k(D−k)**. There the quarter interlay gives

**Y_D(k+1/2)²−[Y_D(k)²+Y_D(k+1)²]/2=+1/4**.

But on the fixed-product **hyperbola** in the present gate, Y²=n is identically constant at every row, and D(k)=k+n/k varies. Thus the +1/4 from v15.932 and the present −n/[4k(k+1)(2k+1)] are **different comparisons in different slices**, and neither may be subtracted as though the same quantity. The fixed-D circle and fixed-n hyperbola intersect at the normalized factor pair (n,1) and its reversal (and at n=1 the two coincide). This distinction prevents a false universal quarter-vs-half Casimir interaction.

## Verification / operational burden

**Reproducer:** `research-notes/k4_hyperbola_interleaved_casimir_global_nplus1_v15_943.py`, additive commit **f4651c8be8d9ae29ec64893db80670bfe962d358**. Executed locally with SymPy PASS: symbolic row-intersection/circle/inversion identities, ΔX/ΔR, all-row n+1 recovery, formal C(j) midpoint −1/16 and exact ΔX/ΔC coefficient, physical scale u normalization, fixed-D +1/4 contrast, and **5,049 exact integer-row checks** n=2..100, k=1..n.

**Verdict:** **Positive:** the interleaved quarter-vertex parabola intersections *along the hyperbola* do encode the global n+1 endpoint diameter through their k-dependent curvature, without inserting measured G or fitting coefficients. The algebraic bridge to quarter **geometric Casimir interpolation** is exact. **Negative/open:** the recovered n+1 is mathematically determined by the original hyperbola parameter n; it is not a newly independent global count, a distinct gravitational physical Casimir, an EM↔G transition operator, or a generated action scale. The quarter row refinement and relative reference scale remain unselected by physical dynamics.

**Next discriminating gate:** Put the same two cosets on a genuine finite divisor-contact (integer factor lattice) hyperbola, distinguish exact contacts from continuously intersecting rational half rows, and compute whether a parity-weighted **global** sum of the normalized local interleave offsets has a nontrivial, arithmetic divisor count after proper boundary treatment. Compare with the earlier Hurwitz/shifted-seat divisor results and any physical source selector. Do not infer graviton, G or spin-two dynamics from midpoint identity alone.

**HANDOFF Audit/Muse:** verify the product-versus-diameter distinction, coefficient in ΔX, normalization by u, formal quarter Casimir −1/16 and exact scaling link, and scope of any claimed n+1 global encoding.
