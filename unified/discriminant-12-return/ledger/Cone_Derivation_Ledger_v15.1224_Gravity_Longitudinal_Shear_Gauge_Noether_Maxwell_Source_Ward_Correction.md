# Cone Derivation Ledger v15.1224 — Longitudinal shear Noether identity and Maxwell momentum Ward: correction to v15.1222's missing-equation diagnosis

**Date:** 2026-11-19 Eastern. **Track:** Gravity/Cone. **Status:** [D] longitudinal scalar-gauge transformation and its exact Noether identity for the frozen Einstein–Hilbert+K4-solid field content; [D] independently derived linear Maxwell longitudinal momentum-conservation equation on spatially-flat FLRW, including the a^5 factor, and its exact source identity in archived ADM metric variables; [CORRECTION] v15.1222's assertion that fixing E=0 necessarily discarded an *independent* sourced longitudinal-shear field equation is unsupported and generally false on a fully conserved source solution; [O] the v15.1222 isotropic electric-Riemann/Einstein-trace discrepancy remains and requires a single physically normalized Maxwell source dictionary, full source-and-initial-data consistency and independent scrutiny of the derived Bardeen transfer; [N] no quarter-grid gravitational or G-free observable. **Immediately prewrite live HEAD:** dcb62d4cebdeec796a1ead651ecbf002ff630949. Target v15.1224 verified unused. Additive-only; Suzuki/Lane A, Audit, Sandbox/Muse, older certified K4 and error-containing historical ledgers preserved.

## Gate 1163 — original scalar geometry and longitudinal diffeomorphism
The *actual archived v14.935 metric and solid field ansatz*, in its signature (+---), has
**g_(0z)=−a ∂z B, g_(zz)=−a²(1−2ψ−2∂z²E), φ^z=z+∂z P**.
For an infinitesimal **passive** longitudinal coordinate transformation `ξ^z=∂z λ(t,z)`, `ξ^0=0`, the linearized field transformations (background scalar field φ^z=z, and `δg=−Lie_ξ g`) are exactly:
**δE=+λ, δP=−λ, δB=−a ∂t λ, δψ=δΦ=0**.
Consequently the combinations **P+E** and **B+a ∂tE** are invariant. The same transformations apply at Fourier k>0, with appropriate real sine/cos quadrature. The sign and factor a are fixed by the archived `g_(0z)=-a B_z`, not invented as a generic gauge slogan.

## Gate 1164 — longitudinal shear Euler equation is Noether-dependent
Let `mathcal E_q=δS/δq` denote the Euler–Lagrange functional derivative of the **complete** linearized source+K4 action, with integration by parts and compatible boundary conditions. Gauge invariance for arbitrary λ gives
**0=δS=∫λ [mathcal E_E−mathcal E_P+∂t(a mathcal E_B)]**,
therefore
**mathcal E_E−mathcal E_P+∂t(a mathcal E_B)=0**.
In particular, if both the *solid displacement* equation and the *longitudinal momentum/shift* equation hold for a physically conserved source, the E equation follows. Setting E=0 **after** fixing the spatial-coordinate gauge does not intrinsically omit an independent physical constraint or a second scalar propagating degree of freedom.

This does **not** establish that every expression in the archived v15.728–729 sourced reduction is correct for the Maxwell source. One still must check that their source normalization is consistent with the uneliminated action and that the chosen initial metric/solid data satisfy all constraints. However, **simply adding the E equation cannot in general fix v15.1222's k-dependent isotropic Ricci mismatch** if its P and B equations and the source are already mutually consistent: the E equation is then redundant. The earlier proposed diagnosis is amended additively rather than silently erased.

The reproducer checks the identity directly on a general quadratic gauge-invariant model **L=(K/2)(∂t(P+E))²−(C/2)(P+E)²+(μ/2)(B+a∂tE)²+(P+E)(B+a∂tE)** with arbitrary functions K(t),C(t),μ(t),a(t). It does *not* substitute that illustrative L for the actual K4 action: the general Noether relation is derived from the actual field transformation and diff invariance, and the model supplies an independent symbolic test.

## Gate 1165 — exact Maxwell longitudinal momentum source identity, including all FLRW powers
The source coupling at first metric order in the archived (+---) variable convention is **S_src=(1/2)∫a³ T^(μν)δg_(μν)**, up to one globally consistent stress sign convention (reversing the stress convention multiplies both sources and identities by −1). Focusing on the scalar shift/shear terms,
**L_src = −a⁴ T^(0z)∂z B + a⁵ T^(zz)∂z²E + [lapse,ψ terms]**.
For a compatible real cos/sin Fourier pair, choose metric amplitudes `B(t) cos(kz), E(t) cos(kz)`, source components **T^(0z)=m(t) sin(kz), T^(zz)=q(t) cos(kz)**, and average over the mode. Then, with a common factor 1/2,
**J_B=(k a⁴/2)m, J_E=−(k² a⁵/2)q**.
The **independently derived Maxwell/other conserved test-stress longitudinal covariant conservation equation** on spatially-flat FLRW is
**∂t T^(0z)+5H T^(0z)+∂z T^(zz)=0**.
In these Fourier quadratures this reads
**∂t(a⁵ m)−k a⁵ q=0**,
and therefore
**J_E+∂t(a J_B)=(k/2)[∂t(a⁵m)−k a⁵q]=0**.
This is exactly the **source** contribution to the gravitational Noether relation for `J_P=0` (Maxwell couples to the metric, not directly to the K4 solid displacement). The spatial-shear Maxwell source itself is **nonzero** whenever Tzz and k are nonzero; the point is not its absence but its dependence on the momentum source via conservation. The factor a^5 is essential: `a^4` or `a^3` in the conserved momentum balance would produce an artificial violation.

This calculation establishes the *gauge identity* and is robust to the material equation of state. It does **not**, alone, resolve the remaining **lapse/pressure source dictionary J_Phi,J_psi** (including (+---) versus (−+++) sign conversion), nor the v15.1222 Ricci trace conflict.

## Gate 1166 — corrected status and next falsification
The v15.1222 **algebraic result** from its declared reduced equations,
**A_iso^(reduced)(tau=1)=sqrt3 J(k²−4)/[2(1+k²)]**,
remains a legitimate algebraic diagnostic. But its interpretation **as proof of a missing independent E field equation** is overturned by this Noether calculation. A curvature-source mismatch can arise from inconsistent definitions of T^(μν), J_B Fourier quadratures, the sign of gravitational metric variation, unreconciled curvature convention, or from initial data not satisfying all field constraints. A genuine defect in the archived reduction would require direct byte-original action variation and source-first/field-identity check, not an argument based solely on the E gauge choice. No quarter/1/16 sector enters the algebra.

**Reproducer:** `research-notes/k4_scalar_longitudinal_gauge_ward_v15_1224.py`, additive SHA **dcb62d4cebdeec796a1ead651ecbf002ff630949**. Executed in local Python/SymPy environment, exit 0: exact gauge transformations/invariant blocks, Noether Euler identity, Maxwell J_E+(aJ_B)' identity and a^5 covariant momentum conservation. Independent post-commit byte-execution Audit pending.

**AUDIT HANDOFF:** verify passive diffeomorphism signs in the original (+---) g0z and gzz, including scalar field P; derive the Noether identity from the *full archived pre-E=0 EH+solid action* rather than relying only on general diffeo invariance; reconstruct Maxwell source J_E and J_B from an actual conserved stress with the same cosine/sine Fourier convention; determine exactly why the E-fixed v15.729 scalar full R00 trace disagrees with the v15.1221 Einstein active-density result at the compact Maxwell initial slice. Check whether prescribed P(1)=Pdot(1)=0 and nonzero matter source satisfy *all* Hamiltonian/momentum and spatial equations in one initial-value setup. Preserve historical results; correct additively.

**NEXT:** perform the physically normalized complete (+---) Maxwell stress-to-`J_Phi,J_B,J_psi,J_E` map, including the explicit k→0 treatment, then re-evaluate Ricci trace before the compact finite-arm readout. The matched EH+same K4 solid+Maxwell theory still has identically zero Cone-minus-comparator residual without an independently selected quarter-grid physical coupling.
