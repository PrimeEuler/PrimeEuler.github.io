# Cone Derivation Ledger v13.266 — Finite-Interval Arithmetic-Ramp Truncation and Exponential Real-Axis Convergence

Date: 2026-09-06
Status: EXACT FINITE-INTERVAL ARITHMETIC RESULT + QUANTITATIVE CONVERGENCE THEOREM — RH/GRH NOT PROVED

## 0. Synchronization and scope

Immediately before this write, the authoritative project README, current `master` tip, v13.265, and the current ledger state were re-fetched.

The current tip was

`a7bb0b6af6cef267484f6ff72c9ddf45f53dc3d2`,

with v13.265 the highest ledger checkpoint and no newer external-audit checkpoint present.

The previous entry reduced the operator program to a very specific real-axis target: if positive finite-interval squared Weyl functions converge to the arithmetic

\[
\mathcal S_K(w)
=
\frac1{\sqrt w}
\frac{\xi_K'}{\xi_K}\left(\frac12+\sqrt w\right)
\]

on one interval `w>1/4`, then the Stieltjes normal-family argument forces the D12 Dedekind GRH statement.

The present entry asks a narrower question first:

\[
\boxed{
\text{what part of that real-axis convergence is already forced purely by the finite-interval arithmetic kernel?}
}
\]

The answer is strong:

\[
\boxed{
\text{the non-archimedean finite-interval ramp converges monotonically and exponentially fast on every compact real interval }w>1/4.
}
\]

Thus the remaining difficulty is not the long-prime tail. It is the nonlinear passage from the restricted screw/form kernel to the boundary Weyl function.

## 1. Positive Dedekind generalized-von-Mangoldt coefficients

Let

\[
K=\mathbf Q(\sqrt3),
\qquad
\chi=\chi_{12}.
\]

From v13.257 and v13.262,

\[
\boxed{
b_K(n)=\Lambda(n)(1+\chi(n))\ge0.}
\]

The completed field screw function has a non-archimedean ramp

\[
\boxed{
R_K(t)
=
\sum_{n\le e^t}
\frac{b_K(n)}{\sqrt n}
(t-\log n),
\qquad t\ge0.
}
\]

Equivalently,

\[
\boxed{
R_K(t)
=
\sum_{n\ge1}
\frac{b_K(n)}{\sqrt n}
(t-\log n)_+.
}
\]

Its distributional second derivative is the positive arithmetic measure

\[
\boxed{
R_K''
=
\mu_K
=
\sum_{n\ge1}
\frac{b_K(n)}{\sqrt n}\,\delta_{\log n}
\ge0.
}
\]

## 2. Why a finite interval sees only finitely many prime powers

Fix `a>0` and restrict the continuous screw kernel to

\[
[-a,a]\times[-a,a].
\]

Every difference variable satisfies

\[
|x-y|\le2a.
\]

The arithmetic ramp at a nonnegative argument `t` contains a prime-power term indexed by `n` only when

\[
\log n\le t.
\]

Therefore on the restricted interval the non-archimedean kernel can involve only

\[
\boxed{n\le e^{2a}.}
\]

This is an exact support statement, not an asymptotic one.

It is independent of any spectral conjecture and follows directly from the ramp support

\[
(t-\log n)_+.
\]

Thus finite interval length corresponds arithmetically to a sharp logarithmic prime-power horizon.

## 3. The exact truncated ramp transform

For a cutoff `T>0`, define

\[
\boxed{
\mathfrak M_{K,T}(z)
:=
z^2\int_0^T R_K(t)e^{-zt}\,dt,
\qquad z>0.
}
\]

For one prime-power term with `u=\log n\le T`, direct integration gives

\[
\begin{aligned}
z^2\int_u^T(t-u)e^{-zt}\,dt
&=
e^{-zu}\Bigl[1-e^{-z(T-u)}\bigl(1+z(T-u)\bigr)\Bigr].
\end{aligned}
\]

Since `e^{-zu}=n^{-z}`, we obtain the exact finite-cutoff identity

\[
\boxed{
\mathfrak M_{K,T}(z)
=
\sum_{\log n\le T}
\frac{b_K(n)}{n^{1/2+z}}
\Bigl[
1-e^{-z(T-\log n)}\bigl(1+z(T-\log n)\bigr)
\Bigr].
}
\]

This is the finite-interval arithmetic transform naturally associated with the ramp.

For the actual interval `[-a,a]`, set

\[
\boxed{T=2a.}
\]

## 4. Infinite-volume limit

For

\[
z>\frac12,
\qquad
s=\frac12+z>1,
\]

the full positive Euler-product logarithmic derivative is

\[
\boxed{
M_K(z)
:=
-\frac{\zeta_K'}{\zeta_K}\left(\frac12+z\right)
=
\sum_{n\ge1}
\frac{b_K(n)}{n^{1/2+z}}.
}
\]

For each fixed `n`, once `T>\log n`, define

\[
q_{n,z}(T)
:=
1-e^{-z(T-\log n)}\bigl(1+z(T-\log n)\bigr).
\]

Then

\[
0\le q_{n,z}(T)<1,
\]

and

\[
\frac{d}{dT}q_{n,z}(T)
=
z^2(T-\log n)e^{-z(T-\log n)}
\ge0.
\]

Therefore every coefficient contribution is monotone increasing in `T`.

Because all `b_K(n)` are nonnegative,

\[
\boxed{
0\le
\mathfrak M_{K,T}(z)
\nearrow
M_K(z)
\qquad(T\to\infty),
}
\]

for every real `z>1/2`.

This monotonicity is exact.

## 5. Exact positive error decomposition

Subtracting the truncated transform from the full logarithmic derivative gives

\[
E_T(z)
:=
M_K(z)-\mathfrak M_{K,T}(z).
\]

Using the formula above,

\[
\boxed{
\begin{aligned}
E_T(z)
={}&
\sum_{\log n>T}
\frac{b_K(n)}{n^{1/2+z}}
\\
&+
\sum_{\log n\le T}
\frac{b_K(n)}{n^{1/2+z}}
 e^{-z(T-\log n)}
 \bigl(1+z(T-\log n)\bigr).
\end{aligned}
}
\]

Hence

\[
\boxed{E_T(z)\ge0.}
\]

The error has two transparent pieces:

1. the genuine long-prime-power tail `\log n>T`;
2. the finite-upper-limit boundary remainder for prime powers already visible before the cutoff.

This decomposition is useful because both pieces have the same exponential scale.

## 6. Elementary coefficient domination

Since

\[
\chi(n)\in\{-1,0,1\}
\]

on prime powers and

\[
0\le1+\chi(n)\le2,
\]

we have

\[
\boxed{
0\le b_K(n)\le2\Lambda(n)\le2\log n
\qquad(n\ge2).
}
\]

No prime-number theorem is needed for the following convergence estimate.

## 7. Long-tail bound

Let

\[
x=e^T,
\qquad
s=\frac12+z>1.
\]

Then

\[
\sum_{n>x}\frac{b_K(n)}{n^s}
\le
2\sum_{n>x}\frac{\log n}{n^s}.
\]

By the integral test, for fixed `s>1`,

\[
\sum_{n>x}\frac{\log n}{n^s}
\le
C_s\,x^{1-s}(1+\log x),
\]

where `C_s` may be chosen locally bounded on compact subsets of `(1,\infty)`.

Since

\[
x^{1-s}
=
e^{-(s-1)T}
=
e^{-(z-1/2)T},
\]

we obtain

\[
\boxed{
\sum_{\log n>T}
\frac{b_K(n)}{n^{1/2+z}}
\le
C_z(1+T)e^{-(z-1/2)T}.
}
\]

## 8. Boundary-remainder bound

For the second error term,

\[
\begin{aligned}
B_T(z)
&:=
\sum_{\log n\le T}
\frac{b_K(n)}{n^{1/2+z}}
 e^{-z(T-\log n)}
 \bigl(1+z(T-\log n)\bigr)
\\
&=
e^{-zT}
\sum_{n\le e^T}
\frac{b_K(n)}{\sqrt n}
\bigl(1+z\log(e^T/n)\bigr).
\end{aligned}
\]

Using `b_K(n)\le2\log n`, elementary integral comparison yields

\[
\sum_{n\le x}
\frac{\log n}{\sqrt n}
\bigl(1+z\log(x/n)\bigr)
\le
C_z\,x^{1/2}(1+\log x)^2.
\]

Therefore

\[
\boxed{
B_T(z)
\le
C_z(1+T)^2e^{-(z-1/2)T}.
}
\]

Combining the two pieces gives the quantitative theorem

\[
\boxed{
0\le
M_K(z)-\mathfrak M_{K,T}(z)
\le
C_z(1+T)^2e^{-(z-1/2)T},
\qquad z>\frac12.
}
\]

The constant can be chosen uniformly when `z` ranges over a compact subinterval of `(1/2,\infty)`.

## 9. Finite-interval form

Setting `T=2a`,

\[
\boxed{
0\le
M_K(z)-\mathfrak M_{K,2a}(z)
\le
C_z(1+a)^2e^{-2a(z-1/2)}.
}
\]

Thus the arithmetic part of the finite-interval kernel approaches its infinite-volume logarithmic derivative exponentially fast for every fixed real `z>1/2`.

On a compact interval

\[
z\in[z_0,z_1],
\qquad z_0>\frac12,
\]

we have uniformly

\[
\boxed{
M_K(z)-\mathfrak M_{K,2a}(z)
=
O\!\left((1+a)^2e^{-2a(z_0-1/2)}\right).
}
\]

## 10. Translation to the squared real-axis variable

Put

\[
z=\sqrt w.
\]

Then the Euler-product region is exactly

\[
\boxed{w>\frac14.}
\]

For any compact interval

\[
J=[w_0,w_1]\subset(1/4,\infty),
\]

define

\[
\delta_J:=\sqrt{w_0}-\frac12>0.
\]

Then uniformly for `w\in J`,

\[
\boxed{
M_K(\sqrt w)-\mathfrak M_{K,2a}(\sqrt w)
=
O_J\!\left((1+a)^2e^{-2a\delta_J}\right).
}
\]

This is precisely the real interval on which v13.265 showed that convergence of positive squared Weyl functions would be enough to force the Stieltjes continuation.

## 11. The archimedean term is not a prime-tail problem

The full centered completed logarithmic derivative is

\[
F_K(z)
=
\frac{\xi_K'}{\xi_K}\left(\frac12+z\right).
\]

From v13.263,

\[
\boxed{
F_K(z)
=
\frac1{1/2+z}
+
\frac1{-1/2+z}
+
\frac12\log12-
\log\pi
+
\psi\left(\frac14+\frac z2\right)
-
M_K(z).
}
\]

The rational/gamma/conductor part is explicit and independent of any prime cutoff.

Therefore replacing `M_K(z)` by the finite-interval arithmetic transform gives an explicit approximation

\[
\boxed{
F_{K,a}^{\rm arith}(z)
:=
\frac1{1/2+z}
+
\frac1{-1/2+z}
+
\frac12\log12-
\log\pi
+
\psi\left(\frac14+\frac z2\right)
-
\mathfrak M_{K,2a}(z),
}
\]

with

\[
\boxed{
F_{K,a}^{\rm arith}(z)-F_K(z)
=
E_{2a}(z)
\ge0
}
\]

for real `z>1/2`, and exponentially small error on compact real intervals.

Dividing by `z=\sqrt w`, define

\[
\mathcal S_{K,a}^{\rm arith}(w)
:=
\frac{F_{K,a}^{\rm arith}(\sqrt w)}{\sqrt w}.
\]

Then on every compact `J\subset(1/4,\infty)`,

\[
\boxed{
\mathcal S_{K,a}^{\rm arith}(w)
-
\mathcal S_K(w)
=
O_J\!\left((1+a)^2e^{-2a\delta_J}\right).
}
\]

This solves the arithmetic truncation problem on the exact real-axis domain required by v13.265.

## 12. Monotonicity direction

Because

\[
\mathfrak M_{K,2a}(z)\nearrow M_K(z),
\]

we have for real `z>1/2`

\[
F_{K,a}^{\rm arith}(z)
\searrow
F_K(z).
\]

Consequently

\[
\boxed{
\mathcal S_{K,a}^{\rm arith}(w)
\searrow
\mathcal S_K(w)
\qquad(w>1/4).
}
\]

This monotonicity belongs to the explicit arithmetic approximation only.

Guardrail: it is **not yet proved** that Suzuki's finite-interval squared boundary Weyl function `s_{K,a}(w)` equals this arithmetic truncation `\mathcal S_{K,a}^{arith}(w)` or inherits this monotonicity.

That identification remains the central operator problem.

## 13. What finite interval has already solved

At the kernel/arithmetic level, finite interval length `a` automatically provides:

\[
\boxed{
\text{prime-power horizon }n\le e^{2a};
}
\]

\[
\boxed{
\text{positive monotone arithmetic approximation};
}
\]

and

\[
\boxed{
\text{exponential convergence on every compact }J\subset(1/4,\infty).
}
\]

Thus the real-axis arithmetic target required by v13.265 is not itself difficult.

The unresolved map is

\[
\boxed{
\text{restricted screw kernel/form}
\longrightarrow
\text{finite boundary Weyl function}.
}
\]

## 14. Exact decomposition of the remaining mismatch

Let

\[
s_{K,a}(w)
\]

denote the finite-interval squared boundary Weyl compression from v13.265, when constructed in the Suzuki/D12 operator framework.

Insert the explicit arithmetic approximation as an intermediate object:

\[
\boxed{
\begin{aligned}
s_{K,a}(w)-\mathcal S_K(w)
={}&
\underbrace{
\bigl[s_{K,a}(w)-\mathcal S_{K,a}^{\rm arith}(w)\bigr]
}_{\text{operator/boundary mismatch}}
\\
&+
\underbrace{
\bigl[\mathcal S_{K,a}^{\rm arith}(w)-\mathcal S_K(w)\bigr]
}_{\text{explicit exponentially small arithmetic tail}}.
\end{aligned}
}
\]

The second term is now controlled.

Therefore v13.265's GRH-triggering convergence theorem reduces further to proving

\[
\boxed{
s_{K,a}(w)-\mathcal S_{K,a}^{\rm arith}(w)\longrightarrow0}
\]

on one real interval `J\subset(1/4,\infty)`.

This is a much sharper target than direct comparison with the infinite-volume arithmetic function.

## 15. Why this matters for the operator program

The prime tail is often the obvious place to expect difficulty in passing from a finite interval to an infinite arithmetic object.

For the D12 Dedekind channel, positivity removes that difficulty almost completely:

\[
\boxed{
\text{long primes are exponentially suppressed in the exact real-axis domain needed for the normal-family argument.}
}
\]

Hence any obstruction to convergence must come from one of the genuinely operator-theoretic ingredients:

- the changing finite-interval Hilbert-space norm;
- the Friedrichs form completion;
- the choice of self-adjoint boundary extension;
- the deficiency-space normalization;
- the boundary functional;
- or the nonlinear Weyl-function map itself.

That localization is the main strategic gain of this entry.

## 16. Relation to recent numerical work

A recent numerical realization of Suzuki's Weil-quadratic-form operator reports that finite-interval spectral behavior has a substantial archimedean component and that the nontrivial zeros appear through explicit-formula residual structure rather than as naive finite-matrix eigenvalues.

This is consistent with the distinction made here: direct spectral matching is not the correct finite-interval target. The relevant target is the boundary Weyl/Stieltjes function and its arithmetic identification.

No numerical result is used in the proof of any formula in this entry.

## 17. Guardrails

1. No RH or GRH statement is proved here.
2. `\mathfrak M_{K,2a}` is the exact Laplace transform of the restricted arithmetic ramp, not automatically the finite Suzuki Weyl function.
3. The exponential estimate is proved in the real Euler-product region `z>1/2`, equivalently `w>1/4`.
4. Positivity and monotonicity here come from `b_K(n)\ge0`; they should not be generalized to an arbitrary signed Dirichlet channel.
5. The H4/D12 matrix deficiency issue from v13.265 remains active: the full two-channel pair has deficiency `(2,2)`.
6. The finite-interval boundary normalization remains the hard analytic datum.
7. The arithmetic approximation is sufficient only after one proves that the actual finite squared Weyl compression is asymptotic to it.

## 18. New sharpened frontier

Combining v13.265 and the present result gives the following conditional chain.

If for one compact real interval

\[
J\subset(1/4,\infty)
\]

one proves

\[
\boxed{
s_{K,a}(w)-\mathcal S_{K,a}^{\rm arith}(w)\to0
\quad(w\in J),}
\]

then the explicit estimate above gives

\[
s_{K,a}(w)\to\mathcal S_K(w).
\]

Since each `s_{K,a}` is Stieltjes, v13.265's normal-family theorem then forces `\mathcal S_K` to be Stieltjes and hence yields the D12 Dedekind critical-line conclusion.

Thus the project frontier is now

\[
\boxed{
\text{boundary Weyl function}
-
\text{explicit finite arithmetic ramp transform}
\longrightarrow0.
}
\]

The most valuable next derivation is therefore to compute the finite-interval boundary functional explicitly enough to express this difference through a Schur complement, Dirichlet-to-Neumann map, or Krein resolvent formula.

That would convert the final mismatch into an operator norm / boundary trace estimate rather than a zero-location problem.