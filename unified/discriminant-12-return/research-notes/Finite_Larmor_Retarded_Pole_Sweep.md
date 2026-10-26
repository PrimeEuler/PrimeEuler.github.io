# Finite-Larmor retarded Maxwell seat pole sweep

Date 2026-10-25. Sandbox return to handoffs v14.880 (harmonic convergence /
finite-Omega pole) and v14.881 (sinc angular reduction cross-check).
Parents v14.871–874, v14.877–881. Additive only; Suzuki and far-tail untouched.

## Deliverable

The first converged finite-rotation complex poles of the causal Maxwell seat
kernel of v14.873/879, continued from the frozen pole of v14.874

    z0 = 0.4108337143730426 - 0.1700926343728676 i        (z = a omega / c)

over rotation rate alpha = Omega a / c and orbit radius beta = R / a.
Field-only kernel: no support mechanics, no bare inertia, no external
source-support dynamics — the same scope as v14.874's frozen result.
Within the swept range (alpha*beta = Omega R / c <= 0.7) the continued pole
stays in the damped half-plane for every (alpha, beta): rotation softens the
mode (Re z decreases monotonically) and slightly reduces |Im z|; no
upper-half-plane zero appears. Numbers are [N] with the convergence and
independent-residual evidence below; the kernel construction is [D, formal]
given the v14.879 source.

## Kernel

Conserved first-order source of v14.879 (g = 2qR/u, f_a = exp(-a^2 k^2/2)):

    rho1 = -i g kx f_a e^{-ik.c(t)} delta,
    J1 = g f_a e^{-ik.c(t)} [deltadot xhat - i kx v(t) delta].

Helical symmetry (v14.878) makes the reduced kernel a scalar
inverse-response function. With h(t) = e^{-ik.c(t)} = sum_n b_n e^{-in Omega t}
and v(t) h(t) = sum_n d_n e^{-in Omega t} (ledger v14.879 convention),

    Dhat(z;alpha,beta) = -1/4 + 6 pi^{3/2} sum_n int d^3p/(2 pi)^3 e^{-p^2}
        |P_T(z b_n xhat + alpha*beta p_x e_n)|^2_bilinear / (p^2 - (z+n alpha)^2)

in units of M_T(0) c^2/a^2, p = ak, d_n = alpha*beta*c*e_n,
e_n = [(0,-i,1) b_{n-1} + (0,i,1) b_{n+1}]/2,
b_n = e^{in phi} (-i)^n J_n(beta p_perp). The Coulomb part is the constant
-1/4 (k_C of v14.873, rotation-invariant per v14.878). The numerator is the
BILINEAR form A_n . A_n^sharp (A^sharp = conjugate of A at conjugate z);
the sesquilinear |A|^2 is not analytic in z. Retarded sheet at Im z < 0 is
obtained by real-axis radial quadrature plus a per-channel +2 pi i residue
correction for each channel with Im(z + n alpha) < 0.

Anchors (all verified numerically):
- alpha = 0 reduces exactly to v14.874's -1/4 + z^2 F(z),
  F = 1 + i sqrt(pi) z e^{-z^2} erfc(-iz), for arbitrary beta.
- Quasistatic limit Dhat(0;alpha,beta) + 1/4 -> (alpha beta)^2 / 5 as
  alpha -> 0: the v14.877 magnetostatic coefficient enters the causal
  equation of motion with the softening sign (the on-shell action term, not
  the field energy — v14.877's own caveat), consistent with v14.860.

## Pole sweep [N]

Residual = |Dhat(z_pole)| from the production kernel; all <= 2e-13.

| beta | alpha | Re z | Im z | Q = Re/(2|Im|) |
|------|-------|--------|--------|------|
| any | 0 | 0.410834 | -0.170093 | 1.2077 |
| 0.5 | 0.05 | 0.410688 | -0.170050 | 1.2078 |
| 0.5 | 0.10 | 0.410245 | -0.169930 | 1.2071 |
| 0.5 | 0.20 | 0.408405 | -0.169567 | 1.2043 |
| 0.5 | 0.35 | 0.402944 | -0.169322 | 1.1898 |
| 0.5 | 0.50 | 0.394157 | -0.170010 | 1.1592 |
| 1.0 | 0.05 | 0.410249 | -0.169921 | 1.2073 |
| 1.0 | 0.10 | 0.408474 | -0.169441 | 1.2054 |
| 1.0 | 0.20 | 0.401056 | -0.167993 | 1.1937 |
| 1.0 | 0.35 | 0.378622 | -0.166983 | 1.1336 |
| 1.0 | 0.50 | 0.342407 | -0.167540 | 1.0219 |
| 2.0 | 0.05 | 0.408492 | -0.169407 | 1.2057 |
| 2.0 | 0.10 | 0.401334 | -0.167477 | 1.1981 |
| 2.0 | 0.20 | 0.370619 | -0.161736 | 1.1458 |
| 2.0 | 0.35 | 0.269209 | -0.151678 | 0.8875 |

Mirror poles at -Re z + Im z (real source). Small-alpha shift is O(alpha^2)
at fixed beta (evenness under Omega -> -Omega), e.g. beta = 1:
Delta Re z = -0.00058, -0.00236, -0.00978 at alpha = 0.05, 0.10, 0.20.

## Convergence and independent residuals

- v14.874 reproducer (their mpmath snippet, verbatim): root reproduced,
  residual 3.3e-32.
- Harmonic coefficients b_n, e_n vs their defining time integrals:
  agreement to 12 digits at random (k, angles); Parseval sum_n |b_n|^2 = 1;
  per-channel continuity identity p . e_n = (n/beta) b_n exact at test points.
- Kernel at alpha = 0 vs closed form F(z): |diff| <= 5e-9 on a two-half-plane
  grid including the pole (composite Gauss panels to p = 11).
- Harmonic cutoff: N = 14 / 22 / 30 at beta = 2 give identical Dhat to 1e-13
  (production N = ceil(4 beta + 14)); this extends v14.880's source-weight
  truncation to the full kernel denominators.
- Grid doubling (radial panels, mu, phi) at finite alpha: change <= 1e-12.
- Independent implementation (v14.881 sinc route): sector kernels from
  finite-difference tensor derivatives of 4 pi sinc(k|Dc|) match brute-force
  (mu, phi, t) quadrature to 4 significant digits pointwise, are exactly
  t-independent, and their retarded tau-transform reproduces the harmonic
  Dhat to <= 2e-5 at (beta, alpha) = (1, 0.35) and (2, 0.2), z = 0.3 + 0.05i
  and 0.45 + 0.05i (and to 2.5e-6 at alpha = 0 vs F). In the tau domain the
  cross sector is odd in tau and pairs source-first,
  <A(t-tau) P_T A^sharp(t)>; with that pairing the two routes agree.
- Retarded-sheet check: Im Dhat(w + i0) has the v14.873 sign
  (Im = w^2 * sqrt(pi) w e^{-w^2} > 0 at alpha = 0); a rotated-contour variant
  that produced the advanced sheet was caught by this check and discarded.
- Upper-half-plane scan at alpha_max for each beta over
  Re z in [-1.2, 1.2], Im z in [0.02, 1.0] (25 x 20 grid): no zero found;
  min |Dhat| = 0.18 / 0.15 / 0.11 for beta = 0.5 / 1 / 2, attained at the
  Im z = 0.02 boundary near the mirror of the damped pole, as expected.
  This is a grid scan, not a proof of global UHP exclusion.

## Scope

Poles of the field-only effective kernel for the prescribed rotating source.
Support mechanics, constraint forces, bare/source inertia, and any physical
bicone eigenmode claim are absent, exactly as in v14.874. No G, Higgs, or
monopole content. Stability statement is for the swept (alpha, beta) range
and this kernel only.

## Reproduction

Payload payloads/sandbox_larmor_pole_v14_884/: DERIVATION.md, kernel5.py
(production kernel), sweep.py + sweep.json (continuation and table),
timedomain_check.py (independent sinc route), reproduce874.py (v14.874
anchor), kernel_cache_*.npz (angular contractions, regenerable from
kernel5.py). Kernel build ~80 s per beta; sweep eval ~ms per Dhat call.

Flags: finite_rotation_pole=COMPUTED_FIELD_ONLY;
pole_stability_in_swept_range=DAMPED_ALL_POINTS;
upper_half_plane_exclusion=GRID_SCAN_ONLY;
support_dynamics=ABSENT; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.
