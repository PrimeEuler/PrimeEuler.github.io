# Cone Derivation Ledger v15.1222 — Compact Maxwell source fails the E-fixed scalar ADM trace-consistency check; longitudinal shear-stress equation required

**Date:** 2026-11-19 Eastern. **Lane:** Gravity/Cone. **Status:** [D] exact closed Maxwell Cauchy source-jet identities at a longitudinal nonzero Fourier k, their substitution into the archived pressure-corrected but scalar-shear-gauge-fixed K4 P and Bardeen equations, and the resulting k-dependent full-Riemann isotropic trace; [OBSTRUCTION] this candidate isotropic trace does not obey the independently required Einstein Ricci-00/active-stress trace normalization for an electromagnetic positive-energy stress at fixed K4 material action, for either constant overall source sign; [OPEN] recover original longitudinal E-shear equation with its nonzero Maxwell anisotropic-stress source and solve the complete constrained system before claiming physical K4 scalar Maxwell curvature; [N] no physical quarter-grid/G-free observable. **Live HEAD immediately prewrite:** abbd300c7faa7e2272e9e67676cf1c73cc385e89. Target v15.1222 unused; additive-only, all Suzuki/Lane A, Audit, Sandbox/Muse, original K4 archived scripts preserved.

## Ledger/audit review before write
Fresh live HEAD followed v15.1221 with current Lane A work at v15.1217. External Audit Round 609/v15.1200 independently confirmed the **mathematics** in Gravity v15.1186–1198 and discovered a nonexecuting bare SymPy assertion in the committed v15.1198 source (additively repaired v15.1221). The original byte-verified v14.935 scalar canonical reproducer was confirmed. **Important distinction:** these are verifications of the declared reduced equations and algebraic coefficients, not a demonstration that a physical Maxwell source satisfies *every* scalar spatial Einstein/shear field equation in the sourced E=0 gauge. v15.1221 discovered an opposite-sign normalization when comparing the formal traveling Maxwell metric trace with physical positive-energy Einstein R_00. This gate tests a stronger, wavenumber-sensitive invariant rather than guessing which sign should be flipped. The local Maxwell compact-source transverse-integrated initial stress and conservation jet are historical v15.1085, while the standard-GR initial STF comparator is Sandbox v15.1159 and remains a different model.

## Gate 1159 — exact Maxwell initial stress/time jet in the original conformal packet
For the original v15.1085 free-Maxwell Cauchy initial state, transverse-integrate on a longitudinal Fourier mode k>0. The conformal energy coefficient is R(k,0)>0 as a real central-amplitude normalization, the initial longitudinal flux is 0, and `Tzz(k,0)=R(k,0)`. Source Fourier amplitudes are generally signed/complex, so positivity refers to physical real-space energy, not each Fourier coefficient. Its source conservation yields `R'_(xi)(0)=0`, `S_z'(xi,0)=-ik R`, and `R''_(xi)(0)=-k²R`, with conformal time `xi=sqrt3 ln tau`. From Maxwell initial B=0, its spatial stress trace derivative is also zero at the initial slice. In the **nominal** archived source convention `J_Phi=a³ rho`, `J_psi=a³ pressure_trace`, `J_B` from longitudinal flux, with tau0=1 and `a=1/sqrt3`, write `J=J_Phi(1)=J_psi(1)`. Then
**J_B(1)=0, J_Phi_dot(1)=J_psi_dot(1)=−J, J_Phi_ddot(1)=(2−3k²)J**.
The original pressure Ward `tau J_Phi_dot+sqrt3 J_B+J_psi=0`, differentiated at tau1, fixes exactly
**J_B_dot(1)=sqrt3 k² J**.
This follows from the source's conservation jet, not a phenomenologically chosen forcing coefficient.

## Gate 1160 — exact candidate K4 constrained initial STF curvature with P=Pdot=0
Use exactly the archived *pressure-corrected, E-fixed* source-first scalar equation v15.728–729:
**Pddot+3Pdot/tau+beta_S P/tau²=3sqrt3 J_psi/(2k²tau³)−9(tau J_B_dot+J_B)/(2k⁴tau³)**,
**beta_S=[8 eta_s(1+k²)−3k²]/3**.
Put the *propagating scalar* initial data P(1)=Pdot(1)=0, retaining nonzero lapse/shift constraint contacts. Substitution gives
**Pddot(1)=−3sqrt3 J/k²**.
Substitute into the *already established v15.729* pressure-corrected Bardeen sources, with the same stress jet:
**Phi_N(1)=−sqrt3 J(k²+2)/[2k²(1+k²)]**,
**Psi_N(1)=+sqrt3 J/[2(1+k²)]**.
Then, through the historic v15.787 metric-level full-electric-Riemann scalar STF expression, with `a(1)²=1/3`,
**R_STF^(E-fixed)(1)=−3k² Phi_N(1)=+3sqrt3 J(k²+2)/[2(1+k²)]**.
This is an exact result *for the E-fixed reduced equations with those initial data*, not yet the physical full-Maxwell K4 STF. It is explicitly k-dependent and does not equal the imported Sandbox standard-GR STF constant `3κR/(2a⁴)`. Do not mistake that difference for a novel Cone effect: the underlying solid and, critically, the constraint completeness are different.

## Gate 1161 — calculate the **full isotropic** electric Riemann and exhibit an invariant obstruction
From the exact scalar metric-level v15.787 identities,
**E_ij=A_raw δij+R_STF n_i n_j**, with
**A_raw=Psi_N,ddot+2H Psi_N,dot+H Phi_N,dot**, and
**A_iso=(tr E)/3=A_raw+R_STF/3**.
Insert the *same* sourced P equation and its differentiated form; retain time derivatives of all pressure and momentum sources before imposing the Maxwell initial conservation jet. SymPy simplifies all higher-derivative source contributions and gives
**A_iso^(E-fixed)(1)=sqrt3 J (k²−4)/[2(1+k²)]**.
Notice this has **no eta_s**, but unlike the Einstein-trace result it varies with k. At k=2, it is exactly zero even though a positive-energy Maxwell packet has nonzero energy density/Fourier coefficient for generic packet widths. The ratio to a nominal positive-source Einstein trace `sqrt3 J` is
**(k²−4)/[2(1+k²)]**, with derivative **5k/(1+k²)²**, so no overall sign or constant normalization fixes it at every k. A single k=2 zero suffices as an explicit counterexample to promoting the truncated E-fixed solution to physical full constrained Einstein–Maxwell–K4 curvature. The same objection applies with opposite Riemann sign: a fixed overall sign cannot turn a k-dependent zero into nonzero energy density.

By independent covariant Einstein trace, `tr E=R_(00)=κ(ρ+sum_i p_i)/2` for signature (−+++), conventionally oriented Riemann. The frozen K4 solid has *exact* `ρ_K4+sum_i p_i=0` by degree-one material homogeneity (v15.1221), while Maxwell has `sum_i p_i=ρ_EM`. Thus the full physical Einstein trace requires `A_iso=κρ_EM/3` in that convention for the comoving, weak-source background, without an independently arbitrary k-dependent response factor. Translating the source sign from archived (+---) to (−+++) is an open issue, but cannot remove the k-dependent obstruction. **The v15.1193–1198 formal source-to-tidal coefficients therefore must not be used as a physically normalized Maxwell response until the missing scalar equations and source dictionary are fully checked.**

## Gate 1162 — identify the omitted longitudinal spatial-shear stress
The actual v15.1085 initial Maxwell longitudinal Fourier spatial stress is (after transverse integration, at k along z)
**T_ij=diag(P_TT,−P_TT,R)**,
so its spatial trace is R and its longitudinal scalar anisotropic stress is
**Pi_L=Tzz−(Tii/3)=2R/3 !=0**.
In the original v14.935 scalar metric ansatz, the spatial scalar shear `Ezz` appears in `gzz=−a²[(1−2psi)−2Ezz]` and therefore the Maxwell source action necessarily has a term `(a³/2)T^(zz) δgzz` proportional to **a³ Tzz Ezz**. For Fourier `Ezz=−k² E`, its coupling is nonzero and proportional to **−k² a³ Tzz E** (up to the declared signature and stress-source phase conventions). The v14.935 `assemble.py` fixes E=0 *before* obtaining the archived reduced scalar action; the `E` Euler equation is therefore not among the source-first lapse/shift/psi/P variations used in v15.728–729. An unsourced or trace-only source can satisfy a reduced set while violating the unsupplied longitudinal anisotropic-stress constraint. This is the concrete missing sector to test next. It is not yet proved that including E alone suffices to reconcile every mismatch; a full source/sign/Bianchi analysis is required. Do **not** repair the mismatch by changing Maxwell energy amplitudes, inserting a quarter Casimir or flipping only one source coefficient.

## Status, reproducibility and required next action
**Locally executed SymPy PASS**: `research-notes/k4_compact_maxwell_shear_constraint_obstruction_v15_1222.py`, additive commit **abbd300c7faa7e2272e9e67676cf1c73cc385e89**. It constructs the archived P equation, pressure-corrected Bardeen potentials, differentiates the full scalar electric Riemann trace, eliminates P'' and P''' using the sourced evolution equation, inserts the Maxwell conservation jet and proves exact rational functions for Pddot, Phi_N, Psi_N, STF and isotropic trace. It tests the explicit k=2 counterexample, nonconstant k derivative and nonzero scalar anisotropic-stress projector. All protected source files preserved; committed-byte independent Audit outstanding.

**AUDIT HANDOFF — PRIORITY:** (1) independently reproduce the Maxwell initial jet and pressure Ward sign against v15.1085 and v15.728; (2) reproduce exactly the isotropic `sqrt3J(k²−4)/(2(1+k²))` from the E-fixed v15.729 transfer, verifying derivative ordering; (3) check physical Einstein trace/Riemann sign and material rest-frame active-density cancellation from v15.1221; (4) inspect full Ezz/E longitudinal shear source and its covariant momentum Ward under one consistent signature; (5) amend prior traveling-source *physical interpretation* if necessary, without silently editing historical results. This is an explicit **constraint completeness failure**, not an experimental Cone discovery.

**NEXT:** reconstruct the unreduced E-containing Einstein–Hilbert+solid scalar action, introduce the complete Maxwell stress *before* gauge fixing, derive and solve both Hamiltonian/momentum and longitudinal spatial-shear equations with compatible Maxwell Cauchy and solid initial data. Validate the physical isotropic trace against Einstein R00, only then supply the true compact Maxwell K4 STF profile to the finite-arm spatial proxy and implement the causal photon/mirror/clock transfer. With unchanged EH+same-solid+Maxwell action, matched-model novelty residual remains exactly zero; no q2 quarter-sector coupling emerges from this negative gate.
