# Cone Derivation Ledger v15.1412 — Cauchy-initialized fifth-order nonlinear H² crossed-wave correction

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [D/N PASS] corrected the particular crossed-null-wave nonlinear H² sigma solution of v15.1410 to obey **zero correction to both field and time derivative on t=0**, by subtracting an exactly propagated homogeneous wave; [N PASS] forced wave PDE, source order, vanishing Cauchy data and spatial-resolution controls in finite 2D periodic domain; [OPEN] strict retarded infinite-domain/finite-packet initial data, corrected source current for *this Cauchy choice*, whole Einstein–Maxwell–sigma action, finite particle detector, unique quarter-grid coupling. Strict additive; archived v15.1409–1411 unmodified. **Preledger live HEAD:** 79b5804f887704262f3ce00273f07315f7e3b77a; new version slot checked clear.

## Gate 1348 — choose physical Cauchy preparation instead of an arbitrary periodic particular solution

Let (A=t-x), (B=t-y), with leading H² sigma fields `u0=a sin A,v0=b sin B`. The v15.1410 exact fifth-order source solution was the particular pair

`u5p=−a³b² sin³ A sin² B/6,quad v5p=−a²b³ sin² A sin³ B/6`.

They solve `Box u5p=−E_u^(5), Box v5p=−E_v^(5)` with the flat 2+1 `Box=−∂t²+∂x²+∂y²`, canceling nonlinear sigma residual through amplitude degree six. But `u5p(0,x,y)` and `∂t u5p(0,x,y)` do not in general vanish; likewise v. An arbitrary homogeneous addition can change the wave and its induced area source at order six. To **fix** this freedom choose physically clear initial conditions

`u5(0,x,y)=v5(0,x,y)=0` and `∂t u5(0,x,y)=∂t v5(0,x,y)=0`.

Define H_u and H_v as exact homogeneous massless waves with the initial data of the original particular solutions:

`Box H_u=0,quad H_u(0)=u5p(0),quad ∂t H_u(0)=∂t u5p(0)`, and similarly v. Then the unique periodic linear forced Cauchy solution is `u5=u5p−H_u, v5=v5p−H_v`. For every 2D Fourier spatial wavevector k=(kx,ky),

`Hhat_k(t)=cos(|k|t) Hhat_k(0)+sin(|k|t)/|k| ∂tHhat_k(0)`,

with `sin(|k|t)/|k|→t` for the zero mode. This is the standard deterministic Cauchy evolution; the fifth-order source does not depend on H at this order because nonlinear feedback from order-five corrections begins at higher amplitude order. This fixes **only** the order-five initial-value problem, not the fully coupled field theory.

## Gate 1349 — reproducible spectral/PDE and zero-initial-data tests

Use real periodic spatial domain x,y∈[0,2π), N×N equispaced grids. Evaluate u5p,v5p and time derivatives analytically, Fourier-propagate homogeneous H and its time derivative with exact |k| frequencies, and reconstruct u5p−H. Check both fields and first time derivatives vanish on the initial slice to floating precision, independently differentiate the reconstructed source in time via centered second derivative step δt=.001 and in space by spectral Laplacian, and compare **the full forced wave PDE**, not only the initial cancellation.

The **actually executed** local Python `/mnt/data/cone_gate/k4_crossed_h2_cauchy_fifth_v15_1412.py` produced at a=b=.3,t=.7:

| N² | max amplitude of fifth-order Cauchy correction | max relative PDE residual | max initial field/velocity |
|---:|---:|---:|---:|
| 16² | 1.2670304609017623e−4 | 1.8463299240266827e−6 | 2.17e−19 |
| 24² | 1.3490341542330407e−4 | 1.8948619695824902e−6 | 4.34e−19 |
| 32² | 1.3584571715397227e−4 | 1.9487417029298016e−6 | 2.17e−19 |

The PDE residual here is **time-second-difference truncation dominated**, not evidence of full spatial/continuum convergence. The small-amplitude corrections are consistent with perturbation theory. The 16/24/32 grid changes in correction peak reflect spatial sampling of a smooth real periodic field; a certified continuum field error bound and full nonlinear residual evaluation for this Cauchy history remain separate tasks. These corrections have zero initial data but do not imply sigma energy conservation under nonzero Weyl–Maxwell interaction, which remains absent in this model.

**Additive GitHub reproducer:** `research-notes/k4_crossed_h2_cauchy_fifth_v15_1412.py`, SHA **79b5804f887704262f3ce00273f07315f7e3b77a**. The exact committed file independently authored to reproduce the local source's Fourier homogeneous subtraction and numerical checks, awaiting independent Audit byte-for-byte replay. All prior v15.1410/1411 code and certified Audit/Sandbox/Suzuki/Muse assets untouched.

## Audit and next gate

**AUDIT:** replay exact committed v15.1410–1412 code; verify Green/Cauchy homogeneous subtraction and wave equation sign, correct zero-k handling, initial velocity cancellation, nonlinear EOM order from v15.1410, Weyl current from v15.1411, and disclose any mismatch in floating precision. Derive the corrected physical normalized area and Weyl-induced Maxwell four-current **for this zero-Cauchy sigma history**, compare against previous special particular solution; then evolve transverse Maxwell packet, track true physical stress/energy exchange and full EH+K4+Maxwell+H² metric backreaction. No physical action yet selects r=1/4, ζ/Λ², f, or the intersector finite-Hilbert bridge (v15.1387–1398). Exact hyperboloid volume 3:1/7:1, null-affine 3:1 and conditional χ=ln2 holonomy do not supply that missing action.
