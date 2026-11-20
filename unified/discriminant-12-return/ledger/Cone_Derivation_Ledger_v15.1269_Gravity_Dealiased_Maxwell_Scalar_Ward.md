# Cone Derivation Ledger v15.1269 — Dealiased Maxwell stress restores exact scalar Ward identity

**Date:** 2026-11-20 Eastern. **Lane:** Gravity/Cone. **Status:** [NEGATIVE] direct finite-grid Maxwell quadratic products fail spectral local energy continuity and v15.729 pressure-corrected scalar Ward at finite N despite v15.1267 Hermitian Nyquist fix; [D] 2x spectral oversampling of quadratic stress restores both identities to roundoff; [N] independent full Einstein/K4 ADM constraints and actual time-dependent metric not yet tested; [N] no quarter-grid coupling or gravitational novelty. **Prewrite live HEAD:** e2e4f2fb6716ba0fc1060f400d69ea4f533a06f6. Code committed separately and additively; no parent source, audit, Suzuki, Sandbox/Muse modifications.

## Gate 1214 — distinguish Nyquist real-field repair from stress-product aliasing

Use the exact compact v15.1078 electric-field sample, discrete transverse Fourier projector, and the v15.1267 common Nyquist-plane zero mask. Maxwell evolution uses conformal propagation `xi=sqrt(3) log(tau)` with `Ehat(tau)=h cos(k xi)`, `Bhat(tau)=-i (q cross h) sin(k xi)/k` and **analytically differentiated** time histories (not finite-difference derivative estimates). At tau=1.08 calculate `rho=(E²+B²)/2`, `F=E cross B`, `rho_dot=E·E_dot+B·B_dot`. The continuum identity is `rho_dot+sqrt(3)/tau div F=0` and scalar gravitational source convention v15.729/v15.1235 is `J_Phi=J_psi=-sqrt(3)rho_hat/tau`, `J_B=-sqrt(3)(i q·F_hat)/tau`, so `tau J_Phi_dot+sqrt(3)J_B+J_psi=-sqrt(3) [rho_dot_hat+sqrt(3) i q·F_hat/tau]`.

With direct N³ FFT of the **quadratic** real-space stress, discrete spectral differentiation fails the continuum product rule at aliased modes. This failure remains even though Maxwell fields themselves have imaginary-part residual <=2e-16 and initial Gauss projector residual <1e-15. This is a genuinely independent obstruction from the earlier v15.1267 Nyquist source-energy mismatch, not an Einstein-law anomaly.

## Gate 1215 — dealiased Ward result

Zero-pad the already-Hermitian N³ field Fourier coefficients, inverse-transform on the (2N)³ product grid with correct (2N/N)³ inverse-FFT normalization, and evaluate quadratic rho, Poynting flux and their exact time derivatives there. The original finite Fourier field, its Nyquist removal and time evolution are held fixed. Reconstruct the divergence using the same (2N)³ Fourier grid. The stress now obeys local conservation and its K4 scalar Ward identity to roundoff:

| Original N³ field mesh | Direct N³ maximum scalar Ward residual | Oversampled (2N)³ scalar Ward residual | Oversampled continuity residual |
|---|---:|---:|---:|
| 16³ | 2.0151611240e-3 | 5.5088637547e-19 | 2.2063224451e-19 |
| 24³ | 8.3825508732e-3 | 3.2032205570e-18 | 1.7411322766e-18 |
| 32³ | 8.4706948205e-3 | 2.6151446331e-18 | 1.3132946748e-18 |
| 40³ | 2.2323604358e-3 | 3.6624130174e-18 | 1.7703541236e-18 |
| 48³ | 1.5986389343e-3 | 3.4828060497e-18 | 2.0107990104e-18 |

These are **actual local Python/NumPy execution results from an independently written equivalent reproducer** for this gate; the byte-original committed wrapper has not been independently replayed after GitHub upload. Do not claim its exact byte-level independent certification. The direct-grid error improves somewhat at larger N but is neither monotone nor near strict constraint tolerance. The dealiased identity is automatic for a resolved real transverse finite Fourier Maxwell solution and therefore should not be mistaken for an independent derivation of a gravitational interaction.

**Additive source reproducer:** `research-notes/k4_maxwell_dealiased_scalar_ward_v15_1269.py`, commit `e2e4f2fb6716ba0fc1060f400d69ea4f533a06f6`. It prints direct and dealiased diagnostics for N=16,24,32,40,48 and asserts the strict dealiased Ward and continuity bounds.

## Gate 1216 — implication for full-metric reconstruction

v15.1267's all-grid `R00` tidal-trace composition remains a valid **algebraic check of the designated sampled Maxwell stress**. The new independent Ward gate reveals that the same quadratic stress, when transformed as an aliased N³ product, does **not** obey the exact spectral local continuum energy conservation law at the full retained Fourier bandwidth. Therefore passing the trace does not imply source Ward compatibility or Einstein constraint propagation. A consistent next metric/ADM run must adopt one declared stress projection / dealiasing scheme across **all** scalar, vector, tensor sources, homogeneous mean, and resulting Einstein+solid stress checks. Merely padding one Ward test while continuing to evolve an independently aliased N³ gravitational source would mix two different discretization prescriptions.

Suggested next falsification sequence: (a) compare the low-band coefficients of original N³ and 2N³ Maxwell stress; quantify whether a common 2/3 truncation can make N³ nonlinear products and time derivatives consistent; (b) rerun v15.1267 with one common dealiased Maxwell stress prescription and check whether its pointwise R00 target must be evaluated on the same product grid/projection; (c) reconstruct `Phi_N,Psi_N,B_i,gamma_ij,u,beta_i` with a single gauge and common time grid; (d) independently evaluate Hamiltonian, momentum and spatial Einstein+K4 residuals; (e) only then finite-baseline null photon and free-mirror emitter-clock observable.

**AUDIT HANDOFF:** independently replay exact committed source, verify the continuum identity and sign of J_B from source definitions, check the 2N zero-padding FFT normalization and the no-Nyquist-mask control, and assess the relationship between dealiased Maxwell stress and the previously passed v15.1267 pointwise trace. Protect all archived parent files and the Suzuki certification lane.

**Scientific boundary:** This is ordinary spectral Maxwell conservation plus the corresponding Einstein–K4 Ward identity. A matched Einstein–Maxwell+same-K4-solid model remains indistinguishable, and no independently selected quarter-grid physical interaction has been supplied.
