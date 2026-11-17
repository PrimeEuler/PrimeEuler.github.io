# Cone Derivation Ledger v15.1096 — Acceleration-parabola focus meets the Zitterbewegung radius, but Maxwell curl leaves the circle scale free

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact near-seat relativistic hyperbola osculating parabola and curvature-circle geometry; [C] conditional focal-length equality to Sandbox's idealized Compton/Zitterbewegung loop; [N] no Maxwell selection of magnetic azimuthal-circle radius, no derivation of the Compton acceleration or independent Cone gravitational observable. **Live HEAD immediately prewrite:** d2d8bb46f2b12b52f2c37990d3125883060362ba, this gate's unique reproducer. Collision verified; additive-only, no protected Suzuki, Audit, Sandbox, Muse or old certified artifact altered.

## Prior ledger, handoffs and nonredundancy
Latest independent Audit Round 592/v15.1092 confirmed Sandbox v15.1091 curl/action-circle numerology plus Gravity v15.1089–1090, and verified the older v15.1081 reproducibility repair. Gravity v15.1093 compared actual compact Maxwell curl to the separate charged-seat azimuthal B. v15.1094–1095 established a localized Dirac Gordon spin-current and its sourced magnetostatic field with arbitrary packet width L. Most critically, **Gravity v15.886** already derived the conditional Compton–Rindler closure **R=c²/a=lambda_Cbar=hbar/(mc)**, and proved a free positive scale ratio rho survives, hence this relation is NOT a physical selector. This gate does NOT claim to discover the Compton–Rindler length relation again. Its fresh geometrical observation, motivated by the user's proposed link of acceleration parabolas to curl circles, is that the **osculating parabola's focus is exactly one-half of R**: a useful explicit geometric correspondence to the Zitterbewegung radius from Sandbox v15.1091. The continuing free ratio and circle-plane distinction remain mandatory.

## Gate 933 — exact near-seat parabola, focus, osculating circle
For constant positive proper acceleration a initially at rest, in a flat SR inertial chart define R=c²/a and the longitudinal worldline
x(t)=R[sqrt(1+(ct/R)²)-1].
This is the standard constant-proper-acceleration hyperbola shifted to have its vertex at (t,x)=(0,0). For the length coordinate y=ct,
x(y)=R[sqrt(1+(y/R)²)-1]
=y²/(2R)-y⁴/(8R³)+O(y⁶).
The associated **osculating parabola** is y²=2R x. In standard parabola form y²=4f x, its focal length is
**f=R/2=c²/(2a)**.
The *osculating circle* of this Euclidean chart curve at the vertex has radius
**R_curv=R=c²/a=2f**.
No assertion that the osculating parabola is the exact hyperbolic worldline away from the seat, or that Euclidean curvature of a spacetime coordinate diagram is a coordinate-invariant spacetime curvature. The focus and curvature-circle radius are geometric facts in the *specified* inertial coordinate plane (x,y=ct) with conventional Euclidean plotting metric. The motion's proper acceleration a itself is physical; extracting the diagram's Euclidean focus uses the chosen inertial coordinates.

## Gate 934 — exact conditional match to Sandbox's proposed action circle
Sandbox v15.1091 compared its idealized classical loop to the Dirac Zitterbewegung scales
r_ZB=hbar/(2mc), omega_ZB=2mc²/hbar, r_ZB omega_ZB=c.
At the **independently imposed** Compton acceleration from v15.886,
a_star=mc³/hbar,
we have R(a_star)=hbar/(mc)=lambda_Cbar; consequently
**f(a_star)=R(a_star)/2=hbar/(2mc)=r_ZB**.
This is a precise one-half geometric identity, not just a visual resemblance. The osculating circle has radius lambda_Cbar=2 r_ZB. A radius match alone cannot identify the parabola's focus, a circle of magnetic field lines, and a circulating particle orbit as the same physical structure. Sandbox explicitly marked Zitterbewegung as Dirac interference, not a literal classical charge moving at c.

The free scale of v15.886 is preserved: for arbitrary rho>0,
R(rho)=rho lambda_Cbar, a(rho)=mc³/(rho hbar), f(rho)=rho r_ZB.
No equation here selects rho=1 or even the existence of a rest-mass action orbit. The match's parameter selector is the open physical question, not a derived theorem of the Cone.

## Gate 935 — Maxwell azimuthal curl circles do not select the focal radius
Sandbox v15.1084/1091 established that for the magnetic *velocity field* of a uniformly moving electric point charge, B lies azimuthally around the velocity axis, with circular spatial field lines for all cylindrical radii r_perp. These circular field lines reside in planes **perpendicular to the trajectory**, whereas the acceleration parabola above is drawn in the longitudinal **(ct,x)** spacetime plane. A physical map between the two planes/radii requires additional frame and constitutive information.

A simple fixed-axial-separation representative of the azimuthal profile is B_phi(r_perp) proportional to r_perp/[r_perp²+d²]^(3/2), with fixed d>0. Its radial maximum is at r_perp=d/sqrt(2). Thus any candidate 'privileged' maximum circle depends on observation separation d, not on R=c²/a or hbar/(2mc). For the actually accelerated Lienard–Wiechert field there are acceleration-dependent radiation terms and retarded-time geometry; this toy profile is an explicit *nonselector witness*, not an exact universal accelerated-charge solution. Faraday/Ampere/Stokes circulation is measured by field flux/currents, not the mechanical action integral integral p·dx, which has different dimensions.

Consequently no Maxwell curl law in this comparison uniquely equates the magnetic circulation radius, parabola focus or Zitterbewegung loop. A true physical bridge would need an explicit current distribution and action or boundary condition fixing both the transverse scale and the longitudinal acceleration consistently, with an independent ratio prediction.

## Gate 936 — checks, negative result and next physical selector
Canonical reproducer: `research-notes/k4_acceleration_parabola_focus_curl_circles_v15_1096.py`, additive commit d2d8bb46f2b12b52f2c37990d3125883060362ba. The exact near-seat expansion, parabolic focus, osculating radius, conditional Compton/ZB match, full rho family and elementary azimuthal profile extremum were checked in a local SymPy run. No dimensional measured G or unproved quantization condition inserted.

**Positive:** a clear exact bridge of **geometric lengths** f=c²/(2a) and r_ZB=hbar/(2mc) at the already-stated conditional Compton acceleration, and a factor-two relation to the osculating circle. **Negative:** no unique scale selector, no action-derived Maxwell 'curl circle' at that radius, no charge current at c guaranteed, no new K4 gravity tensor operator. The correlation is a conditional geometric dictionary rather than a derived dynamical identification.

**NEXT:** formulate an actual covariant Dirac-Maxwell packet/worldline action that fixes acceleration and transverse spin-current localization from boundary/spectral data (if possible), then test whether it fixes rho=1. Avoid importing a_star, the charge-loop radius or measured G as a premise and subsequently advertising them as predictions. The complementary negative test is a one-parameter family of consistent transverse currents at arbitrary L with equal magnetic dipole but differing magnetic stress, as already indicated by v15.1095.

**AUDIT HANDOFF:** verify the (x,ct) Euclidean-osculating-parabola focus convention vs Lorentzian physical curvature; factor-two radius and exact rho freedom; magnetic azimuthal field circles are in a transverse spatial plane; Maxwell representative profile extremum is observation dependent; note original v15.886 already found Compton–Rindler equality conditional. No original-certified file edits.
