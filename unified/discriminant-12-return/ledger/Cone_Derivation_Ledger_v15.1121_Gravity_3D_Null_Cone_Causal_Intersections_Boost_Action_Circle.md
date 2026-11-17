# Cone Derivation Ledger v15.1121 — 3D general-plane conics and intersecting causal null cones: a Lorentz-boosted action circle, two foci and parabolic seat

**Date:** 2026-11-17 Eastern. **Lane:** Gravity/Cone. **Status:** [D] ellipse/parabola/hyperbola classification under arbitrary 3D cutting-plane tilt; [D] intersection of two congruent displaced null cones is a planar conic or degenerate section, with the timelike future/past causal diamond producing a Lorentz-boosted circle; [D] projected ellipse's two spatial foci are the two cone apex locations; [D] exact rest-frame circle and sech/rapidity coordinate dictionary; [D] row/column acceleration parabolic planes intersect at the paired lift poles of an anti-diagonal circle; [N] no dynamical acceleration/action quantization, G-free new gravitational response or physical frequency selected; [O] translate this exact cone-intersection geometry into a sourced Einstein–Maxwell/K4 action operator or conserved physical stress-energy. **Immediately pre-ledger live HEAD:** f7ef7184d544fd51ca2e65fed2487a2052883c10. Collision check: External Audit owns v15.1119, v15.1120 is Audit liveness, Gravity v15.1121 ledger and scripts unique. Additive-only; no earlier certified, Suzuki, Audit, Sandbox or Muse objects modified.

## Motivation and earlier comparator
User observes that two-degree-of-freedom tilting applies just as much to the acceleration/deceleration parabolic and hyperbolic cutting planes as to ellipses, and asks about **3D geometry intersections**, especially in the established acceleration/boost/action-circle dictionary. Unmodified archived PaperA Cutting Plane Theorem already classified planes in the two-sided AM–GM cone X²+Y²=T² and the row/column/fixed-T constructions. Gravity v15.1117–1118 already added arbitrary two-component tilt for ellipses and derived their standard spin-2 Maxwell-stress rotation. External Audit Round 597/v15.1119, commit 362a48a1b6ad7258f57ad53948cbdeb8db23e49c, rederived and executed v15.1114–1118 scripts, all PASS. Latest checked HEAD before this gate contained Audit liveness v15.1120. This gate is **not** a re-proof of PaperA; it studies the new coincidence **two distinct displaced *null-cone surfaces* intersect in exactly a cutting-plane conic**, and physically distinguishes a Lorentz boost of the event frame from the purely oblique viewing shear of Gravity v15.1115.

## Gate 1009 — full tilted-plane classification and 3D intersection dimension
Let the positive upper null cone \mathcal N be T²=X²+Y², T>0. A cutting plane can be written **T+aX+bY=C**. Put s=sqrt(a²+b²), and rotate transverse coordinates so X_parallel=(aX+bY)/s, Y_perp=(-bX+aY)/s. The plane is T+s X_parallel=C. Its intersection is:
- **s<1**: bounded ellipse, centered in transverse projection at -C(a,b)/(1-s²), including the s=0 fixed-height circle;
- **s=1, C≠0**: nondegenerate parabola, e.g. Y_perp²=C²−2C X_parallel; the factor-grid row/column acceleration parabolas are reflection-related instances;
- **s>1, C≠0**: open hyperbola, with positive-T physical branch restrictions; at zero T-plane coefficient one recovers a vertical-plane hyperbola;
- **C=0**: apex-through-plane sections have degeneracies (ray or pair of generator rays depending on plane and sheet), so a zero-offset null plane is *not* automatically a nondegenerate parabola.
The polar representation of a generic section, where the denominator is nonzero and T positive, is T=r=C/[1+a cosφ+b sinφ], X=r cosφ, Y=r sinφ. A second distinct plane meets the first in a straight line, whose intersections with \mathcal N number at most two isolated real points, except a shared generator or coincident plane degeneracy. No physical cross-section interaction follows simply from that algebra.

## Gate 1010 — two displaced congruent null cones intersect in a plane
Place apex A at (T,X,Y)=(0,0,0), and apex B at (t0,ℓ,0), with coordinates in units c=1 and Minkowski spatial transverse axes X,Y. Their full double-null cone surfaces satisfy
F_A=T²−X²−Y²=0,
F_B=(T−t0)²−(X−ℓ)²−Y²=0.
Subtract:
**F_B−F_A=−2t0 T+2ℓ X+(t0²−ℓ²)**.
Therefore their common locus lies in the precise cutting plane
**T−(ℓ/t0)X=(t0²−ℓ²)/(2t0)**, for t0≠0.
The timelike/spacelike/null distinction of apex displacement controls the resulting conic:
- timelike t0>|ℓ|, t0>0: intersection of **future** of A with **past** of B is a closed ellipse on the original cone;
- spacelike example t0=0, ℓ≠0: the plane X=ℓ/2 and first future cone give T²−Y²=ℓ²/4, a hyperbola;
- null example t0=ℓ>0: T=X and Y=0 on first cone, a **degenerate common generator**. Importantly this is *not* the nondegenerate s=1,C≠0 parabola because the apex separation forces C→0 at the null limit.
To obtain a nondegenerate parabola as a limit of timelike-separation cone intersections, s=ℓ/t0→1 while holding plane intercept C=(t0/2)(1−s²) finite requires t0→∞, not a finite null-separated pair. A finite pair of identical null cones does not by itself generate a standalone nondegenerate parabola when apex separation becomes null.

## Gate 1011 — the exact boosted rest-frame circle and two spatial foci
For t0>|ℓ|, let invariant apex proper-time separation in length units be **τ=sqrt(t0²−ℓ²)**, boost ratio **v=ℓ/t0**, and γ=1/sqrt(1−v²)=t0/τ. In the common rest frame of the two apex events, their future/past cone intersection is the fixed time slice T_rest=τ/2 and hence the spatial **circle of radius R_rest=τ/2**. Lorentz-boost its points, parameterized by ordinary rest-frame angle χ:
**T=(t0/2)+(ℓ/2)cosχ**,
**X=(ℓ/2)+(t0/2)cosχ**,
**Y=(τ/2)sinχ**.
This satisfies both null-cone equations and the derived cutting plane identically (symbolically checked). Its XY projection is an ellipse centered at (ℓ/2,0), semi-major A=t0/2, semi-minor B=τ/2 and projected eccentricity **e=|ℓ|/t0=|v|**. Because A²−B²=ℓ²/4, the ellipse's spatial foci are precisely **X=0 and X=ℓ**, the projected locations of the two apex events. In fact for each point on the causal intersection, its two spatial focus distances are |(X,Y)|=T and |(X−ℓ,Y)|=t0−T, so their sum is identically **t0**. The locus is therefore the ordinary two-focus ellipse defined by two equal-speed light rays joining the two events, not merely an arbitrary cutting-plane equation.

This gives an exact, physical-geometry **Lorentz boost** behind the owner's ellipse tilted in T: in its rest frame the circle is at one time T_rest=τ/2, while in the lab the same circle spans T=t0/2+(ℓ/2)cosχ. The center in spacetime is the event midpoint (t0/2,ℓ/2). The lab XY center is ℓ/2; only the rest-frame circle is centered at spatial origin when the apex events share one spatial location. **Do not confuse this Lorentz coordinate transformation with the freely chosen oblique projection U=X+qT of v15.1115**: one is a symmetry of the null-cone metric and a change of inertial frame, the other a visualization map.

## Gate 1012 — rapidity/sech dictionary and its two different meanings
On the rest-frame **upper** semicircle use a real projective parameter u with cosχ=tanh u, sinχ=sech u. Then the boosted intersection becomes
**T=(γτ/2)[1+v tanh u]**,
**X=(γτ/2)[v+tanh u]**,
**Y=(τ/2)sech u**.
Thus the same tanh/sech circle parametrization appears *exactly* in the 3D two-null-cone causal intersection. However two quantities must remain distinct:
1. **v=tanh η** is a *constant* physical frame boost fixed by the chosen separation of the apex events, with rapidity η=artanh v.
2. **u=artanh(cosχ)** is a variable geometric coordinate locating points on the rest-frame action-circle-shaped intersection; u does not give physical elapsed time along the spatial curve unless a separate clock/equation of motion is supplied.
The invariant circle radius R_rest=τ/2 is a **length/time-coordinate scale** of the given events. Calling it the Cone 'action circle' is a structural geometric correspondence. It does **not** establish R_rest=ℏ/(mc), an electron orbit, an atomic transition rate, energy quantization, measured G, or other physics: those require extra action normalization and source dynamics. A nontrivial physically selected boost/τ would likewise have to arise from the underlying current, wavefront or matter model.

## Gate 1013 — the intersecting acceleration/deceleration parabolas mark the balanced action-circle poles
Archive PaperA's reflected row/column plane cuts are **T+X=k** and **T−X=k**, with fixed factor x=k and y=k respectively. Each cuts \mathcal N in a projected parabola
Y²=k²−2kX and Y²=k²+2kX.
Intersect the **two planes simultaneously**: T=k, X=0. On the two-sided cone, their common points are
**(T,X,Y)=(k,0,+k)** and **(k,0,−k)**.
These are the two lift-reflected poles of the fixed-T=k anti-diagonal circle X²+Y²=k², and the factor pair at each is balanced x=y=k. Factor exchange X→−X fixes both common points; lift exchange Y→−Y swaps them. This is the exact crossing/seat relation behind the earlier row-column acceleration-parabola dictionary. Note k labels factor length and the tangent row/column vertices lie at X=±k/2; the circle radius here is k. Choosing mesh values k=1 and k=1/2 reproduces the old vertex offsets ±1/2 and ±1/4 geometrically, but does **not** identify the gravitational mesh Casimir with the EM +1/4 Casimir, supply timing, or select a force law.

## Gate 1014 — intersection of three cones yields discrete states, not dynamics
Because subtracting any two congruent translated null-cone equations yields a linear plane, **three** such cone surfaces yield two linear cutting planes whose common intersection with a base cone generically has at most two points. Explicit reproducible witness: apex events A=(0,0,0), B=(4,0,0), C=(4,1,0). Their common points are **(T,X,Y)=(2,1/2,±sqrt(15)/2)**. Both lie on A's future branch and B,C's past branches, and all three cone equations vanish. This is an exact discrete two-lift constraint intersection. Generic additional cone conditions may eliminate both points; intersections are geometric algebraic constraints and do not imply particle collisions, a selected physical K4 excitation or a novel arithmetic divisor function.

## Reproducibility, results and next gate
Primary executable `research-notes/k4_3d_null_cone_intersections_boost_action_circle_v15_1121.py`, commit **d711b3fc99effa4d2560a095b45b1920120d86e0**: SymPy checks cone subtraction, exact Lorentz-boosted circle and midpoint plane, sech parametrization, three-cone two-point example, spacelike hyperbola and null-ray degeneracy. Supplement `research-notes/k4_parabola_action_circle_intersection_v15_1121.py`, commit **f7ef7184d544fd51ca2e65fed2487a2052883c10**: verifies reflected parabolic-plane crossing at the two balanced-circle poles and the two distinct X/Y involutions. Both equivalent scripts independently executed locally before GitHub create_file, PASS. Independent Audit of committed-byte gate pending.

**Positive:** the user's proposed 3D intersections unify several old Cone elements in one exact construction: physical causal pair of light cones → tilted cutting plane → Lorentz-boosted circle / projected ellipse → two spatial foci at the apex locations → tanh/sech coordinate dictionary. Independent reflected parabolas intersect at the balanced factor/action circle poles. **Negative:** the geometry determines no material/GW phase, length selector or gravitating source; the timelike light-cone pair's ellipse is an exact standard Minkowski causal-diamond result, not a new Cone gravitational law. The general s=1 parabolic cut does **not** follow as a finite null-apex collision because that collision is degenerate.

**AUDIT HANDOFF:** verify chronology and external Audit Round 597, subtracting cone equations and branch restrictions, focus distance sum, timelike/spacelike/null classification including null generator and parabolic infinite-apex limit, gamma/boost sign, χ versus u/η distinction, full 3-cone two-point witness, row/column pole plus lift/factor involutions, and that an algebraic action-shaped circle is not an independently quantified ℏ-scaled physical orbit.

**NEXT:** test a **physically normalized pair of source/detector null cones** against the finite v15.1102 retarded field and the fixed magnetoelastic actuator: do distinct accelerated-source null wavefronts intersect at causal diamond sections with any *new invariant* timing/spectral relation? Compare the exact same geometry under conventional Einstein–Maxwell and the frozen K4 EH+solid action. A free apex separation (t0,ℓ) and free magnetic/current support cannot be relabeled a frequency or G-free observable without field equations.
