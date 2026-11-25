# Cone Derivation Ledger v15.1450 — Actual 3+1 ADM constraint reconstruction for nonlinear H² sigma Cauchy data, and the periodic zero-mode obstruction

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Classification:** [EXACT leading-order geometry] 3+1 Einstein Hamiltonian and momentum constraints demand nontrivial metric and homogeneous background for any periodic positive-energy sigma field; [N PASS] solved *all nonzero spatial Fourier modes* for the conformal metric potential and trace-free longitudinal extrinsic curvature sourced by positive H² sigma stress, with constraint residuals at roundoff; [EXACT NEGATIVE] a strictly static flat periodic torus with zero homogeneous expansion cannot accommodate nonzero positive mean rho at this perturbative order; [OPEN] exact nonlinear ADM constraints, consistent growing FLRW/TT metric evolution, full C F B metric variations, EFT cutoff, physically fixed quarter coupling. Strict additive; no frozen Lane A/Audit/Sandbox assets changed. Parent Audit Round 638 (ledger v15.1423) independently reexecuted Gravity v15.1419–1422 with no bugs. Parent full Weyl characteristic v15.1420 remains a local fixed-background result.

## Gate 1369 — real 3+1 nonlinear target sigma initial data and ADM stress

Set 8πG=κ (chosen illustrative κ=.003), normalized H² sigma kinetic factor f*r=1. On a 3D torus of coordinate length 2π per spatial axis use real initial data

`u=.16 sin x, v=.13 sin(2y+.3), u_t=.10 sin(2x), v_t=.09 sin(4y+.6)`.

These are smooth spatially periodic data for two real *nonlinearly curved-target* fields, not assertions that each is an exact future free sigma wave. The target metric is `G_AB=δ_AB−phi_A phi_B/(1+u²+v²)`. Their positive normal energy density and ADM momentum density in the leading flat background are

`rho=½ G_AB(phi)[phi_t^A phi_t^B + Σ_i ∂_i phi^A ∂_i phi^B]`,
`j_i=−G_AB(phi)phi_t^A∂_i phi^B`.

The spatial mean j_i vanishes (to floating precision) by the chosen paired harmonics. The mean rho is strictly **positive**: ≈.02766700549338619 on N24. The scalar fields therefore source the Einstein constraints already at O(κ rho), even when their proposed Weyl–Maxwell operator has not yet excited EM.

## Gate 1370 — solve nonzero Hamiltonian and momentum constraints

In ADM with metric signature −+++, Hamiltonian and momentum constraints are

`³R+K²−K_ij K^ij = 2κ rho`,
`D_j(K^j_i−δ^j_i K)=κ j_i`.

Choose the controlled small-field spatial metric `γ_ij=(1+2ψ)δ_ij+O(ψ²)`, and decompose extrinsic curvature `K_ij=−H γ_ij+A_ij`, with A tracefree and `A_ij=(LW)_ij=∂iWj+∂jWi−(2/3)δij ∂·W` to leading order. Then

`−4 ∆ψ+6H²=2κ rho+O(κ²)`,
`∆W_i+(1/3)∂i∂·W=κ j_i+O(κ²)`.

Spatial averaging imposes the **zero-mode Friedmann constraint**

`6H²=2κ mean(rho)`, i.e. `H²=κ mean(rho)/3=(8πG/3)mean(rho)`.

For nonzero spatial wavevectors, solve

`ψhat(k)=κ deltahat(rho)(k)/(2|k|²)`.

Decompose momentum Fourier coefficients into longitudinal and transverse pieces relative to k. Solve

`What_i(k)=−κ [jhat_T,i(k)+(3/4)jhat_L,i(k)]/|k|²`.

These explicitly satisfy both elliptic nonzero Fourier constraints, without inventing a gravitational source or setting a nonzero Fourier zero mode to a finite 1/k². A strictly flat, static torus (H=0) would require mean rho=0 at this order and is inconsistent with these positive sigma data. The homogeneous H option is a *necessary constraint ingredient*; it is not an exact globally evolved Einstein solution, which additionally requires lapse/shift gauge, higher constraints, TT gravitational initial data, and time evolution.

**Actually executed local reproducible code** `/mnt/data/cone_gate/k4_full3d_adm_sigma_constraints.py` (Python NumPy FFT) checked N12/16/24; new additive GitHub equivalent `research-notes/k4_curved_h2_adm_3d_constraints_v15_1450.py` SHA **896090608a6e4086c3c90a2ac7a87b427825d886**, awaiting exact committed-byte Audit replay.

| N³ | mean rho | H required | nonzero Hamiltonian max err | momentum max err | max |ψ| |
|---:|---:|---:|---:|---:|---:|
| 12³ | 0.02766882759420178 | 0.00526011669017 | 8.13e−20 | 3.47e−18 | 4.17538e−6 |
| 16³ | 0.02766702996260673 | 0.00525994581366 | 8.13e−20 | 1.39e−17 | 3.95721e−6 |
| 24³ | 0.02766700549338619 | 0.00525994348766 | 1.22e−19 | 2.78e−17 | 4.08999e−6 |

The maximum |ψ| is a sample-grid extremum, not a monotonically converged quantity; mean density and H agree within 10^−4 relative between 12³ and 24³. The very small Fourier residuals are mainly algebraic solver identities and not a proof of exact nonlinear constraints. The periodic spatial topology makes a genuine distinction: a nonzero mean energy cannot be absorbed by a nonzero Fourier Poisson potential on a static flat background. The H² sigma stress source by itself does **not** introduce a G-free gravitational scale, since κ is a free input.

## Audit and next

**AUDIT:** independently rederive ³R≈−4∆ψ, ADM signs for Kij=−Hγij+Aij, mean Friedmann constraint, longitudinal (3/4) momentum Green function, sign of j_i, nonlinear H² positivity, zero mean momentum, and roundoff Fourier residuals; check spatial derivative aliasing and scale of omitted nonlinear terms. Also ensure the 3D *spatial slice* here is distinct from the earlier *2+1 spacetime* Weyl-vanishing statement v15.1421. The next v15.1452 gate evaluates the full nonlinear Hamiltonian residual, demonstrating O(κ²) rather than claiming these are exact full Einstein data.

**NEXT:** solve the nonlinear 3+1 Hamiltonian and momentum constraints simultaneously, including metric conformal factors and a homogeneous expanding background, then evolve a gauge-fixed metric while preserving Bianchi/ADM constraints. The Weyl–F–target-area interaction and its metric stress must be included only after a complete perturbative variation and EFT cutoff analysis. Exact q2=1/16 observability geometry still does not select κ or a physical EM–G coupling.
