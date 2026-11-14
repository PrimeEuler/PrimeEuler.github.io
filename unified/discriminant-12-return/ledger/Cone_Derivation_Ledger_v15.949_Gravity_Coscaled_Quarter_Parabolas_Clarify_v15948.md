# Cone Derivation Ledger v15.949 — Quarter-grid parabola coordinates must co-scale with their vertex and remainder cell

**Date:** 2026-11-13 Eastern. **Status:** [D] exact scale-covariant correction to the interpretation of v15.948; [N] no independent physical gravity selector. **Parents:** v13.690 original parabola remainder formula, v14.767 audited unit-grid covariance, v15.947 original global T=D+A count, v15.948 correct but *different* fixed-coordinate quarter-remainder refinement. **Live HEAD immediately before commit:** f5865cbc9a2b0277976739d2ee68d1c94c16e03e. v15.949 target checked absent; additive-only, do not modify any earlier ledger or Suzuki objects.

## Gate 725 — user's distinction: scale the parabola rather than only the residue window

Original unit-u=1 parabolic secant **v_EM(k)=(n−k²)/(2k)** has vertices ±k/2 and residue cell 1/2. The quarter-vertex u=1/2 scale has **v_G(k)=(n−k²)/(4k)=v_EM(k)/2**, vertices ±k/4 and residue cell 1/4. Both coordinates and remainder cells must scale together, as required by the original normalization v14.767 and the actual u-grid pair (un/k,uk).

For real x and positive a, **(u x mod u a)=u(x mod a)** with Euclidean fractional modulo. Therefore the rowwise exact identity is

**4(v_G(k) mod 1/4)=2(v_EM(k) mod 1/2)={n/k}.**

Summing rows k=1..n gives precisely

**D(n)=nH_n−4 Σ_(k≤n)[(n−k²)/(4k) mod 1/4]**.

This retains the original global T(n)=n(n+1)/2 station count and D(n) hits at the **matched normalized product n**. On the physical u=1/2 grid the fixed normalized shell is **xy=u²n=n/4**, and the endpoint circle diameter is **u(n+1)=(n+1)/2**. Neither becomes an additional physical count merely by scale change. The invariant quotient recovers D(n), as already established in v14.767.

## Gate 726 — rigorous distinction from v15.948

v15.948 held the original EM coordinate v_EM(k) fixed and *only* changed the modulo cell to 1/4. This gives **B_quarter=2Σ(v_EM mod1/4)=1/2 Σ{2n/k}**, hence **D(2n)** via that separate arithmetic operation. The two operations are not equivalent:

- **Physical co-scaling:** v→v/2 and cell 1/2→1/4. Recover D(n).
- **Refined remainder on fixed EM geometry:** hold v and change cell 1/2→1/4. Recover D(2n) with known tail correction.

This explicit distinction corrects the suggestion that v15.948's D(2n) outcome necessarily describes the user-proposed gravitational quarter-grid. Its algebra remains correct on its own terms; its physical interpretation as co-scaled quarter-parabola was too broad. No earlier certified entry is modified.

## Verification and implications

**Exact reproducer:** `research-notes/k4_quarter_coscaled_parabola_divisor_correction_v15_949.py`, commit **f5865cbc9a2b0277976739d2ee68d1c94c16e03e**; locally tested 1000 positive integers using exact rational arithmetic, three uniform grid scales u=1,1/2,1/4, and the distinct unchanged-EM quarter-window construction. All checks PASS. **Independent Audit pending.**

**Verdict:** The user's formula **(n−k²)/(4k)** is the correct half-scaled secant for a quarter-vertex grid, and **co-scaled remainders return D(n)**. This makes the EM/G scale covariance fully explicit and rules out obtaining a new gravity-specific count through pure factor-grid dilation alone. A physically independent normalization, field equation, or interaction must distinguish the sectors if the geometry is to yield a new gravitational observable.

**HANDOFF Audit/Muse:** independently verify scaled Euclidean mod, D(n) at u=1/2, separate v15.948 D(2n) operation and physical product u²n, and note v15.948 is not mathematically refuted.
