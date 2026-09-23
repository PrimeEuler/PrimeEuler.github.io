# Cone Derivation Ledger v13.733 — Exact Screw-Symbol Extraction and Xi/Theta Transfer Obstruction

Date: 2026-09-23

Status: source-faithful extraction of the object \(k^2\widehat g(k)\) entering v13.732. The extraction exposes a decisive correction: the natural full-line symbol is a tempered **distribution**, not an ordinary scalar Wiener--Hopf symbol. Consequently the factorization proposed schematically in v13.732 cannot be performed as an ordinary scalar Wiener--Hopf factorization without an additional regularization/analytic transform.

Synchronization: live head checked before this write. No collision with the Suzuki edge lane.

## 1. Suzuki's exact screw kernel

Suzuki v2, Eq. (1.3), defines the continuous real even function
\[
\begin{aligned}
g(t)=&
-4(e^{t/2}+e^{-t/2}-2)
+\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n)\\
&-\frac{|t|}{2}\bigl(\psi(1/4)-\log\pi\bigr)
-\frac14\left[
\Phi(1,2,1/4)-e^{-|t|/2}\Phi(e^{-2|t|},2,1/4)
\right].
\end{aligned}
\]

Suzuki explicitly notes that \(g(t)\) does not tend to zero as \(|t|\to\infty\). Thus \(\widehat g\) is not naturally an ordinary \(L^1\) Fourier transform.

The source-faithful object entering the differentiated Weil operator is instead the tempered distribution
\[
\boxed{\mathcal K:=-g''}.
\]

## 2. Exact relation to the v13.732 edge symbol

With Fourier convention
\[
\widehat f(k)=\int_{\mathbb R}e^{-ikx}f(x)\,dx,
\]
distributional differentiation gives
\[
\widehat{-g''}(k)=k^2\widehat g(k).
\]

Therefore the v13.732 formal symbol
\[
\mathcal D(k)=k^2\widehat g(k)-\lambda
\]
is exactly
\[
\boxed{
\mathcal D=\widehat{\mathcal K}-\lambda
=
\widehat{-g''}-\lambda
}
\]
as a tempered distribution.

This is the correct source-faithful extraction.

## 3. Suzuki's explicit distribution \(-g''\)

Suzuki Section 2.5 gives
\[
\boxed{
-g''(t)
=
-\frac12\,{\rm Pf}\frac1{|t|}
-(2A+1)\delta_0
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left[\delta(t-\log n)+\delta(t+\log n)\right]
-r''(t),
}
\]
where
\[
A=\frac12(\log(2\pi)+C_0-1)
\]
and \(r\) is the explicit archimedean remainder from the local expansion.

Thus the differentiated screw current consists of

1. the logarithmic finite-part singularity at \(0\);
2. a local delta;
3. the symmetric prime-power delta train at \(\pm\log n\);
4. the smooth/tempered archimedean remainder.

This is exactly the additive-logarithmic explicit-formula structure already isolated independently in the cone current lane.

## 4. Fourier-side explicit-formula representation

Suzuki Section 2.4 derives, at finite interval cutoff, the quadratic-form multiplier
\[
\operatorname{Re}\psi\left(\frac14+\frac{ik}{2}\right)-\log\pi
-2\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}\cos(k\log n)
-\widehat{r''_{0,a}}(k).
\]

The nontrivial archimedean term satisfies
\[
\widehat{r_1''}(k)
=
-\operatorname{Re}\psi\left(\frac14+\frac{ik}{2}\right)
+\log|k|-\log2.
\]

Hence the Fourier image of \(-g''\) is the Weil explicit-formula distribution. It is not an ordinary bounded scalar multiplier on the full line.

Equivalently, Suzuki states formally that the differentiated kernel is
\[
k(t)=\sum_{\xi(1/2+i\gamma)=0}e^{-i\gamma t},
\]
understood as a distribution. Therefore, in the zero-side representation,
\[
\boxed{
\widehat{-g''}
=
2\pi\sum_{\gamma\in\Gamma}m_\gamma\,\delta(\,\cdot+\gamma\,)
}
\]
with the precise pairing understood through Weil's explicit formula and with the usual caveat that off-RH \(\gamma\) need not be real, so this displayed real-axis delta notation is literal only in the real-zero/RH specialization. Unconditionally, the prime/archimedean explicit-formula distribution is the safe representation.

## 5. Correction to ordinary Wiener--Hopf factorization

v13.732 wrote formally
\[
\mathcal D(k)=\mathcal D_+(k)\mathcal D_-(k).
\]

The extraction above shows that, source-faithfully,
\[
\mathcal D=\widehat{-g''}-\lambda
\]
is distribution-valued.

Therefore an ordinary scalar Wiener--Hopf factorization of \(\mathcal D(k)\) is **not currently justified**.

In particular one cannot simply write
\[
Q_+(k)=\frac{\Pi_-(\cdots/\mathcal D_+)}{\mathcal D_-}
\]
without first constructing an analytic regularization or passing to a transform in which the explicit-formula current becomes a genuine holomorphic function.

Status:
\[
\boxed{\textbf{CORRECTION: ordinary scalar WH factorization is blocked at the raw screw-symbol level.}}
\]

## 6. The natural analytic regularization

The additive logarithmic current has a canonical Laplace/Cauchy regularization. From the cone current lane,
\[
\frac{\xi'}{\xi}(s)-\frac{\xi'}{\xi}(2)
=
\int_0^\infty(e^{-sr}-e^{-2r})\,d\nu_\xi(r),
\qquad \Re s>1,
\]
where \(d\nu_\xi\) combines the archimedean current and the von Mangoldt atomic current.

The screw distribution \(-g''\) is the symmetric Fourier realization of this same explicit-formula data, whereas \(\xi'/\xi\) is its analytic Laplace/Cauchy realization.

Thus the correct route from the raw screw current to an analytic edge transfer is not
\[
\widehat{-g''}\stackrel?=\text{ordinary scalar symbol},
\]
but rather
\[
\boxed{
-g''
\longrightarrow
\text{explicit-formula current}
\longrightarrow
\text{Laplace/Cauchy regularization}
\longrightarrow
\xi'/\xi.
}
\]

## 7. Comparison with the theta/Xi current

The theta lane gives the entire bilateral transform
\[
\Xi(w)
=
\frac12+\left(w^2-\frac14\right)
\int_{\mathbb R}K_\theta(r)e^{wr}\,dr,
\]
and, after the shifted-Casimir step v13.722,
\[
\boxed{
\Xi(w)=\int_{\mathbb R}\Phi(r)e^{wr}\,dr
}
\]
for the classical positive Xi kernel \(\Phi\).

This is analytically very different from the raw screw symbol:

- theta current \(\Phi\): rapidly decaying function, entire bilateral transform \(\Xi\);
- screw current \(-g''\): tempered explicit-formula distribution with prime atoms and finite-part singularity, naturally regularized to a logarithmic derivative \(\xi'/\xi\).

Therefore
\[
\boxed{
\mathcal T_{\rm edge}\text{ cannot be identified directly with }\Xi
\text{ or }I_\theta
\text{ by raw Fourier-symbol matching.}
}
\]

The structures are nevertheless related by the elementary identity
\[
\boxed{
\frac{d}{ds}\log\xi(s)=\frac{\xi'(s)}{\xi(s)}.
}
\]

Thus the screw side naturally carries **logarithmic-derivative data**, while the theta side carries **entire Xi data**. Recovering Xi from the screw current requires integration/exponentiation plus normalization, not a scalar multiplier identification.

## 8. Consequence for the edge transfer

The edge transfer remains
\[
\mathcal T_{\rm edge}(p)=(p+1)Q(p).
\]

The exact edge equation says that \(Q\) is obtained by inverting a half-line compression of
\[
G-\lambda K,
\]
whose differentiated full-line current is the Weil explicit-formula distribution.

Hence \(\mathcal T_{\rm edge}\) should be expected to be a **boundary resolvent/scattering object built from the logarithmic derivative data**, rather than Xi itself.

A plausible analytic target is therefore a ratio/Cayley/Weyl object of the form
\[
\boxed{
\mathcal T_{\rm edge}(p)
\sim
\text{normalized function of }
\frac{\xi'}{\xi}\!\left(\frac12+p\right)
}
\]
after the correct half-line regularization and rank-one Green subtraction.

This is structurally consistent with Suzuki's existing Weyl/characteristic framework, but no equality is asserted here.

## 9. A stronger bridge already present in Suzuki's infinite-volume theory

Suzuki Section 7 obtains, for the infinite-volume de Branges model, a boundary combination
\[
(z-i)\widehat f_{+i}(z)-(z+i)\widehat f_{-i}(z)
=
\frac{2\xi'(3/2)}{\pi^2 i}
\frac{\xi(1/2-iz)}{E(z)}.
\]

Thus Suzuki already has an exact infinite-volume **paired deficiency-channel ratio involving Xi itself**.

This is highly relevant: it suggests that the edge transfer need not equal Xi. Instead, nontrivial channel transfer factors may combine/cancel in the paired boundary characteristic, leaving the ratio
\[
\xi(1/2-iz)/E(z).
\]

This is precisely the mechanism that v13.728 listed as the first surviving possibility after scalar normalization failed.

## 10. Result

\[
\boxed{\textbf{PASS: exact screw object extracted}}
\]
\[
\boxed{
\mathcal D=\widehat{-g''}-\lambda
}
\]
as a tempered explicit-formula distribution.

\[
\boxed{\textbf{FAIL: raw ordinary scalar Wiener--Hopf factorization}}
\]

\[
\boxed{\textbf{FAIL: direct }\mathcal T_{\rm edge}=\Xi\textbf{ or }I_\theta\textbf{ symbol match}}
\]

\[
\boxed{\textbf{PROMISING: paired-channel cancellation/normalization}}
\]
because Suzuki's infinite-volume identity already produces
\[
\xi(1/2-iz)/E(z)
\]
from the paired deficiency channels.

## 11. Next gate

Do not attempt to factor the distribution \(\widehat{-g''}\) multiplicatively.

Instead:

1. derive the analytic Cauchy/Laplace transform of the compensated screw current, retaining the \(-\lambda K\) rank-one subtraction;
2. compare that analytic function with Suzuki's de Branges \(E(z)\) and Weyl/Cayley data;
3. insert the resulting transfer into the paired \(+\)/\(-\) deficiency combination;
4. test whether the edge transfer factors cancel to recover Suzuki's exact infinite-volume ratio \(\xi(1/2-iz)/E(z)\);
5. only then compare with the v13.722 theta representation of \(\Xi\).

This is now the source-faithful route to deciding whether the edge transfer fits the Xi/theta structure.
