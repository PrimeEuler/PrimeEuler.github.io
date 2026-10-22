# Gravity: full orbit-averaged hot-bath joint generator and operational-time factorization

2026-10-22. Reuses source-checked coefficients from v14.710–713, with exact zero cross-variation from Gravity_Quadratic_Moments_and_Crosscov.md.

Let \(z=e^2\), \(C(T)=10D_0T/\mu\), and let \(f(T,z)\) be smooth compactly supported on \(T>0,0<z<1\). The orbit-averaged hot-bath generator is
\[
\mathcal A f=C(T)\left[
\frac75 T f_T+\frac25 T^2 f_{TT}
+(1-2z)f_z+z(1-z)f_{zz}
\right].
\]
Derivation: \(b_T=14D_0T^2/\mu\); quadratic variation \(a_{TT}=8D_0T^3/\mu\); \(b_z=C(T)(1-2z)\); \(a_{zz}=2C(T)z(1-z)\); \(a_{Tz}=0\) after Kepler averaging (previous exact note). No other joint terms remain in the assumed secular high-speed diffusion.

Under \(u=\ln T\), \(T∂_T=∂_u\), \(T²∂_{TT}=∂_{uu}-∂_u\), giving
\[
\boxed{\mathcal A=C(T)\left[\partial_u+\frac25\partial_{uu}+(1-2z)\partial_z+z(1-z)\partial_{zz}\right].}
\]
With operational clock \(d\tau=C(T_t)\,dt\), the internal diffusion in τ separates:
\[
du=d\tau+\sqrt{4/5}\,dW_1,\qquad
dz=(1-2z)d\tau+\sqrt{2z(1-z)}\,dW_2,
\]
with independent noises under this exact averaged generator. So the **Jacobi uniform z density remains an invariant law in the internal operational clock** for the joint diffusion, even though C(T) fluctuates and T is not slow. If initialized with uniform z independent of u, z remains uniform at each fixed operational τ. This is stronger than frozen-T modeling, but NOT a claim of uniform z at deterministic physical times or under survival selection.

In this idealized unbounded T model, u has positive drift in τ and \(T\to\infty\) as τ→∞. Since \(dt/dτ=\mu/(10D_0)e^{-u}\), the physical lifetime to T=∞ is finite almost surely (the exponential functional \(\int_0^\infty e^{-u_\tau}dτ\) converges for positive linear drift). This corresponds formally to reaching zero binding energy h=0−. **It is not a physically completed killed-boundary law:** the secular near-escape approximation, weak-kick assumptions and bounded jump corrections must be audited before interpreting this idealized explosion as physical escape. The unconditional operational-time measure has no normalized stationary law in u, since u drifts indefinitely. The ordinary physical-time shape marginal and survival-conditioned/quasi-stationary laws remain uncomputed.

This distinguishes four notions: (i) drift-zero e²=2/3; (ii) uniform Jacobi stationary law in intrinsic τ; (iii) physical-time distribution at given t; and (iv) population conditioned on no unbinding at t. Neither (iii) nor (iv) is inferred from (ii).

No new field-slope ratio Xi deviation or gravitational constant derived. Handoff: audit joint generator and time-change rigorously, especially validity of mixed covariance after secular averaging and near-escape conditions. Sandbox: compare exact joint SDE's conditional distributions against BPS finite-jump/killed bath; seek or disprove an induced measurement coupling, don't transplant arbitrary nonorthogonal Gram values into a torque.
