# Cone Derivation Ledger v13.747 — Exact Sign of Suzuki Screw Positivity Versus Weil Form

**Date:** 2026-09-24
**Status:** exact sign fixed from Suzuki's stated kernel and Weil-form operator; no residual global sign
**Parents:** v13.744–746
**Synchronization:** live head before write was v13.746 (\`d2e3efd...\`). No newer Suzuki/audit commit was present.

## 1. Source sign to be fixed

Suzuki's screw kernel is
\[
G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0).
\]
For the Riemann-zeta screw function, \(g\) is real, even, and \(g(0)=0\), so
\[
G_g(t,u)=g(t-u)-g(t)-g(u).
\]
Suzuki's positivity convention is
\[
\sum_{i,j}G_g(t_i,t_j)\xi_i\overline{\xi_j}\ge0.
\]
Under RH his zero expansion is
\[
G_g(t,u)
=
\sum_\gamma
\frac{(e^{i\gamma t}-1)(e^{-i\gamma u}-1)}{\gamma^2},
\]
which confirms that the displayed \(G_g\), not \(-G_g\), is the positive kernel.

## 2. Continuous quadratic form and zero-mass reduction

For a test function \(f\) with
\[
\int_{\mathbb R}f(x)\,dx=0,
\]
define
\[
Q_{\rm Suz}[f]
=
\iint_{\mathbb R^2}
G_g(x,y)f(x)\overline{f(y)}\,dx\,dy.
\]
The one-variable subtraction terms vanish because \(f\) has zero mass. Therefore
\[
\boxed{
Q_{\rm Suz}[f]
=
\iint g(x-y)f(x)\overline{f(y)}\,dx\,dy.
}
\]

## 3. Put \(f=DF\)

Use the ordinary derivative \(D=d/dx\) for the sign calculation and let
\[
f=F'.
\]
For compactly supported/sufficiently decaying \(F\), \(\int f=0\).

Then
\[
Q_{\rm Suz}[F']
=
\iint g(x-y)F'(x)\overline{F'(y)}\,dx\,dy.
\]

Integrate first in \(x\):
\[
\int g(x-y)F'(x)\,dx
=
-\int g'(x-y)F(x)\,dx.
\]
Then integrate in \(y\):
\[
-\int g'(x-y)\overline{F'(y)}\,dy
=
-\int g''(x-y)\overline{F(y)}\,dy,
\]
because
\[
\partial_y g'(x-y)=-g''(x-y)
\]
and the integration-by-parts minus sign cancels that derivative sign inside the intermediate integral exactly as displayed.

Hence
\[
\boxed{
Q_{\rm Suz}[F']
=
\iint[-g''(x-y)]F(x)\overline{F(y)}\,dx\,dy.
}
\]

Since the common current established in v13.744–746 is
\[
\boxed{\mathscr W=-g'',}
\]
we obtain
\[
\boxed{
Q_{\rm Suz}[DF]
=
Q_{\rm Weil}[F]
}
\]
when \(D=d/dx\).

There is **no global minus sign**.

## 4. Independent Fourier sign check

With Suzuki's convention
\[
\widehat f(t)=\int e^{-itx}f(x)\,dx,
\]
\[
\widehat{F'}(t)=it\,\widehat F(t),
\]
and
\[
\widehat{\mathscr W}(t)
=
\widehat{-g''}(t)
=
t^2\widehat g(t).
\]
Therefore
\[
\widehat g(t)|\widehat{F'}(t)|^2
=
\widehat g(t)t^2|\widehat F(t)|^2
=
\widehat{\mathscr W}(t)|\widehat F(t)|^2.
\]
So Parseval gives the same positive sign:
\[
\boxed{
Q_{\rm Suz}[F']
=
\frac1{2\pi}\langle\widehat g,t^2|\widehat F|^2\rangle
=
\frac1{2\pi}\langle\widehat{\mathscr W},|\widehat F|^2\rangle
=
Q_{\rm Weil}[F].
}
\]

## 5. Match to Suzuki's operator convention \(D=i\,d/dx\)

Suzuki's finite-interval operator lane uses
\[
D_{\rm Suz}=i\frac d{dx}.
\]
For \(v\in H_0^1\),
\[
D_{\rm Suz}v=i v'.
\]
In the Hermitian form the phase cancels:
\[
(i v'(x))\,\overline{i v'(y)}
=
v'(x)\overline{v'(y)}.
\]
Thus
\[
\langle G D_{\rm Suz}v,D_{\rm Suz}v\rangle
=
\iint g(x-y)v'(x)\overline{v'(y)}\,dx\,dy.
\]
Suzuki identifies the Weil-form operator with the Friedrichs extension of
\[
B_a=D_{\rm Suz}G_aD_{\rm Suz}.
\]
Because \(D_{\rm Suz}=i\partial_x\) is symmetric under the Dirichlet convention, this operator statement has the same positive quadratic form. No hidden factor \(i^2=-1\) survives: one factor is conjugated in the Hermitian pairing.

Therefore the sign fixed above is also the sign in Suzuki's operator formulation.

## 6. Zero-side sanity check

Under RH Suzuki's kernel expansion yields
\[
Q_{\rm Suz}[F']
=
\sum_\gamma
\frac{|\widehat{F'}(\gamma)|^2}{\gamma^2}
\]
(up to the fixed Fourier evaluation sign, irrelevant after modulus squared). Since
\[
|\widehat{F'}(\gamma)|^2
=
\gamma^2|\widehat F(\gamma)|^2,
\]
\[
\boxed{
Q_{\rm Suz}[F']
=
\sum_\gamma|\widehat F(\gamma)|^2\ge0.
}
\]
This is the expected sign of Weil positivity. The negative alternative would give a nonpositive zero sum and contradict Suzuki's stated positive-definite screw kernel.

## 7. Exact conclusion

\[
\boxed{
\textbf{Suzuki's sign is positive:}\qquad
Q_{\rm Suz}[DF]=Q_{\rm Weil}[F].
}
\]

Not
\[
Q_{\rm Suz}[DF]=-Q_{\rm Weil}[F].
\]

After v13.746, there is no residual arithmetic normalization and now no residual global sign. The only transport data are:

1. primitive/derivative change of test variable;
2. zero-mass condition on the differentiated screw test function;
3. Fourier \(1/(2\pi)\) Parseval factor if the nonunitary Fourier convention is used.

The identity of forms is unconditional. Positivity on the full Weil test class remains the separate RH-equivalent assertion.

## 8. Next nonredundant gate

Freeze the exact common test-function domain and quotient by the affine gauge of \(g\), then formulate the unitary/isometric map between the completed screw-form space and the Weil-form space on finite intervals. This will distinguish what is an exact form equivalence from what requires positivity/completion.
