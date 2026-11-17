# Cone Derivation Ledger v15.1112 — Maxwell ellipse shape inertia, quartic circular-state stiffness, and passive tidal energy budget

**Date:** 2026-11-17 Eastern. **Lane:** Gravity/Cone. **Classification:** [D] exact electromagnetic electric-field-induced kinetic coefficient M(e) for the v15.1110 compact cone-shaped stream-function family; [D] magnetic-energy quartic circular-state expansion, absence of linear gravitational driving force at perfect circular symmetry; [C] finite-dimensional mechanical constrained action with elastic support and damping yields causal response and checks its **own** total energy balance; [N] neither a unique small-amplitude Maxwell-only frequency nor universal sech/mesh time selector follows; [O] genuine self-consistent material sources, wall elasticity, covariantly conserved Einstein–Maxwell–K4 source and measurable matched residual. **Immediately prewrite live HEAD:** 6a243e529b5eeb6b6a0503b0ea68dc1307bf7da2. Target v15.1112 collision-free; additive-only; no prior audit/Suzuki/Muse/Sandbox/verified foundation files changed.

## Prior work and synchronization
Newest independent external Audit seen is Round 595/v15.1109 commit cd4196eaf8b1a450f6fdc2386f49754842c4edc6, confirming v15.1105–1108, including the disclosed nonsolenoidal v15.1107 prototype and its additive correction. Gravity v15.1110 established a compact Maxwell magnetic field following the **projected** focal cone ellipse with
A=C/(1-e²), B=C/sqrt(1-e²), d=-Ce/(1-e²), q=((y-d)/A)²+(z/B)²,
vector potential A_EM=[psi0 f(x)(1-q)^4,0,0] on q<1 with compact normalized f(x) and zero otherwise. B=curl A is solenoidal and is supported by a current. Gravity v15.1111 introduced arbitrary time-dependent e(t) and proved exact Maxwell charge/current continuity, Poynting balance, and a *prescribed* sech time-lag/tidal work parity. **This gate specifically attempts to derive the missing ellipse shape clock from field energy and a well-identified mechanical support law, rather than postulate e(t)=sech(t).**

## Gate 985 — electric-field energy gives a finite Maxwell shape inertia
Work first at zero external tidal strain h and with the compact profile f normalized by ∫f²dx=1. Let e(t) be a real collective coordinate, |e|<1. In temporal gauge, E_x=-∂t ψ=-[∂e ψ] e_dot, B=(0,ψ_z,-ψ_y). Hence
U_E=(ε0/2)∫E²d³x=(1/2) M(e) e_dot²,
**M(e)=ε0 ∫(∂e ψ)²d³x**.
Use elliptical coordinates y=d(e)+A(e)r cosφ, z=B(e)r sinφ, 0<r<1, Jacobian AB r. Crucially ∂e at **fixed physical y,z**, not fixed r,φ:
∂e q = [2r(1+e²)cosφ-2e r²(1+cos²φ)]/(1-e²).
The angular integral is ∫_0^{2π}(∂e q)²dφ = π[4r²(1+e²)²+19e²r⁴]/(1-e²)².
For F(q)=(1-q)^4, ∂e ψ=ψ0 f F'(q)∂e q; ∫r³ F'(r²)² dr=1/7 and ∫r⁵ F'(r²)²dr=2/63. Integrating gives the exact positive finite result
**M(e)= [2π ε0 ψ0² C²/63] [(18+55e²+18e⁴)/(1-e²)^(7/2)].**
In particular **M(0)=4π ε0 ψ0² C²/7**. Note that near e=0 the shape derivative includes a **translation of the field center** since d'(0)=-C; this is the actual inertia of the specified combined focus-locked translation+ellipticity family, NOT pure ellipticity with a held-fixed center. Moving the source requires actual supporting matter/charges. Its kinetic coefficient is derived from electromagnetic field energy, but the reduction to a single shape coordinate is a **prescribed constrained ansatz**, not a free-vacuum Maxwell eigenmode.

## Gate 986 — the magnetic field has no linear shape restoring frequency at the circle
From v15.1110, using K=4π ψ0²/(7μ0),
U_B(e)=(K/2)(2-e²)/sqrt(1-e²),
I_plus(e)=∫(Tyy-Tzz)d³x= -K e²/sqrt(1-e²).
Exact derivatives:
U'_B= (K/2)e³/(1-e²)^(3/2),
U''_B= (3K/2)e²/(1-e²)^(5/2).
At e=0, U'_B=U''_B=I'_plus=0. Taylor:
**U_B(e)=K+(K/8)e⁴+O(e⁶)**,
**I_plus(e)=-K e²+O(e⁴)**.
The ideal constrained Maxwell shape therefore has a **quartic** potential about e=0 and no finite linear small-amplitude frequency there. This is a critical *negative selector* result: merely invoking a rest-state ellipse and sech geometry does not produce a unique natural frequency. Its leading magneto-electric scale is
**K/M(0)=1/(ε0 μ0 C²)=c²/C²**,
which only gives a dimensionful coefficient set by the **externally supplied** ellipse scale C, not a quantized/selected period. In an *artificial* Maxwell-only constrained shape Lagrangian the leading equation would be e_ddot+(K/(2M(0)))e³=0, which is amplitude-dependent; however this must NOT be promoted to a source-free physical Maxwell mode: the supporting currents and moving charge distribution needed for this ansatz are not accounted for by free Maxwell variation.

For a plus-TT incident tidal strain h, the first-order conventional metric interaction has the reduced Lagrangian contribution +(h/2)I_plus(e), consistent with the earlier externally prescribed work **P_g=-(1/2)h_dot I_plus(e)**. At the perfect circle, the derivative I'_plus(0)=0, so the GW gives no first-order additive shape force; instead the small-e equation has a **parametric stiffness** term h(t)K e. At any nonzero fixed e0 an actuator may hold the shape off-center and the GW provides a linear driving force proportional to h(t)I'_plus(e0). Neither the initial shape e0 nor the time-evolution phase emerges from the cone mesh.

## Gate 987 — passive support produces causal phase and explicit energy partition
Introduce a separately specified mechanical support V_wall(e) and a Rayleigh dissipation coefficient γ≥0. The constrained reduced-field Lagrangian is
**L= (1/2)M(e)e_dot² - U_B(e)-V_wall(e) +(1/2)h(t)I_plus(e)**,
plus an omitted physical support/material action. Its damped Euler–Lagrange equation is
M e_ddot +(M'/2)e_dot²+U'_B+V'_wall-(h/2)I'_plus=-γ e_dot.
Define the total reduced energy
**E=[M e_dot²/2]+U_B+V_wall-(h/2)I_plus**.
Then
**dE/dt=-(h_dot/2) I_plus(e)-γ e_dot²**.
This identity correctly separates external gravitational metric work and irreversible support loss within this **one-coordinate constrained model**. In the actual complete system GW depletion, radiation, walls, self-consistent charges and EM current work must be restored; a correct reduced ODE energy identity alone is not a proof of full covariant conservation.

For a transparent numerical witness choose normalized ε0=μ0=C=ψ0=1, h(t)=0.03(1-t²)^4 on |t|<1, h=0 outside; equilibrium e0=.3 and V_wall=.5*k(e-e0)²-U'_B(e0)(e-e0), k=2, γ=.2; initialize e=e0, e_dot=0 before the pulse and solve t=-4→14. This wall choice is explicit: its linear term balances U'_B(e0). SciPy solve_ivp (rtol 1e-11, atol 1e-13, max_step .01) gave
**W_g=2.976474693214952×10^-5**,
**E_diss=1.661302431541615×10^-5**,
**ΔE_stored=1.3151722615400985×10^-5**,
with **ΔE_stored + E_diss - W_g≈-1.33×10^-15**. This shows a self-consistent *finite-dimensional damped solution* whose phase lag is determined by its externally chosen wall inertia/stiffness/damping, instead of by prescribing a sech delay. These are model energy units, not laboratory numbers or cone predictions, and the gravitational strain h was imposed, not sourced from K4.

## Gate 988 — interpretation, limitations, reproducibility, next test
**Positive:** the *specific* focus-locked cone ellipse carries a finite calculated electromagnetic shape inertia and quartic magnetic shape potential; a supported passive shape can absorb energy from a finite tidal pulse in a causal way, with the reduced budget closing to numerical precision. **Negative:** this still derives no physical current/constitutive law, unique frequency, sech time clock, source G, or new scalar/vector/tensor tidal observable. A constrained trial-field family with arbitrary charge/current source can mimic a mechanical collective coordinate even when no such dynamical mode exists in source-free Maxwell theory. The missing source law is essential, not a small correction.

Canonical full executable script: `research-notes/k4_dynamic_cone_ellipse_collective_inertia_energy_v15_1112.py`, additive commit **6a243e529b5eeb6b6a0503b0ea68dc1307bf7da2**. Equivalent full source was executed locally before commit: PASS exact symbolic M(e), U_B, I_plus, small-e quartic, circular-state zero linear drive, c/C scale, and causal numerical energy closure as above. Independent Audit of committed script pending.

**AUDIT HANDOFF:** check ∂e q taken at **fixed y,z**, not at fixed r,φ; radial integral 2/63, coefficient 19 in angular integral, exact M(e), quartic cancellation of e², tension-source sign in the reduced Hamiltonian, numerical work/dissipation partition, physical source and support caveats. Check no false statement that free Maxwell has a physical quartic nonlinear eigenmode.

**NEXT:** derive a realizable charge/current/elastic-source constitutive action whose collective deformation reduces to e(t) (including Coulomb and electric field stress, boundary work, radiation); compare the induced phase against ordinary Maxwell–Einstein and the **same** K4 solid with full ADM SVT constraints. Alternatively test the sign and magnitude of a source-independent normalized transverse polarization response after apparatus calibration. The cone's sech tracing and ±1/2/±1/4 grids still do not select C or the mechanical support parameters.
