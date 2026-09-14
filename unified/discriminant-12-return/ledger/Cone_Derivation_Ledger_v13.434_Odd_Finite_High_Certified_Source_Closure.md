# Cone Derivation Ledger v13.434 — Odd Finite-High Certified-Source Closure

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N]** midpoint numerical; **[N-cert]** outward-certified numerical inequality; **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was assigned only after a fresh live-ledger search immediately before writing. The newest numbered entry at that check was `v13.433` (`Suzuki Mod-24 Class-Average / Fluctuation Schur Diagnostic`), so `v13.434` was free at creation time.

The active finite-high target is

\[
A_{FF}^{(0)}\succeq0.53I,
\qquad
F=\{22,24,\ldots,4000\},
\]

for the pole-free odd-sector finite-high block. Since

\[
A_{FF}=A_{FF}^{(0)}+2dd^T,
\qquad 2dd^T\succeq0,
\]

this suffices for the full finite-high block.

## 1. Certified-source nominal generator [D/N-cert]

The new replay

`research-notes/suzuki_odd_M4000_certified_source_nominal_replay.py`

assembles the source-faithful pole-free matrix without adaptive quadrature or scipy special-function values.

Its three source channels are generated as follows.

### 1.1 Archimedean channel

`research-notes/suzuki_even_arch_symbolic_rational_certificate.py` builds the exact degree-64 `h_32` polynomial from Bernoulli and Euler numbers and uses the parity-correct even-mode recurrence

\[
I_0=J_0=0,
\qquad
I_p=-\frac p bJ_{p-1},
\qquad
J_p=-\frac{2^p}{b}+\frac p bI_{p-1},
\qquad b=r\pi.
\]

Writing `y=1/b`, both the polynomial `H_n^(32)` and archimedean diagonal become exact rational polynomials in `y`.

The certified rational pi interval gives uniform polynomial-value widths

\[
\operatorname{width}(H_n^{(32)})<9.3\times10^{-23},
\]

\[
\operatorname{width}(D_n^{(32)})<1.3\times10^{-23}.
\]

The audited analytic truncation from v13.357 remains

\[
\boxed{\|\Delta K_{\rm arch}\|_2\le1.22\times10^{-13}.}
\]

Explicit Horner evaluation has about 128 multiply/add operations, while the worst absolute polynomial term sums are only about

\[
3.63\times10^{-3}
\quad\text{and}\quad
2.45\times10^{-4}.
\]

A deliberately loose numerical arch allowance

\[
\boxed{10^{-12}}
\]

therefore dominates the binary64 polynomial-evaluation rounding by many orders of magnitude.

### 1.2 Prime channel

`research-notes/suzuki_prime_trig_rational_certificate.py` uses exact Fraction arithmetic for

\[
\pi=16\arctan(1/5)-4\arctan(1/239),
\]

\[
\log q=2\operatorname{atanh}\frac{q-1}{q+1},
\qquad q\in\{2,3,4,5,7\},
\]

plus rational square-root brackets and degree-40 Taylor enclosures for the five base rotations.

For all `r<=2000`, the worst propagated trigonometric source uncertainty is below

\[
5.4\times10^{-10}.
\]

The helper proves the uniform prime-sequence bound

\[
\boxed{|\Delta P_r|<10^{-9}}
\]

and prime-diagonal bound

\[
\boxed{|\Delta D_r^{\rm prime}|<4\times10^{-10}}.
\]

An additional `10^-11` scalar allowance is charged in the combined replay for binary64 recurrence/weight arithmetic. This is conservative: a 2000-step length-2 rotation recurrence has standard accumulated `gamma` scale below about `2e-12`.

Using the exact Cauchy sensitivity from v13.425,

\[
\|\Delta A_{\rm off}\|_2
\le4.76188937\|\Delta Z\|_\infty,
\]

and the fact that the prime sequence enters `Z` with coefficient two, the combined prime operator budget is

\[
\boxed{\|\Delta A_{\rm prime}\|_2<1.003\times10^{-8}.}
\]

### 1.3 Cusp channel

`research-notes/suzuki_even_cusp_rational_certificate.py` uses only exact rational intervals.

For even `n`, with `x=n pi`,

\[
\sin x=0,
\qquad
\cos x=1,
\]

so

\[
\operatorname{Si}(x)=\frac\pi2-F(x),
\qquad
\operatorname{Ci}(x)=-G(x).
\]

The auxiliary functions are enclosed using the Laplace forms

\[
F(x)=\int_0^\infty\frac{e^{-xt}}{1+t^2}\,dt,
\qquad
G(x)=\int_0^\infty\frac{t e^{-xt}}{1+t^2}\,dt,
\]

and the finite geometric identity for `1/(1+t^2)`, giving explicit first-omitted-Laplace-moment remainders.

The logarithm is range-reduced by

\[
\frac n4=2^e y,
\qquad1\le y<2,
\]

so

\[
\log(n/4)=e\log2+\log y,
\]

with the atanh parameter for `y` at most `1/3`.

Across all 1990 modes the exact-rational helper obtains

\[
\operatorname{width}(\log(n/4))<1.4\times10^{-19},
\]

\[
\operatorname{width}(\operatorname{Si}(n\pi))<4.3\times10^{-14},
\]

\[
\operatorname{width}\!\left(
\log(n/4)-\operatorname{Ci}(n\pi)-\frac{\operatorname{Si}(n\pi)}{n\pi}
\right)<7.4\times10^{-15}.
\]

The combined cusp operator allowance is therefore only

\[
\boxed{\|\Delta A_{\rm cusp}\|_2<1.6\times10^{-13}.}
\]

## 2. Final binary64 assembly budget [N-cert]

For off-diagonal entries

\[
A_{mn}=-\frac2\pi\frac{nZ_m-mZ_n}{n^2-m^2},
\qquad m\ne n,
\]

use the already-valid finite-high source envelope

\[
|Z_n|<8,
\qquad n\le4000.
\]

Because modes differ by at least two,

\[
|n^2-m^2|\ge92.
\]

A direct binary64 operation count gives a per-entry assembly error below `4e-13`, including the final symmetrization. The dimension is 1990, so the row-sum/operator conversion yields

\[
\boxed{\|\Delta A_{\rm assembly}\|_2<8\times10^{-10}.}
\]

This bound is intentionally loose.

## 3. Total exact-source to nominal operator budget [N-cert]

The combined replay uses

\[
\begin{aligned}
\varepsilon_{\rm prime}&<1.003\times10^{-8},\\
\varepsilon_{\rm cusp}&<1.6\times10^{-13},\\
\varepsilon_{\rm arch}&<1.122\times10^{-12},\\
\varepsilon_{\rm assembly}&<8\times10^{-10}.
\end{aligned}
\]

Hence

\[
\boxed{
\|B_{\rm exact}-B_{\rm nominal}\|_2
<1.1\times10^{-8}.
}
\]

This is vastly weaker than the historical `2e-13` target from v13.357, but it is more than sufficient for the present factor margin.

## 4. Deterministic nominal replay [N]

The certified-source generator reproduces the midpoint finite-high spectrum without scipy quadrature or scipy Si/Ci:

\[
\boxed{
\lambda_{\min}(A_{FF,\rm nominal}^{(0)})
\approx0.53284238378444.
}
\]

Thus

\[
\boxed{
\lambda_{\min}(B_{\rm nominal})
\approx0.00284238378444.
}
\]

The binary64 Cholesky point residual is approximately

\[
4.1\times10^{-14}.
\]

This agrees with the earlier scipy-based midpoint replay at the `~10^-12` scale while using a logically independent source generator.

## 5. Verified factor floor [N-cert]

Replaying the v13.424 verified-inverse route on the certified-source nominal gives

\[
\|X\|_F\approx27.65454<28,
\]

with point

\[
\|I-LX\|_F\approx6.4\times10^{-15}.
\]

The standard product factor

\[
\gamma_{1990}=\frac{1990u}{1-1990u}
\]

combined with

\[
\||L||X|\|_F\approx96.83
\]

gives an outward product allowance about

\[
2.14\times10^{-11},
\]

hence safely

\[
\boxed{\|I-LX\|_2<10^{-8}.}
\]

Similarly, the Cholesky reconstruction remains safely below

\[
\boxed{\|B_{\rm nominal}-LL^T\|_2<6\times10^{-11}.}
\]

Therefore

\[
\lambda_{\min}(LL^T)
>
\frac{(1-10^{-8})^2}{28^2}
>
0.0012755.
\]

## 6. Certified finite-high positivity [N-cert]

Combining the factor floor, Cholesky reconstruction error, and source/assembly budget gives

\[
\lambda_{\min}(B_{\rm exact})
>
0.0012755
-6\times10^{-11}
-1.1\times10^{-8}.
\]

Thus conservatively

\[
\boxed{
\lambda_{\min}(B_{\rm exact})>0.00125.
}
\]

Since

\[
B_{\rm exact}=A_{FF}^{(0)}-0.53I,
\]

we have now certified

\[
\boxed{
A_{FF}^{(0)}\succeq0.53125 I>0.53I.
}
\]

In particular,

\[
\boxed{
A_{FF}^{(0)}\succeq0.53I.
}
\]

Finally, because `2dd^T` is exactly PSD,

\[
\boxed{
A_{FF}=A_{FF}^{(0)}+2dd^T\succeq0.53I.
}
\]

This closes the odd finite-high positivity obligation that remained open in v13.406/v13.407/v13.417/v13.424.

## 7. Interaction with v13.433 [Audit]

The concurrently-landed v13.433 mod-24 Schur diagnostic remains structurally useful but is not needed for this finite-high closure. It shows that the balanced class-average sector is safe while the near-critical scale survives in the fluctuation sector after rank-4 feedback. The present certificate instead proves the entire finite-high block positive directly.

The two results are compatible:

\[
\boxed{
\text{v13.433 explains where the small finite-high margin lives;}
\quad
\text{v13.434 certifies that the margin is still strictly positive.}
}
\]

## 8. Guardrails and next target [Audit]

This checkpoint closes only the finite-high condition

\[
A_{FF}\succeq0.53I.
\]

It does **not** yet promote

\[
\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2.
\]

The remaining odd-sector proof obligations are still:

1. independently regenerate and outward-certify
   \[
   \|A_{FT}\|<1.015;
   \]
2. independently close the normalized frozen-subspace bounds
   \[
   C_{\rm odd}\succeq0.80I,
   \qquad
   H_{\rm odd}<0.225I;
   \]
3. then combine them with the raw tail floor and the now-closed finite-high bound.

No exact-zero, RH, or GRH statement is made.

---

**Checkpoint conclusion.** The pole-free odd finite-high block is now outward-certified above `0.53 I` using a deterministic source-faithful nominal generator built from rational prime, cusp, and archimedean certificates. The exact PSD pole then gives the full finite-high result `A_FF >= 0.53 I`. The odd-sector theorem itself remains open pending the cross-tail and normalized residual-Gram certifications.
