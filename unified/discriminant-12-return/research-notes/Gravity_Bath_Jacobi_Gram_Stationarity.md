# Gravity lane: full high-speed bath Fokker–Planck gate, stationary eccentricity, and nonorthogonal Gram observable

**Date:** 2026-10-22. **Parents:** v14.705–709 and gravity v14.708. **Producer:** gravity_bath_jacobi_gram.py. **Status:** exact, conditional on the EFT's homogeneous high-speed isotropic encounter coefficients.

## Source-faithful process

The deposited Kepler_Cone_Revised_EFT_Draft_v3_4_Elevated_Hot_Benchmark.tex explicitly quotes the Hamilton–Modak high-speed coefficients for \(\varepsilon=e^2\):
\[
d\varepsilon=C(1-2\varepsilon)dt+\sqrt{2C\varepsilon(1-\varepsilon)}\,dB_t,\qquad 0\le\varepsilon\le1,\;C>0.
\]
Thus the generator is
\[
{\cal L} f(\varepsilon)
=C(1-2\varepsilon)f'(\varepsilon)+C\varepsilon(1-\varepsilon)f''(\varepsilon).
\]
This is a Jacobi diffusion, not a deterministic scalar ODE. In the EFT the constant \(C=10D_0T/\mu\) when T is frozen at leading secular order.

For \(q=\sqrt{1-\varepsilon}\), Itô gives exactly
\[
{\cal L}q=-\frac{C}{4q}(3q^2-1),\qquad
{\cal L}s=+\frac{C}{4q}(3q^2-1),\quad s=1-q.
\]
The zero q²=1/3, e²=2/3 is a **first-moment drift reversal**. It is NOT a deterministic globally attracting trajectory or by itself a stationary distribution. Noise remains active and gives finite-width stationary statistics.

## New exact stationary law [D]

The Fokker–Planck probability current for density \(p(\varepsilon)\) is
\[
J=C(1-2\varepsilon)p-C\,\partial_\varepsilon[\varepsilon(1-\varepsilon)p].
\]
The normalizable zero-flux stationary density is
\[
\boxed{p_*(\varepsilon)=1\quad(0<\varepsilon<1)}
\]
under the stated no-flux boundary prescription. Consequently
\[
\mathbb E_*(e^2)=\frac12,\qquad \mathbb E_*(q)=\frac23.
\]
The \(2/3\) appears a **third** way, as the ensemble mean \(q\), not as the bath drift-zero \(q_*=1/\sqrt3\), nor the phase's spherical angular moment. The three numerically different quantities must not be conflated.

## Pushforward of the eccentric Gram witness [D]

From v14.701 and the **correct** shape-coordinate map of v14.708,
\[
\rho^2=\frac{1-e}{1+e},\qquad
W(e):=\langle I_{00},I_{20}\rangle=\frac23(1-\rho^2)
=\frac{4e}{3(1+e)}.
\]
The same Itô generator acts on the nonlinear observable as
\[
\boxed{{\cal L}W=-\frac{C(e^2+2e-1)}{3e(1+e)^2}.}
\]
Thus W's drift vanishes at \(e=\sqrt2-1\), NOT at \(e=\sqrt{2/3}\). At the bath's q-drift zero, \({\cal L}W/C=-12+29\sqrt6/6\approx-0.1607995765\), strictly negative.

The static Gram value at that drift-zero is \(W(\sqrt{2/3})=(4\sqrt6-8)/3\approx0.5993196570\), whereas the equilibrium **expectation of the Gram functional** is
\[
\boxed{\mathbb E_*[W]=\int_0^1 W(\sqrt\varepsilon)d\varepsilon
=\frac{8\ln2-4}{3}\approx0.51505914816.}
\]
These are different meaningful exact numbers. The overlap is an algebraic angular functional; identifying this function with an apparatus response remains physically unproven because v14.703's Favard obstruction rules out a conventional eccentric orthonormal sphere eigenbasis.

## Boundary and scope discipline

Stationarity refers to the **one-dimensional idealized high-speed diffusion at fixed T**, with no-flux probability boundary handling. The archived EFT also includes finite-temperature, BPS hard-jump, and unbinding/killing sectors: its different endpoints are not stationary distributions of this idealized Jacobi process. Nor is this an observational prediction of physical gravitational polarization or tidal deviations. Coupling to the gravity ratio Xi=(1-R Phi''/Phi')/3 remains absent, and no measured G enters this algebra.

This corrects the **interpretive overstatement** in v14.705/v14.708 that the hot-bath drift zero can be called an attracting physical equilibrium without specifying the stochastic distribution. It does not change those entries' algebraic value e²=2/3 or the independent Hamilton–Modak normalization match.

## Next handoffs

**Audit:** independently verify the exact Jacobi stationary law, Itô generator for W, and \((8\ln2-4)/3\) expectation, checking boundary classification and assumptions about slow T dependence. Flag if the archived statement about q-dot implies deterministic dynamics beyond its moment drift.

**Sandbox:** test finite-temperature or physically derived anisotropic bath generators and compute stationary/quasi-stationary shape statistics including bound/killed boundary conditions. Determine if any G-free gravitational response Xi inherits a real, measurable effect; do not identify Gram overlap with torque without a measurement operator. Keep producers reproducible, results honest, ledger additive, far-tail untouched.
