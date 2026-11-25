# Cone Derivation Ledger v15.1452 — Nonlinear Hamiltonian constraint remainder is second order in gravitational coupling

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Classification:** [D/N PASS] exact conformal nonlinear 3+1 Hamiltonian constraint evaluated on the *first-order* ADM H² sigma initial-data reconstruction from v15.1450 has residual O(κ²); numerical halving of κ reduces absolute residual almost exactly by factor 4; [EXACT NEGATIVE] leading initial data are not exact solutions to nonlinear Einstein constraints, and periodic mean positive matter requires nonzero homogeneous expansion already at leading order; [OPEN] full nonlinear conformal-constraint solver, momentum constraint beyond first order, complete 3+1 Einstein–Maxwell–Weyl–H² evolution and physical quarter coupling. κ=8πG remains a free input. Strict additive.

## Gate 1373 — evaluate nonlinear spatial scalar curvature and exact Hamiltonian source

Keep the leading v15.1450 positive H² sigma Cauchy fields and the solution ψ and flat tracefree Aij of the nonzero ADM Hamiltonian/momentum constraints. Instead of pretending `γij=(1+2ψ)δij` is exact, choose the nonlinear **conformal** spatial metric

`γij=exp(2ψ)δij`,

whose exact three-dimensional spatial Ricci scalar is

`³R=exp(−2ψ)[−4∆ψ−2|gradψ|²]`.

Define the extrinsic curvature `Kij=−H γij+exp(2ψ) Aij`, with Aij tracefree relative to flat δ; consequently `K=−3H` and `K²−KijK^ij=6H²−Aij Aij`. The nonlinear physical normal-frame sigma energy on that slice, with lapse normalized to one and prescribed canonical normal velocities, is

`rho_gamma=½ G_AB(phi)[phi_t^A phi_t^B+exp(−2ψ) δij ∂i phi^A∂j phi^B]`.

The **actual nonlinear Hamiltonian residual of these specific reconstructed fields** is

`R_H = exp(−2ψ)(−4∆ψ−2|gradψ|²)+6H²−Aij Aij−2κ rho_gamma`.

At first order ψ~κ, A~κ, 6H²~κ and the leading constraints are satisfied by construction. Thus the remaining terms are O(κ²) (curvature exponent/potential gradient, tracefree extrinsic shear squared, curved matter-gradient energy). This is a perturbative-order statement, not an assertion of a complete exact Einstein solution; the momentum constraint also needs nonlinear correction and this initial slice must be evolved with a lapse and shift.

## Gate 1374 — numeric quadratic scaling and no exact-solution overclaim

For N24³ spatial grid with the same smooth u,v/velocities as v15.1450, evaluate the complete nonlinear expression independently from the first-order solved ψ, Aij, H (recompute rather than transcribe residual). Actually executed `/mnt/data/cone_gate/k4_adm_nonlinear_residual.py`, Python NumPy FFT. Compare κ and successive halvings:

| κ=8πG | max absolute nonlinear Hamiltonian residual | max residual / (2κ max rho) | mean residual |
|---:|---:|---:|---:|
| .003 | 2.0881854524072534×10⁻9 | 7.54273349×10⁻6 | −7.89859091×10⁻10 |
| .0015 | 5.220458549769127×10⁻10 | 3.77136307×10⁻6 | −1.97464618×10⁻10 |
| .00075 | 1.3051140023030965×10⁻10 | 1.88568062×10⁻6 | −4.93661350×10⁻11 |

The absolute residual ratios upon halving κ are **4.000003893** and **4.000001947**, agreeing with quadratic perturbation. The relative residual falls by a factor ~2. The nonzero mean residual is itself O(κ²), and cannot be removed merely by modifying the zero Fourier coefficient of a periodic Poisson potential; the homogeneous expansion/background correction must be adjusted along with the nonlinear metric and stresses. The result is a **controlled first-order initial-data approximation** for small κ, not a fully constrained GR+Weyl+Maxwell+sigma Cauchy slice. The scalar stress is the curved H² kinetic stress only; at this order no complete curvature–F–B matter stress or gravitational wave backreaction is included.

**Additive GitHub reproducer:** `research-notes/k4_h2_nonlinear_adm_residual_v15_1452.py`, SHA **e9c17011d7c392cf32f3124781d79f870ab54bfc**. Same mathematical reconstruction as executed local file, independently authored; the exact committed-byte external Audit replay is pending. No frozen Lane A/Sandbox/Audit/Muse or previous certified objects touched.

**AUDIT:** independently check conformal ³R formula, tracefree A scaling in Kij, source rho_gamma, correct Hamiltonian residual, the fact that 6H² includes mean positive rho but A² shifts mean at second order, and reproducing quadratic halving. Verify no missing factor two in κ=8πG convention and no contamination from 2+1 spacetime Weyl-vanishing gate (the ADM initial surface is *three spatial dimensions* of a genuine 3+1 background).

**NEXT:** solve exact nonlinear conformal Einstein constraints by a Newton elliptic method with homogeneous H simultaneously updated to enforce integrated Hamiltonian equation, and solve nonlinear momentum constraints with mean-comoving gauge. Then evolve the H² sigma/EH/Maxwell constrained system with the action-derived full Weyl curvature operator, including EFT order-reduction to avoid treating uncontrolled higher derivatives as extra modes. Crucially compare against the **identical enlarged EFT comparator**: there is still no quarter-grid-selected coupling or G-free gravitational strength.
