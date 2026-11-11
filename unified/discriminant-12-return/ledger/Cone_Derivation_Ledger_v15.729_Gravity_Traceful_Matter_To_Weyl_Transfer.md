# Cone Derivation Ledger v15.729 — Gravity: pressure-corrected K4 source-to-Bardeen and electric-Weyl transfer

**Date:** 2026-11-11 US Eastern. **Parents:** original K4 EH+elastic-solid action v14.928/935, source-first Hessian v15.711/712, on-shell sourced scalar P equation v15.713, tracefree-source metric transfer v15.719/720, physical canonical scalar source v15.727, correct traceful Ward and P forcing v15.728. **Classification:** [D] exact full traceful external-stress scalar-to-gauge-invariant-metric transfer in frozen background; [D] corrected physical Weyl curvature with isotropic pressure; [N] earlier tracefree-only formulas cannot be reused for generic physical matter without modification; [O] explicit localized wavepacket histories and detector transfer. **Immediately prewrite live HEAD:** 1d2eb4fbdc7e50f390669ba67a81bfba694bb224; target ledger absent. All changes additive; frozen Suzuki untouched.

## Gate 360 — direct matter trace changes the lapse Ward but not the auxiliary Hessian

Use the original source-free K4 scalar Einstein–Hilbert/solid quadratic action's lapse/shift Hessian from v15.711, on the exact coasting normalization a=tau/sqrt(3), k>0:

**H=[[-2tau/sqrt(3), 2tau k²/3],[2tau k²/3, 2tau k²/(3sqrt(3))]]**,

**det H=-4tau² k²(1+k²)/9**.

Source the original action before eliminating lapse/shift by **J_Phi Phi+J_B B+J_psi psi**, where the last term represents the physical spatial stress trace absent in the v15.717 tracefree model. The added J_psi psi term does not change the lapse/shift algebraic Hessian or their direct source correction. It does change the psi Euler equation, yielding the corrected FLRW conservation identity **tau J_Phi_dot+sqrt(3) J_B+J_psi=0** certified at v15.728.

## Gate 361 — exact traceful Bardeen potential transfer

The original E=0 gauge defines

**Phi_N=Phi+partial_tau(a B)**,

**Psi_N=psi-(a_dot/a)aB**.

Solve the full algebraic lapse/shift constraints from the original K4 action, keeping an arbitrary physical solid displacement **P(tau)**, arbitrary metric gauge scalar psi(tau), and the three physical source coefficients. Exact gauge cancellation and the pressure-corrected Ward relation yield

**Phi_N=[tau²P_ddot+2tau P_dot]/[3(1+k²)] +sqrt(3)(J_Phi+J_psi)/[2tau(1+k²)] -3 J_B_dot/[2k²(1+k²)]**,

**Psi_N=[k²P-tau P_dot]/[3(1+k²)] +sqrt(3)J_Phi/[2tau(1+k²)] +3J_B/[2k²tau(1+k²)]**.

The **new** traceful contribution relative to v15.720 at a fixed P, J_Phi and J_B is exactly

**Delta Phi_N= sqrt(3) J_psi/[2tau(1+k²)]**,

**Delta Psi_N=0**.

P itself also changes because its forcing now contains J_psi as derived in v15.728. Consequently the complete physical matter response is **not** obtained just by adding a constant lapse shift to an old tracefree particular solution: both the dynamical source and the direct metric contact change.

## Gate 362 — corrected gauge-invariant electric Weyl transfer

FLRW is conformally flat, and its linear Weyl perturbation is gauge invariant. For any scalar Fourier mode with comoving k, in a local orthonormal observer's frame,

**E^Weyl_(ij)=W(tau)[khat_i khat_j-delta_ij/3]**,

**W(tau)=k²[Phi_N(tau)+Psi_N(tau)]/[2a(tau)²]**.

The tracefree spatial rank-two STF norm yields

**E^Weyl_(ij)E^Weyl_(ij)=(2/3)W²**,

independent of the physical source. This is the same *ordinary three-dimensional STF dyad norm* identified in the canonical matter stress at v15.727. It does not fix the amplitude W. Use the pressure-corrected sourced P equation

**P_ddot+3P_dot/tau+[8eta(1+k²)-3k²]P/(3tau²)
 = 3sqrt(3)J_psi/(2k²tau³)-9(tau J_B_dot+J_B)/(2k⁴tau³)**

to eliminate P_ddot and obtain an on-shell scalar Weyl transfer involving P,P_dot,J_Phi,J_B,J_B_dot,J_psi. A retarded Green function for P follows from v15.714 with the *new full forcing*.

The formulas are conditional on the canonical spectator's stress evaluated on the fixed K4 background (stress O(epsilon²)); they are not a unique observed gravitational constant. The matter's positive local energy and wavepacket localization do not imply a universal measurable T/V/S tidal amplitude ratio.

## Gate 363 — precise audit controls

The additive reproducer reconstructs the source auxiliary lapse/shift corrections by an exact 2x2 inverse, applies the pressure-corrected Ward identity, and verifies the explicit pressure contribution and gauge-invariant Weyl STF norm using symbolic algebra. It also substitutes the physical sourced P equation and checks the special J_psi=0 limit reproduces the earlier v15.720 source-to-Weyl transfer.

**Reproducer:** research-notes/k4_traceful_scalar_weyl_v15_729.py, commit 1d2eb4fbdc7e50f390669ba67a81bfba694bb224; locally tested PASS. No edits to historical certified objects or figures.

**HANDOFF:** external audit/gravity/sandbox should verify the +--- metric variation signs, opposite Fourier phase pairing, the source-corrected Ward and direct J_psi source, source-induced lapse/shift inversion and full scalar Bardeen transfer independently against archived v14.935. Distinguish the source's physical stress trace from the longitudinal solid displacement P and the auxiliary metric variable psi.

**NEXT:** insert an **actual on-shell canonical matter configuration** (initially exact nonparallel two-wave mode, then compact wavepackets) into these pressure-corrected sourced equations and obtain a reproducible nonzero electric-Weyl curvature response. Also compute which T/V source projectors remain nonzero and why a spherically symmetric positive-energy source could be SVT-dark in the vector/tensor channels despite a local 2/3 norm.
