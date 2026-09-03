# Cone Derivation Ledger v13.199 — Exact Angular Inverse Measure

Status: **[D] exact derivation; area branch stopping result**

## Purpose

Close the current area-distortion branch with one structural result rather than another fitted approximation.  The flat circle map is

\[
F(x,y)=\left(X,Y\right)=\left(\frac{x-y}{2},\sqrt{xy}\right),
\qquad
T=\frac{x+y}{2}=\sqrt{X^2+Y^2}.
\]

Earlier ledgers established the flat Jacobian

\[
J(x,y)=\left|\frac{\partial(X,Y)}{\partial(x,y)}\right|
=\frac{T}{2Y}.
\]

The question is whether the nonuniform distortion has a natural region-dependent inverse in circle coordinates.

## 1. [D] Exact inverse weight in circle angle

Let \(\theta\in(-\pi/2,\pi/2)\) be measured from the positive \(Y\)-axis:

\[
X=T\sin\theta,\qquad Y=T\cos\theta.
\]

Then

\[
J=\frac{T}{2Y}=\frac{1}{2\cos\theta}.
\]

Therefore

\[
\boxed{dx\,dy=2\cos\theta\,dX\,dY.}
\]

Equivalently, because \(dX\,dY=T\,dT\,d\theta\),

\[
\boxed{dx\,dy=2T\cos\theta\,dT\,d\theta.}
\]

This is the exact region-dependent inverse measure that the constant \(4/\pi\) exploratory normalization of v13.198 was trying to approximate.

For any measurable factor-plane region \(E\) on which the map is one-to-one,

\[
\boxed{
\operatorname{Area}_{xy}(E)
=\iint_{F(E)}2\cos\theta\,dA_{XY}.
}
\]

Thus the correct inverse normalization is local, not a shell-wide constant.

## 2. [D] Rapidity form

With product-ratio coordinates

\[
\rho=\sqrt{xy},\qquad s=\frac12\log\frac{x}{y},
\]

we have

\[
X=\rho\sinh s,\qquad Y=\rho,\qquad T=\rho\cosh s,
\]

and

\[
\cos\theta=\operatorname{sech}s,
\qquad d\theta=\operatorname{sech}s\,ds.
\]

Hence the inverse flat-area weight is also

\[
\boxed{2\cos\theta=2\operatorname{sech}s.}
\]

This gives the exact Lorentz/rapidity interpretation of the area correction: large factor imbalance corresponds to large \(|s|\), and the inverse weight suppresses those highly distorted near-axis regions by \(\operatorname{sech}s\).

## 3. [D] Cone-surface version

Since the Euclidean cone surface element is

\[
dA_{\rm cone}=\sqrt2\,dA_{XY},
\]

we also have

\[
\boxed{dx\,dy=\sqrt2\cos\theta\,dA_{\rm cone}.}
\]

So the factor-plane measure can be recovered exactly from either the flat circle view or the cone surface.

## 4. [D] Whole-shell consistency

For the half-disk of radius \(R=S/2\),

\[
\int_{-\pi/2}^{\pi/2}\int_0^R 2\cos\theta\,T\,dT\,d\theta
=\frac{S^2}{2},
\]

which is exactly the area of the factor-plane triangle

\[
\{x\ge0,\ y\ge0,\ x+y\le S\}.
\]

The unweighted half-disk area is \(\pi S^2/8\), explaining why the whole-shell mean contraction happens to be \(\pi/4\).  The constant \(\pi/4\) is therefore a global average of the local weight, not an inverse Jacobian for arbitrary subregions.

## 5. [D] Exact recovery of the classical and discrete quantities

Let \(E_n\) be the literal continuous under-hyperbola region

\[
E_n=\{(x,y):1\le x\le n,\ 0\le y\le n/x\}.
\]

Its ordinary area is \(n\log n\).  Although its unweighted circle image has area

\[
W_L(n)=\frac23(n-1)\sqrt n,
\]

the angularly weighted image satisfies exactly

\[
\boxed{
\iint_{F(E_n)}2\cos\theta\,dA_{XY}=n\log n.
}
\]

Likewise, for the staircase regions of v13.197 whose ordinary areas are

\[
T_n,\qquad nH_n,\qquad D(n),\qquad A_n=T_n-D(n),
\]

the same weighted circle measure recovers those quantities exactly.  No new estimator is being introduced; this is simply the change-of-variables theorem expressed in the natural circular coordinate.

## 6. [N-cert] n=11 comparison table

For the illustrative shell \(n=11\):

| quantity | factor-plane area/count | unweighted flat-circle image | angularly weighted recovery |
|---|---:|---:|---:|
| \(T_{11}\) | 66 | 51.26352005 | 66 |
| \(11H_{11}\) | 33.21865079 | 32.75071523 | 33.21865079 |
| \(D(11)\) | 29 | 30.18105635 | 29 |
| \(A_{11}\) | 37 | 21.08246370 | 37 |
| \(11\log 11\) | 26.37684800 | 22.11083194 | 26.37684800 |

The unweighted image numbers live on the circle-area scale and need not be close to the original quantities.  The weighted column recovers the original measure exactly because it uses the inverse Jacobian.

## 7. [Audit] What is genuinely structural

The structural result is not that a circle-area formula improves the Dirichlet divisor estimate.  The structural result is

\[
\boxed{
\text{factor-plane area}
\longleftrightarrow
\text{circle area weighted by }2\cos\theta
=2\operatorname{sech}s.
}
\]

This directly joins the area-distortion calculation to the Lorentz rapidity variable already used elsewhere in the Cone framework.

Do **not** claim that \(4/\pi\), \(W_L\), or any fixed rescaling of raw circle area is an improved asymptotic approximation to \(D(n)\).

## 8. Area-branch stopping rule

The area branch has now produced the three planned deliverables:

1. exact continuous and discrete push-forward formulas;
2. an \(n=11\) comparison table on both measures;
3. an exact rapidity-angle inverse normalization.

Unless a new theorem materially affects Paper A, Paper B/C, or the discriminant-12 principal chain, this branch should now be treated as frozen supporting geometry rather than an open approximation search.
