# Cone Derivation Ledger v15.927 — Null quarter-rung shifts: magnetic charges and exact ladder-intertwiner obstruction

**Date:** 2026-11-13 US Eastern. **Gravity lane.** Parents v15.140/v15.180, v15.572–574 and v15.602/v15.627, Gravity v15.922–926. **Live HEAD immediately prewrite:** e1cac8f4e1c2b3726daeb7a96d248258a93b9bee. Ledger target absent; add-only. No modifications to historical, Suzuki, Audit, Sandbox or certified objects.

**Target:** Determine whether the two already identified product-changing null quarter-rung injections can serve as *exact ladder intertwiners* between the original defective step-one AM–GM representations of neighboring shells. Differentiate a charged tensor-like operator from a strict representation intertwiner; neither is automatically a physical electromagnetic dipole or gravitational coupling.

**Status:** [D] exact magnetic-charge commutators and exact obstruction, [N] exact finite SymPy shell test L=1..40, [O] physical action and a justified position-dependent/charged cross-shell operator.

## Gate 664 — two rectangular geometric injections

Original q=2 refined shells H_L have states |L,i>, i=0,...,L; j=L/4; m_i=−j+i/2. The *original* (not alternative B) raising operator J_{+,L} sends i→i+2 with coefficient sqrt[(j−m_i)(j+m_i+1)] for i+2≤L. The magnetic coordinate is M_L=diag(m_i).

Define two simple isometric injections from H_L into H_{L+1}:

**A_L |L,i>=|L+1,i>**, and **B_L |L,i>=|L+1,i+1>**.

Both are rectangular (L+2)×(L+1), and satisfy **A†A=B†B=I**; their overlap A†B is generally nonzero, so their superposition is **not** automatically an isometry. Their adjoints define legitimate reverse maps, and on the direct sum of neighboring shells the off-diagonal Hamiltonian blocks H_U = g U + g* U† are Hermitian **for supplied coefficient g**. This establishes mathematical adjoint-compatibility, but not a physical Hamiltonian.

They move m by ±1/4 exactly:

**M_{L+1}A_L−A_L M_L=−A_L/4**,
**M_{L+1}B_L−B_L M_L=+B_L/4**.

Thus neither is an *M-preserving* intertwiner; each is instead a geometrically charged operator. Both flip the formal q=2 shell grading χ=(-1)^L as in v15.627, and preserve the null metric relation (ΔR)²−(ΔX)²=0 of v15.926. These are necessary geometric compatibilities, not sufficient E1 or gravity selection rules.

## Gate 665 — direct original J+ intertwining test

A strict spin-ladder intertwiner would additionally require **J_{+,L+1}U_L=U_L J_{+,L}**. Define residuals

**F_A=J_{+,L+1}A_L−A_LJ_{+,L}**,
**F_B=J_{+,L+1}B_L−B_LJ_{+,L}**.

Both are generically nonzero. The supports are disjoint: F_A has entries only at target index (i+2, source i), while F_B has entries only at target index (i+3, source i). Consequently no nonzero *state-independent* combination U=c_A A+c_B B can make F_U=0 for L≥2: each residual must independently vanish, and both are nonzero. At L=1, the degenerate B raising-commutator vanishes because the source shell J_+ is identically zero and B maps into destination indices not connected by the destination's step-two ladder; that does **not** make B a magnetic-coordinate-preserving intertwiner or a derived physical operator.

A sharp source of nonzero F_A is the source i=L−1, which has no retained outward step-two edge in H_L but does acquire a step to endpoint i=L+1 in H_{L+1}. This is exactly the old missing-edge obstruction, now expressed as a failure of naturality of the one-rung shift. F_B has an independent nonzero interior comparison for L≥2, e.g. matrix element (row3,col0). These nonzero diagonals cannot interfere destructively with constant coefficients.

A more general position-dependent map `U=∑_i (a_i |L+1,i><L,i|+b_i |L+1,i+1><L,i|)` has extra parameters and may satisfy some partial charged tensor relations; this gate has **not** proved an impossibility for every such U. Exact SU(2) covariant tensor operators need not commute with J_+ at all, so failing strict intertwining is not itself a no-go for physical E1 operators. One must derive the tensor relation, normalization, principal shell correspondence, and conserved charges independently.

## Gate 666 — physical verdict and next test

**Positive:** Both quarter-null injections possess exact ±1/4 magnetic shifts, definite χ-flipping behavior, admissible adjoints, and the same AM–GM parabola geometry. The boundary defect physically motivates seeking a nontrivial charged cross-shell operator, rather than an unweighted shift.

**Negative:** Neither unweighted A nor B, nor any state-independent mixture, is an exact intertwiner of the original defective step-one J algebra for L≥2. Geometric nullness, product change and χ flip therefore do not supply a physical E1 transition rate, coherent EM↔gravity pump, or selected interaction.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_quarter_null_shift_intertwiner_v15_927.py`, additive commit e1cac8f4e1c2b3726daeb7a96d248258a93b9bee. Exact SymPy matrices across L=1..40, including L=1 exception, charge commutators, supports of residuals, isometry of individual injections and grading; independent Audit pending.

**Next gate:** formulate a *specified charged tensor covariance* (e.g., the exact [J+,U] relation required for a rank-one operator, rather than forcing commutation) and solve its site-dependent coefficients with explicit q=2 boundary conditions. Check whether any solution is fixed up to one global constant and whether it can reproduce a genuine **SO(4,2)** hydrogen cross-principal-shell E1 operator without importing the physical matrix elements by fitting. If not, document the mismatch and keep radiation/physical gravity claims out of the quarter lattice.
