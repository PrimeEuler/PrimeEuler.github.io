# Cone Derivation Ledger v15.574 — Lane A: AM–GM half-step bridge and exact offset-sector selector

Date 2026-11-09. Parents v13.583, v15.140, v15.180, v15.572–573; chiral no-go v15.388 and v15.520. Status [D] exact finite-dimensional identities; [C] candidate half-step normalization; [O] physical chirality/dynamics. Live prewrite HEAD 13b9cb2b75d8ef28cd7e0b8ce2b5b422305cffb0; no existing v15.574 collision found. Additive. Frozen Suzuki and far-tail untouched.

## Setup and offset grading [D]

On a refined shell j=N/4 (N nonnegative integer), use basis |i>, i=0,...,N, with m_i=-j+i/2. The original J_+ from AM–GM factors (j-m)(j+m+1) advances i by two. Define Gamma|i>=(-1)^i|i> and reflection R|i>=|N-i>. Exactly:

Gamma²=R²=I, [Gamma,J_±]=0, R Gamma R=(-1)^N Gamma.

For N odd (odd-quarter shells), mirror exchanges two equal-size offset classes; N even leaves classes individually invariant and the established closed/open structure of v15.140 applies. The offset grading is mathematically real, but not automatically Lorentz gamma5 or weak chirality, and mirror does not dynamically select either class.

## Candidate half-step AM–GM bridge [C/D]

For delta=1/2, define B_+|m> = sqrt((j-m)(j+m+delta)) |m+delta> on the refined shell, B_-=B_+†, with zero outside the shell. The half-step AM–GM factors have arithmetic mean j+delta/2=j+1/4, centered offset m+delta/2=m+1/4, and their product gives the squared transition amplitude. This is an explicit, natural candidate; the old ledger does not independently select its physical coupling or uniqueness. Its endpoints close at vanishing factors, and

{Gamma,B_±}=0, R B_+ R=B_-, [J_z,B_±]=±(1/2)B_±, [B_+,B_-]=J_z.

Rescale K_z=2J_z, K_±=2B_±. Then [K_z,K_±]=±K_± and [K_+,K_-]=2K_z: the *ordinary* spin K=2j=N/2 SU(2) representation of dimension N+1. Its Casimir is K(K+1)=2j(2j+1), rather than j(j+1). No new SU(2) Lie group arises; the quarter refined shell admits an ordinary closed SU(2) under a **different operator**.

## Original defective ladder is not the square of the half-step [D]

For m with original J_+ landing m+1 still on shell,

(B_+²)_{m+1,m} / (J_+)_{m+1,m}
= sqrt((j-m-1/2)(j+m+1/2)),

which is m-dependent at generic j. At j=3/4 it equals 1/sqrt(2) on two interior transitions (accidental constant); at j=5/4, the four ratios are (1,sqrt(6)/2,sqrt(6)/2,1). Hence one cannot replace original J_+ with B_+² or a universal scalar multiple while preserving the previously certified boundary defects D and E. Old J_± commute with Gamma, candidate half-step B_± anticommute, confirming the transition selection rule.

## Chirality assessment [D/O]

Gamma is a grading of **lattice offsets** and is equivalent to (-1)^(K_z+K) within the new spin-K irrep. On odd quarters, R Gamma R=-Gamma exactly; that is left/right-like parity exchange, not physical Lorentz chirality. A physical chiral selector would require a source-defined mapping of Gamma to spinor chirality and a dynamical coupling that treats the two sectors differently; known native frame chirality choice remains unresolved (v15.520). The bicone's Spin(4) factors cannot be identified with the weak internal SU(2)_L by dimension/name. No mass law, coupling, G, or Suzuki operator identification.

Verification: exact SymPy matrices and mirrors checked N=1,2,3,4,5,6,7,9; script/reproducer available in Lane A response artifact 'cone_amgm_offset_selector_gates_40_41.zip'.

**HANDOFF** target external-audit; type AM–GM half-step/offset selector; status open; action independently verify Gamma commutators and reflection for N odd/even, half-step SU(2) normalization and Casimir, J_+ vs B_+² ratios; examine whether the half-step weights are uniquely intrinsic or merely a natural added operator. No production/far-tail writes.
