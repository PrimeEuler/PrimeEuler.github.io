# Cone Derivation Ledger v15.730 — Gravity: an actual on-shell canonical matter field sources nonzero gauge-invariant K4 scalar Weyl curvature

**Date:** 2026-11-11 US Eastern. **Parents:** frozen K4 action v14.928/935; source-first scalar action v15.712–714; ordinary scalar Weyl transfer v15.719–720; physical canonical matter v15.727, corrected full stress/pressure Ward v15.728, complete traceful scalar source-to-Weyl transfer v15.729. **Classification:** [D] exact real massless canonical scalar wave and its quadratic source Fourier coefficient, physical FLRW conservation, corrected K4 scalar acceleration and Weyl amplitude; [C] on-shell matter source as a leading O(epsilon²) external spectator on fixed coasting K4; [O] spatially localized source, subsequent fully retarded metric/solid curvature and complete vector/tensor readouts; [N] no source-independent new gravity constant or unique Cone observable. **Immediately prewrite HEAD:** 2f41b289404355085f5c2b191fd351aad58efca9; target ledger absent. Additive-only, no changes to historical certified or Suzuki objects.

## Gate 364 — choose matter fields that actually satisfy their wave equations

On the exact coasting a(tau)=tau/sqrt(3), use the canonical real massless scalar of v15.727, with a small bookkeeping amplitude epsilon (set to one temporarily in the algebra). Choose the explicit nonparallel two-wave real solution

**chi(tau,x,z)=A(tau) cos(2x)+B(tau) cos(z)**,

**A(tau)=cos(sqrt(11) log tau)/tau**,

**B(tau)=cos(sqrt(2) log tau)/tau**.

Directly applying the coasting background Klein–Gordon operator

**chi_ddot+3 chi_dot/tau-(3/tau²) Delta chi=0**

confirms this is an exact solution for all tau>0. Its energy density is pointwise nonnegative. It is, however, a sum of **spatially nonlocalized plane waves**, used only as an exactly solvable Fourier benchmark. Smooth spatially compact wavepacket data are available in principle by superposition, but are not constructed or propagated in this gate.

## Gate 365 — the matter stress has a common nonzero S/V/T Fourier cross mode

Take spatial wavevectors **p=(2,0,0)**, **q=(0,0,1)**, so their stress cross term has a Fourier component at

**K=p+q=(2,0,1)**, **K²=5**.

The stress of a real canonical scalar is quadratic in chi. Pairing the positive-frequency spatial exponential pieces (each real cosine gives a coefficient 1/2), the cross Fourier source at K has

**rho_K=A_dot B_dot/4**,

**T^(0i)_K= -i[A_dot B q_i+B_dot A p_i]/(4a²)**,

**P_trace,K=3A_dot B_dot/4**,

since p.dot(q)=0. The scalar ADM source coefficients in the archived +--- metric convention are therefore

**J_Phi=a³ A_dot B_dot/4**,

**J_B=a²[q² A_dot B+p² B_dot A]/4**,

**J_psi=3J_Phi**.

The last identity is specific to this orthogonal two-wave cross term; **the full local stress of the scalar field remains generally traceful and nonnegative in energy**, not purely the cross mode. Direct symbolic differentiation with both KG equations verifies the complete corrected scalar energy Ward:

**tau J_Phi_dot+sqrt(3)J_B+J_psi=0**.

The anisotropic spatial cross tensor at this K is proportional to **p q^T+q p^T**, whose exact TT, vector and scalar STF projector squared norms from v15.727 are **32/25,72/25,96/25**, respectively. Thus all three source projections are kinematically nonzero *for the same actual on-shell canonical scalar field*. The three gravitational mode transfer functions for this source have not all been computed.

## Gate 366 — exact on-shell matter source produces an explicit scalar Weyl tide

At **tau=1**, the above matter solution satisfies

**A=B=1**, **A_dot=B_dot=-1**, **A_ddot=-9**, **B_ddot=0**.

These values give

**J_Phi=1/(12sqrt(3))**,

**J_B=-5/12**, **J_psi=1/(4sqrt(3))**, **J_B_dot=-7/6**.

Choose **eta=3/4**, **k²=K²=5** (not k=2 from the earlier source-template gates), so the scalar mode Euler coefficient is **beta=[8eta(1+k²)-3k²]/3=7**.

At an initial scalar solid displacement slice with **P(1)=P_dot(1)=0**, the pressure-corrected physical scalar equation derived at v15.728 gives exactly

**P_ddot(1)=9/25**.

This initial choice is compatible with the nondynamical metric constraints: lapse and shift are not set artificially to zero but solved from the matter source. Using the source-first traceful Bardeen transfer of v15.729, the gauge-invariant metric potentials at the same slice are

**Phi_N(1)=191/1800**,

**Psi_N(1)=-1/72**.

The scalar electric Weyl STF amplitude in a local orthonormal FLRW frame is then

**W(1)= k²[Phi_N(1)+Psi_N(1)]/(2a(1)²) = 83/120**,

and

**E^Weyl_(ij)(1)= (83/120) [Khat_i Khat_j-delta_ij/3]**.

The squared norm is exactly **(2/3)(83/120)²**, the same standard three-space STF 2/3 shape factor.

These amplitudes refer to the **complex Fourier coefficient** at K and to a canonical scalar amplitude set epsilon=1 in the algebra; physically the stress and the linear metric/Weyl response scale **epsilon²**, and real spacetime fields require the conjugate -K coefficient. They are model-normalized quantities at the chosen initial time, not laboratory gravitational units or a new determination of G.

## Gate 367 — what was actually closed, and what remains open

The previous v15.716–725 signed tracefree stress was prescribed without a matter action, allowing arbitrary compact-time pulse shaping and exact Mellin notches. Here an explicit conventional positive-energy matter Lagrangian produces the source, and the **pressure-corrected source-first K4 scalar constraint** produces a **nonzero gauge-invariant gravitational curvature**, with exact symbolic values that can be independently audited. This is a strictly stronger source-realization result than freely assigning a stress Fourier coefficient.

**Scope:** the matter configuration is not spatially localized and the chosen initial data for the K4 scalar mode do not correspond to a fully constructed retarded cosmological source switched on from zero matter at a finite time. The presence of nonzero tensor/vector **stress projections** is not proof of observed vector/tensor Weyl signals for this source. Positive local energy of the complete real scalar does not imply a positive definite individual complex Fourier coefficient. The scale parameter eta and source normalization are still free; no novel experimental Cone gravity observable has been established.

**Reproducer:** research-notes/k4_canonical_two_wave_weyl_v15_730.py, additive commit 2f41b289404355085f5c2b191fd351aad58efca9. Independent local SymPy PASS for exact KG wave equation, all source coefficient/derivative evaluations, traceful Ward, scalar forced acceleration, both invariant Newtonian potentials, electric Weyl amplitude 83/120, STF 2/3 and cross-mode S/V/T projector norms. Historical original action files preserved; no images generated.

**HANDOFF:** independent external audit should rederive the canonical two-wave cross stress directly from the action and its Fourier normalization (the 1/4 cos-mode factor), check +--- vs -+++ stress variation consistency, initial-slice scalar source constraints and curvature 83/120, and distinguish physical on-shell spectator matter from a spatially compact realistic matter source. Audit v15.727–730 together, especially the newly required direct pressure source J_psi and the older tracefree-only Ward limit. Do not accept any interpretation that the 2/3 norm determines a new Newton coupling.

**NEXT:** construct a smooth spatially compact initial canonical scalar wavepacket (or a physically bounded ordinary matter stress) and propagate its Fourier stress history through pressure-corrected K4 retarded curvature, while investigating spherical-symmetry vector/tensor nulls. Compare the resulting source/detector transfer with standard GR+relativistic elasticity, and require a genuinely new parameter-free dimensionless signal to pass the originality gate.
