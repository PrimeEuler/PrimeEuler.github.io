# Cone Derivation Ledger v15.1229 — Genuine compact 3D Maxwell time evolution sources the K4 longitudinal scalar full-Riemann channel

**Date:** 2026-11-19 Eastern. **Track:** Gravity/Cone. **Status:** [D] finite-time, three-resolution, exactly Fourier-propagated 3D Maxwell Cauchy field and its time-dependent stress; [D] driven longitudinal K4 scalar mode and model-normalized full-Riemann scalar STF; [D] direct Maxwell Ward checks with refinement; [N] no complete 3D K4 S/V/T metric, causal finite-arm photon/mirror/clock measurement, or physical quarter-grid coupling. **Immediately prewrite live HEAD:** source commit 842f279fdbcd51a5c6652973958938ab4b48eae1. Proposed v15.1229 ledger path checked unused. Additive-only; protected Lane A/Suzuki, Audit, Sandbox/Muse, frozen archived files untouched.

## Collision, provenance and corrected starting point
The original genuinely compact divergence-free Maxwell field was frozen v15.1078, with longitudinal Fourier source and initial stress jets v15.1081/1085. Gravity v15.1226 repaired the source sign and the missing Maxwell second derivative, restoring the physical Einstein Ricci trace, while v15.1228 derived its exact **initial** scalar tidal time derivative. The pressure-corrected K4 scalar mode equation and gauge-invariant sourced Bardeen potentials are archived v15.728/729, and the *full* local Fermi electric Riemann scalar STF channel (not Weyl-only) at v15.787/792. External Audit **Round 616**, commit edf0e96a42371c9cc2e1c143f6c26b58c41d3178, has independently withdrawn its earlier approval of v15.1222's spurious k=2 obstruction and independently confirmed the v15.1226 Maxwell-second-jet repair.

This gate advances the same actual *3D* Maxwell Cauchy packet through a finite time and integrates the physically sourced K4 scalar Fourier mode. It is neither another eternal null-wave toy nor a claimed complete 3D gravity solution.

## Gate 1177 — exact-in-time spatially discretized Maxwell evolution
On conformally flat Minkowski coordinates, use the v15.1078 compact stream function chi=f(x)f(y/2)f(z), where f(s)=(1-s²)^3 on |s|<1 and zero otherwise. Initial conformal fields are **E=(partial_y chi,−partial_x chi,0), B=0**, satisfying Maxwell Gauss constraints analytically. For spatial Fourier vector q and conformal time xi, exact source-free Maxwell mode propagation with initial B=0 is
**Ehat(q,xi)=cos(|q|xi) Ehat0(q)**,
**Bhat(q,xi)=−i(q cross Ehat0(q)) sin(|q|xi)/|q|**.
On coasting FLRW, a(tau)=tau/sqrt3 and xi=sqrt3 log tau. Ordinary Maxwell physical orthonormal stress scales as a^-4. The compact source is *already present* at tau=1; no external source-on, charged wall, fictitious pump or backreaction is introduced.

Use a periodic spectral *computational* box L=4pi per spatial side, for spatial N=48,64,80, with 23 source times tau=1 to 1.2. Initial physical support is within |x|<1,|y|<2,|z|<1; maximal conformal travel before tau=1.2 is xi≈0.316, well below the half-box 2pi and therefore no periodic-image encounter occurs over this interval. The original compact C2 bump and finite spectral grids still cause discretization and source-interpolation error.

At every time, compute the 3D conformal stress from the propagated fields:
**R=(|E|²+|B|²)/2**,
**Tzz=R−Ez²−Bz²**,
**Sz=(E cross B)z**.
Extract the longitudinal Fourier coefficient with wavevector (0,0,k=1), which is FFT index (0,0,nz=2) on the L=4pi periodic box, normalized as the *spatial mean* FFT/N³. Its conjugate −k must be included for the physical real spatial field. Fourier projected Maxwell conservation is **d_xi R_k=−ik S_k**, **d_xi S_k=−ik Tzz_k**, independently tested using cubic-spline derivative approximations to the actual spectral Maxwell data.

## Gate 1178 — pressure-corrected K4 scalar forcing from genuine Maxwell stress
Work with κC=1 and eta_s=3/4. In the frozen archived (+---) physical Maxwell action's *negative* source convention, confirmed v15.1226,
**J_Phi=J_psi=−sqrt3 R_k/tau**,
**J_B=−i sqrt3 k S_k/tau**,
**J_Bdot=[−3k² Tzz_k+i sqrt3 k S_k]/tau²**.
Substitution in the previously audited v15.728 sourced scalar equation reduces its forcing exactly to
**Pddot+3 Pdot/tau+beta_S P/tau²=9(3Tzz_k−R_k)/(2k² tau⁴)**,
where **beta_S=[8eta_s(1+k²)−3k²]/3**.
Evolve with zero *propagating* solid scalar initial data P(1)=Pdot(1)=0, retaining the source-forced nondynamical metric contacts. Numerically solve this ODE on tau=1..1.2, with the actual Maxwell-mode R_k and Tzz_k cubic-spline interpolated in cosmic time; SciPy adaptive solve_ivp rtol=2e-11, atol=2e-13. No arbitrary source temporal law is fitted.

Reconstruct the complete pressure-corrected source metric lapse Phi_N from v15.729, including both direct J_Phi+J_psi and J_Bdot contact terms. The **full local electric Riemann scalar STF** coefficient is **S_K4=−3k² Phi_N/tau²**, distinct from a Weyl-only detector. The Einstein active-stress trace yields the independent **A_iso=3R_k/tau⁴**. This is a constrained initial-value gravitational scalar mode with Maxwell energy already present, **not** a vacuum-past retarded gravitational waveform.

## Gate 1179 — exact initial-jet regression and empirical spatial refinement
For the actual initial source Fourier amplitude R_k(1) and k=1, v15.1226 and v15.1228 require exactly
**S_K4(1)=−27 R_k(1)/4**, and **S_K4dot(1)=+153 R_k(1)/4**.
The reproducer checks the initial STF identity to machine precision; the initial analytic derivative is reported from v15.1228, not inferred by extrapolating a short finite-difference derivative of an interpolated source. The source changes with time, so no claim of constant redshift factor or permanent resonant growth follows.

The computed finite-time Fourier-normalized results are:

| N³ | R_k(1) | S_K4(1) | exact Sdot_K4(1) | S_K4(1.2) | A_iso(1.2) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 48³ | 0.00075314343 | −0.00508371814 | +0.02880773614 | +0.00326239918 | +0.00105038309 |
| 64³ | 0.00075400338 | −0.00508952282 | +0.02884062930 | +0.00329164398 | +0.00105183762 |
| 80³ | 0.00075367594 | −0.00508731262 | +0.02882810485 | +0.00328251365 | +0.00105136364 |

The maximum relative Maxwell *energy Ward* residuals at interior source times, divided by max |R_k|, are approximately **4.59e-4, 5.03e-5, 4.91e-6** for N=48,64,80; the *longitudinal momentum Ward* residuals are **3.61e-4, 3.45e-5, 2.54e-6**. Both decay with refinement. Final STF differences across grids are ~2.92e-5 (48 vs 64) and ~9.13e-6 (64 vs 80), the latter ~0.28% of the 80³ result: useful stability, but **not continuum or high-precision certification**. Original source normalization is fixed by unit stream amplitude and FFT/N³ mean, not the earlier transversely integrated R0=1 proxy; do not compare raw amplitudes across conventions.

## Gate 1180 — what has and has not been physically completed
Positive: one genuinely compact **3D source-first Maxwell field**, evolved for a *finite* period with generated magnetic field and explicitly checked energy/momentum conservation, drives a **genuine finite-time longitudinal K4 scalar Riemann response** in the archived ordinary Einstein+relativistic-solid model. The exact previously derived initial-time jet is reproduced and a three-grid finite-time response is supplied.

Open: only the longitudinal k=(0,0,1) *scalar gravity* mode is integrated. There is no complete 3D sourced K4 S/V/T metric, global k=0/background handling, initial homogeneous elastic perturbation budget, finite-distance real-space metric reconstruction, or photon/free-mirror/emitter-clock/physical emission-event propagation. Earlier v15.811 and v15.821 contain the appropriate coasting FLRW causal optical transfer and gauge-event controls; reusing them is a later task, **not** a result of this gate.

Negative: the gravitational action remains exactly Einstein–Hilbert+the *same ordinary K4 isotropic solid*+Maxwell. The matched source/initial condition/detector subtraction against Einstein+**identical** solid is therefore zero; the quarter Q=1/16 representation has supplied no physical interaction, absolute G or distinct dimensionless observable.

**Reproducer:** research-notes/k4_compact_maxwell_finite_time_longitudinal_scalar_v15_1229.py, additive source commit **842f279fdbcd51a5c6652973958938ab4b48eae1**. A materially equivalent local NumPy/SciPy implementation ran on all three N³ grids with matching displayed finite-time mode values and conservation trends; original committed-byte postwrite independent Audit is pending. The standalone committed script includes original-field Maxwell propagation, source conservation checks, initial exact K4 STF assertion and numerical spatial-refinement checks.

**AUDIT HANDOFF:** independent clean-checkout re-execution of exact committed script; confirm Maxwell compact Gauss initial conditions, spectral curl sign, time/length scaling, k=1 FFT nz=2, both Maxwell longitudinal Ward relations, negative signed ADM source map, pressure-corrected K4 forcing 9(3Tzz-R)/(2k²tau⁴), sourced Phi_N/full Riemann, correct initial v15.1228 jet and quantitative 48/64/80 convergence. Check source interpolation error and no image-generation use.

**NEXT:** extend *the same freely propagated 3D Maxwell field* to fully sourced K4 scalar/vector/tensor Fourier sectors, including correctly treated zero/background modes, and reconstruct full 3D time-dependent metric curvature. Only then use the previously audited coasting photon–free mirror–clock–event transfer for an actual finite-distance optical observable. No independent Cone novelty absent an action-derived physical quarter-grid coupling.
