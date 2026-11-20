# Cone Derivation Ledger v15.1262 — All nonzero 3D Fourier K4 SVT modes reconstructed to real-space Maxwell-sourced electric Riemann; homogeneous/background obstruction isolated

**Date:** 2026-11-20 US Eastern. **Track:** Gravity/Cone. **Status:** [D] explicit full nonzero-FFT-grid 3D linear coasting K4 scalar, vector, tensor time evolution driven by the same original divergence-free compact Maxwell Cauchy field; [D] tensorial real-space mean-subtracted local electric Riemann reconstruction at tau=1.08, discrete Gauss projection, conjugate pairing, tensor symmetry and trace checks at three grids; [N] not yet a continuum-converged field or physical full-gravity background; [O] homogeneous k=0 metric and solid/FLRW backreaction, higher-resolution stability, all constraint identities beyond trace, finite-distance photon/free-mirror/clock/end-event transfer; [N] no physical quarter-grid selector or new G-free matched-action effect. **Immediately prewrite live HEAD:** 7d60c8ca486082c386cf9a7ebb6fea7d81def2a3. Version target v15.1262 checked unused before source commit. Strictly additive; no Suzuki/Lane A, External Audit, Sandbox/Muse, or certified K4 archive rewritten.

## Prior art and collision review
The original compact, positive-energy, divergence-free vacuum-Maxwell field is v15.1078. v15.1085 supplied full Maxwell SVT Fourier stress; v15.728–729 physical pressure-corrected K4 scalar equations; v15.710/721 source-first vector shift; v15.750 tensor equation; v15.787/792 full rather than Weyl-only local electric Riemann; and v15.1226 repaired the physical source-sign and missed Maxwell second derivative. Gravity's historical v15.1229 single-longitudinal Fourier-mode result is **independently verified but noncanonical by number**, as Audit Round 617/v15.1230 found that its own earlier Round 616 owned v15.1229. v15.1234 and v15.1235 extended the exact *same* compact Maxwell source to all scalar/vector/tensor gravitating sectors at one oblique Fourier mode K=(1,0,1). **External Audit Round 619/v15.1236 independently re-executed both producers, verified every table and their full-Riemann polarization source operators, and confirmed the three-sector equations.** Since then the external Audit lane has made liveness-only records through v15.1261; this gate uses v15.1262 with no file collision and no takeover of Audit or Lane A numbering.

**New contribution:** apply *those same verified per-mode source-first operators simultaneously to every nonzero Fourier bin* of a three-dimensional Maxwell sample, reconstruct a real-space electric-Riemann 3×3 symmetric field, explicitly handle numerical Fourier Hermiticity and separately exclude the unresolved homogeneous zero mode. This is a spatial real-field step beyond a single K mode.

## Gate 1191 — physically constrained Maxwell field, common time history, Fourier grid
Retain the v15.1078 original conformal electric field from compact stream function chi=f(x)f(y/2)f(z), f(u)=(1-u²)^3 inside |u|<1, zero elsewhere: **E0=(partial_y chi,−partial_x chi,0), B0=0**. On a computational box of side **L=4π** on each axis, sampled on 32³,40³,48³ grids, transform E0 spatially via numpy FFT. Because sampling the C² compact profile generates small nonzero high-wavenumber discrete divergence (as already warned v15.1234), impose an **explicit discrete transverse Fourier projection** `Ehat0←[I−nn^T]Ehat0` for each nonzero discrete wavevector before propagation. This modifies the finite-grid sampled source slightly; it converges toward the analytic divergence-free original source on refinement and is not silently claimed byte-identical to the *unprojected numerical source* in v15.1234. The zero electric Fourier mode stays zero for this source.

All spectral Maxwell modes evolve with the exact free conformal vacuum propagator **Ehat(q,xi)=cos(|q|xi)Ehat0(q)** and **Bhat(q,xi)=−i(q×Ehat0(q))sin(|q|xi)/|q|**, with **xi=sqrt3 log tau** and coasting scale factor **a=tau/sqrt3**. The compact support and causal travel at tau=1.08, xi≈0.1334, remain well inside half-box 2π, so no periodic-image encounter. At each of nine cosmic times from 1 to 1.08 build full 3D *conformal* Maxwell stress:
**R=(E²+B²)/2, F=E×B, Tij=Rδij−EiEj−BiBj**.
FFT all components (normalization FFT/N³), constructing for each q≠0:
**n=q/|q|, R_q, F_n=n·F_q, F_perp=(I−nn^T)F_q, Tnn=n·T_q·n, T_nperp=(I−nn^T)T_q·n, PiTT=[(I−nn^T)T_q(I−nn^T)]^TT**.
These are source projections from one Maxwell field, not phenomenological sector pumps. The source is present initially; initial K4 propagating P, vector solid f_i, tensor gamma_ij and their time derivatives are all chosen zero, while all nondynamical metric contacts are retained.

## Gate 1192 — simultaneous sourced Fourier equations
For each nonzero spatial |q|=k, use eta_s=3/4, κC=1, and the previously derived source-first K4 operators:
**P''+3P'/tau+[8eta_s(1+k²)−3k²]P/(3tau²)=9(3Tnn−R)/(2k²tau⁴)**.
For **each transverse Cartesian f_i**:
**f_i''+3f_i'/tau+[2eta_s(4+3k²)/(3tau²)] f_i=−18i T_nperp,i/(k tau⁴)**.
For the full tensor **TT gamma_ij**:
**gamma_ij''+3gamma_ij'/tau+[3k²+8eta_s/3]gamma_ij/tau²=−18 PiTT_ij/tau⁴**.
All sources are 3D spatial FFTs of the real evolving Maxwell stress; Fourier vector-mode phase and real-field pairing follow v15.1235. Solve the coupled array of independent forced linear Euler equations with explicit fourth-order Runge–Kutta on the nine source times and cubic-spline stress interpolation. This is a **finite-time numerical integration** with untested temporal-step extrapolation, not a continuum-certified PDE theorem.

The scalar Bardeen lapse is reconstructed with the signed original archived (+---) Maxwell sources, including `Jphi=Jpsi=−sqrt3 R_q/tau` and `JB'=(-3k²Tnn+i sqrt3 k F_n)/tau²`; then the scalar full electric-Riemann STF is **S=−3k²Phi_N/tau²**. The isotropic electric-Riemann coefficient is the exact Einstein active-density trace identity **Aiso=3R_q/tau⁴**. The transverse vector shift (Cartesian):
**B_i=4tau f'_i/[sqrt3(4+3k²)]+18F_perp,i/[tau²(4+3k²)]**,
with **F'_perp=−i sqrt3 k T_nperp/tau** by Maxwell momentum conservation. Full vector electric Riemann is obtained from **v_i=−ik(B'_i+B_i/tau)/(2a)**; the full tensor electric Riemann is **T_ij=−(gamma''_ij+2gamma'_ij/tau)/2**.

Sum per spatial Fourier bin in one 3×3 orthonormal tidal coefficient matrix:
**Ehat_ij=Aiso δij+S(n_i n_j−δij/3)+(n_i v_j+v_i n_j)+T_ij**.
It is symmetric by construction, with non-scalar parts tracefree. This is full **electric Riemann**, not electric Weyl alone. The formulas at nonzero k are singular or degenerate at k=0: the code **explicitly sets Ehat_ij(q=0)=0 instead of applying them**. That means the reconstructed real-space field is *mean-subtracted* and is not a complete Maxwell-driven cosmological background.

## Gate 1193 — Fourier reality and homogeneous-mode control
A finite FFT grid's Nyquist indices lack separate negative-q partners in some directions. Using a signed q directly in normalized n and spin projectors can produce a non-Hermitian Ehat at Nyquist even if ordinary complex coefficients elsewhere are correctly conjugated. **Explicitly symmetrize by Hermitian conjugate mode pairing** `Ehat(q)←[Ehat(q)+Ehat(-q)*]/2`, in addition to ij tensor symmetry, before inverse FFT. This is a declared numerical projection (not a new field equation) needed to obtain a consistent real spatial tensor; an alternate implementation should preferably control Nyquist derivative conventions from the start. Inverse FFT uses the FFT/N³ source convention correctly by multiplying Ehat by N³.

The trace identity for all nonzero Fourier modes is `tr Ehat(q)=3Aiso(q)=9R_q/tau⁴`. After removing q=0, the mean-subtracted real-space identity becomes
**tr E_!=0(x,tau)=9[tau^-4][rho_conf(x,tau)−average(rho_conf(tau))]**.
The omitted homogeneous electric trace is **9 average(rho_conf)/tau⁴**. But it is **not legitimate to simply add an isotropic constant curvature and call the complete global Einstein–K4 cosmology solved**: the total homogeneous Maxwell energy changes the FLRW background, the solid equilibrium, and potentially the metric history, requiring a separate homogeneous Einstein/material initial-value problem. Its numerical mean is tracked, not silently discarded.

**Audit limit on the trace test:** the Aiso source coefficient was explicitly *constructed* from the independently derived Einstein R00 trace relation, so observing trace agreement numerically is a strong FFT/symmetry/normalization consistency control but **not an independent verification** of all dynamic scalar/vector/tensor gravitational field equations. Additional Hamiltonian/momentum and matter/gauge Ward checks for the full inhomogeneous metric remain necessary.

## Gate 1194 — concrete 3D real-space reconstruction and spatial-resolution limits
At tau_final=1.08 and fixed compact Maxwell source amplitude 1, box L=4π, eta_s=3/4, the local *central-grid-point* real-space symmetric electric-tidal matrix is reconstructed on three spatial grids. Its diagonal entries are:

| N³ | E_xx(center) | E_yy(center) | E_zz(center) | trace(center) | rho_conf(center) |
|---|---:|---:|---:|---:|---:|
| 32³ | +2.6313580 | +3.6460440 | −2.7607753 | +3.5166267 | 0.5323601 |
| 40³ | +2.4172113 | +3.6332298 | −3.3593807 | +2.6910604 | 0.4075778 |
| 48³ | +2.4222638 | +3.8154697 | −3.3746104 | +2.8631230 | 0.4335840 |

These are model-normalized *local Fourier-sum* curvature coefficients, **not** gravitational accelerations in SI units or measured strain. At 48³ the off-diagonal Cartesian entries are ≈(−1.17e−6, −6.61e−7, +7.02e−8) for xy,xz,yz, reflecting near-symmetries of this source. The central point is particularly sensitive to sampling the compact bump/source, and **40³→48³ differences remain significant** (notably E_yy and energy density), so no tight continuum error bar or precision claim is justified. The value of finer spatial or source time resolution is to diagnose this, not to fabricate a new gravitational observable.

On all tested grids, the numerical maximum local trace residual against the mean-subtracted Maxwell formula is at most **1.8e−15**; the tensor is symmetric by construction and inverse-FFT imaginary residuals are ≲3.5e−16. After explicitly projecting the initial Maxwell electric spectrum, the relative discrete Fourier Gauss residual is ≲3e−16. These are internal algebraic/numerical checks and do not certify the continuum PDE or physical background.

## Gate 1195 — physical interpretation and audit handoff
**Positive:** the same initial compact Maxwell packet now has an **explicit real-space evolving gravitational tidal tensor** assembled from the ordinary source-first K4 scalar, vector, tensor operators across **all nonzero modes** of a 3D FFT grid. This goes beyond v15.1235's single K=(1,0,1) Fourier result, includes the original source's parity, and exposes the homogeneous-background and spatial-resolution obstructions transparently.

**Open:** solve the physical k=0 Einstein–solid+Maxwell background perturbation (with homogeneous anisotropic stresses if present), source-time error analysis and spectral filtering/alias controls; verify inhomogeneous ADM constraints and source conservation after the discrete Gauss projection; derive the corresponding **real-space metric components** (lapse, longitudinal shift and spatial potentials) for a causal finite-arm photon/mirror/emitter-clock calculation. The electric curvature alone does not supply the finite-distance optical metric or retarded initial/boundary data. The spectral computational box, initial matter packet, and coasting background are not an experimentally calibrated laboratory or realistic astrophysical environment.

**Exact matched-model novelty null:** this K4 system is still precisely Einstein–Hilbert gravity plus a conventional relativistic isotropic-solid action and ordinary Maxwell. For the *identical* matter action, initial data, background and detector the GR+same-solid comparator is identical. No quarter-grid Q=1/16 boost carrier, numerical 1/4 mesh, G-free coupling or measurable new Cone effect follows from these mode sums.

**Reproducer:** `research-notes/k4_compact_maxwell_full_grid_mean_subtracted_riemann_v15_1262.py`, additive source SHA **7d60c8ca486082c386cf9a7ebb6fea7d81def2a3**. An equivalent local independently run Python/NumPy/SciPy implementation completed N=32/40/48, emitted the stated matrices, Gauss/trace/reality residuals and source means, and passed all built-in numerical assertions; the original committed bytes have **not yet** been independently re-executed by External Audit. No files from original certified lanes were overwritten.

**AUDIT HANDOFF:** priority independent replay of committed script and source-projection changes relative to v15.1234/1235; check Maxwell discrete Gauss projection and time Fourier propagate, correct k=0 exclusion and real/Hermitian Nyquist pairing, all three sourced K4 equations on every spatial Fourier bin, physical +--- source signs, vector/tensor polarization normalization, real-space 3×3 inverse FFT and mean-subtracted Einstein Ricci trace. Specifically test temporal and spatial convergence and **do not promote algebraic trace agreement to fully verified gravitational dynamics**. Record a correction additively if needed.

**NEXT:** tackle homogeneous k=0 backreaction/solid equilibrium and fully constrained real-space metric reconstruction with time history; then integrate finite-distance coasting FLRW photon, free mirror, emitter clock and physical emission events as audited v15.811/v15.821. Remain alert to ordinary Einstein+same-solid matched-model null until a new quarter-grid action-derived interaction is physically specified.
