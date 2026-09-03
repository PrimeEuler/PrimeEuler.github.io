# Cone Derivation Ledger v13.200 — Area Branch Publication Checkpoint

Status: **[Audit] supporting branch frozen at a publication-useful checkpoint**

Date: 2026-09-03

## 1. Purpose

The area investigation was opened because Paper A correctly warns that

\[
(x,y)\mapsto\left(X,Y,T\right)
=\left(\frac{x-y}{2},\sqrt{xy},\frac{x+y}{2}\right)
\]

is not area-preserving.  The purpose of the branch was to replace that warning by an exact companion theory, not to turn area numerology into the main Cone project.

The branch has now reached a natural stopping point.

## 2. [D] Exact local area transport

The flat Jacobian is

\[
\boxed{
 dX\,dY
 =\frac{x+y}{4\sqrt{xy}}\,dx\,dy
 =\frac{T}{2Y}\,dx\,dy.
}
\]

The induced Euclidean cone area is

\[
\boxed{dA_{\rm cone}=\sqrt2\,dX\,dY.}
\]

Hence

\[
\boxed{
 dA_{\rm cone}
 =\frac{T}{\sqrt2Y}\,dx\,dy.
}
\]

These are exact differential-geometric identities.

## 3. [D] Exact inverse measure in the circle view

Writing

\[
X=T\sin\theta,\qquad Y=T\cos\theta,
\]

the inverse Jacobian is

\[
\boxed{dx\,dy=2\cos\theta\,dX\,dY.}
\]

Equivalently, in rapidity

\[
s=\frac12\log\frac{x}{y},
\qquad
\cos\theta=\operatorname{sech}s,
\]

so

\[
\boxed{dx\,dy=2\operatorname{sech}s\,dX\,dY.}
\]

For every measurable factor-plane region \(E\),

\[
\boxed{
\operatorname{Area}_{xy}(E)
=\iint_{F(E)}2\cos\theta\,dX\,dY.
}
\]

This pointwise angular weight, not a shell-wide constant, is the exact normalization between factor-plane area and circle-view area.

## 4. [D] Logarithmic-to-circular compactification

With

\[
\rho=\sqrt{xy},\qquad
s=\frac12\log(x/y),
\]

we have

\[
X=\rho\sinh s,\qquad
Y=\rho,\qquad
T=\rho\cosh s.
\]

The corresponding circle angle satisfies

\[
\boxed{
\sin\theta=\tanh s,
\qquad
\cos\theta=\operatorname{sech}s,
\qquad
\tan\theta=\sinh s.
}
\]

Therefore

\[
\boxed{d\theta=\operatorname{sech}s\,ds}
\]

and

\[
\boxed{
\int_0^\infty\operatorname{sech}s\,ds=\frac\pi2.
}
\]

This is the publication-safe content behind the observed logarithmic/exponential versus circular-\(\pi\) relation.  It is an exact coordinate identity, not a claim of a new identity between \(e\) and \(\pi\).

## 5. [D] Hyperbola/secant partition

For the smallest continuous shell containing \((1,n)\) and \((n,1)\),

\[
x+y=n+1,
\]

the constant-product curve

\[
xy=n
\]

maps exactly to the horizontal secant

\[
Y=\sqrt n
\]

of the radius

\[
R=\frac{n+1}{2}
\]

half-disk.

The shell geometry obeys

\[
\left(\frac{n-1}{2}\right)^2+n
=\left(\frac{n+1}{2}\right)^2.
\]

The factor-plane areas are

\[
A(B_n)=n\log n+n+1,
\]

\[
A(C_n)=\frac{n^2-1}{2}-n\log n.
\]

The corresponding raw Euclidean circle areas are the below-secant region and circular cap.  They are images of the same sets under a non-area-preserving map and are not numerically identified with the factor-plane areas.

## 6. [D] Literal \(n\log n\) region

For

\[
E_n=\{1\le x\le n,\ 0\le y\le n/x\},
\]

\[
\operatorname{Area}_{xy}(E_n)=n\log n.
\]

Its raw flat image area is

\[
\boxed{
W_L(n)=\frac23(n-1)\sqrt n.
}
\]

But its exact transported factor-area measure in the circle view is

\[
\boxed{
 n\log n
 =\iint_{F(E_n)}2\cos\theta\,dX\,dY.
}
\]

## 7. [Audit] Rejected constant normalization

The exploratory quantity

\[
\widetilde W_L(n)=\frac4\pi W_L(n)
\]

happens to approximate \(D(11)\) better than \(11\log11\), but it scales as \(n^{3/2}\) rather than \(n\log n\).  It therefore fails as a global divisor approximation.

The exact replacement is the pointwise weight \(2\cos\theta\).

## 8. [D] Discrete staircases

The discrete quantities \(T_n\), \(nH_n\), \(D(n)\), and \(A_n\) admit exact raw-flat push-forwards by summing the column image formula

\[
W_k(h)
=\frac13\left[
\sqrt h\bigl(k^{3/2}-(k-1)^{3/2}\bigr)
+h^{3/2}\bigl(\sqrt k-\sqrt{k-1}\bigr)
\right].
\]

Those raw image areas naturally lie on an \(n^{3/2}\)-type scale.  Their original staircase areas are recovered exactly by integrating the transported weight \(2\cos\theta\) over their image regions.  No additional normalization principle is required.

## 9. [Audit] n=11 example

For \(n=11\):

\[
T_{11}=66,\qquad D(11)=29,\qquad A_{11}=37,
\]

\[
11\log11\approx26.376848,
\qquad
11H_{11}\approx33.218651.
\]

The radius-6 half-disk has raw area

\[
18\pi\approx56.548668.
\]

The raw cap and below-secant areas are approximately

\[
A_{\rm cap}^{\circ}(11)\approx18.880864,
\]

\[
A_{\rm below}^{\circ}(11)\approx37.667804.
\]

The closeness of \(37.667804\) to the discrete complement \(A_{11}=37\) is retained only as an observation.  No structural equality is claimed.

## 10. Publication artifacts

Geometry-only source:

`foundations/Note_AreaDistortion_AMGM_Cone_v1.1.tex`

The older LQG comparison remains separate in:

`foundations/Note_SemiclassicalArea.tex`

and should be treated as a research note, not as the foundation cited by Paper A.

The restrained n=11 area-measure figure source is:

`figures/fig_area_measure_11_2panel.py`

Paper A has been advanced to:

`foundations/PaperA_ConicTheorem_v2.3.tex`

with the hyperbola degeneracy and n=11 triangle wording corrected and the area citation pointed to the geometry-only companion.

## 11. [Audit] Build status at this checkpoint

Paper A v2.3 has been shown by GitHub Actions to compile successfully to a six-page PDF.  The first output push failed only because another repository commit landed during the build, causing a non-fast-forward push rejection.  The workflow has now been changed to rebase before pushing generated output.

The area-paper workflow has likewise been made robust against the same race.

A build is not considered stored/certified on `master` until the generated PDF is confirmed present there.

## 12. Branch freeze

The area branch is now frozen unless one of the following occurs:

1. a mathematical error is discovered in the exact transport formulas;
2. Paper A requires a specific clarification from the companion;
3. the weighted measure produces a theorem directly needed by the main discriminant-12/Lorentz architecture.

Otherwise the main project resumes with Paper B.
