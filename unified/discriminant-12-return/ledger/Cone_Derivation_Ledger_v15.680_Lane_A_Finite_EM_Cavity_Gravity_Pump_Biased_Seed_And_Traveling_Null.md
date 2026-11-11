# Cone Derivation Ledger v15.680 — Gravity lane: finite EM cavity, static-field seeded conversion, and traveling-wave parametric null

**Date:** 2026-11-11 US Eastern. **Parents:** v15.624 EM vs gravity Casimir correction; v14.925–935 K4 elastic source / tensor mass / full SVT return; v15.676 LC pump, energy budget and conformal Maxwell null; v15.678 prescribed homogeneous shear Maxwell Floquet gain; v15.679 traveling WKB K4 phase matching and static-field seed. **Status:** [D] exact static-bias Maxwell source, finite standing-wave mode integral, conditional first-order single-mode pump cancellation and small-K4-mass expansion; [C] fixed-wall prescribed shear rather than experimentally covariant flexible conductors; [O] physical Cone quarter-grid pump, amplitude/phase selection, full 3D cavities and gauge-invariant boundary transfer. **Immediately prewrite live HEAD:** ad045731e4af1d4ad376cac88c0bc4e5f0bead58 (reproducer new additive file); no v15.680 ledger collision. Frozen Suzuki and prior audited entries untouched.

**External literature check:** Gao, Gao, Liu, Sun, “Novel high-frequency gravitational waves detection with split cavity,” *Phys. Rev. D* 109 (2024) 084004, DOI 10.1103/PhysRevD.109.084004, already constructs a split cavity/LC resonator in strong static magnetic field (so using static flux plus LC gain is **not an unreported new concept**); Ahn, Bae, Im, Park, *Phys. Rev. D* 110 (2024) 064061, DOI 10.1103/PhysRevD.110.064061 flags improper gauge-dependent rigidity assumptions and develops elastic/gauge-invariant cavity observables; Gué, Krokotsch, Moortgat-Pick, “Covariant eigenmode overlap formalism for gravitational wave signals in electromagnetic cavities,” *JCAP* 08 (2026) 058, DOI 10.1088/1475-7516/2026/08/058, treats elastic moving boundaries and electromagnetic backreaction covariantly. The results below are intentionally a narrower analytical toy, NOT a claimed rigorous signal from a real detector.

## Gate 206 — boundary-compatible transverse static B is a seed for forced EM conversion

On prescribed anisotropic metric ds²=−dt²+exp(2b(t,z))dx²+exp(−2b(t,z))dy²+dz², use one vector potential A_y(t,z), fixed conducting perturbation-endcap data a_y(t,0)=a_y(t,L)=0, and a prepared transverse background magnetic flux represented by A_y^(0)=B0 z (static B_x=−B0). The exact bulk Maxwell equation is ∂t[e^(2b)∂t A_y]−∂z[e^(2b)∂z A_y]=0. Setting A_y=B0 z+a_y and expanding to first order in b and a_y yields

**(∂t²−∂z²)a_y=2B0∂z b**.

A static **transverse magnetic field** is a valid nonoscillating electromagnetic seed in the prescribed model. A static charge by itself does NOT automatically carry an appropriate transverse EM mode. In particular, a perfectly longitudinal electrostatic E_z field and z-propagating plus-polarized transverse-traceless shear have vanishing first-order direct TT contraction in this arrangement. To use a *capacitor* with static transverse E_y, the electrodes and cavity endcaps must be rearranged—uniform E_y tangential to perfectly conducting z-endcaps would violate that ideal boundary condition. No experiment-ready charge-capacitor sensitivity is claimed here.

## Gate 207 — exact finite sine-mode overlap and forced resonant field

For fixed endcaps, f_n(z)=sqrt(2/L)sin(k_n z), k_n=nπ/L, n≥1; write a_y=Σ q_n(t) f_n(z). With a phenomenological EM quality factor Q, each normal-mode equation is

**q̈_n+(ω_n/Q)q̇_n+ω_n²q_n=2B0∫_0^L f_n(z)∂z b(t,z)dz**, ω_n=k_n (vacuum c=1).

For b=h Re[exp(iΩt−iKz)] the exact dimensionless spatial overlap is

**J_n(K)=(2/L)∫_0^L sin(k_nz)e^(−iKz)dz = (2k_n/L)[1−(−1)^n e^(−iKL)]/(k_n²−K²)**,

with the removable limit at K=±k_n. The idealized signal magnetic-field *peak antinode amplitude*, relative to B0, is

**|B_sig|/|B0|=2h K ω_n |J_n(K)| /sqrt[(ω_n²−Ω²)²+(ω_n Ω/Q)²]**.

For first mode L=π, k_1=1 and **J_1(1)=−i**, a resonant traveling shear K=Ω=ω_1 gives **|B_sig|/|B0|=2Qh**. At Q=100,h=10^(−8) example: Ω=K=0.95→1.98722×10^(−7); 0.99→8.95266×10^(−7); 1.00→2.0×10^(−6); 1.01→8.93477×10^(−7); 1.05→1.98636×10^(−7). These numbers are **unit normalized prescribed-strain responses**, NOT detector sensitivity or realistic astrophysical wave strengths; finite apparatus elasticity, proper-detector-frame fields and external coil energy must be computed.

## Gate 208 — finite standing cavity cancels the first traveling-vacuum 2:1 one-mode pump

With **no static B bias**, restrict to one cavity mode A_y=q(t)f_1(z) and choose the real even shear quadrature b=h cos(Ωt)cos(Kz). The exact Maxwell quadratic Lagrangian becomes 1/2 M(t) q̇²−1/2 S(t)q² with O(h) modulations

M=1+2h M_K cos Ωt, S=1+2h S_K cos Ωt,

where first mode L=π,k_1=1 and

J0(K)=sin(πK)/(πK),
Jc(K)=[sin π(K−2)/(K−2)+sin π(K+2)/(K+2)]/(2π),
M_K=J0−Jc, S_K=J0+Jc.

Rescaling to u=sqrt(M) q gives the canonical normal-mode equation

**ü+[1+h A(K,Ω)cos Ωt+O(h²)]u=0**, A=2(S_K−M_K)+Ω² M_K.

At the primary 2:1 pump frequency Ω=2, exact simplification yields

**A(K,2)=4 sin(πK)/(πK)**.

Hence **A(0,2)=4** for a *spatially uniform time pump*, reproducing the homogeneous positive Floquet gate, whereas **A(2,2)=0** for a **traveling lightlike gravitational wave** (K=Ω=2). The sine spatial quadrature also has vanishing same-mode overlap at K=2. This is a precise *single standing-mode, fixed-wall, first-order* null; it does not exclude cross-mode mixing, other polarizations or boundary deformations. It prevents promoting the earlier homogeneous Mathieu gain directly to a physical propagating GR wave in the same cavity.

## Gate 209 — K4 WKB timelike tensor gives a parametrically weak opening

If one **conditionally** replaces the massless GR dispersion by the *existing* K4 stable elastic-solid local tensor relation Ω²≈K²+m_T² with m_T²=(8η/3)H², 3/8<η≤3/2, and sets Ω=2, then K=sqrt(4−m_T²). The exact mode-overlap coefficient obeys

**A(K,2)=−m_T²/2+O(m_T⁴)** (in units k_1=1).

For a weak prescribed pump, the corresponding primary Floquet amplitude exponent is **σ≈h m_T²/8** *before EM loss*, a source-dependent local-WKB estimate, not a full cosmological solution or gain prediction. For subhorizon lab-like EM frequencies this opening scales h(H/ω_EM)², and is extremely weak. K4 η, h, frequency, phase and mechanical source are not selected by the Cone quarter/half lattice.

## Gate 210 — energy balance and physical experiment selector

A damped forced cavity mode with q̈+ω_n/Q q̇+ω_n²q=F_n(t) has E_n=(q̇²+ω_n²q²)/2 and exact **Ė_n=F_n q̇−(ω_n/Q)q̇²**. The work is supplied by the time-dependent gravitational/mechanical background, with static magnetic flux and supporting currents functioning as bias/geometry; a lone static charge is not perpetual energy. The fully driven and mechanically self-consistent experiment must include Maxwell fields and charge conservation, proper detector frame, finite conducting walls/elastic dynamics and Q, source coherence, polarization, EM pickup calibration and gravitational backreaction. A real capacitor setup also needs non-longitudinal field/electrode geometry to couple to TT shear.

The literature's finite-cavity methods can perform these follow-on tests, but none has yet supplied a **Cone-specific** dimensionless strength or extra frequency. The static ratio u_G=1/4 to u_EM=1/2 is **not** a proof of pump temporal frequency or stress-energy work; scaling the grid without physical operator selection still yields zero chosen coupling.

**Reproducibility:** `research-notes/finite_cavity_gravity_em_v15_680.py`, additive script committed ad045731e4af1d4ad376cac88c0bc4e5f0bead58 and executed locally, PASS. Exact SymPy tests of source linearization, cavity overlap and limit, single-mode 2:1 cancellation, local K4 small-mass expansion; SciPy-independent numeric frequency-response table. A more detailed local report and executable archive are downloadable as `cone_finite_resonator_gates_206_210.zip`, with SHA256 388517f15537b1c874b060ed539ba38f1ba6a6c9036007f936fd1839c4235e39. No image generation, no certified or Suzuki modifications.

**HANDOFF:** independent audit, sandbox and gravity. Check correct finite-cavity Dirichlet perturbation boundary and static B background; the overlap sign and removable resonant limit; gauge-invariant proper-frame meaning and moving elastic walls; exact 2:1 same-mode cancellation in the fixed-wall toy; K4 small-mass expansion and WKB scope; realistic 3D electrode/coil and material response. Also compare explicitly to Gao et al. 2024 quarterly split cavity, Ahn et al. 2024 wall critique, Gué et al. 2026 covariant eigenmode framework. Flag any estimate of real GW sensitivity or claim of novel EM-G pump source without source normalization.

**NEXT:** Recast the exact 1D calculation as a physically fixed finite 3D coil/capacitor geometry using covariant detector-frame eigenmodes and elastic boundary equations. Seek a robust *difference observable* between standard GR massless traveling-wave mode overlaps and the K4 tensor dispersion, with eta and amplitude controlled independently. Absent a selected K4 source, treat resulting generator as conventional inverse-Gertsenshtein engineering rather than a new gravitational law.
