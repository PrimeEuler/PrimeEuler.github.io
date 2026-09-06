# Cone Derivation Ledger v13.269 — Laguerre–Pólya Characteristic Class and Sharp Euler Determinant Truncation

Date: 2026-09-06
Status: EXACT CHARACTERISTIC-FUNCTION REFORMULATION + SHARP REAL-AXIS DETERMINANT APPROXIMATION — RH/GRH NOT PROVED

## 0. Synchronization and strategic move

Immediately before this write, the authoritative project README, current `master` tip, and the ledger state were re-fetched. The tip remained

`8b18ff10d0554f79007a1dbdc49ff32094a1de27`,

with v13.268 the highest ledger checkpoint and no newer external-audit checkpoint present.

The direct Fredholm-endpoint route suggested at the end of v13.268 does not yet canonically close: no project theorem currently identifies the remaining reference ratio

\[
\frac{\mathfrak Z_{K,a}^{0}(w)}{(\Psi_{K,a}^{\rm arith}(w))^2}
\]

with a Fredholm determinant `det(I+K_a)` for which a trace-norm estimate `||K_a||_1 -> 0` is already available.

Following the user's instruction to continue immediately if that reduction does not close, this entry takes the next invariant step.

The outcome is twofold:

1. the exact arithmetic characteristic function in the squared variable belongs to a genus-zero entire-function setting in which GRH is equivalent to a Laguerre–Pólya type-I zero geometry;
2. on the Euler-product real axis `w>1/4`, the characteristic function itself admits a finite prime-power approximation with a **pure exponential** error, sharper than the polynomial-times-exponential bound obtained for the ramp transform in v13.266.

Thus the remaining operator target can be phrased directly as convergence of finite self-adjoint characteristic functions to an explicit arithmetic characteristic function.

## 1. Squared completed characteristic function

Let

\[
K=\mathbf Q(\sqrt3),
\qquad
\xi_K(s)=s(s-1)12^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s),
\]

up to an irrelevant nonzero constant normalization.

Define the centered completed function

\[
\Xi_K(z):=\xi_K\!\left(\frac12+z\right).
\]

The functional equation gives

\[
\Xi_K(-z)=\Xi_K(z).
\]

Therefore there is a unique entire function `Psi_K` satisfying

\[
\boxed{
\Psi_K(w):=\Xi_K(\sqrt w)
}
\]

with the square-root ambiguity canceled by evenness.

Equivalently, if

\[
\Xi_K(z)=\sum_{n\ge0}c_{2n}z^{2n},
\]

then

\[
\boxed{
\Psi_K(w)=\sum_{n\ge0}c_{2n}w^n.
}
\]

From v13.268,

\[
\boxed{
\mathcal S_K(w)
=2\frac{\Psi_K'(w)}{\Psi_K(w)}.
}
\]

## 2. Order reduction under the square map

The completed Dedekind xi-function is entire of order one in the centered variable `z`.

Because `Xi_K` is even and `w=z^2`, its squared characteristic function satisfies the growth relation

\[
\boxed{
\rho(\Psi_K)\le\frac12.
}
\]

In fact the standard degree-two zero counting gives exact order `1/2`, but only the strict inequality

\[
\rho(\Psi_K)<1
\]

is needed below.

Consequently `Psi_K` has genus zero.

This is a major simplification relative to the original centered `z` variable: no genus-one exponential factors are required after symmetric zero pairing and squaring.

## 3. Genus-zero product in the squared variable

Let the nonzero centered zeros of `Xi_K` be written in symmetric pairs

\[
\pm\alpha_j
\]

with multiplicities `m_j`.

Then the zeros of `Psi_K` are

\[
\boxed{
\beta_j:=\alpha_j^2.
}
\]

The standard zero-counting estimate implies

\[
\sum_j\frac{m_j}{|\alpha_j|^2}<\infty,
\]

hence

\[
\boxed{
\sum_j\frac{m_j}{|\beta_j|}<\infty.
}
\]

Let

\[
m_0:=\operatorname{ord}_{w=0}\Psi_K(w).
\]

Then the genus-zero canonical product is

\[
\boxed{
\Psi_K(w)
=C_K w^{m_0}
\prod_j\left(1-\frac{w}{\beta_j}\right)^{m_j},
}
\]

with locally uniform convergence.

No exponential factor `e^{aw}` can occur because `Psi_K` has order strictly less than one.

## 4. Exact GRH zero-geometry criterion

A nontrivial zero

\[
\rho=\frac12+\alpha
\]

lies on the critical line exactly when

\[
\alpha\in i\mathbf R.
\]

Under the square map this is equivalent to

\[
\alpha^2\in(-\infty,0].
\]

Therefore

\[
\boxed{
\mathrm{GRH}(\zeta_K)
\iff
\text{every zero of }\Psi_K(w)
\text{ lies on }(-\infty,0].
}
\]

with a possible zero at `w=0` corresponding to a central zero.

This is the characteristic-function version of the Stieltjes pole criterion from v13.263.

## 5. Laguerre–Pólya type-I equivalence

Factor out any central zero:

\[
\widetilde\Psi_K(w):=w^{-m_0}\Psi_K(w).
\]

Under GRH its zeros are

\[
-\gamma_j^2<0,
\]

so the product becomes

\[
\boxed{
\widetilde\Psi_K(w)
=C_K
\prod_j
\left(1+\frac{w}{\gamma_j^2}\right)^{m_j}.
}
\]

Since

\[
\sum_j\frac{m_j}{\gamma_j^2}<\infty,
\]

this is a Laguerre–Pólya type-I entire function after multiplication by an overall real sign.

Conversely, if `widetilde Psi_K` belongs to the Laguerre–Pólya type-I class with no positive exponential factor and has the actual zero divisor of the D12 completed field function, then all its zeros are nonpositive real and hence every centered zero of `xi_K` is imaginary.

Thus

\[
\boxed{
\mathrm{GRH}(\zeta_K)
\iff
w^{-m_0}\Psi_K(w)
\text{ is Laguerre–Pólya type I}
}
\]

for the actual arithmetic characteristic function.

The order-`1/2` fact is useful here: it rules out an independent `e^{aw}` factor, so the entire class is controlled by the zero divisor and one constant normalization.

## 6. Consequence for finite self-adjoint characteristic functions

Let `D_{K,a}` be any finite-interval self-adjoint first-order realization in the D12 field channel, with real eigenvalues `lambda_{j,a}` and a real entire characteristic function `W_{K,a}(z)` whose zeros are precisely those eigenvalues, counted with multiplicity.

Suzuki's current finite-interval construction supplies exactly this kind of self-adjoint first-order framework in the Riemann-zeta setting; the D12 application remains a project extension target, not a source-established theorem.

Fold the finite characteristic function through the square map:

\[
\boxed{
\mathcal W_{K,a}(w)
:=W_{K,a}(i\sqrt w)W_{K,a}(-i\sqrt w).
}
\]

Because the product is even in `sqrt(w)`, it is entire in `w` whenever `W_{K,a}` is entire.

Its zeros occur at

\[
\boxed{
w=-\lambda_{j,a}^2\le0.}
\]

Hence every normalized finite squared characteristic function belongs to the real-rooted genus-zero/Laguerre–Pólya closure class appropriate to nonpositive zeros, after harmless canonical normalization.

Therefore, if

\[
\boxed{
\frac{\mathcal W_{K,a}(w)}{\mathcal W_{K,a}(w_*)}
\longrightarrow
\left(
\frac{\Psi_K(w)}{\Psi_K(w_*)}
\right)^2
}
\]

locally uniformly in `w`, then Hurwitz closure forces the limiting zero divisor to remain on `(-infinity,0]`, hence GRH for `zeta_K`.

This is the characteristic-function analogue of the Stieltjes normal-family criterion from v13.265.

## 7. Exact Euler logarithm from the positive D12 prime-power coefficients

Recall

\[
b_K(n)=\Lambda(n)(1+\chi_{12}(n))\ge0.
\]

For `s>1`, define

\[
\boxed{
c_K(n):=\frac{b_K(n)}{\log n}}
\]

for `n>=2` with the convention that `b_K(n)=0` off prime powers.

Then

\[
\boxed{
\log\zeta_K(s)
=\sum_{n\ge2}c_K(n)n^{-s}.
}
\]

Indeed differentiation gives

\[
-\frac{d}{ds}\log\zeta_K(s)
=\sum_{n\ge2}c_K(n)\log n\,n^{-s}
=\sum_{n\ge2}b_K(n)n^{-s}
=-\frac{\zeta_K'}{\zeta_K}(s),
\]

and both sides tend to zero as `s -> +infinity` after subtracting the constant logarithm of `1`.

For a prime power `n=p^k`,

\[
c_K(p^k)
=\frac{1+\chi_{12}(p)^k}{k},
\]

with the ramified interpretation `chi=0`, so

\[
\boxed{
0\le c_K(n)\le2.
}
\]

## 8. Sharp finite prime-power determinant cutoff

For `T>0`, define

\[
\boxed{
L_{K,T}(s)
:=\sum_{\log n\le T}c_K(n)n^{-s},
}
\]

and

\[
\boxed{
Z_{K,T}(s):=\exp(L_{K,T}(s)).
}
\]

The cutoff `T=2a` matches the exact finite-interval prime-power horizon found in v13.266:

\[
\boxed{n\le e^{2a}.}
\]

For every real `s>1`, positivity gives

\[
0\le
\log\zeta_K(s)-L_{K,T}(s)
=
\sum_{\log n>T}c_K(n)n^{-s}.
\]

Using `c_K(n)<=2`,

\[
0\le
\log\zeta_K(s)-L_{K,T}(s)
\le
2\sum_{n>e^T}n^{-s}.
\]

For `N=e^T`,

\[
\sum_{n>N}n^{-s}
\le
N^{-s}+\int_N^\infty x^{-s}\,dx
=N^{-s}+\frac{N^{1-s}}{s-1}.
\]

Hence

\[
\boxed{
0\le
\log\zeta_K(s)-L_{K,T}(s)
\le
C_s e^{-(s-1)T}.
}
\]

On every compact real interval `s in [1+delta,S]`,

\[
\boxed{
\log\zeta_K(s)-L_{K,T}(s)
=O_{\delta,S}(e^{-\delta T}).
}
\]

This has no polynomial factor in `T`.

## 9. Exact characteristic-function ratio on the Euler-product real axis

Put

\[
s(w):=\frac12+\sqrt w,
\qquad w>\frac14.
\]

Define the explicit archimedean factor

\[
\boxed{
A_K(s)
:=s(s-1)12^{s/2}\pi^{-s}\Gamma(s/2)^2.
}
\]

Then, up to the fixed nonzero normalization constant already absorbed into `xi_K`,

\[
\boxed{
\Psi_K(w)=A_K(s(w))\zeta_K(s(w)).
}
\]

Fix one normalization point

\[
w_*>\frac14,
\qquad s_*:=s(w_*).
\]

Then exactly

\[
\boxed{
\frac{\Psi_K(w)}{\Psi_K(w_*)}
=
\frac{A_K(s(w))}{A_K(s_*)}
\frac{\zeta_K(s(w))}{\zeta_K(s_*)}.
}
\]

This formula uses only the absolutely convergent Euler-product region.

## 10. Canonical arithmetic characteristic approximant

For `T=2a`, define the normalized finite arithmetic characteristic function on the real Euler-product axis by

\[
\boxed{
\frac{\Psi_{K,a}^{E}(w)}{\Psi_{K,a}^{E}(w_*)}
:=
\frac{A_K(s(w))}{A_K(s_*)}
\frac{Z_{K,2a}(s(w))}{Z_{K,2a}(s_*)}.
}
\]

This is a canonical determinant-level arithmetic truncation tied exactly to the same prime-power horizon `e^{2a}` as the restricted screw kernel.

It differs from the ramp-smoothed approximation of v13.266: the present object is obtained by truncating the **Euler logarithm itself**, not the finite Laplace ramp.

## 11. Pure exponential convergence of the arithmetic characteristic function

Take a compact real interval

\[
J=[w_0,w_1]\subset(1/4,\infty),
\]

and choose `w_* in J`.

Set

\[
\delta_J:=\sqrt{w_0}-\frac12>0.
\]

Then

\[
s(w)-1\ge\delta_J
\qquad(w\in J).
\]

The logarithm of the normalized ratio error is

\[
\begin{aligned}
&\log
\frac{
\Psi_{K,a}^{E}(w)/\Psi_{K,a}^{E}(w_*)
}{
\Psi_K(w)/\Psi_K(w_*)
}
\\
&=
-\bigl(\log\zeta_K(s(w))-L_{K,2a}(s(w))\bigr)
+
\bigl(\log\zeta_K(s_*)-L_{K,2a}(s_*)\bigr).
\end{aligned}
\]

Therefore

\[
\boxed{
\sup_{w\in J}
\left|
\log
\frac{
\Psi_{K,a}^{E}(w)/\Psi_{K,a}^{E}(w_*)
}{
\Psi_K(w)/\Psi_K(w_*)
}
\right|
\le
C_J e^{-2a\delta_J}.
}
\]

Exponentiating,

\[
\boxed{
\frac{
\Psi_{K,a}^{E}(w)/\Psi_{K,a}^{E}(w_*)
}{
\Psi_K(w)/\Psi_K(w_*)
}
=
1+O_J(e^{-2a\delta_J})
}
\]

uniformly for `w in J`.

This improves the v13.266 determinant-level rate from

\[
O_J((1+a)^2e^{-2a\delta_J})
\]

for the integrated-ramp approximation to the pure exponential

\[
\boxed{O_J(e^{-2a\delta_J})}
\]

for the Euler-logarithm characteristic approximation.

## 12. Logarithmic derivative of the sharp Euler cutoff

Differentiate the finite Euler logarithm:

\[
\frac{d}{ds}L_{K,2a}(s)
=-\sum_{\log n\le2a}b_K(n)n^{-s}.
\]

Since

\[
\frac{ds}{dw}=\frac1{2\sqrt w},
\]

we obtain

\[
\boxed{
2\frac{d}{dw}
\log\Psi_{K,a}^{E}(w)
=
2\frac{d}{dw}\log A_K(s(w))
-
\frac1{\sqrt w}
\sum_{\log n\le2a}b_K(n)n^{-s(w)}.
}
\]

Thus the characteristic-level truncation has a particularly simple logarithmic derivative: the full explicit archimedean term plus a **sharp** prime-power cutoff.

This should be compared with v13.266's ramp-smoothed cutoff factor

\[
1-e^{-z(T-\log n)}(1+z(T-\log n)).
\]

The two approximants serve different purposes:

- the ramp truncation is geometrically native to the restricted screw kernel;
- the Euler-logarithm truncation is determinant-native and converges more sharply.

Their difference is explicit and therefore can itself be studied as part of the remaining operator matching problem.

## 13. The new three-factor determinant comparison

Let `mathcal W_{K,a}` denote a normalized finite self-adjoint squared characteristic function with zeros on `(-infinity,0]`.

The natural comparison can now be factored as

\[
\boxed{
\frac{
\mathcal W_{K,a}(w)/\mathcal W_{K,a}(w_*)
}{
(\Psi_K(w)/\Psi_K(w_*))^2
}
=
\mathcal R_{a}^{\rm op/E}(w)
\cdot
\mathcal R_{a}^{E/\infty}(w),
}
\]

where

\[
\boxed{
\mathcal R_{a}^{\rm op/E}(w)
:=
\frac{
\mathcal W_{K,a}(w)/\mathcal W_{K,a}(w_*)
}{
(\Psi_{K,a}^{E}(w)/\Psi_{K,a}^{E}(w_*))^2
}
}
\]

is the remaining operator-to-Euler determinant defect, while

\[
\boxed{
\mathcal R_{a}^{E/\infty}(w)
:=
\left[
\frac{
\Psi_{K,a}^{E}(w)/\Psi_{K,a}^{E}(w_*)
}{
\Psi_K(w)/\Psi_K(w_*)
}
\right]^2
=1+O_J(e^{-2a\delta_J}).
}
\]

Thus the infinite arithmetic tail is now completely controlled at the characteristic-function level with pure exponential rate.

The full problem is reduced to

\[
\boxed{
\mathcal R_{a}^{\rm op/E}(w)\longrightarrow1.
}
\]

## 14. Laguerre–Pólya closure criterion for the remaining defect

Suppose for some compact interval `J subset (1/4,infinity)` with nonempty interior that

\[
\mathcal R_{a}^{\rm op/E}(w)\to1
\]

uniformly on `J`, and suppose the normalized finite characteristic family is normal on the relevant complex domain.

Because the Euler approximation already converges to `Psi_K` on `J`, the finite characteristic functions converge there to `Psi_K^2`.

Any locally uniform subsequential complex limit of the finite self-adjoint characteristic functions has only nonpositive real zeros, by Hurwitz closure of the Laguerre–Pólya class.

Identity on the real interval forces that subsequential limit to be `Psi_K^2` after normalization.

Hence `Psi_K^2`, and therefore `Psi_K`, has only nonpositive real zeros.

Thus

\[
\boxed{
\mathcal R_{a}^{\rm op/E}\to1
\text{ on one real Euler interval}
\quad+\quad
\text{normal-family control}
\Longrightarrow
\mathrm{GRH}(\zeta_K).
}
\]

This is the determinant-class analogue of v13.265's Stieltjes real-axis criterion.

## 15. Resolvent-power trace hierarchy at one positive point

The characteristic formulation also produces a useful local hierarchy.

For a positive squared spectral operator `A` with discrete spectrum `lambda_j^2`,

\[
\frac{d}{dw}\log\det(A+w)
=\operatorname{Tr}(A+w)^{-1}.
\]

Repeated differentiation gives

\[
\boxed{
(-1)^{r-1}\frac{1}{(r-1)!}
\frac{d^r}{dw^r}\log\det(A+w)
=\operatorname{Tr}(A+w)^{-r},
\qquad r\ge1.
}
\]

For the arithmetic target,

\[
\boxed{
(-1)^{r-1}\frac{1}{2(r-1)!}
\frac{d^{r-1}}{dw^{r-1}}\mathcal S_K(w)
}
\]

is the corresponding squared-zero resolvent moment under GRH.

Therefore an alternative exact convergence target is:

for one fixed `w_*>1/4`, prove convergence of the entire hierarchy of finite resolvent-power traces to the arithmetic derivatives at `w_*` together with a uniform growth bound sufficient to recover the local analytic function.

This does not reduce the proof burden by itself, but it turns determinant convergence into a moment/trace problem that may be more accessible numerically or variationally.

## 16. Relation to Suzuki's current operator program

Suzuki's 2026 screw-function/Weil-form program constructs finite-interval self-adjoint operators from localized Weil quadratic forms and formulates an infinite-volume spectral limit without assuming RH.

The present project does not claim that Suzuki proves the D12 Dedekind version developed here, nor that his finite characteristic functions converge to `Psi_K`.

The exact contribution of this ledger entry is to identify the arithmetic target any such D12 extension must reproduce:

\[
\boxed{
\Psi_K(w)
=\xi_K\!\left(\frac12+\sqrt w\right),
}
\]

with an explicit Euler-region finite approximation

\[
\boxed{
\Psi_{K,a}^{E}
}
\]

whose normalized real-axis error is already `O(e^{-2a delta})`.

Thus the conjectural spectral limit no longer needs to be compared directly with the full infinite Euler product; only the finite operator-to-finite Euler determinant defect remains.

## 17. What did and did not reduce

### Reduced exactly

- `Psi_K` is an entire function of the squared coordinate.
- Its order is below one, hence its canonical product is genus zero.
- GRH for `zeta_K` is equivalent to all zeros of `Psi_K` lying on the nonpositive real axis.
- After removing any central zero, this is equivalent to the actual arithmetic `Psi_K` lying in the Laguerre–Pólya type-I class.
- The D12 Euler logarithm has nonnegative coefficients `c_K(n)=b_K(n)/log n`.
- Truncating at the exact finite-interval horizon `n<=e^{2a}` gives a canonical determinant-level arithmetic approximation.
- Its normalized error on compact real intervals `w>1/4` is pure exponential:
  \[
  O_J(e^{-2a(\sqrt{w_0}-1/2)}).
  \]

### Not reduced yet

- No theorem yet identifies the finite self-adjoint D12 characteristic function with `Psi_{K,a}^E`.
- No canonical trace-class endpoint operator `K_a` with `det(I+K_a)` and `||K_a||_1->0` has yet been derived.
- The operator-to-Euler determinant defect remains open.
- No RH/GRH conclusion is proved.

## 18. Strategic next step

The most valuable next move is now narrower than the Fredholm attempt from v13.268.

We should compare the **logarithmic derivatives** of the two finite objects:

\[
\boxed{
\frac{d}{dw}\log\mathcal W_{K,a}(w)
\quad\text{versus}\quad
2\frac{d}{dw}\log\Psi_{K,a}^{E}(w).
}
\]

The first is a finite squared spectral resolvent trace.

The second is explicit:

\[
2\partial_w\log A_K(s(w))
-
\frac1{\sqrt w}
\sum_{\log n\le2a}
\frac{b_K(n)}{n^{1/2+\sqrt w}}.
\]

Thus the remaining theorem can be phrased as a finite-interval **trace formula**:

\[
\boxed{
\operatorname{Tr}(D_{K,a}^2+w)^{-1}
\stackrel{?}{=}
2\partial_w\log A_K(s(w))
-
\frac1{\sqrt w}
\sum_{\log n\le2a}
\frac{b_K(n)}{n^{1/2+\sqrt w}}
+
\varepsilon_a(w),
}
\]

with

\[
\boxed{
\varepsilon_a(w)\to0
}
\]

on one real interval.

This is now the cleanest operator/arithmetic bridge target in the project.

If that finite trace identity can be obtained from the localized screw kernel—perhaps through a Birman–Krein spectral-shift identity, a trace formula for the Friedrichs realization, or Suzuki's finite characteristic function—then v13.265 plus the present Laguerre–Pólya closure would convert it directly into the critical-line statement.

Until that identity is proved, the RH/GRH frontier remains open.