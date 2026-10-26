# Finite-Larmor Maxwell seat: exact angular-phase reduction

Date 2026-10-25. Parents v14.878–880. Additive bicone/gravity note; Suzuki/far-tail unchanged.

For circular common center c(t)=R(0,cos Ωt,sin Ωt), let τ=t-t', Δc=c(t)-c(t'), and d=|Δc|=2R|sin(Ωτ/2)|. The *full three-dimensional isotropic angular average* is exactly
(1/4π)∫_{S²} exp[-ik khat·Δc] dΩ_k = sinc(kd)=sin(kd)/(kd), with sinc(0)=1.
This is a resummation of the entire Bessel harmonic content at fixed k and time difference, not a new approximation. For the isotropic Gaussian blob, multiplication by exp(-a²k²) does not affect the angular identity. It directly proves the time-difference dependence of the scalar angular phase kernel.

Additional tensor averages needed for the exactly conserved source follow by differentiating I(k,Δc)=4π sinc(kd):
∫dΩ_k khat_i exp(-ik khat·Δc) = (i/k) ∂_{Δc_i} I;
∫dΩ_k khat_i khat_j exp(-ik khat·Δc) = -(1/k²) ∂_{Δc_i}∂_{Δc_j} I.
Signs are fixed by ∂_Δ exp(-ikhat·Δ)=-ik khat exp(...). Consequently every angular integral with the transverse projector P_T=δij-khat_i khat_j, and with kx times tangential v(t), can be written in terms of sinc and first/second/higher radial derivatives. The remaining retarded kernel is a radial k integral and time difference τ integral.

Explicit linear source:
rho1(k,t)=-ig kx f_a(k)e^-ikc(t)δ(t),
J1(k,t)=g f_a(k)e^-ikc(t)[δdot(t)ex−ikx v(t)δ(t)].
The Fourier continuity identity dot rho1+i k·J1=0 holds. Coulomb kernel uses rho1rho1 and instantaneous equal-time part; transverse Maxwell source integrates J_T retarded:
A_T(k,t)=μ0 c² ∫_{-∞}^t dt' [sin(ck(t-t'))/(ck)] P_T(k) J1(k,t'),
with retarded condition. Normalization follows Maxwell equation (∂_t²+c²k²) A_T=μ0 c² J_T. This expression plus Coulomb energy gives a causal quadratic effective field response for any prescribed δ history within the linear source model, and fixes the integral to evaluate numerically without truncating Bessel harmonics.

Crucial caution: although the scalar effective action is stationary after isotropic k integration, projecting the photon vector tensor requires angular derivatives and velocity contraction, NOT simply multiplying the frozen result by sinc(kd). The exact angular phase resummation alone does not evaluate the causal pole or prove the sign of dynamical effective inertia. The rotation is prescribed externally, so mechanical support dynamics remain additional input.

For Ω→0, d→0 and sinc→1; v→0, hence the frozen-kernel v14.873 and pole equation v14.874 are recovered. For Ω≠0, exact time-domain angular reduction may accelerate direct retarded pole continuation with Gaussian k integration. No numerical finite-Ω pole claimed; no gravity, G or Higgs determination.
