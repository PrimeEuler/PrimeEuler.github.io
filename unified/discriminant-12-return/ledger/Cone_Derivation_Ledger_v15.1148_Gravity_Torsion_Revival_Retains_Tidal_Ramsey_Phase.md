# Cone Derivation Ledger v15.1148 — Torsional coherent revival retains a nonzero gravitational Ramsey phase

**Date:** 2026-11-18 Eastern. **Gravity/Cone lane.** **Classification:** [D] exact classical harmonic tidal-torque trajectory and induced relative two-spin Larmor phase, [D] the ideal quantum spin–torsion coupling of v15.1147 has unit contrast at a full torsional period while a constant applied tidal torque yields nonzero retained phase, [N] the observed effect is conventional spin–oscillator interferometry with externally fixed mechanical frequency, magnetic gradient, tidal torque and phase clock, [O] dissipative open-system visibility, heating and calibrated field source; any distinct G-free Cone interaction. **Immediate prewrite HEAD:** a781d0242974c9f924abce04808a1ec8b12600f8. v15.1148 collision-free; additive-only; protected Suzuki/Lane A, Audit, Sandbox, Muse and certified paths untouched.

## Gate 1045 — a complete ideal gravitational-torsion-Ramsey transfer
Reuse v15.1131 physical spin-gradient source B=(Gz,0,B0+Gx), two spin probes at opposite positions ±(d/2)(cosθ,sinθ,0), and differential Larmor frequency ΔΩ=γGd cosθ. At bias θ0 the derivative is kΩ=−γGd sinθ0. Define the same torsion mode q=θ−θ0, its moment of inertia I, frequency ω_m=√(κ/I), and input gravitational-gradient g through torque F_g=ΔQ sin2θ0 g. Use the fully coupled Hamiltonian from v15.1147
H=p²/(2I)+Iω_m² q²/2−(ℏ/2)(ΔΩ0+kΩ q)D_z−F_g q.
The **classical common force** from a constant tidal input during the Ramsey interrogation, switched on at t=0 with q(0)=q_dot(0)=0, induces
**q_g(t)=F_g[1−cos(ω_m t)]/(Iω_m²)**.
The relative spin phase induced by that displacement is
**φ_g(t)=kΩ ∫_0^t q_g(s) ds
=kΩ F_g[t−sin(ω_m t)/ω_m]/(Iω_m²)**.
The units and the relative plus/minus signs depend on the chosen Zeeman Hamiltonian convention; absolute sensitivity uses |kΩ|. This is the conditional phase due to a specified force, not a direct coupling of a spin Casimir to spacetime stress-energy. The source law supplying g and the apparatus coefficients remain independent parameters.

## Gate 1046 — a stroboscopic backaction-evading ideal *contrast* point
The two quantum Dz branches induce opposite oscillator coherent displacements; as proved v15.1147, if the oscillator begins in its ground state with no damping, their overlap visibility is
**V(t)=exp[−ℏ kΩ²/(Iω_m³)sin²(ω_m t/2)]**.
At stroboscopic interrogation time **t_n=2πn/ω_m**, n positive integer, their conditional displacements return to the same oscillator state, so **V(t_n)=1**, but the classical gravitationally induced phase remains
**φ_g(t_n)=2πn kΩ F_g/(Iω_m³)**.
In particular one period yields
**dφ_g/dg = [2π kΩ ΔQ sin2θ0]/(Iω_m³)**.
At the previously optimized θ0=arctan√2, sin2θ0=2√2/3 and sinθ0=√(2/3). The full phase-coupling product kΩ sin2θ0 retains the same maximization with absolute gain |γGd| × 4/(3√3). Ramsey correlation at the end of the period is **Cxy=−2cos(φ_bias+ΔΩ0 t_n+φ_g(t_n))** with unit *intrinsic mechanical-backaction contrast* in this ideal model; an independently prepared quadrature phase bias is still required for linear small-g readout. The earlier plain mechanical response amplitude q_g(t_n) returns to zero at the end, while the integrated history records a nonzero phase. This is conventional interferometric phase accumulation in a closed forced oscillator, not a measurement of novel gravitational stress. At the isolated full-revival instant the pointwise torsion displacement has no signal even though the spin history does.

## Gate 1047 — no instrument or gravity-selector overclaim
All these effects hold for an exactly linear two-spin longitudinal coupling, a harmonic oscillator, an ideal ground-state preparation, perfect interrogation timing, constant applied torque, no spin dephasing, no magnetic gradient drift, no mechanical loss and no uncontrolled trajectories. In a fully open physical bicone, oscillator thermal noise, loss, resonant response instability, spin decoherence and timing jitter reduce contrast and prevent a generic perfect revival. Backaction cancellation here is a *coherent displacement return*, not elimination of all quantum measurement noise or an evasion of the usual sensitivity/backaction constraints. A stiff mechanical oscillator/short period and long phase integration trade off; no material-independent optimum emerges. An accelerated-source or causal-diamond circle period is NOT automatically the torsional ω_m, and the three-cone geometric dictionary does not supply a frequency or gravitational field equation.

## Reproducer, status and next comparator
Canonical exact local SymPy reproducer `research-notes/k4_torsion_full_revival_tidal_phase_v15_1148.py`, additive script commit **72cc6d0072345056738984879123a1bc2024bf76**. PASS driven equation Green-function integral, q_g(t), φ_g(t), ideal visibility and full-period revival for n=1–4, optimum-angle phase coefficient. External Audit of Gravity v15.1147–1148 pending; latest independent Round 600/v15.1133 verified Gravity v15.1131–1132; later Audit/Lane A entries concern Suzuki and do not supersede gravity numbers.

**AUDIT HANDOFF:** independently derive the conditional forced-oscillator coherent-state overlap including factors of 2; check the classical force-to-phase response and its revival endpoint, angle gain sinθ sin2θ and 54.7356° identity, physical magnetic gradient axis caveat, source and clock independence, and no spurious no-noise/backaction-free claim.

**NEXT:** include explicitly finite thermal occupation and mechanical damping in an open-system spin-torsion model and quantify contrast loss at t_n; compare matched ordinary spin–torsion/standard Einstein tidal apparatus to the archived K4-gravity action. Demand a source-derived physical operator or parameter-free residual before claiming novel gravity. Avoid disturbing active Suzuki R4 certification files.
