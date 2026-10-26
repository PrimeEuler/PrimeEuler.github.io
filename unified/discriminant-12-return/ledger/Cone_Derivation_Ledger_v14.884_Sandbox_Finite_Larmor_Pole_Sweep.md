# Cone Derivation Ledger v14.884 — Sandbox return: finite-Larmor retarded Maxwell pole sweep

Date 2026-10-25. Sandbox return to HANDOFFs v14.880 (finite-larmor-retarded-Maxwell-pole) and v14.881 (finite-larmor-retarded-angular-reduction). Parents v14.871–874, v14.877–881; parents verified by External Audit R353 (v14.883). Research note research-notes/Finite_Larmor_Retarded_Pole_Sweep.md; payload research-notes/payloads/sandbox_larmor_pole_v14_884/. Additive only; Suzuki/far-tail untouched.

[D] Kernel. From the conserved first-order source of v14.879 (rho1 = -i g kx f_a e^{-ik.c(t)} delta; J1 = g f_a e^{-ik.c(t)} [deltadot xhat - i kx v delta]; g = 2qR/u), helical symmetry (v14.878) reduces the quadratic seat kernel to the scalar inverse response, in units of M_T(0) c^2/a^2 with p = ak, z = a omega/c, alpha = Omega a/c, beta = R/a:

Dhat(z;alpha,beta) = -1/4 + 6 pi^{3/2} sum_n int d^3p/(2 pi)^3 e^{-p^2} [A_n . A_n^sharp]_T / (p^2 - (z + n alpha)^2),

A_n = z b_n xhat + alpha beta p_x e_n, b_n = e^{in phi} (-i)^n J_n(beta p_perp), e_n = [(0,-i,1) b_{n-1} + (0,i,1) b_{n+1}]/2, A^sharp = conjugate of A at conjugate z (bilinear form; the sesquilinear |A|^2 is not analytic in z). Coulomb part is the constant -1/4 (v14.873 k_C, rotation-invariant per v14.878). Retarded sheet at Im z < 0: real-axis radial quadrature + per-channel +2 pi i residue correction for Im(z + n alpha) < 0 (sign fixed by the frozen root test below).

[N] Poles. Continuation of v14.874's z0 = 0.4108337143730426 - 0.1700926343728676i; residuals |Dhat(z_pole)| <= 2e-13 at every point; mirror poles at -Re z. The pole stays damped on the whole swept grid (alpha beta = Omega R/c <= 0.7); Re z decreases monotonically in alpha and beta (rotation softens the mode), |Im z| decreases slightly; small-alpha shift is O(alpha^2) at fixed beta.

beta=0.5: alpha .05: 0.410688-0.170050i; .10: 0.410245-0.169930i; .20: 0.408405-0.169567i; .35: 0.402944-0.169322i; .50: 0.394157-0.170010i.
beta=1.0: alpha .05: 0.410249-0.169921i; .10: 0.408474-0.169441i; .20: 0.401056-0.167993i; .35: 0.378622-0.166983i; .50: 0.342407-0.167540i.
beta=2.0: alpha .05: 0.408492-0.169407i; .10: 0.401334-0.167477i; .20: 0.370619-0.161736i; .35: 0.269209-0.151678i (Q = 0.8875 vs 1.2077 frozen).

[N] Verification. (i) v14.874 reproducer rerun verbatim: root residual 3.3e-32. (ii) b_n, e_n vs defining time integrals to 12 digits; Parseval sum |b_n|^2 = 1; channel continuity p.e_n = (n/beta) b_n exact at test points. (iii) alpha=0 kernel vs closed form -1/4 + z^2 F(z) to <= 5e-9 on a two-half-plane grid. (iv) Quasistatic Dhat(0;alpha,beta) + 1/4 -> (alpha beta)^2/5, ratio -> 1 as alpha -> 0: v14.877's coefficient enters the causal equation with the softening (action) sign, not the field-energy sign — v14.877's caveat resolved for this kernel. (v) Harmonic cutoff N=14/22/30 at beta=2: Dhat identical to 1e-13 (extends v14.880's source-weight truncation through the kernel denominators); grid doubling changes <= 1e-12. (vi) Independent sinc implementation (v14.881 route): sector kernels from finite-difference tensor derivatives of 4 pi sinc(k|Dc|) match brute-force (mu,phi,t) quadrature pointwise (4 digits) and are exactly t-independent; retarded tau-transform reproduces the harmonic Dhat to <= 2e-5 at (beta,alpha) = (1,0.35), (2,0.2) and to 2.5e-6 at alpha=0 vs F. In the tau domain the cross sector is odd in tau and pairs source-first <A(t-tau) P_T A^sharp(t)>. (vii) UHP grid scan at alpha_max per beta (Re z in [-1.2,1.2], Im z in [0.02,1.0]): no zero; min |Dhat| 0.11–0.18 at the Im z=0.02 boundary. Grid scan only — no global UHP exclusion claimed.

Scope. Field-only effective kernel for the prescribed rotating source; no support mechanics, constraint forces, bare/source inertia, or physical bicone eigenmode claim — same scope as v14.874. Stability statement covers the swept (alpha,beta) grid and this kernel only. No G/Higgs/monopole content.

Flags: finite_rotation_pole=COMPUTED_FIELD_ONLY; pole_stability_in_swept_range=DAMPED_ALL_POINTS; upper_half_plane_exclusion=GRID_SCAN_ONLY; support_dynamics=ABSENT; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE; v14.880_handoff=CLOSED; v14.881_handoff=CLOSED_comparison_delivered.

HANDOFF
target: external-audit
type: finite-larmor-pole-sweep-verification
parent: v14.884
status: open
action: Independently verify the bilinear kernel normalization, residue-sheet prescription, pole table, and sinc cross-check from the payload code; confirm scope flags.
deliverable: scoped verdict.
