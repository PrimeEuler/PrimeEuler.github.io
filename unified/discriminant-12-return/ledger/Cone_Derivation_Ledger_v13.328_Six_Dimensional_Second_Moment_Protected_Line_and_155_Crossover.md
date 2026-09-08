# Cone Derivation Ledger v13.328
## Six-Dimensional Second-Moment Protected Line and 155 Crossover

### Scope
Continue v13.327 by adding one more post-Feshbach effective direction.  In the first six effective directions impose five linear constraints:

\[
\langle q,p\rangle=0,
\qquad
\langle q,s\rangle=0,
\qquad
\langle q,t\rangle=0,
\]

\[
M_1:=\sum_m m q_m=0,
\qquad
J_2^{\rm total}:=0.
\]

Here \(p,s,t\) are the exact prime, cusp, and archimedean leading \(1/n\) coordinate channels, and \(J_2^{\rm total}\) is the combined \(n^{-3}\) coefficient of the three extracted remainder expansions.

Five independent constraints in six dimensions leave a one-dimensional line.

### Numerical line at M=399
A unit representative in the first-six effective-eigenvector basis is approximately

\[
q_6\approx
(-0.7198621,-0.2923525,-0.6061967,0.1695635,0.0101081,-0.0005098).
\]

The corresponding odd-coordinate vector is approximately

\[
(0.001047,-0.128724,0.604524,-0.716725,-0.000579,
0.319119,-0.038883,-0.026983,-0.014333,0.001493).
\]

The five numerical constraint residuals are at ordinary floating-roundoff scale.

The formal effective Rayleigh scale is

\[
\boxed{\rho_6\approx6.5171\times10^{-11}}.
\]

Again this is a hybrid numerical scale, not an interval lower bound.

### Exact asymptotic hierarchy
For the combined prime+cusp part, after the three channel constraints and \(M_1=0\),

\[
g_{p+c}(n)
=-\frac{J_2^{p+c}}{n^3}
+\frac{f_n M_3}{n^4}
+O(n^{-5}),
\]

with

\[
f_n=\frac4\pi A_n+\frac2\pi\operatorname{Si}(n\pi).
\]

For the archimedean term the leading channel is also removed, and because \(H_n=O(n^{-1})\), its first remainder contributes a constant \(n^{-3}\) coefficient plus faster terms.

The fifth constraint sets the **combined** constant \(n^{-3}\) coefficient to zero:

\[
J_2^{\rm total}=J_2^{p+c}+J_2^{arch}=0.
\]

Therefore the first surviving adverse term is the prime+cusp oscillatory moment term

\[
\frac{f_n M_3}{n^4},
\]

plus \(O(n^{-5})\) corrections.  Numerically

\[
M_3\approx13.91127733.
\]

Thus the remote-tail norm improves to

\[
\boxed{O(N^{-7/2})}.
\]

### Conservative bound
Using the exact geometric-series remainder structure for \(n>19\), a conservative representative bound has the form

\[
\beta_N
\le
|M_3|\,\|f_n/n^4\|_{\ell^2(n\ge N)}
+
\frac{B_4}{d_N}\sqrt{S_{10}(N)}
+
\frac{F_N M_5}{d_N}\sqrt{S_{12}(N)},
\]

where

\[
d_N=1-(19/N)^2,
\]

and \(B_4,M_5,F_N\) are explicit finite-core/supremum constants.  No pre-projection coordinatewise \(O(n^{-2})\) or \(O(n^{-3})\) term is charged because those coefficients have already been annihilated by the five constraints.

### Crossover at the coercive onset
Using the same analytic tail gap \(\alpha_N\) as the v13.312+ chain gives representative values

| N | alpha_N | beta_N^2/alpha_N |
|---:|---:|---:|
| 151 | 0.0037337 | 4.53e-10 |
| 153 | 0.0170470 | 8.85e-11 |
| 155 | 0.0301854 | 4.47e-11 |
| 157 | 0.0431534 | 2.80e-11 |

Against

\[
\rho_6\approx6.52\times10^{-11},
\]

the first tested odd crossover is

\[
\boxed{N=155}.
\]

The high tail is already certified coercive from the earlier analysis beginning at odd cutoff \(151\).  The new line therefore reaches usefulness essentially immediately after coercivity turns on.

### Substantial structural conclusion
The remote infinite tail is no longer the dominant obstruction for this model reduction.

The working hierarchy is now

\[
\boxed{
\text{finite Feshbach}
\to
\text{kill 3 leading channels}
\to
\text{kill }M_1
\to
\text{kill }J_2^{\rm total}
\to
O(N^{-7/2})\text{ remote tail}.
}
\]

The conservative remote-tail crossover has collapsed through the sequence

\[
115553\to3150\to2250\to281\to155.
\]

The remaining hard problem is therefore not remote-tail coercivity.  It is the **finite effective block / low-core sign problem**, especially the unresolved first three hybrid eigenvalue scales and the need to turn the numerical five-constraint line into a controlled matrix-valued Feshbach statement.

### Guardrails
- \(\rho_6\) is not a certified positive lower bound.
- The first three post-Feshbach eigenvalue signs remain unresolved.
- The six-dimensional constraint line is numerical/hybrid, not an exact algebraic nullspace theorem.
- The displayed tail constants are ordinary floating evaluations, not interval enclosures.
- No positivity theorem, exact zero mode, \(\lambda_1=0\), RH, or GRH conclusion follows.

### Next target
Stop spending effort on larger remote cutoffs.  The next high-leverage step is to certify or sharply enclose the **finite effective low block** itself: either by interval/high-precision Schur assembly, or by an inertia/min-max argument that avoids resolving the tiny eigenvalues directly.  The remote infinite tail is now sufficiently suppressed that this finite problem is the bottleneck.
