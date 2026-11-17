# Cone Derivation Ledger v15.1115 — Tilted cone ellipse as an apparent offset circle within an n+1 circle; long magnetic-pinch pressure equilibrium

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact oblique-view projection mapping the *genuine* tilted-plane ellipse on the AM–GM cone into an offset circle while a fixed-height n+1 circle remains circular; [D] one explicitly radially force-balanced, axially uniform magnetic vortex supported by scalar pressure and external boundary pressure; [N] generic offset top-down XY circles are not automatically plane sections, the perspective is not unique/physical, finite axial confinement still fails scalar-pressure-only balance, no quarter-grid/half-grid frequency or G-free gravitational prediction; [O] locally supported finite magnetoelastic body and derived tidal phase response. **Immediately prewrite live HEAD:** 1ec36582d471ed74d48187e5068da2d8264c585b. Collision checked (v15.1115 free), additive only; no prior certified, Suzuki, Audit, Sandbox or Muse objects touched.

## Previous sources / motivation
User observed that, viewed as circles on the cone, something looking like an offset circle inside the n+1 outer circle could in fact be an ellipse on the three-dimensional cone. The archived PaperA Conic Theorem already identifies general tilted planes as actual ellipses, rows/columns as parabolas and fixed T as circles; Gravity v15.1108 proves the XY projected ellipse has a focus at the cone axis, and Gravity v15.1110–1114 builds its Maxwell magnetic stress and flux-frozen elastic carrier. External Audit Round 596/v15.1113, commit d3e183c29ca8561b3612e82f17616f1d2e02f76e, independently verified Gravity v15.1110–1112. Gravity v15.1114 awaits independent audit. This gate explicitly tests **which view** makes the user's apparent offset-circle statement true and closes the **axially uniform scalar-pressure** branch of the existing finite-axial-pinch objection.

## Gate 994 — precise optical/projective circularization of a tilted cone ellipse
In cone coordinates X²+Y²=T², T>0, cut by T+eX=C, where C>0 and 0<e<1. The ordinary XY orthographic ellipse has
d=-Ce/(1-e²), A=C/(1-e²), B=C/sqrt(1-e²),
and (X-d)²/A²+Y²/B²=1; it is NOT a circle in ordinary XY orthographic projection unless e=0.

Define the physically 3D **oblique linear viewing map**
**U=X+qT, V=Y**, q=(1-sqrt(1-e²))/e, a noncanonical view chosen for this section's eccentricity. On the tilted plane T=C-eX,
U=sqrt(1-e²)X+qC,
so
**(U-U0)²+V² = C²/(1-e²)**,
where **U0=C(1-1/sqrt(1-e²))/e**. The genuine three-dimensional plane section is therefore depicted as a perfect off-center circle of radius r_inner=C/sqrt(1-e²), with center U0.

At the same time the fixed-height section **T=R**, corresponding to outer n+1 circle if n+1=2R in the PaperA factor-coordinate convention, obeys
**(U-qR)²+V²=R²**.
Thus the same viewing map sends the outer cone fixed-T section to a circle centered at qR, and a tilted-section ellipse to an offset circle centered at U0. A genuine nested drawing occurs whenever **C/sqrt(1-e²)+|U0-qR|≤R**. A concrete verified sample: n=5, R=3, C=1, e=2/5 gives q≈0.2087122, inner radius≈1.0910895 and center separation≈0.8538601, hence 1.9449496<3. Note the tilted plane intersects cone at T values different from R: apparent nesting in the view **does not mean the tilted ellipse physically lies on the outer T=R cone circle**, and it does not canonically identify the ellipse with the discrete n+1 divisor shell.

**View dependence / converse caution:** an arbitrarily displaced Euclidean circle in the ordinary XY *orthographic* view, (X-d0)²+Y²=a0², lifts to T²-2d0X+d0²=a0², which is not a single tilted plane relation T+eX=C for generic d0≠0. Consequently not every XY offset circle is a cone plane-section ellipse. The exact positive construction requires the specified oblique projection q selected by e, not a universal rotation, and is a geometry statement, not a derived time/frequency/Maxwell force law.

## Gate 995 — explicitly pressure-balanced ideal long magnetic cylinder
Use a translationally invariant long-cylinder approximation (∂x=0), magnetic circulation B=Bphi(r) e_phi along circles transverse to the x axis, with
**Bphi(r)=b r [1-(r/L)²]²**, 0≤r≤L; B=0 outside, in SI units restore mu0 factors (in the symbolic script mu0=1). This is solenoidal and has regular axis and vanishing B and derivative at the radial surface. Ampere's equation yields axial current
J_x=(1/mu0 r) d(r Bphi)/dr.
The magnetic Lorentz force density is radial,
**F_r=(J×B)_r= -[d(Bphi²)/dr]/(2mu0)-Bphi²/(mu0 r)**.
Static fluid scalar-pressure equilibrium is 0=-dp/dr+F_r, hence p'(r)=F_r. The exact solution with assigned exterior/boundary pressure p(L)=Pext is
**p(r)=Pext+ (b²L²/(10mu0))[1-r²/L²]^5-Bphi(r)²/(2mu0)**.
Its minimum occurs at r=L/sqrt(3):
**p_min=Pext -8 b²L²/(405mu0)**.
Therefore a **nonnegative scalar-pressure profile** is possible if Pext≥8b²L²/(405mu0). All radial Maxwell/Lorentz identities and pressure gradient were verified symbolically. This closes the specific scalar-pressure objection for an *axially uniform* idealized magnetic tube: the v15.1114 no-go concerned **axially localized f(x)**, for which curl of J×B is nonzero; it remains valid and is not contradicted.

A pressure profile and current identity are a magnetostatic equilibrium, not a fully specified conductive medium's equation of state, boundary apparatus or stability criterion. The x-uniform cylinder has infinite total mass/energy unless treated per unit length; a finite apparatus reintroduces ends, currents, interface stresses, stability and radiation/elastic boundary conditions. An axisymmetric ring also has zero integrated co-axial plus-TT stress by the earlier v15.1107 gate, so this solved equilibrium alone does **not** realize a nonzero tidal pump. Making the **elliptic** variant pressure/elastic equilibrated is the next genuinely physical test.

## Gate 996 — result, reproducibility, action gate
The local SymPy reproducer `research-notes/k4_oblique_cone_offset_circle_magnetic_pinch_v15_1115.py`, additive commit **1ec36582d471ed74d48187e5068da2d8264c585b**, was tested locally before upload, exit 0. It checks exact circle-on-ellipse identity (with correct opposite implicit-conic signs), inner/outer circle nesting for n=5, exact Ampere radial force, pressure-gradient balance, boundary pressure and minimum threshold. An initial local assertion incorrectly compared implicit polynomials with matching rather than opposite signs; it was corrected before commit and the passing canonical source uploaded. Independent Audit pending.

**Positive:** the user's apparent offset circle can exactly be a true 3D cone ellipse **from a specific oblique projection**, including an enclosing n+1 fixed-height circle in the very same view. A long magnetic circulation also has an explicit pressure-supported equilibrium with a computable nonnegative-pressure condition. **Negative:** observer geometry remains freely chosen to circularize one given ellipse; no canonical half-grid offset sets e, and pressure-supported circular magnetostatics supplies neither a physical ellipse distortion nor a new tidal observable.

**AUDIT HANDOFF:** verify that q is a *projection shear*, not a physical Lorentz boost, and that the outer T=R circle and inner tilted conic live at different T values. Recheck numerical example n=5 and the non-converse. Verify pressure sign conventions, minimum at r=L/sqrt(3), mu0 factors, current continuity and why the infinite-cylinder limit does not cure finite axial force-balance. Preserve all prior certified and audit objects.

**NEXT:** impose a true off-center/elliptical magnetic equilibrium with explicit finite pressure/shear stress, calculate its current and material support and the TT integrated quadrupole, then compare the observed offset circle in a **fixed** viewing map to assess whether one universal map handles more than one Cone ellipse. A changing q for each ellipse is not a physical fixed observer and cannot generate a robust observable by itself.
