# Gravity: finite-temperature Maxwellian joint generator and survival boundary

Date 2026-10-22. Parents v14.714–719. Producer: gravity_finite_temp_joint_generator.py. All statements below are conditional on EFT v3.4's local isotropic Rosenbluth Fokker–Planck approximation and its adiabatic Kepler averaging.

## Exact local generator [D]

Write specific energy \(h=v^2/2-\mu/r<0\), angular momentum magnitude \(L=|\mathbf r\times\mathbf v|\), \(T=-\mu/(2h)\), \(z=e^2=1+2hL^2/\mu^2\). The velocity drift is \(-A(v)\hat{\mathbf v}\), and \(D=D_\parallel(v)\hat v\hat v^T+D_\perp(v)(I-\hat v\hat v^T)\), half covariance so \(d[v_i,v_j]=2D_{ij}dt\).

The exact **local** h,L drift and covariance (using the 3D Itô curvature of L) are
\[
b_h=-vA+D_\parallel+2D_\perp,\quad
b_L=-AL/v+D_\perp r^2/L;
\]
\[
a_{hh}=2D_\parallel v^2,\quad a_{hL}=2D_\parallel L,\quad
a_{LL}=2[D_\perp r^2+(D_\parallel-D_\perp)L^2/v^2].
\]
The \(D_\perp r^2/L\) term is specifically the out-of-orbital-plane curvature, absent for the earlier planar model.

For \(F=(T,z)\), define Jacobian \(J_{i\alpha}=\partial F_i/\partial(h,L)_\alpha\). Then at each point in the bound Kepler orbit
\[
b_i=\sum_\alpha F_{i,\alpha}b_\alpha+
\frac12\sum_{\alpha\beta}a_{\alpha\beta} F_{i,\alpha\beta},
\quad
a_{ij}=\sum_{\alpha\beta}F_{i,\alpha}a_{\alpha\beta}F_{j,\beta}.
\]
This is a **complete exact constructive specification** of the drift/diffusion coefficients for the local two-coordinate generator; producer computes b_T,b_z,a_TT,a_Tz,a_zz symbolically. Its secular version replaces each coefficient by the physical Kepler time average
\[
\overline k(T,z)=\frac1{2\pi}\int_0^{2\pi}
k\left(r=T(1-e\cos E),\,v^2=\frac\mu T\frac{1+e\cos E}{1-e\cos E},\,L^2=\mu T(1-z)\right)
(1-e\cos E)\,dE.
\]

The mixed coefficient simplifies independently to
\[
\boxed{\bar a_{Tz}=
\frac{8T^3(1-z)}{\mu^2}\langle D_\parallel(v)(v^2-\mu/T)\rangle_{\mathrm{Kep}}.}
\]
It vanishes identically in the constant-diffusion hot limit because \(\langle v^2\rangle=\mu/T\); at finite temperature, generally nonzero. This recovers sandbox v14.716 and audit v14.718, but puts the entire local/averaged generator in one reproducible formula rather than reporting only covariance.

## Forward transport, killing, and conditioning [D]

With coefficient vector \(\bar b=(\bar b_T,\bar b_z)\) and symmetric matrix \(\bar a\), the forward density satisfies
\[
\partial_t p=-\partial_i(\bar b_i p)+\frac12\partial_i\partial_j(\bar a_{ij}p),\qquad i,j\in\{T,z\}.
\]
A survivor density for a given explicitly specified boundary and jump/killing model is \(p_{\rm surv}=p/\int p\). If \(\dot S=-\kappa(t)S\) denotes lost mass then
\[
\partial_t p_{\rm surv}=S^{-1}\mathcal L^*(Sp_{\rm surv})+\kappa(t)p_{\rm surv},
\]
on the surviving domain. This survival-selection term prevents interpreting a killed moment as a survivor moment. The outward probability flux is \(J_i=\bar b_i p-\frac12\partial_j(\bar a_{ij}p)\); escape occurs at h=0 (equivalently T→∞, y=−h→0). The finite-temperature boundary flux and a quasi-stationary distribution remain uncomputed because the v3.4 matched hard-jump/bound-versus-kill prescription changes the near-escape operator.

**Important limitation:** a local diffusion approximation cannot uniquely set the absorbing flux of finite Rutherford kicks across h=0. No finite-temperature numerical stationary/QSD law is claimed, no fabricated numerical values, and no assumption of a universal uniform z marginal. The exact hot joint time-change results of v14.714–718 remain valid in their own limit.

## Structural outcome

Finite-\(\Theta\) cross-covariance is nonzero generically, so the *specific independent-Brownian operational-time decomposition* of the hot model fails. Failure of that factorization does NOT by itself disprove all possible invariant or conditionally stationary shape distributions; such conclusions require a solved forward equation and specified escape treatment.

The bath generator still only evolves orbital energy/angular momentum. There is **no derived bridge** to the independent rotor's static slope ratio \(\Xi=(1-R\Phi''/\Phi')/3\) or an emergent \(G\).

## Next handoffs

Audit: independently verify local 3D L-curvature drift, a_LL covariance, transformed generator in (T,z), physical orbit-average measure and boundary-current sign. Check whether omission of stochastic orbital-phase dynamics at finite temperature is compatible with the secular expansion.

Sandbox: discretize this full averaged finite-temperature two-dimensional forward equation only after choosing explicit bound-preserving or killed boundary conditions; compare with the EFT's BPS exact-hard-jump kernel, not just a diffusion absorber. Track survivor-normalized vs unconditioned shape separately. Return code, convergence checks, negative findings, and no artificial Xi coupling.

Flags: G_derived=false; novel_gravity_field_law=false; finite_temp_joint_generator=DERIVED_FORMALLY; finite_temp_full_QSD=OPEN; physical_killed_boundary=REQUIRES_HARD_JUMPS; far_tail_touched=false; papers_modified=false.
