# Cone Derivation Ledger v15.928 — Nonconstant quarter-rung raising covariance from AM–GM factor weights

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM physical operator gates. **Parents:** v15.140, v15.180, v15.572–574, v15.602/627 and recent Gravity v15.921–927. **Live HEAD immediately before ledger write:** 7da335f24668eeb1caaa5a60528d82cef05db915. Target ledger path checked absent; strictly additive, preserves Audit, Sandbox, Suzuki and certified work. External Audit pending.

**Question:** Can the previous v15.927 failure of constant quarter-rung injections be repaired by site-dependent AM–GM weights, and do those repaired maps become full representation intertwiners or actual electromagnetic dipole operators?

**Status:** [D] exact recurrences and complete solution dimensions in the two restricted injection families; [N] exact SymPy sweeps; [N] no full raising/lowering intertwiner on those support families for L≥2; [O] tensor covariance, energy/radial/KS scaling, physical field coupling.

## Gate 667 — geometry-derived recurrences

Use the old **defective** q=2 step-one ladder on H_L (dim L+1), not the alternative closed half-step representation. States |L,i>, i=0..L, have j=L/4, m_i=−L/4+i/2, and J_{+,L}|L,i> = w_i(L)|L,i+2> for i+2≤L, with `w_i(L)=sqrt((L−i)(i+2))/2`.

Define weighted null injections to the next shell L'=L+1:

**U_A|L,i> = a_i |L+1,i>** and **U_B|L,i> = b_i |L+1,i+1>**.

They preserve the geometric null-step constraint ΔR=1/4 and ΔX=∓1/4 for nonzero matrix elements; the exact charged magnetic relations are `M_{L+1}U_A−U_AM_L=−U_A/4` and `M_{L+1}U_B−U_BM_L=+U_B/4`, including arbitrary site-dependent weights. Both flip χ=(-1)^L.

Impose **raising covariance/intertwining only**, `J_{+,L+1}U=U J_{+,L}`. For i≤L−2 the coefficient recurrences follow exactly:

**a_{i+2}/a_i = sqrt[(L+1−i)/(L−i)]**,

**b_{i+2}/b_i = sqrt[(i+3)/(i+2)]**.

All coefficient ratios are fixed from the pre-existing AM–GM ladder factors. This is constructive progress beyond the *constant-weight* test, but neither a new geometric transition law nor a source of dimensional frequency.

## Gate 668 — boundaries reduce the solution space

On the A shift, the destination operator has a final extra raising edge at source i=L−1 to destination row i=L+1, while the source raising operator has no such edge. Therefore **a_{L−1}=0**, and the same-parity recurrence forces that whole coefficient chain to vanish. Only the opposite parity chain survives: **one independent A-family amplitude parameter** for every L≥2.

On the B shift there is no extra upper boundary equation of that kind; the recursion independently propagates the two mod-2 residue classes, leaving **two independent B-family amplitude parameters** for every L≥2. The two families carry different ±1/4 magnetic charges, and their source→target matrix supports occupy different diagonals. The space of maps with this strictly two-diagonal support and raising covariance therefore has dimension **3**, not a uniquely selected single physical operator. No independent physical selection of the three relative scales/phases is provided by geometry.

For L=3 (j=3/4), a convenient nonzero A solution has coefficients **(a_0,a_1,a_2,a_3)=(0,sqrt6/3,0,1)**. The two B solutions can be normalized as **(sqrt6/3,0,1,0)** and **(0,sqrt3/2,0,1)**, respectively. All satisfy the raising equation exactly.

## Gate 669 — full two-sided intertwining still fails

Requiring **both** `J_{+,L+1}U=UJ_{+,L}` and `J_{-,L+1}U=UJ_{-,L}` in either A or B support family gives only zero for L≥2. This is verified by independently solving the complete exact linear systems for L=2..10, not only checking a particular chosen weight. For L=1 isolated fragments furnish degenerate exceptions and must not be generalized. Moreover, each weighted map still has a nonzero magnetic charge ±1/4, so it is **not** an M-preserving representation intertwiner.

This distinguishes three notions: (i) parity-changing **geometric null shift**, (ii) a nonconstant shift **covariant with raising only** (positive construction), and (iii) full *defective* step-one ladder intertwiner (negative in these support classes). Physical spherical tensor operators generically need not commute with J_+ or J_-: they obey specified, multi-component tensor commutation relations. Such relations have not been derived here. Formal fractional magnetic charge ±1/4 on a quarter-refined non-SU2 module should not be silently identified with the integer-q components of a conventional electric dipole (SO(3) rank one).

## Gate 670 — reproducibility and physical gate

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_weighted_quarter_rung_raising_covariance_v15_928.py`, commit **7da335f24668eeb1caaa5a60528d82cef05db915**. Independently executed under SymPy in the current container: PASS L=2..40 for explicit nonzero A and both B solutions, exact raising and magnetic-charge commutators and nonzero lowering residuals; PASS L=2..10 for complete exact linear-system nullspace dimensions (A=1, B=2, jointly raising+lowering=0). The proof is the explicit two-step recurrence, upper boundary condition on A, and independent parity residue classes.

**Verdict:** Site-dependent weights *do* repair the v15.927 constant-weight failure of raising covariance, and the AM–GM parabola formula supplies those weights exactly. But the solution is non-unique, is not a full representation intertwiner and is not a physical E1/EM–gravity transition. This is not an experimentally novel decay-rate prediction.

**NEXT:** Derive explicit commutators of these three basis solutions with the lowering operator and the Casimir defect, test whether they close as a finite covariant multiplet without importing angular-momentum theory, and compare against a physical hydrogen cross-principal-shell SO(4,2) dipole with its independent parity and radial normalization. Alternatively demonstrate a finite-component closure obstruction. Preserve q=2 sector grading and never replace the defective original J by the alternative closed half-step B without labeling the change.
