# Gravity common-wall local response model

Date: 2026-10-23. Lane: gravity only. Parents: v13.770, v14.768–771. Classification [D] exact statements in a mathematical factor-grid model; [O] missing physical sector map.

## Definition [D]

Let h>0 and attach ordered-pair multiplicity d(n) to radial shell r_h(n)=log(h²n). Fix a nonnegative C¹ compactly supported probe w with integral 1, and width ε>0. Put w_ε(t)=ε⁻¹w(t/ε). Define the *local wall response* 
\[
\mathcal R_h(L,\varepsilon)=\sum_{n\ge1}d(n)w_\varepsilon(\log(h^2n)-L).
\]
It is a finite sum for every finite L and ε. This is a modeled detector of radial factor-pair density, NOT an electromagnetic or gravitational action.

## Exact translation and wall-calibration gauge [D]

Because r_{1/2}(n)=r_1(n)-log4,
\[
\boxed{\mathcal R_{1/2}(L,\varepsilon)
=\mathcal R_1(L+\log4,\varepsilon)}.
\]
If the half-grid wall is *independently* calibrated to L-log4, then
\[
\boxed{\mathcal R_{1/2}(L-\log4,\varepsilon)
=\mathcal R_1(L,\varepsilon)}
\]
for every L, ε, and profile w. Hence a response contrast at equal wall L is mathematical and calibration-dependent unless a common physical wall is independently justified.

Under any *passive* change r'=r+s with simultaneously shifted wall L'=L+s, each response remains identical. The contrast cannot be attributed merely to a naming convention for the coordinate.

## Fixed-resolution, large-wall theorem [D]

Use Dirichlet's classical divisor asymptotic
\[
D(x)=x\log x+(2\gamma-1)x+O(\sqrt x)
\]
with \(\gamma\) Euler's constant. For fixed h, ε and w as L→∞, write
\[
A_\varepsilon=\int_{\mathbb R}e^t w_\varepsilon(t)\,dt>0,\qquad
B_\varepsilon=\int_{\mathbb R}t e^t w_\varepsilon(t)\,dt.
\]
Stieltjes partial summation over shell positions gives
\[
\boxed{\mathcal R_h(L,\varepsilon)
=h^{-2}e^L\Big[(L-2\log h+2\gamma)A_\varepsilon+B_\varepsilon\Big]
+O_{h,\varepsilon,w}(e^{L/2}).}
\]
The derivative of x log x+(2γ-1)x is log x+2γ; the remainder after integration by parts is bounded by e^{L/2} times a constant depending on the compact support and profile derivative. Consequently
\[
\boxed{\lim_{L\to\infty}
\frac{\mathcal R_{1/2}(L,\varepsilon)}
{\mathcal R_1(L,\varepsilon)}=4}
\]
for every fixed ε>0 and admissible w. This establishes **probe-profile-independent leading density contrast within the model**, NOT a regulator-independent physical coupling.

The order of limits matters: sending ε→0 at a fixed L probes discrete atoms and does not imply the above ratio. There is no uniform claim in ε.

## Laplace generating response [D]

The atomic radial pair measure is μ_h=Σ_{n≥1}d(n)δ_{r_h(n)}, with Laplace transform \(Z_h(s)=h^{-2s}\zeta(s)^2\), Re s>1. The local detector is convolution of μ_h against w_ε; translation by -log4 produces the exact identity above. A common normalized response can mask a purely multiplicative unnormalized factor. No identification is made with Suzuki's spectral measure (v13.770).

## Explicit falsifiability / physical action contract [O]

A physical selector requires: (1) one shared sector-independent definition of x,y and radial wall from an operational invariant (e.g. a defined geometric area/proper-distance boundary, not a chosen coordinate); (2) a derivation of the actual EM and gravitational state densities or a justified physical current mapped onto μ_h, without assuming divisor=Suzuki/Weil current; (3) a response coefficient from a gauge/diffeomorphism-invariant action, no inserted measured G or α; (4) stability against permissible regulator, boundary and reference-scale variations. If (1) or (2) fails, the model is a counting analogy only. In particular, a ratio of 4 in this density is not Newton's constant and does not explain the enormous coupling hierarchy.

No Suzuki production, far-tail, or existing payload files changed.
