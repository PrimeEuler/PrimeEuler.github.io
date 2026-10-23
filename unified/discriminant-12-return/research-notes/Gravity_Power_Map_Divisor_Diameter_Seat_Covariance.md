# Cone power-map / divisor-hyperbola selector test: n+1 diameter and quarter-seat covariance

Date 2026-10-23. Parents v13.177, v13.200–202, v13.364, v13.691, v14.550, v14.765–766. Gravity-lane self-run, Suzuki sandbox untouched.

## 1. Factor-level geometry (exact)

Let u>0 be the chosen primitive factor level, and (x,y)=(ua,ub) where a,b>0. Set T=(x+y)/2, X=(x−y)/2, Y=√(xy). A fixed factor row y=u has Y²=u²+2uX with vertex X=−u/2, and the mirror column x=u has vertex X=+u/2, as in v13.177. Thus u_EM=1 has vertices ±1/2; u_G=1/2 has vertices ±1/4. The former and latter are *relative grid scales* (not the affine Hurwitz shifts of v14.765).

For the distinguished (a,b)=(n,1) branch, with n≥1,
\[
d_u=u(n+1),\quad o_u=u(n−1)/2,\quad h_u=u√n,\quad
(d_u/2)^2=o_u^2+h_u^2.
\]
The invariant shape ratios are \(h_u/d_u=√n/(n+1)\) and \(2o_u/d_u=(n−1)/(n+1)\). This distinguishes a diameter's **full length** d_u from its radius d_u/2, avoiding a factor-2 error.

## 2. Power map and covariance (exact)

The raw Paper-B coordinatewise power \((x,y)\mapsto(x^k,y^k)\) is a valid cone power but does not preserve a half-spaced factor grid's unit: y=u maps to u^k. The **unit-preserving conjugated power** is
\[
\mathcal P_{k,u}(x,y)=
\left(u(x/u)^k,\;u(y/u)^k\right)
=\left(x^k/u^{k−1},\ y^k/u^{k−1}\right).
\]
This is a choice of normalization, not the unique intrinsic Lorentz-eigen-coordinate power map of Paper B. It preserves the row y=u and the arithmetic lattice x=um,y=un for integer m,n when k∈Z_{≥1}. On the diagonal distinguished branch:
\[
( un,u)\mapsto( un^k,u),\quad
d'_u=u(n^k+1),\
o'_u=u(n^k−1)/2,\
h'_u=u n^{k/2}.
\]
Therefore \(u\)-independent shape power \(n\mapsto n^k\), or in shell rapidity \(s=\frac12\ln(x/y)\), \(s\mapsto ks\). Geometric compactification \(\tan(\theta/2)=\tanh(s/2)\) from v13.691 then gives \(\theta' = 2\arctan[\tanh(ks/2)]\), not \(\theta\mapsto k\theta\). This last distinction is essential: compactification is not an analytic continuation nor a simple circular power map.

## 3. Divisor slices and global counts (exact)

On the u-scaled integer factor lattice, the physical shell is \(xy=u² n\), with integer pair contacts \(ab=n\). Hence
\[
d_u(u² n)=d(n),\qquad
D_u(u² N)=\sum_{m≤N}d(m)=D(N)
\]
for integer n,N≥1. Fixing instead the *same unscaled physical product* X in the two sectors:
\[
D_{u=1}(X)=D(\lfloor X\rfloor),\qquad
D_{u=1/2}(X)=D(\lfloor4X\rfloor).
\]
Thus apparent difference in global count is fully the unit-rescaling unless an independently physical invariant fixes the cutoff X across sectors.

Under \(\mathcal P_{k,u}\), each divisor shell \(ab=n\) injects into \(ab=n^k\) but not generally onto it:
\[
d(n)=\prod_p(e_p+1),\quad
d(n^k)=\prod_p(ke_p+1).
\]
Example n=12, k=2: 6 source divisor-pair contacts inject into 15 divisor-pair contacts at 144. The power map is NOT a bijection of arithmetic shells in general and does not identify D(N) with D(N^k).

## 4. Selector conclusion and exact next fork

The fixed (n+1) diameter, sqrt(n) chord, ±u/2 vertex, and u-normalized power map establish a **commutative scaled geometry** for EM u=1 and gravitational u=1/2. Because all normalized shape ratios and all dimensionless divisor counts coincide at matched shell index n, this arithmetic construction by itself cannot select a physical fine-structure/G coupling hierarchy. It instead identifies the necessary missing datum: a physically defined absolute cutoff/action or an operator with a nontrivial response to scale u despite equal normalized shape. A candidate selector must supply it independently of measured alpha or G. The quarter-vs-half vertex is geometrically real, but equal up to dilation.

Open gate: derive a scale-sensitive action (field regularization, causal action, or spectral boundary condition) on the known parabolic/hyperbolic Cone without inserting u- and coupling-dependence by hand, then test whether the two seats produce independent values. No G, α, or hierarchy derived; no Suzuki or far-tail touched.
