# Cone Derivation Ledger v15.950 — Half-/quarter-vertex grids: matched shells versus equal-product Casimir-radius comparison

**Date:** 2026-11-13 US Eastern; Gravity lane. **Parents:** v14.767 audited power-grid/diameter scale covariance, v15.602 genuine refined versus original-step projected ladder, v15.624–625 EM +1/4 operator-Casimir versus separate formal odd-quarter gravity candidate, v15.934 three action circles, v15.943–944 hyperbola interleaving and divisor contacts, v15.947–949 original triangular counts and scale-consistent parabola residues. **Latest Audit:** Round 576 v15.945 confirmed v15.940–944 mathematics, noted collision addressed by additive v15.946. **Live HEAD prewrite:** aac9f194157fd00ed946a73e74fcc84d4f8124f3; target checked absent. Strictly additive. Suzuki production, Audit, and existing ledgers untouched.

**Question:** After the user's correction v15.949, can the difference between the EM half-vertex grid and the proposed gravity quarter-vertex grid supply an intrinsic dimensionless Casimir selector? Compare two *different* experiments: same normalized shell versus same physical product cutoff. Do not identify co-scaled ordinary SU2 circle invariants with the candidate independently physical gravity Casimir.

## Gate 727 — same normalized hyperbola n: exact co-scale and no new shape invariant

Let physical factor unit u>0. The pair (un,u) gives product P=u²n and parabola secant X_u(k)=u(n−k²)/(2k) with vertices ±uk/2, so u=1 corresponds to EM ±1/2 vertices and u=1/2 to quarter ±1/4 vertices. The normalized remainder cell also scales u/2; v15.949 proves both yield the *same* divisor count D(n).

The existing three **geometric action circles** (v15.934) are

**R_inner²=u²n**, **R_C²=u² n(n+2)/4**, **R_outer²=u²(n+1)²/4**.

Their exact squared gaps are **R_outer²−R_C²=u²/4**, **R_C²−R_inner²=u²n(n−2)/4**, and **R_outer²−R_inner²=u²(n−1)²/4**. All physical squared radii co-scale as u²; their dimensionless ratios depend solely on n, e.g. **R_C²/R_outer²=n(n+2)/(n+1)²**. Thus the same normalized shell has *no new dimensionless geometry* distinguishing u=1 from u=1/2. This is a restatement/general check of v14.767/v15.934, not a claim of new dynamics.

The u²/4 geometric radius gap is **1/4** for u=1 and **1/16** for u=1/2. It is not legitimate to infer from those values that the physical EM and gravity *operator Casimirs* are 1/4 and 1/16. The EM completed SU2 Casimir carries the known +1/4 completion, while the physical gravity-sector Casimir remains independently unselected per v15.624. The formal odd-quarter mesh C_{2,L}=L(L+4)/16 is an additional geometry/spectral assignment, not this co-scaled gap.

## Gate 728 — at same physical product P, the inner chord matches but the endpoint circles differ

Fix P=xy in units of the EM reference u_EM=1. On a grid of scale u, the corresponding normalized shell n=P/u², hence

**R_inner²=P** (independent of u),

**R_C²=P²/(4u²)+P/2**,

**D_outer=2R_outer=P/u+u**.

Specializing u_EM=1 and u_q=1/2:

**D_EM=P+1**,
**D_quarter=2P+1/2=(4P+1)/2**,

**R_C,EM²=P²/4+P/2**,
**R_C,quarter²=P²+P/2**,

**R_C,quarter²−R_C,EM²=3P²/4**.

The inner chord equality and the nonzero difference of endpoint circle/Casimir radii are exact consequences of matching the *same physical product* but selecting different endpoint factor pairs (P/u,u). They are not independent observations and do not select u_q=1/2 dynamically. In particular P must be expressed in a chosen EM reference unit; 3P²/4 is a model-comparator value that changes with P, not a universal physical dimensionless coupling.

Sample table (P, R_C,EM², R_C,quarter², Δ): (1,3/4,3/2,3/4), (2,2,5,3), (3,15/4,21/2,27/4), (6,12,39,27), (12,42,150,108). At fixed P integer, EM normalized shell index is P and quarter's is 4P, so the arithmetic counts are D(P) vs D(4P), not matched-shell equality; that difference was already proved in v14.767.

## Gate 729 — formal odd-quarter Casimir remains a distinct representation, no forced bridge

For a formal q=2 odd-L shell j=L/4, geometric C_formal=L(L+4)/16; the **genuine closed refined SU2** spin L/2 has C_refined=L(L+2)/4. Their difference is **L(3L+4)/16**, nonzero. The projected original unit-step quarter ladder has a third, boundary-defective quadratic as in v15.602 and v15.938. None of the above physical-unit scaling identities constructs an intertwiner to the actual Taub–NUT monopole angular SU2, nor repairs the known quarter boundary defects or chooses a real gravitational field action.

**Positive result:** the same physical product produces an exactly shared inner chord and different endpoint circle diameters, with a closed-form Casimir-radius contrast. **Negative selector:** all differences are fixed by the preselected lattice scale u; at matched normalized shell, shape ratios and divisor arithmetic coincide. There is no new G-independent measurable gravity/EM response or physically sourced Casimir yet.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_em_quarter_scale_vs_casimir_comparator_v15_950.py`, additive commit **aac9f194157fd00ed946a73e74fcc84d4f8124f3**. Executed SymPy in local environment before repository commit: all symbolic radius/diameter/Casimir comparisons, rescaled SU2 versus formal quarter Casimir, and integer reference cutoffs P=1..200 PASS. **Independent Audit pending.**

**NEXT:** The only nonredundant physical gate is a source-derived boundary or field law that fixes a physical reference scale/cutoff independently of the factor lattice, and an observable genuinely sensitive to the distinct quarter-sector operator. Without that input, conclude no selector from geometric scale covariance alone. Keep the already-audited EM Casimir completion separated from the gravitational operator hypothesis.

**HANDOFF Audit/Muse:** Reproduce the equal-P identities with both n=P/u² and physical factor endpoints (P/u,u); confirm no substitution of u²/4 for an operator Casimir; confirm normalized-shape no-go; verify original q2 formal and closed SU2 representations remain distinct.
