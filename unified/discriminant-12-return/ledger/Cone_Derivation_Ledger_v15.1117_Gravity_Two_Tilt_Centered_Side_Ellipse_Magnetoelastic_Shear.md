# Cone Derivation Ledger v15.1117 — Two-axis tilt of cutting planes, side-centered T-tilted ellipse, spin-2 response and supported elliptical magnetic pinch

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] general normal-vector tilt of a plane cutting the AM–GM cone yields exact two-parameter ellipse magnitude/orientation and a precise X-centered-but-T-tilted side-view case; [D] TT magnetic quadrupole rotates by doubled ellipse angle; [N] a rigid rotation at fixed shape and unchanged apparatus is standard spin-2 covariance, not a new force/coupling; [D] one explicit two-dimensional **periodic**, linear-elastic, spatially inhomogeneous material stress solution balances the non-pressure-gradient Lorentz force of the smooth compact elliptical current to numerical accuracy; [O] isolated finite three-dimensional current/elastic boundary conditions, fully self-consistent induction/current sources and GW/K4 ADM response. **Immediately prewrite live HEAD:** bd99e30d44ba03901baf6f86fe64ccad557dce78. Collision check v15.1117 free; additive-only, no certified/foundation, Suzuki, Audit, Sandbox or Muse files modified.

## Parent work and latest independent Audit
The archived PaperA Cutting Plane theorem gives the plane conics ax+by=c on the AM–GM cone and intrinsic ellipse axes. Gravity v15.1108 extended their projected offset-focal ellipse and sech coordinates; Gravity v15.1110–1114 explored a compact supporting Maxwell stream field, time-dependent shape inertia, a frozen-flux affine material map, and a strictly conditional anchored parametric oscillator. Gravity v15.1115 showed a **view-dependent** oblique projection of a cone ellipse may look like an offset circle inside a fixed-T n+1 circle. Gravity v15.1116 showed a **smooth, elliptic, compact** magnetic pinch has Lorentz-force curl obstructing scalar-pressure-only equilibrium. Latest completed independent external Audit at this HEAD search is Round 596/v15.1113 (commit d3e183c29ca8561b3612e82f17616f1d2e02f76e), verifying Gravity v15.1110–1112; v15.1114–1116 are still pending. This gate implements the owner's proposed *second tilt degree of freedom*, including an ellipse centered along X in side projection despite being tilted in T, and builds a concrete elastic shear solution to v15.1116's pressure no-go.

## Gate 1000 — general plane tilt makes orientation independent of eccentricity
On the upper cone T²=X²+Y², T>0 consider a real cutting plane
**T+aX+bY=C**, with C>0 and s²=a²+b²<1.
Eliminate T:
(C-aX-bY)²=X²+Y².
In matrix notation r=(X,Y)^T, w=(a,b)^T, this is
r^T(I-ww^T)r+2C w^T r-C²=0.
The transverse projected ellipse has center
**r0= -C w/(1-s²)**,
with principal semiaxes
**A=C/(1-s²)** in the w direction and **B=C/sqrt(1-s²)** perpendicular to w, and projection eccentricity **e_proj=s**. One focus is precisely at the cone origin. Its intrinsic three-dimensional plane-section eccentricity is different, **e_intrinsic=sqrt(2)s/sqrt(1+s²)** (the PaperA expression in a rotated axis). Set a=s cos beta,b=s sin beta: the **tilt magnitude s** controls the projected axis ratio and focal displacement, while **tilt azimuth beta** rotates the ellipse in the cone circle view. This is a real two-parameter geometry at fixed C, not two physical forces. Neither angle nor size is selected by a lattice half-step or quarter-step.

## Gate 1001 — an ellipse can be X-centered in a T-tilted view without being centered in XY
Set a=0 and b≠0. The plane reads **T+bY=C**, so it tilts in the T/Y plane even though it is invariant under X→−X. The transverse projected ellipse has **X0=0** and **Y0=−Cb/(1-b²)**. In the (X,T) side view this section is centered in its X coordinate, whereas in the complete (X,Y) circle view its center is shifted along Y. A genuinely **XY-axis-centered** noncircular ellipse is impossible for a single plane T+aX+bY=C intersecting the ordinary centered cone with C≠0: r0=0 implies a=b=0, which is the circle T=C. The center of the intrinsic ellipse *within its own cutting plane* is another coordinate object, generally at nonzero T, and must not be confused with the XY center. This resolves the proposed additional T-tilt example without contradicting the earlier focus-offset identity. Fixed-T=n+1 circles remain distinct horizontal sections; a tilted plane section appears otherwise only after selecting a particular viewing projection as in v15.1115.

## Gate 1002 — the tilt azimuth becomes the magnetic tide's polarization angle
Embed the projected ellipse and its magnetic stream-function current from v15.1110 in a physical y,z transverse plane, with the angular placement treated as a correspondence assumption. Let I2 be its integrated anisotropic spatial Maxwell stress eigenvalue difference in principal axes. Rotate its axes through beta. Under spatial rotation, the transverse stress transforms S→R(beta) S R(beta)^T, so the two gravity-wave TT channels are
**I_plus=I2 cos(2 beta)** and **I_cross=2 S_yz=I2 sin(2 beta)**.
For the earlier compact magnetic stream family,
**I2/U_B = -2s²/(2-s²)**, with our sign and principal-axis convention.
A GW with plus h_plus and cross h_cross couples through their standard TT contraction, schematically
P_ext=−1/2[hdot_plus I_plus+hdot_cross I_cross].
Changing beta rotates sensitivity between polarizations, while the invariant sqrt(I_plus²+I_cross²)=|I2| does **not** change. Thus beta is physically a device orientation or relative-polarization coordinate: this is a useful **experimental handle**, not automatically a new independent observable, and the cone geometry does not set beta. The actual material stress and moving boundaries also gravitate and contribute to a correctly sourced detector; the Maxwell-only expression is not the whole device response.

## Gate 1003 — solve the smooth magnetic pinch's missing elastic shear equilibrium
To address v15.1116's pressure-only obstruction, consider a **2D x-independent** magnetic current supported by a periodic, isotropic, Hookean elastic medium in the transverse y,z plane. Choose a smooth compact elliptical flux function
Ψ(y,z)=[1-q(y,z)]_+^4, q=((y-d)/A)²+(z/B)²,
with illustrative A=1.4,B=0.9,d=0.45 and finite support well inside a square periodic cell of side 12. Set mu0=1. Then B=(Ψ_z,-Ψ_y), Jx=−Δ⊥Ψ and Lorentz force density
**f=J×B=−(Δ⊥Ψ)∇⊥Ψ**.
This generally has a nonzero curl and cannot be balanced by scalar pressure alone. But a *shear-carrying elastic stress* can balance it.

Let a 2D elastic displacement be u=(u_y,u_z), Lamé material constants λ=3, μ=2, with stress σ=λ (∇·u)I+2μ sym(∇u). The equilibrium equation is the well-posed periodic Navier system
**μ Δu+(λ+μ)∇(∇·u)+f=0**.
In Fourier components at wavevector k≠0,
**u_hat(k)=[ f_hat(k) − ((λ+μ)/(λ+2μ)) k(k·f_hat)/|k|² ]/[μ |k|²]**,
setting zero translation mode u_hat(0)=0. The magnetic force has zero total integral and is compatible with periodic equilibrium. A 144×144 FFT calculation in the finite periodic cell found:
- relative force-equilibrium residual **2.3576719320137904×10^(-16)**;
- stored Hookean strain energy **0.23546916628460893** in chosen units;
- half Lorentz force–displacement integral **0.23546916628816347**, agreement within 4×10^-12;
- unnormalized nonzero integrated magnetic plus TT stress **−1.6384715098949827** in the same chosen units.
The energy equality is the ordinary positive linear-elastic work theorem, **not** a net pump energy supply, a constitutive mechanism for maintaining Maxwell current, or an isolated gravitational-wave prediction.

**Limitations are substantive:** the periodic box is not a finite isolated body; the constructed elastic displacement is the solution to a *fixed imposed Lorentz-force source*, not an affine material flow that automatically preserves the exact cone-ellipse field-line labels. The current is assigned by Ampère from Ψ and not derived from mobile charge carriers or a complete conductor action. There is no pressure-only equilibrium but there **is** a standard shear-supported equilibrium of this idealized linear model. For a fully coupled device one must feed the displacement back into induction, current, charge conservation, boundary tractions, and the gravitational source; the axial end problem and 3D spatially supported stress remain open.

## Gate 1004 — verdict and audit
**Positive:** the user's extra cutting-plane freedom is an exact orientation degree of freedom, and its tilt direction maps to TT plus/cross mixing at twice the angle. An X-centered side-view ellipse may nevertheless be T-tilted and Y-offset on the actual cone, resolving the apparent conflict. An explicit elastic shear equilibrium now supports a compact elliptical magnetic current in a 2D periodic material cell; the earlier scalar-pressure no-go does not block all physical supports. **Negative:** the magnitude and orientation of tilt remain unconstrained geometry, and no G-free, experimentally distinguishable gravitational law results from spin-2 covariance or a forced elastic equilibrium.

Canonical reproducible script `research-notes/k4_general_tilt_magnetoelastic_v15_1117.py`, additive GitHub commit **bd99e30d44ba03901baf6f86fe64ccad557dce78**. The equivalent full SymPy + NumPy FFT source was executed locally before the additive upload: PASS projected center identity, X-centered T/Y tilt, spin-2 stress rotation, exact periodic elastic equilibrium and positive strain energy equality. The canonical committed script contains the same essential test calculations. Independent byte-level Audit is pending.

**AUDIT HANDOFF:** check the plane normal two-degree decomposition, projected versus intrinsic eccentricity, exact impossibility of an XY-centered noncircular planar section, which projection is X-centered, the factor of 2 in cross TT contraction, stress sign convention and spin-2 norm invariance. Re-run the periodic elastic Fourier equilibrium; check zero k force and shear strain-energy equality; flag the distinction between a force-balanced periodic **linear elastic response** and a fully self-consistent flux-frozen nonlinear conducting wall, and do not conflate the T cone coordinate with physical spacetime time.

**NEXT:** construct a fixed-coordinate finite-domain or clamped-body elasticity equilibrium under the elliptic current's Maxwell Lorentz force and impose ideal-MHD induction consistently, then compute normalized total Maxwell+material tidal TT source. Compare exactly the same apparatus with ordinary Einstein–Maxwell+elastic-solid and the frozen K4 action. A physically sourced and non-degenerate two-tilt observable—not an arbitrary rotated visualization—is still the discovery gate.
