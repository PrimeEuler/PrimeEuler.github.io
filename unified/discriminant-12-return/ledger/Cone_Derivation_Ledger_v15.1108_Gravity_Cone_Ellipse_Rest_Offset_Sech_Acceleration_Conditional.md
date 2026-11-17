# Cone Derivation Ledger v15.1108 — Cone ellipse's focus-rest offset, hyperbolic-secant trace and conditional acceleration/deceleration

**Date:** 2026-11-17 Eastern. **Gravity/Cone lane.** **Status:** [D] exact intrinsic cone cutting-plane conic and its *projected* ellipse with center offset fixed by eccentricity; [D] exact cone secant/rapidity sech parameterization of this ellipse; [C] if independently imposing areal angular momentum conservation, acceleration/deceleration of radial coordinate follows with an inverse-square central acceleration; [N] no new physical acceleration law, electromagnetically supported magnetic circulation, fixed tidal phase, quarter-grid selector or novel G-free observable. **Immediately prewrite live HEAD:** 856417c8b7b45526cff5983e1cf446deb986b5e6. Commit collision check complete; additive-only; no original foundation, Suzuki, Audit, Sandbox or Muse edits.

## Existing provenance and why the link is meaningful
The owner's prompt identifies cone ellipses as carrying their *own* acceleration/deceleration parabolas, hyperbolic-secant links, and rest offsets. **Archived immutable foundation PaperA Conic Theorem v2.4** already proves the generalized cone cutting-plane ellipse, row/column parabola pair, true intrinsic axes and eccentricity. Prior v13.691/v15.1053 derived the AM–GM hyperbola/secant rapidity-circle map, while v15.1100 traced a uniformly accelerated hyperbolic worldline through confocal parabolas and sech. v15.1107 computed magnetic tension and a physically divergence-free azimuthal ellipse with nonzero TT m=2 stress, after explicitly preserving a naive nonsolenoidal prototype. Latest independent Audit Round 594/v15.1104 confirmed earlier Gravity v15.1100–1103; v15.1105–1107 remain unaudited in this commit check. This gate makes a **previously separate geometric constraint explicit**: the cone's projected ellipse center and projected eccentricity are tied by its cut-plane equation. It does not claim that the projected conic itself is a physical magnetic field.

## Gate 973 — a tilted cone cutting plane gives a focus-centered polar ellipse
Work with physical positive cone sheet T²=X²+Y², T>0, and cutting plane
T+e X=C with C>0 and |e|<1 (the sign of e fixes orientation; for symbolic checks e is chosen positive). Eliminate T:
(C-e X)²=X²+Y².
Completing the square gives the **XY-projected ellipse**
(X-X0)²/A²+Y²/B²=1
where
X0=-Ce/(1-e²), A=C/(1-e²), B=C/sqrt(1-e²).
It obeys **A²-B²=X0²**, and the focal offset of the projected ellipse is |X0|=A|e|, placing **one projected focus precisely at X=0** and the other at X=2X0. The exact polar equation measured from the cone origin/focus is
**r(φ)=C/(1+e cosφ)**, with X=r cosφ, Y=r sinφ, T=r.
For a fixed C, the projected 'rest' center displacement is uniquely determined by the signed tilt e. But C and e themselves are external free cutting-plane parameters; the unit mesh offsets ±1/2 and ±1/4 do not automatically select e or C.

**Important distinction:** PaperA's established **intrinsic 3D ellipse** lies in the tilted cutting plane and has true eccentricity |a-b|/sqrt(a²+b²), where a,b are coefficients of the factor-line ax+by=c. With the current normalized plane T+e X=C this corresponds to factor coefficients (1+e)/2 and (1-e)/2, giving **e_intrinsic=sqrt(2)|e|/sqrt(1+e²)**. The **XY projection** instead has e_projected=|e|; these MUST NOT be conflated. Physical Maxwell stress in a chosen transverse plane could use the projected ellipse, but a 3D field geometry must specify an embedding and actual vector currents.

## Gate 974 — exact hyperbolic secant for each point of the eccentric cone ellipse
On the upper branch 0<φ<π, define rapidity u by
X/T=cosφ=tanh u, Y/T=sinφ=sech u; hence u=artanh(cosφ),
du/dφ=-1/sinφ, dφ/du=-sech u.
The tilted ellipse becomes
**r(u)=C/[1+e tanh u]**, **Y(u)=C sech u/[1+e tanh u]**.
The cone null-factor/secant label k=T+X satisfies
**k(φ)=C(1+cosφ)/(1+e cosφ)**;
its partner T-X=r(1-cosφ), and k(T-X)=Y². This is the exact familiar mean-value/hyperbolic secant map applied *on an eccentric ellipse*, not a newly postulated differential equation. Unlike the fixed-Y secant of Gravity v15.1100, here Y changes with φ and the plane section forms a closed ellipse; it is incorrect to regard every point as lying on one fixed-Y constant-proper-acceleration hyperbola. The row and column parabolas of PaperA are separately present at each fixed factor x=T+X and y=T-X, exchanged by factor reflection. The geometry provides both acceleration/deceleration branch **labels**, but it does not create an actual time evolution or force.

## Gate 975 — acceleration/deceleration branches need a clock law
If an **independent physical dynamics** supplies conservation of specific angular momentum J=r²φdot, then
φdot=J(1+e cosφ)²/C²,
**rdot=(Je/C)sinφ**,
**rddot=(J²e/(C r²))cosφ**,
and the radial central-force acceleration is
**rddot-r φdot²=-J²/(C r²)**,
with tangential acceleration zero.
Thus the radial distance has turning points at φ=0,π; rdot increases on φ in (0,π/2), decreases in (π/2,π), and the pattern reverses around the other half of the closed ellipse. This provides a mathematically coherent **acceleration/deceleration** trajectory whose sech rapidity coordinate is exact. But all these time derivatives and the inverse-square law appear **only after imposing J**, the usual Kepler area law. The cone's row/column *geometric parabolas* are not automatically physical trajectories of uniformly accelerated motion at each point; conflating them would insert missing dynamics.

A small-e expansion of the projected radial shape is
r/C=1-e cosφ+(e²/2)(1+cos2φ)+O(e³).
Thus a focus-centered radial **quadrupolar harmonic arises at order e²**, while the first-order focus/radius perturbation is an m=1 polar harmonic. This is not inconsistent with v15.1107's magnetic-stress quadrupole occurring linearly in its independent elliptical-field parameter: the vector-field direction, divergence-free completion and actual B² stresses differ from a scalar radial boundary function. To equate them requires a physical map from this specific cone cut to a Maxwell stream function, with currents and dynamical boundary conditions. A center offset is not by itself proof of a physical m=2 stress response.

## Gate 976 — status, script, Audit and next material test
Canonical script `research-notes/k4_ellipse_rest_offset_sech_acceleration_v15_1108.py`, commit **856417c8b7b45526cff5983e1cf446deb986b5e6**. Core identities for projected focus/axes, polar small-e Fourier expansion, exact sech map and conditional Kepler areal-law acceleration were **executed in local SymPy and PASS** before commit. The committed script adds equivalent algebraic and endpoint checks; complete committed-byte external Audit remains pending. No G, Compton scale, source phase, electric/magnetic current, or physical mesh selection has been derived.

**Positive:** the previously separate ellipse rest-center shift and its projected eccentricity are linked *exactly* by Cone cutting geometry; the same ellipse admits an exact sech parameter, and an independently chosen areal clock yields controlled acceleration/deceleration phases. **Negative:** this is geometry plus standard Kepler law; it neither fixes J nor e, nor does it force an EM magnetic stream function, tidal quadrupole strength or phase. The archived PaperA classification and older hyperbolic-secant circle are credited instead of being relabeled as new.

**NEXT:** define an explicit compact-support divergence-free Maxwell stream function whose elliptical level sets coincide with the *projected* tilted-cone ellipse, compute its plus/cross TT integrated stress and first-order tidal work, and test if e_projected and the cut-plane offset actually constrain the Maxwell quadrupole beyond an arbitrary deformation. Also consider dynamic e(t) with a physically sourced current/force/energy budget, not just the Kepler area clock. When comparing to the gravitational quarter-grid/EM half-grid, do not identify the 1/4 gravitational mesh vertex with the EM +1/4 Casimir (the latter is a distinct object per v15.624).

**AUDIT HANDOFF:** check distinction between intrinsic 3D plane-section eccentricity and XY projection; origin-focus from X0²=A²-B²; sign/reflection orientation; hyperbolic sech upper branch and k=T+X; radial harmonic first m2 order e²; Kepler inverse-square from *imposed* J, not cone; no generated Maxwell currents or tidal energy claimed.
