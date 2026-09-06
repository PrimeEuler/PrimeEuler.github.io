# Cone Derivation Ledger v13.276 — Suzuki v2 Source Correction and D12 Archimedean Form Closure

Date: 2026-09-06

Status: SOURCE CORRECTION + EXACT CONDUCTOR SCALAR + D12 FINITE-FORM CLOSURE REDUCTION — GRH NOT PROVED

## 0. Synchronization and correction of the Suzuki target

Immediately before this write, the authoritative README, current `master` tip, and highest ledger state were re-fetched. The tip remained

`0828e1dc7f2d56fcb97a7d4af7d208b76ef4d2c0`,

with v13.275 the highest checkpoint and no newer external-audit entry present.

A fresh source check of the current arXiv v2 of Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2, revised 17 Aug 2026, corrects an error in v13.274.

The current v2 Corollary 1.6 states the conjectural compact-uniform limit

\[
\boxed{
\lim_{a\to\infty} e^{\phi(a,z)}W(a,\theta;z)
=
 z^2\frac{\xi(1/2-iz)}{\xi'(1/2-iz)}.
}
\]

Therefore the statement in v13.274 that the current v2 target is

\[
\frac{\xi}{\xi+\xi'}
\]

is incorrect and is superseded by the present checkpoint.

This correction does not affect the exact finite-interval constructions in v13.274–v13.275: Suzuki's Friedrichs theorem, deficiency indices `(1,1)`, and the finite characteristic function `W(a,theta;z)` remain as stated. It changes only the attributed infinite-volume target.

For the D12 extension, the Suzuki-faithful target is consequently

\[
\boxed{
 e^{\phi_K(a,z)}W_K(a,\theta(a);z)
 \stackrel{?}{\longrightarrow}
 z^2\frac{\xi_K(1/2-iz)}{\xi_K'(1/2-iz)}.
}
\]

No convergence theorem and no GRH conclusion are claimed.

---

## 1. The completed D12 gamma/conductor factor

For

\[
K=\mathbb Q(\sqrt3),
\qquad d_K=12,
\qquad (r_1,r_2)=(2,0),
\]

we use

\[
\xi_K(s)
=
 s(s-1)
 12^{s/2}\pi^{-s}\Gamma(s/2)^2\zeta_K(s)
\]

up to a nonzero constant normalization.

The archimedean/conductor logarithmic derivative is

\[
\boxed{
\frac12\log 12-\log\pi+\psi(s/2),
}
\]

where `psi=Gamma'/Gamma`.

For the Riemann zeta factor, Suzuki's corresponding real-place multiplier is

\[
\frac12\psi(s/2)-\frac12\log\pi.
\]

Hence, exactly,

\[
\boxed{
\frac12\log 12-\log\pi+\psi(s/2)
=2\left(\frac12\psi(s/2)-\frac12\log\pi\right)
+\frac12\log 12.
}
\]

Thus the D12 degree-two real-place contribution is two copies of Suzuki's Riemann gamma contribution plus one constant conductor term.

The pole/entire-normalization contribution from `s(s-1)` is **not** doubled: the completed Dedekind function still contains one factor `s(s-1)`. This guardrail prevents the incorrect shorthand “the whole archimedean piece is twice Riemann.” Only the gamma part doubles.

---

## 2. Suzuki's Fourier-form normalization

Suzuki's 2023 screw-function analysis writes the real archimedean contribution to the relevant quadratic form in the shape

\[
I_\infty
=
\frac1{2\pi}\int_{\mathbb R}
\Re\left[
\frac12\psi\left(\frac{s}{2}\right)-\frac12\log\pi
\right]
\left(
|\Phi_1(\phi;z)|^2+|\Phi_1(\phi;-z)|^2
\right)dz,
\]

with

\[
\Phi_1(\phi;z)
=
\frac{\widehat\phi(z)-\widehat\phi(0)}{z}.
\]

On Suzuki's `D^*GD` core take

\[
\phi=Df,
\qquad
D=i\frac d{dx},
\qquad
f\in H_0^1(-a,a).
\]

Because `f` vanishes at the endpoints,

\[
\widehat{Df}(0)=0.
\]

With the Fourier convention `hat f(z)=int f(x)e^{izx}dx`, integration by parts gives

\[
\widehat{Df}(z)=z\widehat f(z).
\]

Therefore

\[
\boxed{
\Phi_1(Df;z)=\widehat f(z).
}
\]

This identity turns the conductor constant into an ordinary scalar operator.

---

## 3. Exact conductor contribution

The extra D12 conductor multiplier in the bracket is

\[
C_{12}=\frac12\log 12.
\]

Its quadratic-form contribution is

\[
I_{\rm cond}[f]
=
\frac{C_{12}}{2\pi}
\int_{\mathbb R}
\left(
|\widehat f(z)|^2+|\widehat f(-z)|^2
\right)dz.
\]

By Parseval,

\[
\frac1{2\pi}\int_{\mathbb R}|\widehat f(z)|^2dz
=\|f\|_2^2,
\]

and the same holds with `z` replaced by `-z`. Hence

\[
\boxed{
I_{\rm cond}[f]
=(\log 12)\|f\|_2^2.
}
\]

Equivalently, on the finite-interval `D^*GD` operator core,

\[
\boxed{
B_{\rm cond}=(\log 12)I.
}
\]

This answers the open question at the end of v13.275 exactly:

\[
\boxed{
\text{the conductor does not disappear under screw anchoring; it becomes a scalar shift.}
}
\]

It is therefore analytically harmless for domains, deficiency indices, compactness, and self-adjoint extension structure.

---

## 4. Exact D12 finite-form decomposition on the core

Separate the D12 finite operator into four pieces:

\[
B_{K,a}
=
B_{\rm pole,a}
+2B_{\gamma,a}^{(\zeta)}
+(\log12)I
+V_{K,a},
\]

where

\[
\boxed{
V_{K,a}
=-\sum_{\log n\le2a}
\frac{b_K(n)}{\sqrt n}
\left(
S_{a,\log n}+S_{a,\log n}^*
\right),
}
\]

and

\[
b_K(n)=\Lambda(n)(1+\chi_{12}(n))\ge0.
\]

Here:

- `B_pole,a` is the contribution of the single `s(s-1)` factor;
- `B_gamma,a^(zeta)` is Suzuki's one-real-place gamma contribution;
- `(log12)I` is the exact conductor shift just derived;
- `V_K,a` is the exact finite prime-power shift operator from v13.273.

For fixed `a`, `V_K,a` is bounded because only `log n<=2a` occurs.

The pole contribution is a smooth finite-interval kernel contribution and hence bounded at the form level.

Thus the only unbounded/high-frequency component is

\[
2B_{\gamma,a}^{(\zeta)}.
\]

---

## 5. Lower boundedness of the D12 gamma multiplier

On the critical Fourier line put

\[
s=\frac12+iz.
\]

The D12 gamma multiplier is

\[
m_{K,\gamma}(z)
=
\Re\left[
\psi\left(\frac14+\frac{iz}{2}\right)-\log\pi
\right].
\]

The digamma asymptotic gives

\[
\Re\psi\left(\frac14+\frac{iz}{2}\right)
=\log|z|+O(1)
\qquad(|z|\to\infty).
\]

Because the argument has fixed positive real part `1/4`, there are no gamma poles on this line. Hence `m_{K,gamma}(z)` is continuous on the real axis and tends to `+infinity` logarithmically.

Therefore

\[
\boxed{
\inf_{z\in\mathbb R}m_{K,\gamma}(z)>-\infty.
}
\]

After adding a sufficiently large scalar constant, the gamma part defines a positive weighted Fourier form.

Consequently the D12 gamma form is closable and lower bounded with the same logarithmic high-frequency form domain as Suzuki's Riemann gamma form; multiplying the gamma contribution by `2` does not change that domain.

---

## 6. Form-domain equivalence with the Riemann finite problem

The Riemann and D12 finite forms differ, at high Fourier frequency, only by multiplication of the real gamma weight by `2`. All other differences on a fixed interval are bounded form perturbations:

\[
B_{\rm pole,a},
\qquad
(\log12)I,
\qquad
V_{K,a}.
\]

Therefore their shifted form norms are equivalent:

\[
\boxed{
\|f\|_{Q_{K,a},c}
\asymp
\|f\|_{Q_{\zeta,a},c'}
}
\]

for suitable lower-bound shifts `c,c'` depending on `a`.

In particular, the closure of `C_c^\infty(-a,a)` in the D12 form norm has the same underlying form-domain topology as in Suzuki's finite Riemann construction.

This removes the main analytic uncertainty left in v13.275: no new degree-two singular domain is introduced by the field gamma factor or conductor.

---

## 7. Consequence for the D12 Friedrichs construction

Suzuki's proof of Theorem 1.1 uses:

1. lower boundedness and closedness of the localized Weil form;
2. equality of the `D^*GD` form with the Weil form on `H_0^1(-a,a)`;
3. density/core control in the form norm.

For D12:

- the prime part is an exact bounded perturbation;
- the conductor is exactly `(log12)I`;
- the gamma part has the same form domain as Suzuki's real-place gamma contribution, with multiplicity two;
- the pole term is bounded on a fixed interval.

Hence the finite D12 form has the same closability/core mechanism as the Riemann finite form once the standard Dedekind Weil explicit formula is inserted.

This yields the project-level finite-form theorem:

\[
\boxed{
Q_{W,K}^{a}
\text{ is lower bounded and closable on the Suzuki finite-interval core.}
}
\]

Let `A_{K,a}` be the self-adjoint operator associated with its closure. Then the same core argument gives

\[
\boxed{
A_{K,a}
\text{ is the Friedrichs extension of }
B_{K,a}=D^*G_{K,a}D
}
\]

provided the D12 screw kernel is normalized by the standard completed Dedekind explicit formula described above.

This is a transfer of Suzuki's finite-form theorem, not a theorem attributed to Suzuki for number fields.

No RH/GRH assumption is used.

---

## 8. Deficiency structure now becomes unconditional within the D12 construction

With the finite form theorem in hand, choose

\[
\lambda<\lambda_{K,a}:=\inf\sigma(A_{K,a})
\]

and set

\[
T_{K,a}=A_{K,a}-\lambda I>0.
\]

The transfer lemma of v13.275 then applies to the established D12 finite operator rather than to a hypothetical one.

Thus

\[
\boxed{
T_{K,a}v_{K,+}=e^x,
\qquad
T_{K,a}v_{K,-}=e^{-x},
}
\]

and

\[
\boxed{
n_+=n_-=1.
}
\]

The corresponding finite characteristic function

\[
\boxed{
W_K(a,\theta;z)
=(z-i)\int_{-a}^{a}v_{K,+}(x)e^{izx}dx
+e^{i\theta}(z+i)\int_{-a}^{a}v_{K,-}(x)e^{izx}dx
}
\]

is entire and has only real zeros for every fixed finite `a`.

The remaining hard problem is therefore no longer finite self-adjointness or deficiency theory. It is the infinite-volume normalization/convergence problem.

---

## 9. Corrected Suzuki-faithful D12 GRH criterion

The current source-faithful target is

\[
\boxed{
 e^{\phi_K(a,z)}W_K(a,\theta(a);z)
 \stackrel{?}{\longrightarrow}
 z^2\frac{\xi_K(1/2-iz)}{\xi_K'(1/2-iz)}.
}
\]

Suzuki proves in the Riemann framework that if the analogous convergence holds uniformly on compact sets, RH follows because every finite characteristic function has only real zeros.

The D12 transfer suggests the conditional field criterion:

\[
\boxed{
\text{compact-uniform D12 Suzuki convergence}
\Longrightarrow
\mathrm{GRH}(\zeta_K).
}
\]

A local version may also suffice near individual zeros after excluding poles of the target, but multiplicities require care because `xi/xi'` has a simple zero at any zero of `xi` only after cancellation is interpreted locally. This should be handled in the next zero-local analysis rather than assumed globally.

---

## 10. What is exact now

1. The v13.274 attribution of `xi/(xi+xi')` to current Suzuki v2 is corrected. Current v2 uses `z^2 xi/xi'`.
2. The D12 real gamma contribution is exactly twice Suzuki's Riemann real-gamma contribution.
3. The D12 conductor `12` contributes exactly
   \[
   \boxed{(\log12)I}
   \]
   on the `D^*GD` core.
4. The conductor does not alter the form domain.
5. The prime contribution remains an exact bounded finite sum of symmetric truncated shifts.
6. The D12 gamma multiplier is continuous, bounded below, and asymptotic to `log|z|`.
7. The D12 finite form has the same high-frequency form domain as Suzuki's Riemann finite form.
8. The Friedrichs/deficiency/finite-real-zero machinery therefore transfers to the D12 completed field construction without RH/GRH.

## 11. Remaining frontier

The finite-volume existence problem is now essentially closed. The main frontier is Suzuki's own hard frontier:

\[
\boxed{
\text{control }\lambda_{K,a},\ v_{K,\pm},\ \theta(a),\ \phi_K(a,z)
\text{ as }a\to\infty.
}
\]

The highest-value next step is to use Suzuki's Section 6–8 formulas as literally as possible to derive:

- the exact Lagrangian boundary condition defining `W_K`;
- parity simplifications for the even D12 kernel;
- the `theta=pi` specialization;
- the first asymptotic normalization constraints on `phi_K(a,z)`;
- and a zero-local Hurwitz criterion matched to the corrected `z^2 xi_K/xi_K'` target.

That is now the clean continuation point.