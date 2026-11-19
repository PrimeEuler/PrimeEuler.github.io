# Cone Derivation Ledger v15.1235 — Same compact Maxwell oblique Fourier mode now drives full K4 scalar/vector/tensor electric Riemann

**Date:** 2026-11-19 Eastern. **Lane:** Gravity/Cone. **Status:** [D] source-first finite-time scalar, transverse-vector and tensor-plus K4 metric-mode integration for the **same actual three-dimensional compact Maxwell packet**, projected at oblique K=(1,0,1); [D] exact K4 source-conservation simplifications and a full 3×3 orthonormal electric-Riemann Fourier-amplitude matrix for that single mode; [D] three spatial resolution comparison 32³/48³/64³ and exact initial oblique gravitational constraint regression; [N] no complete real-space 3D metric, no homogeneous-background k=0 completion, no causal photon/free-mirror/emitter clock readout, and no action-derived quarter-grid coupling/G-free novel gravity. **Immediately before ledger write live HEAD:** c99f93dfdabdbb5224adf4ea1076b59ff689a3db. Target v15.1235 unused at check; strictly additive. All archived K4/Suzuki/Lane A, Audit, Sandbox and Muse assets untouched.

## Gate 1185 — predecessor/audit and actual scope
v15.1078 is the original finite-support vacuum Maxwell Cauchy packet, v15.1085 the Maxwell SVT/Fourier Ward, v15.728–729 the **pressure-corrected** K4 scalar equation and sourced Bardeen transfer, v15.710/721 the source-first vector shift, v15.750 the ordinary K4 vector/tensor coasting mode equations, and v15.787 the **full electric Riemann** scalar/vector/tensor metric readout. v15.1226 reconciled the original (+---) Maxwell action-source sign and the complete initial energy-second-derivative jet; v15.1228 computed the longitudinal scalar tidal first-time jet. The historically flagged Gravity v15.1229 finite-time longitudinal scalar mode was independently verified in External Audit **Round 617/v15.1230**, including the source-file re-execution across all three spatial grids and the version-number collision (Audit Round 616 owns v15.1229 by earlier UTC timestamp). v15.1234 then showed actual scalar anisotropy, generated transverse vector momentum and tensor-plus stress at the **oblique** wavevector K=(1,0,1), and evolved only its tensor-plus metric. v15.1234 had no vector/scalar metric calculation. The purpose of this gate is to **finish all three independent sourced metric sectors at this one oblique Fourier mode** and assemble the full local curvature matrix, without mislabeling a stress projector as a gravitational tide.

## Gate 1186 — physical Maxwell history and oblique initial constraint
The same unmodified 3D compact Maxwell initial stream function and electric field are used:
**chi(x,y,z)=f(x) f(y/2) f(z)**,
**E0=(∂y chi,−∂x chi,0), B0=0**, with **f(u)=(1−u²)^3** for |u|<1, zero outside. Its free conformal Maxwell evolution is `Ehat(q,xi)=cos(|q|xi) Ehat0(q), Bhat(q,xi)=−i(q×Ehat0(q))sin(|q|xi)/|q|`, with **xi=sqrt3 log tau** and coasting **a=tau/sqrt3**. This evolves the actual Maxwell field with magnetic induction and computes the conformal stress
**R=(E²+B²)/2, F=E×B, Tij=R δij−EiEj−BiBj**.
For K=(1,0,1), |K|=sqrt2, select the FFT bin (2,0,2) on box L=4pi; spatial coefficients use FFT/N³. Use orthonormal spatial basis
**n=(1,0,1)/sqrt2, e=(1,0,−1)/sqrt2, b=(0,1,0)**,
where the last two vectors span the plane transverse to K.

At this K, Maxwell source Fourier amplitudes have **R, Tnn=n_iTij n_j, F_n=n·F, F_e=e·F, T_ne=e_iTij n_j, and Pi_plus=(Tee−Tbb)/2**. The extra vector-b polarization and tensor-cross source vanish from this particular separable initial data by reflection symmetry. Crucially, **Tnn(1) != R(1)** for this oblique mode: the longitudinal v15.1228 special-case first-jet formula, which used Tzz(1)=R(1), is **not** an admissible initial oblique scalar constraint. This gate retains the actual Tnn everywhere. The initial-slice gravitating Maxwell source is already present; the K4 propagating solid and TT modes are initialized at zero displacement and velocity, but sourced metric lapse and shifts are not set to zero.

## Gate 1187 — pressure-corrected scalar sector driven by actual R and Tnn
Use the physical signed source coefficients in the original archived (+---) convention:
**J_Phi=J_psi=−sqrt3 R/tau**, **J_B=−i sqrt3 |K| F_n/tau**, and Maxwell momentum conservation `F_n,xi=−i|K|Tnn`, giving
**J_B,dot=[−3|K|² Tnn +i sqrt3 |K| F_n]/tau²**.
The v15.728 source-first scalar mode therefore simplifies *exactly* to
**Pddot+3Pdot/tau + beta_S P/tau²=9(3Tnn−R)/(2|K|²tau⁴)**,
where **beta_S=[8eta_s(1+|K|²)−3|K|²]/3**. For eta_s=3/4, |K|²=2, beta_S=4. Initialize **P(1)=Pdot(1)=0**. The original v15.729 sourced lapse Bardeen potential is
**Phi_N=[tau²Pddot+2tau Pdot]/[3(1+|K|²)]+sqrt3(J_Phi+J_psi)/[2tau(1+|K|²)]−3J_B,dot/[2|K|²(1+|K|²)]**.
The true scalar **full electric-Riemann STF** coefficient is **S=−3|K|² Phi_N/tau²**. The independent full-Riemann isotropic Ricci trace identity, with positive Maxwell energy, is **A_iso=3R/tau⁴**. Both metric coefficients belong to the full Einstein–Hilbert+K4 solid+Maxwell source action, not a Weyl-only projection.

For initial P=Pdot=0 and actual Tnn(1), exact direct constraint algebra gives
**S(1)=−3/[1+|K|²]·{(3/2)[3Tnn(1)−R(1)]+|K|²[−3R(1)+(9/2)Tnn(1)]}**.
This is asserted by the reproducer and does **not** assume Tnn=R. At N=64, R_K(1)≈0.00068121634, Tnn_K(1)≈0.00053543769 and **S(1)≈−0.00211928629**; the tensor and vector source contacts at the initial Cauchy surface are treated separately. No special q=2 arithmetic mesh or new physical length scale enters.

## Gate 1188 — transverse vector shift and full vector electric Riemann
The archived v15.710/721 K4 source-first transverse vector sector has
**A_V=tau(4+3|K|²)/(6sqrt3)**,
**b_V=4tau/[sqrt3(4+3|K|²)]**,
**K_V=2tau³|K|²/[3sqrt3(4+3|K|²)]**,
**B_V=b_V f_dot−J_V/A_V**,
and the vector f equation
**fddot+3fdot/tau+beta_V f/tau²=−(b_V J_V)'/K_V**,
with **beta_V=2eta_s(4+3|K|²)/3=5** at eta_s=3/4 and |K|²=2.
The actual Maxwell transverse flux coefficient in the archived physical source sign is **J_V=−sqrt3 F_e/tau** (the `e` polarization). Thus **b_V J_V=−4F_e/(4+3|K|²)** and, using *actual Maxwell transverse momentum conservation* `F_e,xi=−i|K|T_ne`, the forced vector equation becomes
**fddot+3fdot/tau+beta_V f/tau²=−18i T_ne/(|K|tau⁴)**.
The source is imaginary in the chosen Fourier phase; the reproducer integrates its real imaginary-amplitude `f=i v` and reconstitutes real physical fields with the conjugate -K mode. This avoids numerical differentiation of noisy Fourier momentum stress.

The sourced metric shift is
**B_V=4tau f_dot/[sqrt3(4+3|K|²)]−J_V/A_V**,
which, for `f=i v, F_e=i F_{e,im}`, reads `B_V=i B_im` with
**B_im=4tau v_dot/[sqrt3(4+3|K|²)]+18F_{e,im}/[tau²(4+3|K|²)]**.
Its time derivative is evaluated from the integrated fddot and the Maxwell conservation law, not an unverified finite difference. The *full* vector off-diagonal orthonormal electric-Riemann coefficient, from v15.787, is
**V=−i|K|(B_V,dot+B_V/tau)/(2a)**,
real for this Fourier phase. It is **not** the Weyl-only formula `−i|K| B_V,dot/(4a)`. Parity gives the e-polarization only; b-polarization is zero on this source mode. This vector result requires the archived sign of the physical momentum source `J_V`, a prime target for independent Audit.

## Gate 1189 — tensor-plus and complete 3×3 full tidal matrix
The tensor-plus sector is inherited from v15.1234:
**gammaddot+3gammadot/tau+beta_T gamma/tau²=−18 Pi_plus/tau⁴**, with **beta_T=3|K|²+8eta_s/3=8**, and initially gamma=gammadot=0. The *full* tensor-plus electric-Riemann amplitude from v15.787 is **T=−(gammaddot+2gammadot/tau)/2**. All three mode equations use the **same time-dependent Maxwell source**, identically sampled on each spatial resolution, not independent chosen pumps. Numerical integrations use SciPy solve_ivp, cubic-spline Maxwell stress interpolation, and the same boundary/init conditions; field Fourier modes are paired ±K to recover a real space field.

The full Fourier-coefficient electric tidal matrix in the Cartesian x,y,z frame is
**E_ij=A_iso δij+S(n_i n_j−δij/3)+V(n_i e_j+e_i n_j)+T(e_i e_j−b_i b_j)**.
Every term after A_iso is tracefree and the reproducer checks **tr E=3 A_iso** numerically. This matrix is a **single Fourier mode's local orthonormal Riemann coefficient**, not the full real-space tidal field of the compact packet or an actual proper-arm/geodesic/optical output.

With κC=1, eta_s=3/4, tau_final=1.2, FFT box 4pi, initial field amplitude 1, and exact compact source aspect widths (1,2,1):
| N³ | A_iso(1.2) | scalar S(1.2) | vector V(1.2) | tensor T(1.2) |
| --- | ---: | ---: | ---: | ---: |
| 32³ | 0.00091367207 | 0.00185250481 | −0.00097212046 | −0.00083014628 |
| 48³ | 0.00092255633 | 0.00188157320 | −0.00099230577 | −0.00085034389 |
| 64³ | 0.00092367806 | 0.00189032150 | −0.00100341178 | −0.00085751112 |

For 64³, the **Cartesian full electric Riemann matrix** is approximately
`[[−0.00019344,0,+0.00137392],[0,+0.00115108,0],[+0.00137392,0,+0.00181339]]`.
The vector off-diagonal response is comparable to scalar and tensor contributions; neglecting it changes the complete tidal eigenstructure, even though the second transverse vector polarization vanishes by symmetry. The 48→64 vector coefficient changes ~1.1×10^-5 and the other channel differences similarly indicate only **preliminary numerical spatial convergence**, not continuum or high-precision certification. Finite-time Maxwell source stress is ordinary conserved EM physics; gravitation is ordinary Einstein+specified solid.

## Gate 1190 — reproducibility, Audit's next check, physical interpretation
**Reproducer:** research-notes/k4_compact_maxwell_oblique_three_sector_full_riemann_v15_1235.py, additive SHA **c99f93dfdabdbb5224adf4ea1076b59ff689a3db**. A local independently run NumPy/SciPy implementation with the same spectral Maxwell evolution, vector/scalar/tensor forcing and full-Riemann reconstruction produced the displayed 32/48/64 values, exact initial oblique scalar constraint identity, tensor channel agreement to v15.1234 and isotropic trace identity. The committed script includes corresponding regression and spatial-resolution tolerance assertions. **External independent committed-byte replay remains pending.**

**AUDIT HANDOFF:** clean-checkout replay the exact committed reproducer and check initial compact Maxwell E divergence/source parity and its oblique (2,0,2) FFT coefficient, spectral Maxwell B curl sign, 3D stress trace/Maxwell conservation, signs of J_Phi/J_psi/J_B/J_V in the original archived (+---) metric variation, use of transverse momentum Ward to obtain the **−18i T_ne/(k tau⁴)** vector drive, vector metric shift source/contact term and full-Riemann `Bdot+B/tau` coefficient (not just Weyl), nonparallel scalar source **Tnn!=R**, tensor plus physical 9/tau⁴ stress scaling, assembled matrix trace, and all numerical grid values. Verify the same-source same-parameter matched-model null; the calculated quantity is a Fourier coefficient, not a calibrated gravity observation.

**NEXT:** extend all nonzero 3D Fourier modes and handle k=0/background constraints, reconstruct full real-space metric and local electric Riemann; then use the existing v15.811/v15.821 properly gauge-controlled coasting photon/free-mirror/emitter-clock/event transfer. Only an additional quarter-grid action-derived interaction with a nonzero **matched Einstein+identical solid residual** can support a genuinely new gravity prediction. No such selector appears in this gate.
