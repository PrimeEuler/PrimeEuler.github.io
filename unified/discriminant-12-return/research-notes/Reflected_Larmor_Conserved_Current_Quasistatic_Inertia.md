# Reflected Larmor circles: conserved electromagnetic source and quasistatic inertia

Date 2026-10-25. Parents v14.863, v14.870. Gravity/bicone add-only lane.

## Exact conserved model [D conditional source choice]
Let ξ=δ/u, |ξ|<1, centers rσ(t)=(σ Rξ,R sqrt(1-ξ²)cosφ(t),R sqrt(1-ξ²)sinφ(t)), σ=±1, carrying qσ=σq and identical smooth normalized finite-width Gaussian blobs f_a(r)=(2πa²)^(-3/2)exp(-r²/(2a²)), a>0. Define ρ=Σ qσ f_a(r-rσ), J=Σ qσ rdotσ f_a(r-rσ). Chain rule yields ∂tρ+∇·J=0 identically and total charge ∫ρ=0. The dipole p=∫rρ=2qR ξ xhat (common transverse orbit drops out). Therefore pddot=2qR/u δddot xhat (within long wavelength limit). Radiated electric dipole power P=(2qR/u)² δddot²/(6π ε0 c³), assuming slow sources and neglecting higher multipoles and spin-rotation sidebands. Pair's magnetic moment and complete Larmor drive are not separately fixed by this neutral co-moving pair. To represent a nonzero charge monopole plus dipole requires another charge/current sector or changed assignments; cannot call this neutral example the Coulomb monopole.

## Linearized polarization/current [D]
At ξ≈0 and in a locally comoving frame freezing φ (or subtracting common fast precession), the source reduces to polarization P(r,t)=gδ(t)f_a(r-r0)xhat with g=2qR/u; ρ=-∇·P+O(δ³) for this symmetric pair, J=∂tP+ terms for moving r0. At ξ=0, opposing charges overlap and cancel; Gaussian regularization avoids any point-charge singularity. The frozen-orbit/quasistatic limit is NOT a proof about the full rotating drive.

## Quasistatic transverse Maxwell inertia [D under low-frequency expansion]
In Coulomb gauge for J_T, a slowly varying transverse current produces A_T(k)≈μ0 J_T(k)/k², yielding a positive transverse magnetic energy at quadratic order
E_B,qs=(μ0/2)∫d³k/(2π)³ |J_T(k)|²/k² = (M_T/2) δdot².
With Gaussian Fourier f_a(k)=exp(-a²k²/2) and J=g δdot f_a xhat,
M_T=μ0 g² ∫d³k/(2π)³ (1-kx²/k²) exp(-a²k²)/k²
=μ0 g²/(6π^(3/2) a) > 0.
Derivation: angular mean (1-cos²)=2/3, radial integral ∫_0∞exp(-a²k²)dk=√π/(2a). This is a magnetic/transverse quasistatic effective kinetic coefficient for the explicitly chosen smeared current. It depends on width a, source assignment q,R and u, not solely geometry. It is not necessarily the complete gauge-invariant internal inertia after electric fields, mechanical stresses, and retarded terms are included. At fixed q,R,a, raw δ mass coefficient scales u^(-2), but normalized ξ mass is scale-independent.

## Sharp limitations [O]
The chosen source is globally neutral; it cannot on its own represent a Coulomb monopole. No physical charge/current assignment derives from bicone SU(2) or KS oscillator algebra. At finite φdot, common orbital motion changes source Fourier spectrum, and δ dynamics may generate sidebands; full retarded Maxwell calculation needed. Maxwell field plus source support stress-energy gravitates ordinarily; no new gravity monopole law/Higgs scalar arises. A causal nonlocal retarded kernel and regulator-independent total mass after supports are essential next steps. The quasistatic magnetic coefficient cannot be read as experimentally observed electron mass.
