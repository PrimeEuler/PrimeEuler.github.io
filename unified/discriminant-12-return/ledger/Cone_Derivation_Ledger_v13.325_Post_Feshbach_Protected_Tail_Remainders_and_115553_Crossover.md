# Cone Derivation Ledger v13.325
## Post-Feshbach Protected Tail Remainders and the ~115553 Crossover

### Scope
This checkpoint continues v13.324.  The finite buffer is eliminated first and
the remote-tail remainder bounds are then evaluated directly on the resulting
post-Feshbach effective directions.

Two directions are compared:

1. the computed line in the first four effective directions that annihilates
   all three leading prime/cusp/archimedean 1/n channels;
2. the quasi-protected direction in the three-dimensional ultra-near-null
   effective subspace, whose leading channel residual is the smallest singular
   value of the 3x3 channel matrix.

The purpose is to determine which direction remains useful after the infinite
remote tail is reattached.

### Remainder structure
For a low-coordinate vector q on odd modes m=1,3,...,19, after the exact leading
channels are removed the remote entries obey the already established forms

\[
R^{(p)}_{mn}=O(n^{-2}),\qquad
R^{(c)}_{mn}=O(n^{-2}),\qquad
R^{(a)}_{mn}=O(n^{-3}).
\]

Hence the corresponding tail norms satisfy

\[
\|R^{(p)}P_{\ge N}\|=O(N^{-3/2}),\qquad
\|R^{(c)}P_{\ge N}\|=O(N^{-3/2}),
\]

and

\[
\|R^{(a)}P_{\ge N}\|=O(N^{-5/2}).
\]

The same analytic tail-gap lower bound \(\alpha_N\) used in v13.312--v13.322
is retained.

### Four-dimensional post-Feshbach protected line
At M=399, v13.324 found a computed line in the first four effective directions
whose prime/cusp/arch leading-channel residual is at ordinary floating
roundoff.  Its formal hybrid effective Rayleigh scale is approximately

\[
\rho_{\rm prot}^{(4)}\approx8.06\times10^{-14}.
\]

Because this direction is defined as the null line of the 4x3 channel matrix,
the floating residual is not charged as a physical leading term; only the
explicit remainder bounds are charged.

Representative conservative remote-tail penalties are approximately

| N | beta_N | beta_N^2/alpha_N |
|---:|---:|---:|
| 401 | 3.64e-3 | 1.34e-5 |
| 1001 | 9.13e-4 | 4.38e-7 |
| 5001 | 8.14e-5 | 1.89e-9 |
| 10001 | 2.88e-5 | 1.97e-10 |
| 50001 | 2.57e-6 | 1.14e-12 |

Scanning odd cutoffs gives the first crossover near

\[
\boxed{N\approx115553},
\]

where, using the present non-interval numerical constants,

\[
\alpha_N\approx6.65561,
\qquad
\beta_N\approx7.324\times10^{-7},
\]

and

\[
\boxed{
\beta_N^2/\alpha_N\approx8.06\times10^{-14},
}
\]

comparable to and just below the formal protected-line Rayleigh scale.

At this crossover the adverse pieces are approximately

\[
\beta_{\rm prime}\approx5.46\times10^{-7},
\qquad
\beta_{\rm cusp}\approx1.87\times10^{-7},
\]

\[
\beta_{\rm arch}\approx6.97\times10^{-13}.
\]

Thus the smooth archimedean remainder is already negligible.  The remaining
remote-tail uncertainty is almost entirely the prime and cusp O(n^-2)
remainders.

### Three-dimensional quasi-protected direction
For the deepest three-dimensional post-Feshbach effective subspace, v13.324
found

\[
\sigma_{\min}(C_3)\approx1.36629\times10^{-3}.
\]

This means the quasi-protected direction retains a genuine leading 1/n channel
of that size.  Its remote leading-tail contribution therefore behaves as

\[
\sim1.36629\times10^{-3}
\left(\sum_{\substack{n\ge N\\n\ {\rm odd}}}\frac1{n^2}\right)^{1/2}
=O(N^{-1/2}).
\]

This term eventually dominates the O(N^-3/2) remainders.  Because the formal
Rayleigh scale of the three deepest hybrid levels is around 10^-18 and is itself
below the present reliable sign scale, the quasi-protected direction is not a
practical scalar-tail route.  Its channel residual is simply too large relative
to that ultra-small formal scale.

### Main structural conclusion
The useful post-Feshbach direction is therefore the four-dimensional
channel-null line, not the three-dimensional quasi-protected direction:

\[
\boxed{
\text{finite Feshbach reduction}
\to
\text{4D exact-channel-null line}
\to
\text{fast remote-tail remainders}.
}
\]

The cost of the dramatically smaller post-Feshbach Rayleigh scale is a much
larger conservative remote cutoff (~1.16e5 rather than ~5e3 before finite
elimination).  However, at that scale the archimedean contribution is already
irrelevant; further progress should focus on preserving cancellations inside
the prime and cusp remainder matrices rather than using coefficientwise
absolute-value bounds.

### Guardrails
- The protected line is numerical, defined by the computed post-Feshbach 4x3
  channel nullspace.
- The ~8.06e-14 Rayleigh value is a hybrid numerical scale, not a certified
  positive lower bound.
- The first three effective eigenvalue signs remain unresolved.
- The cutoff and displayed constants are non-interval numerical evaluations.
- This checkpoint does not establish positivity, an exact zero mode,
  lambda_1=0, RH, or GRH.

### Next target
Replace the scalar triangle-inequality bounds on the prime and cusp remainders
by their projected 1x-tail or small-matrix Gram forms on the post-Feshbach
protected line.  The present ~115553 cutoff is driven almost entirely by those
two conservative O(n^-2) estimates; preserving their sign/correlation structure
is the highest-leverage route to lowering it.
