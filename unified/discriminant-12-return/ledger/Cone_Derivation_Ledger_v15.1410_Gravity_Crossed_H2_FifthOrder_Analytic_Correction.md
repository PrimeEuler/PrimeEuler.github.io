# Cone Derivation Ledger v15.1410 — Fifth-order analytic corrections to crossed null H² sigma waves

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [D PASS] explicitly solved the first nonzero nonlinear sigma Euler–Lagrange residual of the crossed-wave configuration v15.1409, raising residual order from 5 to 7 in amplitudes; [N PASS] amplitude-halving and exact symbolic tests; [D PASS] area-form remains nonzero with known order of new correction; [OPEN] retarded initial-condition-specific homogeneous pieces, full sigma+Weyl+Maxwell+Einstein coupled equations, finite localized waves, original quarter-grid carrier and independent force parameter. No G-free force established. **Checked live HEAD** before new ledger v15.1410 and v15.1411 slots: e041b21fdd99634ba985fc4be456ebc98594eda1, only new research scripts occupied those names. Audit v15.1406–1409 return not yet received on live HEAD.

## Gate 1344 — exact first nonlinear sigma source and correction

Use 2+1 flat local spacetime (-++) with null characteristics `A=t−x, B=t−y`. The H² normalized target metric and its Christoffel are `G_AB(phi)=δ_AB−phi_Aphi_B/(1+u²+v²)`, `Gamma^A_BC=−phi^A G_BC`. The exact chosen-sigma kinetic field equations are

`Box phi^A−phi^A G_BC ∂phi^B·∂phi^C=0`,

where `Box f(A,B)=−2∂A∂B f` and `∂f·∂g=−(f_A g_B+f_B g_A)`. For leading crossed waves `u0=a sin A, v0=b sin B`, the exact residuals, with `D=1+u0²+v0²`, are

`E_u[u0,v0]=−2a³b² sin² A sin B cos A cos B/D`,
`E_v[u0,v0]=−2a²b³ sin A sin² B cos A cos B/D`.

The complete fifth-order in amplitudes is canceled by the explicitly integrated particular solution

`δu5=−a³b² sin³ A sin² B/6`,
`δv5=−a²b³ sin² A sin³ B/6`,

because `Box δu5=+2a³b² sin² A sin B cos A cos B`, and the analogous equality for δv5. The remaining exact nonlinear residual after substituting `u=u0+δu5,v=v0+δv5` has **no total amplitude monomial of degree ≤6** and begins at seventh order (with a=b=ε, uncorrected ∼ε⁵ and corrected ∼ε⁷).

These are *periodic particular solutions*. Any homogeneous solution `f(A)+g(B)` may be added to the order-five wave equation; the simple particular solutions do not automatically enforce zero fifth-order correction at a chosen t=0 initial hypersurface. A retarded physical scattering experiment must impose its own Cauchy data, and then the corrected wave shapes can differ, especially at finite time. This is nonlinear sigma backreaction only, **not the force backreaction on Maxwell and Einstein**.

## Gate 1345 — exact source order and executable results

The spacetime pullback of the H² area form is

`B_mu nu=[∂mu u ∂nu v−∂nu u ∂mu v]/sqrt(1+u²+v²)`.

For the crossed characteristic coordinates, the scalar numerator `C=u_Av_B−u_Bv_A` multiplies a fixed bivector, whose nonzero components in (t,x,y) are `Btx=+C/√D, Bty=−C/√D, Bxy=+C/√D`. The leading numerator is `C0=ab cos A cos B`. Under the fifth-order corrected fields its first extra numerator term occurs at total sixth order,

`C−C0=−a³b³ sin² A sin² B cos A cos B+O(10th order)`.

The **normalization of the nonlinear H² metric** already changes B at fourth total order, whereas the *dynamically generated fifth-order sigma correction* changes B first at sixth total order. Hence one must not confuse metric/area normalization with true nonlinear sigma evolution.

Actually executed local exact SymPy script `/mnt/data/cone_gate/k4_crossed_h2_fifth_order_v15_1410.py` checked both Box δ terms and cancellation, the leading area-source correction, and representative residual magnitudes (A=.53,B=.76):

| equal a=b | uncorrected E max | corrected E max | corrected/original |
|---:|---:|---:|---:|
| .25 | 2.8028e−4 | 8.63728e−6 | .0308166 |
| .125 | 9.05516e−6 | 6.90967e−8 | .00763065 |
| .0625 | 2.85388e−7 | 5.43106e−10 | .00190304 |

Halving amplitude reduces the ratio by ≈4, as predicted by the increase of two total amplitude powers. **Additive GitHub reproducer:** `research-notes/k4_crossed_h2_fifth_order_solution_v15_1410.py`, SHA **d800584ca97db5ec2b620957539fbaff9d5ccbb0**, authored with exact derivative-through-degree-six symbolic checks; exact committed-byte external Audit replay pending.

**AUDIT:** independently derive the nonlinear target EOM, Box in cross-characteristic variables and the factor 1/6 in both fifth-order corrections, test Taylor cancellations through degree six, classify homogeneous initial-data freedom, and check normalized B area order. The more physical TT Weyl-induced Maxwell current test is committed separately as v15.1411.
