# Cone Derivation Ledger v15.1101 — Retarded null wavefront circles from the acceleration/secant hyperbola, with a gravitational tidal-source boundary

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact circular wavefront section of retarded Minkowski null cones from a uniformly accelerated charge's worldline, expressed in the v15.1100 confocal-secants' parameter k; [D] electromagnetic radiation has polar electric and azimuthal magnetic directions on its wavefront; [N] locally co-propagating null Maxwell stress has zero TT projection along its same propagation direction, so magnetic circles do not themselves establish gravitational spin-2 tidal waves; [O] conserved complete accelerated charge + external driving stress, spatially resolved global retarded gravity solution and source-to-detector electric Weyl. **Live HEAD prewrite:** cfdc8fdd7f4ead023a194a2d5cbeb0335e227a1f, reproducible source gate. Collisions checked, v15.1101 free, additive only; no certified/Suzuki/Audit/Sandbox/Muse prior object touched.

## Motivation, ledger precedence and cross-lane scope
Owner interjected **'potentially the tidal wave front'** during the gravity continuation from v15.1100. Earlier v13.196, v13.691 and v15.1053 derived hyperbola/secant to tanh/sech circle; v15.1100 explicitly identified the parameter k=R exp(u) and the constant proper acceleration worldline. Sandbox v15.1084, v15.1091 found the azimuthal magnetic field for a moving charge and an idealized Zitterbewegung circle. Gravity v15.1077–1085 already distinguished Maxwell wave source from TT Weyl and the necessity of scalar/vector constrained stress; v15.1089 showed Maxwell duality no-go. Latest completed independent Audit Round 593/v15.1099, commit 232b5900a66075575db14d93f37bee4e48813838, verified v15.1093–1098. Gravity v15.1100 has not yet been independently audited. The genuinely new link here is a **physical retarded null wavefront section** expressed by the confocal-secant label, not merely a projective coordinate circle.

## Gate 949 — accelerated emission worldline and null wavefront
For constant proper acceleration a>0 in Minkowski spacetime, write R=c²/a and proper rapidity u=a tau/c. The source worldline is
ct_e=R sinh u, x_e=R(cosh u-1), y_e=z_e=0.
This is exactly the secant/hyperbola image in v15.1100:
k=R exp(u), T=(k²+R²)/(2k)=R cosh u, X=(k²-R²)/(2k)=R sinh u, x_e=T-R, ct_e=X.
Every individual emission event (t_e,x_e) has a *future* spherical lightfront
(c(t-t_e))²=(x-x_e)²+y²+z², t>t_e.
A transverse spatial cut at fixed (t,x) yields a circle of radius
r_perp²=y²+z²=(ct-R sinh u)²-[x-R(cosh u-1)]²,
provided the right-hand side is nonnegative and the observation is in the event's causal future. This is an actual constant-time lightfront section, not the rapidity/sech compactification circle or the Euclidean Rindler thermal circle.

Take the specific observation cut (t,x)=(0,0). For a past emitter u<0, equivalently 0<k<R,
r_perp²=R² sinh²u-R²(cosh u-1)²
=2R²(cosh u-1)
=4R² sinh²(u/2)
=**R(R-k)²/k**.
Thus **r_perp = sqrt(R/k)(R-k)** for 0<k<R. This is an exact and directly interpretable connection between the accelerated confocal secant parameter and a circular *radiation-front* section. It is not a unique fixed-radius action circle; changing emission time/label k changes the section's radius. It also retains the previously unresolved scale R=c²/a.

The wavefront sphere is not itself a periodic orbit. Its expanding cross-sectional circles and the hyperbolic-secant *projective* unit circle from v15.1100 are distinct geometric objects; identifying them requires explicit coordinates and maps, not shared circle language.

## Gate 950 — polar E and azimuthal B on the radiation front
At a retarded emission instant, use the source acceleration axis as the polar x direction. For a point charge with acceleration a parallel that axis, the standard Lienard–Wiechert acceleration radiation term has electric polarization in the meridional (n,x-axis) plane and transverse to n, and magnetic direction B_rad=(n cross E_rad)/c along the azimuthal e_phi direction. In the instantaneous rest frame for a given emission event,
E_rad=C sin(theta) e_theta / r, B_rad=(C/c) sin(theta) e_phi / r,
where C=q_e a/(4 pi epsilon0 c²) up to the source/retarded sign convention. In units c_light=epsilon0=mu0=1, set the common scalar amplitude C/r as an arbitrary factor A_front. These algebraic directions obey
n cross e_theta=e_phi,
E_rad dot n=B_rad dot n=0, E_rad dot B_rad=0, |E_rad|²=|B_rad|².
Azimuthal magnetic **directions** are tangent to latitude circles on a fixed wavefront; this is the precise radiation-front reading of the user's curl-circle idea. The instantaneous-rest angular pattern is sin(theta), and local EM radiation energy density falls as 1/r². For a general emission rapidity, the relativistic beaming/retardation prefactor changes; do not infer a globally stationary circular magnetic loop or an accelerating charge's own orbit.

## Gate 951 — null stress does not automatically become a spin-2 tidal wavefront
A locally plane outgoing null Maxwell wave with propagation unit n and radiation field above has
rho=(E²+B²)/2=|E|², S=E cross B=rho n, T_ij=rho delta_ij-EiEj-BiBj=rho n_i n_j.
The TT projector for gravitational wavevector parallel to that **same n** is P=I-n n^T; its rank-two tracefree TT stress is
T^TT_ij=[P_i^k P_j^l - (1/2) P_ij P^kl] T_kl=0.
This is an exact local collinear TT non-source result. It does **not** say a globally angularly distributed electromagnetic radiation pulse sources no gravitational waves: Fourier TT projection of the complete stress over its spatial support and accompanying charges/forces can be nonzero, and an outgoing null shell may generate gravitational memory. The full Einstein/K4 perturbation is retarded and subject to global conservation/ADM constraints. One cannot simply identify a local EM field line or its null front with an independent gravitational electric-Weyl tidal-front amplitude.

In particular a charged body under sustained proper acceleration needs an external driving force; its source stress and the driver's stress must be included in a conserved total Tmunu before evaluating gravitational radiation. A local EM radiation field is spin-1/polarization data; the tidal gravitational Weyl field is spin-2 and not the same object. At the same time, both standard Maxwell and Einstein gravitational waves propagate with local null characteristics, so a causal wavefront correspondence is physically natural without proving new Cone dynamics.

## Gate 952 — reproducibility, verdict and next detector gate
Canonical symbolic source `research-notes/k4_secant_null_em_tidal_wavefront_v15_1101.py` committed at cfdc8fdd7f4ead023a194a2d5cbeb0335e227a1f. **Executed local SymPy equivalence tests before commit:** PASS hyperbola/secant/lightfront radius identity, past-branch k<R, exact e_theta/e_phi orientation, null E/B invariants, rho n n spatial stress and locally co-propagating TT=0. An initial simplification assert on cosh(log(k/R)) required exponential rewriting; corrected before the committed script was written. No first-commit failing reproducer exists for this gate. Independent Audit pending.

**Positive:** the geometric circuit now maps to a real propagating null wavefront section, whose B field has circular azimuthal directions. **Negative:** no preferred transverse radius, physical oscillation frequency, Compton/acceleration selector, universal G or nonzero *Cone-only* tidal operator follows. **NEXT:** construct one finite accelerated current + driver history with a globally conserved Maxwell/matter stress and compute the complete retarded TT source and scalar/vector-constrained Weyl at a remote detector; contrast any outcome against identical ordinary Einstein+K4 solid+Maxwell action. Start with compact acceleration pulses rather than eternal uniform acceleration to avoid unbounded apparatus and radiation idealizations.

**AUDIT HANDOFF:** verify null sphere section with the proper emission branch u<0, k=R exp(u), radius²=R(R-k)²/k, near-front versus far-field source assumptions, E_theta/B_phi orientation, exact local collinear null-wave TT cancellation versus global gravitational wave/memory, and full-source conservation requirement.
