# Cone Derivation Ledger v15.1176 — Jxy quarter-midpoint offset versus three inequivalent Casimir assignments

**Date:** 2026-11-18 Eastern. **Lane:** Gravity/Cone. **Status:** [D] exact full-operator midpoint identity and exact distinct quarter-shell Casimir difference; [R] corrects the interpretation of conditional Gravity v15.1174 odd-station mediator hypothesis; [N] no independent gravitational spin Casimir or cross-carrier intertwiner is sourced by the grid. **Immediately prewrite live HEAD:** 7855e6da4f5403022ec85967eb35dc06d35109e4. Unique target v15.1176, additive only; Suzuki/Lane A, Audit, Sandbox, Muse and frozen history untouched.

## Owner clarification and prior ledger control
Owner: 'the Jxy observables are the casimir. the 1/2 parabola transition operators are on the 1/4 grid. the casimir Jxy is offset from the 1/4 grid. and we've already shown the 1/4 grid has a different casimir if we extended the formula to the 1/4 grid.' Precise earlier sources: **v15.952**: one common D=n+1 circle, integer rows K=k label D−1 ordinary Schwinger transition edges; quarter-vertex refinement q=2 admits half-integer rows K=k+1/2, D midpoint stations, alongside those integer edges. **v15.955**: the D midpoint locations are *identical as coordinates* to the D EM magnetic state centers m=(D−1)/2−k; their squared heights exceed the EM transverse (J_x²+J_y²) by exactly 1/4. **v15.602, v15.626, v15.630**: the q=2 formal geometric C and genuine refined closed SU2 C are distinct; odd-quarter j labels are not unitary SU2 highest weights, and standard rank-1/2 Larmor tensors cannot give Δj=1/4. Thus v15.1174's proposed additional odd intermediate *physical states* are **only a new conditional hypothesis**, not the default physical reading of v15.955's geometrical EM state centers. Keep these levels of meaning separate.

## Gate 1082 — positions of transitions and the Jxy midpoint vertical offset
On the common D circle f_D(K)=K(D−K). Standard EM transition edge k=1..D−1 has squared raising amplitude f_D(k). Occupation state |D−1−k,k> (k=0..D−1) has j=(D−1)/2,m=j−k. The quarter-vertex q=2 grid includes the *same* integer EM edge positions plus half-integer physical rows K=k+1/2. The latter sit at X_mid=D/2−(k+1/2)=m, the magnetic state center, not an extra independent conventional spin.

For each k with zeros at f_D(0)=f_D(D)=0,
**Jxy²(k)=<k|J_x²+J_y²|k> = [f_D(k)+f_D(k+1)]/2 = j(j+1)−m²**.
The exact midpoint identity is
**f_D(k+1/2)=[f_D(k)+f_D(k+1)]/2+1/4**.
Consequently **Jxy²(k)=f_D(k+1/2)−1/4**. The −1/4 is a *vertical offset in squared-amplitude geometry*, not a lateral displacement of the state from the quarter mesh, and not an independent gravitational coupling. (Jxy²) is the transverse quadratic **(J²−J_z²)**; it commutes with Jz but **is not the full central SU2 Casimir (J²)** and is generally state-dependent.

## Gate 1083 — three Casimir objects, not one
For ordinary EM D-dimensional Schwinger carrier:
**C_EM=j_EM(j_EM+1)=(D²−1)/4**.

Under the *shared fixed D primitive quarter endpoint convention*, the formal q=2 shell L=2D−1 is assigned j_geom=L/4 and
**C_quarter_geom=L(L+4)/16=(2D−1)(2D+3)/16**,
hence
**C_quarter_geom−C_EM = D/4+1/16 = (4D+1)/16**.
This is **not** the midpoint (+1/4) correction. It compares two different shell assignments and changes with D. q=2 formal L is odd, with 2D formal m-nodes, rather than D quarter-row midpoint *positions* corresponding to EM states. The formula is a well-defined geometric functional label, not a measured gravity operator.

Finally, if we close the refined step-1/2 ladder by scaling its generators to standard SU2, its genuine physical spin is J=L/2 and
**C_closed_SU2=L(L+2)/4**, different from C_quarter_geom by **L(3L+4)/16**. An original-unit-step projected ladder instead has defective operator C_def=C_geom I−E with boundary defect E, a fourth distinct object. Neither is silently equated with Jxy or C_EM.

For D=5: ordinary EM C_EM=6 and Jxy² diagonal (2,5,6,5,2), while f_5(k+1/2) heights are (9/4,21/4,25/4,21/4,9/4). The formal quarter geometric Casimir of L=9 is **117/16**, while the genuine closed refined step-half spin Casimir is **99/4**. These objects do not become equal because their lattice coordinate sets overlap.

## Gate 1084 — correct the v15.1174 conceptual scope and carry forward a sharper physical test
v15.1174 and 1175 correctly tested a *new hypothetical* auxiliary odd-state mediator, common gap and common coupling, yielding the negative nonuniform effective-hop weights. But v15.955's established state-center correspondence shows **the intermediate half-integer rows are not automatically newly available Hilbert-space states**. Therefore the v15.1174 no-go does not refute the original v15.955 midpoint/Casimir geometry; it refutes one additional mediator interpretation.

A legitimate new-physics proposal must (i) specify whether the quarter grid's formal shell (H^{formal}_{q2,L}) is physically occupied independently of the ordinary EM Schwinger D states; (ii) give its true Hilbert-space representation/inner product and energy Hamiltonian; (iii) source an inter-carrier operator through a diffeomorphism/local-Lorentz/U(1)-consistent action; (iv) show a dimensionless, source-normalized measurable tidal/spin effect not equivalent to ordinary SU2 and GR+same-solid. An equality of geometric parabola heights does none of those automatically. The fixed D and the 1/4 spectral differences are *arithmetically exact*, not independently demonstrated physical gravitation.

## Reproducibility and Audit
Canonical `research-notes/k4_quarter_Jxy_casimir_offset_three_carriers_v15_1176.py`, additive source commit **7855e6da4f5403022ec85967eb35dc06d35109e4**; locally executed PASS full midpoint identity, state moments for D=2..13, exact quarter/EM difference `(4D+1)/16` and closed-refined/quarter difference `L(3L+4)/16`, explicit rational D=2,3,5 values. **AUDIT HANDOFF:** verify 1/4 is squared-height rather than shell Casimir difference; confirm D vs 2D counts and state-center X=m; ensure that 'Jxy Casimir observable' is not mistaken for the full center of U(su2); check odd-quarter irrep restriction and v15.1174 scope correction; do not modify the frozen Suzuki work. **NEXT:** use the archived geometric cross-shell (T_{q,L}), parity grading (χ) and physical Larmor spin connection to test any *gauge-covariant* intertwiner between two **specified** physical carriers, without reinterpreting coordinate midpoints as new quantum states or inserting a coupling scale.
