# Cone Derivation Ledger v13.326
## Post-Feshbach Joint Prime-Cusp Moment Bound and ~3150 Crossover

### Scope
This checkpoint continues v13.325.  The v13.325 protected-line remote-tail
bound treated the prime and cusp remainders separately and took coefficientwise
absolute values before projection.  That was safe but highly wasteful.

The present checkpoint projects the two exact remainders onto the computed
post-Feshbach protected low-coordinate vector first, preserves its signed first
moment, and only then applies tail inequalities.

The protected line remains the computed one-dimensional nullspace of the three
leading post-Feshbach prime/cusp/arch `1/n` channels from v13.324.  Its formal
hybrid Rayleigh scale is approximately

\[
\rho_{\rm prot}^{(4)}\approx 8.06\times 10^{-14}.
\]

This is a numerical scale, not an interval-certified lower bound.

### Exact projected prime and cusp remainders
For odd core mode `m` and remote odd mode `n`, v13.319 and v13.320 give

\[
R^{(p)}_{mn}
=-\frac4\pi\frac{1}{1-m^2/n^2}
\left(\frac{A_m m^2}{n^3}-\frac{mA_n}{n^2}\right),
\]

and

\[
R^{(c)}_{mn}
=-\frac2\pi\frac{1}{1-m^2/n^2}
\left(\frac{m^2\operatorname{Si}(m\pi)}{n^3}
-\frac{m\operatorname{Si}(n\pi)}{n^2}\right).
\]

Let `q_m` be the protected low-coordinate vector and define the signed first
moment

\[
M=\sum_m m q_m.
\]

The key numerical fact is

\[
\boxed{M\approx 3.31\times10^{-2}},
\]

whereas the coefficientwise majorant used implicitly in v13.325 behaves like
`sum |m q_m| = O(1)`.  Thus the `n^-2` coefficient was being overestimated by
well over an order of magnitude before squaring in the Schur penalty.

### Moment-preserving decomposition
For `n>=N>19`, write

\[
d_N=1-(19/N)^2.
\]

Using

\[
\sum_m\frac{m q_m}{1-m^2/n^2}
=M+
\sum_m m q_m\frac{m^2/n^2}{1-m^2/n^2},
\]

and the pointwise bounds

\[
|A_n|\le W,
\qquad
W=\sum_q\frac{\Lambda(q)}{\sqrt q}
\approx2.9262341821764086,
\]

\[
|\operatorname{Si}(n\pi)|<2,
\]

we obtain

\[
\boxed{
\|r_{p+c}\|_{\ell^2(n\ge N)}
\le
|M|\frac4\pi(W+1)\sqrt{S_4(N)}
+
\frac{\frac4\pi B_p+\frac2\pi B_c}{d_N}\sqrt{S_6(N)}
+
\frac{4(W+1)M_3}{\pi d_N}\sqrt{S_8(N)}.
}
\]

Here

\[
B_p=\sum_m |q_mA_m|m^2,
\qquad
B_c=\sum_m |q_m\operatorname{Si}(m\pi)|m^2,
\]

\[
M_3=\sum_m |q_m|m^3,
\]

and the elementary odd-tail estimates are

\[
S_4(N)\le N^{-4}+(6N^3)^{-1},
\]

\[
S_6(N)\le N^{-6}+(10N^5)^{-1},
\]

\[
S_8(N)\le N^{-8}+(14N^7)^{-1}.
\]

The first term is the important one: it preserves the small signed moment `M`
instead of replacing it by an absolute first moment.

### Numerical effect
Using the current post-Feshbach protected vector, a representative evaluation
gives a joint prime+cusp bound of order

\[
2.3\times10^{-7}\quad(N\approx5000),
\]

and about

\[
7.4\times10^{-8}\quad(N\approx10000).
\]

The archimedean remainder is already much smaller and does not materially
change these scales.

With the same analytic tail-gap lower bound `alpha_N` used in v13.325, the
moment-preserving Schur penalty

\[
\frac{\beta_N^2}{\alpha_N}
\]

falls below the formal protected-line scale near

\[
\boxed{N\approx3.15\times10^3}.
\]

A representative non-interval computation places the first odd crossover near
`N=3149`.  Because the protected vector and all displayed constants are
ordinary floating/high-precision numerical quantities rather than interval
enclosures, the integer `3149` is descriptive, not a certified sharp cutoff.
The robust conclusion is the scale change

\[
\boxed{1.16\times10^5\ \longrightarrow\ O(3\times10^3)}.
\]

### Exploratory direct projected sequence
Directly summing the combined projected prime+cusp sequence, without replacing
`A_n` and `Si(n pi)` by sup-norm bounds, gives still smaller tail norms and
suggests that the true useful crossover may occur below the conservative
moment-bound cutoff.  Those direct sums are descriptive only and are not used
as a certificate in this checkpoint.

### Structural conclusion
The dominant v13.325 loss was not intrinsic to Suzuki's tail.  It came from the
order of inequalities.

The correct order is now

\[
\boxed{
\text{finite Feshbach elimination}
\to
\text{leading-channel annihilation}
\to
\text{signed moment projection}
\to
\text{tail majorization}.
}
\]

On the protected line, the prime and cusp `O(n^-2)` remainders share the same
small first-moment channel.  Keeping that signed channel before absolute values
collapses the remote-tail scale by roughly two orders of magnitude in cutoff.

### Guardrails
- The post-Feshbach protected line is numerical.
- Its formal Rayleigh scale near `8e-14` is not interval-certified.
- The cutoff near `3149` is a non-interval numerical evaluation of an analytic
  bound, not a rigorous sharp integer threshold.
- The first three hybrid effective eigenvalue signs remain unresolved.
- No exact zero mode, positivity theorem, `lambda_1=0`, RH, or GRH conclusion
  follows.

### Next target
The next high-leverage step is to replace the sup-norm treatment of the
`n^-2` coefficient

\[
M\left[\frac4\pi A_n+\frac2\pi\operatorname{Si}(n\pi)\right]
\]

by a sequence-level `ell^2` estimate.  The prime amplitude `A_n` is an explicit
five-frequency trigonometric sequence and `Si(n pi)=pi/2+O(1/n)`.  Their squared
odd-tail sum can therefore be decomposed into explicit diagonal and oscillatory
cross terms.  A rigorous finite-frequency bound should improve the `~3150`
scale further without changing the proof architecture.
