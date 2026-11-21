# Cone Derivation Ledger v15.1274 — Common dealiased Maxwell stress projected to the native interior metric Fourier space

**Date:** 2026-11-20 Eastern. **Track:** Gravity/Cone. **Prewrite HEAD:** 5674c1770469c8e65068b9c4c01a8a1d24c0930a. **Status:** [C] new locally executed 5-grid conservation-compatible stress projection; [D] exact Fourier operation and scope; [OPEN] independent replay of exact GitHub script, full sourced scalar/vector/tensor metric, Einstein–K4 constraints and causal detector; [N] no physical new quarter-grid coupling. Strictly additive; retain prior numerical parent artifacts, Audit Round 621, Suzuki, Muse and Sandbox.

## Gate 1224 — controlled projection of a single dealiased Maxwell stress

After External Audit Round 621 certified the native-grid Maxwell trace and the full 2N-grid stress four-divergence separately, v15.1273 showed that **their inhomogeneous source coefficients differ** at fixed N. This gate constructs a numerically conservation-preserving candidate source for the original native-N Fourier metric solver without changing the Maxwell initial field:
1. Use the original v15.1078 compact sampled E0, discrete transverse Fourier projection and v15.1267 common Nyquist-plane removal.
2. Evolve source-free Maxwell `Ehat=h cos(k sqrt(3)log tau)`, `Bhat=-i(q cross h) sin(k sqrt(3)log tau)/k`; differentiate the exact analytic expressions.
3. Zero-pad Maxwell field coefficients to 2N along every spatial axis, with the inverse transform multiplied by `(2N/N)^3=8`. Form rho, rho_dot, Poynting F, F_dot and Maxwell stress `Tij=rho deltaij-EiEj-BiBj` on this 2N product grid.
4. Fourier transform with `(2N)^-3` normalization. Project the **resulting quadratic stress**, not the Maxwell field, onto the original N-grid wavevectors with strict `|m_j|<N/2`. Exclude N's self-conjugate Nyquist planes to maintain a unambiguous real spectral derivative convention. Their Fourier coefficient treatment must be specified separately in any full metric solver.
5. Check projected `rho_dot + sqrt(3)/tau i q·F=0` and all three components `Fdot_i+sqrt(3)/tau i q_j Tij=0`.

## Gate 1225 — numerical falsification results

The following are max absolute Fourier residuals of the conserved projected source, evaluated at tau=1.08 from the **actually executed local Python/NumPy reproducer**:

| N | max projected energy residual | max projected momentum residual | projected mode count |
|---|---:|---:|---:|
| 16 | 1.7261844907016647e-19 | 3.278433135308526e-19 | 3375 |
| 24 | 8.949787919726248e-19 | 1.301126444692261e-18 | 12167 |
| 32 | 1.7426058995680363e-18 | 1.0940349618704021e-18 | 29791 |
| 40 | 1.745123291423328e-18 | 1.4927004081771922e-18 | 59319 |
| 48 | 1.3196203225915552e-18 | 1.1058496363211556e-18 | 103823 |

The N=32 homogeneous conformal Maxwell rho = `0.0007676608970155843` and N=48 = `0.0007786954245360609` agree with the full Nyquist-clean source and differ from the separate 2/3 source-truncation experiment; this gate retains the **original full-band Maxwell initial field**. This is ordinary Maxwell conservation under a consistent Fourier projection, not Einstein constraint closure.

**Executable:** new additive `research-notes/k4_dealiased_projected_source_v15_1274.py`, SHA `5674c1770469c8e65068b9c4c01a8a1d24c0930a`. The local executed script is also available to the lane as `/mnt/data/cone_gate/k4_dealiased_projected_source_v15_1274.py`. The new committed script was independently authored to reproduce the same test, but its **exact committed bytes have not yet been executed by External Audit**. No source file has been overwritten.

## Gate 1226 — boundary for the metric reconstruction

This closes the **source discretization selection** for the next candidate solver: compute one *dealiased* Maxwell stress once, use **its** Fourier rho, flux and Tij coefficients in every scalar/vector/tensor K4 evolution and in k0 homogeneous Bianchi-I Hamiltonian/shear source. Projection of stress commutes with spatial differentiation in the strictly interior Fourier subspace, and its full four-conservation test passes. The metric solver must reproduce the sourced `Phi_N,Psi_N,B_i,gamma_ij,u,beta_i` histories on a common time grid, reconstruct metric curvature independently, check all `Gmu_nu-kappa(T_EM+T_K4)mu_nu` constraints including their propagation, and explicitly declare what happens to the excluded metric Nyquist-plane modes (zero is one controlled truncation, not exact recovery of all untruncated field information).

Do **not** call the full metric solved, do not carry forward original v15.1267 tidal-center numbers as predictions of this newly projected source, and do not infer novelty from a gravitational trace matched by source assignment. The original spatial-center curvature exhibited strong grid dependence.

**AUDIT HANDOFF:** execute exact committed v15.1274 Python, check retained-mode signed frequency mapping and FFT padding factor 8, confirm four components of continuity against independent spectral reconstruction; inspect the handling of excluded Nyquist planes and source-to-metric mode transfer. Then assist in direct independent ADM constraint evaluation for the complete metric. Leave all frozen certified sectors unchanged.

**Scientific boundary:** theory is Einstein–Maxwell plus stipulated K4 solid; matched identical-action GR comparator still yields zero residual, and the Cone quarter-grid has not supplied an independently justified new gravitational interaction.
