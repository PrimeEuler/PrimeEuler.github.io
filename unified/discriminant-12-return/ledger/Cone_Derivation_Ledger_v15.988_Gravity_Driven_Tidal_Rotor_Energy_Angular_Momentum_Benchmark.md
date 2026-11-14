# Cone Derivation Ledger v15.988 — Driven physical tidal rotor, torque response, source work and matched-action comparator

**Date:** 2026-11-14 US Eastern. **Lane:** Gravity. **Owner instruction:** continue after v15.986 by evolving the existing rotor in a field-sourced transverse tidal interaction, not an invented curvature/Casimir term. **Status:** [D] exact classical equations and work identity; [N] numerical driven-rotor solutions in a stated dimensionless control, including first-order susceptibility; [N] matched-standard-physics residual is identically zero because the physical Hamiltonian is unchanged; [O] any quarter-grid independent kinetic source, fully sourced K4 tidal waveform, and physically measurable nonstandard response.

**Parents and redundancy:** v15.897 outer geometric acceleration parabola; v15.898 conditional rest/total energy dictionary; v15.900 actual fixed-L central-force rotor and turning-point radial parabolas; v15.908 physical magnetic J_y/tidal J_x Schwinger interactions; v15.914 physical Fermi tide full Fock-space dynamics; v15.918 measured signed-velocity X parity obstruction; v15.984 rotor-versus-ladder clock negative; v15.986 real transverse tidal radial force and torque, and incompatible fixed-L assumption. External Audit Round 582 **v15.987** commit c5841da8cc2eba00804764d6488b55e85553ff0a independently verified v15.986. This gate consequently uses version **v15.988**, avoiding collisions. **Live master HEAD immediately before this write:** 5860d703c0b3d1e8e873e0c15c4fc3508171f892 (reproducer). Target confirmed absent. Strictly additive; no Suzuki/frozen, Audit, Sandbox or Muse file modified.

## Gate 800 — true two-degree driven Hamiltonian instead of frozen-L approximation

Keep the *stipulated* central-force baseline of v15.900, **V_0(r)=F0 r**, with M mass, radial momentum p_r, physical orbital angle phi and conjugate mechanical angular momentum L. Add the **existing** off-diagonal local Fermi tidal potential (v15.986)

**V_tid(t,r,phi)=[M B(t)/2] r² sin(2 phi)**

where B(t)=Phi12(t) is an **external physical tidal curvature** (units s^-2). The Hamiltonian is

**H=p_r²/(2M)+L²/(2Mr²)+F0 r +[M B(t)/2]r² sin(2phi)**.

Its exact Hamilton equations are:

- rdot=p_r/M;
- p_rdot=L²/(Mr³)−F0−M B(t)r sin(2phi);
- phidot=L/(Mr²);
- Ldot=−M B(t)r² cos(2phi).

Thus L(t) is NOT constant when B is generically nonzero; the unforced v15.900 turning radii and exact radial parabolas should not be reused unchanged. The axial magnetic first-order linear Hamiltonian from v15.908, proportional to L, would preserve canonical L in an ideal static uniform B comparator; any finite B² diamagnetic terms, radial effects and canonical/mechanical angular momentum distinction must be handled separately.

For any external B(t), the exact nonautonomous work identity is

**dH/dt = ∂H/∂t = [M/2] Bdot(t) r(t)² sin(2phi(t))**.

Thus the time integral W(t) of this source power must obey **H(t)−H(0)=W(t)**. In the static case Bdot=0, total physical energy is conserved although L and kinetic components exchange. A time-periodic tide can either supply or remove net energy, depending on its phase and trajectory. This is entirely standard Hamiltonian mechanics and linearized tidal coupling; it introduces no parameter-free Cone gravitational drive.

## Gate 801 — reproducible dimensionless benchmark and conservation controls

Use exactly the preexisting v15.900 n=4 rotor control: M=1, ri=1, ro=5/4, initial L=1, p_r=0 at ro, phi=0 and baseline F0=18/25=0.72. Integrate to t=2.2 dimensionless time with SciPy DOP853/RK45 (implementation solve_ivp default RK45), tight rtol=1e-12/atol=1e-13 and time steps ≤0.005, and include Wdot above as a fifth variable.

| Prescribed source | r(2.2) | L(2.2) | W(2.2) |
|---|---:|---:|---:|
| B=0 | 1.000677097175 | 1.000000000000 | 0 |
| Static B=0.02 | 0.962644279631 | 0.991629528224 | 0 |
| Periodic B(t)=0.02 cos(1.7t) | 0.982471701105 | 0.971154304299 | −0.021055726566 |

For the baseline at t=2.2 the rotor is near its original r_i turning point and L=1. For static B≠0, r(2.2)<1: the old inner turning radius is **not conserved** under tidal forcing. Static-tide energy is conserved at numerical residual ~1.1×10^-15, despite angular momentum changing. For periodic B, the source extracts net work in this initial phase configuration: W=−0.0210557; the exact balance E(t)−E(0)−W(t) has numerical residual <2×10^-15 (all integration cases).

These are **dimensionless mathematical controls**, not observed tidal strains, experimentally predicted forces, or a K4 on-shell sourced waveform. A time-varying prescribed Phi12 is a prescribed external field; we do not include its back-reacting stress or prove it is part of a fully consistent global Einstein solution.

## Gate 802 — first-order angular-momentum response confirms the sourced torque

For a static source B=epsilon≪1, the exact first-order variation about the unforced orbit (r_0(t),phi_0(t)) is

**delta L(t)/epsilon = −int_0^t [r_0(t')² cos(2phi_0(t'))] dt' + O(epsilon)**.

At t=2.2 the coefficient is **−0.361502210437**. Finite source estimates (L_epsilon−1)/epsilon are

| epsilon | finite slope |
|---:|---:|
| 0.01 | −0.390219416800 |
| 0.02 | −0.418523588810 |
| 0.04 | −0.473890602455 |

They approach the first-order coefficient as epsilon→0; the error is approximately linear in epsilon at this source range. The response is torque generated by ordinary Fermi tidal mechanics. No independent quarter-grid angular coupling appears; source amplitude and angular phase remain genuine inputs.

## Gate 803 — critical meaning of a matched-action GR comparison

The control reproduces v15.986's sourced radial and angular interactions, with a physical Hamiltonian H. The same *ordinary GR Fermi tidal + classical central-force rotor* reference, using identical source B(t), boundary values, mass M, central F0 and phase, has the exact **same** equations and outputs. Its **Cone-minus-GR residual is identically zero by Hamiltonian identity**, not a claimed independent numerical discovery. v15.760 already proved a general action-matching transfer null for K4+ordinary Einstein/elasticity. Calling the observed Δr or ΔL a *new gravitational signature* would double-count conventional physics.

The baseline central F0 r is assumed external matter/constraint potential; it is not derived from the source-free K4 field and is not a universal gravity prediction. The local external B(t) is likewise supplied, not fixed by Cone geometry or the n+1 boundary. No restoring stiffness, absolute clock, G value, or new dimensionless source-free ratio follows.

Also do **not** assert the original fixed-N EM Schwinger ladder and the classical radial phase space are automatically one physical quantum system. The identification r/ri=gamma and A=1/gamma tested in v15.984 is a conditional comparison; fixed-J_y angular momentum and transverse J_x tidal coupling are incompatible conserved quantities once the tide acts. The physical velocity X parity obstruction from v15.918 remains.

## Gate 804 — precise open selector

A positive next gate needs an **explicit independent Cone-specific term** added to or derived instead of the conventional GR+Maxwell tidal Hamiltonian, with its coefficient and domain fixed by the model rather than postselected to the 9/5, 1/4 or 1/2 features. A concrete measurable signature would then be a source-normalized rotor response ratio or phase difference *after* matching conventional parameters. Until that term exists, our numerical trajectory provides a well-validated standard-GR benchmark, not novel physics.

**Reproducer:** `research-notes/k4_driven_rotor_tidal_work_v15_988.py`, additive commit **5860d703c0b3d1e8e873e0c15c4fc3508171f892**. Local Python/SciPy actually run to PASS, all five tests (including additional static epsilon=.01,.04), energy/work identity at dense output points, torque response, numerical residuals. External independent Audit pending.

**HANDOFF Audit/Muse:** independently reproduce numeric r,L,W table, exact energy-work identity, sign convention and first-order torque slope; check how static B retains total energy but changes angular momentum and old turning radius. Do not confuse time-dependent prescribed field work with an autonomous source-free gravity oscillator. Preserve the negative novelty conclusion unless a new field-derived, constrained kinetic term is actually produced.
