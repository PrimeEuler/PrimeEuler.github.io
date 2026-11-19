# Cone Derivation Ledger v15.1226 — Physical Maxwell-to-ADM sign, corrected second source jet, restored Einstein tidal trace, and compact K4 initial scalar Yukawa kernel

**Date:** 2026-11-19 Eastern. **Lane:** Gravity/Cone. **Status:** [D] exact first-order Maxwell action source coefficients in frozen archived (+---) ADM metric; [D] exact general K4 scalar isotropic electric-Riemann trace identity modulo the *derivative* of the correct source Ward; [CORRECTION] the claimed v15.1222 k-dependent `k=2` obstruction is a **symbolic source-derivative substitution bug**, not an Einstein-constraint failure; [D] pressure-source-compatible initial K4 scalar STF response of the compact Maxwell longitudinal Fourier mode, Fourier/Yukawa real-space inversion and exact fixed-time spatial-arm proxy for one specified dimensionless width; [O] full 3D/zero-mode Maxwell and solid constraints and causal photon/mirror/clock apparatus; [N] no physically sourced quarter-grid gravity operator, measured G, or nonzero matched Einstein–Maxwell+same-solid residual. **Immediately prewrite live HEAD:** 9036dd6009f1f046588836ffb41fe9db739ee15d. **Number collision:** v15.1225 belongs to External Audit Round 615, SHA 5eba16e4002c2980e50dae70c12588c0cc8db183, so Gravity uses v15.1226; target checked unused. All additions only; prior Audit, Lane A/Suzuki, Sandbox/Muse, original v14.935 and historical defective scripts preserved.

## Context and correction of the published interpretations
The original K4 EH+solid scalar action was archived v14.935, with sourced P/Bardeen/pressure-Ward equations v15.728–729 and metric full electric Riemann v15.787 (original script shape defect repaired additively v15.792). Earlier Gravity v15.1193–1198 established algebraically an isotropic traveling-harmonic transfer `A_iso=-sqrt3 J0 tau^(−4−iw)` but called its source sign physical before establishing the actual stress convention. Gravity v15.1221 flagged that `J_Phi=+a³rho` would reverse the Einstein Ricci expectation. Gravity v15.1222 then reported a **k-dependent initial compact-Maxwell A_iso=sqrt3 J(k²−4)/[2(1+k²)]** and alleged missing independent E-shear constraint; v15.1224 correctly derived a longitudinal-diffeomorphism Noether identity showing the E equation is redundant if the full solid displacement and shift equations and Maxwell momentum Ward hold. **External Audit Round 615/v15.1225 reproduced the original v15.1222 output and approved it using the *same incomplete initial derivative jet*.** The present gate identifies its computational cause, independently checks the missing datum and gives an additive mathematical correction. The historical audit finding should be superseded on this specific issue, not erased or treated as proof that both versions are simultaneously physical.

## Gate 1167 — physically signed Maxwell linear action in original (+---)
Use the original archived metric
`g00=1+2Phi; g0z=−a B_z; gxx=gyy=−a²(1−2psi); gzz=−a²(1−2psi−2Ezz)`,
and standard real Maxwell Lagrangian `L_EM=−sqrt(−g) F_mn F^mn/4`, with transverse local coordinate fields `F_0x=e, F_zx=b` (zero otherwise). Define physical Maxwell energy density `rho_EM=e²/(2a²)+b²/(2a⁴)`. Independent first-order matrix-inverse/determinant differentiation of this literal Maxwell action gives exactly
**L_EM^(1)=−a³rho_EM(Phi+psi+Ezz)−e b B_z**.
In particular the action's physical coupling convention is
**J_Phi=−a³rho_EM, J_psi=−a³(p_x+p_y+p_z)=−a³rho_EM**,
where the second equality uses traceless Maxwell stress. The longitudinal Ezz coefficient is **−a³Tzz^(physical)** (equal to −a³rho_EM for the chosen transverse wave); the shift term depends on the Poynting direction and is **−e b B_z**. Thus the plus-sign identification in v15.1193/1221 was a **sign dictionary error**: the archived matter action has **−(a³/2)T^mn δg_mn** in its own (+---) stress convention. This exactly agrees with the original K4 solid **linear** L1 from frozen `matter_sector.py`, `−a C(Phi−psi−Ezz/3+2Pzz/3)`: the solid background has rho=C/a², p_sum=−rho, hence J_Phi=−aC and J_psi=+aC, both correct. When using positive physical rho, source coefficient J is negative.

The old traveling-harmonic **formal** `A_iso=−sqrt3 J0...` now has the **correct Einstein sign** once its physical `J0` is taken as −a³rho, not +a³rho. This does **not** certify every boundary/source statement in the eternal-traveling-wave model; it repairs the physically interpreted source normalization.

## Gate 1168 — exact general sourced trace, without dropping Jphi''
Let `P(tau)` solve the original v15.728 pressure-corrected equation
**Pddot+3 Pdot/tau+beta_S P/tau²= 3sqrt3 J_psi/(2k²tau³)−9(tau J_Bdot+J_B)/(2k⁴tau³)**,
and reconstruct **Phi_N, Psi_N** from the full traceful v15.729 Bardeen expressions (unchanged). The prior v15.787 full local electric Riemann coefficient is
**A_iso=Psi_N,ddot+2Psi_N,dot/tau+Phi_N,dot/tau−k²Phi_N/a²/3**
with a=tau/sqrt3.
Perform symbolic differentiation FIRST, and eliminate both Pddot and P''' with the differentiated P equation while keeping `J_Phi(tau),J_psi(tau),J_B(tau)` as **functions**, not constants. An exact algebraic identity results:
**A_iso=−sqrt3 (J_Phi+J_psi)/(2tau³)+sqrt3/[2tau²(1+k²)]·d/dtau[tau J_Phi,dot+sqrt3 J_B+J_psi]**.
The bracket is exactly the previously established **pressure source Ward**. For any physically conserved source satisfying it, the last term vanishes identically and therefore
**A_iso=−sqrt3 (J_Phi+J_psi)/(2tau³)**.
Substitute `J_Phi=−a³rho`, `J_psi=−a³ Σp_i` with `a³=tau³/(3sqrt3)` and kappa=1:
**A_iso=(rho+Σp_i)/6**.
For Maxwell `Σp_i=rho`, this is **A_iso=rho_EM/3**, while the degree-one K4 solid contributes **rho_K4+Σp_i=0** (v15.1221). Thus the *same* pressure-corrected K4 scalar equations actually reproduce the independent covariant Einstein Ricci-00 trace exactly for every k>0 when all source derivatives are retained. There is no necessary extra E-shear dynamical equation and no genuine k=2 Einstein-trace obstruction.

## Gate 1169 — pinpoint the bad initial Maxwell jet in v15.1222
For the compact Maxwell Cauchy source with zero initial magnetic field and vanishing initial momentum, v15.1085 establishes conformal `R'(0)=0, R''(0)=−k²R(0)`. As `J_Phi=a³rho` **in magnitude** and is proportional to `tau^(−1) R(sqrt3 ln tau)` (with the overall negative action sign), the full initial jet is
**J_Phi(1)=J_psi(1)=J**, **J_Phi'(1)=J_psi'(1)=−J**, **J_B(1)=0**, **J_B'(1)=sqrt3 k² J**, and crucially
**J_Phi''(1)=(2−3k²)J**.
v15.1222's original `jet` dictionary **did not contain J_Phi''**. Its routine substituted `jp(t)=J` before the derivative was given its actual initial value; SymPy then evaluated `d²J/dtau²=0`, producing the spurious
**A_iso,bad=+sqrt3 J(k²−4)/[2(1+k²)]**.
In exact general form the missing derivative contributes **+sqrt3 J_Phi''/[2(1+k²)]** at tau=1; adding the actual `(2−3k²)J` reduces the bad expression to **A_iso(1)=−sqrt3 J** identically. In particular, **A_iso(k=2)=−sqrt3 J !=0** for nonzero Maxwell Fourier source, so the v15.1222 zero and its reported source-trace contradiction are computational artifacts. The regression reproducer explicitly computes both the wrong (derivative zero) and corrected expressions and checks their difference. The prior Audit independently checked the *incomplete stated jet* but did not check the missing source-second-derivative requirement; this is a new substantive correction, not a change to archived source equations.

## Gate 1170 — actual initial K4 scalar STF kernel for the longitudinal compact Maxwell projection
With constrained source contacts retained and **P(1)=Pdot(1)=0**, the previously computed v15.1222 initial lapse potential and STF full electric Riemann remain correct in the revised signed source convention:
**Phi_N(1)=−sqrt3 J(k²+2)/[2k²(1+k²)]**,
**S_K4(k,1)=−3k²Phi_N(1)=3sqrt3 J(k²+2)/[2(1+k²)]**,
while the corrected isotropic trace is **A_iso(k,1)=−sqrt3 J(k)**.
This is a *longitudinal k>0, transverse-integrated, linearized K4 sourced initial-value projection*, not a complete locally resolved 3D field. The scalar source contains no transverse-vector component in this Fourier orientation, and the TT projection can be nulled at the initial slice by the original Maxwell packet's equal transverse widths; no claim about all orientations or future times is made.

Take transverse-integrated compact conformal energy `R0 g(z/c)` with `g(u)=(1−u²)^6` inside |u|<1, zero outside, a0=1/sqrt3 and kappa C=1. The **physical signed** ADM source is `J(z)=−R0 g(z/c)/a0=−sqrt3 R0 g(z/c)`. Hence
**S_K4(k,1)=−(9R0/2)[1+1/(1+k²)] ĝ_c(k)**,
**A_iso(z,1)=+3R0 g(z/c)**.
With Fourier inverse defined by the real-line transform at k!=0, `(1+k²)^(-1)` has Yukawa-type kernel `Y(z)=exp(−|z|)/2` (unit K4 length), so
**S_K4(z,1)=−(9R0/2)[g(z/c)+(Y*g_c)(z)]**.
Unlike isotropic A, the STF response has a noncompact exponential spatial tail. This follows from the sourced K4 initial constraint dressing, **not** a new gravitational force law or a quarter-mesh source selector. The k=0 homogeneous/backreaction mode and full 3D boundary data remain open; the inverse transform should be understood as the nonzero-k longitudinal projection under the stated continuum boundary prescription.

## Gate 1171 — corrected *compact K4* fixed-time spatial-arm benchmark (not a causal detector)
Set dimensionless packet width **c=1** in units of the fixed coasting K4 comoving length, `R0=1` for reproducibility (no fitted physical source amplitude), choose an x-arm at z=0 and longitudinal z-arm from z=0 to L=1, and use the historical v15.793 **equal-time line-average proxy**, not a real photon/mirror/clock response. Define
**G=∫_0^1(1−u²)^6 du=1024/3003**,
**Y0=(Y*g)(0)=∫_0^1 e^(−u)(1−u²)^6 du≈0.2795940607284593**,
**Ybar=∫_0^1(Y*g)(z) dz=∫_0^1(1−u²)^6[1−e^(−1)cosh(u)]du≈0.2113047652607089**.
Then
**Scenter=−(9/2)(1+Y0)≈−5.75817327327807**,
**Sbar=−(9/2)(G+Ybar)≈−2.48533697813872**,
**Acenter=3**, **Abar=3G**.
The exact full scalar spatial-proxy arm difference is
**Delta_E_proxy=(Abar−Acenter)+(2/3)Sbar+(1/3)Scenter≈−5.55330538687482**,
or **Delta_E_proxy/Scenter≈0.96442137520349**.
This is a bounded, dimensionless, model-normalized **spatial line-average** in a 1D transversely integrated longitudinal projection. It is not a physically calibrated signal, has no light travel/clock/mirror dynamics, and need not equal the separate *standard-GR* initial-slice proxy (8G+1)/9 computed in v15.1221 using Sandbox v15.1159's **different** sourced constraints and conventions. Do not compare raw signs/normalizations without using the same Maxwell physical rho and gauge metrics.

## Validation, Audit handoff and next gate
**Reproducer:** `research-notes/k4_maxwell_complete_source_jet_trace_yukawa_v15_1226.py`, source commit **9036dd6009f1f046588836ffb41fe9db739ee15d**. The equivalent complete original script was independently executed in local Python/SymPy and returned **PASS** for the exact Maxwell metric variation in archived (+---), general sourced Riemann trace/pressure-Ward derivative identity, bad and corrected initial-source-second-jet regression, corrected STF and isotropic fields, and compact width-one convolution and fixed-time proxy values. This remains pending **post-commit independent Audit re-execution**; original v15.1222 source and External Audit Round 615 remain untouched.

**AUDIT PRIORITY:** independently derive the full `J_Phi''(1)=(2−3k²)J` from the *actual* Maxwell Cauchy source, inspect v15.1222's `jet` substitution order to confirm why its value became zero, reproduce the exact sourced K4 `A_iso` identity including the Ward derivative, and check the direct (+---) Maxwell L1 signs against the original frozen matter L1. Verify B_z/magnetic phase conventions; test longitudinal nonzero-k Fourier inverse, exponential convolution, spatial proxy and full source normalization. Amend the **physical interpretation** of v15.1222 and of Audit Round 615 additively; this mathematical correction replaces the claimed Einstein-trace obstruction. No quarter-grid interaction appears.

**NEXT:** use this now trace-consistent, signed full scalar initial data for the compact Maxwell packet to evolve its *physical time-dependent Maxwell stress* and K4 solid/metric constraints. Construct a true causal finite-distance photon–mirror–clock readout on coasting FLRW, with k=0/background, realistic source/apparatus boundaries, and the matched ordinary Einstein–Maxwell+same-solid comparator. A distinct dimensionless Cone gravitational observable still requires an independently sourced physical q2/quarter-grid action term; the current matched residual remains exactly zero.
