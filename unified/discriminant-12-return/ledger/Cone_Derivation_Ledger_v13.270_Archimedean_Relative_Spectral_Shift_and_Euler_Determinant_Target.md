# Cone Derivation Ledger v13.270 — Archimedean-Relative Spectral Shift and Euler Determinant Target

Date: 2026-09-06
Status: EXACT RELATIVE-DETERMINANT REDUCTION + STRATEGIC CORRECTION OF THE ABSOLUTE TRACE TARGET — RH/GRH NOT PROVED

## 0. Synchronization and purpose

Immediately before this write, the authoritative project README, current `master` tip, and highest ledger state were re-fetched. The current tip remained

`87cc3889d47ccdf4577ba7c861e90ac3ec313b28`,

with v13.269 the highest ledger checkpoint and no newer external-audit checkpoint present.

The previous entry isolated the finite trace target

\[
\operatorname{Tr}(D_{K,a}^2+w)^{-1}
\stackrel{?}{=}
2\partial_w\log A_K(s(w))
-
\frac1{\sqrt w}
\sum_{\log n\le2a}
\frac{b_K(n)}{n^{1/2+\sqrt w}}
+
\varepsilon_a(w).
\]

The present entry asks whether this should be attacked as an **absolute** spectral trace or as a **relative** trace against the prime-free/archimedean operator.

The latter is the structurally correct target.

The completed arithmetic already splits exactly into an archimedean factor and an Euler factor. Therefore the finite operator program should mirror that split:

\[
\boxed{
\text{full D12 operator}
=
\text{archimedean baseline}
+
\text{arithmetic perturbation}
}
\]

at the level of relative determinants / resolvent traces, not necessarily by literal additive decomposition of unbounded operators.

This removes a large universal background from the comparison and leaves the prime-power term as the sole relative target.

## 1. Exact completed-factor split on the Euler-product real axis

Let

\[
K=\mathbf Q(\sqrt3),
\qquad
s(w)=\frac12+\sqrt w,
\qquad w>\frac14.
\]

Write the completed Dedekind function as

\[
\xi_K(s)=A_K(s)\zeta_K(s),
\]

where, up to a fixed nonzero constant,

\[
\boxed{
A_K(s)=s(s-1)12^{s/2}\pi^{-s}\Gamma(s/2)^2.
}
\]

The squared characteristic function is

\[
\Psi_K(w)=\xi_K(s(w)).
\]

Hence on `w>1/4`,

\[
\boxed{
\Psi_K(w)=A_K(s(w))\zeta_K(s(w)).
}
\]

and therefore

\[
\boxed{
2\partial_w\log\Psi_K(w)
=
2\partial_w\log A_K(s(w))
+
2\partial_w\log\zeta_K(s(w)).
}
\]

Using

\[
\frac{ds}{dw}=\frac1{2\sqrt w}
\]

and

\[
M_K(z):=-\frac{\zeta_K'}{\zeta_K}\left(\frac12+z\right)
=\sum_{n\ge1}\frac{b_K(n)}{n^{1/2+z}},
\]

we get the exact split

\[
\boxed{
\mathcal S_K(w)
=
\mathcal S_{K,\infty}(w)
-
\frac{M_K(\sqrt w)}{\sqrt w},
}
\]

where

\[
\boxed{
\mathcal S_{K,\infty}(w)
:=2\partial_w\log A_K(s(w)).
}
\]

This notation emphasizes that `S_{K,infty}` is the prime-free/archimedean baseline on the Euler-product real axis.

No zero hypothesis is used.

## 2. The arithmetic relative term is completely explicit

From v13.257 and v13.262,

\[
b_K(n)=\Lambda(n)(1+\chi_{12}(n))\ge0.
\]

Thus the entire finite-prime correction is

\[
\boxed{
\mathcal S_K(w)-\mathcal S_{K,\infty}(w)
=
-\frac1{\sqrt w}
\sum_{n\ge1}
\frac{b_K(n)}{n^{1/2+\sqrt w}}.
}
\]

For the finite screw interval `[-a,a]`, the exact arithmetic horizon is

\[
\log n\le2a.
\]

Define

\[
\boxed{
\mathcal R_{K,a}^{E}(w)
:=-\frac1{\sqrt w}
\sum_{\log n\le2a}
\frac{b_K(n)}{n^{1/2+\sqrt w}}.
}
\]

Then v13.269 gives, uniformly on every compact

\[
J=[w_0,w_1]\subset(1/4,\infty),
\]

\[
\boxed{
\mathcal R_{K,a}^{E}(w)
=
\mathcal S_K(w)-\mathcal S_{K,\infty}(w)
+O_J(e^{-2a(\sqrt{w_0}-1/2)}).
}
\]

Thus the arithmetic relative trace is already known to pure exponential accuracy.

## 3. Relative determinant form

Let

\[
L_{K,T}(s)
=
\sum_{\log n\le T}
\frac{b_K(n)}{\log n}\,n^{-s}
\]

and

\[
Z_{K,T}(s)=e^{L_{K,T}(s)}.
\]

Then

\[
2\partial_w\log Z_{K,2a}(s(w))
=
\mathcal R_{K,a}^{E}(w).
\]

The infinite relative determinant is simply

\[
\boxed{
\zeta_K(s(w))^2,
}
\]

because

\[
\partial_w\log\zeta_K(s(w))^2
=
2\partial_w\log\zeta_K(s(w))
=-\frac{M_K(\sqrt w)}{\sqrt w}.
\]

So the finite Euler relative determinant target is

\[
\boxed{
Z_{K,2a}(s(w))^2
\longrightarrow
\zeta_K(s(w))^2
}
\]

with normalized error

\[
\boxed{
1+O_J(e^{-2a(\sqrt{w_0}-1/2)}).
}
\]

This is the determinant-level version of the relative trace split.

## 4. Correct finite operator comparison

Introduce two finite-interval positive squared operators, schematically:

\[
A_{K,a}:=D_{K,a}^2,
\]

for the full localized D12/Dedekind screw form, and

\[
A_{K,a}^{\infty}:=(D_{K,a}^{\infty})^2,
\]

for the corresponding prime-free/archimedean localized form, with identical interval and boundary normalization.

The exact construction of the D12 pair remains open; this notation defines the comparison target rather than asserting existence of a new operator theorem.

The natural finite relative trace is

\[
\boxed{
\mathcal T_{K,a}^{\rm rel}(w)
:=
\operatorname{Tr}
\left[
(A_{K,a}+w)^{-1}
-
(A_{K,a}^{\infty}+w)^{-1}
\right],
}
\]

whenever the resolvent difference is trace class.

The correct arithmetic target is then not the full completed trace but only

\[
\boxed{
\mathcal T_{K,a}^{\rm rel}(w)
\stackrel{?}{=}
\mathcal R_{K,a}^{E}(w)+o(1).
}
\]

Equivalently,

\[
\boxed{
\mathcal T_{K,a}^{\rm rel}(w)
\stackrel{?}{=}
-\frac1{\sqrt w}
\sum_{\log n\le2a}
\frac{b_K(n)}{n^{1/2+\sqrt w}}
+o(1).
}
\]

This is substantially cleaner than the absolute trace formula of v13.269 because the conductor/gamma/pole background has been removed before the arithmetic comparison.

## 5. Relative spectral determinant

If the pair `(A_{K,a},A_{K,a}^{infty})` is resolvent-comparable in the standard determinant sense, define a normalized relative determinant

\[
\mathfrak R_{K,a}(w)
\]

so that

\[
\boxed{
\partial_w\log\mathfrak R_{K,a}(w)
=
\mathcal T_{K,a}^{\rm rel}(w).
}
\]

The target becomes

\[
\boxed{
\frac{\mathfrak R_{K,a}(w)}{\mathfrak R_{K,a}(w_*)}
\longrightarrow
\frac{\zeta_K(s(w))^2}{\zeta_K(s(w_*))^2}
}
\]

on any fixed compact real interval in `w>1/4`.

At finite arithmetic level the explicit comparison object is

\[
\boxed{
\frac{Z_{K,2a}(s(w))^2}{Z_{K,2a}(s(w_*))^2}.
}
\]

Therefore the remaining relative determinant defect is

\[
\boxed{
\mathcal E_{K,a}^{\rm rel}(w)
:=
\frac{
\mathfrak R_{K,a}(w)/\mathfrak R_{K,a}(w_*)
}{
Z_{K,2a}(s(w))^2/Z_{K,2a}(s(w_*))^2
}.
}
\]

The desired theorem is simply

\[
\boxed{
\mathcal E_{K,a}^{\rm rel}(w)\to1
}
\]

uniformly on one compact real interval.

## 6. Why the relative formulation is more canonical

The absolute finite characteristic function contains two qualitatively different pieces:

1. the universal interval/archimedean spectral background;
2. the arithmetic deformation caused by the prime-power part of the screw kernel.

Comparing the absolute finite determinant directly with `Psi_K^2` forces both pieces to be controlled simultaneously.

The relative formulation instead compares

\[
\boxed{
\text{full localized operator}
\quad\text{against}\quad
\text{the same localized operator with the prime term removed}.
}
\]

This fixes the interval, differential part, boundary convention, and archimedean geometry before looking at arithmetic.

It is therefore invariant under many nuisance normalizations that obstructed the scalar Weyl-function comparison in v13.267-v13.268.

## 7. Spectral-shift formulation

Assume for this section that the positive operator pair is resolvent-comparable so that a spectral shift function `xi_a(lambda)` exists in the usual sense.

Then for suitable test functions `f`,

\[
\operatorname{Tr}[f(A_{K,a})-f(A_{K,a}^{\infty})]
=
\int f'(\lambda)\xi_a(\lambda)\,d\lambda.
\]

Taking

\[
f(\lambda)=\frac1{\lambda+w}
\]

gives

\[
\boxed{
\mathcal T_{K,a}^{\rm rel}(w)
=-\int_{\mathbf R}
\frac{\xi_a(\lambda)}{(\lambda+w)^2}\,d\lambda.
}
\]

Thus the finite D12 Euler trace target becomes the exact spectral-shift equation

\[
\boxed{
\int
\frac{\xi_a(\lambda)}{(\lambda+w)^2}\,d\lambda
\stackrel{?}{=}
\frac1{\sqrt w}
\sum_{\log n\le2a}
\frac{b_K(n)}{n^{1/2+\sqrt w}}
+o(1).
}
\]

This is a concrete inverse-transform target for the arithmetic deformation of the finite spectrum.

No positivity of `xi_a` is asserted or required.

That guardrail matters: the arithmetic relative term is negative, so forcing it into a positive Stieltjes measure would be the wrong sign class.

## 8. Laplace form of the relative trace

For `w>0`,

\[
\frac1{(\lambda+w)^2}
=
\int_0^\infty t e^{-t(\lambda+w)}\,dt
\]

whenever the interchange is justified.

Hence

\[
\mathcal T_{K,a}^{\rm rel}(w)
=
-\int_0^\infty
te^{-tw}
\left[
\int e^{-t\lambda}\xi_a(\lambda)\,d\lambda
\right]dt.
\]

The finite prime target can therefore be viewed as asking whether the spectral-shift heat content of the localized operator encodes the cutoff generalized-von-Mangoldt data.

This is a potentially more tractable route than comparing individual finite eigenvalues with zeta zeros.

## 9. Strategic correction to the finite-eigenvalue intuition

Suzuki's 2026 paper formulates a limiting first-order self-adjoint spectral program but does not prove that finite-volume eigenvalues are already approximations to individual zeta-zero ordinates.

A recent 2026 numerical realization of Suzuki's localized Weil-form operator reports a strongly archimedean/universal finite-volume spectral law and finds the zeta-zero information in the explicit-formula residual rather than as a simple one-to-one identification with the raw finite spectrum.

This numerical observation is **not** used as a theorem here. It is, however, consistent with the exact analytic split above:

\[
\boxed{
\text{large universal archimedean baseline}
+
\text{smaller arithmetic spectral shift}.
}
\]

Therefore the project should not require the raw finite spectrum itself to resemble the zero spectrum at finite `a`.

The more invariant object is the arithmetic **change** in spectral data relative to the prime-free operator.

## 10. D12-specific gain

The relative arithmetic coefficients are

\[
\boxed{
b_K(n)=\Lambda(n)(1+\chi_{12}(n))\ge0.}
\]

Thus all field-specific prime information is carried by the split/ramified generalized-prime measure already derived from

\[
a_{12}=1*\chi_{12}.
\]

The inert odd prime powers vanish automatically.

So the proposed relative spectral shift does not need to reproduce a signed prime race. It needs to reproduce the positive Dedekind generalized-prime coefficients, with the minus sign supplied globally by the logarithmic derivative.

This is precisely the arithmetic simplification unique to the field channel emphasized in v13.262.

## 11. Exact three-part error split after relative renormalization

Let

\[
\mathcal T_{K,a}^{\rm full}(w)
:=\operatorname{Tr}(A_{K,a}+w)^{-1},
\]

and similarly define the archimedean trace if both traces make sense after the chosen regularization.

Then schematically

\[
\boxed{
\begin{aligned}
\mathcal T_{K,a}^{\rm full}(w)-\mathcal S_K(w)
={}&
\underbrace{
[\mathcal T_{K,a}^{\infty}(w)-\mathcal S_{K,\infty}(w)]
}_{\text{universal archimedean reference defect}}
\\
&+
\underbrace{
[\mathcal T_{K,a}^{\rm rel}(w)-\mathcal R_{K,a}^{E}(w)]
}_{\text{D12 arithmetic spectral-shift defect}}
\\
&+
\underbrace{
[\mathcal R_{K,a}^{E}(w)-(\mathcal S_K-\mathcal S_{K,\infty})(w)]
}_{\text{explicit exponential Euler tail}}.
\end{aligned}
}
\]

The third term is already solved.

The first term is universal/archimedean rather than D12-specific.

The **only D12-specific unresolved analytic term** is now

\[
\boxed{
\mathcal T_{K,a}^{\rm rel}(w)-\mathcal R_{K,a}^{E}(w).
}
\]

This is the main result of the present reduction.

## 12. Conditional convergence theorem

Suppose one constructs, for all sufficiently large `a`, a resolvent-comparable pair

\[
(A_{K,a},A_{K,a}^{\infty})
\]

from the full and prime-free localized D12 screw forms, using the same interval and boundary normalization.

Assume on one compact interval `J subset (1/4,infty)` that

\[
\boxed{
\mathcal T_{K,a}^{\rm rel}(w)-\mathcal R_{K,a}^{E}(w)\to0
}
\]

uniformly, and separately that the archimedean reference trace converges to `S_{K,infty}` in the required normalized sense.

Then

\[
\operatorname{Tr}(A_{K,a}+w)^{-1}
\to
\mathcal S_K(w)
\]

on `J`.

Combined with the Stieltjes/normal-family mechanism of v13.265, or equivalently with the characteristic-function/Laguerre–Polya mechanism of v13.268-v13.269 once the corresponding determinant normalization is established, this is sufficient to reach the D12 Dedekind GRH criterion.

This is a conditional reduction, not a proof of GRH.

## 13. What is exact and what remains open

### Exact

- The completed real-axis trace splits into archimedean plus Euler terms.
- The relative Euler term is exactly `-M_K(sqrt(w))/sqrt(w)`.
- The finite prime horizon gives the explicit cutoff `R^E_{K,a}`.
- Its error is pure exponential on compact `w>1/4` intervals.
- The relative determinant arithmetic target is `zeta_K(s(w))^2`.
- The finite relative Euler determinant is `Z_{K,2a}(s(w))^2`.
- If a resolvent-comparable operator pair exists, its relative trace can be encoded by a spectral shift function.

### Open

- Constructing the D12 full/archimedean finite operator pair rigorously from Suzuki's localized screw-form framework.
- Proving the corresponding resolvent difference is trace class (or finding the correct regularized class).
- Showing its relative trace equals the finite Euler cutoff plus an error tending to zero.
- Controlling the universal archimedean reference limit in the same normalization.
- Passing from these real-axis statements to the global characteristic-function limit required for the GRH conclusion.

No RH or GRH statement is proved here.

## 14. Strategic next step

The next high-value question is now much more concrete than an absolute trace formula:

\[
\boxed{
\text{Does subtracting the prime-free localized screw operator make the D12 perturbation trace class?}
}
\]

The prime contribution to the finite kernel contains only finitely many prime powers (`n<=e^{2a}`), so this should be tested directly at the localized kernel/form level.

If the full-minus-archimedean form difference is finite rank or trace class after the derivative sandwich, then the Birman–Krein relative determinant becomes rigorous immediately and the remaining arithmetic bridge reduces to evaluating its trace/determinant.

If it is not trace class, the next step is to determine its exact Schatten class and use the corresponding regularized determinant (`det_2`, etc.).

That is the next calculation to perform.
