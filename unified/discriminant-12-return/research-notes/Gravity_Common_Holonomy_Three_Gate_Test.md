# Gravity common-holonomy three-gate test

2026-10-23. Gravity lane. Parents v14.620, v14.622, v14.760–761, v14.773–774. Independent finite-dimensional/topological deductions only, not a derivation of a physical EM-to-gravity field intertwiner.

## Gate A. Physical U(1) loop holonomy [D]

For an oriented closed loop C and charged probe q with mechanical momentum one-form p_mech, its semiclassical phase may be written, with a fixed sign convention,
\[
\Theta_C=\hbar^{-1}\oint_C (p_{\rm mech}+qA)\cdot d\ell.
\]
Under gauge change A→A+dχ with a single-valued U(1) gauge transformation, exp(iΘ_C) is invariant. For a circular orbit of radius R at constant tangent p and enclosed flux Φ, single-valuedness of the complete phase yields
\[
\boxed{pR+\frac{q\Phi}{2\pi}=m\hbar}.
\]
This equation is conditional on the physical mechanical phase and gauge connection having this form, and excludes additional spin/Berry/gravitational holonomies. It shows the previously open v14.774 possibility explicitly: gauge flux can shift radius for fixed p. Neither Φ nor p is provided by circle arithmetic.

## Gate B. Gauge holonomy versus gravity spin holonomy [D/O]

For a common loop carrying representations of U(1) and a spin/Lorentz connection, the combined transport is a representation-dependent product of path-ordered holonomies, schematically
\[
U(C)=\exp(iq\Phi/\hbar)\,\mathcal P\exp(-\oint_C\omega_\mu dx^\mu\,J),
\]
up to representation and signature conventions. The U(1) factor is a phase; spin holonomy is generally matrix-valued, not a scalar phase, and need not commute with arbitrary dynamical transports. Merely placing both connections over the same geometric circle does not fix their coupling constants or establish a shared representation. The spin connection is determined by a chosen tetrad/metric, and extracting an unknown G from it requires independent source dynamics or Einstein field equations, where G already appears. The topological magnetic charge quantization qg=integer multiple of ħ/2 in conventional monopole units constrains a *product* and cannot independently determine q and g.

## Gate C. Double-cover/quarter-offset selector check [D]

On the circle, single-valued scalar angular wavefunctions give integer momentum eigenvalues mħ; anti-periodic boundary condition gives (m+1/2)ħ. Under the general twist \(\psi(\varphi+2\pi)=e^{2\pi i\alpha}\psi(\varphi)\), eigenvalues are
\[
\boxed{J_m=\hbar(m+\alpha)},\quad \alpha\in[0,1).
\]
A fixed, nontrivial Z2 holonomy selects alpha=1/2. Squaring a half-shift produces
\[
(m+\tfrac12)^2=m(m+1)+\tfrac14,
\]
matching the exact AM/GM consecutive-pair quarter square of v14.620. This is a precise algebraic bridge between spin-structure/twisted winding and the quarter *correction*. It is not an identification of the quarter *parabola vertex* with a quarter *flux*: a vertex at 1/4 is a coordinate of the grid, not a holonomy angle, and the two remain distinct.

Moreover, even fixing alpha=1/2 leaves the circle radius R free in the kinetic spectrum
\[
E_m=\frac{\hbar^2(m+\alpha)^2}{2MR^2}
\]
for a nonrelativistic particle of mass M on a circle. Topology fixes an offset, not the physical radius or G.

## Gate D. Fixed common action normalization does not fix relative coupling [D]

The compactness and winding spectrum of a U(1) connection fix the allowed charge lattice only after the representation unit q0 is chosen; multiplying the continuous kinetic action coefficient (1/4g²)∫F² by a positive scalar leaves the topological holonomies and bundle quantization conditions intact while changing local dynamics. Thus one shared phase quantum ħ and even identical loop-holonomy spectra cannot determine g_EM or G. In a gravity theory curvature/metric dynamics provides an independent response normalization; for Einstein-Hilbert this carries c³/(16πG). Requiring a shared circle does not compute it.

## Next physical test [O]

To turn the bridge into a selector: derive a common normalized phase-space symplectic form for both sectors and one fixed, independently measurable dynamical quadratic form or susceptibility (not inserted measured couplings). Check whether these data break the pR scaling and the independent gauge-field kinetic normalization. A quantum-holonomy state-count comparison is not sufficient.

No actual physical half-grid selection, G, EM coupling or Suzuki trace identification is claimed. Existing Suzuki and far-residual certification artifacts remain untouched.
