# Cone Derivation Ledger v15.1417 — Positive reduced H² kinetic energy does not certify luminal causality: a frozen-tidal principal-symbol negative

**Date:** 2026-11-24 Eastern / UTC Nov 25. **Lane:** Gravity/Cone. **Classification:** [D exact] determinant and positivity criterion of the **curved H² nonlinear target** 1+1D coupled EM kinetic matrix from v15.1416, plus its locally linearized principal characteristic speeds about an internal spatial gradient; [NEGATIVE] at a nonzero gradient the deliberately frozen single-tensor-component interaction can exhibit a superluminal **phase/characteristic branch relative to the Minkowski light cone** even while M is positive and the discrete Hamiltonian energy is conserved; [IMPORTANT SCOPE] this is **not** a claim of signal acausality or instability of the complete covariant Weyl–F–H² effective field theory, whose other tensor components, metric constraints and EFT cutoff are omitted; [OPEN] full covariant characteristic determinant, cone-compatible gauge/constraint reduction, EFT Wilsonian completion, causal front, physical quarter selector. Additive only. Parents v15.1415 flat comparator and v15.1416 nonlinear H² coupled variational run. **Pre-ledger latest research script** 98f6042f19e9a2497acdf9705926d27f5ebb9247.

## Gate 1359 — exact kinetic determinant and positivity condition

Use the complete *curved target* reduced Lagrangian from v15.1416,

`L=½(A_t²−A_x²)+½ G_ab(phi)(phi_t^a phi_t^b−phi_x^a phi_x^b)+g A_t Omega_uv(phi)(u_t v_x−u_x v_t)`.

Write `D=1+u²+v²`, `G_ab=δ_ab−phi_a phi_b/D`, `Ω=1/sqrt D` and `z=(u_x,v_x)`. Its 3×3 symmetric velocity Hessian M is

`[[1,gΩ v_x,−gΩ u_x],[gΩ v_x,G_uu,G_uv],[−gΩ u_x,G_uv,G_vv]]`.

The **exact** algebraic determinant identity is

`det M=[1−g² |z|_G²]/D`,
`|z|_G²=G_uu u_x²+2G_uv u_x v_x+G_vv v_x²`.

The G block is strictly positive for finite real (u,v). By its Schur complement, the full three-field M is positive definite if and only if

`g²|z|_G² < 1`.

So the numerical min-eigenvalue test of v15.1416 is an actual sufficient *and* necessary positive local kinetic threshold for this reduced action. It is not a proof of the full tensor-coupled theory's constraint consistency, characteristic hyperbolicity or causal front.

## Gate 1360 — exact principal characteristics around a local internal gradient

At a local point with u=v=0 (thus G=I, Ω=1), choose an internal spatial-gradient background u_x=s, v_x=0 and vanishing background time derivatives, with A=0. This is a **local principal-symbol approximation**, not a claim that the global linear u=sx profile is a finite periodic exact solution of nonlinear H²+Einstein equations. Perturb only the transverse Maxwell A and other internal scalar v. Their quadratic kinetic Lagrangian in a frozen-gradient approximation contains

`L_2=½[A_t²+v_t²−A_x²−v_x²]−g s A_t v_t`.

The time-derivative Hessian is `M_2=[[1,−g s],[−g s,1]]`, with eigenvalues 1±g s; the spatial gradient block in this simplified model is I. Its principal Fourier determinant is

`det[ω² M_2−k² I]=(ω²(1−g s)−k²)(ω²(1+g s)−k²)`.

Therefore the two characteristic phase velocities in the local frozen-tidal reduction are

`c_±=1/sqrt(1±g s)`.

For gs=.10 they are approximately .953462589 and **1.054092553**, and for gs=.25 they are .894427191 and **1.154700538**. The local kinetic matrix is still positive for |gs|<1 and both phase speeds are real, so it is possible for a numerically healthy conservative Hamiltonian to allow a branch faster than c=1 **inside this truncated local model**. No physical photon FTL or signal-causality violation of a completed gravitational theory is inferred: external/background source, complete Weyl contraction, higher-order operators and high-frequency EFT cutoff can change interpretation. This is a **mandatory check** before proposing a physical detector.

## Gate 1361 — exact script and review boundary

**Actually executed local SymPy** `/mnt/data/cone_gate/k4_curved_h2_toy_kinetic_characteristics_v15_1417.py` calculated full determinant using exact target G and Omega, symmetrized quadratic principal matrix, both factorized characteristics, and numeric examples, all assertions PASS after a non-substantive initial SymPy structural-expression equality was replaced by `simplify(lhs-rhs)==0` (the mathematical identity was correct). **Additive canonical GitHub equivalent** `research-notes/k4_curved_h2_toy_kinetic_characteristics_v15_1417.py`, SHA **98f6042f19e9a2497acdf9705926d27f5ebb9247**; exact-byte external Audit replay pending.

**AUDIT:** independently verify full determinant/Schur positivity, local principal linearization including the coefficient −g s and omitted background-EOM terms' lower derivative order, both characteristic velocities, and whether fuller gauge/tidal components remove or modify the off-lightcone branch. The first physical completeness gate is a full variational metric+Weyl+sigma+Maxwell model with a sound local constraint and EFT-characteristic analysis. Keep the positive coupled energy result from v15.1416 but do NOT claim it proves Lorentz causality.

**NEXT:** either construct a gauge- and tensor-consistent action reduction retaining *all curvature-required components* and derive its characteristic matrix, or report obstruction and park the frozen-tidal toy as a useful reduced energy accounting diagnostic. Separately pursue an independent physical representation operator/coupling that survives the 1/4 radius reparameterization no-go, or retain no-new-force verdict.
