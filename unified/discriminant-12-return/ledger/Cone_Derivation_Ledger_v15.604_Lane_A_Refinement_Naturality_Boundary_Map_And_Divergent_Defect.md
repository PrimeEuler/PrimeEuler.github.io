# Cone Derivation Ledger v15.604 — Lane A: exact refinement naturality, inter-shell-map compatibility, and growing total boundary deficit

**Date:** 2026-11-10. **Parents:** v15.602 general q,L mesh; v15.603 External Audit Round 521 (all v15.598–602 confirmed). **Status:** [D] exact refined-grid operator identities; [C] chosen cross-shell geometrical witness maps; [O] continuum physical limit, q=2 selector, coupling and energy. **Prewrite live HEAD:** 527f9d0fef67a88f51797ee2750c0a58f2af7216; v15.604 collision search clean. Additive only; Suzuki frozen and production untouched.

## Gate 67: original step-one dynamics are exactly nested across refinement [D]

For q≥1,L≥1, let j=L/(2q), grid m_i=-j+i/q, i=0...L; original unit-step J_+ connects i to i+q with AM–GM amplitude sqrt((j-m_i)(j+m_i+1)) when destination is present, and J_-=J_+†. M is diagonal m_i. D=[J_+,J_-]-2M; E=j(j+1)I-(Jx²+Jy²+M²), as v15.602.

For any integer k≥2, refine (q,L)→(kq,kL), **holding the same j**. Define the isometric inclusion V_{q→kq} of the coarse shell into fine by V|i>_q=|ki>_{kq}, preserving each magnetic coordinate exactly. Then

J_{+,fine} V=V J_{+,coarse},
J_{-,fine} V=V J_{-,coarse},
M_fine V=V M_coarse,
D_fine V=V D_coarse,
E_fine V=V E_coarse.

The fine ladder decomposes into additional residue chains not supported on the coarse image; there are no coupling edges crossing the image and its orthogonal complement. Hence the coarse original dynamics form a reducing invariant subspace of the fine dynamics. This is exact, and not mere convergence as the mesh refines.

## Gate 68: the generalized boundary map is compatible, but its destination shell rises [D/C]

The q-grid cross-shell map T_{q,L}: H_{j,q}→H_{j_q',q}, with target j_q'=j+(q−1)/q, is the v15.602 witness obtained by sending each nonzero omitted upward/downward edge to the coordinate target m±1, with its original AM–GM coefficient; T†T=2E.

For refined Q=kq, its target shell is j_Q'=j+(kq−1)/(kq) and j_Q'−j_q'=(k−1)/(kq). Both target shells use the same physical magnetic coordinate m at a common point, so there is an isometry U between target shells, embedding the old target index l into fine target index (k−1)+kl. With V on source shells,

**T_{kq,kL} V = U T_{q,L}.**

Thus the exact old missing-edge *destinations as m coordinates* and their amplitudes persist in the refined construction. The target's shell label nevertheless changes; this statement uses a **chosen** centered target inclusion, not a physical identification of two different Casimir sectors. The target label j+(q−1)/q increases monotonically to j+1 as q→∞ without reaching it at finite q. No physical energy spectrum or emission-frequency convergence follows without a Hamiltonian.

For q=1, T=0. Even though fine grids introduce missing edges, they do not create outgoing transitions from old states that were closed in the q=1 spin-j ladder.

## Gate 69: growing total defect and absence of naive finite refinement limit [D]

At fixed j>0, over integer q satisfying L=2qj∈Z and L≥q−1 (eventually for j≥1/2), the audited v15.602 trace identity becomes
tr E_q=(q−1)(6qj+q+1)/(6q)=(q−1)(j+1/6+1/(6q)).
For j≥1/2 this grows asymptotically as q(j+1/6); the total boundary deficit therefore has **no finite unnormalized trace limit** along such nested sequences, even while its value at each old magnetic coordinate is unchanged. For 0<j<1/2, the alternate short-shell formula from v15.602 applies and also grows linearly in q with a different coefficient. A density or renormalized normalization could be investigated, but is an extra choice; no divergent observable or physical energy is inferred from summing increasingly many auxiliary states.

Representative exact tests:
- j=1, q=1→2: trE 0→5/4, rank E 0→2.
- j=1, q=2→4: trE 5/4→29/8, rank E 2→6.
- j=1, q=3→6: trE 22/9→215/36, rank E 4→10.
- j=3/4, q=2→6: trE 1→85/18, rank E 2→8.

Under the **closed** refined-step SU(2) operator B_+ and K_+=q B_+, the physical Schwinger spin on the chosen auxiliary embedding is L/2; changing q at fixed geometric j changes that closed representation. This cannot be confused with the reducing-inclusion naturality of the *original defective unit-step* J.

## Independent checks

Independent exact SymPy construction of P, M, D, E, and rectangular T passed **165/165** (q=1..5, k=2..4, L=1..11) intertwining tests simultaneously for J±, M, D, E and U T = T_f V. Source code and report supplied in the conversation artifact `cone_refinement_compatibility_gates_67_69.zip`. No plots or speculative physics needed.

**Conclusion:** an honest natural nested hierarchy of algebraic shells exists. Refinement adds residue chains and total defects but preserves preexisting original-step dynamics and missing-edge maps. The hierarchy alone does not physically select q=2 / the gravitation offset ±1/4, fix a spectral weight, a canonical physical Hamiltonian, G, or a radiative excitation.

**Next gate:** test compatibility under noninteger rescalings and more general rational refinement denominators, and/or construct a candidate normalized defect density with stated measure. Distinguish refinement-invariance from the separate power-map sector weld of v14.767 and coordinate mesh scaling.

**HANDOFF** target external-audit, sandbox, gravity; status open; type exact refinement naturality/inter-shell boundary commuting diagram/trace asymptotic audit; verify V and U indices, reducibility, T_f V=UT, q=1 limit, and j<1/2 asymptotic caveat. Frozen Suzuki production untouched.