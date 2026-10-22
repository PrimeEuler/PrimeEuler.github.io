# Gravity next stage: equal-mass Rutherford hard-escape geometry reconstructed

Date 2026-10-22. Dedicated gravity lane, no sandbox compute. Parents: v14.720–724 and the source EFT v3.4. Producer gravity_rutherford_escape_kinematics.py, executed locally and verified.

## An exact conditional collision kernel component [D]

At a Kepler phase with test velocity v and bath particle velocity w, for **equal-mass elastic scattering** define center-of-mass velocity V=(v+w)/2 and incoming relative velocity g=v−w, magnitude g. For scattering polar angle θ and azimuth φ about the incoming relative velocity, the outgoing test velocity is
\[
v'=V+\frac g2\{\cos\theta\,\hat g+\sin\theta(\cos\phi\,e_1+\sin\phi\,e_2)\}.
\]
The condition for escape at fixed separation r is \(h'=|v'|^2/2-\mu/r\ge0\), or \(|v'|^2\ge v_{\rm esc}^2=2\mu/r\).

Let \(V_\parallel=V\cdot\hat g\), \(V_\perp=|V-V_\parallel\hat g|\). Then
\[
|v'|^2=a+b\cos\phi,\quad
a=|V|^2+g^2/4+gV_\parallel\cos\theta,\quad
b=gV_\perp\sin\theta\ge0.
\]
The exact azimuthal *escape fraction* of Rutherford scattering at θ is
\[
P_{\rm esc}(\theta;v,w,r)=
\begin{cases}
0,&(v_{\rm esc}^2-a)/b\ge1,\\
1,&(v_{\rm esc}^2-a)/b\le-1,\\
\pi^{-1}\arccos[(v_{\rm esc}^2-a)/b],&\text{otherwise},
\end{cases}
\]
with the evident deterministic threshold when b=0.

For differential Rutherford cross-section \(d\sigma/d\Omega=K(g)\sin^{-4}(\theta/2)\), the *angular* escape-rate factor with a physical hard-scattering angular cutoff θ_min is
\[
\mathcal J_{\rm esc}(v,w,r;\theta_{\min})
=2\pi\int_{\theta_{\min}}^\pi
\frac{\sin\theta\,P_{\rm esc}(\theta;v,w,r)}
{\sin^4(\theta/2)}d\theta.
\]
A true rate also requires bath density, relative speed, target-velocity Maxwellian integration and absolute \(K(g)\); moreover the matched BPS hard/soft partition is not fixed by the source's **fold-local** numerical coefficients. This formula is a valid exact *conditional angular building block*, not a finished BPS model.

## Nontrivial analytic/numerical test [D/N]

Choose μ=r=1, v=(0,0.8,0), w=(0,3,0). The initial bound test particle has speed 0.8 and escape threshold √2. In this collinear configuration azimuth drops out, and escape begins only above
\[
\theta_0=\arccos\frac{|V|^2+g^2/4-2}{|V|g}\approx0.830317885457.
\]
The angular Rutherford escape integral is exactly
\[
\mathcal J_{\rm esc}=4\pi[\csc^2(\theta_0/2)-1]\approx64.679848750378,
\]
for *any* cutoff \(\theta_{\min}<\theta_0\). The Python quadrature reproduces the analytic value within 1e−7 for cutoff choices 0.01, 0.05, 0.10 and 0.50 radians. Thus, for this fixed incoming pair, the small-angle Rutherford divergence does not contaminate the finite escape hazard; grazing events lack sufficient energy transfer to unbind. This does NOT establish cutoff independence after unbounded Maxwellian averaging or BPS matching; those require separate estimates.

## Status of the other two open items

The exact killed/censored Markov generator and survivor hazard-covariance equation were derived at v14.723. The conditional collision angular kernel here is one step closer to a full physical \(\lambda(T,e^2)\), but Maxwellian integration, BPS subtraction, phase averaging, finite-temperature distribution dynamics, and boundary controls remain unsolved. Therefore **no numerical QSD is claimed**.

The v14.700 \(\Xi\) ratio remains \((1-R\Phi''/\Phi')/3\). The collision kinematics change energy/shape trajectories and may affect noise/selection, but provide no new mean external-field potential or rotor coupling. No G derivation or new \(\Xi\) claim.

**Next within gravity lane only:** compute the Maxwellian-averaged hard angular hazard with explicit physical cutoff/matching parameter and errors; then combine with a source-derived soft operator *only if* the matching data are available. Do not use shared Suzuki compute, no sandbox handoff.
