# Cone Derivation Ledger v13.199 — Exact Weighted Circle Measure

Status: **[D] exact derivation**

Date: 2026-09-03

## Goal

Close the area branch at a structurally useful point by replacing ad hoc global renormalizations with the exact region-dependent inverse weight induced by

\[
F(x,y)=\left(\frac{x-y}{2},\sqrt{xy}\right).
\]

From the area paper,

\[
J(x,y)=\left|\frac{\partial(X,Y)}{\partial(x,y)}\right|
=\frac{T}{2Y}.
\]

Therefore

\[
dX\,dY=\frac{T}{2Y}\,dx\,dy.
\]

## 1. [D] Exact inverse weight in circle coordinates

Since

\[
X=T\sin\theta,\qquad Y=T\cos\theta,
\]

with \(\theta\) measured from the positive \(Y\)-axis,

\[
\frac{Y}{T}=\cos\theta.
\]

Hence the inverse area transformation is

\[
\boxed{dx\,dy=2\cos\theta\,dX\,dY.}
\]

Equivalently, because the flat polar element is

\[
dX\,dY=T\,dT\,d\theta,
\]

we have

\[
\boxed{dx\,dy=2T\cos\theta\,dT\,d\theta.}
\]

Thus the factor-plane Lebesgue measure is carried to the circle view as a **weighted circular measure** with density

\[
\boxed{w(\theta)=2\cos\theta.}
\]

This is the exact region-dependent normalization sought after v13.198. No global constant such as \(4/\pi\) is needed.

## 2. [D] Rapidity form of the same weight

The logarithmic/circular dictionary from v13.196 is

\[
\cos\theta=\operatorname{sech}s,
\qquad
s=\frac12\log\frac{x}{y},
\qquad
d\theta=\operatorname{sech}s\,ds.
\]

Therefore

\[
\boxed{dx\,dy=2\operatorname{sech}s\,dX\,dY.}
\]

On the Euclidean cone surface, where

\[
dA_{\rm cone}=\sqrt2\,dX\,dY,
\]

this becomes

\[
\boxed{dx\,dy=\sqrt2\cos\theta\,dA_{\rm cone}
=\sqrt2\operatorname{sech}s\,dA_{\rm cone}.}
\]

So the same \(\operatorname{sech}\) factor has two exact roles:

1. it compresses rapidity into circle angle, \(d\theta=\operatorname{sech}s\,ds\);
2. it is the inverse flat-area distortion up to the factor 2.

This is a stronger and cleaner log/circle bridge than any constant shell normalization.

## 3. [D] Exact recovery of any factor-plane area

For every measurable factor-plane region \(E\) in the positive quadrant,

\[
\boxed{
\operatorname{Area}_{xy}(E)
=\iint_{F(E)}2\cos\theta\,dX\,dY.
}
\]

In polar circle coordinates,

\[
\boxed{
\operatorname{Area}_{xy}(E)
=\iint_{F(E)}2T\cos\theta\,dT\,d\theta.
}
\]

This means that \(n\log n\), \(nH_n\), \(D(n)\), \(A_n\), and \(T_n\) can all be represented exactly in the circle picture, provided one uses the transported weighted measure rather than raw Euclidean circle area.

For the literal continuous divisor region

\[
E_n=\{1\le x\le n,\ 0\le y\le n/x\},
\]

we therefore have the exact identity

\[
\boxed{
 n\log n
=\iint_{F(E_n)}2\cos\theta\,dX\,dY.
}
\]

The raw flat image area

\[
W_L(n)=\frac23(n-1)\sqrt n
\]

is a different measure of the same image region; it should not be rescaled by a shell-wide constant to recover \(n\log n\).

## 4. [D] Whole triangle as a check

Let \(\Delta_S\) be the factor triangle \(x+y\le S\), and let \(H_S\) be its half-disk image of radius \(R=S/2\).

The weighted circle measure gives

\[
\int_{-\pi/2}^{\pi/2}\int_0^R
2T\cos\theta\,dT\,d\theta
=R^2\int_{-\pi/2}^{\pi/2}\cos\theta\,d\theta
=2R^2
=\frac{S^2}{2},
\]

which is exactly the ordinary factor-plane triangle area.

By contrast, the unweighted Euclidean half-disk area is

\[
\frac{\pi R^2}{2}=\frac{\pi S^2}{8},
\]

so the previously observed global ratio \(\pi/4\) is simply the ratio of two different measures on the same transported region.

## 5. [D] Continuous hyperbola/secant partition

Inside the shell \(x+y\le n+1\), the boundary \(xy=n\) becomes the secant \(Y=\sqrt n\).

Let \(B_n\) be the factor region below the hyperbola and \(C_n\) its complement in the shell. Then

\[
\operatorname{Area}(B_n)=n\log n+n+1,
\]

\[
\operatorname{Area}(C_n)=\frac{n^2-1}{2}-n\log n.
\]

Their exact circle representations are now

\[
\boxed{
 n\log n+n+1
=\iint_{F(B_n)}2\cos\theta\,dX\,dY,
}
\]

and

\[
\boxed{
 \frac{n^2-1}{2}-n\log n
=\iint_{F(C_n)}2\cos\theta\,dX\,dY.
}
\]

The raw Euclidean areas \(A_{\rm below}^{\circ}(n)\) and \(A_{\rm cap}^{\circ}(n)\) are therefore complementary geometric observables, not replacements for these factor-plane quantities.

## 6. [D] Discrete staircases require no new normalization principle

The exact staircase push-forwards of v13.197 used the raw flat Jacobian and produced \(\mathcal W_T,\mathcal W_H,\mathcal W_D,\mathcal W_A\), all on the \(n^{3/2}\) circle-area scale.

The present result explains how to recover the original staircase areas from their image regions exactly:

\[
\boxed{
T_n=\iint_{F(\mathcal T_n)}2\cos\theta\,dX\,dY,
}
\]

\[
\boxed{
D(n)=\iint_{F(\mathcal D_n)}2\cos\theta\,dX\,dY,
}
\]

and similarly for \(nH_n\) and \(A_n\).

Thus there is no need to invent a special constant renormalization for the divisor staircase. The exact normalization is pointwise and angular.

## 7. [Audit] What survives from the exploratory n=11 observation

At \(n=11\), the globally normalized quantity

\[
\widetilde W_L(11)=\frac4\pi W_L(11)
\]

happened to lie close to \(D(11)\), but v13.198 showed that this fails asymptotically.

The exact statement replacing it is:

> The circle image of the divisor region carries a canonical angular weight \(2\cos\theta=2\operatorname{sech}s\). Integrating with this weight recovers the original factor-plane area exactly for every region and every scale.

This is publication-safe and structurally connected to the existing rapidity/circle relation.

## 8. [I] Relation to the broader Cone framework

This weighted-measure result is directly compatible with the Lorentz/rapidity framework already used in the discriminant-12 return paper:

\[
s=\frac12\log(x/y)
\]

is the real boost coordinate, while

\[
\theta=\int_0^s\operatorname{sech}t\,dt
\]

is its circular compactification. The measure density \(\operatorname{sech}s\) is therefore not an added fitting function; it is forced by the same coordinate transformation.

Guardrail: this does **not** imply any new zeta-zero, RH, or spectral statement. It is an exact area/coordinate identity.

## 9. Area-branch stopping point

This is a natural stopping point for the exploratory area branch before returning to the main publication sequence.

Publication-ready core:

\[
\boxed{dX\,dY=\frac{1}{2\cos\theta}\,dx\,dy}
\]

and therefore

\[
\boxed{dx\,dy=2\cos\theta\,dX\,dY.}
\]

Together with

\[
\boxed{d\theta=\operatorname{sech}s\,ds,\qquad \cos\theta=\operatorname{sech}s,}
\]

this gives the exact triangle/logarithmic-to-circle measure correspondence we were looking for.

Next project action: fold this proposition into the geometry-only area paper, add one restrained n=11 comparison figure/table, then return to Paper A cleanup and Paper B audit.
