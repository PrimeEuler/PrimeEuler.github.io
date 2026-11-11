# Cone Derivation Ledger v15.711 — Gravity: source-first K4 scalar ADM lapse/shift Hessian and exact constraint response

**Date:** 2026-11-11, US Eastern. **Parents:** v14.928 K4 Einstein–Hilbert+elastic-solid action; v14.935 archived full SVT return, especially eh_scalar.py, matter_sector.py and assemble.py; v15.708 conserved Fourier common-source comparator; v15.709 metric scalar electric tidal tensor; v15.710 sourced K4 vector shift and pole response. **Audit:** Round 544/v15.707 independently confirmed v15.701–706; v15.708–710 still pending external verification. **Status:** [D] sourced scalar lapse/shift *constraint block* reconstructed from original frozen K4 action, its Hessian and Schur-complement source response; [N] full inhomogeneous scalar propagator/physical tidal transfer not yet solved; [O] covariantly conserved physical FLRW source and scalar field/metric eigenvectors. **Immediately prewrite HEAD:** a6ad5cfafb4fdc3c8b213cc4c9f0bd5b92a6a680. Target ledger path absent, collision check clean. Additive-only; protected Suzuki/far-tail objects untouched.

## Gate 301 — isolate the original scalar auxiliary block, not a guessed oscillator

Take the source-free frozen v14.935 action with the scalar spatial gauge E=0, scalar lapse Phi and scalar longitudinal shift B. To extract the Hessian in (Phi,B), set *propagating* perturbations psi and solid longitudinal P and their derivatives to zero **only when taking the quadratic auxiliary block**; the resulting Hessian is the same block appearing in the full quadratic action. This does not eliminate or freeze psi,P for subsequent dynamics.

The homogeneous spatial metric is h_ij=a² delta_ij, the ADM lapse satisfies

**N²=1+2 epsilon Phi+epsilon² B_z²**, and the covariant longitudinal shift is N_z=a epsilon B_z. The relevant extrinsic-curvature expression yields, at second order in epsilon,

**L_EH,aux^(2) = [a/(2 kappa)](-9 adot² Phi²+3 adot² B_z²-4 adot Phi B_zz)**.

For the frozen K4 solid with phi^I=x^I, its B^(IJ) eigenvalues in this restricted block are proportional to **(1,1,R)**, with

**R=(1+2 epsilon Phi)/(1+2 epsilon Phi+epsilon² B_z²)**.

The elastic anisotropy J=tr(B²)/(tr B)²-1/3 starts at fourth order in this auxiliary-only perturbation, so the quadratic matter block is

**L_m,aux^(2)=a C(Phi²/2-B_z²/6)**.

This independence from eta is only an **auxiliary Hessian** fact. The full scalar elastic action, its couplings to solid P and metric psi and its dispersion absolutely DO depend on eta.

After the original archive's cos-Fourier substitutions **B_z=-k B, B_zz=-k² B**, the exact Hessian H=(partial² L_aux/partial(Phi,B)²) is

**H = [[a(kappa C-9 adot²)/kappa, 2 a adot k²/kappa], [2 a adot k²/kappa, a k²(9 adot²-kappa C)/(3 kappa)]]**.

This was obtained by direct symbolic expansion of the original EH ADM and solid determinant formulas. It is not a generic freely chosen constraint matrix.

## Gate 302 — explicit K4 source-induced lapse and shift

At the coasting K4 normalization tau=1, **kappa=C=1, a=adot=1/sqrt(3)**, the scalar auxiliary Hessian becomes

**H_K4 = [[-2/sqrt(3), 2 k²/3],[2 k²/3,2 k²/(3 sqrt(3))]]**,

with exact determinant

**det H_K4= -4 k²(1+k²)/9**.

It is invertible for **k>0**; the k=0 homogeneous constraint is singular and is excluded rather than assigned an artificial sourced solution.

Introduce formal scalar source coefficients **J=(J_Phi,J_B)^T** by adding **J_Phi Phi+J_B B** to the *unreduced* quadratic action. For arbitrary other scalar field perturbations q, the unsourced auxiliary constraint has the form **H q_aux + d(q,qdot)=0**. The sourced shift relative to the unsourced solution is exactly

**delta q_aux = -H_K4^(-1) J**,

giving

**delta Phi=(sqrt(3) J_Phi-3 J_B)/[2(1+k²)]**,

**delta B=-3(sqrt(3)J_B+k² J_Phi)/[2 k²(1+k²)]**.

These expressions explicitly show how source terms alter lapse and shift before eliminating them; no scalar propagating-mode normalization has been assumed. The source components are formal ADM coefficients, and their conversion from covariant physical stress must be derived using the background metric and source action, respecting the cos-mode projection normalization and covariant conservation.

## Gate 303 — scalar source contact and what it cannot determine

The exact Schur-complement source contribution to the constraint-eliminated Lagrangian is

**delta L_red = - J^T H^(-1) d - (1/2) J^T H^(-1) J**,

where d(q,qdot) denotes the original action's mixed auxiliary-to-propagating-source vector. The pure source contact on the tau=1 K4 slice is

**delta L_contact = -[3 sqrt(3) J_B²+6 k² J_B J_Phi-sqrt(3) k² J_Phi²]/[4 k²(1+k²)]**.

Because H is indefinite, this contact form need not be positive. The missing **d(q,qdot)** and the already-known reduced scalar propagator are both needed to convert the sourced constraint into a scalar mode pole residue, an actual Phi/Psi response, and the electric tidal matrix of v15.709. Merely calculating H^(-1) does **not** complete that calculation. In particular the source term must be introduced before eliminating lapse/shift, as in v15.710.

**Result:** the second K4 source-first constraint calculation has a complete exact auxiliary response for k>0, advancing beyond the previous purely kinematic stress projectors. No new parameter-free, experimentally calibrated gravitational observable is claimed.

## Gate 304 — required next physical calculation

To close the single-common-source program, take the original v14.935 scalar fields (psi,P), restore all mixed terms d(q,qdot) of the unreduced scalar quadratic action, and compute **-J^T H^(-1) d** with a full *covariantly conserved* external stress perturbation around coasting FLRW. Then derive the sourced scalar Green function and reconstruct both gauge-invariant Newtonian potentials or the full local Fermi R_(0i0j). Alongside the sourced v15.710 vector pole and the v14.928 tensor source, compare three detector-pole locations, residues and angular nulls separately. Any ratio of pole locations remains the conventional relativistic-elasticity identity v15.706 unless a genuinely distinct sourced prediction survives.

**Reproducibility:** research-notes/k4_sourced_scalar_aux_hessian_v15_711.py, additive commit a6ad5cfafb4fdc3c8b213cc4c9f0bd5b92a6a680. Independently executed locally to PASS, including complete restricted EH+solid expansion, exact Hessian, zero quadratic contribution from Jsolid in the auxiliary-only block, on-shell determinant, sourced shift and contact. All prior certified scripts intact; no images generated.

**HANDOFF:** external audit/gravity/sandbox: verify the ADM sign and cos-Fourier B_z/B_zz conventions against v14.935 original sources, independently reproduce H and source contact, check the k=0 degeneracy, and reject any promotion of the auxiliary source solution to a complete K4 scalar metric-wave observable. Follow the existing additive-ledger protocol and do not interfere with Suzuki production.
