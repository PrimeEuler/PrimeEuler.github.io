# Cone Derivation Ledger v13.327
## Five-Dimensional Post-Feshbach Moment-Protected Line and 281 Crossover

### Scope
Continue v13.326 in the **post-Feshbach effective basis**.  The first four effective directions already contained a line annihilating the three leading remote-tail channels (prime, exact cusp, archimedean).  The remaining obstruction was the signed first moment

\[
M_1=\sum_{m=1,3,\dots,19}m q_m,
\]

which drives the combined prime+cusp \(n^{-2}\) remainder and therefore an \(O(N^{-3/2})\) tail norm.

The first five effective directions give one extra degree of freedom.  Impose four linear constraints:

\[
\langle q,p\rangle=\langle q,s\rangle=\langle q,t\rangle=0,
\qquad M_1=0.
\]

This leaves a one-dimensional line.

### Numerical line at M=399
Using the same hybrid finite Feshbach construction as v13.323--324 (high-precision 10x10 low block, ordinary-double finite Schur correction), a unit representative in the first-five effective eigenvector basis is approximately

\[
q_5\approx(-0.7437544,-0.2981924,-0.5822596,0.1364685,0.0161491).
\]

Its odd-coordinate representative is approximately

\[
(0.002725,-0.147226,0.629325,-0.706647,-0.000545,
0.285143,-0.032702,-0.020979,-0.009966,0.000864).
\]

The four constraint residuals are at floating roundoff in the numerical construction.

The formal effective Rayleigh scale is

\[
\boxed{\rho_5\approx1.0823\times10^{-11}}.
\]

This is a hybrid numerical scale, not an interval lower bound.

### Tail-order improvement
For prime+cusp, after the three leading channels and \(M_1\) vanish, the exact geometric expansion begins

\[
g_{p+c}(n)
=-\frac{J_2}{n^3}+\frac{f_n M_3}{n^4}+O(n^{-5}),
\]

where

\[
f_n=\frac4\pi A_n+\frac2\pi\operatorname{Si}(n\pi),
\]

\[
J_2=\sum_m q_m m^2
\left(\frac4\pi A_m+\frac2\pi\operatorname{Si}(m\pi)\right),
\qquad
M_3=\sum_m m^3q_m.
\]

Numerically on this line,

\[
J_2\approx0.9955201181,
\qquad
M_3\approx25.75471341.
\]

Therefore the prime+cusp remote-tail norm is now

\[
\boxed{O(N^{-5/2})},
\]

rather than \(O(N^{-3/2})\).

The archimedean leading channel is also removed, and its remainder remains \(O(N^{-5/2})\) in tail norm.

### Conservative crossover
Using the same analytic tail gap \(\alpha_N\) as v13.312--326 and conservative absolute-value bounds only **after** the four cancellations, the scalar Schur penalty

\[
\beta_N^2/\alpha_N
\]

falls below \(\rho_5\) at approximately

\[
\boxed{N=281}.
\]

This is a large structural improvement over the v13.326 protected-line scale near \(N\approx2250\).

### Interpretation
The reduction hierarchy is now visibly moment-structured:

\[
\text{finite Feshbach}
\to
\text{kill three }1/n\text{ channels}
\to
\text{kill }M_1
\to
O(N^{-5/2})\text{ remote tail}.
\]

The infinite tail is no longer separated from the coercive onset by orders of magnitude.

### Guardrails
- The first three post-Feshbach effective eigenvalue signs remain unresolved.
- \(\rho_5\) is a hybrid numerical Rayleigh scale, not a certified lower bound.
- The constraint nullspace is numerically constructed, not an exact algebraic kernel statement.
- No positivity theorem, exact zero mode, \(\lambda_1=0\), RH, or GRH conclusion follows.

### Next target
Use one more effective direction to cancel the combined \(n^{-3}\) coefficient of prime+cusp+arch as well.  Six dimensions provide five constraints and still leave a line.  If energetically affordable, the adverse tail should begin at \(n^{-4}\), with \(O(N^{-7/2})\) tail norm.
