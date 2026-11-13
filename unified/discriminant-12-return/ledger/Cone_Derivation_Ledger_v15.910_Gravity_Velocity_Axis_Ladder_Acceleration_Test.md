# Cone Derivation Ledger v15.910 — Physical m/s velocity axis, fixed-shell ladder, and acceleration discriminator

**Date:** 2026-11-13 US Eastern. **Gravity lane.** Parents: Gravity v15.884–888 (physical velocity-axis and time-selector no-go), v15.895–909 (two circles, nested product shells and transverse Schwinger operators), Paper C quantum realization, External Audit Round 571. **Live master HEAD immediately before write:** 0f1370804ec21cd5945dd3a0c92f706b1691a4e0. Target checked absent. Additive-only; preserve certified, Suzuki, Audit and Sandbox objects.

**Owner instruction:** X is measured in *meters per second*, with nodes along X; test whether this makes the acceleration parabolas at every diameter-secant transition physical and selects their rates.

**[D] Gate 608 — velocity steps with actual units.** For fixed outer D=n+k and sector velocity unit u>0 m/s, define v_X(n,k)=u(n−k)/2. Each Schwinger raising transition (n,k)->(n+1,k−1) changes the velocity-axis label by **Delta v_X=u m/s**, regardless of k. Different product shells have local radius R_k=u sqrt(nk) in **velocity units**, and the fixed outer circle radius is uD/2 in velocity units. This is an exact velocity-space geometry and supplies a measurable *velocity interval* conditional on identifying X with a genuine measured velocity component. It supplies neither a spatial lever arm (m) nor a temporal interval (s). The old v15.899 figure-skater I=Mr² contraction model cannot reuse velocity radii as physical lever-arm lengths without additional conversion.

If v_X really represents an object's signed velocity component, a relativistic massive realization requires all populated velocity eigenvalues satisfying |v_X|<c; on a full fixed-D ladder, |v_X| can reach uD/2 (or u(D−2)/2 on the positive x>=1 restricted endpoint, depending on truncation). No universal u may be inferred from c without an independent calibration; v15.884–885 already establish these limitations.

**[D] Gate 609 — a concrete transverse Hamiltonian produces a velocity waveform.** On a fixed-D Schwinger representation, Paper C's coordinate is the operator **Xhat=u(J_z+1/2)**. Take an explicitly supplied physical interaction **H=hbar g J_x**, with g in s^-1 and J_x=(J_++J_-)/2. The SU(2) commutators give Heisenberg equations

**d<X>/dt=g u <J_y>; d²<X>/dt²=−g² u <J_z>=−g²(<X>−u/2)**,

and therefore for an initial number eigenstate |n−1,k> with <J_y>_0=0 and <J_z>_0=(n−k−1)/2:

**<X>(t)=u/2+[u(n−k−1)/2]cos(gt)**.

The exact waveform is sinusoidal in expectation; locally near t=0,
**<X>(t)=v_X(0)−[u(n−k−1)g²/4]t²+O(t⁴)**.
If X is a physical particle velocity, *physical acceleration* is a_X=d<X>/dt, with **a_X(0)=0**, while the quadratic coefficient describes **jerk** j_X=d²<X>/dt² at t=0, not a finite constant initial acceleration. This is an especially important dimensional correction to the tempting 'acceleration parabola' description. Geometric osculation of an action circle in (X,Y) velocity space also is not acceleration versus time; an angle speed g is still required.

For an initial state n−k−1=0, as with pair (3,2), the expectation <X>=u/2 remains fixed even though transitions can occur and the velocity distribution changes. Hence mean-X acceleration cannot be identified with every individual ladder transition's rate. The full probability distribution and quantum measurement protocol are required.

**[D] Gate 610 — the ladder amplitudes enter the change, but do not fix g.** At (n,k), right and left J_x amplitudes have squares nk/4 and (n−1)(k+1)/4, so the short-time expectation shift is

**Delta<X>(t)=(u g²t²/4)[nk−(n−1)(k+1)]+O(t⁴)=−u g²(n−k−1)t²/4+O(t⁴)**.

This matches the exact SU(2) Heisenberg expression. Geometry provides both uniform step u and relative amplitudes sqrt(nk), but a common arbitrary g>0 changes every transition time and acceleration while leaving all circles, node velocities, chord amplitudes and parabolas unchanged. For two examples g and 2g, initial jerk differs by a factor four. Thus **negative clock-selector result:** m/s axis and its curvature do not independently derive a or the transition frequency.

**[C] Gate 611 — physical field comparator.** The v15.908 magnetic J_y or tidal J_x interaction provides a candidate g only upon supplying real measured/predicted B or off-diagonal Hessian Phi12 and the physical detector's oscillator frequency omega*. In the tidal RWA, g=Phi12/omega*. No Cone-derived field or gravitational coupling fixes these parameters. A fully sourced gravity response may ultimately supply g; the present result is ordinary SU(2) kinematics rather than a novel G-free observable. The 'n+1 cycles of sqrt(n)' proposal remains distinguishable from these actual expectation-value oscillations, which have g-controlled frequency and no automatic n+1 factor.

**Reproducibility:** research-notes/k4_velocity_axis_ladder_v15_910.py, commit 0f1370804ec21cd5945dd3a0c92f706b1691a4e0. Fresh exact SymPy verification for fixed D=2..10: step Delta X=u, commutators, acceleration/jerk sign and magnitude, all matrix positions and initial eigenstate conditions. Independent Audit pending.

**Next:** calculate the full time-dependent occupation distribution on D=5 and larger circles, distinguish literal discrete velocity-state quantum jumps from continuous mean velocity, and compare transitions under a physically sourced K4+Maxwell tidal Hamiltonian. Test whether curvature-dependent inter-rung interaction coefficients could survive normalization by standard sqrt(nk) without inventing new fields. Audit/Muse: check sign of Heisenberg motion, velocity-component relativity constraint, and crucial distinction between velocity-versus-time *quadratic tangent* and acceleration-versus-time *parabola*. Note open standalone reproducer process gaps v15.888/890/895/897.
