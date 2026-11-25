# Cone Derivation Ledger v15.1420 — Complete 4D Weyl tensor retains a nonluminal local transverse Maxwell–H² characteristic sector

**Date:** 2026-11-24 Eastern / Nov 25 UTC. **Lane:** Gravity/Cone. **Parents:** v15.1381 full Weyl–F–H²-area EFT, v15.1416 actual nonlinear H² frozen-tidal Hamiltonian, v15.1417 reduced superluminal characteristic warning. **Status:** [D PASS] exact four-index Weyl tensor of linearized **4D vacuum TT curvature**, nonzero polarization-scalar principal mixing and characteristic split in a specified local frozen-background subblock; [NEGATIVE] the simplified truncation's off-Minkowski-cone branch is NOT automatically removed by adding the omitted Weyl components; [OPEN] consistent full dynamical Einstein–Maxwell–sigma principal-symbol/gauge constraints, EFT cutoff, causality and any quarter-grid-selected coupling. **Audit Round 637** at 24d458daf3ae3b84d5859522304b2e44b3b61db5 confirmed exactly committed v15.1403–1417, independently rederived the reduced warning, and found no bugs; also found historical v15.1403 ledger collision, restated canonically v15.1419. Strict additive.

## Gate 1362 — evaluate the ENTIRE vacuum TT Weyl, not a chosen component

Use 4D background Minkowski metric diag(-1,1,1,1), a small vacuum TT wave with h_xx=ε cos(t−z), h_yy=−ε cos(t−z), all other linear h components zero. The covariant Fourier carrier is kμ=(-1,0,0,1), null. Form every component of the exact first-order Riemann tensor by standard linearized second derivatives; check **all 16 Ricci components vanish**. Hence the whole linearized Riemann is Weyl. At the chosen wave phase cos(t−z)=1, with ε factored out, find

`C^(0y0y)=-1/2, C^(0yxy)=0, C^(xyxy)=0`.

These are not arbitrary frozen coefficients; they are extracted from one physically admissible **vacuum TT four-index curvature tensor**. Choose an H² target apex at u=v=0, a local background internal gradient ∂_y v=s (with ∂u=0), a perturbation δu(t,x) and a transverse physical Maxwell polarization δA_y(t,x). All derivatives and fields here are LOCAL eikonal data in a freely falling tetrad; the global background `v=s y` is not a finite-energy self-consistent nonlinear Einstein-sigma solution. The sigma background stress and metric constraints are neglected at this gate.

At the apex Ω_uv=1. The full chosen action term `L_int=−(g/2) C^μνρσ F_μν B_ρσ`, with `B=du∧dv`, contributes to this sector

`L_int=+g ε s A_(y,t) (δu)_t`.

The exact full C kernel `M^ν=C^μνρy p_μ p_ρ` for Fourier perturbation p=(-ω,q,0,0) is `M^ν=(0,0,−ω²/2,0)`. Therefore the mixing is in a *gauge-transverse* A_y polarization, not just a longitudinal gauge artifact.

## Gate 1363 — complete local two-field characteristic block

At the apex and in local orthonormal coordinates, the standard free quadratic Maxwell and canonical sigma kinetic terms read

`L_2=½[A_(y,t)²−A_(y,x)²+u_t²−u_x²]+g ε s A_(y,t) u_t`.

Its velocity Hessian and spatial-gradient matrix are

`K_t=[[1,z],[z,1]], K_x=I`, with `z=g ε s` **after canonical normalization**, i.e. g here includes the independently selected dimensionful EFT coefficient and sigma normalization. Thus the local dispersion polynomial is

`det[ω²K_t−q² I]=[ω²(1+z)−q²][ω²(1−z)−q²]`,

and the speeds are `c±=1/sqrt(1±z)`. The kinetic block is positive for |z|<1. At |z|=.10 its speeds are 0.953462589 and **1.054092553** relative to the local background light cone; at |z|=.25 they are 0.894427191 and **1.154700538**. At z=.01 the speed excess is only ~.5%. This shows the prior frozen-tidal warning persists in one fully Weyl-derived fixed-background physical polarization sector; it does NOT establish a globally hyperbolic physical solution or faster-than-light information, since the complete metric variation and constraints, omitted curvature couplings from the full higher-derivative action, and Wilsonian cutoff have NOT been incorporated.

In particular, retaining flat free kinetic terms while using a small nonzero background tidal tensor must be understood in a local inertial frame at one point. Coordinate perturbations h can be locally transformed away at that point, but the invariant curvature C remains, so the result is not based on assigning Minkowski metric globally alongside a finite vacuum curvature. The scalar background gradient and GW stress require gravitational backreaction for a globally valid configuration, and that can modify the completed principal symbol.

## Reproducer and Audit

Actually executed local exact SymPy `/mnt/data/cone_gate/k4_full_weyl_local_characteristics_v15_1420.py`: full Riemann/Ricci check, C component tests, full transverse mixing kernel, determinant factorization and exact characteristic speeds all PASS. **Additive committed source** `research-notes/k4_full_weyl_local_characteristics_v15_1420.py`, SHA **117fa7ade727852cf9380f43a8768a72d64a30ec**, mathematically equivalent and awaiting independent committed-byte replay.

**AUDIT:** reconstruct independent full vacuum Weyl tensor using a different method, confirm TT vacuum Ricci and sign/normalization of the 4-index C-F-B contraction, the gauge-transverse polarization and true principal EOM including all fields/gauge/metric constraints. Decide whether finite GW stress and metric fluctuations alter or constrain this fixed-background high-frequency branch. Check positivity threshold with canonical sigma f,r normalization and EFT validity. Do not present nonluminal phase/characteristic branches as demonstrated superluminal signalling, especially at frequencies above a derivative EFT cutoff.

**NEXT:** derive full covariant metric Euler–Lagrange variation including its curvature-dependence and scalar/Maxwell feedback; check whether higher derivative terms introduce additional EFT modes and whether a constrained order-reduced formulation has a well-posed causal initial value problem. If no completion is selected, keep v15.1416 as an illustrative reduction only.
