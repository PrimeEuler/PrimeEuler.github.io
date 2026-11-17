# Cone Derivation Ledger v15.1114 — Flux-frozen magnetic cone ellipse, material elasticity, anchor-selected resonance and local force-balance no-go

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact ideal-MHD frozen-flux kinematics for the existing compact Maxwell cone ellipse, derived material mass/inertial coefficient, quartic free elastic shape energy, and conditional anchor frequency; [N] unanchored linear resonance absent and a purely scalar-pressure equilibrium fails for the finite axially localized circulating field; [C] weak-TT parametric stiffness shift under the same prescribed Maxwell-pump action; [O] local Lorentz-force-balanced material stress, perfect-conductor microscopic constitutive law, actual free-boundary dynamics, K4 ADM source-to-detector. **Live HEAD immediately before ledger write:** 956c1fa5dcb1c614fd3117277f940dcf33301f1f. Collision check: External Audit owns v15.1113, Gravity target v15.1114 is new. Strictly additive; no previous certified, Suzuki, Audit, Sandbox or Muse material changed.

## Provenance, checked audit and physical comparator
Independent External Audit Round 596/v15.1113 (commit d3e183c29ca8561b3612e82f17616f1d2e02f76e) independently recalculated and executed all Gravity v15.1110–1112 scripts, including their exact compact Maxwell stress/energy, time-dependent current and Poynting identity, shape inertia, quartic circular energy and reduced damped work, all PASS with no corrections. The archived PaperA Cutting Plane theorem supplies tilted-cone ellipse, rest/focal offset and sech labels; Gravity v15.1110–1112 supply its *specified* magnetic vector-potential ansatz, not a free-vacuum EM eigenmode. Standard ideal-MHD comparators: UT Austin Fitzpatrick flux-freezing lecture https://farside.ph.utexas.edu/teaching/plasma/lectures/node106.html and University of Wisconsin MHD lectures https://magnetohydrodynamics.physics.wisc.edu/lecture2.html, both state E+v×B=0 as the ideal-conductivity/frozen-flux limit. The present gate explicitly tests whether the **same exact cone ellipse** is kinematically realizable as flux advected by moving material rather than arbitrarily redrawn. It does not infer a new microscopic Ampère force.

## Gate 989 — ideal-conducting affine material carrier, exact frozen flux
Let reference points be (x,Y,Z) in a finite circular cylinder Y²+Z²<C², with a fixed compact x envelope f(x). For |e|<1 define the cone-projected ellipse's semiaxes and rest-center offset exactly:
A(e)=C/(1-e²), B(e)=C/sqrt(1-e²), d(e)=-Ce/(1-e²).
The affine material map is
x_current=x, y_current=d(e(t))+[A(e(t))/C]Y, z_current=[B(e(t))/C]Z.
Thus Eulerian material velocity is v=(0,d_dot+(A_dot/A)(y-d),(B_dot/B)z). The material ellipse label
q_e(y,z)=((y-d)/A)²+(z/B)²
satisfies **(∂t+v·grad)q_e=0 exactly**. With A_EM=(Ψ,0,0), Ψ=ψ0 f(x) F(q_e), F(q)=(1-q)^4 for q<1 and zero outside, the previously derived E=(-Ψ_t,0,0), B=(0,Ψ_z,-Ψ_y) satisfy
**E+v×B=0** exactly, as do div B=0, Faraday's law and Maxwell charge-current continuity from v15.1110–1111. This is precisely standard ideal magnetohydrodynamic flux freezing in a material motion. The Cauchy flux transformation for transverse B reads B_y=(C/B)B_y^reference and B_z=(C/A)B_z^reference, with deformation Jacobian J=A B/C².

**Important positive limitation:** this is an ideal-conducting kinematic completion, not yet a self-consistent elastomagnetic **force equilibrium**. The current and space charge remain those inferred from Maxwell's equations; E+v×B=0 fixes induction but not the force equation rho_m D_t v= rho_e E+J×B+div σ_material, nor the actual conductor boundaries, pressure tensor, elasticity, electron microphysics or energy losses. A fully resistive Ohmic material instead has E+v×B=ηJ, so the ideal frozen-flux construction requires effectively vanishing resistivity/suitable flux-carrying medium.

## Gate 990 — material displacement is first-order translation, second-order elliptic shear
At e=0, d=-Ce+O(e³), A=C(1+e²+O(e⁴)), B=C(1+e²/2+O(e⁴)). The first-order displacement of all reference points is a common translation -Ce in y; the first *elastic internal strain* is O(e²). Let reference material have total rest mass M_mat in the cylinder. Integrating the nonrelativistic material kinetic energy 1/2 ∫rho |∂e position|² e_dot² d³X yields
**M_mat,eff(e)=M_mat[d'(e)²+(A'(e)²+B'(e)²)/4]**,
because a uniform reference disk has <Y²>=<Z²>=C²/4. Thus **M_mat,eff(0)=M_mat C²**. The electromagnetic shape inertia independently obtained in audited v15.1112 is M_EM(0)=K C²/c², where K=U_B(0) is the source's magnetic energy. Their combined reduced inertia is **M_total(0)=C²[M_mat+K/c²]**, within the small-velocity constrained field+material ansatz. This is an *effective coordinate mass*, not a universal electromagnetic rest mass of an electron.

For an isotropic linearly elastic support in the unstrained reference state, use the small-strain energy density W=(λ/2)(tr ε)²+μ ε_ij ε_ij, with transverse uniform strains ε_yy=A/C-1, ε_zz=B/C-1. Integrating over reference material volume V,
**U_el(e)= V[(λ/2)(A/C+B/C-2)²+μ((A/C-1)²+(B/C-1)²)]**
=**V(9λ/8+5μ/4)e⁴+O(e⁶)**.
No e² term appears. Hence a freely translating/deforming ideal elastic body does NOT acquire an ordinary small-amplitude rest frequency from the Cone ellipse. The magnetic field energy is likewise K+K e⁴/8+O(e⁶), already proven in v15.1112. Even adding real linear material elasticity fails the circular small-frequency selector **because the cone's focal relation forces the leading deformation to be a translation**. A finite translation stiffness requires supports, external potentials or independently chosen geometry; no quarter-grid offset supplies one.

## Gate 991 — an anchor selects a frequency; the tidal Maxwell vertex shifts its stiffness
Introduce a physically anchored center potential U_anchor=(κ/2)d(e)², where κ has units of force/length and is an **externally specified** anchor stiffness. Then U_anchor''(0)=κ C², while U_B''(0)=U_el''(0)=0, giving
**omega0²=κ C²/M_total(0)=κ/[M_mat+K/c²]**.
This formula does not select κ, M_mat, C or a universal frequency. For a homogeneous weak plus TT strain h(t) in the same polarization/geometry, retain the **previously used Maxwell** prescribed-metric interaction L_int=(h/2)I_plus(e), I_plus=-K e²/sqrt(1-e²); the reduced potential is U_eff=U_B+U_el+U_anchor-(h/2)I_plus. Its quadratic coefficient is **k_eff=κ C²+K h(t)**. At small e, with an added support damping γ, the restricted shape equation is
M_total(0)e_ddot+γ e_dot+[κ C²+K h(t)]e=0.
An externally imposed sinusoidal tidal modulation could produce ordinary parametric resonance if the pump frequency approaches 2omega0, its amplitude overcomes loss, and the physically supported mode exists; this follows the usual Maxwell+elastic parametric-oscillator comparator, not new Cone dynamics. At e=0 exactly the first-order tidal *force* is zero and an unseeded classical mode remains unexcited. A preexisting static magnetic field is not automatically a finite-e shape seed.

**Gauge/coupling caution:** the material itself also couples directly to spacetime tides. Its material quadrupole in a Fermi local inertial frame is
Q_yy-Q_zz=M_mat[d²+(A²-B²)/4]= (5/4)M_mat d²,
with zero first derivative at e=0. A Fermi tidal potential involving h_ddot times this mass moment is not to be added blindly to the above TT-gauge **Maxwell** interaction: comparison requires one coherent metric gauge and the properly transformed material/wall action. Therefore k_eff=κC²+Kh is a *Maxwell vertex only* comparator, not the full gravito-elastic stiffness of a realizable detector.

## Gate 992 — finite-support magnetic pinch cannot be held by scalar pressure alone
An actual static current feels a Lorentz force J×B. This is not automatically balanced by the above homogeneous elastic strain. In the unperturbed circular case, with locally cylindrical B=B_phi(x,r) e_phi=f(x)b(r)e_phi, the nonrelativistic force density is (μ0 set to 1)
F_x=-(1/2)∂x B_phi²,
F_r=-(1/2)∂r B_phi²-B_phi²/r,
with magnetic curvature/tension term -B_phi²/r. If pressure alone balanced the field, F=-∇p would have zero two-dimensional curl. But
**∂x F_r -∂r F_x =-∂x(B_phi²/r) =-2 f(x)f'(x)b(r)²/r**,
which is nonzero wherever an axially compact field envelope changes. Thus a simple scalar-pressure-only magnetic equilibrium is impossible for this finite localized azimuthal curl. A complete apparatus requires non-isotropic elastic shear stress, surface tractions, current returns or an independently configured material stress tensor. The proposed uniform Hookean ansatz is therefore a **reduced test constitutive model**, not an exact local solution to full Lorentz-force balance. This is a substantive negative result, and must not be hidden by the ideal-MHD induction identity.

## Gate 993 — verdict and reproducibility
**Positive:** the cone's actual offset ellipse can be moved as a frozen-in magnetic flux pattern in an ideal conductor; its translation-dominated first-order deformation, material inertia and quartic elastic energy are explicit. Introducing a real anchor yields the conventional damped tidal parametric oscillator and a calculable conditional natural frequency. **Negative:** neither ideal MHD nor unanchored material elasticity supplies an intrinsic linear resonance or missing physical clock; the localized magnetic pinch cannot be supported by isotropic pressure alone; the full material coupling to GW is not yet treated gauge-consistently; the Cone half/quarter offsets do not fix a new physical parameter. The frozen-flux relationship is established standard ideal MHD (UT Austin/Wisconsin references), not a Cone-only law.

Local test script `research-notes/k4_cone_ellipse_frozen_flux_elastic_v15_1114.py`, additive commit **956c1fa5dcb1c614fd3117277f940dcf33301f1f**. Its algebra was executed locally with SymPy, PASS: material advection, exact E+v×B, Cauchy transform, correct reference-material kinetic integral, quartic linear elasticity, U_B/I_plus zero second/first derivative, anchor omega0², Maxwell-only TT stiffness, material quadrupole and nonzero pinch-force curl. Independent committed-byte Audit pending.

**AUDIT HANDOFF:** validate ideal Ohm sign and advection at finite compact x profile, matter inertia disk averages, the choice of small-strain elastic energy, translation suppression of quadratic stiffness, anchor spring dimensional normalization, matter quadrupole/Fermi versus TT gauge separation, and pressure-only Lorentz force curl. In particular do not portray E+v×B=0 as demonstrating full force equilibrium or the anchor-selected resonance as a prediction of Cone mathematics.

**NEXT:** construct an explicit locally force-balanced 2D (x-independent idealization) azimuthal pinch with scalar pressure, then reinstate finite x dependence with a shear-stress constitutive completion; embed the bound matter stress covariantly and calculate matched tidal response. Alternatively, test whether a physically plausible free-boundary magnetoelastic mode has a nonzero shape frequency and whether any cone-specific ratio survives identical standard Einstein–Maxwell+K4 apparatus calibration.
