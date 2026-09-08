# Cone Derivation Ledger v13.322
## Fully protected active line and the N≈4963 remote-tail scale

### Status
This checkpoint continues v13.321 and combines the extracted prime, exact cusp, and archimedean leading channels on the four-dimensional active core.

Guardrail: the channel rank, protected vector, and all displayed decimal thresholds are numerical/high-precision, not interval-certified.  This checkpoint does not prove positivity, an exact zero mode, lambda_1=0, RH, or GRH.

## 1. Three-channel active geometry
The leading adverse remote-tail channels are:

- prime: \(L/n\), from v13.318;
- exact cusp: \(S/n\), from v13.320;
- smooth archimedean: \(T/n\), from v13.321.

Numerically the 4x3 channel matrix [L S T] has singular values

\[
\boxed{2.17382638,\quad0.50546923,\quad0.00409808.}
\]

Thus it has numerical rank three and leaves one unit active vector orthogonal to all three channels:

\[
\boxed{p\approx(-0.23116867,-0.73865405,0.60819101,-0.17622408)}
\]

in the first-four core-eigenvector basis.

In the original odd coordinate core \(n=1,3,\ldots,19\), this direction is approximately

\[
(-0.00159647,\ 0.14514853,\ -0.63640583,\ 0.70701295,\ 0.00053232,
-0.26977389,\ 0.02966508,\ 0.01805907,\ 0.00805280,\ -0.00065265).
\]

## 2. Isolated-core scale
Using the first four high-precision core eigenvalues, the Rayleigh quotient of p in the isolated 10-mode core is

\[
\boxed{\rho_{\rm core}(p)\approx1.484089836\times10^{-9}.}
\]

This is only an isolated-core scale.  It is not the final effective eigenvalue after eliminating the stiff low core, finite buffer, and infinite tail.

## 3. Remote-tail coupling on the protected line
Because p is orthogonal to all three extracted 1/n channels, only the remainders remain:

\[
\|P_{\ge N}B_{\rm prime}p\|=O(N^{-3/2}),
\]

\[
\|P_{\ge N}C_{\rm cusp}p\|=O(N^{-3/2}),
\]

\[
\|P_{\ge N}K_{\rm arch}p\|=O(N^{-5/2}).
\]

The pole term remains globally positive in the even-v sector and is not charged as an adverse remainder.

A conservative combined coupling bound is

\[
\beta_N\le\beta_N^{(p)}+\beta_N^{(c)}+\beta_N^{(a)}.
\]

Representative values:

- N=401: beta≈3.18335e-3
- N=501: beta≈2.27218e-3
- N=701: beta≈1.36808e-3
- N=1001: beta≈7.99782e-4
- N=2001: beta≈2.82213e-4
- N=5001: beta≈7.13170e-5
- N=10001: beta≈2.52055e-5

At N=401 the component bounds are approximately

\[
\beta_p=2.36568\times10^{-3},\quad
\beta_c=8.167997\times10^{-4},\quad
\beta_a=8.7283\times10^{-7}.
\]

So the arch remainder is already negligible at this scale; prime and cusp dominate.

## 4. Comparison with the analytic tail gap
Using the previously established analytic tail gap \(\alpha_N\), a crude scalar elimination cost is

\[
\frac{\beta_N^2}{\alpha_N}.
\]

Representative values:

- N=401: alpha≈0.9877500, penalty≈1.026e-5
- N=501: alpha≈1.2112690, penalty≈4.262e-6
- N=701: alpha≈1.5481684, penalty≈1.209e-6
- N=1001: alpha≈1.9051621, penalty≈3.357e-7
- N=2001: alpha≈2.5986796, penalty≈3.065e-8
- N=5001: alpha≈3.5151914, penalty≈1.447e-9
- N=10001: alpha≈4.2084121, penalty≈1.510e-10

Scanning odd cutoffs, the first displayed cutoff at which this conservative remote-tail penalty falls below the isolated-core Rayleigh scale is

\[
\boxed{N=4963.}
\]

At N=4963:

\[
\alpha_{4963}\approx3.50756125,
\]

\[
\beta_{4963}\approx7.21382\times10^{-5},
\]

\[
\boxed{\beta_{4963}^2/\alpha_{4963}\approx1.48363\times10^{-9}}
\]

versus

\[
\rho_{\rm core}(p)\approx1.48409\times10^{-9}.
\]

## 5. What this does and does not establish
This is the first scale where the crude adverse remote-tail Schur penalty on the fully protected direction is no longer automatically larger than that direction's isolated-core energy.

It does **not** close positivity.  The remaining unresolved pieces are:

1. eliminate the remaining six low-core directions consistently;
2. eliminate the finite buffer without replacing its anisotropic Schur correction by a scalar norm;
3. combine those finite corrections with the protected-line tail estimate in one matrix-valued Feshbach map;
4. interval-certify any sign-sensitive final inequality.

The important structural point is that remote-tail control itself is no longer the dominant conceptual obstruction on the protected line.  The bottleneck has shifted to the finite/stiff Feshbach geometry.

## Files
- `research-notes/suzuki_fully_protected_line_tail_scale.py`
