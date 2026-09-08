# Cone Derivation Ledger v13.324
## Post-Feshbach Tail-Channel Geometry and Effective Protected Directions

### Scope
This checkpoint continues v13.323.  The finite buffer is eliminated first,
producing the hybrid effective low-core operator

\[
F_M=A_{CC}^{(hp)}-A_{CB}A_{BB}^{-1}A_{BC}.
\]

Only after this finite Feshbach reduction are the three exact leading remote-tail
channels projected onto the resulting effective eigenbasis.  This reverses the
order used in v13.318--v13.322 and is the correct working order after v13.323.

The three coordinate channels on the odd core \(m=1,3,\ldots,19\) are

\[
p_m=-\frac4\pi A_m,
\qquad
s_m=-\frac2\pi\operatorname{Si}(m\pi),
\qquad
t_m=-\frac4\pi H_m,
\]

where

\[
A_m=\sum_q \frac{\Lambda(q)}{\sqrt q}
\sin\!\left(\frac{m\pi\log q}{2}\right),
\]

and

\[
H_m=\int_0^2 h(t)\sin\!\left(\frac{m\pi t}{2}\right)dt,
\qquad h(t)=r''(t).
\]

The first channel is the prime \(1/n\) term from v13.318--319, the second is
the exact cusp \(1/n\) term from v13.320, and the third is the archimedean
\(1/n\) term from v13.321.

### Numerical construction
The finite matrix was assembled through odd mode \(399\) with archimedean
Gauss--Legendre order 800.  The low \(10\times10\) block was reconstructed at
70 digits before subtracting the ordinary-double Schur correction, as in
v13.323.

At \(M=399\), the first effective eigenvalues were numerically

\[
-4.29\times10^{-19},\quad
-7.64\times10^{-20},\quad
1.33\times10^{-17},\quad
1.4400\times10^{-12},
\]
\[
4.1398\times10^{-8},\quad
2.3435\times10^{-4},\ldots
\]

The first three signs remain below the trustworthy sign scale of the present
hybrid assembly.  They are anatomy only.  The resolvable fourth-through-sixth
levels agree with v13.323.

### Channel compression after finite Feshbach elimination
Project the three coordinate channels into the first \(k\) effective
eigendirections of \(F_M\).  Let \(C_k\) be the resulting \(k\times3\) channel
matrix.

For the **three-dimensional ultra-near-null effective subspace** at \(M=399\),

\[
\sigma(C_3)\approx
\boxed{(2.45913616,\ 0.228753517,\ 0.00136629188)}.
\]

Thus the deepest three-dimensional effective subspace is dominated by two
leading channel directions, while the third independent channel is roughly
three orders of magnitude weaker than the first.

For the first four effective directions,

\[
\sigma(C_4)\approx
\boxed{(2.57678894,\ 0.43781850,\ 0.00287906)}.
\]

Therefore the low-rank prime/cusp/arch channel compression found before finite
Feshbach elimination survives after the finite buffer is removed.

### Buffer-cutoff stability
The channel singular values are remarkably stable as the eliminated buffer
cutoff grows.

For the three-dimensional effective subspace:

| M | sigma_1 | sigma_2 | sigma_3 |
|---:|---:|---:|---:|
| 101 | 2.45895855 | 0.228581913 | 0.00136538717 |
| 151 | 2.45908611 | 0.228705094 | 0.00136603630 |
| 201 | 2.45912369 | 0.228740550 | 0.00136622160 |
| 237 | 2.45912700 | 0.228744213 | 0.00136624434 |
| 301 | 2.45913227 | 0.228749480 | 0.00136625853 |
| 351 | 2.45913368 | 0.228750400 | 0.00136627084 |
| 399 | 2.45913616 | 0.228753517 | 0.00136629188 |

For the first four effective directions:

| M | sigma_1 | sigma_2 | sigma_3 |
|---:|---:|---:|---:|
| 101 | 2.57671589 | 0.43751310 | 0.00287337 |
| 151 | 2.57675845 | 0.43769106 | 0.00287685 |
| 201 | 2.57676762 | 0.43772944 | 0.00287757 |
| 237 | 2.57677117 | 0.43774430 | 0.00287782 |
| 301 | 2.57677862 | 0.43777541 | 0.00287834 |
| 351 | 2.57678424 | 0.43779888 | 0.00287873 |
| 399 | 2.57678894 | 0.43781850 | 0.00287906 |

This stability is strong numerical evidence that the channel compression is not
a cutoff artifact.

### Effective quasi-protected direction inside the deepest three-dimensional subspace
The left singular vector corresponding to the smallest singular value of
\(C_3\) is approximately

\[
q_{\rm quasi}\approx
(0.921129,-0.160999,0.354402)
\]

in the first-three effective-eigenvector basis.  Its leading-channel residual
has norm

\[
\|C_3^Tq_{\rm quasi}\|\approx
\boxed{1.36629\times10^{-3}}.
\]

The corresponding low-coordinate vector is approximately

\[
(-0.03565,\ 0.34706,\ -0.75445,\ 0.54257,\ 2.98\!\times10^{-4},
-0.12050,\ 0.01145,\ 0.00656,\ 0.00306,\ -3.01\!\times10^{-4}).
\]

A formal Rayleigh value computed from the first three hybrid effective
eigenvalues is about \(1.3\times10^{-18}\), but this number is **not** a
reliable sign/scale certificate because those three eigenvalues themselves lie
below the hybrid assembly's trustworthy scale.

### Computed protected line in the first four effective directions
Because a computed \(4\times3\) channel matrix has a one-dimensional numerical
nullspace, there is a computed line orthogonal to all three leading channels.
At \(M=399\), one unit representative is

\[
q_{\rm prot}^{(4)}\approx
(0.687533,-0.0233854,0.686118,-0.236630)
\]

in the first-four effective-eigenvector basis, with channel residual at ordinary
floating roundoff.

Its coordinate-core representative is approximately

\[
(0.00583,\ 0.06985,\ -0.53888,\ 0.74060,\ 6.55\!\times10^{-4},
-0.38918,\ 0.05138,\ 0.03926,\ 0.02366,\ -0.00295).
\]

The corresponding formal effective Rayleigh scale is

\[
\boxed{\rho_{\rm prot}^{(4)}\approx8.06\times10^{-14}}.
\]

This scale is primarily inherited from the resolvable fourth effective level,
but it is still a numerical hybrid quantity, not an interval-certified lower
bound or an exact eigenvalue.

### Structural conclusion
The main result is

\[
\boxed{
\text{finite Feshbach elimination preserves the low-rank remote-tail channel geometry.}
}
\]

More specifically:

1. the finite buffer does not randomize the prime/cusp/arch channel structure;
2. the deepest effective three-dimensional subspace retains one strongly
   quasi-protected direction;
3. the first four effective directions retain a computed line annihilating all
   three leading \(1/n\) channels;
4. therefore the next remote-tail analysis should be performed in the
   **post-Feshbach effective basis**, not in the isolated-core basis used in
   v13.318--v13.322.

### Guardrails
- The first three effective eigenvalue signs are unresolved at present precision.
- The computed four-dimensional protected line is numerical, not an exact
  algebraic kernel statement.
- The displayed singular values and vectors are non-interval numerical data.
- No exact zero mode, positivity theorem, \(\lambda_1=0\), RH, or GRH conclusion
  follows.

### Next target
Recompute the prime, cusp, and arch **remainder** bounds directly on the
post-Feshbach computed protected line and on the three-dimensional
quasi-protected direction.  Then compare their remote-tail Schur penalties
against the post-Feshbach scales, with special attention to whether the very
small third channel permits a substantially earlier useful tail cutoff than a
coordinatewise bound would suggest.
