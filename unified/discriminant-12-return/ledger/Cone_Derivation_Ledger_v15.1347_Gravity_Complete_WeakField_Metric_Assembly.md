# Cone Derivation Ledger v15.1347 — First complete weak-field scalar/vector/physical-TT + homogeneous four-metric from one conserved Maxwell source

**Date:** 2026-11-23 Eastern. **Lane:** Gravity/Cone. **Immediately pre-ledger HEAD:** bc093a84ca34e48e873da6bc8b8b8ba4ff96cf04. **Classification:** [N] first actually executed 3D four-metric reconstruction including all scalar, transverse vector and corrected TT helicity sectors plus k=0 isotropic expansion and Bianchi-I shear from one dealiased Maxwell packet at tau=1.08; [PASS conditional] reality, spatial symmetry, projected source/sector Einstein 00/0i/vector-spatial/TT consistency and source-amplitude quadratic scaling; [NEGATIVE] the historical unit-amplitude field is outside a reliably small metric perturbation domain at tested grids; [OPEN] independent Christoffel/Ricci of the **assembled** metric, truly off-shell all-component Einstein+solid residual, evolved scalar spatial trace measured from assembled metric instead of source identity, background--inhomogeneous coupling beyond first order, gauge-controlled observer clock/mirror null propagation and independently selected 1/4-Casimir gravity interaction. Strictly additive. Sandbox's distinct v15.1346 commit fe99331e8042cfa7e68eeee71b7b5f3c6a269f08 was detected during this work and preserved untouched. Audit Round 626 (canonical v15.1344) independently validated the previous Gravity v15.1343 physical TT sign repair; the earlier Gravity source filename bearing v15.1344 remains numerically noncanonical by Audit timestamp precedence, with canonical Gravity result v15.1345. This entry uses the freely checked canonical v15.1347.

## Gate 1260 — a common dealiased 3D Maxwell source and complete linear metric

For the original v15.1078 compact vacuum Maxwell electric field `E0=(1/2 f(x)f'(y/2)f(z),−f'(x)f(y/2)f(z),0)`, `f(x)=(1−x²)^3` on |x|<1, in L=4π periodic spatial cell, apply the exact discrete transverse Gauss projector and shared v15.1267 Nyquist-plane cleaning. Multiply the initial field by a declared amplitude `A`, so all quadratic electromagnetic sources scale as `A²`. Evolve the Maxwell Fourier E/B time histories analytically using conformal time `xi=sqrt3 log tau`. **Always form quadratic** `r=(E²+B²)/2`, `F=E×B`, `Tij=r δij−EiEj−BiBj` **on a doubled 2N³ Fourier-product grid**, then project their Fourier coefficients onto matching signed original N-grid modes with strict `|m_i|<N/2`, discarding k=0 from the nonzero SVT solvers. This is the conservation-preserving v15.1274 prescription, not the earlier aliased native-grid multiplication.

Decompose one and the same `Tij` into `r, F_parallel, F_perp, T_nn, T_nperp, T_TT` by the physical SO(3) projectors, retaining both transverse-vector and both TT tensor polarizations at each Fourier wavevector. The same k=0 Maxwell mean energy and pressure anisotropy drive the v15.1264 homogeneous Bianchi-I `u,beta_i`. Integrate nonzero scalar solid P, transverse vector displacement f_i, and **physical tensor strain** `h_ij` (not the historical negative-source gamma interpreted as metric) with RK4 using cubic-spline interpolation of the same 13-slice Maxwell stress history tau=1..1.08, all propagating variables and first derivatives initialized to zero at tau=1. The scalar lapse/spatial potential use the pressure-corrected v15.729 transfers; the transverse metric shift uses the source-first v15.710/721 constraint; the physical TT tensor obeys the positive-source Einstein equation fixed by Audit Round 626.

The final position-space metric (signature -+++) is reconstructed by inverse discrete Fourier transform:

`g00=−1−2 Phi_N(x,tau)`,
`g0i=−a(tau) B_i(x,tau)`,
`gij=a(tau)²[(1+2u−2Psi_N(x,tau)) δij+2 diag(beta_i)+hij(x,tau)]`,
`a=tau/sqrt3`, `sum beta_i=0`.

Uniform u,beta are supplied **only** from the common source's k=0 Bianchi history and inserted at the exact metric Fourier zero mode; scalar/vector/TT k>0 modes exclude the zero and self-conjugate Nyquist planes. No fictitious k0 scalar inverse k² is used. The symmetry/parity-constrained center values can have near-zero shift even when the **global shift is nonzero**, so report global maxima rather than declaring the vector sector absent.

## Gate 1261 — weak-field validity negative control, four spatial resolutions

The historical A=1 field can make first-order metric corrections large. At N24 and tau=1.08 it produces max |g00+1|=0.4501592720967432, max |gij/a²−δij|=0.31441651139366167, and max |g0i|=0.0429640435869349. Thus a small residual from an equation used to compute the field **cannot** license interpretation as a reliably linearized geometry. This explicitly fails the weak-field-admissibility gate; it does not say the full nonlinear Einstein solution is singular.

Repeat **the same physical field shape** at electric-field amplitude A=0.1. The metric perturbations are then O(A²) and small on all tested meshes:

| N³ | max |g00+1| | max |gij/a²−δij| | max |g0i| | max nonzero TT Fourier strain | max real-space metric imaginary |
|---|---:|---:|---:|---:|---:|
| 12³ | 0.0004951865790260301 | 0.0003466660448581127 | 0.000030023439820154296 | 6.150449762587703e−8 | 7.121470848149013e−20 |
| 16³ | 0.0017027167390677445 | 0.0008841253807951865 | 0.00009669692982606806 | 9.241716825163677e−8 | 4.2402302798771276e−20 |
| 24³ | 0.004501592720967396 | 0.003144165113936559 | 0.00042964043586934893 | 2.839015710848925e−7 | 5.229638762333195e−19 |
| 32³ | 0.004460612220106075 | 0.0030903340592012274 | 0.0005001001668601423 | 2.640986242324861e−7 | 2.338484920175125e−19 |

At N32, the actual spatial offdiagonal g_ij magnitude reaches 3.82e−5; both shift and TT are nonzero and the reconstructed spatial metric is symmetric to ~1e−19 or better. The 24³-to-32³ lapse/diagonal spatial changes are about 1–2% of the full perturbation maxima, but the shift and offdiagonal terms are still more resolution-sensitive (~16% shift increase); no continuum convergence claim. N12/16 poor resolution is visible plainly in the mean Maxwell energy and metric fields. Proper gauge-independent apparatus observables remain absent.

## Gate 1262 — conditional Einstein sector residuals and independent controls

For each retained nonzero Fourier mode at tau=1.08, use the direct metric Einstein scalar operators derived at v15.1276, vector operators verified at v15.1318, and corrected physical TT spatial operator at v15.1343. Compare their 00/longitudinal 0i/transverse 0i/vector spatial/TT spatial components against the separately named Maxwell+original K4 material sources. At A=0.1, the respective maximal Fourier residual classes over all modes are:

| N³ | max scalar 00 | max scalar longitudinal 0i | max transverse 0i | max vector spatial | max TT spatial |
|---|---:|---:|---:|---:|---:|
| 12³ | 2.1743201279226323e−20 | 4.084014308670142e−21 | 3.5299932640700456e−22 | 2.455072058057386e−21 | 1.998468359928115e−21 |
| 16³ | 2.2464230577486786e−20 | 3.8150553015535115e−21 | 7.411538288475128e−22 | 3.196225886904899e−21 | 2.0778776987332055e−21 |
| 24³ | 1.1407253993472904e−19 | 1.9599284164997677e−20 | 1.976961664001736e−21 | 7.914464100907369e−21 | 9.979106909839726e−21 |
| 32³ | 3.2377737356921105e−20 | 1.0598262642289654e−20 | 1.765203427188161e−21 | 6.246867986000465e−21 | 6.6174449004242214e−21 |

These are **conditional on-shell Fourier source-to-mode equation checks** using the *same* P/f/h accelerations employed to evolve the fields, not an independent numerical geometric Einstein tensor for the assembled 4-metric. The scalar spatial trace has a prior independent on-shell symbolic proof (v15.1317), but is not recalculated directly from assembled position-space metric in this gate. The homogeneous Bianchi-I sourced solution was previously independently geometrically checked (v15.1275) but likewise not recomputed by an entirely independent 3D Einstein tensor here. Therefore **do not claim complete independently verified all-component Einstein closure** just from this gate.

Further controls: the computed real 3D metric imaginary leakage is at most 5.3e−19; metric antisymmetry at most ~1e−18; TT trace/divergence at most ~1e−19. At N16, varying source-time samples nt=9/13/25 shifts the final max lapse perturbation only ~9e−13 absolute and relative spatial perturbation ~3e−11 absolute, but this does not certify **spatial** convergence. An amplitude scaling test N16 with A=.05 then A=.2 found the ratio in mean Maxwell energy, max |g00+1|, max relative spatial perturbation, max shift and max TT Fourier strain **exactly 16** (to ~1e−12 relative), matching ordinary quadratic Maxwell stress, not a new nonlinear or quarter-grid effect.

## Gate 1263 — reproducer, Audit and next falsification

Local Python/NumPy/SciPy source **actually executed** is `/mnt/data/cone_gate/k4_common_full_metric_assembly_v15_1346.py`; despite the legacy filename, it corresponds to the **canonical v15.1347** gate, and includes the four weak-field grids, A=1 negative control, two time refinements and additional amplitude scaling experiments (A=.05/.2). Newly added canonical GitHub source `research-notes/k4_common_full_metric_assembly_v15_1347.py`, commit **bc093a84ca34e48e873da6bc8b8b8ba4ff96cf04**, independently authored as a compact full combined reproducer with the same equations, four A=.1 grids, unit-amplitude caveat control, and temporal refinement. Its exact committed bytes have **not** been replayed post-upload by external Audit; do not claim bit-for-bit certification yet.

**AUDIT PRIORITY:** execute the exact committed v15.1347 source; verify 2N product normalization, shared Nyquist cleaning, scalar potential signs, vector material displacement convention, physical positive-source TT sign, k0 u/beta from the same Maxwell history, Hermitian reality and temporal/spectral refinement. Look for any hidden cancellation caused by computing G and stress using the same equation. Then derive an **independent full 3D metric-to-Einstein linearized tensor** with spatial FFT and geometric time derivatives (or an independent ADM Einstein-tensor construction) and compare all 10 mixed components to independently varied K4 solid plus dealiased Maxwell stress on a shared grid. Specifically verify the scalar spatial trace numerically and its propagation. Without this genuinely off-shell verification the full model remains only **conditionally assembled**.

**NEXT:** ensure independent all-component source/metric residual and stronger N32/40/48 refinement at amplitude .1; compute fully causal photon/free-mirror/emitter-clock worldlines/optical phase and compare to exactly matched Einstein–Maxwell+identical K4 action. Mere gravitational strain from the same original material action cannot demonstrate a new Cone-specific observable. No independently justified physical q=1/4 gravitational coupling, SI calibration or G-free prediction has yet emerged.
