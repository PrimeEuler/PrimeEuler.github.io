# Cone Derivation Ledger v15.1122 — Two accelerated secant events create a causal boost/action-circle ellipse with independently controlled shape and scale

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] the null-cone causal intersection of two events on the *existing* constant-proper-acceleration / confocal secant worldline produces exactly the tilted-ellipse/boosted-rest-circle of v15.1121; its eccentricity, radius, offset and focal separation are closed functions of the pair of original secant labels; [N] no physical action circle size, acceleration, gravitational source G, real oscillator period or G-free new observable selected; [O] sourced Maxwell+K4 tidal response to accelerated emission/detection and true phase-selection law. **Immediately before ledger write live HEAD:** f50814cf163a0b12d7bc2324cca68a75b9396409. Version collision check for v15.1122 clear; External Audit Round 597/v15.1119 and Audit liveness v15.1120 inspected; v15.1121 Gravity already landed. All commits additive; certified Suzuki, prior Audit, Sandbox and Muse objects untouched.

## Prior definitions and motivation
The user explicitly emphasizes the established **acceleration/boost/action-circle dictionary** for interpreting three-dimensional cone intersections. Gravity v15.1100 (independently audited Round 594) derived the exact confocal unit parabola and constant proper acceleration dictionary:
Y²=k²−2kX, moving secant Y=R, R=c²/a,
T(u)=R cosh u, X(u)=R sinh u and k=R exp u in the auxiliary cone coordinate, with u=a τ_source/c.
In physical flat spacetime with the source initially at rest in the chosen lab frame, the corresponding accelerated worldline is (ct,x)=(R sinh u,R(cosh u−1)); the two descriptions use different coordinate zero-points and X/T labels. Gravity v15.1121 (new, pending Audit) proved that for a timelike-separated pair of arbitrary events, the intersection of the first *future* null cone with the second *past* null cone is an ellipse with one focus at each event's spatial location; in the common rest frame of their apex separation the locus is a circle. This gate inserts **two points from the actual uniformly accelerated worldline**, rather than freely choosing the null-cone apex separation (t0,ℓ), and derives the exact pair-to-ellipse map. It reuses conventional SR; an accelerated source does not change the local null-cone geometry.

## Gate 1015 — chord of uniformly accelerated worldline and relative boost
Let R=c²/a>0, u1=m−δ and u2=m+δ, with δ>0. Source event i is
P_i=(T_i,X_i)=(R sinh u_i,R(cosh u_i−1)),
where T=ct and X=x (length units). Their separation is
**ΔT=2R cosh(m) sinh(δ)**,
**ΔX=2R sinh(m) sinh(δ)**.
Hence the invariant (Minkowski) chord length is
**τ_chord=sqrt(ΔT²−ΔX²)=2R sinh(δ)**, in *length* units.
The boost between the lab frame and the rest frame of the event pair is
**v=ΔX/ΔT=tanh(m)** (dimensionless; physical speed =c v).
Crucial: m is the **midpoint source rapidity**, while δ is half the **proper-acceleration rapidity interval**. The causal ellipse eccentricity is **e=|v|=|tanh(m)|** and its rest-frame circle radius is
**R_circle=τ_chord/2=R sinh(δ)**.
The plane cutting the first event's forward null cone (in relative coordinates T'=T−T1,X'=X−X1) is
T'−vX'=C_cut with **C_cut=τ_chord²/(2ΔT)=R sinhδ sech m**.
The XY-projected ellipse has major semiaxis
A=ΔT/2=R cosh(m) sinhδ,
minor B=R sinhδ,
focal displacement from the ellipse center to each focus |ΔX|/2=R |sinh(m)| sinhδ.
Thus **A²−B²=(ΔX/2)²** exactly. The ellipse's spatial focus points are the source positions x1 and x2, and its center is (x1+x2)/2, as in v15.1121's general two-null-cone theorem. The boosted circle is an intersection of light-front surfaces, not an electron trajectory, an orbit, or a dynamical normal mode.

## Gate 1016 — two original secant labels separate shape and scale exactly
From v15.1100, each source rapidity label maps to k_i=R exp u_i. Therefore
m=(1/2)ln(k1 k2/R²)=ln(sqrt(k1 k2)/R),
δ=(1/2)ln(k2/k1), with k2>k1>0.
Substituting and simplifying gives the *fully explicit* dictionary
**v=(k1 k2−R²)/(k1 k2+R²)**,
**e=|(k1 k2−R²)/(k1 k2+R²)|**,
**R_circle=R(k2−k1)/(2 sqrt(k1 k2))**,
**C_cut=R_circle sqrt(1−v²)**.
Thus the **geometric mean / product** of secant labels determines the pair's boost/eccentricity, whereas their **ratio** determines the invariant circle radius in units of R. These are the same AM–GM pair variables that originally motivated the Cone. For example m=0 corresponds k1 k2=R², v=0, so the ellipse becomes a spatial circle despite the source being accelerated during the interval. Shifting both rapidities by the same amount changes m (therefore eccentricity and lab orientation) while leaving δ (therefore invariant circle radius) fixed. Changing δ at fixed m changes size without changing e. This is exactly the two-free-input split the owner's extra plane-tilt degrees suggested, now realized by physically defined accelerated worldline events.

## Gate 1017 — conditional clock and sech: avoid the false selector
For the source's proper-time separation Δτ_source, δ=a Δτ_source/(2c). Hence
**R_circle=(c²/a) sinh[a Δτ_source/(2c)]**,
which for a Δτ_source/c≪1 tends to c Δτ_source/2, as an ordinary local light-front circle should. This is a *kinematic* dependence on the already supplied acceleration a and source event separation. An actual event-selection mechanism must still determine the two times τ1,τ2 or equivalently the secant labels k1,k2.
The different appearances of rapidity/sech are exact but have distinct roles:
- m controls the physical lab-to-pair-rest **constant** boost v=tanh m and cutting-plane intercept C_cut=R_circle sech m.
- a separate point-dependent u from the χ-parameterization of the rest-frame circle obeys cosχ=tanh u, sinχ=sech u; it is not physical elapsed time around the spatial intersection circle.
- the source acceleration rapidity u_i=a τ_i/c labels each source **event**, and is neither the χ-circle point coordinate nor a periodic oscillator clock.
There is no external period, quantization or genuine action value selected by the geometric circle. In particular the circle radius is set by the freely chosen event separation, and no \hbar, Compton length or Newton G emerges. Identifying an action per cycle from that geometry requires a sourced degree of freedom with a canonical phase-space symplectic form; visual/metric circles alone do not provide it.

## Gate 1018 — relation to parabola/hyperbola intersections and matched controls
The spatial ellipse of two accelerated-source light fronts is a fixed causal-diamond intersection, not the accelerated worldline itself. The confocal row/column **parabolas** provide the *event labels* k_i and physical worldline acceleration once the acceleration scale a is supplied, while **null cones** from those two events produce the Lorentz-boosted **action-circle-shaped** intersection. This closes the geometry-only dictionary
confocal acceleration parabola → event rapidities/secant k1,k2 → relative boost → 3D null-cone cutting-plane ellipse → rest-frame circle → sech coordinate.
The same construction follows from ordinary flat Minkowski geometry and applies with identical kinematic form to Einstein–Maxwell/K4 wherever the local null propagation relation is unchanged. A genuinely distinctive physical prediction would have to derive either (i) a law fixing a and the source event separation from a Cone action/mesh, (ii) an altered characteristic null propagation/polarization operator, or (iii) a sourced measurable tidal/EM response beyond matched GR+elastic comparator, none shown here.

## Reproducer, audit and verdict
Canonical script `research-notes/k4_accelerated_secant_pair_causal_circle_v15_1122.py` committed **f50814cf163a0b12d7bc2324cca68a75b9396409**, with exact SymPy assertions for all chord/boost/axis/focus/sech/secant-label identities, including frame-shift invariance of R_circle. An equivalent full local script was executed and passed all tests, after fixing a **SymPy rewrite simplification limitation**: tanh(log(expression)) requires rewriting in exponentials for a canonical zero assertion, not a change to the mathematics. Independent committed-byte Audit pending.

**Positive:** this is a new fully explicit bridge *within our research ledger* from the earlier acceleration secant map to the literal 3D intersection of two physical causal cones, eliminating arbitrary ellipse tilt and radius **conditional on the two selected source events**. **Negative:** the event pair and acceleration still supply all continuous parameters, and a Lorentz-boosted causal circle is established special relativity, not a Cone gravitational law or electromagnetic parametric generator.

**AUDIT HANDOFF:** independently rederive the exact worldline chord, boost v=tanh m, invariant radius R sinh δ, plane offset R sinhδ sech m, pair-label product/ratio dictionary, coordinate-zero shift between v15.1100 cone coordinates and physical worldline, event-foci interpretation, rapidity distinctions and small-δ limit. Verify the parent v15.1121 null-cone intersection plane, three-cone discrete intersection and null-degenerate versus nondegenerate parabola classification. Do not equate R_circle to a quantum action radius or interpret constant-rapidity midpoint as frequency.

**NEXT:** insert a pair of events from the *finite acceleration pulse* v15.1102 and test how its retarded electromagnetic wavefront and local tidal GW detector surfaces line up, then compare any dimensionless causal intersection invariant to ordinary Einstein–Maxwell and the same frozen K4 elastic-solid model. This must preserve full source conservation/driver caveats and cannot assume flat null-cone geometry by itself fixes a parametric phase.
