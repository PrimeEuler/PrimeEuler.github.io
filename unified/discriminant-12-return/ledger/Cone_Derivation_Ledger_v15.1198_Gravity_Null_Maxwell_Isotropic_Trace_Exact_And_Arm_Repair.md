# Cone Derivation Ledger v15.1198 — Additive correction of full-Riemann finite-arm basis and universal null-Maxwell isotropic contact

**Date:** 2026-11-18 Eastern. **Lane:** Gravity/Cone. **Status:** [D] exact correction of the v15.1197 isotropic electric-Riemann basis error; [D] striking exact identity `A_iso/(J0 tau^(−4−i sqrt3 k))=−sqrt(3)` for the declared sourced traveling null-Maxwell scalar **particular** solution at k>0, independent of the solid shear η_s and k; [D] corrected fixed-time spatial curvature arm proxy; [N] coefficient is an ordinary Einstein–Maxwell–same-solid contact/trace identity, not a selected quarter-grid gravity coupling; [O] causal Maxwell apparatus, original fully compact 3D Maxwell packet, homogeneous k=0 mode, supported initial conditions and photon/mirror/clock transfer. **Immediately prewrite live HEAD:** 70d43a903af4c3cc268536f0fd7d25f85ec82c7b. v15.1198 checked free. Additive-only; all certified Suzuki/Lane A, Audit, Sandbox/Muse, frozen historic scripts unmodified.

## Why this correction matters
v15.787 derives the true local electric Riemann in the scalar sector as
**E_ij=A_raw δij+R n_i n_j**, with
**A_raw=Ψ_N,ddot+2H Ψ_N,dot+H Φ_N,dot** and **R=−k² Φ_N/a²**.
But v15.793's finite-arm *STF* decomposition is
**E_ij=A_iso δij+R Q_ij**, with **Q_ij=n_i n_j−δij/3**, and consequently
**A_iso=A_raw+R/3=(tr E)/3**.
v15.1197 incorrectly substituted A_raw for A_iso in the second representation and initially reported **5.687002726622−0.804222903504 i** for a fixed-time arm difference. The error was identified before certifying v15.1197; its ledger explicitly warns against the premature number. The v15.1197 script and ledger are preserved for transparent provenance. The corrected number here supersedes its arithmetic; the v15.1194/1195 source-to-Weyl/full-tensor metric solutions themselves are not changed.

## Gate 1151 — universal isotropic curvature coefficient for this Maxwell harmonic
In the prior v15.1195 source setup, `J_Phi=J_psi=J0 tau^(−1−iw)`, `J_B=ik J_Phi`, `w=sqrt3 k`, and `P_part=−3sqrt3 J0 tau^(−2−iw)/(k² D)`, where `D=(−1−iw)²+nu_S²`, `nu_S²=(8η_s−3)(1+k²)/3`. The pressure-corrected v15.729 Bardeen potentials then take the form
**Φ_N=J0 tau^(−2−iw) C_Φ(η_s,k)**,
**Ψ_N=J0 tau^(−2−iw) C_Ψ(η_s,k)**.
Using *only* the archived complete electric Riemann tensor and the correct isotropic basis conversion,
**A_iso=A_raw+R/3**,
an exact independent SymPy simplification yields
**A_iso=−sqrt(3) J0 tau^(−4−iw)**.
The η_s and k dependencies cancel **identically** for k>0, real η_s, where the original particular solution is defined. This is a real structural simplification: the scalar **trace** of the electric tidal curvature follows the null-Maxwell source envelope for this highly specific source/gauge/particular solution. It is NOT an independent physical prediction of the q2 quarter level, a mass or G-free coupling: the (J0) amplitude itself already contains the ordinary gravitational field-source normalization. This does NOT establish an analogous relation for general Maxwell stresses, free homogeneous K4 perturbations, gauge- and boundary-complete Cauchy packets or the k=0 homogeneous cosmological mode. Linearity permits a nonzero-k Fourier superposition of such *collinearly traveling null harmonics* when they share the specified particular-solution boundary prescription; this is not the v15.1085 compact 3D standing Cauchy Maxwell packet (which has zero initial Poynting and more complicated stress).

## Gate 1152 — corrected fully specified fixed-time Fourier-arm proxy
For a longitudinal z-arm and a transverse x-arm attached at the same starting point, and for an eternal harmonic source normalized by `J0 tau^(−4−iw)`, the fixed-time *spatial* average factor is
**F(κL)=[exp(iκL)−1]/(iκL)=exp(iκL/2)sinc(κL/2)**.
With `R=R_STF`, the exact local full-Riemann spatial proxy is
**Delta_E=[(2F+1)/3]R+(F−1)A_iso**.
It equals the independently projected raw-tensor expression
**Delta_E=(A_raw+R)F−A_raw**,
and tends to R as `κL→0`. The latter expression is a second, basis-independent check of the correction.

At η_s=3/4, κ²=1/2, κL=1:
- R_STF coefficient **+5.567306167186−0.909137290097 i**.
- Electric Weyl coefficient **−3.711537444790+2.727411870291 i** (unchanged).
- Correct isotropic A_iso coefficient **−sqrt3≈−1.732050807569** (real).
- Spatially averaged STF part **+5.257538668486+0.893131007806 i**.
- Correct isotropic leakage **+0.274580308787−0.796219762359 i**.
- **Correct full fixed-time spatial-arm proxy Delta_E/(J0 tau^(−4−iw))=+5.532118977272+0.096911245448 i**.
This is not an SI acceleration, physical causal light travel delay or a measured transfer coefficient. Real physical perturbations require complex conjugate Fourier pairing. The original v15.1197 number is wrong by the explicit basis-conversion term `(F−1)R/3`.

## Gate 1153 — what remains open for the owner's compact-packet research goal
The new identity fixes the isotropic curvature for this *traveling Maxwell null harmonic particular-solution family*, but it cannot be transplanted uncritically onto the original v15.1085 spatially compact 3D Maxwell Cauchy packet, whose initial electric field is nonzero, magnetic field zero and longitudinal Poynting zero, and whose Fourier stress has multiple helicities and nontrivial time jets. Sandbox v15.1159 solved its initial GR scalar constraints only on a specified longitudinal Fourier slice. The isotropic full K4 electric-Riemann profile of that packet still needs its actual **time-dependent solid and metric perturbations, constrained lapse/shift/spatial shear and complete physical Maxwell stress**. An operational finite detector also needs causal null rays, moving mirrors, beam-splitter clock and real boundary preparation; see v15.810.

**Reproducer:** `research-notes/k4_null_maxwell_full_riemann_arm_proxy_v15_1198_corrected.py`, additive SHA **70d43a903af4c3cc268536f0fd7d25f85ec82c7b**. Equivalent complete local SymPy tests PASS for universal `A_iso=−sqrt3`, Ricci completion, independently expressed two-arm transfer, and corrected numeric responses. The committed script is not yet independently re-executed by external Audit. **Audit handoff:** ensure the two basis conventions are reconciled correctly; verify exact universal source-trace cancellation for arbitrary η_s/k, the fixed-time Fourier phase, corrected numeric values and the strict non-transferability to the original compact packet. Maintain the exact matched Einstein–Maxwell+same-solid residual zero. Do not claim v15.1197's first numerical value as valid or that a finite-arm causal experiment has been completed.
