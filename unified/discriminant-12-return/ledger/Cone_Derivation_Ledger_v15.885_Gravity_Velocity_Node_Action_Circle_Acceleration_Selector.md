# Cone Derivation Ledger v15.885 — Gravity: Does action-circle tangency select velocity-node traversal and foundational frequency?

**Date:** 2026-11-13 (US Eastern). **Parents:** Sandbox v14.620 ħ action unit-circle interpretation, v15.233 constant-acceleration parabola/Rindler hyperbola, v15.857 Abel/HJ inverse of the constant-force bouncer action, v15.864 parabola/hyperbola/action-circle tangency, v15.866 gravity-sector h-similar action circle, v15.860 ±c SI null tags; Gravity v15.881–882 Gertsenshtein physical beat length, v15.883 action circle's phase-frequency input, v15.884 user correction that X is a **velocity m/s axis** containing nodes. **Live HEAD immediately prewrite:** 9433dc7a6bb7799a51c8d8232bd0a165fad311e2. Target absent. Strict additive-only; no certified, Sandbox, Audit or Suzuki object modified.

**Question:** Does the tangency of acceleration/deceleration parabolas with the action circle give an **acceleration a=dv/dt** that clocks the nodes along a velocity (m/s) X-axis, turning the EM 1/2 and G 1/4 mesh into an independently selected physical frequency?

**Category:** [D] exact special-relativistic constant-proper-acceleration coordinate-time traversal of conditional velocity nodes and its scale covariance; [D] exact HJ bouncer J(E), J'(E), fixed-action quantization and parameter-rescaling counterexample; [N] no autonomous acceleration/frequency selector; [O] an independent on-shell force/acceleration/mass-energy rule and a physically identified cyclic return path.

## Gate 536 — constant-proper-acceleration trajectory with the *physical velocity axis*

Let c be light speed and a>0 a prescribed *proper acceleration*, not an output of the cone. Start from rest in flat Minkowski spacetime. In inertial lab time t,

**x_rel(t)=(c²/a)[√(1+(at/c)²)−1]**,

**v(t)=c(at/c)/√(1+(at/c)²)**,

**dv/dt=a/[1+(at/c)²]^(3/2)**.

The Galilean parabola sharing this same vertex is **x_par(t)=at²/2**. Both have the same initial x, velocity and second derivative a; their difference is

**(a/c²)(x_par−x_rel)=u⁴/8−u⁶/16+O(u⁸), u=at/c**,

matching the v15.233/v15.864 tangency family. In dimensionless coordinates xi=ax/c² and u=at/c, all a>0 give exactly the same normalized hyperbola **xi=√(1+u²)−1** and parabola **xi=u²/2**. A change in a rescales length c²/a and time c/a while preserving tangency and the entire normalized geometry.

**Important coordinate caveat:** the user's X-axis is **velocity in metres per second**, not the position x in x_rel(t). Tangency of a worldline in position-time coordinates does not identify the X-axis velocity nodes with particular x or t values. The following beta values are conditional examples of velocity-axis node locations, not a newly derived identification.

## Gate 537 — exact time to cross two conditional velocity nodes

For beta=v/c in (0,1), invert the exact relativistic trajectory:

**t(beta)= (c/a) beta/√(1−beta²)**.

If (and only if) the correct node assignment places nodes at v_1=c/4 and v_2=c/2, their lab clock separation is

**Delta t_(1/4→1/2) = (c/a) [1/√3−1/√15] ≈0.319151379 c/a**.

For a→7a the crossing interval scales as 1/7. Proper time satisfies tau(beta)=(c/a) atanh(beta), so its interval is similarly ∝1/a, but has a different functional coefficient. In fact the coordinate acceleration decreases with beta; a uniform spacing on the v axis does NOT entail uniform timing.

A one-way traversal of two static node velocities is **not** a periodic motion. Defining an oscillator frequency from one such crossing would require an independently specified repeating return map or boundary condition. A null light ray with fixed locally measured speed c also does not sweep through massive-state velocity nodes c/4 and c/2.

## Gate 538 — can a fixed action circle close the missing acceleration input?

Use the precise Sandbox v15.857 bouncer action for a *separately specified Newtonian constant-force bound/reflecting model* (not the relativistic hyperbola itself):

**J(E)= (4√2/(3a√m)) E^(3/2)**.

Here E is the bouncer's mechanical energy, m its positive inertial mass and a a supplied constant acceleration (linear potential U=ma x). The full orbit period follows exactly from action differentiation:

**T(E)=dJ/dE=(2√2/(a√m)) √E=2√(2E/m)/a**.

Impose a fixed full-cycle action quantum, with arbitrary positive dimensionless N representing a possible integer+Maslov offset:

**J(E)=2π ħ N**.

Then

**E³=[(3π ħ N a√m)/(2√2)]²**,

so **E∝(ħ a√m)^(2/3)** and consequently **T∝a^(−2/3)**, for fixed m,ħ,N. This defines energy as a function of a, not a from fixed action alone.

An exact counterfamily makes the degeneracy explicit: replacing **a→8a**, **E→4E** keeps the bouncer action **J unchanged** (8× increase in a, 8× increase in E^(3/2)), while the period becomes **T→T/4**. The phase-space action quantum remains the same; the oscillation frequency becomes four times larger. This is a genuine dynamic bouncer with a periodic reflecting return, unlike the monotone velocity-node crossing, but it is a Newtonian comparator, not a derivation of the frozen K4 force.

The constant-force Abel/HJ inversion v15.857 already showed the same limitation: the inverse action recovers the input potential U=ma x *with a retained as an arbitrary supplied constant*. The new exact fixed-action counterfamily demonstrates that even adding an action-quantization condition does not remove it.

## Gate 539 — decisive selector status and open route

**Positive:** the user's physical m/s node axis makes an absolute velocity scale possible if independently normalized to c; a dynamical law converts velocity-node differences to measurable lab/proper times. The action-circle structure and parabola/Rindler tangent identities remain exactly compatible with those trajectories. The action-invariant bouncer demonstration provides a precise quantum-action comparator.

**Negative:** tangency, the ±c ray tags, the AM–GM paired-step/quarter offsets and a fixed action J=2πħN do not fix the acceleration a, time between physical nodes or frequency. In particular, fixing J while varying a changes frequency; the action circle is *not alone a clock*. Nor do these identities establish that velocity nodes c/4 and c/2 occur on an actual EM field or K4 gravitation state, that velocity-axis traversal is cyclic, or that a particular magnetic-field reversal spacing emerges.

**Next gate:** seek an **additional, independent dynamical constraint** (e.g. on-shell K4+Maxwell charge/force equation, action-derived field energy and boundary conditions) that actually fixes a and/or the velocity return map, then test whether it predicts a phase-matching length without inputting the result. A measured rest energy E=mc² could set a *Compton* phase rate E/ħ, but importing m is not deriving an absolute frequency from geometry, and massless rays do not have nonzero proper Compton clocks.

**Reproducer:** research-notes/k4_velocity_node_tangency_action_acceleration_selector_v15_885.py, additive commit **9433dc7a6bb7799a51c8d8232bd0a165fad311e2**. The script was first run in a scratch working copy; two naive SymPy assertion simplification issues were corrected **before commit** (series expansion must be with respect to the underlying time symbol, and positive-sub-luminal square-root branch should be verified on the physical nodes rather than relying on unconstrained beta simplification). The final prepared source executed to PASS completely: symbolic trajectory/acceleration/vertex/series, velocity-node lab and proper intervals, acceleration rescaling, bouncer action derivative, fixed-action energy and rescaling family. No historical files overwritten. Committed-source external audit pending.

**HANDOFF External Audit/Muse:** independently reproduce the exact SR constant-proper-acceleration velocity crossing and the 8a/4E constant-J counterfamily. Check especially the distinction between the input a of the Newtonian bouncer and the proper acceleration a of the SR comparator; they are two models using an acceleration parameter, not automatically the same physical force law. Independently challenge any missing action-derived acceleration selector, any unsupported absolute node position or automatic periodicity, and the 2π action-per-full-winding convention.
