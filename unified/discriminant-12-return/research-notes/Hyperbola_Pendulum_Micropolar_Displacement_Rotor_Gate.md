# Translation-invariant displacement–rotor (micropolar) bridge

2026-10-24. Gravity subgate. Parents v14.626, v14.826–828. Audit v14.828 verified previous series. No Suzuki/far-tail changes.

Define a 3-vector displacement u(x,t), an independent axial 3-vector microrotation θ(x,t), and mass density ρ_m>0, microinertia j>0. Let e=sym(∇u), dev e=e-(tr e/3)I, and c=curl u. Postulate the parity-even isotropic quadratic action
\[
\mathcal L={\rho_m\over2}|\dot u|²+{j\over2}|\dot θ|²
 - {B\over2}(\nabla\cdot u)²-\mu|\operatorname{dev}e|²
 - {\gamma\over2}|\nabla\times u-2θ|²
 - {K\over2}|θ|²-{A\over2}|\nabla θ|².
\]
Here μ,γ,A,K are nonnegative material moduli and B is bulk stiffness. Pure global translation u→u+a leaves this action unchanged; unlike θ=u/ell from v14.827 the pendulum K pins *orientation only*, not translation. A separate background source is still needed to produce K=Mgl; this is an effective nonrelativistic toy, not covariant GR.

For wavevector q parallel to z, define longitudinal u_L and θ_L, transverse u_T and θ_T. Longitudinal u_L decouples from microrotation because curl ∇φ=0, and obeys
\[
\boxed{\omega_L²={B+4\mu/3\over\rho_m}q²}.
\]
Longitudinal microrotation obeys
\[
\boxed{\omega_{\theta L}²={K+4\gamma+Aq²\over j}}.
\]
For circular transverse helicity σ=±1, curl u_T = σ q u_T in a complex helicity basis with suitably signed amplitudes. The quadratic potential matrix for the pair (u_T,θ_T) is
\[
V_\sigma(q)=\frac12
\begin{pmatrix}u_T^*&θ_T^*\end{pmatrix}
\begin{pmatrix}
(\mu+\gamma)q²&-2\gamma\sigma q\\
-2\gamma\sigma q&4\gamma+K+Aq²
\end{pmatrix}
\begin{pmatrix}u_T\\θ_T\end{pmatrix},
\]
where the μ coefficient is understood with the dev shear normalization used above. Direct Fourier evaluation gives the bare dev-strain transverse potential μq² |u_T|²/2. The two transverse squared frequencies are the eigenvalues of the mass-weighted stiffness matrix diag(ρ_m,j)^(-1/2) V_matrix diag(ρ_m,j)^(-1/2):
\[
\omega_\pm²=\tfrac12\left[a+d\pm\sqrt{(a-d)²+4b²}\right],\
a=(\mu+\gamma)q²/\rho_m,\ d=(4\gamma+K+Aq²)/j,\ b=-2\gamma q/\sqrt{\rho_m j}.
\]
For μ>0, γ>=0, K>=0, A>=0, the transverse stiffness determinant is
\[
q²\big[4\gamma\mu+(\mu+\gamma)K+(\mu+\gamma)Aq²\big]\ge0;
\]
both branches are nonnegative, with one acoustic transverse branch and one optical rotor branch at q=0. When γ=0, rotor and displacement decouple; when K>0 the long-wave acoustic effective shear coefficient is μ+γ K/(4γ+K). If K=0, it is μ; local rotations can relax the rotational shear at zero wavelength.

This coupling does NOT automatically repair a negative longitudinal stiffness: if B+4μ/3<0, a longitudinal gradient instability survives, because the curl coupling vanishes for longitudinal displacement. To reproduce the relativistic w=-1/3 medium of v14.827 one must independently derive the mapping of (B,μ,γ,K,A,ρ_m,j) to covariant stress-energy and relativistic moduli. Naively identifying B=(ρ+p)dp/dρ=-2ρ/9 and μ>=ρ/6 gives marginal longitudinal stability at μ=ρ/6, but local uniform compression still has negative bulk stiffness B<0; dynamical wave stability is weaker than global energetic stability. In particular a mathematically stable K>0 nonrelativistic micropolar material does not imply a complete healthy relativistic cosmology. No G derived.

Next: derive fully covariant isotropic material-scalar action with independent shear invariants and compute scalar/vector perturbations, or independently test constrained finite-wavelength stability with explicit moduli, without claiming pendulum uniquely selects them.
