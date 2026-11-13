# Cone Derivation Ledger v15.891 — Exact action-angle map from the hyperbolic velocity circle

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** v15.864 tangency seat, v15.889 hyperbolic pendulum, v15.890 exact velocity circle. **Fresh master HEAD:** 8f77636b87ee85e8ada0193c2a9988cd66a7df56; target checked absent immediately before this additive commit. No edits to certified, Audit, Suzuki or Sandbox artifacts.

**Question:** Does the geometrical 1/4→1/2 velocity-circle marker interval correspond to a fixed fraction of an actual physical oscillator phase, thereby selecting an amplitude, frequency, or rho?

**Status:** [D] elliptic action-angle reparameterization and exact complete orbit; [N] node phase is amplitude dependent and no frequency or rho is selected; [C] marker interpretation and arithmetic-to-velocity normalization remain conditional.

## Gate 552 — exact nonlinear map and the physical clock

Use the same classical 1D Hamiltonian H=p²/(2m)+V0(cosh(q/ell)−1), omega0=sqrt(V0/(m ell²)), with dimensionless peak displacement A>0 and k=sinh(A/2). Velocity-circle coordinates from v15.890 are v=qdot and w=2sqrt(V0/m)sinh[q/(2ell)], with v²+w²=R_v², R_v=2sqrt(V0/m)k. Define the continuously unwrapped geometrical angle theta by v=R_v cos(theta), w=R_v sin(theta). This fixes sin(theta)=sinh[q/(2ell)]/k and exactly yields

**theta_dot=omega0 sqrt(1+k² sin²(theta))**.

Consequently the period is **T=4 K(−k²)/omega0** where K is the complete elliptic integral of the first kind, and the uniform physical action angle phi, measured from theta=0, is

**phi(theta)= pi F(theta|−k²)/(2K(−k²))**,

with F the *continuously unwrapped* incomplete elliptic integral. Hence phi_dot=2pi/T identically; theta and phi each make a full 2pi rotation over one physical orbit but are not equal except in the harmonic limit k→0. The physical action-angle phase is a clock only once omega0 and amplitude are supplied. No independently chosen Compton frequency is introduced.

## Gate 553 — fixed marker geometry does not imply fixed phase spacing

Conditionally identify the physical marker pair as **w/R_v=1/4** and **w/R_v=1/2** on the same positive-v branch. Then theta_1=asin(1/4), theta_2=asin(1/2)=pi/6. Their *geometrical* angular gap is 0.2709185204562203 rad and is amplitude independent. However their action-angle phase gap is

**Delta phi(A)= pi [F(asin(1/2)|−sinh²(A/2))−F(asin(1/4)|−sinh²(A/2))]/[2K(−sinh²(A/2))].**

Independent quadrature and scipy elliptic functions agree to <2e−12 for all test amplitudes.

| A | Delta phi (rad) | fraction of cycle |
|---:|---:|---:|
| 0.01 | 0.27091971389665 | 0.043118211648 |
| 0.1 | 0.27103781663066 | 0.043137008282 |
| 0.5 | 0.27387186737158 | 0.043588061466 |
| 1.0 | 0.28236653464472 | 0.044940029752 |
| 2.0 | 0.31079001868188 | 0.049463767737 |
| 4.0 | 0.34827431813823 | 0.055429579284 |
| 8.0 | 0.24850882589275 | 0.039551408043 |

A numerical bounded minimization of minus this phase gap finds a *local* maximum at **A≈3.853357, Delta phi≈0.3485526544 rad** (not a derived physical preferred amplitude). The function is not monotonic in A, so a speculative imposed phase-gap target can admit multiple amplitudes, and no mesh-only condition selects one.

Important: these are w/R_v marker fractions, NOT laboratory speeds v/c (as tested conditionally in v15.885–888). w is an encoded potential coordinate with units m/s, not a second Cartesian velocity. Nor is the separate v15.864 tangent shell/action circle proven physically identical to this velocity-energy circle. Identifying the 1/4 gravity and 1/2 EM offsets with these marker fractions is expressly a hypothesis.

## Gate 554 — free physical frequency persists

At fixed amplitude A, rescaling V0→s² V0 while keeping m,ell,A fixed scales omega0 and the entire oscillator rate by s but keeps the dimensionless function phi(theta), its markers, and their phase gap unchanged. The velocity-circle radius changes by s; an independent velocity normalization v_* can compensate it if one assumes R_v(n)=v_*sqrt(n). Even if R_v(n) is fixed numerically, there is remaining freedom in ell while adjusting V0 and E: omega0=sqrt(V0/m)/ell. Thus no value of omega0, the Rindler/Compton ratio rho, Newton G, or a new physical transition frequency is derived.

The ordinary canonical action-angle property phi_dot=2pi/T holds here by construction from an integrable autonomous 1D Hamiltonian; it is not a new prediction of gravity. Tangency at the rest seat fixes contact geometry but not stiffness or inertial normalization.

## Verification and next step

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_hyperbolic_velocity_circle_action_phase_v15_891.py`, commit **8f77636b87ee85e8ada0193c2a9988cd66a7df56**. Executed locally with Python/SymPy/SciPy/NumPy: PASS for cosh half-angle identity, elliptic-versus-independent-quadrature comparison, complete-cycle K normalization, small-amplitude limit, node noninvariance, and local phase-gap maximum. **Independent Audit pending**.

**NEXT:** Evaluate marker choice by genuine observables, not presumed offsets; compare action-phase marker position using the original parabola/force geometry and explicit field-derived stiffness. Build a relativistically admissible counterpart to avoid assuming |v| can exceed c. Test coupled EM/gravity parametric response only after an interaction and physical units are specified. Report null results.

**HANDOFF Audit/Muse:** independently check K(−k²) period, global unwrapped F, sign/orientation, two-marker branch convention and nonmonotone phase gap; review whether any authentic Cone mesh boundary condition derives w/R_v nodes. Also note Audit Round 569's unrelated v15.888 missing reproducer remains open.
