# Cone Derivation Ledger v15.1060 — Penrose/Milne identification of the secant-circle coordinate and causal null-hinge obstruction

**Date:** 2026-11-16 US Eastern (2026-11-17 UTC). **Lane:** Gravity/Cone. **Status:** [D] exact Milne-null Penrose-coordinate dictionary; [D] conditional Minkowski causal classification of v15.1052 hinge paths; [N] common circle alone is not a Penrose conformal compactification; [O] no physical time/causal metric specified on the actual arithmetic Cone field carrier. **Live HEAD immediately before ledger write:** 9f01e74cbd81da46dff24affdde2fdedb8bff880, canonical reproducer. All changes additive. Do not edit Suzuki, Audit, Sandbox, Muse or foundations.

**Synchronize / prior art:** v13.196 and v13.691 already give real hyperbola-to-circle rapidity compactification; v13.534 mentions a Penrose/projective-null analogy but explicitly leaves conformal identification unproved; v15.1042 establishes signed T/X wedges; v15.1052 gives signed hinge paths; v15.1053-1056 establish secant circle, sign quotient and cotangent lift; v15.1057-1058 physical Maxwell-K4 source restrictions. **External Audit Round 588 landed at canonical v15.1059**, commit 327be861ae7d4cd823515872bfa14a8c5a618628, independently confirming Gravity v15.1052-1058 and collision resolution. Thus this gate is v15.1060, not v15.1059. External contextual source: Izaak Neutelings, "Penrose diagrams of Minkowski and Schwarzschild spacetime", https://tikz.net/relativity_penrose_diagram/ ; standard conformal compactification reference: https://doi.org/10.12942/lrr-2004-1 .

## Gate 873 — the existing Cone coordinates are precisely algebraic Minkowski null coordinates, conditionally

Let u=T+X and v=T-X. Then T²-X²=uv and the *chosen* flat Lorentzian metric is dℓ²=-dT²+dX²=-du dv. The metric is not automatically the physically induced metric of the project's arithmetic factor-plane or K4 action: it is a conditional test embedding.

On u>0,v>0 set rho=sqrt(uv), eta=(1/2)log(u/v). Then u=rho exp(eta),v=rho exp(-eta), T=rho cosh eta, X=rho sinh eta, with exact metric
dℓ²=-d rho²+rho² d eta².
These are ordinary Milne coordinates on the future timelike wedge. Fixed-product shells uv=n are constant rho=sqrt(n) Milne hyperbolas. Their shell parameter n is not physical proper time until a dimensional field identification is supplied.

For u>0,v<0 put epsilon=sgn(v)=-1, rho=sqrt(|uv|), eta=(1/2)log(u/|v|). Both sectors satisfy u=rho exp eta, v=epsilon rho exp(-eta), and
dℓ²=-epsilon d rho²+epsilon rho² d eta².
Thus in the X/spacelike wedge the causal roles of rho and eta swap. The same raw symbol sqrt|uv| is not a physical temporal coordinate on both sheets.

## Gate 874 — the circle is a ratio/rapidity compactification, not a whole Penrose compactification

Define the single upper semicircle angular coordinate theta=2 arctan exp(-eta), 0<theta<pi. Then cos theta=tanh eta, sin theta=sech eta, exactly
x_A/A=(u-|v|)/(u+|v|)=cos theta,
y_A/A=2sqrt(u|v|)/(u+|v|)=sin theta.
Inverting with the extra radial and sheet variables:
u=rho cot(theta/2), v=epsilon rho tan(theta/2).
In the T wedge the metric takes the exact angular form
dℓ²=-d rho² + rho²/sin²(theta) d theta².
The 1D circle projection theta depends only on u/|v| and is unchanged under (u,v)->(a u,a v), a>0. Therefore it drops one independent spacetime coordinate rho; it cannot by itself be a conformal coordinate chart for the 1+1 Minkowski plane.

The STANDARD Penrose compactification independently bounds both physical null coordinates:
U=arctan(u/ell), V=arctan(v/ell), ell>0.
The conformal factor Omega=(cos U cos V)/ell satisfies Omega²(-du dv)=-dU dV exactly (in 1+1 dimensions). Penrose coordinates can be constructed from the FULL triple (rho,theta,epsilon) via
U=arctan[rho cot(theta/2)/ell],
V=arctan[epsilon rho tan(theta/2)/ell].
This is a precise bridge of coordinates, not equality of the circle map and Penrose map.

The circle endpoint theta=0 occurs both as v->0 at fixed finite u (an ordinary finite null line) and as u->infinity, v=n/u->0 along a fixed positive product shell (a conformal boundary limit). These are different Penrose limits; the circle collapses them together. Thus it cannot label i^+, i^0, I^+, etc without restoring rho and causal/spacetime data. Similarly Penrose conformal infinity is NOT the Cone null hinge by analogy.

## Gate 875 — the old v15.1052 fixed-u crossing is an unparametrized PAST-directed null geodesic

The hinge family v_p(t)=-(2t-1)^p, with u=r>0 fixed and p positive odd, has
T=(r+v)/2, X=(r-v)/2.
Therefore for ALL such p,
(dT/dt)²-(dX/dt)²=(du/dt)(dv/dt)=0.
The curve lies on the null line u=r. Because dv/dt=-2p(2t-1)^(p-1) <=0, the chosen orientation is past-directed wherever the tangent is nonzero, even though it traverses from uv>0 to uv<0. For p>=3 the tangent vanishes at t=1/2; the underlying geometric curve is still the same null-line segment, but its parameterization is not regular there. All odd p give the SAME geometric locus, different traversal rates. The height regularity p=1,3,5 in v15.1052 is valid as an arbitrary-parameter coordinate regularity statement, not a distinction between geometrically different curves or physically forced energies.

Under the Penrose mapping U=arctan(r/ell) is constant and V decreases through zero at v=0. This is an ordinary null line on the conformal diagram, not a horizon or singularity. If T is physical time and dℓ² is the physical causal metric, NO future-directed causal worldline can leave the interior u>0,v>0 future wedge to reach u>0,v<0 through decreasing v. Along future-directed causal curves both u and v must be nondecreasing. Reversing the parameter orientation permits a future-directed null curve from X wedge into T wedge, not the other way round. This causality conclusion is conditional on the spacetime embedding; it is not a no-go for independent quantum-sector transitions, a different physical metric, or nonlocal/field-mediated phenomena.

## Gate 876 — implications for Maxwell-K4 and required next test

The previous v15.1058 electromagnetic drive was calculated on physical cavity coordinates (t,z); the Cone factor-plane (T,X) has not been shown to equal those physical coordinates. Therefore no mere Penrose drawing or circle cotangent lift constitutes an intertwiner between the two physical systems. To physically use the Minkowski/Milne picture one must (i) derive a Lorentzian metric and canonical carrier for the Cone variables from K4/Maxwell, (ii) specify physical sign/time orientation and stress-energy, (iii) solve retarded boundary-value/constraint equations for a sourced mode, and (iv) compare resulting operator matrix elements and measurable predictions with standard gravity/Maxwell. If future-directed causal propagation is requested in the conditional flat embedding, the v15.1052 T->X crossing path fails that criterion exactly.

**Reproducer:** research-notes/k4_penrose_milne_circle_causal_hinge_v15_1060.py, commit 9f01e74cbd81da46dff24affdde2fdedb8bff880, executed in independent local Python/SymPy: verified Milne metric, angular metric, 1+1 Penrose conformal factor, radial-invariance of circle ratio and null/past-directed hinge for p=1,3,5,7. PASS. Request independent Audit of physical interpretation and causal orientation. No new G-free dimensionless observable, physical frequency, EM/G interaction or quarter-ladder projector established.
