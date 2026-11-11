# Cone Derivation Ledger v15.709 — Gravity: local gauge-invariant SVT electric tidal response and missing sourced metric transfer

**Date:** 2026-11-11 US Eastern. **Parents:** v14.935 full K4 SVT source-free quadratic return and payloads/k4_full_svt_v14_935/NOTE.md, vector_sector.py and scalar_statespace.py; v15.703 standard GR rank-two tidal matrix; v15.705 pure-TT K4 eigenvalue null; v15.706 homogeneous three-sector pole-gap ratio 3; v15.708 conserved one-source stress projectors and gauge-invariant linear source. **Audit:** external Round 544/v15.707 confirmed v15.701–706. **Status:** [D] exact local flat linearized Riemann tidal tensor and full infinitesimal-diffeomorphism check; [D] scalar/vector metric-potential dependence; [N] no unique three-sector observable from frequencies or source projectors alone; [O] sourced K4 lapse/shift constraints and proper-FLRW Fermi transfer. **Immediately prewrite HEAD:** 5e2e0d3aa83ba4e482c6b0b16271fd588451acc8; target v15.709 path absent. Additive only; protected Suzuki/far-tail untouched.

## Gate 293 — compute the actual linearized detector tidal tensor, not merely SO(2) stress projectors

Use a local approximately inertial detector frame, Fourier dependence exp(-i omega t+i k z), and the metric perturbation components

**h_00=-2 Phi; h_ij(scalar)=-2 Psi delta_ij;**

**h_xx(T)=P, h_yy(T)=-P, h_xy(T)=C;**

**h_0x=V_x, h_0y=V_y, h_xz=H_x, h_yz=H_y**,

with other metric components zero in the stated scalar Newtonian-gauge/vector decomposition. These are generic metric amplitudes; they are not the canonical variables P,psi,f of the v14.935 ADM derivation and must not be conflated.

From

**R_(0i0j)=(1/2)(partial_0 partial_i h_0j+partial_j partial_0 h_i0-partial_0² h_ij-partial_i partial_j h_00)**

the electric tidal matrix E_ij=R_(0i0j) is exactly

**E_xx=-omega² Psi+(omega²/2)P**,

**E_yy=-omega² Psi-(omega²/2)P**,

**E_xy=(omega²/2)C**,

**E_xz=(omega/2)(k V_x+omega H_x)**,

**E_yz=(omega/2)(k V_y+omega H_y)**,

**E_zz=-omega² Psi-k² Phi**.

Every entry is invariant under an arbitrary **linearized** diffeomorphism delta h_(mu nu)=partial_mu xi_nu+partial_nu xi_mu on a flat background. An exact symbolic check with arbitrary xi_0,xi_x,xi_y,xi_z confirmed delta R_(0i0j)=0. This is standard gravitational perturbation theory, not a novel Cone result.

## Gate 294 — scalar amplitude-normalized tidal shape requires gravitational slip

If only scalar metric perturbations are present, the transverse tidal eigenvalues are both

**lambda_perp=-omega² Psi**

and the longitudinal eigenvalue is

**lambda_parallel=-omega² Psi-k² Phi**.

When Psi nonzero, the dimensionless ratio is

**lambda_parallel/lambda_perp=1+(k²/omega²)(Phi/Psi)**.

Consequently the scalar *dispersion* omega_S(k) alone does not determine a unique scalar tidal-shape ratio: the ratio additionally needs the physical potential transfer **Phi/Psi**, set by source-free eigenvector constraints for a specified mode or by sourced field equations and boundary conditions. For example Phi=0 and Phi=Psi give different tidal ratios at the same (omega,k). Neither value is asserted to solve the K4 constraints; these are independent kinematic witnesses that the dispersion relation is insufficient data.

For a full expanding K4 background the proper-frame tidal tensor also contains background terms, and the scalar gauge-invariant combinations must be defined with cosmological perturbation conventions. This gate proves only the local flat-background algebraic dependency.

## Gate 295 — vector physical tide depends on a gauge-invariant shift-plus-shear combination

The xz/yz vector tidal entries depend on

**k V_a + omega H_a** for a=x,y.

The individual vector shift and shear amplitudes depend on the gauge convention, but their displayed combination (multiplied by omega/2) is directly the gauge-invariant electric curvature in the local Fourier model. In particular **H_a=-(k/omega)V_a** makes the vector tidal curvature vanish even while both metric components are nonzero; this cancellation is a gauge/curvature statement, not proof that an independently sourced K4 vector mode can be gauged away or is physically absent.

The archived v14.935 vector_sector.py uses the vector spatial gauge F_i=0 and constrains the shift B_v in terms of a transverse solid displacement. Its source-free reduced-action frequency by itself does not supply the response to the *external conserved T^(mu nu)* of v15.708. The corresponding amplitude and proper tidal transfer must be derived from the sourced constraints, not read off from the sound-speed coefficient.

## Gate 296 — precise unresolved sourced ADM handoff

The v14.935 payload establishes a full coupled *homogeneous* SVT quadratic model and its stability window. Inspection of NOTE.md, scalar_statespace.py, vector_sector.py, final_checks.py confirms the published return is a source-free dispersion/stability derivation with constraints eliminated before source insertion. Therefore an external source added after reduction is not guaranteed equivalent to adding it before lapse/shift elimination.

The correct next calculation is to introduce a **covariantly conserved** source action in the original frozen Einstein–Hilbert+solid model, vary with respect to lapse, shift, spatial metric and solid fields, and **then** eliminate the sourced nondynamical constraints. It must return explicit gauge-invariant metric E_ij transfer functions, along with source overlaps and residues for tensor, vector and scalar poles. The local Fourier source v15.708 is an algebraic comparator, not yet a globally physical source on coasting FLRW.

**Conclusion:** exact curvature components and gauge invariance [D]; three-frequency ratio 3 remains a valid algebraic same-k local K4 identity, but its visibility in a gauge-invariant three-channel gravitational detector is unestablished [O]. Avoid claiming a measured amplitude ratio or interpreting the *scalar stress projector* as the complete scalar gravitational transfer.

**Reproducibility:** research-notes/k4_gauge_invariant_tidal_svt_v15_709.py, additive commit 5e2e0d3aa83ba4e482c6b0b16271fd588451acc8. Locally executed PASS for full curvature formula, linearized gauge invariance for arbitrary xi_mu, vector cancellation and two inequivalent scalar potential ratios at same dispersion. No imagegen; no edits to frozen scripts.

**HANDOFF:** independent audit/gravity and optional K4 sandbox: check Riemann signs, Fourier conventions, scalar/vector gauge-invariant combinations, and the distinction between homogeneous ADM eigenfrequencies and inhomogeneous sourced detector transfer. Independently inspect v14.935 payload for whether it already contains the needed source coupling (the inspected return does not explicitly include an external T source). Do not replace a physical K4 source computation with a phenomenological arbitrary slip Phi/Psi.

**NEXT:** attempt a limited but actual source-first model by deriving how a conserved stress modifies the v14.935 ADM vector shift constraint, using the original unreduced vector quadratic action in vector_sector.py; find the exact source-dependent shift and whether its residue is normalized without adding free Couplings. Treat the result as an intermediate, not a full three-sector source or new gravitational observable.
